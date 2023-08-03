from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.process_data, name='process_data'),
    path('download-output-csv/', views.download_output_csv, name='download_output_csv'),
]
