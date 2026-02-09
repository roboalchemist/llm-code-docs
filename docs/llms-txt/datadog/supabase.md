# Source: https://docs.datadoghq.com/database_monitoring/setup_postgres/supabase.md

---
title: Setting Up Database Monitoring for Supabase
description: Install and configure Database Monitoring for Supabase.
breadcrumbs: >-
  Docs > Database Monitoring > Setting up Postgres > Setting Up Database
  Monitoring for Supabase
---

# Setting Up Database Monitoring for Supabase

Database Monitoring provides deep visibility into your Supabase databases by exposing query metrics, query samples, explain plans, database states, failovers, and events.

The Agent collects telemetry directly from the database by logging in as a read-only user. Do the following setup to enable Database Monitoring with your Supabase database:

1. Grant the Agent access to the database
1. Install the Agent

## Before you begin{% #before-you-begin %}

{% dl %}

{% dt %}
Supported PostgreSQL versions
{% /dt %}

{% dd %}
9.6, 10, 11, 12, 13, 14, 15, 16, 17
{% /dd %}

{% dt %}
Supported Agent versions
{% /dt %}

{% dd %}
7.69.1+
{% /dd %}

{% dt %}
Performance impact
{% /dt %}

{% dd %}
The default Agent configuration for Database Monitoring is conservative, but you can adjust settings such as the collection interval and query sampling rate to better suit your needs. For most workloads, the Agent represents less than one percent of query execution time on the database and less than one percent of CPU.Database Monitoring runs as an integration on top of the base Agent ([see benchmarks](https://docs.datadoghq.com/database_monitoring/agent_integration_overhead/?tab=postgres)).
{% /dd %}

{% dt %}
Proxies, load balancers, and connection poolers
{% /dt %}

{% dd %}
The Datadog Agent must connect directly to the host being monitored. For self-hosted databases, `127.0.0.1` or the socket is preferred. The Agent should not connect to the database through a proxy, load balancer, or connection pooler such as Supabase's Dedicated Pooler (pgbouncer) or Session Pooler (Supavisor). If the Agent connects to different hosts while it is running (as in the case of failover, load balancing, and so on), the Agent calculates the difference in statistics between two hosts, producing inaccurate metrics.
{% /dd %}

{% dt %}
Data security considerations
{% /dt %}

{% dd %}
See [Sensitive information](https://docs.datadoghq.com/database_monitoring/data_collected/#sensitive-information) for information about what data the Agent collects from your databases and how to ensure it is secure.
{% /dd %}

{% /dl %}

## Grant the Agent access{% #grant-the-agent-access %}

The Datadog Agent requires read-only access to the database server in order to collect statistics and queries.

The following SQL commands should be executed on the **primary** database server (the writer) in the cluster if Supabase is replicated. Choose a Supabase database on the database server for the Agent to connect to. The Agent can collect telemetry from all databases on the database server regardless of which one it connects to, so a good option is to use the default `postgres` database. Choose a different database only if you need the Agent to run [custom queries against data unique to that database](https://docs.datadoghq.com/integrations/faq/postgres-custom-metric-collection-explained/).

Connect to the chosen database as a superuser (or another user with sufficient permissions). For example, if your chosen database is `postgres`, connect as the `postgres` user.

Navigate to the SQL Editor tab inside Supabase and run:

```SQL
CREATE USER datadog WITH password '<PASSWORD>';
```

{% tab title="Postgres â¥ 15" %}
Give the `datadog` user permission to relevant tables:

```SQL
ALTER ROLE datadog INHERIT;
```

Create the following schema **in every database**:

```SQL
CREATE SCHEMA datadog;
GRANT USAGE ON SCHEMA datadog TO datadog;
GRANT USAGE ON SCHEMA public TO datadog;
GRANT USAGE ON SCHEMA extensions TO datadog;
GRANT pg_monitor TO datadog;
```

In addition, ensure that the `pg_stat_statements` extension is enabled for your project in Supabase.```
{% /tab %}

{% tab title="Postgres â¥ 10" %}
Create the following schema **in every database**:

```SQL
CREATE SCHEMA datadog;
GRANT USAGE ON SCHEMA datadog TO datadog;
GRANT USAGE ON SCHEMA public TO datadog;
GRANT USAGE ON SCHEMA extensions TO datadog;
GRANT pg_monitor TO datadog;
```

In addition, ensure that the `pg_stat_statements` extension is enabled for your project in Supabase.```
{% /tab %}

{% alert level="info" %}
For data collection or custom metrics that require querying additional tables, you may need to grant the `SELECT` permission on those tables to the `datadog` user. Example: `grant SELECT on <TABLE_NAME> to datadog;`. See [PostgreSQL custom metric collection](https://docs.datadoghq.com/integrations/faq/postgres-custom-metric-collection-explained/) for more information.
{% /alert %}

Create the following function **in every database** to enable the Agent to collect explain plans.

```SQL
CREATE OR REPLACE FUNCTION datadog.explain_statement(
   l_query TEXT,
   OUT explain JSON
)
RETURNS SETOF JSON AS
$$
DECLARE
curs REFCURSOR;
plan JSON;

BEGIN
   OPEN curs FOR EXECUTE pg_catalog.concat('EXPLAIN (FORMAT JSON) ', l_query);
   FETCH curs INTO plan;
   CLOSE curs;
   RETURN QUERY SELECT plan;
END;
$$
LANGUAGE 'plpgsql'
RETURNS NULL ON NULL INPUT
SECURITY DEFINER;
```

### Securely store your password{% #securely-store-your-password %}

Store your password using secret management software such as [Vault](https://www.vaultproject.io/). You can then reference this password as `ENC[<SECRET_NAME>]` in your Agent configuration files: for example, `ENC[datadog_user_database_password]`. See [Secrets Management](https://docs.datadoghq.com/agent/configuration/secrets-management/) for more information.

The examples on this page use `datadog_user_database_password` to refer to the name of the secret where your password is stored. It is possible to reference your password in plain text, but this is not recommended.

### Verify{% #verify %}

To verify that the permissions are correct, connect to the database as the `datadog` user and run the following commands. For example, if your database is `postgres`, connect as the `datadog` user using [psql](https://www.postgresql.org/docs/current/app-psql.html) and run:

```shell
psql -h {SUPABASE_HOST} -U datadog postgres -A \
  -c "select * from pg_stat_database limit 1;" \
  && echo -e "\e[0;32mPostgres connection - OK\e[0m" \
  || echo -e "\e[0;31mCannot connect to Postgres\e[0m"
psql -h {SUPABASE_HOST} -U datadog postgres -A \
  -c "select * from pg_stat_activity limit 1;" \
  && echo -e "\e[0;32mPostgres pg_stat_activity read OK\e[0m" \
  || echo -e "\e[0;31mCannot read from pg_stat_activity\e[0m"
psql -h {SUPABASE_HOST} -U datadog postgres -A \
  -c "select * from pg_stat_statements limit 1;" \
  && echo -e "\e[0;32mPostgres pg_stat_statements read OK\e[0m" \
  || echo -e "\e[0;31mCannot read from pg_stat_statements\e[0m"
```

When prompted for a password, use the password you created for the `datadog` user.

## Install the Agent{% #install-the-agent %}

Installing the Datadog Agent also installs the Postgres check, which is required for Database Monitoring on Supabase. If you haven't installed the Agent, see the [Agent installation instructions](https://app.datadoghq.com/account/settings/agent/latest). Then, return here to continue with the instructions for your installation method.

{% alert level="info" %}
Supabase's default direct connection string is only valid on IPv6 networks. To connect the Agent to a Supabase instance using this method, ensure that the machine running the Agent is IPv6 enabled. Reference your cloud provider's documentation for more information. Supabase instances on the Pro plan or above support IPv4 addresses as an add-on.
{% /alert %}

Edit the Agent's `conf.d/postgres.d/conf.yaml` file to point to the Supabase instance you want to monitor. For a complete list of configuration options, see the [sample postgres.d/conf.yaml](https://github.com/DataDog/integrations-core/blob/master/postgres/datadog_checks/postgres/data/conf.yaml.example).

```yaml
init_config:
instances:
    - dbm: true
      host: <SUPABASE_INSTANCE_ENDPOINT>
      port: 5432
      username: datadog
      password: 'ENC[datadog_user_database_password]'

      ## Optional: Connect to a different database if needed for `custom_queries`
      # dbname: '<DB_NAME>'
```

**Note**: If your password includes special characters, wrap it in single quotes.

[Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent) to apply the changes.

### Validate{% #validate %}

[Run the Agent's status subcommand](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-status-and-information) and look for `postgres` under the Checks section. Or visit the [Databases](https://app.datadoghq.com/databases) page to get started!

## Example Agent Configurations{% #example-agent-configurations %}

### With Supavisor's session pooler{% #with-supavisors-session-pooler %}

Although we recommend having a direct connection to the database instead of connecting via proxy, you can still connect the Agent to your Supabase instance if the above options are not available to you. This will work best when you only have one instance in your Supabase project.

Get the session pooler connection string for your project via the Connect dialog, and copy it into your Agent configuration file:

```yaml
init_config:
instances:
    - dbm: true
      host: <SUPABASE_POOLER_ENDPOINT>
      port: 5432
      username: datadog.some-project-id
      password: 'ENC[datadog_user_database_password]'
```

### One agent connecting to multiple hosts{% #one-agent-connecting-to-multiple-hosts %}

It is common to configure a single Agent host to connect to multiple remote database instances (see [Agent installation architectures](https://docs.datadoghq.com/database_monitoring/architecture/) for DBM). To connect to multiple hosts, create an entry for each host in the Postgres integration config.

{% alert level="info" %}
Datadog recommends using one Agent to monitor no more than 30 database instances.Benchmarks show that one Agent running on a t4g.medium EC2 instance (2 CPUs and 4GB of RAM) can successfully monitor 30 RDS db.t3.medium instances (2 CPUs and 4GB of RAM).
{% /alert %}

```yaml
init_config:
instances:
  - dbm: true
    host: example-service-primary.example-host.com
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    tags:
      - 'env:prod'
      - 'team:team-discovery'
      - 'service:example-service'
  - dbm: true
    host: example-serviceâreplica-1.example-host.com
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    tags:
      - 'env:prod'
      - 'team:team-discovery'
      - 'service:example-service'
  - dbm: true
    host: example-serviceâreplica-2.example-host.com
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    tags:
      - 'env:prod'
      - 'team:team-discovery'
      - 'service:example-service'
    [...]
```

### Monitoring multiple databases on a database host{% #monitoring-multiple-databases-on-a-database-host %}

Use the `database_autodiscovery` option to permit the Agent to discover all databases on your host to monitor. You can specify `include` or `exclude` fields to narrow the scope of databases discovered. See the sample [postgres.d/conf.yaml](https://github.com/DataDog/integrations-core/blob/master/postgres/datadog_checks/postgres/data/conf.yaml.example) for more details.

```yaml
init_config:
instances:
  - dbm: true
    host: example-service-primary.example-host.com
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    database_autodiscovery:
      enabled: true
      # Optionally, set the include field to specify
      # a set of databases you are interested in discovering
      include:
        - mydb.*
        - example.*
    tags:
      - 'env:prod'
      - 'team:team-discovery'
      - 'service:example-service'
```

### Running custom queries{% #running-custom-queries %}

To collect custom metrics, use the `custom_queries` option. See the sample [postgres.d/conf.yaml](https://github.com/DataDog/integrations-core/blob/master/postgres/datadog_checks/postgres/data/conf.yaml.example) for more details.

```yaml
init_config:
instances:
  - dbm: true
    host: localhost
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    custom_queries:
    - metric_prefix: employee
      query: SELECT age, salary, hours_worked, name FROM hr.employees;
      columns:
        - name: custom.employee_age
          type: gauge
        - name: custom.employee_salary
           type: gauge
        - name: custom.employee_hours
           type: count
        - name: name
           type: tag
      tags:
        - 'table:employees'
```

### Monitoring relation metrics for multiple databases{% #monitoring-relation-metrics-for-multiple-databases %}

In order to collect relation metrics (such as `postgresql.seq_scans`, `postgresql.dead_rows`, `postgresql.index_rows_read`, and `postgresql.table_size`), the Agent must be configured to connect to each database (by default, the Agent only connects to the `postgres` database).

Specify a single "DBM" instance to collect DBM telemetry from all databases. Use the `database_autodiscovery` option to avoid specifying each database name.

```yaml
init_config:
instances:
  # This instance is the "DBM" instance. It will connect to the
  # all logical databases, and send DBM telemetry from all databases
  - dbm: true
    host: example-service-primary.example-host.com
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    database_autodiscovery:
      enabled: true
      exclude:
        - ^users$
        - ^inventory$
    relations:
      - relation_regex: .*
  # This instance only collects data from the `users` database
  # and collects relation metrics from tables prefixed by "2022_"
  - host: example-service-primary.example-host.com
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    dbname: users
    dbstrict: true
    relations:
      - relation_regex: 2022_.*
        relkind:
          - r
          - i
  # This instance only collects data from the `inventory` database
  # and collects relation metrics only from the specified tables
  - host: example-service-primary.example-host.com
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    dbname: inventory
    dbstrict: true
    relations:
      - relation_name: products
      - relation_name: external_seller_products
```

### Collecting schemas{% #collecting-schemas %}

To enable this feature, use the `collect_schemas` option. You must also configure the Agent to connect to each logical database.

Use the `database_autodiscovery` option to avoid specifying each logical database. See the sample [postgres.d/conf.yaml](https://github.com/DataDog/integrations-core/blob/master/postgres/datadog_checks/postgres/data/conf.yaml.example) for more details.

```yaml
init_config:
# This instance only collects data from the `users` database
# and collects relation metrics only from the specified tables
instances:
  - dbm: true
    host: example-service-primary.example-host.com
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    dbname: users
    dbstrict: true
    collect_schemas:
      enabled: true
    relations:
      - products
      - external_seller_products
  # This instance detects every logical database automatically
  # and collects relation metrics from every table
  - dbm: true
    host: example-serviceâreplica-1.example-host.com
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    database_autodiscovery:
      enabled: true
    collect_schemas:
      enabled: true
    relations:
      - relation_regex: .*
```

### Working with hosts through a proxy{% #working-with-hosts-through-a-proxy %}

If the Agent must connect through a proxy such as the [Cloud SQL Auth proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy), all telemetry is tagged with the hostname of the proxy rather than the database instance. Use the `reported_hostname` option to set a custom override of the hostname detected by the Agent.

```yaml
init_config:
instances:
  - dbm: true
    host: localhost
    port: 5000
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    reported_hostname: example-service-primary
  - dbm: true
    host: localhost
    port: 5001
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    reported_hostname: example-service-replica-1
```

## Troubleshooting{% #troubleshooting %}

If you have installed and configured the integrations and Agent as described and it is not working as expected, see [Troubleshooting](https://docs.datadoghq.com/database_monitoring/troubleshooting/?tab=postgres)

## Further reading{% #further-reading %}

- [Basic Postgres Integration](https://docs.datadoghq.com/integrations/postgres/)
