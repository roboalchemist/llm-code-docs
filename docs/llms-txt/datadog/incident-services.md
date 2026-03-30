# Source: https://docs.datadoghq.com/api/latest/incident-services.md

---
title: Incident Services
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Incident Services
---

# Incident Services

Create, update, delete, and retrieve services which can be associated with incidents. See the [Incident Management page](https://docs.datadoghq.com/service_management/incident_management/) for more information.

## Get details of an incident service{% #get-details-of-an-incident-service %}
**Note**: This endpoint is deprecated.
| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/services/{service_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/services/{service_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/services/{service_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/services/{service_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/services/{service_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/services/{service_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/services/{service_id} |

### Overview

Get details of an incident service. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident services. This endpoint requires the `incident_read` permission.

OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-services) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description                     |
| ---------------------------- | ------ | ------------------------------- |
| service_id [*required*] | string | The ID of the incident service. |

#### Query Strings

| Name    | Type | Description                                                                                                           |
| ------- | ---- | --------------------------------------------------------------------------------------------------------------------- |
| include | enum | Specifies which types of related objects should be included in the response.Allowed enum values: `users, attachments` |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with an incident service payload.

| Parent field     | Field                  | Type            | Description                                                     |
| ---------------- | ---------------------- | --------------- | --------------------------------------------------------------- |
|                  | data [*required*] | object          | Incident Service data from responses.                           |
| data             | attributes             | object          | The incident service's attributes from a response.              |
| attributes       | created                | date-time       | Timestamp of when the incident service was created.             |
| attributes       | modified               | date-time       | Timestamp of when the incident service was modified.            |
| attributes       | name                   | string          | Name of the incident service.                                   |
| data             | id [*required*]   | string          | The incident service's ID.                                      |
| data             | relationships          | object          | The incident service's relationships.                           |
| relationships    | created_by             | object          | Relationship to user.                                           |
| created_by       | data [*required*] | object          | Relationship to user object.                                    |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`               |
| relationships    | last_modified_by       | object          | Relationship to user.                                           |
| last_modified_by | data [*required*] | object          | Relationship to user object.                                    |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`               |
| data             | type [*required*] | enum            | Incident service resource type. Allowed enum values: `services` |
|                  | included               | [ <oneOf>] | Included objects from relationships.                            |
| included         | Option 1               | object          | User object returned by the API.                                |
| Option 1         | attributes             | object          | Attributes of user object returned by the API.                  |
| attributes       | created_at             | date-time       | Creation time of the user.                                      |
| attributes       | disabled               | boolean         | Whether the user is disabled.                                   |
| attributes       | email                  | string          | Email of the user.                                              |
| attributes       | handle                 | string          | Handle of the user.                                             |
| attributes       | icon                   | string          | URL of the user's icon.                                         |
| attributes       | last_login_time        | date-time       | The last time the user logged in.                               |
| attributes       | mfa_enabled            | boolean         | If user has MFA enabled.                                        |
| attributes       | modified_at            | date-time       | Time that the user was last modified.                           |
| attributes       | name                   | string          | Name of the user.                                               |
| attributes       | service_account        | boolean         | Whether the user is a service account.                          |
| attributes       | status                 | string          | Status of the user.                                             |
| attributes       | title                  | string          | Title of the user.                                              |
| attributes       | verified               | boolean         | Whether the user is verified.                                   |
| Option 1         | id                     | string          | ID of the user.                                                 |
| Option 1         | relationships          | object          | Relationships of the user object returned by the API.           |
| relationships    | org                    | object          | Relationship to an organization.                                |
| org              | data [*required*] | object          | Relationship to organization object.                            |
| data             | id [*required*]   | string          | ID of the organization.                                         |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`        |
| relationships    | other_orgs             | object          | Relationship to organizations.                                  |
| other_orgs       | data [*required*] | [object]        | Relationships to organization objects.                          |
| data             | id [*required*]   | string          | ID of the organization.                                         |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`        |
| relationships    | other_users            | object          | Relationship to users.                                          |
| other_users      | data [*required*] | [object]        | Relationships to user objects.                                  |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`               |
| relationships    | roles                  | object          | Relationship to roles.                                          |
| roles            | data                   | [object]        | An array containing type and the unique identifier of a role.   |
| data             | id                     | string          | The unique identifier of the role.                              |
| data             | type                   | enum            | Roles type. Allowed enum values: `roles`                        |
| Option 1         | type                   | enum            | Users resource type. Allowed enum values: `users`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created": "2019-09-19T10:00:00.000Z",
      "modified": "2019-09-19T10:00:00.000Z",
      "name": "service name"
    },
    "id": "00000000-0000-0000-0000-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "services"
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
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
                  \# Path parametersexport service_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/${service_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get details of an incident service returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi

# there is a valid "service" in the system
SERVICE_DATA_ID = environ["SERVICE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_incident_service"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentServicesApi(api_client)
    response = api_instance.get_incident_service(
        service_id=SERVICE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get details of an incident service returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_incident_service".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentServicesAPI.new

# there is a valid "service" in the system
SERVICE_DATA_ID = ENV["SERVICE_DATA_ID"]
p api_instance.get_incident_service(SERVICE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get details of an incident service returns "OK" response

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
    // there is a valid "service" in the system
    ServiceDataID := os.Getenv("SERVICE_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.GetIncidentService", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewIncidentServicesApi(apiClient)
    resp, r, err := api.GetIncidentService(ctx, ServiceDataID, *datadogV2.NewGetIncidentServiceOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IncidentServicesApi.GetIncidentService`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `IncidentServicesApi.GetIncidentService`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get details of an incident service returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentServicesApi;
import com.datadog.api.client.v2.model.IncidentServiceResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getIncidentService", true);
    IncidentServicesApi apiInstance = new IncidentServicesApi(defaultClient);

    // there is a valid "service" in the system
    String SERVICE_DATA_ID = System.getenv("SERVICE_DATA_ID");

    try {
      IncidentServiceResponse result = apiInstance.getIncidentService(SERVICE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentServicesApi#getIncidentService");
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
// Get details of an incident service returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incident_services::GetIncidentServiceOptionalParams;
use datadog_api_client::datadogV2::api_incident_services::IncidentServicesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "service" in the system
    let service_data_id = std::env::var("SERVICE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetIncidentService", true);
    let api = IncidentServicesAPI::with_config(configuration);
    let resp = api
        .get_incident_service(
            service_data_id.clone(),
            GetIncidentServiceOptionalParams::default(),
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
 * Get details of an incident service returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getIncidentService"] = true;
const apiInstance = new v2.IncidentServicesApi(configuration);

// there is a valid "service" in the system
const SERVICE_DATA_ID = process.env.SERVICE_DATA_ID as string;

const params: v2.IncidentServicesApiGetIncidentServiceRequest = {
  serviceId: SERVICE_DATA_ID,
};

apiInstance
  .getIncidentService(params)
  .then((data: v2.IncidentServiceResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Delete an existing incident service{% #delete-an-existing-incident-service %}
**Note**: This endpoint is deprecated.
| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/services/{service_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/services/{service_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/services/{service_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/services/{service_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/services/{service_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/services/{service_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/services/{service_id} |

### Overview

Deletes an existing incident service. This endpoint requires the `incident_settings_write` permission.

OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-services) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description                     |
| ---------------------------- | ------ | ------------------------------- |
| service_id [*required*] | string | The ID of the incident service. |

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
                  \# Path parametersexport service_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/${service_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete an existing incident service returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi

# there is a valid "service" in the system
SERVICE_DATA_ID = environ["SERVICE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_service"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentServicesApi(api_client)
    api_instance.delete_incident_service(
        service_id=SERVICE_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete an existing incident service returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_incident_service".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentServicesAPI.new

# there is a valid "service" in the system
SERVICE_DATA_ID = ENV["SERVICE_DATA_ID"]
api_instance.delete_incident_service(SERVICE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete an existing incident service returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "service" in the system
    ServiceDataID := os.Getenv("SERVICE_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.DeleteIncidentService", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewIncidentServicesApi(apiClient)
    r, err := api.DeleteIncidentService(ctx, ServiceDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IncidentServicesApi.DeleteIncidentService`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete an existing incident service returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteIncidentService", true);
    IncidentServicesApi apiInstance = new IncidentServicesApi(defaultClient);

    // there is a valid "service" in the system
    String SERVICE_DATA_ID = System.getenv("SERVICE_DATA_ID");

    try {
      apiInstance.deleteIncidentService(SERVICE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentServicesApi#deleteIncidentService");
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
// Delete an existing incident service returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incident_services::IncidentServicesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "service" in the system
    let service_data_id = std::env::var("SERVICE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteIncidentService", true);
    let api = IncidentServicesAPI::with_config(configuration);
    let resp = api.delete_incident_service(service_data_id.clone()).await;
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
 * Delete an existing incident service returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteIncidentService"] = true;
const apiInstance = new v2.IncidentServicesApi(configuration);

// there is a valid "service" in the system
const SERVICE_DATA_ID = process.env.SERVICE_DATA_ID as string;

const params: v2.IncidentServicesApiDeleteIncidentServiceRequest = {
  serviceId: SERVICE_DATA_ID,
};

apiInstance
  .deleteIncidentService(params)
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
## Update an existing incident service{% #update-an-existing-incident-service %}
**Note**: This endpoint is deprecated.
| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/services/{service_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/services/{service_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/services/{service_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/services/{service_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/services/{service_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/services/{service_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/services/{service_id} |

### Overview

Updates an existing incident service. Only provide the attributes which should be updated as this request is a partial update. This endpoint requires the `incident_settings_write` permission.

OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-services) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type   | Description                     |
| ---------------------------- | ------ | ------------------------------- |
| service_id [*required*] | string | The ID of the incident service. |

### Request

#### Body Data (required)

Incident Service Payload.

{% tab title="Model" %}

| Parent field     | Field                  | Type   | Description                                                     |
| ---------------- | ---------------------- | ------ | --------------------------------------------------------------- |
|                  | data [*required*] | object | Incident Service payload for update requests.                   |
| data             | attributes             | object | The incident service's attributes for an update request.        |
| attributes       | name [*required*] | string | Name of the incident service.                                   |
| data             | id                     | string | The incident service's ID.                                      |
| data             | relationships          | object | The incident service's relationships.                           |
| relationships    | created_by             | object | Relationship to user.                                           |
| created_by       | data [*required*] | object | Relationship to user object.                                    |
| data             | id [*required*]   | string | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum   | Users resource type. Allowed enum values: `users`               |
| relationships    | last_modified_by       | object | Relationship to user.                                           |
| last_modified_by | data [*required*] | object | Relationship to user object.                                    |
| data             | id [*required*]   | string | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum   | Users resource type. Allowed enum values: `users`               |
| data             | type [*required*] | enum   | Incident service resource type. Allowed enum values: `services` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "services",
    "attributes": {
      "name": "service name-updated"
    }
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with an incident service payload.

| Parent field     | Field                  | Type            | Description                                                     |
| ---------------- | ---------------------- | --------------- | --------------------------------------------------------------- |
|                  | data [*required*] | object          | Incident Service data from responses.                           |
| data             | attributes             | object          | The incident service's attributes from a response.              |
| attributes       | created                | date-time       | Timestamp of when the incident service was created.             |
| attributes       | modified               | date-time       | Timestamp of when the incident service was modified.            |
| attributes       | name                   | string          | Name of the incident service.                                   |
| data             | id [*required*]   | string          | The incident service's ID.                                      |
| data             | relationships          | object          | The incident service's relationships.                           |
| relationships    | created_by             | object          | Relationship to user.                                           |
| created_by       | data [*required*] | object          | Relationship to user object.                                    |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`               |
| relationships    | last_modified_by       | object          | Relationship to user.                                           |
| last_modified_by | data [*required*] | object          | Relationship to user object.                                    |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`               |
| data             | type [*required*] | enum            | Incident service resource type. Allowed enum values: `services` |
|                  | included               | [ <oneOf>] | Included objects from relationships.                            |
| included         | Option 1               | object          | User object returned by the API.                                |
| Option 1         | attributes             | object          | Attributes of user object returned by the API.                  |
| attributes       | created_at             | date-time       | Creation time of the user.                                      |
| attributes       | disabled               | boolean         | Whether the user is disabled.                                   |
| attributes       | email                  | string          | Email of the user.                                              |
| attributes       | handle                 | string          | Handle of the user.                                             |
| attributes       | icon                   | string          | URL of the user's icon.                                         |
| attributes       | last_login_time        | date-time       | The last time the user logged in.                               |
| attributes       | mfa_enabled            | boolean         | If user has MFA enabled.                                        |
| attributes       | modified_at            | date-time       | Time that the user was last modified.                           |
| attributes       | name                   | string          | Name of the user.                                               |
| attributes       | service_account        | boolean         | Whether the user is a service account.                          |
| attributes       | status                 | string          | Status of the user.                                             |
| attributes       | title                  | string          | Title of the user.                                              |
| attributes       | verified               | boolean         | Whether the user is verified.                                   |
| Option 1         | id                     | string          | ID of the user.                                                 |
| Option 1         | relationships          | object          | Relationships of the user object returned by the API.           |
| relationships    | org                    | object          | Relationship to an organization.                                |
| org              | data [*required*] | object          | Relationship to organization object.                            |
| data             | id [*required*]   | string          | ID of the organization.                                         |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`        |
| relationships    | other_orgs             | object          | Relationship to organizations.                                  |
| other_orgs       | data [*required*] | [object]        | Relationships to organization objects.                          |
| data             | id [*required*]   | string          | ID of the organization.                                         |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`        |
| relationships    | other_users            | object          | Relationship to users.                                          |
| other_users      | data [*required*] | [object]        | Relationships to user objects.                                  |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`               |
| relationships    | roles                  | object          | Relationship to roles.                                          |
| roles            | data                   | [object]        | An array containing type and the unique identifier of a role.   |
| data             | id                     | string          | The unique identifier of the role.                              |
| data             | type                   | enum            | Roles type. Allowed enum values: `roles`                        |
| Option 1         | type                   | enum            | Users resource type. Allowed enum values: `users`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created": "2019-09-19T10:00:00.000Z",
      "modified": "2019-09-19T10:00:00.000Z",
      "name": "service name"
    },
    "id": "00000000-0000-0000-0000-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "services"
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
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
                          \# Path parametersexport service_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services/${service_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "services",
    "attributes": {
      "name": "service name-updated"
    }
  }
}
EOF

#####

```go
// Update an existing incident service returns "OK" response

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
    // there is a valid "service" in the system
    ServiceDataID := os.Getenv("SERVICE_DATA_ID")

    body := datadogV2.IncidentServiceUpdateRequest{
        Data: datadogV2.IncidentServiceUpdateData{
            Type: datadogV2.INCIDENTSERVICETYPE_SERVICES,
            Attributes: &datadogV2.IncidentServiceUpdateAttributes{
                Name: "service name-updated",
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.UpdateIncidentService", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewIncidentServicesApi(apiClient)
    resp, r, err := api.UpdateIncidentService(ctx, ServiceDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IncidentServicesApi.UpdateIncidentService`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `IncidentServicesApi.UpdateIncidentService`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update an existing incident service returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentServicesApi;
import com.datadog.api.client.v2.model.IncidentServiceResponse;
import com.datadog.api.client.v2.model.IncidentServiceType;
import com.datadog.api.client.v2.model.IncidentServiceUpdateAttributes;
import com.datadog.api.client.v2.model.IncidentServiceUpdateData;
import com.datadog.api.client.v2.model.IncidentServiceUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateIncidentService", true);
    IncidentServicesApi apiInstance = new IncidentServicesApi(defaultClient);

    // there is a valid "service" in the system
    String SERVICE_DATA_ATTRIBUTES_NAME = System.getenv("SERVICE_DATA_ATTRIBUTES_NAME");
    String SERVICE_DATA_ID = System.getenv("SERVICE_DATA_ID");

    IncidentServiceUpdateRequest body =
        new IncidentServiceUpdateRequest()
            .data(
                new IncidentServiceUpdateData()
                    .type(IncidentServiceType.SERVICES)
                    .attributes(
                        new IncidentServiceUpdateAttributes().name("service name-updated")));

    try {
      IncidentServiceResponse result = apiInstance.updateIncidentService(SERVICE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentServicesApi#updateIncidentService");
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
Update an existing incident service returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi
from datadog_api_client.v2.model.incident_service_type import IncidentServiceType
from datadog_api_client.v2.model.incident_service_update_attributes import IncidentServiceUpdateAttributes
from datadog_api_client.v2.model.incident_service_update_data import IncidentServiceUpdateData
from datadog_api_client.v2.model.incident_service_update_request import IncidentServiceUpdateRequest

# there is a valid "service" in the system
SERVICE_DATA_ATTRIBUTES_NAME = environ["SERVICE_DATA_ATTRIBUTES_NAME"]
SERVICE_DATA_ID = environ["SERVICE_DATA_ID"]

body = IncidentServiceUpdateRequest(
    data=IncidentServiceUpdateData(
        type=IncidentServiceType.SERVICES,
        attributes=IncidentServiceUpdateAttributes(
            name="service name-updated",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_service"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentServicesApi(api_client)
    response = api_instance.update_incident_service(service_id=SERVICE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update an existing incident service returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_incident_service".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentServicesAPI.new

# there is a valid "service" in the system
SERVICE_DATA_ATTRIBUTES_NAME = ENV["SERVICE_DATA_ATTRIBUTES_NAME"]
SERVICE_DATA_ID = ENV["SERVICE_DATA_ID"]

body = DatadogAPIClient::V2::IncidentServiceUpdateRequest.new({
  data: DatadogAPIClient::V2::IncidentServiceUpdateData.new({
    type: DatadogAPIClient::V2::IncidentServiceType::SERVICES,
    attributes: DatadogAPIClient::V2::IncidentServiceUpdateAttributes.new({
      name: "service name-updated",
    }),
  }),
})
p api_instance.update_incident_service(SERVICE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update an existing incident service returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incident_services::IncidentServicesAPI;
use datadog_api_client::datadogV2::model::IncidentServiceType;
use datadog_api_client::datadogV2::model::IncidentServiceUpdateAttributes;
use datadog_api_client::datadogV2::model::IncidentServiceUpdateData;
use datadog_api_client::datadogV2::model::IncidentServiceUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "service" in the system
    let service_data_id = std::env::var("SERVICE_DATA_ID").unwrap();
    let body = IncidentServiceUpdateRequest::new(
        IncidentServiceUpdateData::new(IncidentServiceType::SERVICES).attributes(
            IncidentServiceUpdateAttributes::new("service name-updated".to_string()),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateIncidentService", true);
    let api = IncidentServicesAPI::with_config(configuration);
    let resp = api
        .update_incident_service(service_data_id.clone(), body)
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
 * Update an existing incident service returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateIncidentService"] = true;
const apiInstance = new v2.IncidentServicesApi(configuration);

// there is a valid "service" in the system
const SERVICE_DATA_ID = process.env.SERVICE_DATA_ID as string;

const params: v2.IncidentServicesApiUpdateIncidentServiceRequest = {
  body: {
    data: {
      type: "services",
      attributes: {
        name: "service name-updated",
      },
    },
  },
  serviceId: SERVICE_DATA_ID,
};

apiInstance
  .updateIncidentService(params)
  .then((data: v2.IncidentServiceResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Get a list of all incident services{% #get-a-list-of-all-incident-services %}
**Note**: This endpoint is deprecated.
| Datadog site      | API endpoint                                      |
| ----------------- | ------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/services |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/services |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/services      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/services      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/services     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/services |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/services |

### Overview

Get all incident services uploaded for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident services. This endpoint requires the `incident_read` permission.

OAuth apps require the `incident_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-services) to access this endpoint.



### Arguments

#### Query Strings

| Name         | Type    | Description                                                                                                           |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------------------- |
| include      | enum    | Specifies which types of related objects should be included in the response.Allowed enum values: `users, attachments` |
| page[size]   | integer | Size for a given page. The maximum allowed value is 100.                                                              |
| page[offset] | integer | Specific offset to use as the beginning of the returned page.                                                         |
| filter       | string  | A search query that filters services by name.                                                                         |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with a list of incident service payloads.

| Parent field     | Field                  | Type            | Description                                                                                                 |
| ---------------- | ---------------------- | --------------- | ----------------------------------------------------------------------------------------------------------- |
|                  | data [*required*] | [object]        | An array of incident services.                                                                              |
| data             | attributes             | object          | The incident service's attributes from a response.                                                          |
| attributes       | created                | date-time       | Timestamp of when the incident service was created.                                                         |
| attributes       | modified               | date-time       | Timestamp of when the incident service was modified.                                                        |
| attributes       | name                   | string          | Name of the incident service.                                                                               |
| data             | id [*required*]   | string          | The incident service's ID.                                                                                  |
| data             | relationships          | object          | The incident service's relationships.                                                                       |
| relationships    | created_by             | object          | Relationship to user.                                                                                       |
| created_by       | data [*required*] | object          | Relationship to user object.                                                                                |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                                                               |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                           |
| relationships    | last_modified_by       | object          | Relationship to user.                                                                                       |
| last_modified_by | data [*required*] | object          | Relationship to user object.                                                                                |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                                                               |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                           |
| data             | type [*required*] | enum            | Incident service resource type. Allowed enum values: `services`                                             |
|                  | included               | [ <oneOf>] | Included related resources which the user requested.                                                        |
| included         | Option 1               | object          | User object returned by the API.                                                                            |
| Option 1         | attributes             | object          | Attributes of user object returned by the API.                                                              |
| attributes       | created_at             | date-time       | Creation time of the user.                                                                                  |
| attributes       | disabled               | boolean         | Whether the user is disabled.                                                                               |
| attributes       | email                  | string          | Email of the user.                                                                                          |
| attributes       | handle                 | string          | Handle of the user.                                                                                         |
| attributes       | icon                   | string          | URL of the user's icon.                                                                                     |
| attributes       | last_login_time        | date-time       | The last time the user logged in.                                                                           |
| attributes       | mfa_enabled            | boolean         | If user has MFA enabled.                                                                                    |
| attributes       | modified_at            | date-time       | Time that the user was last modified.                                                                       |
| attributes       | name                   | string          | Name of the user.                                                                                           |
| attributes       | service_account        | boolean         | Whether the user is a service account.                                                                      |
| attributes       | status                 | string          | Status of the user.                                                                                         |
| attributes       | title                  | string          | Title of the user.                                                                                          |
| attributes       | verified               | boolean         | Whether the user is verified.                                                                               |
| Option 1         | id                     | string          | ID of the user.                                                                                             |
| Option 1         | relationships          | object          | Relationships of the user object returned by the API.                                                       |
| relationships    | org                    | object          | Relationship to an organization.                                                                            |
| org              | data [*required*] | object          | Relationship to organization object.                                                                        |
| data             | id [*required*]   | string          | ID of the organization.                                                                                     |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`                                                    |
| relationships    | other_orgs             | object          | Relationship to organizations.                                                                              |
| other_orgs       | data [*required*] | [object]        | Relationships to organization objects.                                                                      |
| data             | id [*required*]   | string          | ID of the organization.                                                                                     |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`                                                    |
| relationships    | other_users            | object          | Relationship to users.                                                                                      |
| other_users      | data [*required*] | [object]        | Relationships to user objects.                                                                              |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                                                               |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                           |
| relationships    | roles                  | object          | Relationship to roles.                                                                                      |
| roles            | data                   | [object]        | An array containing type and the unique identifier of a role.                                               |
| data             | id                     | string          | The unique identifier of the role.                                                                          |
| data             | type                   | enum            | Roles type. Allowed enum values: `roles`                                                                    |
| Option 1         | type                   | enum            | Users resource type. Allowed enum values: `users`                                                           |
|                  | meta                   | object          | The metadata object containing pagination metadata.                                                         |
| meta             | pagination             | object          | Pagination properties.                                                                                      |
| pagination       | next_offset            | int64           | The index of the first element in the next page of results. Equal to page size added to the current offset. |
| pagination       | offset                 | int64           | The index of the first element in the results.                                                              |
| pagination       | size                   | int64           | Maximum size of pages to return.                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created": "2019-09-19T10:00:00.000Z",
        "modified": "2019-09-19T10:00:00.000Z",
        "name": "service name"
      },
      "id": "00000000-0000-0000-0000-000000000000",
      "relationships": {
        "created_by": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        },
        "last_modified_by": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        }
      },
      "type": "services"
    }
  ],
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ],
  "meta": {
    "pagination": {
      "next_offset": 1000,
      "offset": 10,
      "size": 1000
    }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a list of all incident services returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi

# there is a valid "service" in the system
SERVICE_DATA_ATTRIBUTES_NAME = environ["SERVICE_DATA_ATTRIBUTES_NAME"]

configuration = Configuration()
configuration.unstable_operations["list_incident_services"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentServicesApi(api_client)
    response = api_instance.list_incident_services(
        filter=SERVICE_DATA_ATTRIBUTES_NAME,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get a list of all incident services returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_incident_services".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentServicesAPI.new

# there is a valid "service" in the system
SERVICE_DATA_ATTRIBUTES_NAME = ENV["SERVICE_DATA_ATTRIBUTES_NAME"]
opts = {
  filter: SERVICE_DATA_ATTRIBUTES_NAME,
}
p api_instance.list_incident_services(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get a list of all incident services returns "OK" response

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
    // there is a valid "service" in the system
    ServiceDataAttributesName := os.Getenv("SERVICE_DATA_ATTRIBUTES_NAME")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.ListIncidentServices", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewIncidentServicesApi(apiClient)
    resp, r, err := api.ListIncidentServices(ctx, *datadogV2.NewListIncidentServicesOptionalParameters().WithFilter(ServiceDataAttributesName))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IncidentServicesApi.ListIncidentServices`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `IncidentServicesApi.ListIncidentServices`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get a list of all incident services returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentServicesApi;
import com.datadog.api.client.v2.api.IncidentServicesApi.ListIncidentServicesOptionalParameters;
import com.datadog.api.client.v2.model.IncidentServicesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listIncidentServices", true);
    IncidentServicesApi apiInstance = new IncidentServicesApi(defaultClient);

    // there is a valid "service" in the system
    String SERVICE_DATA_ATTRIBUTES_NAME = System.getenv("SERVICE_DATA_ATTRIBUTES_NAME");

    try {
      IncidentServicesResponse result =
          apiInstance.listIncidentServices(
              new ListIncidentServicesOptionalParameters().filter(SERVICE_DATA_ATTRIBUTES_NAME));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentServicesApi#listIncidentServices");
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
// Get a list of all incident services returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incident_services::IncidentServicesAPI;
use datadog_api_client::datadogV2::api_incident_services::ListIncidentServicesOptionalParams;

#[tokio::main]
async fn main() {
    // there is a valid "service" in the system
    let service_data_attributes_name = std::env::var("SERVICE_DATA_ATTRIBUTES_NAME").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListIncidentServices", true);
    let api = IncidentServicesAPI::with_config(configuration);
    let resp = api
        .list_incident_services(
            ListIncidentServicesOptionalParams::default()
                .filter(service_data_attributes_name.clone()),
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
 * Get a list of all incident services returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listIncidentServices"] = true;
const apiInstance = new v2.IncidentServicesApi(configuration);

// there is a valid "service" in the system
const SERVICE_DATA_ATTRIBUTES_NAME = process.env
  .SERVICE_DATA_ATTRIBUTES_NAME as string;

const params: v2.IncidentServicesApiListIncidentServicesRequest = {
  filter: SERVICE_DATA_ATTRIBUTES_NAME,
};

apiInstance
  .listIncidentServices(params)
  .then((data: v2.IncidentServicesResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Create a new incident service{% #create-a-new-incident-service %}
**Note**: This endpoint is deprecated.
| Datadog site      | API endpoint                                       |
| ----------------- | -------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/services |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/services |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/services      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/services      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/services     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/services |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/services |

### Overview

Creates a new incident service. This endpoint requires the `incident_settings_write` permission.

OAuth apps require the `incident_settings_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#incident-services) to access this endpoint.



### Request

#### Body Data (required)

Incident Service Payload.

{% tab title="Model" %}

| Parent field     | Field                  | Type   | Description                                                     |
| ---------------- | ---------------------- | ------ | --------------------------------------------------------------- |
|                  | data [*required*] | object | Incident Service payload for create requests.                   |
| data             | attributes             | object | The incident service's attributes for a create request.         |
| attributes       | name [*required*] | string | Name of the incident service.                                   |
| data             | relationships          | object | The incident service's relationships.                           |
| relationships    | created_by             | object | Relationship to user.                                           |
| created_by       | data [*required*] | object | Relationship to user object.                                    |
| data             | id [*required*]   | string | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum   | Users resource type. Allowed enum values: `users`               |
| relationships    | last_modified_by       | object | Relationship to user.                                           |
| last_modified_by | data [*required*] | object | Relationship to user object.                                    |
| data             | id [*required*]   | string | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum   | Users resource type. Allowed enum values: `users`               |
| data             | type [*required*] | enum   | Incident service resource type. Allowed enum values: `services` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "type": "services",
    "attributes": {
      "name": "Example-Incident-Service"
    }
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Response with an incident service payload.

| Parent field     | Field                  | Type            | Description                                                     |
| ---------------- | ---------------------- | --------------- | --------------------------------------------------------------- |
|                  | data [*required*] | object          | Incident Service data from responses.                           |
| data             | attributes             | object          | The incident service's attributes from a response.              |
| attributes       | created                | date-time       | Timestamp of when the incident service was created.             |
| attributes       | modified               | date-time       | Timestamp of when the incident service was modified.            |
| attributes       | name                   | string          | Name of the incident service.                                   |
| data             | id [*required*]   | string          | The incident service's ID.                                      |
| data             | relationships          | object          | The incident service's relationships.                           |
| relationships    | created_by             | object          | Relationship to user.                                           |
| created_by       | data [*required*] | object          | Relationship to user object.                                    |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`               |
| relationships    | last_modified_by       | object          | Relationship to user.                                           |
| last_modified_by | data [*required*] | object          | Relationship to user object.                                    |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`               |
| data             | type [*required*] | enum            | Incident service resource type. Allowed enum values: `services` |
|                  | included               | [ <oneOf>] | Included objects from relationships.                            |
| included         | Option 1               | object          | User object returned by the API.                                |
| Option 1         | attributes             | object          | Attributes of user object returned by the API.                  |
| attributes       | created_at             | date-time       | Creation time of the user.                                      |
| attributes       | disabled               | boolean         | Whether the user is disabled.                                   |
| attributes       | email                  | string          | Email of the user.                                              |
| attributes       | handle                 | string          | Handle of the user.                                             |
| attributes       | icon                   | string          | URL of the user's icon.                                         |
| attributes       | last_login_time        | date-time       | The last time the user logged in.                               |
| attributes       | mfa_enabled            | boolean         | If user has MFA enabled.                                        |
| attributes       | modified_at            | date-time       | Time that the user was last modified.                           |
| attributes       | name                   | string          | Name of the user.                                               |
| attributes       | service_account        | boolean         | Whether the user is a service account.                          |
| attributes       | status                 | string          | Status of the user.                                             |
| attributes       | title                  | string          | Title of the user.                                              |
| attributes       | verified               | boolean         | Whether the user is verified.                                   |
| Option 1         | id                     | string          | ID of the user.                                                 |
| Option 1         | relationships          | object          | Relationships of the user object returned by the API.           |
| relationships    | org                    | object          | Relationship to an organization.                                |
| org              | data [*required*] | object          | Relationship to organization object.                            |
| data             | id [*required*]   | string          | ID of the organization.                                         |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`        |
| relationships    | other_orgs             | object          | Relationship to organizations.                                  |
| other_orgs       | data [*required*] | [object]        | Relationships to organization objects.                          |
| data             | id [*required*]   | string          | ID of the organization.                                         |
| data             | type [*required*] | enum            | Organizations resource type. Allowed enum values: `orgs`        |
| relationships    | other_users            | object          | Relationship to users.                                          |
| other_users      | data [*required*] | [object]        | Relationships to user objects.                                  |
| data             | id [*required*]   | string          | A unique identifier that represents the user.                   |
| data             | type [*required*] | enum            | Users resource type. Allowed enum values: `users`               |
| relationships    | roles                  | object          | Relationship to roles.                                          |
| roles            | data                   | [object]        | An array containing type and the unique identifier of a role.   |
| data             | id                     | string          | The unique identifier of the role.                              |
| data             | type                   | enum            | Roles type. Allowed enum values: `roles`                        |
| Option 1         | type                   | enum            | Users resource type. Allowed enum values: `users`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created": "2019-09-19T10:00:00.000Z",
      "modified": "2019-09-19T10:00:00.000Z",
      "name": "service name"
    },
    "id": "00000000-0000-0000-0000-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      },
      "last_modified_by": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "services"
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/services" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "type": "services",
    "attributes": {
      "name": "Example-Incident-Service"
    }
  }
}
EOF

#####

```go
// Create a new incident service returns "CREATED" response

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
    body := datadogV2.IncidentServiceCreateRequest{
        Data: datadogV2.IncidentServiceCreateData{
            Type: datadogV2.INCIDENTSERVICETYPE_SERVICES,
            Attributes: &datadogV2.IncidentServiceCreateAttributes{
                Name: "Example-Incident-Service",
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateIncidentService", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewIncidentServicesApi(apiClient)
    resp, r, err := api.CreateIncidentService(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `IncidentServicesApi.CreateIncidentService`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `IncidentServicesApi.CreateIncidentService`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create a new incident service returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.IncidentServicesApi;
import com.datadog.api.client.v2.model.IncidentServiceCreateAttributes;
import com.datadog.api.client.v2.model.IncidentServiceCreateData;
import com.datadog.api.client.v2.model.IncidentServiceCreateRequest;
import com.datadog.api.client.v2.model.IncidentServiceResponse;
import com.datadog.api.client.v2.model.IncidentServiceType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createIncidentService", true);
    IncidentServicesApi apiInstance = new IncidentServicesApi(defaultClient);

    IncidentServiceCreateRequest body =
        new IncidentServiceCreateRequest()
            .data(
                new IncidentServiceCreateData()
                    .type(IncidentServiceType.SERVICES)
                    .attributes(
                        new IncidentServiceCreateAttributes().name("Example-Incident-Service")));

    try {
      IncidentServiceResponse result = apiInstance.createIncidentService(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentServicesApi#createIncidentService");
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
Create a new incident service returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi
from datadog_api_client.v2.model.incident_service_create_attributes import IncidentServiceCreateAttributes
from datadog_api_client.v2.model.incident_service_create_data import IncidentServiceCreateData
from datadog_api_client.v2.model.incident_service_create_request import IncidentServiceCreateRequest
from datadog_api_client.v2.model.incident_service_type import IncidentServiceType

body = IncidentServiceCreateRequest(
    data=IncidentServiceCreateData(
        type=IncidentServiceType.SERVICES,
        attributes=IncidentServiceCreateAttributes(
            name="Example-Incident-Service",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_service"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentServicesApi(api_client)
    response = api_instance.create_incident_service(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create a new incident service returns "CREATED" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_incident_service".to_sym] = true
end
api_instance = DatadogAPIClient::V2::IncidentServicesAPI.new

body = DatadogAPIClient::V2::IncidentServiceCreateRequest.new({
  data: DatadogAPIClient::V2::IncidentServiceCreateData.new({
    type: DatadogAPIClient::V2::IncidentServiceType::SERVICES,
    attributes: DatadogAPIClient::V2::IncidentServiceCreateAttributes.new({
      name: "Example-Incident-Service",
    }),
  }),
})
p api_instance.create_incident_service(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create a new incident service returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_incident_services::IncidentServicesAPI;
use datadog_api_client::datadogV2::model::IncidentServiceCreateAttributes;
use datadog_api_client::datadogV2::model::IncidentServiceCreateData;
use datadog_api_client::datadogV2::model::IncidentServiceCreateRequest;
use datadog_api_client::datadogV2::model::IncidentServiceType;

#[tokio::main]
async fn main() {
    let body = IncidentServiceCreateRequest::new(
        IncidentServiceCreateData::new(IncidentServiceType::SERVICES).attributes(
            IncidentServiceCreateAttributes::new("Example-Incident-Service".to_string()),
        ),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateIncidentService", true);
    let api = IncidentServicesAPI::with_config(configuration);
    let resp = api.create_incident_service(body).await;
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
 * Create a new incident service returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createIncidentService"] = true;
const apiInstance = new v2.IncidentServicesApi(configuration);

const params: v2.IncidentServicesApiCreateIncidentServiceRequest = {
  body: {
    data: {
      type: "services",
      attributes: {
        name: "Example-Incident-Service",
      },
    },
  },
};

apiInstance
  .createIncidentService(params)
  .then((data: v2.IncidentServiceResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"