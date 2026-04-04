# Source: https://docs.datadoghq.com/api/latest/service-definition.md

---
title: Service Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Service Definition
---

# Service Definition

API to create, update, retrieve and delete service definitions. Note: Service Catalog [v3.0 schema](https://docs.datadoghq.com/service_catalog/service_definitions/v3-0/) has new API endpoints documented under [Software Catalog](https://docs.datadoghq.com/api/latest/software-catalog/). Use the following Service Definition endpoints for v2.2 and earlier.

## Get all service definitions{% #get-all-service-definitions %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/services/definitions |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/services/definitions |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/services/definitions      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/services/definitions      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/services/definitions     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/services/definitions |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/services/definitions |

### Overview

Get a list of all service definitions from the Datadog Service Catalog. This endpoint requires the `apm_service_catalog_read` permission.

OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-definition) to access this endpoint.



### Arguments

#### Query Strings

| Name           | Type    | Description                                                                          |
| -------------- | ------- | ------------------------------------------------------------------------------------ |
| page[size]     | integer | Size for a given page. The maximum allowed value is 100.                             |
| page[number]   | integer | Specific page number to return.                                                      |
| schema_version | enum    | The schema version desired in the response.Allowed enum values: `v1, v2, v2.1, v2.2` |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Create service definitions response.

| Parent field       | Field                            | Type            | Description                                                                                                                                       |
| ------------------ | -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                             | [object]        | Data representing service definitions.                                                                                                            |
| data               | attributes                       | object          | Service definition attributes.                                                                                                                    |
| attributes         | meta                             | object          | Metadata about a service definition.                                                                                                              |
| meta               | github-html-url                  | string          | GitHub HTML URL.                                                                                                                                  |
| meta               | ingested-schema-version          | string          | Ingestion schema version.                                                                                                                         |
| meta               | ingestion-source                 | string          | Ingestion source of the service definition.                                                                                                       |
| meta               | last-modified-time               | string          | Last modified time of the service definition.                                                                                                     |
| meta               | origin                           | string          | User defined origin of the service definition.                                                                                                    |
| meta               | origin-detail                    | string          | User defined origin's detail of the service definition.                                                                                           |
| meta               | warnings                         | [object]        | A list of schema validation warnings.                                                                                                             |
| warnings           | instance-location                | string          | The warning instance location.                                                                                                                    |
| warnings           | keyword-location                 | string          | The warning keyword location.                                                                                                                     |
| warnings           | message                          | string          | The warning message.                                                                                                                              |
| attributes         | schema                           |  <oneOf>   | Service definition schema.                                                                                                                        |
| schema             | Option 1                         | object          | **DEPRECATED**: Deprecated - Service definition V1 for providing additional service metadata and integrations.                                    |
| Option 1           | contact                          | object          | Contact information about the service.                                                                                                            |
| contact            | email                            | string          | Service owner's email.                                                                                                                            |
| contact            | slack                            | string          | Service owner's Slack channel.                                                                                                                    |
| Option 1           | extensions                       | object          | Extensions to V1 schema.                                                                                                                          |
| Option 1           | external-resources               | [object]        | A list of external links related to the services.                                                                                                 |
| external-resources | name [*required*]           | string          | Link name.                                                                                                                                        |
| external-resources | type [*required*]           | enum            | Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`                                                            |
| external-resources | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 1           | info [*required*]           | object          | Basic information about a service.                                                                                                                |
| info               | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| info               | description                      | string          | A short description of the service.                                                                                                               |
| info               | display-name                     | string          | A friendly name of the service.                                                                                                                   |
| info               | service-tier                     | string          | Service tier.                                                                                                                                     |
| Option 1           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | pagerduty                        | string          | PagerDuty service URL for the service.                                                                                                            |
| Option 1           | org                              | object          | Org related information about the service.                                                                                                        |
| org                | application                      | string          | App feature this service supports.                                                                                                                |
| org                | team                             | string          | Team that owns the service.                                                                                                                       |
| Option 1           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v1`                                                                                              |
| Option 1           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| schema             | Option 2                         | object          | Service definition V2 for providing service metadata and integrations.                                                                            |
| Option 2           | contacts                         | [ <oneOf>] | A list of contacts related to the services.                                                                                                       |
| contacts           | Option 1                         | object          | Service owner's email.                                                                                                                            |
| Option 1           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 1           | name                             | string          | Contact email.                                                                                                                                    |
| Option 1           | type [*required*]           | enum            | Contact type. Allowed enum values: `email`                                                                                                        |
| contacts           | Option 2                         | object          | Service owner's Slack channel.                                                                                                                    |
| Option 2           | contact [*required*]        | string          | Slack Channel.                                                                                                                                    |
| Option 2           | name                             | string          | Contact Slack.                                                                                                                                    |
| Option 2           | type [*required*]           | enum            | Contact type. Allowed enum values: `slack`                                                                                                        |
| contacts           | Option 3                         | object          | Service owner's Microsoft Teams.                                                                                                                  |
| Option 3           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 3           | name                             | string          | Contact Microsoft Teams.                                                                                                                          |
| Option 3           | type [*required*]           | enum            | Contact type. Allowed enum values: `microsoft-teams`                                                                                              |
| Option 2           | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 2           | dd-team                          | string          | Experimental feature. A Team handle that matches a Team in the Datadog Teams product.                                                             |
| Option 2           | docs                             | [object]        | A list of documentation related to the services.                                                                                                  |
| docs               | name [*required*]           | string          | Document name.                                                                                                                                    |
| docs               | provider                         | string          | Document provider.                                                                                                                                |
| docs               | url [*required*]            | string          | Document URL.                                                                                                                                     |
| Option 2           | extensions                       | object          | Extensions to V2 schema.                                                                                                                          |
| Option 2           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie           | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie           | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations       | pagerduty                        | string          | PagerDuty service URL for the service.                                                                                                            |
| Option 2           | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links              | name [*required*]           | string          | Link name.                                                                                                                                        |
| links              | type [*required*]           | enum            | Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`                                                            |
| links              | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 2           | repos                            | [object]        | A list of code repositories related to the services.                                                                                              |
| repos              | name [*required*]           | string          | Repository name.                                                                                                                                  |
| repos              | provider                         | string          | Repository provider.                                                                                                                              |
| repos              | url [*required*]            | string          | Repository URL.                                                                                                                                   |
| Option 2           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2`                                                                                              |
| Option 2           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 2           | team                             | string          | Team that owns the service.                                                                                                                       |
| schema             | Option 3                         | object          | Service definition v2.1 for providing service metadata and integrations.                                                                          |
| Option 3           | application                      | string          | Identifier for a group of related services serving a product feature, which the service is a part of.                                             |
| Option 3           | contacts                         | [ <oneOf>] | A list of contacts related to the services.                                                                                                       |
| contacts           | Option 1                         | object          | Service owner's email.                                                                                                                            |
| Option 1           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 1           | name                             | string          | Contact email.                                                                                                                                    |
| Option 1           | type [*required*]           | enum            | Contact type. Allowed enum values: `email`                                                                                                        |
| contacts           | Option 2                         | object          | Service owner's Slack channel.                                                                                                                    |
| Option 2           | contact [*required*]        | string          | Slack Channel.                                                                                                                                    |
| Option 2           | name                             | string          | Contact Slack.                                                                                                                                    |
| Option 2           | type [*required*]           | enum            | Contact type. Allowed enum values: `slack`                                                                                                        |
| contacts           | Option 3                         | object          | Service owner's Microsoft Teams.                                                                                                                  |
| Option 3           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 3           | name                             | string          | Contact Microsoft Teams.                                                                                                                          |
| Option 3           | type [*required*]           | enum            | Contact type. Allowed enum values: `microsoft-teams`                                                                                              |
| Option 3           | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 3           | description                      | string          | A short description of the service.                                                                                                               |
| Option 3           | extensions                       | object          | Extensions to v2.1 schema.                                                                                                                        |
| Option 3           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie           | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie           | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations       | pagerduty                        | object          | PagerDuty integration for the service.                                                                                                            |
| pagerduty          | service-url                      | string          | PagerDuty service url.                                                                                                                            |
| Option 3           | lifecycle                        | string          | The current life cycle phase of the service.                                                                                                      |
| Option 3           | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links              | name [*required*]           | string          | Link name.                                                                                                                                        |
| links              | provider                         | string          | Link provider.                                                                                                                                    |
| links              | type [*required*]           | enum            | Link type. Allowed enum values: `doc,repo,runbook,dashboard,other`                                                                                |
| links              | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 3           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2.1`                                                                                            |
| Option 3           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 3           | team                             | string          | Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.                                                    |
| Option 3           | tier                             | string          | Importance of the service.                                                                                                                        |
| schema             | Option 4                         | object          | Service definition v2.2 for providing service metadata and integrations.                                                                          |
| Option 4           | application                      | string          | Identifier for a group of related services serving a product feature, which the service is a part of.                                             |
| Option 4           | ci-pipeline-fingerprints         | [string]        | A set of CI fingerprints.                                                                                                                         |
| Option 4           | contacts                         | [object]        | A list of contacts related to the services.                                                                                                       |
| contacts           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| contacts           | name                             | string          | Contact Name.                                                                                                                                     |
| contacts           | type [*required*]           | string          | Contact type. Datadog recognizes the following types: `email`, `slack`, and `microsoft-teams`.                                                    |
| Option 4           | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 4           | description                      | string          | A short description of the service.                                                                                                               |
| Option 4           | extensions                       | object          | Extensions to v2.2 schema.                                                                                                                        |
| Option 4           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie           | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie           | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations       | pagerduty                        | object          | PagerDuty integration for the service.                                                                                                            |
| pagerduty          | service-url                      | string          | PagerDuty service url.                                                                                                                            |
| Option 4           | languages                        | [string]        | The service's programming language. Datadog recognizes the following languages: `dotnet`, `go`, `java`, `js`, `php`, `python`, `ruby`, and `c++`. |
| Option 4           | lifecycle                        | string          | The current life cycle phase of the service.                                                                                                      |
| Option 4           | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links              | name [*required*]           | string          | Link name.                                                                                                                                        |
| links              | provider                         | string          | Link provider.                                                                                                                                    |
| links              | type [*required*]           | string          | Link type. Datadog recognizes the following types: `runbook`, `doc`, `repo`, `dashboard`, and `other`.                                            |
| links              | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 4           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2.2`                                                                                            |
| Option 4           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 4           | team                             | string          | Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.                                                    |
| Option 4           | tier                             | string          | Importance of the service.                                                                                                                        |
| Option 4           | type                             | string          | The type of service.                                                                                                                              |
| data               | id                               | string          | Service definition id.                                                                                                                            |
| data               | type                             | string          | Service definition type.                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "meta": {
          "github-html-url": "string",
          "ingested-schema-version": "string",
          "ingestion-source": "string",
          "last-modified-time": "string",
          "origin": "string",
          "origin-detail": "string",
          "warnings": [
            {
              "instance-location": "string",
              "keyword-location": "string",
              "message": "string"
            }
          ]
        },
        "schema": {
          "contact": {
            "email": "contact@datadoghq.com",
            "slack": "https://yourcompany.slack.com/archives/channel123"
          },
          "extensions": {
            "myorg/extension": "extensionValue"
          },
          "external-resources": [
            {
              "name": "Runbook",
              "type": "runbook",
              "url": "https://my-runbook"
            }
          ],
          "info": {
            "dd-service": "myservice",
            "description": "A shopping cart service",
            "display-name": "My Service",
            "service-tier": "Tier 1"
          },
          "integrations": {
            "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"
          },
          "org": {
            "application": "E-Commerce",
            "team": "my-team"
          },
          "schema-version": "v1",
          "tags": [
            "my:tag",
            "service:tag"
          ]
        }
      },
      "id": "string",
      "type": "string"
    }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all service definitions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_schema_versions import ServiceDefinitionSchemaVersions

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.list_service_definitions(
        schema_version=ServiceDefinitionSchemaVersions.V2_1,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get all service definitions returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new
opts = {
  schema_version: ServiceDefinitionSchemaVersions::V2_1,
}
p api_instance.list_service_definitions(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get all service definitions returns "OK" response

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
    api := datadogV2.NewServiceDefinitionApi(apiClient)
    resp, r, err := api.ListServiceDefinitions(ctx, *datadogV2.NewListServiceDefinitionsOptionalParameters().WithSchemaVersion(datadogV2.SERVICEDEFINITIONSCHEMAVERSIONS_V2_1))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.ListServiceDefinitions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceDefinitionApi.ListServiceDefinitions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get all service definitions returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;
import com.datadog.api.client.v2.api.ServiceDefinitionApi.ListServiceDefinitionsOptionalParameters;
import com.datadog.api.client.v2.model.ServiceDefinitionSchemaVersions;
import com.datadog.api.client.v2.model.ServiceDefinitionsListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    try {
      ServiceDefinitionsListResponse result =
          apiInstance.listServiceDefinitions(
              new ListServiceDefinitionsOptionalParameters()
                  .schemaVersion(ServiceDefinitionSchemaVersions.V2_1));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceDefinitionApi#listServiceDefinitions");
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
// Get all service definitions returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::ListServiceDefinitionsOptionalParams;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;
use datadog_api_client::datadogV2::model::ServiceDefinitionSchemaVersions;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api
        .list_service_definitions(
            ListServiceDefinitionsOptionalParams::default()
                .schema_version(ServiceDefinitionSchemaVersions::V2_1),
        )
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
 * Get all service definitions returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiListServiceDefinitionsRequest = {
  schemaVersion: "v2.1",
};

apiInstance
  .listServiceDefinitions(params)
  .then((data: v2.ServiceDefinitionsListResponse) => {
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

## Create or update service definition{% #create-or-update-service-definition %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/services/definitions |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/services/definitions |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/services/definitions      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/services/definitions      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/services/definitions     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/services/definitions |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/services/definitions |

### Overview

Create or update service definition in the Datadog Service Catalog. This endpoint requires the `apm_service_catalog_write` permission.

OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-definition) to access this endpoint.



### Request

#### Body Data (required)

Service Definition YAML/JSON.

{% tab title="Model" %}

| Parent field | Field                            | Type            | Description                                                                                                                                       |
| ------------ | -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | Option 1                         | object          | Service definition v2.2 for providing service metadata and integrations.                                                                          |
| Option 1     | application                      | string          | Identifier for a group of related services serving a product feature, which the service is a part of.                                             |
| Option 1     | ci-pipeline-fingerprints         | [string]        | A set of CI fingerprints.                                                                                                                         |
| Option 1     | contacts                         | [object]        | A list of contacts related to the services.                                                                                                       |
| contacts     | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| contacts     | name                             | string          | Contact Name.                                                                                                                                     |
| contacts     | type [*required*]           | string          | Contact type. Datadog recognizes the following types: `email`, `slack`, and `microsoft-teams`.                                                    |
| Option 1     | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 1     | description                      | string          | A short description of the service.                                                                                                               |
| Option 1     | extensions                       | object          | Extensions to v2.2 schema.                                                                                                                        |
| Option 1     | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie     | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie     | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations | pagerduty                        | object          | PagerDuty integration for the service.                                                                                                            |
| pagerduty    | service-url                      | string          | PagerDuty service url.                                                                                                                            |
| Option 1     | languages                        | [string]        | The service's programming language. Datadog recognizes the following languages: `dotnet`, `go`, `java`, `js`, `php`, `python`, `ruby`, and `c++`. |
| Option 1     | lifecycle                        | string          | The current life cycle phase of the service.                                                                                                      |
| Option 1     | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links        | name [*required*]           | string          | Link name.                                                                                                                                        |
| links        | provider                         | string          | Link provider.                                                                                                                                    |
| links        | type [*required*]           | string          | Link type. Datadog recognizes the following types: `runbook`, `doc`, `repo`, `dashboard`, and `other`.                                            |
| links        | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 1     | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2.2`                                                                                            |
| Option 1     | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 1     | team                             | string          | Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.                                                    |
| Option 1     | tier                             | string          | Importance of the service.                                                                                                                        |
| Option 1     | type                             | string          | The type of service.                                                                                                                              |
|              | Option 2                         | object          | Service definition v2.1 for providing service metadata and integrations.                                                                          |
| Option 2     | application                      | string          | Identifier for a group of related services serving a product feature, which the service is a part of.                                             |
| Option 2     | contacts                         | [ <oneOf>] | A list of contacts related to the services.                                                                                                       |
| contacts     | Option 1                         | object          | Service owner's email.                                                                                                                            |
| Option 1     | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 1     | name                             | string          | Contact email.                                                                                                                                    |
| Option 1     | type [*required*]           | enum            | Contact type. Allowed enum values: `email`                                                                                                        |
| contacts     | Option 2                         | object          | Service owner's Slack channel.                                                                                                                    |
| Option 2     | contact [*required*]        | string          | Slack Channel.                                                                                                                                    |
| Option 2     | name                             | string          | Contact Slack.                                                                                                                                    |
| Option 2     | type [*required*]           | enum            | Contact type. Allowed enum values: `slack`                                                                                                        |
| contacts     | Option 3                         | object          | Service owner's Microsoft Teams.                                                                                                                  |
| Option 3     | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 3     | name                             | string          | Contact Microsoft Teams.                                                                                                                          |
| Option 3     | type [*required*]           | enum            | Contact type. Allowed enum values: `microsoft-teams`                                                                                              |
| Option 2     | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 2     | description                      | string          | A short description of the service.                                                                                                               |
| Option 2     | extensions                       | object          | Extensions to v2.1 schema.                                                                                                                        |
| Option 2     | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie     | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie     | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations | pagerduty                        | object          | PagerDuty integration for the service.                                                                                                            |
| pagerduty    | service-url                      | string          | PagerDuty service url.                                                                                                                            |
| Option 2     | lifecycle                        | string          | The current life cycle phase of the service.                                                                                                      |
| Option 2     | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links        | name [*required*]           | string          | Link name.                                                                                                                                        |
| links        | provider                         | string          | Link provider.                                                                                                                                    |
| links        | type [*required*]           | enum            | Link type. Allowed enum values: `doc,repo,runbook,dashboard,other`                                                                                |
| links        | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 2     | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2.1`                                                                                            |
| Option 2     | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 2     | team                             | string          | Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.                                                    |
| Option 2     | tier                             | string          | Importance of the service.                                                                                                                        |
|              | Option 3                         | object          | Service definition V2 for providing service metadata and integrations.                                                                            |
| Option 3     | contacts                         | [ <oneOf>] | A list of contacts related to the services.                                                                                                       |
| contacts     | Option 1                         | object          | Service owner's email.                                                                                                                            |
| Option 1     | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 1     | name                             | string          | Contact email.                                                                                                                                    |
| Option 1     | type [*required*]           | enum            | Contact type. Allowed enum values: `email`                                                                                                        |
| contacts     | Option 2                         | object          | Service owner's Slack channel.                                                                                                                    |
| Option 2     | contact [*required*]        | string          | Slack Channel.                                                                                                                                    |
| Option 2     | name                             | string          | Contact Slack.                                                                                                                                    |
| Option 2     | type [*required*]           | enum            | Contact type. Allowed enum values: `slack`                                                                                                        |
| contacts     | Option 3                         | object          | Service owner's Microsoft Teams.                                                                                                                  |
| Option 3     | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 3     | name                             | string          | Contact Microsoft Teams.                                                                                                                          |
| Option 3     | type [*required*]           | enum            | Contact type. Allowed enum values: `microsoft-teams`                                                                                              |
| Option 3     | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 3     | dd-team                          | string          | Experimental feature. A Team handle that matches a Team in the Datadog Teams product.                                                             |
| Option 3     | docs                             | [object]        | A list of documentation related to the services.                                                                                                  |
| docs         | name [*required*]           | string          | Document name.                                                                                                                                    |
| docs         | provider                         | string          | Document provider.                                                                                                                                |
| docs         | url [*required*]            | string          | Document URL.                                                                                                                                     |
| Option 3     | extensions                       | object          | Extensions to V2 schema.                                                                                                                          |
| Option 3     | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie     | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie     | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations | pagerduty                        | string          | PagerDuty service URL for the service.                                                                                                            |
| Option 3     | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links        | name [*required*]           | string          | Link name.                                                                                                                                        |
| links        | type [*required*]           | enum            | Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`                                                            |
| links        | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 3     | repos                            | [object]        | A list of code repositories related to the services.                                                                                              |
| repos        | name [*required*]           | string          | Repository name.                                                                                                                                  |
| repos        | provider                         | string          | Repository provider.                                                                                                                              |
| repos        | url [*required*]            | string          | Repository URL.                                                                                                                                   |
| Option 3     | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2`                                                                                              |
| Option 3     | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 3     | team                             | string          | Team that owns the service.                                                                                                                       |
|              | Option 4                         | string          | Service Definition in raw JSON/YAML representation.                                                                                               |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "dd-team": "my-team",
  "docs": [
    {
      "name": "Architecture",
      "provider": "google drive",
      "url": "https://gdrive/mydoc"
    }
  ],
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    }
  ],
  "repos": [
    {
      "name": "Source Code",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    }
  ],
  "schema-version": "v2",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
```

#####

```json
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": {
      "service-url": "https://my-org.pagerduty.com/service-directory/PMyService"
    }
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    },
    {
      "name": "Source Code",
      "type": "repo",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    },
    {
      "name": "Architecture",
      "type": "doc",
      "provider": "Gigoogle drivetHub",
      "url": "https://my-runbook"
    }
  ],
  "schema-version": "v2.1",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
```

#####

```json
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": {
      "service-url": "https://my-org.pagerduty.com/service-directory/PMyService"
    }
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    },
    {
      "name": "Source Code",
      "type": "repo",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    },
    {
      "name": "Architecture",
      "type": "doc",
      "provider": "Gigoogle drivetHub",
      "url": "https://my-runbook"
    }
  ],
  "schema-version": "v2.2",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
```

{% /tab %}

### Response

{% tab title="200" %}
CREATED
{% tab title="Model" %}
Create service definitions response.

| Parent field       | Field                            | Type            | Description                                                                                                                                       |
| ------------------ | -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                             | [object]        | Create service definitions response payload.                                                                                                      |
| data               | attributes                       | object          | Service definition attributes.                                                                                                                    |
| attributes         | meta                             | object          | Metadata about a service definition.                                                                                                              |
| meta               | github-html-url                  | string          | GitHub HTML URL.                                                                                                                                  |
| meta               | ingested-schema-version          | string          | Ingestion schema version.                                                                                                                         |
| meta               | ingestion-source                 | string          | Ingestion source of the service definition.                                                                                                       |
| meta               | last-modified-time               | string          | Last modified time of the service definition.                                                                                                     |
| meta               | origin                           | string          | User defined origin of the service definition.                                                                                                    |
| meta               | origin-detail                    | string          | User defined origin's detail of the service definition.                                                                                           |
| meta               | warnings                         | [object]        | A list of schema validation warnings.                                                                                                             |
| warnings           | instance-location                | string          | The warning instance location.                                                                                                                    |
| warnings           | keyword-location                 | string          | The warning keyword location.                                                                                                                     |
| warnings           | message                          | string          | The warning message.                                                                                                                              |
| attributes         | schema                           |  <oneOf>   | Service definition schema.                                                                                                                        |
| schema             | Option 1                         | object          | **DEPRECATED**: Deprecated - Service definition V1 for providing additional service metadata and integrations.                                    |
| Option 1           | contact                          | object          | Contact information about the service.                                                                                                            |
| contact            | email                            | string          | Service owner's email.                                                                                                                            |
| contact            | slack                            | string          | Service owner's Slack channel.                                                                                                                    |
| Option 1           | extensions                       | object          | Extensions to V1 schema.                                                                                                                          |
| Option 1           | external-resources               | [object]        | A list of external links related to the services.                                                                                                 |
| external-resources | name [*required*]           | string          | Link name.                                                                                                                                        |
| external-resources | type [*required*]           | enum            | Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`                                                            |
| external-resources | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 1           | info [*required*]           | object          | Basic information about a service.                                                                                                                |
| info               | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| info               | description                      | string          | A short description of the service.                                                                                                               |
| info               | display-name                     | string          | A friendly name of the service.                                                                                                                   |
| info               | service-tier                     | string          | Service tier.                                                                                                                                     |
| Option 1           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | pagerduty                        | string          | PagerDuty service URL for the service.                                                                                                            |
| Option 1           | org                              | object          | Org related information about the service.                                                                                                        |
| org                | application                      | string          | App feature this service supports.                                                                                                                |
| org                | team                             | string          | Team that owns the service.                                                                                                                       |
| Option 1           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v1`                                                                                              |
| Option 1           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| schema             | Option 2                         | object          | Service definition V2 for providing service metadata and integrations.                                                                            |
| Option 2           | contacts                         | [ <oneOf>] | A list of contacts related to the services.                                                                                                       |
| contacts           | Option 1                         | object          | Service owner's email.                                                                                                                            |
| Option 1           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 1           | name                             | string          | Contact email.                                                                                                                                    |
| Option 1           | type [*required*]           | enum            | Contact type. Allowed enum values: `email`                                                                                                        |
| contacts           | Option 2                         | object          | Service owner's Slack channel.                                                                                                                    |
| Option 2           | contact [*required*]        | string          | Slack Channel.                                                                                                                                    |
| Option 2           | name                             | string          | Contact Slack.                                                                                                                                    |
| Option 2           | type [*required*]           | enum            | Contact type. Allowed enum values: `slack`                                                                                                        |
| contacts           | Option 3                         | object          | Service owner's Microsoft Teams.                                                                                                                  |
| Option 3           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 3           | name                             | string          | Contact Microsoft Teams.                                                                                                                          |
| Option 3           | type [*required*]           | enum            | Contact type. Allowed enum values: `microsoft-teams`                                                                                              |
| Option 2           | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 2           | dd-team                          | string          | Experimental feature. A Team handle that matches a Team in the Datadog Teams product.                                                             |
| Option 2           | docs                             | [object]        | A list of documentation related to the services.                                                                                                  |
| docs               | name [*required*]           | string          | Document name.                                                                                                                                    |
| docs               | provider                         | string          | Document provider.                                                                                                                                |
| docs               | url [*required*]            | string          | Document URL.                                                                                                                                     |
| Option 2           | extensions                       | object          | Extensions to V2 schema.                                                                                                                          |
| Option 2           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie           | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie           | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations       | pagerduty                        | string          | PagerDuty service URL for the service.                                                                                                            |
| Option 2           | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links              | name [*required*]           | string          | Link name.                                                                                                                                        |
| links              | type [*required*]           | enum            | Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`                                                            |
| links              | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 2           | repos                            | [object]        | A list of code repositories related to the services.                                                                                              |
| repos              | name [*required*]           | string          | Repository name.                                                                                                                                  |
| repos              | provider                         | string          | Repository provider.                                                                                                                              |
| repos              | url [*required*]            | string          | Repository URL.                                                                                                                                   |
| Option 2           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2`                                                                                              |
| Option 2           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 2           | team                             | string          | Team that owns the service.                                                                                                                       |
| schema             | Option 3                         | object          | Service definition v2.1 for providing service metadata and integrations.                                                                          |
| Option 3           | application                      | string          | Identifier for a group of related services serving a product feature, which the service is a part of.                                             |
| Option 3           | contacts                         | [ <oneOf>] | A list of contacts related to the services.                                                                                                       |
| contacts           | Option 1                         | object          | Service owner's email.                                                                                                                            |
| Option 1           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 1           | name                             | string          | Contact email.                                                                                                                                    |
| Option 1           | type [*required*]           | enum            | Contact type. Allowed enum values: `email`                                                                                                        |
| contacts           | Option 2                         | object          | Service owner's Slack channel.                                                                                                                    |
| Option 2           | contact [*required*]        | string          | Slack Channel.                                                                                                                                    |
| Option 2           | name                             | string          | Contact Slack.                                                                                                                                    |
| Option 2           | type [*required*]           | enum            | Contact type. Allowed enum values: `slack`                                                                                                        |
| contacts           | Option 3                         | object          | Service owner's Microsoft Teams.                                                                                                                  |
| Option 3           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 3           | name                             | string          | Contact Microsoft Teams.                                                                                                                          |
| Option 3           | type [*required*]           | enum            | Contact type. Allowed enum values: `microsoft-teams`                                                                                              |
| Option 3           | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 3           | description                      | string          | A short description of the service.                                                                                                               |
| Option 3           | extensions                       | object          | Extensions to v2.1 schema.                                                                                                                        |
| Option 3           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie           | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie           | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations       | pagerduty                        | object          | PagerDuty integration for the service.                                                                                                            |
| pagerduty          | service-url                      | string          | PagerDuty service url.                                                                                                                            |
| Option 3           | lifecycle                        | string          | The current life cycle phase of the service.                                                                                                      |
| Option 3           | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links              | name [*required*]           | string          | Link name.                                                                                                                                        |
| links              | provider                         | string          | Link provider.                                                                                                                                    |
| links              | type [*required*]           | enum            | Link type. Allowed enum values: `doc,repo,runbook,dashboard,other`                                                                                |
| links              | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 3           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2.1`                                                                                            |
| Option 3           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 3           | team                             | string          | Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.                                                    |
| Option 3           | tier                             | string          | Importance of the service.                                                                                                                        |
| schema             | Option 4                         | object          | Service definition v2.2 for providing service metadata and integrations.                                                                          |
| Option 4           | application                      | string          | Identifier for a group of related services serving a product feature, which the service is a part of.                                             |
| Option 4           | ci-pipeline-fingerprints         | [string]        | A set of CI fingerprints.                                                                                                                         |
| Option 4           | contacts                         | [object]        | A list of contacts related to the services.                                                                                                       |
| contacts           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| contacts           | name                             | string          | Contact Name.                                                                                                                                     |
| contacts           | type [*required*]           | string          | Contact type. Datadog recognizes the following types: `email`, `slack`, and `microsoft-teams`.                                                    |
| Option 4           | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 4           | description                      | string          | A short description of the service.                                                                                                               |
| Option 4           | extensions                       | object          | Extensions to v2.2 schema.                                                                                                                        |
| Option 4           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie           | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie           | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations       | pagerduty                        | object          | PagerDuty integration for the service.                                                                                                            |
| pagerduty          | service-url                      | string          | PagerDuty service url.                                                                                                                            |
| Option 4           | languages                        | [string]        | The service's programming language. Datadog recognizes the following languages: `dotnet`, `go`, `java`, `js`, `php`, `python`, `ruby`, and `c++`. |
| Option 4           | lifecycle                        | string          | The current life cycle phase of the service.                                                                                                      |
| Option 4           | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links              | name [*required*]           | string          | Link name.                                                                                                                                        |
| links              | provider                         | string          | Link provider.                                                                                                                                    |
| links              | type [*required*]           | string          | Link type. Datadog recognizes the following types: `runbook`, `doc`, `repo`, `dashboard`, and `other`.                                            |
| links              | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 4           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2.2`                                                                                            |
| Option 4           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 4           | team                             | string          | Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.                                                    |
| Option 4           | tier                             | string          | Importance of the service.                                                                                                                        |
| Option 4           | type                             | string          | The type of service.                                                                                                                              |
| data               | id                               | string          | Service definition id.                                                                                                                            |
| data               | type                             | string          | Service definition type.                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "meta": {
          "github-html-url": "string",
          "ingested-schema-version": "string",
          "ingestion-source": "string",
          "last-modified-time": "string",
          "origin": "string",
          "origin-detail": "string",
          "warnings": [
            {
              "instance-location": "string",
              "keyword-location": "string",
              "message": "string"
            }
          ]
        },
        "schema": {
          "contact": {
            "email": "contact@datadoghq.com",
            "slack": "https://yourcompany.slack.com/archives/channel123"
          },
          "extensions": {
            "myorg/extension": "extensionValue"
          },
          "external-resources": [
            {
              "name": "Runbook",
              "type": "runbook",
              "url": "https://my-runbook"
            }
          ],
          "info": {
            "dd-service": "myservice",
            "description": "A shopping cart service",
            "display-name": "My Service",
            "service-tier": "Tier 1"
          },
          "integrations": {
            "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"
          },
          "org": {
            "application": "E-Commerce",
            "team": "my-team"
          },
          "schema-version": "v1",
          "tags": [
            "my:tag",
            "service:tag"
          ]
        }
      },
      "id": "string",
      "type": "string"
    }
  ]
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

{% tab title="409" %}
Conflict
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "dd-team": "my-team",
  "docs": [
    {
      "name": "Architecture",
      "provider": "google drive",
      "url": "https://gdrive/mydoc"
    }
  ],
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    }
  ],
  "repos": [
    {
      "name": "Source Code",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    }
  ],
  "schema-version": "v2",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": {
      "service-url": "https://my-org.pagerduty.com/service-directory/PMyService"
    }
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    },
    {
      "name": "Source Code",
      "type": "repo",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    },
    {
      "name": "Architecture",
      "type": "doc",
      "provider": "Gigoogle drivetHub",
      "url": "https://my-runbook"
    }
  ],
  "schema-version": "v2.1",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "contacts": [
    {
      "contact": "contact@datadoghq.com",
      "name": "Team Email",
      "type": "email"
    }
  ],
  "dd-service": "service-exampleservicedefinition",
  "extensions": {
    "myorgextension": "extensionvalue"
  },
  "integrations": {
    "opsgenie": {
      "region": "US",
      "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
    },
    "pagerduty": {
      "service-url": "https://my-org.pagerduty.com/service-directory/PMyService"
    }
  },
  "links": [
    {
      "name": "Runbook",
      "type": "runbook",
      "url": "https://my-runbook"
    },
    {
      "name": "Source Code",
      "type": "repo",
      "provider": "GitHub",
      "url": "https://github.com/DataDog/schema"
    },
    {
      "name": "Architecture",
      "type": "doc",
      "provider": "Gigoogle drivetHub",
      "url": "https://my-runbook"
    }
  ],
  "schema-version": "v2.2",
  "tags": [
    "my:tag",
    "service:tag"
  ],
  "team": "my-team"
}
EOF

#####

```go
// Create or update service definition using schema v2 returns "CREATED" response

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
    body := datadogV2.ServiceDefinitionsCreateRequest{
        ServiceDefinitionV2: &datadogV2.ServiceDefinitionV2{
            Contacts: []datadogV2.ServiceDefinitionV2Contact{
                datadogV2.ServiceDefinitionV2Contact{
                    ServiceDefinitionV2Email: &datadogV2.ServiceDefinitionV2Email{
                        Contact: "contact@datadoghq.com",
                        Name:    datadog.PtrString("Team Email"),
                        Type:    datadogV2.SERVICEDEFINITIONV2EMAILTYPE_EMAIL,
                    }},
            },
            DdService: "service-exampleservicedefinition",
            DdTeam:    datadog.PtrString("my-team"),
            Docs: []datadogV2.ServiceDefinitionV2Doc{
                {
                    Name:     "Architecture",
                    Provider: datadog.PtrString("google drive"),
                    Url:      "https://gdrive/mydoc",
                },
            },
            Extensions: map[string]interface{}{
                "myorgextension": "extensionvalue",
            },
            Integrations: &datadogV2.ServiceDefinitionV2Integrations{
                Opsgenie: &datadogV2.ServiceDefinitionV2Opsgenie{
                    Region:     datadogV2.SERVICEDEFINITIONV2OPSGENIEREGION_US.Ptr(),
                    ServiceUrl: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
                },
                Pagerduty: datadog.PtrString("https://my-org.pagerduty.com/service-directory/PMyService"),
            },
            Links: []datadogV2.ServiceDefinitionV2Link{
                {
                    Name: "Runbook",
                    Type: datadogV2.SERVICEDEFINITIONV2LINKTYPE_RUNBOOK,
                    Url:  "https://my-runbook",
                },
            },
            Repos: []datadogV2.ServiceDefinitionV2Repo{
                {
                    Name:     "Source Code",
                    Provider: datadog.PtrString("GitHub"),
                    Url:      "https://github.com/DataDog/schema",
                },
            },
            SchemaVersion: datadogV2.SERVICEDEFINITIONV2VERSION_V2,
            Tags: []string{
                "my:tag",
                "service:tag",
            },
            Team: datadog.PtrString("my-team"),
        }}
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceDefinitionApi(apiClient)
    resp, r, err := api.CreateOrUpdateServiceDefinitions(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`:\n%s\n", responseContent)
}
```

#####

```go
// Create or update service definition using schema v2-1 returns "CREATED" response

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
    body := datadogV2.ServiceDefinitionsCreateRequest{
        ServiceDefinitionV2Dot1: &datadogV2.ServiceDefinitionV2Dot1{
            Contacts: []datadogV2.ServiceDefinitionV2Dot1Contact{
                datadogV2.ServiceDefinitionV2Dot1Contact{
                    ServiceDefinitionV2Dot1Email: &datadogV2.ServiceDefinitionV2Dot1Email{
                        Contact: "contact@datadoghq.com",
                        Name:    datadog.PtrString("Team Email"),
                        Type:    datadogV2.SERVICEDEFINITIONV2DOT1EMAILTYPE_EMAIL,
                    }},
            },
            DdService: "service-exampleservicedefinition",
            Extensions: map[string]interface{}{
                "myorgextension": "extensionvalue",
            },
            Integrations: &datadogV2.ServiceDefinitionV2Dot1Integrations{
                Opsgenie: &datadogV2.ServiceDefinitionV2Dot1Opsgenie{
                    Region:     datadogV2.SERVICEDEFINITIONV2DOT1OPSGENIEREGION_US.Ptr(),
                    ServiceUrl: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
                },
                Pagerduty: &datadogV2.ServiceDefinitionV2Dot1Pagerduty{
                    ServiceUrl: datadog.PtrString("https://my-org.pagerduty.com/service-directory/PMyService"),
                },
            },
            Links: []datadogV2.ServiceDefinitionV2Dot1Link{
                {
                    Name: "Runbook",
                    Type: datadogV2.SERVICEDEFINITIONV2DOT1LINKTYPE_RUNBOOK,
                    Url:  "https://my-runbook",
                },
                {
                    Name:     "Source Code",
                    Type:     datadogV2.SERVICEDEFINITIONV2DOT1LINKTYPE_REPO,
                    Provider: datadog.PtrString("GitHub"),
                    Url:      "https://github.com/DataDog/schema",
                },
                {
                    Name:     "Architecture",
                    Type:     datadogV2.SERVICEDEFINITIONV2DOT1LINKTYPE_DOC,
                    Provider: datadog.PtrString("Gigoogle drivetHub"),
                    Url:      "https://my-runbook",
                },
            },
            SchemaVersion: datadogV2.SERVICEDEFINITIONV2DOT1VERSION_V2_1,
            Tags: []string{
                "my:tag",
                "service:tag",
            },
            Team: datadog.PtrString("my-team"),
        }}
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceDefinitionApi(apiClient)
    resp, r, err := api.CreateOrUpdateServiceDefinitions(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`:\n%s\n", responseContent)
}
```

#####

```go
// Create or update service definition using schema v2-2 returns "CREATED" response

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
    body := datadogV2.ServiceDefinitionsCreateRequest{
        ServiceDefinitionV2Dot2: &datadogV2.ServiceDefinitionV2Dot2{
            Contacts: []datadogV2.ServiceDefinitionV2Dot2Contact{
                {
                    Contact: "contact@datadoghq.com",
                    Name:    datadog.PtrString("Team Email"),
                    Type:    "email",
                },
            },
            DdService: "service-exampleservicedefinition",
            Extensions: map[string]interface{}{
                "myorgextension": "extensionvalue",
            },
            Integrations: &datadogV2.ServiceDefinitionV2Dot2Integrations{
                Opsgenie: &datadogV2.ServiceDefinitionV2Dot2Opsgenie{
                    Region:     datadogV2.SERVICEDEFINITIONV2DOT2OPSGENIEREGION_US.Ptr(),
                    ServiceUrl: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
                },
                Pagerduty: &datadogV2.ServiceDefinitionV2Dot2Pagerduty{
                    ServiceUrl: datadog.PtrString("https://my-org.pagerduty.com/service-directory/PMyService"),
                },
            },
            Links: []datadogV2.ServiceDefinitionV2Dot2Link{
                {
                    Name: "Runbook",
                    Type: "runbook",
                    Url:  "https://my-runbook",
                },
                {
                    Name:     "Source Code",
                    Type:     "repo",
                    Provider: datadog.PtrString("GitHub"),
                    Url:      "https://github.com/DataDog/schema",
                },
                {
                    Name:     "Architecture",
                    Type:     "doc",
                    Provider: datadog.PtrString("Gigoogle drivetHub"),
                    Url:      "https://my-runbook",
                },
            },
            SchemaVersion: datadogV2.SERVICEDEFINITIONV2DOT2VERSION_V2_2,
            Tags: []string{
                "my:tag",
                "service:tag",
            },
            Team: datadog.PtrString("my-team"),
        }}
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceDefinitionApi(apiClient)
    resp, r, err := api.CreateOrUpdateServiceDefinitions(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceDefinitionApi.CreateOrUpdateServiceDefinitions`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create or update service definition using schema v2 returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;
import com.datadog.api.client.v2.model.ServiceDefinitionCreateResponse;
import com.datadog.api.client.v2.model.ServiceDefinitionV2;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Contact;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Doc;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Email;
import com.datadog.api.client.v2.model.ServiceDefinitionV2EmailType;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Integrations;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Link;
import com.datadog.api.client.v2.model.ServiceDefinitionV2LinkType;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Opsgenie;
import com.datadog.api.client.v2.model.ServiceDefinitionV2OpsgenieRegion;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Repo;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Version;
import com.datadog.api.client.v2.model.ServiceDefinitionsCreateRequest;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    ServiceDefinitionsCreateRequest body =
        new ServiceDefinitionsCreateRequest(
            new ServiceDefinitionV2()
                .contacts(
                    Collections.singletonList(
                        new ServiceDefinitionV2Contact(
                            new ServiceDefinitionV2Email()
                                .contact("contact@datadoghq.com")
                                .name("Team Email")
                                .type(ServiceDefinitionV2EmailType.EMAIL))))
                .ddService("service-exampleservicedefinition")
                .ddTeam("my-team")
                .docs(
                    Collections.singletonList(
                        new ServiceDefinitionV2Doc()
                            .name("Architecture")
                            .provider("google drive")
                            .url("https://gdrive/mydoc")))
                .extensions(Map.ofEntries(Map.entry("myorgextension", "extensionvalue")))
                .integrations(
                    new ServiceDefinitionV2Integrations()
                        .opsgenie(
                            new ServiceDefinitionV2Opsgenie()
                                .region(ServiceDefinitionV2OpsgenieRegion.US)
                                .serviceUrl(
                                    "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"))
                        .pagerduty("https://my-org.pagerduty.com/service-directory/PMyService"))
                .links(
                    Collections.singletonList(
                        new ServiceDefinitionV2Link()
                            .name("Runbook")
                            .type(ServiceDefinitionV2LinkType.RUNBOOK)
                            .url("https://my-runbook")))
                .repos(
                    Collections.singletonList(
                        new ServiceDefinitionV2Repo()
                            .name("Source Code")
                            .provider("GitHub")
                            .url("https://github.com/DataDog/schema")))
                .schemaVersion(ServiceDefinitionV2Version.V2)
                .tags(Arrays.asList("my:tag", "service:tag"))
                .team("my-team"));

    try {
      ServiceDefinitionCreateResponse result = apiInstance.createOrUpdateServiceDefinitions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceDefinitionApi#createOrUpdateServiceDefinitions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#####

```java
// Create or update service definition using schema v2-1 returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;
import com.datadog.api.client.v2.model.ServiceDefinitionCreateResponse;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Contact;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Email;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1EmailType;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Integrations;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Link;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1LinkType;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Opsgenie;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1OpsgenieRegion;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Pagerduty;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot1Version;
import com.datadog.api.client.v2.model.ServiceDefinitionsCreateRequest;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    ServiceDefinitionsCreateRequest body =
        new ServiceDefinitionsCreateRequest(
            new ServiceDefinitionV2Dot1()
                .contacts(
                    Collections.singletonList(
                        new ServiceDefinitionV2Dot1Contact(
                            new ServiceDefinitionV2Dot1Email()
                                .contact("contact@datadoghq.com")
                                .name("Team Email")
                                .type(ServiceDefinitionV2Dot1EmailType.EMAIL))))
                .ddService("service-exampleservicedefinition")
                .extensions(Map.ofEntries(Map.entry("myorgextension", "extensionvalue")))
                .integrations(
                    new ServiceDefinitionV2Dot1Integrations()
                        .opsgenie(
                            new ServiceDefinitionV2Dot1Opsgenie()
                                .region(ServiceDefinitionV2Dot1OpsgenieRegion.US)
                                .serviceUrl(
                                    "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"))
                        .pagerduty(
                            new ServiceDefinitionV2Dot1Pagerduty()
                                .serviceUrl(
                                    "https://my-org.pagerduty.com/service-directory/PMyService")))
                .links(
                    Arrays.asList(
                        new ServiceDefinitionV2Dot1Link()
                            .name("Runbook")
                            .type(ServiceDefinitionV2Dot1LinkType.RUNBOOK)
                            .url("https://my-runbook"),
                        new ServiceDefinitionV2Dot1Link()
                            .name("Source Code")
                            .type(ServiceDefinitionV2Dot1LinkType.REPO)
                            .provider("GitHub")
                            .url("https://github.com/DataDog/schema"),
                        new ServiceDefinitionV2Dot1Link()
                            .name("Architecture")
                            .type(ServiceDefinitionV2Dot1LinkType.DOC)
                            .provider("Gigoogle drivetHub")
                            .url("https://my-runbook")))
                .schemaVersion(ServiceDefinitionV2Dot1Version.V2_1)
                .tags(Arrays.asList("my:tag", "service:tag"))
                .team("my-team"));

    try {
      ServiceDefinitionCreateResponse result = apiInstance.createOrUpdateServiceDefinitions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceDefinitionApi#createOrUpdateServiceDefinitions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#####

```java
// Create or update service definition using schema v2-2 returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;
import com.datadog.api.client.v2.model.ServiceDefinitionCreateResponse;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Contact;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Integrations;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Link;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Opsgenie;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2OpsgenieRegion;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Pagerduty;
import com.datadog.api.client.v2.model.ServiceDefinitionV2Dot2Version;
import com.datadog.api.client.v2.model.ServiceDefinitionsCreateRequest;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    ServiceDefinitionsCreateRequest body =
        new ServiceDefinitionsCreateRequest(
            new ServiceDefinitionV2Dot2()
                .contacts(
                    Collections.singletonList(
                        new ServiceDefinitionV2Dot2Contact()
                            .contact("contact@datadoghq.com")
                            .name("Team Email")
                            .type("email")))
                .ddService("service-exampleservicedefinition")
                .extensions(Map.ofEntries(Map.entry("myorgextension", "extensionvalue")))
                .integrations(
                    new ServiceDefinitionV2Dot2Integrations()
                        .opsgenie(
                            new ServiceDefinitionV2Dot2Opsgenie()
                                .region(ServiceDefinitionV2Dot2OpsgenieRegion.US)
                                .serviceUrl(
                                    "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"))
                        .pagerduty(
                            new ServiceDefinitionV2Dot2Pagerduty()
                                .serviceUrl(
                                    "https://my-org.pagerduty.com/service-directory/PMyService")))
                .links(
                    Arrays.asList(
                        new ServiceDefinitionV2Dot2Link()
                            .name("Runbook")
                            .type("runbook")
                            .url("https://my-runbook"),
                        new ServiceDefinitionV2Dot2Link()
                            .name("Source Code")
                            .type("repo")
                            .provider("GitHub")
                            .url("https://github.com/DataDog/schema"),
                        new ServiceDefinitionV2Dot2Link()
                            .name("Architecture")
                            .type("doc")
                            .provider("Gigoogle drivetHub")
                            .url("https://my-runbook")))
                .schemaVersion(ServiceDefinitionV2Dot2Version.V2_2)
                .tags(Arrays.asList("my:tag", "service:tag"))
                .team("my-team"));

    try {
      ServiceDefinitionCreateResponse result = apiInstance.createOrUpdateServiceDefinitions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling ServiceDefinitionApi#createOrUpdateServiceDefinitions");
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
Create or update service definition using schema v2 returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_v2 import ServiceDefinitionV2
from datadog_api_client.v2.model.service_definition_v2_doc import ServiceDefinitionV2Doc
from datadog_api_client.v2.model.service_definition_v2_email import ServiceDefinitionV2Email
from datadog_api_client.v2.model.service_definition_v2_email_type import ServiceDefinitionV2EmailType
from datadog_api_client.v2.model.service_definition_v2_integrations import ServiceDefinitionV2Integrations
from datadog_api_client.v2.model.service_definition_v2_link import ServiceDefinitionV2Link
from datadog_api_client.v2.model.service_definition_v2_link_type import ServiceDefinitionV2LinkType
from datadog_api_client.v2.model.service_definition_v2_opsgenie import ServiceDefinitionV2Opsgenie
from datadog_api_client.v2.model.service_definition_v2_opsgenie_region import ServiceDefinitionV2OpsgenieRegion
from datadog_api_client.v2.model.service_definition_v2_repo import ServiceDefinitionV2Repo
from datadog_api_client.v2.model.service_definition_v2_version import ServiceDefinitionV2Version

body = ServiceDefinitionV2(
    contacts=[
        ServiceDefinitionV2Email(
            contact="contact@datadoghq.com",
            name="Team Email",
            type=ServiceDefinitionV2EmailType.EMAIL,
        ),
    ],
    dd_service="service-exampleservicedefinition",
    dd_team="my-team",
    docs=[
        ServiceDefinitionV2Doc(
            name="Architecture",
            provider="google drive",
            url="https://gdrive/mydoc",
        ),
    ],
    extensions=dict([("myorgextension", "extensionvalue")]),
    integrations=ServiceDefinitionV2Integrations(
        opsgenie=ServiceDefinitionV2Opsgenie(
            region=ServiceDefinitionV2OpsgenieRegion.US,
            service_url="https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
        ),
        pagerduty="https://my-org.pagerduty.com/service-directory/PMyService",
    ),
    links=[
        ServiceDefinitionV2Link(
            name="Runbook",
            type=ServiceDefinitionV2LinkType.RUNBOOK,
            url="https://my-runbook",
        ),
    ],
    repos=[
        ServiceDefinitionV2Repo(
            name="Source Code",
            provider="GitHub",
            url="https://github.com/DataDog/schema",
        ),
    ],
    schema_version=ServiceDefinitionV2Version.V2,
    tags=[
        "my:tag",
        "service:tag",
    ],
    team="my-team",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.create_or_update_service_definitions(body=body)

    print(response)
```

#####

```python
"""
Create or update service definition using schema v2-1 returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_v2_dot1 import ServiceDefinitionV2Dot1
from datadog_api_client.v2.model.service_definition_v2_dot1_email import ServiceDefinitionV2Dot1Email
from datadog_api_client.v2.model.service_definition_v2_dot1_email_type import ServiceDefinitionV2Dot1EmailType
from datadog_api_client.v2.model.service_definition_v2_dot1_integrations import ServiceDefinitionV2Dot1Integrations
from datadog_api_client.v2.model.service_definition_v2_dot1_link import ServiceDefinitionV2Dot1Link
from datadog_api_client.v2.model.service_definition_v2_dot1_link_type import ServiceDefinitionV2Dot1LinkType
from datadog_api_client.v2.model.service_definition_v2_dot1_opsgenie import ServiceDefinitionV2Dot1Opsgenie
from datadog_api_client.v2.model.service_definition_v2_dot1_opsgenie_region import ServiceDefinitionV2Dot1OpsgenieRegion
from datadog_api_client.v2.model.service_definition_v2_dot1_pagerduty import ServiceDefinitionV2Dot1Pagerduty
from datadog_api_client.v2.model.service_definition_v2_dot1_version import ServiceDefinitionV2Dot1Version

body = ServiceDefinitionV2Dot1(
    contacts=[
        ServiceDefinitionV2Dot1Email(
            contact="contact@datadoghq.com",
            name="Team Email",
            type=ServiceDefinitionV2Dot1EmailType.EMAIL,
        ),
    ],
    dd_service="service-exampleservicedefinition",
    extensions=dict([("myorgextension", "extensionvalue")]),
    integrations=ServiceDefinitionV2Dot1Integrations(
        opsgenie=ServiceDefinitionV2Dot1Opsgenie(
            region=ServiceDefinitionV2Dot1OpsgenieRegion.US,
            service_url="https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
        ),
        pagerduty=ServiceDefinitionV2Dot1Pagerduty(
            service_url="https://my-org.pagerduty.com/service-directory/PMyService",
        ),
    ),
    links=[
        ServiceDefinitionV2Dot1Link(
            name="Runbook",
            type=ServiceDefinitionV2Dot1LinkType.RUNBOOK,
            url="https://my-runbook",
        ),
        ServiceDefinitionV2Dot1Link(
            name="Source Code",
            type=ServiceDefinitionV2Dot1LinkType.REPO,
            provider="GitHub",
            url="https://github.com/DataDog/schema",
        ),
        ServiceDefinitionV2Dot1Link(
            name="Architecture",
            type=ServiceDefinitionV2Dot1LinkType.DOC,
            provider="Gigoogle drivetHub",
            url="https://my-runbook",
        ),
    ],
    schema_version=ServiceDefinitionV2Dot1Version.V2_1,
    tags=[
        "my:tag",
        "service:tag",
    ],
    team="my-team",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.create_or_update_service_definitions(body=body)

    print(response)
```

#####

```python
"""
Create or update service definition using schema v2-2 returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_v2_dot2 import ServiceDefinitionV2Dot2
from datadog_api_client.v2.model.service_definition_v2_dot2_contact import ServiceDefinitionV2Dot2Contact
from datadog_api_client.v2.model.service_definition_v2_dot2_integrations import ServiceDefinitionV2Dot2Integrations
from datadog_api_client.v2.model.service_definition_v2_dot2_link import ServiceDefinitionV2Dot2Link
from datadog_api_client.v2.model.service_definition_v2_dot2_opsgenie import ServiceDefinitionV2Dot2Opsgenie
from datadog_api_client.v2.model.service_definition_v2_dot2_opsgenie_region import ServiceDefinitionV2Dot2OpsgenieRegion
from datadog_api_client.v2.model.service_definition_v2_dot2_pagerduty import ServiceDefinitionV2Dot2Pagerduty
from datadog_api_client.v2.model.service_definition_v2_dot2_version import ServiceDefinitionV2Dot2Version

body = ServiceDefinitionV2Dot2(
    contacts=[
        ServiceDefinitionV2Dot2Contact(
            contact="contact@datadoghq.com",
            name="Team Email",
            type="email",
        ),
    ],
    dd_service="service-exampleservicedefinition",
    extensions=dict([("myorgextension", "extensionvalue")]),
    integrations=ServiceDefinitionV2Dot2Integrations(
        opsgenie=ServiceDefinitionV2Dot2Opsgenie(
            region=ServiceDefinitionV2Dot2OpsgenieRegion.US,
            service_url="https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
        ),
        pagerduty=ServiceDefinitionV2Dot2Pagerduty(
            service_url="https://my-org.pagerduty.com/service-directory/PMyService",
        ),
    ),
    links=[
        ServiceDefinitionV2Dot2Link(
            name="Runbook",
            type="runbook",
            url="https://my-runbook",
        ),
        ServiceDefinitionV2Dot2Link(
            name="Source Code",
            type="repo",
            provider="GitHub",
            url="https://github.com/DataDog/schema",
        ),
        ServiceDefinitionV2Dot2Link(
            name="Architecture",
            type="doc",
            provider="Gigoogle drivetHub",
            url="https://my-runbook",
        ),
    ],
    schema_version=ServiceDefinitionV2Dot2Version.V2_2,
    tags=[
        "my:tag",
        "service:tag",
    ],
    team="my-team",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.create_or_update_service_definitions(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create or update service definition using schema v2 returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new

body = DatadogAPIClient::V2::ServiceDefinitionV2.new({
  contacts: [
    DatadogAPIClient::V2::ServiceDefinitionV2Email.new({
      contact: "contact@datadoghq.com",
      name: "Team Email",
      type: DatadogAPIClient::V2::ServiceDefinitionV2EmailType::EMAIL,
    }),
  ],
  dd_service: "service-exampleservicedefinition",
  dd_team: "my-team",
  docs: [
    DatadogAPIClient::V2::ServiceDefinitionV2Doc.new({
      name: "Architecture",
      provider: "google drive",
      url: "https://gdrive/mydoc",
    }),
  ],
  extensions: {
    "myorgextension": "extensionvalue",
  },
  integrations: DatadogAPIClient::V2::ServiceDefinitionV2Integrations.new({
    opsgenie: DatadogAPIClient::V2::ServiceDefinitionV2Opsgenie.new({
      region: DatadogAPIClient::V2::ServiceDefinitionV2OpsgenieRegion::US,
      service_url: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
    }),
    pagerduty: "https://my-org.pagerduty.com/service-directory/PMyService",
  }),
  links: [
    DatadogAPIClient::V2::ServiceDefinitionV2Link.new({
      name: "Runbook",
      type: DatadogAPIClient::V2::ServiceDefinitionV2LinkType::RUNBOOK,
      url: "https://my-runbook",
    }),
  ],
  repos: [
    DatadogAPIClient::V2::ServiceDefinitionV2Repo.new({
      name: "Source Code",
      provider: "GitHub",
      url: "https://github.com/DataDog/schema",
    }),
  ],
  schema_version: DatadogAPIClient::V2::ServiceDefinitionV2Version::V2,
  tags: [
    "my:tag",
    "service:tag",
  ],
  team: "my-team",
})
p api_instance.create_or_update_service_definitions(body)
```

#####

```ruby
# Create or update service definition using schema v2-1 returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new

body = DatadogAPIClient::V2::ServiceDefinitionV2Dot1.new({
  contacts: [
    DatadogAPIClient::V2::ServiceDefinitionV2Dot1Email.new({
      contact: "contact@datadoghq.com",
      name: "Team Email",
      type: DatadogAPIClient::V2::ServiceDefinitionV2Dot1EmailType::EMAIL,
    }),
  ],
  dd_service: "service-exampleservicedefinition",
  extensions: {
    "myorgextension": "extensionvalue",
  },
  integrations: DatadogAPIClient::V2::ServiceDefinitionV2Dot1Integrations.new({
    opsgenie: DatadogAPIClient::V2::ServiceDefinitionV2Dot1Opsgenie.new({
      region: DatadogAPIClient::V2::ServiceDefinitionV2Dot1OpsgenieRegion::US,
      service_url: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
    }),
    pagerduty: DatadogAPIClient::V2::ServiceDefinitionV2Dot1Pagerduty.new({
      service_url: "https://my-org.pagerduty.com/service-directory/PMyService",
    }),
  }),
  links: [
    DatadogAPIClient::V2::ServiceDefinitionV2Dot1Link.new({
      name: "Runbook",
      type: DatadogAPIClient::V2::ServiceDefinitionV2Dot1LinkType::RUNBOOK,
      url: "https://my-runbook",
    }),
    DatadogAPIClient::V2::ServiceDefinitionV2Dot1Link.new({
      name: "Source Code",
      type: DatadogAPIClient::V2::ServiceDefinitionV2Dot1LinkType::REPO,
      provider: "GitHub",
      url: "https://github.com/DataDog/schema",
    }),
    DatadogAPIClient::V2::ServiceDefinitionV2Dot1Link.new({
      name: "Architecture",
      type: DatadogAPIClient::V2::ServiceDefinitionV2Dot1LinkType::DOC,
      provider: "Gigoogle drivetHub",
      url: "https://my-runbook",
    }),
  ],
  schema_version: DatadogAPIClient::V2::ServiceDefinitionV2Dot1Version::V2_1,
  tags: [
    "my:tag",
    "service:tag",
  ],
  team: "my-team",
})
p api_instance.create_or_update_service_definitions(body)
```

#####

```ruby
# Create or update service definition using schema v2-2 returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new

body = DatadogAPIClient::V2::ServiceDefinitionV2Dot2.new({
  contacts: [
    DatadogAPIClient::V2::ServiceDefinitionV2Dot2Contact.new({
      contact: "contact@datadoghq.com",
      name: "Team Email",
      type: "email",
    }),
  ],
  dd_service: "service-exampleservicedefinition",
  extensions: {
    "myorgextension": "extensionvalue",
  },
  integrations: DatadogAPIClient::V2::ServiceDefinitionV2Dot2Integrations.new({
    opsgenie: DatadogAPIClient::V2::ServiceDefinitionV2Dot2Opsgenie.new({
      region: DatadogAPIClient::V2::ServiceDefinitionV2Dot2OpsgenieRegion::US,
      service_url: "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
    }),
    pagerduty: DatadogAPIClient::V2::ServiceDefinitionV2Dot2Pagerduty.new({
      service_url: "https://my-org.pagerduty.com/service-directory/PMyService",
    }),
  }),
  links: [
    DatadogAPIClient::V2::ServiceDefinitionV2Dot2Link.new({
      name: "Runbook",
      type: "runbook",
      url: "https://my-runbook",
    }),
    DatadogAPIClient::V2::ServiceDefinitionV2Dot2Link.new({
      name: "Source Code",
      type: "repo",
      provider: "GitHub",
      url: "https://github.com/DataDog/schema",
    }),
    DatadogAPIClient::V2::ServiceDefinitionV2Dot2Link.new({
      name: "Architecture",
      type: "doc",
      provider: "Gigoogle drivetHub",
      url: "https://my-runbook",
    }),
  ],
  schema_version: DatadogAPIClient::V2::ServiceDefinitionV2Dot2Version::V2_2,
  tags: [
    "my:tag",
    "service:tag",
  ],
  team: "my-team",
})
p api_instance.create_or_update_service_definitions(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create or update service definition using schema v2 returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Contact;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Doc;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Email;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2EmailType;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Integrations;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Link;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2LinkType;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Opsgenie;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2OpsgenieRegion;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Repo;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Version;
use datadog_api_client::datadogV2::model::ServiceDefinitionsCreateRequest;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = ServiceDefinitionsCreateRequest::ServiceDefinitionV2(Box::new(
        ServiceDefinitionV2::new(
            "service-exampleservicedefinition".to_string(),
            ServiceDefinitionV2Version::V2,
        )
        .contacts(vec![ServiceDefinitionV2Contact::ServiceDefinitionV2Email(
            Box::new(
                ServiceDefinitionV2Email::new(
                    "contact@datadoghq.com".to_string(),
                    ServiceDefinitionV2EmailType::EMAIL,
                )
                .name("Team Email".to_string()),
            ),
        )])
        .dd_team("my-team".to_string())
        .docs(vec![ServiceDefinitionV2Doc::new(
            "Architecture".to_string(),
            "https://gdrive/mydoc".to_string(),
        )
        .provider("google drive".to_string())])
        .extensions(BTreeMap::from([(
            "myorgextension".to_string(),
            Value::from("extensionvalue"),
        )]))
        .integrations(
            ServiceDefinitionV2Integrations::new()
                .opsgenie(
                    ServiceDefinitionV2Opsgenie::new(
                        "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
                            .to_string(),
                    )
                    .region(ServiceDefinitionV2OpsgenieRegion::US),
                )
                .pagerduty("https://my-org.pagerduty.com/service-directory/PMyService".to_string()),
        )
        .links(vec![ServiceDefinitionV2Link::new(
            "Runbook".to_string(),
            ServiceDefinitionV2LinkType::RUNBOOK,
            "https://my-runbook".to_string(),
        )])
        .repos(vec![ServiceDefinitionV2Repo::new(
            "Source Code".to_string(),
            "https://github.com/DataDog/schema".to_string(),
        )
        .provider("GitHub".to_string())])
        .tags(vec!["my:tag".to_string(), "service:tag".to_string()])
        .team("my-team".to_string()),
    ));
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api.create_or_update_service_definitions(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#####

```rust
// Create or update service definition using schema v2-1 returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Contact;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Email;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1EmailType;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Integrations;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Link;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1LinkType;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Opsgenie;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1OpsgenieRegion;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Pagerduty;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot1Version;
use datadog_api_client::datadogV2::model::ServiceDefinitionsCreateRequest;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = ServiceDefinitionsCreateRequest::ServiceDefinitionV2Dot1(Box::new(
        ServiceDefinitionV2Dot1::new(
            "service-exampleservicedefinition".to_string(),
            ServiceDefinitionV2Dot1Version::V2_1,
        )
        .contacts(vec![
            ServiceDefinitionV2Dot1Contact::ServiceDefinitionV2Dot1Email(Box::new(
                ServiceDefinitionV2Dot1Email::new(
                    "contact@datadoghq.com".to_string(),
                    ServiceDefinitionV2Dot1EmailType::EMAIL,
                )
                .name("Team Email".to_string()),
            )),
        ])
        .extensions(BTreeMap::from([(
            "myorgextension".to_string(),
            Value::from("extensionvalue"),
        )]))
        .integrations(
            ServiceDefinitionV2Dot1Integrations::new()
                .opsgenie(
                    ServiceDefinitionV2Dot1Opsgenie::new(
                        "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
                            .to_string(),
                    )
                    .region(ServiceDefinitionV2Dot1OpsgenieRegion::US),
                )
                .pagerduty(ServiceDefinitionV2Dot1Pagerduty::new().service_url(
                    "https://my-org.pagerduty.com/service-directory/PMyService".to_string(),
                )),
        )
        .links(vec![
            ServiceDefinitionV2Dot1Link::new(
                "Runbook".to_string(),
                ServiceDefinitionV2Dot1LinkType::RUNBOOK,
                "https://my-runbook".to_string(),
            ),
            ServiceDefinitionV2Dot1Link::new(
                "Source Code".to_string(),
                ServiceDefinitionV2Dot1LinkType::REPO,
                "https://github.com/DataDog/schema".to_string(),
            )
            .provider("GitHub".to_string()),
            ServiceDefinitionV2Dot1Link::new(
                "Architecture".to_string(),
                ServiceDefinitionV2Dot1LinkType::DOC,
                "https://my-runbook".to_string(),
            )
            .provider("Gigoogle drivetHub".to_string()),
        ])
        .tags(vec!["my:tag".to_string(), "service:tag".to_string()])
        .team("my-team".to_string()),
    ));
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api.create_or_update_service_definitions(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#####

```rust
// Create or update service definition using schema v2-2 returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Contact;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Integrations;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Link;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Opsgenie;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2OpsgenieRegion;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Pagerduty;
use datadog_api_client::datadogV2::model::ServiceDefinitionV2Dot2Version;
use datadog_api_client::datadogV2::model::ServiceDefinitionsCreateRequest;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = ServiceDefinitionsCreateRequest::ServiceDefinitionV2Dot2(Box::new(
        ServiceDefinitionV2Dot2::new(
            "service-exampleservicedefinition".to_string(),
            ServiceDefinitionV2Dot2Version::V2_2,
        )
        .contacts(vec![ServiceDefinitionV2Dot2Contact::new(
            "contact@datadoghq.com".to_string(),
            "email".to_string(),
        )
        .name("Team Email".to_string())])
        .extensions(BTreeMap::from([(
            "myorgextension".to_string(),
            Value::from("extensionvalue"),
        )]))
        .integrations(
            ServiceDefinitionV2Dot2Integrations::new()
                .opsgenie(
                    ServiceDefinitionV2Dot2Opsgenie::new(
                        "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"
                            .to_string(),
                    )
                    .region(ServiceDefinitionV2Dot2OpsgenieRegion::US),
                )
                .pagerduty(ServiceDefinitionV2Dot2Pagerduty::new().service_url(
                    "https://my-org.pagerduty.com/service-directory/PMyService".to_string(),
                )),
        )
        .links(vec![
            ServiceDefinitionV2Dot2Link::new(
                "Runbook".to_string(),
                "runbook".to_string(),
                "https://my-runbook".to_string(),
            ),
            ServiceDefinitionV2Dot2Link::new(
                "Source Code".to_string(),
                "repo".to_string(),
                "https://github.com/DataDog/schema".to_string(),
            )
            .provider("GitHub".to_string()),
            ServiceDefinitionV2Dot2Link::new(
                "Architecture".to_string(),
                "doc".to_string(),
                "https://my-runbook".to_string(),
            )
            .provider("Gigoogle drivetHub".to_string()),
        ])
        .tags(vec!["my:tag".to_string(), "service:tag".to_string()])
        .team("my-team".to_string()),
    ));
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api.create_or_update_service_definitions(body).await;
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
 * Create or update service definition using schema v2 returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiCreateOrUpdateServiceDefinitionsRequest = {
  body: {
    contacts: [
      {
        contact: "contact@datadoghq.com",
        name: "Team Email",
        type: "email",
      },
    ],
    ddService: "service-exampleservicedefinition",
    ddTeam: "my-team",
    docs: [
      {
        name: "Architecture",
        provider: "google drive",
        url: "https://gdrive/mydoc",
      },
    ],
    extensions: {
      myorgextension: "extensionvalue",
    },
    integrations: {
      opsgenie: {
        region: "US",
        serviceUrl:
          "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
      },
      pagerduty: "https://my-org.pagerduty.com/service-directory/PMyService",
    },
    links: [
      {
        name: "Runbook",
        type: "runbook",
        url: "https://my-runbook",
      },
    ],
    repos: [
      {
        name: "Source Code",
        provider: "GitHub",
        url: "https://github.com/DataDog/schema",
      },
    ],
    schemaVersion: "v2",
    tags: ["my:tag", "service:tag"],
    team: "my-team",
  },
};

apiInstance
  .createOrUpdateServiceDefinitions(params)
  .then((data: v2.ServiceDefinitionCreateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#####

```typescript
/**
 * Create or update service definition using schema v2-1 returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiCreateOrUpdateServiceDefinitionsRequest = {
  body: {
    contacts: [
      {
        contact: "contact@datadoghq.com",
        name: "Team Email",
        type: "email",
      },
    ],
    ddService: "service-exampleservicedefinition",
    extensions: {
      myorgextension: "extensionvalue",
    },
    integrations: {
      opsgenie: {
        region: "US",
        serviceUrl:
          "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
      },
      pagerduty: {
        serviceUrl: "https://my-org.pagerduty.com/service-directory/PMyService",
      },
    },
    links: [
      {
        name: "Runbook",
        type: "runbook",
        url: "https://my-runbook",
      },
      {
        name: "Source Code",
        type: "repo",
        provider: "GitHub",
        url: "https://github.com/DataDog/schema",
      },
      {
        name: "Architecture",
        type: "doc",
        provider: "Gigoogle drivetHub",
        url: "https://my-runbook",
      },
    ],
    schemaVersion: "v2.1",
    tags: ["my:tag", "service:tag"],
    team: "my-team",
  },
};

apiInstance
  .createOrUpdateServiceDefinitions(params)
  .then((data: v2.ServiceDefinitionCreateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#####

```typescript
/**
 * Create or update service definition using schema v2-2 returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiCreateOrUpdateServiceDefinitionsRequest = {
  body: {
    contacts: [
      {
        contact: "contact@datadoghq.com",
        name: "Team Email",
        type: "email",
      },
    ],
    ddService: "service-exampleservicedefinition",
    extensions: {
      myorgextension: "extensionvalue",
    },
    integrations: {
      opsgenie: {
        region: "US",
        serviceUrl:
          "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
      },
      pagerduty: {
        serviceUrl: "https://my-org.pagerduty.com/service-directory/PMyService",
      },
    },
    links: [
      {
        name: "Runbook",
        type: "runbook",
        url: "https://my-runbook",
      },
      {
        name: "Source Code",
        type: "repo",
        provider: "GitHub",
        url: "https://github.com/DataDog/schema",
      },
      {
        name: "Architecture",
        type: "doc",
        provider: "Gigoogle drivetHub",
        url: "https://my-runbook",
      },
    ],
    schemaVersion: "v2.2",
    tags: ["my:tag", "service:tag"],
    team: "my-team",
  },
};

apiInstance
  .createOrUpdateServiceDefinitions(params)
  .then((data: v2.ServiceDefinitionCreateResponse) => {
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

## Get a single service definition{% #get-a-single-service-definition %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                 |
| ----------------- | ---------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/services/definitions/{service_name} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/services/definitions/{service_name} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/services/definitions/{service_name}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/services/definitions/{service_name}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/services/definitions/{service_name}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/services/definitions/{service_name} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/services/definitions/{service_name} |

### Overview

Get a single service definition from the Datadog Service Catalog. This endpoint requires the `apm_service_catalog_read` permission.

OAuth apps require the `apm_service_catalog_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-definition) to access this endpoint.



### Arguments

#### Path Parameters

| Name                           | Type   | Description              |
| ------------------------------ | ------ | ------------------------ |
| service_name [*required*] | string | The name of the service. |

#### Query Strings

| Name           | Type | Description                                                                          |
| -------------- | ---- | ------------------------------------------------------------------------------------ |
| schema_version | enum | The schema version desired in the response.Allowed enum values: `v1, v2, v2.1, v2.2` |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Get service definition response.

| Parent field       | Field                            | Type            | Description                                                                                                                                       |
| ------------------ | -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                             | object          | Service definition data.                                                                                                                          |
| data               | attributes                       | object          | Service definition attributes.                                                                                                                    |
| attributes         | meta                             | object          | Metadata about a service definition.                                                                                                              |
| meta               | github-html-url                  | string          | GitHub HTML URL.                                                                                                                                  |
| meta               | ingested-schema-version          | string          | Ingestion schema version.                                                                                                                         |
| meta               | ingestion-source                 | string          | Ingestion source of the service definition.                                                                                                       |
| meta               | last-modified-time               | string          | Last modified time of the service definition.                                                                                                     |
| meta               | origin                           | string          | User defined origin of the service definition.                                                                                                    |
| meta               | origin-detail                    | string          | User defined origin's detail of the service definition.                                                                                           |
| meta               | warnings                         | [object]        | A list of schema validation warnings.                                                                                                             |
| warnings           | instance-location                | string          | The warning instance location.                                                                                                                    |
| warnings           | keyword-location                 | string          | The warning keyword location.                                                                                                                     |
| warnings           | message                          | string          | The warning message.                                                                                                                              |
| attributes         | schema                           |  <oneOf>   | Service definition schema.                                                                                                                        |
| schema             | Option 1                         | object          | **DEPRECATED**: Deprecated - Service definition V1 for providing additional service metadata and integrations.                                    |
| Option 1           | contact                          | object          | Contact information about the service.                                                                                                            |
| contact            | email                            | string          | Service owner's email.                                                                                                                            |
| contact            | slack                            | string          | Service owner's Slack channel.                                                                                                                    |
| Option 1           | extensions                       | object          | Extensions to V1 schema.                                                                                                                          |
| Option 1           | external-resources               | [object]        | A list of external links related to the services.                                                                                                 |
| external-resources | name [*required*]           | string          | Link name.                                                                                                                                        |
| external-resources | type [*required*]           | enum            | Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`                                                            |
| external-resources | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 1           | info [*required*]           | object          | Basic information about a service.                                                                                                                |
| info               | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| info               | description                      | string          | A short description of the service.                                                                                                               |
| info               | display-name                     | string          | A friendly name of the service.                                                                                                                   |
| info               | service-tier                     | string          | Service tier.                                                                                                                                     |
| Option 1           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | pagerduty                        | string          | PagerDuty service URL for the service.                                                                                                            |
| Option 1           | org                              | object          | Org related information about the service.                                                                                                        |
| org                | application                      | string          | App feature this service supports.                                                                                                                |
| org                | team                             | string          | Team that owns the service.                                                                                                                       |
| Option 1           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v1`                                                                                              |
| Option 1           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| schema             | Option 2                         | object          | Service definition V2 for providing service metadata and integrations.                                                                            |
| Option 2           | contacts                         | [ <oneOf>] | A list of contacts related to the services.                                                                                                       |
| contacts           | Option 1                         | object          | Service owner's email.                                                                                                                            |
| Option 1           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 1           | name                             | string          | Contact email.                                                                                                                                    |
| Option 1           | type [*required*]           | enum            | Contact type. Allowed enum values: `email`                                                                                                        |
| contacts           | Option 2                         | object          | Service owner's Slack channel.                                                                                                                    |
| Option 2           | contact [*required*]        | string          | Slack Channel.                                                                                                                                    |
| Option 2           | name                             | string          | Contact Slack.                                                                                                                                    |
| Option 2           | type [*required*]           | enum            | Contact type. Allowed enum values: `slack`                                                                                                        |
| contacts           | Option 3                         | object          | Service owner's Microsoft Teams.                                                                                                                  |
| Option 3           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 3           | name                             | string          | Contact Microsoft Teams.                                                                                                                          |
| Option 3           | type [*required*]           | enum            | Contact type. Allowed enum values: `microsoft-teams`                                                                                              |
| Option 2           | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 2           | dd-team                          | string          | Experimental feature. A Team handle that matches a Team in the Datadog Teams product.                                                             |
| Option 2           | docs                             | [object]        | A list of documentation related to the services.                                                                                                  |
| docs               | name [*required*]           | string          | Document name.                                                                                                                                    |
| docs               | provider                         | string          | Document provider.                                                                                                                                |
| docs               | url [*required*]            | string          | Document URL.                                                                                                                                     |
| Option 2           | extensions                       | object          | Extensions to V2 schema.                                                                                                                          |
| Option 2           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie           | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie           | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations       | pagerduty                        | string          | PagerDuty service URL for the service.                                                                                                            |
| Option 2           | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links              | name [*required*]           | string          | Link name.                                                                                                                                        |
| links              | type [*required*]           | enum            | Link type. Allowed enum values: `doc,wiki,runbook,url,repo,dashboard,oncall,code,link`                                                            |
| links              | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 2           | repos                            | [object]        | A list of code repositories related to the services.                                                                                              |
| repos              | name [*required*]           | string          | Repository name.                                                                                                                                  |
| repos              | provider                         | string          | Repository provider.                                                                                                                              |
| repos              | url [*required*]            | string          | Repository URL.                                                                                                                                   |
| Option 2           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2`                                                                                              |
| Option 2           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 2           | team                             | string          | Team that owns the service.                                                                                                                       |
| schema             | Option 3                         | object          | Service definition v2.1 for providing service metadata and integrations.                                                                          |
| Option 3           | application                      | string          | Identifier for a group of related services serving a product feature, which the service is a part of.                                             |
| Option 3           | contacts                         | [ <oneOf>] | A list of contacts related to the services.                                                                                                       |
| contacts           | Option 1                         | object          | Service owner's email.                                                                                                                            |
| Option 1           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 1           | name                             | string          | Contact email.                                                                                                                                    |
| Option 1           | type [*required*]           | enum            | Contact type. Allowed enum values: `email`                                                                                                        |
| contacts           | Option 2                         | object          | Service owner's Slack channel.                                                                                                                    |
| Option 2           | contact [*required*]        | string          | Slack Channel.                                                                                                                                    |
| Option 2           | name                             | string          | Contact Slack.                                                                                                                                    |
| Option 2           | type [*required*]           | enum            | Contact type. Allowed enum values: `slack`                                                                                                        |
| contacts           | Option 3                         | object          | Service owner's Microsoft Teams.                                                                                                                  |
| Option 3           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| Option 3           | name                             | string          | Contact Microsoft Teams.                                                                                                                          |
| Option 3           | type [*required*]           | enum            | Contact type. Allowed enum values: `microsoft-teams`                                                                                              |
| Option 3           | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 3           | description                      | string          | A short description of the service.                                                                                                               |
| Option 3           | extensions                       | object          | Extensions to v2.1 schema.                                                                                                                        |
| Option 3           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie           | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie           | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations       | pagerduty                        | object          | PagerDuty integration for the service.                                                                                                            |
| pagerduty          | service-url                      | string          | PagerDuty service url.                                                                                                                            |
| Option 3           | lifecycle                        | string          | The current life cycle phase of the service.                                                                                                      |
| Option 3           | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links              | name [*required*]           | string          | Link name.                                                                                                                                        |
| links              | provider                         | string          | Link provider.                                                                                                                                    |
| links              | type [*required*]           | enum            | Link type. Allowed enum values: `doc,repo,runbook,dashboard,other`                                                                                |
| links              | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 3           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2.1`                                                                                            |
| Option 3           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 3           | team                             | string          | Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.                                                    |
| Option 3           | tier                             | string          | Importance of the service.                                                                                                                        |
| schema             | Option 4                         | object          | Service definition v2.2 for providing service metadata and integrations.                                                                          |
| Option 4           | application                      | string          | Identifier for a group of related services serving a product feature, which the service is a part of.                                             |
| Option 4           | ci-pipeline-fingerprints         | [string]        | A set of CI fingerprints.                                                                                                                         |
| Option 4           | contacts                         | [object]        | A list of contacts related to the services.                                                                                                       |
| contacts           | contact [*required*]        | string          | Contact value.                                                                                                                                    |
| contacts           | name                             | string          | Contact Name.                                                                                                                                     |
| contacts           | type [*required*]           | string          | Contact type. Datadog recognizes the following types: `email`, `slack`, and `microsoft-teams`.                                                    |
| Option 4           | dd-service [*required*]     | string          | Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.                              |
| Option 4           | description                      | string          | A short description of the service.                                                                                                               |
| Option 4           | extensions                       | object          | Extensions to v2.2 schema.                                                                                                                        |
| Option 4           | integrations                     | object          | Third party integrations that Datadog supports.                                                                                                   |
| integrations       | opsgenie                         | object          | Opsgenie integration for the service.                                                                                                             |
| opsgenie           | region                           | enum            | Opsgenie instance region. Allowed enum values: `US,EU`                                                                                            |
| opsgenie           | service-url [*required*]    | string          | Opsgenie service url.                                                                                                                             |
| integrations       | pagerduty                        | object          | PagerDuty integration for the service.                                                                                                            |
| pagerduty          | service-url                      | string          | PagerDuty service url.                                                                                                                            |
| Option 4           | languages                        | [string]        | The service's programming language. Datadog recognizes the following languages: `dotnet`, `go`, `java`, `js`, `php`, `python`, `ruby`, and `c++`. |
| Option 4           | lifecycle                        | string          | The current life cycle phase of the service.                                                                                                      |
| Option 4           | links                            | [object]        | A list of links related to the services.                                                                                                          |
| links              | name [*required*]           | string          | Link name.                                                                                                                                        |
| links              | provider                         | string          | Link provider.                                                                                                                                    |
| links              | type [*required*]           | string          | Link type. Datadog recognizes the following types: `runbook`, `doc`, `repo`, `dashboard`, and `other`.                                            |
| links              | url [*required*]            | string          | Link URL.                                                                                                                                         |
| Option 4           | schema-version [*required*] | enum            | Schema version being used. Allowed enum values: `v2.2`                                                                                            |
| Option 4           | tags                             | [string]        | A set of custom tags.                                                                                                                             |
| Option 4           | team                             | string          | Team that owns the service. It is used to locate a team defined in Datadog Teams if it exists.                                                    |
| Option 4           | tier                             | string          | Importance of the service.                                                                                                                        |
| Option 4           | type                             | string          | The type of service.                                                                                                                              |
| data               | id                               | string          | Service definition id.                                                                                                                            |
| data               | type                             | string          | Service definition type.                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "meta": {
        "github-html-url": "string",
        "ingested-schema-version": "string",
        "ingestion-source": "string",
        "last-modified-time": "string",
        "origin": "string",
        "origin-detail": "string",
        "warnings": [
          {
            "instance-location": "string",
            "keyword-location": "string",
            "message": "string"
          }
        ]
      },
      "schema": {
        "contact": {
          "email": "contact@datadoghq.com",
          "slack": "https://yourcompany.slack.com/archives/channel123"
        },
        "extensions": {
          "myorg/extension": "extensionValue"
        },
        "external-resources": [
          {
            "name": "Runbook",
            "type": "runbook",
            "url": "https://my-runbook"
          }
        ],
        "info": {
          "dd-service": "myservice",
          "description": "A shopping cart service",
          "display-name": "My Service",
          "service-tier": "Tier 1"
        },
        "integrations": {
          "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"
        },
        "org": {
          "application": "E-Commerce",
          "team": "my-team"
        },
        "schema-version": "v1",
        "tags": [
          "my:tag",
          "service:tag"
        ]
      }
    },
    "id": "string",
    "type": "string"
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

{% tab title="409" %}
Conflict
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
                  \# Path parametersexport service_name="my-service"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions/${service_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a single service definition returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_schema_versions import ServiceDefinitionSchemaVersions

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.get_service_definition(
        service_name="service-definition-test",
        schema_version=ServiceDefinitionSchemaVersions.V2_1,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get a single service definition returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new
opts = {
  schema_version: ServiceDefinitionSchemaVersions::V2_1,
}
p api_instance.get_service_definition("service-definition-test", opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get a single service definition returns "OK" response

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
    api := datadogV2.NewServiceDefinitionApi(apiClient)
    resp, r, err := api.GetServiceDefinition(ctx, "service-definition-test", *datadogV2.NewGetServiceDefinitionOptionalParameters().WithSchemaVersion(datadogV2.SERVICEDEFINITIONSCHEMAVERSIONS_V2_1))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.GetServiceDefinition`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceDefinitionApi.GetServiceDefinition`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a single service definition returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;
import com.datadog.api.client.v2.api.ServiceDefinitionApi.GetServiceDefinitionOptionalParameters;
import com.datadog.api.client.v2.model.ServiceDefinitionGetResponse;
import com.datadog.api.client.v2.model.ServiceDefinitionSchemaVersions;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    try {
      ServiceDefinitionGetResponse result =
          apiInstance.getServiceDefinition(
              "service-definition-test",
              new GetServiceDefinitionOptionalParameters()
                  .schemaVersion(ServiceDefinitionSchemaVersions.V2_1));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceDefinitionApi#getServiceDefinition");
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
// Get a single service definition returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::GetServiceDefinitionOptionalParams;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;
use datadog_api_client::datadogV2::model::ServiceDefinitionSchemaVersions;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api
        .get_service_definition(
            "service-definition-test".to_string(),
            GetServiceDefinitionOptionalParams::default()
                .schema_version(ServiceDefinitionSchemaVersions::V2_1),
        )
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
 * Get a single service definition returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiGetServiceDefinitionRequest = {
  serviceName: "service-definition-test",
  schemaVersion: "v2.1",
};

apiInstance
  .getServiceDefinition(params)
  .then((data: v2.ServiceDefinitionGetResponse) => {
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

## Delete a single service definition{% #delete-a-single-service-definition %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                    |
| ----------------- | ------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/services/definitions/{service_name} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/services/definitions/{service_name} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/services/definitions/{service_name}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/services/definitions/{service_name}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/services/definitions/{service_name}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/services/definitions/{service_name} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/services/definitions/{service_name} |

### Overview

Delete a single service definition in the Datadog Service Catalog. This endpoint requires the `apm_service_catalog_write` permission.

OAuth apps require the `apm_service_catalog_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-definition) to access this endpoint.



### Arguments

#### Path Parameters

| Name                           | Type   | Description              |
| ------------------------------ | ------ | ------------------------ |
| service_name [*required*] | string | The name of the service. |

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
                  \# Path parametersexport service_name="my-service"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/definitions/${service_name}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a single service definition returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    api_instance.delete_service_definition(
        service_name="service-definition-test",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete a single service definition returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ServiceDefinitionAPI.new
api_instance.delete_service_definition("service-definition-test")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete a single service definition returns "OK" response

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
    api := datadogV2.NewServiceDefinitionApi(apiClient)
    r, err := api.DeleteServiceDefinition(ctx, "service-definition-test")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceDefinitionApi.DeleteServiceDefinition`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete a single service definition returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ServiceDefinitionApi apiInstance = new ServiceDefinitionApi(defaultClient);

    try {
      apiInstance.deleteServiceDefinition("service-definition-test");
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceDefinitionApi#deleteServiceDefinition");
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
// Delete a single service definition returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_definition::ServiceDefinitionAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ServiceDefinitionAPI::with_config(configuration);
    let resp = api
        .delete_service_definition("service-definition-test".to_string())
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
 * Delete a single service definition returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ServiceDefinitionApi(configuration);

const params: v2.ServiceDefinitionApiDeleteServiceDefinitionRequest = {
  serviceName: "service-definition-test",
};

apiInstance
  .deleteServiceDefinition(params)
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
