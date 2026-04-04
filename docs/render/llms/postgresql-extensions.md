# Source: https://render.com/docs/postgresql-extensions.md

# Supported Extensions for Render Postgres

Render Postgres databases support most popular extensions (`pgvector`, `postgis`, and so on). Your database's PostgreSQL version determines exactly which extensions are supported, along with how you add them:

## PostgreSQL 13 and later

To enable any supported extension, run the [`CREATE EXTENSION`](https://www.postgresql.org/docs/current/sql-createextension.html) command like so:

```sql
CREATE EXTENSION postgis;
```

To run this command, you can start a psql session in your terminal. Use the *PSQL Command* provided on your database's Info page in the [Render Dashboard](https://dashboard.render.com).

Except where noted, these extensions are available for all databases running PostgreSQL 13 or later:

- [adminpack](https://www.postgresql.org/docs/current/adminpack.html)
- [amcheck](https://www.postgresql.org/docs/current/amcheck.html)
- [autoinc](https://www.postgresql.org/docs/current/contrib-spi.html)
- [bloom](https://www.postgresql.org/docs/current/bloom.html)
- [btree_gin](https://www.postgresql.org/docs/current/btree-gin.html)
- [btree_gist](https://www.postgresql.org/docs/current/btree-gist.html)
- [citext](https://www.postgresql.org/docs/current/citext.html)
- [cube](https://www.postgresql.org/docs/current/cube.html)
- [dblink](https://www.postgresql.org/docs/current/dblink.html)
- [dict_int](https://www.postgresql.org/docs/current/dict-int.html)
- [dict_xsyn](https://www.postgresql.org/docs/current/dict-xsyn.html)
- [earthdistance](https://www.postgresql.org/docs/current/earthdistance.html)
- [file_fdw](https://www.postgresql.org/docs/current/file-fdw.html)
- [fuzzystrmatch](https://www.postgresql.org/docs/current/fuzzystrmatch.html)
- [hstore](https://www.postgresql.org/docs/current/hstore.html)
- [insert_username](https://www.postgresql.org/docs/current/contrib-spi.html)
- [intagg](https://www.postgresql.org/docs/current/intagg.html)
- [intarray](https://www.postgresql.org/docs/current/intarray.html)
- [isn](https://www.postgresql.org/docs/current/isn.html)
- [lo](https://www.postgresql.org/docs/current/lo.html)
- [ltree](https://www.postgresql.org/docs/current/ltree.html)
- [moddatetime](https://www.postgresql.org/docs/current/contrib-spi.html)
- [old_snapshot](https://www.postgresql.org/docs/current/oldsnapshot.html)\*
  - \*Requires PostgreSQL 14 or later.
- [pageinspect](https://www.postgresql.org/docs/current/pageinspect.html)
- [pg_buffercache](https://www.postgresql.org/docs/current/pgbuffercache.html)
- [pg_duckdb](https://github.com/duckdb/pg_duckdb)\*
  - \*Requires PostgreSQL 16 or later. Database must have been created after 30 January 2025.
- [pg_freespacemap](https://www.postgresql.org/docs/current/pgfreespacemap.html)
- [pg_ivm](https://github.com/sraoss/pg_ivm)
- [pg_prewarm](https://www.postgresql.org/docs/current/pgprewarm.html)
- [pg_similarity](https://github.com/eulerto/pg_similarity)\*
  - \*This extension is currently not available for PostgreSQL 16 or later.
- [pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html)
- [pg_surgery](https://www.postgresql.org/docs/current/pgsurgery.html)\*
  - \*Requires PostgreSQL 14 or later.
- [pg_trgm](https://www.postgresql.org/docs/current/pgtrgm.html)
- [pg_visibility](https://www.postgresql.org/docs/current/pgvisibility.html)
- [pgaudit](https://www.pgaudit.org/)
- [pgcrypto](https://www.postgresql.org/docs/current/pgcrypto.html)
- [pgrowlocks](https://www.postgresql.org/docs/current/pgrowlocks.html)
- [pgstattuple](https://www.postgresql.org/docs/current/pgstattuple.html)
- [pgvector](https://github.com/pgvector/pgvector)\*
  - \*Enable this extension with `CREATE EXTENSION vector;`
- [plpgsql](https://www.postgresql.org/docs/current/plpgsql.html)\*
  - \*This extension is enabled by default.
- [postgis](https://postgis.net)
- [postgis_raster](https://trac.osgeo.org/postgis/wiki/WKTRaster)
- [postgis_tiger_geocoder](https://postgis.net/docs/Extras.html#Tiger_Geocoder)
- [postgis_topology](https://postgis.net/docs/Topology.html)
- [refint](https://www.postgresql.org/docs/current/contrib-spi.html)
- [seg](https://www.postgresql.org/docs/current/seg.html)
- [sslinfo](https://www.postgresql.org/docs/current/sslinfo.html)
- [tablefunc](https://www.postgresql.org/docs/current/tablefunc.html)
- [tcn](https://www.postgresql.org/docs/current/tcn.html)
- [timescaledb](https://www.timescale.com/)\*
  - \*Database must have been created after 12 January 2023. [Community features](https://docs.timescale.com/about/latest/timescaledb-editions/#feature-comparison) are not available.
- [tsm_system_rows](https://www.postgresql.org/docs/current/tsm-system-rows.html)
- [tsm_system_time](https://www.postgresql.org/docs/current/tsm-system-time.html)
- [unaccent](https://www.postgresql.org/docs/current/unaccent.html)
- [uuid-ossp](https://www.postgresql.org/docs/current/uuid-ossp.html)
- [xml2](https://www.postgresql.org/docs/current/xml2.html)

## PostgreSQL 11 and 12

On Render Postgres databases running PostgreSQL 11 or 12, *supported extensions are enabled by default and cannot be customized.* These extensions are enabled for all PostgreSQL 11 and 12 databases:

> Some of these extensions (like `postgis`) create additional schemas (like `topology`) and tables (like `spatial_ref_sys`).

- [bloom](https://www.postgresql.org/docs/12/bloom.html)
- [btree_gin](https://www.postgresql.org/docs/12/btree-gin.html)
- [btree_gist](https://www.postgresql.org/docs/12/btree-gist.html)
- [citext](https://www.postgresql.org/docs/12/citext.html)
- [cube](https://www.postgresql.org/docs/12/cube.html)
- [dblink](https://www.postgresql.org/docs/12/dblink.html)
- [dict_int](https://www.postgresql.org/docs/12/dict-int.html)
- [dict_xsyn](https://www.postgresql.org/docs/12/dict-xsyn.html)
- [earthdistance](https://www.postgresql.org/docs/12/earthdistance.html)
- [fuzzystrmatch](https://www.postgresql.org/docs/12/fuzzystrmatch.html)
- [hstore](https://www.postgresql.org/docs/12/hstore.html)
- [intagg](https://www.postgresql.org/docs/12/intagg.html)
- [intarray](https://www.postgresql.org/docs/12/intarray.html)
- [isn](https://www.postgresql.org/docs/12/isn.html)
- [lo](https://www.postgresql.org/docs/12/lo.html)
- [ltree](https://www.postgresql.org/docs/12/ltree.html)
- [pg_buffercache](https://www.postgresql.org/docs/12/pgbuffercache.html)
- [pg_prewarm](https://www.postgresql.org/docs/12/pgprewarm.html)
- [pg_stat_statements](https://www.postgresql.org/docs/12/pgstatstatements.html)
- [pg_trgm](https://www.postgresql.org/docs/12/pgtrgm.html)
- [pgcrypto](https://www.postgresql.org/docs/12/pgcrypto.html)
- [pgrowlocks](https://www.postgresql.org/docs/12/pgrowlocks.html)
- [pgstattuple](https://www.postgresql.org/docs/12/pgstattuple.html)
- [pgvector](https://github.com/pgvector/pgvector)
  - \*Database must have been created or received maintenance after 11 April 2024. Contact support for assistance.
- [postgis](https://postgis.net)
  - Not available on the Starter instance type for PostgreSQL 12, due to resource requirements.
- [postgis_tiger_geocoder](https://postgis.net/docs/Extras.html#Tiger_Geocoder)
- [postgis_topology](https://postgis.net/docs/Topology.html)
- [tablefunc](https://www.postgresql.org/docs/12/tablefunc.html)
- [unaccent](https://www.postgresql.org/docs/12/unaccent.html)
- [uuid-ossp](https://www.postgresql.org/docs/12/uuid-ossp.html)

### Removing extensions

If you don't need some of these extensions and want to remove them from your PostgreSQL 11 or 12 database, [email support](mailto:support@render.com) and we'll be happy to delete them for you.