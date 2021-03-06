from django.urls import path

from . import views

app_name = 'cms'
#これはurlを定義するためのやつ
urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.UserCreate.as_view(), name='signup'),
    path('post/', views.Post.as_view(), name='post'),
    #path('user/<int:pk>/post/', views.UserPost.as_view(), name='user_post'),
    path('user/<int:pk>/post/', views.UserPostView.as_view(), name='user_post'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user/', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
]