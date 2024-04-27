from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import DocumentForm
from .models import Document

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()

    # Handle search query
    search_query = request.GET.get('search', '')
    if search_query:
        documents = Document.objects.filter(name__icontains=search_query)
    else:
        documents = Document.objects.all()

    return render(request, 'template_marketplace/model_form_upload.html', {
        'form': form,
        'documents': documents,
        'request': request
    })
def download_file(request, pk):
    document = Document.objects.get(pk=pk)
    response = FileResponse(document.file.open(), as_attachment=True)
    return response