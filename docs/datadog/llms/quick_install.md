# Source: https://docs.datadoghq.com/database_monitoring/setup_postgres/rds/quick_install.md

---
title: Database Monitoring Quick Install for Postgres RDS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Database Monitoring > Setting up Postgres > Setting Up Database
  Monitoring for Amazon RDS managed Postgres > Database Monitoring Quick Install
  for Postgres RDS
---

# Database Monitoring Quick Install for Postgres RDS

Database Monitoring Quick Install for RDS enables you to quickly set up Agents to monitor your RDS Postgres instances. After you specify a few options, Datadog generates a CloudFormation template that configures your instance for monitoring, and uses Amazon ECS to deploy the Agent to the RDS instance with recommended DBM configurations.

## Prerequisites{% #prerequisites %}

- A security group must be configured on the instance to allow incoming connections from the instance's VPC and outgoing connections to the internet.
- The RDS instance's admin access username and password must be stored in an AWS Secret within AWS Secrets Manager. Ensure that you note the Amazon Resource Name (ARN) of this secret, since Datadog uses it to access the credentials during setup and operation.

{% alert level="info" %}
Datadog does not store the admin credentials. They are only used temporarily to connect the Agent, and no data is retained after the process is completed.
{% /alert %}

## Installation{% #installation %}

1. Navigate to the [Database Monitoring Setup](https://app.datadoghq.com/databases/setup) page.
1. On the **Unmonitored Hosts** tab, click **Add Agent** for the RDS instance where you want to install the Agent.
1. If you don't have an ECS cluster installed for your account and region, click **Create Cluster**.
1. Select a security group from the **Security Group** dropdown list.
1. Click **Select API Key**, select an API key from the list, and then click **Use API Key**.
1. Click **Launch CloudFormation Stack in AWS Console**. A new page opens, displaying the AWS CloudFormation screen. Use the provided CloudFormation template to create a stack. The template includes the configuration required to deploy the Agent to monitor your RDS instance.

## Further reading{% #further-reading %}

- [Setting up Postgres](https://docs.datadoghq.com/database_monitoring/setup_postgres/)
- [Setting Up Database Monitoring for Amazon RDS managed Postgres](https://docs.datadoghq.com/database_monitoring/setup_postgres/rds)
