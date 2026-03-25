# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/statuspage.md

# Statuspage

![](/img/guides/icons/StatusPage.svg)![](/img/guides/icons/StatusPage.svg)

Loading version...

Port's Statuspage integration allows you to model Statuspage resources in your software catalog and ingest data into them.

Supported resources ![](/img/icons/external-link.svg)[Page](https://developer.statuspage.io/#tag/pages)[Component Group](https://developer.statuspage.io/#tag/component-groups)[Component](https://developer.statuspage.io/#tag/components)[Incident](https://developer.statuspage.io/#tag/incidents)[Incident Update](https://developer.statuspage.io/#tag/incident-updates)

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* A Statuspage account with permissions to create API keys.
* Your Port user role is set to `Admin`.

## Setup[â](#setup "Direct link to Setup")

Choose your preferred installation method below. Not sure which to pick? See the [installation methods overview](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

1Choose method2Install

Hosted by Port

* â§Port hosts and manages the integration
* â§Customizable resync interval for data ingestion
* â§Access control flexibility

Self-hosted

* â§Host and manage the integration in your infrastructure
* â§Real-time updates via webhooks
* â§Best for high-security or custom networking needs

CI

* â§Run as a one-time job in your CI pipeline or on a scheduled basis
* â§Minimal infrastructure management

Install

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration for this integration:

**Default mapping configuration (Click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
- kind: statuspage
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"statuspage"'
        properties:
          page_description: .page_description
          headline: .headline
          branding: .branding
          status_indicator: .status_indicator
          status_description: .status_description
          subdomain: .subdomain
          domain: .domain
          url: .url
          allow_page_subscribers: .allow_page_subscribers
          allow_incident_subscribers: .allow_incident_subscribers
          allow_email_subscribers: .allow_email_subscribers
          allow_sms_subscribers: .allow_sms_subscribers
          allow_rss_atom_feeds: .allow_rss_atom_feeds
          allow_webhook_subscribers: .allow_webhook_subscribers
          time_zone: .time_zone
          createdAt: .created_at
          updatedAt: .updated_at
- kind: component_group
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"statuspageComponentGroup"'
        properties:
          description: .description
          position: .position
          createdAt: .created_at
          updatedAt: .updated_at
        relations:
          statuspage: .page_id
- kind: component
  selector:
    query: .group == false
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"statuspageComponent"'
        properties:
          description: .description
          position: .position
          status: .status
          showcase: .showcase
          only_show_if_degraded: .only_show_if_degraded
          startDate: .start_date | if . == null then null else (strptime("%Y-%m-%d") | todateiso8601) end
          createdAt: .created_at
          updatedAt: .updated_at
        relations:
          componentGroup: .group_id
          statuspage: .page_id
- kind: incident
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"statuspageIncident"'
        properties:
          status: .status
          impact: .impact
          createdAt: .created_at
          updatedAt: .updated_at
          startedAt: .started_at
          resolvedAt: .resolved_at
          shortlink: .shortlink
          scheduled_for: .scheduled_for
          scheduled_until: .scheduled_until
          scheduled_remind_prior: .scheduled_remind_prior
          scheduled_reminded_at: .scheduled_reminded_at
          impact_override: .impact_override
          scheduled_auto_in_progress: .scheduled_auto_in_progress
          scheduled_auto_completed: .scheduled_auto_completed
          metadata: .metadata
          reminder_intervals: .reminder_intervals
          postmortem_body: .postmortem_body
          postmortem_body_last_updated_at: .postmortem_body_last_updated_at
          postmortem_ignored: .postmortem_ignored
          postmortem_published_at: .postmortem_published_at
          postmortem_notified_subscribers: .postmortem_notified_subscribers
          postmortem_notified_twitter: .postmortem_notified_twitter
        relations:
          components: '[.components[].id]'
          statuspage: .page_id
- kind: incident_update
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .body
        blueprint: '"statuspageIncidentUpdate"'
        properties:
          status: .status
          body: .body
          createdAt: .created_at
          displayAt: .display_at
          deliverNotifications: .deliver_notifications
          wantsTwitterUpdate: .wants_twitter_update
          tweet_id: .tweet_id
          custom_tweet: .custom_tweet
        relations:
          incident: .incident_id
          affectedComponents: '[.affected_components[].code]'
```

## Mapping & examples per resource[â](#mapping--examples-per-resource "Direct link to Mapping & examples per resource")

Use the explorer below to view sample payloads and the resulting Port entities for each resource type. For additional resources and advanced configurations, see the [examples page](/build-your-software-catalog/sync-data-to-catalog/incident-management/statuspage/examples.md).

PageComponent GroupComponentIncidentIncident Update

Default mappingYAML

Sample payloadJSON

Port entityJSON

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

For blueprint and configuration examples across all supported resource kinds, see the [Statuspage examples page](/build-your-software-catalog/sync-data-to-catalog/incident-management/statuspage/examples.md).

To view and test the integration's mapping against live API responses, use the **jq playground** in your [data sources page](https://app.getport.io/settings/data-sources).
