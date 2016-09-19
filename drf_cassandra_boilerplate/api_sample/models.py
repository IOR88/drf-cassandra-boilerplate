import uuid

from cassandra.cqlengine import columns as cassandra_columns
from django_cassandra_engine.models import DjangoCassandraModel


class CassandraAdventuresModel(DjangoCassandraModel):
    __keyspace__ = 'db'
    adventure_id = cassandra_columns.UUID(primary_key=True, default=uuid.uuid4)
    adventure_desc = cassandra_columns.Text()
    last_modified = cassandra_columns.DateTime()

    class Meta:
        get_pk_field = 'adventure_id'


class CassandraAdventuresModel_1(DjangoCassandraModel):
    __keyspace__ = 'db'
    id = cassandra_columns.UUID(primary_key=True, default=uuid.uuid4)
    adventure_desc = cassandra_columns.Text()
    last_modified = cassandra_columns.DateTime()

    class Meta:
        get_pk_field = 'id'




# class CassandraAdventuresModel(DjangoCassandraModel):
#     __keyspace__ = 'db'
#     adventure_id = cassandra_columns.UUID(primary_key=True, default=uuid.uuid4)
#     adventure_desc = cassandra_columns.Text()
#     last_modified = cassandra_columns.DateTime()
#
#     class Meta:
#         get_pk_field = 'adventure_id'
