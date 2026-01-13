# Source: https://docs.datadoghq.com/cloudcraft/getting-started/using-bits-menu.md

---
title: Using the Bits menu
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > Getting started > Using the Bits menu
source_url: https://docs.datadoghq.com/getting-started/using-bits-menu/index.html
---

# Using the Bits menu

## Overview{% #overview %}

Using Cloudcraft's Bits menu, you can seamlessly move from any resource within Cloudcraft to the most relevant views in Datadog. This feature enables quick access to relevant information tailored to the specific resource you're examining. Whether it's logs, APM traces, or other data in Datadog, accessing it from your Cloudcraft diagram is a click away.

{% alert level="info" %}
To access this feature, log into Cloudcraft using your Datadog account. If you are logging in using another login method, [contact our support team](https://app.cloudcraft.co/app/support) for assistance.
{% /alert %}

## The Bits menu{% #the-bits-menu %}

Start by clicking on a supported component in your diagram. After you've selected a component, the Bits menu appears on the right-hand side of the screen.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/using-bits-menu/bits-menu.be9d9358b47d5d59d2ca885e7c8c78d7.png?auto=format"
   alt="Screenshot showing the Cloudcraft interface with a red arrow highlighting the Bits menu." /%}

Click on the Bits menu to view the available options for the selected component.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/using-bits-menu/bits-menu-clicked.807b20ebb01ce785f79346b40953b0fa.png?auto=format"
   alt="Screenshot of Cloudcraft with the Bits menu clicked showing several options, including Host dashboard, Database monitoring, Query metrics, and MySQL dashboard." /%}

Click on any of the options to open the relevant view in Datadog.

## Supported components{% #supported-components %}

The Bits menu is available for the following Cloudcraft components:

**From AWS:**

- Cloudfront.
- DocumentDB.
- DynamoDB.
- EBS.
- EC2.
- EKS Cluster.
- ELB/ALB.
- Elasticache.
- Lambda.
- NAT Gateway.
- OpenSearch.
- RDS.
- Redshift.
- S3.
- SNS Topic.
- SQS.
- VPC Endpoint.

**From Azure:**

- AKS Cluster.
- Database for MySQL.
- Database for PostgreSQL.
- Function App.
- Managed Disk.
- SQL Database.
- Virtual Machine.
- Web App.

Support for additional components is coming soon.

**Note**: To view telemetry in Datadog for a component, the component must have Datadog Agents or other integrations installed and configured.
