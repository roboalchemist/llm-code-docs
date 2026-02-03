# Source: https://docs.datadoghq.com/api/latest/software-catalog.md

---
title: Software Catalog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Software Catalog
---

# Software Catalog

API to create, update, retrieve, and delete Software Catalog entities.

## Get a list of entities{% #get-a-list-of-entities %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/catalog/entity |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/catalog/entity |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/catalog/entity      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/catalog/entity      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/catalog/entity     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/catalog/entity |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/catalog/entity |

### Overview

Get a list of entities from Software Catalog.

OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.



### Arguments

#### Query Strings

| Name                     | Type    | Description                                                                                                                                                                                                                                                                                  |
| ------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page[offset]             | integer | Specific offset to use as the beginning of the returned page.                                                                                                                                                                                                                                |
| page[limit]              | integer | Maximum number of entities in the response.                                                                                                                                                                                                                                                  |
| filter[id]               | string  | Filter entities by UUID.                                                                                                                                                                                                                                                                     |
| filter[ref]              | string  | Filter entities by reference                                                                                                                                                                                                                                                                 |
| filter[name]             | string  | Filter entities by name.                                                                                                                                                                                                                                                                     |
| filter[kind]             | string  | Filter entities by kind.                                                                                                                                                                                                                                                                     |
| filter[owner]            | string  | Filter entities by owner.                                                                                                                                                                                                                                                                    |
| filter[relation][type]   | enum    | Filter entities by relation type.Allowed enum values: `RelationTypeOwns, RelationTypeOwnedBy, RelationTypeDependsOn, RelationTypeDependencyOf, RelationTypePartsOf, RelationTypeHasPart, RelationTypeOtherOwns, RelationTypeOtherOwnedBy, RelationTypeImplementedBy, RelationTypeImplements` |
| filter[exclude_snapshot] | string  | Filter entities by excluding snapshotted entities.                                                                                                                                                                                                                                           |
| include                  | enum    | Include relationship data.Allowed enum values: `schema, raw_schema, oncall, incident, relation`                                                                                                                                                                                              |
| includeDiscovered        | boolean | If true, includes discovered services from APM and USM that do not have entity definitions.                                                                                                                                                                                                  |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List entity response.

| Parent field     | Field                        | Type            | Description                                                                                                                                                                                                                                           |
| ---------------- | ---------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                  | data                         | [object]        | List of entity data.                                                                                                                                                                                                                                  |
| data             | attributes                   | object          | Entity attributes.                                                                                                                                                                                                                                    |
| attributes       | apiVersion                   | string          | The API version.                                                                                                                                                                                                                                      |
| attributes       | description                  | string          | The description.                                                                                                                                                                                                                                      |
| attributes       | displayName                  | string          | The display name.                                                                                                                                                                                                                                     |
| attributes       | kind                         | string          | The kind.                                                                                                                                                                                                                                             |
| attributes       | name                         | string          | The name.                                                                                                                                                                                                                                             |
| attributes       | namespace                    | string          | The namespace.                                                                                                                                                                                                                                        |
| attributes       | owner                        | string          | The owner.                                                                                                                                                                                                                                            |
| attributes       | tags                         | [string]        | The tags.                                                                                                                                                                                                                                             |
| data             | id                           | string          | Entity ID.                                                                                                                                                                                                                                            |
| data             | meta                         | object          | Entity metadata.                                                                                                                                                                                                                                      |
| meta             | createdAt                    | string          | The creation time.                                                                                                                                                                                                                                    |
| meta             | ingestionSource              | string          | The ingestion source.                                                                                                                                                                                                                                 |
| meta             | modifiedAt                   | string          | The modification time.                                                                                                                                                                                                                                |
| meta             | origin                       | string          | The origin.                                                                                                                                                                                                                                           |
| data             | relationships                | object          | Entity relationships.                                                                                                                                                                                                                                 |
| relationships    | incidents                    | object          | Entity to incidents relationship.                                                                                                                                                                                                                     |
| incidents        | data                         | [object]        | Relationships.                                                                                                                                                                                                                                        |
| data             | id                           | string          | Associated data ID.                                                                                                                                                                                                                                   |
| data             | type                         | string          | Relationship type.                                                                                                                                                                                                                                    |
| relationships    | oncall                       | object          | Entity to oncalls relationship.                                                                                                                                                                                                                       |
| oncall           | data                         | [object]        | Relationships.                                                                                                                                                                                                                                        |
| data             | id                           | string          | Associated data ID.                                                                                                                                                                                                                                   |
| data             | type                         | string          | Relationship type.                                                                                                                                                                                                                                    |
| relationships    | rawSchema                    | object          | Entity to raw schema relationship.                                                                                                                                                                                                                    |
| rawSchema        | data                         | object          | Relationship entry.                                                                                                                                                                                                                                   |
| data             | id                           | string          | Associated data ID.                                                                                                                                                                                                                                   |
| data             | type                         | string          | Relationship type.                                                                                                                                                                                                                                    |
| relationships    | relatedEntities              | object          | Entity to related entities relationship.                                                                                                                                                                                                              |
| relatedEntities  | data                         | [object]        | Relationships.                                                                                                                                                                                                                                        |
| data             | id                           | string          | Associated data ID.                                                                                                                                                                                                                                   |
| data             | type                         | string          | Relationship type.                                                                                                                                                                                                                                    |
| relationships    | schema                       | object          | Entity to detail schema relationship.                                                                                                                                                                                                                 |
| schema           | data                         | object          | Relationship entry.                                                                                                                                                                                                                                   |
| data             | id                           | string          | Associated data ID.                                                                                                                                                                                                                                   |
| data             | type                         | string          | Relationship type.                                                                                                                                                                                                                                    |
| data             | type                         | string          | Entity.                                                                                                                                                                                                                                               |
|                  | included                     | [ <oneOf>] | List entity response included.                                                                                                                                                                                                                        |
| included         | Option 1                     | object          | Included detail entity schema.                                                                                                                                                                                                                        |
| Option 1         | attributes                   | object          | Included schema.                                                                                                                                                                                                                                      |
| attributes       | schema                       |  <oneOf>   | Entity schema v3.                                                                                                                                                                                                                                     |
| schema           | Option 1                     | object          | Schema for service entities.                                                                                                                                                                                                                          |
| Option 1         | apiVersion [*required*] | enum            | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 1         | datadog                      | object          | Datadog product integrations for the service entity.                                                                                                                                                                                                  |
| datadog          | codeLocations                | [object]        | Schema for mapping source code locations to an entity.                                                                                                                                                                                                |
| codeLocations    | paths                        | [string]        | The paths (glob) to the source code of the service.                                                                                                                                                                                                   |
| codeLocations    | repositoryURL                | string          | The repository path of the source code of the entity.                                                                                                                                                                                                 |
| datadog          | events                       | [object]        | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]        | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object          | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]        | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| datadog          | pipelines                    | object          | CI Pipelines association.                                                                                                                                                                                                                             |
| pipelines        | fingerprints                 | [string]        | A list of CI Fingerprints that associate CI Pipelines with the entity.                                                                                                                                                                                |
| Option 1         | extensions                   | object          | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 1         | integrations                 | object          | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object          | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string          | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string          | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object          | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string          | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 1         | kind [*required*]       | enum            | The definition of Entity V3 Service Kind object. Allowed enum values: `service`                                                                                                                                                                       |
| Option 1         | metadata [*required*]   | object          | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]        | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string          | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string          | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]        | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string          | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string          | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string          | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string          | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string          | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string          | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string          | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]        | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string          | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string          | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string          | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string          | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object          | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string          | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string          | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string          | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]        | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 1         | spec                         | object          | The definition of Entity V3 Service Spec object.                                                                                                                                                                                                      |
| spec             | componentOf                  | [string]        | A list of components the service is a part of                                                                                                                                                                                                         |
| spec             | dependsOn                    | [string]        | A list of components the service depends on.                                                                                                                                                                                                          |
| spec             | languages                    | [string]        | The service's programming language.                                                                                                                                                                                                                   |
| spec             | lifecycle                    | string          | The lifecycle state of the component.                                                                                                                                                                                                                 |
| spec             | tier                         | string          | The importance of the component.                                                                                                                                                                                                                      |
| spec             | type                         | string          | The type of service.                                                                                                                                                                                                                                  |
| schema           | Option 2                     | object          | Schema for datastore entities.                                                                                                                                                                                                                        |
| Option 2         | apiVersion [*required*] | enum            | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 2         | datadog                      | object          | Datadog product integrations for the datastore entity.                                                                                                                                                                                                |
| datadog          | events                       | [object]        | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]        | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object          | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]        | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| Option 2         | extensions                   | object          | Custom extensions. This is the free-formed field to send client side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 2         | integrations                 | object          | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object          | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string          | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string          | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object          | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string          | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 2         | kind [*required*]       | enum            | The definition of Entity V3 Datastore Kind object. Allowed enum values: `datastore`                                                                                                                                                                   |
| Option 2         | metadata [*required*]   | object          | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]        | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string          | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string          | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]        | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string          | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string          | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string          | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string          | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string          | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string          | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string          | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]        | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string          | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string          | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string          | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string          | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object          | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string          | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string          | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string          | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]        | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 2         | spec                         | object          | The definition of Entity V3 Datastore Spec object.                                                                                                                                                                                                    |
| spec             | componentOf                  | [string]        | A list of components the datastore is a part of                                                                                                                                                                                                       |
| spec             | lifecycle                    | string          | The lifecycle state of the datastore.                                                                                                                                                                                                                 |
| spec             | tier                         | string          | The importance of the datastore.                                                                                                                                                                                                                      |
| spec             | type                         | string          | The type of datastore.                                                                                                                                                                                                                                |
| schema           | Option 3                     | object          | Schema for queue entities.                                                                                                                                                                                                                            |
| Option 3         | apiVersion [*required*] | enum            | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 3         | datadog                      | object          | Datadog product integrations for the datastore entity.                                                                                                                                                                                                |
| datadog          | events                       | [object]        | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]        | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object          | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]        | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| Option 3         | extensions                   | object          | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 3         | integrations                 | object          | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object          | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string          | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string          | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object          | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string          | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 3         | kind [*required*]       | enum            | The definition of Entity V3 Queue Kind object. Allowed enum values: `queue`                                                                                                                                                                           |
| Option 3         | metadata [*required*]   | object          | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]        | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string          | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string          | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]        | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string          | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string          | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string          | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string          | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string          | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string          | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string          | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]        | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string          | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string          | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string          | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string          | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object          | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string          | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string          | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string          | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]        | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 3         | spec                         | object          | The definition of Entity V3 Queue Spec object.                                                                                                                                                                                                        |
| spec             | componentOf                  | [string]        | A list of components the queue is a part of                                                                                                                                                                                                           |
| spec             | lifecycle                    | string          | The lifecycle state of the queue.                                                                                                                                                                                                                     |
| spec             | tier                         | string          | The importance of the queue.                                                                                                                                                                                                                          |
| spec             | type                         | string          | The type of queue.                                                                                                                                                                                                                                    |
| schema           | Option 4                     | object          | Schema for system entities.                                                                                                                                                                                                                           |
| Option 4         | apiVersion [*required*] | enum            | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 4         | datadog                      | object          | Datadog product integrations for the service entity.                                                                                                                                                                                                  |
| datadog          | events                       | [object]        | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]        | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object          | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]        | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| datadog          | pipelines                    | object          | CI Pipelines association.                                                                                                                                                                                                                             |
| pipelines        | fingerprints                 | [string]        | A list of CI Fingerprints that associate CI Pipelines with the entity.                                                                                                                                                                                |
| Option 4         | extensions                   | object          | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 4         | integrations                 | object          | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object          | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string          | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string          | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object          | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string          | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 4         | kind [*required*]       | enum            | The definition of Entity V3 System Kind object. Allowed enum values: `system`                                                                                                                                                                         |
| Option 4         | metadata [*required*]   | object          | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]        | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string          | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string          | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]        | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string          | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string          | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string          | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string          | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string          | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string          | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string          | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]        | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string          | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string          | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string          | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string          | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object          | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string          | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string          | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string          | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]        | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 4         | spec                         | object          | The definition of Entity V3 System Spec object.                                                                                                                                                                                                       |
| spec             | components                   | [string]        | A list of components belongs to the system.                                                                                                                                                                                                           |
| spec             | lifecycle                    | string          | The lifecycle state of the component.                                                                                                                                                                                                                 |
| spec             | tier                         | string          | An entity reference to the owner of the component.                                                                                                                                                                                                    |
| schema           | Option 5                     | object          | Schema for API entities.                                                                                                                                                                                                                              |
| Option 5         | apiVersion [*required*] | enum            | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 5         | datadog                      | object          | Datadog product integrations for the API entity.                                                                                                                                                                                                      |
| datadog          | codeLocations                | [object]        | Schema for mapping source code locations to an entity.                                                                                                                                                                                                |
| codeLocations    | paths                        | [string]        | The paths (glob) to the source code of the service.                                                                                                                                                                                                   |
| codeLocations    | repositoryURL                | string          | The repository path of the source code of the entity.                                                                                                                                                                                                 |
| datadog          | events                       | [object]        | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]        | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object          | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]        | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| datadog          | pipelines                    | object          | CI Pipelines association.                                                                                                                                                                                                                             |
| pipelines        | fingerprints                 | [string]        | A list of CI Fingerprints that associate CI Pipelines with the entity.                                                                                                                                                                                |
| Option 5         | extensions                   | object          | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 5         | integrations                 | object          | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object          | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string          | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string          | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object          | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string          | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 5         | kind [*required*]       | enum            | The definition of Entity V3 API Kind object. Allowed enum values: `api`                                                                                                                                                                               |
| Option 5         | metadata [*required*]   | object          | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]        | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string          | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string          | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]        | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string          | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string          | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string          | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string          | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string          | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string          | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string          | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]        | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string          | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string          | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string          | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string          | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object          | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string          | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string          | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string          | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]        | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 5         | spec                         | object          | The definition of Entity V3 API Spec object.                                                                                                                                                                                                          |
| spec             | implementedBy                | [string]        | Services which implemented the API.                                                                                                                                                                                                                   |
| spec             | interface                    |  <oneOf>   | The API definition.                                                                                                                                                                                                                                   |
| spec             | lifecycle                    | string          | The lifecycle state of the component.                                                                                                                                                                                                                 |
| spec             | tier                         | string          | The importance of the component.                                                                                                                                                                                                                      |
| spec             | type                         | string          | The type of API.                                                                                                                                                                                                                                      |
| Option 1         | id                           | string          | Entity ID.                                                                                                                                                                                                                                            |
| Option 1         | type                         | enum            | Schema type. Allowed enum values: `schema`                                                                                                                                                                                                            |
| included         | Option 2                     | object          | Included raw schema.                                                                                                                                                                                                                                  |
| Option 2         | attributes                   | object          | Included raw schema attributes.                                                                                                                                                                                                                       |
| attributes       | rawSchema                    | string          | Schema from user input in base64 encoding.                                                                                                                                                                                                            |
| Option 2         | id                           | string          | Raw schema ID.                                                                                                                                                                                                                                        |
| Option 2         | type                         | enum            | Raw schema type. Allowed enum values: `rawSchema`                                                                                                                                                                                                     |
| included         | Option 3                     | object          | Included related entity.                                                                                                                                                                                                                              |
| Option 3         | attributes                   | object          | Related entity attributes.                                                                                                                                                                                                                            |
| attributes       | kind                         | string          | Entity kind.                                                                                                                                                                                                                                          |
| attributes       | name                         | string          | Entity name.                                                                                                                                                                                                                                          |
| attributes       | namespace                    | string          | Entity namespace.                                                                                                                                                                                                                                     |
| attributes       | type                         | string          | Entity relation type to the associated entity.                                                                                                                                                                                                        |
| Option 3         | id                           | string          | Entity UUID.                                                                                                                                                                                                                                          |
| Option 3         | meta                         | object          | Included related entity meta.                                                                                                                                                                                                                         |
| meta             | createdAt                    | date-time       | Entity creation time.                                                                                                                                                                                                                                 |
| meta             | defined_by                   | string          | Entity relation defined by.                                                                                                                                                                                                                           |
| meta             | modifiedAt                   | date-time       | Entity modification time.                                                                                                                                                                                                                             |
| meta             | source                       | string          | Entity relation source.                                                                                                                                                                                                                               |
| Option 3         | type                         | enum            | Related entity. Allowed enum values: `relatedEntity`                                                                                                                                                                                                  |
| included         | Option 4                     | object          | Included oncall.                                                                                                                                                                                                                                      |
| Option 4         | attributes                   | object          | Included related oncall attributes.                                                                                                                                                                                                                   |
| attributes       | escalations                  | [object]        | Oncall escalations.                                                                                                                                                                                                                                   |
| escalations      | email                        | string          | Oncall email.                                                                                                                                                                                                                                         |
| escalations      | escalationLevel              | int64           | Oncall level.                                                                                                                                                                                                                                         |
| escalations      | name                         | string          | Oncall name.                                                                                                                                                                                                                                          |
| attributes       | provider                     | string          | Oncall provider.                                                                                                                                                                                                                                      |
| Option 4         | id                           | string          | Oncall ID.                                                                                                                                                                                                                                            |
| Option 4         | type                         | enum            | Oncall type. Allowed enum values: `oncall`                                                                                                                                                                                                            |
| included         | Option 5                     | object          | Included incident.                                                                                                                                                                                                                                    |
| Option 5         | attributes                   | object          | Incident attributes.                                                                                                                                                                                                                                  |
| attributes       | createdAt                    | date-time       | Incident creation time.                                                                                                                                                                                                                               |
| attributes       | htmlURL                      | string          | Incident URL.                                                                                                                                                                                                                                         |
| attributes       | provider                     | string          | Incident provider.                                                                                                                                                                                                                                    |
| attributes       | status                       | string          | Incident status.                                                                                                                                                                                                                                      |
| attributes       | title                        | string          | Incident title.                                                                                                                                                                                                                                       |
| Option 5         | id                           | string          | Incident ID.                                                                                                                                                                                                                                          |
| Option 5         | type                         | enum            | Incident description. Allowed enum values: `incident`                                                                                                                                                                                                 |
|                  | links                        | object          | List entity response links.                                                                                                                                                                                                                           |
| links            | next                         | string          | Next link.                                                                                                                                                                                                                                            |
| links            | previous                     | string          | Previous link.                                                                                                                                                                                                                                        |
| links            | self                         | string          | Current link.                                                                                                                                                                                                                                         |
|                  | meta                         | object          | Entity metadata.                                                                                                                                                                                                                                      |
| meta             | count                        | int64           | Total entities count.                                                                                                                                                                                                                                 |
| meta             | includeCount                 | int64           | Total included data count.                                                                                                                                                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "apiVersion": "string",
        "description": "string",
        "displayName": "string",
        "kind": "string",
        "name": "string",
        "namespace": "string",
        "owner": "string",
        "tags": []
      },
      "id": "string",
      "meta": {
        "createdAt": "string",
        "ingestionSource": "string",
        "modifiedAt": "string",
        "origin": "string"
      },
      "relationships": {
        "incidents": {
          "data": [
            {
              "id": "string",
              "type": "string"
            }
          ]
        },
        "oncall": {
          "data": [
            {
              "id": "string",
              "type": "string"
            }
          ]
        },
        "rawSchema": {
          "data": {
            "id": "string",
            "type": "string"
          }
        },
        "relatedEntities": {
          "data": [
            {
              "id": "string",
              "type": "string"
            }
          ]
        },
        "schema": {
          "data": {
            "id": "string",
            "type": "string"
          }
        }
      },
      "type": "string"
    }
  ],
  "included": [
    {
      "attributes": {
        "schema": {
          "apiVersion": "v3",
          "datadog": {
            "codeLocations": [
              {
                "paths": [],
                "repositoryURL": "string"
              }
            ],
            "events": [
              {
                "name": "string",
                "query": "string"
              }
            ],
            "logs": [
              {
                "name": "string",
                "query": "string"
              }
            ],
            "performanceData": {
              "tags": []
            },
            "pipelines": {
              "fingerprints": []
            }
          },
          "extensions": {},
          "integrations": {
            "opsgenie": {
              "region": "string",
              "serviceURL": "https://www.opsgenie.com/service/shopping-cart"
            },
            "pagerduty": {
              "serviceURL": "https://www.pagerduty.com/service-directory/Pshopping-cart"
            }
          },
          "kind": "service",
          "metadata": {
            "additionalOwners": [
              {
                "name": "",
                "type": "string"
              }
            ],
            "contacts": [
              {
                "contact": "https://slack/",
                "name": "string",
                "type": "slack"
              }
            ],
            "description": "string",
            "displayName": "string",
            "id": "4b163705-23c0-4573-b2fb-f6cea2163fcb",
            "inheritFrom": "application:default/myapp",
            "links": [
              {
                "name": "mylink",
                "provider": "string",
                "type": "link",
                "url": "https://mylink"
              }
            ],
            "managed": {},
            "name": "myService",
            "namespace": "default",
            "owner": "string",
            "tags": [
              "this:tag",
              "that:tag"
            ]
          },
          "spec": {
            "componentOf": [],
            "dependsOn": [],
            "languages": [],
            "lifecycle": "string",
            "tier": "string",
            "type": "string"
          }
        }
      },
      "id": "string",
      "type": "string"
    }
  ],
  "links": {
    "next": "string",
    "previous": "string",
    "self": "string"
  },
  "meta": {
    "count": "integer",
    "includeCount": "integer"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/entity" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a list of entities returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    response = api_instance.list_catalog_entity()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a list of entities returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
p api_instance.list_catalog_entity()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a list of entities returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSoftwareCatalogApi(apiClient)
	resp, r, err := api.ListCatalogEntity(ctx, *datadogV2.NewListCatalogEntityOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareCatalogApi.ListCatalogEntity`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SoftwareCatalogApi.ListCatalogEntity`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a list of entities returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SoftwareCatalogApi;
import com.datadog.api.client.v2.model.ListEntityCatalogResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SoftwareCatalogApi apiInstance = new SoftwareCatalogApi(defaultClient);

    try {
      ListEntityCatalogResponse result = apiInstance.listCatalogEntity();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareCatalogApi#listCatalogEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
// Get a list of entities returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_software_catalog::ListCatalogEntityOptionalParams;
use datadog_api_client::datadogV2::api_software_catalog::SoftwareCatalogAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SoftwareCatalogAPI::with_config(configuration);
    let resp = api
        .list_catalog_entity(ListCatalogEntityOptionalParams::default())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Get a list of entities returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SoftwareCatalogApi(configuration);

apiInstance
  .listCatalogEntity()
  .then((data: v2.ListEntityCatalogResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create or update entities{% #create-or-update-entities %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/catalog/entity |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/catalog/entity |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/catalog/entity      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/catalog/entity      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/catalog/entity     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/catalog/entity |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/catalog/entity |

### Overview

Create or update entities in Software Catalog.

OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.



### Request

#### Body Data (required)

Entity YAML or JSON.

{% tab title="Model" %}

| Parent field     | Field                        | Type          | Description                                                                                                                                                                                                                                           |
| ---------------- | ---------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                  | Option 1                     |  <oneOf> | Entity schema v3.                                                                                                                                                                                                                                     |
| Option 1         | Option 1                     | object        | Schema for service entities.                                                                                                                                                                                                                          |
| Option 1         | apiVersion [*required*] | enum          | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 1         | datadog                      | object        | Datadog product integrations for the service entity.                                                                                                                                                                                                  |
| datadog          | codeLocations                | [object]      | Schema for mapping source code locations to an entity.                                                                                                                                                                                                |
| codeLocations    | paths                        | [string]      | The paths (glob) to the source code of the service.                                                                                                                                                                                                   |
| codeLocations    | repositoryURL                | string        | The repository path of the source code of the entity.                                                                                                                                                                                                 |
| datadog          | events                       | [object]      | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string        | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string        | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]      | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string        | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string        | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object        | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]      | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| datadog          | pipelines                    | object        | CI Pipelines association.                                                                                                                                                                                                                             |
| pipelines        | fingerprints                 | [string]      | A list of CI Fingerprints that associate CI Pipelines with the entity.                                                                                                                                                                                |
| Option 1         | extensions                   | object        | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 1         | integrations                 | object        | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object        | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string        | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string        | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object        | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string        | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 1         | kind [*required*]       | enum          | The definition of Entity V3 Service Kind object. Allowed enum values: `service`                                                                                                                                                                       |
| Option 1         | metadata [*required*]   | object        | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]      | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string        | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string        | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]      | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string        | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string        | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string        | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string        | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string        | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string        | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string        | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]      | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string        | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string        | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string        | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string        | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object        | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string        | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string        | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string        | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]      | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 1         | spec                         | object        | The definition of Entity V3 Service Spec object.                                                                                                                                                                                                      |
| spec             | componentOf                  | [string]      | A list of components the service is a part of                                                                                                                                                                                                         |
| spec             | dependsOn                    | [string]      | A list of components the service depends on.                                                                                                                                                                                                          |
| spec             | languages                    | [string]      | The service's programming language.                                                                                                                                                                                                                   |
| spec             | lifecycle                    | string        | The lifecycle state of the component.                                                                                                                                                                                                                 |
| spec             | tier                         | string        | The importance of the component.                                                                                                                                                                                                                      |
| spec             | type                         | string        | The type of service.                                                                                                                                                                                                                                  |
| Option 1         | Option 2                     | object        | Schema for datastore entities.                                                                                                                                                                                                                        |
| Option 2         | apiVersion [*required*] | enum          | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 2         | datadog                      | object        | Datadog product integrations for the datastore entity.                                                                                                                                                                                                |
| datadog          | events                       | [object]      | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string        | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string        | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]      | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string        | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string        | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object        | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]      | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| Option 2         | extensions                   | object        | Custom extensions. This is the free-formed field to send client side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 2         | integrations                 | object        | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object        | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string        | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string        | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object        | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string        | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 2         | kind [*required*]       | enum          | The definition of Entity V3 Datastore Kind object. Allowed enum values: `datastore`                                                                                                                                                                   |
| Option 2         | metadata [*required*]   | object        | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]      | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string        | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string        | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]      | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string        | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string        | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string        | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string        | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string        | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string        | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string        | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]      | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string        | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string        | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string        | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string        | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object        | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string        | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string        | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string        | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]      | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 2         | spec                         | object        | The definition of Entity V3 Datastore Spec object.                                                                                                                                                                                                    |
| spec             | componentOf                  | [string]      | A list of components the datastore is a part of                                                                                                                                                                                                       |
| spec             | lifecycle                    | string        | The lifecycle state of the datastore.                                                                                                                                                                                                                 |
| spec             | tier                         | string        | The importance of the datastore.                                                                                                                                                                                                                      |
| spec             | type                         | string        | The type of datastore.                                                                                                                                                                                                                                |
| Option 1         | Option 3                     | object        | Schema for queue entities.                                                                                                                                                                                                                            |
| Option 3         | apiVersion [*required*] | enum          | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 3         | datadog                      | object        | Datadog product integrations for the datastore entity.                                                                                                                                                                                                |
| datadog          | events                       | [object]      | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string        | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string        | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]      | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string        | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string        | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object        | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]      | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| Option 3         | extensions                   | object        | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 3         | integrations                 | object        | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object        | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string        | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string        | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object        | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string        | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 3         | kind [*required*]       | enum          | The definition of Entity V3 Queue Kind object. Allowed enum values: `queue`                                                                                                                                                                           |
| Option 3         | metadata [*required*]   | object        | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]      | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string        | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string        | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]      | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string        | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string        | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string        | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string        | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string        | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string        | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string        | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]      | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string        | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string        | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string        | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string        | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object        | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string        | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string        | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string        | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]      | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 3         | spec                         | object        | The definition of Entity V3 Queue Spec object.                                                                                                                                                                                                        |
| spec             | componentOf                  | [string]      | A list of components the queue is a part of                                                                                                                                                                                                           |
| spec             | lifecycle                    | string        | The lifecycle state of the queue.                                                                                                                                                                                                                     |
| spec             | tier                         | string        | The importance of the queue.                                                                                                                                                                                                                          |
| spec             | type                         | string        | The type of queue.                                                                                                                                                                                                                                    |
| Option 1         | Option 4                     | object        | Schema for system entities.                                                                                                                                                                                                                           |
| Option 4         | apiVersion [*required*] | enum          | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 4         | datadog                      | object        | Datadog product integrations for the service entity.                                                                                                                                                                                                  |
| datadog          | events                       | [object]      | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string        | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string        | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]      | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string        | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string        | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object        | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]      | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| datadog          | pipelines                    | object        | CI Pipelines association.                                                                                                                                                                                                                             |
| pipelines        | fingerprints                 | [string]      | A list of CI Fingerprints that associate CI Pipelines with the entity.                                                                                                                                                                                |
| Option 4         | extensions                   | object        | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 4         | integrations                 | object        | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object        | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string        | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string        | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object        | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string        | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 4         | kind [*required*]       | enum          | The definition of Entity V3 System Kind object. Allowed enum values: `system`                                                                                                                                                                         |
| Option 4         | metadata [*required*]   | object        | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]      | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string        | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string        | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]      | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string        | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string        | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string        | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string        | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string        | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string        | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string        | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]      | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string        | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string        | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string        | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string        | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object        | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string        | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string        | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string        | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]      | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 4         | spec                         | object        | The definition of Entity V3 System Spec object.                                                                                                                                                                                                       |
| spec             | components                   | [string]      | A list of components belongs to the system.                                                                                                                                                                                                           |
| spec             | lifecycle                    | string        | The lifecycle state of the component.                                                                                                                                                                                                                 |
| spec             | tier                         | string        | An entity reference to the owner of the component.                                                                                                                                                                                                    |
| Option 1         | Option 5                     | object        | Schema for API entities.                                                                                                                                                                                                                              |
| Option 5         | apiVersion [*required*] | enum          | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 5         | datadog                      | object        | Datadog product integrations for the API entity.                                                                                                                                                                                                      |
| datadog          | codeLocations                | [object]      | Schema for mapping source code locations to an entity.                                                                                                                                                                                                |
| codeLocations    | paths                        | [string]      | The paths (glob) to the source code of the service.                                                                                                                                                                                                   |
| codeLocations    | repositoryURL                | string        | The repository path of the source code of the entity.                                                                                                                                                                                                 |
| datadog          | events                       | [object]      | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string        | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string        | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]      | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string        | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string        | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object        | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]      | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| datadog          | pipelines                    | object        | CI Pipelines association.                                                                                                                                                                                                                             |
| pipelines        | fingerprints                 | [string]      | A list of CI Fingerprints that associate CI Pipelines with the entity.                                                                                                                                                                                |
| Option 5         | extensions                   | object        | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 5         | integrations                 | object        | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object        | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string        | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string        | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object        | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string        | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 5         | kind [*required*]       | enum          | The definition of Entity V3 API Kind object. Allowed enum values: `api`                                                                                                                                                                               |
| Option 5         | metadata [*required*]   | object        | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]      | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string        | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string        | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]      | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string        | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string        | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string        | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string        | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string        | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string        | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string        | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]      | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string        | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string        | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string        | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string        | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object        | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string        | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string        | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string        | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]      | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 5         | spec                         | object        | The definition of Entity V3 API Spec object.                                                                                                                                                                                                          |
| spec             | implementedBy                | [string]      | Services which implemented the API.                                                                                                                                                                                                                   |
| spec             | interface                    |  <oneOf> | The API definition.                                                                                                                                                                                                                                   |
| spec             | lifecycle                    | string        | The lifecycle state of the component.                                                                                                                                                                                                                 |
| spec             | tier                         | string        | The importance of the component.                                                                                                                                                                                                                      |
| spec             | type                         | string        | The type of API.                                                                                                                                                                                                                                      |
|                  | Option 2                     | string        | Entity definition in raw JSON or YAML representation.                                                                                                                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "apiVersion": "v3",
  "datadog": {
    "codeLocations": [
      {
        "paths": []
      }
    ],
    "events": [
      {}
    ],
    "logs": [
      {}
    ],
    "performanceData": {
      "tags": []
    },
    "pipelines": {
      "fingerprints": []
    }
  },
  "integrations": {
    "opsgenie": {
      "serviceURL": "https://www.opsgenie.com/service/shopping-cart"
    },
    "pagerduty": {
      "serviceURL": "https://www.pagerduty.com/service-directory/Pshopping-cart"
    }
  },
  "kind": "service",
  "metadata": {
    "additionalOwners": [],
    "contacts": [
      {
        "contact": "https://slack/",
        "type": "slack"
      }
    ],
    "id": "4b163705-23c0-4573-b2fb-f6cea2163fcb",
    "inheritFrom": "application:default/myapp",
    "links": [
      {
        "name": "mylink",
        "type": "link",
        "url": "https://mylink"
      }
    ],
    "name": "service-examplesoftwarecatalog",
    "tags": [
      "this:tag",
      "that:tag"
    ]
  },
  "spec": {
    "dependsOn": [],
    "languages": []
  }
}
```

{% /tab %}

### Response

{% tab title="202" %}
ACCEPTED
{% tab title="Model" %}
Upsert entity response.

| Parent field     | Field                        | Type            | Description                                                                                                                                                                                                                                           |
| ---------------- | ---------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                  | data                         | [object]        | List of entity data.                                                                                                                                                                                                                                  |
| data             | attributes                   | object          | Entity attributes.                                                                                                                                                                                                                                    |
| attributes       | apiVersion                   | string          | The API version.                                                                                                                                                                                                                                      |
| attributes       | description                  | string          | The description.                                                                                                                                                                                                                                      |
| attributes       | displayName                  | string          | The display name.                                                                                                                                                                                                                                     |
| attributes       | kind                         | string          | The kind.                                                                                                                                                                                                                                             |
| attributes       | name                         | string          | The name.                                                                                                                                                                                                                                             |
| attributes       | namespace                    | string          | The namespace.                                                                                                                                                                                                                                        |
| attributes       | owner                        | string          | The owner.                                                                                                                                                                                                                                            |
| attributes       | tags                         | [string]        | The tags.                                                                                                                                                                                                                                             |
| data             | id                           | string          | Entity ID.                                                                                                                                                                                                                                            |
| data             | meta                         | object          | Entity metadata.                                                                                                                                                                                                                                      |
| meta             | createdAt                    | string          | The creation time.                                                                                                                                                                                                                                    |
| meta             | ingestionSource              | string          | The ingestion source.                                                                                                                                                                                                                                 |
| meta             | modifiedAt                   | string          | The modification time.                                                                                                                                                                                                                                |
| meta             | origin                       | string          | The origin.                                                                                                                                                                                                                                           |
| data             | relationships                | object          | Entity relationships.                                                                                                                                                                                                                                 |
| relationships    | incidents                    | object          | Entity to incidents relationship.                                                                                                                                                                                                                     |
| incidents        | data                         | [object]        | Relationships.                                                                                                                                                                                                                                        |
| data             | id                           | string          | Associated data ID.                                                                                                                                                                                                                                   |
| data             | type                         | string          | Relationship type.                                                                                                                                                                                                                                    |
| relationships    | oncall                       | object          | Entity to oncalls relationship.                                                                                                                                                                                                                       |
| oncall           | data                         | [object]        | Relationships.                                                                                                                                                                                                                                        |
| data             | id                           | string          | Associated data ID.                                                                                                                                                                                                                                   |
| data             | type                         | string          | Relationship type.                                                                                                                                                                                                                                    |
| relationships    | rawSchema                    | object          | Entity to raw schema relationship.                                                                                                                                                                                                                    |
| rawSchema        | data                         | object          | Relationship entry.                                                                                                                                                                                                                                   |
| data             | id                           | string          | Associated data ID.                                                                                                                                                                                                                                   |
| data             | type                         | string          | Relationship type.                                                                                                                                                                                                                                    |
| relationships    | relatedEntities              | object          | Entity to related entities relationship.                                                                                                                                                                                                              |
| relatedEntities  | data                         | [object]        | Relationships.                                                                                                                                                                                                                                        |
| data             | id                           | string          | Associated data ID.                                                                                                                                                                                                                                   |
| data             | type                         | string          | Relationship type.                                                                                                                                                                                                                                    |
| relationships    | schema                       | object          | Entity to detail schema relationship.                                                                                                                                                                                                                 |
| schema           | data                         | object          | Relationship entry.                                                                                                                                                                                                                                   |
| data             | id                           | string          | Associated data ID.                                                                                                                                                                                                                                   |
| data             | type                         | string          | Relationship type.                                                                                                                                                                                                                                    |
| data             | type                         | string          | Entity.                                                                                                                                                                                                                                               |
|                  | included                     | [ <oneOf>] | Upsert entity response included.                                                                                                                                                                                                                      |
| included         | Option 1                     | object          | Included detail entity schema.                                                                                                                                                                                                                        |
| Option 1         | attributes                   | object          | Included schema.                                                                                                                                                                                                                                      |
| attributes       | schema                       |  <oneOf>   | Entity schema v3.                                                                                                                                                                                                                                     |
| schema           | Option 1                     | object          | Schema for service entities.                                                                                                                                                                                                                          |
| Option 1         | apiVersion [*required*] | enum            | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 1         | datadog                      | object          | Datadog product integrations for the service entity.                                                                                                                                                                                                  |
| datadog          | codeLocations                | [object]        | Schema for mapping source code locations to an entity.                                                                                                                                                                                                |
| codeLocations    | paths                        | [string]        | The paths (glob) to the source code of the service.                                                                                                                                                                                                   |
| codeLocations    | repositoryURL                | string          | The repository path of the source code of the entity.                                                                                                                                                                                                 |
| datadog          | events                       | [object]        | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]        | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object          | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]        | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| datadog          | pipelines                    | object          | CI Pipelines association.                                                                                                                                                                                                                             |
| pipelines        | fingerprints                 | [string]        | A list of CI Fingerprints that associate CI Pipelines with the entity.                                                                                                                                                                                |
| Option 1         | extensions                   | object          | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 1         | integrations                 | object          | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object          | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string          | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string          | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object          | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string          | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 1         | kind [*required*]       | enum            | The definition of Entity V3 Service Kind object. Allowed enum values: `service`                                                                                                                                                                       |
| Option 1         | metadata [*required*]   | object          | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]        | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string          | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string          | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]        | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string          | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string          | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string          | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string          | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string          | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string          | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string          | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]        | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string          | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string          | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string          | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string          | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object          | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string          | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string          | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string          | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]        | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 1         | spec                         | object          | The definition of Entity V3 Service Spec object.                                                                                                                                                                                                      |
| spec             | componentOf                  | [string]        | A list of components the service is a part of                                                                                                                                                                                                         |
| spec             | dependsOn                    | [string]        | A list of components the service depends on.                                                                                                                                                                                                          |
| spec             | languages                    | [string]        | The service's programming language.                                                                                                                                                                                                                   |
| spec             | lifecycle                    | string          | The lifecycle state of the component.                                                                                                                                                                                                                 |
| spec             | tier                         | string          | The importance of the component.                                                                                                                                                                                                                      |
| spec             | type                         | string          | The type of service.                                                                                                                                                                                                                                  |
| schema           | Option 2                     | object          | Schema for datastore entities.                                                                                                                                                                                                                        |
| Option 2         | apiVersion [*required*] | enum            | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 2         | datadog                      | object          | Datadog product integrations for the datastore entity.                                                                                                                                                                                                |
| datadog          | events                       | [object]        | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]        | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object          | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]        | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| Option 2         | extensions                   | object          | Custom extensions. This is the free-formed field to send client side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 2         | integrations                 | object          | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object          | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string          | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string          | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object          | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string          | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 2         | kind [*required*]       | enum            | The definition of Entity V3 Datastore Kind object. Allowed enum values: `datastore`                                                                                                                                                                   |
| Option 2         | metadata [*required*]   | object          | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]        | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string          | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string          | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]        | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string          | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string          | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string          | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string          | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string          | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string          | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string          | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]        | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string          | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string          | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string          | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string          | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object          | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string          | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string          | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string          | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]        | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 2         | spec                         | object          | The definition of Entity V3 Datastore Spec object.                                                                                                                                                                                                    |
| spec             | componentOf                  | [string]        | A list of components the datastore is a part of                                                                                                                                                                                                       |
| spec             | lifecycle                    | string          | The lifecycle state of the datastore.                                                                                                                                                                                                                 |
| spec             | tier                         | string          | The importance of the datastore.                                                                                                                                                                                                                      |
| spec             | type                         | string          | The type of datastore.                                                                                                                                                                                                                                |
| schema           | Option 3                     | object          | Schema for queue entities.                                                                                                                                                                                                                            |
| Option 3         | apiVersion [*required*] | enum            | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 3         | datadog                      | object          | Datadog product integrations for the datastore entity.                                                                                                                                                                                                |
| datadog          | events                       | [object]        | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]        | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object          | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]        | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| Option 3         | extensions                   | object          | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 3         | integrations                 | object          | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object          | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string          | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string          | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object          | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string          | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 3         | kind [*required*]       | enum            | The definition of Entity V3 Queue Kind object. Allowed enum values: `queue`                                                                                                                                                                           |
| Option 3         | metadata [*required*]   | object          | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]        | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string          | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string          | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]        | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string          | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string          | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string          | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string          | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string          | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string          | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string          | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]        | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string          | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string          | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string          | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string          | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object          | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string          | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string          | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string          | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]        | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 3         | spec                         | object          | The definition of Entity V3 Queue Spec object.                                                                                                                                                                                                        |
| spec             | componentOf                  | [string]        | A list of components the queue is a part of                                                                                                                                                                                                           |
| spec             | lifecycle                    | string          | The lifecycle state of the queue.                                                                                                                                                                                                                     |
| spec             | tier                         | string          | The importance of the queue.                                                                                                                                                                                                                          |
| spec             | type                         | string          | The type of queue.                                                                                                                                                                                                                                    |
| schema           | Option 4                     | object          | Schema for system entities.                                                                                                                                                                                                                           |
| Option 4         | apiVersion [*required*] | enum            | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 4         | datadog                      | object          | Datadog product integrations for the service entity.                                                                                                                                                                                                  |
| datadog          | events                       | [object]        | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]        | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object          | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]        | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| datadog          | pipelines                    | object          | CI Pipelines association.                                                                                                                                                                                                                             |
| pipelines        | fingerprints                 | [string]        | A list of CI Fingerprints that associate CI Pipelines with the entity.                                                                                                                                                                                |
| Option 4         | extensions                   | object          | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 4         | integrations                 | object          | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object          | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string          | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string          | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object          | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string          | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 4         | kind [*required*]       | enum            | The definition of Entity V3 System Kind object. Allowed enum values: `system`                                                                                                                                                                         |
| Option 4         | metadata [*required*]   | object          | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]        | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string          | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string          | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]        | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string          | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string          | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string          | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string          | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string          | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string          | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string          | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]        | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string          | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string          | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string          | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string          | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object          | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string          | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string          | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string          | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]        | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 4         | spec                         | object          | The definition of Entity V3 System Spec object.                                                                                                                                                                                                       |
| spec             | components                   | [string]        | A list of components belongs to the system.                                                                                                                                                                                                           |
| spec             | lifecycle                    | string          | The lifecycle state of the component.                                                                                                                                                                                                                 |
| spec             | tier                         | string          | An entity reference to the owner of the component.                                                                                                                                                                                                    |
| schema           | Option 5                     | object          | Schema for API entities.                                                                                                                                                                                                                              |
| Option 5         | apiVersion [*required*] | enum            | The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2` |
| Option 5         | datadog                      | object          | Datadog product integrations for the API entity.                                                                                                                                                                                                      |
| datadog          | codeLocations                | [object]        | Schema for mapping source code locations to an entity.                                                                                                                                                                                                |
| codeLocations    | paths                        | [string]        | The paths (glob) to the source code of the service.                                                                                                                                                                                                   |
| codeLocations    | repositoryURL                | string          | The repository path of the source code of the entity.                                                                                                                                                                                                 |
| datadog          | events                       | [object]        | Events associations.                                                                                                                                                                                                                                  |
| events           | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| events           | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | logs                         | [object]        | Logs association.                                                                                                                                                                                                                                     |
| logs             | name                         | string          | The name of the query.                                                                                                                                                                                                                                |
| logs             | query                        | string          | The query to run.                                                                                                                                                                                                                                     |
| datadog          | performanceData              | object          | Performance stats association.                                                                                                                                                                                                                        |
| performanceData  | tags                         | [string]        | A list of APM entity tags that associates the APM Stats data with the entity.                                                                                                                                                                         |
| datadog          | pipelines                    | object          | CI Pipelines association.                                                                                                                                                                                                                             |
| pipelines        | fingerprints                 | [string]        | A list of CI Fingerprints that associate CI Pipelines with the entity.                                                                                                                                                                                |
| Option 5         | extensions                   | object          | Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.                                                                                                                        |
| Option 5         | integrations                 | object          | A base schema for defining third-party integrations.                                                                                                                                                                                                  |
| integrations     | opsgenie                     | object          | An Opsgenie integration schema.                                                                                                                                                                                                                       |
| opsgenie         | region                       | string          | The region for the Opsgenie integration.                                                                                                                                                                                                              |
| opsgenie         | serviceURL [*required*] | string          | The service URL for the Opsgenie integration.                                                                                                                                                                                                         |
| integrations     | pagerduty                    | object          | A PagerDuty integration schema.                                                                                                                                                                                                                       |
| pagerduty        | serviceURL [*required*] | string          | The service URL for the PagerDuty integration.                                                                                                                                                                                                        |
| Option 5         | kind [*required*]       | enum            | The definition of Entity V3 API Kind object. Allowed enum values: `api`                                                                                                                                                                               |
| Option 5         | metadata [*required*]   | object          | The definition of Entity V3 Metadata object.                                                                                                                                                                                                          |
| metadata         | additionalOwners             | [object]        | The additional owners of the entity, usually a team.                                                                                                                                                                                                  |
| additionalOwners | name [*required*]       | string          | Team name.                                                                                                                                                                                                                                            |
| additionalOwners | type                         | string          | Team type.                                                                                                                                                                                                                                            |
| metadata         | contacts                     | [object]        | A list of contacts for the entity.                                                                                                                                                                                                                    |
| contacts         | contact [*required*]    | string          | Contact value.                                                                                                                                                                                                                                        |
| contacts         | name                         | string          | Contact name.                                                                                                                                                                                                                                         |
| contacts         | type [*required*]       | string          | Contact type.                                                                                                                                                                                                                                         |
| metadata         | description                  | string          | Short description of the entity. The UI can leverage the description for display.                                                                                                                                                                     |
| metadata         | displayName                  | string          | User friendly name of the entity. The UI can leverage the display name for display.                                                                                                                                                                   |
| metadata         | id                           | string          | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.                                                                                                                                         |
| metadata         | inheritFrom                  | string          | The entity reference from which to inherit metadata                                                                                                                                                                                                   |
| metadata         | links                        | [object]        | A list of links for the entity.                                                                                                                                                                                                                       |
| links            | name [*required*]       | string          | Link name.                                                                                                                                                                                                                                            |
| links            | provider                     | string          | Link provider.                                                                                                                                                                                                                                        |
| links            | type [*required*]       | string          | Link type.                                                                                                                                                                                                                                            |
| links            | url [*required*]        | string          | Link URL.                                                                                                                                                                                                                                             |
| metadata         | managed                      | object          | A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.                                                                                                                                                 |
| metadata         | name [*required*]       | string          | Unique name given to an entity under the kind/namespace.                                                                                                                                                                                              |
| metadata         | namespace                    | string          | Namespace is a part of unique identifier. It has a default value of 'default'.                                                                                                                                                                        |
| metadata         | owner                        | string          | The owner of the entity, usually a team.                                                                                                                                                                                                              |
| metadata         | tags                         | [string]        | A set of custom tags.                                                                                                                                                                                                                                 |
| Option 5         | spec                         | object          | The definition of Entity V3 API Spec object.                                                                                                                                                                                                          |
| spec             | implementedBy                | [string]        | Services which implemented the API.                                                                                                                                                                                                                   |
| spec             | interface                    |  <oneOf>   | The API definition.                                                                                                                                                                                                                                   |
| spec             | lifecycle                    | string          | The lifecycle state of the component.                                                                                                                                                                                                                 |
| spec             | tier                         | string          | The importance of the component.                                                                                                                                                                                                                      |
| spec             | type                         | string          | The type of API.                                                                                                                                                                                                                                      |
| Option 1         | id                           | string          | Entity ID.                                                                                                                                                                                                                                            |
| Option 1         | type                         | enum            | Schema type. Allowed enum values: `schema`                                                                                                                                                                                                            |
|                  | meta                         | object          | Entity metadata.                                                                                                                                                                                                                                      |
| meta             | count                        | int64           | Total entities count.                                                                                                                                                                                                                                 |
| meta             | includeCount                 | int64           | Total included data count.                                                                                                                                                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "apiVersion": "string",
        "description": "string",
        "displayName": "string",
        "kind": "string",
        "name": "string",
        "namespace": "string",
        "owner": "string",
        "tags": []
      },
      "id": "string",
      "meta": {
        "createdAt": "string",
        "ingestionSource": "string",
        "modifiedAt": "string",
        "origin": "string"
      },
      "relationships": {
        "incidents": {
          "data": [
            {
              "id": "string",
              "type": "string"
            }
          ]
        },
        "oncall": {
          "data": [
            {
              "id": "string",
              "type": "string"
            }
          ]
        },
        "rawSchema": {
          "data": {
            "id": "string",
            "type": "string"
          }
        },
        "relatedEntities": {
          "data": [
            {
              "id": "string",
              "type": "string"
            }
          ]
        },
        "schema": {
          "data": {
            "id": "string",
            "type": "string"
          }
        }
      },
      "type": "string"
    }
  ],
  "included": [
    {
      "attributes": {
        "schema": {
          "apiVersion": "v3",
          "datadog": {
            "codeLocations": [
              {
                "paths": [],
                "repositoryURL": "string"
              }
            ],
            "events": [
              {
                "name": "string",
                "query": "string"
              }
            ],
            "logs": [
              {
                "name": "string",
                "query": "string"
              }
            ],
            "performanceData": {
              "tags": []
            },
            "pipelines": {
              "fingerprints": []
            }
          },
          "extensions": {},
          "integrations": {
            "opsgenie": {
              "region": "string",
              "serviceURL": "https://www.opsgenie.com/service/shopping-cart"
            },
            "pagerduty": {
              "serviceURL": "https://www.pagerduty.com/service-directory/Pshopping-cart"
            }
          },
          "kind": "service",
          "metadata": {
            "additionalOwners": [
              {
                "name": "",
                "type": "string"
              }
            ],
            "contacts": [
              {
                "contact": "https://slack/",
                "name": "string",
                "type": "slack"
              }
            ],
            "description": "string",
            "displayName": "string",
            "id": "4b163705-23c0-4573-b2fb-f6cea2163fcb",
            "inheritFrom": "application:default/myapp",
            "links": [
              {
                "name": "mylink",
                "provider": "string",
                "type": "link",
                "url": "https://mylink"
              }
            ],
            "managed": {},
            "name": "myService",
            "namespace": "default",
            "owner": "string",
            "tags": [
              "this:tag",
              "that:tag"
            ]
          },
          "spec": {
            "componentOf": [],
            "dependsOn": [],
            "languages": [],
            "lifecycle": "string",
            "tier": "string",
            "type": "string"
          }
        }
      },
      "id": "string",
      "type": "string"
    }
  ],
  "meta": {
    "count": "integer",
    "includeCount": "integer"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/entity" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "apiVersion": "v3",
  "datadog": {
    "codeLocations": [
      {
        "paths": []
      }
    ],
    "events": [
      {}
    ],
    "logs": [
      {}
    ],
    "performanceData": {
      "tags": []
    },
    "pipelines": {
      "fingerprints": []
    }
  },
  "integrations": {
    "opsgenie": {
      "serviceURL": "https://www.opsgenie.com/service/shopping-cart"
    },
    "pagerduty": {
      "serviceURL": "https://www.pagerduty.com/service-directory/Pshopping-cart"
    }
  },
  "kind": "service",
  "metadata": {
    "additionalOwners": [],
    "contacts": [
      {
        "contact": "https://slack/",
        "type": "slack"
      }
    ],
    "id": "4b163705-23c0-4573-b2fb-f6cea2163fcb",
    "inheritFrom": "application:default/myapp",
    "links": [
      {
        "name": "mylink",
        "type": "link",
        "url": "https://mylink"
      }
    ],
    "name": "service-examplesoftwarecatalog",
    "tags": [
      "this:tag",
      "that:tag"
    ]
  },
  "spec": {
    "dependsOn": [],
    "languages": []
  }
}
EOF
                        
##### 

```go
// Create or update software catalog entity using schema v3 returns "ACCEPTED" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.UpsertCatalogEntityRequest{
		EntityV3: &datadogV2.EntityV3{
			EntityV3Service: &datadogV2.EntityV3Service{
				ApiVersion: datadogV2.ENTITYV3APIVERSION_V3,
				Datadog: &datadogV2.EntityV3ServiceDatadog{
					CodeLocations: []datadogV2.EntityV3DatadogCodeLocationItem{
						{
							Paths: []string{},
						},
					},
					Events: []datadogV2.EntityV3DatadogEventItem{
						{},
					},
					Logs: []datadogV2.EntityV3DatadogLogItem{
						{},
					},
					PerformanceData: &datadogV2.EntityV3DatadogPerformance{
						Tags: []string{},
					},
					Pipelines: &datadogV2.EntityV3DatadogPipelines{
						Fingerprints: []string{},
					},
				},
				Integrations: &datadogV2.EntityV3Integrations{
					Opsgenie: &datadogV2.EntityV3DatadogIntegrationOpsgenie{
						ServiceUrl: "https://www.opsgenie.com/service/shopping-cart",
					},
					Pagerduty: &datadogV2.EntityV3DatadogIntegrationPagerduty{
						ServiceUrl: "https://www.pagerduty.com/service-directory/Pshopping-cart",
					},
				},
				Kind: datadogV2.ENTITYV3SERVICEKIND_SERVICE,
				Metadata: datadogV2.EntityV3Metadata{
					AdditionalOwners: []datadogV2.EntityV3MetadataAdditionalOwnersItems{},
					Contacts: []datadogV2.EntityV3MetadataContactsItems{
						{
							Contact: "https://slack/",
							Type:    "slack",
						},
					},
					Id:          datadog.PtrString("4b163705-23c0-4573-b2fb-f6cea2163fcb"),
					InheritFrom: datadog.PtrString("application:default/myapp"),
					Links: []datadogV2.EntityV3MetadataLinksItems{
						{
							Name: "mylink",
							Type: "link",
							Url:  "https://mylink",
						},
					},
					Name: "service-examplesoftwarecatalog",
					Tags: []string{
						"this:tag",
						"that:tag",
					},
				},
				Spec: &datadogV2.EntityV3ServiceSpec{
					DependsOn: []string{},
					Languages: []string{},
				},
			}}}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSoftwareCatalogApi(apiClient)
	resp, r, err := api.UpsertCatalogEntity(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareCatalogApi.UpsertCatalogEntity`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SoftwareCatalogApi.UpsertCatalogEntity`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create or update software catalog entity using schema v3 returns "ACCEPTED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SoftwareCatalogApi;
import com.datadog.api.client.v2.model.EntityV3;
import com.datadog.api.client.v2.model.EntityV3APIVersion;
import com.datadog.api.client.v2.model.EntityV3DatadogCodeLocationItem;
import com.datadog.api.client.v2.model.EntityV3DatadogEventItem;
import com.datadog.api.client.v2.model.EntityV3DatadogIntegrationOpsgenie;
import com.datadog.api.client.v2.model.EntityV3DatadogIntegrationPagerduty;
import com.datadog.api.client.v2.model.EntityV3DatadogLogItem;
import com.datadog.api.client.v2.model.EntityV3DatadogPerformance;
import com.datadog.api.client.v2.model.EntityV3DatadogPipelines;
import com.datadog.api.client.v2.model.EntityV3Integrations;
import com.datadog.api.client.v2.model.EntityV3Metadata;
import com.datadog.api.client.v2.model.EntityV3MetadataContactsItems;
import com.datadog.api.client.v2.model.EntityV3MetadataLinksItems;
import com.datadog.api.client.v2.model.EntityV3Service;
import com.datadog.api.client.v2.model.EntityV3ServiceDatadog;
import com.datadog.api.client.v2.model.EntityV3ServiceKind;
import com.datadog.api.client.v2.model.EntityV3ServiceSpec;
import com.datadog.api.client.v2.model.UpsertCatalogEntityRequest;
import com.datadog.api.client.v2.model.UpsertCatalogEntityResponse;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SoftwareCatalogApi apiInstance = new SoftwareCatalogApi(defaultClient);

    UpsertCatalogEntityRequest body =
        new UpsertCatalogEntityRequest(
            new EntityV3(
                new EntityV3Service()
                    .apiVersion(EntityV3APIVersion.V3)
                    .datadog(
                        new EntityV3ServiceDatadog()
                            .codeLocations(
                                Collections.singletonList(new EntityV3DatadogCodeLocationItem()))
                            .events(Collections.singletonList(new EntityV3DatadogEventItem()))
                            .logs(Collections.singletonList(new EntityV3DatadogLogItem()))
                            .performanceData(new EntityV3DatadogPerformance())
                            .pipelines(new EntityV3DatadogPipelines()))
                    .integrations(
                        new EntityV3Integrations()
                            .opsgenie(
                                new EntityV3DatadogIntegrationOpsgenie()
                                    .serviceUrl("https://www.opsgenie.com/service/shopping-cart"))
                            .pagerduty(
                                new EntityV3DatadogIntegrationPagerduty()
                                    .serviceUrl(
                                        "https://www.pagerduty.com/service-directory/Pshopping-cart")))
                    .kind(EntityV3ServiceKind.SERVICE)
                    .metadata(
                        new EntityV3Metadata()
                            .contacts(
                                Collections.singletonList(
                                    new EntityV3MetadataContactsItems()
                                        .contact("https://slack/")
                                        .type("slack")))
                            .id("4b163705-23c0-4573-b2fb-f6cea2163fcb")
                            .inheritFrom("application:default/myapp")
                            .links(
                                Collections.singletonList(
                                    new EntityV3MetadataLinksItems()
                                        .name("mylink")
                                        .type("link")
                                        .url("https://mylink")))
                            .name("service-examplesoftwarecatalog")
                            .tags(Arrays.asList("this:tag", "that:tag")))
                    .spec(new EntityV3ServiceSpec())));

    try {
      UpsertCatalogEntityResponse result = apiInstance.upsertCatalogEntity(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareCatalogApi#upsertCatalogEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
"""
Create or update software catalog entity using schema v3 returns "ACCEPTED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi
from datadog_api_client.v2.model.entity_v3_api_version import EntityV3APIVersion
from datadog_api_client.v2.model.entity_v3_datadog_code_location_item import EntityV3DatadogCodeLocationItem
from datadog_api_client.v2.model.entity_v3_datadog_event_item import EntityV3DatadogEventItem
from datadog_api_client.v2.model.entity_v3_datadog_integration_opsgenie import EntityV3DatadogIntegrationOpsgenie
from datadog_api_client.v2.model.entity_v3_datadog_integration_pagerduty import EntityV3DatadogIntegrationPagerduty
from datadog_api_client.v2.model.entity_v3_datadog_log_item import EntityV3DatadogLogItem
from datadog_api_client.v2.model.entity_v3_datadog_performance import EntityV3DatadogPerformance
from datadog_api_client.v2.model.entity_v3_datadog_pipelines import EntityV3DatadogPipelines
from datadog_api_client.v2.model.entity_v3_integrations import EntityV3Integrations
from datadog_api_client.v2.model.entity_v3_metadata import EntityV3Metadata
from datadog_api_client.v2.model.entity_v3_metadata_contacts_items import EntityV3MetadataContactsItems
from datadog_api_client.v2.model.entity_v3_metadata_links_items import EntityV3MetadataLinksItems
from datadog_api_client.v2.model.entity_v3_service import EntityV3Service
from datadog_api_client.v2.model.entity_v3_service_datadog import EntityV3ServiceDatadog
from datadog_api_client.v2.model.entity_v3_service_kind import EntityV3ServiceKind
from datadog_api_client.v2.model.entity_v3_service_spec import EntityV3ServiceSpec

body = EntityV3Service(
    api_version=EntityV3APIVersion.V3,
    datadog=EntityV3ServiceDatadog(
        code_locations=[
            EntityV3DatadogCodeLocationItem(
                paths=[],
            ),
        ],
        events=[
            EntityV3DatadogEventItem(),
        ],
        logs=[
            EntityV3DatadogLogItem(),
        ],
        performance_data=EntityV3DatadogPerformance(
            tags=[],
        ),
        pipelines=EntityV3DatadogPipelines(
            fingerprints=[],
        ),
    ),
    integrations=EntityV3Integrations(
        opsgenie=EntityV3DatadogIntegrationOpsgenie(
            service_url="https://www.opsgenie.com/service/shopping-cart",
        ),
        pagerduty=EntityV3DatadogIntegrationPagerduty(
            service_url="https://www.pagerduty.com/service-directory/Pshopping-cart",
        ),
    ),
    kind=EntityV3ServiceKind.SERVICE,
    metadata=EntityV3Metadata(
        additional_owners=[],
        contacts=[
            EntityV3MetadataContactsItems(
                contact="https://slack/",
                type="slack",
            ),
        ],
        id="4b163705-23c0-4573-b2fb-f6cea2163fcb",
        inherit_from="application:default/myapp",
        links=[
            EntityV3MetadataLinksItems(
                name="mylink",
                type="link",
                url="https://mylink",
            ),
        ],
        name="service-examplesoftwarecatalog",
        tags=[
            "this:tag",
            "that:tag",
        ],
    ),
    spec=EntityV3ServiceSpec(
        depends_on=[],
        languages=[],
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    response = api_instance.upsert_catalog_entity(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create or update software catalog entity using schema v3 returns "ACCEPTED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new

body = DatadogAPIClient::V2::EntityV3Service.new({
  api_version: DatadogAPIClient::V2::EntityV3APIVersion::V3,
  datadog: DatadogAPIClient::V2::EntityV3ServiceDatadog.new({
    code_locations: [
      DatadogAPIClient::V2::EntityV3DatadogCodeLocationItem.new({
        paths: [],
      }),
    ],
    events: [
      DatadogAPIClient::V2::EntityV3DatadogEventItem.new({}),
    ],
    logs: [
      DatadogAPIClient::V2::EntityV3DatadogLogItem.new({}),
    ],
    performance_data: DatadogAPIClient::V2::EntityV3DatadogPerformance.new({
      tags: [],
    }),
    pipelines: DatadogAPIClient::V2::EntityV3DatadogPipelines.new({
      fingerprints: [],
    }),
  }),
  integrations: DatadogAPIClient::V2::EntityV3Integrations.new({
    opsgenie: DatadogAPIClient::V2::EntityV3DatadogIntegrationOpsgenie.new({
      service_url: "https://www.opsgenie.com/service/shopping-cart",
    }),
    pagerduty: DatadogAPIClient::V2::EntityV3DatadogIntegrationPagerduty.new({
      service_url: "https://www.pagerduty.com/service-directory/Pshopping-cart",
    }),
  }),
  kind: DatadogAPIClient::V2::EntityV3ServiceKind::SERVICE,
  metadata: DatadogAPIClient::V2::EntityV3Metadata.new({
    additional_owners: [],
    contacts: [
      DatadogAPIClient::V2::EntityV3MetadataContactsItems.new({
        contact: "https://slack/",
        type: "slack",
      }),
    ],
    id: "4b163705-23c0-4573-b2fb-f6cea2163fcb",
    inherit_from: "application:default/myapp",
    links: [
      DatadogAPIClient::V2::EntityV3MetadataLinksItems.new({
        name: "mylink",
        type: "link",
        url: "https://mylink",
      }),
    ],
    name: "service-examplesoftwarecatalog",
    tags: [
      "this:tag",
      "that:tag",
    ],
  }),
  spec: DatadogAPIClient::V2::EntityV3ServiceSpec.new({
    depends_on: [],
    languages: [],
  }),
})
p api_instance.upsert_catalog_entity(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Create or update software catalog entity using schema v3 returns "ACCEPTED"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_software_catalog::SoftwareCatalogAPI;
use datadog_api_client::datadogV2::model::EntityV3;
use datadog_api_client::datadogV2::model::EntityV3APIVersion;
use datadog_api_client::datadogV2::model::EntityV3DatadogCodeLocationItem;
use datadog_api_client::datadogV2::model::EntityV3DatadogEventItem;
use datadog_api_client::datadogV2::model::EntityV3DatadogIntegrationOpsgenie;
use datadog_api_client::datadogV2::model::EntityV3DatadogIntegrationPagerduty;
use datadog_api_client::datadogV2::model::EntityV3DatadogLogItem;
use datadog_api_client::datadogV2::model::EntityV3DatadogPerformance;
use datadog_api_client::datadogV2::model::EntityV3DatadogPipelines;
use datadog_api_client::datadogV2::model::EntityV3Integrations;
use datadog_api_client::datadogV2::model::EntityV3Metadata;
use datadog_api_client::datadogV2::model::EntityV3MetadataContactsItems;
use datadog_api_client::datadogV2::model::EntityV3MetadataLinksItems;
use datadog_api_client::datadogV2::model::EntityV3Service;
use datadog_api_client::datadogV2::model::EntityV3ServiceDatadog;
use datadog_api_client::datadogV2::model::EntityV3ServiceKind;
use datadog_api_client::datadogV2::model::EntityV3ServiceSpec;
use datadog_api_client::datadogV2::model::UpsertCatalogEntityRequest;

#[tokio::main]
async fn main() {
    let body = UpsertCatalogEntityRequest::EntityV3(Box::new(EntityV3::EntityV3Service(Box::new(
        EntityV3Service::new(
            EntityV3APIVersion::V3,
            EntityV3ServiceKind::SERVICE,
            EntityV3Metadata::new("service-examplesoftwarecatalog".to_string())
                .additional_owners(vec![])
                .contacts(vec![EntityV3MetadataContactsItems::new(
                    "https://slack/".to_string(),
                    "slack".to_string(),
                )])
                .id("4b163705-23c0-4573-b2fb-f6cea2163fcb".to_string())
                .inherit_from("application:default/myapp".to_string())
                .links(vec![EntityV3MetadataLinksItems::new(
                    "mylink".to_string(),
                    "link".to_string(),
                    "https://mylink".to_string(),
                )])
                .tags(vec!["this:tag".to_string(), "that:tag".to_string()]),
        )
        .datadog(
            EntityV3ServiceDatadog::new()
                .code_locations(vec![EntityV3DatadogCodeLocationItem::new().paths(vec![])])
                .events(vec![EntityV3DatadogEventItem::new()])
                .logs(vec![EntityV3DatadogLogItem::new()])
                .performance_data(EntityV3DatadogPerformance::new().tags(vec![]))
                .pipelines(EntityV3DatadogPipelines::new().fingerprints(vec![])),
        )
        .integrations(
            EntityV3Integrations::new()
                .opsgenie(EntityV3DatadogIntegrationOpsgenie::new(
                    "https://www.opsgenie.com/service/shopping-cart".to_string(),
                ))
                .pagerduty(EntityV3DatadogIntegrationPagerduty::new(
                    "https://www.pagerduty.com/service-directory/Pshopping-cart".to_string(),
                )),
        )
        .spec(
            EntityV3ServiceSpec::new()
                .depends_on(vec![])
                .languages(vec![]),
        ),
    ))));
    let configuration = datadog::Configuration::new();
    let api = SoftwareCatalogAPI::with_config(configuration);
    let resp = api.upsert_catalog_entity(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Create or update software catalog entity using schema v3 returns "ACCEPTED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SoftwareCatalogApi(configuration);

const params: v2.SoftwareCatalogApiUpsertCatalogEntityRequest = {
  body: {
    apiVersion: "v3",
    datadog: {
      codeLocations: [
        {
          paths: [],
        },
      ],
      events: [{}],
      logs: [{}],
      performanceData: {
        tags: [],
      },
      pipelines: {
        fingerprints: [],
      },
    },
    integrations: {
      opsgenie: {
        serviceUrl: "https://www.opsgenie.com/service/shopping-cart",
      },
      pagerduty: {
        serviceUrl:
          "https://www.pagerduty.com/service-directory/Pshopping-cart",
      },
    },
    kind: "service",
    metadata: {
      additionalOwners: [],
      contacts: [
        {
          contact: "https://slack/",
          type: "slack",
        },
      ],
      id: "4b163705-23c0-4573-b2fb-f6cea2163fcb",
      inheritFrom: "application:default/myapp",
      links: [
        {
          name: "mylink",
          type: "link",
          url: "https://mylink",
        },
      ],
      name: "service-examplesoftwarecatalog",
      tags: ["this:tag", "that:tag"],
    },
    spec: {
      dependsOn: [],
      languages: [],
    },
  },
};

apiInstance
  .upsertCatalogEntity(params)
  .then((data: v2.UpsertCatalogEntityResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete a single entity{% #delete-a-single-entity %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/catalog/entity/{entity_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/catalog/entity/{entity_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/catalog/entity/{entity_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/catalog/entity/{entity_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/catalog/entity/{entity_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/catalog/entity/{entity_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/catalog/entity/{entity_id} |

### Overview

Delete a single entity in Software Catalog.

OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.



### Arguments

#### Path Parameters

| Name                        | Type   | Description         |
| --------------------------- | ------ | ------------------- |
| entity_id [*required*] | string | UUID or Entity Ref. |

### Response

{% tab title="204" %}
OK
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Path parametersexport entity_id="service:myservice"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/entity/${entity_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a single entity returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    api_instance.delete_catalog_entity(
        entity_id="service:myservice",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete a single entity returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
api_instance.delete_catalog_entity("service:myservice")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete a single entity returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSoftwareCatalogApi(apiClient)
	r, err := api.DeleteCatalogEntity(ctx, "service:myservice")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareCatalogApi.DeleteCatalogEntity`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete a single entity returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SoftwareCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SoftwareCatalogApi apiInstance = new SoftwareCatalogApi(defaultClient);

    try {
      apiInstance.deleteCatalogEntity("service:myservice");
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareCatalogApi#deleteCatalogEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
// Delete a single entity returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_software_catalog::SoftwareCatalogAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SoftwareCatalogAPI::with_config(configuration);
    let resp = api
        .delete_catalog_entity("service:myservice".to_string())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Delete a single entity returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SoftwareCatalogApi(configuration);

const params: v2.SoftwareCatalogApiDeleteCatalogEntityRequest = {
  entityId: "service:myservice",
};

apiInstance
  .deleteCatalogEntity(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a list of entity relations{% #get-a-list-of-entity-relations %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/catalog/relation |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/catalog/relation |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/catalog/relation      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/catalog/relation      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/catalog/relation     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/catalog/relation |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/catalog/relation |

### Overview

Get a list of entity relations from Software Catalog.

OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.



### Arguments

#### Query Strings

| Name              | Type    | Description                                                                                                                                                                                                                                                                          |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| page[offset]      | integer | Specific offset to use as the beginning of the returned page.                                                                                                                                                                                                                        |
| page[limit]       | integer | Maximum number of relations in the response.                                                                                                                                                                                                                                         |
| filter[type]      | enum    | Filter relations by type.Allowed enum values: `RelationTypeOwns, RelationTypeOwnedBy, RelationTypeDependsOn, RelationTypeDependencyOf, RelationTypePartsOf, RelationTypeHasPart, RelationTypeOtherOwns, RelationTypeOtherOwnedBy, RelationTypeImplementedBy, RelationTypeImplements` |
| filter[from_ref]  | string  | Filter relations by the reference of the first entity in the relation.                                                                                                                                                                                                               |
| filter[to_ref]    | string  | Filter relations by the reference of the second entity in the relation.                                                                                                                                                                                                              |
| include           | enum    | Include relationship data.Allowed enum values: `entity, schema`                                                                                                                                                                                                                      |
| includeDiscovered | boolean | If true, includes relationships discovered by APM and USM.                                                                                                                                                                                                                           |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List entity relation response.

| Parent field    | Field           | Type      | Description                                                                                                                                                                                                                                                                  |
| --------------- | --------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                 | data            | [object]  | Array of relation responses                                                                                                                                                                                                                                                  |
| data            | attributes      | object    | Relation attributes.                                                                                                                                                                                                                                                         |
| attributes      | from            | object    | Relation entity reference.                                                                                                                                                                                                                                                   |
| from            | kind            | string    | Entity kind.                                                                                                                                                                                                                                                                 |
| from            | name            | string    | Entity name.                                                                                                                                                                                                                                                                 |
| from            | namespace       | string    | Entity namespace.                                                                                                                                                                                                                                                            |
| attributes      | to              | object    | Relation entity reference.                                                                                                                                                                                                                                                   |
| to              | kind            | string    | Entity kind.                                                                                                                                                                                                                                                                 |
| to              | name            | string    | Entity name.                                                                                                                                                                                                                                                                 |
| to              | namespace       | string    | Entity namespace.                                                                                                                                                                                                                                                            |
| attributes      | type            | enum      | Supported relation types. Allowed enum values: `RelationTypeOwns,RelationTypeOwnedBy,RelationTypeDependsOn,RelationTypeDependencyOf,RelationTypePartsOf,RelationTypeHasPart,RelationTypeOtherOwns,RelationTypeOtherOwnedBy,RelationTypeImplementedBy,RelationTypeImplements` |
| data            | id              | string    | Relation ID.                                                                                                                                                                                                                                                                 |
| data            | meta            | object    | Relation metadata.                                                                                                                                                                                                                                                           |
| meta            | createdAt       | date-time | Relation creation time.                                                                                                                                                                                                                                                      |
| meta            | definedBy       | string    | Relation defined by.                                                                                                                                                                                                                                                         |
| meta            | modifiedAt      | date-time | Relation modification time.                                                                                                                                                                                                                                                  |
| meta            | source          | string    | Relation source.                                                                                                                                                                                                                                                             |
| data            | relationships   | object    | Relation relationships.                                                                                                                                                                                                                                                      |
| relationships   | fromEntity      | object    | Relation to entity.                                                                                                                                                                                                                                                          |
| fromEntity      | data            | object    | Relationship entry.                                                                                                                                                                                                                                                          |
| data            | id              | string    | Associated data ID.                                                                                                                                                                                                                                                          |
| data            | type            | string    | Relationship type.                                                                                                                                                                                                                                                           |
| fromEntity      | meta            | object    | Entity metadata.                                                                                                                                                                                                                                                             |
| meta            | createdAt       | string    | The creation time.                                                                                                                                                                                                                                                           |
| meta            | ingestionSource | string    | The ingestion source.                                                                                                                                                                                                                                                        |
| meta            | modifiedAt      | string    | The modification time.                                                                                                                                                                                                                                                       |
| meta            | origin          | string    | The origin.                                                                                                                                                                                                                                                                  |
| relationships   | toEntity        | object    | Relation to entity.                                                                                                                                                                                                                                                          |
| toEntity        | data            | object    | Relationship entry.                                                                                                                                                                                                                                                          |
| data            | id              | string    | Associated data ID.                                                                                                                                                                                                                                                          |
| data            | type            | string    | Relationship type.                                                                                                                                                                                                                                                           |
| toEntity        | meta            | object    | Entity metadata.                                                                                                                                                                                                                                                             |
| meta            | createdAt       | string    | The creation time.                                                                                                                                                                                                                                                           |
| meta            | ingestionSource | string    | The ingestion source.                                                                                                                                                                                                                                                        |
| meta            | modifiedAt      | string    | The modification time.                                                                                                                                                                                                                                                       |
| meta            | origin          | string    | The origin.                                                                                                                                                                                                                                                                  |
| data            | subtype         | string    | Relation subtype.                                                                                                                                                                                                                                                            |
| data            | type            | enum      | Relation type. Allowed enum values: `relation`                                                                                                                                                                                                                               |
|                 | included        | [object]  | List relation response included entities.                                                                                                                                                                                                                                    |
| included        | attributes      | object    | Entity attributes.                                                                                                                                                                                                                                                           |
| attributes      | apiVersion      | string    | The API version.                                                                                                                                                                                                                                                             |
| attributes      | description     | string    | The description.                                                                                                                                                                                                                                                             |
| attributes      | displayName     | string    | The display name.                                                                                                                                                                                                                                                            |
| attributes      | kind            | string    | The kind.                                                                                                                                                                                                                                                                    |
| attributes      | name            | string    | The name.                                                                                                                                                                                                                                                                    |
| attributes      | namespace       | string    | The namespace.                                                                                                                                                                                                                                                               |
| attributes      | owner           | string    | The owner.                                                                                                                                                                                                                                                                   |
| attributes      | tags            | [string]  | The tags.                                                                                                                                                                                                                                                                    |
| included        | id              | string    | Entity ID.                                                                                                                                                                                                                                                                   |
| included        | meta            | object    | Entity metadata.                                                                                                                                                                                                                                                             |
| meta            | createdAt       | string    | The creation time.                                                                                                                                                                                                                                                           |
| meta            | ingestionSource | string    | The ingestion source.                                                                                                                                                                                                                                                        |
| meta            | modifiedAt      | string    | The modification time.                                                                                                                                                                                                                                                       |
| meta            | origin          | string    | The origin.                                                                                                                                                                                                                                                                  |
| included        | relationships   | object    | Entity relationships.                                                                                                                                                                                                                                                        |
| relationships   | incidents       | object    | Entity to incidents relationship.                                                                                                                                                                                                                                            |
| incidents       | data            | [object]  | Relationships.                                                                                                                                                                                                                                                               |
| data            | id              | string    | Associated data ID.                                                                                                                                                                                                                                                          |
| data            | type            | string    | Relationship type.                                                                                                                                                                                                                                                           |
| relationships   | oncall          | object    | Entity to oncalls relationship.                                                                                                                                                                                                                                              |
| oncall          | data            | [object]  | Relationships.                                                                                                                                                                                                                                                               |
| data            | id              | string    | Associated data ID.                                                                                                                                                                                                                                                          |
| data            | type            | string    | Relationship type.                                                                                                                                                                                                                                                           |
| relationships   | rawSchema       | object    | Entity to raw schema relationship.                                                                                                                                                                                                                                           |
| rawSchema       | data            | object    | Relationship entry.                                                                                                                                                                                                                                                          |
| data            | id              | string    | Associated data ID.                                                                                                                                                                                                                                                          |
| data            | type            | string    | Relationship type.                                                                                                                                                                                                                                                           |
| relationships   | relatedEntities | object    | Entity to related entities relationship.                                                                                                                                                                                                                                     |
| relatedEntities | data            | [object]  | Relationships.                                                                                                                                                                                                                                                               |
| data            | id              | string    | Associated data ID.                                                                                                                                                                                                                                                          |
| data            | type            | string    | Relationship type.                                                                                                                                                                                                                                                           |
| relationships   | schema          | object    | Entity to detail schema relationship.                                                                                                                                                                                                                                        |
| schema          | data            | object    | Relationship entry.                                                                                                                                                                                                                                                          |
| data            | id              | string    | Associated data ID.                                                                                                                                                                                                                                                          |
| data            | type            | string    | Relationship type.                                                                                                                                                                                                                                                           |
| included        | type            | string    | Entity.                                                                                                                                                                                                                                                                      |
|                 | links           | object    | List relation response links.                                                                                                                                                                                                                                                |
| links           | next            | string    | Next link.                                                                                                                                                                                                                                                                   |
| links           | previous        | string    | Previous link.                                                                                                                                                                                                                                                               |
| links           | self            | string    | Current link.                                                                                                                                                                                                                                                                |
|                 | meta            | object    | Relation response metadata.                                                                                                                                                                                                                                                  |
| meta            | count           | int64     | Total relations count.                                                                                                                                                                                                                                                       |
| meta            | includeCount    | int64     | Total included data count.                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "from": {
          "kind": "string",
          "name": "string",
          "namespace": "string"
        },
        "to": {
          "kind": "string",
          "name": "string",
          "namespace": "string"
        },
        "type": "string"
      },
      "id": "string",
      "meta": {
        "createdAt": "2019-09-19T10:00:00.000Z",
        "definedBy": "string",
        "modifiedAt": "2019-09-19T10:00:00.000Z",
        "source": "string"
      },
      "relationships": {
        "fromEntity": {
          "data": {
            "id": "string",
            "type": "string"
          },
          "meta": {
            "createdAt": "string",
            "ingestionSource": "string",
            "modifiedAt": "string",
            "origin": "string"
          }
        },
        "toEntity": {
          "data": {
            "id": "string",
            "type": "string"
          },
          "meta": {
            "createdAt": "string",
            "ingestionSource": "string",
            "modifiedAt": "string",
            "origin": "string"
          }
        }
      },
      "subtype": "string",
      "type": "string"
    }
  ],
  "included": [
    {
      "attributes": {
        "apiVersion": "string",
        "description": "string",
        "displayName": "string",
        "kind": "string",
        "name": "string",
        "namespace": "string",
        "owner": "string",
        "tags": []
      },
      "id": "string",
      "meta": {
        "createdAt": "string",
        "ingestionSource": "string",
        "modifiedAt": "string",
        "origin": "string"
      },
      "relationships": {
        "incidents": {
          "data": [
            {
              "id": "string",
              "type": "string"
            }
          ]
        },
        "oncall": {
          "data": [
            {
              "id": "string",
              "type": "string"
            }
          ]
        },
        "rawSchema": {
          "data": {
            "id": "string",
            "type": "string"
          }
        },
        "relatedEntities": {
          "data": [
            {
              "id": "string",
              "type": "string"
            }
          ]
        },
        "schema": {
          "data": {
            "id": "string",
            "type": "string"
          }
        }
      },
      "type": "string"
    }
  ],
  "links": {
    "next": "/api/v2/catalog/relation?filter[from_ref]=service:service-catalog\u0026include=entity\u0026page[limit]=2\u0026page[offset]=2",
    "previous": "string",
    "self": "/api/v2/catalog/relation?filter[from_ref]=service:service-catalog\u0026include=entity\u0026page[limit]=2\u0026page[offset]=0"
  },
  "meta": {
    "count": "integer",
    "includeCount": "integer"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/relation" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a list of entity relations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    response = api_instance.list_catalog_relation()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a list of entity relations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
p api_instance.list_catalog_relation()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a list of entity relations returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSoftwareCatalogApi(apiClient)
	resp, r, err := api.ListCatalogRelation(ctx, *datadogV2.NewListCatalogRelationOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareCatalogApi.ListCatalogRelation`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SoftwareCatalogApi.ListCatalogRelation`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a list of entity relations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SoftwareCatalogApi;
import com.datadog.api.client.v2.model.ListRelationCatalogResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SoftwareCatalogApi apiInstance = new SoftwareCatalogApi(defaultClient);

    try {
      ListRelationCatalogResponse result = apiInstance.listCatalogRelation();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareCatalogApi#listCatalogRelation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
// Get a list of entity relations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_software_catalog::ListCatalogRelationOptionalParams;
use datadog_api_client::datadogV2::api_software_catalog::SoftwareCatalogAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SoftwareCatalogAPI::with_config(configuration);
    let resp = api
        .list_catalog_relation(ListCatalogRelationOptionalParams::default())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Get a list of entity relations returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SoftwareCatalogApi(configuration);

apiInstance
  .listCatalogRelation()
  .then((data: v2.ListRelationCatalogResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Preview catalog entities{% #preview-catalog-entities %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/catalog/entity/preview |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/catalog/entity/preview |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/catalog/entity/preview      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/catalog/entity/preview      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/catalog/entity/preview     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/catalog/entity/preview |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/catalog/entity/preview |

### Overview



OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.



### Response

{% tab title="202" %}
Accepted
{% tab title="Model" %}

| Parent field    | Field                  | Type     | Description                                                        |
| --------------- | ---------------------- | -------- | ------------------------------------------------------------------ |
|                 | data [*required*] | [object] |
| data            | attributes             | object   |
| attributes      | apiVersion             | string   |
| attributes      | description            | string   |
| attributes      | displayName            | string   |
| attributes      | kind                   | string   |
| attributes      | name                   | string   |
| attributes      | namespace              | string   |
| attributes      | owner                  | string   |
| attributes      | properties             | object   |
| attributes      | tags                   | [string] |
| data            | id                     | string   |
| data            | relationships          | object   |
| relationships   | incidents              | object   |
| incidents       | data                   | [object] |
| data            | id [*required*]   | string   |
| data            | type [*required*] | enum     | Incident resource type. Allowed enum values: `incident`            |
| relationships   | oncalls                | object   |
| oncalls         | data                   | [object] |
| data            | id [*required*]   | string   |
| data            | type [*required*] | enum     | Oncall resource type. Allowed enum values: `oncall`                |
| relationships   | rawSchema              | object   |
| rawSchema       | data [*required*] | object   |
| data            | id [*required*]   | string   |
| data            | type [*required*] | enum     | Raw schema resource type. Allowed enum values: `rawSchema`         |
| relationships   | relatedEntities        | object   |
| relatedEntities | data                   | [object] |
| data            | id [*required*]   | string   |
| data            | type [*required*] | enum     | Related entity resource type. Allowed enum values: `relatedEntity` |
| relationships   | schema                 | object   |
| schema          | data [*required*] | object   |
| data            | id [*required*]   | string   |
| data            | type [*required*] | enum     | Schema resource type. Allowed enum values: `schema`                |
| data            | type [*required*] | enum     | Entity resource type. Allowed enum values: `entity`                |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "apiVersion": "string",
        "description": "string",
        "displayName": "string",
        "kind": "string",
        "name": "string",
        "namespace": "string",
        "owner": "string",
        "properties": {},
        "tags": []
      },
      "id": "string",
      "relationships": {
        "incidents": {
          "data": [
            {
              "id": "",
              "type": "incident"
            }
          ]
        },
        "oncalls": {
          "data": [
            {
              "id": "",
              "type": "oncall"
            }
          ]
        },
        "rawSchema": {
          "data": {
            "id": "",
            "type": "rawSchema"
          }
        },
        "relatedEntities": {
          "data": [
            {
              "id": "",
              "type": "relatedEntity"
            }
          ]
        },
        "schema": {
          "data": {
            "id": "",
            "type": "schema"
          }
        }
      },
      "type": "entity"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/entity/preview" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Preview catalog entities returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    response = api_instance.preview_catalog_entities()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Preview catalog entities returns "Accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
p api_instance.preview_catalog_entities()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Preview catalog entities returns "Accepted" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSoftwareCatalogApi(apiClient)
	resp, r, err := api.PreviewCatalogEntities(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareCatalogApi.PreviewCatalogEntities`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SoftwareCatalogApi.PreviewCatalogEntities`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Preview catalog entities returns "Accepted" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SoftwareCatalogApi;
import com.datadog.api.client.v2.model.EntityResponseArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SoftwareCatalogApi apiInstance = new SoftwareCatalogApi(defaultClient);

    try {
      EntityResponseArray result = apiInstance.previewCatalogEntities();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareCatalogApi#previewCatalogEntities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
// Preview catalog entities returns "Accepted" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_software_catalog::SoftwareCatalogAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SoftwareCatalogAPI::with_config(configuration);
    let resp = api.preview_catalog_entities().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Preview catalog entities returns "Accepted" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SoftwareCatalogApi(configuration);

apiInstance
  .previewCatalogEntities()
  .then((data: v2.EntityResponseArray) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a list of entity kinds{% #get-a-list-of-entity-kinds %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/catalog/kind |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/catalog/kind |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/catalog/kind      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/catalog/kind      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/catalog/kind     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/catalog/kind |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/catalog/kind |

### Overview

Get a list of entity kinds from Software Catalog.

OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.



### Arguments

#### Query Strings

| Name         | Type    | Description                                                   |
| ------------ | ------- | ------------------------------------------------------------- |
| page[offset] | integer | Specific offset to use as the beginning of the returned page. |
| page[limit]  | integer | Maximum number of kinds in the response.                      |
| filter[id]   | string  | Filter entities by UUID.                                      |
| filter[name] | string  | Filter entities by name.                                      |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List kind response.

| Parent field | Field       | Type     | Description                                                                                                   |
| ------------ | ----------- | -------- | ------------------------------------------------------------------------------------------------------------- |
|              | data        | [object] | List of kind responses.                                                                                       |
| data         | attributes  | object   | Kind attributes.                                                                                              |
| attributes   | description | string   | Short description of the kind.                                                                                |
| attributes   | displayName | string   | User friendly name of the kind.                                                                               |
| attributes   | name        | string   | The kind name.                                                                                                |
| data         | id          | string   | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored. |
| data         | meta        | object   | Kind metadata.                                                                                                |
| meta         | createdAt   | string   | The creation time.                                                                                            |
| meta         | modifiedAt  | string   | The modification time.                                                                                        |
| data         | type        | string   | Kind.                                                                                                         |
|              | meta        | object   | Kind response metadata.                                                                                       |
| meta         | count       | int64    | Total kinds count.                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "description": "string",
        "displayName": "string",
        "name": "my-job"
      },
      "id": "4b163705-23c0-4573-b2fb-f6cea2163fcb",
      "meta": {
        "createdAt": "string",
        "modifiedAt": "string"
      },
      "type": "string"
    }
  ],
  "meta": {
    "count": "integer"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/kind" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a list of entity kinds returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    response = api_instance.list_catalog_kind()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a list of entity kinds returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
p api_instance.list_catalog_kind()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a list of entity kinds returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSoftwareCatalogApi(apiClient)
	resp, r, err := api.ListCatalogKind(ctx, *datadogV2.NewListCatalogKindOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareCatalogApi.ListCatalogKind`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SoftwareCatalogApi.ListCatalogKind`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a list of entity kinds returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SoftwareCatalogApi;
import com.datadog.api.client.v2.model.ListKindCatalogResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SoftwareCatalogApi apiInstance = new SoftwareCatalogApi(defaultClient);

    try {
      ListKindCatalogResponse result = apiInstance.listCatalogKind();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareCatalogApi#listCatalogKind");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
// Get a list of entity kinds returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_software_catalog::ListCatalogKindOptionalParams;
use datadog_api_client::datadogV2::api_software_catalog::SoftwareCatalogAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SoftwareCatalogAPI::with_config(configuration);
    let resp = api
        .list_catalog_kind(ListCatalogKindOptionalParams::default())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Get a list of entity kinds returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SoftwareCatalogApi(configuration);

apiInstance
  .listCatalogKind()
  .then((data: v2.ListKindCatalogResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create or update kinds{% #create-or-update-kinds %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                           |
| ----------------- | ------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/catalog/kind |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/catalog/kind |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/catalog/kind      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/catalog/kind      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/catalog/kind     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/catalog/kind |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/catalog/kind |

### Overview

Create or update kinds in Software Catalog.

OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.



### Request

#### Body Data (required)

Kind YAML or JSON.

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                                                  |
| ------------ | ---------------------- | ------ | ---------------------------------------------------------------------------- |
|              | Option 1               | object | Schema for kind.                                                             |
| Option 1     | description            | string | Short description of the kind.                                               |
| Option 1     | displayName            | string | The display name of the kind. Automatically generated if not provided.       |
| Option 1     | kind [*required*] | string | The name of the kind to create or update. This must be in kebab-case format. |
|              | Option 2               | string | Kind definition in raw JSON or YAML representation.                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "description": "string",
  "displayName": "string",
  "kind": "my-job"
}
```

{% /tab %}

### Response

{% tab title="202" %}
ACCEPTED
{% tab title="Model" %}
Upsert kind response.

| Parent field | Field       | Type     | Description                                                                                                   |
| ------------ | ----------- | -------- | ------------------------------------------------------------------------------------------------------------- |
|              | data        | [object] | List of kind responses.                                                                                       |
| data         | attributes  | object   | Kind attributes.                                                                                              |
| attributes   | description | string   | Short description of the kind.                                                                                |
| attributes   | displayName | string   | User friendly name of the kind.                                                                               |
| attributes   | name        | string   | The kind name.                                                                                                |
| data         | id          | string   | A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored. |
| data         | meta        | object   | Kind metadata.                                                                                                |
| meta         | createdAt   | string   | The creation time.                                                                                            |
| meta         | modifiedAt  | string   | The modification time.                                                                                        |
| data         | type        | string   | Kind.                                                                                                         |
|              | meta        | object   | Kind response metadata.                                                                                       |
| meta         | count       | int64    | Total kinds count.                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "description": "string",
        "displayName": "string",
        "name": "my-job"
      },
      "id": "4b163705-23c0-4573-b2fb-f6cea2163fcb",
      "meta": {
        "createdAt": "string",
        "modifiedAt": "string"
      },
      "type": "string"
    }
  ],
  "meta": {
    "count": "integer"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/kind" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF
                
##### 

```python
"""
Create or update kinds returns "ACCEPTED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi
from datadog_api_client.v2.model.kind_obj import KindObj

body = KindObj(
    kind="my-job",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    response = api_instance.upsert_catalog_kind(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create or update kinds returns "ACCEPTED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new

body = DatadogAPIClient::V2::KindObj.new({
  kind: "my-job",
})
p api_instance.upsert_catalog_kind(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Create or update kinds returns "ACCEPTED" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.UpsertCatalogKindRequest{
		KindObj: &datadogV2.KindObj{
			Kind: "my-job",
		}}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSoftwareCatalogApi(apiClient)
	resp, r, err := api.UpsertCatalogKind(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareCatalogApi.UpsertCatalogKind`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `SoftwareCatalogApi.UpsertCatalogKind`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create or update kinds returns "ACCEPTED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SoftwareCatalogApi;
import com.datadog.api.client.v2.model.KindObj;
import com.datadog.api.client.v2.model.UpsertCatalogKindRequest;
import com.datadog.api.client.v2.model.UpsertCatalogKindResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SoftwareCatalogApi apiInstance = new SoftwareCatalogApi(defaultClient);

    UpsertCatalogKindRequest body = new UpsertCatalogKindRequest(new KindObj().kind("my-job"));

    try {
      UpsertCatalogKindResponse result = apiInstance.upsertCatalogKind(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareCatalogApi#upsertCatalogKind");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
// Create or update kinds returns "ACCEPTED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_software_catalog::SoftwareCatalogAPI;
use datadog_api_client::datadogV2::model::KindObj;
use datadog_api_client::datadogV2::model::UpsertCatalogKindRequest;

#[tokio::main]
async fn main() {
    let body = UpsertCatalogKindRequest::KindObj(Box::new(KindObj::new("my-job".to_string())));
    let configuration = datadog::Configuration::new();
    let api = SoftwareCatalogAPI::with_config(configuration);
    let resp = api.upsert_catalog_kind(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Create or update kinds returns "ACCEPTED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SoftwareCatalogApi(configuration);

const params: v2.SoftwareCatalogApiUpsertCatalogKindRequest = {
  body: {
    kind: "my-job",
  },
};

apiInstance
  .upsertCatalogKind(params)
  .then((data: v2.UpsertCatalogKindResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete a single kind{% #delete-a-single-kind %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/catalog/kind/{kind_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/catalog/kind/{kind_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/catalog/kind/{kind_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/catalog/kind/{kind_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/catalog/kind/{kind_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/catalog/kind/{kind_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/catalog/kind/{kind_id} |

### Overview

Delete a single kind in Software Catalog.

OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type   | Description  |
| ------------------------- | ------ | ------------ |
| kind_id [*required*] | string | Entity kind. |

### Response

{% tab title="204" %}
OK
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Path parametersexport kind_id="my-job"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/kind/${kind_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a single kind returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    api_instance.delete_catalog_kind(
        kind_id="my-job",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete a single kind returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
api_instance.delete_catalog_kind("my-job")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete a single kind returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewSoftwareCatalogApi(apiClient)
	r, err := api.DeleteCatalogKind(ctx, "my-job")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SoftwareCatalogApi.DeleteCatalogKind`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete a single kind returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.SoftwareCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    SoftwareCatalogApi apiInstance = new SoftwareCatalogApi(defaultClient);

    try {
      apiInstance.deleteCatalogKind("my-job");
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareCatalogApi#deleteCatalogKind");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
// Delete a single kind returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_software_catalog::SoftwareCatalogAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = SoftwareCatalogAPI::with_config(configuration);
    let resp = api.delete_catalog_kind("my-job".to_string()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Delete a single kind returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.SoftwareCatalogApi(configuration);

const params: v2.SoftwareCatalogApiDeleteCatalogKindRequest = {
  kindId: "my-job",
};

apiInstance
  .deleteCatalogKind(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
