from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('post/<slug:slug>/edit', views.post_edit.as_view(), name='post_edit'),
    path('new/', views.post_create.as_view(), name='post_new'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)