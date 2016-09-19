from django.conf.urls import url, include

from rest_framework import routers

from .views import CassandraAdventuresViewSet\
    , CassandraAdventuresViewSet_M, CassandraFamilyMemberViewSet

router = routers.DefaultRouter()
router.register('cassandra-adventures', CassandraAdventuresViewSet)
router.register('cassandra-adventures-m', CassandraAdventuresViewSet_M)
router.register('cassandra-adventures-f', CassandraFamilyMemberViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]