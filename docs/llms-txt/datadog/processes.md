# Source: https://docs.datadoghq.com/api/latest/processes.md

---
title: Processes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Processes
---

# Processes

The processes API allows you to query processes data for your organization. See the [Live Processes page](https://docs.datadoghq.com/infrastructure/process/) for more information.

## Get all processes{% #get-all-processes %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                       |
| ----------------- | -------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/processes |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/processes |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/processes      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/processes      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/processes     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/processes |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/processes |

### Overview

Get all processes for your organization.

### Arguments

#### Query Strings

| Name         | Type    | Description                                                                                                                                                                                                                                                         |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| search       | string  | String to search processes by.                                                                                                                                                                                                                                      |
| tags         | string  | Comma-separated list of tags to filter processes by.                                                                                                                                                                                                                |
| from         | integer | Unix timestamp (number of seconds since epoch) of the start of the query window. If not provided, the start of the query window will be 15 minutes before the `to` timestamp. If neither `from` nor `to` are provided, the query window will be `[now - 15m, now]`. |
| to           | integer | Unix timestamp (number of seconds since epoch) of the end of the query window. If not provided, the end of the query window will be 15 minutes after the `from` timestamp. If neither `from` nor `to` are provided, the query window will be `[now - 15m, now]`.    |
| page[limit]  | integer | Maximum number of results returned.                                                                                                                                                                                                                                 |
| page[cursor] | string  | String to query the next page of results. This key is provided with each valid response from the API in `meta.page.after`.                                                                                                                                          |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List of process summaries.

| Parent field | Field      | Type     | Description                                                                                                                                 |
| ------------ | ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data       | [object] | Array of process summary objects.                                                                                                           |
| data         | attributes | object   | Attributes for a process summary.                                                                                                           |
| attributes   | cmdline    | string   | Process command line.                                                                                                                       |
| attributes   | host       | string   | Host running the process.                                                                                                                   |
| attributes   | pid        | int64    | Process ID.                                                                                                                                 |
| attributes   | ppid       | int64    | Parent process ID.                                                                                                                          |
| attributes   | start      | string   | Time the process was started.                                                                                                               |
| attributes   | tags       | [string] | List of tags associated with the process.                                                                                                   |
| attributes   | timestamp  | string   | Time the process was seen.                                                                                                                  |
| attributes   | user       | string   | Process owner.                                                                                                                              |
| data         | id         | string   | Process ID.                                                                                                                                 |
| data         | type       | enum     | Type of process summary. Allowed enum values: `process`                                                                                     |
|              | meta       | object   | Response metadata object.                                                                                                                   |
| meta         | page       | object   | Paging attributes.                                                                                                                          |
| page         | after      | string   | The cursor used to get the next results, if any. To make the next request, use the same parameters with the addition of the `page[cursor]`. |
| page         | size       | int32    | Number of results returned.                                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "cmdline": "string",
        "host": "string",
        "pid": "integer",
        "ppid": "integer",
        "start": "string",
        "tags": [],
        "timestamp": "string",
        "user": "string"
      },
      "id": "string",
      "type": "process"
    }
  ],
  "meta": {
    "page": {
      "after": "911abf1204838d9cdfcb9a96d0b6a1bd03e1b514074f1ce1737c4cbd",
      "size": "integer"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/processes" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all processes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.processes_api import ProcessesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ProcessesApi(api_client)
    response = api_instance.list_processes(
        search="process-agent",
        tags="testing:true",
        page_limit=2,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get all processes returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ProcessesAPI.new
opts = {
  search: "process-agent",
  tags: "testing:true",
  page_limit: 2,
}
p api_instance.list_processes(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get all processes returns "OK" response

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
	api := datadogV2.NewProcessesApi(apiClient)
	resp, r, err := api.ListProcesses(ctx, *datadogV2.NewListProcessesOptionalParameters().WithSearch("process-agent").WithTags("testing:true").WithPageLimit(2))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProcessesApi.ListProcesses`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `ProcessesApi.ListProcesses`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get all processes returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ProcessesApi;
import com.datadog.api.client.v2.api.ProcessesApi.ListProcessesOptionalParameters;
import com.datadog.api.client.v2.model.ProcessSummariesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ProcessesApi apiInstance = new ProcessesApi(defaultClient);

    try {
      ProcessSummariesResponse result =
          apiInstance.listProcesses(
              new ListProcessesOptionalParameters()
                  .search("process-agent")
                  .tags("testing:true")
                  .pageLimit(2));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessesApi#listProcesses");
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
// Get all processes returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_processes::ListProcessesOptionalParams;
use datadog_api_client::datadogV2::api_processes::ProcessesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = ProcessesAPI::with_config(configuration);
    let resp = api
        .list_processes(
            ListProcessesOptionalParams::default()
                .search("process-agent".to_string())
                .tags("testing:true".to_string())
                .page_limit(2),
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Get all processes returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ProcessesApi(configuration);

const params: v2.ProcessesApiListProcessesRequest = {
  search: "process-agent",
  tags: "testing:true",
  pageLimit: 2,
};

apiInstance
  .listProcesses(params)
  .then((data: v2.ProcessSummariesResponse) => {
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
