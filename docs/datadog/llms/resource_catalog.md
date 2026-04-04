# Source: https://docs.datadoghq.com/infrastructure/resource_catalog.md

---
title: Datadog Resource Catalog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# Datadog Resource Catalog

## Overview{% #overview %}

Datadog Resource Catalog is the central hub of all your infrastructure resources. It can help you manage resource compliance, investigate root causes for incidents, and close observability gaps on your infrastructure. With the Resource Catalog, you can understand key resource information such as metadata, ownership, configurations, relationship between assets, and active security risks for your resources.

Resource Catalog leverages Datadog cloud integrations and the Datadog Agent to gather data from cloud resources such as hosts, databases, and storage services.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/resource_catalog/resource_catalog_new_2.1439cc35b7ca64bc131547df70960468.png?auto=format"
   alt="The Resource Catalog page showing the Catalog tab, grouped by resource type" /%}

### Use Cases{% #use-cases %}

#### Resource policies and reporting{% #resource-policies-and-reporting %}

- Gain visibility into the compliance of your infrastructure with regards to ownership, versioning, migrations, and so on.
- Facilitate good tagging practices to optimize cross-telemetry insights.
- Reduce application risks by identifying and fixing security vulnerabilities in the dependencies of your services.
- Provide engineering leadership with a high-level view of security practices across teams and cloud accounts.
- Export resources for record-keeping or auditing.

#### Troubleshoot incidents and performance issues{% #troubleshoot-incidents-and-performance-issues %}

- Access telemetry, dashboards and other Datadog views with rich insights to understand the health and performance of your resources.
- Locate team and service owners of relevant resources to speed up incident recovery.
- View resource configuration changes to identify probable root causes.

#### Optimize observability{% #optimize-observability %}

- Spot resources that can be better monitored by Datadog and bridge observability gaps.
- Ensure proper security coverage by identifying resources that are most prone to misconfigurations or are not actively reporting security misconfigurations.

## Setup{% #setup %}

By default, when you navigate to the Resource Catalog, you are able to see Datadog Agent monitored hosts, as well as cloud resources crawled for other Datadog products such as CNM (Cloud Network Monitoring), and DBM (Database Monitoring). To view additional cloud resources in the Resource Catalog, toggle on **extend resource collection** from the [Resource Catalog](https://app.datadoghq.com/infrastructure/catalog/configuration) setup page.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/resource_catalog/resource_catalog_settings.dd0f7f391b49e67e34383e257df14c66.png?auto=format"
   alt="The Resource Catalog configuration page for extending resource collection" /%}

{% alert level="warning" %}
Enabling resource collection can impact your AWS CloudWatch costs. To avoid these charges, disable **Usage** metrics in the **Metric Collection** tab of the [Datadog AWS Integration](https://app.datadoghq.com/integrations/amazon-web-services).


{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/resource_catalog/aws_usage_toggle.29cf267747c34ec33d1420700500ba52.png?auto=format"
   alt="AWS Usage toggle in account settings" /%}

{% /alert %}



## Browse the Resource Catalog{% #browse-the-resource-catalog %}

On the [Resource Catalog page](https://app.datadoghq.com/infrastructure/catalog), explore the cloud resources in your Datadog organization. The catalog detects a resource either because it has an Agent installed on it, or because a cloud integration is configured on it.

### Catalog tab{% #catalog-tab %}

The Catalog tab shows context for a resource, including team ownership and related services. It helps you proactively identify and fill in missing ownership information before it's needed in an incident. The Resource Catalog also shows resource attributes customized for each resource type. You can search resources by specific attributes such as the instance type for a host, or the version for a database.

**Note**: If you use [Datadog Teams](https://docs.datadoghq.com/account_management/teams), select the **Teams** toggle on the left panel, then select the toggle for the teams to which you're assigned to view only the resources assigned to those teams. In addition, you can export your Resource Catalog list as a CSV file from the top right corner of the list.

To access the relevant cloud console for any resource in your list, click on a resource to open a side panel. Then, click the **Open Resource** dropdown in the top right corner to be redirected.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/resource_catalog/resource_catalog_sidepanel_2.0c2044622b9a11946017f2c00077449c.png?auto=format"
   alt="Resource Catalog side panel highlighting the Open Resource drop down" /%}

### Investigate a host or resource{% #investigate-a-host-or-resource %}

{% alert level="info" %}
No secrets are displayed in this panel. Any displayed "secrets" are randomly generated strings that do not pose a security risk.
{% /alert %}

Clicking on a host opens a side panel with details including:

- **Host information** such as the name, account, OS, instance type, tags, and metadata associated with the resource
- **Telemetry** including metrics, logs, traces, processes, and so on
- **Active monitor alerts** and enabled monitors status on the host
- **Agent configuration** information

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/resource_catalog/resource_catalog_host_side_panel.c6abb23b7ac8cddf10c23a551c898a1d.png?auto=format"
   alt="Resource Catalog with the host side panel open" /%}

Clicking on any resource opens a side panel with details including:

- **Resource information** such as the resource type, name, account, and tags associated with the resource.
- **Resource definition** in JSON showing the full configuration of the asset.
- **Recent Changes** showing a 7-day history of changes to the resource
- **Relationship** view showing interdependencies between resources
- **Service and team ownership** of the resource
- **Security risks** that the resource is exposed to, including misconfigurations, signals, identity risks, and vulnerabilities

## Resource Changes (in Preview){% #resource-changes-in-preview %}

{% callout %}
##### Join the Preview!

Resource Changes is in Preview. Click **Request Access** and complete the form to request access.

[Request Access](https://www.datadoghq.com/product-preview/recent-changes-tab/)
{% /callout %}

Resource Changes provides visibility and control over configuration changes to your cloud infrastructure. It helps you monitor modifications to resources, aiding in troubleshooting incidents and understanding the evolution of your environment.

For more information, see [Resource Changes](https://docs.datadoghq.com/infrastructure/resource_catalog/resource_changes/).

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/resource_catalog/resource-changes.ffd46b9efb6e21c355471807fb74b6fb.png?auto=format"
   alt="Datadog Resource Changes interface showing a list of infrastructure configuration changes. The screen displays a VM instance named \"vm-new-jmcintyre-kafka\" with a StorageProfile update, including a side-by-side diff view highlighting changes in JSON format. The table shows multiple resources with timestamps, change types (mostly \"UPDATE\"), and details of the modifications. Filters are available at the top for cloud, region, environment, and other attributes." /%}

## Further reading{% #further-reading %}

- [How Cambia Health Solutions saved $30,000 monthly with Cloud Cost Management and the Datadog Resource Catalog](https://www.datadoghq.com/blog/cambia-health-cost-optimization)
- [Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/)
- [Workload Protection](https://docs.datadoghq.com/security/threats/)
- [Govern your infrastructure resources with the Datadog Resource Catalog](https://www.datadoghq.com/blog/datadog-resource-catalog/)
- [Troubleshoot infrastructure issues faster with Recent Changes](https://www.datadoghq.com/blog/infrastructure-troubleshooting-recent-changes/)
