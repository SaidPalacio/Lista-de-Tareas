from rest_framework.routers import DefaultRouter
from .api import TaskViewSet

router = DefaultRouter()
router.register('api/tasks', TaskViewSet)

urlpatterns = router.urls
