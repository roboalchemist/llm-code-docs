# Source: https://docs.datadoghq.com/api/latest/rum-replay-heatmaps.md

---
title: Rum Replay Heatmaps
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Rum Replay Heatmaps
---

# Rum Replay Heatmaps

Manage heatmap snapshots for RUM replay sessions. Create, update, delete, and retrieve snapshots to visualize user interactions on specific views.

## Create replay heatmap snapshot{% #create-replay-heatmap-snapshot %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/replay/heatmap/snapshots |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/replay/heatmap/snapshots |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/replay/heatmap/snapshots      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/replay/heatmap/snapshots      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/replay/heatmap/snapshots     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/replay/heatmap/snapshots |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/replay/heatmap/snapshots |

### Overview

Create a heatmap snapshot.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                                             | Type    | Description                                               |
| ------------ | ------------------------------------------------- | ------- | --------------------------------------------------------- |
|              | data [*required*]                            | object  |
| data         | attributes                                        | object  |
| attributes   | application_id [*required*]                  | string  |
| attributes   | device_type [*required*]                     | string  |
| attributes   | event_id [*required*]                        | string  |
| attributes   | is_device_type_selected_by_user [*required*] | boolean |
| attributes   | session_id                                        | string  |
| attributes   | snapshot_name [*required*]                   | string  |
| attributes   | start [*required*]                           | int64   |
| attributes   | view_id                                           | string  |
| attributes   | view_name [*required*]                       | string  |
| data         | type [*required*]                            | enum    | Snapshots resource type. Allowed enum values: `snapshots` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "application_id": "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
      "device_type": "desktop",
      "event_id": "11111111-2222-3333-4444-555555555555",
      "is_device_type_selected_by_user": false,
      "session_id": "string",
      "snapshot_name": "My Snapshot",
      "start": 0,
      "view_id": "string",
      "view_name": "/home"
    },
    "type": "snapshots"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field | Field                           | Type      | Description                                               |
| ------------ | ------------------------------- | --------- | --------------------------------------------------------- |
|              | data                            | object    |
| data         | attributes                      | object    |
| attributes   | application_id                  | string    |
| attributes   | created_at                      | date-time |
| attributes   | created_by                      | string    |
| attributes   | created_by_handle               | string    |
| attributes   | created_by_user_id              | int64     |
| attributes   | device_type                     | string    |
| attributes   | event_id                        | string    |
| attributes   | is_device_type_selected_by_user | boolean   |
| attributes   | modified_at                     | date-time |
| attributes   | org_id                          | int64     |
| attributes   | session_id                      | string    |
| attributes   | snapshot_name                   | string    |
| attributes   | start                           | int64     |
| attributes   | view_id                         | string    |
| attributes   | view_name                       | string    |
| data         | id                              | string    |
| data         | type [*required*]          | enum      | Snapshots resource type. Allowed enum values: `snapshots` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "application_id": "string",
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": "string",
      "created_by_handle": "string",
      "created_by_user_id": "integer",
      "device_type": "string",
      "event_id": "string",
      "is_device_type_selected_by_user": false,
      "modified_at": "2019-09-19T10:00:00.000Z",
      "org_id": "integer",
      "session_id": "string",
      "snapshot_name": "string",
      "start": "integer",
      "view_id": "string",
      "view_name": "string"
    },
    "id": "string",
    "type": "snapshots"
  }
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/replay/heatmap/snapshots" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "application_id": "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
      "device_type": "desktop",
      "event_id": "11111111-2222-3333-4444-555555555555",
      "is_device_type_selected_by_user": false,
      "snapshot_name": "My Snapshot",
      "start": 0,
      "view_name": "/home"
    },
    "type": "snapshots"
  }
}
EOF
                
##### 

```python
"""
Create replay heatmap snapshot returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_heatmaps_api import RumReplayHeatmapsApi
from datadog_api_client.v2.model.snapshot_create_request import SnapshotCreateRequest
from datadog_api_client.v2.model.snapshot_create_request_data import SnapshotCreateRequestData
from datadog_api_client.v2.model.snapshot_create_request_data_attributes import SnapshotCreateRequestDataAttributes
from datadog_api_client.v2.model.snapshot_update_request_data_type import SnapshotUpdateRequestDataType

body = SnapshotCreateRequest(
    data=SnapshotCreateRequestData(
        attributes=SnapshotCreateRequestDataAttributes(
            application_id="aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
            device_type="desktop",
            event_id="11111111-2222-3333-4444-555555555555",
            is_device_type_selected_by_user=False,
            snapshot_name="My Snapshot",
            start=0,
            view_name="/home",
        ),
        type=SnapshotUpdateRequestDataType.SNAPSHOTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayHeatmapsApi(api_client)
    response = api_instance.create_replay_heatmap_snapshot(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create replay heatmap snapshot returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayHeatmapsAPI.new

body = DatadogAPIClient::V2::SnapshotCreateRequest.new({
  data: DatadogAPIClient::V2::SnapshotCreateRequestData.new({
    attributes: DatadogAPIClient::V2::SnapshotCreateRequestDataAttributes.new({
      application_id: "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
      device_type: "desktop",
      event_id: "11111111-2222-3333-4444-555555555555",
      is_device_type_selected_by_user: false,
      snapshot_name: "My Snapshot",
      start: 0,
      view_name: "/home",
    }),
    type: DatadogAPIClient::V2::SnapshotUpdateRequestDataType::SNAPSHOTS,
  }),
})
p api_instance.create_replay_heatmap_snapshot(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Create replay heatmap snapshot returns "Created" response

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
	body := datadogV2.SnapshotCreateRequest{
		Data: datadogV2.SnapshotCreateRequestData{
			Attributes: &datadogV2.SnapshotCreateRequestDataAttributes{
				ApplicationId:              "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
				DeviceType:                 "desktop",
				EventId:                    "11111111-2222-3333-4444-555555555555",
				IsDeviceTypeSelectedByUser: false,
				SnapshotName:               "My Snapshot",
				Start:                      0,
				ViewName:                   "/home",
			},
			Type: datadogV2.SNAPSHOTUPDATEREQUESTDATATYPE_SNAPSHOTS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumReplayHeatmapsApi(apiClient)
	resp, r, err := api.CreateReplayHeatmapSnapshot(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumReplayHeatmapsApi.CreateReplayHeatmapSnapshot`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumReplayHeatmapsApi.CreateReplayHeatmapSnapshot`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create replay heatmap snapshot returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayHeatmapsApi;
import com.datadog.api.client.v2.model.Snapshot;
import com.datadog.api.client.v2.model.SnapshotCreateRequest;
import com.datadog.api.client.v2.model.SnapshotCreateRequestData;
import com.datadog.api.client.v2.model.SnapshotCreateRequestDataAttributes;
import com.datadog.api.client.v2.model.SnapshotUpdateRequestDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayHeatmapsApi apiInstance = new RumReplayHeatmapsApi(defaultClient);

    SnapshotCreateRequest body =
        new SnapshotCreateRequest()
            .data(
                new SnapshotCreateRequestData()
                    .attributes(
                        new SnapshotCreateRequestDataAttributes()
                            .applicationId("aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb")
                            .deviceType("desktop")
                            .eventId("11111111-2222-3333-4444-555555555555")
                            .isDeviceTypeSelectedByUser(false)
                            .snapshotName("My Snapshot")
                            .start(0L)
                            .viewName("/home"))
                    .type(SnapshotUpdateRequestDataType.SNAPSHOTS));

    try {
      Snapshot result = apiInstance.createReplayHeatmapSnapshot(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumReplayHeatmapsApi#createReplayHeatmapSnapshot");
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
// Create replay heatmap snapshot returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_heatmaps::RumReplayHeatmapsAPI;
use datadog_api_client::datadogV2::model::SnapshotCreateRequest;
use datadog_api_client::datadogV2::model::SnapshotCreateRequestData;
use datadog_api_client::datadogV2::model::SnapshotCreateRequestDataAttributes;
use datadog_api_client::datadogV2::model::SnapshotUpdateRequestDataType;

#[tokio::main]
async fn main() {
    let body = SnapshotCreateRequest::new(
        SnapshotCreateRequestData::new(SnapshotUpdateRequestDataType::SNAPSHOTS).attributes(
            SnapshotCreateRequestDataAttributes::new(
                "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb".to_string(),
                "desktop".to_string(),
                "11111111-2222-3333-4444-555555555555".to_string(),
                false,
                "My Snapshot".to_string(),
                0,
                "/home".to_string(),
            ),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = RumReplayHeatmapsAPI::with_config(configuration);
    let resp = api.create_replay_heatmap_snapshot(body).await;
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
 * Create replay heatmap snapshot returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayHeatmapsApi(configuration);

const params: v2.RumReplayHeatmapsApiCreateReplayHeatmapSnapshotRequest = {
  body: {
    data: {
      attributes: {
        applicationId: "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
        deviceType: "desktop",
        eventId: "11111111-2222-3333-4444-555555555555",
        isDeviceTypeSelectedByUser: false,
        snapshotName: "My Snapshot",
        start: 0,
        viewName: "/home",
      },
      type: "snapshots",
    },
  },
};

apiInstance
  .createReplayHeatmapSnapshot(params)
  .then((data: v2.Snapshot) => {
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

## List replay heatmap snapshots{% #list-replay-heatmap-snapshots %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/replay/heatmap/snapshots |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/replay/heatmap/snapshots |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/replay/heatmap/snapshots      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/replay/heatmap/snapshots      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/replay/heatmap/snapshots     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/replay/heatmap/snapshots |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/replay/heatmap/snapshots |

### Overview

List heatmap snapshots.

### Arguments

#### Query Strings

| Name                                | Type    | Description                            |
| ----------------------------------- | ------- | -------------------------------------- |
| filter[device_type]                 | string  | Device type to filter snapshots.       |
| filter[view_name] [*required*] | string  | View name to filter snapshots.         |
| page[limit]                         | integer | Maximum number of snapshots to return. |
| filter[application_id]              | string  | Filter by application ID.              |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                           | Type      | Description                                               |
| ------------ | ------------------------------- | --------- | --------------------------------------------------------- |
|              | data [*required*]          | [object]  |
| data         | attributes                      | object    |
| attributes   | application_id                  | string    |
| attributes   | created_at                      | date-time |
| attributes   | created_by                      | string    |
| attributes   | created_by_handle               | string    |
| attributes   | created_by_user_id              | int64     |
| attributes   | device_type                     | string    |
| attributes   | event_id                        | string    |
| attributes   | is_device_type_selected_by_user | boolean   |
| attributes   | modified_at                     | date-time |
| attributes   | org_id                          | int64     |
| attributes   | session_id                      | string    |
| attributes   | snapshot_name                   | string    |
| attributes   | start                           | int64     |
| attributes   | view_id                         | string    |
| attributes   | view_name                       | string    |
| data         | id                              | string    |
| data         | type [*required*]          | enum      | Snapshots resource type. Allowed enum values: `snapshots` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "application_id": "string",
        "created_at": "2019-09-19T10:00:00.000Z",
        "created_by": "string",
        "created_by_handle": "string",
        "created_by_user_id": "integer",
        "device_type": "string",
        "event_id": "string",
        "is_device_type_selected_by_user": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "org_id": "integer",
        "session_id": "string",
        "snapshot_name": "string",
        "start": "integer",
        "view_id": "string",
        "view_name": "string"
      },
      "id": "string",
      "type": "snapshots"
    }
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
                  \# Required query argumentsexport filter[view_name]="/home"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/replay/heatmap/snapshots?filter[view_name]=${filter[view_name]}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
List replay heatmap snapshots returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_heatmaps_api import RumReplayHeatmapsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayHeatmapsApi(api_client)
    response = api_instance.list_replay_heatmap_snapshots(
        filter_view_name="/home",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# List replay heatmap snapshots returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayHeatmapsAPI.new
p api_instance.list_replay_heatmap_snapshots("/home")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// List replay heatmap snapshots returns "OK" response

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
	api := datadogV2.NewRumReplayHeatmapsApi(apiClient)
	resp, r, err := api.ListReplayHeatmapSnapshots(ctx, "/home", *datadogV2.NewListReplayHeatmapSnapshotsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumReplayHeatmapsApi.ListReplayHeatmapSnapshots`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumReplayHeatmapsApi.ListReplayHeatmapSnapshots`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// List replay heatmap snapshots returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayHeatmapsApi;
import com.datadog.api.client.v2.model.SnapshotArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayHeatmapsApi apiInstance = new RumReplayHeatmapsApi(defaultClient);

    try {
      SnapshotArray result = apiInstance.listReplayHeatmapSnapshots("/home");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumReplayHeatmapsApi#listReplayHeatmapSnapshots");
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
// List replay heatmap snapshots returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_heatmaps::ListReplayHeatmapSnapshotsOptionalParams;
use datadog_api_client::datadogV2::api_rum_replay_heatmaps::RumReplayHeatmapsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplayHeatmapsAPI::with_config(configuration);
    let resp = api
        .list_replay_heatmap_snapshots(
            "/home".to_string(),
            ListReplayHeatmapSnapshotsOptionalParams::default(),
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
 * List replay heatmap snapshots returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayHeatmapsApi(configuration);

const params: v2.RumReplayHeatmapsApiListReplayHeatmapSnapshotsRequest = {
  filterViewName: "/home",
};

apiInstance
  .listReplayHeatmapSnapshots(params)
  .then((data: v2.SnapshotArray) => {
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

## Update replay heatmap snapshot{% #update-replay-heatmap-snapshot %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                      |
| ----------------- | --------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/replay/heatmap/snapshots/{snapshot_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/replay/heatmap/snapshots/{snapshot_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/replay/heatmap/snapshots/{snapshot_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/replay/heatmap/snapshots/{snapshot_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/replay/heatmap/snapshots/{snapshot_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/replay/heatmap/snapshots/{snapshot_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/replay/heatmap/snapshots/{snapshot_id} |

### Overview

Update a heatmap snapshot.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                                |
| ----------------------------- | ------ | ------------------------------------------ |
| snapshot_id [*required*] | string | Unique identifier of the heatmap snapshot. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                                             | Type    | Description                                               |
| ------------ | ------------------------------------------------- | ------- | --------------------------------------------------------- |
|              | data [*required*]                            | object  |
| data         | attributes                                        | object  |
| attributes   | event_id [*required*]                        | string  |
| attributes   | is_device_type_selected_by_user [*required*] | boolean |
| attributes   | session_id                                        | string  |
| attributes   | start [*required*]                           | int64   |
| attributes   | view_id                                           | string  |
| data         | id                                                | string  |
| data         | type [*required*]                            | enum    | Snapshots resource type. Allowed enum values: `snapshots` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "event_id": "11111111-2222-3333-4444-555555555555",
      "is_device_type_selected_by_user": false,
      "session_id": "string",
      "start": 0,
      "view_id": "string"
    },
    "id": "00000000-0000-0000-0000-000000000001",
    "type": "snapshots"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                           | Type      | Description                                               |
| ------------ | ------------------------------- | --------- | --------------------------------------------------------- |
|              | data                            | object    |
| data         | attributes                      | object    |
| attributes   | application_id                  | string    |
| attributes   | created_at                      | date-time |
| attributes   | created_by                      | string    |
| attributes   | created_by_handle               | string    |
| attributes   | created_by_user_id              | int64     |
| attributes   | device_type                     | string    |
| attributes   | event_id                        | string    |
| attributes   | is_device_type_selected_by_user | boolean   |
| attributes   | modified_at                     | date-time |
| attributes   | org_id                          | int64     |
| attributes   | session_id                      | string    |
| attributes   | snapshot_name                   | string    |
| attributes   | start                           | int64     |
| attributes   | view_id                         | string    |
| attributes   | view_name                       | string    |
| data         | id                              | string    |
| data         | type [*required*]          | enum      | Snapshots resource type. Allowed enum values: `snapshots` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "application_id": "string",
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": "string",
      "created_by_handle": "string",
      "created_by_user_id": "integer",
      "device_type": "string",
      "event_id": "string",
      "is_device_type_selected_by_user": false,
      "modified_at": "2019-09-19T10:00:00.000Z",
      "org_id": "integer",
      "session_id": "string",
      "snapshot_name": "string",
      "start": "integer",
      "view_id": "string",
      "view_name": "string"
    },
    "id": "string",
    "type": "snapshots"
  }
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
                  \# Path parametersexport snapshot_id="00000000-0000-0000-0000-000000000001"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/replay/heatmap/snapshots/${snapshot_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "event_id": "11111111-2222-3333-4444-555555555555",
      "is_device_type_selected_by_user": false,
      "start": 0
    },
    "type": "snapshots"
  }
}
EOF
                
##### 

```python
"""
Update replay heatmap snapshot returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_heatmaps_api import RumReplayHeatmapsApi
from datadog_api_client.v2.model.snapshot_update_request import SnapshotUpdateRequest
from datadog_api_client.v2.model.snapshot_update_request_data import SnapshotUpdateRequestData
from datadog_api_client.v2.model.snapshot_update_request_data_attributes import SnapshotUpdateRequestDataAttributes
from datadog_api_client.v2.model.snapshot_update_request_data_type import SnapshotUpdateRequestDataType

body = SnapshotUpdateRequest(
    data=SnapshotUpdateRequestData(
        attributes=SnapshotUpdateRequestDataAttributes(
            event_id="11111111-2222-3333-4444-555555555555",
            is_device_type_selected_by_user=False,
            start=0,
        ),
        id="00000000-0000-0000-0000-000000000001",
        type=SnapshotUpdateRequestDataType.SNAPSHOTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayHeatmapsApi(api_client)
    response = api_instance.update_replay_heatmap_snapshot(
        snapshot_id="00000000-0000-0000-0000-000000000001", body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update replay heatmap snapshot returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayHeatmapsAPI.new

body = DatadogAPIClient::V2::SnapshotUpdateRequest.new({
  data: DatadogAPIClient::V2::SnapshotUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::SnapshotUpdateRequestDataAttributes.new({
      event_id: "11111111-2222-3333-4444-555555555555",
      is_device_type_selected_by_user: false,
      start: 0,
    }),
    id: "00000000-0000-0000-0000-000000000001",
    type: DatadogAPIClient::V2::SnapshotUpdateRequestDataType::SNAPSHOTS,
  }),
})
p api_instance.update_replay_heatmap_snapshot("00000000-0000-0000-0000-000000000001", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Update replay heatmap snapshot returns "OK" response

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
	body := datadogV2.SnapshotUpdateRequest{
		Data: datadogV2.SnapshotUpdateRequestData{
			Attributes: &datadogV2.SnapshotUpdateRequestDataAttributes{
				EventId:                    "11111111-2222-3333-4444-555555555555",
				IsDeviceTypeSelectedByUser: false,
				Start:                      0,
			},
			Id:   datadog.PtrString("00000000-0000-0000-0000-000000000001"),
			Type: datadogV2.SNAPSHOTUPDATEREQUESTDATATYPE_SNAPSHOTS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewRumReplayHeatmapsApi(apiClient)
	resp, r, err := api.UpdateReplayHeatmapSnapshot(ctx, "00000000-0000-0000-0000-000000000001", body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumReplayHeatmapsApi.UpdateReplayHeatmapSnapshot`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `RumReplayHeatmapsApi.UpdateReplayHeatmapSnapshot`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update replay heatmap snapshot returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayHeatmapsApi;
import com.datadog.api.client.v2.model.Snapshot;
import com.datadog.api.client.v2.model.SnapshotUpdateRequest;
import com.datadog.api.client.v2.model.SnapshotUpdateRequestData;
import com.datadog.api.client.v2.model.SnapshotUpdateRequestDataAttributes;
import com.datadog.api.client.v2.model.SnapshotUpdateRequestDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayHeatmapsApi apiInstance = new RumReplayHeatmapsApi(defaultClient);

    SnapshotUpdateRequest body =
        new SnapshotUpdateRequest()
            .data(
                new SnapshotUpdateRequestData()
                    .attributes(
                        new SnapshotUpdateRequestDataAttributes()
                            .eventId("11111111-2222-3333-4444-555555555555")
                            .isDeviceTypeSelectedByUser(false)
                            .start(0L))
                    .id("00000000-0000-0000-0000-000000000001")
                    .type(SnapshotUpdateRequestDataType.SNAPSHOTS));

    try {
      Snapshot result =
          apiInstance.updateReplayHeatmapSnapshot("00000000-0000-0000-0000-000000000001", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumReplayHeatmapsApi#updateReplayHeatmapSnapshot");
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
// Update replay heatmap snapshot returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_heatmaps::RumReplayHeatmapsAPI;
use datadog_api_client::datadogV2::model::SnapshotUpdateRequest;
use datadog_api_client::datadogV2::model::SnapshotUpdateRequestData;
use datadog_api_client::datadogV2::model::SnapshotUpdateRequestDataAttributes;
use datadog_api_client::datadogV2::model::SnapshotUpdateRequestDataType;

#[tokio::main]
async fn main() {
    let body = SnapshotUpdateRequest::new(
        SnapshotUpdateRequestData::new(SnapshotUpdateRequestDataType::SNAPSHOTS)
            .attributes(SnapshotUpdateRequestDataAttributes::new(
                "11111111-2222-3333-4444-555555555555".to_string(),
                false,
                0,
            ))
            .id("00000000-0000-0000-0000-000000000001".to_string()),
    );
    let configuration = datadog::Configuration::new();
    let api = RumReplayHeatmapsAPI::with_config(configuration);
    let resp = api
        .update_replay_heatmap_snapshot("00000000-0000-0000-0000-000000000001".to_string(), body)
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
 * Update replay heatmap snapshot returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayHeatmapsApi(configuration);

const params: v2.RumReplayHeatmapsApiUpdateReplayHeatmapSnapshotRequest = {
  body: {
    data: {
      attributes: {
        eventId: "11111111-2222-3333-4444-555555555555",
        isDeviceTypeSelectedByUser: false,
        start: 0,
      },
      id: "00000000-0000-0000-0000-000000000001",
      type: "snapshots",
    },
  },
  snapshotId: "00000000-0000-0000-0000-000000000001",
};

apiInstance
  .updateReplayHeatmapSnapshot(params)
  .then((data: v2.Snapshot) => {
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

## Delete replay heatmap snapshot{% #delete-replay-heatmap-snapshot %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/replay/heatmap/snapshots/{snapshot_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/replay/heatmap/snapshots/{snapshot_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/replay/heatmap/snapshots/{snapshot_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/replay/heatmap/snapshots/{snapshot_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/replay/heatmap/snapshots/{snapshot_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/replay/heatmap/snapshots/{snapshot_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/replay/heatmap/snapshots/{snapshot_id} |

### Overview

Delete a heatmap snapshot.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                                |
| ----------------------------- | ------ | ------------------------------------------ |
| snapshot_id [*required*] | string | Unique identifier of the heatmap snapshot. |

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
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Path parametersexport snapshot_id="00000000-0000-0000-0000-000000000001"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/replay/heatmap/snapshots/${snapshot_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete replay heatmap snapshot returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_heatmaps_api import RumReplayHeatmapsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayHeatmapsApi(api_client)
    api_instance.delete_replay_heatmap_snapshot(
        snapshot_id="00000000-0000-0000-0000-000000000001",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete replay heatmap snapshot returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayHeatmapsAPI.new
api_instance.delete_replay_heatmap_snapshot("00000000-0000-0000-0000-000000000001")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete replay heatmap snapshot returns "No Content" response

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
	api := datadogV2.NewRumReplayHeatmapsApi(apiClient)
	r, err := api.DeleteReplayHeatmapSnapshot(ctx, "00000000-0000-0000-0000-000000000001")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RumReplayHeatmapsApi.DeleteReplayHeatmapSnapshot`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete replay heatmap snapshot returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayHeatmapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayHeatmapsApi apiInstance = new RumReplayHeatmapsApi(defaultClient);

    try {
      apiInstance.deleteReplayHeatmapSnapshot("00000000-0000-0000-0000-000000000001");
    } catch (ApiException e) {
      System.err.println("Exception when calling RumReplayHeatmapsApi#deleteReplayHeatmapSnapshot");
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
// Delete replay heatmap snapshot returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_heatmaps::RumReplayHeatmapsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplayHeatmapsAPI::with_config(configuration);
    let resp = api
        .delete_replay_heatmap_snapshot("00000000-0000-0000-0000-000000000001".to_string())
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
 * Delete replay heatmap snapshot returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayHeatmapsApi(configuration);

const params: v2.RumReplayHeatmapsApiDeleteReplayHeatmapSnapshotRequest = {
  snapshotId: "00000000-0000-0000-0000-000000000001",
};

apiInstance
  .deleteReplayHeatmapSnapshot(params)
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
