# Source: https://docs.datadoghq.com/database_monitoring/guide/aurora_autodiscovery.md

---
title: Configuring Database Monitoring for Amazon Aurora DB Clusters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Database Monitoring > Database Monitoring Guides > Configuring Database
  Monitoring for Amazon Aurora DB Clusters
---

# Configuring Database Monitoring for Amazon Aurora DB Clusters

This guide assumes you have configured Database Monitoring for your Amazon Aurora [Postgres](https://docs.datadoghq.com/database_monitoring/setup_postgres/aurora/?tab=postgres10) or [MySQL](https://docs.datadoghq.com/database_monitoring/setup_mysql/aurora?tab=mysql56) databases.

## Before you begin{% #before-you-begin %}

{% dl %}

{% dt %}
Supported databases
{% /dt %}

{% dd %}
Postgres, MySQL
{% /dd %}

{% dt %}
Supported Agent versions
{% /dt %}

{% dd %}
7.53.0+
{% /dd %}

{% /dl %}

## Overview{% #overview %}

Datadog's [Autodiscovery](https://docs.datadoghq.com/getting_started/containers/autodiscovery/?tab=adannotationsv2agent736) enables you to configure monitoring in dynamic infrastructures. You can use this feature to monitor your Aurora clusters without having to list individual database host endpoints (for example, `postgres.d/conf.yaml`). This is especially helpful for clusters that use [Aurora Auto Scaling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html), which dynamically adjusts the number of Aurora Replicas in response to variations in connectivity or workload. Autodiscovery automatically discovers and monitors both primary and replica endpoint instances.

With Autodiscovery and Database Monitoring, you can define configuration templates for Postgres or MySQL checks and specify which clusters to apply each check to.

## Enabling Autodiscovery for Aurora clusters{% #enabling-autodiscovery-for-aurora-clusters %}

1. Grant AWS permissions
1. Configure Aurora tags
1. Configure the Datadog Agent
1. Create a configuration template

### Grant AWS permissions{% #grant-aws-permissions %}

The Datadog Agent requires permission to run `rds:DescribeDBClusters` and `rds:DescribeDBInstances` in your AWS account. Datadog recommends that you attach an IAM role policy to the EC2 instance where the Agent is running.

An example policy that grants these permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBClusters",
        "rds:DescribeDBInstances"
      ],
      "Resource": [
        "arn:aws:rds:<region>:<account>:cluster:*",
        "arn:aws:rds:<region>:<account>:db:*"
      ]
    }
  ]
}
```

You can also attach the [`AmazonRDSReadOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRDSReadOnlyAccess.html) policy.

### Configure Aurora tags{% #configure-aurora-tags %}

The listener discovers all Aurora clusters in the account and region where the Agent is running that have the `datadoghq.com/scrape:true` tag applied. You can also configure the Agent to discover clusters with specific tags.

You must apply these tags to the DB cluster (Role: `Regional cluster`). For more information on tagging RDS resources, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html#Tagging.HowTo).

If you configure `tags` as an empty array, Autodiscovery will discovery all clusters in the account and region.

### Configure the Datadog Agent{% #configure-the-datadog-agent %}

Autodiscovery uses an Agent service listener, which discovers all database host endpoints in an Aurora cluster and forwards discovered endpoints to the existing Agent check scheduling pipeline. You can configure the listener in the `datadog.yaml` file:

```yaml
database_monitoring:
  autodiscovery:
    aurora:
      enabled: true
```

**Note**: The Agent only discovers Aurora instances running in the same region as the Agent. To determine the region of the instance, the Agent uses [IMDS (Instance Metadata Service)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html). If your EC2 instance requires `IMDSv2`, you must configure the Agent to use `IMDSv2` by setting `ec2_prefer_imdsv2: true` in `datadog.yaml`, as shown below:

```yaml
ec2_prefer_imdsv2: true
database_monitoring:
  autodiscovery:
    aurora:
      enabled: true
```

By default, the listener only discovers Aurora clusters in the account and region where the Agent is running, and only those with the `datadoghq.com/scrape:true` tag. You can also configure the listener to discover clusters with specific tags.

To specify custom tags for Aurora cluster discovery in the `datadog.yaml` file:

```yaml
database_monitoring:
  autodiscovery:
    aurora:
      enabled: true
      tags:
        - "my-cluster-tag-key:value"
```

To monitor all clusters in the account and region:

```yaml
database_monitoring:
  autodiscovery:
    aurora:
      enabled: true
      tags: []
```

The listener queries the AWS API for the list of hosts in a loop. The frequency with which the listener queries the AWS API, in seconds, is configurable in the `datadog.yaml` file:

```yaml
database_monitoring:
  autodiscovery:
    aurora:
      enabled: true
      discovery_interval: 300
```

The listener provides an `%%extra_dbm%%` variable that can be used to enable or disable DBM for the instance. This value defaults to `true` if the tag `datadoghq.com/dbm:true` is present. To specify a custom tag for this value use `dbm_tag`:

```yaml
database_monitoring:
  autodiscovery:
    aurora:
      enabled: true
      dbm_tag:
        - "use_dbm:true"
```

The `%%extra_dbm%%` value is true if the tag is present, and false otherwise. It does not set its value to the value of the tag.

### Create a configuration template{% #create-a-configuration-template %}

The Datadog Agent supports configuration templates for the Postgres and MySQL integrations. Define a configuration template for the Aurora clusters you wish to monitor.

{% tab title="Postgres" %}
First, add an `ad_identifier` for Aurora-managed Postgres to your configuration template (`postgres.d/conf_aws_aurora.yaml`) file:

```yaml
ad_identifiers:
  - _dbm_postgres_aurora
```

Then, define the remainder of the template. Use template variables for parameters that may change, such as `host` and `port`.

```yaml
ad_identifiers:
  - _dbm_postgres_aurora
init_config:
instances:
  - host: "%%host%%"
    port: "%%port%%"
    username: datadog
    dbm: "%%extra_dbm%%"
    aws:
      instance_endpoint: "%%host%%"
      region: "%%extra_region%%"
    tags:
    - "dbclusteridentifier:%%extra_dbclusteridentifier%%"
    - "region:%%extra_region%%"
```

In this example, the template variables `%%host%%`, `%%port%%`, `%%extra_dbclusteridentifier%%`, `%%extra_dbm%%`, and `%%extra_region%%` are dynamically populated with information from the Aurora cluster.

#### Authentication{% #authentication %}

If you are using password for authentication note that the password provided in this template file will be used across every database discovered.

{% collapsible-section #securely-store-your-password %}
##### Securely store your password

##### Securely store your password{% #securely-store-your-password %}

Store your password using secret management software such as [Vault](https://www.vaultproject.io/). You can then reference this password as `ENC[<SECRET_NAME>]` in your Agent configuration files: for example, `ENC[datadog_user_database_password]`. See [Secrets Management](https://docs.datadoghq.com/agent/configuration/secrets-management/) for more information.

The examples on this page use `datadog_user_database_password` to refer to the name of the secret where your password is stored. It is possible to reference your password in plain text, but this is not recommended.

The following example configuration template is applied to every instance discovered in the Aurora cluster:

```yaml
ad_identifiers:
  - _dbm_postgres_aurora
init_config:
instances:
  - host: "%%host%%"
    port: "%%port%%"
    username: datadog
    password: "ENC[datadog_user_database_password]"
    dbm: "%%extra_dbm%%"
    aws:
      instance_endpoint: "%%host%%"
      region: "%%extra_region%%"
    tags:
    - "dbclusteridentifier:%%extra_dbclusteridentifier%%"
    - "region:%%extra_region%%"
```

{% /collapsible-section %}

{% collapsible-section #iam-authentication %}
##### IAM Authentication

##### IAM Authentication{% #iam-authentication %}

To use [IAM authentication](https://docs.datadoghq.com/database_monitoring/guide/managed_authentication/?tab=aurora#configure-iam-authentication) to connect to your Aurora cluster, use the following template:

```yaml
ad_identifiers:
  - _dbm_postgres_aurora
init_config:
instances:
  - host: "%%host%%"
    port: "%%port%%"
    username: datadog
    dbm: true
    aws:
      instance_endpoint: "%%host%%"
      region: "%%extra_region%%"
      managed_authentication:
        enabled: "%%extra_managed_authentication_enabled%%"
    tags:
      - "dbclusteridentifier:%%extra_dbclusteridentifier%%"
      - "region:%%extra_region%%"
```

The template variable `%%extra_managed_authentication_enabled%%` resolves to `true` if the instance is using IAM authentication.
{% /collapsible-section %}

{% /tab %}

{% tab title="MySQL" %}
First, add an `ad_identifier` for Aurora-managed MySQL to your configuration template (`mysql.d/conf_aws_aurora.yaml`) file:

```yaml
ad_identifiers:
  - _dbm_mysql_aurora
```

Then, define the remainder of the template. Use template variables for parameters that may change, such as `host` and `port`.

```yaml
ad_identifiers:
  - _dbm_mysql_aurora
init_config:
instances:
  - host: "%%host%%"
    port: "%%port%%"
    username: datadog
    dbm: "%%extra_dbm%%"
    aws:
      instance_endpoint: "%%host%%"
      region: "%%extra_region%%"
    tags:
    - "dbclusteridentifier:%%extra_dbclusteridentifier%%"
    - "region:%%extra_region%%"
```

In this example, the template variables `%%host%%`, `%%port%%`, `%%extra_dbclusteridentifier%%`, `%%extra_dbm%%`, and `%%extra_region%%` are dynamically populated with information from the Aurora cluster.

#### Authentication{% #authentication %}

If you are using password for authentication note that the password provided in this template file will be used across every database discovered.

{% collapsible-section #securely-store-your-password %}
##### Securely store your password

##### Securely store your password{% #securely-store-your-password %}

Store your password using secret management software such as [Vault](https://www.vaultproject.io/). You can then reference this password as `ENC[<SECRET_NAME>]` in your Agent configuration files: for example, `ENC[datadog_user_database_password]`. See [Secrets Management](https://docs.datadoghq.com/agent/configuration/secrets-management/) for more information.

The examples on this page use `datadog_user_database_password` to refer to the name of the secret where your password is stored. It is possible to reference your password in plain text, but this is not recommended.

The following example configuration template is applied to every instance discovered in the Aurora cluster:

```yaml
ad_identifiers:
  - _dbm_mysql_aurora
init_config:
instances:
  - host: "%%host%%"
    port: "%%port%%"
    username: datadog
    password: "ENC[datadog_user_database_password]"
    dbm: "%%extra_dbm%%"
    aws:
      instance_endpoint: "%%host%%"
      region: "%%extra_region%%"
    tags:
    - "dbclusteridentifier:%%extra_dbclusteridentifier%%"
    - "region:%%extra_region%%"
```

{% /collapsible-section %}

{% collapsible-section #iam-authentication %}
##### IAM Authentication (7.67.0+)

##### IAM Authentication{% #iam-authentication %}

To use [IAM authentication](https://docs.datadoghq.com/database_monitoring/guide/managed_authentication/?tab=aurora#configure-iam-authentication) to connect to your RDS instance, make sure that you are using Agent version 7.67.0 or above and use the following template:

```yaml
ad_identifiers:
  - _dbm_mysql_aurora
init_config:
instances:
  - host: "%%host%%"
    port: "%%port%%"
    username: datadog
    dbm: true
    aws:
      instance_endpoint: "%%host%%"
      region: "%%extra_region%%"
      managed_authentication:
        enabled: "%%extra_managed_authentication_enabled%%"
    tags:
      - "dbclusteridentifier:%%extra_dbclusteridentifier%%"
      - "region:%%extra_region%%"
```

The template variable `%%extra_managed_authentication_enabled%%` resolves to `true` if the instance is using IAM authentication.
{% /collapsible-section %}

{% /tab %}

For more information on configuring Autodiscovery with integrations, see the [Autodiscovery documentation](https://docs.datadoghq.com/containers/docker/integrations/?tab=dockeradv2).

#### Supported template variables{% #supported-template-variables %}

| Template variable                        | Source                                                                                                                                   |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| %%host%%                                 | The Aurora instance endpoint                                                                                                             |
| %%port%%                                 | The port of the Aurora instance                                                                                                          |
| %%extra_region%%                         | The AWS region where the instance is located                                                                                             |
| %%extra_dbclusteridentifier%%            | The cluster identifier of the discovered Aurora cluster                                                                                  |
| %%extra_dbm%%                            | Whether DBM is enabled on the cluster. Determined by the presence of `dbm_tag`, which defaults to `datadoghq.com/dbm:true`.              |
| %%extra_managed_authentication_enabled%% | Whether IAM authentication enabled on the cluster.This is used to determine if managed authentication should be used for the connection. |
