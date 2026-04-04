# Source: https://docs.datadoghq.com/database_monitoring/setup_oracle/rac.md

---
title: Setting Up Database Monitoring for Oracle RAC
description: Install and configure Database Monitoring for Oracle RAC
breadcrumbs: >-
  Docs > Database Monitoring > Setting up Oracle > Setting Up Database
  Monitoring for Oracle RAC
---

# Setting Up Database Monitoring for Oracle RAC

Database Monitoring provides deep visibility into your Oracle databases by exposing query samples to profile your different workloads and diagnose issues.

The Agent collects telemetry directly from the database by logging in as a read-only user.

## Before you begin{% #before-you-begin %}

{% dl %}

{% dt %}
Supported Oracle versions
{% /dt %}

{% dd %}
11g, 12c, 18c, 19c, 21c
{% /dd %}

{% dt %}
Supported Agent version
{% /dt %}

{% dd %}
7.53.0+
{% /dd %}

{% dt %}
Performance impact
{% /dt %}

{% dd %}
The default Agent configuration for Database Monitoring is conservative, but you can adjust settings such as the collection interval and query sampling rate to better suit your needs. For most workloads, the Agent represents less than one percent of query execution time on the database and less than one percent of CPU.Database Monitoring runs as an integration on top of the base Agent ([see benchmarks](https://docs.datadoghq.com/database_monitoring/agent_integration_overhead/?tab=oracle)).
{% /dd %}

{% dt %}
Proxies, load balancers, and connection poolers
{% /dt %}

{% dd %}
The Agent must connect directly to the host being monitored. The Agent should not connect to the database through a proxy, load balancer, or connection pooler. Each Agent must have knowledge of the underlying hostname and should stick to a single host for its lifetime, even in cases of failover. If the Datadog Agent connects to different hosts while it is running, the values of metrics will be incorrect.
{% /dd %}

{% dt %}
Data security considerations
{% /dt %}

{% dd %}
See [Sensitive information](https://docs.datadoghq.com/database_monitoring/data_collected/#sensitive-information) for information about what data the Agent collects from your databases and how to ensure it is secure.
{% /dd %}

{% /dl %}

## Setup{% #setup %}

Complete the following to enable Database Monitoring with your Oracle database:

1. Create the Datadog user
1. Install the Agent
1. Configure the Agent
1. Install or verify the Oracle integration
1. Validate the setup

### Create the Datadog user{% #create-the-datadog-user %}

If you already have the legacy Oracle integration installed, the user already exists, and you can skip this step.

Create a read-only login to connect to your server and grant the required permissions:

```SQL
CREATE USER datadog IDENTIFIED BY <YOUR_PASSWORD>;
```

### Securely store your password{% #securely-store-your-password %}

Store your password using secret management software such as [Vault](https://www.vaultproject.io/). You can then reference this password as `ENC[<SECRET_NAME>]` in your Agent configuration files: for example, `ENC[datadog_user_database_password]`. See [Secrets Management](https://docs.datadoghq.com/agent/configuration/secrets-management/) for more information.

The examples on this page use `datadog_user_database_password` to refer to the name of the secret where your password is stored. It is possible to reference your password in plain text, but this is not recommended.

### Install the Agent{% #install-the-agent %}

See the [DBM Setup Architecture](https://docs.datadoghq.com/database_monitoring/architecture/) documentation to determine where to install the Agent. The Agent doesn't require any external Oracle clients.

For installation steps, see the [Agent installation instructions](https://app.datadoghq.com/account/settings/agent/latest).

### Configure the Agent{% #configure-the-agent %}

Configure the Agent for each RAC node by following the instructions for [self-hosted Oracle databases](https://docs.datadoghq.com/database_monitoring/setup_oracle/selfhosted).

You must configure the Agent for each Real Application Cluster (RAC) node, because the Agent collects information from every node separately by querying `V$` views. The Agent doesn't query any `GV$` views to avoid generating interconnect traffic. The collected data from each RAC node is aggregated in the frontend.

```yaml
init_config:
instances:
  - server: '<RAC_NODE_1>:<PORT>'
    service_name: "<CDB_SERVICE_NAME>" # The Oracle CDB service name
    username: 'c##datadog'
    password: 'ENC[datadog_user_database_password]'
    dbm: true
    tags:  # Optional
      - rac_cluster:<CLUSTER_NAME>
      - 'service:<CUSTOM_SERVICE>'
      - 'env:<CUSTOM_ENV>'
  - server: '<RAC_NODE_2>:<PORT>'
    service_name: "<CDB_SERVICE_NAME>" # The Oracle CDB service name
    username: 'c##datadog'
    password: 'ENC[datadog_user_database_password]'
    dbm: true
    tags:  # Optional
      - rac_cluster:<CLUSTER_NAME>
      - 'service:<CUSTOM_SERVICE>'
      - 'env:<CUSTOM_ENV>'
```

The Agent connects only to CDB. It queries the information about PDBs while connected to CDB. Don't create connections to individual PDBs.

Set the `rac_cluster` configuration parameter to the name of your RAC cluster or some user friendly alias. The `rac_cluster` filter helps you select all RAC nodes in the [DBM Oracle Database Overview dashboard](https://app.datadoghq.com/dash/integration/30990/dbm-oracle-database-overview). You can set an additional filter for the database of interest.

### Validate the setup{% #validate-the-setup %}

[Run the Agent's status subcommand](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-status-and-information) and look for `oracle` under the **Checks** section. Navigate to the [Dashboard](https://app.datadoghq.com/dash/integration/30990/dbm-oracle-database-overview) and [Databases](https://app.datadoghq.com/databases) page in Datadog to get started.

## Custom queries{% #custom-queries %}

Database Monitoring supports custom queries for Oracle databases. See the [conf.yaml.example](https://github.com/DataDog/datadog-agent/blob/main/cmd/agent/dist/conf.d/oracle.d/conf.yaml.example) to learn more about the configuration options available.

{% alert level="danger" %}
Running custom queries may result in additional costs or fees assessed by Oracle.
{% /alert %}

## Further reading{% #further-reading %}

- [Basic Oracle Integration](https://docs.datadoghq.com/integrations/oracle/)
