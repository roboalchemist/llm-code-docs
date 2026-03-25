# Source: https://ebean.io/docs/testing

Title: Testing | Ebean

URL Source: https://ebean.io/docs/testing

Markdown Content:
Third age of testing
--------------------

Rob Opinion: I believe with respect to testing and persistence we are now in the "3rd age" of testing.

### (I) First age - all persistence mocked/stubbed

In the first age testing against real databases was generally too slow, expensive and difficult. Tests mocked/stubbed out all persistence (often via Repository API's). Tests only ran against real databases on an "integration server".

### (II) Second age - in memory DB's

In the second age of testing in memory databases like H2 became available. This allowed developers to use these in memory databases rather than mocking out all persistence API's.

This resulted in far less mocking/stubbing used in tests.

The limitations of testing using in memory DB's like H2 for testing is around the functional difference compared to the "real" target database like Postgres or Oracle etc. Differences in types (e.g. UUID, Array, Json, Hstore, Range types) and features (sql functions, advanced locking, table partitioning etc).

### (III) Third age - testing using docker DB's

The limitations with testing against H2 can now be addressed in this "third age" of persistence testing. Docker has made it easier to automate the install/setup of databases on developer machines. Developer machines are powerful enough to run tests fast enough against the "real" target database (where docker versions of databases are functionally the same as the real thing).

*   Tests can cover database specific functionality and types (no excuses on test coverage)
*   The ease of using docker test containers needs to match the ease of using H2
*   We want tests to run against new/clean ephemeral databases
*   We need tests to run fast - match in memory database experience
*   build/tests run on the CI server match build/tests run on the developer machine

`ebean-test` is provided to make testing against docker test containers as simple and good as using H2. Developers new to a project can just `git clone` and `mvn clean test` and it "just works" without any setup steps.

For Postgres, MySql, SQL Server we can very successfully use docker test containers today. For the relatively heavier databases like Oracle, SAP Hana and DB2 we can be successful but there can be some argument for staying with H2 for testing depending on the situation.

Personally I have had great results using ebean-test / docker test containers over the last few years (largely Postgres). I highly recommend people look at this approach aiming for great test coverage, simpler test code and reduced variation between developer, CI and Production.

ebean-test also supports using [ElasticSearch](https://ebean.io/docs/testing#elasticsearch) and [Redis](https://ebean.io/docs/testing#redis) containers.

ebean-test dependency
---------------------

### 1. Add ebean-test as a test dependency

<dependency>
  <groupId>io.ebean</groupId>
  <artifactId>ebean-test</artifactId>
  <version>17.2.0</version>
  <scope>test</scope>
</dependency>

### 2. Add application-test.yaml

Add into `src/test/resources` a `application-test.yaml` configuration file that we use for testing.

ebean:
  test:
    platform: h2 #, h2, postgres, mysql, oracle, sqlserver, hana, clickhouse, sqlite
    ddlMode: dropCreate # none | dropCreate | migrations | create
    dbName: my_app

We can modify this test configuration to control what DDL is executed (create-all.sql or migrations) and the database platform we want to test against (potentially using docker).

### 3. Add ~/.ebean/ignore-docker-shutdown

mkdir ~/.ebean
touch ~/.ebean/ignore-docker-shutdown

For running tests on CI servers we typically want to stop and remove the docker containers when the tests have completed. However, for local development we want to keep the docker containers running making it faster to run tests.

Adding a marker file `~/.ebean/ignore-docker-shutdown` means the docker containers will stay running (which is good for local development).

ebean-test will take care of:

*   DDL generation and execution modes
*   Docker test container setup and execution based on the database platform
*   Current user and tenant provider if not already specified (to ease testing with @Who properties etc)

ebean.test.platform - application-test.yaml
-------------------------------------------

We use `ebean.test.platform` to specify the database platform we want to use when running tests. For example, we can specify _h2, postgres, mysql_ etc as the platform to run the tests.

##### e.g. Testing against Postgres

ebean:
  test:
    platform: postgres # h2, postgres, ...
    ddlMode: dropCreate # none | dropCreate | migrations | create
    dbName: my_app

##### e.g. Testing against MariaDB

ebean:
  test:
    platform: mariadb
    ddlMode: dropCreate # none | dropCreate | migrations | create
    dbName: my_app

For more details on each database platform see: 

[clickhouse](https://ebean.io/docs/database/clickhouse) , [cockroach](https://ebean.io/docs/database/cockroach) , [db2](https://ebean.io/docs/database/db2) , [h2](https://ebean.io/docs/database/h2) , [hana](https://ebean.io/docs/database/hana) , [mariadb](https://ebean.io/docs/database/mariadb) , [mysql](https://ebean.io/docs/database/mysql) , [nuodb](https://ebean.io/docs/database/nuodb) , [oracle](https://ebean.io/docs/database/oracle) , [postgres](https://ebean.io/docs/database/postgres) , [sqlite](https://ebean.io/docs/database/sqlite) , [sqlserver](https://ebean.io/docs/database/sqlserver) , [yugabytedb](https://ebean.io/docs/database/yugabyte)

DDL Mode
--------

Most of the time we use `dropCreate` mode which means that the database will be dropped and then re-created before we run all the tests.

We use _migrations_ to test database migrations.

| Mode | Description |
| --- | --- |
| dropCreate | Drop and then create all the tables etc. Most commonly used mode. |
| none | Do not run any DDL. Useful if we want to run 1 particular test without any DDL change. |
| migrations | Run the DB migration but first delete the database first ensuring the migration runs against a new database. |
| create | Run the create-all.sql DDL script but delete and recreate the database first. |

Note that `dropCreate` will generate `db-create-all.sql` and `db-drop-all.sql` scripts and these can be found in the maven `target` or gradle `build` directory.

Docker test containers
----------------------

Ebean provides docker test containers for Postgres, MariaDB, MySql, SqlServer, Oracle, Hana, DB2, Clickhouse, CockroachDB, YugabyteDB, Redis, ElasticSearch plus DynamoDB and Localstack.

_ebean-test_ automatically manages the docker containers and sets them up ready for running tests. As developers we just need to specify the platform (e.g. postgres) and Ebean will do the rest:

*   Start a docker container(s)
*   Wait for the container to be ready
*   Create the database and user setting any permissions as necessary
*   When ready allow the tests to run

We can see/review what is occurring by increasing the logging for `io.ebean.docker` to `TRACE`. When we do that we can see log messages like:

... Docker test container start and setup

15:15:02.537 INFO  io.ebean.docker.commands.Commands - Container ut_postgres running with port:6432 db:test_ex user:test_ex mode:Create shutdown:
15:15:02.538 DEBUG io.ebean.docker.commands.Commands - docker exec -i ut_postgres pg_isready -h localhost -p 5432
15:15:02.645 DEBUG io.ebean.docker.commands.Commands - docker exec -i ut_postgres psql -U postgres -c select datname from pg_database
15:15:02.753 DEBUG io.ebean.docker.commands.Commands - docker exec -i ut_postgres psql -U postgres -c select rolname from pg_roles where rolname = 'test_ex'
15:15:02.871 DEBUG io.ebean.docker.commands.Commands - docker exec -i ut_postgres psql -U postgres -c select 1 from pg_database where datname = 'test_ex'
15:15:02.960 DEBUG io.ebean.docker.commands.Commands - create database extensions hstore,pgcrypto
15:15:02.960 DEBUG io.ebean.docker.commands.Commands - docker exec -i ut_postgres psql -U postgres -d test_ex -c create extension if not exists hstore
15:15:03.058 DEBUG io.ebean.docker.commands.Commands - docker exec -i ut_postgres psql -U postgres -d test_ex -c create extension if not exists pgcrypto
15:15:03.143 DEBUG io.ebean.docker.commands.Commands - waitForConnectivity ut_postgres ...
15:15:03.143 DEBUG io.ebean.docker.commands.Commands - checkConnectivity on ut_postgres ...
15:15:03.190 DEBUG io.ebean.docker.commands.Commands - connectivity confirmed for ut_postgres
15:15:03.190 DEBUG io.ebean.docker.commands.Commands - Container ut_postgres ready with port 6432

...

15:15:03.239 [main] INFO  o.a.datasource.pool.ConnectionPool - DataSourcePool [db] autoCommit[false] transIsolation[READ_COMMITTED] min[2] max[200]
15:15:03.277 [main] INFO  io.ebean.internal.DefaultContainer - DatabasePlatform name:db platform:postgres

... DDL Execution

15:15:03.618 [main] INFO  io.ebean.DDL - Executing extra-dll - 0 statements
15:15:03.618 [main] INFO  io.ebean.DDL - Executing db-drop-all.sql - 26 statements
15:15:03.649 [main] DEBUG io.ebean.DDL - executing 1 of 26 alter table if exists address drop constraint if exists fk_address_country_code
15:15:03.651 [main] DEBUG io.ebean.DDL - executing 2 of 26 drop index if exists ix_address_country_code
...
15:15:03.701 [main] INFO  io.ebean.DDL - Executing db-create-all.sql - 28 statements
15:15:03.701 [main] DEBUG io.ebean.DDL - executing 1 of 28 create table address ( id                            bigserial not null, line1...
15:15:03.709 [main] DEBUG io.ebean.DDL - executing 2 of 28 create table contact ( id                            bigserial not null, first_n...
...
15:15:03.841 [main] INFO  io.ebean.DDL - Executing extra-dll - 1 statements
15:15:03.842 [main] DEBUG io.ebean.DDL - executing 1 of 1 create or replace view order_agg_vw as select d.order_id as id, d.order_id as or...

Container startup
-----------------

To startup the docker containers `ebean-test` hooks into the Ebean lifecycle. This means that it will "just work" whether the tests are run from the IDE, maven, gradle or any build tool. In prior iterations the startup of docker containers was hooked specifically into the maven lifecycle but this proved to be less than ideal. This approach also avoids the need to modify test code.

This docker test container integration provides a similar developer experience to using H2 database. That is, ebean-test brings up the database (if needed), sets up the database user, roles, schema etc (if needed) and gets the database ready for testing by running DDL (typically drop and recreate tables etc) ... and then run all tests.

Developers new to a project can just `git clone` and `mvn clean test` and it "just works" without any setup steps (as long as the developer machine has docker installed).

Container shutdown
------------------

On developer machines we generally want to keep the docker container running such that running tests is fast. For a developer running a single test via the IDE - most often this will just drop and recreate tables as the container is already running closely matching the speed of using in-memory H2.

To keep docker containers running on developer machines we put a marker file at `~/.ebean/ignore-docker-shutdown`.

On CI servers we want the docker containers to be stopped and removed at completion of tests. To do this we set `shutdown` to either `remove` (to stop and remove the container) or `stop` (to just stop the container).

ebean:
  test:
    shutdown: remove  # stop | remove
    platform: postgres # h2, postgres, mysql, oracle, sqlserver
    ddlMode: dropCreate # none | dropCreate | migrations
    dbName: my_app

Not using Docker
----------------

If we don't want to start and run a Docker container but instead test against some other existing database we can do that via setting `useDocker: false`.

The below configuration runs against an existing Postgres database. Typically when not using docker we need to set the username, password and url to appropriate values.

When we are using `useDocker: false` the database and user are expected to already exist.

ebean:
  test:
    useDocker: false  ## DO NOT USE DOCKER
    platform: postgres # h2, postgres, mysql, oracle, sqlserver
    ddlMode: dropCreate # none | dropCreate | migrations | create
    dbName: test
    postgres:
      username: test
      password: test
      url: jdbc:postgresql://localhost:5432/test

Current User and Tenant
-----------------------

ebean-test will automatically register a _current user provider_ and a _current tenant provider_. These are only set if you don't set them yourself.

This means is that without doing anything we can use `@WhoCreated / @WhoModified` in tests and via `io.ebean.test.UserContext` we can set current user and tenant in tests.

// set the current userId which will be put
// into 'WhoCreated' and 'WhoModified' properties

UserContext.setUserId("U1");

DDL generation properties
-------------------------

If we are **NOT** using `ebean-test` then we need to set appropriate properties to control the generation and running of DDL. We use the properties below to control DDL generation and execution of `db-create-all.sql` and `db-drop-all.sql`.

| Property | Description |
| --- | --- |
| ddl.generate | Set to true to generate the db-create-all.sql and db-drop-all.sql DDL scripts. |
| ddl.run | Set to true to run the db-create-all.sql, db-drop-all.sql and extra DDL scripts |
| ddl.createOnly | Set to true to run the db-create-all.sql but **NOT** run the db-drop-all.sql. Mostly used with H2 database in-memory testing when we know that the database is not populated / there are no tables to drop first. |
| ddl.initSql | Specify a SQL script to run prior to running the create-all ddl. |
| ddl.seedSql | Specify a SQL script to run after to running the create-all ddl. Typically this inserts seed data into the test database. |
| ebean.migraton.run | Set to true or false to run the migrations when the EbeanServer starts |

### Example application-test.properties

ebean.db.ddl.generate=true
ebean.db.ddl.run=true
ebean.db.ddl.initSql=initialise-test-db.sql
ebean.db.ddl.seedSql=seed-test-db.sql

datasource.db.username=sa
datasource.db.password=
datasource.db.databaseUrl=jdbc:h2:mem:tests
datasource.db.databaseDriver=org.h2.Driver

DDL/SQL Script Runner
---------------------

We can use `ScriptRunner` to runs DDL and SQL scripts. Typically these are scripts used for testing such as seed SQL scripts or truncate SQL scripts.

Scripts are executed in their own transaction and committed on successful completion.

#### Example of simple use

Database database = DB.getDefault();
database.script().run("/scripts/test-script.sql");

#### Example using place holders in the script

Map<String,String> placeholders = new HashMap();
placeholders.put("tableName", "e_basic");

Database database = DB.getDefault();
database.script().run("/scripts/test-script.sql", placeholders);

In our SQL scripts the way to reference the placeholder is:

`delete from ${tableName}`

`select count(*) from ${tableName}`
Notice that, the path to the script should start with "/". Ebean will load the script as a resource using `this.getClass().getResource(PATH_TO_RESOURCE)` so the resource should be available in the class path.

ElasticSearch
-------------

With Ebean we can use ElasticSearch by itself without another database (Postgres etc) or we can use ElasticSearch in conjunction with another [source of truth] database (Postgres etc).

To automatically start ElasticSearch as a docker container set `ebean.docstore` properties like those below in application-test.yaml:

ebean:
  test:
    platform: h2
    ddlMode: dropCreate # none | dropCreate | migrations | create
    dbName: myapp

  docstore:
    url: http://127.0.0.1:9201
    active: true
    generateMapping: true
    dropCreate: true

    elastic:
      version: 5.6.0
      port: 9201

Goto [database / elasticsearch](https://ebean.io/docs/database/elasticsearch) for more details.

Redis
-----

When we want to use Redis for L2 caching we can get `ebean-test` to automatically start a redis docker test container. To do this add `ebean.test.redis=latest` property like the example below:

ebean:
  test:
    redis: latest
    platform: h2 # h2, postgres, mysql, oracle, sqlserver, sqlite
    ddlMode: dropCreate # none | dropCreate | migrations | create
    dbName: my_app

Goto [database / redis](https://ebean.io/docs/database/redis) for more details.

[Edit Page](https://github.com/ebean-orm/website-source/blob/master/docs/testing/index.html)

[Next: CI Testing](https://ebean.io/docs/ci-testing)
