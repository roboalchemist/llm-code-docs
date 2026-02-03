# Source: https://docs.datadoghq.com/api/latest/microsoft-teams-integration.md

---
title: Microsoft Teams Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Microsoft Teams Integration
---

# Microsoft Teams Integration

Configure your [Datadog Microsoft Teams integration](https://docs.datadoghq.com/integrations/microsoft_teams/) directly through the Datadog API. Note: These endpoints do not support legacy connector handles.

## Create tenant-based handle{% #create-tenant-based-handle %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/tenant-based-handles      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/tenant-based-handles      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles |

### Overview

Create a tenant-based handle in the Datadog Microsoft Teams integration.

### Request

#### Body Data (required)

Tenant-based handle payload.

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                 |
| ------------ | ---------------------------- | ------ | ------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | Tenant-based handle data from a response.                                                   |
| data         | attributes [*required*] | object | Tenant-based handle attributes.                                                             |
| attributes   | channel_id [*required*] | string | Channel id.                                                                                 |
| attributes   | name [*required*]       | string | Tenant-based handle name.                                                                   |
| attributes   | team_id [*required*]    | string | Team id.                                                                                    |
| attributes   | tenant_id [*required*]  | string | Tenant id.                                                                                  |
| data         | type [*required*]       | enum   | Specifies the tenant-based handle resource type. Allowed enum values: `tenant-based-handle` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "channel_id": "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
      "name": "Example-Microsoft-Teams-Integration",
      "team_id": "e5f50a58-c929-4fb3-8866-e2cd836de3c2",
      "tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97"
    },
    "type": "tenant-based-handle"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Response of a tenant-based handle.

| Parent field | Field                  | Type   | Description                                                                                 |
| ------------ | ---------------------- | ------ | ------------------------------------------------------------------------------------------- |
|              | data [*required*] | object | Tenant-based handle data from a response.                                                   |
| data         | attributes             | object | Tenant-based handle attributes.                                                             |
| attributes   | channel_id             | string | Channel id.                                                                                 |
| attributes   | name                   | string | Tenant-based handle name.                                                                   |
| attributes   | team_id                | string | Team id.                                                                                    |
| attributes   | tenant_id              | string | Tenant id.                                                                                  |
| data         | id                     | string | The ID of the tenant-based handle.                                                          |
| data         | type                   | enum   | Specifies the tenant-based handle resource type. Allowed enum values: `tenant-based-handle` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "channel_id": "fake-channel-id",
      "name": "fake-handle-name",
      "team_id": "00000000-0000-0000-0000-000000000000",
      "tenant_id": "00000000-0000-0000-0000-000000000001"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "tenant-based-handle"
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

{% tab title="412" %}
Failed Precondition
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "channel_id": "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
      "name": "Example-Microsoft-Teams-Integration",
      "team_id": "e5f50a58-c929-4fb3-8866-e2cd836de3c2",
      "tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97"
    },
    "type": "tenant-based-handle"
  }
}
EOF
                        
##### 

```go
// Create api handle returns "CREATED" response

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
	body := datadogV2.MicrosoftTeamsCreateTenantBasedHandleRequest{
		Data: datadogV2.MicrosoftTeamsTenantBasedHandleRequestData{
			Attributes: datadogV2.MicrosoftTeamsTenantBasedHandleRequestAttributes{
				ChannelId: "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
				Name:      "Example-Microsoft-Teams-Integration",
				TeamId:    "e5f50a58-c929-4fb3-8866-e2cd836de3c2",
				TenantId:  "4d3bac44-0230-4732-9e70-cc00736f0a97",
			},
			Type: datadogV2.MICROSOFTTEAMSTENANTBASEDHANDLETYPE_TENANT_BASED_HANDLE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.CreateTenantBasedHandle(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.CreateTenantBasedHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.CreateTenantBasedHandle`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create api handle returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsCreateTenantBasedHandleRequest;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleRequestAttributes;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleRequestData;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleResponse;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    MicrosoftTeamsCreateTenantBasedHandleRequest body =
        new MicrosoftTeamsCreateTenantBasedHandleRequest()
            .data(
                new MicrosoftTeamsTenantBasedHandleRequestData()
                    .attributes(
                        new MicrosoftTeamsTenantBasedHandleRequestAttributes()
                            .channelId(
                                "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2")
                            .name("Example-Microsoft-Teams-Integration")
                            .teamId("e5f50a58-c929-4fb3-8866-e2cd836de3c2")
                            .tenantId("4d3bac44-0230-4732-9e70-cc00736f0a97"))
                    .type(MicrosoftTeamsTenantBasedHandleType.TENANT_BASED_HANDLE));

    try {
      MicrosoftTeamsTenantBasedHandleResponse result = apiInstance.createTenantBasedHandle(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#createTenantBasedHandle");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
"""
Create api handle returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_create_tenant_based_handle_request import (
    MicrosoftTeamsCreateTenantBasedHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_request_attributes import (
    MicrosoftTeamsTenantBasedHandleRequestAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_request_data import (
    MicrosoftTeamsTenantBasedHandleRequestData,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_type import MicrosoftTeamsTenantBasedHandleType

body = MicrosoftTeamsCreateTenantBasedHandleRequest(
    data=MicrosoftTeamsTenantBasedHandleRequestData(
        attributes=MicrosoftTeamsTenantBasedHandleRequestAttributes(
            channel_id="19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
            name="Example-Microsoft-Teams-Integration",
            team_id="e5f50a58-c929-4fb3-8866-e2cd836de3c2",
            tenant_id="4d3bac44-0230-4732-9e70-cc00736f0a97",
        ),
        type=MicrosoftTeamsTenantBasedHandleType.TENANT_BASED_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.create_tenant_based_handle(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create api handle returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new

body = DatadogAPIClient::V2::MicrosoftTeamsCreateTenantBasedHandleRequest.new({
  data: DatadogAPIClient::V2::MicrosoftTeamsTenantBasedHandleRequestData.new({
    attributes: DatadogAPIClient::V2::MicrosoftTeamsTenantBasedHandleRequestAttributes.new({
      channel_id: "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
      name: "Example-Microsoft-Teams-Integration",
      team_id: "e5f50a58-c929-4fb3-8866-e2cd836de3c2",
      tenant_id: "4d3bac44-0230-4732-9e70-cc00736f0a97",
    }),
    type: DatadogAPIClient::V2::MicrosoftTeamsTenantBasedHandleType::TENANT_BASED_HANDLE,
  }),
})
p api_instance.create_tenant_based_handle(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create api handle returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;
use datadog_api_client::datadogV2::model::MicrosoftTeamsCreateTenantBasedHandleRequest;
use datadog_api_client::datadogV2::model::MicrosoftTeamsTenantBasedHandleRequestAttributes;
use datadog_api_client::datadogV2::model::MicrosoftTeamsTenantBasedHandleRequestData;
use datadog_api_client::datadogV2::model::MicrosoftTeamsTenantBasedHandleType;

#[tokio::main]
async fn main() {
    let body = MicrosoftTeamsCreateTenantBasedHandleRequest::new(
        MicrosoftTeamsTenantBasedHandleRequestData::new(
            MicrosoftTeamsTenantBasedHandleRequestAttributes::new(
                "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2".to_string(),
                "Example-Microsoft-Teams-Integration".to_string(),
                "e5f50a58-c929-4fb3-8866-e2cd836de3c2".to_string(),
                "4d3bac44-0230-4732-9e70-cc00736f0a97".to_string(),
            ),
            MicrosoftTeamsTenantBasedHandleType::TENANT_BASED_HANDLE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api.create_tenant_based_handle(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Create api handle returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiCreateTenantBasedHandleRequest = {
  body: {
    data: {
      attributes: {
        channelId:
          "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
        name: "Example-Microsoft-Teams-Integration",
        teamId: "e5f50a58-c929-4fb3-8866-e2cd836de3c2",
        tenantId: "4d3bac44-0230-4732-9e70-cc00736f0a97",
      },
      type: "tenant-based-handle",
    },
  },
};

apiInstance
  .createTenantBasedHandle(params)
  .then((data: v2.MicrosoftTeamsTenantBasedHandleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Create Workflows webhook handle{% #create-workflows-webhook-handle %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/workflows-webhook-handles      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles |

### Overview

Create a Workflows webhook handle in the Datadog Microsoft Teams integration.

### Request

#### Body Data (required)

Workflows Webhook handle payload.

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                           |
| ------------ | ---------------------------- | ------ | ----------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | Workflows Webhook handle data from a response.                                                        |
| data         | attributes [*required*] | object | Workflows Webhook handle attributes.                                                                  |
| attributes   | name [*required*]       | string | Workflows Webhook handle name.                                                                        |
| attributes   | url [*required*]        | string | Workflows Webhook URL.                                                                                |
| data         | type [*required*]       | enum   | Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "Example-Microsoft-Teams-Integration",
      "url": "https://example.logic.azure.com/workflows/123"
    },
    "type": "workflows-webhook-handle"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
CREATED
{% tab title="Model" %}
Response of a Workflows webhook handle.

| Parent field | Field                  | Type   | Description                                                                                           |
| ------------ | ---------------------- | ------ | ----------------------------------------------------------------------------------------------------- |
|              | data [*required*] | object | Workflows Webhook handle data from a response.                                                        |
| data         | attributes             | object | Workflows Webhook handle attributes.                                                                  |
| attributes   | name                   | string | Workflows Webhook handle name.                                                                        |
| data         | id                     | string | The ID of the Workflows webhook handle.                                                               |
| data         | type                   | enum   | Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "fake-handle-name"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "workflows-webhook-handle"
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

{% tab title="412" %}
Failed Precondition
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Example-Microsoft-Teams-Integration",
      "url": "https://example.logic.azure.com/workflows/123"
    },
    "type": "workflows-webhook-handle"
  }
}
EOF
                        
##### 

```go
// Create workflow webhook handle returns "CREATED" response

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
	body := datadogV2.MicrosoftTeamsCreateWorkflowsWebhookHandleRequest{
		Data: datadogV2.MicrosoftTeamsWorkflowsWebhookHandleRequestData{
			Attributes: datadogV2.MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes{
				Name: "Example-Microsoft-Teams-Integration",
				Url:  "https://example.logic.azure.com/workflows/123",
			},
			Type: datadogV2.MICROSOFTTEAMSWORKFLOWSWEBHOOKHANDLETYPE_WORKFLOWS_WEBHOOK_HANDLE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.CreateWorkflowsWebhookHandle(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.CreateWorkflowsWebhookHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.CreateWorkflowsWebhookHandle`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Create workflow webhook handle returns "CREATED" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsCreateWorkflowsWebhookHandleRequest;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleRequestData;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleResponse;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    MicrosoftTeamsCreateWorkflowsWebhookHandleRequest body =
        new MicrosoftTeamsCreateWorkflowsWebhookHandleRequest()
            .data(
                new MicrosoftTeamsWorkflowsWebhookHandleRequestData()
                    .attributes(
                        new MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes()
                            .name("Example-Microsoft-Teams-Integration")
                            .url("https://example.logic.azure.com/workflows/123"))
                    .type(MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE));

    try {
      MicrosoftTeamsWorkflowsWebhookHandleResponse result =
          apiInstance.createWorkflowsWebhookHandle(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#createWorkflowsWebhookHandle");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
"""
Create workflow webhook handle returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_create_workflows_webhook_handle_request import (
    MicrosoftTeamsCreateWorkflowsWebhookHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_request_attributes import (
    MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_request_data import (
    MicrosoftTeamsWorkflowsWebhookHandleRequestData,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_type import (
    MicrosoftTeamsWorkflowsWebhookHandleType,
)

body = MicrosoftTeamsCreateWorkflowsWebhookHandleRequest(
    data=MicrosoftTeamsWorkflowsWebhookHandleRequestData(
        attributes=MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes(
            name="Example-Microsoft-Teams-Integration",
            url="https://example.logic.azure.com/workflows/123",
        ),
        type=MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.create_workflows_webhook_handle(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Create workflow webhook handle returns "CREATED" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new

body = DatadogAPIClient::V2::MicrosoftTeamsCreateWorkflowsWebhookHandleRequest.new({
  data: DatadogAPIClient::V2::MicrosoftTeamsWorkflowsWebhookHandleRequestData.new({
    attributes: DatadogAPIClient::V2::MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes.new({
      name: "Example-Microsoft-Teams-Integration",
      url: "https://example.logic.azure.com/workflows/123",
    }),
    type: DatadogAPIClient::V2::MicrosoftTeamsWorkflowsWebhookHandleType::WORKFLOWS_WEBHOOK_HANDLE,
  }),
})
p api_instance.create_workflows_webhook_handle(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Create workflow webhook handle returns "CREATED" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;
use datadog_api_client::datadogV2::model::MicrosoftTeamsCreateWorkflowsWebhookHandleRequest;
use datadog_api_client::datadogV2::model::MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes;
use datadog_api_client::datadogV2::model::MicrosoftTeamsWorkflowsWebhookHandleRequestData;
use datadog_api_client::datadogV2::model::MicrosoftTeamsWorkflowsWebhookHandleType;

#[tokio::main]
async fn main() {
    let body = MicrosoftTeamsCreateWorkflowsWebhookHandleRequest::new(
        MicrosoftTeamsWorkflowsWebhookHandleRequestData::new(
            MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes::new(
                "Example-Microsoft-Teams-Integration".to_string(),
                "https://example.logic.azure.com/workflows/123".to_string(),
            ),
            MicrosoftTeamsWorkflowsWebhookHandleType::WORKFLOWS_WEBHOOK_HANDLE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api.create_workflows_webhook_handle(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Create workflow webhook handle returns "CREATED" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiCreateWorkflowsWebhookHandleRequest =
  {
    body: {
      data: {
        attributes: {
          name: "Example-Microsoft-Teams-Integration",
          url: "https://example.logic.azure.com/workflows/123",
        },
        type: "workflows-webhook-handle",
      },
    },
  };

apiInstance
  .createWorkflowsWebhookHandle(params)
  .then((data: v2.MicrosoftTeamsWorkflowsWebhookHandleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete tenant-based handle{% #delete-tenant-based-handle %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                    |
| ----------------- | --------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |

### Overview

Delete a tenant-based handle from the Datadog Microsoft Teams integration.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                  |
| --------------------------- | ------ | ---------------------------- |
| handle_id [*required*] | string | Your tenant-based handle id. |

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

{% tab title="412" %}
Failed Precondition
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
                  \# Path parametersexport handle_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/${handle_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete tenant-based handle returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    api_instance.delete_tenant_based_handle(
        handle_id="handle_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete tenant-based handle returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
api_instance.delete_tenant_based_handle("handle_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete tenant-based handle returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	r, err := api.DeleteTenantBasedHandle(ctx, "handle_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.DeleteTenantBasedHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete tenant-based handle returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      apiInstance.deleteTenantBasedHandle("handle_id");
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#deleteTenantBasedHandle");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
// Delete tenant-based handle returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_tenant_based_handle("handle_id".to_string())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Delete tenant-based handle returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiDeleteTenantBasedHandleRequest = {
  handleId: "handle_id",
};

apiInstance
  .deleteTenantBasedHandle(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Delete Workflows webhook handle{% #delete-workflows-webhook-handle %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                         |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |

### Overview

Delete a Workflows webhook handle from the Datadog Microsoft Teams integration.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                       |
| --------------------------- | ------ | --------------------------------- |
| handle_id [*required*] | string | Your Workflows webhook handle id. |

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

{% tab title="412" %}
Failed Precondition
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
                  \# Path parametersexport handle_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/${handle_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete Workflows webhook handle returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    api_instance.delete_workflows_webhook_handle(
        handle_id="handle_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Workflows webhook handle returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
api_instance.delete_workflows_webhook_handle("handle_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete Workflows webhook handle returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	r, err := api.DeleteWorkflowsWebhookHandle(ctx, "handle_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.DeleteWorkflowsWebhookHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete Workflows webhook handle returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      apiInstance.deleteWorkflowsWebhookHandle("handle_id");
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#deleteWorkflowsWebhookHandle");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
// Delete Workflows webhook handle returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .delete_workflows_webhook_handle("handle_id".to_string())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Delete Workflows webhook handle returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiDeleteWorkflowsWebhookHandleRequest =
  {
    handleId: "handle_id",
  };

apiInstance
  .deleteWorkflowsWebhookHandle(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get all tenant-based handles{% #get-all-tenant-based-handles %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/tenant-based-handles      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/tenant-based-handles      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles |

### Overview

Get a list of all tenant-based handles from the Datadog Microsoft Teams integration.

### Arguments

#### Query Strings

| Name      | Type   | Description                    |
| --------- | ------ | ------------------------------ |
| tenant_id | string | Your tenant id.                |
| name      | string | Your tenant-based handle name. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with a list of tenant-based handles.

| Parent field | Field                  | Type     | Description                                                                                 |
| ------------ | ---------------------- | -------- | ------------------------------------------------------------------------------------------- |
|              | data [*required*] | [object] | An array of tenant-based handles.                                                           |
| data         | attributes             | object   | Tenant-based handle attributes.                                                             |
| attributes   | channel_id             | string   | Channel id.                                                                                 |
| attributes   | channel_name           | string   | Channel name.                                                                               |
| attributes   | name                   | string   | Tenant-based handle name.                                                                   |
| attributes   | team_id                | string   | Team id.                                                                                    |
| attributes   | team_name              | string   | Team name.                                                                                  |
| attributes   | tenant_id              | string   | Tenant id.                                                                                  |
| attributes   | tenant_name            | string   | Tenant name.                                                                                |
| data         | id                     | string   | The ID of the tenant-based handle.                                                          |
| data         | type                   | enum     | Tenant-based handle resource type. Allowed enum values: `ms-teams-tenant-based-handle-info` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "channel_id": "fake-channel-id",
        "channel_name": "fake-channel-name",
        "name": "fake-handle-name",
        "team_id": "00000000-0000-0000-0000-000000000000",
        "team_name": "fake-team-name",
        "tenant_id": "00000000-0000-0000-0000-000000000001",
        "tenant_name": "fake-tenant-name"
      },
      "id": "596da4af-0563-4097-90ff-07230c3f9db3",
      "type": "ms-teams-tenant-based-handle-info"
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

{% tab title="412" %}
Failed Precondition
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all tenant-based handles returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.list_tenant_based_handles()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all tenant-based handles returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
p api_instance.list_tenant_based_handles()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all tenant-based handles returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.ListTenantBasedHandles(ctx, *datadogV2.NewListTenantBasedHandlesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.ListTenantBasedHandles`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.ListTenantBasedHandles`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all tenant-based handles returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandlesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      MicrosoftTeamsTenantBasedHandlesResponse result = apiInstance.listTenantBasedHandles();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#listTenantBasedHandles");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
// Get all tenant-based handles returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::ListTenantBasedHandlesOptionalParams;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .list_tenant_based_handles(ListTenantBasedHandlesOptionalParams::default())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Get all tenant-based handles returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

apiInstance
  .listTenantBasedHandles()
  .then((data: v2.MicrosoftTeamsTenantBasedHandlesResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get all Workflows webhook handles{% #get-all-workflows-webhook-handles %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                          |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/workflows-webhook-handles      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles |

### Overview

Get a list of all Workflows webhook handles from the Datadog Microsoft Teams integration.

### Arguments

#### Query Strings

| Name | Type   | Description                         |
| ---- | ------ | ----------------------------------- |
| name | string | Your Workflows webhook handle name. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with a list of Workflows webhook handles.

| Parent field | Field                  | Type     | Description                                                                                           |
| ------------ | ---------------------- | -------- | ----------------------------------------------------------------------------------------------------- |
|              | data [*required*] | [object] | An array of Workflows webhook handles.                                                                |
| data         | attributes             | object   | Workflows Webhook handle attributes.                                                                  |
| attributes   | name                   | string   | Workflows Webhook handle name.                                                                        |
| data         | id                     | string   | The ID of the Workflows webhook handle.                                                               |
| data         | type                   | enum     | Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "name": "fake-handle-name"
      },
      "id": "596da4af-0563-4097-90ff-07230c3f9db3",
      "type": "workflows-webhook-handle"
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

{% tab title="412" %}
Failed Precondition
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all Workflows webhook handles returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.list_workflows_webhook_handles()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get all Workflows webhook handles returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
p api_instance.list_workflows_webhook_handles()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get all Workflows webhook handles returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.ListWorkflowsWebhookHandles(ctx, *datadogV2.NewListWorkflowsWebhookHandlesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.ListWorkflowsWebhookHandles`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.ListWorkflowsWebhookHandles`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get all Workflows webhook handles returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandlesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      MicrosoftTeamsWorkflowsWebhookHandlesResponse result =
          apiInstance.listWorkflowsWebhookHandles();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#listWorkflowsWebhookHandles");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
// Get all Workflows webhook handles returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::ListWorkflowsWebhookHandlesOptionalParams;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .list_workflows_webhook_handles(ListWorkflowsWebhookHandlesOptionalParams::default())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Get all Workflows webhook handles returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

apiInstance
  .listWorkflowsWebhookHandles()
  .then((data: v2.MicrosoftTeamsWorkflowsWebhookHandlesResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get channel information by name{% #get-channel-information-by-name %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                                 |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/{tenant_name}/{team_name}/{channel_name} |

### Overview

Get the tenant, team, and channel ID of a channel in the Datadog Microsoft Teams integration.

### Arguments

#### Path Parameters

| Name                           | Type   | Description        |
| ------------------------------ | ------ | ------------------ |
| tenant_name [*required*]  | string | Your tenant name.  |
| team_name [*required*]    | string | Your team name.    |
| channel_name [*required*] | string | Your channel name. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with channel, team, and tenant ID information.

| Parent field | Field      | Type    | Description                                                              |
| ------------ | ---------- | ------- | ------------------------------------------------------------------------ |
|              | data       | object  | Channel data from a response.                                            |
| data         | attributes | object  | Channel attributes.                                                      |
| attributes   | is_primary | boolean | Indicates if this is the primary channel.                                |
| attributes   | team_id    | string  | Team id.                                                                 |
| attributes   | tenant_id  | string  | Tenant id.                                                               |
| data         | id         | string  | The ID of the channel.                                                   |
| data         | type       | enum    | Channel info resource type. Allowed enum values: `ms-teams-channel-info` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "is_primary": true,
      "team_id": "00000000-0000-0000-0000-000000000000",
      "tenant_id": "00000000-0000-0000-0000-000000000001"
    },
    "id": "19:b41k24b14bn1nwffkernfkwrnfneubgkr@thread.tacv2",
    "type": "ms-teams-channel-info"
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
                  \# Path parametersexport tenant_name="CHANGE_ME"export team_name="CHANGE_ME"export channel_name="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/channel/${tenant_name}/${team_name}/${channel_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get channel information by name returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.get_channel_by_name(
        tenant_name="tenant_name",
        team_name="team_name",
        channel_name="channel_name",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get channel information by name returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
p api_instance.get_channel_by_name("tenant_name", "team_name", "channel_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get channel information by name returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.GetChannelByName(ctx, "tenant_name", "team_name", "channel_name")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.GetChannelByName`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.GetChannelByName`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get channel information by name returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsGetChannelByNameResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      MicrosoftTeamsGetChannelByNameResponse result =
          apiInstance.getChannelByName("tenant_name", "team_name", "channel_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrosoftTeamsIntegrationApi#getChannelByName");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
// Get channel information by name returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .get_channel_by_name(
            "tenant_name".to_string(),
            "team_name".to_string(),
            "channel_name".to_string(),
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Get channel information by name returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiGetChannelByNameRequest = {
  tenantName: "tenant_name",
  teamName: "team_name",
  channelName: "channel_name",
};

apiInstance
  .getChannelByName(params)
  .then((data: v2.MicrosoftTeamsGetChannelByNameResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get tenant-based handle information{% #get-tenant-based-handle-information %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |

### Overview

Get the tenant, team, and channel information of a tenant-based handle from the Datadog Microsoft Teams integration.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                  |
| --------------------------- | ------ | ---------------------------- |
| handle_id [*required*] | string | Your tenant-based handle id. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response of a tenant-based handle.

| Parent field | Field                  | Type   | Description                                                                                 |
| ------------ | ---------------------- | ------ | ------------------------------------------------------------------------------------------- |
|              | data [*required*] | object | Tenant-based handle data from a response.                                                   |
| data         | attributes             | object | Tenant-based handle attributes.                                                             |
| attributes   | channel_id             | string | Channel id.                                                                                 |
| attributes   | name                   | string | Tenant-based handle name.                                                                   |
| attributes   | team_id                | string | Team id.                                                                                    |
| attributes   | tenant_id              | string | Tenant id.                                                                                  |
| data         | id                     | string | The ID of the tenant-based handle.                                                          |
| data         | type                   | enum   | Specifies the tenant-based handle resource type. Allowed enum values: `tenant-based-handle` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "channel_id": "fake-channel-id",
      "name": "fake-handle-name",
      "team_id": "00000000-0000-0000-0000-000000000000",
      "tenant_id": "00000000-0000-0000-0000-000000000001"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "tenant-based-handle"
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

{% tab title="412" %}
Failed Precondition
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
                  \# Path parametersexport handle_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/${handle_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get tenant-based handle information returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.get_tenant_based_handle(
        handle_id="handle_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get tenant-based handle information returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
p api_instance.get_tenant_based_handle("handle_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get tenant-based handle information returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.GetTenantBasedHandle(ctx, "handle_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.GetTenantBasedHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.GetTenantBasedHandle`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get tenant-based handle information returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      MicrosoftTeamsTenantBasedHandleResponse result =
          apiInstance.getTenantBasedHandle("handle_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#getTenantBasedHandle");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
// Get tenant-based handle information returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api.get_tenant_based_handle("handle_id".to_string()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Get tenant-based handle information returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiGetTenantBasedHandleRequest = {
  handleId: "handle_id",
};

apiInstance
  .getTenantBasedHandle(params)
  .then((data: v2.MicrosoftTeamsTenantBasedHandleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get Workflows webhook handle information{% #get-workflows-webhook-handle-information %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                      |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |

### Overview

Get the name of a Workflows webhook handle from the Datadog Microsoft Teams integration.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                       |
| --------------------------- | ------ | --------------------------------- |
| handle_id [*required*] | string | Your Workflows webhook handle id. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response of a Workflows webhook handle.

| Parent field | Field                  | Type   | Description                                                                                           |
| ------------ | ---------------------- | ------ | ----------------------------------------------------------------------------------------------------- |
|              | data [*required*] | object | Workflows Webhook handle data from a response.                                                        |
| data         | attributes             | object | Workflows Webhook handle attributes.                                                                  |
| attributes   | name                   | string | Workflows Webhook handle name.                                                                        |
| data         | id                     | string | The ID of the Workflows webhook handle.                                                               |
| data         | type                   | enum   | Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "fake-handle-name"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "workflows-webhook-handle"
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

{% tab title="412" %}
Failed Precondition
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
                  \# Path parametersexport handle_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/${handle_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get Workflows webhook handle information returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.get_workflows_webhook_handle(
        handle_id="handle_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get Workflows webhook handle information returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new
p api_instance.get_workflows_webhook_handle("handle_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get Workflows webhook handle information returns "OK" response

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
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.GetWorkflowsWebhookHandle(ctx, "handle_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.GetWorkflowsWebhookHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.GetWorkflowsWebhookHandle`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get Workflows webhook handle information returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    try {
      MicrosoftTeamsWorkflowsWebhookHandleResponse result =
          apiInstance.getWorkflowsWebhookHandle("handle_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#getWorkflowsWebhookHandle");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```rust
// Get Workflows webhook handle information returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .get_workflows_webhook_handle("handle_id".to_string())
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Get Workflows webhook handle information returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

const params: v2.MicrosoftTeamsIntegrationApiGetWorkflowsWebhookHandleRequest =
  {
    handleId: "handle_id",
  };

apiInstance
  .getWorkflowsWebhookHandle(params)
  .then((data: v2.MicrosoftTeamsWorkflowsWebhookHandleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update tenant-based handle{% #update-tenant-based-handle %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                   |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/{handle_id} |

### Overview

Update a tenant-based handle from the Datadog Microsoft Teams integration.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                  |
| --------------------------- | ------ | ---------------------------- |
| handle_id [*required*] | string | Your tenant-based handle id. |

### Request

#### Body Data (required)

Tenant-based handle payload.

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                 |
| ------------ | ---------------------------- | ------ | ------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | Tenant-based handle data from a response.                                                   |
| data         | attributes [*required*] | object | Tenant-based handle attributes.                                                             |
| attributes   | channel_id                   | string | Channel id.                                                                                 |
| attributes   | name                         | string | Tenant-based handle name.                                                                   |
| attributes   | team_id                      | string | Team id.                                                                                    |
| attributes   | tenant_id                    | string | Tenant id.                                                                                  |
| data         | type [*required*]       | enum   | Specifies the tenant-based handle resource type. Allowed enum values: `tenant-based-handle` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "fake-handle-name--updated"
    },
    "type": "tenant-based-handle"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response of a tenant-based handle.

| Parent field | Field                  | Type   | Description                                                                                 |
| ------------ | ---------------------- | ------ | ------------------------------------------------------------------------------------------- |
|              | data [*required*] | object | Tenant-based handle data from a response.                                                   |
| data         | attributes             | object | Tenant-based handle attributes.                                                             |
| attributes   | channel_id             | string | Channel id.                                                                                 |
| attributes   | name                   | string | Tenant-based handle name.                                                                   |
| attributes   | team_id                | string | Team id.                                                                                    |
| attributes   | tenant_id              | string | Tenant id.                                                                                  |
| data         | id                     | string | The ID of the tenant-based handle.                                                          |
| data         | type                   | enum   | Specifies the tenant-based handle resource type. Allowed enum values: `tenant-based-handle` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "channel_id": "fake-channel-id",
      "name": "fake-handle-name",
      "team_id": "00000000-0000-0000-0000-000000000000",
      "tenant_id": "00000000-0000-0000-0000-000000000001"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "tenant-based-handle"
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

{% tab title="412" %}
Failed Precondition
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
                          \# Path parametersexport handle_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/tenant-based-handles/${handle_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "fake-handle-name--updated"
    },
    "type": "tenant-based-handle"
  }
}
EOF
                        
##### 

```go
// Update api handle returns "OK" response

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
	// there is a valid "tenant_based_handle" in the system
	TenantBasedHandleDataID := os.Getenv("TENANT_BASED_HANDLE_DATA_ID")

	body := datadogV2.MicrosoftTeamsUpdateTenantBasedHandleRequest{
		Data: datadogV2.MicrosoftTeamsUpdateTenantBasedHandleRequestData{
			Attributes: datadogV2.MicrosoftTeamsTenantBasedHandleAttributes{
				Name: datadog.PtrString("fake-handle-name--updated"),
			},
			Type: datadogV2.MICROSOFTTEAMSTENANTBASEDHANDLETYPE_TENANT_BASED_HANDLE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.UpdateTenantBasedHandle(ctx, TenantBasedHandleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.UpdateTenantBasedHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.UpdateTenantBasedHandle`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update api handle returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleAttributes;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleResponse;
import com.datadog.api.client.v2.model.MicrosoftTeamsTenantBasedHandleType;
import com.datadog.api.client.v2.model.MicrosoftTeamsUpdateTenantBasedHandleRequest;
import com.datadog.api.client.v2.model.MicrosoftTeamsUpdateTenantBasedHandleRequestData;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    // there is a valid "tenant_based_handle" in the system
    String TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME =
        System.getenv("TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME");
    String TENANT_BASED_HANDLE_DATA_ID = System.getenv("TENANT_BASED_HANDLE_DATA_ID");

    MicrosoftTeamsUpdateTenantBasedHandleRequest body =
        new MicrosoftTeamsUpdateTenantBasedHandleRequest()
            .data(
                new MicrosoftTeamsUpdateTenantBasedHandleRequestData()
                    .attributes(
                        new MicrosoftTeamsTenantBasedHandleAttributes()
                            .name("fake-handle-name--updated"))
                    .type(MicrosoftTeamsTenantBasedHandleType.TENANT_BASED_HANDLE));

    try {
      MicrosoftTeamsTenantBasedHandleResponse result =
          apiInstance.updateTenantBasedHandle(TENANT_BASED_HANDLE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#updateTenantBasedHandle");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
"""
Update api handle returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_attributes import (
    MicrosoftTeamsTenantBasedHandleAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_type import MicrosoftTeamsTenantBasedHandleType
from datadog_api_client.v2.model.microsoft_teams_update_tenant_based_handle_request import (
    MicrosoftTeamsUpdateTenantBasedHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_update_tenant_based_handle_request_data import (
    MicrosoftTeamsUpdateTenantBasedHandleRequestData,
)

# there is a valid "tenant_based_handle" in the system
TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME = environ["TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME"]
TENANT_BASED_HANDLE_DATA_ID = environ["TENANT_BASED_HANDLE_DATA_ID"]

body = MicrosoftTeamsUpdateTenantBasedHandleRequest(
    data=MicrosoftTeamsUpdateTenantBasedHandleRequestData(
        attributes=MicrosoftTeamsTenantBasedHandleAttributes(
            name="fake-handle-name--updated",
        ),
        type=MicrosoftTeamsTenantBasedHandleType.TENANT_BASED_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.update_tenant_based_handle(handle_id=TENANT_BASED_HANDLE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update api handle returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new

# there is a valid "tenant_based_handle" in the system
TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME = ENV["TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME"]
TENANT_BASED_HANDLE_DATA_ID = ENV["TENANT_BASED_HANDLE_DATA_ID"]

body = DatadogAPIClient::V2::MicrosoftTeamsUpdateTenantBasedHandleRequest.new({
  data: DatadogAPIClient::V2::MicrosoftTeamsUpdateTenantBasedHandleRequestData.new({
    attributes: DatadogAPIClient::V2::MicrosoftTeamsTenantBasedHandleAttributes.new({
      name: "fake-handle-name--updated",
    }),
    type: DatadogAPIClient::V2::MicrosoftTeamsTenantBasedHandleType::TENANT_BASED_HANDLE,
  }),
})
p api_instance.update_tenant_based_handle(TENANT_BASED_HANDLE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update api handle returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;
use datadog_api_client::datadogV2::model::MicrosoftTeamsTenantBasedHandleAttributes;
use datadog_api_client::datadogV2::model::MicrosoftTeamsTenantBasedHandleType;
use datadog_api_client::datadogV2::model::MicrosoftTeamsUpdateTenantBasedHandleRequest;
use datadog_api_client::datadogV2::model::MicrosoftTeamsUpdateTenantBasedHandleRequestData;

#[tokio::main]
async fn main() {
    // there is a valid "tenant_based_handle" in the system
    let tenant_based_handle_data_id = std::env::var("TENANT_BASED_HANDLE_DATA_ID").unwrap();
    let body = MicrosoftTeamsUpdateTenantBasedHandleRequest::new(
        MicrosoftTeamsUpdateTenantBasedHandleRequestData::new(
            MicrosoftTeamsTenantBasedHandleAttributes::new()
                .name("fake-handle-name--updated".to_string()),
            MicrosoftTeamsTenantBasedHandleType::TENANT_BASED_HANDLE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .update_tenant_based_handle(tenant_based_handle_data_id.clone(), body)
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Update api handle returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

// there is a valid "tenant_based_handle" in the system
const TENANT_BASED_HANDLE_DATA_ID = process.env
  .TENANT_BASED_HANDLE_DATA_ID as string;

const params: v2.MicrosoftTeamsIntegrationApiUpdateTenantBasedHandleRequest = {
  body: {
    data: {
      attributes: {
        name: "fake-handle-name--updated",
      },
      type: "tenant-based-handle",
    },
  },
  handleId: TENANT_BASED_HANDLE_DATA_ID,
};

apiInstance
  .updateTenantBasedHandle(params)
  .then((data: v2.MicrosoftTeamsTenantBasedHandleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update Workflows webhook handle{% #update-workflows-webhook-handle %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/{handle_id} |

### Overview

Update a Workflows webhook handle from the Datadog Microsoft Teams integration.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                       |
| --------------------------- | ------ | --------------------------------- |
| handle_id [*required*] | string | Your Workflows webhook handle id. |

### Request

#### Body Data (required)

Workflows Webhook handle payload.

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                           |
| ------------ | ---------------------------- | ------ | ----------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | Workflows Webhook handle data from a response.                                                        |
| data         | attributes [*required*] | object | Workflows Webhook handle attributes.                                                                  |
| attributes   | name                         | string | Workflows Webhook handle name.                                                                        |
| attributes   | url                          | string | Workflows Webhook URL.                                                                                |
| data         | type [*required*]       | enum   | Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "fake-handle-name--updated"
    },
    "type": "workflows-webhook-handle"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response of a Workflows webhook handle.

| Parent field | Field                  | Type   | Description                                                                                           |
| ------------ | ---------------------- | ------ | ----------------------------------------------------------------------------------------------------- |
|              | data [*required*] | object | Workflows Webhook handle data from a response.                                                        |
| data         | attributes             | object | Workflows Webhook handle attributes.                                                                  |
| attributes   | name                   | string | Workflows Webhook handle name.                                                                        |
| data         | id                     | string | The ID of the Workflows webhook handle.                                                               |
| data         | type                   | enum   | Specifies the Workflows webhook handle resource type. Allowed enum values: `workflows-webhook-handle` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "fake-handle-name"
    },
    "id": "596da4af-0563-4097-90ff-07230c3f9db3",
    "type": "workflows-webhook-handle"
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

{% tab title="412" %}
Failed Precondition
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
                          \# Path parametersexport handle_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/ms-teams/configuration/workflows-webhook-handles/${handle_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "fake-handle-name--updated"
    },
    "type": "workflows-webhook-handle"
  }
}
EOF
                        
##### 

```go
// Update workflow webhook handle returns "OK" response

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
	// there is a valid "workflows_webhook_handle" in the system
	WorkflowsWebhookHandleDataID := os.Getenv("WORKFLOWS_WEBHOOK_HANDLE_DATA_ID")

	body := datadogV2.MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest{
		Data: datadogV2.MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData{
			Attributes: datadogV2.MicrosoftTeamsWorkflowsWebhookHandleAttributes{
				Name: datadog.PtrString("fake-handle-name--updated"),
			},
			Type: datadogV2.MICROSOFTTEAMSWORKFLOWSWEBHOOKHANDLETYPE_WORKFLOWS_WEBHOOK_HANDLE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMicrosoftTeamsIntegrationApi(apiClient)
	resp, r, err := api.UpdateWorkflowsWebhookHandle(ctx, WorkflowsWebhookHandleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MicrosoftTeamsIntegrationApi.UpdateWorkflowsWebhookHandle`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MicrosoftTeamsIntegrationApi.UpdateWorkflowsWebhookHandle`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update workflow webhook handle returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MicrosoftTeamsIntegrationApi;
import com.datadog.api.client.v2.model.MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest;
import com.datadog.api.client.v2.model.MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleAttributes;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleResponse;
import com.datadog.api.client.v2.model.MicrosoftTeamsWorkflowsWebhookHandleType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MicrosoftTeamsIntegrationApi apiInstance = new MicrosoftTeamsIntegrationApi(defaultClient);

    // there is a valid "workflows_webhook_handle" in the system
    String WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME =
        System.getenv("WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME");
    String WORKFLOWS_WEBHOOK_HANDLE_DATA_ID = System.getenv("WORKFLOWS_WEBHOOK_HANDLE_DATA_ID");

    MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest body =
        new MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest()
            .data(
                new MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData()
                    .attributes(
                        new MicrosoftTeamsWorkflowsWebhookHandleAttributes()
                            .name("fake-handle-name--updated"))
                    .type(MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE));

    try {
      MicrosoftTeamsWorkflowsWebhookHandleResponse result =
          apiInstance.updateWorkflowsWebhookHandle(WORKFLOWS_WEBHOOK_HANDLE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling MicrosoftTeamsIntegrationApi#updateWorkflowsWebhookHandle");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
"""
Update workflow webhook handle returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_update_workflows_webhook_handle_request import (
    MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_update_workflows_webhook_handle_request_data import (
    MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_attributes import (
    MicrosoftTeamsWorkflowsWebhookHandleAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_type import (
    MicrosoftTeamsWorkflowsWebhookHandleType,
)

# there is a valid "workflows_webhook_handle" in the system
WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME = environ["WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME"]
WORKFLOWS_WEBHOOK_HANDLE_DATA_ID = environ["WORKFLOWS_WEBHOOK_HANDLE_DATA_ID"]

body = MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest(
    data=MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData(
        attributes=MicrosoftTeamsWorkflowsWebhookHandleAttributes(
            name="fake-handle-name--updated",
        ),
        type=MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.update_workflows_webhook_handle(handle_id=WORKFLOWS_WEBHOOK_HANDLE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update workflow webhook handle returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MicrosoftTeamsIntegrationAPI.new

# there is a valid "workflows_webhook_handle" in the system
WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME = ENV["WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME"]
WORKFLOWS_WEBHOOK_HANDLE_DATA_ID = ENV["WORKFLOWS_WEBHOOK_HANDLE_DATA_ID"]

body = DatadogAPIClient::V2::MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest.new({
  data: DatadogAPIClient::V2::MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData.new({
    attributes: DatadogAPIClient::V2::MicrosoftTeamsWorkflowsWebhookHandleAttributes.new({
      name: "fake-handle-name--updated",
    }),
    type: DatadogAPIClient::V2::MicrosoftTeamsWorkflowsWebhookHandleType::WORKFLOWS_WEBHOOK_HANDLE,
  }),
})
p api_instance.update_workflows_webhook_handle(WORKFLOWS_WEBHOOK_HANDLE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update workflow webhook handle returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_microsoft_teams_integration::MicrosoftTeamsIntegrationAPI;
use datadog_api_client::datadogV2::model::MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest;
use datadog_api_client::datadogV2::model::MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData;
use datadog_api_client::datadogV2::model::MicrosoftTeamsWorkflowsWebhookHandleAttributes;
use datadog_api_client::datadogV2::model::MicrosoftTeamsWorkflowsWebhookHandleType;

#[tokio::main]
async fn main() {
    // there is a valid "workflows_webhook_handle" in the system
    let workflows_webhook_handle_data_id =
        std::env::var("WORKFLOWS_WEBHOOK_HANDLE_DATA_ID").unwrap();
    let body = MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest::new(
        MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData::new(
            MicrosoftTeamsWorkflowsWebhookHandleAttributes::new()
                .name("fake-handle-name--updated".to_string()),
            MicrosoftTeamsWorkflowsWebhookHandleType::WORKFLOWS_WEBHOOK_HANDLE,
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = MicrosoftTeamsIntegrationAPI::with_config(configuration);
    let resp = api
        .update_workflows_webhook_handle(workflows_webhook_handle_data_id.clone(), body)
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Update workflow webhook handle returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MicrosoftTeamsIntegrationApi(configuration);

// there is a valid "workflows_webhook_handle" in the system
const WORKFLOWS_WEBHOOK_HANDLE_DATA_ID = process.env
  .WORKFLOWS_WEBHOOK_HANDLE_DATA_ID as string;

const params: v2.MicrosoftTeamsIntegrationApiUpdateWorkflowsWebhookHandleRequest =
  {
    body: {
      data: {
        attributes: {
          name: "fake-handle-name--updated",
        },
        type: "workflows-webhook-handle",
      },
    },
    handleId: WORKFLOWS_WEBHOOK_HANDLE_DATA_ID,
  };

apiInstance
  .updateWorkflowsWebhookHandle(params)
  .then((data: v2.MicrosoftTeamsWorkflowsWebhookHandleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
