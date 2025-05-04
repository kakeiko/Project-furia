from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fanprofile.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'project_furia.views.error_404'
handler500 = 'project_furia.views.error_500'
handler429 = 'project_furia.views.error_429'