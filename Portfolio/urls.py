from django.contrib import admin
from django.urls import path
from my_portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('contact-messages/', views.contact_messages, name='contact_messages'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('message_success/', views.message_success, name='message_success'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)