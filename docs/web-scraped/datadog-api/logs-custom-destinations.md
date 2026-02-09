# Source: https://docs.datadoghq.com/api/latest/logs-custom-destinations/

# Logs Custom Destinations
Custom Destinations forward all the logs ingested to an external destination.
**Note** : Log forwarding is not available for the Government (US1-FED) site. Contact your account representative for more information.
See the [Custom Destinations Page](https://app.datadoghq.com/logs/pipelines/log-forwarding/custom-destinations) for a list of the custom destinations currently configured in web UI.
## [Get all custom destinations](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#get-all-custom-destinations)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#get-all-custom-destinations-v2)


GET https://api.ap1.datadoghq.com/api/v2/logs/config/custom-destinationshttps://api.ap2.datadoghq.com/api/v2/logs/config/custom-destinationshttps://api.datadoghq.eu/api/v2/logs/config/custom-destinationshttps://api.ddog-gov.com/api/v2/logs/config/custom-destinationshttps://api.datadoghq.com/api/v2/logs/config/custom-destinationshttps://api.us3.datadoghq.com/api/v2/logs/config/custom-destinationshttps://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations
### Overview
Get the list of configured custom destinations in your organization with their definitions. This endpoint requires any of the following permissions:
* `logs_read_config`
* `logs_read_data`
  

### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#ListLogsCustomDestinations-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#ListLogsCustomDestinations-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#ListLogsCustomDestinations-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


The available custom destinations.
Field
Type
Description
data
[object]
A list of custom destinations.
attributes
object
The attributes associated with the custom destination.
enabled
boolean
Whether logs matching this custom destination should be forwarded or not.
default: `true`
forward_tags
boolean
Whether tags from the forwarded logs should be forwarded or not.
default: `true`
forward_tags_restriction_list
[string]
List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be filtered.
An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter.
default: 
forward_tags_restriction_list_type
enum
How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.
`BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST`
default: `ALLOW_LIST`
forwarder_destination
<oneOf>
A custom destination's location to forward logs.
Option 1
object
The HTTP destination.
auth [_required_]
<oneOf>
Authentication method of the HTTP requests.
Option 1
object
Basic access authentication.
type [_required_]
enum
Type of the basic access authentication. Allowed enum values: `basic`
default: `basic`
Option 2
object
Custom header access authentication.
header_name [_required_]
string
The header name of the authentication.
type [_required_]
enum
Type of the custom header access authentication. Allowed enum values: `custom_header`
default: `custom_header`
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the HTTP destination. Allowed enum values: `http`
default: `http`
Option 2
object
The Splunk HTTP Event Collector (HEC) destination.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`
default: `splunk_hec`
Option 3
object
The Elasticsearch destination.
auth [_required_]
object
Basic access authentication.
<any-key>
Basic access authentication.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
index_name [_required_]
string
Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).
index_rotation
string
Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options:
  * Hourly: `yyyy-MM-dd-HH` (as an example, it would render: `2022-10-19-09`)
  * Daily: `yyyy-MM-dd` (as an example, it would render: `2022-10-19`)
  * Weekly: `yyyy-'W'ww` (as an example, it would render: `2022-W42`)
  * Monthly: `yyyy-MM` (as an example, it would render: `2022-10`)


If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).
type [_required_]
enum
Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`
default: `elasticsearch`
Option 4
object
The Microsoft Sentinel destination.
client_id [_required_]
string
Client ID from the Datadog Azure integration.
data_collection_endpoint [_required_]
string
Azure data collection endpoint.
data_collection_rule_id [_required_]
string
Azure data collection rule ID.
stream_name [_required_]
string
Azure stream name.
tenant_id [_required_]
string
Tenant ID from the Datadog Azure integration.
type [_required_]
enum
Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
name
string
The custom destination name.
query
string
The custom destination query filter. Logs matching this query are forwarded to the destination.
id
string
The custom destination ID.
type
enum
The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`
default: `custom_destination`
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=typescript)


#####  Get all custom destinations
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all custom destinations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all custom destinations
```
# Get all custom destinations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsCustomDestinationsAPI.new
p api_instance.list_logs_custom_destinations()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all custom destinations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all custom destinations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get all custom destinations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get all custom destinations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Create a custom destination](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#create-a-custom-destination)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#create-a-custom-destination-v2)


POST https://api.ap1.datadoghq.com/api/v2/logs/config/custom-destinationshttps://api.ap2.datadoghq.com/api/v2/logs/config/custom-destinationshttps://api.datadoghq.eu/api/v2/logs/config/custom-destinationshttps://api.ddog-gov.com/api/v2/logs/config/custom-destinationshttps://api.datadoghq.com/api/v2/logs/config/custom-destinationshttps://api.us3.datadoghq.com/api/v2/logs/config/custom-destinationshttps://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations
### Overview
Create a custom destination in your organization. This endpoint requires the `logs_write_forwarding_rules` permission.
### Request
#### Body Data (required)
The definition of the new custom destination.
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


Field
Type
Description
data
object
The definition of a custom destination.
attributes [_required_]
object
The attributes associated with the custom destination.
enabled
boolean
Whether logs matching this custom destination should be forwarded or not.
default: `true`
forward_tags
boolean
Whether tags from the forwarded logs should be forwarded or not.
default: `true`
forward_tags_restriction_list
[string]
List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be filtered.
An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter.
default: 
forward_tags_restriction_list_type
enum
How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.
`BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST`
default: `ALLOW_LIST`
forwarder_destination [_required_]
<oneOf>
A custom destination's location to forward logs.
Option 1
object
The HTTP destination.
auth [_required_]
<oneOf>
Authentication method of the HTTP requests.
Option 1
object
Basic access authentication.
password [_required_]
string
The password of the authentication. This field is not returned by the API.
type [_required_]
enum
Type of the basic access authentication. Allowed enum values: `basic`
default: `basic`
username [_required_]
string
The username of the authentication. This field is not returned by the API.
Option 2
object
Custom header access authentication.
header_name [_required_]
string
The header name of the authentication.
header_value [_required_]
string
The header value of the authentication. This field is not returned by the API.
type [_required_]
enum
Type of the custom header access authentication. Allowed enum values: `custom_header`
default: `custom_header`
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the HTTP destination. Allowed enum values: `http`
default: `http`
Option 2
object
The Splunk HTTP Event Collector (HEC) destination.
access_token [_required_]
string
Access token of the Splunk HTTP Event Collector. This field is not returned by the API.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`
default: `splunk_hec`
Option 3
object
The Elasticsearch destination.
auth [_required_]
object
Basic access authentication.
password [_required_]
string
The password of the authentication. This field is not returned by the API.
username [_required_]
string
The username of the authentication. This field is not returned by the API.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
index_name [_required_]
string
Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).
index_rotation
string
Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options:
  * Hourly: `yyyy-MM-dd-HH` (as an example, it would render: `2022-10-19-09`)
  * Daily: `yyyy-MM-dd` (as an example, it would render: `2022-10-19`)
  * Weekly: `yyyy-'W'ww` (as an example, it would render: `2022-W42`)
  * Monthly: `yyyy-MM` (as an example, it would render: `2022-10`)


If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).
type [_required_]
enum
Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`
default: `elasticsearch`
Option 4
object
The Microsoft Sentinel destination.
client_id [_required_]
string
Client ID from the Datadog Azure integration.
data_collection_endpoint [_required_]
string
Azure data collection endpoint.
data_collection_rule_id [_required_]
string
Azure data collection rule ID.
stream_name [_required_]
string
Azure stream name.
tenant_id [_required_]
string
Tenant ID from the Datadog Azure integration.
type [_required_]
enum
Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
name [_required_]
string
The custom destination name.
query
string
The custom destination query and filter. Logs matching this query are forwarded to the destination.
type [_required_]
enum
The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`
default: `custom_destination`
#####  Create a Basic HTTP custom destination returns "OK" response
```
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

Copy
#####  Create a Custom Header HTTP custom destination returns "OK" response
```
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

Copy
#####  Create a Microsoft Sentinel custom destination returns "OK" response
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#CreateLogsCustomDestination-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#CreateLogsCustomDestination-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#CreateLogsCustomDestination-403-v2)
  * [409](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#CreateLogsCustomDestination-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#CreateLogsCustomDestination-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


The custom destination.
Field
Type
Description
data
object
The definition of a custom destination.
attributes
object
The attributes associated with the custom destination.
enabled
boolean
Whether logs matching this custom destination should be forwarded or not.
default: `true`
forward_tags
boolean
Whether tags from the forwarded logs should be forwarded or not.
default: `true`
forward_tags_restriction_list
[string]
List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be filtered.
An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter.
default: 
forward_tags_restriction_list_type
enum
How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.
`BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST`
default: `ALLOW_LIST`
forwarder_destination
<oneOf>
A custom destination's location to forward logs.
Option 1
object
The HTTP destination.
auth [_required_]
<oneOf>
Authentication method of the HTTP requests.
Option 1
object
Basic access authentication.
type [_required_]
enum
Type of the basic access authentication. Allowed enum values: `basic`
default: `basic`
Option 2
object
Custom header access authentication.
header_name [_required_]
string
The header name of the authentication.
type [_required_]
enum
Type of the custom header access authentication. Allowed enum values: `custom_header`
default: `custom_header`
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the HTTP destination. Allowed enum values: `http`
default: `http`
Option 2
object
The Splunk HTTP Event Collector (HEC) destination.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`
default: `splunk_hec`
Option 3
object
The Elasticsearch destination.
auth [_required_]
object
Basic access authentication.
<any-key>
Basic access authentication.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
index_name [_required_]
string
Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).
index_rotation
string
Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options:
  * Hourly: `yyyy-MM-dd-HH` (as an example, it would render: `2022-10-19-09`)
  * Daily: `yyyy-MM-dd` (as an example, it would render: `2022-10-19`)
  * Weekly: `yyyy-'W'ww` (as an example, it would render: `2022-W42`)
  * Monthly: `yyyy-MM` (as an example, it would render: `2022-10`)


If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).
type [_required_]
enum
Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`
default: `elasticsearch`
Option 4
object
The Microsoft Sentinel destination.
client_id [_required_]
string
Client ID from the Datadog Azure integration.
data_collection_endpoint [_required_]
string
Azure data collection endpoint.
data_collection_rule_id [_required_]
string
Azure data collection rule ID.
stream_name [_required_]
string
Azure stream name.
tenant_id [_required_]
string
Tenant ID from the Datadog Azure integration.
type [_required_]
enum
Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
name
string
The custom destination name.
query
string
The custom destination query filter. Logs matching this query are forwarded to the destination.
id
string
The custom destination ID.
type
enum
The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`
default: `custom_destination`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=typescript)


#####  Create a Basic HTTP custom destination returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations" \
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

                        
```

#####  Create a Custom Header HTTP custom destination returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations" \
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

                        
```

#####  Create a Microsoft Sentinel custom destination returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations" \
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

                        
```

#####  Create a Basic HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Custom Header HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Microsoft Sentinel custom destination returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a Basic HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Custom Header HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Microsoft Sentinel custom destination returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Create a Basic HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Custom Header HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Microsoft Sentinel custom destination returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a Basic HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Custom Header HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Microsoft Sentinel custom destination returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a Basic HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Custom Header HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Microsoft Sentinel custom destination returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Create a Basic HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Custom Header HTTP custom destination returns "OK" response 
```
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

Copy
#####  Create a Microsoft Sentinel custom destination returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get a custom destination](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#get-a-custom-destination)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#get-a-custom-destination-v2)


GET https://api.ap1.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.ap2.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.datadoghq.eu/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.ddog-gov.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.us3.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}
### Overview
Get a specific custom destination in your organization. This endpoint requires any of the following permissions:
* `logs_read_config`
* `logs_read_data`
  

### Arguments
#### Path Parameters
Name
Type
Description
custom_destination_id [_required_]
string
The ID of the custom destination.
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#GetLogsCustomDestination-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#GetLogsCustomDestination-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#GetLogsCustomDestination-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#GetLogsCustomDestination-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#GetLogsCustomDestination-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


The custom destination.
Field
Type
Description
data
object
The definition of a custom destination.
attributes
object
The attributes associated with the custom destination.
enabled
boolean
Whether logs matching this custom destination should be forwarded or not.
default: `true`
forward_tags
boolean
Whether tags from the forwarded logs should be forwarded or not.
default: `true`
forward_tags_restriction_list
[string]
List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be filtered.
An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter.
default: 
forward_tags_restriction_list_type
enum
How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.
`BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST`
default: `ALLOW_LIST`
forwarder_destination
<oneOf>
A custom destination's location to forward logs.
Option 1
object
The HTTP destination.
auth [_required_]
<oneOf>
Authentication method of the HTTP requests.
Option 1
object
Basic access authentication.
type [_required_]
enum
Type of the basic access authentication. Allowed enum values: `basic`
default: `basic`
Option 2
object
Custom header access authentication.
header_name [_required_]
string
The header name of the authentication.
type [_required_]
enum
Type of the custom header access authentication. Allowed enum values: `custom_header`
default: `custom_header`
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the HTTP destination. Allowed enum values: `http`
default: `http`
Option 2
object
The Splunk HTTP Event Collector (HEC) destination.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`
default: `splunk_hec`
Option 3
object
The Elasticsearch destination.
auth [_required_]
object
Basic access authentication.
<any-key>
Basic access authentication.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
index_name [_required_]
string
Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).
index_rotation
string
Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options:
  * Hourly: `yyyy-MM-dd-HH` (as an example, it would render: `2022-10-19-09`)
  * Daily: `yyyy-MM-dd` (as an example, it would render: `2022-10-19`)
  * Weekly: `yyyy-'W'ww` (as an example, it would render: `2022-W42`)
  * Monthly: `yyyy-MM` (as an example, it would render: `2022-10`)


If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).
type [_required_]
enum
Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`
default: `elasticsearch`
Option 4
object
The Microsoft Sentinel destination.
client_id [_required_]
string
Client ID from the Datadog Azure integration.
data_collection_endpoint [_required_]
string
Azure data collection endpoint.
data_collection_rule_id [_required_]
string
Azure data collection rule ID.
stream_name [_required_]
string
Azure stream name.
tenant_id [_required_]
string
Tenant ID from the Datadog Azure integration.
type [_required_]
enum
Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
name
string
The custom destination name.
query
string
The custom destination query filter. Logs matching this query are forwarded to the destination.
id
string
The custom destination ID.
type
enum
The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`
default: `custom_destination`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=typescript)


#####  Get a custom destination
Copy
```
                  # Path parameters  
export custom_destination_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/${custom_destination_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a custom destination
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a custom destination
```
# Get a custom destination returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsCustomDestinationsAPI.new

# there is a valid "custom_destination" in the system
CUSTOM_DESTINATION_DATA_ID = ENV["CUSTOM_DESTINATION_DATA_ID"]
p api_instance.get_logs_custom_destination(CUSTOM_DESTINATION_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a custom destination
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a custom destination
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get a custom destination
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get a custom destination
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update a custom destination](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#update-a-custom-destination)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#update-a-custom-destination-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.ap2.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.datadoghq.eu/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.ddog-gov.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.us3.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}
### Overview
Update the given fields of a specific custom destination in your organization. This endpoint requires the `logs_write_forwarding_rules` permission.
### Arguments
#### Path Parameters
Name
Type
Description
custom_destination_id [_required_]
string
The ID of the custom destination.
### Request
#### Body Data (required)
New definition of the custom destination’s fields.
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


Field
Type
Description
data
object
The definition of a custom destination.
attributes
object
The attributes associated with the custom destination.
enabled
boolean
Whether logs matching this custom destination should be forwarded or not.
default: `true`
forward_tags
boolean
Whether tags from the forwarded logs should be forwarded or not.
default: `true`
forward_tags_restriction_list
[string]
List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be restricted from being forwarded. An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter.
default: 
forward_tags_restriction_list_type
enum
How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.
`BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST`
default: `ALLOW_LIST`
forwarder_destination
<oneOf>
A custom destination's location to forward logs.
Option 1
object
The HTTP destination.
auth [_required_]
<oneOf>
Authentication method of the HTTP requests.
Option 1
object
Basic access authentication.
password [_required_]
string
The password of the authentication. This field is not returned by the API.
type [_required_]
enum
Type of the basic access authentication. Allowed enum values: `basic`
default: `basic`
username [_required_]
string
The username of the authentication. This field is not returned by the API.
Option 2
object
Custom header access authentication.
header_name [_required_]
string
The header name of the authentication.
header_value [_required_]
string
The header value of the authentication. This field is not returned by the API.
type [_required_]
enum
Type of the custom header access authentication. Allowed enum values: `custom_header`
default: `custom_header`
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the HTTP destination. Allowed enum values: `http`
default: `http`
Option 2
object
The Splunk HTTP Event Collector (HEC) destination.
access_token [_required_]
string
Access token of the Splunk HTTP Event Collector. This field is not returned by the API.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`
default: `splunk_hec`
Option 3
object
The Elasticsearch destination.
auth [_required_]
object
Basic access authentication.
password [_required_]
string
The password of the authentication. This field is not returned by the API.
username [_required_]
string
The username of the authentication. This field is not returned by the API.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
index_name [_required_]
string
Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).
index_rotation
string
Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options:
  * Hourly: `yyyy-MM-dd-HH` (as an example, it would render: `2022-10-19-09`)
  * Daily: `yyyy-MM-dd` (as an example, it would render: `2022-10-19`)
  * Weekly: `yyyy-'W'ww` (as an example, it would render: `2022-W42`)
  * Monthly: `yyyy-MM` (as an example, it would render: `2022-10`)


If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).
type [_required_]
enum
Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`
default: `elasticsearch`
Option 4
object
The Microsoft Sentinel destination.
client_id [_required_]
string
Client ID from the Datadog Azure integration.
data_collection_endpoint [_required_]
string
Azure data collection endpoint.
data_collection_rule_id [_required_]
string
Azure data collection rule ID.
stream_name [_required_]
string
Azure stream name.
tenant_id [_required_]
string
Tenant ID from the Datadog Azure integration.
type [_required_]
enum
Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
name
string
The custom destination name.
query
string
The custom destination query and filter. Logs matching this query are forwarded to the destination.
id [_required_]
string
The custom destination ID.
type [_required_]
enum
The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`
default: `custom_destination`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#UpdateLogsCustomDestination-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#UpdateLogsCustomDestination-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#UpdateLogsCustomDestination-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#UpdateLogsCustomDestination-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#UpdateLogsCustomDestination-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#UpdateLogsCustomDestination-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


The custom destination.
Field
Type
Description
data
object
The definition of a custom destination.
attributes
object
The attributes associated with the custom destination.
enabled
boolean
Whether logs matching this custom destination should be forwarded or not.
default: `true`
forward_tags
boolean
Whether tags from the forwarded logs should be forwarded or not.
default: `true`
forward_tags_restriction_list
[string]
List of [keys of tags](https://docs.datadoghq.com/getting_started/tagging/#define-tags) to be filtered.
An empty list represents no restriction is in place and either all or no tags will be forwarded depending on `forward_tags_restriction_list_type` parameter.
default: 
forward_tags_restriction_list_type
enum
How `forward_tags_restriction_list` parameter should be interpreted. If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list are forwarded.
`BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list. Allowed enum values: `ALLOW_LIST,BLOCK_LIST`
default: `ALLOW_LIST`
forwarder_destination
<oneOf>
A custom destination's location to forward logs.
Option 1
object
The HTTP destination.
auth [_required_]
<oneOf>
Authentication method of the HTTP requests.
Option 1
object
Basic access authentication.
type [_required_]
enum
Type of the basic access authentication. Allowed enum values: `basic`
default: `basic`
Option 2
object
Custom header access authentication.
header_name [_required_]
string
The header name of the authentication.
type [_required_]
enum
Type of the custom header access authentication. Allowed enum values: `custom_header`
default: `custom_header`
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the HTTP destination. Allowed enum values: `http`
default: `http`
Option 2
object
The Splunk HTTP Event Collector (HEC) destination.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
type [_required_]
enum
Type of the Splunk HTTP Event Collector (HEC) destination. Allowed enum values: `splunk_hec`
default: `splunk_hec`
Option 3
object
The Elasticsearch destination.
auth [_required_]
object
Basic access authentication.
<any-key>
Basic access authentication.
endpoint [_required_]
string
The destination for which logs will be forwarded to. Must have HTTPS scheme and forwarding back to Datadog is not allowed.
index_name [_required_]
string
Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).
index_rotation
string
Date pattern with US locale and UTC timezone to be appended to the index name after adding `-` (that is, `${index_name}-${indexPattern}`). You can customize the index rotation naming pattern by choosing one of these options:
  * Hourly: `yyyy-MM-dd-HH` (as an example, it would render: `2022-10-19-09`)
  * Daily: `yyyy-MM-dd` (as an example, it would render: `2022-10-19`)
  * Weekly: `yyyy-'W'ww` (as an example, it would render: `2022-W42`)
  * Monthly: `yyyy-MM` (as an example, it would render: `2022-10`)


If this field is missing or is blank, it means that the index name will always be the same (that is, no rotation).
type [_required_]
enum
Type of the Elasticsearch destination. Allowed enum values: `elasticsearch`
default: `elasticsearch`
Option 4
object
The Microsoft Sentinel destination.
client_id [_required_]
string
Client ID from the Datadog Azure integration.
data_collection_endpoint [_required_]
string
Azure data collection endpoint.
data_collection_rule_id [_required_]
string
Azure data collection rule ID.
stream_name [_required_]
string
Azure stream name.
tenant_id [_required_]
string
Tenant ID from the Datadog Azure integration.
type [_required_]
enum
Type of the Microsoft Sentinel destination. Allowed enum values: `microsoft_sentinel`
default: `microsoft_sentinel`
name
string
The custom destination name.
query
string
The custom destination query filter. Logs matching this query are forwarded to the destination.
id
string
The custom destination ID.
type
enum
The type of the resource. The value should always be `custom_destination`. Allowed enum values: `custom_destination`
default: `custom_destination`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=typescript)


#####  Update a custom destination returns "OK" response
Copy
```
                          # Path parameters  
export custom_destination_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/${custom_destination_id}" \
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

                        
```

#####  Update a custom destination returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a custom destination returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update a custom destination returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a custom destination returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a custom destination returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update a custom destination returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete a custom destination](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#delete-a-custom-destination)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#delete-a-custom-destination-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.ap2.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.datadoghq.eu/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.ddog-gov.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.us3.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/{custom_destination_id}
### Overview
Delete a specific custom destination in your organization. This endpoint requires the `logs_write_forwarding_rules` permission.
### Arguments
#### Path Parameters
Name
Type
Description
custom_destination_id [_required_]
string
The ID of the custom destination.
### Response
  * [204](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#DeleteLogsCustomDestination-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#DeleteLogsCustomDestination-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#DeleteLogsCustomDestination-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#DeleteLogsCustomDestination-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/logs-custom-destinations/#DeleteLogsCustomDestination-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Model](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)
  * [Example](https://docs.datadoghq.com/api/latest/logs-custom-destinations/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/logs-custom-destinations/?code-lang=typescript)


#####  Delete a custom destination
Copy
```
                  # Path parameters  
export custom_destination_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/custom-destinations/${custom_destination_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a custom destination
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a custom destination
```
# Delete a custom destination returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::LogsCustomDestinationsAPI.new

# there is a valid "custom_destination" in the system
CUSTOM_DESTINATION_DATA_ID = ENV["CUSTOM_DESTINATION_DATA_ID"]
api_instance.delete_logs_custom_destination(CUSTOM_DESTINATION_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a custom destination
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete a custom destination
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete a custom destination
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete a custom destination
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4cf33b55-1e5e-45d2-ab93-0fe3a591a204&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=fe3226e5-c39d-423e-ab6f-5ba618931cc0&pt=Logs%20Custom%20Destinations&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-custom-destinations%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4cf33b55-1e5e-45d2-ab93-0fe3a591a204&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=fe3226e5-c39d-423e-ab6f-5ba618931cc0&pt=Logs%20Custom%20Destinations&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-custom-destinations%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=b55e9adc-0ddd-4329-b202-fab38f39f2fa&bo=2&sid=c4ba0d50f0bf11f09afde9c0412ba014&vid=c4ba67e0f0bf11f099fcdb9b6c7a6b3e&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Logs%20Custom%20Destinations&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Flogs-custom-destinations%2F&r=&lt=1662&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=849368)
