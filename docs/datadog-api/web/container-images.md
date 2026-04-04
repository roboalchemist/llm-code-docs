# Source: https://docs.datadoghq.com/api/latest/container-images/

# Container Images
The Container Images API allows you to query Container Image data for your organization. See the [Container Images View page](https://docs.datadoghq.com/infrastructure/containers/container_images/) for more information.
## [Get all Container Images](https://docs.datadoghq.com/api/latest/container-images/#get-all-container-images)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/container-images/#get-all-container-images-v2)


GET https://api.ap1.datadoghq.com/api/v2/container_imageshttps://api.ap2.datadoghq.com/api/v2/container_imageshttps://api.datadoghq.eu/api/v2/container_imageshttps://api.ddog-gov.com/api/v2/container_imageshttps://api.datadoghq.com/api/v2/container_imageshttps://api.us3.datadoghq.com/api/v2/container_imageshttps://api.us5.datadoghq.com/api/v2/container_images
### Overview
Get all Container Images for your organization. **Note** : To enrich the data returned by this endpoint with security scans, see the new [api/v2/security/scanned-assets-metadata](https://docs.datadoghq.com/api/latest/security-monitoring/#list-scanned-assets-metadata) endpoint.
### Arguments
#### Query Strings
Name
Type
Description
filter[tags]
string
Comma-separated list of tags to filter Container Images by.
group_by
string
Comma-separated list of tags to group Container Images by.
sort
string
Attribute to sort Container Images by.
page[size]
integer
Maximum number of results returned.
page[cursor]
string
String to query the next page of results. This key is provided with each valid response from the API in `meta.pagination.next_cursor`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/container-images/#ListContainerImages-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/container-images/#ListContainerImages-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/container-images/#ListContainerImages-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/container-images/#ListContainerImages-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/container-images/)
  * [Example](https://docs.datadoghq.com/api/latest/container-images/)


List of Container Images.
Field
Type
Description
data
[ <oneOf>]
Array of Container Image objects.
Option 1
object
Container Image object.
attributes
object
Attributes for a Container Image.
container_count
int64
Number of containers running the image.
image_flavors
[object]
List of platform-specific images associated with the image record. The list contains more than 1 entry for multi-architecture images.
built_at
string
Time the platform-specific Container Image was built.
os_architecture
string
Operating System architecture supported by the Container Image.
os_name
string
Operating System name supported by the Container Image.
os_version
string
Operating System version supported by the Container Image.
size
int64
Size of the platform-specific Container Image.
image_tags
[string]
List of image tags associated with the Container Image.
images_built_at
[string]
List of build times associated with the Container Image. The list contains more than 1 entry for multi-architecture images.
name
string
Name of the Container Image.
os_architectures
[string]
List of Operating System architectures supported by the Container Image.
os_names
[string]
List of Operating System names supported by the Container Image.
os_versions
[string]
List of Operating System versions supported by the Container Image.
published_at
string
Time the image was pushed to the container registry.
registry
string
Registry the Container Image was pushed to.
repo_digest
string
Digest of the compressed image manifest.
repository
string
Repository where the Container Image is stored in.
short_image
string
Short version of the Container Image name.
sizes
[integer]
List of size for each platform-specific image associated with the image record. The list contains more than 1 entry for multi-architecture images.
sources
[string]
List of sources where the Container Image was collected from.
tags
[string]
List of tags associated with the Container Image.
vulnerability_count
object
Vulnerability counts associated with the Container Image.
asset_id
string
ID of the Container Image.
critical
int64
Number of vulnerabilities with CVSS Critical severity.
high
int64
Number of vulnerabilities with CVSS High severity.
low
int64
Number of vulnerabilities with CVSS Low severity.
medium
int64
Number of vulnerabilities with CVSS Medium severity.
none
int64
Number of vulnerabilities with CVSS None severity.
unknown
int64
Number of vulnerabilities with an unknown CVSS severity.
id
string
Container Image ID.
type
enum
Type of Container Image. Allowed enum values: `container_image`
default: `container_image`
Option 2
object
Container Image Group object.
attributes
object
Attributes for a Container Image Group.
count
int64
Number of Container Images in the group.
name
string
Name of the Container Image group.
tags
object
Tags from the group name parsed in key/value format.
id
string
Container Image Group ID.
relationships
object
Relationships inside a Container Image Group.
container_images
object
Relationships to Container Images inside a Container Image Group.
data
[string]
Links data.
links
object
Links attributes.
related
string
Link to related Container Images.
type
enum
Type of Container Image Group. Allowed enum values: `container_image_group`
default: `container_image_group`
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
Type of Container Image pagination. Allowed enum values: `cursor_limit`
default: `cursor_limit`
```
{
  "data": [
    {
      "attributes": {
        "container_count": "integer",
        "image_flavors": [
          {
            "built_at": "string",
            "os_architecture": "string",
            "os_name": "string",
            "os_version": "string",
            "size": "integer"
          }
        ],
        "image_tags": [],
        "images_built_at": [],
        "name": "string",
        "os_architectures": [
          "amd64"
        ],
        "os_names": [
          "linux"
        ],
        "os_versions": [],
        "published_at": "string",
        "registry": "string",
        "repo_digest": "string",
        "repository": "string",
        "short_image": "string",
        "sizes": [],
        "sources": [],
        "tags": [],
        "vulnerability_count": {
          "asset_id": "string",
          "critical": "integer",
          "high": "integer",
          "low": "integer",
          "medium": "integer",
          "none": "integer",
          "unknown": "integer"
        }
      },
      "id": "string",
      "type": "container_image"
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
  * [Model](https://docs.datadoghq.com/api/latest/container-images/)
  * [Example](https://docs.datadoghq.com/api/latest/container-images/)


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
  * [Model](https://docs.datadoghq.com/api/latest/container-images/)
  * [Example](https://docs.datadoghq.com/api/latest/container-images/)


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
  * [Model](https://docs.datadoghq.com/api/latest/container-images/)
  * [Example](https://docs.datadoghq.com/api/latest/container-images/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/container-images/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/container-images/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/container-images/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/container-images/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/container-images/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/container-images/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/container-images/?code-lang=typescript)


#####  Get all Container Images
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/container_images" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all Container Images
```
"""
Get all Container Images returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.container_images_api import ContainerImagesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ContainerImagesApi(api_client)
    response = api_instance.list_container_images()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all Container Images
```
# Get all Container Images returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ContainerImagesAPI.new
p api_instance.list_container_images()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all Container Images
```
// Get all Container Images returns "OK" response

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
	api := datadogV2.NewContainerImagesApi(apiClient)
	resp, r, err := api.ListContainerImages(ctx, *datadogV2.NewListContainerImagesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ContainerImagesApi.ListContainerImages`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ContainerImagesApi.ListContainerImages`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all Container Images
```
// Get all Container Images returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ContainerImagesApi;
import com.datadog.api.client.v2.model.ContainerImagesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ContainerImagesApi apiInstance = new ContainerImagesApi(defaultClient);

    try {
      ContainerImagesResponse result = apiInstance.listContainerImages();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerImagesApi#listContainerImages");
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

#####  Get all Container Images
```
// Get all Container Images returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_container_images::ContainerImagesAPI;
use datadog_api_client::datadogV2::api_container_images::ListContainerImagesOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ContainerImagesAPI::with_config(configuration);
    let resp = api
        .list_container_images(ListContainerImagesOptionalParams::default())
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

#####  Get all Container Images
```
/**
 * Get all Container Images returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ContainerImagesApi(configuration);

apiInstance
  .listContainerImages()
  .then((data: v2.ContainerImagesResponse) => {
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
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=96a38cb7-6e81-4580-9977-e726897ba85a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=37fb4afe-2b31-4028-a90a-5c5e0326b028&pt=Container%20Images&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcontainer-images%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=96a38cb7-6e81-4580-9977-e726897ba85a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=37fb4afe-2b31-4028-a90a-5c5e0326b028&pt=Container%20Images&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcontainer-images%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=f5f9cbbe-8954-483b-b84d-7e34900f8142&bo=2&sid=48345350f0bf11f0bc2fb78c0d5ba948&vid=48355510f0bf11f08ea5d5d0a8745430&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Container%20Images&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fcontainer-images%2F&r=&lt=1321&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=938675)
