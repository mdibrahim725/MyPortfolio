from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('project/', views.project, name='project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]
