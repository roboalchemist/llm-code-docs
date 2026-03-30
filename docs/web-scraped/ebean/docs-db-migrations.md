# Source: https://ebean.io/docs/db-migrations

Title: DB Migration | Docs | Ebean

URL Source: https://ebean.io/docs/db-migrations

Markdown Content:
DB Migrations
-------------

DB Migrations are DDL changes that are applied typically when the application is started.

Ebean can generate the migrations for us by performing a `diff` on the model and then generating database platform specific DDL for the change.

Ebean can also run the migrations (similar to FlywayDb). It is recommended to use Ebean's built in migration runner rather than `FlywayDb` or `LiquiBase`.

Dependencies
------------

Add either ebean-test as a test scope dependency (which includes ebean-ddl-generator and other dependencies).

<dependency>
  <groupId>io.ebean</groupId>
  <artifactId>ebean-test</artifactId>
  <version>17.2.0</version>
  <scope>test</scope>
</dependency>

OR add ebean-ddl-generator as a test scope dependency.

<dependency>
  <groupId>io.ebean</groupId>
  <artifactId>ebean-ddl-generator</artifactId>
  <version>17.2.0</version>
  <scope>test</scope>
</dependency>

Generate a Migration
--------------------

In `src/test/java` add code to generate migrations. This first example generates database migrations for a single database platform - Postgres in this example.

*   [java](https://ebean.io/docs/db-migrations)
*   [kotlin](https://ebean.io/docs/db-migrations)

package main;

import io.ebean.annotation.Platform;
import io.ebean.dbmigration.DbMigration;
import java.io.IOException;

public class MigrationGenerator {

  /**
 * Generate the next "DB schema DIFF" migration.
 */
  public static void main(String[] args) throws IOException {

    DbMigration dbMigration = DbMigration.create();
    dbMigration.setPlatform(Platform.POSTGRES);

    dbMigration.generateMigration();
  }
}

import io.ebean.annotation.Platform
import io.ebean.dbmigration.DbMigration

fun main() {
  DbMigration.create().apply {
    setPlatform(Platform.POSTGRES)
  }.generateMigration()
}

### Multi-platform migration generation

To generate migrations for multiple different database platforms we use `addPlatform()` for each platform we want to generate migrations for. In the below example we generate migrations for Postgres, SqlServer and MySql.

*   [java](https://ebean.io/docs/db-migrations)
*   [kotlin](https://ebean.io/docs/db-migrations)

...
public class MigrationGenerator {

  /**
 * Generate the next "DB schema DIFF" migration.
 */
  public static void main(String[] args) throws IOException {

    DbMigration dbMigration = DbMigration.create();

    dbMigration.addPlatform(Platform.POSTGRES);
    dbMigration.addPlatform(Platform.SQLSERVER17);
    dbMigration.addPlatform(Platform.MYSQL);

    dbMigration.generateMigration();
  }
}

...
fun main() {
  DbMigration.create().apply {
    addPlatform(Platform.POSTGRES)
    addPlatform(Platform.SQLSERVER17)
    addPlatform(Platform.MYSQL)
  }.generateMigration()
}

Run the main method to generate the database migration. If nothing has changed then no migration will be generated. If the model has changed then the database migration is generated for the DIFF to the model.

Running the generation starts Ebean in offline mode (we do not need a database running to generate the migration). Ebean performs a DIFF to the model and generates the migration DDL script(s) for the platforms that we specified.

By default the generated migrations go into `src/main/resources/dbmigration`.

Running migrations
------------------

To get Ebean to run the DB migrations on startup:

#### 1. Set `ebean.migration.run` to true

##### Via properties - e.g. application.properties

## run migrations when the Ebean starts
ebean.migration.run=true

##### Via yaml - e.g. application.yaml

## run migrations when the Ebean starts
ebean:
  migration:
    run: true

#### 2. Add ebean-migration dependency

Add `io.ebean:ebean-migration` as a dependency if it is not already.

<dependency>
  <groupId>io.ebean</groupId>
  <artifactId>ebean-migration</artifactId>
  <version>13.6.0</version>
</dependency>

With `ebean.migration.run=true` then when Ebean starts it will look at the migrations and run any that need to be run. The migration runner will by default create a table called `db_migration` that holds the metadata about the migrations that have been run and inserts into this table when migrations are successfully executed.

[Next: DB Migration details](https://ebean.io/docs/db-migrations/detail)
