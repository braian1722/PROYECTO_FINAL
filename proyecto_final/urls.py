from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

## braian 1234


urlpatterns = [
    path('admin/', admin.site.urls),
    path('local_de_ropa/', include("local_de_ropa.urls")),
]


urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 