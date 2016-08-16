# drf-cassandra-boilerplate
Boilerplate code do deliver working example of REST API on Django &amp; DRF for Cassandra with Docker containers.

To build: docker-compose build web // please note that it is taking a while to install cassandra-driver so be patient.

To sync primary relational database backend: docker-compose run web python manage.py migrate

To sync cassandra database backend: docker-compose run web python manage.py sync_cassandra --database cassandra

Access to CQL on Docker Cassandra container: docker exec -it drfcassandraboilerplate_cassandra_1 cqlsh