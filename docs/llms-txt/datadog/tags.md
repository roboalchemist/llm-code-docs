# Source: https://docs.datadoghq.com/api/latest/tags.md

---
title: Tags
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Tags
---

The tag endpoint allows you to assign tags to hosts, for example: `role:database`. Those tags are applied to all metrics sent by the host. Refer to hosts by name (`yourhost.example.com`) when fetching and applying tags to a particular host.

The component of your infrastructure responsible for a tag is identified by a source. For example, some valid sources include nagios, hudson, jenkins, users, feed, chef, puppet, git, bitbucket, fabric, capistrano, etc. Find a complete list of source type names under [API Source Attributes](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).

Read more about tags on [Getting Started with Tags](https://docs.datadoghq.com/getting_started/tagging/).

## Get All Host Tags{% #get-all-host-tags %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                        |
| ----------------- | --------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/tags/hosts |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/tags/hosts |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/tags/hosts      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/tags/hosts      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/tags/hosts     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/tags/hosts |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/tags/hosts |

### Overview

Returns a mapping of tags to hosts. For each tag, the response returns a list of host names that contain this tag. There is a restriction of 10k total host names from the org that can be attached to tags and returned.

### Arguments

#### Query Strings

| Name   | Type   | Description                                                                                                                                                                              |
| ------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| source | string | Source to filter. [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). Use "user" source for custom-defined tags. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
In this object, the key is the tag, and the value is a list of host names that are reporting that tag.

| Parent field         | Field     | Type     | Description                                 |
| -------------------- | --------- | -------- | ------------------------------------------- |
|                      | tags      | object   | A mapping of tags to host names             |
| additionalProperties | <any-key> | [string] | A list of host names which contain this tag |

{% /tab %}

{% tab title="Example" %}

```json
{
  "tags": {
    "<any-key>": [
      "test.metric.host"
    ]
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/tags/hosts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get All Host Tags returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    response = api_instance.list_host_tags()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::TagsAPI.new
p api_instance.list_host_tags()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get All Host Tags returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewTagsApi(apiClient)
    resp, r, err := api.ListHostTags(ctx, *datadogV1.NewListHostTagsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TagsApi.ListHostTags`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TagsApi.ListHostTags`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get All Host Tags returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.TagsApi;
import com.datadog.api.client.v1.model.TagToHosts;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TagsApi apiInstance = new TagsApi(defaultClient);

    try {
      TagToHosts result = apiInstance.listHostTags();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#listHostTags");
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
// Get All Host Tags returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_tags::ListHostTagsOptionalParams;
use datadog_api_client::datadogV1::api_tags::TagsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = TagsAPI::with_config(configuration);
    let resp = api
        .list_host_tags(ListHostTagsOptionalParams::default())
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
 * Get All Host Tags returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.TagsApi(configuration);

apiInstance
  .listHostTags()
  .then((data: v1.TagToHosts) => {
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

## Get Host Tags{% #get-host-tags %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/tags/hosts/{host_name} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/tags/hosts/{host_name} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/tags/hosts/{host_name}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/tags/hosts/{host_name}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/tags/hosts/{host_name}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/tags/hosts/{host_name} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/tags/hosts/{host_name} |

### Overview

Return the list of tags that apply to a given host.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                           |
| --------------------------- | ------ | ------------------------------------- |
| host_name [*required*] | string | Name of the host to retrieve tags for |

#### Query Strings

| Name   | Type   | Description                                                                                                                                                                              |
| ------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| source | string | Source to filter. [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). Use "user" source for custom-defined tags. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Host name and an array of its tags

| Field | Type     | Description                            |
| ----- | -------- | -------------------------------------- |
| host  | string   | Your host name.                        |
| tags  | [string] | A list of tags associated with a host. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "host": "test.host",
  "tags": [
    "environment:production"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Path parametersexport host_name="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/tags/hosts/${host_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get Host Tags returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    response = api_instance.get_host_tags(
        host_name="host_name",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::TagsAPI.new
p api_instance.get_host_tags("host_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get Host Tags returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewTagsApi(apiClient)
    resp, r, err := api.GetHostTags(ctx, "host_name", *datadogV1.NewGetHostTagsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TagsApi.GetHostTags`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TagsApi.GetHostTags`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get Host Tags returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.TagsApi;
import com.datadog.api.client.v1.model.HostTags;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TagsApi apiInstance = new TagsApi(defaultClient);

    try {
      HostTags result = apiInstance.getHostTags("host_name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#getHostTags");
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
// Get Host Tags returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_tags::GetHostTagsOptionalParams;
use datadog_api_client::datadogV1::api_tags::TagsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = TagsAPI::with_config(configuration);
    let resp = api
        .get_host_tags(
            "host_name".to_string(),
            GetHostTagsOptionalParams::default(),
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
 * Get Host Tags returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.TagsApi(configuration);

const params: v1.TagsApiGetHostTagsRequest = {
  hostName: "host_name",
};

apiInstance
  .getHostTags(params)
  .then((data: v1.HostTags) => {
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

## Add tags to a host{% #add-tags-to-a-host %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/tags/hosts/{host_name} |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/tags/hosts/{host_name} |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/tags/hosts/{host_name}      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/tags/hosts/{host_name}      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/tags/hosts/{host_name}     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/tags/hosts/{host_name} |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/tags/hosts/{host_name} |

### Overview

This endpoint allows you to add new tags to a host, optionally specifying what source these tags come from. If tags already exist, appends new tags to the tag list. If no source is specified, defaults to "user".

### Arguments

#### Path Parameters

| Name                        | Type   | Description                         |
| --------------------------- | ------ | ----------------------------------- |
| host_name [*required*] | string | Specified host name to add new tags |

#### Query Strings

| Name   | Type   | Description                                                                                                                                                                                                                               |
| ------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| source | string | Source to add tags. [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). Use "user" source for custom-defined tags. If no source is specified, defaults to "user". |

### Request

#### Body Data (required)

Update host tags request body.

{% tab title="Model" %}

| Field | Type     | Description                            |
| ----- | -------- | -------------------------------------- |
| host  | string   | Your host name.                        |
| tags  | [string] | A list of tags associated with a host. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "host": "test.host",
  "tags": [
    "environment:production"
  ]
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Host name and an array of its tags

| Field | Type     | Description                            |
| ----- | -------- | -------------------------------------- |
| host  | string   | Your host name.                        |
| tags  | [string] | A list of tags associated with a host. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "host": "test.host",
  "tags": [
    "environment:production"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Path parametersexport host_name="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/tags/hosts/${host_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF

#####

```python
"""
Add tags to a host returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi
from datadog_api_client.v1.model.host_tags import HostTags

body = HostTags(
    host="test.host",
    tags=[
        "environment:production",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    response = api_instance.create_host_tags(host_name="host_name", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::TagsAPI.new

body = DatadogAPIClient::V1::HostTags.new({
  host: "test.host",
  tags: [
    "environment:production",
  ],
})
p api_instance.create_host_tags("host_name", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Add tags to a host returns "Created" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.HostTags{
        Host: datadog.PtrString("test.host"),
        Tags: []string{
            "environment:production",
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewTagsApi(apiClient)
    resp, r, err := api.CreateHostTags(ctx, "host_name", body, *datadogV1.NewCreateHostTagsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TagsApi.CreateHostTags`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TagsApi.CreateHostTags`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Add tags to a host returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.TagsApi;
import com.datadog.api.client.v1.model.HostTags;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TagsApi apiInstance = new TagsApi(defaultClient);

    HostTags body =
        new HostTags().host("test.host").tags(Collections.singletonList("environment:production"));

    try {
      HostTags result = apiInstance.createHostTags("host_name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#createHostTags");
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
// Add tags to a host returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_tags::CreateHostTagsOptionalParams;
use datadog_api_client::datadogV1::api_tags::TagsAPI;
use datadog_api_client::datadogV1::model::HostTags;

#[tokio::main]
async fn main() {
    let body = HostTags::new()
        .host("test.host".to_string())
        .tags(vec!["environment:production".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = TagsAPI::with_config(configuration);
    let resp = api
        .create_host_tags(
            "host_name".to_string(),
            body,
            CreateHostTagsOptionalParams::default(),
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
 * Add tags to a host returns "Created" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.TagsApi(configuration);

const params: v1.TagsApiCreateHostTagsRequest = {
  body: {
    host: "test.host",
    tags: ["environment:production"],
  },
  hostName: "host_name",
};

apiInstance
  .createHostTags(params)
  .then((data: v1.HostTags) => {
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

## Update host tags{% #update-host-tags %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/tags/hosts/{host_name} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/tags/hosts/{host_name} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/tags/hosts/{host_name}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/tags/hosts/{host_name}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/tags/hosts/{host_name}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/tags/hosts/{host_name} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/tags/hosts/{host_name} |

### Overview

This endpoint allows you to update/replace all tags in an integration source with those supplied in the request.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                        |
| --------------------------- | ------ | ---------------------------------- |
| host_name [*required*] | string | Specified host name to change tags |

#### Query Strings

| Name   | Type   | Description                                                                                                                                                                                                                               |
| ------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| source | string | Source to update tags. [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). Use "user" source for custom-defined tags. If no source specified, defaults to "user". |

### Request

#### Body Data (required)

Add tags to host

{% tab title="Model" %}

| Field | Type     | Description                            |
| ----- | -------- | -------------------------------------- |
| host  | string   | Your host name.                        |
| tags  | [string] | A list of tags associated with a host. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "host": "test.host",
  "tags": [
    "environment:production"
  ]
}
```

{% /tab %}

### Response

{% tab title="201" %}
OK
{% tab title="Model" %}
Host name and an array of its tags

| Field | Type     | Description                            |
| ----- | -------- | -------------------------------------- |
| host  | string   | Your host name.                        |
| tags  | [string] | A list of tags associated with a host. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "host": "test.host",
  "tags": [
    "environment:production"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Path parametersexport host_name="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/tags/hosts/${host_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF

#####

```python
"""
Update host tags returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi
from datadog_api_client.v1.model.host_tags import HostTags

body = HostTags(
    host="test.host",
    tags=[
        "environment:production",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    response = api_instance.update_host_tags(host_name="host_name", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::TagsAPI.new

body = DatadogAPIClient::V1::HostTags.new({
  host: "test.host",
  tags: [
    "environment:production",
  ],
})
p api_instance.update_host_tags("host_name", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Update host tags returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.HostTags{
        Host: datadog.PtrString("test.host"),
        Tags: []string{
            "environment:production",
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewTagsApi(apiClient)
    resp, r, err := api.UpdateHostTags(ctx, "host_name", body, *datadogV1.NewUpdateHostTagsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TagsApi.UpdateHostTags`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `TagsApi.UpdateHostTags`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update host tags returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.TagsApi;
import com.datadog.api.client.v1.model.HostTags;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TagsApi apiInstance = new TagsApi(defaultClient);

    HostTags body =
        new HostTags().host("test.host").tags(Collections.singletonList("environment:production"));

    try {
      HostTags result = apiInstance.updateHostTags("host_name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#updateHostTags");
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
// Update host tags returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_tags::TagsAPI;
use datadog_api_client::datadogV1::api_tags::UpdateHostTagsOptionalParams;
use datadog_api_client::datadogV1::model::HostTags;

#[tokio::main]
async fn main() {
    let body = HostTags::new()
        .host("test.host".to_string())
        .tags(vec!["environment:production".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = TagsAPI::with_config(configuration);
    let resp = api
        .update_host_tags(
            "host_name".to_string(),
            body,
            UpdateHostTagsOptionalParams::default(),
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
 * Update host tags returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.TagsApi(configuration);

const params: v1.TagsApiUpdateHostTagsRequest = {
  body: {
    host: "test.host",
    tags: ["environment:production"],
  },
  hostName: "host_name",
};

apiInstance
  .updateHostTags(params)
  .then((data: v1.HostTags) => {
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

## Remove host tags{% #remove-host-tags %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/tags/hosts/{host_name} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/tags/hosts/{host_name} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/tags/hosts/{host_name}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/tags/hosts/{host_name}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/tags/hosts/{host_name}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/tags/hosts/{host_name} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/tags/hosts/{host_name} |

### Overview

This endpoint allows you to remove all tags for a single host. If no source is specified, only deletes from the source "User".

### Arguments

#### Path Parameters

| Name                        | Type   | Description                        |
| --------------------------- | ------ | ---------------------------------- |
| host_name [*required*] | string | Specified host name to delete tags |

#### Query Strings

| Name   | Type   | Description                                                                                                                                                                                              |
| ------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| source | string | Source of the tags to be deleted. [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). Use "user" source for custom-defined tags. |

### Response

{% tab title="204" %}
OK
{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Path parametersexport host_name="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/tags/hosts/${host_name}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Remove host tags returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    api_instance.delete_host_tags(
        host_name="host_name",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::TagsAPI.new
api_instance.delete_host_tags("host_name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Remove host tags returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewTagsApi(apiClient)
    r, err := api.DeleteHostTags(ctx, "host_name", *datadogV1.NewDeleteHostTagsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TagsApi.DeleteHostTags`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Remove host tags returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    TagsApi apiInstance = new TagsApi(defaultClient);

    try {
      apiInstance.deleteHostTags("host_name");
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#deleteHostTags");
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
// Remove host tags returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_tags::DeleteHostTagsOptionalParams;
use datadog_api_client::datadogV1::api_tags::TagsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = TagsAPI::with_config(configuration);
    let resp = api
        .delete_host_tags(
            "host_name".to_string(),
            DeleteHostTagsOptionalParams::default(),
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
 * Remove host tags returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.TagsApi(configuration);

const params: v1.TagsApiDeleteHostTagsRequest = {
  hostName: "host_name",
};

apiInstance
  .deleteHostTags(params)
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
