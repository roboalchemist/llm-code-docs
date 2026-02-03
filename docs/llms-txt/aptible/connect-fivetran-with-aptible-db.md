# Source: https://www.aptible.com/docs/how-to-guides/database-guides/connect-fivetran-with-aptible-db.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to connect Fivetran with your Aptible databases

> Learn how to connect Fivetran with your Aptible Databases

## Overview

[Fivetran](https://www.fivetran.com/) is a cloud-based platform that automates data movement, allowing easy extraction, loading, and transformation of data between various sources and destinations. Fivetran is compatible with Aptible Postgres and MySQL databases.

## Connecting with PostgreSQL Databases

> ⚠️ Prerequisites: A Fivetran account with the role to Create Destinations

To connect your existing Aptible [PostgreSQL](/core-concepts/managed-databases/supported-databases/postgresql) Database to Fivetran:

**Step 1: Configure Fivetran**

Follow Fivetran’s [General PostgreSQL Guide](https://fivetran.com/docs/databases/postgresql/setup-guide), noting the following:

* The only supported “Connection method” is to Connect Directly

* `pgoutput` is the preferred method. All PostgreSQL databases version 10+ have this as the default logical replication plugin.

* The `wal_level` and `max_replication_slots` settings will already be present on your Aptible PostgreSQL database

  * Note: The default `max_replication_slots` is 10. You may need to increase this if you have many Aptible replicas or 3rd party replication using the allotted replication slots.

* The step to add a record to `pg_hba.conf` file can be skipped, as the settings Aptible sets for you are sufficient to allow a connection/authentication.

* Aptible PostgreSQL databases use the default value for `wal_sender_timeout` , so you’ll likely have to run `ALTER SYSTEM SET wal_sender_timeout 0;` or something similar, see related guide: [How to configure Aptible PostgreSQL Databases](/how-to-guides/database-guides/configure-aptible-postgresql-databases)

**Step 2: Expose your database to Fivetram**

You’ll need to expose the PostgreSQL Database to your Fivetran instance:

* If you're running it as an Aptible App in the same Stack then it can access it by default.

* Otherwise, create a [Database Endpoint](/core-concepts/managed-databases/connecting-databases/database-endpoints). Be sure to only allow [Fivetran's IP addresses](https://fivetran.com/docs/getting-started/ips) to connect!

## Connecting with MySQL Databases

> ⚠️ Prerequisites: A Fivetran account with the role to Create Destinations

To connect your existing Aptible [MySQL](/core-concepts/managed-databases/supported-databases/mysql) Database to Fivetran:

**Step 1: Configure Fivetran** Follow Fivetran’s [General MySQL Guide](https://fivetran.com/docs/destinations/mysql/setup-guide), noting the following:

* The only supported “Connection method” is to Connect Directly

**Step 2: Expose your database to Fivetram**

You’ll need to expose the PostgreSQL Database to your Fivetran instance:

* If you're running it as an Aptible App in the same Stack then it can access it by default.

* Otherwise, create a [Database Endpoint](/core-concepts/managed-databases/connecting-databases/database-endpoints). Be sure to only allow [Fivetran's IP addresses](https://fivetran.com/docs/getting-started/ips) to connect!

## Troubleshooting

* Fivetran replication queries can return a large amount of data per query. Fivetran support can tune down page size per query to smaller sizes, and this has resulted in positive results as a troubleshooting step.

* Very large Text / BLOB columns can have a potential impact on the Fivetran replication process. Customers have had success unblocking Fivetran replication by removing large Text / BLOB columns from the target Fivetran schema.
