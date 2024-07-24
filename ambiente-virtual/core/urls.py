

from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include # adicionar include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', include('accounts.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('myapp.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto