# Source: https://docs.upsun.com/development/sanitize-db/postgresql.md

# Source: https://docs.upsun.com/add-services/postgresql.md

# PostgreSQL (Database service)

PostgreSQL is a high-performance, standards-compliant relational SQL database.

See the [PostgreSQL documentation](https://www.postgresql.org/docs/9.6/index.md) for more information.

**Note**: 

The [example](#usage-example) provided later in this topic is specific to using only a **primary** database. For details about using read-only replicas to improve performance of read-heavy applications, see the [PostgreSQL read-only replication](https://docs.upsun.com/add-services/postgresql/postgresql-readonly-replication.md) topic.

## Supported versions

You can select the major version. But the latest compatible minor version is applied automatically and can’t be overridden.

Patch versions are applied periodically for bug fixes and the like. When you deploy your app, you always get the latest available patches.

   - 18

   - 17

   - 16

   - 15

   - 14

   - 13

   - 12

**Note**: 

You can’t upgrade to PostgreSQL 12 with the ``postgis`` extension enabled.
For more details, see how to [upgrade to PostgreSQL 12 with ](#upgrade-to-postgresql-12-with-the-postgis-extension).

### Deprecated versions

The following versions are [deprecated](https://docs.upsun.com/glossary.md#deprecated-versions).
They're available, but they don't receive security updates from upstream and aren't guaranteed to work.
They'll be removed in the future – consider migrating to a [supported version](#supported-versions).

   - 11

   - 10

   - 9.6

   - 9.5

   - 9.4

   - 9.3

## Relationship reference

For each service [defined via a relationship](#usage-example) to your application,
Upsun automatically generates corresponding environment variables within your application container,
in the ``$_`` format.

Here is example information available through the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) themselves,
or through the [``PLATFORM_RELATIONSHIPS`` environment variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).

For some advanced use cases, you can use the [PLATFORM_RELATIONSHIPS](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).
The structure of the ``PLATFORM_RELATIONSHIPS`` environment variable can be obtained by running ``upsun relationships`` in your terminal:

```json {}
{
  "username": "main",
  "scheme": "pgsql",
  "service": "postgresql",
  "fragment": null,
  "ip": "123.456.78.90",
  "hostname": "azertyuiopqsdfghjklm.postgresql.service._.eu-1.platformsh.site",
  "port": 5432,
  "cluster": "azertyuiopqsdf-main-afdwftq",
  "host": "postgresql.internal",
  "rel": "postgresql",
  "path": "main",
  "query": {
    "is_master": true
  },
  "password": "ChangeMe",
  "type": "postgresql:18",
  "public": false,
  "host_mapped": false
}
```

Here is an example of how to gather [PLATFORM_RELATIONSHIPS](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables) information in a [.environment](https://docs.upsun.com/development/variables/set-variables.md#use-env-files):

    .environment

```bash {}
# Decode the built-in credentials object variable.
export RELATIONSHIPS_JSON="$(echo "$PLATFORM_RELATIONSHIPS" | base64 --decode)"

# Set environment variables for individual credentials.
export APP_POSTGRESQL_HOST="$(echo "$RELATIONSHIPS_JSON" | jq -r '.postgresql[0].host')"
```

## Usage example

**Note**: 

Use the steps and sample code below if your application will connect to a **primary** PostgreSQL database. For details about using read-only replicas to improve performance of read-heavy applications, see the [PostgreSQL read-only replication](https://docs.upsun.com/add-services/postgresql/postgresql-readonly-replication.md) topic.

### 1. Configure the service

To define the service, use the ``postgresql`` type:

```yaml  {location=".upsun/config.yaml"}
services:
  # The name of the service container. Must be unique within a project.
  <SERVICE_NAME>:
    type: postgresql:<VERSION>
```

Note that changing the name of the service replaces it with a brand new service and all existing data is lost. Back up your data before changing the service.

### 2. Define the relationship

To define the relationship, use the following configuration:

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  <APP_NAME>:
    # Relationships enable access from this app to a given service.
    # The example below shows simplified configuration leveraging a default service
    # (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      <SERVICE_NAME>:
```

You can define ``<SERVICE_NAME>`` as you like, so long as it’s unique between all defined services
and matches in both the application and services configuration.
The example above leverages [default endpoint](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships) configuration for relationships.
That is, it uses default endpoints behind-the-scenes, providing a [relationship](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships)
(the network address a service is accessible from) that is identical to the name of that service.
Depending on your needs, instead of default endpoint configuration,
you can use [explicit endpoint configuration](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships).
With the above definition, the application container (``<APP_NAME>``) now has access to the service via the relationship ``<SERVICE_NAME>`` and its corresponding [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables).

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  <APP_NAME>:
    # Relationships enable access from this app to a given service.
    # The example below shows configuration with an explicitly set service name and endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      <RELATIONSHIP_NAME>:
        service: <SERVICE_NAME>
        endpoint: postgresql
```

You can define ``<SERVICE_NAME>`` and ``<RELATIONSHIP_NAME>`` as you like, so long as it’s unique between all defined services and relationships
and matches in both the application and services configuration.
The example above leverages [explicit endpoint](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships) configuration for relationships.
Depending on your needs, instead of explicit endpoint configuration,
you can use [default endpoint configuration](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships).
With the above definition, the application container now has [access to the service](#use-in-app) via the relationship ``<RELATIONSHIP_NAME>`` and its corresponding [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables).

For PHP, enable the [extension](https://docs.upsun.com/languages/php/extensions.md) for the service:

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  <APP_NAME>:
    # PHP extensions.
    runtime:
      extensions:
        - pdo_pgsql
    # Relationships enable access from this app to a given service.
    # The example below shows simplified configuration leveraging a default service
    # (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      <SERVICE_NAME>:
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  <APP_NAME>:
    # PHP extensions.
    runtime:
      extensions:
        - pdo_pgsql
    # Relationships enable access from this app to a given service.
    # The example below shows configuration with an explicitly set service name and endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      <RELATIONSHIP_NAME>:
        service: <SERVICE_NAME>
        endpoint: postgresql
```

### Example configuration

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # PHP extensions.
    runtime:
      extensions:
        - pdo_pgsql
    # Relationships enable access from this app to a given service.
    # The example below shows simplified configuration leveraging a default service
    # (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      postgresql:
services:
  # The name of the service container. Must be unique within a project.
  postgresql:
    type: postgresql:18
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # PHP extensions.
    runtime:
      extensions:
        - pdo_pgsql
    # Relationships enable access from this app to a given service.
    # The example below shows configuration with an explicitly set service name and endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      postgresql:
        service: postgresql
        endpoint: postgresql
services:
  # The name of the service container. Must be unique within a project.
  postgresql:
      type: postgresql:18
```

### Use in app

To use the configured service in your app, add a configuration file similar to the following to your project.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"

    # PHP extensions.
    runtime:
      extensions:
        - pdo_pgsql

    [...]

    # Relationships enable access from this app to a given service.
    # The example below shows simplified configuration leveraging a default service
    # (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      postgresql:
services:
  # The name of the service container. Must be unique within a project.
  postgresql:
    type: postgresql:18
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"

    # PHP extensions.
    runtime:
      extensions:
        - pdo_pgsql

    [...]

    # Relationships enable access from this app to a given service.
    # The example below shows configuration with an explicitly set service name and endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      postgresql:
        service: postgresql
        endpoint: postgresql
services:
  # The name of the service container. Must be unique within a project.
  postgresql:
    type: postgresql:18
```

This configuration defines a single application (`myapp`), whose source code exists in the `<PROJECT_ROOT>/myapp` directory. 
`myapp` has access to the `postgresql` service, via a relationship whose name is [identical to the service name](#2-define-the-relationship)
(as per [default endpoint](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships) configuration for relationships).

From this, ``myapp`` can retrieve access credentials to the service through the [relationship environment variables](#relationship-reference).

```bash  {location="myapp/.environment"}
# Set environment variables for individual credentials.
# For more information, please visit https://docs.upsun.com/development/variables.html#service-environment-variables.
export DB_CONNECTION="${POSTGRESQL_SCHEME}"
export DB_USERNAME="${POSTGRESQL_USERNAME}"
export DB_PASSWORD="${POSTGRESQL_PASSWORD}"
export DB_HOST="${POSTGRESQL_HOST}"
export DB_PORT="${POSTGRESQL_PORT}"
export DB_DATABASE="${POSTGRESQL_PATH}"

# Surface connection string variable for use in app.
export DATABASE_URL="${DB_CONNECTION}://${DB_USERNAME}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_DATABASE}"
```

The above file — ``.environment`` in the ``myapp`` directory — is automatically sourced by Upsun into the runtime environment, so that the variable ``DATABASE_URL`` can be used within the application to connect to the service.

Note that ``DATABASE_URL``, and all Upsun [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) like ``POSTGRESQL_HOST``, are environment-dependent.
Unlike the build produced for a given commit,
they can’t be reused across environments and only allow your app to connect to a single service instance on a single environment.

A file very similar to this is generated automatically for your when using the ``upsun ify`` command to [migrate a codebase to Upsun](https://docs.upsun.com/get-started.md).

## Access the service directly

Access the service using the Upsun CLI by running `upsun sql`.

You can also access it from your app container via [SSH](https://docs.upsun.com/development/ssh.md).
From your [relationship data](#relationship-reference), you need: `POSTGRESQL_USERNAME`, `POSTGRESQL_HOST`, and `POSTGRESQL_PORT`.
Then run the following command:

```bash
psql -U <POSTGRESQL_USERNAME> -h <POSTGRESQL_HOST> -p <POSTGRESQL_PORT>
```

Using the values from the [example](#relationship-reference), that would be:

```bash
psql -U main -h postgresql.internal -p 5432
```

You can obtain the complete list of available service environment variables in your app container by running ``upsun ssh env``.

Note that the information about the relationship can change when an app is redeployed or restarted or the relationship is changed. So your apps should only rely on the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) directly rather than hard coding any values.

## Exporting data

The easiest way to download all data in a PostgreSQL instance is with the Upsun CLI. If you have a single SQL database, the following command exports all data using the `pg_dump` command to a local file:

```bash
upsun db:dump
```

If you have multiple SQL databases it prompts you which one to export. You can also specify one by relationship name explicitly:

```bash
upsun db:dump --relationship postgresql
```

By default the file is uncompressed. If you want to compress it, use the `--gzip` (`-z`) option:

```bash
upsun db:dump --gzip
```

You can use the `--stdout` option to pipe the result to another command. For example, if you want to create a bzip2-compressed file, you can run:

```bash
upsun db:dump --stdout | bzip2 > dump.sql.bz2
```

It is also possible to generate the dump locally if you have the `pg_dump` command installed with `upsun tunnel:single`. The command will first ask for the service and then will provide a prompt for the URI string that you can use. For example:

```bash
pg_dump -d postgresql://REPLACE_URI_FROM_OUTPUT -f dump.sql
```

## Importing data

Make sure that the imported file contains objects with cleared ownership and `IF EXISTS` clauses. For example, you can create a DB dump with following parameters:

```bash
pg_dump --no-owner --clean --if-exists
```

The easiest way to load data into a database is to pipe an SQL dump through the `upsun sql` command, like so:

```bash
upsun sql < my_database_backup.sql
```

That runs the database backup against the SQL database on Upsun.
That works for any SQL file, so the usual caveats about importing an SQL dump apply
(for example, it's best to run against an empty database).
As with exporting, you can also specify a specific environment to use and a specific database relationship to use, if there are multiple.

```bash
upsun sql --relationship postgresql -e <BRANCH_NAME> < my_database_backup.sql
```

**Note**: 

Importing a database backup is a destructive operation. It overwrites data already in your database.
Taking a backup or a database export before doing so is strongly recommended.

## Sanitizing data

To ensure people who review code changes can't access personally identifiable information stored in your database,
[sanitize your preview environments](https://docs.upsun.com/development/sanitize-db/postgresql.md).

## Set locale for database

You can choose your locale when a database is created by setting locale-related variables. There are three ways to set a locale option, as detailed in the table below:

| Name   | Type      | Default  | Description  |
|--------|-----------|----------|--------------|
| `default_ctype` | `string`  | `C.UTF-8` | The default character classification. Affects any tables created after it's set.|
| `default_collation` | `string`|`C.UTF-8`| The default collation rules. Affects any tables created after it's set.|
| `default_charset` | `string`  | `UTF8` | The default encoding character set. Affects any tables created after it's set.|

## Multiple databases

Support for defining multiple databases and multiple users with different permissions is available in versions `10` and later of this service. 
To do so requires defining multiple endpoints.
Under the `configuration` key of your service there are two additional keys:

* `databases`:  This is a YAML array listing the databases that should be created. If not specified, a single database named `main` is created.

  Note that removing a schema from the list of `schemas` on further deployments results in **the deletion of the schema.**
* `endpoints`: This is a nested YAML object defining different credentials. Each endpoint may have access to one or more schemas (databases), and may have different levels of permission for each. The valid permission levels are:
  * `ro`: Using this endpoint only `SELECT` queries are allowed.
  * `rw`: Using this endpoint `SELECT` queries as well as `INSERT`/`UPDATE`/`DELETE` queries are allowed.
  * `admin`: Using this endpoint all queries are allowed, including DDL queries (`CREATE TABLE`, `DROP TABLE`, etc.).

Consider the following illustrative example:

```yaml  {location=".upsun/config.yaml"}
services:
  # The name of the service container. Must be unique within a project.
  postgresql:
    type: "postgresql:18"
    configuration:
      databases:
        - main
        - legacy
      endpoints:
        admin:
          privileges:
            main: admin
            legacy: admin
        reporter:
          default_database: main
          privileges:
            main: ro
        importer:
          default_database: legacy
          privileges:
            legacy: rw
```

This example creates a single PostgreSQL service named `postgresql`. The server has two databases, `main` and `legacy` with three endpoints created.

* `admin`: has full access to both databases.
* `reporter`: has `SELECT` query access to the `main` database, but no access to `legacy`.
* `importer`: has `SELECT`/`INSERT`/`UPDATE`/`DELETE` access (but not DDL access) to the `legacy` database. It doesn't have access to `main`.

If a given endpoint has access to multiple databases you should also specify which is listed by default in the relationships array. If one isn't specified, the `path` property of the relationship is `null`. While that may be acceptable for an application that knows the name of the database it's connecting to, automated tools like the Upsun CLI can't access the database on that relationship. For that reason, defining the `default_database` property is always recommended.

Once these endpoints are defined, you need to expose them to your application as a relationship. Continuing with the above example, your `relationships` in `.upsun/config.yaml` might look like:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:

    source:
      root: "/"

    [...]

    # Relationships enable access from this app to a given service.
    # The example below shows configuration with explicitly set service names and endpoints.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      database:
        service: postgresql
        endpoint: admin
      reports:
        service: postgresql
        endpoint: reporter
      imports:
        service: postgresql
        endpoint: importer

services:
  # The name of the service container. Must be unique within a project.
  postgresql:
    type: "postgresql:18"
    configuration:
      databases:
          - main
          - legacy
      endpoints:
        admin:
          privileges:
            main: admin
            legacy: admin
        reporter:
          default_database: main
          privileges:
            main: ro
        importer:
          default_database: legacy
          privileges:
            legacy: rw
```

Each database is accessible to your application through the `database`, `reports`, and `imports` relationships.
They'll be available in the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) and all have the same structure documented [above](#relationship-reference), but with different credentials. You can use those to connect to the appropriate database with the specified restrictions using whatever the SQL access tools are for your language and application.

A service configuration without the `configuration` block defined is equivalent to the following default values:

```yaml  {location=".upsun/config.yaml"}
services:
  # The name of the service container. Must be unique within a project.
  postgresql:
    type: "postgresql:18"
    configuration:
      databases:
        - main
      endpoints:
        postgresql:
          default_database: main
          privileges:
            main: admin
```

If you do not define `database` but `endpoints` are defined, then the single database `main` is created with the following assumed configuration:

```yaml  {location=".upsun/config.yaml"}
services:
  # The name of the service container. Must be unique within a project.
  postgresql:
    type: "postgresql:18"
    configuration:
      databases:
        - main
      endpoints: 
```

Alternatively, if you define multiple databases but no endpoints, a single user `main` is created with `admin` access to each of your databases, equivalent to the configuration below:

```yaml  {location=".upsun/config.yaml"}
services:
  # The name of the service container. Must be unique within a project.
  postgresql:
    type: "postgresql:18"
    configuration:
      databases:
        - firstdb
        - seconddb
        - thirddb
      endpoints:
        main:
          firstdb: admin
          seconddb: admin
          thirddb: admin
```

## Password generation

When you connect your app to a database,
an empty password is generated for the database by default.
This can cause issues with your app.

To generate real passwords for your database,
define custom endpoints in your [service configuration](#1-configure-the-service).
For each custom endpoint you create,
you get an automatically generated password,
similarly to when you create [multiple databases](#multiple-databases).
Note that you can't customize these automatically generated passwords.

After your custom endpoints are exposed as relationships in your [app configuration](https://docs.upsun.com../../create-apps.md),
you can retrieve the password for each endpoint
through the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) within your [application containers](https://docs.upsun.com/development/variables/use-variables.md#access-variables-in-your-app).
The password value changes automatically over time, to avoid downtime its value has to be read dynamically by your app.
Globally speaking, having passwords hard-coded into your codebase can cause security issues and should be avoided.

When you switch from the default configuration with an empty password to custom endpoints,
make sure your service name remains unchanged.
Failure to do so results in the creation of a new service,
which removes any existing data from your database.

## Service timezone

To change the timezone for the current session, run `SET TIME ZONE <TIMEZONE>;`.

## Extensions

Upsun supports a number of PostgreSQL extensions. To enable them, list them under the `configuration.extensions` key in your `.upsun/config.yaml` file, like so:

```yaml  {location=".upsun/config.yaml"}
services:
  # The name of the service container. Must be unique within a project.
  postgresql:
    type: "postgresql:18"
    configuration:
      extensions:
        - pg_trgm
        - hstore
```

In this case, you have `pg_trgm` installed, providing functions to determine the similarity of text based on trigram matching, and `hstore` providing a key-value store.

### Available extensions

The following is the extensive list of supported extensions. Note that you can't currently add custom
extensions not listed here.

* `address_standardizer` - Used to parse an address into constituent elements. Generally used to support geocoding address normalization step.
* `address_standardizer_data_us` - For standardizing addresses based on US dataset example
* `adminpack` - administrative functions for PostgreSQL (only available in versions less than 17)
* `autoinc` - functions for auto-incrementing fields
* `bloom` - bloom access method - signature file based index (requires 9.6 or higher)
* `btree_gin` - support for indexing common data types in GIN
* `btree_gist` - support for indexing common data types in GiST
* `chkpass` - data type for auto-encrypted passwords
* `citext` - data type for case-insensitive character strings
* `cube` - data type for multidimensional cubes
* `dblink` - connect to other PostgreSQL databases from within a database
* `dict_int` - text search dictionary template for integers
* `dict_xsyn` - text search dictionary template for extended synonym processing
* `earthdistance` - calculate great-circle distances on the surface of the Earth
* `file_fdw` - foreign-data wrapper for flat file access
* `fuzzystrmatch` - determine similarities and distance between strings
* `hstore` - data type for storing sets of (key, value) pairs
* `insert_username` - functions for tracking who changed a table
* `intagg` - integer aggregator and enumerator (obsolete)
* `intarray` - functions, operators, and index support for 1-D arrays of integers
* `isn` - data types for international product numbering standards
* `lo` - Large Object maintenance
* `ltree` - data type for hierarchical tree-like structures
* `moddatetime` - functions for tracking last modification time
* `pageinspect` - inspect the contents of database pages at a low level
* `pg_buffercache` - examine the shared buffer cache
* `pg_freespacemap` - examine the free space map (FSM)
* `pg_prewarm` - prewarm relation data (requires 9.6 or higher)
* `pg_stat_statements` - track execution statistics of all SQL statements executed
* `pg_trgm` - text similarity measurement and index searching based on trigrams
* `pg_visibility` - examine the visibility map (VM) and page-level visibility info (requires 9.6 or higher)
* `pgcrypto` - cryptographic functions
* `pgrouting` - pgRouting Extension (requires 9.6 or higher)
* `pgrowlocks` - show row-level locking information
* `pgstattuple` - show tuple-level statistics
* `plpgsql` - PL/pgSQL procedural language
* `postgis` - PostGIS geometry, geography, and raster spatial types and functions
* `postgis_sfcgal` - PostGIS SFCGAL functions
* `postgis_tiger_geocoder` - PostGIS tiger geocoder and reverse geocoder
* `postgis_topology` - PostGIS topology spatial types and functions
* `postgres_fdw` - foreign-data wrapper for remote PostgreSQL servers
* `refint` - functions for implementing referential integrity (obsolete)
* `seg` - data type for representing line segments or floating-point intervals
* `sslinfo` - information about SSL certificates
* `tablefunc` - functions that manipulate whole tables, including `crosstab`
* `tcn` - Triggered change notifications
* `timetravel` - functions for implementing time travel
* `tsearch2` - compatibility package for pre-8.3 text search functions (obsolete, only available for 9.6 and 9.3)
* `tsm_system_rows` - TABLESAMPLE method which accepts number of rows as a limit (requires 9.6 or higher)
* `tsm_system_time` - TABLESAMPLE method which accepts time in milliseconds as a limit (requires 9.6 or higher)
* `unaccent` - text search dictionary that removes accents
* `uuid-ossp` - generate universally unique identifiers (UUIDs)
* `vector` - Open-source [vector](https://github.com/pgvector/pgvector) similarity search for PostgreSQL 11+
* `xml2` - XPath querying and XSLT

**Note**: 

You can’t upgrade to PostgreSQL 12 with the ``postgis`` extension enabled.
For more details, see how to [upgrade to PostgreSQL 12 with ](#upgrade-to-postgresql-12-with-the-postgis-extension).

## Notes

### Could not find driver

If you see this error: `Fatal error: Uncaught exception 'PDOException' with message 'could not find driver'`, this means you are missing the `pdo_pgsql` PHP extension. You need to enable it in your `.upsun/config.yaml` ([see above](#1-configure-the-service)).

## Upgrading

PostgreSQL 10 and later include an upgrade utility that can convert databases from previous versions to version 10 or later. If you upgrade your service from a previous version of PostgreSQL to version 10 or above, it upgrades automatically.

The utility can't upgrade PostgreSQL 9 versions, so upgrades from PostgreSQL 9.3 to 9.6 aren't supported. Upgrade straight to version 11 instead.

**Note**: 

Make sure you first test your migration on a separate branch.

Also, be sure to take a backup of your production environment **before** you merge this change.

**Warning**: 

Downgrading isn’t supported. If you need to downgrade, dump to SQL, remove the service, recreate the service, and import your dump.

### Upgrade to PostgreSQL 12 with the `postgis` extension

You can't upgrade to PostgreSQL 12 with the `postgis` extension enabled.
It involves a change to a major version that results in a failed deployment that requires support intervention to fix.
Upgrading from 12 to a higher version is possible.

If you need to upgrade to version 12, follow the same steps recommended for downgrading:

1. Dump the database.
2. Remove the service.
3. Create a new service with PostgreSQL 12.
4. Import the dump to that service.

