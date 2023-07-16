from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Other URL patterns...
    path('', views.my_view, name='my-form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
