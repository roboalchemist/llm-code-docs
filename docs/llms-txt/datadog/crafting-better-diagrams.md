# Source: https://docs.datadoghq.com/cloudcraft/getting-started/crafting-better-diagrams.md

---
title: 'Crafting Better Diagrams: Cloudcraft''s Live Diagramming and Filtering'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Cloudcraft (Standalone) > Getting started > Crafting Better Diagrams:
  Cloudcraft's Live Diagramming and Filtering
---

# Crafting Better Diagrams: Cloudcraft's Live Diagramming and Filtering

## Overview{% #overview %}

Cloudcraft is a powerful tool for creating diagrams of your cloud infrastructure. With the New Live Experience feature you can create accurate and up-to-date diagrams of your cloud infrastructure.

Filter resources by type and tags to create targeted diagrams that focus on the specific components you care about. This not only improves diagram performance and readability, but also allows you to craft more meaningful visualizations of your infrastructure.

In this guide, learn how to enable the new live experience and use it to create informative diagrams tailored to your needs.

## Prerequisites{% #prerequisites %}

Before you begin, you must connect your AWS or Azure account to Cloudcraft. For more information, see:

- [Connect your AWS account with Cloudcraft](https://docs.datadoghq.com/cloudcraft/getting-started/connect-aws-account-with-cloudcraft/)
- [Connect your Azure account with Cloudcraft](https://docs.datadoghq.com/cloudcraft/getting-started/connect-azure-account-with-cloudcraft/)

## Enable new live experience{% #enable-new-live-experience %}

To enable, toggle the **New Live Experience** switch at the top of the **Live** tab in Cloudcraft.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/crafting-better-diagrams/enable-new-experience.fd869fc6c9df6c4711bccbf6332e9e80.png?auto=format"
   alt="Screenshot highlighting the switch to enable the new live experience beta feature in the Cloudcraft interface with a red arrow pointing to the switch." /%}

If you're a new user, you may already have the New Live Experience enabled by default.

## Select account and region{% #select-account-and-region %}

Click the dropdown under the **Account** section and select the account you want to scan. If you only added one AWS or Azure account to Cloudcraft, it's automatically selected for you.

Under **Region**, select the regions you want to scan. By default, `Global` and your default region are selected, but you can click the **More** button to select or search for additional regions.

After you make your selections, regions are scanned automatically and the number of resources found is displayed next to the region name. You can click the **Sync** button above the **Region** section to trigger a manual scan of all selected regions.

{% alert level="danger" %}
Selecting many regions may impact performance of the live scanning process.
{% /alert %}

## Filter resources{% #filter-resources %}

You can filter resources by type and tags.

Tags are automatically detected from your AWS account and displayed in the **Custom tags**, **AWS tags**, **Terraform tags**, and **Kubernetes tags** sections.

- **Custom tags** are tags that you added to resources in AWS or Azure.
- **AWS tags** are tags that are automatically added to resources by AWS.
- **Terraform tags** are tags that are automatically added to resources by Terraform.
- **Kubernetes tags** are tags that are automatically added to resources by Kubernetes.

To filter resources by type, click the **Resource** section and select the resource type you want to filter by. By default, all resource types are selected and displayed in order of the number of resources found.

To filter resources by tags. Click the **Custom tags**, **AWS tags**, **Terraform tags**, or **Kubernetes tags** section and select the tags you want to filter by. By default, all tags are selected and ordered by the number of resources found, with `Untagged` always at the bottom.

{% alert level="info" %}
Focus on the most relevant resource types and tags for your specific use case to ensure optimal performance and readability of your diagram.
{% /alert %}

## Use cases{% #use-cases %}

### Create a diagram showing only EC2 instances and RDS databases{% #create-a-diagram-showing-only-ec2-instances-and-rds-databases %}

1. Click the **Resource** section.
1. Deselect all resource types, and select **EC2** and **RDS**.
1. Click **Apply layout** to create a diagram showing only the selected resources.

{% video
   url="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/crafting-better-diagrams/select-specific-resources.mp4" /%}

### Create a diagram showing EC2 instances and RDS databases without the `Environment` tag{% #create-a-diagram-showing-ec2-instances-and-rds-databases-without-the-environment-tag %}

1. Click the **Resource** section.
1. Deselect all resource types, and select **EC2** and **RDS**.
1. Click the **Custom tags** section.
1. Click the **Environment** tag, and leave only the `Untagged` option selected.
1. Click **Apply layout** to create a diagram showing only the selected resources without the `Environment` tag.

{% video
   url="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/crafting-better-diagrams/select-specific-resources-and-tags.mp4" /%}

## Feedback{% #feedback %}

Cloudcraft's New Live Experience is part of an ongoing effort to improve the user experience and make cloud infrastructure diagramming more efficient and effective. Tell us how you use these new features and [give feedback in this form](https://docs.google.com/forms/d/e/1FAIpQLSemnd5CJgrS9o-5ZCoZSxi99ATqIg9jpgqtcUZpMBzPJO75Wg/viewform).
