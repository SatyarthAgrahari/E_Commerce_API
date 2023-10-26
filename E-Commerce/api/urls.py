from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewset,ProductViewset,CartItemViewset,OrderItemViewset


router=DefaultRouter()
router.register('categories',CategoryViewset)
router.register('product',ProductViewset)
router.register('cartitem',CartItemViewset)
router.register('orderitem',OrderItemViewset)


urlpatterns = [
    path('',include(router.urls)),

]