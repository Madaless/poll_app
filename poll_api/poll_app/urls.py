# poll_app/urls.py
from rest_framework.routers import DefaultRouter
from .views import PollViewSet

router = DefaultRouter()
router.register(r'polls', PollViewSet, basename='poll')
urlpatterns = router.urls