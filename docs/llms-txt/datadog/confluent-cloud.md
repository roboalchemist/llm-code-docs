# Source: https://docs.datadoghq.com/api/latest/confluent-cloud.md

---
title: Confluent Cloud
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Confluent Cloud
---

# Confluent Cloud

Manage your Datadog Confluent Cloud integration accounts and account resources directly through the Datadog API. See the [Confluent Cloud page](https://docs.datadoghq.com/integrations/confluent_cloud/) for more information.

## Update resource in Confluent account{% #update-resource-in-confluent-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                          |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |

### Overview

Update a Confluent resource with the provided resource id for the account associated with the provided account ID. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                    |
| ----------------------------- | ------ | ------------------------------ |
| account_id [*required*]  | string | Confluent Account ID.          |
| resource_id [*required*] | string | Confluent Account Resource ID. |

### Request

#### Body Data (required)

Confluent payload

{% tab title="Model" %}

| Parent field | Field                           | Type     | Description                                                                                        |
| ------------ | ------------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
|              | data [*required*]          | object   | JSON:API request for updating a Confluent resource.                                                |
| data         | attributes [*required*]    | object   | Attributes object for updating a Confluent resource.                                               |
| attributes   | enable_custom_metrics           | boolean  | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.                  |
| attributes   | resource_type [*required*] | string   | The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.      |
| attributes   | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon. |
| data         | id [*required*]            | string   | The ID associated with a Confluent resource.                                                       |
| data         | type [*required*]          | enum     | The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enable_custom_metrics": false,
      "resource_type": "kafka",
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "resource-id-123",
    "type": "confluent-cloud-resources"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response schema when interacting with a Confluent resource.

| Parent field | Field                           | Type     | Description                                                                                        |
| ------------ | ------------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
|              | data                            | object   | Confluent Cloud resource data.                                                                     |
| data         | attributes [*required*]    | object   | Model representation of a Confluent Cloud resource.                                                |
| attributes   | enable_custom_metrics           | boolean  | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.                  |
| attributes   | id                              | string   | The ID associated with the Confluent resource.                                                     |
| attributes   | resource_type [*required*] | string   | The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.      |
| attributes   | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon. |
| data         | id [*required*]            | string   | The ID associated with the Confluent resource.                                                     |
| data         | type [*required*]          | enum     | The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enable_custom_metrics": false,
      "id": "resource_id_abc123",
      "resource_type": "kafka",
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "resource_id_abc123",
    "type": "confluent-cloud-resources"
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
                  \# Path parametersexport account_id="CHANGE_ME"export resource_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}/resources/${resource_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "resource_type": "kafka"
    },
    "id": "resource-id-123",
    "type": "confluent-cloud-resources"
  }
}
EOF
                
##### 

```python
"""
Update resource in Confluent account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi
from datadog_api_client.v2.model.confluent_resource_request import ConfluentResourceRequest
from datadog_api_client.v2.model.confluent_resource_request_attributes import ConfluentResourceRequestAttributes
from datadog_api_client.v2.model.confluent_resource_request_data import ConfluentResourceRequestData
from datadog_api_client.v2.model.confluent_resource_type import ConfluentResourceType

body = ConfluentResourceRequest(
    data=ConfluentResourceRequestData(
        attributes=ConfluentResourceRequestAttributes(
            enable_custom_metrics=False,
            resource_type="kafka",
            tags=[
                "myTag",
                "myTag2:myValue",
            ],
        ),
        id="resource-id-123",
        type=ConfluentResourceType.CONFLUENT_CLOUD_RESOURCES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.update_confluent_resource(account_id="account_id", resource_id="resource_id", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update resource in Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new

body = DatadogAPIClient::V2::ConfluentResourceRequest.new({
  data: DatadogAPIClient::V2::ConfluentResourceRequestData.new({
    attributes: DatadogAPIClient::V2::ConfluentResourceRequestAttributes.new({
      enable_custom_metrics: false,
      resource_type: "kafka",
      tags: [
        "myTag",
        "myTag2:myValue",
      ],
    }),
    id: "resource-id-123",
    type: DatadogAPIClient::V2::ConfluentResourceType::CONFLUENT_CLOUD_RESOURCES,
  }),
})
p api_instance.update_confluent_resource("account_id", "resource_id", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Update resource in Confluent account returns "OK" response

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
	body := datadogV2.ConfluentResourceRequest{
		Data: datadogV2.ConfluentResourceRequestData{
			Attributes: datadogV2.ConfluentResourceRequestAttributes{
				EnableCustomMetrics: datadog.PtrBool(false),
				ResourceType:        "kafka",
				Tags: []string{
					"myTag",
					"myTag2:myValue",
				},
			},
			Id:   "resource-id-123",
			Type: datadogV2.CONFLUENTRESOURCETYPE_CONFLUENT_CLOUD_RESOURCES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewConfluentCloudApi(apiClient)
	resp, r, err := api.UpdateConfluentResource(ctx, "account_id", "resource_id", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConfluentCloudApi.UpdateConfluentResource`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ConfluentCloudApi.UpdateConfluentResource`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update resource in Confluent account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ConfluentCloudApi;
import com.datadog.api.client.v2.model.ConfluentResourceRequest;
import com.datadog.api.client.v2.model.ConfluentResourceRequestAttributes;
import com.datadog.api.client.v2.model.ConfluentResourceRequestData;
import com.datadog.api.client.v2.model.ConfluentResourceResponse;
import com.datadog.api.client.v2.model.ConfluentResourceType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ConfluentCloudApi apiInstance = new ConfluentCloudApi(defaultClient);

    ConfluentResourceRequest body =
        new ConfluentResourceRequest()
            .data(
                new ConfluentResourceRequestData()
                    .attributes(
                        new ConfluentResourceRequestAttributes()
                            .enableCustomMetrics(false)
                            .resourceType("kafka")
                            .tags(Arrays.asList("myTag", "myTag2:myValue")))
                    .id("resource-id-123")
                    .type(ConfluentResourceType.CONFLUENT_CLOUD_RESOURCES));

    try {
      ConfluentResourceResponse result =
          apiInstance.updateConfluentResource("account_id", "resource_id", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfluentCloudApi#updateConfluentResource");
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
// Update resource in Confluent account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_confluent_cloud::ConfluentCloudAPI;
use datadog_api_client::datadogV2::model::ConfluentResourceRequest;
use datadog_api_client::datadogV2::model::ConfluentResourceRequestAttributes;
use datadog_api_client::datadogV2::model::ConfluentResourceRequestData;
use datadog_api_client::datadogV2::model::ConfluentResourceType;

#[tokio::main]
async fn main() {
    let body = ConfluentResourceRequest::new(ConfluentResourceRequestData::new(
        ConfluentResourceRequestAttributes::new("kafka".to_string())
            .enable_custom_metrics(false)
            .tags(vec!["myTag".to_string(), "myTag2:myValue".to_string()]),
        "resource-id-123".to_string(),
        ConfluentResourceType::CONFLUENT_CLOUD_RESOURCES,
    ));
    let configuration = datadog::Configuration::new();
    let api = ConfluentCloudAPI::with_config(configuration);
    let resp = api
        .update_confluent_resource("account_id".to_string(), "resource_id".to_string(), body)
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
 * Update resource in Confluent account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ConfluentCloudApi(configuration);

const params: v2.ConfluentCloudApiUpdateConfluentResourceRequest = {
  body: {
    data: {
      attributes: {
        enableCustomMetrics: false,
        resourceType: "kafka",
        tags: ["myTag", "myTag2:myValue"],
      },
      id: "resource-id-123",
      type: "confluent-cloud-resources",
    },
  },
  accountId: "account_id",
  resourceId: "resource_id",
};

apiInstance
  .updateConfluentResource(params)
  .then((data: v2.ConfluentResourceResponse) => {
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

## Get resource from Confluent account{% #get-resource-from-confluent-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |

### Overview

Get a Confluent resource with the provided resource id for the account associated with the provided account ID. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                    |
| ----------------------------- | ------ | ------------------------------ |
| account_id [*required*]  | string | Confluent Account ID.          |
| resource_id [*required*] | string | Confluent Account Resource ID. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response schema when interacting with a Confluent resource.

| Parent field | Field                           | Type     | Description                                                                                        |
| ------------ | ------------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
|              | data                            | object   | Confluent Cloud resource data.                                                                     |
| data         | attributes [*required*]    | object   | Model representation of a Confluent Cloud resource.                                                |
| attributes   | enable_custom_metrics           | boolean  | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.                  |
| attributes   | id                              | string   | The ID associated with the Confluent resource.                                                     |
| attributes   | resource_type [*required*] | string   | The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.      |
| attributes   | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon. |
| data         | id [*required*]            | string   | The ID associated with the Confluent resource.                                                     |
| data         | type [*required*]          | enum     | The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enable_custom_metrics": false,
      "id": "resource_id_abc123",
      "resource_type": "kafka",
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "resource_id_abc123",
    "type": "confluent-cloud-resources"
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
                  \# Path parametersexport account_id="CHANGE_ME"export resource_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}/resources/${resource_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get resource from Confluent account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.get_confluent_resource(
        account_id="account_id",
        resource_id="resource_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get resource from Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new
p api_instance.get_confluent_resource("account_id", "resource_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get resource from Confluent account returns "OK" response

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
	api := datadogV2.NewConfluentCloudApi(apiClient)
	resp, r, err := api.GetConfluentResource(ctx, "account_id", "resource_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConfluentCloudApi.GetConfluentResource`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ConfluentCloudApi.GetConfluentResource`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get resource from Confluent account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ConfluentCloudApi;
import com.datadog.api.client.v2.model.ConfluentResourceResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ConfluentCloudApi apiInstance = new ConfluentCloudApi(defaultClient);

    try {
      ConfluentResourceResponse result =
          apiInstance.getConfluentResource("account_id", "resource_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfluentCloudApi#getConfluentResource");
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
// Get resource from Confluent account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_confluent_cloud::ConfluentCloudAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ConfluentCloudAPI::with_config(configuration);
    let resp = api
        .get_confluent_resource("account_id".to_string(), "resource_id".to_string())
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
 * Get resource from Confluent account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ConfluentCloudApi(configuration);

const params: v2.ConfluentCloudApiGetConfluentResourceRequest = {
  accountId: "account_id",
  resourceId: "resource_id",
};

apiInstance
  .getConfluentResource(params)
  .then((data: v2.ConfluentResourceResponse) => {
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

## Delete resource from Confluent account{% #delete-resource-from-confluent-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                                           |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id} |

### Overview

Delete a Confluent resource with the provided resource id for the account associated with the provided account ID. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                    |
| ----------------------------- | ------ | ------------------------------ |
| account_id [*required*]  | string | Confluent Account ID.          |
| resource_id [*required*] | string | Confluent Account Resource ID. |

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
                  \# Path parametersexport account_id="CHANGE_ME"export resource_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}/resources/${resource_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete resource from Confluent account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    api_instance.delete_confluent_resource(
        account_id="account_id",
        resource_id="resource_id",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete resource from Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new
api_instance.delete_confluent_resource("account_id", "resource_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete resource from Confluent account returns "OK" response

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
	api := datadogV2.NewConfluentCloudApi(apiClient)
	r, err := api.DeleteConfluentResource(ctx, "account_id", "resource_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConfluentCloudApi.DeleteConfluentResource`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete resource from Confluent account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ConfluentCloudApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ConfluentCloudApi apiInstance = new ConfluentCloudApi(defaultClient);

    try {
      apiInstance.deleteConfluentResource("account_id", "resource_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfluentCloudApi#deleteConfluentResource");
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
// Delete resource from Confluent account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_confluent_cloud::ConfluentCloudAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ConfluentCloudAPI::with_config(configuration);
    let resp = api
        .delete_confluent_resource("account_id".to_string(), "resource_id".to_string())
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
 * Delete resource from Confluent account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ConfluentCloudApi(configuration);

const params: v2.ConfluentCloudApiDeleteConfluentResourceRequest = {
  accountId: "account_id",
  resourceId: "resource_id",
};

apiInstance
  .deleteConfluentResource(params)
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

## Add resource to Confluent account{% #add-resource-to-confluent-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources |

### Overview

Create a Confluent resource for the account associated with the provided ID. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description           |
| ---------------------------- | ------ | --------------------- |
| account_id [*required*] | string | Confluent Account ID. |

### Request

#### Body Data (required)

Confluent payload

{% tab title="Model" %}

| Parent field | Field                           | Type     | Description                                                                                        |
| ------------ | ------------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
|              | data [*required*]          | object   | JSON:API request for updating a Confluent resource.                                                |
| data         | attributes [*required*]    | object   | Attributes object for updating a Confluent resource.                                               |
| attributes   | enable_custom_metrics           | boolean  | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.                  |
| attributes   | resource_type [*required*] | string   | The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.      |
| attributes   | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon. |
| data         | id [*required*]            | string   | The ID associated with a Confluent resource.                                                       |
| data         | type [*required*]          | enum     | The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "resource_type": "kafka",
      "tags": [
        "myTag",
        "myTag2:myValue"
      ],
      "enable_custom_metrics": false
    },
    "id": "exampleconfluentcloud",
    "type": "confluent-cloud-resources"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
Response schema when interacting with a Confluent resource.

| Parent field | Field                           | Type     | Description                                                                                        |
| ------------ | ------------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
|              | data                            | object   | Confluent Cloud resource data.                                                                     |
| data         | attributes [*required*]    | object   | Model representation of a Confluent Cloud resource.                                                |
| attributes   | enable_custom_metrics           | boolean  | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.                  |
| attributes   | id                              | string   | The ID associated with the Confluent resource.                                                     |
| attributes   | resource_type [*required*] | string   | The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.      |
| attributes   | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon. |
| data         | id [*required*]            | string   | The ID associated with the Confluent resource.                                                     |
| data         | type [*required*]          | enum     | The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enable_custom_metrics": false,
      "id": "resource_id_abc123",
      "resource_type": "kafka",
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "resource_id_abc123",
    "type": "confluent-cloud-resources"
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
                          \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}/resources" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "resource_type": "kafka",
      "tags": [
        "myTag",
        "myTag2:myValue"
      ],
      "enable_custom_metrics": false
    },
    "id": "exampleconfluentcloud",
    "type": "confluent-cloud-resources"
  }
}
EOF
                        
##### 

```go
// Add resource to Confluent account returns "OK" response

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
	// there is a valid "confluent_account" in the system
	ConfluentAccountDataID := os.Getenv("CONFLUENT_ACCOUNT_DATA_ID")

	body := datadogV2.ConfluentResourceRequest{
		Data: datadogV2.ConfluentResourceRequestData{
			Attributes: datadogV2.ConfluentResourceRequestAttributes{
				ResourceType: "kafka",
				Tags: []string{
					"myTag",
					"myTag2:myValue",
				},
				EnableCustomMetrics: datadog.PtrBool(false),
			},
			Id:   "exampleconfluentcloud",
			Type: datadogV2.CONFLUENTRESOURCETYPE_CONFLUENT_CLOUD_RESOURCES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewConfluentCloudApi(apiClient)
	resp, r, err := api.CreateConfluentResource(ctx, ConfluentAccountDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConfluentCloudApi.CreateConfluentResource`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ConfluentCloudApi.CreateConfluentResource`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Add resource to Confluent account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ConfluentCloudApi;
import com.datadog.api.client.v2.model.ConfluentResourceRequest;
import com.datadog.api.client.v2.model.ConfluentResourceRequestAttributes;
import com.datadog.api.client.v2.model.ConfluentResourceRequestData;
import com.datadog.api.client.v2.model.ConfluentResourceResponse;
import com.datadog.api.client.v2.model.ConfluentResourceType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ConfluentCloudApi apiInstance = new ConfluentCloudApi(defaultClient);

    // there is a valid "confluent_account" in the system
    String CONFLUENT_ACCOUNT_DATA_ID = System.getenv("CONFLUENT_ACCOUNT_DATA_ID");

    ConfluentResourceRequest body =
        new ConfluentResourceRequest()
            .data(
                new ConfluentResourceRequestData()
                    .attributes(
                        new ConfluentResourceRequestAttributes()
                            .resourceType("kafka")
                            .tags(Arrays.asList("myTag", "myTag2:myValue"))
                            .enableCustomMetrics(false))
                    .id("exampleconfluentcloud")
                    .type(ConfluentResourceType.CONFLUENT_CLOUD_RESOURCES));

    try {
      ConfluentResourceResponse result =
          apiInstance.createConfluentResource(CONFLUENT_ACCOUNT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfluentCloudApi#createConfluentResource");
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
Add resource to Confluent account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi
from datadog_api_client.v2.model.confluent_resource_request import ConfluentResourceRequest
from datadog_api_client.v2.model.confluent_resource_request_attributes import ConfluentResourceRequestAttributes
from datadog_api_client.v2.model.confluent_resource_request_data import ConfluentResourceRequestData
from datadog_api_client.v2.model.confluent_resource_type import ConfluentResourceType

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ID = environ["CONFLUENT_ACCOUNT_DATA_ID"]

body = ConfluentResourceRequest(
    data=ConfluentResourceRequestData(
        attributes=ConfluentResourceRequestAttributes(
            resource_type="kafka",
            tags=[
                "myTag",
                "myTag2:myValue",
            ],
            enable_custom_metrics=False,
        ),
        id="exampleconfluentcloud",
        type=ConfluentResourceType.CONFLUENT_CLOUD_RESOURCES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.create_confluent_resource(account_id=CONFLUENT_ACCOUNT_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Add resource to Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ID = ENV["CONFLUENT_ACCOUNT_DATA_ID"]

body = DatadogAPIClient::V2::ConfluentResourceRequest.new({
  data: DatadogAPIClient::V2::ConfluentResourceRequestData.new({
    attributes: DatadogAPIClient::V2::ConfluentResourceRequestAttributes.new({
      resource_type: "kafka",
      tags: [
        "myTag",
        "myTag2:myValue",
      ],
      enable_custom_metrics: false,
    }),
    id: "exampleconfluentcloud",
    type: DatadogAPIClient::V2::ConfluentResourceType::CONFLUENT_CLOUD_RESOURCES,
  }),
})
p api_instance.create_confluent_resource(CONFLUENT_ACCOUNT_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Add resource to Confluent account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_confluent_cloud::ConfluentCloudAPI;
use datadog_api_client::datadogV2::model::ConfluentResourceRequest;
use datadog_api_client::datadogV2::model::ConfluentResourceRequestAttributes;
use datadog_api_client::datadogV2::model::ConfluentResourceRequestData;
use datadog_api_client::datadogV2::model::ConfluentResourceType;

#[tokio::main]
async fn main() {
    // there is a valid "confluent_account" in the system
    let confluent_account_data_id = std::env::var("CONFLUENT_ACCOUNT_DATA_ID").unwrap();
    let body = ConfluentResourceRequest::new(ConfluentResourceRequestData::new(
        ConfluentResourceRequestAttributes::new("kafka".to_string())
            .enable_custom_metrics(false)
            .tags(vec!["myTag".to_string(), "myTag2:myValue".to_string()]),
        "exampleconfluentcloud".to_string(),
        ConfluentResourceType::CONFLUENT_CLOUD_RESOURCES,
    ));
    let configuration = datadog::Configuration::new();
    let api = ConfluentCloudAPI::with_config(configuration);
    let resp = api
        .create_confluent_resource(confluent_account_data_id.clone(), body)
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
 * Add resource to Confluent account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ConfluentCloudApi(configuration);

// there is a valid "confluent_account" in the system
const CONFLUENT_ACCOUNT_DATA_ID = process.env
  .CONFLUENT_ACCOUNT_DATA_ID as string;

const params: v2.ConfluentCloudApiCreateConfluentResourceRequest = {
  body: {
    data: {
      attributes: {
        resourceType: "kafka",
        tags: ["myTag", "myTag2:myValue"],
        enableCustomMetrics: false,
      },
      id: "exampleconfluentcloud",
      type: "confluent-cloud-resources",
    },
  },
  accountId: CONFLUENT_ACCOUNT_DATA_ID,
};

apiInstance
  .createConfluentResource(params)
  .then((data: v2.ConfluentResourceResponse) => {
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

## List Confluent Account resources{% #list-confluent-account-resources %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                          |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources |

### Overview

Get a Confluent resource for the account associated with the provided ID. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description           |
| ---------------------------- | ------ | --------------------- |
| account_id [*required*] | string | Confluent Account ID. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response schema when interacting with a list of Confluent resources.

| Parent field | Field                           | Type     | Description                                                                                        |
| ------------ | ------------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
|              | data                            | [object] | The JSON:API data attribute.                                                                       |
| data         | attributes [*required*]    | object   | Model representation of a Confluent Cloud resource.                                                |
| attributes   | enable_custom_metrics           | boolean  | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.                  |
| attributes   | id                              | string   | The ID associated with the Confluent resource.                                                     |
| attributes   | resource_type [*required*] | string   | The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.      |
| attributes   | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon. |
| data         | id [*required*]            | string   | The ID associated with the Confluent resource.                                                     |
| data         | type [*required*]          | enum     | The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "enable_custom_metrics": false,
        "id": "resource_id_abc123",
        "resource_type": "kafka",
        "tags": [
          "myTag",
          "myTag2:myValue"
        ]
      },
      "id": "resource_id_abc123",
      "type": "confluent-cloud-resources"
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
                  \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}/resources" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List Confluent Account resources returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.list_confluent_resource(
        account_id="account_id",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List Confluent Account resources returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new
p api_instance.list_confluent_resource("account_id")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List Confluent Account resources returns "OK" response

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
	api := datadogV2.NewConfluentCloudApi(apiClient)
	resp, r, err := api.ListConfluentResource(ctx, "account_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConfluentCloudApi.ListConfluentResource`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ConfluentCloudApi.ListConfluentResource`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List Confluent Account resources returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ConfluentCloudApi;
import com.datadog.api.client.v2.model.ConfluentResourcesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ConfluentCloudApi apiInstance = new ConfluentCloudApi(defaultClient);

    try {
      ConfluentResourcesResponse result = apiInstance.listConfluentResource("account_id");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfluentCloudApi#listConfluentResource");
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
// List Confluent Account resources returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_confluent_cloud::ConfluentCloudAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ConfluentCloudAPI::with_config(configuration);
    let resp = api.list_confluent_resource("account_id".to_string()).await;
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
 * List Confluent Account resources returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ConfluentCloudApi(configuration);

const params: v2.ConfluentCloudApiListConfluentResourceRequest = {
  accountId: "account_id",
};

apiInstance
  .listConfluentResource(params)
  .then((data: v2.ConfluentResourcesResponse) => {
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

## Update Confluent account{% #update-confluent-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |

### Overview

Update the Confluent account with the provided account ID. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description           |
| ---------------------------- | ------ | --------------------- |
| account_id [*required*] | string | Confluent Account ID. |

### Request

#### Body Data (required)

Confluent payload

{% tab title="Model" %}

| Parent field | Field                        | Type     | Description                                                                                                                  |
| ------------ | ---------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object   | Data object for updating a Confluent account.                                                                                |
| data         | attributes [*required*] | object   | Attributes object for updating a Confluent account.                                                                          |
| attributes   | api_key [*required*]    | string   | The API key associated with your Confluent account.                                                                          |
| attributes   | api_secret [*required*] | string   | The API secret associated with your Confluent account.                                                                       |
| attributes   | tags                         | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.                           |
| data         | type [*required*]       | enum     | The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "api_key": "TESTAPIKEY123",
      "api_secret": "update-secret",
      "tags": [
        "updated_tag:val"
      ]
    },
    "type": "confluent-cloud-accounts"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting a Confluent account.

| Parent field | Field                           | Type     | Description                                                                                                                  |
| ------------ | ------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
|              | data                            | object   | An API key and API secret pair that represents a Confluent account.                                                          |
| data         | attributes [*required*]    | object   | The attributes of a Confluent account.                                                                                       |
| attributes   | api_key [*required*]       | string   | The API key associated with your Confluent account.                                                                          |
| attributes   | resources                       | [object] | A list of Confluent resources associated with the Confluent account.                                                         |
| resources    | enable_custom_metrics           | boolean  | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.                                            |
| resources    | id                              | string   | The ID associated with the Confluent resource.                                                                               |
| resources    | resource_type [*required*] | string   | The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.                                |
| resources    | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.                           |
| attributes   | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.                           |
| data         | id [*required*]            | string   | A randomly generated ID associated with a Confluent account.                                                                 |
| data         | type [*required*]          | enum     | The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "api_key": "TESTAPIKEY123",
      "resources": [
        {
          "enable_custom_metrics": false,
          "id": "resource_id_abc123",
          "resource_type": "kafka",
          "tags": [
            "myTag",
            "myTag2:myValue"
          ]
        }
      ],
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "account_id_abc123",
    "type": "confluent-cloud-accounts"
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
                          \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "api_key": "TESTAPIKEY123",
      "api_secret": "update-secret",
      "tags": [
        "updated_tag:val"
      ]
    },
    "type": "confluent-cloud-accounts"
  }
}
EOF
                        
##### 

```go
// Update Confluent account returns "OK" response

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
	// there is a valid "confluent_account" in the system
	ConfluentAccountDataAttributesAPIKey := os.Getenv("CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY")
	ConfluentAccountDataID := os.Getenv("CONFLUENT_ACCOUNT_DATA_ID")

	body := datadogV2.ConfluentAccountUpdateRequest{
		Data: datadogV2.ConfluentAccountUpdateRequestData{
			Attributes: datadogV2.ConfluentAccountUpdateRequestAttributes{
				ApiKey:    ConfluentAccountDataAttributesAPIKey,
				ApiSecret: "update-secret",
				Tags: []string{
					"updated_tag:val",
				},
			},
			Type: datadogV2.CONFLUENTACCOUNTTYPE_CONFLUENT_CLOUD_ACCOUNTS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewConfluentCloudApi(apiClient)
	resp, r, err := api.UpdateConfluentAccount(ctx, ConfluentAccountDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConfluentCloudApi.UpdateConfluentAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ConfluentCloudApi.UpdateConfluentAccount`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update Confluent account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ConfluentCloudApi;
import com.datadog.api.client.v2.model.ConfluentAccountResponse;
import com.datadog.api.client.v2.model.ConfluentAccountType;
import com.datadog.api.client.v2.model.ConfluentAccountUpdateRequest;
import com.datadog.api.client.v2.model.ConfluentAccountUpdateRequestAttributes;
import com.datadog.api.client.v2.model.ConfluentAccountUpdateRequestData;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ConfluentCloudApi apiInstance = new ConfluentCloudApi(defaultClient);

    // there is a valid "confluent_account" in the system
    String CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY =
        System.getenv("CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY");
    String CONFLUENT_ACCOUNT_DATA_ID = System.getenv("CONFLUENT_ACCOUNT_DATA_ID");

    ConfluentAccountUpdateRequest body =
        new ConfluentAccountUpdateRequest()
            .data(
                new ConfluentAccountUpdateRequestData()
                    .attributes(
                        new ConfluentAccountUpdateRequestAttributes()
                            .apiKey(CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY)
                            .apiSecret("update-secret")
                            .tags(Collections.singletonList("updated_tag:val")))
                    .type(ConfluentAccountType.CONFLUENT_CLOUD_ACCOUNTS));

    try {
      ConfluentAccountResponse result =
          apiInstance.updateConfluentAccount(CONFLUENT_ACCOUNT_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfluentCloudApi#updateConfluentAccount");
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
Update Confluent account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi
from datadog_api_client.v2.model.confluent_account_type import ConfluentAccountType
from datadog_api_client.v2.model.confluent_account_update_request import ConfluentAccountUpdateRequest
from datadog_api_client.v2.model.confluent_account_update_request_attributes import (
    ConfluentAccountUpdateRequestAttributes,
)
from datadog_api_client.v2.model.confluent_account_update_request_data import ConfluentAccountUpdateRequestData

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY = environ["CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY"]
CONFLUENT_ACCOUNT_DATA_ID = environ["CONFLUENT_ACCOUNT_DATA_ID"]

body = ConfluentAccountUpdateRequest(
    data=ConfluentAccountUpdateRequestData(
        attributes=ConfluentAccountUpdateRequestAttributes(
            api_key=CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY,
            api_secret="update-secret",
            tags=[
                "updated_tag:val",
            ],
        ),
        type=ConfluentAccountType.CONFLUENT_CLOUD_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.update_confluent_account(account_id=CONFLUENT_ACCOUNT_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY = ENV["CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY"]
CONFLUENT_ACCOUNT_DATA_ID = ENV["CONFLUENT_ACCOUNT_DATA_ID"]

body = DatadogAPIClient::V2::ConfluentAccountUpdateRequest.new({
  data: DatadogAPIClient::V2::ConfluentAccountUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::ConfluentAccountUpdateRequestAttributes.new({
      api_key: CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY,
      api_secret: "update-secret",
      tags: [
        "updated_tag:val",
      ],
    }),
    type: DatadogAPIClient::V2::ConfluentAccountType::CONFLUENT_CLOUD_ACCOUNTS,
  }),
})
p api_instance.update_confluent_account(CONFLUENT_ACCOUNT_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update Confluent account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_confluent_cloud::ConfluentCloudAPI;
use datadog_api_client::datadogV2::model::ConfluentAccountType;
use datadog_api_client::datadogV2::model::ConfluentAccountUpdateRequest;
use datadog_api_client::datadogV2::model::ConfluentAccountUpdateRequestAttributes;
use datadog_api_client::datadogV2::model::ConfluentAccountUpdateRequestData;

#[tokio::main]
async fn main() {
    // there is a valid "confluent_account" in the system
    let confluent_account_data_attributes_api_key =
        std::env::var("CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY").unwrap();
    let confluent_account_data_id = std::env::var("CONFLUENT_ACCOUNT_DATA_ID").unwrap();
    let body = ConfluentAccountUpdateRequest::new(ConfluentAccountUpdateRequestData::new(
        ConfluentAccountUpdateRequestAttributes::new(
            confluent_account_data_attributes_api_key.clone(),
            "update-secret".to_string(),
        )
        .tags(vec!["updated_tag:val".to_string()]),
        ConfluentAccountType::CONFLUENT_CLOUD_ACCOUNTS,
    ));
    let configuration = datadog::Configuration::new();
    let api = ConfluentCloudAPI::with_config(configuration);
    let resp = api
        .update_confluent_account(confluent_account_data_id.clone(), body)
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
 * Update Confluent account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ConfluentCloudApi(configuration);

// there is a valid "confluent_account" in the system
const CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY = process.env
  .CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY as string;
const CONFLUENT_ACCOUNT_DATA_ID = process.env
  .CONFLUENT_ACCOUNT_DATA_ID as string;

const params: v2.ConfluentCloudApiUpdateConfluentAccountRequest = {
  body: {
    data: {
      attributes: {
        apiKey: CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY,
        apiSecret: "update-secret",
        tags: ["updated_tag:val"],
      },
      type: "confluent-cloud-accounts",
    },
  },
  accountId: CONFLUENT_ACCOUNT_DATA_ID,
};

apiInstance
  .updateConfluentAccount(params)
  .then((data: v2.ConfluentAccountResponse) => {
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

## Get Confluent account{% #get-confluent-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |

### Overview

Get the Confluent account with the provided account ID. This endpoint requires the `integrations_read` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description           |
| ---------------------------- | ------ | --------------------- |
| account_id [*required*] | string | Confluent Account ID. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The expected response schema when getting a Confluent account.

| Parent field | Field                           | Type     | Description                                                                                                                  |
| ------------ | ------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
|              | data                            | object   | An API key and API secret pair that represents a Confluent account.                                                          |
| data         | attributes [*required*]    | object   | The attributes of a Confluent account.                                                                                       |
| attributes   | api_key [*required*]       | string   | The API key associated with your Confluent account.                                                                          |
| attributes   | resources                       | [object] | A list of Confluent resources associated with the Confluent account.                                                         |
| resources    | enable_custom_metrics           | boolean  | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.                                            |
| resources    | id                              | string   | The ID associated with the Confluent resource.                                                                               |
| resources    | resource_type [*required*] | string   | The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.                                |
| resources    | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.                           |
| attributes   | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.                           |
| data         | id [*required*]            | string   | A randomly generated ID associated with a Confluent account.                                                                 |
| data         | type [*required*]          | enum     | The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "api_key": "TESTAPIKEY123",
      "resources": [
        {
          "enable_custom_metrics": false,
          "id": "resource_id_abc123",
          "resource_type": "kafka",
          "tags": [
            "myTag",
            "myTag2:myValue"
          ]
        }
      ],
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "account_id_abc123",
    "type": "confluent-cloud-accounts"
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
                  \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get Confluent account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ID = environ["CONFLUENT_ACCOUNT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.get_confluent_account(
        account_id=CONFLUENT_ACCOUNT_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Get Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ID = ENV["CONFLUENT_ACCOUNT_DATA_ID"]
p api_instance.get_confluent_account(CONFLUENT_ACCOUNT_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Get Confluent account returns "OK" response

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
	// there is a valid "confluent_account" in the system
	ConfluentAccountDataID := os.Getenv("CONFLUENT_ACCOUNT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewConfluentCloudApi(apiClient)
	resp, r, err := api.GetConfluentAccount(ctx, ConfluentAccountDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConfluentCloudApi.GetConfluentAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ConfluentCloudApi.GetConfluentAccount`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Get Confluent account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ConfluentCloudApi;
import com.datadog.api.client.v2.model.ConfluentAccountResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ConfluentCloudApi apiInstance = new ConfluentCloudApi(defaultClient);

    // there is a valid "confluent_account" in the system
    String CONFLUENT_ACCOUNT_DATA_ID = System.getenv("CONFLUENT_ACCOUNT_DATA_ID");

    try {
      ConfluentAccountResponse result = apiInstance.getConfluentAccount(CONFLUENT_ACCOUNT_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfluentCloudApi#getConfluentAccount");
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
// Get Confluent account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_confluent_cloud::ConfluentCloudAPI;

#[tokio::main]
async fn main() {
    // there is a valid "confluent_account" in the system
    let confluent_account_data_id = std::env::var("CONFLUENT_ACCOUNT_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ConfluentCloudAPI::with_config(configuration);
    let resp = api
        .get_confluent_account(confluent_account_data_id.clone())
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
 * Get Confluent account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ConfluentCloudApi(configuration);

// there is a valid "confluent_account" in the system
const CONFLUENT_ACCOUNT_DATA_ID = process.env
  .CONFLUENT_ACCOUNT_DATA_ID as string;

const params: v2.ConfluentCloudApiGetConfluentAccountRequest = {
  accountId: CONFLUENT_ACCOUNT_DATA_ID,
};

apiInstance
  .getConfluentAccount(params)
  .then((data: v2.ConfluentAccountResponse) => {
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

## Delete Confluent account{% #delete-confluent-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id} |

### Overview

Delete a Confluent account with the provided account ID. This endpoint requires the `manage_integrations` permission.

### Arguments

#### Path Parameters

| Name                         | Type   | Description           |
| ---------------------------- | ------ | --------------------- |
| account_id [*required*] | string | Confluent Account ID. |

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
                  \# Path parametersexport account_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete Confluent account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ID = environ["CONFLUENT_ACCOUNT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    api_instance.delete_confluent_account(
        account_id=CONFLUENT_ACCOUNT_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ID = ENV["CONFLUENT_ACCOUNT_DATA_ID"]
api_instance.delete_confluent_account(CONFLUENT_ACCOUNT_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Delete Confluent account returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "confluent_account" in the system
	ConfluentAccountDataID := os.Getenv("CONFLUENT_ACCOUNT_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewConfluentCloudApi(apiClient)
	r, err := api.DeleteConfluentAccount(ctx, ConfluentAccountDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConfluentCloudApi.DeleteConfluentAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete Confluent account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ConfluentCloudApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ConfluentCloudApi apiInstance = new ConfluentCloudApi(defaultClient);

    // there is a valid "confluent_account" in the system
    String CONFLUENT_ACCOUNT_DATA_ID = System.getenv("CONFLUENT_ACCOUNT_DATA_ID");

    try {
      apiInstance.deleteConfluentAccount(CONFLUENT_ACCOUNT_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfluentCloudApi#deleteConfluentAccount");
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
// Delete Confluent account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_confluent_cloud::ConfluentCloudAPI;

#[tokio::main]
async fn main() {
    // there is a valid "confluent_account" in the system
    let confluent_account_data_id = std::env::var("CONFLUENT_ACCOUNT_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = ConfluentCloudAPI::with_config(configuration);
    let resp = api
        .delete_confluent_account(confluent_account_data_id.clone())
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
 * Delete Confluent account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ConfluentCloudApi(configuration);

// there is a valid "confluent_account" in the system
const CONFLUENT_ACCOUNT_DATA_ID = process.env
  .CONFLUENT_ACCOUNT_DATA_ID as string;

const params: v2.ConfluentCloudApiDeleteConfluentAccountRequest = {
  accountId: CONFLUENT_ACCOUNT_DATA_ID,
};

apiInstance
  .deleteConfluentAccount(params)
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

## Add Confluent account{% #add-confluent-account %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                    |
| ----------------- | ------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts |

### Overview

Create a Confluent account. This endpoint requires the `manage_integrations` permission.

### Request

#### Body Data (required)

Confluent payload

{% tab title="Model" %}

| Parent field | Field                           | Type     | Description                                                                                                                  |
| ------------ | ------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]          | object   | The data body for adding a Confluent account.                                                                                |
| data         | attributes [*required*]    | object   | Attributes associated with the account creation request.                                                                     |
| attributes   | api_key [*required*]       | string   | The API key associated with your Confluent account.                                                                          |
| attributes   | api_secret [*required*]    | string   | The API secret associated with your Confluent account.                                                                       |
| attributes   | resources                       | [object] | A list of Confluent resources associated with the Confluent account.                                                         |
| resources    | enable_custom_metrics           | boolean  | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.                                            |
| resources    | id                              | string   | The ID associated with a Confluent resource.                                                                                 |
| resources    | resource_type [*required*] | string   | The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.                                |
| resources    | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.                           |
| attributes   | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.                           |
| data         | type [*required*]          | enum     | The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "api_key": "TESTAPIKEY123",
      "api_secret": "test-api-secret-123",
      "resources": [
        {
          "enable_custom_metrics": false,
          "id": "resource-id-123",
          "resource_type": "kafka",
          "tags": [
            "myTag",
            "myTag2:myValue"
          ]
        }
      ],
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "type": "confluent-cloud-accounts"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
The expected response schema when getting a Confluent account.

| Parent field | Field                           | Type     | Description                                                                                                                  |
| ------------ | ------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
|              | data                            | object   | An API key and API secret pair that represents a Confluent account.                                                          |
| data         | attributes [*required*]    | object   | The attributes of a Confluent account.                                                                                       |
| attributes   | api_key [*required*]       | string   | The API key associated with your Confluent account.                                                                          |
| attributes   | resources                       | [object] | A list of Confluent resources associated with the Confluent account.                                                         |
| resources    | enable_custom_metrics           | boolean  | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.                                            |
| resources    | id                              | string   | The ID associated with the Confluent resource.                                                                               |
| resources    | resource_type [*required*] | string   | The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.                                |
| resources    | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.                           |
| attributes   | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.                           |
| data         | id [*required*]            | string   | A randomly generated ID associated with a Confluent account.                                                                 |
| data         | type [*required*]          | enum     | The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "api_key": "TESTAPIKEY123",
      "resources": [
        {
          "enable_custom_metrics": false,
          "id": "resource_id_abc123",
          "resource_type": "kafka",
          "tags": [
            "myTag",
            "myTag2:myValue"
          ]
        }
      ],
      "tags": [
        "myTag",
        "myTag2:myValue"
      ]
    },
    "id": "account_id_abc123",
    "type": "confluent-cloud-accounts"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "api_key": "TESTAPIKEY123",
      "api_secret": "test-api-secret-123",
      "resources": [
        {
          "resource_type": "kafka"
        }
      ]
    },
    "type": "confluent-cloud-accounts"
  }
}
EOF
                
##### 

```python
"""
Add Confluent account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi
from datadog_api_client.v2.model.confluent_account_create_request import ConfluentAccountCreateRequest
from datadog_api_client.v2.model.confluent_account_create_request_attributes import (
    ConfluentAccountCreateRequestAttributes,
)
from datadog_api_client.v2.model.confluent_account_create_request_data import ConfluentAccountCreateRequestData
from datadog_api_client.v2.model.confluent_account_resource_attributes import ConfluentAccountResourceAttributes
from datadog_api_client.v2.model.confluent_account_type import ConfluentAccountType

body = ConfluentAccountCreateRequest(
    data=ConfluentAccountCreateRequestData(
        attributes=ConfluentAccountCreateRequestAttributes(
            api_key="TESTAPIKEY123",
            api_secret="test-api-secret-123",
            resources=[
                ConfluentAccountResourceAttributes(
                    enable_custom_metrics=False,
                    id="resource-id-123",
                    resource_type="kafka",
                    tags=[
                        "myTag",
                        "myTag2:myValue",
                    ],
                ),
            ],
            tags=[
                "myTag",
                "myTag2:myValue",
            ],
        ),
        type=ConfluentAccountType.CONFLUENT_CLOUD_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.create_confluent_account(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Add Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new

body = DatadogAPIClient::V2::ConfluentAccountCreateRequest.new({
  data: DatadogAPIClient::V2::ConfluentAccountCreateRequestData.new({
    attributes: DatadogAPIClient::V2::ConfluentAccountCreateRequestAttributes.new({
      api_key: "TESTAPIKEY123",
      api_secret: "test-api-secret-123",
      resources: [
        DatadogAPIClient::V2::ConfluentAccountResourceAttributes.new({
          enable_custom_metrics: false,
          id: "resource-id-123",
          resource_type: "kafka",
          tags: [
            "myTag",
            "myTag2:myValue",
          ],
        }),
      ],
      tags: [
        "myTag",
        "myTag2:myValue",
      ],
    }),
    type: DatadogAPIClient::V2::ConfluentAccountType::CONFLUENT_CLOUD_ACCOUNTS,
  }),
})
p api_instance.create_confluent_account(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// Add Confluent account returns "OK" response

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
	body := datadogV2.ConfluentAccountCreateRequest{
		Data: datadogV2.ConfluentAccountCreateRequestData{
			Attributes: datadogV2.ConfluentAccountCreateRequestAttributes{
				ApiKey:    "TESTAPIKEY123",
				ApiSecret: "test-api-secret-123",
				Resources: []datadogV2.ConfluentAccountResourceAttributes{
					{
						EnableCustomMetrics: datadog.PtrBool(false),
						Id:                  datadog.PtrString("resource-id-123"),
						ResourceType:        "kafka",
						Tags: []string{
							"myTag",
							"myTag2:myValue",
						},
					},
				},
				Tags: []string{
					"myTag",
					"myTag2:myValue",
				},
			},
			Type: datadogV2.CONFLUENTACCOUNTTYPE_CONFLUENT_CLOUD_ACCOUNTS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewConfluentCloudApi(apiClient)
	resp, r, err := api.CreateConfluentAccount(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConfluentCloudApi.CreateConfluentAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ConfluentCloudApi.CreateConfluentAccount`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Add Confluent account returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ConfluentCloudApi;
import com.datadog.api.client.v2.model.ConfluentAccountCreateRequest;
import com.datadog.api.client.v2.model.ConfluentAccountCreateRequestAttributes;
import com.datadog.api.client.v2.model.ConfluentAccountCreateRequestData;
import com.datadog.api.client.v2.model.ConfluentAccountResourceAttributes;
import com.datadog.api.client.v2.model.ConfluentAccountResponse;
import com.datadog.api.client.v2.model.ConfluentAccountType;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ConfluentCloudApi apiInstance = new ConfluentCloudApi(defaultClient);

    ConfluentAccountCreateRequest body =
        new ConfluentAccountCreateRequest()
            .data(
                new ConfluentAccountCreateRequestData()
                    .attributes(
                        new ConfluentAccountCreateRequestAttributes()
                            .apiKey("TESTAPIKEY123")
                            .apiSecret("test-api-secret-123")
                            .resources(
                                Collections.singletonList(
                                    new ConfluentAccountResourceAttributes()
                                        .enableCustomMetrics(false)
                                        .id("resource-id-123")
                                        .resourceType("kafka")
                                        .tags(Arrays.asList("myTag", "myTag2:myValue"))))
                            .tags(Arrays.asList("myTag", "myTag2:myValue")))
                    .type(ConfluentAccountType.CONFLUENT_CLOUD_ACCOUNTS));

    try {
      ConfluentAccountResponse result = apiInstance.createConfluentAccount(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfluentCloudApi#createConfluentAccount");
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
// Add Confluent account returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_confluent_cloud::ConfluentCloudAPI;
use datadog_api_client::datadogV2::model::ConfluentAccountCreateRequest;
use datadog_api_client::datadogV2::model::ConfluentAccountCreateRequestAttributes;
use datadog_api_client::datadogV2::model::ConfluentAccountCreateRequestData;
use datadog_api_client::datadogV2::model::ConfluentAccountResourceAttributes;
use datadog_api_client::datadogV2::model::ConfluentAccountType;

#[tokio::main]
async fn main() {
    let body = ConfluentAccountCreateRequest::new(ConfluentAccountCreateRequestData::new(
        ConfluentAccountCreateRequestAttributes::new(
            "TESTAPIKEY123".to_string(),
            "test-api-secret-123".to_string(),
        )
        .resources(vec![ConfluentAccountResourceAttributes::new(
            "kafka".to_string(),
        )
        .enable_custom_metrics(false)
        .id("resource-id-123".to_string())
        .tags(vec!["myTag".to_string(), "myTag2:myValue".to_string()])])
        .tags(vec!["myTag".to_string(), "myTag2:myValue".to_string()]),
        ConfluentAccountType::CONFLUENT_CLOUD_ACCOUNTS,
    ));
    let configuration = datadog::Configuration::new();
    let api = ConfluentCloudAPI::with_config(configuration);
    let resp = api.create_confluent_account(body).await;
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
 * Add Confluent account returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ConfluentCloudApi(configuration);

const params: v2.ConfluentCloudApiCreateConfluentAccountRequest = {
  body: {
    data: {
      attributes: {
        apiKey: "TESTAPIKEY123",
        apiSecret: "test-api-secret-123",
        resources: [
          {
            enableCustomMetrics: false,
            id: "resource-id-123",
            resourceType: "kafka",
            tags: ["myTag", "myTag2:myValue"],
          },
        ],
        tags: ["myTag", "myTag2:myValue"],
      },
      type: "confluent-cloud-accounts",
    },
  },
};

apiInstance
  .createConfluentAccount(params)
  .then((data: v2.ConfluentAccountResponse) => {
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

## List Confluent accounts{% #list-confluent-accounts %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                   |
| ----------------- | ------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts |

### Overview

List Confluent accounts. This endpoint requires the `integrations_read` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Confluent account returned by the API.

| Parent field | Field                           | Type     | Description                                                                                                                  |
| ------------ | ------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
|              | data                            | [object] | The Confluent account.                                                                                                       |
| data         | attributes [*required*]    | object   | The attributes of a Confluent account.                                                                                       |
| attributes   | api_key [*required*]       | string   | The API key associated with your Confluent account.                                                                          |
| attributes   | resources                       | [object] | A list of Confluent resources associated with the Confluent account.                                                         |
| resources    | enable_custom_metrics           | boolean  | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.                                            |
| resources    | id                              | string   | The ID associated with the Confluent resource.                                                                               |
| resources    | resource_type [*required*] | string   | The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.                                |
| resources    | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.                           |
| attributes   | tags                            | [string] | A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.                           |
| data         | id [*required*]            | string   | A randomly generated ID associated with a Confluent account.                                                                 |
| data         | type [*required*]          | enum     | The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "api_key": "TESTAPIKEY123",
        "resources": [
          {
            "enable_custom_metrics": false,
            "id": "resource_id_abc123",
            "resource_type": "kafka",
            "tags": [
              "myTag",
              "myTag2:myValue"
            ]
          }
        ],
        "tags": [
          "myTag",
          "myTag2:myValue"
        ]
      },
      "id": "account_id_abc123",
      "type": "confluent-cloud-accounts"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List Confluent accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.list_confluent_account()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# List Confluent accounts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new
p api_instance.list_confluent_account()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```go
// List Confluent accounts returns "OK" response

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
	api := datadogV2.NewConfluentCloudApi(apiClient)
	resp, r, err := api.ListConfluentAccount(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConfluentCloudApi.ListConfluentAccount`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ConfluentCloudApi.ListConfluentAccount`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// List Confluent accounts returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ConfluentCloudApi;
import com.datadog.api.client.v2.model.ConfluentAccountsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ConfluentCloudApi apiInstance = new ConfluentCloudApi(defaultClient);

    try {
      ConfluentAccountsResponse result = apiInstance.listConfluentAccount();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfluentCloudApi#listConfluentAccount");
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
// List Confluent accounts returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_confluent_cloud::ConfluentCloudAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ConfluentCloudAPI::with_config(configuration);
    let resp = api.list_confluent_account().await;
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
 * List Confluent accounts returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ConfluentCloudApi(configuration);

apiInstance
  .listConfluentAccount()
  .then((data: v2.ConfluentAccountsResponse) => {
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
