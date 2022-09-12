from django.urls import path, include
from . import views

pathname = "api/"
urlpatterns = [
    path('', views.ExampleView.as_view()),  
    path('messages/', views.MessagesListView.as_view()),
    path('projects/', views.ProjectListCreateView.as_view()),
    path('createProjects/', views.CreateProject.as_view()),
    path('testS3/', views.TestingUploadView.as_view())
]
