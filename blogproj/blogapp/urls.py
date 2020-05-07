from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.redirect_to_posts, name='redirect_to_posts'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('posts/create/', views.PostCreate.as_view(), name='create_post'),
    path('posts/update/<int:pk>/', views.PostUpdate.as_view(), name='update_post'),
    path('posts/delete/<int:pk>/', views.PostDelete.as_view(), name='delete_post'),

]
