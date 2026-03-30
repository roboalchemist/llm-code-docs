# Source: https://render.com/docs/postgresql-creating-connecting.md

# Create and Connect to Render Postgres


> *Migrating a large database from Heroku?*
>
> The Render team can help you orchestrate your migration to minimize downtime, even for apps with multi-terabyte databases.

Render Postgres databases provide fully managed, scalable storage of relational data.

All paid Render Postgres databases provide [point-in-time recovery](postgresql-backups) and on-demand logical exports. Larger instances support [read replicas](postgresql-read-replicas) and [high availability](postgresql-high-availability) for improved performance and reliability.

## Quickstarts

Here are a few Render quickstarts that include a Render Postgres database as part of their application stack:

- [Django](/deploy-django)
- [Rails](/deploy-rails-8)
- [Phoenix](/deploy-phoenix-distillery)

## Create your database

1. Go to [dashboard.render.com/new/database](https://dashboard.render.com/new/database), or click *+ New > Postgres* in the Render Dashboard.

   This form appears:

   [image: New Postgres creation form]

2. Provide a helpful *Name* for your database.
   - You can change this value at any time.
3. Optionally fill in the *Database* and/or *User* fields if you want to set your PostgreSQL `dbname` and/or username.
   - Render generates values for either of these that you don't specify.
   - You _can't_ change these values after creating your database.
4. Choose a *Region* to run your database in.
   - Choose the same region as your services that will connect to the database. This minimizes latency and enables communication over your [private network](private-network).
5. Optionally change the *PostgreSQL Version* if you want to use an older version.
   - Major versions <oldest-supported-postgres></oldest-supported-postgres> through <latest-postgres></latest-postgres> are available for all new instances.
   - Versions 11 and 12 are available for workspaces that have at least one _existing_ database on the corresponding version.
6. Scroll down and select an *instance type* for your database. This determines its available RAM and CPU.

> [Learn about limitations of the Free instance type.](free#free-postgres)

   [image: Selecting a Postgres instance type]

   You can [change your instance type](#changing-your-instance-type) later.

7. Scroll down and set your database's initial storage, in GB.

   - You can specify 1 GB or any multiple of 5 GB.
   - You can increase your storage later, but you can't decrease it.

8. Optionally enable *Storage Autoscaling*.

   - Whenever your database is 90% full, Render automatically increases its storage by 50%, rounded up to the nearest multiple of 5 GB. You can't reduce storage after increasing it. [Learn more.](#storage-autoscaling)

9. Click *Create Database*.

You're all set! Your new database's status updates to *Available* in the Render Dashboard when it's ready to use.

## Connect to your database

Every Render Postgres database has two different URLs for incoming connections:

- An *internal URL* for connections from your other Render services hosted in the _same region_
- An *external URL* for connections from _everything else_

[diagram]

*Use the internal URL wherever possible.* It minimizes query latency by enabling communication over your [private network](private-network).

Both URLs are available from the *Connect* menu in the top-right corner of your database's page in the [Render Dashboard](https://dashboard.render.com):

[image: The Connect menu for a Render Postgres database]

How you connect to your database depends on your code: some frameworks expect a single connection string or URL in an environment variable, while others need multiple connection parameters in a configuration file. See [Quickstarts](#quickstarts) for examples.

At a minimum, your app needs to know your database's hostname, port, username, password, and database name (such as `mydb` in the [official PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial-createdb.html)).

> Render Postgres uses the default PostgreSQL port `5432`. You can usually leave this port unspecified.

### Internal connections

> To use the internal URL, your connecting service and your database must belong to the same account and [region](regions).

Wherever possible, connect to your database using its internal URL. Internal connection details are available on your database's *Info* page in the [Render Dashboard](https://dashboard.render.com):

[image: PostgreSQL private connection details in the Render Dashboard]

You can view individual details, along with the assembled internal URL (of the format `postgresql://USER:PASSWORD@INTERNAL_HOST:PORT/DATABASE`). Use whichever format your framework expects for database credentials.

### External connections

> *External URL connections are slower because they traverse the public internet.*
>
> To minimize latency, use your database's [internal URL](#internal-connections) when connecting from a Render service running in the same region.

Tools and systems outside of Render can connect to your database via its external URL, available from its *Info* page in the [Render Dashboard](https://dashboard.render.com):

[image: PostgreSQL public connection details in the Render Dashboard]

Most database clients understand the external URL, which has the format `postgresql://USER:PASSWORD@EXTERNAL_HOST:PORT/DATABASE`.

You can also run the provided *PSQL Command* directly in your terminal to start a psql session.

> If you encounter an SSL error, confirm that your PostgreSQL client supports TLS version 1.2 or higher, and that it supports any of the following cipher suites:
>
>
> *Click to show*
>
> - `TLS_AES_128_GCM_SHA256`
> - `TLS_AES_256_GCM_SHA384`
> - `TLS_CHACHA20_POLY1305_SHA256`
> - `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
> - `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`
> - `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`

### Restricting external access

By default, your Render Postgres instance is accessible from any IP address (if the connection uses valid credentials). You can modify this default behavior by restricting access to a set of IPs or even disabling external access entirely.

In the [Render Dashboard](https://dashboard.render.com), go to your database's *Info* page and scroll down to the *Networking* section:

[image: Setting PostgreSQL access control in the Render Dashboard]

You can specify IP address blocks using [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_blocks). The default block is `0.0.0.0/0`, which allows access from any IP address.

> *These rules apply only to connections that use your database's [*external URL*](#external-connections).*
>
> Your Render services in the same region as your database can always connect using your database's [internal URL](#internal-connections).

### Connection limits

Your database's maximum number of simultaneous connections depends on its instance type's total memory (RAM):

| Memory | Max Connections |
| --- | --- |
| < 8GB | 100 connections |
| 8 GB <= memory < 16 GB | 200 connections |
| 16 GB <= memory < 32 GB | 400 connections |
| \>= 32GB | 500 connections |

If you're approaching your connection limit, consider [upgrading your instance type](#changing-your-instance-type) or implementing [connection pooling](postgresql-connection-pooling).

> *Databases on a [*legacy instance type*](postgresql-legacy-instance-types) support fewer connections:*
>
>
> *View legacy instance connection limits*
>
>
> | Memory | Max Connections |
> | --- | --- |
> | \<= 6GB | 97 connections |
> | Between 6GB and 10GB | 197 connections |
> | \>= 10GB | 397 connections |
>
>
>
> You can move your database to a flexible plan by [changing its instance type](#changing-your-instance-type).

## Adding storage

You set your database's initial storage during [creation](#create-your-database). Any time after that, you can increase your database's storage to any higher multiple of 5 GB, up to 16 TB.

> *Need more than 16 TB of storage?*
>
> Please [contact support](https://dashboard.render.com?contact-support) in the Render Dashboard.

You can increase storage [automatically](#storage-autoscaling) or [manually](#increasing-storage-manually).

Note the following:

- After you increase a database's storage, you can't increase it again for 12 hours.
- It is not possible to reduce a database's storage.
- Databases on a [legacy instance type](postgresql-legacy-instance-types) have a fixed storage capacity.
  - You can move your database to a flexible plan by [changing its instance type](#changing-your-instance-type).

### Storage autoscaling

You can automatically add storage to your database whenever it's running low. With *storage autoscaling* enabled, Render detects when your database is 90% full and permanently increases its storage by 50%, rounded up to the nearest multiple of 5 GB.

Here are some example increases:

| Original Storage | New Storage |
| --- | --- |
| 1 GB | 5 GB |
| 10 GB | 15 GB |
| 25 GB | 40 GB |

Enable storage autoscaling with any of the following methods:

**Dashboard**

#### Dashboard

1. From your database's *Info* page in the [Render Dashboard](https://dashboard.render.com), scroll down to the *PostgreSQL Instance* section and click *Update*:

   [image: Update PostgreSQL storage in the Render Dashboard]

2. Scroll down to the *Enable Storage Autoscaling* field and toggle the switch.

3. Click *Save Changes*.

That's it! Render will automatically add storage to your database whenever it's 90% full.

**API**

#### API

Using the [Render API](api), you enable storage autoscaling with the [Update Postgres instance](https://api-docs.render.com/reference/update-postgres/) endpoint. In your request, set the `enableDiskAutoscaling` parameter to `true`.

### Increasing storage manually

Manually add storage to your database with any of the following methods:

**Dashboard**

#### Dashboard

1. From your database's *Info* page in the [Render Dashboard](https://dashboard.render.com), scroll down to the *PostgreSQL Instance* section and click *Update*:

   [image: Update PostgreSQL storage in the Render Dashboard]

2. Scroll down to the *Storage* field and provide a new value.

   - Provide any multiple of 5 GB greater than the current storage capacity.

3. Click *Save Changes*.

That's it! The additional storage becomes available within a minute or two.

**API**

#### API

Using the [Render API](api), you increase your database's storage capacity with the [Update Postgres instance](https://api-docs.render.com/reference/update-postgres/) endpoint. Provide the new value in the `diskSizeGB` parameter.

Provide any multiple of 5 GB greater than the current storage capacity.

### Running out of storage

*If your database exceeds its storage limit, it becomes unhealthy.* Render automatically suspends the database to prevent data loss or other unexpected behavior.

To restore your database:

1. In the [Render Dashboard](https://dashboard.render.com), scroll to the bottom of your database's *Info* page and click *Resume Database*.

2. Wait a minute or two for the database to finish resuming.

3. Follow the steps to [manually add storage capacity](#increasing-storage-manually).
   - If you wait too long after resuming, Render will suspend your database again. In this case, return to step 1.

Your database will become healthy within a few minutes.

## Changing your instance type

You can change your Render Postgres database's instance type, which determines its available RAM and CPU. [View available instance types.](/pricing#postgresql)

> *Your database will be unavailable temporarily during the change.*
>
> - With [high availability](postgresql-high-availability) enabled, your database is unavailable for only a few seconds.
> - Otherwise, it's unavailable for a few minutes.
>
> Schedule your change during off hours to minimize user impact.

1. From your database's *Info* page in the [Render Dashboard](https://dashboard.render.com), scroll down to the *PostgreSQL Instance* section and click *Update*:

   [image: Update Postgres instance type in the Render Dashboard]

2. Under *Plan Options*, select a new *Instance Type*.

   - If your database currently uses a [legacy instance type](postgresql-legacy-instance-types), you won't be able to move _back_ to a legacy instance type after changing.

3. Click *Save Changes*.

That's it! Your new instance will be available within a few minutes.

## Adding multiple databases to a single instance

You can create additional databases in your Render Postgres instance with the following steps:

1. In your terminal, open a psql session to your instance using the *PSQL Command* provided in the [Render Dashboard](https://dashboard.render.com):

   [image: Postgres public connection details in the Render Dashboard]

2. Run `CREATE DATABASE <name>`, providing the name for your new database.

You're all set! Use your instance's same internal and external URLs to connect, except substitute your new database's name as the final component:

```
postgresql://USER:PASSWORD@INTERNAL_HOST:PORT/DATABASE
```

## Encryption

Render Postgres databases are encrypted at rest using AES-256 data encryption. This encryption applies to both primary and replica instances, along with all backups. [External connections](#external-connections) to your database are encrypted in transit using Render-managed TLS certificates.

## Metrics and logs

### Dashboard

View a variety of metrics for your database (disk usage, active connections, etc.) from its *Metrics* page in the [Render Dashboard](https://dashboard.render.com):

[image: Postgres metrics in the Render Dashboard]

For details, see [Service Metrics](service-metrics#available-metrics).

### Datadog

The Datadog integration provides additional metrics related to your PostgreSQL instance's host and disk. You can also use the Datadog UI to create dashboards and alerts for your database.

For details, see the [Datadog integration docs](datadog#setting-up-postgres-monitoring).

### Viewing slow query logs

Queries that take longer than 2 seconds are logged with a line that starts with `duration:` followed by the SQL statement. Here's an example:

[image: Postgres slow query log]

## Deleting your database

> *Render does not retain backups or snapshots of a deleted database instance!*
>
> Make sure to download any necessary backups before deleting your database.

You can delete a database instance in the [Render Dashboard](https://dashboard.render.com). Scroll down to the bottom of your database's *Info* page and click *Delete Database*.

## Additional topics

See articles on the following:

- [Recovery and backups](postgresql-backups)
- [Read replicas](postgresql-read-replicas)
- [High availability](postgresql-high-availability)
- [Upgrading your PostgreSQL version](postgresql-upgrading)
- [Connection pooling](postgresql-connection-pooling)
- [Render Postgres extensions](postgresql-extensions)
- [Performance troubleshooting](postgresql-performance-troubleshooting)

---

##### Appendix: Glossary definitions

###### region

Each Render service runs in one of the following regions: *Oregon*, *Ohio*, *Virginia*, *Frankfurt*, or *Singapore*.

Services in the same region can communicate over their *private network*.

Related article: https://render.com/docs/regions.md