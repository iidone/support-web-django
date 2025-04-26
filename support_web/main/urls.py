from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path("login", views.login, name = 'login'),
    path("", views.index, name='index'),
    path("control", views.control, name='control'),
    path("moder", views.moders, name = 'moders'),
    path("moder_home", views.moder_home, name = 'moder_home'),
    path("login2", views.loginToControl, name = 'loginToControl')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
