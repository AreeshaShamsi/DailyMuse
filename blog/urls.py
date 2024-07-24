from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views

import app1

urlpatterns = [
        path('',include('app1.urls')),
        path('admin/', admin.site.urls),
        path('accounts/', include('django.contrib.auth.urls')),


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
