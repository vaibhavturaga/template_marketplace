import os
import zipfile
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Document
from .forms import DocumentForm
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import get_object_or_404

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = form.save(commit=False)
            newdoc.save()  # Save the model which includes the file and image
            handle_uploaded_file(newdoc.file.path, newdoc.id)
            return redirect('home')
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    return render(request, 'template_marketplace/model_form_upload.html', {
        'form': form,
        'documents': documents
    })

def handle_uploaded_file(file_path, doc_id):
    if file_path.endswith('.zip'):
        extraction_path = os.path.join(settings.MEDIA_ROOT, f'extracted/{doc_id}')
        os.makedirs(extraction_path, exist_ok=True)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)


def download_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    file_path = document.file.path
    try:
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=document.file.name)
    except FileNotFoundError:
        raise Http404('File does not exist')

def serve_html_file(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    html_file_path = document.file_url()

    if html_file_path:
        with open(html_file_path, 'r') as f:
            html_content = f.read()
        return HttpResponse(html_content)
    else:
        return HttpResponse('HTML file not found')