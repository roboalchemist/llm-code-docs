# Source: https://docs.datadoghq.com/api/latest/logs-custom-destinations.md

---
title: Logs Custom Destinations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Logs Custom Destinations
---

# Logs Custom Destinations

Custom Destinations forward all the logs ingested to an external destination.

**Note**: Log forwarding is not available for the Government (US1-FED) site. Contact your account representative for more information.

See the [Custom Destinations Page](https://app.datadoghq.com/logs/pipelines/log-forwarding/custom-destinations) for a list of the custom destinations currently configured in web UI.

## Get all custom destinations{% #get-all-custom-destinations %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/custom-destinations |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/custom-destinations |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/custom-destinations      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/custom-destinations      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/custom-destinations     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/custom-destinations |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations |

### Overview

Get the list of configured custom destinations in your organization with their definitions. This endpoint requires any of the following permissions:
`logs_read_config``logs_read_data`


### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The available custom destinations.

| Parent field          | Field                                      | Type          | Description                                                                                                                                                                                                                      |
| --------------------- | ------------------------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                                       | [object]      | A list of custom destinations.                                                                                                                                                                                                   |
| data                  | attributes                                 | object        | The attributes associated with the custom destination.                                                                                                                                                                           |
| attributes            | enabled                                    | boolean       | Whether logs matching this custom destination should be forwarded or not.                                                                                                                                                        |
| attributes            | forward_tags                               | boolean       | Whether tags from the forwarded logs should be forwarded or not.                                                                                                                                                                 |
| attributes            | forward_tags_restriction_list              | [string]      | List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be filtered.                                                                                                                          | An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter. |
| attributes            | forward_tags_restriction_list_type         | enum          | How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.                                      | `BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST`                |
| attributes            | forwarder_destination                      |  <oneOf> | A custom destination's location to forward logs.                                                                                                                                                                                 |
| forwarder_destination | Option 1                                   | object        | The HTTP destination.                                                                                                                                                                                                            |
| Option 1              | auth [*required*]                     |  <oneOf> | Authentication method of the HTTP requests.                                                                                                                                                                                      |
| auth                  | Option 1                                   | object        | Basic access authentication.                                                                                                                                                                                                     |
| Option 1              | type [*required*]                     | enum          | Type of the basic access authentication. Allowed enum values: `basic`                                                                                                                                                            |
| auth                  | Option 2                                   | object        | Custom header access authentication.                                                                                                                                                                                             |
| Option 2              | header_name [*required*]              | string        | The header name of the authentication.                                                                                                                                                                                           |
| Option 2              | type [*required*]                     | enum          | Type of the custom header access authentication. Allowed enum values: `custom_header`                                                                                                                                            |
| Option 1              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 1              | type [*required*]                     | enum          | Type of the HTTP destination. Allowed enum values: `http`                                                                                                                                                                        |
| forwarder_destination | Option 2                                   | object        | The Splunk HTTP Event Collector (HEC) destination.                                                                                                                                                                               |
| Option 2              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 2              | type [*required*]                     | enum          | Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`                                                                                                                                     |
| forwarder_destination | Option 3                                   | object        | The Elasticsearch destination.                                                                                                                                                                                                   |
| Option 3              | auth [*required*]                     | object        | Basic access authentication.                                                                                                                                                                                                     |
| additionalProperties  | <any-key>                                  |               | Basic access authentication.                                                                                                                                                                                                     |
| Option 3              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 3              | index_name [*required*]               | string        | Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).                                 |
| Option 3              | index_rotation                             | string        | Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options: | If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).                                           |
| Option 3              | type [*required*]                     | enum          | Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`                                                                                                                                                      |
| forwarder_destination | Option 4                                   | object        | The Microsoft Sentinel destination.                                                                                                                                                                                              |
| Option 4              | client_id [*required*]                | string        | Client ID from the Datadog Azure integration.                                                                                                                                                                                    |
| Option 4              | data_collection_endpoint [*required*] | string        | Azure data collection endpoint.                                                                                                                                                                                                  |
| Option 4              | data_collection_rule_id [*required*]  | string        | Azure data collection rule ID.                                                                                                                                                                                                   |
| Option 4              | stream_name [*required*]              | string        | Azure stream name.                                                                                                                                                                                                               |
| Option 4              | tenant_id [*required*]                | string        | Tenant ID from the Datadog Azure integration.                                                                                                                                                                                    |
| Option 4              | type [*required*]                     | enum          | Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`                                                                                                                                            |
| attributes            | name                                       | string        | The custom destination name.                                                                                                                                                                                                     |
| attributes            | query                                      | string        | The custom destination query filter. Logs matching this query are forwarded to the destination.                                                                                                                                  |
| data                  | id                                         | string        | The custom destination ID.                                                                                                                                                                                                       |
| data                  | type                                       | enum          | The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`                                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "enabled": true,
        "forward_tags": true,
        "forward_tags_restriction_list": [
          "datacenter",
          "host"
        ],
        "forward_tags_restriction_list_type": "ALLOW_LIST",
        "forwarder_destination": {
          "auth": {
            "type": "basic"
          },
          "endpoint": "https://example.com",
          "type": "http"
        },
        "name": "Nginx logs",
        "query": "source:nginx"
      },
      "id": "be5d7a69-d0c8-4d4d-8ee8-bba292d98139",
      "type": "custom_destination"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all custom destinations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.list_logs_custom_destinations()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get all custom destinations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsCustomDestinationsAPI.new
p api_instance.list_logs_custom_destinations()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get all custom destinations returns "OK" response

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
    api := datadogV2.NewLogsCustomDestinationsApi(apiClient)
    resp, r, err := api.ListLogsCustomDestinations(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsCustomDestinationsApi.ListLogsCustomDestinations`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsCustomDestinationsApi.ListLogsCustomDestinations`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get all custom destinations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsCustomDestinationsApi;
import com.datadog.api.client.v2.model.CustomDestinationsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsCustomDestinationsApi apiInstance = new LogsCustomDestinationsApi(defaultClient);

    try {
      CustomDestinationsResponse result = apiInstance.listLogsCustomDestinations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsCustomDestinationsApi#listLogsCustomDestinations");
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
// Get all custom destinations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_custom_destinations::LogsCustomDestinationsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsCustomDestinationsAPI::with_config(configuration);
    let resp = api.list_logs_custom_destinations().await;
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
 * Get all custom destinations returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsCustomDestinationsApi(configuration);

apiInstance
  .listLogsCustomDestinations()
  .then((data: v2.CustomDestinationsResponse) => {
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

## Create a custom destination{% #create-a-custom-destination %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/logs/config/custom-destinations |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/logs/config/custom-destinations |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/logs/config/custom-destinations      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/logs/config/custom-destinations      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/logs/config/custom-destinations     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/logs/config/custom-destinations |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations |

### Overview

Create a custom destination in your organization. This endpoint requires the `logs_write_forwarding_rules` permission.

### Request

#### Body Data (required)

The definition of the new custom destination.

{% tab title="Model" %}

| Parent field          | Field                                      | Type          | Description                                                                                                                                                                                                                      |
| --------------------- | ------------------------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                                       | object        | The definition of a custom destination.                                                                                                                                                                                          |
| data                  | attributes [*required*]               | object        | The attributes associated with the custom destination.                                                                                                                                                                           |
| attributes            | enabled                                    | boolean       | Whether logs matching this custom destination should be forwarded or not.                                                                                                                                                        |
| attributes            | forward_tags                               | boolean       | Whether tags from the forwarded logs should be forwarded or not.                                                                                                                                                                 |
| attributes            | forward_tags_restriction_list              | [string]      | List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be filtered.                                                                                                                          | An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter. |
| attributes            | forward_tags_restriction_list_type         | enum          | How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.                                      | `BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST`                |
| attributes            | forwarder_destination [*required*]    |  <oneOf> | A custom destination's location to forward logs.                                                                                                                                                                                 |
| forwarder_destination | Option 1                                   | object        | The HTTP destination.                                                                                                                                                                                                            |
| Option 1              | auth [*required*]                     |  <oneOf> | Authentication method of the HTTP requests.                                                                                                                                                                                      |
| auth                  | Option 1                                   | object        | Basic access authentication.                                                                                                                                                                                                     |
| Option 1              | password [*required*]                 | string        | The password of the authentication. This field is not returned by the API.                                                                                                                                                       |
| Option 1              | type [*required*]                     | enum          | Type of the basic access authentication. Allowed enum values: `basic`                                                                                                                                                            |
| Option 1              | username [*required*]                 | string        | The username of the authentication. This field is not returned by the API.                                                                                                                                                       |
| auth                  | Option 2                                   | object        | Custom header access authentication.                                                                                                                                                                                             |
| Option 2              | header_name [*required*]              | string        | The header name of the authentication.                                                                                                                                                                                           |
| Option 2              | header_value [*required*]             | string        | The header value of the authentication. This field is not returned by the API.                                                                                                                                                   |
| Option 2              | type [*required*]                     | enum          | Type of the custom header access authentication. Allowed enum values: `custom_header`                                                                                                                                            |
| Option 1              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 1              | type [*required*]                     | enum          | Type of the HTTP destination. Allowed enum values: `http`                                                                                                                                                                        |
| forwarder_destination | Option 2                                   | object        | The Splunk HTTP Event Collector (HEC) destination.                                                                                                                                                                               |
| Option 2              | access_token [*required*]             | string        | Access token of the Splunk HTTP Event Collector. This field is not returned by the API.                                                                                                                                          |
| Option 2              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 2              | type [*required*]                     | enum          | Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`                                                                                                                                     |
| forwarder_destination | Option 3                                   | object        | The Elasticsearch destination.                                                                                                                                                                                                   |
| Option 3              | auth [*required*]                     | object        | Basic access authentication.                                                                                                                                                                                                     |
| auth                  | password [*required*]                 | string        | The password of the authentication. This field is not returned by the API.                                                                                                                                                       |
| auth                  | username [*required*]                 | string        | The username of the authentication. This field is not returned by the API.                                                                                                                                                       |
| Option 3              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 3              | index_name [*required*]               | string        | Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).                                 |
| Option 3              | index_rotation                             | string        | Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options: | If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).                                           |
| Option 3              | type [*required*]                     | enum          | Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`                                                                                                                                                      |
| forwarder_destination | Option 4                                   | object        | The Microsoft Sentinel destination.                                                                                                                                                                                              |
| Option 4              | client_id [*required*]                | string        | Client ID from the Datadog Azure integration.                                                                                                                                                                                    |
| Option 4              | data_collection_endpoint [*required*] | string        | Azure data collection endpoint.                                                                                                                                                                                                  |
| Option 4              | data_collection_rule_id [*required*]  | string        | Azure data collection rule ID.                                                                                                                                                                                                   |
| Option 4              | stream_name [*required*]              | string        | Azure stream name.                                                                                                                                                                                                               |
| Option 4              | tenant_id [*required*]                | string        | Tenant ID from the Datadog Azure integration.                                                                                                                                                                                    |
| Option 4              | type [*required*]                     | enum          | Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`                                                                                                                                            |
| attributes            | name [*required*]                     | string        | The custom destination name.                                                                                                                                                                                                     |
| attributes            | query                                      | string        | The custom destination query and filter. Logs matching this query are forwarded to the destination.                                                                                                                              |
| data                  | type [*required*]                     | enum          | The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`                                                                                                             |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "data": {
    "attributes": {
      "enabled": false,
      "forward_tags": false,
      "forward_tags_restriction_list": [
        "datacenter",
        "host"
      ],
      "forward_tags_restriction_list_type": "ALLOW_LIST",
      "forwarder_destination": {
        "auth": {
          "password": "datadog-custom-destination-password",
          "type": "basic",
          "username": "datadog-custom-destination-username"
        },
        "endpoint": "https://example.com",
        "type": "http"
      },
      "name": "Nginx logs",
      "query": "source:nginx"
    },
    "type": "custom_destination"
  }
}
```

#####

```json
{
  "data": {
    "attributes": {
      "enabled": false,
      "forward_tags": false,
      "forward_tags_restriction_list": [
        "datacenter",
        "host"
      ],
      "forward_tags_restriction_list_type": "ALLOW_LIST",
      "forwarder_destination": {
        "auth": {
          "header_value": "my-secret",
          "type": "custom_header",
          "header_name": "MY-AUTHENTICATION-HEADER"
        },
        "endpoint": "https://example.com",
        "type": "http"
      },
      "name": "Nginx logs",
      "query": "source:nginx"
    },
    "type": "custom_destination"
  }
}
```

#####

```json
{
  "data": {
    "attributes": {
      "enabled": false,
      "forward_tags": false,
      "forward_tags_restriction_list": [
        "datacenter",
        "host"
      ],
      "forward_tags_restriction_list_type": "ALLOW_LIST",
      "forwarder_destination": {
        "type": "microsoft_sentinel",
        "tenant_id": "f3c9a8a1-4c2e-4d2e-b911-9f3c28c3c8b2",
        "client_id": "9a2f4d83-2b5e-429e-a35a-2b3c4182db71",
        "data_collection_endpoint": "https://my-dce-5kyl.eastus-1.ingest.monitor.azure.com",
        "data_collection_rule_id": "dcr-000a00a000a00000a000000aa000a0aa",
        "stream_name": "Custom-MyTable"
      },
      "name": "Nginx logs",
      "query": "source:nginx"
    },
    "type": "custom_destination"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The custom destination.

| Parent field          | Field                                      | Type          | Description                                                                                                                                                                                                                      |
| --------------------- | ------------------------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                                       | object        | The definition of a custom destination.                                                                                                                                                                                          |
| data                  | attributes                                 | object        | The attributes associated with the custom destination.                                                                                                                                                                           |
| attributes            | enabled                                    | boolean       | Whether logs matching this custom destination should be forwarded or not.                                                                                                                                                        |
| attributes            | forward_tags                               | boolean       | Whether tags from the forwarded logs should be forwarded or not.                                                                                                                                                                 |
| attributes            | forward_tags_restriction_list              | [string]      | List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be filtered.                                                                                                                          | An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter. |
| attributes            | forward_tags_restriction_list_type         | enum          | How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.                                      | `BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST`                |
| attributes            | forwarder_destination                      |  <oneOf> | A custom destination's location to forward logs.                                                                                                                                                                                 |
| forwarder_destination | Option 1                                   | object        | The HTTP destination.                                                                                                                                                                                                            |
| Option 1              | auth [*required*]                     |  <oneOf> | Authentication method of the HTTP requests.                                                                                                                                                                                      |
| auth                  | Option 1                                   | object        | Basic access authentication.                                                                                                                                                                                                     |
| Option 1              | type [*required*]                     | enum          | Type of the basic access authentication. Allowed enum values: `basic`                                                                                                                                                            |
| auth                  | Option 2                                   | object        | Custom header access authentication.                                                                                                                                                                                             |
| Option 2              | header_name [*required*]              | string        | The header name of the authentication.                                                                                                                                                                                           |
| Option 2              | type [*required*]                     | enum          | Type of the custom header access authentication. Allowed enum values: `custom_header`                                                                                                                                            |
| Option 1              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 1              | type [*required*]                     | enum          | Type of the HTTP destination. Allowed enum values: `http`                                                                                                                                                                        |
| forwarder_destination | Option 2                                   | object        | The Splunk HTTP Event Collector (HEC) destination.                                                                                                                                                                               |
| Option 2              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 2              | type [*required*]                     | enum          | Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`                                                                                                                                     |
| forwarder_destination | Option 3                                   | object        | The Elasticsearch destination.                                                                                                                                                                                                   |
| Option 3              | auth [*required*]                     | object        | Basic access authentication.                                                                                                                                                                                                     |
| additionalProperties  | <any-key>                                  |               | Basic access authentication.                                                                                                                                                                                                     |
| Option 3              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 3              | index_name [*required*]               | string        | Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).                                 |
| Option 3              | index_rotation                             | string        | Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options: | If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).                                           |
| Option 3              | type [*required*]                     | enum          | Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`                                                                                                                                                      |
| forwarder_destination | Option 4                                   | object        | The Microsoft Sentinel destination.                                                                                                                                                                                              |
| Option 4              | client_id [*required*]                | string        | Client ID from the Datadog Azure integration.                                                                                                                                                                                    |
| Option 4              | data_collection_endpoint [*required*] | string        | Azure data collection endpoint.                                                                                                                                                                                                  |
| Option 4              | data_collection_rule_id [*required*]  | string        | Azure data collection rule ID.                                                                                                                                                                                                   |
| Option 4              | stream_name [*required*]              | string        | Azure stream name.                                                                                                                                                                                                               |
| Option 4              | tenant_id [*required*]                | string        | Tenant ID from the Datadog Azure integration.                                                                                                                                                                                    |
| Option 4              | type [*required*]                     | enum          | Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`                                                                                                                                            |
| attributes            | name                                       | string        | The custom destination name.                                                                                                                                                                                                     |
| attributes            | query                                      | string        | The custom destination query filter. Logs matching this query are forwarded to the destination.                                                                                                                                  |
| data                  | id                                         | string        | The custom destination ID.                                                                                                                                                                                                       |
| data                  | type                                       | enum          | The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`                                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enabled": true,
      "forward_tags": true,
      "forward_tags_restriction_list": [
        "datacenter",
        "host"
      ],
      "forward_tags_restriction_list_type": "ALLOW_LIST",
      "forwarder_destination": {
        "auth": {
          "type": "basic"
        },
        "endpoint": "https://example.com",
        "type": "http"
      },
      "name": "Nginx logs",
      "query": "source:nginx"
    },
    "id": "be5d7a69-d0c8-4d4d-8ee8-bba292d98139",
    "type": "custom_destination"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "enabled": false,
      "forward_tags": false,
      "forward_tags_restriction_list": [
        "datacenter",
        "host"
      ],
      "forward_tags_restriction_list_type": "ALLOW_LIST",
      "forwarder_destination": {
        "auth": {
          "password": "datadog-custom-destination-password",
          "type": "basic",
          "username": "datadog-custom-destination-username"
        },
        "endpoint": "https://example.com",
        "type": "http"
      },
      "name": "Nginx logs",
      "query": "source:nginx"
    },
    "type": "custom_destination"
  }
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "enabled": false,
      "forward_tags": false,
      "forward_tags_restriction_list": [
        "datacenter",
        "host"
      ],
      "forward_tags_restriction_list_type": "ALLOW_LIST",
      "forwarder_destination": {
        "auth": {
          "header_value": "my-secret",
          "type": "custom_header",
          "header_name": "MY-AUTHENTICATION-HEADER"
        },
        "endpoint": "https://example.com",
        "type": "http"
      },
      "name": "Nginx logs",
      "query": "source:nginx"
    },
    "type": "custom_destination"
  }
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "enabled": false,
      "forward_tags": false,
      "forward_tags_restriction_list": [
        "datacenter",
        "host"
      ],
      "forward_tags_restriction_list_type": "ALLOW_LIST",
      "forwarder_destination": {
        "type": "microsoft_sentinel",
        "tenant_id": "f3c9a8a1-4c2e-4d2e-b911-9f3c28c3c8b2",
        "client_id": "9a2f4d83-2b5e-429e-a35a-2b3c4182db71",
        "data_collection_endpoint": "https://my-dce-5kyl.eastus-1.ingest.monitor.azure.com",
        "data_collection_rule_id": "dcr-000a00a000a00000a000000aa000a0aa",
        "stream_name": "Custom-MyTable"
      },
      "name": "Nginx logs",
      "query": "source:nginx"
    },
    "type": "custom_destination"
  }
}
EOF

#####

```go
// Create a Basic HTTP custom destination returns "OK" response

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
    body := datadogV2.CustomDestinationCreateRequest{
        Data: &datadogV2.CustomDestinationCreateRequestDefinition{
            Attributes: datadogV2.CustomDestinationCreateRequestAttributes{
                Enabled:     datadog.PtrBool(false),
                ForwardTags: datadog.PtrBool(false),
                ForwardTagsRestrictionList: []string{
                    "datacenter",
                    "host",
                },
                ForwardTagsRestrictionListType: datadogV2.CUSTOMDESTINATIONATTRIBUTETAGSRESTRICTIONLISTTYPE_ALLOW_LIST.Ptr(),
                ForwarderDestination: datadogV2.CustomDestinationForwardDestination{
                    CustomDestinationForwardDestinationHttp: &datadogV2.CustomDestinationForwardDestinationHttp{
                        Auth: datadogV2.CustomDestinationHttpDestinationAuth{
                            CustomDestinationHttpDestinationAuthBasic: &datadogV2.CustomDestinationHttpDestinationAuthBasic{
                                Password: "datadog-custom-destination-password",
                                Type:     datadogV2.CUSTOMDESTINATIONHTTPDESTINATIONAUTHBASICTYPE_BASIC,
                                Username: "datadog-custom-destination-username",
                            }},
                        Endpoint: "https://example.com",
                        Type:     datadogV2.CUSTOMDESTINATIONFORWARDDESTINATIONHTTPTYPE_HTTP,
                    }},
                Name:  "Nginx logs",
                Query: datadog.PtrString("source:nginx"),
            },
            Type: datadogV2.CUSTOMDESTINATIONTYPE_CUSTOM_DESTINATION,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsCustomDestinationsApi(apiClient)
    resp, r, err := api.CreateLogsCustomDestination(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsCustomDestinationsApi.CreateLogsCustomDestination`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsCustomDestinationsApi.CreateLogsCustomDestination`:\n%s\n", responseContent)
}
```

#####

```go
// Create a Custom Header HTTP custom destination returns "OK" response

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
    body := datadogV2.CustomDestinationCreateRequest{
        Data: &datadogV2.CustomDestinationCreateRequestDefinition{
            Attributes: datadogV2.CustomDestinationCreateRequestAttributes{
                Enabled:     datadog.PtrBool(false),
                ForwardTags: datadog.PtrBool(false),
                ForwardTagsRestrictionList: []string{
                    "datacenter",
                    "host",
                },
                ForwardTagsRestrictionListType: datadogV2.CUSTOMDESTINATIONATTRIBUTETAGSRESTRICTIONLISTTYPE_ALLOW_LIST.Ptr(),
                ForwarderDestination: datadogV2.CustomDestinationForwardDestination{
                    CustomDestinationForwardDestinationHttp: &datadogV2.CustomDestinationForwardDestinationHttp{
                        Auth: datadogV2.CustomDestinationHttpDestinationAuth{
                            CustomDestinationHttpDestinationAuthCustomHeader: &datadogV2.CustomDestinationHttpDestinationAuthCustomHeader{
                                HeaderValue: "my-secret",
                                Type:        datadogV2.CUSTOMDESTINATIONHTTPDESTINATIONAUTHCUSTOMHEADERTYPE_CUSTOM_HEADER,
                                HeaderName:  "MY-AUTHENTICATION-HEADER",
                            }},
                        Endpoint: "https://example.com",
                        Type:     datadogV2.CUSTOMDESTINATIONFORWARDDESTINATIONHTTPTYPE_HTTP,
                    }},
                Name:  "Nginx logs",
                Query: datadog.PtrString("source:nginx"),
            },
            Type: datadogV2.CUSTOMDESTINATIONTYPE_CUSTOM_DESTINATION,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsCustomDestinationsApi(apiClient)
    resp, r, err := api.CreateLogsCustomDestination(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsCustomDestinationsApi.CreateLogsCustomDestination`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsCustomDestinationsApi.CreateLogsCustomDestination`:\n%s\n", responseContent)
}
```

#####

```go
// Create a Microsoft Sentinel custom destination returns "OK" response

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
    body := datadogV2.CustomDestinationCreateRequest{
        Data: &datadogV2.CustomDestinationCreateRequestDefinition{
            Attributes: datadogV2.CustomDestinationCreateRequestAttributes{
                Enabled:     datadog.PtrBool(false),
                ForwardTags: datadog.PtrBool(false),
                ForwardTagsRestrictionList: []string{
                    "datacenter",
                    "host",
                },
                ForwardTagsRestrictionListType: datadogV2.CUSTOMDESTINATIONATTRIBUTETAGSRESTRICTIONLISTTYPE_ALLOW_LIST.Ptr(),
                ForwarderDestination: datadogV2.CustomDestinationForwardDestination{
                    CustomDestinationForwardDestinationMicrosoftSentinel: &datadogV2.CustomDestinationForwardDestinationMicrosoftSentinel{
                        Type:                   datadogV2.CUSTOMDESTINATIONFORWARDDESTINATIONMICROSOFTSENTINELTYPE_MICROSOFT_SENTINEL,
                        TenantId:               "f3c9a8a1-4c2e-4d2e-b911-9f3c28c3c8b2",
                        ClientId:               "9a2f4d83-2b5e-429e-a35a-2b3c4182db71",
                        DataCollectionEndpoint: "https://my-dce-5kyl.eastus-1.ingest.monitor.azure.com",
                        DataCollectionRuleId:   "dcr-000a00a000a00000a000000aa000a0aa",
                        StreamName:             "Custom-MyTable",
                    }},
                Name:  "Nginx logs",
                Query: datadog.PtrString("source:nginx"),
            },
            Type: datadogV2.CUSTOMDESTINATIONTYPE_CUSTOM_DESTINATION,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsCustomDestinationsApi(apiClient)
    resp, r, err := api.CreateLogsCustomDestination(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsCustomDestinationsApi.CreateLogsCustomDestination`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsCustomDestinationsApi.CreateLogsCustomDestination`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create a Basic HTTP custom destination returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsCustomDestinationsApi;
import com.datadog.api.client.v2.model.CustomDestinationAttributeTagsRestrictionListType;
import com.datadog.api.client.v2.model.CustomDestinationCreateRequest;
import com.datadog.api.client.v2.model.CustomDestinationCreateRequestAttributes;
import com.datadog.api.client.v2.model.CustomDestinationCreateRequestDefinition;
import com.datadog.api.client.v2.model.CustomDestinationForwardDestination;
import com.datadog.api.client.v2.model.CustomDestinationForwardDestinationHttp;
import com.datadog.api.client.v2.model.CustomDestinationForwardDestinationHttpType;
import com.datadog.api.client.v2.model.CustomDestinationHttpDestinationAuth;
import com.datadog.api.client.v2.model.CustomDestinationHttpDestinationAuthBasic;
import com.datadog.api.client.v2.model.CustomDestinationHttpDestinationAuthBasicType;
import com.datadog.api.client.v2.model.CustomDestinationResponse;
import com.datadog.api.client.v2.model.CustomDestinationType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsCustomDestinationsApi apiInstance = new LogsCustomDestinationsApi(defaultClient);

    CustomDestinationCreateRequest body =
        new CustomDestinationCreateRequest()
            .data(
                new CustomDestinationCreateRequestDefinition()
                    .attributes(
                        new CustomDestinationCreateRequestAttributes()
                            .enabled(false)
                            .forwardTags(false)
                            .forwardTagsRestrictionList(Arrays.asList("datacenter", "host"))
                            .forwardTagsRestrictionListType(
                                CustomDestinationAttributeTagsRestrictionListType.ALLOW_LIST)
                            .forwarderDestination(
                                new CustomDestinationForwardDestination(
                                    new CustomDestinationForwardDestinationHttp()
                                        .auth(
                                            new CustomDestinationHttpDestinationAuth(
                                                new CustomDestinationHttpDestinationAuthBasic()
                                                    .password("datadog-custom-destination-password")
                                                    .type(
                                                        CustomDestinationHttpDestinationAuthBasicType
                                                            .BASIC)
                                                    .username(
                                                        "datadog-custom-destination-username")))
                                        .endpoint("https://example.com")
                                        .type(CustomDestinationForwardDestinationHttpType.HTTP)))
                            .name("Nginx logs")
                            .query("source:nginx"))
                    .type(CustomDestinationType.CUSTOM_DESTINATION));

    try {
      CustomDestinationResponse result = apiInstance.createLogsCustomDestination(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsCustomDestinationsApi#createLogsCustomDestination");
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
// Create a Custom Header HTTP custom destination returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsCustomDestinationsApi;
import com.datadog.api.client.v2.model.CustomDestinationAttributeTagsRestrictionListType;
import com.datadog.api.client.v2.model.CustomDestinationCreateRequest;
import com.datadog.api.client.v2.model.CustomDestinationCreateRequestAttributes;
import com.datadog.api.client.v2.model.CustomDestinationCreateRequestDefinition;
import com.datadog.api.client.v2.model.CustomDestinationForwardDestination;
import com.datadog.api.client.v2.model.CustomDestinationForwardDestinationHttp;
import com.datadog.api.client.v2.model.CustomDestinationForwardDestinationHttpType;
import com.datadog.api.client.v2.model.CustomDestinationHttpDestinationAuth;
import com.datadog.api.client.v2.model.CustomDestinationHttpDestinationAuthCustomHeader;
import com.datadog.api.client.v2.model.CustomDestinationHttpDestinationAuthCustomHeaderType;
import com.datadog.api.client.v2.model.CustomDestinationResponse;
import com.datadog.api.client.v2.model.CustomDestinationType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsCustomDestinationsApi apiInstance = new LogsCustomDestinationsApi(defaultClient);

    CustomDestinationCreateRequest body =
        new CustomDestinationCreateRequest()
            .data(
                new CustomDestinationCreateRequestDefinition()
                    .attributes(
                        new CustomDestinationCreateRequestAttributes()
                            .enabled(false)
                            .forwardTags(false)
                            .forwardTagsRestrictionList(Arrays.asList("datacenter", "host"))
                            .forwardTagsRestrictionListType(
                                CustomDestinationAttributeTagsRestrictionListType.ALLOW_LIST)
                            .forwarderDestination(
                                new CustomDestinationForwardDestination(
                                    new CustomDestinationForwardDestinationHttp()
                                        .auth(
                                            new CustomDestinationHttpDestinationAuth(
                                                new CustomDestinationHttpDestinationAuthCustomHeader()
                                                    .headerValue("my-secret")
                                                    .type(
                                                        CustomDestinationHttpDestinationAuthCustomHeaderType
                                                            .CUSTOM_HEADER)
                                                    .headerName("MY-AUTHENTICATION-HEADER")))
                                        .endpoint("https://example.com")
                                        .type(CustomDestinationForwardDestinationHttpType.HTTP)))
                            .name("Nginx logs")
                            .query("source:nginx"))
                    .type(CustomDestinationType.CUSTOM_DESTINATION));

    try {
      CustomDestinationResponse result = apiInstance.createLogsCustomDestination(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsCustomDestinationsApi#createLogsCustomDestination");
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
// Create a Microsoft Sentinel custom destination returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsCustomDestinationsApi;
import com.datadog.api.client.v2.model.CustomDestinationAttributeTagsRestrictionListType;
import com.datadog.api.client.v2.model.CustomDestinationCreateRequest;
import com.datadog.api.client.v2.model.CustomDestinationCreateRequestAttributes;
import com.datadog.api.client.v2.model.CustomDestinationCreateRequestDefinition;
import com.datadog.api.client.v2.model.CustomDestinationForwardDestination;
import com.datadog.api.client.v2.model.CustomDestinationForwardDestinationMicrosoftSentinel;
import com.datadog.api.client.v2.model.CustomDestinationForwardDestinationMicrosoftSentinelType;
import com.datadog.api.client.v2.model.CustomDestinationResponse;
import com.datadog.api.client.v2.model.CustomDestinationType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsCustomDestinationsApi apiInstance = new LogsCustomDestinationsApi(defaultClient);

    CustomDestinationCreateRequest body =
        new CustomDestinationCreateRequest()
            .data(
                new CustomDestinationCreateRequestDefinition()
                    .attributes(
                        new CustomDestinationCreateRequestAttributes()
                            .enabled(false)
                            .forwardTags(false)
                            .forwardTagsRestrictionList(Arrays.asList("datacenter", "host"))
                            .forwardTagsRestrictionListType(
                                CustomDestinationAttributeTagsRestrictionListType.ALLOW_LIST)
                            .forwarderDestination(
                                new CustomDestinationForwardDestination(
                                    new CustomDestinationForwardDestinationMicrosoftSentinel()
                                        .type(
                                            CustomDestinationForwardDestinationMicrosoftSentinelType
                                                .MICROSOFT_SENTINEL)
                                        .tenantId("f3c9a8a1-4c2e-4d2e-b911-9f3c28c3c8b2")
                                        .clientId("9a2f4d83-2b5e-429e-a35a-2b3c4182db71")
                                        .dataCollectionEndpoint(
                                            "https://my-dce-5kyl.eastus-1.ingest.monitor.azure.com")
                                        .dataCollectionRuleId(
                                            "dcr-000a00a000a00000a000000aa000a0aa")
                                        .streamName("Custom-MyTable")))
                            .name("Nginx logs")
                            .query("source:nginx"))
                    .type(CustomDestinationType.CUSTOM_DESTINATION));

    try {
      CustomDestinationResponse result = apiInstance.createLogsCustomDestination(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsCustomDestinationsApi#createLogsCustomDestination");
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
Create a Basic HTTP custom destination returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination_attribute_tags_restriction_list_type import (
    CustomDestinationAttributeTagsRestrictionListType,
)
from datadog_api_client.v2.model.custom_destination_create_request import CustomDestinationCreateRequest
from datadog_api_client.v2.model.custom_destination_create_request_attributes import (
    CustomDestinationCreateRequestAttributes,
)
from datadog_api_client.v2.model.custom_destination_create_request_definition import (
    CustomDestinationCreateRequestDefinition,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_http import (
    CustomDestinationForwardDestinationHttp,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_http_type import (
    CustomDestinationForwardDestinationHttpType,
)
from datadog_api_client.v2.model.custom_destination_http_destination_auth_basic import (
    CustomDestinationHttpDestinationAuthBasic,
)
from datadog_api_client.v2.model.custom_destination_http_destination_auth_basic_type import (
    CustomDestinationHttpDestinationAuthBasicType,
)
from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType

body = CustomDestinationCreateRequest(
    data=CustomDestinationCreateRequestDefinition(
        attributes=CustomDestinationCreateRequestAttributes(
            enabled=False,
            forward_tags=False,
            forward_tags_restriction_list=[
                "datacenter",
                "host",
            ],
            forward_tags_restriction_list_type=CustomDestinationAttributeTagsRestrictionListType.ALLOW_LIST,
            forwarder_destination=CustomDestinationForwardDestinationHttp(
                auth=CustomDestinationHttpDestinationAuthBasic(
                    password="datadog-custom-destination-password",
                    type=CustomDestinationHttpDestinationAuthBasicType.BASIC,
                    username="datadog-custom-destination-username",
                ),
                endpoint="https://example.com",
                type=CustomDestinationForwardDestinationHttpType.HTTP,
            ),
            name="Nginx logs",
            query="source:nginx",
        ),
        type=CustomDestinationType.CUSTOM_DESTINATION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.create_logs_custom_destination(body=body)

    print(response)
```

#####

```python
"""
Create a Custom Header HTTP custom destination returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination_attribute_tags_restriction_list_type import (
    CustomDestinationAttributeTagsRestrictionListType,
)
from datadog_api_client.v2.model.custom_destination_create_request import CustomDestinationCreateRequest
from datadog_api_client.v2.model.custom_destination_create_request_attributes import (
    CustomDestinationCreateRequestAttributes,
)
from datadog_api_client.v2.model.custom_destination_create_request_definition import (
    CustomDestinationCreateRequestDefinition,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_http import (
    CustomDestinationForwardDestinationHttp,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_http_type import (
    CustomDestinationForwardDestinationHttpType,
)
from datadog_api_client.v2.model.custom_destination_http_destination_auth_custom_header import (
    CustomDestinationHttpDestinationAuthCustomHeader,
)
from datadog_api_client.v2.model.custom_destination_http_destination_auth_custom_header_type import (
    CustomDestinationHttpDestinationAuthCustomHeaderType,
)
from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType

body = CustomDestinationCreateRequest(
    data=CustomDestinationCreateRequestDefinition(
        attributes=CustomDestinationCreateRequestAttributes(
            enabled=False,
            forward_tags=False,
            forward_tags_restriction_list=[
                "datacenter",
                "host",
            ],
            forward_tags_restriction_list_type=CustomDestinationAttributeTagsRestrictionListType.ALLOW_LIST,
            forwarder_destination=CustomDestinationForwardDestinationHttp(
                auth=CustomDestinationHttpDestinationAuthCustomHeader(
                    header_value="my-secret",
                    type=CustomDestinationHttpDestinationAuthCustomHeaderType.CUSTOM_HEADER,
                    header_name="MY-AUTHENTICATION-HEADER",
                ),
                endpoint="https://example.com",
                type=CustomDestinationForwardDestinationHttpType.HTTP,
            ),
            name="Nginx logs",
            query="source:nginx",
        ),
        type=CustomDestinationType.CUSTOM_DESTINATION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.create_logs_custom_destination(body=body)

    print(response)
```

#####

```python
"""
Create a Microsoft Sentinel custom destination returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination_attribute_tags_restriction_list_type import (
    CustomDestinationAttributeTagsRestrictionListType,
)
from datadog_api_client.v2.model.custom_destination_create_request import CustomDestinationCreateRequest
from datadog_api_client.v2.model.custom_destination_create_request_attributes import (
    CustomDestinationCreateRequestAttributes,
)
from datadog_api_client.v2.model.custom_destination_create_request_definition import (
    CustomDestinationCreateRequestDefinition,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_microsoft_sentinel import (
    CustomDestinationForwardDestinationMicrosoftSentinel,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_microsoft_sentinel_type import (
    CustomDestinationForwardDestinationMicrosoftSentinelType,
)
from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType

body = CustomDestinationCreateRequest(
    data=CustomDestinationCreateRequestDefinition(
        attributes=CustomDestinationCreateRequestAttributes(
            enabled=False,
            forward_tags=False,
            forward_tags_restriction_list=[
                "datacenter",
                "host",
            ],
            forward_tags_restriction_list_type=CustomDestinationAttributeTagsRestrictionListType.ALLOW_LIST,
            forwarder_destination=CustomDestinationForwardDestinationMicrosoftSentinel(
                type=CustomDestinationForwardDestinationMicrosoftSentinelType.MICROSOFT_SENTINEL,
                tenant_id="f3c9a8a1-4c2e-4d2e-b911-9f3c28c3c8b2",
                client_id="9a2f4d83-2b5e-429e-a35a-2b3c4182db71",
                data_collection_endpoint="https://my-dce-5kyl.eastus-1.ingest.monitor.azure.com",
                data_collection_rule_id="dcr-000a00a000a00000a000000aa000a0aa",
                stream_name="Custom-MyTable",
            ),
            name="Nginx logs",
            query="source:nginx",
        ),
        type=CustomDestinationType.CUSTOM_DESTINATION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.create_logs_custom_destination(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create a Basic HTTP custom destination returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsCustomDestinationsAPI.new

body = DatadogAPIClient::V2::CustomDestinationCreateRequest.new({
  data: DatadogAPIClient::V2::CustomDestinationCreateRequestDefinition.new({
    attributes: DatadogAPIClient::V2::CustomDestinationCreateRequestAttributes.new({
      enabled: false,
      forward_tags: false,
      forward_tags_restriction_list: [
        "datacenter",
        "host",
      ],
      forward_tags_restriction_list_type: DatadogAPIClient::V2::CustomDestinationAttributeTagsRestrictionListType::ALLOW_LIST,
      forwarder_destination: DatadogAPIClient::V2::CustomDestinationForwardDestinationHttp.new({
        auth: DatadogAPIClient::V2::CustomDestinationHttpDestinationAuthBasic.new({
          password: "datadog-custom-destination-password",
          type: DatadogAPIClient::V2::CustomDestinationHttpDestinationAuthBasicType::BASIC,
          username: "datadog-custom-destination-username",
        }),
        endpoint: "https://example.com",
        type: DatadogAPIClient::V2::CustomDestinationForwardDestinationHttpType::HTTP,
      }),
      name: "Nginx logs",
      query: "source:nginx",
    }),
    type: DatadogAPIClient::V2::CustomDestinationType::CUSTOM_DESTINATION,
  }),
})
p api_instance.create_logs_custom_destination(body)
```

#####

```ruby
# Create a Custom Header HTTP custom destination returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsCustomDestinationsAPI.new

body = DatadogAPIClient::V2::CustomDestinationCreateRequest.new({
  data: DatadogAPIClient::V2::CustomDestinationCreateRequestDefinition.new({
    attributes: DatadogAPIClient::V2::CustomDestinationCreateRequestAttributes.new({
      enabled: false,
      forward_tags: false,
      forward_tags_restriction_list: [
        "datacenter",
        "host",
      ],
      forward_tags_restriction_list_type: DatadogAPIClient::V2::CustomDestinationAttributeTagsRestrictionListType::ALLOW_LIST,
      forwarder_destination: DatadogAPIClient::V2::CustomDestinationForwardDestinationHttp.new({
        auth: DatadogAPIClient::V2::CustomDestinationHttpDestinationAuthCustomHeader.new({
          header_value: "my-secret",
          type: DatadogAPIClient::V2::CustomDestinationHttpDestinationAuthCustomHeaderType::CUSTOM_HEADER,
          header_name: "MY-AUTHENTICATION-HEADER",
        }),
        endpoint: "https://example.com",
        type: DatadogAPIClient::V2::CustomDestinationForwardDestinationHttpType::HTTP,
      }),
      name: "Nginx logs",
      query: "source:nginx",
    }),
    type: DatadogAPIClient::V2::CustomDestinationType::CUSTOM_DESTINATION,
  }),
})
p api_instance.create_logs_custom_destination(body)
```

#####

```ruby
# Create a Microsoft Sentinel custom destination returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsCustomDestinationsAPI.new

body = DatadogAPIClient::V2::CustomDestinationCreateRequest.new({
  data: DatadogAPIClient::V2::CustomDestinationCreateRequestDefinition.new({
    attributes: DatadogAPIClient::V2::CustomDestinationCreateRequestAttributes.new({
      enabled: false,
      forward_tags: false,
      forward_tags_restriction_list: [
        "datacenter",
        "host",
      ],
      forward_tags_restriction_list_type: DatadogAPIClient::V2::CustomDestinationAttributeTagsRestrictionListType::ALLOW_LIST,
      forwarder_destination: DatadogAPIClient::V2::CustomDestinationForwardDestinationMicrosoftSentinel.new({
        type: DatadogAPIClient::V2::CustomDestinationForwardDestinationMicrosoftSentinelType::MICROSOFT_SENTINEL,
        tenant_id: "f3c9a8a1-4c2e-4d2e-b911-9f3c28c3c8b2",
        client_id: "9a2f4d83-2b5e-429e-a35a-2b3c4182db71",
        data_collection_endpoint: "https://my-dce-5kyl.eastus-1.ingest.monitor.azure.com",
        data_collection_rule_id: "dcr-000a00a000a00000a000000aa000a0aa",
        stream_name: "Custom-MyTable",
      }),
      name: "Nginx logs",
      query: "source:nginx",
    }),
    type: DatadogAPIClient::V2::CustomDestinationType::CUSTOM_DESTINATION,
  }),
})
p api_instance.create_logs_custom_destination(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Create a Basic HTTP custom destination returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_custom_destinations::LogsCustomDestinationsAPI;
use datadog_api_client::datadogV2::model::CustomDestinationAttributeTagsRestrictionListType;
use datadog_api_client::datadogV2::model::CustomDestinationCreateRequest;
use datadog_api_client::datadogV2::model::CustomDestinationCreateRequestAttributes;
use datadog_api_client::datadogV2::model::CustomDestinationCreateRequestDefinition;
use datadog_api_client::datadogV2::model::CustomDestinationForwardDestination;
use datadog_api_client::datadogV2::model::CustomDestinationForwardDestinationHttp;
use datadog_api_client::datadogV2::model::CustomDestinationForwardDestinationHttpType;
use datadog_api_client::datadogV2::model::CustomDestinationHttpDestinationAuth;
use datadog_api_client::datadogV2::model::CustomDestinationHttpDestinationAuthBasic;
use datadog_api_client::datadogV2::model::CustomDestinationHttpDestinationAuthBasicType;
use datadog_api_client::datadogV2::model::CustomDestinationType;

#[tokio::main]
async fn main() {
    let body = CustomDestinationCreateRequest::new()
        .data(CustomDestinationCreateRequestDefinition::new(
        CustomDestinationCreateRequestAttributes::new(
            CustomDestinationForwardDestination::CustomDestinationForwardDestinationHttp(Box::new(
                CustomDestinationForwardDestinationHttp::new(
                    CustomDestinationHttpDestinationAuth::CustomDestinationHttpDestinationAuthBasic(
                        Box::new(CustomDestinationHttpDestinationAuthBasic::new(
                            "datadog-custom-destination-password".to_string(),
                            CustomDestinationHttpDestinationAuthBasicType::BASIC,
                            "datadog-custom-destination-username".to_string(),
                        )),
                    ),
                    "https://example.com".to_string(),
                    CustomDestinationForwardDestinationHttpType::HTTP,
                ),
            )),
            "Nginx logs".to_string(),
        )
        .enabled(false)
        .forward_tags(false)
        .forward_tags_restriction_list(vec!["datacenter".to_string(), "host".to_string()])
        .forward_tags_restriction_list_type(
            CustomDestinationAttributeTagsRestrictionListType::ALLOW_LIST,
        )
        .query("source:nginx".to_string()),
        CustomDestinationType::CUSTOM_DESTINATION,
    ));
    let configuration = datadog::Configuration::new();
    let api = LogsCustomDestinationsAPI::with_config(configuration);
    let resp = api.create_logs_custom_destination(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#####

```rust
// Create a Custom Header HTTP custom destination returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_custom_destinations::LogsCustomDestinationsAPI;
use datadog_api_client::datadogV2::model::CustomDestinationAttributeTagsRestrictionListType;
use datadog_api_client::datadogV2::model::CustomDestinationCreateRequest;
use datadog_api_client::datadogV2::model::CustomDestinationCreateRequestAttributes;
use datadog_api_client::datadogV2::model::CustomDestinationCreateRequestDefinition;
use datadog_api_client::datadogV2::model::CustomDestinationForwardDestination;
use datadog_api_client::datadogV2::model::CustomDestinationForwardDestinationHttp;
use datadog_api_client::datadogV2::model::CustomDestinationForwardDestinationHttpType;
use datadog_api_client::datadogV2::model::CustomDestinationHttpDestinationAuth;
use datadog_api_client::datadogV2::model::CustomDestinationHttpDestinationAuthCustomHeader;
use datadog_api_client::datadogV2::model::CustomDestinationHttpDestinationAuthCustomHeaderType;
use datadog_api_client::datadogV2::model::CustomDestinationType;

#[tokio::main]
async fn main() {
    let body =
        CustomDestinationCreateRequest
        ::new().data(
            CustomDestinationCreateRequestDefinition::new(
                CustomDestinationCreateRequestAttributes::new(
                    CustomDestinationForwardDestination::CustomDestinationForwardDestinationHttp(
                        Box::new(
                            CustomDestinationForwardDestinationHttp::new(
                                CustomDestinationHttpDestinationAuth::CustomDestinationHttpDestinationAuthCustomHeader(
                                    Box::new(
                                        CustomDestinationHttpDestinationAuthCustomHeader::new(
                                            "MY-AUTHENTICATION-HEADER".to_string(),
                                            "my-secret".to_string(),
                                            CustomDestinationHttpDestinationAuthCustomHeaderType::CUSTOM_HEADER,
                                        ),
                                    ),
                                ),
                                "https://example.com".to_string(),
                                CustomDestinationForwardDestinationHttpType::HTTP,
                            ),
                        ),
                    ),
                    "Nginx logs".to_string(),
                )
                    .enabled(false)
                    .forward_tags(false)
                    .forward_tags_restriction_list(vec!["datacenter".to_string(), "host".to_string()])
                    .forward_tags_restriction_list_type(CustomDestinationAttributeTagsRestrictionListType::ALLOW_LIST)
                    .query("source:nginx".to_string()),
                CustomDestinationType::CUSTOM_DESTINATION,
            ),
        );
    let configuration = datadog::Configuration::new();
    let api = LogsCustomDestinationsAPI::with_config(configuration);
    let resp = api.create_logs_custom_destination(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#####

```rust
// Create a Microsoft Sentinel custom destination returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_custom_destinations::LogsCustomDestinationsAPI;
use datadog_api_client::datadogV2::model::CustomDestinationAttributeTagsRestrictionListType;
use datadog_api_client::datadogV2::model::CustomDestinationCreateRequest;
use datadog_api_client::datadogV2::model::CustomDestinationCreateRequestAttributes;
use datadog_api_client::datadogV2::model::CustomDestinationCreateRequestDefinition;
use datadog_api_client::datadogV2::model::CustomDestinationForwardDestination;
use datadog_api_client::datadogV2::model::CustomDestinationForwardDestinationMicrosoftSentinel;
use datadog_api_client::datadogV2::model::CustomDestinationForwardDestinationMicrosoftSentinelType;
use datadog_api_client::datadogV2::model::CustomDestinationType;

#[tokio::main]
async fn main() {
    let body =
        CustomDestinationCreateRequest
        ::new().data(
            CustomDestinationCreateRequestDefinition::new(
                CustomDestinationCreateRequestAttributes::new(
                    CustomDestinationForwardDestination::CustomDestinationForwardDestinationMicrosoftSentinel(
                        Box::new(
                            CustomDestinationForwardDestinationMicrosoftSentinel::new(
                                "9a2f4d83-2b5e-429e-a35a-2b3c4182db71".to_string(),
                                "https://my-dce-5kyl.eastus-1.ingest.monitor.azure.com".to_string(),
                                "dcr-000a00a000a00000a000000aa000a0aa".to_string(),
                                "Custom-MyTable".to_string(),
                                "f3c9a8a1-4c2e-4d2e-b911-9f3c28c3c8b2".to_string(),
                                CustomDestinationForwardDestinationMicrosoftSentinelType::MICROSOFT_SENTINEL,
                            ),
                        ),
                    ),
                    "Nginx logs".to_string(),
                )
                    .enabled(false)
                    .forward_tags(false)
                    .forward_tags_restriction_list(vec!["datacenter".to_string(), "host".to_string()])
                    .forward_tags_restriction_list_type(CustomDestinationAttributeTagsRestrictionListType::ALLOW_LIST)
                    .query("source:nginx".to_string()),
                CustomDestinationType::CUSTOM_DESTINATION,
            ),
        );
    let configuration = datadog::Configuration::new();
    let api = LogsCustomDestinationsAPI::with_config(configuration);
    let resp = api.create_logs_custom_destination(body).await;
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
 * Create a Basic HTTP custom destination returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsCustomDestinationsApi(configuration);

const params: v2.LogsCustomDestinationsApiCreateLogsCustomDestinationRequest = {
  body: {
    data: {
      attributes: {
        enabled: false,
        forwardTags: false,
        forwardTagsRestrictionList: ["datacenter", "host"],
        forwardTagsRestrictionListType: "ALLOW_LIST",
        forwarderDestination: {
          auth: {
            password: "datadog-custom-destination-password",
            type: "basic",
            username: "datadog-custom-destination-username",
          },
          endpoint: "https://example.com",
          type: "http",
        },
        name: "Nginx logs",
        query: "source:nginx",
      },
      type: "custom_destination",
    },
  },
};

apiInstance
  .createLogsCustomDestination(params)
  .then((data: v2.CustomDestinationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#####

```typescript
/**
 * Create a Custom Header HTTP custom destination returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsCustomDestinationsApi(configuration);

const params: v2.LogsCustomDestinationsApiCreateLogsCustomDestinationRequest = {
  body: {
    data: {
      attributes: {
        enabled: false,
        forwardTags: false,
        forwardTagsRestrictionList: ["datacenter", "host"],
        forwardTagsRestrictionListType: "ALLOW_LIST",
        forwarderDestination: {
          auth: {
            headerValue: "my-secret",
            type: "custom_header",
            headerName: "MY-AUTHENTICATION-HEADER",
          },
          endpoint: "https://example.com",
          type: "http",
        },
        name: "Nginx logs",
        query: "source:nginx",
      },
      type: "custom_destination",
    },
  },
};

apiInstance
  .createLogsCustomDestination(params)
  .then((data: v2.CustomDestinationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#####

```typescript
/**
 * Create a Microsoft Sentinel custom destination returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsCustomDestinationsApi(configuration);

const params: v2.LogsCustomDestinationsApiCreateLogsCustomDestinationRequest = {
  body: {
    data: {
      attributes: {
        enabled: false,
        forwardTags: false,
        forwardTagsRestrictionList: ["datacenter", "host"],
        forwardTagsRestrictionListType: "ALLOW_LIST",
        forwarderDestination: {
          type: "microsoft_sentinel",
          tenantId: "f3c9a8a1-4c2e-4d2e-b911-9f3c28c3c8b2",
          clientId: "9a2f4d83-2b5e-429e-a35a-2b3c4182db71",
          dataCollectionEndpoint:
            "https://my-dce-5kyl.eastus-1.ingest.monitor.azure.com",
          dataCollectionRuleId: "dcr-000a00a000a00000a000000aa000a0aa",
          streamName: "Custom-MyTable",
        },
        name: "Nginx logs",
        query: "source:nginx",
      },
      type: "custom_destination",
    },
  },
};

apiInstance
  .createLogsCustomDestination(params)
  .then((data: v2.CustomDestinationResponse) => {
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

## Get a custom destination{% #get-a-custom-destination %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/custom-destinations/{custom_destination_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/custom-destinations/{custom_destination_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |

### Overview

Get a specific custom destination in your organization. This endpoint requires any of the following permissions:
`logs_read_config``logs_read_data`


### Arguments

#### Path Parameters

| Name                                    | Type   | Description                       |
| --------------------------------------- | ------ | --------------------------------- |
| custom_destination_id [*required*] | string | The ID of the custom destination. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The custom destination.

| Parent field          | Field                                      | Type          | Description                                                                                                                                                                                                                      |
| --------------------- | ------------------------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                                       | object        | The definition of a custom destination.                                                                                                                                                                                          |
| data                  | attributes                                 | object        | The attributes associated with the custom destination.                                                                                                                                                                           |
| attributes            | enabled                                    | boolean       | Whether logs matching this custom destination should be forwarded or not.                                                                                                                                                        |
| attributes            | forward_tags                               | boolean       | Whether tags from the forwarded logs should be forwarded or not.                                                                                                                                                                 |
| attributes            | forward_tags_restriction_list              | [string]      | List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be filtered.                                                                                                                          | An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter. |
| attributes            | forward_tags_restriction_list_type         | enum          | How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.                                      | `BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST`                |
| attributes            | forwarder_destination                      |  <oneOf> | A custom destination's location to forward logs.                                                                                                                                                                                 |
| forwarder_destination | Option 1                                   | object        | The HTTP destination.                                                                                                                                                                                                            |
| Option 1              | auth [*required*]                     |  <oneOf> | Authentication method of the HTTP requests.                                                                                                                                                                                      |
| auth                  | Option 1                                   | object        | Basic access authentication.                                                                                                                                                                                                     |
| Option 1              | type [*required*]                     | enum          | Type of the basic access authentication. Allowed enum values: `basic`                                                                                                                                                            |
| auth                  | Option 2                                   | object        | Custom header access authentication.                                                                                                                                                                                             |
| Option 2              | header_name [*required*]              | string        | The header name of the authentication.                                                                                                                                                                                           |
| Option 2              | type [*required*]                     | enum          | Type of the custom header access authentication. Allowed enum values: `custom_header`                                                                                                                                            |
| Option 1              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 1              | type [*required*]                     | enum          | Type of the HTTP destination. Allowed enum values: `http`                                                                                                                                                                        |
| forwarder_destination | Option 2                                   | object        | The Splunk HTTP Event Collector (HEC) destination.                                                                                                                                                                               |
| Option 2              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 2              | type [*required*]                     | enum          | Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`                                                                                                                                     |
| forwarder_destination | Option 3                                   | object        | The Elasticsearch destination.                                                                                                                                                                                                   |
| Option 3              | auth [*required*]                     | object        | Basic access authentication.                                                                                                                                                                                                     |
| additionalProperties  | <any-key>                                  |               | Basic access authentication.                                                                                                                                                                                                     |
| Option 3              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 3              | index_name [*required*]               | string        | Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).                                 |
| Option 3              | index_rotation                             | string        | Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options: | If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).                                           |
| Option 3              | type [*required*]                     | enum          | Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`                                                                                                                                                      |
| forwarder_destination | Option 4                                   | object        | The Microsoft Sentinel destination.                                                                                                                                                                                              |
| Option 4              | client_id [*required*]                | string        | Client ID from the Datadog Azure integration.                                                                                                                                                                                    |
| Option 4              | data_collection_endpoint [*required*] | string        | Azure data collection endpoint.                                                                                                                                                                                                  |
| Option 4              | data_collection_rule_id [*required*]  | string        | Azure data collection rule ID.                                                                                                                                                                                                   |
| Option 4              | stream_name [*required*]              | string        | Azure stream name.                                                                                                                                                                                                               |
| Option 4              | tenant_id [*required*]                | string        | Tenant ID from the Datadog Azure integration.                                                                                                                                                                                    |
| Option 4              | type [*required*]                     | enum          | Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`                                                                                                                                            |
| attributes            | name                                       | string        | The custom destination name.                                                                                                                                                                                                     |
| attributes            | query                                      | string        | The custom destination query filter. Logs matching this query are forwarded to the destination.                                                                                                                                  |
| data                  | id                                         | string        | The custom destination ID.                                                                                                                                                                                                       |
| data                  | type                                       | enum          | The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`                                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enabled": true,
      "forward_tags": true,
      "forward_tags_restriction_list": [
        "datacenter",
        "host"
      ],
      "forward_tags_restriction_list_type": "ALLOW_LIST",
      "forwarder_destination": {
        "auth": {
          "type": "basic"
        },
        "endpoint": "https://example.com",
        "type": "http"
      },
      "name": "Nginx logs",
      "query": "source:nginx"
    },
    "id": "be5d7a69-d0c8-4d4d-8ee8-bba292d98139",
    "type": "custom_destination"
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
                  \# Path parametersexport custom_destination_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/${custom_destination_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a custom destination returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi

# there is a valid "custom_destination" in the system
CUSTOM_DESTINATION_DATA_ID = environ["CUSTOM_DESTINATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.get_logs_custom_destination(
        custom_destination_id=CUSTOM_DESTINATION_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a custom destination returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsCustomDestinationsAPI.new

# there is a valid "custom_destination" in the system
CUSTOM_DESTINATION_DATA_ID = ENV["CUSTOM_DESTINATION_DATA_ID"]
p api_instance.get_logs_custom_destination(CUSTOM_DESTINATION_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a custom destination returns "OK" response

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
    // there is a valid "custom_destination" in the system
    CustomDestinationDataID := os.Getenv("CUSTOM_DESTINATION_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsCustomDestinationsApi(apiClient)
    resp, r, err := api.GetLogsCustomDestination(ctx, CustomDestinationDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsCustomDestinationsApi.GetLogsCustomDestination`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsCustomDestinationsApi.GetLogsCustomDestination`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a custom destination returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsCustomDestinationsApi;
import com.datadog.api.client.v2.model.CustomDestinationResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsCustomDestinationsApi apiInstance = new LogsCustomDestinationsApi(defaultClient);

    // there is a valid "custom_destination" in the system
    String CUSTOM_DESTINATION_DATA_ID = System.getenv("CUSTOM_DESTINATION_DATA_ID");

    try {
      CustomDestinationResponse result =
          apiInstance.getLogsCustomDestination(CUSTOM_DESTINATION_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsCustomDestinationsApi#getLogsCustomDestination");
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
// Get a custom destination returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_custom_destinations::LogsCustomDestinationsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "custom_destination" in the system
    let custom_destination_data_id = std::env::var("CUSTOM_DESTINATION_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = LogsCustomDestinationsAPI::with_config(configuration);
    let resp = api
        .get_logs_custom_destination(custom_destination_data_id.clone())
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
 * Get a custom destination returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsCustomDestinationsApi(configuration);

// there is a valid "custom_destination" in the system
const CUSTOM_DESTINATION_DATA_ID = process.env
  .CUSTOM_DESTINATION_DATA_ID as string;

const params: v2.LogsCustomDestinationsApiGetLogsCustomDestinationRequest = {
  customDestinationId: CUSTOM_DESTINATION_DATA_ID,
};

apiInstance
  .getLogsCustomDestination(params)
  .then((data: v2.CustomDestinationResponse) => {
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

## Update a custom destination{% #update-a-custom-destination %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/logs/config/custom-destinations/{custom_destination_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/logs/config/custom-destinations/{custom_destination_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |

### Overview

Update the given fields of a specific custom destination in your organization. This endpoint requires the `logs_write_forwarding_rules` permission.

### Arguments

#### Path Parameters

| Name                                    | Type   | Description                       |
| --------------------------------------- | ------ | --------------------------------- |
| custom_destination_id [*required*] | string | The ID of the custom destination. |

### Request

#### Body Data (required)

New definition of the custom destination's fields.

{% tab title="Model" %}

| Parent field          | Field                                      | Type          | Description                                                                                                                                                                                                                                                                                 |
| --------------------- | ------------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                                       | object        | The definition of a custom destination.                                                                                                                                                                                                                                                     |
| data                  | attributes                                 | object        | The attributes associated with the custom destination.                                                                                                                                                                                                                                      |
| attributes            | enabled                                    | boolean       | Whether logs matching this custom destination should be forwarded or not.                                                                                                                                                                                                                   |
| attributes            | forward_tags                               | boolean       | Whether tags from the forwarded logs should be forwarded or not.                                                                                                                                                                                                                            |
| attributes            | forward_tags_restriction_list              | [string]      | List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be restricted from being forwarded. An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter. |
| attributes            | forward_tags_restriction_list_type         | enum          | How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.                                                                                                 | `BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST` |
| attributes            | forwarder_destination                      |  <oneOf> | A custom destination's location to forward logs.                                                                                                                                                                                                                                            |
| forwarder_destination | Option 1                                   | object        | The HTTP destination.                                                                                                                                                                                                                                                                       |
| Option 1              | auth [*required*]                     |  <oneOf> | Authentication method of the HTTP requests.                                                                                                                                                                                                                                                 |
| auth                  | Option 1                                   | object        | Basic access authentication.                                                                                                                                                                                                                                                                |
| Option 1              | password [*required*]                 | string        | The password of the authentication. This field is not returned by the API.                                                                                                                                                                                                                  |
| Option 1              | type [*required*]                     | enum          | Type of the basic access authentication. Allowed enum values: `basic`                                                                                                                                                                                                                       |
| Option 1              | username [*required*]                 | string        | The username of the authentication. This field is not returned by the API.                                                                                                                                                                                                                  |
| auth                  | Option 2                                   | object        | Custom header access authentication.                                                                                                                                                                                                                                                        |
| Option 2              | header_name [*required*]              | string        | The header name of the authentication.                                                                                                                                                                                                                                                      |
| Option 2              | header_value [*required*]             | string        | The header value of the authentication. This field is not returned by the API.                                                                                                                                                                                                              |
| Option 2              | type [*required*]                     | enum          | Type of the custom header access authentication. Allowed enum values: `custom_header`                                                                                                                                                                                                       |
| Option 1              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                                                                                  |
| Option 1              | type [*required*]                     | enum          | Type of the HTTP destination. Allowed enum values: `http`                                                                                                                                                                                                                                   |
| forwarder_destination | Option 2                                   | object        | The Splunk HTTP Event Collector (HEC) destination.                                                                                                                                                                                                                                          |
| Option 2              | access_token [*required*]             | string        | Access token of the Splunk HTTP Event Collector. This field is not returned by the API.                                                                                                                                                                                                     |
| Option 2              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                                                                                  |
| Option 2              | type [*required*]                     | enum          | Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`                                                                                                                                                                                                |
| forwarder_destination | Option 3                                   | object        | The Elasticsearch destination.                                                                                                                                                                                                                                                              |
| Option 3              | auth [*required*]                     | object        | Basic access authentication.                                                                                                                                                                                                                                                                |
| auth                  | password [*required*]                 | string        | The password of the authentication. This field is not returned by the API.                                                                                                                                                                                                                  |
| auth                  | username [*required*]                 | string        | The username of the authentication. This field is not returned by the API.                                                                                                                                                                                                                  |
| Option 3              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                                                                                  |
| Option 3              | index_name [*required*]               | string        | Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).                                                                                            |
| Option 3              | index_rotation                             | string        | Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options:                                                            | If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).                            |
| Option 3              | type [*required*]                     | enum          | Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`                                                                                                                                                                                                                 |
| forwarder_destination | Option 4                                   | object        | The Microsoft Sentinel destination.                                                                                                                                                                                                                                                         |
| Option 4              | client_id [*required*]                | string        | Client ID from the Datadog Azure integration.                                                                                                                                                                                                                                               |
| Option 4              | data_collection_endpoint [*required*] | string        | Azure data collection endpoint.                                                                                                                                                                                                                                                             |
| Option 4              | data_collection_rule_id [*required*]  | string        | Azure data collection rule ID.                                                                                                                                                                                                                                                              |
| Option 4              | stream_name [*required*]              | string        | Azure stream name.                                                                                                                                                                                                                                                                          |
| Option 4              | tenant_id [*required*]                | string        | Tenant ID from the Datadog Azure integration.                                                                                                                                                                                                                                               |
| Option 4              | type [*required*]                     | enum          | Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`                                                                                                                                                                                                       |
| attributes            | name                                       | string        | The custom destination name.                                                                                                                                                                                                                                                                |
| attributes            | query                                      | string        | The custom destination query and filter. Logs matching this query are forwarded to the destination.                                                                                                                                                                                         |
| data                  | id [*required*]                       | string        | The custom destination ID.                                                                                                                                                                                                                                                                  |
| data                  | type [*required*]                     | enum          | The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`                                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "Nginx logs (Updated)",
      "query": "source:nginx",
      "enabled": false,
      "forward_tags": false,
      "forward_tags_restriction_list_type": "BLOCK_LIST"
    },
    "type": "custom_destination",
    "id": "be5d7a69-d0c8-4d4d-8ee8-bba292d98139"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The custom destination.

| Parent field          | Field                                      | Type          | Description                                                                                                                                                                                                                      |
| --------------------- | ------------------------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                                       | object        | The definition of a custom destination.                                                                                                                                                                                          |
| data                  | attributes                                 | object        | The attributes associated with the custom destination.                                                                                                                                                                           |
| attributes            | enabled                                    | boolean       | Whether logs matching this custom destination should be forwarded or not.                                                                                                                                                        |
| attributes            | forward_tags                               | boolean       | Whether tags from the forwarded logs should be forwarded or not.                                                                                                                                                                 |
| attributes            | forward_tags_restriction_list              | [string]      | List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be filtered.                                                                                                                          | An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter. |
| attributes            | forward_tags_restriction_list_type         | enum          | How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.                                      | `BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST`                |
| attributes            | forwarder_destination                      |  <oneOf> | A custom destination's location to forward logs.                                                                                                                                                                                 |
| forwarder_destination | Option 1                                   | object        | The HTTP destination.                                                                                                                                                                                                            |
| Option 1              | auth [*required*]                     |  <oneOf> | Authentication method of the HTTP requests.                                                                                                                                                                                      |
| auth                  | Option 1                                   | object        | Basic access authentication.                                                                                                                                                                                                     |
| Option 1              | type [*required*]                     | enum          | Type of the basic access authentication. Allowed enum values: `basic`                                                                                                                                                            |
| auth                  | Option 2                                   | object        | Custom header access authentication.                                                                                                                                                                                             |
| Option 2              | header_name [*required*]              | string        | The header name of the authentication.                                                                                                                                                                                           |
| Option 2              | type [*required*]                     | enum          | Type of the custom header access authentication. Allowed enum values: `custom_header`                                                                                                                                            |
| Option 1              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 1              | type [*required*]                     | enum          | Type of the HTTP destination. Allowed enum values: `http`                                                                                                                                                                        |
| forwarder_destination | Option 2                                   | object        | The Splunk HTTP Event Collector (HEC) destination.                                                                                                                                                                               |
| Option 2              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 2              | type [*required*]                     | enum          | Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`                                                                                                                                     |
| forwarder_destination | Option 3                                   | object        | The Elasticsearch destination.                                                                                                                                                                                                   |
| Option 3              | auth [*required*]                     | object        | Basic access authentication.                                                                                                                                                                                                     |
| additionalProperties  | <any-key>                                  |               | Basic access authentication.                                                                                                                                                                                                     |
| Option 3              | endpoint [*required*]                 | string        | The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.                                                                                                       |
| Option 3              | index_name [*required*]               | string        | Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).                                 |
| Option 3              | index_rotation                             | string        | Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options: | If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).                                           |
| Option 3              | type [*required*]                     | enum          | Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`                                                                                                                                                      |
| forwarder_destination | Option 4                                   | object        | The Microsoft Sentinel destination.                                                                                                                                                                                              |
| Option 4              | client_id [*required*]                | string        | Client ID from the Datadog Azure integration.                                                                                                                                                                                    |
| Option 4              | data_collection_endpoint [*required*] | string        | Azure data collection endpoint.                                                                                                                                                                                                  |
| Option 4              | data_collection_rule_id [*required*]  | string        | Azure data collection rule ID.                                                                                                                                                                                                   |
| Option 4              | stream_name [*required*]              | string        | Azure stream name.                                                                                                                                                                                                               |
| Option 4              | tenant_id [*required*]                | string        | Tenant ID from the Datadog Azure integration.                                                                                                                                                                                    |
| Option 4              | type [*required*]                     | enum          | Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`                                                                                                                                            |
| attributes            | name                                       | string        | The custom destination name.                                                                                                                                                                                                     |
| attributes            | query                                      | string        | The custom destination query filter. Logs matching this query are forwarded to the destination.                                                                                                                                  |
| data                  | id                                         | string        | The custom destination ID.                                                                                                                                                                                                       |
| data                  | type                                       | enum          | The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`                                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "enabled": true,
      "forward_tags": true,
      "forward_tags_restriction_list": [
        "datacenter",
        "host"
      ],
      "forward_tags_restriction_list_type": "ALLOW_LIST",
      "forwarder_destination": {
        "auth": {
          "type": "basic"
        },
        "endpoint": "https://example.com",
        "type": "http"
      },
      "name": "Nginx logs",
      "query": "source:nginx"
    },
    "id": "be5d7a69-d0c8-4d4d-8ee8-bba292d98139",
    "type": "custom_destination"
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
                          \# Path parametersexport custom_destination_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/${custom_destination_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Nginx logs (Updated)",
      "query": "source:nginx",
      "enabled": false,
      "forward_tags": false,
      "forward_tags_restriction_list_type": "BLOCK_LIST"
    },
    "type": "custom_destination",
    "id": "be5d7a69-d0c8-4d4d-8ee8-bba292d98139"
  }
}
EOF

#####

```go
// Update a custom destination returns "OK" response

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
    // there is a valid "custom_destination" in the system
    CustomDestinationDataID := os.Getenv("CUSTOM_DESTINATION_DATA_ID")

    body := datadogV2.CustomDestinationUpdateRequest{
        Data: &datadogV2.CustomDestinationUpdateRequestDefinition{
            Attributes: &datadogV2.CustomDestinationUpdateRequestAttributes{
                Name:                           datadog.PtrString("Nginx logs (Updated)"),
                Query:                          datadog.PtrString("source:nginx"),
                Enabled:                        datadog.PtrBool(false),
                ForwardTags:                    datadog.PtrBool(false),
                ForwardTagsRestrictionListType: datadogV2.CUSTOMDESTINATIONATTRIBUTETAGSRESTRICTIONLISTTYPE_BLOCK_LIST.Ptr(),
            },
            Type: datadogV2.CUSTOMDESTINATIONTYPE_CUSTOM_DESTINATION,
            Id:   CustomDestinationDataID,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsCustomDestinationsApi(apiClient)
    resp, r, err := api.UpdateLogsCustomDestination(ctx, CustomDestinationDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsCustomDestinationsApi.UpdateLogsCustomDestination`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsCustomDestinationsApi.UpdateLogsCustomDestination`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update a custom destination returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsCustomDestinationsApi;
import com.datadog.api.client.v2.model.CustomDestinationAttributeTagsRestrictionListType;
import com.datadog.api.client.v2.model.CustomDestinationResponse;
import com.datadog.api.client.v2.model.CustomDestinationType;
import com.datadog.api.client.v2.model.CustomDestinationUpdateRequest;
import com.datadog.api.client.v2.model.CustomDestinationUpdateRequestAttributes;
import com.datadog.api.client.v2.model.CustomDestinationUpdateRequestDefinition;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsCustomDestinationsApi apiInstance = new LogsCustomDestinationsApi(defaultClient);

    // there is a valid "custom_destination" in the system
    String CUSTOM_DESTINATION_DATA_ID = System.getenv("CUSTOM_DESTINATION_DATA_ID");

    CustomDestinationUpdateRequest body =
        new CustomDestinationUpdateRequest()
            .data(
                new CustomDestinationUpdateRequestDefinition()
                    .attributes(
                        new CustomDestinationUpdateRequestAttributes()
                            .name("Nginx logs (Updated)")
                            .query("source:nginx")
                            .enabled(false)
                            .forwardTags(false)
                            .forwardTagsRestrictionListType(
                                CustomDestinationAttributeTagsRestrictionListType.BLOCK_LIST))
                    .type(CustomDestinationType.CUSTOM_DESTINATION)
                    .id(CUSTOM_DESTINATION_DATA_ID));

    try {
      CustomDestinationResponse result =
          apiInstance.updateLogsCustomDestination(CUSTOM_DESTINATION_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsCustomDestinationsApi#updateLogsCustomDestination");
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
Update a custom destination returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination_attribute_tags_restriction_list_type import (
    CustomDestinationAttributeTagsRestrictionListType,
)
from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType
from datadog_api_client.v2.model.custom_destination_update_request import CustomDestinationUpdateRequest
from datadog_api_client.v2.model.custom_destination_update_request_attributes import (
    CustomDestinationUpdateRequestAttributes,
)
from datadog_api_client.v2.model.custom_destination_update_request_definition import (
    CustomDestinationUpdateRequestDefinition,
)

# there is a valid "custom_destination" in the system
CUSTOM_DESTINATION_DATA_ID = environ["CUSTOM_DESTINATION_DATA_ID"]

body = CustomDestinationUpdateRequest(
    data=CustomDestinationUpdateRequestDefinition(
        attributes=CustomDestinationUpdateRequestAttributes(
            name="Nginx logs (Updated)",
            query="source:nginx",
            enabled=False,
            forward_tags=False,
            forward_tags_restriction_list_type=CustomDestinationAttributeTagsRestrictionListType.BLOCK_LIST,
        ),
        type=CustomDestinationType.CUSTOM_DESTINATION,
        id=CUSTOM_DESTINATION_DATA_ID,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.update_logs_custom_destination(custom_destination_id=CUSTOM_DESTINATION_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update a custom destination returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsCustomDestinationsAPI.new

# there is a valid "custom_destination" in the system
CUSTOM_DESTINATION_DATA_ID = ENV["CUSTOM_DESTINATION_DATA_ID"]

body = DatadogAPIClient::V2::CustomDestinationUpdateRequest.new({
  data: DatadogAPIClient::V2::CustomDestinationUpdateRequestDefinition.new({
    attributes: DatadogAPIClient::V2::CustomDestinationUpdateRequestAttributes.new({
      name: "Nginx logs (Updated)",
      query: "source:nginx",
      enabled: false,
      forward_tags: false,
      forward_tags_restriction_list_type: DatadogAPIClient::V2::CustomDestinationAttributeTagsRestrictionListType::BLOCK_LIST,
    }),
    type: DatadogAPIClient::V2::CustomDestinationType::CUSTOM_DESTINATION,
    id: CUSTOM_DESTINATION_DATA_ID,
  }),
})
p api_instance.update_logs_custom_destination(CUSTOM_DESTINATION_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Update a custom destination returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_custom_destinations::LogsCustomDestinationsAPI;
use datadog_api_client::datadogV2::model::CustomDestinationAttributeTagsRestrictionListType;
use datadog_api_client::datadogV2::model::CustomDestinationType;
use datadog_api_client::datadogV2::model::CustomDestinationUpdateRequest;
use datadog_api_client::datadogV2::model::CustomDestinationUpdateRequestAttributes;
use datadog_api_client::datadogV2::model::CustomDestinationUpdateRequestDefinition;

#[tokio::main]
async fn main() {
    // there is a valid "custom_destination" in the system
    let custom_destination_data_id = std::env::var("CUSTOM_DESTINATION_DATA_ID").unwrap();
    let body = CustomDestinationUpdateRequest::new().data(
        CustomDestinationUpdateRequestDefinition::new(
            custom_destination_data_id.clone(),
            CustomDestinationType::CUSTOM_DESTINATION,
        )
        .attributes(
            CustomDestinationUpdateRequestAttributes::new()
                .enabled(false)
                .forward_tags(false)
                .forward_tags_restriction_list_type(
                    CustomDestinationAttributeTagsRestrictionListType::BLOCK_LIST,
                )
                .name("Nginx logs (Updated)".to_string())
                .query("source:nginx".to_string()),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = LogsCustomDestinationsAPI::with_config(configuration);
    let resp = api
        .update_logs_custom_destination(custom_destination_data_id.clone(), body)
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
 * Update a custom destination returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsCustomDestinationsApi(configuration);

// there is a valid "custom_destination" in the system
const CUSTOM_DESTINATION_DATA_ID = process.env
  .CUSTOM_DESTINATION_DATA_ID as string;

const params: v2.LogsCustomDestinationsApiUpdateLogsCustomDestinationRequest = {
  body: {
    data: {
      attributes: {
        name: "Nginx logs (Updated)",
        query: "source:nginx",
        enabled: false,
        forwardTags: false,
        forwardTagsRestrictionListType: "BLOCK_LIST",
      },
      type: "custom_destination",
      id: CUSTOM_DESTINATION_DATA_ID,
    },
  },
  customDestinationId: CUSTOM_DESTINATION_DATA_ID,
};

apiInstance
  .updateLogsCustomDestination(params)
  .then((data: v2.CustomDestinationResponse) => {
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

## Delete a custom destination{% #delete-a-custom-destination %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                        |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/logs/config/custom-destinations/{custom_destination_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/logs/config/custom-destinations/{custom_destination_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id} |

### Overview

Delete a specific custom destination in your organization. This endpoint requires the `logs_write_forwarding_rules` permission.

### Arguments

#### Path Parameters

| Name                                    | Type   | Description                       |
| --------------------------------------- | ------ | --------------------------------- |
| custom_destination_id [*required*] | string | The ID of the custom destination. |

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
                  \# Path parametersexport custom_destination_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/${custom_destination_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a custom destination returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi

# there is a valid "custom_destination" in the system
CUSTOM_DESTINATION_DATA_ID = environ["CUSTOM_DESTINATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    api_instance.delete_logs_custom_destination(
        custom_destination_id=CUSTOM_DESTINATION_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete a custom destination returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsCustomDestinationsAPI.new

# there is a valid "custom_destination" in the system
CUSTOM_DESTINATION_DATA_ID = ENV["CUSTOM_DESTINATION_DATA_ID"]
api_instance.delete_logs_custom_destination(CUSTOM_DESTINATION_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete a custom destination returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "custom_destination" in the system
    CustomDestinationDataID := os.Getenv("CUSTOM_DESTINATION_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsCustomDestinationsApi(apiClient)
    r, err := api.DeleteLogsCustomDestination(ctx, CustomDestinationDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsCustomDestinationsApi.DeleteLogsCustomDestination`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete a custom destination returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsCustomDestinationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsCustomDestinationsApi apiInstance = new LogsCustomDestinationsApi(defaultClient);

    // there is a valid "custom_destination" in the system
    String CUSTOM_DESTINATION_DATA_ID = System.getenv("CUSTOM_DESTINATION_DATA_ID");

    try {
      apiInstance.deleteLogsCustomDestination(CUSTOM_DESTINATION_DATA_ID);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsCustomDestinationsApi#deleteLogsCustomDestination");
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
// Delete a custom destination returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_custom_destinations::LogsCustomDestinationsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "custom_destination" in the system
    let custom_destination_data_id = std::env::var("CUSTOM_DESTINATION_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = LogsCustomDestinationsAPI::with_config(configuration);
    let resp = api
        .delete_logs_custom_destination(custom_destination_data_id.clone())
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
 * Delete a custom destination returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.LogsCustomDestinationsApi(configuration);

// there is a valid "custom_destination" in the system
const CUSTOM_DESTINATION_DATA_ID = process.env
  .CUSTOM_DESTINATION_DATA_ID as string;

const params: v2.LogsCustomDestinationsApiDeleteLogsCustomDestinationRequest = {
  customDestinationId: CUSTOM_DESTINATION_DATA_ID,
};

apiInstance
  .deleteLogsCustomDestination(params)
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
