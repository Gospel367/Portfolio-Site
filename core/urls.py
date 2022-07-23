from django.urls import path
from . import views


urlpatterns = [
    path('author', views.myprojects, name='author'),
    #path('countryposts', views.country, name='countryposts'),
    path('/<slug:author>', views.authorposts, name='allposts'),
    path('register/', views.Register.as_view(), name='register'),           
    path('login/', views.CustomLoginView.as_view(next_page='home'), name='login'),
    path('logout/', views.CustomLogout.as_view(next_page ='index'), name='logout'),
    path('create-project/', views.Createproj.as_view(), name ='create'),
    path('myprofile/', views.Myprofile.as_view(), name='myprofile'),
    path('create-profile/', views.Createprofile.as_view(), name ='createprofile'),
    path('update-profile/<int:pk>', views.Updateprofile.as_view(), name ='updateprofile'),
    path('create-category/', views.Createcate.as_view(), name ='createcate'),
    #path('delete-project/<int:slun>', views.Deleteproj.as_view(), name ='delete'),
    path('update-project/<int:pk>', views.Updateproj.as_view(), name ='update'),
    path('index', views.Index.as_view(), name='index'),
    path('', views.Projhome.as_view(), name ='home' ),
    path('<slug:slug>', views.Projdetail.as_view(), name='projdetail'),
    path('category/<slug:pk>', views.categorypage, name='category'),
    path('delete/<int:proj_id>', views.delete_post, name='deleter'),
    path('allprofile/', views.Allprofiles.as_view(), name='allprofiles'),

   ]
