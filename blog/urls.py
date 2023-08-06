from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='blog-index'),
    path('detail/<int:pk>',views.postDetail,name='post-detail'),
    path('edit/<int:pk>',views.postEdit,name='post-edit'),
    path('delete/<int:pk>',views.postDelete,name='post-delete')
] 
