# Source: https://docs.datadoghq.com/datadog_cloudcraft.md

---
title: Cloudcraft in Datadog
description: >-
  Visualize and analyze AWS and Azure cloud infrastructure with live Cloudcraft
  diagrams in Datadog for troubleshooting, security analysis, and cost
  optimization.
breadcrumbs: Docs > Cloudcraft in Datadog
---

# Cloudcraft in Datadog

## Overview{% #overview %}

Cloudcraft offers a powerful, live read-only visualization tool for cloud architecture, enabling you to explore, analyze, and manage your infrastructure with ease. Not to be confused with the [Standalone Cloudcraft documentation](https://docs.datadoghq.com/cloudcraft), this guide outlines the functionality, setup, and use cases of Cloudcraft *in Datadog*, detailing its benefits for various user personas, and highlighting key features and capabilities.

{% alert level="info" %}
This documentation applies to the Cloudcraft *in Datadog* product. For information on the standalone Cloudcraft product, please refer to the [Cloudcraft (Standalone)](https://docs.datadoghq.com/cloudcraft) documentation.
{% /alert %}

Cloudcraft's core functionality is its ability to generate detailed architecture diagrams. These diagrams visually represent AWS and Azure cloud resources, allowing you to explore and analyze your environments. Cloudcraft's diagrams are optimized for clarity and performance, providing an intuitive interface for navigating large-scale deployments. This helps teams to:

- Trace incidents back to their root causes through infrastructure dependencies.
- Determine if infrastructure is the cause of an incident, such as cross-region traffic causing latency or increased costs.
- Analyze and address the most relevant security misconfigurations.
- Onboard new team members.
- Accelerate incident MTTR and proactive governance tasks by simplifying infrastructure navigation.

{% video
   url="https://datadog-docs.imgix.net/images/datadog_cloudcraft/cloudcraft_with_azure_tab_2.mp4" /%}

{% alert level="info" %}
Cloudcraft in Datadog is only available for AWS and Azure accounts.
{% /alert %}

## Prerequisites{% #prerequisites %}

{% tab title="AWS" %}

- To access Cloudcraft in Datadog, you need the `cloudcraft_read` permission.

- [Resource collection](https://docs.datadoghq.com/integrations/amazon_web_services/#resource-collection) must be enabled for your AWS accounts.

- For the best experience, Datadog strongly recommends using the AWS-managed [`SecurityAudit`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SecurityAudit.html) policy, or the more permissive [`ReadOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ReadOnlyAccess.html) policy.

- Viewing content on the [Security overlay](https://docs.datadoghq.com/datadog_cloudcraft/overlays#security) requires additional products to be enabled:

  - To view security misconfigurations and identity risks, [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management) must be enabled.
  - To view sensitive data, [Sensitive Data Scanner](https://docs.datadoghq.com/security/sensitive_data_scanner) must be enabled. For a user to turn the layer on, they must have the [`data_scanner_read`](https://docs.datadoghq.com/account_management/rbac/permissions/#compliance) permission.

**Note**: Cloudcraft adapts to restrictive permissions by excluding inaccessible resources. For example, if you don't grant permission to list S3 buckets, the diagram excludes those buckets. If permissions block certain resources, an alert displays in the UI.

{% alert level="warning" %}
Enabling resource collection can impact your AWS CloudWatch costs. To avoid these charges, disable **Usage** metrics in the **Metric Collection** tab of the [Datadog AWS Integration](https://app.datadoghq.com/integrations/amazon-web-services).
{% /alert %}

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/resource_catalog/aws_usage_toggle.29cf267747c34ec33d1420700500ba52.png?auto=format"
   alt="The Usage service highlighted in the Metric Collection tab of the AWS integration tile" /%}

{% /tab %}

{% tab title="Azure" %}

- To access Cloudcraft in Datadog, you need the `cloudcraft_read` permission.

- You need the Datadog Admin Role, or any role with the `azure_configurations_manage` permission. See the [Azure setup](https://docs.datadoghq.com/integrations/guide/azure-manual-setup/?tab=azurecli#setup) instructions for more information.

- Enable [resource collection](https://docs.datadoghq.com/getting_started/integrations/azure/) for your Azure accounts:

  1. Navigate to [**Integrations > Azure**](https://app.datadoghq.com/integrations/azure).
  1. Add your Azure subscription by selecting **+ Add New App Registration** if not already added.
  1. Select the App Registration containing your Azure subscription.
  1. On the Resource Collection tab, ensure the **Enable Resource Collection** toggle is enabled.

- Viewing content on the [Security overlay](https://docs.datadoghq.com/datadog_cloudcraft/overlays#security) requires additional products to be enabled:

  - To view security misconfigurations and identity risks, [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management) must be enabled.
  - To view sensitive data, [Sensitive Data Scanner](https://docs.datadoghq.com/security/sensitive_data_scanner) must be enabled. For a user to turn the layer on, they must have the [`data_scanner_read`](https://docs.datadoghq.com/account_management/rbac/permissions/#compliance) permission.

{% /tab %}

## Getting started{% #getting-started %}

To get started using Cloudcraft, use the following steps:

1. Navigate to [**Infrastructure > Resources > Cloudcraft**](https://app.datadoghq.com/cloud-maps).
1. A real-time diagram of the resources is displayed in your environment.

**Note**: If your environment has more than 10,000 resources, filter the diagram by account, region, or tags to display it.

{% image
   source="https://datadog-docs.imgix.net/images/datadog_cloudcraft/getting_started.866db85b6e982b1b9a93edf691fc3583.png?auto=format"
   alt="Getting started in Cloudcraft, displaying a list of resources for the selected account and region" /%}
The account name in the **Account** dropdown comes from your AWS account tags in the AWS integration tile. For Azure, the **Subscription** name comes from the subscription name in your Azure integration tile's list of managed subscriptions.
### Group By{% #group-by %}

With Group By, Cloudcraft divides your diagram into distinct sections based on different group types. This feature offers a clear and organized perspective of your resources, making it especially helpful for visualizing complex cloud environments.

Enable the **Show All Controls** toggle to display the available **Group By** options. You can remove specific groupings by unchecking options like VPC and Region. To view the current nesting structure and add the Network ACL (Network Access Control List) layer, click the **+ Tags** menu.

{% image
   source="https://datadog-docs.imgix.net/images/datadog_cloudcraft/cloudcraft_group_by_with_network_acl.daae8bc3f2aabf5c98a987fbe68faf77.png?auto=format"
   alt="Group by feature in Cloudcraft, highlighting the Group By menu." /%}

#### Group by tags{% #group-by-tags %}

You can group resources by AWS and Azure tags, such as app, service, team, or cost center, to organize your view by team or workload. When grouping by tags, color-coded labels are displayed on each group. When grouping by the `service` tag, a raised block is displayed to visually indicate the service grouping.

**Note**: Grouping by tags is supported for AWS and Azure tags only. Tags from the Datadog Agent (for example, locally configured `env` or `team` tags) are not supported.

{% image
   source="https://datadog-docs.imgix.net/images/datadog_cloudcraft/cloudcraft_group_by_with_team_tags.8dae7903501789bd0a608d8d7846c852.png?auto=format"
   alt="Cloudcraft landing page with Group by highlighted, and grouping by Team" /%}

### Saved views{% #saved-views %}

Saved views allow you to save specific filters on your diagram that are most important to you, enabling efficient troubleshooting with scoped queries on your accounts, regions, environments, and resources.

To apply a saved view to your diagram:

- Navigate to [**Infrastructure > Resources > Cloudcraft**](https://app.datadoghq.com/cloud-maps). Select one or more accounts, regions, and resources. Apply any desired filters to your saved view, then click **+Save as new view**.
- Select the desired saved view from the menu at the top of the diagram view. The diagram automatically updates to reflect the chosen view.

{% image
   source="https://datadog-docs.imgix.net/images/datadog_cloudcraft/saved_views.6111f6ddda3a4087ddab2f2923944d9f.png?auto=format"
   alt="Screenshot of the saved views" /%}

### Explore resources{% #explore-resources %}

Use the zoom and hover features to pinpoint the most critical resources. As you zoom in, additional resource names become visible. Hovering over a resource displays a panel with basic information, while clicking on a resource opens a side panel with observability, cost, and security data, along with cross-links to other relevant Datadog products.

{% video
   url="https://datadog-docs.imgix.net/images/datadog_cloudcraft/cloudcraft_with_security_2.mp4" /%}

#### Projection toggle{% #projection-toggle %}

Toggle the projection from 3D (default) to 2D to visualize your resources from a top-down view.

{% image
   source="https://datadog-docs.imgix.net/images/datadog_cloudcraft/cloudcraft_2D_2.3f4ddffcf1c43cb3dd2c3dd79607a53b.png?auto=format"
   alt="Cloudcraft landing page with the 2D toggle enabled" /%}

### Filtering and search{% #filtering-and-search %}

Diagrams can be filtered by tags, such as team, application, or service, allowing you to concentrate on relevant resources while maintaining context through connected resources. Additionally, Cloudcraft provides a powerful search and highlight feature, enabling ease of location of specific resources or groups of resources.

Click the **+ Filter** menu to filter your resources by commonly used tags such as service, team, region, and more. Additionally, click the **More Filters** option to filter by AWS and Azure tags, custom tags, and Terraform tags. The filter option reloads the diagram to display only the infrastructure that matches the filter criteria.

### Search and highlight{% #search-and-highlight %}

Use the search bar to locate resources on the diagram by name, ID, or tag. This feature is effective for finding specific resources within your cloud architecture. It highlights the search criteria in the diagram, without creating a new diagram, by greying out the elements that do not match the search criteria.

{% video
   url="https://datadog-docs.imgix.net/images/datadog_cloudcraft/search_highlight_4.mp4" /%}

## Permissions{% #permissions %}

To access Cloudcraft in Datadog, you need the `cloudcraft_read` permission. This permission is included in the Datadog Read Only Role by default. If your organization uses custom roles, add this permission to the appropriate role. For more information on managing permissions, see the [RBAC documentation](https://docs.datadoghq.com/account_management/rbac/permissions/#infrastructure).

## Next steps{% #next-steps %}

Learn how to navigate between [built-in overlays](https://docs.datadoghq.com/datadog_cloudcraft/overlays) to view your architecture from different perspectives. Each overlay is designed to support specific operational goals, such as:

- [Infrastructure](https://docs.datadoghq.com/datadog_cloudcraft/overlays#infrastructure): High-level view of services and resources.
- [Observability](https://docs.datadoghq.com/datadog_cloudcraft/overlays#observability): Indicates which hosts have the Agent installed and what observability features are enabled.
- [Security](https://docs.datadoghq.com/datadog_cloudcraft/overlays#security): IAM, firewall, and security group visibility.
- [Cloud Cost Management](https://docs.datadoghq.com/datadog_cloudcraft/overlays#cloud-cost-management): Track and optimize resource spend.

## Further reading{% #further-reading %}

- [Plan new architectures and track your cloud footprint with Cloudcraft (Standalone)](https://www.datadoghq.com/blog/cloud-architecture-diagrams-cost-compliance-cloudcraft-datadog/)
- [Create rich, up-to-date visualizations of your AWS infrastructure with Cloudcraft in Datadog](https://www.datadoghq.com/blog/introducing-cloudcraft/)
- [Visually identify and prioritize security risks using Cloudcraft](https://www.datadoghq.com/blog/cloudcraft-security/)
