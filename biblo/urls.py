from django.urls import path
from django.urls import path, include
from .views import *

urlpatterns = [
path('', ProductHome.as_view(), name='home'),
# path('', index, name='home'),
path('about/', about, name='about'),
# path('addpage/', addpage, name='addpage'),
path('addpage/', AddPage.as_view(), name='addpage'),
path('contact/', contact, name='contact'),
path('login/', LoginUser.as_view(), name='login'),
path('logout/', logout_user, name='logout'),
path('register/', RegisterUser.as_view(), name='register'),
path('category/<int:cat_id>/', show_category, name='category'),
# path('category/<slug:cat_slug>/', ProductCategory.as_view(), name='category'),
path('post/<slug:post_slug>/', show_post, name='post'),

# path('cat/<slug:catid>/', categories),
]