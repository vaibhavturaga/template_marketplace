from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_form_upload, name='home'),
    path('download/<int:doc_id>/', views.download_document, name='download'),
    path('serve/<int:doc_id>/', views.serve_html_file, name='serve_html'),
]