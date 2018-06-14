from Detail import views
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile', views.ProfileViewSet)
router.register(r'detail', views.DetailsViewSet)
router.register(r'login', views.LoginViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^this/', views.my ,name='my'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]