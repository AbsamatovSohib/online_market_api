"""
URL configuration for market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include



from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from selling.views import *
from rest_framework import permissions
from django.urls import path


schema_view = get_schema_view(
    openapi.Info(
        title="Online Market CRUD API",
        default_version="v1",
        description="Online market API documentation",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'customer', CustomerModelViewSet)
router.register(r'product', ProductModelViewSet)
router.register(r'item', ItemModelViewSet)
router.register(r'category', CategoryModelViewSet)
router.register(r'shop_card', ShopcardModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/shopcard/<str:pk>',customer_purchase_history),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('create/', views.add_items, name='add-items'),
]