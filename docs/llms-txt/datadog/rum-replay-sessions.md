# Source: https://docs.datadoghq.com/api/latest/rum-replay-sessions.md

---
title: Rum Replay Sessions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Rum Replay Sessions
---

# Rum Replay Sessions

Retrieve segments for RUM replay sessions. Access session replay data stored in event platform or blob storage.

## Get segments{% #get-segments %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/views/{view_id}/segments |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/views/{view_id}/segments |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/replay/sessions/{session_id}/views/{view_id}/segments      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/replay/sessions/{session_id}/views/{view_id}/segments      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/views/{view_id}/segments     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/views/{view_id}/segments |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/views/{view_id}/segments |

### Overview

Get segments for a view.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                       |
| ---------------------------- | ------ | --------------------------------- |
| view_id [*required*]    | string | Unique identifier of the view.    |
| session_id [*required*] | string | Unique identifier of the session. |

#### Query Strings

| Name          | Type    | Description                                 |
| ------------- | ------- | ------------------------------------------- |
| source        | string  | Storage source: 'event_platform' or 'blob'. |
| ts            | integer | Server-side timestamp in milliseconds.      |
| max_list_size | integer | Maximum size in bytes for the segment list. |
| paging        | string  | Paging token for pagination.                |

### Response

{% tab title="200" %}
OK
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
                  \# Path parametersexport view_id="00000000-0000-0000-0000-000000000002"export session_id="00000000-0000-0000-0000-000000000001"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/sessions/${session_id}/views/${view_id}/segments" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get segments returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_sessions_api import RumReplaySessionsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplaySessionsApi(api_client)
    api_instance.get_segments(
        view_id="00000000-0000-0000-0000-000000000002",
        session_id="00000000-0000-0000-0000-000000000001",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get segments returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplaySessionsAPI.new
p api_instance.get_segments("00000000-0000-0000-0000-000000000002", "00000000-0000-0000-0000-000000000001")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get segments returns "OK" response

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
	api := datadogV2.NewRumReplaySessionsApi(apiClient)
	r, err := api.GetSegments(ctx, "00000000-0000-0000-0000-000000000002", "00000000-0000-0000-0000-000000000001", *datadogV2.NewGetSegmentsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumReplaySessionsApi.GetSegments`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get segments returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplaySessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplaySessionsApi apiInstance = new RumReplaySessionsApi(defaultClient);

    try {
      apiInstance.getSegments(
          "00000000-0000-0000-0000-000000000002", "00000000-0000-0000-0000-000000000001");
    } catch (ApiException e) {
      System.err.println("Exception when calling RumReplaySessionsApi#getSegments");
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
// Get segments returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_sessions::GetSegmentsOptionalParams;
use datadog_api_client::datadogV2::api_rum_replay_sessions::RumReplaySessionsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplaySessionsAPI::with_config(configuration);
    let resp = api
        .get_segments(
            "00000000-0000-0000-0000-000000000002".to_string(),
            "00000000-0000-0000-0000-000000000001".to_string(),
            GetSegmentsOptionalParams::default(),
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
 * Get segments returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplaySessionsApi(configuration);

const params: v2.RumReplaySessionsApiGetSegmentsRequest = {
  viewId: "00000000-0000-0000-0000-000000000002",
  sessionId: "00000000-0000-0000-0000-000000000001",
};

apiInstance
  .getSegments(params)
  .then((data: any) => {
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
