from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='my_home'),
    path('about/', views.about,name='my_about'),
    path('blog/', views.blog,name='my_blog'),
    path('blog-details/', views.blog_details,name='my_blog_deatils'),
    path('contact/', views.contact,name='my_contact'),
    path('projects/', views.projects,name='my_projects'),
    path('project-details',views.project_details,name='my_project_details'),
    path('services/', views.services,name='my_services'),
    path('service-details', views.service_details,name='my_service_details'),
    path('starter-page', views.starter_page,name='my_starter-page'),
    path('master', views.master,name='my_master'),
    
]