from django.urls import path
from django.urls import path, include
from .views import *

urlpatterns = [
path('', index, name='home'),
path('about/', about, name='about'),
path('addpage/', addpage, name='addpage'),
path('contact/', contact, name='contact'),
path('login/', login, name='login'),
path('category/<int:cat_id>/', show_category, name='category'),

# path('cat/<slug:catid>/', categories),
]