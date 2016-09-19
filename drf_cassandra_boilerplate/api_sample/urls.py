from django.conf.urls import url, include

from rest_framework import routers

from .views import CassandraAdventuresViewSet


router = routers.DefaultRouter()
router.register('cassandra-adventures', CassandraAdventuresViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]