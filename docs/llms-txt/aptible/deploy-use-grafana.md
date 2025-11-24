# Source: https://www.aptible.com/docs/how-to-guides/observability-guides/deploy-use-grafana.md

# How to deploy and use Grafana

> Learn how to deploy and use Aptible-hosted analytics and monitoring with Grafana

## Overview

[Grafana](https://grafana.com/) is an open-source platform for analytics and monitoring. It's an ideal choice to use in combination with an [InfluxDB metric drain.](/core-concepts/observability/metrics/metrics-drains/influxdb-metric-drain) Grafan is useful in a number of ways:

* It makes it easy to build beautiful graphs and set up alerts.

* It works out of the box with InfluxDB.

* It works very well in a containerized environment like Aptible.

## Set up

### Deploying with Terraform

The **easiest and recommended way** to set up Grafana on Aptible is using the [Aptible Metrics Terraform Module](https://registry.terraform.io/modules/aptible/metrics/aptible/latest). This provisions Aptible metric drains with pre-built Grafana dashboards and alerts for monitoring RAM and CPU usage for your Aptible apps and databases. This simplifies the setup of metric drains so you can start monitoring your Aptible resources immediately, all hosted within your Aptible account. If you would rather set it up from scratch, use this guide.

### Deploying via the CLI

#### Step 1: Provision a PostgreSQL database

Grafana needs a Database to store sessions and Dashboard definitions. It works great with [PostgreSQL](/core-concepts/managed-databases/supported-databases/postgresql), which you can deploy on Aptible.

#### Step 2: Configure the database

Once you have created the PostgreSQL Database, create a tunnel using the [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel) command, then connect using `psql` and run the following commands to create a `sessions` database for use by Grafana:

```sql  theme={null}
CREATE DATABASE sessions;
```

Then, connect to the newly-created `sessions` database:

```sql  theme={null}
\c sessions;
```

And finally, create a table for Grafana to store sessions in:

```sql  theme={null}
CREATE TABLE session (
        key       CHAR(16) NOT NULL,
        data      BYTEA,
        expiry    INTEGER NOT NULL,
        PRIMARY KEY (key)
);
```

#### Step 3: Deploy the Grafana app

Grafana is available as a Docker image and can be configured using environment variables. As a result, you can use [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) to easily deploy Grafana on Aptible.

Here is the minimal deployment configuration to get you started. In the example below, you'll have to substitute a number of variables:

* `$ADMIN_PASSWORD`: Generate a strong password for your Grafana `admin` user.

* `$SECRET_KEY`: Generate a random string (40 characters will do).

* `$YOUR_DOMAIN`: The domain name you intend to use to connect to Grafana (e.g. `grafana.example.com`).

* `$DB_USERNAME`: The username for your PostgreSQL database. For a PostgreSQL database on Aptible, this will be `aptible`.

* `$DB_PASSWORD`: The password for your PostgreSQL database.

* `$DB_HOST`: The host for your PostgreSQL database.

* `$DB_PORT`: The port for your PostgreSQL database.

```sql  theme={null}
aptible apps:create grafana

aptible deploy --app grafana --docker-image grafana/grafana \
        "GF_SECURITY_ADMIN_PASSWORD=$ADMIN_PASSWORD" \
        "GF_SECURITY_SECRET_KEY=$SECRET_KEY" \
        "GF_DEFAULT_INSTANCE_NAME=aptible" \
        "GF_SERVER_ROOT_URL=https://$YOUR_DOMAIN" \
        "GF_SESSION_PROVIDER=postgres" \
        "GF_SESSION_PROVIDER_CONFIG=user=$DB_USERNAME password=$DB_PASSWORD host=$DB_HOST port=$DB_PORT dbname=sessions sslmode=require" \
        "GF_LOG_MODE=console" \
        "GF_DATABASE_TYPE=postgres" \
        "GF_DATABASE_HOST=$DB_HOST:$DB_PORT" \
        "GF_DATABASE_NAME=db" \
        "GF_DATABASE_USER=$DB_USERNAME" \
        "GF_DATABASE_PASSWORD=$DB_PASSWORD" \
        "GF_DATABASE_SSL_MODE=require" \
        "FORCE_SSL=true"
```

> 📘 There are many more configuration options available in Grafana. Review [Grafana's configuration documentation](http://docs.grafana.org/installation/configuration/) for more information.

#### Step 4: Expose Grafana

Finally, follow the [How do I expose my web app on the Internet?](/how-to-guides/app-guides/expose-web-app-to-internet) tutorial to expose your Grafana app over the internet. Make sure to use the same domain you configured Grafana with (`$YOUR_DOMAIN` in the example above)!

## Using Grafana

#### Step 1: Log in

Once you've exposed Grafana, you can navigate to `$YOUR_DOMAIN` to access Grafana. Connect using the username `admin` and the password you configured above (`ADMIN_PASSWORD`).

#### Step 2: Connect to an InfluxDB Database

Once logged in to Grafana, you can connect Grafana to an [InfluxDB](/core-concepts/managed-databases/supported-databases/influxdb) database by creating a new data source. To do so, click the Grafana icon in the top left, then navigate to data sources and click "Add data source".

The following assumes you have provisioned an InfluxDB database. You'll need to interpolate the following values

* `$INFLUXDB_HOST`: The hostname for your InfluxDB database. This is of the form `db-$STACK-$ID.aptible.in`.

* `$INFLUXDB_PORT`: The port for your InfluxDB database.

* `$INFLUXDB_USERNAME`: The username for your InfluxDB database. Typically `aptible`.

* `$INFLUXDB_PASSWORD`: The password.

These parameters are represented by the connection URL for your InfluxDB database in the Aptible dashboard and CLI. For example, if your connection URL is `https://foo:bar@db-qux-123.aptible.in:456`, then the parameters are:

* `$INFLUXDB_HOST`: `db-qux-123.aptible.in`

* `$INFLUXDB_PORT`: `456`

* `$INFLUXDB_USERNAME`: `foo`

* `$INFLUXDB_PASSWORD`: `bar`

Once you have those parameters in Grafana, use the following configuration for your data source:

* **Name**: Any name of your choosing. This will be used to reference this data source in the Grafana web interface.

* **Type**: InfluxDB

* **HTTP settings**:

  * **URL**: `https://$INFLUXDB_HOST:$INFLUXDB_PORT`.

  * **Access**: `proxy`

* **HTTP Auth**: Leave everything unchecked

* **Skip TLS Verification**: Do not select

* **InfluxDB Details**: - Database: If you provisioned this InfluxDB database on Aptible and/or are using it for an [InfluxDB database](/core-concepts/managed-databases/supported-databases/influxdb) metric drain, set this to `db`. Otherwise, use the database of your choice. - User: `$INFLUXDB_USERNAME` - Password: `$INFLUXDB_PASSWORD`

Finally, save your changes.

#### Step 3: Set up Queries

Here are a few suggested queries to get started with an InfluxDB metric drain. These queries are designed with Grafana in mind. To copy those queries into Grafana, use the [raw text editor mode](http://docs.grafana.org/features/datasources/influxdb/#text-editor-mode-raw) in Grafana.

> 📘 In the queries below, `$__interval` and `$timeFilter` will automatically be interpolated by Grafana. Leave those parameters as-is.

**RSS Memory Utilization across all resources**

```sql  theme={null}
SELECT MAX("memory_rss_mb") AS rss_mb
FROM "metrics"
WHERE $timeFilter
GROUP BY
        time($__interval),
        "app", "database", "service", "host"
        fill(null)
```

**CPU Utilization for a single App**

In the example below, replace `ENVIRONMENT` with the handle for your [environment](/core-concepts/architecture/environments) and `HANDLE` with the handle for your [app](/core-concepts/apps/overview)

```sql  theme={null}
SELECT MEAN("milli_cpu_usage") / 1000 AS cpu
FROM "metrics"
WHERE
        environment = 'ENVIRONMENT' AND
        app = 'HANDLE' AND
        $timeFilter
GROUP BY
        time($__interval),
        "service", "host"
        fill(null)
```

#### Disk Utilization across all Databases

```sql  theme={null}
SELECT LAST(disk_usage_mb) / LAST(disk_limit_mb) AS utilization
FROM "metrics"
WHERE
        "database" <> '' AND
        $timeFilter
GROUP BY
        time($__interval),
        "database", "service", "host"
        fill(null)
```

## Grafana documentation

Once you've added your first data source, you might also want to consider following [Grafana's getting started documentation](http://docs.grafana.org/guides/getting_started/) to familiarize yourself with Grafana.

> 📘 If you get an error connecting, use the [`aptible logs`](/reference/aptible-cli/cli-commands/cli-logs) commands to troubleshoot.

> That said, an error logging in is very likely due to not properly creating the `sessions` database and the `session` table in it as indicated in [Configuring the database](/how-to-guides/observability-guides/deploy-use-grafana#configuring-the-database).

## Upgrading Grafana

To upgrade Grafana, deploy the desired version to your existing app containers:

```sql  theme={null}
aptible deploy --app grafana --docker-image grafana/grafana:VERSION
```

> 📘 **Doing a big upgrade?** If you need to downgrade, you can redeploy with a lower version. Alternatively, you can deploy a test Grafana app to ensure it works beforehand and deprovisioned the test app once complete.
