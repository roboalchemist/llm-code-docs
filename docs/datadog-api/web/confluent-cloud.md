# Source: https://docs.datadoghq.com/api/latest/confluent-cloud/

# Confluent Cloud
Manage your Datadog Confluent Cloud integration accounts and account resources directly through the Datadog API. See the [Confluent Cloud page](https://docs.datadoghq.com/integrations/confluent_cloud/) for more information.
## [Update resource in Confluent account](https://docs.datadoghq.com/api/latest/confluent-cloud/#update-resource-in-confluent-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/confluent-cloud/#update-resource-in-confluent-account-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}
### Overview
Update a Confluent resource with the provided resource id for the account associated with the provided account ID. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Confluent Account ID.
resource_id [_required_]
string
Confluent Account Resource ID.
### Request
#### Body Data (required)
Confluent payload
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


Field
Type
Description
data [_required_]
object
JSON:API request for updating a Confluent resource.
attributes [_required_]
object
Attributes object for updating a Confluent resource.
enable_custom_metrics
boolean
Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.
resource_type [_required_]
string
The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
id [_required_]
string
The ID associated with a Confluent resource.
type [_required_]
enum
The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`
default: `confluent-cloud-resources`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/confluent-cloud/#UpdateConfluentResource-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/confluent-cloud/#UpdateConfluentResource-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/confluent-cloud/#UpdateConfluentResource-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/confluent-cloud/#UpdateConfluentResource-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/confluent-cloud/#UpdateConfluentResource-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


Response schema when interacting with a Confluent resource.
Field
Type
Description
data
object
Confluent Cloud resource data.
attributes [_required_]
object
Model representation of a Confluent Cloud resource.
enable_custom_metrics
boolean
Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.
id
string
The ID associated with the Confluent resource.
resource_type [_required_]
string
The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
id [_required_]
string
The ID associated with the Confluent resource.
type [_required_]
enum
The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`
default: `confluent-cloud-resources`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=typescript)


#####  Update resource in Confluent account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
export resource_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}/resources/${resource_id}" \
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

                
```

#####  Update resource in Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update resource in Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update resource in Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update resource in Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update resource in Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update resource in Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get resource from Confluent account](https://docs.datadoghq.com/api/latest/confluent-cloud/#get-resource-from-confluent-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/confluent-cloud/#get-resource-from-confluent-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}
### Overview
Get a Confluent resource with the provided resource id for the account associated with the provided account ID. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Confluent Account ID.
resource_id [_required_]
string
Confluent Account Resource ID.
### Response
  * [200](https://docs.datadoghq.com/api/latest/confluent-cloud/#GetConfluentResource-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/confluent-cloud/#GetConfluentResource-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/confluent-cloud/#GetConfluentResource-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/confluent-cloud/#GetConfluentResource-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/confluent-cloud/#GetConfluentResource-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


Response schema when interacting with a Confluent resource.
Field
Type
Description
data
object
Confluent Cloud resource data.
attributes [_required_]
object
Model representation of a Confluent Cloud resource.
enable_custom_metrics
boolean
Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.
id
string
The ID associated with the Confluent resource.
resource_type [_required_]
string
The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
id [_required_]
string
The ID associated with the Confluent resource.
type [_required_]
enum
The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`
default: `confluent-cloud-resources`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=typescript)


#####  Get resource from Confluent account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
export resource_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}/resources/${resource_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get resource from Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get resource from Confluent account
```
# Get resource from Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new
p api_instance.get_confluent_resource("account_id", "resource_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get resource from Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get resource from Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get resource from Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get resource from Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete resource from Confluent account](https://docs.datadoghq.com/api/latest/confluent-cloud/#delete-resource-from-confluent-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/confluent-cloud/#delete-resource-from-confluent-account-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources/{resource_id}
### Overview
Delete a Confluent resource with the provided resource id for the account associated with the provided account ID. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Confluent Account ID.
resource_id [_required_]
string
Confluent Account Resource ID.
### Response
  * [204](https://docs.datadoghq.com/api/latest/confluent-cloud/#DeleteConfluentResource-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/confluent-cloud/#DeleteConfluentResource-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/confluent-cloud/#DeleteConfluentResource-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/confluent-cloud/#DeleteConfluentResource-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/confluent-cloud/#DeleteConfluentResource-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=typescript)


#####  Delete resource from Confluent account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
export resource_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}/resources/${resource_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete resource from Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete resource from Confluent account
```
# Delete resource from Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new
api_instance.delete_confluent_resource("account_id", "resource_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete resource from Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete resource from Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete resource from Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete resource from Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Add resource to Confluent account](https://docs.datadoghq.com/api/latest/confluent-cloud/#add-resource-to-confluent-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/confluent-cloud/#add-resource-to-confluent-account-v2)


POST https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources
### Overview
Create a Confluent resource for the account associated with the provided ID. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Confluent Account ID.
### Request
#### Body Data (required)
Confluent payload
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


Field
Type
Description
data [_required_]
object
JSON:API request for updating a Confluent resource.
attributes [_required_]
object
Attributes object for updating a Confluent resource.
enable_custom_metrics
boolean
Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.
resource_type [_required_]
string
The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
id [_required_]
string
The ID associated with a Confluent resource.
type [_required_]
enum
The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`
default: `confluent-cloud-resources`
```
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

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/confluent-cloud/#CreateConfluentResource-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/confluent-cloud/#CreateConfluentResource-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/confluent-cloud/#CreateConfluentResource-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/confluent-cloud/#CreateConfluentResource-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/confluent-cloud/#CreateConfluentResource-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


Response schema when interacting with a Confluent resource.
Field
Type
Description
data
object
Confluent Cloud resource data.
attributes [_required_]
object
Model representation of a Confluent Cloud resource.
enable_custom_metrics
boolean
Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.
id
string
The ID associated with the Confluent resource.
resource_type [_required_]
string
The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
id [_required_]
string
The ID associated with the Confluent resource.
type [_required_]
enum
The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`
default: `confluent-cloud-resources`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=typescript)


#####  Add resource to Confluent account returns "OK" response
Copy
```
                          # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}/resources" \
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

                        
```

#####  Add resource to Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Add resource to Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Add resource to Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Add resource to Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Add resource to Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Add resource to Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [List Confluent Account resources](https://docs.datadoghq.com/api/latest/confluent-cloud/#list-confluent-account-resources)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/confluent-cloud/#list-confluent-account-resources-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resourceshttps://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}/resources
### Overview
Get a Confluent resource for the account associated with the provided ID. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Confluent Account ID.
### Response
  * [200](https://docs.datadoghq.com/api/latest/confluent-cloud/#ListConfluentResource-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/confluent-cloud/#ListConfluentResource-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/confluent-cloud/#ListConfluentResource-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/confluent-cloud/#ListConfluentResource-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/confluent-cloud/#ListConfluentResource-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


Response schema when interacting with a list of Confluent resources.
Field
Type
Description
data
[object]
The JSON:API data attribute.
attributes [_required_]
object
Model representation of a Confluent Cloud resource.
enable_custom_metrics
boolean
Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.
id
string
The ID associated with the Confluent resource.
resource_type [_required_]
string
The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
id [_required_]
string
The ID associated with the Confluent resource.
type [_required_]
enum
The JSON:API type for this request. Allowed enum values: `confluent-cloud-resources`
default: `confluent-cloud-resources`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=typescript)


#####  List Confluent Account resources
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}/resources" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List Confluent Account resources
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List Confluent Account resources
```
# List Confluent Account resources returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new
p api_instance.list_confluent_resource("account_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List Confluent Account resources
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List Confluent Account resources
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  List Confluent Account resources
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  List Confluent Account resources
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update Confluent account](https://docs.datadoghq.com/api/latest/confluent-cloud/#update-confluent-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/confluent-cloud/#update-confluent-account-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}
### Overview
Update the Confluent account with the provided account ID. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Confluent Account ID.
### Request
#### Body Data (required)
Confluent payload
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


Field
Type
Description
data [_required_]
object
Data object for updating a Confluent account.
attributes [_required_]
object
Attributes object for updating a Confluent account.
api_key [_required_]
string
The API key associated with your Confluent account.
api_secret [_required_]
string
The API secret associated with your Confluent account.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
type [_required_]
enum
The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts`
default: `confluent-cloud-accounts`
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/confluent-cloud/#UpdateConfluentAccount-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/confluent-cloud/#UpdateConfluentAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/confluent-cloud/#UpdateConfluentAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/confluent-cloud/#UpdateConfluentAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/confluent-cloud/#UpdateConfluentAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


The expected response schema when getting a Confluent account.
Field
Type
Description
data
object
An API key and API secret pair that represents a Confluent account.
attributes [_required_]
object
The attributes of a Confluent account.
api_key [_required_]
string
The API key associated with your Confluent account.
resources
[object]
A list of Confluent resources associated with the Confluent account.
enable_custom_metrics
boolean
Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.
id
string
The ID associated with the Confluent resource.
resource_type [_required_]
string
The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
id [_required_]
string
A randomly generated ID associated with a Confluent account.
type [_required_]
enum
The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts`
default: `confluent-cloud-accounts`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=typescript)


#####  Update Confluent account returns "OK" response
Copy
```
                          # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}" \
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

                        
```

#####  Update Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update Confluent account returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get Confluent account](https://docs.datadoghq.com/api/latest/confluent-cloud/#get-confluent-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/confluent-cloud/#get-confluent-account-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}
### Overview
Get the Confluent account with the provided account ID. This endpoint requires the `integrations_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Confluent Account ID.
### Response
  * [200](https://docs.datadoghq.com/api/latest/confluent-cloud/#GetConfluentAccount-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/confluent-cloud/#GetConfluentAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/confluent-cloud/#GetConfluentAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/confluent-cloud/#GetConfluentAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/confluent-cloud/#GetConfluentAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


The expected response schema when getting a Confluent account.
Field
Type
Description
data
object
An API key and API secret pair that represents a Confluent account.
attributes [_required_]
object
The attributes of a Confluent account.
api_key [_required_]
string
The API key associated with your Confluent account.
resources
[object]
A list of Confluent resources associated with the Confluent account.
enable_custom_metrics
boolean
Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.
id
string
The ID associated with the Confluent resource.
resource_type [_required_]
string
The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
id [_required_]
string
A randomly generated ID associated with a Confluent account.
type [_required_]
enum
The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts`
default: `confluent-cloud-accounts`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=typescript)


#####  Get Confluent account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get Confluent account
```
# Get Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ID = ENV["CONFLUENT_ACCOUNT_DATA_ID"]
p api_instance.get_confluent_account(CONFLUENT_ACCOUNT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete Confluent account](https://docs.datadoghq.com/api/latest/confluent-cloud/#delete-confluent-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/confluent-cloud/#delete-confluent-account-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/{account_id}
### Overview
Delete a Confluent account with the provided account ID. This endpoint requires the `manage_integrations` permission.
### Arguments
#### Path Parameters
Name
Type
Description
account_id [_required_]
string
Confluent Account ID.
### Response
  * [204](https://docs.datadoghq.com/api/latest/confluent-cloud/#DeleteConfluentAccount-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/confluent-cloud/#DeleteConfluentAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/confluent-cloud/#DeleteConfluentAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/confluent-cloud/#DeleteConfluentAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/confluent-cloud/#DeleteConfluentAccount-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=typescript)


#####  Delete Confluent account
Copy
```
                  # Path parameters  
export account_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete Confluent account
```
# Delete Confluent account returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ID = ENV["CONFLUENT_ACCOUNT_DATA_ID"]
api_instance.delete_confluent_account(CONFLUENT_ACCOUNT_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Add Confluent account](https://docs.datadoghq.com/api/latest/confluent-cloud/#add-confluent-account)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/confluent-cloud/#add-confluent-account-v2)


POST https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accountshttps://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accountshttps://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accountshttps://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accountshttps://api.datadoghq.com/api/v2/integrations/confluent-cloud/accountshttps://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accountshttps://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts
### Overview
Create a Confluent account. This endpoint requires the `manage_integrations` permission.
### Request
#### Body Data (required)
Confluent payload
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


Field
Type
Description
data [_required_]
object
The data body for adding a Confluent account.
attributes [_required_]
object
Attributes associated with the account creation request.
api_key [_required_]
string
The API key associated with your Confluent account.
api_secret [_required_]
string
The API secret associated with your Confluent account.
resources
[object]
A list of Confluent resources associated with the Confluent account.
enable_custom_metrics
boolean
Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.
id
string
The ID associated with a Confluent resource.
resource_type [_required_]
string
The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
type [_required_]
enum
The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts`
default: `confluent-cloud-accounts`
```
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

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/confluent-cloud/#CreateConfluentAccount-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/confluent-cloud/#CreateConfluentAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/confluent-cloud/#CreateConfluentAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/confluent-cloud/#CreateConfluentAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/confluent-cloud/#CreateConfluentAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


The expected response schema when getting a Confluent account.
Field
Type
Description
data
object
An API key and API secret pair that represents a Confluent account.
attributes [_required_]
object
The attributes of a Confluent account.
api_key [_required_]
string
The API key associated with your Confluent account.
resources
[object]
A list of Confluent resources associated with the Confluent account.
enable_custom_metrics
boolean
Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.
id
string
The ID associated with the Confluent resource.
resource_type [_required_]
string
The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
id [_required_]
string
A randomly generated ID associated with a Confluent account.
type [_required_]
enum
The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts`
default: `confluent-cloud-accounts`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=typescript)


#####  Add Confluent account
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts" \
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

                
```

#####  Add Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Add Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Add Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Add Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Add Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Add Confluent account
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [List Confluent accounts](https://docs.datadoghq.com/api/latest/confluent-cloud/#list-confluent-accounts)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/confluent-cloud/#list-confluent-accounts-v2)


GET https://api.ap1.datadoghq.com/api/v2/integrations/confluent-cloud/accountshttps://api.ap2.datadoghq.com/api/v2/integrations/confluent-cloud/accountshttps://api.datadoghq.eu/api/v2/integrations/confluent-cloud/accountshttps://api.ddog-gov.com/api/v2/integrations/confluent-cloud/accountshttps://api.datadoghq.com/api/v2/integrations/confluent-cloud/accountshttps://api.us3.datadoghq.com/api/v2/integrations/confluent-cloud/accountshttps://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts
### Overview
List Confluent accounts. This endpoint requires the `integrations_read` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/confluent-cloud/#ListConfluentAccount-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/confluent-cloud/#ListConfluentAccount-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/confluent-cloud/#ListConfluentAccount-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/confluent-cloud/#ListConfluentAccount-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/confluent-cloud/#ListConfluentAccount-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


Confluent account returned by the API.
Field
Type
Description
data
[object]
The Confluent account.
attributes [_required_]
object
The attributes of a Confluent account.
api_key [_required_]
string
The API key associated with your Confluent account.
resources
[object]
A list of Confluent resources associated with the Confluent account.
enable_custom_metrics
boolean
Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags.
id
string
The ID associated with the Confluent resource.
resource_type [_required_]
string
The resource type of the Resource. Can be `kafka`, `connector`, `ksql`, or `schema_registry`.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
tags
[string]
A list of strings representing tags. Can be a single key, or key-value pairs separated by a colon.
id [_required_]
string
A randomly generated ID associated with a Confluent account.
type [_required_]
enum
The JSON:API type for this API. Should always be `confluent-cloud-accounts`. Allowed enum values: `confluent-cloud-accounts`
default: `confluent-cloud-accounts`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Model](https://docs.datadoghq.com/api/latest/confluent-cloud/)
  * [Example](https://docs.datadoghq.com/api/latest/confluent-cloud/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/confluent-cloud/?code-lang=typescript)


#####  List Confluent accounts
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations/confluent-cloud/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List Confluent accounts
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List Confluent accounts
```
# List Confluent accounts returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ConfluentCloudAPI.new
p api_instance.list_confluent_account()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List Confluent accounts
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List Confluent accounts
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  List Confluent accounts
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  List Confluent accounts
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=1af7079c-9ae9-4d8e-b494-246c54444394&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=483bf997-a98a-4eb7-bcce-ea8b350336bd&pt=Confluent%20Cloud&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fconfluent-cloud%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=1af7079c-9ae9-4d8e-b494-246c54444394&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=483bf997-a98a-4eb7-bcce-ea8b350336bd&pt=Confluent%20Cloud&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fconfluent-cloud%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=542c90e2-c027-4501-a031-f799da1fc534&bo=2&sid=429bc5c0f0bf11f0a4206f1647a1e4e9&vid=429c17d0f0bf11f0be3e793ded46c7de&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Confluent%20Cloud&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fconfluent-cloud%2F&r=&lt=2217&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=389470)
