# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/opsgenie.md

# Opsgenie

![](/img/guides/icons/OpsGenie.svg)![](/img/guides/icons/OpsGenie.svg)

Loading version...

Port's Opsgenie integration allows you to model Opsgenie resources in your software catalog and ingest data into them.

Supported resources ![](/img/icons/external-link.svg)[Alert](https://docs.opsgenie.com/docs/alert-api#list-alerts)[Incident](https://docs.opsgenie.com/docs/incident-api#list-incidents)[Service](https://docs.opsgenie.com/docs/service-api#list-services)[User](https://docs.opsgenie.com/docs/user-api#list-user)[Team](https://docs.opsgenie.com/docs/team-api#list-teams)[Schedule](https://docs.opsgenie.com/docs/schedule-api#list-schedules)[Schedule-Oncall](https://docs.opsgenie.com/docs/who-is-on-call-api#get-on-calls)

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired Opsgenie resources and their metadata in Port (see supported resources below).
* Watch for Opsgenie object changes (create/update/delete) in real-time, and automatically apply the changes to your entities in Port.

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods: Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

1Choose method2Install

Hosted by Port (Recommended)

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

## Capabilities[â](#capabilities "Direct link to Capabilities")

### Configure real-time updates[â](#configure-real-time-updates "Direct link to Configure real-time updates")

Currently, the OpsGenie API lacks support for programmatic webhook creation. To set up a webhook configuration in OpsGenie for sending alert notifications to the Ocean integration, follow these steps:

#### Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Prepare a webhook `URL` using this format: `{app_host}/integration/webhook`. The `app_host` parameter should match the ingress or external load balancer where the integration will be deployed. For example, if your ingress or load balancer exposes the OpsGenie Ocean integration at `https://myservice.domain.com`, your webhook `URL` should be `https://myservice.domain.com/integration/webhook`.

#### Create a webhook in OpsGenie[â](#create-a-webhook-in-opsgenie "Direct link to Create a webhook in OpsGenie")

1. Go to OpsGenie.

2. Select **Settings**.

3. Click on **Integrations** under the **Integrations** section of the sidebar.

4. Click on **Add integration**.

5. In the search box, type *Webhook* and select the webhook option.

6. Input the following details:

   <!-- -->

   1. `Name` - use a meaningful name such as Port Ocean Webhook.

   2. Be sure to keep the "Enabled" checkbox checked.

   3. Check the "Add Alert Description to Payload" checkbox.

   4. Check the "Add Alert Details to Payload" checkbox.

   5. Add the following action triggers to the webhook by clicking on **Add new action**:

      <!-- -->

      1. If *alert is snoozed* in Opsgenie, *post to url* in Webhook.
      2. If *alert's description is updated* in Opsgenie, *post to url* in Webhook.
      3. If *alert's message is updated* in Opsgenie, *post to url* in Webhook.
      4. If *alert's priority is updated* in Opsgenie, *post to url* in Webhook.
      5. If *a responder is added to the alert* in Opsgenie, *post to url* in Webhook.
      6. if *a user executes "Assign Ownership* in Opsgenie, *post to url* in Webhook.
      7. if *a tag is added to the alert* in Opsgenie, *post to url* in Webhook.
      8. .if *a tag is removed from the alert* in Opsgenie, *post to url* in Webhook.

   6. `Webhook URL` - enter the value of the `URL` you created above.

7. Click **Save integration**.

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration for this integration:

**Default mapping configuration (Click to expand)**

```
deleteDependentEntities: true
createMissingRelatedEntities: true
enableMergeEntity: true
resources:
- kind: team
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"opsGenieTeam"'
        properties:
          description: .description
          url: .links.web
- kind: schedule
  selector:
    query: 'true'
    apiQueryParams:
      expand: rotation
  port:
    entity:
      mappings:
        identifier: .id + "_" + .item.id
        title: .name + "_" + .item.name
        blueprint: '"opsGenieSchedule"'
        properties:
          timezone: .timezone
          description: .description
          startDate: .item.startDate
          endDate: .item.endDate
          rotationType: .item.type
        relations:
          owner_opsgenie_team: .ownerTeam.id
          schedule_opsgenie_users: '[.item.participants[] | select(has("username")) | .username]'
          schedule_users:
            combinator: '"and"'
            rules:
            - property: '"_opsGenieUserId"'
              operator: '"in"'
              value: '[.item.participants[] | select(has("username")) | .username]'
    itemsToParse: .rotations
- kind: service
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"opsGenieService"'
        properties:
          description: .description
          url: .links.web
          tags: .tags
        relations:
          owner_opsgenie_team: .teamId
- kind: alert
  selector:
    query: 'true'
    apiQueryParams:
      status: open
  port:
    entity:
      mappings:
        identifier: .id
        title: .message
        blueprint: '"opsGenieAlert"'
        properties:
          status: .status
          acknowledged: .acknowledged
          priority: .priority
          sourceName: .source
          tags: .tags
          count: .count
          createdBy: .owner
          createdAt: .createdAt
          updatedAt: .updatedAt
          description: .description
          integration: .integration.name
        relations:
          relatedIncident: if (.alias | contains("_")) then (.alias | split("_")[0]) else null end
          responding_opsgenie_team: .responders | [.[] | select(.type == "team") | .id]
          responding_team:
            combinator: '"and"'
            rules:
            - property: '"opsgenie_team_id"'
              operator: '"in"'
              value: .responders | [.[] | select(.type == "team") | .id]
          responding_opsgenie_user: .responders | [.[] | select(.type == "user") | .id]
          responding_user:
            combinator: '"and"'
            rules:
            - property: '"_opsGenieUserId"'
              operator: '"in"'
              value: .responders | [.[] | select(.type == "user") | .id]
- kind: incident
  selector:
    query: 'true'
    apiQueryParams:
      status: open
  port:
    entity:
      mappings:
        identifier: .id
        title: .message
        blueprint: '"opsGenieIncident"'
        properties:
          status: .status
          priority: .priority
          tags: .tags
          url: .links.web
          createdAt: .createdAt
          updatedAt: .updatedAt
          description: .description
        relations:
          impacted_opsgenie_services: .impactedServices
          impacted_services:
            combinator: '"and"'
            rules:
            - property: '"_opsGenieServiceId"'
              operator: '"in"'
              value: .impactedServices
          responding_opsgenie_team: .responders | [.[] | select(.type == "team") | .id]
          responding_team:
            combinator: '"and"'
            rules:
            - property: '"opsgenie_team_id"'
              operator: '"in"'
              value: .responders | [.[] | select(.type == "team") | .id]
          responding_opsgenie_user: .responders | [.[] | select(.type == "user") | .id]
          responding_user:
            combinator: '"and"'
            rules:
            - property: '"_opsGenieUserId"'
              operator: '"in"'
              value: .responders | [.[] | select(.type == "user") | .id]
- kind: schedule-oncall
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .ownerTeam.id
        title: .ownerTeam.name
        blueprint: '"opsGenieTeam"'
        properties:
          oncallUsers: .__currentOncalls.onCallRecipients
        relations:
          schedule_opsgenie_users: .__currentOncalls.onCallRecipients
          schedule_users:
            combinator: '"and"'
            rules:
            - property: '"_opsGenieUserId"'
              operator: '"in"'
              value: .__currentOncalls.onCallRecipients
- kind: user
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .fullName
        blueprint: '"opsGenieUser"'
        properties:
          email: .username
          role: .role.name
          timeZone: .timeZone
          isVerified: .verified
          isBlocked: .blocked
          address: .userAddress
          createdAt: .createdAt
```

## Mapping & examples per resource[â](#mapping--examples-per-resource "Direct link to Mapping & examples per resource")

Use the explorer below to view sample payloads and the resulting Port entities for each resource type. For additional resources and advanced configurations, see the [examples page](/build-your-software-catalog/sync-data-to-catalog/incident-management/opsgenie/examples.md).

AlertIncidentServiceUserTeamScheduleSchedule-Oncall

Default mappingYAML

Sample payloadJSON

Port entityJSON

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Limitations[â](#limitations "Direct link to Limitations")

### Maximum offset in OpsGenie APIs[â](#maximum-offset-in-opsgenie-apis "Direct link to Maximum offset in OpsGenie APIs")

The OpsGenie APIs for [Alerts](https://docs.opsgenie.com/docs/alert-api#list-alerts) and [Incidents](https://docs.opsgenie.com/docs/incident-api#list-incidents) have a pagination limit where the sum of `offset` and `limit` parameters cannot exceed 20,000 records. This means you can retrieve up to 20,000 records in a single query session for each resource type.

Working with large datasets

To access records beyond the 20,000 limit, use filters to narrow your result set. This approach reduces the number of records returned and helps you bypass the offset limitation. For implementation details and supported filter options, see the [examples](/build-your-software-catalog/sync-data-to-catalog/incident-management/opsgenie/examples.md#alert) section.

## Examples[â](#examples "Direct link to Examples")

To view and test the integration's mapping against examples of the third-party API responses, use the jq playground in your [data sources page](https://app.getport.io/settings/data-sources). Find the integration in the list of data sources and click on it to open the playground.

Examples of blueprints and the relevant integration configurations can be found on the opsgenie [examples page](/build-your-software-catalog/sync-data-to-catalog/incident-management/opsgenie/examples.md)

## Alternative installation via webhook[â](#alternative-installation-via-webhook "Direct link to Alternative installation via webhook")

While the Ocean integration described above is the recommended installation method, you may prefer to use a webhook to ingest data from Opsgenie. If so, use the following instructions:

**Webhook installation (click to expand)**

In this example you are going to create a webhook integration between [OpsGenie](https://www.atlassian.com/software/opsgenie) and Port, which will ingest alert entities.

### Port configuration[â](#port-configuration "Direct link to Port configuration")

Create the following blueprint definition:

OpsGenie alert blueprint

Create in Port

```
{
  "identifier": "opsGenieAlert",
  "description": "This blueprint represents an OpsGenie alert in our software catalog",
  "title": "OpsGenie Alert",
  "icon": "OpsGenie",
  "schema": {
    "properties": {
      "description": {
        "type": "string",
        "title": "Description"
      },
      "lastChangeType": {
        "type": "string",
        "title": "Last Change Type",
        "description": "The type of the last change made to the alert"
      },
      "tags": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Tags"
      },
      "responders": {
        "type": "array",
        "title": "Responders",
        "description": "Responders to the alert"
      },
      "teams": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Teams",
        "description": "IDs of teams assigned to the alert"
      },
      "priority": {
        "type": "string",
        "title": "Priority"
      },
      "sourceName": {
        "type": "string",
        "title": "Source Name",
        "description": "Alert source name"
      },
      "sourceType": {
        "type": "string",
        "title": "Source Type",
        "description": "Alert source type"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {
    "status": {
      "title": "Status",
      "calculation": "if .properties.lastChangeType == \"Close\" then \"Closed\" else \"Active\" end",
      "type": "string",
      "colorized": true,
      "colors": {
        "Closed": "green",
        "Active": "red"
      }
    }
  },
  "relations": {}
}
```

Create the following webhook configuration [using Port UI](/build-your-software-catalog/sync-data-to-catalog/.md?operation=ui#configuring-webhook-endpoints):

OpsGenie alert webhook configuration

1. **Basic details** tab - fill the following details:

   1. Title : `OpsGenie mapper`;
   2. Identifier : `opsgenie_mapper`;
   3. Description : `A webhook configuration to map OpsGenie alerts to Port`;
   4. Icon : `OpsGenie`;

2. **Integration configuration** tab - fill the following JQ mapping:

   ```
   [
     {
       "blueprint": "opsGenieAlert",
       "entity": {
         "identifier": ".body.alert.alertId",
         "title": ".body.alert.tinyId + \" - \" + .body.alert.message",
         "properties": {
           "description": ".body.alert.description",
           "lastChangeType": ".body.action",
           "priority": ".body.alert.priority",
           "sourceName": ".body.source.name",
           "sourceType": ".body.source.type",
           "tags": ".body.alert.tags",
           "responders": ".body.alert.responders",
           "teams": ".body.alert.teams"
         }
       }
     }
   ]
   ```

3. Click **Save** at the bottom of the page.

## Create a webhook in OpsGenie

1. Go to OpsGenie;

2. Select **Settings**;

3. Click on **Integrations** under the **Integrations** section of the sidebar;

4. Click on **Add integration**;

5. In the search box, type *Webhook* and select the webhook option;

6. Input the following details:

   <!-- -->

   1. `Name` - use a meaningful name such as Port Webhook;

   2. Be sure to keep the "Enabled" checkbox checked;

   3. Check the "Add Alert Description to Payload" checkbox;

   4. Check the "Add Alert Details to Payload" checkbox;

   5. Add the following action triggers to the webhook by clicking on **Add new action**:

      <!-- -->

      1. If *alert is snoozed* in Opsgenie, *post to url* in Webhook;
      2. If *alert's description is updated* in Opsgenie, *post to url* in Webhook;
      3. If *alert's message is updated* in Opsgenie, *post to url* in Webhook;
      4. If *alert's priority is updated* in Opsgenie, *post to url* in Webhook;
      5. If *a responder is added to the alert* in Opsgenie, *post to url* in Webhook;
      6. if *a user executes "Assign Ownership* in Opsgenie, *post to url* in Webhook;
      7. if *a tag is added to the alert* in Opsgenie, *post to url* in Webhook;
      8. .if *a tag is removed from the alert* in Opsgenie, *post to url* in Webhook;

   6. `Webhook URL` - enter the value of the `url` key you received after creating the webhook configuration;

7. Click **Save integration**

tip

In order to view the different payloads and events available in Opsgenie webhooks, [look here](https://support.atlassian.com/opsgenie/docs/opsgenie-edge-connector-alert-action-data/)

Done! any change that happens to an OpsGenie alert (created, acknowledged, etc.) will trigger a webhook event that OpsGenie will send to the webhook URL provided by Port. Port will parse the events according to the mapping and update the catalog entities accordingly.

## Let's Test It

This section includes a sample webhook event sent from OpsGenie when an alert is created. In addition, it includes the entity created from the event based on the webhook configuration provided in the previous section.

### Payload

Here is an example of the payload structure sent to the webhook URL when an OpsGenie alert is created:

Webhook event payload

```
{
  "source": {
    "name": "web",
    "type": "API"
  },
  "alert": {
    "tags": ["tag1", "tag2"],
    "teams": ["team1", "team2"],
    "responders": ["recipient1", "recipient2"],
    "message": "test alert",
    "username": "username",
    "alertId": "052652ac-5d1c-464a-812a-7dd18bbfba8c",
    "source": "user@domain.com",
    "alias": "aliastest",
    "tinyId": "10",
    "entity": "An example entity",
    "createdAt": 1686916265415,
    "updatedAt": 1686916266116,
    "userId": "daed1180-0ce8-438b-8f8e-57e1a5920a2d",
    "description": "Testing opsgenie alerts",
    "priority": "P1"
  },
  "action": "Create",
  "integrationId": "37c8f316-17c6-49d7-899b-9c7e540c048d",
  "integrationName": "Port-Integration"
}
```

### Mapping Result

The combination of the sample payload and the webhook configuration generates the following Port entity:

```
{
  "identifier": "052652ac-5d1c-464a-812a-7dd18bbfba8c",
  "title": "10 - test alert",
  "blueprint": "opsGenieAlert",
  "properties": {
    "description": "Testing opsgenie alerts",
    "lastChangeType": "Create",
    "priority": "P1",
    "sourceName": "web",
    "sourceType": "API",
    "tags": ["tag1", "tag2"],
    "responders": ["recipient1", "recipient2"],
    "teams": ["team1", "team2"]
  },
  "relations": {}
}
```

## Ingest who is on-call

In this example we will create a blueprint for `service` entities with an `on-call` property that will be ingested directly from OpsGenie. The examples below pull data from the OpsGenie REST Api, in a defined scheduled period using GitLab Pipelines or GitHub Workflows, and report the data to Port as a property to the `service` blueprint.

* [Github Workflow](https://github.com/port-labs/opsgenie-oncall-example)
* [GitLab CI Pipeline](https://gitlab.com/getport-labs/opsgenie-oncall-example)

## Migration Guide to Version 0.2.0[â](#migration-guide-to-version-020 "Direct link to Migration Guide to Version 0.2.0")

This guide outlines how to update your existing OpsGenie integration configuration to take advantage of the performance improvements and breaking changes introduced in version 0.2.0.

### Key Improvements[â](#key-improvements "Direct link to Key Improvements")

* **New Blueprints and Kinds**: Added new kinds for team, schedule, and schedule-oncall.
* **Data Filtering**: Introduced support for filtering data from the OpsGenie API to fetch only the necessary information.
* **Enhanced Logging**: Added logs for easier debugging and better insight into integration issues.

### Breaking Changes[â](#breaking-changes "Direct link to Breaking Changes")

* **Optimized API Calls**: Removed redundant API calls for fetching impacted services and alert-incident relationships, improving performance by leveraging existing relations and JQ
* **Blueprint Changes**: The `OpsGenieService` blueprint no longer contains team properties like `oncallTeam`, `teamMembers`, and `oncallUsers`. These have been moved to a new `OpsGenieTeam` blueprint, reflecting a new relation between services and teams.

### Migration Steps[â](#migration-steps "Direct link to Migration Steps")

#### Step 1: Understand Existing Configuration

In versions prior to 0.2.0, your Port app's configuration may have used a mapping like the one below:

Existing configuration (click to expand)

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: service
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .name | gsub("[^a-zA-Z0-9@_.:/=-]"; "-") | tostring
          title: .name
          blueprint: '"opsGenieService"'
          properties:
            description: .description
            url: .links.web
            tags: .tags
            oncallTeam: .__team.name
            teamMembers: '[.__team.members[].user.username]'
            oncallUsers: .__oncalls.onCallRecipients
  - kind: alert
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .message
          blueprint: '"opsGenieAlert"'
          properties:
            status: .status
            acknowledged: .acknowledged
            responders: .responders
            priority: .priority
            sourceName: .source
            tags: .tags
            count: .count
            createdBy: .owner
            createdAt: .createdAt
            updatedAt: .updatedAt
            description: .description
            integration: .integration.name
          relations:
            relatedIncident: .__relatedIncident.id
  - kind: incident
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .message
          blueprint: '"opsGenieIncident"'
          properties:
            status: .status
            responders: .responders
            priority: .priority
            tags: .tags
            url: .links.web
            createdAt: .createdAt
            updatedAt: .updatedAt
            description: .description
          relations:
            services: '[.__impactedServices[] | .name | gsub("[^a-zA-Z0-9@_.:/=-]"; "-") | tostring]'
```

#### Step 2: Update to New Configuration

To adapt to version 0.2.0, you will need to update your configuration as follows:

New configuration (click to expand)

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: service
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id  # The identifier of the service now uses the unique ID from OpsGenie instead of the name
          title: .name
          blueprint: '"opsGenieService"'
          properties:
            description: .description
            url: .links.web
            tags: .tags
  - kind: alert
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .message
          blueprint: '"opsGenieAlert"'
          properties:
            status: .status
            acknowledged: .acknowledged
            responders: .responders
            priority: .priority
            sourceName: .source
            tags: .tags
            count: .count
            createdBy: .owner
            createdAt: .createdAt
            updatedAt: .updatedAt
            description: .description
            integration: .integration.name
          relations:
            relatedIncident: 'if (.alias | contains("_")) then (.alias | split("_")[0]) else null end'  # We now use JQ logic to map alerts to incidents to avoid making extra API call
  - kind: incident
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .message
          blueprint: '"opsGenieIncident"'
          properties:
            status: .status
            responders: .responders
            priority: .priority
            tags: .tags
            url: .links.web
            createdAt: .createdAt
            updatedAt: .updatedAt
            description: .description
          relations:
            services: .impactedServices  # We can now directly map incidents to impacted services using the data that is coming from the API
```

In the updated configuration, the `opsGenieService` blueprint no longer includes properties like `oncallTeam`, `teamMembers`, and `oncallUsers`. These properties are now part of the new `OpsGenieTeam` blueprint. If you need to track on-call teams and users for each service, follow the steps below.

#### Step 3: Create the OpsGenieTeam Blueprint

To manage team-related data, create a new `OpsGenieTeam` blueprint in Port using the following schema:

OpsGenie team blueprint (click to expand)

Create in Port

```
{
  "identifier": "opsGenieTeam",
  "description": "This blueprint represents an OpsGenie team in our software catalog",
  "title": "OpsGenie Team",
  "icon": "OpsGenie",
  "schema": {
    "properties": {
      "description": {
        "type": "string",
        "title": "Description",
        "icon": "DefaultProperty"
      },
      "url": {
        "title": "URL",
        "type": "string",
        "description": "URL to the service",
        "format": "url",
        "icon": "DefaultProperty"
      },
      "oncallUsers": {
        "type": "array",
        "title": "Current Oncalls",
        "items": {
          "type": "string",
          "format": "user"
        }
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {}
}
```

#### Step 4: Update the OpsGenieService Blueprint

Next, update the `opsGenieService` blueprint to reference the `OpsGenieTeam` blueprint by establishing a relation and mirroring relevant properties:

Updated OpsGenie service blueprint (click to expand)

Create in Port

```
{
  "identifier": "opsGenieService",
  "description": "This blueprint represents an OpsGenie service in our software catalog",
  "title": "OpsGenie Service",
  "icon": "OpsGenie",
  "schema": {
    "properties": {
      "description": {
        "type": "string",
        "title": "Description",
        "icon": "DefaultProperty"
      },
      "url": {
        "title": "URL",
        "type": "string",
        "description": "URL to the service",
        "format": "url",
        "icon": "DefaultProperty"
      },
      "tags": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Tags",
        "icon": "DefaultProperty"
      }
    },
    "required": []
  },
  "mirrorProperties": {
    "oncallUsers": {
      "title": "Current Oncalls",
      "path": "ownerTeam.oncallUsers"
    }
  },
  "calculationProperties": {
  },
  "aggregationProperties": {
    "numberOfOpenIncidents": {
      "title": "Number of open incidents",
      "type": "number",
      "target": "opsGenieIncident",
      "query": {
        "combinator": "and",
        "rules": [
          {
            "property": "status",
            "operator": "=",
            "value": "open"
          }
        ]
      },
      "calculationSpec": {
        "calculationBy": "entities",
        "func": "count"
      }
    }
  },
  "relations": {
    "ownerTeam": {
      "title": "Owner Team",
      "target": "opsGenieTeam",
      "required": false,
      "many": false
    }
  }
}
```

#### Step 5: Update the Mapping Configuration

Update your configuration mapping to correctly populate the `OpsGenieTeam` blueprint with team and on-call data. This will enable you to view on-call team information at the service level:

Updated configuration to add teams and oncalls (click to expand)

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: team
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .name
          blueprint: '"opsGenieTeam"'
          properties:
            description: .description
            url: .links.web
  - kind: service
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .name
          blueprint: '"opsGenieService"'
          properties:
            description: .description
            url: .links.web
            tags: .tags
          relations:
            ownerTeam: .teamId
  - kind: schedule-oncall
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .ownerTeam.id
          title: .ownerTeam.name
          blueprint: '"opsGenieTeam"'
          properties:
            oncallUsers: .__currentOncalls.onCallRecipients
```

#### Final Step: Full Configuration Example

After completing these changes, your configuration should look like this, incorporating blueprints for `team`, `service`, `alert` and `incident`:

Full configuration (click to expand)

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: team
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .name
          blueprint: '"opsGenieTeam"'
          properties:
            description: .description
            url: .links.web
  - kind: service
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .name
          blueprint: '"opsGenieService"'
          properties:
            description: .description
            url: .links.web
            tags: .tags
          relations:
            ownerTeam: .teamId
  - kind: alert
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .message
          blueprint: '"opsGenieAlert"'
          properties:
            status: .status
            acknowledged: .acknowledged
            responders: .responders
            priority: .priority
            sourceName: .source
            tags: .tags
            count: .count
            createdBy: .owner
            createdAt: .createdAt
            updatedAt: .updatedAt
            description: .description
            integration: .integration.name
          relations:
            relatedIncident: 'if (.alias | contains("_")) then (.alias | split("_")[0]) else null end'
  - kind: incident
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .message
          blueprint: '"opsGenieIncident"'
          properties:
            status: .status
            responders: .responders
            priority: .priority
            tags: .tags
            url: .links.web
            createdAt: .createdAt
            updatedAt: .updatedAt
            description: .description
          relations:
            services: .impactedServices
  - kind: schedule-oncall
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .ownerTeam.id
          title: .ownerTeam.name
          blueprint: '"opsGenieTeam"'
          properties:
            oncallUsers: .__currentOncalls.onCallRecipients
```

Following this guide will ensure your integration is up-to-date and optimized for performance with version 0.2.0. For any issues during the migration, refer to the newly introduced debug logs to identify and contact your support personnel to resolve problems efficiently.

## More relevant guides and examples[â](#more-relevant-guides-and-examples "Direct link to More relevant guides and examples")

* [Self-service action to trigger an OpsGenie incident](https://docs.port.io/guides/all/create-an-opsgenie-incident)
