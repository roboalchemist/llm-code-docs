# Source: https://docs.datadoghq.com/api/latest/software-catalog

# Software Catalog
API to create, update, retrieve, and delete Software Catalog entities.
## [Get a list of entities](https://docs.datadoghq.com/api/latest/software-catalog/#get-a-list-of-entities)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/software-catalog/#get-a-list-of-entities-v2)


GET https://api.ap1.datadoghq.com/api/v2/catalog/entityhttps://api.ap2.datadoghq.com/api/v2/catalog/entityhttps://api.datadoghq.eu/api/v2/catalog/entityhttps://api.ddog-gov.com/api/v2/catalog/entityhttps://api.datadoghq.com/api/v2/catalog/entityhttps://api.us3.datadoghq.com/api/v2/catalog/entityhttps://api.us5.datadoghq.com/api/v2/catalog/entity
### Overview
Get a list of entities from Software Catalog.
OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
page[offset]
integer
Specific offset to use as the beginning of the returned page.
page[limit]
integer
Maximum number of entities in the response.
filter[id]
string
Filter entities by UUID.
filter[ref]
string
Filter entities by reference
filter[name]
string
Filter entities by name.
filter[kind]
string
Filter entities by kind.
filter[owner]
string
Filter entities by owner.
filter[relation][type]
enum
Filter entities by relation type.  
Allowed enum values: `RelationTypeOwns, RelationTypeOwnedBy, RelationTypeDependsOn, RelationTypeDependencyOf, RelationTypePartsOf, RelationTypeHasPart, RelationTypeOtherOwns, RelationTypeOtherOwnedBy, RelationTypeImplementedBy, RelationTypeImplements`
filter[exclude_snapshot]
string
Filter entities by excluding snapshotted entities.
include
enum
Include relationship data.  
Allowed enum values: `schema, raw_schema, oncall, incident, relation`
includeDiscovered
boolean
If true, includes discovered services from APM and USM that do not have entity definitions.
### Response
  * [200](https://docs.datadoghq.com/api/latest/software-catalog/#ListCatalogEntity-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/software-catalog/#ListCatalogEntity-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/software-catalog/#ListCatalogEntity-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


List entity response.
Field
Type
Description
data
[object]
List of entity data.
attributes
object
Entity attributes.
apiVersion
string
The API version.
description
string
The description.
displayName
string
The display name.
kind
string
The kind.
name
string
The name.
namespace
string
The namespace.
owner
string
The owner.
tags
[string]
The tags.
id
string
Entity ID.
meta
object
Entity metadata.
createdAt
string
The creation time.
ingestionSource
string
The ingestion source.
modifiedAt
string
The modification time.
origin
string
The origin.
relationships
object
Entity relationships.
incidents
object
Entity to incidents relationship.
data
[object]
Relationships.
id
string
Associated data ID.
type
string
Relationship type.
oncall
object
Entity to oncalls relationship.
data
[object]
Relationships.
id
string
Associated data ID.
type
string
Relationship type.
rawSchema
object
Entity to raw schema relationship.
data
object
Relationship entry.
id
string
Associated data ID.
type
string
Relationship type.
relatedEntities
object
Entity to related entities relationship.
data
[object]
Relationships.
id
string
Associated data ID.
type
string
Relationship type.
schema
object
Entity to detail schema relationship.
data
object
Relationship entry.
id
string
Associated data ID.
type
string
Relationship type.
type
string
Entity.
included
[ <oneOf>]
List entity response included.
Option 1
object
Included detail entity schema.
attributes
object
Included schema.
schema
<oneOf>
Entity schema v3.
Option 1
object
Schema for service entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the service entity.
codeLocations
[object]
Schema for mapping source code locations to an entity.
paths
[string]
The paths (glob) to the source code of the service.
repositoryURL
string
The repository path of the source code of the entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
pipelines
object
CI Pipelines association.
fingerprints
[string]
A list of CI Fingerprints that associate CI Pipelines with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 Service Kind object. Allowed enum values: `service`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 Service Spec object.
componentOf
[string]
A list of components the service is a part of
dependsOn
[string]
A list of components the service depends on.
languages
[string]
The service's programming language.
lifecycle
string
The lifecycle state of the component.
tier
string
The importance of the component.
type
string
The type of service.
Option 2
object
Schema for datastore entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the datastore entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 Datastore Kind object. Allowed enum values: `datastore`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 Datastore Spec object.
componentOf
[string]
A list of components the datastore is a part of
lifecycle
string
The lifecycle state of the datastore.
tier
string
The importance of the datastore.
type
string
The type of datastore.
Option 3
object
Schema for queue entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the datastore entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 Queue Kind object. Allowed enum values: `queue`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 Queue Spec object.
componentOf
[string]
A list of components the queue is a part of
lifecycle
string
The lifecycle state of the queue.
tier
string
The importance of the queue.
type
string
The type of queue.
Option 4
object
Schema for system entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the service entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
pipelines
object
CI Pipelines association.
fingerprints
[string]
A list of CI Fingerprints that associate CI Pipelines with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 System Kind object. Allowed enum values: `system`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 System Spec object.
components
[string]
A list of components belongs to the system.
lifecycle
string
The lifecycle state of the component.
tier
string
An entity reference to the owner of the component.
Option 5
object
Schema for API entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the API entity.
codeLocations
[object]
Schema for mapping source code locations to an entity.
paths
[string]
The paths (glob) to the source code of the service.
repositoryURL
string
The repository path of the source code of the entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
pipelines
object
CI Pipelines association.
fingerprints
[string]
A list of CI Fingerprints that associate CI Pipelines with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 API Kind object. Allowed enum values: `api`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 API Spec object.
implementedBy
[string]
Services which implemented the API.
interface
<oneOf>
The API definition.
lifecycle
string
The lifecycle state of the component.
tier
string
The importance of the component.
type
string
The type of API.
id
string
Entity ID.
type
enum
Schema type. Allowed enum values: `schema`
Option 2
object
Included raw schema.
attributes
object
Included raw schema attributes.
rawSchema
string
Schema from user input in base64 encoding.
id
string
Raw schema ID.
type
enum
Raw schema type. Allowed enum values: `rawSchema`
Option 3
object
Included related entity.
attributes
object
Related entity attributes.
kind
string
Entity kind.
name
string
Entity name.
namespace
string
Entity namespace.
type
string
Entity relation type to the associated entity.
id
string
Entity UUID.
meta
object
Included related entity meta.
createdAt
date-time
Entity creation time.
defined_by
string
Entity relation defined by.
modifiedAt
date-time
Entity modification time.
source
string
Entity relation source.
type
enum
Related entity. Allowed enum values: `relatedEntity`
Option 4
object
Included oncall.
attributes
object
Included related oncall attributes.
escalations
[object]
Oncall escalations.
email
string
Oncall email.
escalationLevel
int64
Oncall level.
name
string
Oncall name.
provider
string
Oncall provider.
id
string
Oncall ID.
type
enum
Oncall type. Allowed enum values: `oncall`
Option 5
object
Included incident.
attributes
object
Incident attributes.
createdAt
date-time
Incident creation time.
htmlURL
string
Incident URL.
provider
string
Incident provider.
status
string
Incident status.
title
string
Incident title.
id
string
Incident ID.
type
enum
Incident description. Allowed enum values: `incident`
links
object
List entity response links.
next
string
Next link.
previous
string
Previous link.
self
string
Current link.
meta
object
Entity metadata.
count
int64
Total entities count.
includeCount
int64
Total included data count.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=typescript)


#####  Get a list of entities
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/entity" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of entities
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of entities
```
# Get a list of entities returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
p api_instance.list_catalog_entity()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of entities
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of entities
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get a list of entities
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a list of entities
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create or update entities](https://docs.datadoghq.com/api/latest/software-catalog/#create-or-update-entities)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/software-catalog/#create-or-update-entities-v2)


POST https://api.ap1.datadoghq.com/api/v2/catalog/entityhttps://api.ap2.datadoghq.com/api/v2/catalog/entityhttps://api.datadoghq.eu/api/v2/catalog/entityhttps://api.ddog-gov.com/api/v2/catalog/entityhttps://api.datadoghq.com/api/v2/catalog/entityhttps://api.us3.datadoghq.com/api/v2/catalog/entityhttps://api.us5.datadoghq.com/api/v2/catalog/entity
### Overview
Create or update entities in Software Catalog.
OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.
### Request
#### Body Data (required)
Entity YAML or JSON.
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


Field
Type
Description
Option 1
<oneOf>
Entity schema v3.
Option 1
object
Schema for service entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the service entity.
codeLocations
[object]
Schema for mapping source code locations to an entity.
paths
[string]
The paths (glob) to the source code of the service.
repositoryURL
string
The repository path of the source code of the entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
pipelines
object
CI Pipelines association.
fingerprints
[string]
A list of CI Fingerprints that associate CI Pipelines with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 Service Kind object. Allowed enum values: `service`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 Service Spec object.
componentOf
[string]
A list of components the service is a part of
dependsOn
[string]
A list of components the service depends on.
languages
[string]
The service's programming language.
lifecycle
string
The lifecycle state of the component.
tier
string
The importance of the component.
type
string
The type of service.
Option 2
object
Schema for datastore entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the datastore entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 Datastore Kind object. Allowed enum values: `datastore`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 Datastore Spec object.
componentOf
[string]
A list of components the datastore is a part of
lifecycle
string
The lifecycle state of the datastore.
tier
string
The importance of the datastore.
type
string
The type of datastore.
Option 3
object
Schema for queue entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the datastore entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 Queue Kind object. Allowed enum values: `queue`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 Queue Spec object.
componentOf
[string]
A list of components the queue is a part of
lifecycle
string
The lifecycle state of the queue.
tier
string
The importance of the queue.
type
string
The type of queue.
Option 4
object
Schema for system entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the service entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
pipelines
object
CI Pipelines association.
fingerprints
[string]
A list of CI Fingerprints that associate CI Pipelines with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 System Kind object. Allowed enum values: `system`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 System Spec object.
components
[string]
A list of components belongs to the system.
lifecycle
string
The lifecycle state of the component.
tier
string
An entity reference to the owner of the component.
Option 5
object
Schema for API entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the API entity.
codeLocations
[object]
Schema for mapping source code locations to an entity.
paths
[string]
The paths (glob) to the source code of the service.
repositoryURL
string
The repository path of the source code of the entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
pipelines
object
CI Pipelines association.
fingerprints
[string]
A list of CI Fingerprints that associate CI Pipelines with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 API Kind object. Allowed enum values: `api`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 API Spec object.
implementedBy
[string]
Services which implemented the API.
interface
<oneOf>
The API definition.
lifecycle
string
The lifecycle state of the component.
tier
string
The importance of the component.
type
string
The type of API.
Option 2
string
Entity definition in raw JSON or YAML representation.
```
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

Copy
### Response
  * [202](https://docs.datadoghq.com/api/latest/software-catalog/#UpsertCatalogEntity-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/software-catalog/#UpsertCatalogEntity-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/software-catalog/#UpsertCatalogEntity-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/software-catalog/#UpsertCatalogEntity-429-v2)


ACCEPTED
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


Upsert entity response.
Field
Type
Description
data
[object]
List of entity data.
attributes
object
Entity attributes.
apiVersion
string
The API version.
description
string
The description.
displayName
string
The display name.
kind
string
The kind.
name
string
The name.
namespace
string
The namespace.
owner
string
The owner.
tags
[string]
The tags.
id
string
Entity ID.
meta
object
Entity metadata.
createdAt
string
The creation time.
ingestionSource
string
The ingestion source.
modifiedAt
string
The modification time.
origin
string
The origin.
relationships
object
Entity relationships.
incidents
object
Entity to incidents relationship.
data
[object]
Relationships.
id
string
Associated data ID.
type
string
Relationship type.
oncall
object
Entity to oncalls relationship.
data
[object]
Relationships.
id
string
Associated data ID.
type
string
Relationship type.
rawSchema
object
Entity to raw schema relationship.
data
object
Relationship entry.
id
string
Associated data ID.
type
string
Relationship type.
relatedEntities
object
Entity to related entities relationship.
data
[object]
Relationships.
id
string
Associated data ID.
type
string
Relationship type.
schema
object
Entity to detail schema relationship.
data
object
Relationship entry.
id
string
Associated data ID.
type
string
Relationship type.
type
string
Entity.
included
[ <oneOf>]
Upsert entity response included.
Option 1
object
Included detail entity schema.
attributes
object
Included schema.
schema
<oneOf>
Entity schema v3.
Option 1
object
Schema for service entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the service entity.
codeLocations
[object]
Schema for mapping source code locations to an entity.
paths
[string]
The paths (glob) to the source code of the service.
repositoryURL
string
The repository path of the source code of the entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
pipelines
object
CI Pipelines association.
fingerprints
[string]
A list of CI Fingerprints that associate CI Pipelines with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 Service Kind object. Allowed enum values: `service`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 Service Spec object.
componentOf
[string]
A list of components the service is a part of
dependsOn
[string]
A list of components the service depends on.
languages
[string]
The service's programming language.
lifecycle
string
The lifecycle state of the component.
tier
string
The importance of the component.
type
string
The type of service.
Option 2
object
Schema for datastore entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the datastore entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 Datastore Kind object. Allowed enum values: `datastore`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 Datastore Spec object.
componentOf
[string]
A list of components the datastore is a part of
lifecycle
string
The lifecycle state of the datastore.
tier
string
The importance of the datastore.
type
string
The type of datastore.
Option 3
object
Schema for queue entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the datastore entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 Queue Kind object. Allowed enum values: `queue`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 Queue Spec object.
componentOf
[string]
A list of components the queue is a part of
lifecycle
string
The lifecycle state of the queue.
tier
string
The importance of the queue.
type
string
The type of queue.
Option 4
object
Schema for system entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the service entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
pipelines
object
CI Pipelines association.
fingerprints
[string]
A list of CI Fingerprints that associate CI Pipelines with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 System Kind object. Allowed enum values: `system`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 System Spec object.
components
[string]
A list of components belongs to the system.
lifecycle
string
The lifecycle state of the component.
tier
string
An entity reference to the owner of the component.
Option 5
object
Schema for API entities.
apiVersion [_required_]
enum
The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version. Allowed enum values: `v3,v2.2,v2.1,v2`
datadog
object
Datadog product integrations for the API entity.
codeLocations
[object]
Schema for mapping source code locations to an entity.
paths
[string]
The paths (glob) to the source code of the service.
repositoryURL
string
The repository path of the source code of the entity.
events
[object]
Events associations.
name
string
The name of the query.
query
string
The query to run.
logs
[object]
Logs association.
name
string
The name of the query.
query
string
The query to run.
performanceData
object
Performance stats association.
tags
[string]
A list of APM entity tags that associates the APM Stats data with the entity.
pipelines
object
CI Pipelines association.
fingerprints
[string]
A list of CI Fingerprints that associate CI Pipelines with the entity.
extensions
object
Custom extensions. This is the free-formed field to send client-side metadata. No Datadog features are affected by this field.
integrations
object
A base schema for defining third-party integrations.
opsgenie
object
An Opsgenie integration schema.
region
string
The region for the Opsgenie integration.
serviceURL [_required_]
string
The service URL for the Opsgenie integration.
pagerduty
object
A PagerDuty integration schema.
serviceURL [_required_]
string
The service URL for the PagerDuty integration.
kind [_required_]
enum
The definition of Entity V3 API Kind object. Allowed enum values: `api`
metadata [_required_]
object
The definition of Entity V3 Metadata object.
additionalOwners
[object]
The additional owners of the entity, usually a team.
name [_required_]
string
Team name.
type
string
Team type.
contacts
[object]
A list of contacts for the entity.
contact [_required_]
string
Contact value.
name
string
Contact name.
type [_required_]
string
Contact type.
description
string
Short description of the entity. The UI can leverage the description for display.
displayName
string
User friendly name of the entity. The UI can leverage the display name for display.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
inheritFrom
string
The entity reference from which to inherit metadata
links
[object]
A list of links for the entity.
name [_required_]
string
Link name.
provider
string
Link provider.
type [_required_]
string
Link type.
default: `other`
url [_required_]
string
Link URL.
managed
object
A read-only set of Datadog managed attributes generated by Datadog. User supplied values are ignored.
name [_required_]
string
Unique name given to an entity under the kind/namespace.
namespace
string
Namespace is a part of unique identifier. It has a default value of 'default'.
owner
string
The owner of the entity, usually a team.
tags
[string]
A set of custom tags.
spec
object
The definition of Entity V3 API Spec object.
implementedBy
[string]
Services which implemented the API.
interface
<oneOf>
The API definition.
lifecycle
string
The lifecycle state of the component.
tier
string
The importance of the component.
type
string
The type of API.
id
string
Entity ID.
type
enum
Schema type. Allowed enum values: `schema`
meta
object
Entity metadata.
count
int64
Total entities count.
includeCount
int64
Total included data count.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=typescript)


#####  Create or update software catalog entity using schema v3 returns "ACCEPTED" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/entity" \
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

                        
```

#####  Create or update software catalog entity using schema v3 returns "ACCEPTED" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create or update software catalog entity using schema v3 returns "ACCEPTED" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create or update software catalog entity using schema v3 returns "ACCEPTED" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create or update software catalog entity using schema v3 returns "ACCEPTED" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create or update software catalog entity using schema v3 returns "ACCEPTED" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create or update software catalog entity using schema v3 returns "ACCEPTED" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Delete a single entity](https://docs.datadoghq.com/api/latest/software-catalog/#delete-a-single-entity)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/software-catalog/#delete-a-single-entity-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/catalog/entity/{entity_id}https://api.ap2.datadoghq.com/api/v2/catalog/entity/{entity_id}https://api.datadoghq.eu/api/v2/catalog/entity/{entity_id}https://api.ddog-gov.com/api/v2/catalog/entity/{entity_id}https://api.datadoghq.com/api/v2/catalog/entity/{entity_id}https://api.us3.datadoghq.com/api/v2/catalog/entity/{entity_id}https://api.us5.datadoghq.com/api/v2/catalog/entity/{entity_id}
### Overview
Delete a single entity in Software Catalog.
OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
entity_id [_required_]
string
UUID or Entity Ref.
### Response
  * [204](https://docs.datadoghq.com/api/latest/software-catalog/#DeleteCatalogEntity-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/software-catalog/#DeleteCatalogEntity-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/software-catalog/#DeleteCatalogEntity-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/software-catalog/#DeleteCatalogEntity-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/software-catalog/#DeleteCatalogEntity-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=typescript)


#####  Delete a single entity
Copy
```
                  # Path parameters  
export entity_id="service:myservice"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/entity/${entity_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a single entity
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a single entity
```
# Delete a single entity returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
api_instance.delete_catalog_entity("service:myservice")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a single entity
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete a single entity
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Delete a single entity
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Delete a single entity
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a list of entity relations](https://docs.datadoghq.com/api/latest/software-catalog/#get-a-list-of-entity-relations)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/software-catalog/#get-a-list-of-entity-relations-v2)


GET https://api.ap1.datadoghq.com/api/v2/catalog/relationhttps://api.ap2.datadoghq.com/api/v2/catalog/relationhttps://api.datadoghq.eu/api/v2/catalog/relationhttps://api.ddog-gov.com/api/v2/catalog/relationhttps://api.datadoghq.com/api/v2/catalog/relationhttps://api.us3.datadoghq.com/api/v2/catalog/relationhttps://api.us5.datadoghq.com/api/v2/catalog/relation
### Overview
Get a list of entity relations from Software Catalog.
OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
page[offset]
integer
Specific offset to use as the beginning of the returned page.
page[limit]
integer
Maximum number of relations in the response.
filter[type]
enum
Filter relations by type.  
Allowed enum values: `RelationTypeOwns, RelationTypeOwnedBy, RelationTypeDependsOn, RelationTypeDependencyOf, RelationTypePartsOf, RelationTypeHasPart, RelationTypeOtherOwns, RelationTypeOtherOwnedBy, RelationTypeImplementedBy, RelationTypeImplements`
filter[from_ref]
string
Filter relations by the reference of the first entity in the relation.
filter[to_ref]
string
Filter relations by the reference of the second entity in the relation.
include
enum
Include relationship data.  
Allowed enum values: `entity, schema`
includeDiscovered
boolean
If true, includes relationships discovered by APM and USM.
### Response
  * [200](https://docs.datadoghq.com/api/latest/software-catalog/#ListCatalogRelation-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/software-catalog/#ListCatalogRelation-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/software-catalog/#ListCatalogRelation-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


List entity relation response.
Field
Type
Description
data
[object]
Array of relation responses
attributes
object
Relation attributes.
from
object
Relation entity reference.
kind
string
Entity kind.
name
string
Entity name.
namespace
string
Entity namespace.
to
object
Relation entity reference.
kind
string
Entity kind.
name
string
Entity name.
namespace
string
Entity namespace.
type
enum
Supported relation types. Allowed enum values: `RelationTypeOwns,RelationTypeOwnedBy,RelationTypeDependsOn,RelationTypeDependencyOf,RelationTypePartsOf,RelationTypeHasPart,RelationTypeOtherOwns,RelationTypeOtherOwnedBy,RelationTypeImplementedBy,RelationTypeImplements`
id
string
Relation ID.
meta
object
Relation metadata.
createdAt
date-time
Relation creation time.
definedBy
string
Relation defined by.
modifiedAt
date-time
Relation modification time.
source
string
Relation source.
relationships
object
Relation relationships.
fromEntity
object
Relation to entity.
data
object
Relationship entry.
id
string
Associated data ID.
type
string
Relationship type.
meta
object
Entity metadata.
createdAt
string
The creation time.
ingestionSource
string
The ingestion source.
modifiedAt
string
The modification time.
origin
string
The origin.
toEntity
object
Relation to entity.
data
object
Relationship entry.
id
string
Associated data ID.
type
string
Relationship type.
meta
object
Entity metadata.
createdAt
string
The creation time.
ingestionSource
string
The ingestion source.
modifiedAt
string
The modification time.
origin
string
The origin.
subtype
string
Relation subtype.
type
enum
Relation type. Allowed enum values: `relation`
included
[object]
List relation response included entities.
attributes
object
Entity attributes.
apiVersion
string
The API version.
description
string
The description.
displayName
string
The display name.
kind
string
The kind.
name
string
The name.
namespace
string
The namespace.
owner
string
The owner.
tags
[string]
The tags.
id
string
Entity ID.
meta
object
Entity metadata.
createdAt
string
The creation time.
ingestionSource
string
The ingestion source.
modifiedAt
string
The modification time.
origin
string
The origin.
relationships
object
Entity relationships.
incidents
object
Entity to incidents relationship.
data
[object]
Relationships.
id
string
Associated data ID.
type
string
Relationship type.
oncall
object
Entity to oncalls relationship.
data
[object]
Relationships.
id
string
Associated data ID.
type
string
Relationship type.
rawSchema
object
Entity to raw schema relationship.
data
object
Relationship entry.
id
string
Associated data ID.
type
string
Relationship type.
relatedEntities
object
Entity to related entities relationship.
data
[object]
Relationships.
id
string
Associated data ID.
type
string
Relationship type.
schema
object
Entity to detail schema relationship.
data
object
Relationship entry.
id
string
Associated data ID.
type
string
Relationship type.
type
string
Entity.
links
object
List relation response links.
next
string
Next link.
previous
string
Previous link.
self
string
Current link.
meta
object
Relation response metadata.
count
int64
Total relations count.
includeCount
int64
Total included data count.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=typescript)


#####  Get a list of entity relations
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/relation" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of entity relations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of entity relations
```
# Get a list of entity relations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
p api_instance.list_catalog_relation()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of entity relations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of entity relations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get a list of entity relations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a list of entity relations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Preview catalog entities](https://docs.datadoghq.com/api/latest/software-catalog/#preview-catalog-entities)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/software-catalog/#preview-catalog-entities-v2)


POST https://api.ap1.datadoghq.com/api/v2/catalog/entity/previewhttps://api.ap2.datadoghq.com/api/v2/catalog/entity/previewhttps://api.datadoghq.eu/api/v2/catalog/entity/previewhttps://api.ddog-gov.com/api/v2/catalog/entity/previewhttps://api.datadoghq.com/api/v2/catalog/entity/previewhttps://api.us3.datadoghq.com/api/v2/catalog/entity/previewhttps://api.us5.datadoghq.com/api/v2/catalog/entity/preview
### Overview
OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.
### Response
  * [202](https://docs.datadoghq.com/api/latest/software-catalog/#PreviewCatalogEntities-202-v2)
  * [429](https://docs.datadoghq.com/api/latest/software-catalog/#PreviewCatalogEntities-429-v2)


Accepted
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


Field
Type
Description
data [_required_]
[object]
attributes
object
apiVersion
string
description
string
displayName
string
kind
string
name
string
namespace
string
owner
string
properties
object
tags
[string]
id
string
relationships
object
incidents
object
data
[object]
id [_required_]
string
type [_required_]
enum
Incident resource type. Allowed enum values: `incident`
default: `incident`
oncalls
object
data
[object]
id [_required_]
string
type [_required_]
enum
Oncall resource type. Allowed enum values: `oncall`
default: `oncall`
rawSchema
object
data [_required_]
object
id [_required_]
string
type [_required_]
enum
Raw schema resource type. Allowed enum values: `rawSchema`
default: `rawSchema`
relatedEntities
object
data
[object]
id [_required_]
string
type [_required_]
enum
Related entity resource type. Allowed enum values: `relatedEntity`
default: `relatedEntity`
schema
object
data [_required_]
object
id [_required_]
string
type [_required_]
enum
Schema resource type. Allowed enum values: `schema`
default: `schema`
type [_required_]
enum
Entity resource type. Allowed enum values: `entity`
default: `entity`
```
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

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=typescript)


#####  Preview catalog entities
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/entity/preview" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Preview catalog entities
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Preview catalog entities
```
# Preview catalog entities returns "Accepted" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
p api_instance.preview_catalog_entities()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Preview catalog entities
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Preview catalog entities
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Preview catalog entities
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Preview catalog entities
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a list of entity kinds](https://docs.datadoghq.com/api/latest/software-catalog/#get-a-list-of-entity-kinds)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/software-catalog/#get-a-list-of-entity-kinds-v2)


GET https://api.ap1.datadoghq.com/api/v2/catalog/kindhttps://api.ap2.datadoghq.com/api/v2/catalog/kindhttps://api.datadoghq.eu/api/v2/catalog/kindhttps://api.ddog-gov.com/api/v2/catalog/kindhttps://api.datadoghq.com/api/v2/catalog/kindhttps://api.us3.datadoghq.com/api/v2/catalog/kindhttps://api.us5.datadoghq.com/api/v2/catalog/kind
### Overview
Get a list of entity kinds from Software Catalog.
OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
page[offset]
integer
Specific offset to use as the beginning of the returned page.
page[limit]
integer
Maximum number of kinds in the response.
filter[id]
string
Filter entities by UUID.
filter[name]
string
Filter entities by name.
### Response
  * [200](https://docs.datadoghq.com/api/latest/software-catalog/#ListCatalogKind-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/software-catalog/#ListCatalogKind-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/software-catalog/#ListCatalogKind-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/software-catalog/#ListCatalogKind-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


List kind response.
Field
Type
Description
data
[object]
List of kind responses.
attributes
object
Kind attributes.
description
string
Short description of the kind.
displayName
string
User friendly name of the kind.
name
string
The kind name.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
meta
object
Kind metadata.
createdAt
string
The creation time.
modifiedAt
string
The modification time.
type
string
Kind.
meta
object
Kind response metadata.
count
int64
Total kinds count.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=typescript)


#####  Get a list of entity kinds
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/kind" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a list of entity kinds
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a list of entity kinds
```
# Get a list of entity kinds returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
p api_instance.list_catalog_kind()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a list of entity kinds
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a list of entity kinds
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get a list of entity kinds
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a list of entity kinds
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Create or update kinds](https://docs.datadoghq.com/api/latest/software-catalog/#create-or-update-kinds)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/software-catalog/#create-or-update-kinds-v2)


POST https://api.ap1.datadoghq.com/api/v2/catalog/kindhttps://api.ap2.datadoghq.com/api/v2/catalog/kindhttps://api.datadoghq.eu/api/v2/catalog/kindhttps://api.ddog-gov.com/api/v2/catalog/kindhttps://api.datadoghq.com/api/v2/catalog/kindhttps://api.us3.datadoghq.com/api/v2/catalog/kindhttps://api.us5.datadoghq.com/api/v2/catalog/kind
### Overview
Create or update kinds in Software Catalog.
OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.
### Request
#### Body Data (required)
Kind YAML or JSON.
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


Field
Type
Description
Option 1
object
Schema for kind.
description
string
Short description of the kind.
displayName
string
The display name of the kind. Automatically generated if not provided.
kind [_required_]
string
The name of the kind to create or update. This must be in kebab-case format.
Option 2
string
Kind definition in raw JSON or YAML representation.
```
{
  "description": "string",
  "displayName": "string",
  "kind": "my-job"
}
```

Copy
### Response
  * [202](https://docs.datadoghq.com/api/latest/software-catalog/#UpsertCatalogKind-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/software-catalog/#UpsertCatalogKind-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/software-catalog/#UpsertCatalogKind-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/software-catalog/#UpsertCatalogKind-429-v2)


ACCEPTED
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


Upsert kind response.
Field
Type
Description
data
[object]
List of kind responses.
attributes
object
Kind attributes.
description
string
Short description of the kind.
displayName
string
User friendly name of the kind.
name
string
The kind name.
id
string
A read-only globally unique identifier for the entity generated by Datadog. User supplied values are ignored.
meta
object
Kind metadata.
createdAt
string
The creation time.
modifiedAt
string
The modification time.
type
string
Kind.
meta
object
Kind response metadata.
count
int64
Total kinds count.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=typescript)


#####  Create or update kinds
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/kind" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Create or update kinds
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create or update kinds
```
# Create or update kinds returns "ACCEPTED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new

body = DatadogAPIClient::V2::KindObj.new({
  kind: "my-job",
})
p api_instance.upsert_catalog_kind(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create or update kinds
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create or update kinds
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create or update kinds
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create or update kinds
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Delete a single kind](https://docs.datadoghq.com/api/latest/software-catalog/#delete-a-single-kind)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/software-catalog/#delete-a-single-kind-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/catalog/kind/{kind_id}https://api.ap2.datadoghq.com/api/v2/catalog/kind/{kind_id}https://api.datadoghq.eu/api/v2/catalog/kind/{kind_id}https://api.ddog-gov.com/api/v2/catalog/kind/{kind_id}https://api.datadoghq.com/api/v2/catalog/kind/{kind_id}https://api.us3.datadoghq.com/api/v2/catalog/kind/{kind_id}https://api.us5.datadoghq.com/api/v2/catalog/kind/{kind_id}
### Overview
Delete a single kind in Software Catalog.
OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#software-catalog) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
kind_id [_required_]
string
Entity kind.
### Response
  * [204](https://docs.datadoghq.com/api/latest/software-catalog/#DeleteCatalogKind-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/software-catalog/#DeleteCatalogKind-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/software-catalog/#DeleteCatalogKind-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/software-catalog/#DeleteCatalogKind-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/software-catalog/#DeleteCatalogKind-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/software-catalog/)
  * [Example](https://docs.datadoghq.com/api/latest/software-catalog/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/software-catalog/?code-lang=typescript)


#####  Delete a single kind
Copy
```
                  # Path parameters  
export kind_id="my-job"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/catalog/kind/${kind_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a single kind
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a single kind
```
# Delete a single kind returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::SoftwareCatalogAPI.new
api_instance.delete_catalog_kind("my-job")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a single kind
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete a single kind
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Delete a single kind
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Delete a single kind
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=6ad15fea-7ced-4fb3-a43c-51efabf5cb5a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=03d0c8e6-6442-4f0a-a4a5-0bb3027479df&pt=Software%20Catalog&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fsoftware-catalog%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=6ad15fea-7ced-4fb3-a43c-51efabf5cb5a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=03d0c8e6-6442-4f0a-a4a5-0bb3027479df&pt=Software%20Catalog&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fsoftware-catalog%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=4af5b44a-7737-4dee-9476-a81e3a252a57&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Software%20Catalog&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fsoftware-catalog%2F&r=&lt=13096&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=835151)
