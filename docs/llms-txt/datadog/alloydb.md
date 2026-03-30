# Source: https://docs.datadoghq.com/database_monitoring/setup_postgres/alloydb.md

---
title: Setting Up Database Monitoring for Google AlloyDB managed Postgres
description: >-
  Install and configure Database Monitoring for Postgres managed on Google
  AlloyDB.
breadcrumbs: >-
  Docs > Database Monitoring > Setting up Postgres > Setting Up Database
  Monitoring for Google AlloyDB managed Postgres
---

# Setting Up Database Monitoring for Google AlloyDB managed Postgres

Database Monitoring provides deep visibility into your Postgres databases by exposing query metrics, query samples, explain plans, database states, failovers, and events.

The Agent collects telemetry directly from the database by logging in as a read-only user. Do the following setup to enable Database Monitoring with your Postgres database:

1. Configure database parameters
1. Grant the Agent access to the database
1. Install and configure the Agent
1. Install the AlloyDB Integration

## Before you begin{% #before-you-begin %}

{% dl %}

{% dt %}
Supported PostgreSQL versions
{% /dt %}

{% dd %}
14, 15, 16, 17
{% /dd %}

{% dt %}
Supported Agent versions
{% /dt %}

{% dd %}
7.36.1+
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
The Datadog Agent must connect directly to the host being monitored. For self-hosted databases, `127.0.0.1` or the socket is preferred. The Agent should not connect to the database through a proxy, load balancer, or connection pooler such as `pgbouncer`. If the Agent connects to different hosts while it is running (as in the case of failover, load balancing, and so on), the Agent calculates the difference in statistics between two hosts, producing inaccurate metrics.
{% /dd %}

{% dt %}
Data security considerations
{% /dt %}

{% dd %}
See [Sensitive information](https://docs.datadoghq.com/database_monitoring/data_collected/#sensitive-information) for information about what data the Agent collects from your databases and how to ensure it is secure.
{% /dd %}

{% /dl %}

## Configure Postgres settings{% #configure-postgres-settings %}

Configure the following [parameters](https://www.postgresql.org/docs/current/config-setting.html) in [Database flags](https://cloud.google.com/sql/docs/postgres/flags) and then **restart the server** for the settings to take effect. For more information about these parameters, see the [Postgres documentation](https://www.postgresql.org/docs/current/pgstatstatements.html).

| Parameter                          | Value   | Description                                                                                                                                                                                                       |
| ---------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `track_activity_query_size`        | `4096`  | Required for collection of larger queries. Increases the size of SQL text in `pg_stat_activity`. If left at the default value then queries longer than `1024` characters will not be collected.                   |
| `pg_stat_statements.track`         | `all`   | Optional. Enables tracking of statements within stored procedures and functions.                                                                                                                                  |
| `pg_stat_statements.max`           | `10000` | Optional. Increases the number of normalized queries tracked in `pg_stat_statements`. This setting is recommended for high-volume databases that see many different types of queries from many different clients. |
| `pg_stat_statements.track_utility` | `off`   | Optional. Disables utility commands like PREPARE and EXPLAIN. Setting this value to `off` means only queries like SELECT, UPDATE, and DELETE are tracked.                                                         |
| `track_io_timing`                  | `on`    | Optional. Enables collection of block read and write times for queries.                                                                                                                                           |

## Grant the Agent access{% #grant-the-agent-access %}

The Datadog Agent requires read-only access to the database server in order to collect statistics and queries.

The following SQL commands should be executed on the **primary** database server (the writer) in the cluster if Postgres is replicated. Choose a PostgreSQL database on the database server for the Agent to connect to. The Agent can collect telemetry from all databases on the database server regardless of which one it connects to, so a good option is to use the default `postgres` database. Choose a different database only if you need the Agent to run [custom queries against data unique to that database](https://docs.datadoghq.com/integrations/faq/postgres-custom-metric-collection-explained/).

Connect to the chosen database as a superuser (or another user with sufficient permissions). For example, if your chosen database is `postgres`, connect as the `postgres` user using [psql](https://www.postgresql.org/docs/current/app-psql.html) by running:

```bash
psql -h mydb.example.com -d postgres -U postgres
```

Create the `datadog` user:

```SQL
CREATE USER datadog WITH password '<PASSWORD>';
```

Create the following schema **in every database**:

```SQL
CREATE SCHEMA datadog;
GRANT USAGE ON SCHEMA datadog TO datadog;
GRANT USAGE ON SCHEMA public TO datadog;
GRANT pg_monitor TO datadog;
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

{% alert level="info" %}
For data collection or custom metrics that require querying additional tables, you may need to grant the `SELECT` permission on those tables to the `datadog` user. Example: `grant SELECT on <TABLE_NAME> to datadog;`. See [PostgreSQL custom metric collection](https://docs.datadoghq.com/integrations/faq/postgres-custom-metric-collection-explained/) for more information.
{% /alert %}

Create the function **in every database** to enable the Agent to collect explain plans.

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
   SET TRANSACTION READ ONLY;

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

To verify the permissions are correct, run the following commands to confirm the Agent user is able to connect to the database and read the core tables:

```shell
psql -h localhost -U datadog postgres -A \
  -c "select * from pg_stat_database limit 1;" \
  && echo -e "\e[0;32mPostgres connection - OK\e[0m" \
  || echo -e "\e[0;31mCannot connect to Postgres\e[0m"
psql -h localhost -U datadog postgres -A \
  -c "select * from pg_stat_activity limit 1;" \
  && echo -e "\e[0;32mPostgres pg_stat_activity read OK\e[0m" \
  || echo -e "\e[0;31mCannot read from pg_stat_activity\e[0m"
psql -h localhost -U datadog postgres -A \
  -c "select * from pg_stat_statements limit 1;" \
  && echo -e "\e[0;32mPostgres pg_stat_statements read OK\e[0m" \
  || echo -e "\e[0;31mCannot read from pg_stat_statements\e[0m"
```

When it prompts for a password, use the password you entered when you created the `datadog` user.

## Install and configure the Agent{% #install-and-configure-the-agent %}

To monitor AlloyDB hosts, install the Datadog Agent in your infrastructure and configure it to connect to each instance remotely. The Agent does not need to run on the database, it only needs to connect to it. For additional Agent installation methods not mentioned here, see the [Agent installation instructions](https://app.datadoghq.com/account/settings/agent/latest).

{% tab title="Host" %}
To configure Database Monitoring metrics collection for an Agent running on a host, for example when you provision a small GCE instance for the Agent to collect from a Google AlloyDB database:

1. Edit the `postgres.d/conf.yaml` file to point to your `host` / `port` and set the masters to monitor. See the [sample postgres.d/conf.yaml](https://github.com/DataDog/integrations-core/blob/master/postgres/datadog_checks/postgres/data/conf.yaml.example) for all available configuration options. The location of the `postgres.d` directory depends on your operating system. For more information, see [Agent configuration directory](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/?tab=agentv6v7#agent-configuration-directory).

   ```yaml
   init_config:
   instances:
     - dbm: true
       host: '<INSTANCE_ADDRESS>'
       port: 5432
       username: datadog
       password: 'ENC[datadog_user_database_password]'
       gcp:
        project_id: '<PROJECT_ID>'
        instance_id: '<INSTANCE_ID>'

       ## Optional: Connect to a different database if needed for `custom_queries`
       # dbname: '<DB_NAME>'
   ```

1. [Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#start-stop-and-restart-the-agent).

{% /tab %}

{% tab title="Docker" %}
To configure an integration for an Agent running in a Docker container such as in Google Cloud Run, you have a couple of methods available, all of which are covered in detail in the [Docker Configuration Documentation](https://docs.datadoghq.com/containers/docker/integrations/?tab=labels#configuration).

The examples below show how to use [Docker Labels](https://docs.docker.com/engine/manage-resources/labels/) and [Autodiscovery Templates](https://docs.datadoghq.com/getting_started/containers/autodiscovery/) to configure the Postgres integration.

**Note**: The Agent must have read permission on the Docker socket for Autodiscovery of labels to work.

### Command line{% #command-line %}

Run the following command from your [command line](https://docs.datadoghq.com/containers/docker/integrations/?tab=labels#using-docker-run-nerdctl-run-or-podman-run) to start the Agent. Replace the placeholder values with those for your account and environment.

```bash
export DD_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
export DD_AGENT_VERSION=<AGENT_VERSION>

docker run -e "DD_API_KEY=${DD_API_KEY}" \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -l com.datadoghq.ad.check_names='["postgres"]' \
  -l com.datadoghq.ad.init_configs='[{}]' \
  -l com.datadoghq.ad.instances='[{
    "dbm": true,
    "host": "<INSTANCE_ADDRESS>",
    "port": 5432,
    "username": "datadog",
    "password": "<UNIQUEPASSWORD>",
    "gcp": {
      "project_id": "<PROJECT_ID>",
      "instance_id": "<INSTANCE_ID>"
    }
  }]' \
  gcr.io/datadoghq/agent:${DD_AGENT_VERSION}
```

### Dockerfile{% #dockerfile %}

Labels can also be specified in a `Dockerfile`, so you can build and deploy a custom agent without changing any infrastructure configuration:

```Dockerfile
FROM gcr.io/datadoghq/agent:<AGENT_VERSION>

LABEL "com.datadoghq.ad.check_names"='["postgres"]'
LABEL "com.datadoghq.ad.init_configs"='[{}]'
LABEL "com.datadoghq.ad.instances"='[{"dbm": true, "host": "<INSTANCE_ADDRESS>", "port": 5432,"username": "datadog","password": "ENC[datadog_user_database_password]", "gcp": {"project_id": "<PROJECT_ID>", "instance_id": "<INSTANCE_ID>"}}]'
```

To avoid exposing the `datadog` user's password in plain text, use the Agent's [secret management package](https://docs.datadoghq.com/agent/configuration/secrets-management) and declare the password using the `ENC[]` syntax. Alternatively, see the [Autodiscovery template variables documentation](https://docs.datadoghq.com/agent/faq/template_variables/) to provide the password as an environment variable.
{% /tab %}

{% tab title="Kubernetes" %}
If you're running a Kubernetes cluster, use the [Datadog Cluster Agent](https://docs.datadoghq.com/containers/cluster_agent/setup/) to enable Database Monitoring.

**Note**: Make sure [cluster checks](https://docs.datadoghq.com/containers/cluster_agent/clusterchecks/) are enabled for your Datadog Cluster Agent before proceeding.

Below are step-by-step instructions for configuring the Postgres integration using different Datadog Cluster Agent deployment methods.

### Operator{% #operator %}

Using the [Operator instructions in Kubernetes and Integrations](https://docs.datadoghq.com/containers/kubernetes/integrations/?tab=datadogoperator) as a reference, follow the steps below to set up the Postgres integration:

1. Create or update the `datadog-agent.yaml` file with the following configuration:

   ```yaml
   apiVersion: datadoghq.com/v2alpha1
   kind: DatadogAgent
   metadata:
     name: datadog
   spec:
     global:
       clusterName: <CLUSTER_NAME>
       site: <DD_SITE>
       credentials:
         apiSecret:
           secretName: datadog-agent-secret
           keyName: api-key

     features:
       clusterChecks:
         enabled: true

     override:
       nodeAgent:
         image:
           name: agent
           tag: <AGENT_VERSION>

       clusterAgent:
         extraConfd:
           configDataMap:
             postgres.yaml: |-
               cluster_check: true
               init_config:
               instances:
               - host: <INSTANCE_ADDRESS>
                 port: 5432
                 username: datadog
                 password: 'ENC[datadog_user_database_password]'
                 dbm: true
                 gcp:
                   project_id: '<PROJECT_ID>'
                   instance_id: '<INSTANCE_ID>'
   ```

1. Apply the changes to the Datadog Operator using the following command:

   ```shell
   kubectl apply -f datadog-agent.yaml
   ```

### Helm{% #helm %}

Using the [Helm instructions in Kubernetes and Integrations](https://docs.datadoghq.com/containers/kubernetes/integrations/?tab=helm) as a reference, follow the steps below to set up the Postgres integration:

1. Update your `datadog-values.yaml` file (used in the Cluster Agent installation instructions) with the following configuration:

   ```yaml
   clusterAgent:
     confd:
       postgres.yaml: |-
         cluster_check: true
         init_config:
         instances:
         - dbm: true
           host: <INSTANCE_ADDRESS>
           port: 5432
           username: datadog
           password: 'ENC[datadog_user_database_password]'
           gcp:
             project_id: '<PROJECT_ID>'
             instance_id: '<INSTANCE_ID>'

   clusterChecksRunner:
     enabled: true
   ```

1. Deploy the Agent with the above configuration file using the following command:

   ```shell
   helm install datadog-agent -f datadog-values.yaml datadog/datadog
   ```

{% alert level="info" %}
For Windows, append `--set targetSystem=windows` to the `helm install` command.
{% /alert %}

### Configure with mounted files{% #configure-with-mounted-files %}

To configure a cluster check with a mounted configuration file, mount the configuration file in the Cluster Agent container on the path: `/conf.d/postgres.yaml`:

```yaml
cluster_check: true  # Make sure to include this flag
init_config:
instances:
  - dbm: true
    host: '<INSTANCE_ADDRESS>'
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    gcp:
      project_id: '<PROJECT_ID>'
      instance_id: '<INSTANCE_ID>'
```

### Configure with Kubernetes service annotations{% #configure-with-kubernetes-service-annotations %}

Instead of mounting a file, you can declare the instance configuration as a Kubernetes Service. To configure this check for an Agent running on Kubernetes, create a service using the following syntax:

#### Autodiscovery annotations v2{% #autodiscovery-annotations-v2 %}

```yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres
  labels:
    tags.datadoghq.com/env: '<ENV>'
    tags.datadoghq.com/service: '<SERVICE>'
  annotations:
    ad.datadoghq.com/service.check_names: '["postgres"]'
    ad.datadoghq.com/service.init_configs: '[{}]'
    ad.datadoghq.com/service.instances: |
      [
        {
          "dbm": true,
          "host": "<INSTANCE_ADDRESS>",
          "port": 5432,
          "username": "datadog",
          "password": "ENC[datadog_user_database_password]",
          "gcp": {
            "project_id": "<PROJECT_ID>",
            "instance_id": "<INSTANCE_ID>"
          }
        }
      ]
spec:
  ports:
  - port: 5432
    protocol: TCP
    targetPort: 5432
    name: postgres
```

For more information, see [Autodiscovery Annotations](https://docs.datadoghq.com/containers/kubernetes/integrations/?tab=annotations#configuration).

The Cluster Agent automatically registers this configuration and begin running the Postgres check.
{% /tab %}

See the [Postgres integration spec](https://github.com/DataDog/integrations-core/blob/master/postgres/datadog_checks/postgres/data/conf.yaml.example#L638-L662) for additional information on setting `project_id` and `instance_id` fields.

### Validate{% #validate %}

[Run the Agent's status subcommand](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-status-and-information) and look for `postgres` under the Checks section. Or visit the [Databases](https://app.datadoghq.com/databases) page to get started!

## Example Agent Configurations{% #example-agent-configurations %}

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

## Install the AlloyDB integration{% #install-the-alloydb-integration %}

To collect more comprehensive database metrics from AlloyDB, install the [AlloyDB integration](https://docs.datadoghq.com/integrations/google_cloud_alloydb) (optional).

## Troubleshooting{% #troubleshooting %}

If you have installed and configured the integrations and Agent as described and it is not working as expected, see [Troubleshooting](https://docs.datadoghq.com/database_monitoring/troubleshooting/?tab=postgres)

## Further reading{% #further-reading %}

- [Basic Postgres Integration](https://docs.datadoghq.com/integrations/postgres/)
- [Capturing SQL Query Parameter Values](https://docs.datadoghq.com/database_monitoring/guide/parameterized_queries/)
