# Source: https://planetscale.com/docs/postgres/cluster-configuration/versions.md

# Supported versions

> When creating a PlanetScale Postgres cluster, you can choose from any of the Postgres versions we support.

PlanetScale Postgres supports versions 17 and 18 of Postgres.

Specifically, the following versions are currently supported:

* 17.5
* 18.1

New databases will be created using the latest version by default and we recommend sticking to that default, but you can choose an older version if you need to.

## Major version upgrades

PlanetScale doesn't currently offer in-place upgrades between major versions of Postgres. To upgrade from Postgres 17 to 18, create a new PostgreSQL 18 database and perform an online migration from your existing PlanetScale Postgres 17 database using our [import guides](/docs/postgres/imports/postgres-imports).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt