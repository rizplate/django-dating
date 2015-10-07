from django.conf.urls import include, url

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from dating_project.users.api import viewsets as user_api_views
from dating_project.board import views as board_api_views

router = DefaultRouter()
router.register(r'users', user_api_views.UserViewSet)

urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
]