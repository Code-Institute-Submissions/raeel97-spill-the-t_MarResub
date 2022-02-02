from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('create-post/', views.PostCreate.as_view(), name='create_post'),
    path('future-feature/', views.future_feature, name='future_feature'),
    path('postview/', views.PostList.as_view(), name='post_view'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]