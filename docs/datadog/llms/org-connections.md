# Source: https://docs.datadoghq.com/api/latest/org-connections.md

---
title: Org Connections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Org Connections
---

# Org Connections

Manage connections between organizations. Org connections allow for controlled sharing of data between different Datadog organizations. See the [Cross-Organization Visibiltiy](https://docs.datadoghq.com/account_management/org_settings/cross_org_visibility/) page for more information.

## List Org Connections{% #list-org-connections %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/org_connections |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/org_connections |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/org_connections      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/org_connections      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/org_connections     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/org_connections |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/org_connections |

### Overview

Returns a list of org connections. This endpoint requires the `org_connections_read` permission.

OAuth apps require the `org_connections_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#org-connections) to access this endpoint.



### Arguments

#### Query Strings

| Name          | Type    | Description                                                         |
| ------------- | ------- | ------------------------------------------------------------------- |
| sink_org_id   | string  | The Org ID of the sink org.                                         |
| source_org_id | string  | The Org ID of the source org.                                       |
| limit         | integer | The limit of number of entries you want to return. Default is 1000. |
| offset        | integer | The pagination offset which you want to query from. Default is 0.   |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a list of org connections.

| Parent field  | Field                              | Type      | Description                                                            |
| ------------- | ---------------------------------- | --------- | ---------------------------------------------------------------------- |
|               | data [*required*]             | [object]  | List of org connections.                                               |
| data          | attributes [*required*]       | object    | Org connection attributes.                                             |
| attributes    | connection_types [*required*] | [string]  | List of connection types.                                              |
| attributes    | created_at [*required*]       | date-time | Timestamp when the connection was created.                             |
| data          | id [*required*]               | uuid      | The unique identifier of the org connection.                           |
| data          | relationships [*required*]    | object    | Related organizations and user.                                        |
| relationships | created_by                         | object    | User relationship.                                                     |
| created_by    | data                               | object    | The data for a user relationship.                                      |
| data          | id                                 | string    | User UUID.                                                             |
| data          | name                               | string    | User name.                                                             |
| data          | type                               | enum      | The type of the user relationship. Allowed enum values: `users`        |
| relationships | sink_org                           | object    | Org relationship.                                                      |
| sink_org      | data                               | object    | The definition of `OrgConnectionOrgRelationshipData` object.           |
| data          | id                                 | string    | Org UUID.                                                              |
| data          | name                               | string    | Org name.                                                              |
| data          | type                               | enum      | The type of the organization relationship. Allowed enum values: `orgs` |
| relationships | source_org                         | object    | Org relationship.                                                      |
| source_org    | data                               | object    | The definition of `OrgConnectionOrgRelationshipData` object.           |
| data          | id                                 | string    | Org UUID.                                                              |
| data          | name                               | string    | Org name.                                                              |
| data          | type                               | enum      | The type of the organization relationship. Allowed enum values: `orgs` |
| data          | type [*required*]             | enum      | Org connection type. Allowed enum values: `org_connection`             |
|               | meta                               | object    | Pagination metadata.                                                   |
| meta          | page                               | object    | Page information.                                                      |
| page          | total_count                        | int64     | Total number of org connections.                                       |
| page          | total_filtered_count               | int64     | Total number of org connections matching the filter.                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "connection_types": [
          "logs",
          "metrics"
        ],
        "created_at": "2023-01-01T12:00:00Z"
      },
      "id": "f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a",
      "relationships": {
        "created_by": {
          "data": {
            "id": "usr123abc456",
            "name": "John Doe",
            "type": "users"
          }
        },
        "sink_org": {
          "data": {
            "id": "f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a",
            "name": "Example Org",
            "type": "orgs"
          }
        },
        "source_org": {
          "data": {
            "id": "f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a",
            "name": "Example Org",
            "type": "orgs"
          }
        }
      },
      "type": "org_connection"
    }
  ],
  "meta": {
    "page": {
      "total_count": 0,
      "total_filtered_count": 0
    }
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/org_connections" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List Org Connections returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_connections_api import OrgConnectionsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgConnectionsApi(api_client)
    response = api_instance.list_org_connections()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List Org Connections returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OrgConnectionsAPI.new
p api_instance.list_org_connections()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List Org Connections returns "OK" response

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
    api := datadogV2.NewOrgConnectionsApi(apiClient)
    resp, r, err := api.ListOrgConnections(ctx, *datadogV2.NewListOrgConnectionsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrgConnectionsApi.ListOrgConnections`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrgConnectionsApi.ListOrgConnections`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List Org Connections returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OrgConnectionsApi;
import com.datadog.api.client.v2.model.OrgConnectionListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrgConnectionsApi apiInstance = new OrgConnectionsApi(defaultClient);

    try {
      OrgConnectionListResponse result = apiInstance.listOrgConnections();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrgConnectionsApi#listOrgConnections");
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
// List Org Connections returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_org_connections::ListOrgConnectionsOptionalParams;
use datadog_api_client::datadogV2::api_org_connections::OrgConnectionsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OrgConnectionsAPI::with_config(configuration);
    let resp = api
        .list_org_connections(ListOrgConnectionsOptionalParams::default())
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
 * List Org Connections returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OrgConnectionsApi(configuration);

apiInstance
  .listOrgConnections()
  .then((data: v2.OrgConnectionListResponse) => {
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

## Create Org Connection{% #create-org-connection %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/org_connections |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/org_connections |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/org_connections      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/org_connections      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/org_connections     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/org_connections |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/org_connections |

### Overview

Create a new org connection between the current org and a target org. This endpoint requires the `org_connections_write` permission.

OAuth apps require the `org_connections_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#org-connections) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                              | Type     | Description                                                            |
| ------------- | ---------------------------------- | -------- | ---------------------------------------------------------------------- |
|               | data [*required*]             | object   | Org connection creation data.                                          |
| data          | attributes [*required*]       | object   | Attributes for creating an org connection.                             |
| attributes    | connection_types [*required*] | [string] | List of connection types to establish.                                 |
| data          | relationships [*required*]    | object   | Relationships for org connection creation.                             |
| relationships | sink_org [*required*]         | object   | Org relationship.                                                      |
| sink_org      | data                               | object   | The definition of `OrgConnectionOrgRelationshipData` object.           |
| data          | id                                 | string   | Org UUID.                                                              |
| data          | name                               | string   | Org name.                                                              |
| data          | type                               | enum     | The type of the organization relationship. Allowed enum values: `orgs` |
| data          | type [*required*]             | enum     | Org connection type. Allowed enum values: `org_connection`             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "org_connection",
    "relationships": {
      "sink_org": {
        "data": {
          "type": "orgs",
          "id": "83999dcd-7f97-11f0-8de1-1ecf66f1aa85"
        }
      }
    },
    "attributes": {
      "connection_types": [
        "logs"
      ]
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single org connection.

| Parent field  | Field                              | Type      | Description                                                            |
| ------------- | ---------------------------------- | --------- | ---------------------------------------------------------------------- |
|               | data [*required*]             | object    | An org connection.                                                     |
| data          | attributes [*required*]       | object    | Org connection attributes.                                             |
| attributes    | connection_types [*required*] | [string]  | List of connection types.                                              |
| attributes    | created_at [*required*]       | date-time | Timestamp when the connection was created.                             |
| data          | id [*required*]               | uuid      | The unique identifier of the org connection.                           |
| data          | relationships [*required*]    | object    | Related organizations and user.                                        |
| relationships | created_by                         | object    | User relationship.                                                     |
| created_by    | data                               | object    | The data for a user relationship.                                      |
| data          | id                                 | string    | User UUID.                                                             |
| data          | name                               | string    | User name.                                                             |
| data          | type                               | enum      | The type of the user relationship. Allowed enum values: `users`        |
| relationships | sink_org                           | object    | Org relationship.                                                      |
| sink_org      | data                               | object    | The definition of `OrgConnectionOrgRelationshipData` object.           |
| data          | id                                 | string    | Org UUID.                                                              |
| data          | name                               | string    | Org name.                                                              |
| data          | type                               | enum      | The type of the organization relationship. Allowed enum values: `orgs` |
| relationships | source_org                         | object    | Org relationship.                                                      |
| source_org    | data                               | object    | The definition of `OrgConnectionOrgRelationshipData` object.           |
| data          | id                                 | string    | Org UUID.                                                              |
| data          | name                               | string    | Org name.                                                              |
| data          | type                               | enum      | The type of the organization relationship. Allowed enum values: `orgs` |
| data          | type [*required*]             | enum      | Org connection type. Allowed enum values: `org_connection`             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "connection_types": [
        "logs",
        "metrics"
      ],
      "created_at": "2023-01-01T12:00:00Z"
    },
    "id": "f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a",
    "relationships": {
      "created_by": {
        "data": {
          "id": "usr123abc456",
          "name": "John Doe",
          "type": "users"
        }
      },
      "sink_org": {
        "data": {
          "id": "f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a",
          "name": "Example Org",
          "type": "orgs"
        }
      },
      "source_org": {
        "data": {
          "id": "f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a",
          "name": "Example Org",
          "type": "orgs"
        }
      }
    },
    "type": "org_connection"
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

{% tab title="401" %}
Unauthorized
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/org_connections" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "org_connection",
    "relationships": {
      "sink_org": {
        "data": {
          "type": "orgs",
          "id": "83999dcd-7f97-11f0-8de1-1ecf66f1aa85"
        }
      }
    },
    "attributes": {
      "connection_types": [
        "logs"
      ]
    }
  }
}
EOF

#####

```go
// Create Org Connection returns "OK" response

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
    body := datadogV2.OrgConnectionCreateRequest{
        Data: datadogV2.OrgConnectionCreate{
            Type: datadogV2.ORGCONNECTIONTYPE_ORG_CONNECTION,
            Relationships: datadogV2.OrgConnectionCreateRelationships{
                SinkOrg: datadogV2.OrgConnectionOrgRelationship{
                    Data: &datadogV2.OrgConnectionOrgRelationshipData{
                        Type: datadogV2.ORGCONNECTIONORGRELATIONSHIPDATATYPE_ORGS.Ptr(),
                        Id:   datadog.PtrString("83999dcd-7f97-11f0-8de1-1ecf66f1aa85"),
                    },
                },
            },
            Attributes: datadogV2.OrgConnectionCreateAttributes{
                ConnectionTypes: []datadogV2.OrgConnectionTypeEnum{
                    datadogV2.ORGCONNECTIONTYPEENUM_LOGS,
                },
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewOrgConnectionsApi(apiClient)
    resp, r, err := api.CreateOrgConnections(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrgConnectionsApi.CreateOrgConnections`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrgConnectionsApi.CreateOrgConnections`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create Org Connection returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OrgConnectionsApi;
import com.datadog.api.client.v2.model.OrgConnectionCreate;
import com.datadog.api.client.v2.model.OrgConnectionCreateAttributes;
import com.datadog.api.client.v2.model.OrgConnectionCreateRelationships;
import com.datadog.api.client.v2.model.OrgConnectionCreateRequest;
import com.datadog.api.client.v2.model.OrgConnectionOrgRelationship;
import com.datadog.api.client.v2.model.OrgConnectionOrgRelationshipData;
import com.datadog.api.client.v2.model.OrgConnectionOrgRelationshipDataType;
import com.datadog.api.client.v2.model.OrgConnectionResponse;
import com.datadog.api.client.v2.model.OrgConnectionType;
import com.datadog.api.client.v2.model.OrgConnectionTypeEnum;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrgConnectionsApi apiInstance = new OrgConnectionsApi(defaultClient);

    OrgConnectionCreateRequest body =
        new OrgConnectionCreateRequest()
            .data(
                new OrgConnectionCreate()
                    .type(OrgConnectionType.ORG_CONNECTION)
                    .relationships(
                        new OrgConnectionCreateRelationships()
                            .sinkOrg(
                                new OrgConnectionOrgRelationship()
                                    .data(
                                        new OrgConnectionOrgRelationshipData()
                                            .type(OrgConnectionOrgRelationshipDataType.ORGS)
                                            .id("83999dcd-7f97-11f0-8de1-1ecf66f1aa85"))))
                    .attributes(
                        new OrgConnectionCreateAttributes()
                            .connectionTypes(
                                Collections.singletonList(OrgConnectionTypeEnum.LOGS))));

    try {
      OrgConnectionResponse result = apiInstance.createOrgConnections(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrgConnectionsApi#createOrgConnections");
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
Create Org Connection returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_connections_api import OrgConnectionsApi
from datadog_api_client.v2.model.org_connection_create import OrgConnectionCreate
from datadog_api_client.v2.model.org_connection_create_attributes import OrgConnectionCreateAttributes
from datadog_api_client.v2.model.org_connection_create_relationships import OrgConnectionCreateRelationships
from datadog_api_client.v2.model.org_connection_create_request import OrgConnectionCreateRequest
from datadog_api_client.v2.model.org_connection_org_relationship import OrgConnectionOrgRelationship
from datadog_api_client.v2.model.org_connection_org_relationship_data import OrgConnectionOrgRelationshipData
from datadog_api_client.v2.model.org_connection_org_relationship_data_type import OrgConnectionOrgRelationshipDataType
from datadog_api_client.v2.model.org_connection_type import OrgConnectionType
from datadog_api_client.v2.model.org_connection_type_enum import OrgConnectionTypeEnum

body = OrgConnectionCreateRequest(
    data=OrgConnectionCreate(
        type=OrgConnectionType.ORG_CONNECTION,
        relationships=OrgConnectionCreateRelationships(
            sink_org=OrgConnectionOrgRelationship(
                data=OrgConnectionOrgRelationshipData(
                    type=OrgConnectionOrgRelationshipDataType.ORGS,
                    id="83999dcd-7f97-11f0-8de1-1ecf66f1aa85",
                ),
            ),
        ),
        attributes=OrgConnectionCreateAttributes(
            connection_types=[
                OrgConnectionTypeEnum.LOGS,
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgConnectionsApi(api_client)
    response = api_instance.create_org_connections(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create Org Connection returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OrgConnectionsAPI.new

body = DatadogAPIClient::V2::OrgConnectionCreateRequest.new({
  data: DatadogAPIClient::V2::OrgConnectionCreate.new({
    type: DatadogAPIClient::V2::OrgConnectionType::ORG_CONNECTION,
    relationships: DatadogAPIClient::V2::OrgConnectionCreateRelationships.new({
      sink_org: DatadogAPIClient::V2::OrgConnectionOrgRelationship.new({
        data: DatadogAPIClient::V2::OrgConnectionOrgRelationshipData.new({
          type: DatadogAPIClient::V2::OrgConnectionOrgRelationshipDataType::ORGS,
          id: "83999dcd-7f97-11f0-8de1-1ecf66f1aa85",
        }),
      }),
    }),
    attributes: DatadogAPIClient::V2::OrgConnectionCreateAttributes.new({
      connection_types: [
        DatadogAPIClient::V2::OrgConnectionTypeEnum::LOGS,
      ],
    }),
  }),
})
p api_instance.create_org_connections(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create Org Connection returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_org_connections::OrgConnectionsAPI;
use datadog_api_client::datadogV2::model::OrgConnectionCreate;
use datadog_api_client::datadogV2::model::OrgConnectionCreateAttributes;
use datadog_api_client::datadogV2::model::OrgConnectionCreateRelationships;
use datadog_api_client::datadogV2::model::OrgConnectionCreateRequest;
use datadog_api_client::datadogV2::model::OrgConnectionOrgRelationship;
use datadog_api_client::datadogV2::model::OrgConnectionOrgRelationshipData;
use datadog_api_client::datadogV2::model::OrgConnectionOrgRelationshipDataType;
use datadog_api_client::datadogV2::model::OrgConnectionType;
use datadog_api_client::datadogV2::model::OrgConnectionTypeEnum;

#[tokio::main]
async fn main() {
    let body = OrgConnectionCreateRequest::new(OrgConnectionCreate::new(
        OrgConnectionCreateAttributes::new(vec![OrgConnectionTypeEnum::LOGS]),
        OrgConnectionCreateRelationships::new(
            OrgConnectionOrgRelationship::new().data(
                OrgConnectionOrgRelationshipData::new()
                    .id("83999dcd-7f97-11f0-8de1-1ecf66f1aa85".to_string())
                    .type_(OrgConnectionOrgRelationshipDataType::ORGS),
            ),
        ),
        OrgConnectionType::ORG_CONNECTION,
    ));
    let configuration = datadog::Configuration::new();
    let api = OrgConnectionsAPI::with_config(configuration);
    let resp = api.create_org_connections(body).await;
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
 * Create Org Connection returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OrgConnectionsApi(configuration);

const params: v2.OrgConnectionsApiCreateOrgConnectionsRequest = {
  body: {
    data: {
      type: "org_connection",
      relationships: {
        sinkOrg: {
          data: {
            type: "orgs",
            id: "83999dcd-7f97-11f0-8de1-1ecf66f1aa85",
          },
        },
      },
      attributes: {
        connectionTypes: ["logs"],
      },
    },
  },
};

apiInstance
  .createOrgConnections(params)
  .then((data: v2.OrgConnectionResponse) => {
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

## Update Org Connection{% #update-org-connection %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/org_connections/{connection_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/org_connections/{connection_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/org_connections/{connection_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/org_connections/{connection_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/org_connections/{connection_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/org_connections/{connection_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/org_connections/{connection_id} |

### Overview

Update an existing org connection. This endpoint requires the `org_connections_write` permission.

OAuth apps require the `org_connections_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#org-connections) to access this endpoint.



### Arguments

#### Path Parameters

| Name                            | Type   | Description                                  |
| ------------------------------- | ------ | -------------------------------------------- |
| connection_id [*required*] | string | The unique identifier of the org connection. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                              | Type     | Description                                                |
| ------------ | ---------------------------------- | -------- | ---------------------------------------------------------- |
|              | data [*required*]             | object   | Org connection update data.                                |
| data         | attributes [*required*]       | object   | Attributes for updating an org connection.                 |
| attributes   | connection_types [*required*] | [string] | Updated list of connection types.                          |
| data         | id [*required*]               | uuid     | The unique identifier of the org connection.               |
| data         | type [*required*]             | enum     | Org connection type. Allowed enum values: `org_connection` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "org_connection",
    "id": "f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a",
    "attributes": {
      "connection_types": [
        "logs",
        "metrics"
      ]
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single org connection.

| Parent field  | Field                              | Type      | Description                                                            |
| ------------- | ---------------------------------- | --------- | ---------------------------------------------------------------------- |
|               | data [*required*]             | object    | An org connection.                                                     |
| data          | attributes [*required*]       | object    | Org connection attributes.                                             |
| attributes    | connection_types [*required*] | [string]  | List of connection types.                                              |
| attributes    | created_at [*required*]       | date-time | Timestamp when the connection was created.                             |
| data          | id [*required*]               | uuid      | The unique identifier of the org connection.                           |
| data          | relationships [*required*]    | object    | Related organizations and user.                                        |
| relationships | created_by                         | object    | User relationship.                                                     |
| created_by    | data                               | object    | The data for a user relationship.                                      |
| data          | id                                 | string    | User UUID.                                                             |
| data          | name                               | string    | User name.                                                             |
| data          | type                               | enum      | The type of the user relationship. Allowed enum values: `users`        |
| relationships | sink_org                           | object    | Org relationship.                                                      |
| sink_org      | data                               | object    | The definition of `OrgConnectionOrgRelationshipData` object.           |
| data          | id                                 | string    | Org UUID.                                                              |
| data          | name                               | string    | Org name.                                                              |
| data          | type                               | enum      | The type of the organization relationship. Allowed enum values: `orgs` |
| relationships | source_org                         | object    | Org relationship.                                                      |
| source_org    | data                               | object    | The definition of `OrgConnectionOrgRelationshipData` object.           |
| data          | id                                 | string    | Org UUID.                                                              |
| data          | name                               | string    | Org name.                                                              |
| data          | type                               | enum      | The type of the organization relationship. Allowed enum values: `orgs` |
| data          | type [*required*]             | enum      | Org connection type. Allowed enum values: `org_connection`             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "connection_types": [
        "logs",
        "metrics"
      ],
      "created_at": "2023-01-01T12:00:00Z"
    },
    "id": "f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a",
    "relationships": {
      "created_by": {
        "data": {
          "id": "usr123abc456",
          "name": "John Doe",
          "type": "users"
        }
      },
      "sink_org": {
        "data": {
          "id": "f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a",
          "name": "Example Org",
          "type": "orgs"
        }
      },
      "source_org": {
        "data": {
          "id": "f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a",
          "name": "Example Org",
          "type": "orgs"
        }
      }
    },
    "type": "org_connection"
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

{% tab title="401" %}
Unauthorized
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
                          \# Path parametersexport connection_id="f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/org_connections/${connection_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "org_connection",
    "id": "f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a",
    "attributes": {
      "connection_types": [
        "logs",
        "metrics"
      ]
    }
  }
}
EOF

#####

```go
// Update Org Connection returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "org_connection" in the system
    OrgConnectionDataID := uuid.MustParse(os.Getenv("ORG_CONNECTION_DATA_ID"))

    body := datadogV2.OrgConnectionUpdateRequest{
        Data: datadogV2.OrgConnectionUpdate{
            Type: datadogV2.ORGCONNECTIONTYPE_ORG_CONNECTION,
            Id:   OrgConnectionDataID,
            Attributes: datadogV2.OrgConnectionUpdateAttributes{
                ConnectionTypes: []datadogV2.OrgConnectionTypeEnum{
                    datadogV2.ORGCONNECTIONTYPEENUM_LOGS,
                    datadogV2.ORGCONNECTIONTYPEENUM_METRICS,
                },
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewOrgConnectionsApi(apiClient)
    resp, r, err := api.UpdateOrgConnections(ctx, OrgConnectionDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrgConnectionsApi.UpdateOrgConnections`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrgConnectionsApi.UpdateOrgConnections`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update Org Connection returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OrgConnectionsApi;
import com.datadog.api.client.v2.model.OrgConnectionResponse;
import com.datadog.api.client.v2.model.OrgConnectionType;
import com.datadog.api.client.v2.model.OrgConnectionTypeEnum;
import com.datadog.api.client.v2.model.OrgConnectionUpdate;
import com.datadog.api.client.v2.model.OrgConnectionUpdateAttributes;
import com.datadog.api.client.v2.model.OrgConnectionUpdateRequest;
import java.util.Arrays;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrgConnectionsApi apiInstance = new OrgConnectionsApi(defaultClient);

    // there is a valid "org_connection" in the system
    UUID ORG_CONNECTION_DATA_ID = null;
    try {
      ORG_CONNECTION_DATA_ID = UUID.fromString(System.getenv("ORG_CONNECTION_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    OrgConnectionUpdateRequest body =
        new OrgConnectionUpdateRequest()
            .data(
                new OrgConnectionUpdate()
                    .type(OrgConnectionType.ORG_CONNECTION)
                    .id(ORG_CONNECTION_DATA_ID)
                    .attributes(
                        new OrgConnectionUpdateAttributes()
                            .connectionTypes(
                                Arrays.asList(
                                    OrgConnectionTypeEnum.LOGS, OrgConnectionTypeEnum.METRICS))));

    try {
      OrgConnectionResponse result = apiInstance.updateOrgConnections(ORG_CONNECTION_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrgConnectionsApi#updateOrgConnections");
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
Update Org Connection returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_connections_api import OrgConnectionsApi
from datadog_api_client.v2.model.org_connection_type import OrgConnectionType
from datadog_api_client.v2.model.org_connection_type_enum import OrgConnectionTypeEnum
from datadog_api_client.v2.model.org_connection_update import OrgConnectionUpdate
from datadog_api_client.v2.model.org_connection_update_attributes import OrgConnectionUpdateAttributes
from datadog_api_client.v2.model.org_connection_update_request import OrgConnectionUpdateRequest

# there is a valid "org_connection" in the system
ORG_CONNECTION_DATA_ID = environ["ORG_CONNECTION_DATA_ID"]

body = OrgConnectionUpdateRequest(
    data=OrgConnectionUpdate(
        type=OrgConnectionType.ORG_CONNECTION,
        id=ORG_CONNECTION_DATA_ID,
        attributes=OrgConnectionUpdateAttributes(
            connection_types=[
                OrgConnectionTypeEnum.LOGS,
                OrgConnectionTypeEnum.METRICS,
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgConnectionsApi(api_client)
    response = api_instance.update_org_connections(connection_id=ORG_CONNECTION_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update Org Connection returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OrgConnectionsAPI.new

# there is a valid "org_connection" in the system
ORG_CONNECTION_DATA_ID = ENV["ORG_CONNECTION_DATA_ID"]

body = DatadogAPIClient::V2::OrgConnectionUpdateRequest.new({
  data: DatadogAPIClient::V2::OrgConnectionUpdate.new({
    type: DatadogAPIClient::V2::OrgConnectionType::ORG_CONNECTION,
    id: ORG_CONNECTION_DATA_ID,
    attributes: DatadogAPIClient::V2::OrgConnectionUpdateAttributes.new({
      connection_types: [
        DatadogAPIClient::V2::OrgConnectionTypeEnum::LOGS,
        DatadogAPIClient::V2::OrgConnectionTypeEnum::METRICS,
      ],
    }),
  }),
})
p api_instance.update_org_connections(ORG_CONNECTION_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update Org Connection returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_org_connections::OrgConnectionsAPI;
use datadog_api_client::datadogV2::model::OrgConnectionType;
use datadog_api_client::datadogV2::model::OrgConnectionTypeEnum;
use datadog_api_client::datadogV2::model::OrgConnectionUpdate;
use datadog_api_client::datadogV2::model::OrgConnectionUpdateAttributes;
use datadog_api_client::datadogV2::model::OrgConnectionUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "org_connection" in the system
    let org_connection_data_id =
        uuid::Uuid::parse_str(&std::env::var("ORG_CONNECTION_DATA_ID").unwrap())
            .expect("Invalid UUID");
    let body = OrgConnectionUpdateRequest::new(OrgConnectionUpdate::new(
        OrgConnectionUpdateAttributes::new(vec![
            OrgConnectionTypeEnum::LOGS,
            OrgConnectionTypeEnum::METRICS,
        ]),
        org_connection_data_id.clone(),
        OrgConnectionType::ORG_CONNECTION,
    ));
    let configuration = datadog::Configuration::new();
    let api = OrgConnectionsAPI::with_config(configuration);
    let resp = api
        .update_org_connections(org_connection_data_id.clone(), body)
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
 * Update Org Connection returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OrgConnectionsApi(configuration);

// there is a valid "org_connection" in the system
const ORG_CONNECTION_DATA_ID = process.env.ORG_CONNECTION_DATA_ID as string;

const params: v2.OrgConnectionsApiUpdateOrgConnectionsRequest = {
  body: {
    data: {
      type: "org_connection",
      id: ORG_CONNECTION_DATA_ID,
      attributes: {
        connectionTypes: ["logs", "metrics"],
      },
    },
  },
  connectionId: ORG_CONNECTION_DATA_ID,
};

apiInstance
  .updateOrgConnections(params)
  .then((data: v2.OrgConnectionResponse) => {
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

## Delete Org Connection{% #delete-org-connection %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/org_connections/{connection_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/org_connections/{connection_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/org_connections/{connection_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/org_connections/{connection_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/org_connections/{connection_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/org_connections/{connection_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/org_connections/{connection_id} |

### Overview

Delete an existing org connection. This endpoint requires the `org_connections_write` permission.

OAuth apps require the `org_connections_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#org-connections) to access this endpoint.



### Arguments

#### Path Parameters

| Name                            | Type   | Description                                  |
| ------------------------------- | ------ | -------------------------------------------- |
| connection_id [*required*] | string | The unique identifier of the org connection. |

### Response

{% tab title="200" %}
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

{% tab title="401" %}
Unauthorized
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
                  \# Path parametersexport connection_id="f9ec96b0-8c8a-4b0a-9b0a-1b2c3d4e5f6a"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/org_connections/${connection_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete Org Connection returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_connections_api import OrgConnectionsApi

# there is a valid "org_connection" in the system
ORG_CONNECTION_DATA_ID = environ["ORG_CONNECTION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgConnectionsApi(api_client)
    api_instance.delete_org_connections(
        connection_id=ORG_CONNECTION_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete Org Connection returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OrgConnectionsAPI.new

# there is a valid "org_connection" in the system
ORG_CONNECTION_DATA_ID = ENV["ORG_CONNECTION_DATA_ID"]
p api_instance.delete_org_connections(ORG_CONNECTION_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete Org Connection returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "org_connection" in the system
    OrgConnectionDataID := uuid.MustParse(os.Getenv("ORG_CONNECTION_DATA_ID"))

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewOrgConnectionsApi(apiClient)
    r, err := api.DeleteOrgConnections(ctx, OrgConnectionDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrgConnectionsApi.DeleteOrgConnections`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete Org Connection returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OrgConnectionsApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrgConnectionsApi apiInstance = new OrgConnectionsApi(defaultClient);

    // there is a valid "org_connection" in the system
    UUID ORG_CONNECTION_DATA_ID = null;
    try {
      ORG_CONNECTION_DATA_ID = UUID.fromString(System.getenv("ORG_CONNECTION_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      apiInstance.deleteOrgConnections(ORG_CONNECTION_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrgConnectionsApi#deleteOrgConnections");
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
// Delete Org Connection returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_org_connections::OrgConnectionsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "org_connection" in the system
    let org_connection_data_id =
        uuid::Uuid::parse_str(&std::env::var("ORG_CONNECTION_DATA_ID").unwrap())
            .expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = OrgConnectionsAPI::with_config(configuration);
    let resp = api
        .delete_org_connections(org_connection_data_id.clone())
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
 * Delete Org Connection returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OrgConnectionsApi(configuration);

// there is a valid "org_connection" in the system
const ORG_CONNECTION_DATA_ID = process.env.ORG_CONNECTION_DATA_ID as string;

const params: v2.OrgConnectionsApiDeleteOrgConnectionsRequest = {
  connectionId: ORG_CONNECTION_DATA_ID,
};

apiInstance
  .deleteOrgConnections(params)
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
