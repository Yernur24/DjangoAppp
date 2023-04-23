from django.urls import path
from django.urls import path, include
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
path('',cache_page(60)( ProductHome.as_view()), name='home'),
path('about/', about, name='about'),
path('addpage/', AddPage.as_view(), name='addpage'),
path('login/', LoginUser.as_view(), name='login'),
path('logout/', logout_user, name='logout'),
path('register/', RegisterUser.as_view(), name='register'),
path('category/<int:cat_id>/', show_category, name='category'),
path('contact/', ContactFormView.as_view(), name='contact'),
path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
]