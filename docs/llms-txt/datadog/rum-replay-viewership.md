# Source: https://docs.datadoghq.com/api/latest/rum-replay-viewership.md

---
title: Rum Replay Viewership
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Rum Replay Viewership
---

# Rum Replay Viewership

Track and manage RUM replay session viewership. Monitor who watches replay sessions and maintain watch history for audit and analytics purposes.

## List rum replay viewership history sessions{% #list-rum-replay-viewership-history-sessions %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                    |
| ----------------- | ------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/replay/viewership-history/sessions |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/replay/viewership-history/sessions |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/replay/viewership-history/sessions      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/replay/viewership-history/sessions      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/replay/viewership-history/sessions     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/replay/viewership-history/sessions |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/replay/viewership-history/sessions |

### Overview

List watched sessions.

### Arguments

#### Query Strings

| Name                      | Type    | Description                                                     |
| ------------------------- | ------- | --------------------------------------------------------------- |
| filter[watched_at][start] | integer | Start timestamp in milliseconds for watched_at filter.          |
| page[number]              | integer | Page number for pagination (0-indexed).                         |
| filter[created_by]        | string  | Filter by user UUID. Defaults to current user if not specified. |
| filter[watched_at][end]   | integer | End timestamp in milliseconds for watched_at filter.            |
| filter[session_ids]       | string  | Comma-separated list of session IDs to filter by.               |
| page[size]                | integer | Number of items per page.                                       |
| filter[application_id]    | string  | Filter by application ID.                                       |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                             | Type      | Description                                                                 |
| ------------ | --------------------------------- | --------- | --------------------------------------------------------------------------- |
|              | data [*required*]            | [object]  |
| data         | attributes                        | object    |
| attributes   | event_id                          | string    |
| attributes   | last_watched_at [*required*] | date-time |
| attributes   | session_event                     | object    |
| attributes   | track                             | string    |
| data         | id                                | string    |
| data         | type [*required*]            | enum      | Rum replay session resource type. Allowed enum values: `rum_replay_session` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "event_id": "string",
        "last_watched_at": "2026-01-13T17:15:53.208340Z",
        "session_event": {},
        "track": "string"
      },
      "id": "string",
      "type": "rum_replay_session"
    }
  ]
}
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/viewership-history/sessions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List rum replay viewership history sessions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_viewership_api import RumReplayViewershipApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayViewershipApi(api_client)
    response = api_instance.list_rum_replay_viewership_history_sessions()

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List rum replay viewership history sessions returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayViewershipAPI.new
p api_instance.list_rum_replay_viewership_history_sessions()
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List rum replay viewership history sessions returns "OK" response

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
    api := datadogV2.NewRumReplayViewershipApi(apiClient)
    resp, r, err := api.ListRumReplayViewershipHistorySessions(ctx, *datadogV2.NewListRumReplayViewershipHistorySessionsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayViewershipApi.ListRumReplayViewershipHistorySessions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RumReplayViewershipApi.ListRumReplayViewershipHistorySessions`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List rum replay viewership history sessions returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayViewershipApi;
import com.datadog.api.client.v2.model.ViewershipHistorySessionArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayViewershipApi apiInstance = new RumReplayViewershipApi(defaultClient);

    try {
      ViewershipHistorySessionArray result = apiInstance.listRumReplayViewershipHistorySessions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling RumReplayViewershipApi#listRumReplayViewershipHistorySessions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// List rum replay viewership history sessions returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_viewership::ListRumReplayViewershipHistorySessionsOptionalParams;
use datadog_api_client::datadogV2::api_rum_replay_viewership::RumReplayViewershipAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplayViewershipAPI::with_config(configuration);
    let resp = api
        .list_rum_replay_viewership_history_sessions(
            ListRumReplayViewershipHistorySessionsOptionalParams::default(),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * List rum replay viewership history sessions returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayViewershipApi(configuration);

apiInstance
  .listRumReplayViewershipHistorySessions()
  .then((data: v2.ViewershipHistorySessionArray) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create rum replay session watch{% #create-rum-replay-session-watch %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watches |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watches |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/rum/replay/sessions/{session_id}/watches      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/rum/replay/sessions/{session_id}/watches      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watches     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watches |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watches |

### Overview

Record a session watch.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                       |
| ---------------------------- | ------ | --------------------------------- |
| session_id [*required*] | string | Unique identifier of the session. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                            | Type      | Description                                                             |
| ------------ | -------------------------------- | --------- | ----------------------------------------------------------------------- |
|              | data [*required*]           | object    |
| data         | attributes                       | object    |
| attributes   | application_id [*required*] | string    |
| attributes   | data_source                      | string    |
| attributes   | event_id [*required*]       | string    |
| attributes   | timestamp [*required*]      | date-time |
| data         | id                               | string    |
| data         | type [*required*]           | enum      | Rum replay watch resource type. Allowed enum values: `rum_replay_watch` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "application_id": "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
      "data_source": "string",
      "event_id": "11111111-2222-3333-4444-555555555555",
      "timestamp": "2026-01-13T17:15:53.208340Z"
    },
    "id": "string",
    "type": "rum_replay_watch"
  }
}
```text

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field | Field                            | Type      | Description                                                             |
| ------------ | -------------------------------- | --------- | ----------------------------------------------------------------------- |
|              | data [*required*]           | object    |
| data         | attributes                       | object    |
| attributes   | application_id [*required*] | string    |
| attributes   | data_source                      | string    |
| attributes   | event_id [*required*]       | string    |
| attributes   | timestamp [*required*]      | date-time |
| data         | id                               | string    |
| data         | type [*required*]           | enum      | Rum replay watch resource type. Allowed enum values: `rum_replay_watch` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "application_id": "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
      "data_source": "string",
      "event_id": "11111111-2222-3333-4444-555555555555",
      "timestamp": "2026-01-13T17:15:53.208340Z"
    },
    "id": "string",
    "type": "rum_replay_watch"
  }
}
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport session_id="00000000-0000-0000-0000-000000000001"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/sessions/${session_id}/watches" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "application_id": "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
      "event_id": "11111111-2222-3333-4444-555555555555",
      "timestamp": "2026-01-13T17:15:53.208340Z"
    },
    "type": "rum_replay_watch"
  }
}
EOF

#####

```python
"""
Create rum replay session watch returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_viewership_api import RumReplayViewershipApi
from datadog_api_client.v2.model.watch import Watch
from datadog_api_client.v2.model.watch_data import WatchData
from datadog_api_client.v2.model.watch_data_attributes import WatchDataAttributes
from datadog_api_client.v2.model.watch_data_type import WatchDataType
from datetime import datetime
from dateutil.tz import tzutc

body = Watch(
    data=WatchData(
        attributes=WatchDataAttributes(
            application_id="aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
            event_id="11111111-2222-3333-4444-555555555555",
            timestamp=datetime(2026, 1, 13, 17, 15, 53, 208340, tzinfo=tzutc()),
        ),
        type=WatchDataType.RUM_REPLAY_WATCH,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayViewershipApi(api_client)
    response = api_instance.create_rum_replay_session_watch(
        session_id="00000000-0000-0000-0000-000000000001", body=body
    )

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create rum replay session watch returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayViewershipAPI.new

body = DatadogAPIClient::V2::Watch.new({
  data: DatadogAPIClient::V2::WatchData.new({
    attributes: DatadogAPIClient::V2::WatchDataAttributes.new({
      application_id: "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
      event_id: "11111111-2222-3333-4444-555555555555",
      timestamp: "2026-01-13T17:15:53.208340Z",
    }),
    type: DatadogAPIClient::V2::WatchDataType::RUM_REPLAY_WATCH,
  }),
})
p api_instance.create_rum_replay_session_watch("00000000-0000-0000-0000-000000000001", body)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Create rum replay session watch returns "Created" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"
    "time"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.Watch{
        Data: datadogV2.WatchData{
            Attributes: &datadogV2.WatchDataAttributes{
                ApplicationId: "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
                EventId:       "11111111-2222-3333-4444-555555555555",
                Timestamp:     time.Date(2026, 1, 13, 17, 15, 53, 208340, time.UTC),
            },
            Type: datadogV2.WATCHDATATYPE_RUM_REPLAY_WATCH,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRumReplayViewershipApi(apiClient)
    resp, r, err := api.CreateRumReplaySessionWatch(ctx, "00000000-0000-0000-0000-000000000001", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayViewershipApi.CreateRumReplaySessionWatch`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RumReplayViewershipApi.CreateRumReplaySessionWatch`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create rum replay session watch returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayViewershipApi;
import com.datadog.api.client.v2.model.Watch;
import com.datadog.api.client.v2.model.WatchData;
import com.datadog.api.client.v2.model.WatchDataAttributes;
import com.datadog.api.client.v2.model.WatchDataType;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayViewershipApi apiInstance = new RumReplayViewershipApi(defaultClient);

    Watch body =
        new Watch()
            .data(
                new WatchData()
                    .attributes(
                        new WatchDataAttributes()
                            .applicationId("aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb")
                            .eventId("11111111-2222-3333-4444-555555555555")
                            .timestamp(OffsetDateTime.parse("2026-01-13T17:15:53.208340Z")))
                    .type(WatchDataType.RUM_REPLAY_WATCH));

    try {
      Watch result =
          apiInstance.createRumReplaySessionWatch("00000000-0000-0000-0000-000000000001", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling RumReplayViewershipApi#createRumReplaySessionWatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Create rum replay session watch returns "Created" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_viewership::RumReplayViewershipAPI;
use datadog_api_client::datadogV2::model::Watch;
use datadog_api_client::datadogV2::model::WatchData;
use datadog_api_client::datadogV2::model::WatchDataAttributes;
use datadog_api_client::datadogV2::model::WatchDataType;

#[tokio::main]
async fn main() {
    let body = Watch::new(
        WatchData::new(WatchDataType::RUM_REPLAY_WATCH).attributes(WatchDataAttributes::new(
            "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb".to_string(),
            "11111111-2222-3333-4444-555555555555".to_string(),
            DateTime::parse_from_rfc3339("2026-01-13T17:15:53.208340+00:00")
                .expect("Failed to parse datetime")
                .with_timezone(&Utc),
        )),
    );
    let configuration = datadog::Configuration::new();
    let api = RumReplayViewershipAPI::with_config(configuration);
    let resp = api
        .create_rum_replay_session_watch("00000000-0000-0000-0000-000000000001".to_string(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Create rum replay session watch returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayViewershipApi(configuration);

const params: v2.RumReplayViewershipApiCreateRumReplaySessionWatchRequest = {
  body: {
    data: {
      attributes: {
        applicationId: "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
        eventId: "11111111-2222-3333-4444-555555555555",
        timestamp: new Date(2026, 1, 13, 17, 15, 53, 208340),
      },
      type: "rum_replay_watch",
    },
  },
  sessionId: "00000000-0000-0000-0000-000000000001",
};

apiInstance
  .createRumReplaySessionWatch(params)
  .then((data: v2.Watch) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete rum replay session watch{% #delete-rum-replay-session-watch %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watches |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watches |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/rum/replay/sessions/{session_id}/watches      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/rum/replay/sessions/{session_id}/watches      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watches     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watches |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watches |

### Overview

Delete session watch history.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                       |
| ---------------------------- | ------ | --------------------------------- |
| session_id [*required*] | string | Unique identifier of the session. |

### Response

{% tab title="204" %}
No Content
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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport session_id="00000000-0000-0000-0000-000000000001"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/sessions/${session_id}/watches" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete rum replay session watch returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_viewership_api import RumReplayViewershipApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayViewershipApi(api_client)
    api_instance.delete_rum_replay_session_watch(
        session_id="00000000-0000-0000-0000-000000000001",
    )
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete rum replay session watch returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayViewershipAPI.new
api_instance.delete_rum_replay_session_watch("00000000-0000-0000-0000-000000000001")
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete rum replay session watch returns "No Content" response

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
    api := datadogV2.NewRumReplayViewershipApi(apiClient)
    r, err := api.DeleteRumReplaySessionWatch(ctx, "00000000-0000-0000-0000-000000000001")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayViewershipApi.DeleteRumReplaySessionWatch`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete rum replay session watch returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayViewershipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayViewershipApi apiInstance = new RumReplayViewershipApi(defaultClient);

    try {
      apiInstance.deleteRumReplaySessionWatch("00000000-0000-0000-0000-000000000001");
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling RumReplayViewershipApi#deleteRumReplaySessionWatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// Delete rum replay session watch returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_viewership::RumReplayViewershipAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplayViewershipAPI::with_config(configuration);
    let resp = api
        .delete_rum_replay_session_watch("00000000-0000-0000-0000-000000000001".to_string())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Delete rum replay session watch returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayViewershipApi(configuration);

const params: v2.RumReplayViewershipApiDeleteRumReplaySessionWatchRequest = {
  sessionId: "00000000-0000-0000-0000-000000000001",
};

apiInstance
  .deleteRumReplaySessionWatch(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## List rum replay session watchers{% #list-rum-replay-session-watchers %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watchers |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watchers |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/replay/sessions/{session_id}/watchers      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/replay/sessions/{session_id}/watchers      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watchers     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watchers |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/replay/sessions/{session_id}/watchers |

### Overview

List session watchers.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                       |
| ---------------------------- | ------ | --------------------------------- |
| session_id [*required*] | string | Unique identifier of the session. |

#### Query Strings

| Name         | Type    | Description                             |
| ------------ | ------- | --------------------------------------- |
| page[size]   | integer | Number of items per page.               |
| page[number] | integer | Page number for pagination (0-indexed). |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                             | Type      | Description                                                                 |
| ------------ | --------------------------------- | --------- | --------------------------------------------------------------------------- |
|              | data [*required*]            | [object]  |
| data         | attributes                        | object    |
| attributes   | handle [*required*]          | string    |
| attributes   | icon                              | string    |
| attributes   | last_watched_at [*required*] | date-time |
| attributes   | name                              | string    |
| attributes   | watch_count [*required*]     | int32     |
| data         | id                                | string    |
| data         | type [*required*]            | enum      | Rum replay watcher resource type. Allowed enum values: `rum_replay_watcher` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "handle": "john.doe@example.com",
        "icon": "string",
        "last_watched_at": "2026-01-13T17:15:53.208340Z",
        "name": "string",
        "watch_count": 0
      },
      "id": "string",
      "type": "rum_replay_watcher"
    }
  ]
}
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport session_id="00000000-0000-0000-0000-000000000001"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/sessions/${session_id}/watchers" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List rum replay session watchers returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_viewership_api import RumReplayViewershipApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayViewershipApi(api_client)
    response = api_instance.list_rum_replay_session_watchers(
        session_id="00000000-0000-0000-0000-000000000001",
    )

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List rum replay session watchers returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayViewershipAPI.new
p api_instance.list_rum_replay_session_watchers("00000000-0000-0000-0000-000000000001")
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List rum replay session watchers returns "OK" response

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
    api := datadogV2.NewRumReplayViewershipApi(apiClient)
    resp, r, err := api.ListRumReplaySessionWatchers(ctx, "00000000-0000-0000-0000-000000000001", *datadogV2.NewListRumReplaySessionWatchersOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayViewershipApi.ListRumReplaySessionWatchers`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RumReplayViewershipApi.ListRumReplaySessionWatchers`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List rum replay session watchers returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayViewershipApi;
import com.datadog.api.client.v2.model.WatcherArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayViewershipApi apiInstance = new RumReplayViewershipApi(defaultClient);

    try {
      WatcherArray result =
          apiInstance.listRumReplaySessionWatchers("00000000-0000-0000-0000-000000000001");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling RumReplayViewershipApi#listRumReplaySessionWatchers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
// List rum replay session watchers returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_viewership::ListRumReplaySessionWatchersOptionalParams;
use datadog_api_client::datadogV2::api_rum_replay_viewership::RumReplayViewershipAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplayViewershipAPI::with_config(configuration);
    let resp = api
        .list_rum_replay_session_watchers(
            "00000000-0000-0000-0000-000000000001".to_string(),
            ListRumReplaySessionWatchersOptionalParams::default(),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * List rum replay session watchers returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayViewershipApi(configuration);

const params: v2.RumReplayViewershipApiListRumReplaySessionWatchersRequest = {
  sessionId: "00000000-0000-0000-0000-000000000001",
};

apiInstance
  .listRumReplaySessionWatchers(params)
  .then((data: v2.WatcherArray) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
