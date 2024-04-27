from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_form_upload, name='home'),
    path('download/<int:pk>/', views.download_file, name='download'),
]

