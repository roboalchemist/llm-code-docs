# Source: https://docs.datadoghq.com/database_monitoring/setup_documentdb/amazon_documentdb.md

---
title: Setting Up Database Monitoring for Amazon DocumentDB
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Database Monitoring > Setting up Amazon DocumentDB > Setting Up
  Database Monitoring for Amazon DocumentDB
---

# Setting Up Database Monitoring for Amazon DocumentDB

Database Monitoring offers comprehensive insights into your Amazon DocumentDB (with MongoDB compatibility) databases by providing access to critical metrics, operation samples, explain plans, and replication state changes. To take advantage of Database Monitoring for Amazon DocumentDB, ensure that the Datadog Agent is installed and configured to connect to your Amazon DocumentDB instances. This guide outlines the steps to set up Database Monitoring for Amazon DocumentDB.

## Before you begin{% #before-you-begin %}

{% dl %}

{% dt %}
Supported Amazon DocumentDB major versions
{% /dt %}

{% dd %}
4.0.0, 5.0.0
{% /dd %}

{% dt %}
Supported Amazon DocumentDB cluster types
{% /dt %}

{% dd %}
Instance-based clusters.**Note**: Amazon DocumentDB Elastic cluster is not supported.
{% /dd %}

{% dt %}
Supported Agent versions
{% /dt %}

{% dd %}
7.59.0+
{% /dd %}

{% dt %}
Performance impact
{% /dt %}

{% dd %}
The default Agent configuration for Database Monitoring is conservative, but you can adjust settings such as the collection interval and operation sampling rate to better suit your needs. For most workloads, the Agent represents less than one percent of query execution time on the database and less than one percent of CPU.
{% /dd %}

{% dt %}
Connection strings or SRV strings
{% /dt %}

{% dd %}
Although Amazon DocumentDB connection strings provide many benefits such as automatic failover and load balancing, the Datadog Agent must connect directly to the DocumentDB instance being monitored. If the Agent connects to a different DocumentDB instance while it is running (as in the case of failover, load balancing, and so on), the Agent calculates the difference in statistics between two hosts, producing inaccurate metrics.
{% /dd %}

{% dt %}
Data security considerations
{% /dt %}

{% dd %}
Read about how Database Management handles [sensitive information](https://docs.datadoghq.com/database_monitoring/data_collected/#sensitive-information) for information about what data the Agent collects from your databases and how to ensure it is secure.
{% /dd %}

{% /dl %}

## Setup{% #setup %}

To enable Database Monitoring for your database:

1. Grant the Agent access to your Amazon DocumentDB instances
1. Install and configure the Agent
1. (Optional) Install the Amazon DocumentDB integration

### Grant the Agent access to your Amazon DocumentDB instances{% #grant-the-agent-access-to-your-amazon-documentdb-instances %}

The Datadog Agent requires read-only access to the Amazon DocumentDB instance to collect statistics and queries.

In a Mongo shell, authenticate to the primary node of the replica set, create a read-only user for the Datadog Agent in the `admin` database, and grant the required permissions:

```shell
# Authenticate as the admin user.

use admin
db.auth("admin", "<YOUR_AMAZON_DOCUMENTDB_ADMIN_PASSWORD>")

# Create the user for the Datadog Agent.

db.createUser({
"user": "datadog",
"pwd": "<UNIQUE_PASSWORD>",
"roles": [
{ role: "read", db: "admin" },
{ role: "read", db: "local" },
{ role: "clusterMonitor", db: "admin" }
]
})
```

Grant additional permissions to the `datadog` user in the databases you want to monitor:

```shell
db.grantRolesToUser("datadog", [
{ role: "read", db: "mydatabase" },
{ role: "read", db: "myotherdatabase" }
])
```

Alternatively, you can grant the `readAnyDatabase` role to the `datadog` user in the `admin` database to monitor all databases:

```shell
db.grantRolesToUser("datadog", [
{ role: "readAnyDatabase", db: "admin" }
])
```

### Securely store your password{% #securely-store-your-password %}

Store your password using secret management software such as [Vault](https://www.vaultproject.io/). You can then reference this password as `ENC[<SECRET_NAME>]` in your Agent configuration files: for example, `ENC[datadog_user_database_password]`. See [Secrets Management](https://docs.datadoghq.com/agent/configuration/secrets-management/) for more information.

The examples on this page use `datadog_user_database_password` to refer to the name of the secret where your password is stored. It is possible to reference your password in plain text, but this is not recommended.

### Install and configure the Agent{% #install-and-configure-the-agent %}

To monitor your Amazon DocumentDB Cluster, you must install and configure the Datadog Agent on a host that can [remotely access](https://docs.datadoghq.com/account_management/api-app-keys/) your Amazon DocumentDB Cluster. This host can be a Linux host, a Docker container, or a Kubernetes pod.

#### Create the configuration file{% #create-the-configuration-file %}

To monitor an Amazon DocumentDB replica set, the Agent needs to connect to all members (including the arbiter) of the replica set.

Use the following configuration block as an example to configure the Agent to connect to a replica set member:

```yaml
init_config:
instances:
    ## @param hosts - required
    ## Specify the hostname, IP address, or UNIX domain socket of
    ## a mongod instance as listed in the replica set configuration.
    ## If the port number is not specified, the default port 27017 is used.
    #
    - hosts:
          - <HOST>:<PORT>

      ## @param username - string - optional
      ## The username to use for authentication.
      #
      username: datadog

      ## @param password - string - optional
      ## The password to use for authentication.
      #
      password: 'ENC[datadog_user_database_password]'

      ## @param options - mapping - optional
      ## Connection options. For a complete list, see:
      ## https://docs.mongodb.com/manual/reference/connection-string/#connections-connection-options
      #
      options:
          authSource: admin

      ## @param tls - boolean - required
      ## Required 'true' in Amazon DocumentDB.
      tls: true

      ## @param tls_ca_file - string - required
      ## Path to the CA certificate file used to verify the server certificate.
      tls_ca_file: <CERT_FILE_PATH>

      ## @param dbm - boolean - optional
      ## Set to true to enable Database Monitoring.
      #
      dbm: true

      ## @param cluster_name - string - optional
      ## The unique name of the cluster to which the monitored MongoDB instance belongs.
      ## Used to group MongoDB instances in a MongoDB cluster.
      ## cluster_name should follow Datadog tags naming conventions. See:
      ## https://docs.datadoghq.com/developers/guide/what-best-practices-are-recommended-for-naming-metrics-and-tags/#rules-and-best-practices-for-naming-tags
      ## Required when `dbm` is enabled.
      #
      cluster_name: <MONGO_CLUSTER_NAME>

      ## @param reported_database_hostname - string - optional
      ## Set the reported database hostname for the connected MongoDB instance.
      ## This value overrides the MongoDB hostname detected by the Agent
      ## from the MongoDB admin command serverStatus.host.
      #
      reported_database_hostname: <DATABASE_HOSTNAME_OVERRIDE>

      ## @param additional_metrics - list of strings - optional
      ## List of additional metrics to collect. Available options are:
      ## - metrics.commands: Use of database commands
      ## - tcmalloc: TCMalloc memory allocator
      ## - top: Usage statistics for each collection
      ## - collection: Metrics of the specified collections
      #
      additional_metrics: ['metrics.commands', 'tcmalloc', 'top', 'collection']

      ## @param collections_indexes_stats - boolean - optional
      ## Set to true to collect index statistics for the specified collections.
      ## Requires `collections` to be set.
      #
      collections_indexes_stats: true

      ## @param database_autodiscovery - mapping - optional
      ## Enable database autodiscovery to automatically collect metrics from all your MongoDB databases.
      #
      database_autodiscovery:
          ## @param enabled - boolean - required
          ## Enable database autodiscovery.
          #
          enabled: true

          ## @param include - list of strings - optional
          ## List of databases to include in the autodiscovery. Use regular expressions to match multiple databases.
          ## For example, to include all databases starting with "mydb", use "^mydb.*".
          ## By default, include is set to ".*" and all databases are included.
          #
          include:
              - '^mydb.*'

          ## @param exclude - list of strings - optional
          ## List of databases to exclude from the autodiscovery. Use regular expressions to match multiple databases.
          ## For example, to exclude all databases starting with "mydb", use "^mydb.*".
          ## When the exclude list conflicts with include list, the exclude list takes precedence.
          #
          exclude:
              - '^mydb2.*'
              - 'admin$'

          ## @param max_databases - integer - optional
          ## Maximum number of databases to collect metrics from. The default value is 100.
          #
          max_databases: 100

          ## @param refresh_interval - integer - optional
          ## Interval in seconds to refresh the list of databases. The default value is 600 seconds.
          #
          refresh_interval: 600
```

An example configuration for a replica set with 1 primary and 2 secondaries is as follows:

```yaml
init_config:
instances:
    - hosts:
          - <HOST_REPLICA_1>:<PORT> # Primary node
      username: datadog
      password: 'ENC[datadog_user_database_password]'
      options:
          authSource: admin
      tls: true
      tls_ca_file: <CERT_FILE_PATH>
      dbm: true
      cluster_name: <MONGO_CLUSTER_NAME>
      reported_database_hostname: <DATABASE_HOSTNAME_OVERRIDE>
      additional_metrics: ['metrics.commands', 'tcmalloc', 'top', 'collection']
      collections_indexes_stats: true
      database_autodiscovery:
          enabled: true
    - hosts:
          - <HOST_REPLICA_2>:<PORT> # Secondary node
      username: datadog
      password: 'ENC[datadog_user_database_password]'
      options:
          authSource: admin
      tls: true
      tls_ca_file: <CERT_FILE_PATH>
      dbm: true
      cluster_name: <MONGO_CLUSTER_NAME>
      reported_database_hostname: <DATABASE_HOSTNAME_OVERRIDE>
      additional_metrics: ['metrics.commands', 'tcmalloc', 'top', 'collection']
      collections_indexes_stats: true
      database_autodiscovery:
          enabled: true
    - hosts:
          - <HOST_REPLICA_3>:<PORT> # Secondary node
      username: datadog
      password: 'ENC[datadog_user_database_password]'
      options:
          authSource: admin
      tls: true
      tls_ca_file: <CERT_FILE_PATH>
      dbm: true
      cluster_name: <MONGO_CLUSTER_NAME>
      reported_database_hostname: <DATABASE_HOSTNAME_OVERRIDE>
      additional_metrics: ['metrics.commands', 'tcmalloc', 'top', 'collection']
      collections_indexes_stats: true
      database_autodiscovery:
          enabled: true
```

If you installed the [Amazon DocumentDB integration](https://docs.datadoghq.com/integrations/amazon_documentdb/) to enrich instances with Amazon DocumentDB integration telemetry, add this section to your configuration:

```yaml
## @param aws - mapping - optional
## This block defines the configuration for Amazon DocumentDB instances.
## These values are only applied when `dbm: true` option is set.
#
aws:
    ## @param instance_endpoint - string - optional
    ## Equal to the Endpoint.Address of the instance the Agent is connecting to.
    ## This value is optional if the value of `host` is already configured to the instance endpoint.
    ##
    ## For more information on instance endpoints,
    ## see the AWS docs https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Endpoint.html
    #
    instance_endpoint: <AMAZON_DOCUMENTDB_ENDPOINT>
    ## @param cluster_identifier - string - optional
    ## Equal to the cluster identifier of the instance the Agent is connecting to.
    ## This value is optional if the value of `cluster_name` is already configured to the cluster identifier.
    ##
    ## For more information on cluster identifiers,
    ## see the AWS docs https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBCluster.html
    #
    cluster_identifier: <AMAZON_DOCUMENTDB_CLUSTER_IDENTIFIER>
```

#### Set up the Agent{% #set-up-the-agent %}

{% tab title="Linux Host" %}
Place the MongoDB Agent configuration file created in the previous step in `/etc/datadog-agent/conf.d/mongo.d/conf.yaml`. See the [sample conf file](https://github.com/DataDog/integrations-core/blob/master/mongo/datadog_checks/mongo/data/conf.yaml.example) for all available configuration options.

Once all Agent configuration is complete, [restart the Datadog Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/?tab=agentv6v7#restart-the-agent).

### Validate{% #validate %}

[Run the Agent's status subcommand](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-status-and-information) and look for `mongo` under the **Checks** section. Navigate to the [Database Monitoring for MongoDB](https://app.datadoghq.com/databases/list?listView=mongo) page in Datadog to get started.
{% /tab %}

{% tab title="Docker" %}
To configure the Database Monitoring Agent running in a Docker container, set the [Autodiscovery Integration Templates](https://docs.datadoghq.com/agent/faq/template_variables/) as Docker labels on your Agent container.

The MongoDB check is included in the Datadog Agent. No additional installation is necessary.

**Note**: The Agent must have read permission on the Docker socket for autodiscovery of labels to work.

Add the configuration details for the MongoDB check from the previous step in the `com.datadoghq.ad.checks` label. See the [sample conf file](https://github.com/DataDog/integrations-core/blob/master/mongo/datadog_checks/mongo/data/conf.yaml.example) for all available configuration options.

```shell
export DD_API_KEY=<DD_API_KEY>
export DD_AGENT_VERSION=7.58.0

docker run -e "DD_API_KEY=${DD_API_KEY}" \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -l com.datadoghq.ad.checks='{
    "mongo": {
      "init_config": {},
      "instances": [{
        "hosts": ["<HOST>:<PORT>"],
        "username": "datadog",
        "password": "<UNIQUE_PASSWORD>",
        "options": {
          "authSource": "admin"
        },
        "dbm": true,
        "cluster_name": "<MONGO_CLUSTER_NAME>",
        "reported_database_hostname": "<DATABASE_HOSTNAME_OVERRIDE>",
        "additional_metrics": ["metrics.commands", "tcmalloc", "top", "collection"],
        "collections_indexes_stats": true,
        "database_autodiscovery": {
          "enabled": true
        }
      }]
    }
  }' \
  datadog/agent:${DD_AGENT_VERSION}
```

### Validate{% #validate %}

[Run the Agent's status subcommand](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-status-and-information) and look for `mongo` under the **Checks** section. Navigate to the [Database Monitoring for MongoDB](https://app.datadoghq.com/databases/list?listView=mongo) page in Datadog to get started.
{% /tab %}

{% tab title="Kubernetes" %}
If you have a Kubernetes cluster, use the [Datadog Cluster Agent](https://docs.datadoghq.com/agent/cluster_agent) for Database Monitoring.

If cluster checks are not already enabled in your Kubernetes cluster, follow the instructions to [enable cluster checks](https://docs.datadoghq.com/agent/cluster_agent/clusterchecks/). You can configure the Cluster Agent either with static files mounted in the Cluster Agent container, or by using Kubernetes service annotations.

### Command line with Helm{% #command-line-with-helm %}

Execute the following [Helm](https://helm.sh) command to install the [Datadog Cluster Agent](https://docs.datadoghq.com/agent/cluster_agent) on your Kubernetes cluster. Replace the values to match your account and environment:

```bash
helm repo add datadog https://helm.datadoghq.com
helm repo update

helm install <RELEASE_NAME> \
  --set 'datadog.apiKey=<DATADOG_API_KEY>' \
  --set 'clusterAgent.enabled=true' \
  --set 'clusterChecksRunner.enabled=true' \
  --set 'clusterAgent.confd.mongo\.yaml=cluster_check: true
init_config:
instances:
  - hosts:
      - <HOST>:<PORT>
    username: datadog
    password: <UNIQUE_PASSWORD>
    options:
      authSource: admin
    dbm: true
    cluster_name: <MONGO_CLUSTER_NAME>
    reported_database_hostname: <DATABASE_HOSTNAME_OVERRIDE>
    database_autodiscovery:
      enabled: true
    additional_metrics: ["metrics.commands", "tcmalloc", "top", "collection"]
    collections_indexes_stats: true' \
  datadog/datadog
```

### Configure with mounted files{% #configure-with-mounted-files %}

To configure a cluster check with a mounted configuration file, mount the configuration file in the Cluster Agent container on the path: `/conf.d/mongo.yaml`:

```yaml
cluster_check: true  # Make sure to include this flag
init_config:
instances:
  - hosts:
      - <HOST>:<PORT>
    username: datadog
    password: "ENC[datadog_user_database_password]"
    options:
      authSource: admin
    dbm: true
    cluster_name: <MONGO_CLUSTER_NAME>
    reported_database_hostname: <DATABASE_HOSTNAME_OVERRIDE>
    database_autodiscovery:
      enabled: true
    additional_metrics: ["metrics.commands", "tcmalloc", "top", "collection"]
    collections_indexes_stats: true
```

### Configure with Kubernetes service annotations{% #configure-with-kubernetes-service-annotations %}

Rather than mounting a file, you can declare the instance configuration as a Kubernetes Service. To configure this check for an Agent running on Kubernetes, create a Service in the same namespace as the Datadog Cluster Agent:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mongodb-datadog-check-instances
  annotations:
    ad.datadoghq.com/service.checks: |
    {
      "mongo": {
        "init_config": {},
        "instances": [{
          "hosts": ["<HOST>:<PORT>"],
          "username": "datadog",
          "password": "ENC[datadog_user_database_password]",
          "options": {
            "authSource": "admin"
          },
          "dbm": true,
          "cluster_name": "<MONGO_CLUSTER_NAME>",
          "reported_database_hostname": "<DATABASE_HOSTNAME_OVERRIDE>",
          "additional_metrics": ["metrics.commands", "tcmalloc", "top", "collection"],
          "collections_indexes_stats": true,
          "database_autodiscovery": {
            "enabled": true
          }
        }]
      }
    }
spec:
  ports:
  - port: 27017
    protocol: TCP
    targetPort: 27017
    name: mongodb
```

The Cluster Agent automatically registers this configuration and begins running the MongoDB integration.

To avoid exposing the `datadog` user's password in plain text, use the Agent's [secret management package](https://docs.datadoghq.com/agent/configuration/secrets-management) and declare the password using the `ENC[]` syntax.

### Validate{% #validate %}

[Run the Agent's status subcommand](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-status-and-information) and look for `mongo` under the **Checks** section. Navigate to the [Database Monitoring for MongoDB](https://app.datadoghq.com/databases/list?listView=mongo) page in Datadog to get started.
{% /tab %}

### Install the Amazon DocumentDB integration{% #install-the-amazon-documentdb-integration %}

To collect more comprehensive database metrics from Amazon DocumentDB, install the [Amazon DocumentDB integration](https://docs.datadoghq.com/integrations/amazon_documentdb/) (optional).

## Data Collected{% #data-collected %}

### Metrics{% #metrics %}

Refer to the [integration documentation](https://docs.datadoghq.com/integrations/mongo/?tab=replicaset#metrics) for a comprehensive list of metrics collected by the integration.

### Operation samples and explain plans{% #operation-samples-and-explain-plans %}

Database Monitoring for Amazon DocumentDB gathers operation samples using the `currentOp` command. This command provides information about operations that are currently being executed on the DocumentDB instance. Additionally, Database Monitoring collects explain plans for the read operation samples using the `explain` command, offering detailed insights into the query execution plans.

### Replication state changes{% #replication-state-changes %}

Database Monitoring for Amazon DocumentDB generates an event each time there is a change in the replication state within the DocumentDB instance. This ensures that any changes in replication are promptly detected and reported.

### Collection of schemas and indexes{% #collection-of-schemas-and-indexes %}

Database Monitoring for Amazon DocumentDB collects inferred schemas and indexes of Amazon DocumentDB collections. This information is used to provide insights into the structure and organization of your collections.

When analyzing Amazon DocumentDB collections, Datadog collects inferred schema information by sampling documents using the `$sample` aggregation stage. From this analysis, only metadata about the schema is gathered and sent to Datadog, including field names, field prevalence (how often each field appears), and their respective data types. Datadog does not collect or transmit the actual content of documents or any customer business data. This ensures that sensitive data remains protected while still providing valuable insights into the structure and organization of your collections.
