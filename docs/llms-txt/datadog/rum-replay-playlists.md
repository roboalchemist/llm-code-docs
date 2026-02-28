# Source: https://docs.datadoghq.com/api/latest/rum-replay-playlists.md

---
title: Rum Replay Playlists
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Rum Replay Playlists
---

# Rum Replay Playlists

Create and manage playlists of RUM replay sessions. Organize, categorize, and share collections of replay sessions for analysis and collaboration.

## Create rum replay playlist{% #create-rum-replay-playlist %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/rum/replay/playlists |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/rum/replay/playlists |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/rum/replay/playlists      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/rum/replay/playlists      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/rum/replay/playlists     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/rum/replay/playlists |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/rum/replay/playlists |

### Overview

Create a playlist.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                    | Type      | Description                                                                   |
| ------------ | ------------------------ | --------- | ----------------------------------------------------------------------------- |
|              | data [*required*]   | object    |
| data         | attributes               | object    |
| attributes   | created_at               | date-time |
| attributes   | created_by               | object    |
| created_by   | handle [*required*] | string    |
| created_by   | icon                     | string    |
| created_by   | id [*required*]     | string    |
| created_by   | name                     | string    |
| created_by   | uuid [*required*]   | string    |
| attributes   | description              | string    |
| attributes   | name [*required*]   | string    |
| attributes   | session_count            | int64     |
| attributes   | updated_at               | date-time |
| data         | id                       | string    |
| data         | type [*required*]   | enum      | Rum replay playlist resource type. Allowed enum values: `rum_replay_playlist` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": {
        "handle": "john.doe@example.com",
        "icon": "string",
        "id": "00000000-0000-0000-0000-000000000001",
        "name": "string",
        "uuid": "00000000-0000-0000-0000-000000000001"
      },
      "description": "string",
      "name": "My Playlist",
      "session_count": "integer",
      "updated_at": "2019-09-19T10:00:00.000Z"
    },
    "id": "string",
    "type": "rum_replay_playlist"
  }
}
```text

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field | Field                    | Type      | Description                                                                   |
| ------------ | ------------------------ | --------- | ----------------------------------------------------------------------------- |
|              | data [*required*]   | object    |
| data         | attributes               | object    |
| attributes   | created_at               | date-time |
| attributes   | created_by               | object    |
| created_by   | handle [*required*] | string    |
| created_by   | icon                     | string    |
| created_by   | id [*required*]     | string    |
| created_by   | name                     | string    |
| created_by   | uuid [*required*]   | string    |
| attributes   | description              | string    |
| attributes   | name [*required*]   | string    |
| attributes   | session_count            | int64     |
| attributes   | updated_at               | date-time |
| data         | id                       | string    |
| data         | type [*required*]   | enum      | Rum replay playlist resource type. Allowed enum values: `rum_replay_playlist` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": {
        "handle": "john.doe@example.com",
        "icon": "string",
        "id": "00000000-0000-0000-0000-000000000001",
        "name": "string",
        "uuid": "00000000-0000-0000-0000-000000000001"
      },
      "description": "string",
      "name": "My Playlist",
      "session_count": "integer",
      "updated_at": "2019-09-19T10:00:00.000Z"
    },
    "id": "string",
    "type": "rum_replay_playlist"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/playlists" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "created_by": {
        "handle": "john.doe@example.com",
        "id": "00000000-0000-0000-0000-000000000001",
        "uuid": "00000000-0000-0000-0000-000000000001"
      },
      "name": "My Playlist"
    },
    "type": "rum_replay_playlist"
  }
}
EOF

#####

```python
"""
Create rum replay playlist returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi
from datadog_api_client.v2.model.playlist import Playlist
from datadog_api_client.v2.model.playlist_data import PlaylistData
from datadog_api_client.v2.model.playlist_data_attributes import PlaylistDataAttributes
from datadog_api_client.v2.model.playlist_data_attributes_created_by import PlaylistDataAttributesCreatedBy
from datadog_api_client.v2.model.playlist_data_type import PlaylistDataType

body = Playlist(
    data=PlaylistData(
        attributes=PlaylistDataAttributes(
            created_by=PlaylistDataAttributesCreatedBy(
                handle="john.doe@example.com",
                id="00000000-0000-0000-0000-000000000001",
                uuid="00000000-0000-0000-0000-000000000001",
            ),
            name="My Playlist",
        ),
        type=PlaylistDataType.RUM_REPLAY_PLAYLIST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    response = api_instance.create_rum_replay_playlist(body=body)

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create rum replay playlist returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayPlaylistsAPI.new

body = DatadogAPIClient::V2::Playlist.new({
  data: DatadogAPIClient::V2::PlaylistData.new({
    attributes: DatadogAPIClient::V2::PlaylistDataAttributes.new({
      created_by: DatadogAPIClient::V2::PlaylistDataAttributesCreatedBy.new({
        handle: "john.doe@example.com",
        id: "00000000-0000-0000-0000-000000000001",
        uuid: "00000000-0000-0000-0000-000000000001",
      }),
      name: "My Playlist",
    }),
    type: DatadogAPIClient::V2::PlaylistDataType::RUM_REPLAY_PLAYLIST,
  }),
})
p api_instance.create_rum_replay_playlist(body)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Create rum replay playlist returns "Created" response

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
    body := datadogV2.Playlist{
        Data: datadogV2.PlaylistData{
            Attributes: &datadogV2.PlaylistDataAttributes{
                CreatedBy: &datadogV2.PlaylistDataAttributesCreatedBy{
                    Handle: "john.doe@example.com",
                    Id:     "00000000-0000-0000-0000-000000000001",
                    Uuid:   "00000000-0000-0000-0000-000000000001",
                },
                Name: "My Playlist",
            },
            Type: datadogV2.PLAYLISTDATATYPE_RUM_REPLAY_PLAYLIST,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRumReplayPlaylistsApi(apiClient)
    resp, r, err := api.CreateRumReplayPlaylist(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayPlaylistsApi.CreateRumReplayPlaylist`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RumReplayPlaylistsApi.CreateRumReplayPlaylist`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create rum replay playlist returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayPlaylistsApi;
import com.datadog.api.client.v2.model.Playlist;
import com.datadog.api.client.v2.model.PlaylistData;
import com.datadog.api.client.v2.model.PlaylistDataAttributes;
import com.datadog.api.client.v2.model.PlaylistDataAttributesCreatedBy;
import com.datadog.api.client.v2.model.PlaylistDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayPlaylistsApi apiInstance = new RumReplayPlaylistsApi(defaultClient);

    Playlist body =
        new Playlist()
            .data(
                new PlaylistData()
                    .attributes(
                        new PlaylistDataAttributes()
                            .createdBy(
                                new PlaylistDataAttributesCreatedBy()
                                    .handle("john.doe@example.com")
                                    .id("00000000-0000-0000-0000-000000000001")
                                    .uuid("00000000-0000-0000-0000-000000000001"))
                            .name("My Playlist"))
                    .type(PlaylistDataType.RUM_REPLAY_PLAYLIST));

    try {
      Playlist result = apiInstance.createRumReplayPlaylist(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumReplayPlaylistsApi#createRumReplayPlaylist");
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
// Create rum replay playlist returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_playlists::RumReplayPlaylistsAPI;
use datadog_api_client::datadogV2::model::Playlist;
use datadog_api_client::datadogV2::model::PlaylistData;
use datadog_api_client::datadogV2::model::PlaylistDataAttributes;
use datadog_api_client::datadogV2::model::PlaylistDataAttributesCreatedBy;
use datadog_api_client::datadogV2::model::PlaylistDataType;

#[tokio::main]
async fn main() {
    let body = Playlist::new(
        PlaylistData::new(PlaylistDataType::RUM_REPLAY_PLAYLIST).attributes(
            PlaylistDataAttributes::new("My Playlist".to_string()).created_by(
                PlaylistDataAttributesCreatedBy::new(
                    "john.doe@example.com".to_string(),
                    "00000000-0000-0000-0000-000000000001".to_string(),
                    "00000000-0000-0000-0000-000000000001".to_string(),
                ),
            ),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = RumReplayPlaylistsAPI::with_config(configuration);
    let resp = api.create_rum_replay_playlist(body).await;
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
 * Create rum replay playlist returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayPlaylistsApi(configuration);

const params: v2.RumReplayPlaylistsApiCreateRumReplayPlaylistRequest = {
  body: {
    data: {
      attributes: {
        createdBy: {
          handle: "john.doe@example.com",
          id: "00000000-0000-0000-0000-000000000001",
          uuid: "00000000-0000-0000-0000-000000000001",
        },
        name: "My Playlist",
      },
      type: "rum_replay_playlist",
    },
  },
};

apiInstance
  .createRumReplayPlaylist(params)
  .then((data: v2.Playlist) => {
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

## List rum replay playlists{% #list-rum-replay-playlists %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/replay/playlists |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/replay/playlists |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/replay/playlists      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/replay/playlists      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/replay/playlists     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/replay/playlists |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/replay/playlists |

### Overview

List playlists.

### Arguments

#### Query Strings

| Name                    | Type    | Description                                                |
| ----------------------- | ------- | ---------------------------------------------------------- |
| filter[created_by_uuid] | string  | Filter playlists by the UUID of the user who created them. |
| filter[query]           | string  | Search query to filter playlists by name.                  |
| page[number]            | integer | Page number for pagination (0-indexed).                    |
| page[size]              | integer | Number of items per page.                                  |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                    | Type      | Description                                                                   |
| ------------ | ------------------------ | --------- | ----------------------------------------------------------------------------- |
|              | data [*required*]   | [object]  |
| data         | attributes               | object    |
| attributes   | created_at               | date-time |
| attributes   | created_by               | object    |
| created_by   | handle [*required*] | string    |
| created_by   | icon                     | string    |
| created_by   | id [*required*]     | string    |
| created_by   | name                     | string    |
| created_by   | uuid [*required*]   | string    |
| attributes   | description              | string    |
| attributes   | name [*required*]   | string    |
| attributes   | session_count            | int64     |
| attributes   | updated_at               | date-time |
| data         | id                       | string    |
| data         | type [*required*]   | enum      | Rum replay playlist resource type. Allowed enum values: `rum_replay_playlist` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "created_by": {
          "handle": "john.doe@example.com",
          "icon": "string",
          "id": "00000000-0000-0000-0000-000000000001",
          "name": "string",
          "uuid": "00000000-0000-0000-0000-000000000001"
        },
        "description": "string",
        "name": "My Playlist",
        "session_count": "integer",
        "updated_at": "2019-09-19T10:00:00.000Z"
      },
      "id": "string",
      "type": "rum_replay_playlist"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/playlists" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List rum replay playlists returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    response = api_instance.list_rum_replay_playlists()

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List rum replay playlists returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayPlaylistsAPI.new
p api_instance.list_rum_replay_playlists()
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List rum replay playlists returns "OK" response

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
    api := datadogV2.NewRumReplayPlaylistsApi(apiClient)
    resp, r, err := api.ListRumReplayPlaylists(ctx, *datadogV2.NewListRumReplayPlaylistsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayPlaylistsApi.ListRumReplayPlaylists`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RumReplayPlaylistsApi.ListRumReplayPlaylists`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List rum replay playlists returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayPlaylistsApi;
import com.datadog.api.client.v2.model.PlaylistArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayPlaylistsApi apiInstance = new RumReplayPlaylistsApi(defaultClient);

    try {
      PlaylistArray result = apiInstance.listRumReplayPlaylists();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumReplayPlaylistsApi#listRumReplayPlaylists");
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
// List rum replay playlists returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_playlists::ListRumReplayPlaylistsOptionalParams;
use datadog_api_client::datadogV2::api_rum_replay_playlists::RumReplayPlaylistsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplayPlaylistsAPI::with_config(configuration);
    let resp = api
        .list_rum_replay_playlists(ListRumReplayPlaylistsOptionalParams::default())
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
 * List rum replay playlists returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayPlaylistsApi(configuration);

apiInstance
  .listRumReplayPlaylists()
  .then((data: v2.PlaylistArray) => {
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

## List rum replay playlist sessions{% #list-rum-replay-playlist-sessions %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/replay/playlists/{playlist_id}/sessions      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/replay/playlists/{playlist_id}/sessions      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions |

### Overview

List sessions in a playlist.

### Arguments

#### Path Parameters

| Name                          | Type    | Description                        |
| ----------------------------- | ------- | ---------------------------------- |
| playlist_id [*required*] | integer | Unique identifier of the playlist. |

#### Query Strings

| Name         | Type    | Description                             |
| ------------ | ------- | --------------------------------------- |
| page[number] | integer | Page number for pagination (0-indexed). |
| page[size]   | integer | Number of items per page.               |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                 |
| ------------ | ---------------------- | -------- | --------------------------------------------------------------------------- |
|              | data [*required*] | [object] |
| data         | attributes             | object   |
| attributes   | session_event          | object   |
| attributes   | track                  | string   |
| data         | id                     | string   |
| data         | type [*required*] | enum     | Rum replay session resource type. Allowed enum values: `rum_replay_session` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
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
                  \# Path parametersexport playlist_id="1.234567e+06"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/${playlist_id}/sessions" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List rum replay playlist sessions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    response = api_instance.list_rum_replay_playlist_sessions(
        playlist_id=1234567,
    )

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List rum replay playlist sessions returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayPlaylistsAPI.new
p api_instance.list_rum_replay_playlist_sessions(1234567)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List rum replay playlist sessions returns "OK" response

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
    api := datadogV2.NewRumReplayPlaylistsApi(apiClient)
    resp, r, err := api.ListRumReplayPlaylistSessions(ctx, 1234567, *datadogV2.NewListRumReplayPlaylistSessionsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayPlaylistsApi.ListRumReplayPlaylistSessions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RumReplayPlaylistsApi.ListRumReplayPlaylistSessions`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List rum replay playlist sessions returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayPlaylistsApi;
import com.datadog.api.client.v2.model.PlaylistsSessionArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayPlaylistsApi apiInstance = new RumReplayPlaylistsApi(defaultClient);

    try {
      PlaylistsSessionArray result = apiInstance.listRumReplayPlaylistSessions(1234567);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling RumReplayPlaylistsApi#listRumReplayPlaylistSessions");
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
// List rum replay playlist sessions returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_playlists::ListRumReplayPlaylistSessionsOptionalParams;
use datadog_api_client::datadogV2::api_rum_replay_playlists::RumReplayPlaylistsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplayPlaylistsAPI::with_config(configuration);
    let resp = api
        .list_rum_replay_playlist_sessions(
            1234567,
            ListRumReplayPlaylistSessionsOptionalParams::default(),
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
 * List rum replay playlist sessions returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayPlaylistsApi(configuration);

const params: v2.RumReplayPlaylistsApiListRumReplayPlaylistSessionsRequest = {
  playlistId: 1234567,
};

apiInstance
  .listRumReplayPlaylistSessions(params)
  .then((data: v2.PlaylistsSessionArray) => {
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

## Bulk remove rum replay playlist sessions{% #bulk-remove-rum-replay-playlist-sessions %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                            |
| ----------------- | --------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/rum/replay/playlists/{playlist_id}/sessions      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/rum/replay/playlists/{playlist_id}/sessions      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions |

### Overview

Remove sessions from a playlist.

### Arguments

#### Path Parameters

| Name                          | Type    | Description                        |
| ----------------------------- | ------- | ---------------------------------- |
| playlist_id [*required*] | integer | Unique identifier of the playlist. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                 |
| ------------ | ---------------------- | -------- | --------------------------------------------------------------------------- |
|              | data [*required*] | [object] |
| data         | id                     | string   |
| data         | type [*required*] | enum     | Rum replay session resource type. Allowed enum values: `rum_replay_session` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "id": "00000000-0000-0000-0000-000000000001",
      "type": "rum_replay_session"
    }
  ]
}
```text

{% /tab %}

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
                  \# Path parametersexport playlist_id="1.234567e+06"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/${playlist_id}/sessions" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": [
    {
      "type": "rum_replay_session"
    }
  ]
}
EOF

#####

```python
"""
Bulk remove rum replay playlist sessions returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi
from datadog_api_client.v2.model.session_id_array import SessionIdArray
from datadog_api_client.v2.model.session_id_data import SessionIdData
from datadog_api_client.v2.model.viewership_history_session_data_type import ViewershipHistorySessionDataType

body = SessionIdArray(
    data=[
        SessionIdData(
            id="00000000-0000-0000-0000-000000000001",
            type=ViewershipHistorySessionDataType.RUM_REPLAY_SESSION,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    api_instance.bulk_remove_rum_replay_playlist_sessions(playlist_id=1234567, body=body)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Bulk remove rum replay playlist sessions returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayPlaylistsAPI.new

body = DatadogAPIClient::V2::SessionIdArray.new({
  data: [
    DatadogAPIClient::V2::SessionIdData.new({
      id: "00000000-0000-0000-0000-000000000001",
      type: DatadogAPIClient::V2::ViewershipHistorySessionDataType::RUM_REPLAY_SESSION,
    }),
  ],
})
api_instance.bulk_remove_rum_replay_playlist_sessions(1234567, body)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Bulk remove rum replay playlist sessions returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.SessionIdArray{
        Data: []datadogV2.SessionIdData{
            {
                Id:   datadog.PtrString("00000000-0000-0000-0000-000000000001"),
                Type: datadogV2.VIEWERSHIPHISTORYSESSIONDATATYPE_RUM_REPLAY_SESSION,
            },
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRumReplayPlaylistsApi(apiClient)
    r, err := api.BulkRemoveRumReplayPlaylistSessions(ctx, 1234567, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayPlaylistsApi.BulkRemoveRumReplayPlaylistSessions`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Bulk remove rum replay playlist sessions returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayPlaylistsApi;
import com.datadog.api.client.v2.model.SessionIdArray;
import com.datadog.api.client.v2.model.SessionIdData;
import com.datadog.api.client.v2.model.ViewershipHistorySessionDataType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayPlaylistsApi apiInstance = new RumReplayPlaylistsApi(defaultClient);

    SessionIdArray body =
        new SessionIdArray()
            .data(
                Collections.singletonList(
                    new SessionIdData()
                        .id("00000000-0000-0000-0000-000000000001")
                        .type(ViewershipHistorySessionDataType.RUM_REPLAY_SESSION)));

    try {
      apiInstance.bulkRemoveRumReplayPlaylistSessions(1234567, body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling RumReplayPlaylistsApi#bulkRemoveRumReplayPlaylistSessions");
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
// Bulk remove rum replay playlist sessions returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_playlists::RumReplayPlaylistsAPI;
use datadog_api_client::datadogV2::model::SessionIdArray;
use datadog_api_client::datadogV2::model::SessionIdData;
use datadog_api_client::datadogV2::model::ViewershipHistorySessionDataType;

#[tokio::main]
async fn main() {
    let body = SessionIdArray::new(vec![SessionIdData::new(
        ViewershipHistorySessionDataType::RUM_REPLAY_SESSION,
    )
    .id("00000000-0000-0000-0000-000000000001".to_string())]);
    let configuration = datadog::Configuration::new();
    let api = RumReplayPlaylistsAPI::with_config(configuration);
    let resp = api
        .bulk_remove_rum_replay_playlist_sessions(1234567, body)
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
 * Bulk remove rum replay playlist sessions returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayPlaylistsApi(configuration);

const params: v2.RumReplayPlaylistsApiBulkRemoveRumReplayPlaylistSessionsRequest =
  {
    body: {
      data: [
        {
          id: "00000000-0000-0000-0000-000000000001",
          type: "rum_replay_session",
        },
      ],
    },
    playlistId: 1234567,
  };

apiInstance
  .bulkRemoveRumReplayPlaylistSessions(params)
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

## Get rum replay playlist{% #get-rum-replay-playlist %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/rum/replay/playlists/{playlist_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/rum/replay/playlists/{playlist_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |

### Overview

Get a playlist.

### Arguments

#### Path Parameters

| Name                          | Type    | Description                        |
| ----------------------------- | ------- | ---------------------------------- |
| playlist_id [*required*] | integer | Unique identifier of the playlist. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                    | Type      | Description                                                                   |
| ------------ | ------------------------ | --------- | ----------------------------------------------------------------------------- |
|              | data [*required*]   | object    |
| data         | attributes               | object    |
| attributes   | created_at               | date-time |
| attributes   | created_by               | object    |
| created_by   | handle [*required*] | string    |
| created_by   | icon                     | string    |
| created_by   | id [*required*]     | string    |
| created_by   | name                     | string    |
| created_by   | uuid [*required*]   | string    |
| attributes   | description              | string    |
| attributes   | name [*required*]   | string    |
| attributes   | session_count            | int64     |
| attributes   | updated_at               | date-time |
| data         | id                       | string    |
| data         | type [*required*]   | enum      | Rum replay playlist resource type. Allowed enum values: `rum_replay_playlist` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": {
        "handle": "john.doe@example.com",
        "icon": "string",
        "id": "00000000-0000-0000-0000-000000000001",
        "name": "string",
        "uuid": "00000000-0000-0000-0000-000000000001"
      },
      "description": "string",
      "name": "My Playlist",
      "session_count": "integer",
      "updated_at": "2019-09-19T10:00:00.000Z"
    },
    "id": "string",
    "type": "rum_replay_playlist"
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
                  \# Path parametersexport playlist_id="1.234567e+06"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/${playlist_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get rum replay playlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    response = api_instance.get_rum_replay_playlist(
        playlist_id=1234567,
    )

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get rum replay playlist returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayPlaylistsAPI.new
p api_instance.get_rum_replay_playlist(1234567)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get rum replay playlist returns "OK" response

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
    api := datadogV2.NewRumReplayPlaylistsApi(apiClient)
    resp, r, err := api.GetRumReplayPlaylist(ctx, 1234567)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayPlaylistsApi.GetRumReplayPlaylist`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RumReplayPlaylistsApi.GetRumReplayPlaylist`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get rum replay playlist returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayPlaylistsApi;
import com.datadog.api.client.v2.model.Playlist;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayPlaylistsApi apiInstance = new RumReplayPlaylistsApi(defaultClient);

    try {
      Playlist result = apiInstance.getRumReplayPlaylist(1234567);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumReplayPlaylistsApi#getRumReplayPlaylist");
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
// Get rum replay playlist returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_playlists::RumReplayPlaylistsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplayPlaylistsAPI::with_config(configuration);
    let resp = api.get_rum_replay_playlist(1234567).await;
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
 * Get rum replay playlist returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayPlaylistsApi(configuration);

const params: v2.RumReplayPlaylistsApiGetRumReplayPlaylistRequest = {
  playlistId: 1234567,
};

apiInstance
  .getRumReplayPlaylist(params)
  .then((data: v2.Playlist) => {
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

## Update rum replay playlist{% #update-rum-replay-playlist %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                |
| ----------------- | --------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/rum/replay/playlists/{playlist_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/rum/replay/playlists/{playlist_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |

### Overview

Update a playlist.

### Arguments

#### Path Parameters

| Name                          | Type    | Description                        |
| ----------------------------- | ------- | ---------------------------------- |
| playlist_id [*required*] | integer | Unique identifier of the playlist. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                    | Type      | Description                                                                   |
| ------------ | ------------------------ | --------- | ----------------------------------------------------------------------------- |
|              | data [*required*]   | object    |
| data         | attributes               | object    |
| attributes   | created_at               | date-time |
| attributes   | created_by               | object    |
| created_by   | handle [*required*] | string    |
| created_by   | icon                     | string    |
| created_by   | id [*required*]     | string    |
| created_by   | name                     | string    |
| created_by   | uuid [*required*]   | string    |
| attributes   | description              | string    |
| attributes   | name [*required*]   | string    |
| attributes   | session_count            | int64     |
| attributes   | updated_at               | date-time |
| data         | id                       | string    |
| data         | type [*required*]   | enum      | Rum replay playlist resource type. Allowed enum values: `rum_replay_playlist` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": {
        "handle": "john.doe@example.com",
        "icon": "string",
        "id": "00000000-0000-0000-0000-000000000001",
        "name": "string",
        "uuid": "00000000-0000-0000-0000-000000000001"
      },
      "description": "string",
      "name": "My Playlist",
      "session_count": "integer",
      "updated_at": "2019-09-19T10:00:00.000Z"
    },
    "id": "string",
    "type": "rum_replay_playlist"
  }
}
```text

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                    | Type      | Description                                                                   |
| ------------ | ------------------------ | --------- | ----------------------------------------------------------------------------- |
|              | data [*required*]   | object    |
| data         | attributes               | object    |
| attributes   | created_at               | date-time |
| attributes   | created_by               | object    |
| created_by   | handle [*required*] | string    |
| created_by   | icon                     | string    |
| created_by   | id [*required*]     | string    |
| created_by   | name                     | string    |
| created_by   | uuid [*required*]   | string    |
| attributes   | description              | string    |
| attributes   | name [*required*]   | string    |
| attributes   | session_count            | int64     |
| attributes   | updated_at               | date-time |
| data         | id                       | string    |
| data         | type [*required*]   | enum      | Rum replay playlist resource type. Allowed enum values: `rum_replay_playlist` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2019-09-19T10:00:00.000Z",
      "created_by": {
        "handle": "john.doe@example.com",
        "icon": "string",
        "id": "00000000-0000-0000-0000-000000000001",
        "name": "string",
        "uuid": "00000000-0000-0000-0000-000000000001"
      },
      "description": "string",
      "name": "My Playlist",
      "session_count": "integer",
      "updated_at": "2019-09-19T10:00:00.000Z"
    },
    "id": "string",
    "type": "rum_replay_playlist"
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
                  \# Path parametersexport playlist_id="1.234567e+06"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/${playlist_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "created_by": {
        "handle": "john.doe@example.com",
        "id": "00000000-0000-0000-0000-000000000001",
        "uuid": "00000000-0000-0000-0000-000000000001"
      },
      "name": "My Playlist"
    },
    "type": "rum_replay_playlist"
  }
}
EOF

#####

```python
"""
Update rum replay playlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi
from datadog_api_client.v2.model.playlist import Playlist
from datadog_api_client.v2.model.playlist_data import PlaylistData
from datadog_api_client.v2.model.playlist_data_attributes import PlaylistDataAttributes
from datadog_api_client.v2.model.playlist_data_attributes_created_by import PlaylistDataAttributesCreatedBy
from datadog_api_client.v2.model.playlist_data_type import PlaylistDataType

body = Playlist(
    data=PlaylistData(
        attributes=PlaylistDataAttributes(
            created_by=PlaylistDataAttributesCreatedBy(
                handle="john.doe@example.com",
                id="00000000-0000-0000-0000-000000000001",
                uuid="00000000-0000-0000-0000-000000000001",
            ),
            name="My Playlist",
        ),
        type=PlaylistDataType.RUM_REPLAY_PLAYLIST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    response = api_instance.update_rum_replay_playlist(playlist_id=1234567, body=body)

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update rum replay playlist returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayPlaylistsAPI.new

body = DatadogAPIClient::V2::Playlist.new({
  data: DatadogAPIClient::V2::PlaylistData.new({
    attributes: DatadogAPIClient::V2::PlaylistDataAttributes.new({
      created_by: DatadogAPIClient::V2::PlaylistDataAttributesCreatedBy.new({
        handle: "john.doe@example.com",
        id: "00000000-0000-0000-0000-000000000001",
        uuid: "00000000-0000-0000-0000-000000000001",
      }),
      name: "My Playlist",
    }),
    type: DatadogAPIClient::V2::PlaylistDataType::RUM_REPLAY_PLAYLIST,
  }),
})
p api_instance.update_rum_replay_playlist(1234567, body)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Update rum replay playlist returns "OK" response

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
    body := datadogV2.Playlist{
        Data: datadogV2.PlaylistData{
            Attributes: &datadogV2.PlaylistDataAttributes{
                CreatedBy: &datadogV2.PlaylistDataAttributesCreatedBy{
                    Handle: "john.doe@example.com",
                    Id:     "00000000-0000-0000-0000-000000000001",
                    Uuid:   "00000000-0000-0000-0000-000000000001",
                },
                Name: "My Playlist",
            },
            Type: datadogV2.PLAYLISTDATATYPE_RUM_REPLAY_PLAYLIST,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewRumReplayPlaylistsApi(apiClient)
    resp, r, err := api.UpdateRumReplayPlaylist(ctx, 1234567, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayPlaylistsApi.UpdateRumReplayPlaylist`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RumReplayPlaylistsApi.UpdateRumReplayPlaylist`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update rum replay playlist returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayPlaylistsApi;
import com.datadog.api.client.v2.model.Playlist;
import com.datadog.api.client.v2.model.PlaylistData;
import com.datadog.api.client.v2.model.PlaylistDataAttributes;
import com.datadog.api.client.v2.model.PlaylistDataAttributesCreatedBy;
import com.datadog.api.client.v2.model.PlaylistDataType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayPlaylistsApi apiInstance = new RumReplayPlaylistsApi(defaultClient);

    Playlist body =
        new Playlist()
            .data(
                new PlaylistData()
                    .attributes(
                        new PlaylistDataAttributes()
                            .createdBy(
                                new PlaylistDataAttributesCreatedBy()
                                    .handle("john.doe@example.com")
                                    .id("00000000-0000-0000-0000-000000000001")
                                    .uuid("00000000-0000-0000-0000-000000000001"))
                            .name("My Playlist"))
                    .type(PlaylistDataType.RUM_REPLAY_PLAYLIST));

    try {
      Playlist result = apiInstance.updateRumReplayPlaylist(1234567, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumReplayPlaylistsApi#updateRumReplayPlaylist");
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
// Update rum replay playlist returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_playlists::RumReplayPlaylistsAPI;
use datadog_api_client::datadogV2::model::Playlist;
use datadog_api_client::datadogV2::model::PlaylistData;
use datadog_api_client::datadogV2::model::PlaylistDataAttributes;
use datadog_api_client::datadogV2::model::PlaylistDataAttributesCreatedBy;
use datadog_api_client::datadogV2::model::PlaylistDataType;

#[tokio::main]
async fn main() {
    let body = Playlist::new(
        PlaylistData::new(PlaylistDataType::RUM_REPLAY_PLAYLIST).attributes(
            PlaylistDataAttributes::new("My Playlist".to_string()).created_by(
                PlaylistDataAttributesCreatedBy::new(
                    "john.doe@example.com".to_string(),
                    "00000000-0000-0000-0000-000000000001".to_string(),
                    "00000000-0000-0000-0000-000000000001".to_string(),
                ),
            ),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = RumReplayPlaylistsAPI::with_config(configuration);
    let resp = api.update_rum_replay_playlist(1234567, body).await;
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
 * Update rum replay playlist returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayPlaylistsApi(configuration);

const params: v2.RumReplayPlaylistsApiUpdateRumReplayPlaylistRequest = {
  body: {
    data: {
      attributes: {
        createdBy: {
          handle: "john.doe@example.com",
          id: "00000000-0000-0000-0000-000000000001",
          uuid: "00000000-0000-0000-0000-000000000001",
        },
        name: "My Playlist",
      },
      type: "rum_replay_playlist",
    },
  },
  playlistId: 1234567,
};

apiInstance
  .updateRumReplayPlaylist(params)
  .then((data: v2.Playlist) => {
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

## Delete rum replay playlist{% #delete-rum-replay-playlist %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                   |
| ----------------- | ------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/rum/replay/playlists/{playlist_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/rum/replay/playlists/{playlist_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id} |

### Overview

Delete a playlist.

### Arguments

#### Path Parameters

| Name                          | Type    | Description                        |
| ----------------------------- | ------- | ---------------------------------- |
| playlist_id [*required*] | integer | Unique identifier of the playlist. |

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
                  \# Path parametersexport playlist_id="1.234567e+06"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/${playlist_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete rum replay playlist returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    api_instance.delete_rum_replay_playlist(
        playlist_id=1234567,
    )
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete rum replay playlist returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayPlaylistsAPI.new
api_instance.delete_rum_replay_playlist(1234567)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete rum replay playlist returns "No Content" response

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
    api := datadogV2.NewRumReplayPlaylistsApi(apiClient)
    r, err := api.DeleteRumReplayPlaylist(ctx, 1234567)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayPlaylistsApi.DeleteRumReplayPlaylist`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete rum replay playlist returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayPlaylistsApi apiInstance = new RumReplayPlaylistsApi(defaultClient);

    try {
      apiInstance.deleteRumReplayPlaylist(1234567);
    } catch (ApiException e) {
      System.err.println("Exception when calling RumReplayPlaylistsApi#deleteRumReplayPlaylist");
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
// Delete rum replay playlist returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_playlists::RumReplayPlaylistsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplayPlaylistsAPI::with_config(configuration);
    let resp = api.delete_rum_replay_playlist(1234567).await;
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
 * Delete rum replay playlist returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayPlaylistsApi(configuration);

const params: v2.RumReplayPlaylistsApiDeleteRumReplayPlaylistRequest = {
  playlistId: 1234567,
};

apiInstance
  .deleteRumReplayPlaylist(params)
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

## Add rum replay session to playlist{% #add-rum-replay-session-to-playlist %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id} |

### Overview

Add a session to a playlist.

### Arguments

#### Path Parameters

| Name                          | Type    | Description                        |
| ----------------------------- | ------- | ---------------------------------- |
| playlist_id [*required*] | integer | Unique identifier of the playlist. |
| session_id [*required*]  | string  | Unique identifier of the session.  |

#### Query Strings

| Name                 | Type    | Description                                                                      |
| -------------------- | ------- | -------------------------------------------------------------------------------- |
| data_source          | string  | Data source type. Valid values: 'rum' or 'product_analytics'. Defaults to 'rum'. |
| ts [*required*] | integer | Server-side timestamp in milliseconds.                                           |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                                                 |
| ------------ | ---------------------- | ------ | --------------------------------------------------------------------------- |
|              | data [*required*] | object |
| data         | attributes             | object |
| attributes   | session_event          | object |
| attributes   | track                  | string |
| data         | id                     | string |
| data         | type [*required*] | enum   | Rum replay session resource type. Allowed enum values: `rum_replay_session` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "session_event": {},
      "track": "string"
    },
    "id": "string",
    "type": "rum_replay_session"
  }
}
```text

{% /tab %}

{% /tab %}

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                                                 |
| ------------ | ---------------------- | ------ | --------------------------------------------------------------------------- |
|              | data [*required*] | object |
| data         | attributes             | object |
| attributes   | session_event          | object |
| attributes   | track                  | string |
| data         | id                     | string |
| data         | type [*required*] | enum   | Rum replay session resource type. Allowed enum values: `rum_replay_session` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "session_event": {},
      "track": "string"
    },
    "id": "string",
    "type": "rum_replay_session"
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
                  \# Path parametersexport playlist_id="1.234567e+06"export session_id="00000000-0000-0000-0000-000000000001"\# Required query argumentsexport ts="1.7040672e+12"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/${playlist_id}/sessions/${session_id}?ts=${ts}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Add rum replay session to playlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    response = api_instance.add_rum_replay_session_to_playlist(
        ts=1704067200000,
        playlist_id=1234567,
        session_id="00000000-0000-0000-0000-000000000001",
    )

    print(response)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Add rum replay session to playlist returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayPlaylistsAPI.new
p api_instance.add_rum_replay_session_to_playlist(1704067200000, 1234567, "00000000-0000-0000-0000-000000000001")
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Add rum replay session to playlist returns "OK" response

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
    api := datadogV2.NewRumReplayPlaylistsApi(apiClient)
    resp, r, err := api.AddRumReplaySessionToPlaylist(ctx, 1704067200000, 1234567, "00000000-0000-0000-0000-000000000001", *datadogV2.NewAddRumReplaySessionToPlaylistOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayPlaylistsApi.AddRumReplaySessionToPlaylist`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `RumReplayPlaylistsApi.AddRumReplaySessionToPlaylist`:\n%s\n", responseContent)
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Add rum replay session to playlist returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayPlaylistsApi;
import com.datadog.api.client.v2.model.PlaylistsSession;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayPlaylistsApi apiInstance = new RumReplayPlaylistsApi(defaultClient);

    try {
      PlaylistsSession result =
          apiInstance.addRumReplaySessionToPlaylist(
              1704067200000L, 1234567, "00000000-0000-0000-0000-000000000001");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling RumReplayPlaylistsApi#addRumReplaySessionToPlaylist");
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
// Add rum replay session to playlist returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_playlists::AddRumReplaySessionToPlaylistOptionalParams;
use datadog_api_client::datadogV2::api_rum_replay_playlists::RumReplayPlaylistsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplayPlaylistsAPI::with_config(configuration);
    let resp = api
        .add_rum_replay_session_to_playlist(
            1704067200000,
            1234567,
            "00000000-0000-0000-0000-000000000001".to_string(),
            AddRumReplaySessionToPlaylistOptionalParams::default(),
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
 * Add rum replay session to playlist returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayPlaylistsApi(configuration);

const params: v2.RumReplayPlaylistsApiAddRumReplaySessionToPlaylistRequest = {
  ts: 1704067200000,
  playlistId: 1234567,
  sessionId: "00000000-0000-0000-0000-000000000001",
};

apiInstance
  .addRumReplaySessionToPlaylist(params)
  .then((data: v2.PlaylistsSession) => {
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

## Remove rum replay session from playlist{% #remove-rum-replay-session-from-playlist %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id} |

### Overview

Remove a session from a playlist.

### Arguments

#### Path Parameters

| Name                          | Type    | Description                        |
| ----------------------------- | ------- | ---------------------------------- |
| playlist_id [*required*] | integer | Unique identifier of the playlist. |
| session_id [*required*]  | string  | Unique identifier of the session.  |

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
                  \# Path parametersexport playlist_id="1.234567e+06"export session_id="00000000-0000-0000-0000-000000000001"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/rum/replay/playlists/${playlist_id}/sessions/${session_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Remove rum replay session from playlist returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    api_instance.remove_rum_replay_session_from_playlist(
        playlist_id=1234567,
        session_id="00000000-0000-0000-0000-000000000001",
    )
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Remove rum replay session from playlist returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::RumReplayPlaylistsAPI.new
api_instance.remove_rum_replay_session_from_playlist(1234567, "00000000-0000-0000-0000-000000000001")
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Remove rum replay session from playlist returns "No Content" response

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
    api := datadogV2.NewRumReplayPlaylistsApi(apiClient)
    r, err := api.RemoveRumReplaySessionFromPlaylist(ctx, 1234567, "00000000-0000-0000-0000-000000000001")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `RumReplayPlaylistsApi.RemoveRumReplaySessionFromPlaylist`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Remove rum replay session from playlist returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.RumReplayPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    RumReplayPlaylistsApi apiInstance = new RumReplayPlaylistsApi(defaultClient);

    try {
      apiInstance.removeRumReplaySessionFromPlaylist(
          1234567, "00000000-0000-0000-0000-000000000001");
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling RumReplayPlaylistsApi#removeRumReplaySessionFromPlaylist");
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
// Remove rum replay session from playlist returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_rum_replay_playlists::RumReplayPlaylistsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = RumReplayPlaylistsAPI::with_config(configuration);
    let resp = api
        .remove_rum_replay_session_from_playlist(
            1234567,
            "00000000-0000-0000-0000-000000000001".to_string(),
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
 * Remove rum replay session from playlist returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.RumReplayPlaylistsApi(configuration);

const params: v2.RumReplayPlaylistsApiRemoveRumReplaySessionFromPlaylistRequest =
  {
    playlistId: 1234567,
    sessionId: "00000000-0000-0000-0000-000000000001",
  };

apiInstance
  .removeRumReplaySessionFromPlaylist(params)
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
