# Source: https://planetscale.com/docs/postgres/extensions.md

# Extensions

> PostgreSQL extensions are add-on modules that extend the functionality of your database beyond the core features. They provide additional data types, functions, operators, indexes, and other capabilities without requiring modifications to the PostgreSQL source code.

<Note>
  You can submit and vote for the extensions you want us to support next at [ps-extensions.io](https://ps-extensions.io/).
</Note>

Extensions work by packaging related database objects (functions, data types, operators, etc.) into a single installable unit. When you install an extension, PostgreSQL loads the necessary code and creates the required database objects in your database schema. This modular approach allows you to add only the functionality you need while keeping your database lightweight and maintainable.

## Types of Extensions

PostgreSQL extensions generally fall into two main categories:

### Native Extensions

These are extensions that ship with PostgreSQL itself and are maintained by the PostgreSQL core team. Examples include:

* **Data type extensions**: `citext`, `hstore`, `uuid-ossp` for specialized data types
* **Index extensions**: `btree_gin`, `btree_gist` for advanced indexing capabilities
* **Text search extensions**: `unaccent`, `pg_trgm` for full-text search enhancements
* **Utility extensions**: `pgcrypto` for cryptographic functions, `tablefunc` for table manipulation

### Community Extensions

These are developed and maintained by the community or third-party organizations. Popular examples include:

* **Vector search**: `pgvector` for AI/ML vector operations
* **Query optimization**: `pg_hint_plan` for query plan hints
* **Partitioning**: `pg_partman` for automated table partitioning

<Warning>
  Extensions that modify shared memory settings, background worker processes, or core database functionality typically require a restart. You can only enable these extensions through the [Dashboard](#configuring-extensions-in-the-dashboard).

  Most simple extensions like data types or functions can be installed without a restart.
</Warning>

## Managing Extensions

<Note>
  Some extensions may require that you use a role with superuser privileges to enable them on your PlanetScale Postgres database. See [supported extensions](#supported-extensions) for more information.
</Note>

### Installing an Extension

To install an extension in your database, use the `CREATE EXTENSION` command:

```sql  theme={null}
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

### Removing an Extension

To remove an extension from your database, use the `DROP EXTENSION` command:

```sql  theme={null}
DROP EXTENSION IF EXISTS pgcrypto;
```

### Updating an Extension

To update an extension to a newer version, use the `ALTER EXTENSION` command:

```sql  theme={null}
ALTER EXTENSION pgcrypto UPDATE;
```

### Viewing Installed Extensions

To see all extensions currently installed in your database, use this query:

```sql  theme={null}
SELECT name, default_version, installed_version, comment
FROM pg_available_extensions
WHERE installed_version IS NOT NULL
ORDER BY name;
```

To view all available extensions (both installed and available for installation):

```sql  theme={null}
SELECT name, default_version, comment
FROM pg_available_extensions
ORDER BY name;
```

### Installing Extensions in Specific Schemas

By default, extensions are installed in the `public` schema. To install an extension in a specific schema:

```sql  theme={null}
CREATE EXTENSION IF NOT EXISTS pgcrypto SCHEMA my_schema;
```

To move an existing extension to a different schema:

```sql  theme={null}
ALTER EXTENSION pgcrypto SET SCHEMA new_schema;
```

<Note>
  Not all extensions support being installed in non-public schemas. Most utility and data type extensions work fine, but some system-level extensions must remain in the public schema.
</Note>

## Configuring Extensions in the Dashboard

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/extensions/configure-extensions.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=302182a33fecf2d1249c09bf789417f5" alt="Configuring Extensions" data-og-width="2182" width="2182" data-og-height="1266" height="1266" data-path="docs/postgres/extensions/configure-extensions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/extensions/configure-extensions.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=af9ce7f2b12a9e8ed1fae56f893b833a 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/extensions/configure-extensions.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=cfa0e454fb27894977c890280f89aefd 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/extensions/configure-extensions.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=f52fef0fa6a024579e06a83deab87322 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/extensions/configure-extensions.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=202621209cea2adb9f66d1dc5bc0162d 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/extensions/configure-extensions.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=cfbc152a65a3f2b142f3fa30fd09a646 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/extensions/configure-extensions.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=0ae4b1a13c7ca56fd00852e7650a0a6e 2500w" />

Some extensions require explicit configuration through the PlanetScale dashboard and may consume additional resources on your database instances. Configuring these extensions may require a database restart.
The extensions that require a restart are marked with a ✅ in the "Restart required" column. For `Production` clusters, these reboots are applied in a rolling cadence through the cluster's instances.

For detailed configuration instructions and parameter descriptions for each extension, please refer to their individual documentation pages via the 📝 links in the "Additional Notes" column.

## Troubleshooting

### Common Extension Issues

#### Extension not found

```sql  theme={null}
ERROR: extension "extension_name" is not available
```

This means the extension is not installed on the server or not supported. Check the [supported extensions list](#supported-extensions) below.

#### Permission denied

```sql  theme={null}
ERROR: permission denied to create extension "extension_name"
```

Extensions typically require database owner or superuser privileges. Contact support if you encounter permission issues.

#### Extension already exists

```sql  theme={null}
ERROR: extension "extension_name" already exists
```

Use `CREATE EXTENSION IF NOT EXISTS extension_name;` to avoid this error, or check installed extensions first.

#### Dependency conflicts

```sql  theme={null}
ERROR: required extension "dependency_name" is not installed
```

Some extensions depend on others. Install the required dependency first, then retry installing your desired extension.

## Supported Extensions

### Table Column Legend

<Note>
  Newer Postgres versions ship with newer versions of extensions. When upgrading to a newer Postgres version, make sure to test your application for compatibility with those extension versions.\*
</Note>

* **Extension**: Extension name with link to official documentation
* **Description**: Brief description of extension functionality
* **Version**: Version number available in PlanetScale (or *TBD* if placeholder)
* **Superuser required**: ⭐ = Extension requires superuser privileges to use its functionality
* **Restart required**: ✅ = Must be enabled through PlanetScale dashboard first because the extension requires shared libraries and a restart (blank = install directly with `CREATE EXTENSION`)
* **Additional Notes**: 📝 = Link to detailed configuration documentation

### Supported Native PostgreSQL Extensions

#### Postgres 18.1

| Extension                                                                                                | Description                                                                                           | Version | Superuser required | Restart required | Additional Notes                                   |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------- | ------------------ | ---------------- | -------------------------------------------------- |
| [autoinc](https://www.postgresql.org/docs/current/contrib-spi.html#CONTRIB-SPI-AUTOINC)                  | Functions for autoincrementing fields                                                                 | 1.0     | ⭐                  |                  |                                                    |
| [bloom](https://www.postgresql.org/docs/current/bloom.html)                                              | Bloom filter index access method                                                                      | 1.0     | ⭐                  |                  |                                                    |
| [btree\_gin](https://www.postgresql.org/docs/current/btree-gin.html)                                     | Provides GIN operator classes that implement B-tree equivalent behavior for various data types        | 1.3     |                    |                  |                                                    |
| [btree\_gist](https://www.postgresql.org/docs/current/btree-gist.html)                                   | Provides GiST index operator classes that implement B-tree equivalent behavior                        | 1.8     |                    |                  |                                                    |
| [citext](https://www.postgresql.org/docs/current/citext.html)                                            | Provides case-insensitive character string type                                                       | 1.8     |                    |                  |                                                    |
| [cube](https://www.postgresql.org/docs/current/cube.html)                                                | Data type for representing multidimensional cubes                                                     | 1.5     |                    |                  |                                                    |
| [dict\_int](https://www.postgresql.org/docs/current/dict-int.html)                                       | Text search dictionary template for integers                                                          | 1.0     |                    |                  |                                                    |
| [dict\_xsyn](https://www.postgresql.org/docs/current/dict-xsyn.html)                                     | Text search dictionary for extended synonym processing                                                | 1.0     | ⭐                  |                  |                                                    |
| [earthdistance](https://www.postgresql.org/docs/current/earthdistance.html)                              | Calculate great circle distances on the surface of the Earth                                          | 1.2     | ⭐                  |                  |                                                    |
| [fuzzystrmatch](https://www.postgresql.org/docs/current/fuzzystrmatch.html)                              | Functions for determining similarities and distance between strings                                   | 1.2     |                    |                  |                                                    |
| [hstore](https://www.postgresql.org/docs/current/hstore.html)                                            | Data type for storing sets of key/value pairs within a single PostgreSQL value                        | 1.8     |                    |                  |                                                    |
| [insert\_username](https://www.postgresql.org/docs/current/contrib-spi.html#CONTRIB-SPI-INSERT-USERNAME) | Functions for tracking who changed a table                                                            | 1.0     | ⭐                  |                  |                                                    |
| [intagg](https://www.postgresql.org/docs/current/intagg.html)                                            | Integer aggregator and enumerator (deprecated)                                                        | 1.1     | ⭐                  |                  |                                                    |
| [intarray](https://www.postgresql.org/docs/current/intarray.html)                                        | Functions and operators for manipulating null-free arrays of integers                                 | 1.5     |                    |                  |                                                    |
| [isn](https://www.postgresql.org/docs/current/isn.html)                                                  | Data types for international product numbering standards                                              | 1.3     |                    |                  |                                                    |
| [lo](https://www.postgresql.org/docs/current/lo.html)                                                    | Support for managing Large Objects (also called BLOBs)                                                | 1.2     |                    |                  |                                                    |
| [ltree](https://www.postgresql.org/docs/current/ltree.html)                                              | Data type for representing labels of data stored in hierarchical tree-like structures                 | 1.3     |                    |                  |                                                    |
| [moddatetime](https://www.postgresql.org/docs/current/contrib-spi.html#CONTRIB-SPI-MODDATETIME)          | Functions for tracking last modification time                                                         | 1.0     | ⭐                  |                  |                                                    |
| [pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html)                    | Provides a means for tracking planning and execution statistics of all SQL statements                 | 1.12    | ⭐                  | ✅                | [📝](/docs/postgres/extensions/pg_stat_statements) |
| [pg\_trgm](https://www.postgresql.org/docs/current/pgtrgm.html)                                          | Functions and operators for determining the similarity of alphanumeric text based on trigram matching | 1.6     |                    |                  |                                                    |
| [pgcrypto](https://www.postgresql.org/docs/current/pgcrypto.html)                                        | Cryptographic functions for PostgreSQL                                                                | 1.4     |                    |                  |                                                    |
| [pgrowlocks](https://www.postgresql.org/docs/current/pgrowlocks.html)                                    | Show row-level locking information                                                                    | 1.2     | ⭐                  |                  |                                                    |
| [pgstattuple](https://www.postgresql.org/docs/current/pgstattuple.html)                                  | Obtain tuple-level statistics                                                                         | 1.5     | ⭐                  |                  |                                                    |
| [plpgsql](https://www.postgresql.org/docs/current/plpgsql.html)                                          | Loadable procedural language for the PostgreSQL database system                                       | 1.0     |                    |                  |                                                    |
| [postgres\_fdw](https://www.postgresql.org/docs/current/postgres-fdw.html)                               | Foreign data wrapper for remote PostgreSQL servers                                                    | 1.2     | ⭐                  |                  |                                                    |
| [seg](https://www.postgresql.org/docs/current/seg.html)                                                  | Data type for representing line segments or floating-point intervals                                  | 1.4     |                    |                  |                                                    |
| [tablefunc](https://www.postgresql.org/docs/current/tablefunc.html)                                      | Functions that return tables (multiple rows)                                                          | 1.0     |                    |                  |                                                    |
| [tcn](https://www.postgresql.org/docs/current/tcn.html)                                                  | Provides a trigger function that notifies listeners of changes to any table                           | 1.0     |                    |                  |                                                    |
| [tsm\_system\_rows](https://www.postgresql.org/docs/current/tsm-system-rows.html)                        | Table sampling method SYSTEM\_ROWS which can be used in TABLESAMPLE clause                            | 1.0     |                    |                  |                                                    |
| [tsm\_system\_time](https://www.postgresql.org/docs/current/tsm-system-time.html)                        | Table sampling method SYSTEM\_TIME which can be used in TABLESAMPLE clause                            | 1.0     |                    |                  |                                                    |
| [unaccent](https://www.postgresql.org/docs/current/unaccent.html)                                        | Text search dictionary for removing accents (diacritic signs) from lexemes                            | 1.1     |                    |                  |                                                    |
| [uuid-ossp](https://www.postgresql.org/docs/current/uuid-ossp.html)                                      | Functions to generate universally unique identifiers (UUIDs)                                          | 1.1     |                    |                  |                                                    |

#### Postgres 17.5

| Extension                                                                                                | Description                                                                                           | Version | Superuser required | Restart required | Additional Notes                                   |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------- | ------------------ | ---------------- | -------------------------------------------------- |
| [autoinc](https://www.postgresql.org/docs/current/contrib-spi.html#CONTRIB-SPI-AUTOINC)                  | Functions for autoincrementing fields                                                                 | 1.0     | ⭐                  |                  |                                                    |
| [bloom](https://www.postgresql.org/docs/current/bloom.html)                                              | Bloom filter index access method                                                                      | 1.0     | ⭐                  |                  |                                                    |
| [btree\_gin](https://www.postgresql.org/docs/current/btree-gin.html)                                     | Provides GIN operator classes that implement B-tree equivalent behavior for various data types        | 1.3     |                    |                  |                                                    |
| [btree\_gist](https://www.postgresql.org/docs/current/btree-gist.html)                                   | Provides GiST index operator classes that implement B-tree equivalent behavior                        | 1.7     |                    |                  |                                                    |
| [citext](https://www.postgresql.org/docs/current/citext.html)                                            | Provides case-insensitive character string type                                                       | 1.6     |                    |                  |                                                    |
| [cube](https://www.postgresql.org/docs/current/cube.html)                                                | Data type for representing multidimensional cubes                                                     | 1.5     |                    |                  |                                                    |
| [dict\_int](https://www.postgresql.org/docs/current/dict-int.html)                                       | Text search dictionary template for integers                                                          | 1.0     |                    |                  |                                                    |
| [dict\_xsyn](https://www.postgresql.org/docs/current/dict-xsyn.html)                                     | Text search dictionary for extended synonym processing                                                | 1.0     | ⭐                  |                  |                                                    |
| [earthdistance](https://www.postgresql.org/docs/current/earthdistance.html)                              | Calculate great circle distances on the surface of the Earth                                          | 1.2     | ⭐                  |                  |                                                    |
| [fuzzystrmatch](https://www.postgresql.org/docs/current/fuzzystrmatch.html)                              | Functions for determining similarities and distance between strings                                   | 1.2     |                    |                  |                                                    |
| [hstore](https://www.postgresql.org/docs/current/hstore.html)                                            | Data type for storing sets of key/value pairs within a single PostgreSQL value                        | 1.8     |                    |                  |                                                    |
| [insert\_username](https://www.postgresql.org/docs/current/contrib-spi.html#CONTRIB-SPI-INSERT-USERNAME) | Functions for tracking who changed a table                                                            | 1.0     | ⭐                  |                  |                                                    |
| [intagg](https://www.postgresql.org/docs/current/intagg.html)                                            | Integer aggregator and enumerator (deprecated)                                                        | 1.1     | ⭐                  |                  |                                                    |
| [intarray](https://www.postgresql.org/docs/current/intarray.html)                                        | Functions and operators for manipulating null-free arrays of integers                                 | 1.5     |                    |                  |                                                    |
| [isn](https://www.postgresql.org/docs/current/isn.html)                                                  | Data types for international product numbering standards                                              | 1.2     |                    |                  |                                                    |
| [lo](https://www.postgresql.org/docs/current/lo.html)                                                    | Support for managing Large Objects (also called BLOBs)                                                | 1.1     |                    |                  |                                                    |
| [ltree](https://www.postgresql.org/docs/current/ltree.html)                                              | Data type for representing labels of data stored in hierarchical tree-like structures                 | 1.3     |                    |                  |                                                    |
| [moddatetime](https://www.postgresql.org/docs/current/contrib-spi.html#CONTRIB-SPI-MODDATETIME)          | Functions for tracking last modification time                                                         | 1.0     | ⭐                  |                  |                                                    |
| [pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html)                    | Provides a means for tracking planning and execution statistics of all SQL statements                 | 1.11    | ⭐                  | ✅                | [📝](/docs/postgres/extensions/pg_stat_statements) |
| [pg\_trgm](https://www.postgresql.org/docs/current/pgtrgm.html)                                          | Functions and operators for determining the similarity of alphanumeric text based on trigram matching | 1.6     |                    |                  |                                                    |
| [pgcrypto](https://www.postgresql.org/docs/current/pgcrypto.html)                                        | Cryptographic functions for PostgreSQL                                                                | 1.3     |                    |                  |                                                    |
| [pgrowlocks](https://www.postgresql.org/docs/current/pgrowlocks.html)                                    | Show row-level locking information                                                                    | 1.2     | ⭐                  |                  |                                                    |
| [pgstattuple](https://www.postgresql.org/docs/current/pgstattuple.html)                                  | Obtain tuple-level statistics                                                                         | 1.5     | ⭐                  |                  |                                                    |
| [plpgsql](https://www.postgresql.org/docs/current/plpgsql.html)                                          | Loadable procedural language for the PostgreSQL database system                                       | 1.0     |                    |                  |                                                    |
| [postgres\_fdw](https://www.postgresql.org/docs/current/postgres-fdw.html)                               | Foreign data wrapper for remote PostgreSQL servers                                                    | 1.1     | ⭐                  |                  |                                                    |
| [seg](https://www.postgresql.org/docs/current/seg.html)                                                  | Data type for representing line segments or floating-point intervals                                  | 1.4     |                    |                  |                                                    |
| [tablefunc](https://www.postgresql.org/docs/current/tablefunc.html)                                      | Functions that return tables (multiple rows)                                                          | 1.0     |                    |                  |                                                    |
| [tcn](https://www.postgresql.org/docs/current/tcn.html)                                                  | Provides a trigger function that notifies listeners of changes to any table                           | 1.0     |                    |                  |                                                    |
| [tsm\_system\_rows](https://www.postgresql.org/docs/current/tsm-system-rows.html)                        | Table sampling method SYSTEM\_ROWS which can be used in TABLESAMPLE clause                            | 1.0     |                    |                  |                                                    |
| [tsm\_system\_time](https://www.postgresql.org/docs/current/tsm-system-time.html)                        | Table sampling method SYSTEM\_TIME which can be used in TABLESAMPLE clause                            | 1.0     |                    |                  |                                                    |
| [unaccent](https://www.postgresql.org/docs/current/unaccent.html)                                        | Text search dictionary for removing accents (diacritic signs) from lexemes                            | 1.1     |                    |                  |                                                    |
| [uuid-ossp](https://www.postgresql.org/docs/current/uuid-ossp.html)                                      | Functions to generate universally unique identifiers (UUIDs)                                          | 1.1     |                    |                  |                                                    |

### Supported Community Extensions

#### Postgres 18.1

| Extension                                                                                               | Description                                                                                                                                                                                              | Version | Superuser required | Restart required | Additional Notes                               |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------ | ---------------- | ---------------------------------------------- |
| [address\_standardizer](https://postgis.net/docs/manual-3.5/Extras.html#Address_Standardizer)           | Used to parse an address into constituent elements. Generally used to support geocoding address normalization step. (Part of PostGIS)                                                                    | 3.6.1   | ⭐                  |                  |                                                |
| [address\_standardizer\_data\_us](https://postgis.net/docs/manual-3.5/Extras.html#Address_Standardizer) | Address Standardizer US dataset example. (Part of PostGIS)                                                                                                                                               | 3.6.1   | ⭐                  |                  |                                                |
| [hypopg](https://github.com/HypoPG/hypopg) (installed by default)                                       | Hypothetical indexes - allows testing the impact of indexes without actually creating them                                                                                                               | 1.4.2   |                    |                  |                                                |
| [pg\_cron](https://github.com/citusdata/pg_cron)                                                        | Simple cron-based job scheduler for PostgreSQL that allows you to run SQL commands on a schedule                                                                                                         | 1.6.7   | ⭐                  | ✅                | [📝](/docs/postgres/extensions/pg_cron)        |
| [pg\_duckdb](https://github.com/duckdb/pg_duckdb)                                                       | Embeds DuckDB's analytical database engine directly into PostgreSQL for high-performance analytical queries                                                                                              | 1.1.0   | ⭐                  | ✅                | [📝](/docs/postgres/extensions/pg_duckdb)      |
| [pg\_hint\_plan](https://github.com/ossc-db/pg_hint_plan)                                               | Provides query plan hints to control the PostgreSQL planner                                                                                                                                              | 1.8.0   | ⭐                  | ✅                | [📝](/docs/postgres/extensions/pg_hint_plan)   |
| [pg\_partman](https://github.com/pgpartman/pg_partman)                                                  | Extension to create and manage both time-based and serial-based table partition sets                                                                                                                     | 5.3.1   |                    |                  |                                                |
| [pg\_partman\_bgw](https://github.com/pgpartman/pg_partman)                                             | Background worker to automatically run partition maintenance for pg\_partman                                                                                                                             | 5.3.1   |                    | ✅                | [📝](/docs/postgres/extensions/pg_partman_bgw) |
| [pg\_squeeze](https://github.com/cybertec-postgresql/pg_squeeze/)                                       | Automatically cleans up unused space in tables (table bloat)                                                                                                                                             | 1.9.1   | ⭐                  | ✅                | [📝](/docs/postgres/extensions/pg_squeeze)     |
| [pgvector](https://github.com/pgvector/pgvector)                                                        | Open-source vector similarity search for PostgreSQL, designed for AI/ML applications                                                                                                                     | 0.8.1   | ⭐                  |                  |                                                |
| [postgis](https://postgis.net/)                                                                         | PostGIS extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data                                                             | 3.6.1   | ⭐                  |                  |                                                |
| [postgis\_sfcgal](https://postgis.net/docs/manual-3.5/reference_sfcgal.html)                            | SFCGAL is a C++ wrapper library around CGAL that provides advanced 2D and 3D spatial functions                                                                                                           | 3.6.1   | ⭐                  |                  |                                                |
| [postgis\_tiger\_geocoder](https://postgis.net/docs/manual-3.5/Extras.html#Tiger_Geocoder)              | A plpgsql based geocoder written to work with the TIGER (Topologically Integrated Geographic Encoding and Referencing system) / Line and Master Address database export released by the US Census Bureau | 3.6.1   |                    |                  |                                                |
| [postgis\_topology](https://postgis.net/docs/manual-3.5/Topology.html)                                  | The PostGIS Topology types and functions are used to manage topological objects such as faces, edges and nodes                                                                                           | 3.6.1   | ⭐                  |                  |                                                |
| [TimescaleDB](https://github.com/timescale/timescaledb)                                                 | A time-series database for high-performance real-time analytics packaged as a Postgres extension ([Apache 2 Edition](https://docs.tigerdata.com/about/latest/timescaledb-editions/))                     | 2.23.1  |                    | ✅                | [📝](/docs/postgres/extensions/timescaledb)    |

#### Postgres 17.5

| Extension                                                                                               | Description                                                                                                                                                                                              | Version | Superuser required | Restart required | Additional Notes                               |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------ | ---------------- | ---------------------------------------------- |
| [address\_standardizer](https://postgis.net/docs/manual-3.5/Extras.html#Address_Standardizer)           | Used to parse an address into constituent elements. Generally used to support geocoding address normalization step. (Part of PostGIS)                                                                    | 3.5.3   | ⭐                  |                  |                                                |
| [address\_standardizer\_data\_us](https://postgis.net/docs/manual-3.5/Extras.html#Address_Standardizer) | Address Standardizer US dataset example. (Part of PostGIS)                                                                                                                                               | 3.5.3   | ⭐                  |                  |                                                |
| [hypopg](https://github.com/HypoPG/hypopg) (installed by default)                                       | Hypothetical indexes - allows testing the impact of indexes without actually creating them                                                                                                               | 1.4.2   |                    |                  |                                                |
| [pg\_cron](https://github.com/citusdata/pg_cron)                                                        | Simple cron-based job scheduler for PostgreSQL that allows you to run SQL commands on a schedule                                                                                                         | 1.6.5   | ⭐                  | ✅                | [📝](/docs/postgres/extensions/pg_cron)        |
| [pg\_duckdb](https://github.com/duckdb/pg_duckdb)                                                       | Embeds DuckDB's analytical database engine directly into PostgreSQL for high-performance analytical queries                                                                                              | 1.0.0   | ⭐                  | ✅                | [📝](/docs/postgres/extensions/pg_duckdb)      |
| [pg\_hint\_plan](https://github.com/ossc-db/pg_hint_plan)                                               | Provides query plan hints to control the PostgreSQL planner                                                                                                                                              | 1.7.0   | ⭐                  | ✅                | [📝](/docs/postgres/extensions/pg_hint_plan)   |
| [pg\_partman](https://github.com/pgpartman/pg_partman)                                                  | Extension to create and manage both time-based and serial-based table partition sets                                                                                                                     | 5.2.4   |                    |                  |                                                |
| [pg\_partman\_bgw](https://github.com/pgpartman/pg_partman)                                             | Background worker to automatically run partition maintenance for pg\_partman                                                                                                                             | 5.2.4   |                    | ✅                | [📝](/docs/postgres/extensions/pg_partman_bgw) |
| [pg\_squeeze](https://github.com/cybertec-postgresql/pg_squeeze/)                                       | Automatically cleans up unused space in tables (table bloat)                                                                                                                                             | 1.9.0   | ⭐                  | ✅                | [📝](/docs/postgres/extensions/pg_squeeze)     |
| [pgvector](https://github.com/pgvector/pgvector)                                                        | Open-source vector similarity search for PostgreSQL, designed for AI/ML applications                                                                                                                     | 0.8.0   | ⭐                  |                  |                                                |
| [postgis](https://postgis.net/)                                                                         | PostGIS extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data                                                             | 3.5.3   | ⭐                  |                  |                                                |
| [postgis\_sfcgal](https://postgis.net/docs/manual-3.5/reference_sfcgal.html)                            | SFCGAL is a C++ wrapper library around CGAL that provides advanced 2D and 3D spatial functions                                                                                                           | 3.5.3   | ⭐                  |                  |                                                |
| [postgis\_tiger\_geocoder](https://postgis.net/docs/manual-3.5/Extras.html#Tiger_Geocoder)              | A plpgsql based geocoder written to work with the TIGER (Topologically Integrated Geographic Encoding and Referencing system) / Line and Master Address database export released by the US Census Bureau | 3.5.3   |                    |                  |                                                |
| [postgis\_topology](https://postgis.net/docs/manual-3.5/Topology.html)                                  | The PostGIS Topology types and functions are used to manage topological objects such as faces, edges and nodes                                                                                           | 3.5.3   | ⭐                  |                  |                                                |
| [TimescaleDB](https://github.com/timescale/timescaledb)                                                 | A time-series database for high-performance real-time analytics packaged as a Postgres extension ([Apache 2 Edition](https://docs.tigerdata.com/about/latest/timescaledb-editions/))                     | 2.21.3  |                    | ✅                | [📝](/docs/postgres/extensions/timescaledb)    |

### PlanetScale Extensions

These extensions are installed by PlanetScale and cannot be disabled.

| Extension         | Description                                                           | Version | Additional Notes                           |
| ----------------- | --------------------------------------------------------------------- | ------- | ------------------------------------------ |
| pgextwlist        | PostgreSQL Extension Allowlist                                        | N/A     |                                            |
| pginsights        | PlanetScale Insights plugin                                           | N/A     | [📝](/docs/postgres/extensions/pginsights) |
| pg\_pscale\_utils | Utility extension to handle superuser actions in PlanetScale Postgres | N/A     |                                            |

## Need Additional Extensions?

If you require an extension that is not currently supported, please [reach out to support](https://planetscale.com/contact?initial=support). We regularly evaluate and add new extensions based on customer needs and security considerations.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt