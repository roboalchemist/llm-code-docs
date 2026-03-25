# Source: https://ebean.io/docs/ddl-generation

Title: Create All DDL | Docs

URL Source: https://ebean.io/docs/ddl-generation

Markdown Content:
DDL Generation
--------------

Ebean can generate and execute `CREATE ALL` and `DROP ALL` DDL scripts which create all the tables. This is used for testing purposes.

> When running a test or suite of tests the DB is created entirely from scratch

Using ebean-test
----------------

The best way to control and run DDL for testing is to use [ebean-test](https://ebean.io/docs/testing) and the [ddlMode](https://ebean.io/docs/testing#ddlmode). Using `dropCreate` means the DDL for create-all and drop-all is generated and run.

##### In application-test.yml

ebean:
  test:
    platform: h2 # h2, postgres, mysql, oracle, sqlserver
    ddlMode: dropCreate # none | dropCreate | migrations | create
    dbName: myapp

Using properties
----------------

If we don't want to use [ebean-test](https://ebean.io/docs/testing) we can instead set both `ebean.ddl.generate` and `ebean.ddl.run` properties to true in `application-test.yml` (which is in src/test/resources) and in this way the `CREATE ALL` DDL is only generated and executed when running tests.

##### In application-test.yml

ebean:
  ddl:
    generate: true
    run: true

##### Or application-test.properties

ebean.ddl.generate=true
ebean.ddl.run=true

db-create-all.sql
-----------------

When DDL is generated `db-create-all.sql` and `db-drop-all.sql` are generated and put into the maven `target` or gradle `build` directory.

When tests are run Ebean automatically regenerates these ddl script files and executes them prior to running the tests. This effectively recreates the database prior to running tests.

Initial DDL
-----------

We can additionally specify DDL to execute prior to running the "create-all" DDL via the `initSql` property.

ebean.ddl.initSql=testInitialDdl.sql

Seed DDL
--------

We can additionally specify DDL to execute after running the "create-all" DDL which we typically use to seed the database via the `seedSql` property.

ebean.ddl.seedSql=testSeedData.sql

#### Compared to DB Migrations

[DB Migration](https://ebean.io/docs/db-migrations) is different in that `DIFF` DDL scripts are generated for the changes to the model and these `DIFF` DDL scripts can be applied to the target database typically when Ebean starts.

[Next: Extra DDL](https://ebean.io/docs/extra-ddl)
