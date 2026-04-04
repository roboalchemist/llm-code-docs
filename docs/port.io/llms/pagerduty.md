# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty.md

# PagerDuty

![](/img/guides/icons/PagerDuty.svg)![](/img/guides/icons/PagerDuty.svg)

Loading version...

Port's PagerDuty integration allows you to model PagerDuty resources in your software catalog and ingest data into them.

Supported resources ![](/img/icons/external-link.svg)[User](https://developer.pagerduty.com/api-reference/c96e889522dd6-list-users)[Schedule](https://developer.pagerduty.com/api-reference/846ecf84402bb-list-schedules)[Oncall](https://developer.pagerduty.com/api-reference/3a6b910f11050-list-all-of-the-on-calls)[Service](https://developer.pagerduty.com/api-reference/e960cca205c0f-list-services)[Incident](https://developer.pagerduty.com/api-reference/9d0b4b12e36f9-list-incidents)[Escalation Policy](https://developer.pagerduty.com/api-reference/51b21014a4f5a-list-escalation-policies)

Ingesting additional resources

The resources listed above are just a subset of what the PagerDuty integration supports. You can ingest additional PagerDuty resources if they have a `GET List <resource name>` endpoint in the [PagerDuty API documentation](https://developer.pagerduty.com/api-reference/e65c5833eeb07-pager-duty-api). This means, resources such as teams, audit records, business services, extensions, incident workflows, status dashboards, vendor etc can be ingested into Port.

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods: Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

1Choose method2Install

Hosted by Port with OAuth

* â§Port hosts and manages the integration
* â§Customizable resync interval for data ingestion
* â§Fast OAuth setup - no API token required
* â§Great for getting started, not recommended for production environments

Hosted by Port with custom settings

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
deleteDependentEntities: true
createMissingRelatedEntities: true
enableMergeEntity: true
resources:
- kind: services
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"pagerdutyService"'
        properties:
          status: .status
          url: .html_url
          oncall: .__oncall_user | sort_by(.escalation_level) | .[0].user.email
          secondaryOncall: .__oncall_user | sort_by(.escalation_level) | .[1].user.email
          escalationLevels: .__oncall_user | map(.escalation_level) | unique | length
          meanSecondsToResolve: .__analytics.mean_seconds_to_resolve
          meanSecondsToFirstAck: .__analytics.mean_seconds_to_first_ack
          meanSecondsToEngage: .__analytics.mean_seconds_to_engage
- kind: incidents
  selector:
    query: 'true'
    apiQueryParams:
      include:
      - assignees
      - first_trigger_log_entries
      statuses:
      - resolved
  port:
    entity:
      mappings:
        identifier: .id | tostring
        title: .title
        blueprint: '"pagerdutyIncident"'
        properties:
          status: .status
          url: .html_url
          urgency: .urgency
          escalation_policy: .escalation_policy.summary
          created_at: .created_at
          updated_at: .updated_at
          priority: if .priority != null then .priority.summary else null end
          description: .description
          triggered_by: .first_trigger_log_entry.agent.summary
        relations:
          pagerdutyService: .service.id
          service:
            combinator: '"and"'
            rules:
            - property: '"pagerdutyServiceId"'
              operator: '"="'
              value: .service.id
- kind: incidents
  selector:
    query: 'true'
    apiQueryParams:
      include:
      - assignees
      - first_trigger_log_entries
      statuses:
      - triggered
      - acknowledged
  port:
    entity:
      mappings:
        identifier: .id | tostring
        title: .title
        blueprint: '"pagerdutyIncident"'
        properties:
          status: .status
          url: .html_url
          urgency: .urgency
          escalation_policy: .escalation_policy.summary
          created_at: .created_at
          updated_at: .updated_at
          priority: if .priority != null then .priority.summary else null end
          description: .description
          resolvedAt: .resolved_at
          recoveryTime: |-
            (.created_at as $createdAt | .resolved_at as $resolvedAt | if $resolvedAt == null then null else  ( ($resolvedAt | strptime("%Y-%m-%dT%H:%M:%SZ") | mktime) -
              ($createdAt | strptime("%Y-%m-%dT%H:%M:%SZ") | mktime) ) / 60 | floor end)
          triggered_by: .first_trigger_log_entry.agent.summary
        relations:
          pagerdutyService: .service.id
          incident_port_assignee:
            combinator: '"and"'
            rules:
            - property: '"pagerduty_user_id"'
              operator: '"in"'
              value: .assignments | map(.assignee.id)
          incident_pagerduty_assignee: .assignments | map(.assignee.id)
- kind: schedules
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"pagerdutySchedule"'
        properties:
          url: .html_url
          timezone: .time_zone
          description: .description
          users: '[.users[] | select(has("__email")) | .__email]'
- kind: oncalls
  selector:
    query: 'true'
    apiQueryParams:
      include:
      - users
  port:
    entity:
      mappings:
        identifier: .user.id + "-" + .schedule.id + "-" + .start
        title: .user.name
        blueprint: '"pagerdutyOncall"'
        properties:
          startDate: .start
          endDate: .end
          url: .schedule.html_url
        relations:
          pagerdutySchedule: .schedule.id
          pagerdutyEscalationPolicy: .escalation_policy.id
          pagerduty_user: .user.id
          port_user:
            combinator: '"and"'
            rules:
            - property: '"$identifier"'
              operator: '"="'
              value: .user.email
- kind: escalation_policies
  selector:
    query: 'true'
    attachOncallUsers: true
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"pagerdutyEscalationPolicy"'
        properties:
          url: .html_url
          summary: .summary
          primaryOncall: .__oncall_users | sort_by(.escalation_level) | .[0].user.email
          escalationRules: .escalation_rules
- kind: users
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"pagerdutyUser"'
        properties:
          url: .html_url
          time_zone: .time_zone
          email: .email
          description: .description
          role: .role
          job_title: .job_title
          teams: .teams
          contact_methods: .contact_methods
- kind: incidents
  selector:
    query: 'true'
    apiQueryParams:
      include:
      - assignees
      - first_trigger_log_entries
      statuses:
      - resolved
  port:
    entity:
      mappings:
        identifier: .id | tostring
        blueprint: '"pagerdutyIncident"'
        relations:
          original_alert: .first_trigger_log_entry.channel.details.id
          extrakey: if .kind == "Incident" then .children.edges[].node.identifier else null end
          additionalField: .some.new.field.value
- kind: incidents
  selector:
    query: 'true'
    apiQueryParams:
      include:
      - assignees
      - first_trigger_log_entries
      statuses:
      - triggered
      - acknowledged
      inducer:
      - assignees
      - first_trigger_log_entries
  port:
    entity:
      mappings:
        identifier: .id | tostring
        blueprint: '"pagerdutyIncident"'
        relations:
          original_alert: .first_trigger_log_entry.channel.details.id
          extrakey: if .kind == "Incident" then .children.edges[].node.identifier else null end
```

## Mapping & examples per resource[â](#mapping--examples-per-resource "Direct link to Mapping & examples per resource")

Use the explorer below to view sample payloads and the resulting Port entities for each resource type.

<!-- -->

ServiceIncidentScheduleOncallEscalation PolicyUser

Default mappingYAML

Sample payloadJSON

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Capabilities[â](#capabilities "Direct link to Capabilities")

### Ingesting service analytics[â](#ingesting-service-analytics "Direct link to Ingesting service analytics")

To enrich your PagerDuty service entities with analytics data, follow the steps below:

1. Update the service blueprint to include analytics properties. You can add any property that is returned from the [PagerDuty aggregated service analytics API](https://developer.pagerduty.com/api-reference/694e92fe4f943-get-aggregated-service-data)

   **Updated service blueprint (click to expand)**

   Create in Port

   ```
   {
     "identifier":"pagerdutyService",
     "description":"This blueprint represents a PagerDuty service in our software catalog",
     "title":"PagerDuty Service",
     "icon":"pagerduty",
     "schema":{
         "properties":{
           "status":{
               "title":"Status",
               "type":"string"
           },
           "url":{
               "title":"URL",
               "type":"string",
               "format":"url"
           },
           "oncall":{
               "title":"On Call",
               "type":"array",
               "items":{
                 "type":"string",
                 "format":"user"
               }
           },
           "meanSecondsToResolve":{
               "title":"Mean Seconds to Resolve",
               "type":"number"
           },
           "meanSecondsToFirstAck":{
               "title":"Mean Seconds to First Acknowledge",
               "type":"number"
           },
           "meanSecondsToEngage":{
               "title":"Mean Seconds to Engage",
               "type":"number"
           },
           "totalIncidentCount":{
               "title":"Total Incident Count",
               "type":"number"
           },
           "totalIncidentsAcknowledged":{
               "title":"Total Incidents Acknowledged",
               "type":"number"
           },
           "totalIncidentsAutoResolved":{
               "title":"Total Incidents Auto Resolved",
               "type":"number"
           },
           "totalIncidentsManualEscalated":{
               "title":"Total Incident Manual Escalated",
               "type":"number"
           }
         },
         "required":[]
     },
     "mirrorProperties":{},
     "calculationProperties":{},
     "relations":{}
   }
   ```

2. Add `serviceAnalytics` property to the integration `selector` key. When set to `true`, the integration will fetch data from the [PagerDuty aggregated service analytics API](https://developer.pagerduty.com/api-reference/694e92fe4f943-get-aggregated-service-data) and ingest it to Port. By default, this property is set to `true`.

   Also, by default, the integration aggregates the analytics over a period of 3 months. Use the `analyticsMonthsPeriod` filter to override this date range. The accepted values are positive number between 1 to 12. In the provided example below, we aggregate the analytics over the past 6 months.

   ```
   resources:
     - kind: services
       selector:
         query: "true"
         serviceAnalytics: "true"
         analyticsMonthsPeriod: 6
       port:
         entity:
           mappings:
             identifier: .id
             title: .name
             blueprint: '"pagerdutyService"'
             properties:
               status: .status
               url: .html_url
               oncall: .__oncall_user | sort_by(.escalation_level) | .[0].user.email
               secondaryOncall: .__oncall_user | sort_by(.escalation_level) | .[1].user.email
   ```

3. Establish a mapping between the analytics properties and the service analytics data response. Following a convention, the aggregated result of the PagerDuty service analytics API is saved to the `__analytics` key and merged with the response of the service API. Consequently, users can access specific metrics such as the mean seconds to resolve by referencing `__analytics.mean_seconds_to_resolve`.

   ```
   resources:
     - kind: services
       selector:
         query: "true"
         serviceAnalytics: "true"
         analyticsMonthsPeriod: 6
       port:
         entity:
           mappings:
             identifier: .id
             title: .name
             blueprint: '"pagerdutyService"'
             properties:
               status: .status
               url: .html_url
               oncall: .__oncall_user | sort_by(.escalation_level) | .[0].user.email
               secondaryOncall: .__oncall_user | sort_by(.escalation_level) | .[1].user.email
               meanSecondsToResolve: .__analytics.mean_seconds_to_resolve
   ```

4. Below is the complete integration configuration for enriching the service blueprint with analytics data.

   **Service analytics integration configuration (click to expand)**

   ```
   resources:
     - kind: services
       selector:
         query: "true"
         serviceAnalytics: "true"
         analyticsMonthsPeriod: 6
       port:
         entity:
           mappings:
             identifier: .id
             title: .name
             blueprint: '"pagerdutyService"'
             properties:
               status: .status
               url: .html_url
               oncall: .__oncall_user | sort_by(.escalation_level) | .[0].user.email
               secondaryOncall: .__oncall_user | sort_by(.escalation_level) | .[1].user.email
               meanSecondsToResolve: .__analytics.mean_seconds_to_resolve
               meanSecondsToFirstAck: .__analytics.mean_seconds_to_first_ack
               meanSecondsToEngage: .__analytics.mean_seconds_to_engage
               totalIncidentCount: .__analytics.total_incident_count
               totalIncidentsAcknowledged: .__analytics.total_incidents_acknowledged
               totalIncidentsAutoResolved: .__analytics.total_incidents_auto_resolved
               totalIncidentsManualEscalated: .__analytics.total_incidents_manual_escalated
   ```

### Ingesting incident analytics[â](#ingesting-incident-analytics "Direct link to Ingesting incident analytics")

To enrich your PagerDuty incident entities with analytics data, follow the steps below:

1. Update the incident blueprint to include an `analytics` property.

   **Updated incident blueprint (click to expand)**

   Create in Port

   ```
   {
     "identifier": "pagerdutyIncident",
     "description": "This blueprint represents a PagerDuty incident in our software catalog",
     "title": "PagerDuty Incident",
     "icon": "pagerduty",
     "schema": {
       "properties": {
         "status": {
           "type": "string",
           "title": "Incident Status",
           "enum": [
             "triggered",
             "annotated",
             "acknowledged",
             "reassigned",
             "escalated",
             "reopened",
             "resolved"
           ],
           "enumColors": {
             "triggered": "red",
             "annotated": "blue",
             "acknowledged": "yellow",
             "reassigned": "blue",
             "escalated": "yellow",
             "reopened": "red",
             "resolved": "green"
           }
         },
         "url": {
           "type": "string",
           "format": "url",
           "title": "Incident URL"
         },
         "urgency": {
           "title": "Incident Urgency",
           "type": "string",
           "enum": [
             "high",
             "low"
           ],
           "enumColors": {
             "high": "red",
             "low": "green"
           }
         },
         "priority": {
           "type": "string",
           "title": "Priority",
           "enum": [
             "P1",
             "P2",
             "P3",
             "P4",
             "P5"
           ],
           "enumColors": {
             "P1": "red",
             "P2": "yellow",
             "P3": "blue",
             "P4": "lightGray",
             "P5": "darkGray"
           }
         },
         "description": {
           "type": "string",
           "title": "Description"
         },
         "assignees": {
           "title": "Assignees",
           "type": "array",
           "items": {
             "type": "string",
             "format": "user"
           }
         },
         "escalation_policy": {
           "type": "string",
           "title": "Escalation Policy"
         },
         "created_at": {
           "title": "Create At",
           "type": "string",
           "format": "date-time"
         },
         "updated_at": {
           "title": "Updated At",
           "type": "string",
           "format": "date-time"
         },
         "analytics": {
           "title": "Analytics",
           "type": "object"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "relations": {
       "pagerdutyService": {
         "title": "PagerDuty Service",
         "target": "pagerdutyService",
         "required": false,
         "many": true
       }
     }
   }
   ```

2. Add `incidentAnalytics` property to the integration `selector` key. When set to `true`, the integration will fetch data from the [PagerDuty Analytics API](https://developer.pagerduty.com/api-reference/328d94baeaa0e-get-raw-data-single-incident) and ingest it to Port. By default, this property is set to `false`.

   ```
   resources:
     - kind: incidents
       selector:
         query: "true"
         incidentAnalytics: "true"
       port:
         entity:
           mappings:
             identifier: .id | tostring
             title: .title
             blueprint: '"pagerdutyIncident"'
             properties:
               status: .status
               url: .self
   ```

3. Establish a mapping between the `analytics` blueprint property and the analytics data response.

   ```
   resources:
   - kind: incidents
     selector:
       query: 'true'
       include: ['assignees']
     port:
       entity:
         mappings:
           identifier: .id | tostring
           title: .title
           blueprint: '"pagerdutyIncident"'
           properties:
             status: .status
             url: .self
             urgency: .urgency
             assignees: .assignments | map(.assignee.email)
             escalation_policy: .escalation_policy.summary
             created_at: .created_at
             updated_at: .updated_at
             priority: if .priority != null then .priority.summary else null end
             description: .description
             analytics: .__analytics
           relations:
             pagerdutyService: .service.id
   ```

4. Below is the complete integration configuration for enriching the incident blueprint with analytics data.

   **Incident analytics integration configuration (click to expand)**

   ```
   resources:
   - kind: incidents
     selector:
       query: 'true'
       include: ['assignees']
     port:
       entity:
         mappings:
           identifier: .id | tostring
           title: .title
           blueprint: '"pagerdutyIncident"'
           properties:
             status: .status
             url: .self
             urgency: .urgency
             assignees: .assignments | map(.assignee.email)
             escalation_policy: .escalation_policy.summary
             created_at: .created_at
             updated_at: .updated_at
             priority: if .priority != null then .priority.summary else null end
             description: .description
             analytics: .__analytics
           relations:
             pagerdutyService: .service.id
   ```

### Ingesting service custom fields[â](#ingesting-service-custom-fields "Direct link to Ingesting service custom fields")

To enrich your PagerDuty service entities with [custom fields](https://support.pagerduty.com/main/docs/custom-fields-on-incidents) data, follow the steps below:

1. Update the service blueprint to include properties for the custom fields you want to ingest. When enabled, the integration fetches the [custom field values](https://developer.pagerduty.com/api-reference/d64ec707c5ee4-list-custom-field-values-for-a-service) for each service and stores them under the `__custom_fields` key. Each custom field in the array has the following structure:

   ```
   {
     "id": "FIELD_ID",
     "name": "my_custom_field",
     "display_name": "My Custom Field",
     "data_type": "string",
     "field_type": "single_value",
     "type": "field_value",
     "value": {
       "value": "field value here"
     }
   }
   ```

   You can extract specific custom field values into individual blueprint properties using jq.<br /><!-- -->For example, if you have custom fields named `team` and `environment` in PagerDuty:

   **Updated service blueprint (click to expand)**

   Create in Port

   ```
   {
     "identifier":"pagerdutyService",
     "description":"This blueprint represents a PagerDuty service in our software catalog",
     "title":"PagerDuty Service",
     "icon":"pagerduty",
     "schema":{
         "properties":{
           "status":{
               "title":"Status",
               "type":"string"
           },
           "url":{
               "title":"URL",
               "type":"string",
               "format":"url"
           },
           "oncall":{
               "title":"On Call",
               "type":"array",
               "items":{
                 "type":"string",
                 "format":"user"
               }
           },
           "team":{
               "title":"Team",
               "type":"string"
           },
           "environment":{
               "title":"Environment",
               "type":"string"
           }
         },
         "required":[]
     },
     "mirrorProperties":{},
     "calculationProperties":{},
     "relations":{}
   }
   ```

2. Add `includeCustomFields` to the `selector` key and map specific custom field values using jq. When set to `true`, the integration fetches custom field values for each service. By default, this property is set to `false`. Use jq expressions to extract specific fields by their `name`, for example: `(.__custom_fields[] | select(.name == "team")).value`.

   ```
   resources:
     - kind: services
       selector:
         query: "true"
         includeCustomFields: "true"
       port:
         entity:
           mappings:
             identifier: .id
             title: .name
             blueprint: '"pagerdutyService"'
             properties:
               status: .status
               url: .html_url
               oncall: .__oncall_user | sort_by(.escalation_level) | .[0].user.email
               secondaryOncall: .__oncall_user | sort_by(.escalation_level) | .[1].user.email
               team: (.__custom_fields[] | select(.name == "team")).value
               environment: (.__custom_fields[] | select(.name == "environment")).value
   ```

### Ingesting incident custom fields[â](#ingesting-incident-custom-fields "Direct link to Ingesting incident custom fields")

To enrich your PagerDuty incident entities with [custom fields](https://support.pagerduty.com/main/docs/custom-fields-on-incidents) data, follow the steps below:

1. Update the incident blueprint to include properties for the custom fields you want to ingest. The `__custom_fields` array has the same structure as described in the [service custom fields section](#ingesting-service-custom-fields) above. For example, if you have custom fields named `severity` and `affected_region` in PagerDuty:

   **Updated incident blueprint (click to expand)**

   Create in Port

   ```
   {
     "identifier": "pagerdutyIncident",
     "description": "This blueprint represents a PagerDuty incident in our software catalog",
     "title": "PagerDuty Incident",
     "icon": "pagerduty",
     "schema": {
       "properties": {
         "status": {
           "type": "string",
           "title": "Incident Status",
           "enum": [
             "triggered",
             "annotated",
             "acknowledged",
             "reassigned",
             "escalated",
             "reopened",
             "resolved"
           ],
           "enumColors": {
             "triggered": "red",
             "annotated": "blue",
             "acknowledged": "yellow",
             "reassigned": "blue",
             "escalated": "yellow",
             "reopened": "red",
             "resolved": "green"
           }
         },
         "url": {
           "type": "string",
           "format": "url",
           "title": "Incident URL"
         },
         "urgency": {
           "title": "Incident Urgency",
           "type": "string",
           "enum": [
             "high",
             "low"
           ],
           "enumColors": {
             "high": "red",
             "low": "green"
           }
         },
         "priority": {
           "type": "string",
           "title": "Priority",
           "enum": [
             "P1",
             "P2",
             "P3",
             "P4",
             "P5"
           ],
           "enumColors": {
             "P1": "red",
             "P2": "yellow",
             "P3": "blue",
             "P4": "lightGray",
             "P5": "darkGray"
           }
         },
         "description": {
           "type": "string",
           "title": "Description"
         },
         "assignees": {
           "title": "Assignees",
           "type": "array",
           "items": {
             "type": "string",
             "format": "user"
           }
         },
         "escalation_policy": {
           "type": "string",
           "title": "Escalation Policy"
         },
         "created_at": {
           "title": "Create At",
           "type": "string",
           "format": "date-time"
         },
         "updated_at": {
           "title": "Updated At",
           "type": "string",
           "format": "date-time"
         },
         "severity":{
           "title": "Severity",
           "type": "string"
         },
         "affectedRegion":{
           "title": "Affected Region",
           "type": "string"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "relations": {
       "pagerdutyService": {
         "title": "PagerDuty Service",
         "target": "pagerdutyService",
         "required": false,
         "many": true
       }
     }
   }
   ```

2. Add `includeCustomFields` to the `selector` key and map specific custom field values using jq. When set to `true`, the integration fetches custom field values from the [PagerDuty Custom Fields API](https://developer.pagerduty.com/api-reference/a2d1780626a5c-list-incident-custom-field-values) for each incident. By default, this property is set to `false`. Extract specific fields the same way as in the [service example](#ingesting-service-custom-fields) above.

   ```
   resources:
   - kind: incidents
     selector:
       query: 'true'
       include: ['assignees']
       includeCustomFields: 'true'
     port:
       entity:
         mappings:
           identifier: .id | tostring
           title: .title
           blueprint: '"pagerdutyIncident"'
           properties:
             status: .status
             url: .self
             urgency: .urgency
             assignees: .assignments | map(.assignee.email)
             escalation_policy: .escalation_policy.summary
             created_at: .created_at
             updated_at: .updated_at
             priority: if .priority != null then .priority.summary else null end
             description: .description
             severity: (.__custom_fields[] | select(.name == "severity")).value
             affectedRegion: (.__custom_fields[] | select(.name == "affected_region")).value
           relations:
             pagerdutyService: .service.id
   ```

## Examples[â](#examples "Direct link to Examples")

To view and test the integration's mapping against examples of the third-party API responses, use the jq playground in your [data sources page](https://app.getport.io/settings/data-sources). Find the integration in the list of data sources and click on it to open the playground.

Additional examples of blueprints and the relevant integration configurations can be found on the pagerduty [examples page](/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/examples.md)

## Relevant guides[â](#relevant-guides "Direct link to Relevant guides")

For relevant guides and examples, see the [guides section](https://docs.port.io/guides?tags=PagerDuty).

## Limitations[â](#limitations "Direct link to Limitations")

* The PagerDuty API uses offset-based pagination, which has a limitation of retrieving a maximum of 10,000 resources. This may affect the integration's ability to sync data if you have more than 10,000 of a specific resource type (e.g., users, services, etc.). Refer to PagerDuty's [official documentation on pagination](https://developer.pagerduty.com/docs/pagination) for further details.

## Support[â](#support "Direct link to Support")

For any questions or issues, contact us at [support.port.io](http://support.port.io/) or via our [Community Slack channel](https://port.io/community).

## Alternative installation via webhook[â](#alternative-installation-via-webhook "Direct link to Alternative installation via webhook")

While the Ocean integration described above is the recommended installation method, you may prefer to use a webhook to ingest data from PagerDuty. If so, use the following instructions:

**Note** that when using the webhook installation method, data will be ingested into Port only when the webhook is triggered.

**Webhook installation (click to expand)**

In this example you are going to create a webhook integration between [PagerDuty](https://www.pagerduty.com/) and Port, which will ingest PagerDuty services and its related incidents into Port. This integration will involve setting up a webhook to receive notifications from PagerDuty whenever an incident is created or updated, allowing Port to ingest and process the incident entities accordingly.

## Import PagerDuty services and incidents

### Port configuration

Create the following blueprint definitions:

**PagerDuty service blueprint (click to expand)**

Create in Port

```
{
  "identifier": "pagerdutyService",
  "description": "This blueprint represents a PagerDuty service in our software catalog",
  "title": "PagerDuty Service",
  "icon": "pagerduty",
  "schema": {
    "properties": {
      "status": {
        "title": "Status",
        "type": "string",
        "enum": [
          "active",
          "warning",
          "critical",
          "maintenance",
          "disabled"
        ],
        "enumColors": {
          "active": "green",
          "warning": "yellow",
          "critical": "red",
          "maintenance": "lightGray",
          "disabled": "darkGray"
        }
      },
      "url": {
        "title": "URL",
        "type": "string",
        "format": "url"
      },
      "oncall": {
        "title": "On Call",
        "type": "string",
        "format": "user"
      },
      "escalationLevels": {
        "title": "Escalation Levels",
        "type": "number"
      },
      "meanSecondsToResolve": {
        "title": "Mean Seconds to Resolve",
        "type": "number"
      },
      "meanSecondsToFirstAck": {
        "title": "Mean Seconds to First Acknowledge",
        "type": "number"
      },
      "meanSecondsToEngage": {
        "title": "Mean Seconds to Engage",
        "type": "number"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

**PagerDuty incident blueprint (click to expand)**

Create in Port

```
{
  "identifier": "pagerdutyIncident",
  "description": "This blueprint represents a PagerDuty incident in our software catalog",
  "title": "PagerDuty Incident",
  "icon": "pagerduty",
  "schema": {
    "properties": {
      "status": {
        "type": "string",
        "title": "Incident Status",
        "enum": [
          "triggered",
          "annotated",
          "acknowledged",
          "reassigned",
          "escalated",
          "reopened",
          "resolved"
        ],
        "enumColors": {
          "triggered": "red",
          "annotated": "blue",
          "acknowledged": "yellow",
          "reassigned": "blue",
          "escalated": "yellow",
          "reopened": "red",
          "resolved": "green"
        }
      },
      "url": {
        "type": "string",
        "format": "url",
        "title": "Incident URL"
      },
      "urgency": {
        "title": "Incident Urgency",
        "type": "string",
        "enum": [
          "high",
          "low"
        ],
        "enumColors": {
          "high": "red",
          "low": "green"
        }
      },
      "priority": {
        "type": "string",
        "title": "Priority",
        "enum": [
          "P1",
          "P2",
          "P3",
          "P4",
          "P5"
        ],
        "enumColors": {
          "P1": "red",
          "P2": "yellow",
          "P3": "blue",
          "P4": "lightGray",
          "P5": "darkGray"
        }
      },
      "description": {
        "type": "string",
        "title": "Description"
      },
      "assignees": {
        "title": "Assignees",
        "type": "array",
        "items": {
          "type": "string",
          "format": "user"
        }
      },
      "escalation_policy": {
        "type": "string",
        "title": "Escalation Policy"
      },
      "created_at": {
        "title": "Create At",
        "type": "string",
        "format": "date-time"
      },
      "updated_at": {
        "title": "Updated At",
        "type": "string",
        "format": "date-time"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "pagerdutyService": {
      "title": "PagerDuty Service",
      "target": "pagerdutyService",
      "required": false,
      "many": true
    }
  }
}
```

Create the following webhook configuration [using Port UI](/build-your-software-catalog/custom-integration/webhook/.md?operation=ui#configuring-webhook-endpoints)

**PagerDuty webhook configuration (click to expand)**

1. **Basic details** tab - fill the following details:

   1. Title : `PagerDuty Mapper`;
   2. Identifier : `pagerduty_mapper`;
   3. Description : `A webhook configuration to map PagerDuty services and its related incidents to Port`;
   4. Icon : `Pagerduty`;

2. **Integration configuration** tab - fill the following JQ mapping:

   ```
   [
     {
       "blueprint": "microservice",
       "filter": ".body.event.event_type | startswith(\"service\")",
       "entity": {
         "identifier": ".body.event.data.id",
         "title": ".body.event.data.summary",
         "properties": {
           "status": ".body.event.data.status",
           "url": ".body.event.data.html_url",
           "oncall": ".body.event.data.__oncall_user[] | select(.escalation_level == 1) | .user.email",
           "escalationLevels": ".body.event.data.__oncall_user | map(.escalation_level) | unique | length",
           "meanSecondsToResolve": ".body.event.data.__analytics.mean_seconds_to_resolve",
           "meanSecondsToFirstAck": ".body.event.data.__analytics.mean_seconds_to_first_ack",
           "meanSecondsToEngage": ".body.event.data.__analytics.mean_seconds_to_engage",
         }
       }
     },
     {
       "blueprint": "pagerdutyIncident",
       "filter": ".body.event.event_type | startswith(\"incident\")",
       "entity": {
         "identifier": ".body.event.data.id",
         "title": ".body.event.data.title",
         "properties": {
           "status": ".body.event.data.status",
           "url": ".body.event.data.html_url",
           "urgency": ".body.event.data.urgency",
           "assignees": ".body.event.data.assignments | map(.assignee.email)",
           "escalation_policy": ".body.event.data.escalation_policy.summary",
           "created_at": ".body.event.data.created_at",
           "updated_at": ".body.event.data.updated_at",
           "priority": ".body.event.dataif .priority != null then .priority.summary else null end",
           "description": ".body.event.data.description"
         },
         "relations": {
           "microservice": ".body.event.data.service.id"
         }
       }
     }
   ]
   ```

3. Scroll down to **Advanced settings** and input the following details:

   1. secret: `WEBHOOK_SECRET`;
   2. Signature Header Name : `x-pagerduty-signature`;
   3. Signature Algorithm : Select `sha256` from dropdown option;
   4. Signature Prefix : `v1=`
   5. Click **Save** at the bottom of the page.

   Remember to update the `WEBHOOK_SECRET` with the real secret you receive after subscribing to the webhook in PagerDuty.

### Create a webhook in PagerDuty

1. Go to [PagerDuty](https://www.pagerduty.com/) and select the account you want to configure the webhook for.

2. Navigate to **Integrations** in the navigation bar and click on **Generic Webhooks (v3)**.

3. Click **New Webhook** and provide the following information:

   <!-- -->

   1. `Webhook URL` - enter the value of the `url` key you received after [creating the webhook configuration](/build-your-software-catalog/custom-integration/webhook/.md?operation=ui#configuring-webhook-endpoints).
   2. `Scope Type` - select whether you want to receive webhook events for a specific service (select `Service` if applicable) or for all services in your account (select `Account` if applicable).
   3. `Description` - provide an optional description for your webhook.
   4. `Event Subscription` - choose the event types you would like to subscribe to.
   5. `Custom Header` - enter any optional HTTP header to be added to your webhook payload.

4. Click **Add webhook** to create your webhook.

5. Alternatively, you can use the `curl` method to create the webhook. Copy the code below and run it in your terminal:

```
  curl --request POST \
  --url \
 https://api.pagerduty.com/webhook_subscriptions
  --header 'Accept: application/vnd.pagerduty+json;version=2' \
  --header 'Authorization: Token token=<YOUR_PAGERDUTY_API_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data \
 '{
  "webhook_subscription": {
  "delivery_method": {
    "type": "http_delivery_method",
    "url": "https://ingest.getport.io/<YOUR_PORT_WEBHOOK_KEY>",
    "custom_headers": [
      {
        "name": "your-header-name",
        "value": "your-header-value"
      }
    ]
  },
  "description": "Sends PagerDuty v3 webhook events to Port.",
  "events": [
      "service.created",
      "service.updated",
      "incident.triggered",
      "incident.responder.added",
      "incident.acknowledged",
      "incident.annotated",
      "incident.delegated",
      "incident.escalated",
      "incident.priority_updated",
      "incident.reassigned",
      "incident.reopened",
      "incident.resolved",
      "incident.responder.replied",
      "incident.status_update_published",
      "incident.unacknowledged"
  ],
  "filter": {
    "type": "account_reference"
  },
  "type": "webhook_subscription"
  }
  }'
```

Webhook event types

In order to view the different events available in PagerDuty webhooks, [look here](https://developer.pagerduty.com/docs/db0fa8c8984fc-overview#event-types)

Done! any change that happens to your services or incidents in PagerDuty will trigger a webhook event to the webhook URL provided by Port. Port will parse the events according to the mapping and update the catalog entities accordingly.

## Let's Test It

This section includes a sample webhook event sent from PagerDuty when an incident is created or updated. In addition, it includes the entity created from the event based on the webhook configuration provided in the previous section.

### Payload

Here is an example of the payload structure sent to the webhook URL when a PagerDuty incident is created:

**Webhook event payload (click to expand)**

```
{
  "event": {
    "id": "01DVUHO6P4XQDFJ9AHOADT3UQ4",
    "event_type": "incident.triggered",
    "resource_type": "incident",
    "occurred_at": "2023-06-12T11:56:08.355Z",
    "agent": {
      "html_url": "https://your_account.pagerduty.com/users/PJCRRLH",
      "id": "PJCRRLH",
      "self": "https://api.pagerduty.com/users/PJCRRLH",
      "summary": "username",
      "type": "user_reference"
    },
    "client": "None",
    "data": {
      "id": "Q01J2OS7YBWLNY",
      "type": "incident",
      "self": "https://api.pagerduty.com/incidents/Q01J2OS7YBWLNY",
      "html_url": "https://your_account.pagerduty.com/incidents/Q01J2OS7YBWLNY",
      "number": 7,
      "status": "triggered",
      "incident_key": "acda20953f7446248f90260db65144f8",
      "created_at": "2023-06-12T11:56:08Z",
      "title": "Test PagerDuty Incident",
      "service": {
        "html_url": "https://your_account.pagerduty.com/services/PWJAGSD",
        "id": "PWJAGSD",
        "self": "https://api.pagerduty.com/services/PWJAGSD",
        "summary": "Port Internal Service",
        "type": "service_reference"
      },
      "assignees": [
        {
          "html_url": "https://your_account.pagerduty.com/users/PRGAUI4",
          "id": "PRGAUI4",
          "self": "https://api.pagerduty.com/users/PRGAUI4",
          "summary": "username",
          "type": "user_reference"
        }
      ],
      "escalation_policy": {
        "html_url": "https://your_account.pagerduty.com/escalation_policies/P7LVMYP",
        "id": "P7LVMYP",
        "self": "https://api.pagerduty.com/escalation_policies/P7LVMYP",
        "summary": "Test Escalation Policy",
        "type": "escalation_policy_reference"
      },
      "teams": [],
      "priority": "None",
      "urgency": "high",
      "conference_bridge": "None",
      "resolve_reason": "None"
    }
  }
}
```

### Mapping Result

The combination of the sample payload and the webhook configuration generates the following Port entity:

```
{
  "identifier": "Q01J2OS7YBWLNY",
  "title": "Test PagerDuty Incident",
  "blueprint": "pagerdutyIncident",
  "team": [],
  "properties": {
    "status": "triggered",
    "url": "https://your_account.pagerduty.com/incidents/Q01J2OS7YBWLNY",
    "details": "Test PagerDuty Incident",
    "urgency": "high",
    "responder": "Username",
    "escalation_policy": "Test Escalation Policy"
  },
  "relations": {
    "microservice": "PWJAGSD"
  }
}
```

## Import PagerDuty historical data

In this example you are going to use the provided Bash script to fetch data from the PagerDuty API and ingest it to Port.

The script extracts services and incidents from PagerDuty, and sends them to Port as microservice and incident entities respectively.

### Port configuration

This example utilizes the same [blueprint](#prerequisites) definition from the previous section, along with a new webhook configuration:

Create the following webhook configuration [using Port UI](/build-your-software-catalog/custom-integration/webhook/.md?operation=ui#configuring-webhook-endpoints)

**PagerDuty webhook configuration for historical data (click to expand)**

1. **Basic details** tab - fill the following details:

   1. Title : `PagerDuty History Mapper`;
   2. Identifier : `pagerduty_history_mapper`;
   3. Description : `A webhook configuration to map PagerDuty Historical services and its related incidents to Port`;
   4. Icon : `Pagerduty`;

2. **Integration configuration** tab - fill the following JQ mapping:

   ```
   [
     {
       "blueprint": "microservice",
       "filter": ".body.event.event_type | startswith(\"service\")",
       "entity": {
         "identifier": ".body.event.data.identifier",
         "title": ".body.event.data.title",
         "properties": {
           "status": ".body.event.data.properties.status",
           "url": ".body.event.data.properties.html_url",
           "oncall": ".body.event.data.properties.__oncall_user[] | select(.escalation_level == 1) | .user.email",
           "escalationLevels": ".body.event.data.properties.__oncall_user | map(.escalation_level) | unique | length",
           "meanSecondsToResolve": ".body.event.data.properties.__analytics.mean_seconds_to_resolve",
           "meanSecondsToFirstAck": ".body.event.data.properties.__analytics.mean_seconds_to_first_ack",
           "meanSecondsToEngage": ".body.event.data.properties.__analytics.mean_seconds_to_engage",
         }
       }
     },
     {
       "blueprint": "pagerdutyIncident",
       "filter": ".body.event.event_type | startswith(\"incident\")",
       "entity": {
         "identifier": ".body.event.data.identifier",
         "title": ".body.event.data.title",
         "properties": {
           "status": ".body.event.data.properties.status",
           "url": ".body.event.data.properties.url",
           "details": ".body.event.data.properties.details",
           "priority": ".body.event.data.properties.priority",
           "urgency": ".body.event.data.properties.urgency",
           "responder": ".body.event.data.properties.responder",
           "escalation_policy": ".body.event.data.properties.escalation_policy"
         },
         "relations": {
           "microservice": ".body.event.data.relations.microservice"
         }
       }
     }
   ]
   ```

3. Scroll down to **Advanced settings** and input the following details:

   1. secret: `WEBHOOK_SECRET`;
   2. Signature Header Name : `x-pagerduty-signature`;
   3. Signature Algorithm : Select `sha256` from dropdown option;
   4. Signature Prefix : `v1=`
   5. Click **Save** at the bottom of the page.

Remember to update the `WEBHOOK_SECRET` with the real secret you receive after subscribing to the webhook in PagerDuty.

**PagerDuty Bash script for historical data (click to expand)**

```
#!/bin/bash

set -e
# PagerDuty API endpoints and token
PD_API_SERVICES='https://api.pagerduty.com/services'
PD_API_INCIDENTS='https://api.pagerduty.com/incidents'
PD_TOKEN='API_TOKEN'

# Port webhook URL
PORT_URL='https://ingest.getport.io/WEBHOOK_SECRET'

# Fetch services from PagerDuty
services=$(curl --silent --header "Authorization: Token token=${PD_TOKEN}" --header "Accept: application/vnd.pagerduty+json;version=2" --request GET ${PD_API_SERVICES})

# Extract services array
services_list=$(echo ${services} | jq '.services')

# Iterate over services and push to Port
for i in $(seq 0 $(($(echo ${services_list} | jq '. | length') - 1)))
do
    service=$(echo ${services_list} | jq ".[$i]")

    # Prepare payload for Port
    payload=$(jq -n \
                  --arg id "$(echo ${service} | jq -r '.id')" \
                  --arg name "$(echo ${service} | jq -r '.name')" \
                  --arg status "$(echo ${service} | jq -r '.status')" \
                  '{event: {event_type: "service", data: {identifier: $id, title: $name, properties: {status: $status}}}}')

    # Push to Port
    curl --silent --header 'Content-Type: application/json' --request POST --data "${payload}" ${PORT_URL}

    # Output payload to output.json file
    echo ${payload} >> output.json
done

# Fetch incidents from PagerDuty
incidents=$(curl --silent --header "Authorization: Token token=${PD_TOKEN}" --header "Accept: application/vnd.pagerduty+json;version=2" --request GET ${PD_API_INCIDENTS})

# Extract incidents array
incidents_list=$(echo ${incidents} | jq '.incidents')

# Iterate over incidents and push to Port
for i in $(seq 0 $(($(echo ${incidents_list} | jq '. | length') - 1)))
do
    incident=$(echo ${incidents_list} | jq ".[$i]")

    # Prepare payload for Port
    payload=$(jq -n \
                  --arg id "$(echo ${incident} | jq -r '.id')" \
                  --arg title "$(echo ${incident} | jq -r '.title')" \
                  --arg status "$(echo ${incident} | jq -r '.status')" \
                  --arg url "$(echo ${incident} | jq -r '.html_url')" \
                  --arg description "$(echo ${incident} | jq -r '.description')" \
                  --arg urgency "$(echo ${incident} | jq -r '.urgency')" \
                  --arg responder "$(echo ${incident} | jq -r '.last_status_change_by.summary')" \
                  --arg escalation_policy "$(echo ${incident} | jq -r '.escalation_policy.summary')" \
                  --arg service "$(echo ${incident} | jq -r '.service.id')" \
                  '{event: {event_type: "incident", data: {identifier: $id, title: $title, properties: {status: $status, url: $url, details: $description, urgency: $urgency, responder: $responder, escalation_policy: $escalation_policy}, relations: {microservice: $service}}}}')

    # Push to Port
    curl  --header 'Content-Type: application/json' --request POST --data "${payload}" ${PORT_URL}

    # Output payload to output.json file
    echo ${payload} >> output.json
done
```

### How to Run the script

This script requires two configuration values:

1. `PD_TOKEN`: your PagerDuty API token;
2. `PORT_URL`: your Port webhook URL.

Then trigger the script by running:

```
bash pagerduty_to_port.sh
```

This script fetches services and incidents from PagerDuty and sends them to Port.

Script output

The script writes the JSON payload for each service and incident to a file named `output.json`. This can be useful for debugging if you encounter any issues.

Done! you can now import historical data from PagerDuty into Port. Port will parse the events according to the mapping and update the catalog entities accordingly.
