# Source: https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/investigator.md

---
title: Investigator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud SIEM > Triage and Investigate > Investigator
---

# Investigator

## Overview{% #overview %}

When a security signal alerts on suspicious activity by a user or a resource, some commonly asked questions during the investigation include:

- Is the user accessing other accounts?
- What other actions did the user take around that specific time frame?
- What are all the actions taken on a resource by the user?
- What users have interacted with this resource?

For example, suppose you receive a security signal that someone changed the configuration of an Amazon S3 bucket so that it is accessible by everyone, but the action was taken by an assumed role. To investigate, look into who took the action and what other activities they did recently, as that could indicate compromised credentials.

The Cloud SIEM Investigator provides a graphical interface for you to pivot from one affected entity to another, so that you can see user behavior and its impact on your environment.

## Visualize and investigate the activity{% #visualize-and-investigate-the-activity %}

{% tab title="AWS" %}

1. Navigate to **Security** > **Cloud SIEM** and click the **Investigate** tab, and then the [**AWS Investigator**](https://app.datadoghq.com/security/siem/investigator?provider=aws) tab.

1. Select an entity type in the **In** field dropdown menu.

1. Select an entity or enter a specific entity name in the **Investigate** field to see a diagram of the activities associated with the entity.

1. Click on a node and select **View related logs** or **View related signals** to investigate further. Use the **Search for** dropdown menu to filter by actions.

{% /tab %}

{% tab title="GCP" %}

1. Navigate to **Security** > **Cloud SIEM** and click the **Investigate** tab, and then the [**GCP Investigator**](https://app.datadoghq.com/security/siem/investigator?provider=gcp) tab.

1. Select an entity type in the **In** field dropdown menu.

1. Select an entity or enter a specific entity name in the **Investigate** field to see a diagram of the activities associated with the entity.

1. Click on a node and select **View related logs** or **View related signals** to investigate further. Use the **Search for** dropdown menu to filter by actions.

{% /tab %}

{% tab title="Azure" %}

1. Navigate to **Security** > **Cloud SIEM** and click the **Investigate** tab, and then the [**Azure Investigator**](https://app.datadoghq.com/security/siem/investigator?provider=azure) tab.

1. Select an entity type in the **In** field dropdown menu.

1. Select an entity or enter a specific entity name in the **Investigate** field to see a diagram of the activities associated with the entity.

1. Click on a node and select **View related logs** or **View related signals** to investigate further. Use the **Search for** dropdown menu to filter by actions.

{% /tab %}

{% tab title="Datadog" %}

1. Navigate to **Security** > **Cloud SIEM** and click the **Investigate** tab, and then the [**Datadog Investigator**](https://app.datadoghq.com/security/siem/investigator?provider=datadog) tab.

1. Select an entity type in the **In** field dropdown menu.

1. Select an entity or enter a specific entity name in the **Investigate** field to see a diagram of the activities associated with the entity.

1. Click on a node and select **View related Audit Trail** or **View related signals** to investigate further. Use the **Search for** dropdown menu to filter by actions.

{% /tab %}

You can also navigate to the Cloud SIEM Investigator directly from a security signal. In the security signal panel, click **Investigate user activity** (where `user` is the user identity in question) to see the Investigator view filtered to the specific user identity.

## Further reading{% #further-reading %}

- [Configure AWS for Cloud SIEM](https://docs.datadoghq.com/security/cloud_siem/guide/aws-config-guide-for-cloud-siem/)
- [Learn about the Security Signals Explorer](https://docs.datadoghq.com/cloud_siem/explorer/)
- [Visualize activity in your cloud environment with Datadog Cloud SIEM Investigator](https://www.datadoghq.com/blog/visualize-cloud-activity-datadog-cloud-siem-investigator/)
