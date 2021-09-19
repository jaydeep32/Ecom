from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Swagger Api',
        default_version='v1'
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/', schema_view.with_ui()),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('', include('product.urls')),
    path('payment/', include('payments.urls')),
    path('gettoken/', TokenObtainPairView.as_view(), name='gettoken'),
    # path('refreshtoken/', TokenRefreshView.as_view(), name='refreshtoken'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
