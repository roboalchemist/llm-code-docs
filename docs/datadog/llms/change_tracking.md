# Source: https://docs.datadoghq.com/change_tracking.md

---
title: Change Tracking
description: >-
  Streamline troubleshooting with Change Tracking by monitoring deployments,
  feature flags, configuration changes, and other modifications to your
  services.
breadcrumbs: Docs > Change Tracking
---

# Change Tracking

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Change Tracking is not available in the selected site ()
{% /alert %}


{% /callout %}

## Overview{% #overview %}

Change Tracking streamlines troubleshooting and incident response by surfacing relevant changes to your service and its dependencies, enabling faster detection and remediation when issues arise.

{% image
   source="https://datadog-docs.imgix.net/images/change_tracking/change-tracking-overview-2.7460117a5d61a37080f55551cdbe3e9b.png?auto=format"
   alt="The details of a change on the Recent Changes timeline in the Service Summary" /%}

Change Tracking supports monitoring of a range of modifications to your service and its dependencies including:

- Deployments
- [Feature Flags](https://docs.datadoghq.com/change_tracking/feature_flags)
- Traffic Spikes
- Configuration Changes
- Database Modifications
- Schema Changes
- Scale Adjustments
- Kubernetes Adjustments
- Kubernetes Pod Crashes
- Watchdog Alerts

For details on specific types of supported changes and setup requirements, see the Tracked changes section.

## Using Change Tracking{% #using-change-tracking %}

Change Tracking is available on several pages in Datadog:

### Monitor status page{% #monitor-status-page %}

View and analyze changes from the [monitor status page](https://docs.datadoghq.com/monitors/status/).

{% image
   source="https://datadog-docs.imgix.net/images/change_tracking/change-tracking-monitor-status-page-2.c7d68010060c5c8c82990d09f7877c73.png?auto=format"
   alt="Change Tracking displayed on the Monitor Status Page" /%}

#### Prerequisites{% #prerequisites %}

To use change tracking on the Monitor Status Page, ensure the appropriate service has been:

- Specified in the monitor query.
- Selected as part of a group.
- Added as a `service` tag on the monitor.

#### To analyze changes from the monitor status page:{% #to-analyze-changes-from-the-monitor-status-page %}

1. Go to the monitor status page for the monitor you are analyzing.
1. Locate the change tracking timeline at the top of the page.
   - For monitors with multiple graphs (dictated by the group by in the monitor query), filter to an individual group.
1. Use the timeline together with the event graphs to correlate change events with the alert.
1. Click the change indicator in the timeline to view more details about the change in the side panel.
1. From the side panel, you can investigate more details about the change and take the following actions:
   - View the deployment in your CI/CD system.
   - View the latest commits in your repository.
   - Compare changes between deployments to identify potential issues.
   - Configure additional custom links in the deployment side panel to quickly access other resources relevant to you.

### Services{% #services %}

View and analyze changes from the [service page](https://docs.datadoghq.com/tracing/services/service_page/).

{% image
   source="https://datadog-docs.imgix.net/images/change_tracking/change-tracking-service-page-2.f6bb2bd128568b667c967ce1dec2e906.png?auto=format"
   alt="Recent Changes component within the Service Summary section with dependency changes shown" /%}

#### To analyze changes from the service page:{% #to-analyze-changes-from-the-service-page %}

1. Navigate to the service page you want to investigate.
1. Locate the changes timeline in the **Service Summary** section.
1. Use the service and dependencies tabs to view either:
   - Changes limited to the specific service (**Changes by Service**)
   - Changes to the specific service and dependent services that might impact this service (**Changes by Service + Dependencies**)
1. Click the change indicator to view detailed information and take remediation actions.

### Dashboards{% #dashboards %}

View and analyze changes from any [dashboard](https://docs.datadoghq.com/dashboards/).

{% image
   source="https://datadog-docs.imgix.net/images/change_tracking/change-tracking-dashboard-show-overlays-active-2.2bec2599a8674444d50b796ff98f37c7.png?auto=format"
   alt="Change Tracking displayed on the Dashboard" /%}

#### Prerequisites{% #prerequisites-1 %}

To see relevant changes within the timeline and as overlays on your dashboard, ensure you have set at least one timeseries widget.

#### To analyze changes from dashboards:{% #to-analyze-changes-from-dashboards %}

1. Navigate to your dashboard.
1. Click **Show Overlays** at the top of the page to enable the change timeline and change overlays on supported widgets.
1. Hover over any change indicator or overlay to view a summary of the change.
1. Click the change indicator or overlay to view detailed information and take remediation actions.

### Widgets{% #widgets %}

In addition to the out-of-the-box integrations, Change Tracking is available as a data source for widgets across Datadog, including Dashboards and Notebooks.

{% image
   source="https://datadog-docs.imgix.net/images/change_tracking/change-tracking-datasource-examples.6de4bb5bbc078a6d29a7c4149c570de8.png?auto=format"
   alt="Change Tracking datasource examples" /%}

To configure a widget using Change Tracking data:

1. In a dashboard or notebook, add or edit a supported widget type (Timeseries, Query Value, Table, Tree Map, Top List, Pie, Change, or Bar Chart).
1. From the **data source** dropdown, select `Change Tracking`.
1. Configure your filters (**Service** is required).
1. (Optional) For widgets that support grouping, use **Group by** to split results.

{% image
   source="https://datadog-docs.imgix.net/images/change_tracking/change-tracking-datasource-edit-widget.4a8becf174362b04f38a62f30863a128.png?auto=format"
   alt="Change Tracking datasource widgets" /%}

For Timeseries widgets, you can also enable Change Tracking as an **Event Overlay**, which displays changes on top of the timeseries to help correlate them with metric behavior.

{% image
   source="https://datadog-docs.imgix.net/images/change_tracking/change-tracking-datasource-edit-overlay.73fe5f475f55f38922328434ee27c731.png?auto=format"
   alt="Change Tracking datasource as Event Overlay" /%}

#### View change details{% #view-change-details %}

To view information about a change or set of changes, click a datapoint in the widget and select **View Changes**. This opens the Change Tracking side panel with additional details.

## Tracked changes{% #tracked-changes %}

Change Tracking follows these types of changes across your infrastructure:

| Change Type                                                                                                                                                                                                                                   | Tracking Requirements                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code Deployments (APM)                                                                                                                                                                                                                        | APM & [Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/). A version must be available on the service.                                                                                                                                                                            |
| Kubernetes Deployment Manifest Updates                                                                                                                                                                                                        | Datadog Agent Set Up for Kubernetes (Add service label to Kubernetes yaml file if possible).                                                                                                                                                                                                                          |
| Feature Flags                                                                                                                                                                                                                                 | Use the LaunchDarkly integration or send custom events using the Events API. See the [Feature Flag Tracking documentation](https://docs.datadoghq.com/change_tracking/feature_flags) for setup and advanced options.                                                                                                  |
| Custom Configuration Change Events                                                                                                                                                                                                            | [Event Management API](https://docs.datadoghq.com/api/latest/events/).                                                                                                                                                                                                                                                |
| Watchdog Alerts (Error Rate Spikes, Latency Spikes, Cloud and API Outages, etc.)                                                                                                                                                              | See [Watchdog](https://docs.datadoghq.com/watchdog/) documentation to learn more about requirements for specific Watchdog Alerts.                                                                                                                                                                                     |
| Traffic Spikes (APM)                                                                                                                                                                                                                          | [Application Performance Monitoring (APM)](https://docs.datadoghq.com/tracing)                                                                                                                                                                                                                                        |
| CrashLoopBackOff Kubernetes Pod Crashes                                                                                                                                                                                                       | Kubernetes Integration (Add service label to Kubernetes yaml file if possible).                                                                                                                                                                                                                                       |
| PostgreSQL, SQL Server and MySQL Database Table (Schemas) Change                                                                                                                                                                              | See [Exploring Database Schemas](https://docs.datadoghq.com/database_monitoring/schema_explorer) documentation to learn more about tracking schemas using DBM, and [Correlate Database Monitoring and Traces](https://docs.datadoghq.com/database_monitoring/connect_dbm_and_apm/) to set up APM and DBM correlation. |
| MongoDB Index & SearchIndex Changes                                                                                                                                                                                                           | [Database Monitoring (DBM)](https://docs.datadoghq.com/database_monitoring/), [Correlate Database Monitoring and Traces](https://docs.datadoghq.com/database_monitoring/connect_dbm_and_apm/).                                                                                                                        |
| PostgreSQL Database Settings Change                                                                                                                                                                                                           | [Database Monitoring (DBM)](https://docs.datadoghq.com/database_monitoring/), [Correlate Database Monitoring and Traces](https://docs.datadoghq.com/database_monitoring/connect_dbm_and_apm/).                                                                                                                        |
| SQL Server Database Settings Change                                                                                                                                                                                                           | [Database Monitoring (DBM)](https://docs.datadoghq.com/database_monitoring/), [Correlate Database Monitoring and Traces](https://docs.datadoghq.com/database_monitoring/connect_dbm_and_apm/).                                                                                                                        |
| Kafka Schema Updates                                                                                                                                                                                                                          | [Data Streams Monitoring (DSM)](https://docs.datadoghq.com/data_streams/).                                                                                                                                                                                                                                            |
| Manual Kubernetes Deployment Scale Events                                                                                                                                                                                                     | Kubernetes Audit Logging.                                                                                                                                                                                                                                                                                             |
| Cloud Infrastructure Resource Changes (in Preview (This feature is in Preview and currently limited to a small sample of cloud resource changes. To request access, see the Resource Changes documentation linked in Tracking Requirements.)) | [Resource Changes](https://docs.datadoghq.com/infrastructure/resource_catalog/resource_changes/) - Enable Resource Collection and optionally cloud provider event forwarding.                                                                                                                                         |

## Further reading{% #further-reading %}

- [Monitor Status Page](https://docs.datadoghq.com/monitors/status/)
- [Dashboards](https://docs.datadoghq.com/dashboards/)
- [Service Page](https://docs.datadoghq.com/tracing/services/service_page/)
- [Event Management API](https://docs.datadoghq.com/api/latest/events/)
- [Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/)
- [LaunchDarkly](https://docs.datadoghq.com/integrations/launchdarkly/#feature-flag-tracking-integration/)
- [Watchdog](https://docs.datadoghq.com/watchdog/)
- [Database Monitoring](https://docs.datadoghq.com/database_monitoring/)
- [Data Streams Monitoring](https://docs.datadoghq.com/data_streams/)
- [Unify visibility into changes to your services and dependencies](https://www.datadoghq.com/blog/change-tracking/)
