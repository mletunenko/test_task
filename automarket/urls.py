from .views import ManufacturerViewSet, DealerViewSet, ModelViewSet, CarViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register(r'manufacturer', ManufacturerViewSet, basename='manufacturer')
router.register(r'dealer', DealerViewSet, basename='dealer')
router.register(r'model', ModelViewSet, basename='model')
router.register(r'car', CarViewSet, basename='car')

urlpatterns = router.urls
