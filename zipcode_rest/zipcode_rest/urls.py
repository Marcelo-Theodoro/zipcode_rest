from rest_framework.routers import DefaultRouter
from zipcode import views

router = DefaultRouter()
router.register(r'zipcode', views.Zipcode, 'zipcode')
urlpatterns = router.urls
