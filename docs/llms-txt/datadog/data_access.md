# Source: https://docs.datadoghq.com/account_management/rbac/data_access.md

---
title: Data Access Control
description: Define a Restricted Dataset for access control
breadcrumbs: Docs > Account Management > Access Control > Data Access Control
---

# Data Access Control

## Overview{% #overview %}

Your data in Datadog may contain sensitive data, and should be handled carefully. If you are ingesting sensitive data into Datadog, Data Access Control enables administrators and access managers within a Datadog organization to regulate access to this data. Use Data Access Control to identify sensitive data with a query and restrict access to only specific [Teams](https://docs.datadoghq.com/account_management/teams/) or [Roles](https://docs.datadoghq.com/account_management/rbac/?tab=datadogapplication#role-based-access-control).

When you define a *Restricted Dataset*, any data within the boundary of that dataset is restricted. Data outside of any Restricted Dataset remains unrestricted and accessible to users with appropriate permissions. Data Access Control provides an intuitive interface that allows access managers to grant only permitted users access to sensitive data enclosed within the datasets.

## Prerequisites{% #prerequisites %}

### Configure access controls{% #configure-access-controls %}

Data Access Control builds on your organization's existing Datadog access control configuration. Set up [Access Controls](https://docs.datadoghq.com/account_management/rbac/) first before configuring Data Access Control.

### Tag incoming data{% #tag-incoming-data %}

Data Access Control relies on tags and attributes in your data that can be used to define an access boundary. If you do not have tags defined, consider [Getting Started with Tags](https://docs.datadoghq.com/getting_started/tagging/) before configuring Data Access Control.

## Configure data access{% #configure-data-access %}

Data Access Control allows you to create a Restricted Dataset, specifying data that only users in designated teams or roles can access.

To view all of your Restricted Datasets, navigate to [Organization Settings](https://app.datadoghq.com/organization-settings/), and select [Data Access Controls](https://app.datadoghq.com/organization-settings/data-access-controls/) on the left, under the **Access** heading.

### Datadog site{% #datadog-site %}

Log in as a user assigned the Datadog Admin role, or any user with a role in your organization with the [`user_access_manage` permission](https://docs.datadoghq.com/account_management/rbac/permissions/#access-management).

1. Navigate to [Organization Settings](https://app.datadoghq.com/organization-settings/).
1. On the left side of the page, select [Data Access Controls](https://app.datadoghq.com/organization-settings/data-access-controls/).
1. Click **New Restricted Dataset**.

In order to create a Restricted Dataset, identify the data to be restricted with a query.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/rbac/restricted_dataset-2.85ef8382b812309224b8ab87dc63f201.png?auto=format"
   alt="Create a Restricted Dataset dialog. Selects data in RUM, APM, Logs, and Metrics matching the tag service:hr. Grants access to a Privileged access team." /%}

{% dl %}

{% dt %}
Name Dataset
{% /dt %}

{% dd %}
A descriptive name to help users understand what data is contained in the dataset.
{% /dd %}

{% dt %}
Select data to be included in this Dataset
{% /dt %}

{% dd %}
The boundary definition that describes which data to restrict to a specific set of users. Boundaries are query statements with limitations that allow an access manager to define the scope of sensitive data to be protected. The [supported telemetry types](https://docs.datadoghq.com/account_management/rbac/data_access/#supported-telemetry) are custom metrics, RUM sessions, APM traces, logs, cloud costs, error tracking issues, and Software Delivery repository info (CI Visibility pipelines).
{% /dd %}

{% dt %}
Grant access
{% /dt %}

{% dd %}
Select one or more teams or roles that may access the content bound in the Restricted Dataset. Any users who are not members of these groups are blocked from accessing this data.
{% /dd %}

{% /dl %}

You may create a maximum of 10 key:value pairs per Restricted Dataset. Consider defining an additional Restricted Dataset if you need additional pairs.

After completing all the fields to define the dataset, click **Create Restricted Dataset** to apply it to your organization.

You may create a maximum of 100 Restricted Datasets under the Enterprise plan, and a maximum of 10 datasets otherwise. If you need a higher limit, reach out to Support.

### Supported telemetry types{% #supported-telemetry %}

- APM traces
- Logs
- RUM sessions

The following are available as a Preview upon request:

- Cloud costs
- Custom metrics
  - **Note:** Standard and OpenTelemetry (OTel) metrics are not supported
- Error Tracking issues
- LLM Observability
- Software Delivery repository info (in CI Visibility pipelines)

## Usage constraints{% #usage-constraints %}

After you turn on Data Access Control, Datadog disables or limits other features to control access to sensitive data. See the list of affected features below to see how they are restricted.

### Real User Monitoring (RUM){% #real-user-monitoring-rum %}

#### Session Replay: Extended Retention{% #session-replay-extended-retention %}

By default, Session Replay data is retained for 30 days. To extend retention to 15 months, you can enable Extended Retention on individual session replays. When you create a restricted dataset for RUM, Datadog disables the option for Extended Retention.

#### Session Replay: Playlists{% #session-replay-playlists %}

Playlists are collections of Session Replays you can aggregate in a folder-like structure. When you create a restricted dataset for RUM, Datadog disables Session Replay Playlists.

### Logs{% #logs %}

Data Access Control is separate from the existing [Logs RBAC permissions](https://docs.datadoghq.com/logs/guide/logs-rbac/?tab=ui#restrict-access-to-logs) feature, also known as log restriction queries. Datadog recommends using a single solution to restrict logs data. If you limit user access using both Data Access Control and log restriction queries, both sets of restrictions apply.

### Monitors{% #monitors %}

Users can create monitors that query and alert on active telemetry. While the user can only directly query data they're allowed to access, the monitor operates as a system user with full access to data.

If you are concerned about unauthorized data access through monitors, Datadog recommends that you track the monitors your users create. Then, restrict access to the creation of monitors that read sensitive data.

### Software Delivery repository info (CI Visibility pipelines){% #software-delivery-repository-info-ci-visibility-pipelines %}

- **Supported telemetry**: Only CI Visibility pipelines are supported. Test Optimizations tests are not supported.
- **CI Logs**: CI Logs are stored in the Log Management product. To restrict access to CI Logs, create a Logs dataset.
- **Supported dataset tags**: Only the following tags are supported:
  - `@git.repository_url`
  - `@git.repository.id`
  - `@gitlab.groups`

## Select tags for access{% #select-tags-for-access %}

Each Restricted Dataset can control access to multiple types of data, such as metrics. You are free to use the same or different tags across multiple types of telemetry. Within each telemetry type, you must use a *single* tag or attribute to define your access strategy.

If you have too many combinations of tags or attributes to fit within these constraints, consider [revisiting your tagging](https://docs.datadoghq.com/getting_started/tagging/) to define a new tag that better reflects your access strategy.

### Supported example{% #supported-example %}

#### Restricted Dataset 1{% #restricted-dataset-1 %}

- Telemetry Type: RUM
  - Filters: `@application.id:ABCD`

#### Restricted Dataset 2{% #restricted-dataset-2 %}

- Telemetry type: RUM
  - Filters: `@application.id:EFGH`
- Telemetry type: Metrics
  - Filters: `env:prod`

### Not supported example{% #not-supported-example %}

#### Restricted Dataset 1:{% #restricted-dataset-1-1 %}

- Telemetry type: RUM
  - Filters: `@application.id:ABCD`

#### Restricted Dataset 2:{% #restricted-dataset-2-1 %}

- Telemetry type: RUM
  - Filters: `env:prod`

Restricted Dataset 1 uses `@application.id` as the tag for RUM data, so a new Restricted Dataset can't change to a different tag. Instead, consider reconfiguring Restricted Dataset 2 to use `@application.id`, or changing all of your Restricted Datasets with RUM data to use another tag.

### Not supported example{% #not-supported-example-1 %}

#### Restricted Dataset 1:{% #restricted-dataset-1-2 %}

- Telemetry type: RUM
  - Filters: `@application.id:ABCD`

#### Restricted Dataset 2:{% #restricted-dataset-2-2 %}

- Telemetry type: RUM
  - Filters: `@application.id:IJKL` `env:prod`

This example correctly uses the `@application.id` tag for RUM, as was done for Restricted Dataset 1. However, the limit is one tag per telemetry type. Instead, consider creating a Restricted Dataset with *either* `application.id` or `env`, or identify a different tag that better combines these attributes.

## Best practices{% #best-practices %}

### Access strategy{% #access-strategy %}

Before configuring Data Access Control, it's important to evaluate your access strategy. Consider reviewing [Reducing Data Related Risks](https://docs.datadoghq.com/data_security/) as you consider your access strategy. Removing or reducing unnecessary or sensitive data before it reaches Datadog reduces the need for additional access setup.

#### Protecting known sensitive data{% #protecting-known-sensitive-data %}

If you have already identified which data needs to be protected, you can build your Data Access Control configuration around only this specific data. This ensures that non-sensitive data is generally available to your users, allowing them to collaborate and understand ongoing issues or incidents.

For example, if you have a single application that is instrumented with Real User Monitoring (RUM) and captures sensitive inputs from users, consider creating a Restricted Dataset only for that application:

- **Name dataset:** Restricted RUM data
- **Select data to be included in this Dataset:**
  - Telemetry type: RUM
    - Filters: `@application.id:<rum-app-id>`
- **Grant access:**
  - Teams or roles of users who can see this RUM data

This configuration example would protect the RUM data from this application, and keep other data from this application available to existing users in your organization.

#### Protecting all data from a service{% #protecting-all-data-from-a-service %}

If you are instead looking to protect data from a specific service, you can build your Data Access Control configuration around the `service:` tag.

For example, if you have a service `NewService` that is instrumented with Real User Monitoring (RUM) and capturing sensitive inputs from users, consider creating a Restricted Dataset only for that application:

- **Name Dataset:** Restricted NewService data
- **Select data to be included in this Dataset:**
  - Telemetry type: RUM
    - Filters: `@service:NewService`
  - Telemetry type: Metrics
    - Filters: `@service:NewService`
  - Telemetry type: APM
    - Filters: `@service:NewService`
  - Telemetry type: Logs
    - Filters: `@service:NewService`
- **Grant access:**
  - Team who owns the service

This configuration example protects all supported data from `NewService`.

### Teams and roles{% #teams-and-roles %}

Data Access Control supports granting access to users through Datadog roles or teams. When granting access, consider your existing access control configuration and access strategy. If you are pursuing a service-based approach and are already [customizing the Software Catalog](https://docs.datadoghq.com/software_catalog/customize/), take advantage of the service ownership model by using Teams as part of your Data Access Control configuration.

**Note:** Teams used for Data Access Control must be configured such that adding or removing users can only be done by team members or an administrator, not `Anyone in the organization`.

## Access enforcement{% #access-enforcement %}

Users in a Datadog organization with Data Access Control enabled can only see query results for data to which they have access, such as in a Dashboard, in an Explorer, or through the API. A Restricted Dataset removes access to the data defined in the Restricted Dataset for users who are not permitted, across all Datadog experiences and entry points.

### Data explorers{% #data-explorers %}

When exploring Datadog with restrictions enabled, users without permissions can still browse the list of asset names (applications or metrics), but they cannot see query results, top tags, or facet details restricted by datasets. For instance, querying a metric with restricted data returns a blank graph, making it appear as if the query does not match any data.

### Dashboards and Notebooks{% #dashboards-and-notebooks %}

Similar to exploring data in a data explorer like the RUM Explorer or Metrics Explorer, viewing data in dashboards in an organization that has Restricted Datasets enabled only shows the data the user can access. Since dashboards are shared objects that can be accessed by others, it is possible for two users who have different access to view the same dashboard or notebook at the same time and see different data.

**Note**: Viewers of [Shared Dashboards](https://docs.datadoghq.com/dashboards/sharing/shared_dashboards/) see all telemetry data displayed in the Dashboard in accordance to the creator's permissions. Review your dashboard content before sharing to ensure no sensitive or confidential data is exposed.

### APIs{% #apis %}

When querying data through Datadog APIs with restrictions enabled, users without permissions do **not** see query results that have been restricted by Restricted Datasets.

## Further reading{% #further-reading %}

- [Reducing Data Related Risks](https://docs.datadoghq.com/data_security/)
