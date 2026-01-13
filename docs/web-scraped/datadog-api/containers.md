# Source: https://docs.datadoghq.com/api/latest/containers/

# Containers
The Containers API allows you to query container data for your organization. See the [Container Monitoring page](https://docs.datadoghq.com/containers/) for more information.
## [Get All Containers](https://docs.datadoghq.com/api/latest/containers/#get-all-containers)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/containers/#get-all-containers-v2)


GET https://api.ap1.datadoghq.com/api/v2/containershttps://api.ap2.datadoghq.com/api/v2/containershttps://api.datadoghq.eu/api/v2/containershttps://api.ddog-gov.com/api/v2/containershttps://api.datadoghq.com/api/v2/containershttps://api.us3.datadoghq.com/api/v2/containershttps://api.us5.datadoghq.com/api/v2/containers
### Overview
Get all containers for your organization.
### Arguments
#### Query Strings
Name
Type
Description
filter[tags]
string
Comma-separated list of tags to filter containers by.
group_by
string
Comma-separated list of tags to group containers by.
sort
string
Attribute to sort containers by.
page[size]
integer
Maximum number of results returned.
page[cursor]
string
String to query the next page of results. This key is provided with each valid response from the API in `meta.pagination.next_cursor`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/containers/#ListContainers-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/containers/#ListContainers-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/containers/#ListContainers-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/containers/#ListContainers-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/containers/)
  * [Example](https://docs.datadoghq.com/api/latest/containers/)


List of containers.
Field
Type
Description
data
[ <oneOf>]
Array of Container objects.
Option 1
object
Container object.
attributes
object
Attributes for a container.
container_id
string
The ID of the container.
created_at
string
Time the container was created.
host
string
Hostname of the host running the container.
image_digest
string
Digest of the compressed image manifest.
image_name
string
Name of the associated container image.
image_tags
[string]
List of image tags associated with the container image.
name
string
Name of the container.
started_at
string
Time the container was started.
state
string
State of the container. This depends on the container runtime.
tags
[string]
List of tags associated with the container.
id
string
Container ID.
type
enum
Type of container. Allowed enum values: `container`
default: `container`
Option 2
object
Container group object.
attributes
object
Attributes for a container group.
count
int64
Number of containers in the group.
tags
object
Tags from the group name parsed in key/value format.
id
string
Container Group ID.
relationships
object
Relationships to containers inside a container group.
containers
object
Relationships to Containers inside a Container Group.
data
[string]
Links data.
links
object
Links attributes.
related
string
Link to related containers.
type
enum
Type of container group. Allowed enum values: `container_group`
default: `container_group`
links
object
Pagination links.
first
string
Link to the first page.
last
string
Link to the last page.
next
string
Link to the next page.
prev
string
Link to previous page.
self
string
Link to current page.
meta
object
Response metadata object.
pagination
object
Paging attributes.
cursor
string
The cursor used to get the current results, if any.
limit
int32
Number of results returned
next_cursor
string
The cursor used to get the next results, if any.
prev_cursor
string
The cursor used to get the previous results, if any.
total
int64
Total number of records that match the query.
type
enum
Type of Container pagination. Allowed enum values: `cursor_limit`
default: `cursor_limit`
```
{
  "data": [
    {
      "attributes": {
        "container_id": "string",
        "created_at": "string",
        "host": "string",
        "image_digest": "string",
        "image_name": "string",
        "image_tags": [],
        "name": "string",
        "started_at": "string",
        "state": "string",
        "tags": []
      },
      "id": "string",
      "type": "container"
    }
  ],
  "links": {
    "first": "string",
    "last": "string",
    "next": "string",
    "prev": "string",
    "self": "string"
  },
  "meta": {
    "pagination": {
      "cursor": "string",
      "limit": "integer",
      "next_cursor": "string",
      "prev_cursor": "string",
      "total": "integer",
      "type": "cursor_limit"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/containers/)
  * [Example](https://docs.datadoghq.com/api/latest/containers/)


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
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/containers/)
  * [Example](https://docs.datadoghq.com/api/latest/containers/)


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
  * [Model](https://docs.datadoghq.com/api/latest/containers/)
  * [Example](https://docs.datadoghq.com/api/latest/containers/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/containers/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/containers/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/containers/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/containers/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/containers/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/containers/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/containers/?code-lang=typescript)


#####  Get All Containers
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/containers" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get All Containers
```
"""
Get All Containers returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.containers_api import ContainersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ContainersApi(api_client)
    response = api_instance.list_containers()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get All Containers
```
# Get All Containers returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ContainersAPI.new
p api_instance.list_containers()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get All Containers
```
// Get All Containers returns "OK" response

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
	api := datadogV2.NewContainersApi(apiClient)
	resp, r, err := api.ListContainers(ctx, *datadogV2.NewListContainersOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ContainersApi.ListContainers`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ContainersApi.ListContainers`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get All Containers
```
// Get All Containers returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ContainersApi;
import com.datadog.api.client.v2.model.ContainersResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ContainersApi apiInstance = new ContainersApi(defaultClient);

    try {
      ContainersResponse result = apiInstance.listContainers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainersApi#listContainers");
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

#####  Get All Containers
```
// Get All Containers returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_containers::ContainersAPI;
use datadog_api_client::datadogV2::api_containers::ListContainersOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ContainersAPI::with_config(configuration);
    let resp = api
        .list_containers(ListContainersOptionalParams::default())
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

#####  Get All Containers
```
/**
 * Get All Containers returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ContainersApi(configuration);

apiInstance
  .listContainers()
  .then((data: v2.ContainersResponse) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=0a5a37f5-7d35-48f6-a252-6eda0299449d&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=46782de7-6a6d-40c5-bfe1-92ac81b87c87&pt=Containers&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcontainers%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=0a5a37f5-7d35-48f6-a252-6eda0299449d&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=46782de7-6a6d-40c5-bfe1-92ac81b87c87&pt=Containers&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcontainers%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=83e2f6e0-e40d-41ff-930c-d4d651fb31b9&bo=2&sid=4bf34e80f0bf11f09e1d5327e47010f6&vid=4bf3d8e0f0bf11f0a7cfe9f253ca5829&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Containers&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcontainers%2F&r=&lt=904&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=146370)
