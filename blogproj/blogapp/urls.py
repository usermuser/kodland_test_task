from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.PostsView.as_view(), name='posts'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
