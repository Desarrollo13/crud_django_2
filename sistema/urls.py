from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path("libros", views.libros,name='libros'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('crear',views.crear,name='crear'),
    path('editar',views.crear,name='editar'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# 50:16
