# Source: https://docs.datadoghq.com/api/latest/container-images.md

---
title: Container Images
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Container Images
---

# Container Images

The Container Images API allows you to query Container Image data for your organization. See the [Container Images View page](https://docs.datadoghq.com/infrastructure/containers/container_images/) for more information.

## Get all Container Images{% #get-all-container-images %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/container_images |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/container_images |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/container_images      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/container_images      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/container_images     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/container_images |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/container_images |

### Overview

Get all Container Images for your organization. **Note**: To enrich the data returned by this endpoint with security scans, see the new [api/v2/security/scanned-assets-metadata](https://docs.datadoghq.com/api/latest/security-monitoring/#list-scanned-assets-metadata) endpoint.

### Arguments

#### Query Strings

| Name         | Type    | Description                                                                                                                            |
| ------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| filter[tags] | string  | Comma-separated list of tags to filter Container Images by.                                                                            |
| group_by     | string  | Comma-separated list of tags to group Container Images by.                                                                             |
| sort         | string  | Attribute to sort Container Images by.                                                                                                 |
| page[size]   | integer | Maximum number of results returned.                                                                                                    |
| page[cursor] | string  | String to query the next page of results. This key is provided with each valid response from the API in `meta.pagination.next_cursor`. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of Container Images.

| Parent field        | Field               | Type            | Description                                                                                                                                        |
| ------------------- | ------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|                     | data                | [ <oneOf>] | Array of Container Image objects.                                                                                                                  |
| data                | Option 1            | object          | Container Image object.                                                                                                                            |
| Option 1            | attributes          | object          | Attributes for a Container Image.                                                                                                                  |
| attributes          | container_count     | int64           | Number of containers running the image.                                                                                                            |
| attributes          | image_flavors       | [object]        | List of platform-specific images associated with the image record. The list contains more than 1 entry for multi-architecture images.              |
| image_flavors       | built_at            | string          | Time the platform-specific Container Image was built.                                                                                              |
| image_flavors       | os_architecture     | string          | Operating System architecture supported by the Container Image.                                                                                    |
| image_flavors       | os_name             | string          | Operating System name supported by the Container Image.                                                                                            |
| image_flavors       | os_version          | string          | Operating System version supported by the Container Image.                                                                                         |
| image_flavors       | size                | int64           | Size of the platform-specific Container Image.                                                                                                     |
| attributes          | image_tags          | [string]        | List of image tags associated with the Container Image.                                                                                            |
| attributes          | images_built_at     | [string]        | List of build times associated with the Container Image. The list contains more than 1 entry for multi-architecture images.                        |
| attributes          | name                | string          | Name of the Container Image.                                                                                                                       |
| attributes          | os_architectures    | [string]        | List of Operating System architectures supported by the Container Image.                                                                           |
| attributes          | os_names            | [string]        | List of Operating System names supported by the Container Image.                                                                                   |
| attributes          | os_versions         | [string]        | List of Operating System versions supported by the Container Image.                                                                                |
| attributes          | published_at        | string          | Time the image was pushed to the container registry.                                                                                               |
| attributes          | registry            | string          | Registry the Container Image was pushed to.                                                                                                        |
| attributes          | repo_digest         | string          | Digest of the compressed image manifest.                                                                                                           |
| attributes          | repository          | string          | Repository where the Container Image is stored in.                                                                                                 |
| attributes          | short_image         | string          | Short version of the Container Image name.                                                                                                         |
| attributes          | sizes               | [integer]       | List of size for each platform-specific image associated with the image record. The list contains more than 1 entry for multi-architecture images. |
| attributes          | sources             | [string]        | List of sources where the Container Image was collected from.                                                                                      |
| attributes          | tags                | [string]        | List of tags associated with the Container Image.                                                                                                  |
| attributes          | vulnerability_count | object          | Vulnerability counts associated with the Container Image.                                                                                          |
| vulnerability_count | asset_id            | string          | ID of the Container Image.                                                                                                                         |
| vulnerability_count | critical            | int64           | Number of vulnerabilities with CVSS Critical severity.                                                                                             |
| vulnerability_count | high                | int64           | Number of vulnerabilities with CVSS High severity.                                                                                                 |
| vulnerability_count | low                 | int64           | Number of vulnerabilities with CVSS Low severity.                                                                                                  |
| vulnerability_count | medium              | int64           | Number of vulnerabilities with CVSS Medium severity.                                                                                               |
| vulnerability_count | none                | int64           | Number of vulnerabilities with CVSS None severity.                                                                                                 |
| vulnerability_count | unknown             | int64           | Number of vulnerabilities with an unknown CVSS severity.                                                                                           |
| Option 1            | id                  | string          | Container Image ID.                                                                                                                                |
| Option 1            | type                | enum            | Type of Container Image. Allowed enum values: `container_image`                                                                                    |
| data                | Option 2            | object          | Container Image Group object.                                                                                                                      |
| Option 2            | attributes          | object          | Attributes for a Container Image Group.                                                                                                            |
| attributes          | count               | int64           | Number of Container Images in the group.                                                                                                           |
| attributes          | name                | string          | Name of the Container Image group.                                                                                                                 |
| attributes          | tags                | object          | Tags from the group name parsed in key/value format.                                                                                               |
| Option 2            | id                  | string          | Container Image Group ID.                                                                                                                          |
| Option 2            | relationships       | object          | Relationships inside a Container Image Group.                                                                                                      |
| relationships       | container_images    | object          | Relationships to Container Images inside a Container Image Group.                                                                                  |
| container_images    | data                | [string]        | Links data.                                                                                                                                        |
| container_images    | links               | object          | Links attributes.                                                                                                                                  |
| links               | related             | string          | Link to related Container Images.                                                                                                                  |
| Option 2            | type                | enum            | Type of Container Image Group. Allowed enum values: `container_image_group`                                                                        |
|                     | links               | object          | Pagination links.                                                                                                                                  |
| links               | first               | string          | Link to the first page.                                                                                                                            |
| links               | last                | string          | Link to the last page.                                                                                                                             |
| links               | next                | string          | Link to the next page.                                                                                                                             |
| links               | prev                | string          | Link to previous page.                                                                                                                             |
| links               | self                | string          | Link to current page.                                                                                                                              |
|                     | meta                | object          | Response metadata object.                                                                                                                          |
| meta                | pagination          | object          | Paging attributes.                                                                                                                                 |
| pagination          | cursor              | string          | The cursor used to get the current results, if any.                                                                                                |
| pagination          | limit               | int32           | Number of results returned                                                                                                                         |
| pagination          | next_cursor         | string          | The cursor used to get the next results, if any.                                                                                                   |
| pagination          | prev_cursor         | string          | The cursor used to get the previous results, if any.                                                                                               |
| pagination          | total               | int64           | Total number of records that match the query.                                                                                                      |
| pagination          | type                | enum            | Type of Container Image pagination. Allowed enum values: `cursor_limit`                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
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
Authentication Error
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/container_images" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get all Container Images returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ContainerImagesAPI.new
p api_instance.list_container_images()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
