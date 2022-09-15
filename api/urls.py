from django.urls import path, include
from . import views

pathname = "api/"
urlpatterns = [
    path('messages/', views.MessagesListView.as_view()),
    path('projects/', views.ProjectsListView.as_view()),
    path('createProjects/', views.CreateProject.as_view()),
]
