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


class CassandraAdventuresModel_M(DjangoCassandraModel):
    __keyspace__ = 'db'
    adventure_id = cassandra_columns.UUID(primary_key=True, default=uuid.uuid4)
    adventure_season_id = cassandra_columns.UUID(primary_key=True, default=uuid.uuid4)
    adventure_group_id = cassandra_columns.Integer(primary_key=True)
    adventure_type = cassandra_columns.Text()
    adventure_desc = cassandra_columns.Text()
    last_modified = cassandra_columns.DateTime()

    class Meta:
        get_pk_field = 'adventure_id'


class CassandraFamilyMember(DjangoCassandraModel):
    __keyspace__ = 'db'
    id = cassandra_columns.UUID(primary_key=True, default=uuid.uuid4)
    first_name = cassandra_columns.Text(primary_key=True)
    last_name = cassandra_columns.Text(primary_key=True)
    favourite_number = cassandra_columns.Integer(required=False)
    favourite_float_number = cassandra_columns.Float(partition_key=True)
    created_on = cassandra_columns.DateTime()

    class Meta:
        get_pk_field = 'id'
