from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ecommerce.drf import views

router = routers.DefaultRouter()
router.register(
    r'api', views.AllProductsViewSet, basename="allproducts"
)
router.register(
    r'product', views.ProductInventoryViewSet, basename="products"
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include("ecommerce.demo.urls", namespace="demo")),
    path('', include(router.urls)),
]
