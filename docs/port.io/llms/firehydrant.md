# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/firehydrant.md

# FireHydrant

![](/img/guides/icons/FireHydrant.svg)![](/img/guides/icons/FireHydrant.svg)

Loading version...

Port's FireHydrant integration allows you to model FireHydrant resources in your software catalog and ingest data into them.

Supported resources ![](/img/icons/external-link.svg)[Environment](https://developers.firehydrant.com/#/operations/getV1Environments)[Service](https://developers.firehydrant.com/#/operations/getV1Services)[Incident](https://developers.firehydrant.com/#/operations/getV1Incidents)[Retrospective](https://developers.firehydrant.com/#/operations/getV1PostMortemsReports)

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
- kind: environment
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        blueprint: '"firehydrantEnvironment"'
        identifier: .id
        title: .name
        properties:
          description: .description
          activeIncidents: .active_incidents | length
          createdAt: .created_at
          updatedAt: .updated_at
- kind: service
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        blueprint: '"firehydrantService"'
        identifier: .id
        title: .name
        properties:
          description: .description
          slug: .slug
          links: .links[].href_url
          labels: .labels
          owner: .owner.name
          activeIncidents: .active_incidents | length
          meanTimeToAcknowledge: '[(.__incidents.milestones[] | map(select(.type == "started" or .type == "acknowledged")) | sort_by(.occurred_at) | group_by(.type) | map(.[0].occurred_at) | select(length == 2) | ([.[1], .[0]] | map(sub("\\.\\d+Z$"; "Z") | fromdate)) | .[1] - .[0] // null)] | add / length / 3600 | floor'
          meanTimeToDetect: '[(.__incidents.milestones[] | map(select(.type == "started" or .type == "detected")) | sort_by(.occurred_at) | group_by(.type) | map(.[0].occurred_at) | select(length == 2) | ([.[1], .[0]] | map(sub("\\.\\d+Z$"; "Z") | fromdate)) | .[1] - .[0] // null)] | add / length / 3600 | floor'
          meanTimeToMitigate: '[(.__incidents.milestones[] | map(select(.type == "started" or .type == "mitigated")) | sort_by(.occurred_at) | group_by(.type) | map(.[0].occurred_at) | select(length == 2) | ([.[1], .[0]] | map(sub("\\.\\d+Z$"; "Z") | fromdate)) | .[1] - .[0] // null)] | add / length / 3600 | floor'
          meanTimeToResolve: '[(.__incidents.milestones[] | map(select(.type == "started" or .type == "resolved")) | sort_by(.occurred_at) | group_by(.type) | map(.[0].occurred_at) | select(length == 2) | ([.[1], .[0]] | map(sub("\\.\\d+Z$"; "Z") | fromdate)) | .[1] - .[0] // null)] | add / length / 3600 | floor'
          createdAt: .created_at
          updatedAt: .updated_at
- kind: incident
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        blueprint: '"firehydrantIncident"'
        identifier: .id
        title: .name
        properties:
          url: .incident_url
          priority: .priority
          severity: .severity
          tags: .tag_list
          currentMilestone: .current_milestone
          functionalities: .functionalities[].name
          description: .description
          customerImpact: .customers_impacted
          commander: .role_assignments[] | select(.incident_role.name == "Commander") | .user.email
          createdBy: .created_by.email
          createdAt: .created_at
        relations:
          environment: .environments | map(.id)
          service: .services | map(.id)
- kind: retrospective
  selector:
    query: .incident.current_milestone == "postmortem_completed"
  port:
    entity:
      mappings:
        blueprint: '"firehydrantRetrospective"'
        identifier: .id
        title: .name
        properties:
          url: .incident.incident_url
          tags: .tag_list
          services: .incident.services[].name
          environments: .incident.environments[].name
          functionalities: .incident.functionalities[].name
          description: .incident.description
          customerImpact: .incident.customers_impacted
          commander: .incident.role_assignments[] | select(.incident_role.name == "Commander") | .user.email
          createdBy: .incident.created_by.email
          resolvedAt: .incident.milestones[] | select(.type == "resolved") | .created_at
          createdAt: .incident.created_at
          publishedAt: .incident.milestones[] | select(.type == "postmortem_completed") | .created_at
          duration: (.incident.milestones | map(select(.type == "started" or .type == "resolved")) | sort_by(.occurred_at) | group_by(.type) | map(.[0].occurred_at) | select(length == 2) | ([.[1], .[0]] | map(sub("\\.\\d+Z$"; "Z") | fromdate)) | .[1] - .[0] // null) | ./3600 | floor
          completedTasks: .__incident.tasks | map(select(.state == "done")) | length
          incompletedTasks: .__incident.tasks | map(select(.state != "done")) | length
          questions: '.questions | map({question: .title, answer: .body})'
        relations:
          incident: .incident.id
```

## Mapping & examples per resource[â](#mapping--examples-per-resource "Direct link to Mapping & examples per resource")

EnvironmentServiceIncidentRetrospective

Default mappingYAML

Sample payloadJSON

Port entityJSON

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).
