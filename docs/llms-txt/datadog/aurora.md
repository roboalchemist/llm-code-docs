# Source: https://docs.datadoghq.com/database_monitoring/setup_postgres/aurora.md

# Source: https://docs.datadoghq.com/database_monitoring/setup_mysql/aurora.md

---
title: Setting Up Database Monitoring for Aurora managed MySQL
description: Install and configure Database Monitoring for MySQL managed on Aurora.
breadcrumbs: >-
  Docs > Database Monitoring > Setting up MySQL > Setting Up Database Monitoring
  for Aurora managed MySQL
---

# Setting Up Database Monitoring for Aurora managed MySQL

Database Monitoring provides deep visibility into your MySQL databases by exposing query metrics, query samples, explain plans, connection data, system metrics, and telemetry for the InnoDB storage engine.

The Agent collects telemetry directly from the database by logging in as a read-only user. Do the following setup to enable Database Monitoring with your MySQL database:

1. Configure database parameters
1. Grant the Agent access to the database
1. Install and configure the Agent
1. Install the RDS integration

## Before you begin{% #before-you-begin %}

{% dl %}

{% dt %}
Supported MySQL versions
{% /dt %}

{% dd %}
5.6, 5.7, and 8.0 or later
{% /dd %}

{% dt %}
Supported Agent versions
{% /dt %}

{% dd %}
7.36.1 or later
{% /dd %}

{% dt %}
Performance impact
{% /dt %}

{% dd %}
The default Agent configuration for Database Monitoring is conservative, but you can adjust settings such as the collection interval and query sampling rate to better suit your needs. For most workloads, the Agent represents less than one percent of query execution time on the database and less than one percent of CPU.Database Monitoring runs as an integration on top of the base Agent ([see benchmarks](https://docs.datadoghq.com/database_monitoring/agent_integration_overhead/?tab=mysql)).
{% /dd %}

{% dt %}
Proxies, load balancers, and connection poolers
{% /dt %}

{% dd %}
The Datadog Agent must connect directly to the host being monitored, preferably through the instance endpoint. The Agent should not connect to the database through a proxy, load balancer, connection pooler, or the **Aurora cluster endpoint**. If connected to the cluster endpoint, the Agent collects data from one random replica, and only provides visibility into that replica. If the Agent connects to different hosts while it is running (as in the case of failover, load balancing, and so on), the Agent calculates the difference in statistics between two hosts, producing inaccurate metrics.
{% /dd %}

{% dt %}
Data security considerations
{% /dt %}

{% dd %}
See [Sensitive information](https://docs.datadoghq.com/containers/cluster_agent/clusterchecks/?tab=datadogoperator) for information about what data the Agent collects from your databases and how to ensure it is secure.
{% /dd %}

{% /dl %}

## Configure MySQL settings{% #configure-mysql-settings %}

Configure the following in the [DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) and then **restart the server** for the settings to take effect:

{% tab title="MySQL â¥ 5.7" %}

| Parameter                                                  | Value  | Description                                                                                                                                                                        |
| ---------------------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `performance_schema`                                       | `1`    | Required. Enables the [Performance Schema](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-quick-start.html).                                                           |
| performance_schema_consumer_events_statements_current      | `1`    | Required. Enables monitoring of currently running queries.                                                                                                                         |
| performance-schema-consumer-events-waits-current           | `ON`   | Required. Enables the collection of wait events.                                                                                                                                   |
| performance_schema_consumer_events_statements_history      | `1`    | Optional. Enables tracking recent query history per thread. If enabled it increases the likelihood of capturing execution details from infrequent queries.                         |
| performance_schema_consumer_events_statements_history_long | `1`    | Optional. Enables tracking of a larger number of recent queries across all threads. If enabled it increases the likelihood of capturing execution details from infrequent queries. |
| performance_schema_max_digest_length                       | `4096` | Increases the size of SQL digest text in `events_statements_*` tables. If left at the default value then queries longer than `1024` characters are not collected.                  |
| performance_schema_max_sql_text_length                     | `4096` | Must match performance_schema_max_digest_length.                                                                                                                                   |

{% /tab %}

{% tab title="MySQL 5.6" %}

| Parameter                                                  | Value | Description                                                                                                                                                                        |
| ---------------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `performance_schema`                                       | `1`   | Required. Enables the [Performance Schema](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-quick-start.html).                                                           |
| performance_schema_consumer_events_statements_current      | `1`   | Required. Enables monitoring of currently running queries.                                                                                                                         |
| performance-schema-consumer-events-waits-current           | `ON`  | Required. Enables the collection of wait events.                                                                                                                                   |
| performance_schema_consumer_events_statements_history      | `1`   | Optional. Enables tracking recent query history per thread. If enabled it increases the likelihood of capturing execution details from infrequent queries.                         |
| performance_schema_consumer_events_statements_history_long | `1`   | Optional. Enables tracking of a larger number of recent queries across all threads. If enabled it increases the likelihood of capturing execution details from infrequent queries. |

{% /tab %}

**Note**: A recommended practice is to allow the Agent to enable the `performance-schema-consumer-*` settings dynamically at runtime, as part of granting the Agent access. See Runtime setup consumers.

## Grant the Agent access{% #grant-the-agent-access %}

The Datadog Agent requires read-only access to the database in order to collect statistics and queries.

The following instructions grant the Agent permission to login from any host using `datadog@'%'`. You can restrict the `datadog` user to be allowed to login only from localhost by using `datadog@'localhost'`. See the [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/creating-accounts.html) for more info.

{% tab title="MySQL â¥ 5.7" %}
Create the `datadog` user and grant basic permissions:

```sql
CREATE USER datadog@'%' IDENTIFIED by '<UNIQUEPASSWORD>';
ALTER USER datadog@'%' WITH MAX_USER_CONNECTIONS 5;
GRANT REPLICATION CLIENT ON *.* TO datadog@'%';
GRANT PROCESS ON *.* TO datadog@'%';
GRANT SELECT ON performance_schema.* TO datadog@'%';
```

{% /tab %}

{% tab title="MySQL 5.6" %}
Create the `datadog` user and grant basic permissions:

```sql
CREATE USER datadog@'%' IDENTIFIED BY '<UNIQUEPASSWORD>';
GRANT REPLICATION CLIENT ON *.* TO datadog@'%' WITH MAX_USER_CONNECTIONS 5;
GRANT PROCESS ON *.* TO datadog@'%';
GRANT SELECT ON performance_schema.* TO datadog@'%';
```

{% /tab %}

Create the following schema:

```sql
CREATE SCHEMA IF NOT EXISTS datadog;
GRANT EXECUTE ON datadog.* to datadog@'%';
```

Create the `explain_statement` procedure to enable the Agent to collect explain plans:

```sql
DELIMITER $$
CREATE PROCEDURE datadog.explain_statement(IN query TEXT)
    SQL SECURITY DEFINER
BEGIN
    SET @explain := CONCAT('EXPLAIN FORMAT=json ', query);
    PREPARE stmt FROM @explain;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;
```

Additionally, create this procedure **in every schema** from which you want to collect explain plans. Replace `<YOUR_SCHEMA>` with your database schema:

```sql
DELIMITER $$
CREATE PROCEDURE <YOUR_SCHEMA>.explain_statement(IN query TEXT)
    SQL SECURITY DEFINER
BEGIN
    SET @explain := CONCAT('EXPLAIN FORMAT=json ', query);
    PREPARE stmt FROM @explain;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;
GRANT EXECUTE ON PROCEDURE <YOUR_SCHEMA>.explain_statement TO datadog@'%';
```

To collect index metrics, grant the `datadog` user an additional privilege:

```sql
GRANT SELECT ON mysql.innodb_index_stats TO datadog@'%';
```

Starting from Agent v7.65, the Datadog Agent can collect schema information from MySQL databases. See the [Collecting schemas](https://docs.datadoghq.com/database_monitoring/setup_mysql/aurora?tab=mysql57#collecting-schemas) section below for more info on how to grant the Agent permissions for this collection.

### Runtime setup consumers{% #runtime-setup-consumers %}

Datadog recommends that you create the following procedure to give the Agent the ability to enable `performance_schema.events_*` consumers at runtime.

```SQL
DELIMITER $$
CREATE PROCEDURE datadog.enable_events_statements_consumers()
    SQL SECURITY DEFINER
BEGIN
    UPDATE performance_schema.setup_consumers SET enabled='YES' WHERE name LIKE 'events_statements_%';
    UPDATE performance_schema.setup_consumers SET enabled='YES' WHERE name = 'events_waits_current';
END $$
DELIMITER ;
GRANT EXECUTE ON PROCEDURE datadog.enable_events_statements_consumers TO datadog@'%';
```

### Securely store your password{% #securely-store-your-password %}

Store your password using secret management software such as [Vault](https://www.vaultproject.io/). You can then reference this password as `ENC[<SECRET_NAME>]` in your Agent configuration files: for example, `ENC[datadog_user_database_password]`. See [Secrets Management](https://docs.datadoghq.com/agent/configuration/secrets-management/) for more information.

The examples on this page use `datadog_user_database_password` to refer to the name of the secret where your password is stored. It is possible to reference your password in plain text, but this is not recommended.

## Install and configure the Agent{% #install-and-configure-the-agent %}

To monitor Aurora hosts, install the Datadog Agent in your infrastructure and configure it to connect to each instance endpoint remotely. The Agent does not need to run on the database, it only needs to connect to it. For additional Agent installation methods not mentioned here, see the [Agent installation instructions](https://app.datadoghq.com/account/settings/agent/latest).

{% tab title="Host" %}
### Autodiscovery setup (recommended){% #autodiscovery-setup-recommended %}

The Datadog Agent supports Autodiscovery of all Aurora endpoints in a cluster. Unless you want different configurations for different instances, or want to find and list Aurora endpoints manually, follow the [Autodiscovery setup instructions for Aurora DB clusters](https://docs.datadoghq.com/database_monitoring/guide/aurora_autodiscovery/?tab=mysql) instead of the manual setup section below.

### Manual setup{% #manual-setup %}

To configure this check for an Agent running on a host, for example when you provision a small EC2 instance for the Agent to collect from an Aurora database:

Edit the `mysql.d/conf.yaml` file, in the `conf.d/` folder at the root of your [Agent's configuration directory](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-configuration-directory). See the [sample mysql.d/conf.yaml](https://github.com/DataDog/integrations-core/blob/master/mysql/datadog_checks/mysql/data/conf.yaml.example) for all available configuration options, including those for custom metrics.

Add this configuration block to your `mysql.d/conf.yaml` to collect MySQL metrics:

```yaml
init_config:

instances:
  - dbm: true
    host: '<AWS_INSTANCE_ENDPOINT>'
    port: 3306
    username: datadog
    password: 'ENC[datadog_user_database_password]' # from the CREATE USER step earlier, stored as a secret

    # After adding your project and instance, configure the Datadog AWS integration to pull additional cloud data such as CPU and Memory.
    aws:
      instance_endpoint: '<AWS_INSTANCE_ENDPOINT>'
```

{% alert level="danger" %}
Use the Aurora instance endpoint here, not the cluster endpoint.
{% /alert %}

[Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#start-stop-and-restart-the-agent) to start sending MySQL metrics to Datadog.
{% /tab %}

{% tab title="Docker" %}
To configure the Database Monitoring Agent running in a Docker container such as in ECS or Fargate, you can set the [Autodiscovery Integration Templates](https://docs.datadoghq.com/agent/docker/integrations/?tab=docker) as Docker labels on your agent container.

**Note**: The Agent must have read permission on the Docker socket for Autodiscovery of labels to work.

### Command line{% #command-line %}

Get up and running quickly by executing the following command to run the agent from your command line. Replace the values to match your account and environment:

```bash
export DD_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
export DD_AGENT_VERSION=7.36.1

docker run -e "DD_API_KEY=${DD_API_KEY}" \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -l com.datadoghq.ad.check_names='["mysql"]' \
  -l com.datadoghq.ad.init_configs='[{}]' \
  -l com.datadoghq.ad.instances='[{
    "dbm": true,
    "host": "<AWS_INSTANCE_ENDPOINT>",
    "port": 3306,
    "username": "datadog",
    "password": "<UNIQUEPASSWORD>"
  }]' \
  gcr.io/datadoghq/agent:${DD_AGENT_VERSION}
```

### Dockerfile{% #dockerfile %}

Labels can also be specified in a `Dockerfile`, so you can build and deploy a custom agent without changing any infrastructure configuration:

```Dockerfile
FROM gcr.io/datadoghq/agent:7.36.1

LABEL "com.datadoghq.ad.check_names"='["mysql"]'
LABEL "com.datadoghq.ad.init_configs"='[{}]'
LABEL "com.datadoghq.ad.instances"='[{"dbm": true, "host": "<AWS_INSTANCE_ENDPOINT>", "port": 3306,"username": "datadog","password": "ENC[datadog_user_database_password]"}]'
```

{% alert level="danger" %}
Use the Aurora instance endpoint as the host, not the cluster endpoint.
{% /alert %}

{% /tab %}

{% tab title="Kubernetes" %}
If you have a Kubernetes cluster, use the [Datadog Cluster Agent](https://docs.datadoghq.com/containers/cluster_agent/setup/) for Database Monitoring.

Follow the instructions to [enable the cluster checks](https://docs.datadoghq.com/containers/cluster_agent/clusterchecks/) if not already enabled in your Kubernetes cluster. You can declare the MySQL configuration either with static files mounted in the Cluster Agent container or using service annotations:

### Operator{% #operator %}

Using the [Operator instructions in Kubernetes and Integrations](https://docs.datadoghq.com/containers/kubernetes/integrations/?tab=datadogoperator) as a reference, follow the steps below to set up the MySQL integration:

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
             mysql.yaml: |-
               cluster_check: true
               init_config:
               instances:
               - host: <AWS_INSTANCE_ENDPOINT>
                 port: <PORT>
                 username: datadog
                 password: 'ENC[datadog_user_database_password]'
                 dbm: true
                 aws:
                   instance_endpoint: <AWS_INSTANCE_ENDPOINT>
                   region: <AWS_REGION>
   ```

1. Apply the changes to the Datadog Operator using the following command:

   ```shell
   kubectl apply -f datadog-agent.yaml
   ```

### Helm{% #helm %}

1. Complete the [Datadog Agent installation instructions](https://docs.datadoghq.com/containers/kubernetes/integrations/?tab=helm) for Helm.

1. Update your YAML configuration file (`datadog-values.yaml` in the Cluster Agent installation instructions) to include the following:

   ```yaml
   clusterAgent:
     confd:
       mysql.yaml: |-
         cluster_check: true
         init_config:
         instances:
           - dbm: true
             host: <AWS_INSTANCE_ENDPOINT>
             port: <PORT>
             username: datadog
             password: 'ENC[datadog_user_database_password]'
             aws:
               instance_endpoint: <AWS_INSTANCE_ENDPOINT>
               region: <AWS_REGION>

   clusterChecksRunner:
     enabled: true
   ```

1. Deploy the Agent with the above configuration file from the command line:

   ```shell
   helm install datadog-agent -f datadog-values.yaml datadog/datadog
   ```

{% alert level="info" %}
For Windows, append `--set targetSystem=windows` to the `helm install` command.
{% /alert %}

### Configure with mounted files{% #configure-with-mounted-files %}

To configure a cluster check with a mounted configuration file, mount the configuration file in the Cluster Agent container on the path `/conf.d/mysql.yaml`:

```yaml
cluster_check: true  # Make sure to include this flag
init_config:
instances:
  - dbm: true
    host: '<AWS_INSTANCE_ENDPOINT>'
    port: <PORT>
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    aws:
      instance_endpoint: <AWS_INSTANCE_ENDPOINT>
      region: <AWS_REGION>
```

### Configure with Kubernetes service annotations{% #configure-with-kubernetes-service-annotations %}

Rather than mounting a file, you can declare the instance configuration as a Kubernetes Service. To configure this check for an Agent running on Kubernetes, create a service using the following syntax:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql
  labels:
    tags.datadoghq.com/env: '<ENV>'
    tags.datadoghq.com/service: '<SERVICE>'
  annotations:
    ad.datadoghq.com/service.check_names: '["mysql"]'
    ad.datadoghq.com/service.init_configs: '[{}]'
    ad.datadoghq.com/service.instances: |
      [
        {
          "dbm": true,
          "host": "<AWS_INSTANCE_ENDPOINT>",
          "port": <PORT>,
          "username": "datadog",
          "password": "ENC[datadog_user_database_password]",
          "aws": {
            "instance_endpoint": "<AWS_INSTANCE_ENDPOINT>",
            "region": "<AWS_REGION>"
          }
        }
      ]
spec:
  ports:
  - port: <PORT>
    protocol: TCP
    targetPort: <PORT>
    name: mysql
```

The Cluster Agent automatically registers this configuration and begins running the MySQL check.

To avoid exposing the `datadog` user's password in plain text, use the Agent's [secret management package](https://docs.datadoghq.com/agent/configuration/secrets-management) and declare the password using the `ENC[]` syntax.
{% /tab %}

### Validate{% #validate %}

[Run the Agent's status subcommand](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-status-and-information) and look for `mysql` under the Checks section, or see the [Databases](https://app.datadoghq.com/databases) page to get started!

## Example Agent Configurations{% #example-agent-configurations %}

### One agent connecting to multiple hosts{% #one-agent-connecting-to-multiple-hosts %}

It is common to configure a single Agent host to connect to multiple remote database instances (see [Agent installation architectures](https://docs.datadoghq.com/database_monitoring/architecture/) for DBM). To connect to multiple hosts, create an entry for each host in the MySQL integration config.

{% alert level="info" %}
Datadog recommends using one Agent to monitor no more than 30 database instances.Benchmarks show that one Agent running on a t4g.medium EC2 instance (2 CPUs and 4GB of RAM) can successfully monitor 30 RDS db.t3.medium instances (2 CPUs and 4GB of RAM).
{% /alert %}

```yaml
init_config:
instances:
  - dbm: true
    host: example-service-primary.example-host.com
    port: 3306
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    tags:
      - 'env:prod'
      - 'team:team-discovery'
      - 'service:example-service'
  - dbm: true
    host: example-service-replica-1.example-host.com
    port: 3306
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    options:
      replication: true
    tags:
      - 'env:prod'
      - 'team:team-discovery'
      - 'service:example-service'
  - dbm: true
    host: example-service-replica-2.example-host.com
    port: 3306
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    options:
      replication: true
    tags:
      - 'env:prod'
      - 'team:team-discovery'
      - 'service:example-service'
    [...]
```

### Running custom queries{% #running-custom-queries %}

To collect custom metrics, use the `custom_queries` option. See the sample [mysql.d/conf.yaml](https://github.com/DataDog/integrations-core/blob/master/mysql/datadog_checks/mysql/data/conf.yaml.example) for more details.

```yaml
init_config:
instances:
  - dbm: true
    host: localhost
    port: 3306
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    custom_queries:
    - query: SELECT age, salary, hours_worked, name FROM hr.employees;
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

### Collecting schemas{% #collecting-schemas %}

{% alert level="danger" %}
Datadog Agent v7.65+ is required for MySQL schema collection.
{% /alert %}

To enable this feature, use the `collect_schemas` option. See the sample [mysql.d/conf.yaml](https://github.com/DataDog/integrations-core/blob/master/mysql/datadog_checks/mysql/data/conf.yaml.example) for more details.

```yaml
init_config:
instances:
  - dbm: true
    host: localhost
    port: 3306
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    collect_schemas:
      enabled: true
```

**Note**: For Agent v7.68 and below, use `schemas_collection` instead of `collect_schemas`.

**Note**: To collect schemas for a table, MySQL requires that the Datadog Agent has SELECT access for it. This is a [MySQL-enforced restriction](https://dev.mysql.com/doc/refman/8.4/en/information-schema-introduction.html#information-schema-privileges). Without SELECT access, the table will not appear in metadata queries.

The Agent does not use SELECT to access or read your table data. This permission is needed solely to retrieve schema details, due to how MySQL handles metadata visibility.

To grant SELECT permissions to a Datadog user, use one or a combination of the following commands:

- **All databases**:
  ```sql
  GRANT SELECT ON *.* TO datadog@'%';
  ```
- **Per database basis**:
  ```sql
  GRANT SELECT ON [database name].* TO datadog@'%';
  ```
- **Per table basis**:
  ```sql
  GRANT SELECT ON [database name].[table name] TO datadog@'%';
  ```
- **Per column basis**:
  ```sql
  GRANT SELECT ([column name1], [column name 2]) ON [database name].[table name] TO datadog@'%';
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

## Install the RDS Integration{% #install-the-rds-integration %}

To see infrastructure metrics from AWS, such as CPU, alongside the database telemetry in DBM, install the [RDS integration](https://docs.datadoghq.com/integrations/amazon_rds) (optional).

## Troubleshooting{% #troubleshooting %}

If you have installed and configured the integrations and Agent as described and it is not working as expected, see [Troubleshooting](https://docs.datadoghq.com/database_monitoring/troubleshooting/?tab=mysql)

## Further reading{% #further-reading %}

- [Basic MySQL Integration](https://docs.datadoghq.com/integrations/mysql/)
