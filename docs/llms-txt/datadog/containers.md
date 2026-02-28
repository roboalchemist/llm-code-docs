# Source: https://docs.datadoghq.com/api/latest/containers.md

---
title: Containers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Containers
---

# Containers

The Containers API allows you to query container data for your organization. See the [Container Monitoring page](https://docs.datadoghq.com/containers/) for more information.

## Get All Containers{% #get-all-containers %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                        |
| ----------------- | --------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/containers |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/containers |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/containers      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/containers      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/containers     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/containers |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/containers |

### Overview

Get all containers for your organization.

### Arguments

#### Query Strings

| Name         | Type    | Description                                                                                                                            |
| ------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| filter[tags] | string  | Comma-separated list of tags to filter containers by.                                                                                  |
| group_by     | string  | Comma-separated list of tags to group containers by.                                                                                   |
| sort         | string  | Attribute to sort containers by.                                                                                                       |
| page[size]   | integer | Maximum number of results returned.                                                                                                    |
| page[cursor] | string  | String to query the next page of results. This key is provided with each valid response from the API in `meta.pagination.next_cursor`. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of containers.

| Parent field  | Field         | Type            | Description                                                       |
| ------------- | ------------- | --------------- | ----------------------------------------------------------------- |
|               | data          | [<oneOf>] | Array of Container objects.                                       |
| data          | Option 1      | object          | Container object.                                                 |
| Option 1      | attributes    | object          | Attributes for a container.                                       |
| attributes    | container_id  | string          | The ID of the container.                                          |
| attributes    | created_at    | string          | Time the container was created.                                   |
| attributes    | host          | string          | Hostname of the host running the container.                       |
| attributes    | image_digest  | string          | Digest of the compressed image manifest.                          |
| attributes    | image_name    | string          | Name of the associated container image.                           |
| attributes    | image_tags    | [string]        | List of image tags associated with the container image.           |
| attributes    | name          | string          | Name of the container.                                            |
| attributes    | started_at    | string          | Time the container was started.                                   |
| attributes    | state         | string          | State of the container. This depends on the container runtime.    |
| attributes    | tags          | [string]        | List of tags associated with the container.                       |
| Option 1      | id            | string          | Container ID.                                                     |
| Option 1      | type          | enum            | Type of container. Allowed enum values: `container`               |
| data          | Option 2      | object          | Container group object.                                           |
| Option 2      | attributes    | object          | Attributes for a container group.                                 |
| attributes    | count         | int64           | Number of containers in the group.                                |
| attributes    | tags          | object          | Tags from the group name parsed in key/value format.              |
| Option 2      | id            | string          | Container Group ID.                                               |
| Option 2      | relationships | object          | Relationships to containers inside a container group.             |
| relationships | containers    | object          | Relationships to Containers inside a Container Group.             |
| containers    | data          | [string]        | Links data.                                                       |
| containers    | links         | object          | Links attributes.                                                 |
| links         | related       | string          | Link to related containers.                                       |
| Option 2      | type          | enum            | Type of container group. Allowed enum values: `container_group`   |
|               | links         | object          | Pagination links.                                                 |
| links         | first         | string          | Link to the first page.                                           |
| links         | last          | string          | Link to the last page.                                            |
| links         | next          | string          | Link to the next page.                                            |
| links         | prev          | string          | Link to previous page.                                            |
| links         | self          | string          | Link to current page.                                             |
|               | meta          | object          | Response metadata object.                                         |
| meta          | pagination    | object          | Paging attributes.                                                |
| pagination    | cursor        | string          | The cursor used to get the current results, if any.               |
| pagination    | limit         | int32           | Number of results returned                                        |
| pagination    | next_cursor   | string          | The cursor used to get the next results, if any.                  |
| pagination    | prev_cursor   | string          | The cursor used to get the previous results, if any.              |
| pagination    | total         | int64           | Total number of records that match the query.                     |
| pagination    | type          | enum            | Type of Container pagination. Allowed enum values: `cursor_limit` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [{
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
    }],
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
  "errors": ["Bad Request"]
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
  "errors": ["Bad Request"]
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
  "errors": ["Bad Request"]
}

```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/containers" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get All Containers returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ContainersAPI.new
p api_instance.list_containers()

```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
