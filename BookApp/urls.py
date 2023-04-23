from datetime import timedelta

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from BookApp.settings import SECRET_KEY
from biblo.views import *
from rest_framework import routers

from BookApp import settings
# router = routers.SimpleRouter()
# router.register(r'product', bibloViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/product/', bibloAPIList.as_view()),
    path('api/v1/product/<int:pk>/', bibloAPIList.as_view()),
    path('api/v1/productdelete/<int:pk>/', bibloAPIList.as_view()),
    path('captcha/', include('captcha.urls')),
    path('', include('biblo.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'biblo.views.handler400'
handler403 = 'biblo.views.handler403'
handler404 = 'biblo.views.handler404'
handler500 = 'biblo.views.handler500'
