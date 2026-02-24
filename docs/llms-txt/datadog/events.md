# Source: https://docs.datadoghq.com/api/latest/events.md

---
title: Events
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Events
---

# Events

The Event Management API allows you to programmatically post events to the Events Explorer and fetch events from the Events Explorer. See the [Event Management page](https://docs.datadoghq.com/service_management/events/) for more information.

**Update to Datadog monitor events `aggregation_key` starting March 1, 2025:** The Datadog monitor events `aggregation_key` is unique to each Monitor ID. Starting March 1st, this key will also include Monitor Group, making it unique per *Monitor ID and Monitor Group*. If you're using monitor events `aggregation_key` in dashboard queries or the Event API, you must migrate to use `@monitor.id`. Reach out to [support](https://www.datadoghq.com/support/) if you have any question.

## Get a list of events{% #get-a-list-of-events %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                    |
| ----------------- | ----------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/events |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/events |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/events      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/events      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/events     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/events |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/events |

### Overview



The event stream can be queried and filtered by time, priority, sources and tags.

**Notes**:

- If the event you're querying contains markdown formatting of any kind, you may see characters such as `%`,`\`,`n` in your output.

- This endpoint returns a maximum of `1000` most recent results. To return additional results, identify the last timestamp of the last result and set that as the `end` query time to paginate the results. You can also use the page parameter to specify which set of `1000` results to return.
This endpoint requires the `events_read` permission.
OAuth apps require the `events_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#events) to access this endpoint.



### Arguments

#### Query Strings

| Name                    | Type    | Description                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| start [*required*] | integer | POSIX timestamp.                                                                                                                                                                                                                                                                                                                                                   |
| end [*required*]   | integer | POSIX timestamp.                                                                                                                                                                                                                                                                                                                                                   |
| priority                | enum    | Priority of your events, either `low` or `normal`.Allowed enum values: `normal, low`                                                                                                                                                                                                                                                                               |
| sources                 | string  | A comma separated string of sources.                                                                                                                                                                                                                                                                                                                               |
| tags                    | string  | A comma separated list indicating what tags, if any, should be used to filter the list of events.                                                                                                                                                                                                                                                                  |
| unaggregated            | boolean | Set unaggregated to `true` to return all events within the specified [`start`,`end`] timeframe. Otherwise if an event is aggregated to a parent event with a timestamp outside of the timeframe, it won't be available in the output. Aggregated events with `is_aggregate=true` in the response will still be returned unless exclude_aggregate is set to `true.` |
| exclude_aggregate       | boolean | Set `exclude_aggregate` to `true` to only return unaggregated events where `is_aggregate=false` in the response. If the `exclude_aggregate` parameter is set to `true`, then the unaggregated parameter is ignored and will be `true` by default.                                                                                                                  |
| page                    | integer | By default 1000 results are returned per request. Set page to the number of the page to return with `0` being the first page. The page parameter can only be used when either unaggregated or exclude_aggregate is set to `true.`                                                                                                                                  |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An event list response.

| Parent field | Field            | Type     | Description                                                                                                                                                                                                                                                                 |
| ------------ | ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | events           | [object] | An array of events.                                                                                                                                                                                                                                                         |
| events       | alert_type       | enum     | If an alert event is enabled, set its type. For example, `error`, `warning`, `info`, `success`, `user_update`, `recommendation`, and `snapshot`. Allowed enum values: `error,warning,info,success,user_update,recommendation,snapshot`                                      |
| events       | date_happened    | int64    | POSIX timestamp of the event. Must be sent as an integer (that is no quotes). Limited to events up to 18 hours in the past and two hours in the future.                                                                                                                     |
| events       | device_name      | string   | A device name.                                                                                                                                                                                                                                                              |
| events       | host             | string   | Host name to associate with the event. Any tags associated with the host are also applied to this event.                                                                                                                                                                    |
| events       | id               | int64    | Integer ID of the event.                                                                                                                                                                                                                                                    |
| events       | id_str           | string   | Handling IDs as large 64-bit numbers can cause loss of accuracy issues with some programming languages. Instead, use the string representation of the Event ID to avoid losing accuracy.                                                                                    |
| events       | payload          | string   | Payload of the event.                                                                                                                                                                                                                                                       |
| events       | priority         | enum     | The priority of the event. For example, `normal` or `low`. Allowed enum values: `normal,low`                                                                                                                                                                                |
| events       | source_type_name | string   | The type of event being posted. Option examples include nagios, hudson, jenkins, my_apps, chef, puppet, git, bitbucket, etc. The list of standard source attribute values [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). |
| events       | tags             | [string] | A list of tags to apply to the event.                                                                                                                                                                                                                                       |
| events       | text             | string   | The body of the event. Limited to 4000 characters. The text supports markdown. To use markdown in the event text, start the text block with `%%% \n` and end the text block with `\n %%%`. Use `msg_text` with the Datadog Ruby library.                                    |
| events       | title            | string   | The event title.                                                                                                                                                                                                                                                            |
| events       | url              | string   | URL of the event.                                                                                                                                                                                                                                                           |
|              | status           | string   | A status.                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "events": [
    {
      "alert_type": "info",
      "date_happened": "integer",
      "device_name": "string",
      "host": "string",
      "id": "integer",
      "id_str": "string",
      "payload": "{}",
      "priority": "normal",
      "source_type_name": "string",
      "tags": [
        "environment:test"
      ],
      "text": "Oh boy!",
      "title": "Did you hear the news today?",
      "url": "string"
    }
  ],
  "status": "string"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="403" %}
Authentication Error
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
                  \# Required query argumentsexport start="CHANGE_ME"export end="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/events?start=${start}&end=${end}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a list of events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.events_api import EventsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.list_events(
        start=9223372036854775807,
        end=9223372036854775807,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a list of events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::EventsAPI.new
p api_instance.list_events(9223372036854775807, 9223372036854775807)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

end_time = Time.now.to_i
start_time = end_time - 100

dog.stream(start_time, end_time, :priority => "normal", :tags => ["-env:dev,application:web"], :unaggregated => true)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a list of events returns "OK" response

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
	api := datadogV1.NewEventsApi(apiClient)
	resp, r, err := api.ListEvents(ctx, 9223372036854775807, 9223372036854775807, *datadogV1.NewListEventsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EventsApi.ListEvents`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `EventsApi.ListEvents`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a list of events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.EventsApi;
import com.datadog.api.client.v1.model.EventListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    EventsApi apiInstance = new EventsApi(defaultClient);

    try {
      EventListResponse result = apiInstance.listEvents(9223372036854775807L, 9223372036854775807L);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#listEvents");
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

```python
from datadog import initialize, api
import time

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

end_time = time.time()
start_time = end_time - 100

api.Event.query(
    start=start_time,
    end=end_time,
    priority="normal",
    tags=["-env:dev,application:web"],
    unaggregated=True
)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
##### 

```rust
// Get a list of events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_events::EventsAPI;
use datadog_api_client::datadogV1::api_events::ListEventsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = EventsAPI::with_config(configuration);
    let resp = api
        .list_events(
            9223372036854775807,
            9223372036854775807,
            ListEventsOptionalParams::default(),
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
 * Get a list of events returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.EventsApi(configuration);

const params: v1.EventsApiListEventsRequest = {
  start: 9223372036854775807,
  end: 9223372036854775807,
};

apiInstance
  .listEvents(params)
  .then((data: v1.EventListResponse) => {
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

{% tab title="v2" %}

| Datadog site      | API endpoint                                    |
| ----------------- | ----------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/events |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/events |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/events      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/events      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/events     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/events |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/events |

### Overview



List endpoint returns events that match an events search query. [Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).

Use this endpoint to see your latest events.
This endpoint requires the `events_read` permission.
OAuth apps require the `events_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#events) to access this endpoint.



### Arguments

#### Query Strings

| Name          | Type    | Description                                                             |
| ------------- | ------- | ----------------------------------------------------------------------- |
| filter[query] | string  | Search query following events syntax.                                   |
| filter[from]  | string  | Minimum timestamp for requested events, in milliseconds.                |
| filter[to]    | string  | Maximum timestamp for requested events, in milliseconds.                |
| sort          | enum    | Order of events in results.Allowed enum values: `timestamp, -timestamp` |
| page[cursor]  | string  | List following results with a cursor provided in the previous query.    |
| page[limit]   | integer | Maximum number of events in the response.                               |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The response object with all events matching the request and pagination information.

| Parent field | Field            | Type      | Description                                                                                                                                                                                                                                                                      |
| ------------ | ---------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data             | [object]  | An array of events matching the request.                                                                                                                                                                                                                                         |
| data         | attributes       | object    | The object description of an event response attribute.                                                                                                                                                                                                                           |
| attributes   | attributes       | object    | Object description of attributes from your event.                                                                                                                                                                                                                                |
| attributes   | aggregation_key  | string    | Aggregation key of the event.                                                                                                                                                                                                                                                    |
| attributes   | date_happened    | int64     | POSIX timestamp of the event. Must be sent as an integer (no quotation marks). Limited to events no older than 18 hours.                                                                                                                                                         |
| attributes   | device_name      | string    | A device name.                                                                                                                                                                                                                                                                   |
| attributes   | duration         | int64     | The duration between the triggering of the event and its recovery in nanoseconds.                                                                                                                                                                                                |
| attributes   | event_object     | string    | The event title.                                                                                                                                                                                                                                                                 |
| attributes   | evt              | object    | The metadata associated with a request.                                                                                                                                                                                                                                          |
| evt          | id               | string    | Event ID.                                                                                                                                                                                                                                                                        |
| evt          | name             | string    | The event name.                                                                                                                                                                                                                                                                  |
| evt          | source_id        | int64     | Event source ID.                                                                                                                                                                                                                                                                 |
| evt          | type             | string    | Event type.                                                                                                                                                                                                                                                                      |
| attributes   | hostname         | string    | Host name to associate with the event. Any tags associated with the host are also applied to this event.                                                                                                                                                                         |
| attributes   | monitor          | object    | Attributes from the monitor that triggered the event.                                                                                                                                                                                                                            |
| monitor      | created_at       | int64     | The POSIX timestamp of the monitor's creation in nanoseconds.                                                                                                                                                                                                                    |
| monitor      | group_status     | int32     | Monitor group status used when there is no `result_groups`.                                                                                                                                                                                                                      |
| monitor      | groups           | [string]  | Groups to which the monitor belongs.                                                                                                                                                                                                                                             |
| monitor      | id               | int64     | The monitor ID.                                                                                                                                                                                                                                                                  |
| monitor      | message          | string    | The monitor message.                                                                                                                                                                                                                                                             |
| monitor      | modified         | int64     | The monitor's last-modified timestamp.                                                                                                                                                                                                                                           |
| monitor      | name             | string    | The monitor name.                                                                                                                                                                                                                                                                |
| monitor      | query            | string    | The query that triggers the alert.                                                                                                                                                                                                                                               |
| monitor      | tags             | [string]  | A list of tags attached to the monitor.                                                                                                                                                                                                                                          |
| monitor      | templated_name   | string    | The templated name of the monitor before resolving any template variables.                                                                                                                                                                                                       |
| monitor      | type             | string    | The monitor type.                                                                                                                                                                                                                                                                |
| attributes   | monitor_groups   | [string]  | List of groups referred to in the event.                                                                                                                                                                                                                                         |
| attributes   | monitor_id       | int64     | ID of the monitor that triggered the event. When an event isn't related to a monitor, this field is empty.                                                                                                                                                                       |
| attributes   | priority         | enum      | The priority of the event's monitor. For example, `normal` or `low`. Allowed enum values: `normal,low`                                                                                                                                                                           |
| attributes   | related_event_id | int64     | Related event ID.                                                                                                                                                                                                                                                                |
| attributes   | service          | string    | Service that triggered the event.                                                                                                                                                                                                                                                |
| attributes   | source_type_name | string    | The type of event being posted. For example, `nagios`, `hudson`, `jenkins`, `my_apps`, `chef`, `puppet`, `git` or `bitbucket`. The list of standard source attribute values is [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). |
| attributes   | sourcecategory   | string    | Identifier for the source of the event, such as a monitor alert, an externally-submitted event, or an integration.                                                                                                                                                               |
| attributes   | status           | enum      | If an alert event is enabled, its status is one of the following: `failure`, `error`, `warning`, `info`, `success`, `user_update`, `recommendation`, or `snapshot`. Allowed enum values: `failure,error,warning,info,success,user_update,recommendation,snapshot`                |
| attributes   | tags             | [string]  | A list of tags to apply to the event.                                                                                                                                                                                                                                            |
| attributes   | timestamp        | int64     | POSIX timestamp of your event in milliseconds.                                                                                                                                                                                                                                   |
| attributes   | title            | string    | The event title.                                                                                                                                                                                                                                                                 |
| attributes   | message          | string    | The message of the event.                                                                                                                                                                                                                                                        |
| attributes   | tags             | [string]  | An array of tags associated with the event.                                                                                                                                                                                                                                      |
| attributes   | timestamp        | date-time | The timestamp of the event.                                                                                                                                                                                                                                                      |
| data         | id               | string    | the unique ID of the event.                                                                                                                                                                                                                                                      |
| data         | type             | enum      | Type of the event. Allowed enum values: `event`                                                                                                                                                                                                                                  |
|              | links            | object    | Links attributes.                                                                                                                                                                                                                                                                |
| links        | next             | string    | Link for the next set of results. Note that the request can also be made using the POST endpoint.                                                                                                                                                                                |
|              | meta             | object    | The metadata associated with a request.                                                                                                                                                                                                                                          |
| meta         | elapsed          | int64     | The time elapsed in milliseconds.                                                                                                                                                                                                                                                |
| meta         | page             | object    | Pagination attributes.                                                                                                                                                                                                                                                           |
| page         | after            | string    | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of the `page[cursor]`.                                                                                                                                    |
| meta         | request_id       | string    | The identifier of the request.                                                                                                                                                                                                                                                   |
| meta         | status           | string    | The request status.                                                                                                                                                                                                                                                              |
| meta         | warnings         | [object]  | A list of warnings (non-fatal errors) encountered. Partial results might be returned if warnings are present in the response.                                                                                                                                                    |
| warnings     | code             | string    | A unique code for this type of warning.                                                                                                                                                                                                                                          |
| warnings     | detail           | string    | A detailed explanation of this specific warning.                                                                                                                                                                                                                                 |
| warnings     | title            | string    | A short human-readable summary of the warning.                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "attributes": {
          "aggregation_key": "string",
          "date_happened": "integer",
          "device_name": "string",
          "duration": "integer",
          "event_object": "Did you hear the news today?",
          "evt": {
            "id": "6509751066204996294",
            "name": "string",
            "source_id": 36,
            "type": "error_tracking_alert"
          },
          "hostname": "string",
          "monitor": {
            "created_at": 1646318692000,
            "group_status": "integer",
            "groups": [],
            "id": "integer",
            "message": "string",
            "modified": "integer",
            "name": "string",
            "query": "string",
            "tags": [
              "environment:test"
            ],
            "templated_name": "string",
            "type": "string"
          },
          "monitor_groups": [],
          "monitor_id": "integer",
          "priority": "normal",
          "related_event_id": "integer",
          "service": "datadog-api",
          "source_type_name": "string",
          "sourcecategory": "string",
          "status": "info",
          "tags": [
            "environment:test"
          ],
          "timestamp": 1652274265000,
          "title": "Oh boy!"
        },
        "message": "string",
        "tags": [
          "team:A"
        ],
        "timestamp": "2019-01-02T09:42:36.320Z"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "event"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/events?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
  },
  "meta": {
    "elapsed": 132,
    "page": {
      "after": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
    },
    "request_id": "MWlFUjVaWGZTTTZPYzM0VXp1OXU2d3xLSVpEMjZKQ0VKUTI0dEYtM3RSOFVR",
    "status": "done",
    "warnings": [
      {
        "code": "unknown_index",
        "detail": "indexes: foo, bar",
        "title": "One or several indexes are missing or invalid. Results hold data from the other indexes."
      }
    ]
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
Not Authorized
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/events" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a list of events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.list_events()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a list of events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::EventsAPI.new
p api_instance.list_events()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a list of events returns "OK" response

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
	api := datadogV2.NewEventsApi(apiClient)
	resp, r, err := api.ListEvents(ctx, *datadogV2.NewListEventsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EventsApi.ListEvents`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `EventsApi.ListEvents`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a list of events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.EventsApi;
import com.datadog.api.client.v2.model.EventsListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    EventsApi apiInstance = new EventsApi(defaultClient);

    try {
      EventsListResponse result = apiInstance.listEvents();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#listEvents");
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
// Get a list of events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_events::EventsAPI;
use datadog_api_client::datadogV2::api_events::ListEventsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = EventsAPI::with_config(configuration);
    let resp = api.list_events(ListEventsOptionalParams::default()).await;
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
 * Get a list of events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.EventsApi(configuration);

apiInstance
  .listEvents()
  .then((data: v2.EventsListResponse) => {
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

## Post an event{% #post-an-event %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                     |
| ----------------- | ------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/events |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/events |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/events      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/events      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/events     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/events |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/events |

### Overview

This endpoint allows you to post events to the stream. Tag them, set priority and event aggregate them with other events.

### Request

#### Body Data (required)

Event request object

{% tab title="Model" %}

| Field                   | Type     | Description                                                                                                                                                                                                                                                               |
| ----------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| aggregation_key         | string   | An arbitrary string to use for aggregation. Limited to 100 characters. If you specify a key, all events using that key are grouped together in the Event Stream.                                                                                                          |
| alert_type              | enum     | If an alert event is enabled, set its type. For example, `error`, `warning`, `info`, `success`, `user_update`, `recommendation`, and `snapshot`. Allowed enum values: `error,warning,info,success,user_update,recommendation,snapshot`                                    |
| date_happened           | int64    | POSIX timestamp of the event. Must be sent as an integer (that is no quotes). Limited to events no older than 18 hours                                                                                                                                                    |
| device_name             | string   | A device name.                                                                                                                                                                                                                                                            |
| host                    | string   | Host name to associate with the event. Any tags associated with the host are also applied to this event.                                                                                                                                                                  |
| priority                | enum     | The priority of the event. For example, `normal` or `low`. Allowed enum values: `normal,low`                                                                                                                                                                              |
| related_event_id        | int64    | ID of the parent event. Must be sent as an integer (that is no quotes).                                                                                                                                                                                                   |
| source_type_name        | string   | The type of event being posted. Option examples include nagios, hudson, jenkins, my_apps, chef, puppet, git, bitbucket, etc. A complete list of source attribute values [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). |
| tags                    | [string] | A list of tags to apply to the event.                                                                                                                                                                                                                                     |
| text [*required*]  | string   | The body of the event. Limited to 4000 characters. The text supports markdown. To use markdown in the event text, start the text block with `%%% \n` and end the text block with `\n %%%`. Use `msg_text` with the Datadog Ruby library.                                  |
| title [*required*] | string   | The event title.                                                                                                                                                                                                                                                          |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "title": "Example-Event",
  "text": "A text message.",
  "tags": [
    "test:ExampleEvent"
  ]
}
```

##### 

```json
{
  "title": "Example-Event very very very looooooooong looooooooooooong loooooooooooooooooooooong looooooooooooooooooooooooooong title with 100+ characters",
  "text": "A text message.",
  "tags": [
    "test:ExampleEvent"
  ]
}
```

{% /tab %}

### Response

{% tab title="202" %}
OK
{% tab title="Model" %}
Object containing an event response.

| Parent field | Field            | Type     | Description                                                                                                                                                                                                                                                                 |
| ------------ | ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | event            | object   | Object representing an event.                                                                                                                                                                                                                                               |
| event        | alert_type       | enum     | If an alert event is enabled, set its type. For example, `error`, `warning`, `info`, `success`, `user_update`, `recommendation`, and `snapshot`. Allowed enum values: `error,warning,info,success,user_update,recommendation,snapshot`                                      |
| event        | date_happened    | int64    | POSIX timestamp of the event. Must be sent as an integer (that is no quotes). Limited to events up to 18 hours in the past and two hours in the future.                                                                                                                     |
| event        | device_name      | string   | A device name.                                                                                                                                                                                                                                                              |
| event        | host             | string   | Host name to associate with the event. Any tags associated with the host are also applied to this event.                                                                                                                                                                    |
| event        | id               | int64    | Integer ID of the event.                                                                                                                                                                                                                                                    |
| event        | id_str           | string   | Handling IDs as large 64-bit numbers can cause loss of accuracy issues with some programming languages. Instead, use the string representation of the Event ID to avoid losing accuracy.                                                                                    |
| event        | payload          | string   | Payload of the event.                                                                                                                                                                                                                                                       |
| event        | priority         | enum     | The priority of the event. For example, `normal` or `low`. Allowed enum values: `normal,low`                                                                                                                                                                                |
| event        | source_type_name | string   | The type of event being posted. Option examples include nagios, hudson, jenkins, my_apps, chef, puppet, git, bitbucket, etc. The list of standard source attribute values [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). |
| event        | tags             | [string] | A list of tags to apply to the event.                                                                                                                                                                                                                                       |
| event        | text             | string   | The body of the event. Limited to 4000 characters. The text supports markdown. To use markdown in the event text, start the text block with `%%% \n` and end the text block with `\n %%%`. Use `msg_text` with the Datadog Ruby library.                                    |
| event        | title            | string   | The event title.                                                                                                                                                                                                                                                            |
| event        | url              | string   | URL of the event.                                                                                                                                                                                                                                                           |
|              | status           | string   | A status.                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "event": {
    "alert_type": "info",
    "date_happened": "integer",
    "device_name": "string",
    "host": "string",
    "id": "integer",
    "id_str": "string",
    "payload": "{}",
    "priority": "normal",
    "source_type_name": "string",
    "tags": [
      "environment:test"
    ],
    "text": "Oh boy!",
    "title": "Did you hear the news today?",
    "url": "string"
  },
  "status": "string"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/events" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "title": "Example-Event",
  "text": "A text message.",
  "tags": [
    "test:ExampleEvent"
  ]
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/events" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "title": "Example-Event very very very looooooooong looooooooooooong loooooooooooooooooooooong looooooooooooooooooooooooooong title with 100+ characters",
  "text": "A text message.",
  "tags": [
    "test:ExampleEvent"
  ]
}
EOF
                        
##### 

```go
// Post an event returns "OK" response

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
	body := datadogV1.EventCreateRequest{
		Title: "Example-Event",
		Text:  "A text message.",
		Tags: []string{
			"test:ExampleEvent",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewEventsApi(apiClient)
	resp, r, err := api.CreateEvent(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EventsApi.CreateEvent`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `EventsApi.CreateEvent`:\n%s\n", responseContent)
}
```

##### 

```go
// Post an event with a long title returns "OK" response

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
	body := datadogV1.EventCreateRequest{
		Title: "Example-Event very very very looooooooong looooooooooooong loooooooooooooooooooooong looooooooooooooooooooooooooong title with 100+ characters",
		Text:  "A text message.",
		Tags: []string{
			"test:ExampleEvent",
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewEventsApi(apiClient)
	resp, r, err := api.CreateEvent(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EventsApi.CreateEvent`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `EventsApi.CreateEvent`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"
##### 

```java
// Post an event returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.EventsApi;
import com.datadog.api.client.v1.model.EventCreateRequest;
import com.datadog.api.client.v1.model.EventCreateResponse;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    EventsApi apiInstance = new EventsApi(defaultClient);

    EventCreateRequest body =
        new EventCreateRequest()
            .title("Example-Event")
            .text("A text message.")
            .tags(Collections.singletonList("test:ExampleEvent"));

    try {
      EventCreateResponse result = apiInstance.createEvent(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#createEvent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

##### 

```java
// Post an event with a long title returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.EventsApi;
import com.datadog.api.client.v1.model.EventCreateRequest;
import com.datadog.api.client.v1.model.EventCreateResponse;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    EventsApi apiInstance = new EventsApi(defaultClient);

    EventCreateRequest body =
        new EventCreateRequest()
            .title(
                "Example-Event very very very looooooooong looooooooooooong"
                    + " loooooooooooooooooooooong looooooooooooooooooooooooooong title with 100+"
                    + " characters")
            .text("A text message.")
            .tags(Collections.singletonList("test:ExampleEvent"));

    try {
      EventCreateResponse result = apiInstance.createEvent(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#createEvent");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"
##### 

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

title = "Something big happened!"
text = 'And let me tell you all about it here!'
tags = ['version:1', 'application:web']

api.Event.create(title=title, text=text, tags=tags)

# If you are programmatically adding a comment to this new event
# you might want to insert a pause of .5 - 1 second to allow the
# event to be available.
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python "example.py"
##### 

```python
"""
Post an event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.events_api import EventsApi
from datadog_api_client.v1.model.event_create_request import EventCreateRequest

body = EventCreateRequest(
    title="Example-Event",
    text="A text message.",
    tags=[
        "test:ExampleEvent",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.create_event(body=body)

    print(response)
```

##### 

```python
"""
Post an event with a long title returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.events_api import EventsApi
from datadog_api_client.v1.model.event_create_request import EventCreateRequest

body = EventCreateRequest(
    title="Example-Event very very very looooooooong looooooooooooong loooooooooooooooooooooong looooooooooooooooooooooooooong title with 100+ characters",
    text="A text message.",
    tags=[
        "test:ExampleEvent",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.create_event(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"
##### 

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# submitting events doesn 't require an application_key,
# so we don't bother setting it
dog = Dogapi::Client.new(api_key)

dog.emit_event(Dogapi::Event.new('msg_text', :msg_title => 'Title'))

# If you are programmatically adding a comment to this new event
# you might want to insert a pause of.5 - 1 second to allow the
# event to be available.
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
##### 

```ruby
# Post an event returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::EventsAPI.new

body = DatadogAPIClient::V1::EventCreateRequest.new({
  title: "Example-Event",
  text: "A text message.",
  tags: [
    "test:ExampleEvent",
  ],
})
p api_instance.create_event(body)
```

##### 

```ruby
# Post an event with a long title returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::EventsAPI.new

body = DatadogAPIClient::V1::EventCreateRequest.new({
  title: "Example-Event very very very looooooooong looooooooooooong loooooooooooooooooooooong looooooooooooooooooooooooooong title with 100+ characters",
  text: "A text message.",
  tags: [
    "test:ExampleEvent",
  ],
})
p api_instance.create_event(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
##### 

```rust
// Post an event returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_events::EventsAPI;
use datadog_api_client::datadogV1::model::EventCreateRequest;

#[tokio::main]
async fn main() {
    let body = EventCreateRequest::new("A text message.".to_string(), "Example-Event".to_string())
        .tags(vec!["test:ExampleEvent".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = EventsAPI::with_config(configuration);
    let resp = api.create_event(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Post an event with a long title returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_events::EventsAPI;
use datadog_api_client::datadogV1::model::EventCreateRequest;

#[tokio::main]
async fn main() {
    let body =
        EventCreateRequest::new(
            "A text message.".to_string(),
            "Example-Event very very very looooooooong looooooooooooong loooooooooooooooooooooong looooooooooooooooooooooooooong title with 100+ characters".to_string(),
        ).tags(vec!["test:ExampleEvent".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = EventsAPI::with_config(configuration);
    let resp = api.create_event(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run
##### 

```typescript
/**
 * Post an event returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.EventsApi(configuration);

const params: v1.EventsApiCreateEventRequest = {
  body: {
    title: "Example-Event",
    text: "A text message.",
    tags: ["test:ExampleEvent"],
  },
};

apiInstance
  .createEvent(params)
  .then((data: v1.EventCreateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Post an event with a long title returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.EventsApi(configuration);

const params: v1.EventsApiCreateEventRequest = {
  body: {
    title:
      "Example-Event very very very looooooooong looooooooooooong loooooooooooooooooooooong looooooooooooooooooooooooooong title with 100+ characters",
    text: "A text message.",
    tags: ["test:ExampleEvent"],
  },
};

apiInstance
  .createEvent(params)
  .then((data: v1.EventCreateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://event-management-intake.ap1.datadoghq.com/api/v2/events |
| ap2.datadoghq.com | POST https://event-management-intake.ap2.datadoghq.com/api/v2/events |
| app.datadoghq.eu  | POST https://event-management-intake.datadoghq.eu/api/v2/events      |
| app.ddog-gov.com  | POST https://event-management-intake.ddog-gov.com/api/v2/events      |
| app.datadoghq.com | POST https://event-management-intake.datadoghq.com/api/v2/events     |
| us3.datadoghq.com | POST https://event-management-intake.us3.datadoghq.com/api/v2/events |
| us5.datadoghq.com | POST https://event-management-intake.us5.datadoghq.com/api/v2/events |

### Overview



This endpoint allows you to publish events.

**Note:** To utilize this endpoint with our client libraries, please ensure you are using the latest version released on or after July 1, 2025. Earlier versions do not support this functionality.

**Important:** Upgrade to the latest client library version to use the updated endpoint at `https://event-management-intake.{site}/api/v2/events`. Older client library versions of the Post an event (v2) API send requests to a deprecated endpoint (`https://api.{site}/api/v2/events`).

â **Only events with the `change` or `alert` category** are in General Availability. For change events, see [Change Tracking](https://docs.datadoghq.com/change_tracking) for more details.

â For use cases involving other event categories, use the V1 endpoint or reach out to [support](https://www.datadoghq.com/support/).



### Request

#### Body Data (required)

Event creation request payload.

{% tab title="Model" %}

| Parent field       | Field                              | Type          | Description                                                                                                                                                                                                                                            |
| ------------------ | ---------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                    | data [*required*]             | object        | An event object.                                                                                                                                                                                                                                       |
| data               | attributes [*required*]       | object        | Event attributes.                                                                                                                                                                                                                                      |
| attributes         | aggregation_key                    | string        | A string used for aggregation when [correlating](https://docs.datadoghq.com/service_management/events/correlation/) events. If you specify a key, events are deduplicated to alerts based on this key. Limited to 100 characters.                      |
| attributes         | attributes [*required*]       |  <oneOf> | JSON object for category-specific attributes. Schema is different per event category.                                                                                                                                                                  |
| attributes         | Option 1                           | object        | Change event attributes.                                                                                                                                                                                                                               |
| Option 1           | author                             | object        | The entity that made the change. Optional, if provided it must include `type` and `name`.                                                                                                                                                              |
| author             | name [*required*]             | string        | The name of the user or system that made the change. Limited to 128 characters.                                                                                                                                                                        |
| author             | type [*required*]             | enum          | Author's type. Allowed enum values: `user,system,api,automation`                                                                                                                                                                                       |
| Option 1           | change_metadata                    | object        | Free form JSON object with information related to the `change` event. Supports up to 100 properties per object and a maximum nesting depth of 10 levels.                                                                                               |
| Option 1           | changed_resource [*required*] | object        | A uniquely identified resource.                                                                                                                                                                                                                        |
| changed_resource   | name [*required*]             | string        | The name of the resource that was changed. Limited to 128 characters. Must contain at least one non-whitespace character.                                                                                                                              |
| changed_resource   | type [*required*]             | enum          | The type of the resource that was changed. Allowed enum values: `feature_flag,configuration`                                                                                                                                                           |
| Option 1           | impacted_resources                 | [object]      | A list of resources impacted by this change. It is recommended to provide an impacted resource to display the change event at the correct location. Only resources of type `service` are supported. Maximum of 100 impacted resources allowed.         |
| impacted_resources | name [*required*]             | string        | The name of the impacted resource. Limited to 128 characters.                                                                                                                                                                                          |
| impacted_resources | type [*required*]             | enum          | The type of the impacted resource. Allowed enum values: `service`                                                                                                                                                                                      |
| Option 1           | new_value                          | object        | Free form JSON object representing the new state of the changed resource.                                                                                                                                                                              |
| Option 1           | prev_value                         | object        | Free form JSON object representing the previous state of the changed resource.                                                                                                                                                                         |
| attributes         | Option 2                           | object        | Alert event attributes.                                                                                                                                                                                                                                |
| Option 2           | custom                             | object        | Free form JSON object for arbitrary data. Supports up to 100 properties per object and a maximum nesting depth of 10 levels.                                                                                                                           |
| Option 2           | links                              | [object]      | The links related to the event. Maximum of 20 links allowed.                                                                                                                                                                                           |
| links              | category [*required*]         | enum          | The category of the link. Allowed enum values: `runbook,documentation,dashboard,resource`                                                                                                                                                              |
| links              | title                              | string        | The display text of the link. Limited to 300 characters.                                                                                                                                                                                               |
| links              | url [*required*]              | string        | The URL of the link. Limited to 2048 characters.                                                                                                                                                                                                       |
| Option 2           | priority                           | enum          | The priority of the alert. Allowed enum values: `1,2,3,4,5`                                                                                                                                                                                            |
| Option 2           | status [*required*]           | enum          | The status of the alert. Allowed enum values: `warn,error,ok`                                                                                                                                                                                          |
| attributes         | category [*required*]         | enum          | Event category identifying the type of event. Allowed enum values: `change,alert`                                                                                                                                                                      |
| attributes         | host                               | string        | Host name to associate with the event. Any tags associated with the host are also applied to this event. Limited to 255 characters.                                                                                                                    |
| attributes         | integration_id                     | enum          | Integration ID sourced from integration manifests. Allowed enum values: `custom-events`                                                                                                                                                                |
| attributes         | message                            | string        | Free formed text associated with the event. It's suggested to use `data.attributes.attributes.custom` for well-structured attributes. Limited to 4000 characters.                                                                                      |
| attributes         | tags                               | [string]      | A list of tags associated with the event. Maximum of 100 tags allowed. Refer to [Tags docs](https://docs.datadoghq.com/getting_started/tagging/).                                                                                                      |
| attributes         | timestamp                          | string        | Timestamp when the event occurred. Must follow [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. For example `"2017-01-15T01:30:15.010000Z"`. Defaults to the timestamp of receipt. Limited to values no older than 18 hours. |
| attributes         | title [*required*]            | string        | The title of the event. Limited to 500 characters.                                                                                                                                                                                                     |
| data               | type [*required*]             | enum          | Entity type. Allowed enum values: `event`                                                                                                                                                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "aggregation_key": "aggregation_key_123",
      "attributes": {
        "author": {
          "name": "example@datadog.com",
          "type": "user"
        },
        "change_metadata": {
          "dd": {
            "team": "datadog_team",
            "user_email": "datadog@datadog.com",
            "user_id": "datadog_user_id",
            "user_name": "datadog_username"
          },
          "resource_link": "datadog.com/feature/fallback_payments_test"
        },
        "changed_resource": {
          "name": "fallback_payments_test",
          "type": "feature_flag"
        },
        "impacted_resources": [
          {
            "name": "payments_api",
            "type": "service"
          }
        ],
        "new_value": {
          "enabled": true,
          "percentage": "50%",
          "rule": {
            "datacenter": "devcycle.us1.prod"
          }
        },
        "prev_value": {
          "enabled": true,
          "percentage": "10%",
          "rule": {
            "datacenter": "devcycle.us1.prod"
          }
        }
      },
      "category": "change",
      "integration_id": "custom-events",
      "host": "test-host",
      "message": "payment_processed feature flag has been enabled",
      "tags": [
        "env:api_client_test"
      ],
      "title": "payment_processed feature flag updated"
    },
    "type": "event"
  }
}
```

{% /tab %}

### Response

{% tab title="202" %}
OK
{% tab title="Model" %}
Event creation response.

| Parent field | Field      | Type   | Description                                                                                                                      |
| ------------ | ---------- | ------ | -------------------------------------------------------------------------------------------------------------------------------- |
|              | data       | object | Event object.                                                                                                                    |
| data         | attributes | object | Event attributes.                                                                                                                |
| attributes   | attributes | object | JSON object for category-specific attributes.                                                                                    |
| attributes   | evt        | object | JSON object of event system attributes.                                                                                          |
| evt          | id         | string | **DEPRECATED**: Event identifier. This field is deprecated and will be removed in a future version. Use the `uid` field instead. |
| evt          | uid        | string | A unique identifier for the event. You can use this identifier to query or reference the event.                                  |
| data         | type       | string | Entity type.                                                                                                                     |
|              | links      | object | Links to the event.                                                                                                              |
| links        | self       | string | The URL of the event. This link is only functional when using the default subdomain.                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "attributes": {
        "evt": {
          "id": "string",
          "uid": "string"
        }
      }
    },
    "type": "event"
  },
  "links": {
    "self": "string"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
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
                          \## Alert Event
# Example of an alert event for tracking alerts and monitoring events.
\# Curl commandcurl -X POST "https://event-management-intake.ap1.datadoghq.com"https://event-management-intake.ap2.datadoghq.com"https://event-management-intake.datadoghq.eu"https://event-management-intake.ddog-gov.com"https://event-management-intake.datadoghq.com"https://event-management-intake.us3.datadoghq.com"https://event-management-intake.us5.datadoghq.com/api/v2/events" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "aggregation_key": "deduplication_key_here",
      "attributes": {
        "custom": {
          "my-object-attribute": {
            "my-array-attribute": [
              1,
              2,
              3
            ],
            "my-array-object-attribute": [
              {
                "name": "test-object-1"
              },
              {
                "name": "test-object-2"
              }
            ],
            "my-integer-attribute": 1
          },
          "my-string-attribute": "my-custom-value"
        },
        "links": [
          {
            "category": "runbook",
            "title": "Datadog website",
            "url": "https://datadoghq.com"
          }
        ],
        "priority": "1",
        "status": "error"
      },
      "category": "alert",
      "message": "Something is broken!",
      "tags": [
        "service:my-test-service",
        "datacenter:primary"
      ],
      "title": "My Alerting Event"
    },
    "type": "event"
  }
}
EOF\## Change Event
# Example of a change event for tracking configuration or feature flag changes.
\# Curl commandcurl -X POST "https://event-management-intake.ap1.datadoghq.com"https://event-management-intake.ap2.datadoghq.com"https://event-management-intake.datadoghq.eu"https://event-management-intake.ddog-gov.com"https://event-management-intake.datadoghq.com"https://event-management-intake.us3.datadoghq.com"https://event-management-intake.us5.datadoghq.com/api/v2/events" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "aggregation_key": "aggregation_key_123",
      "attributes": {
        "author": {
          "name": "example@datadog.com",
          "type": "user"
        },
        "change_metadata": {
          "dd": {
            "team": "datadog_team",
            "user_email": "datadog@datadog.com",
            "user_id": "datadog_user_id",
            "user_name": "datadog_username"
          },
          "resource_link": "datadog.com/feature/fallback_payments_test"
        },
        "changed_resource": {
          "name": "fallback_payments_test",
          "type": "feature_flag"
        },
        "impacted_resources": [
          {
            "name": "payments_api",
            "type": "service"
          }
        ],
        "new_value": {
          "enabled": true,
          "percentage": "50%",
          "rule": {
            "datacenter": "devcycle.us1.prod"
          }
        },
        "prev_value": {
          "enabled": true,
          "percentage": "10%",
          "rule": {
            "datacenter": "devcycle.us1.prod"
          }
        }
      },
      "category": "change",
      "host": "hostname",
      "integration_id": "custom-events",
      "message": "payment_processed feature flag has been enabled",
      "tags": [
        "env:api_client_test"
      ],
      "timestamp": "2020-01-01T01:30:15.010000Z",
      "title": "payment_processed feature flag updated"
    },
    "type": "event"
  }
}
EOF
                        
##### 

```go
// Post an event returns "OK" response

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
	body := datadogV2.EventCreateRequestPayload{
		Data: datadogV2.EventCreateRequest{
			Attributes: datadogV2.EventPayload{
				AggregationKey: datadog.PtrString("aggregation_key_123"),
				Attributes: datadogV2.EventPayloadAttributes{
					ChangeEventCustomAttributes: &datadogV2.ChangeEventCustomAttributes{
						Author: &datadogV2.ChangeEventCustomAttributesAuthor{
							Name: "example@datadog.com",
							Type: datadogV2.CHANGEEVENTCUSTOMATTRIBUTESAUTHORTYPE_USER,
						},
						ChangeMetadata: map[string]interface{}{
							"dd":            "{'team': 'datadog_team', 'user_email': 'datadog@datadog.com', 'user_id': 'datadog_user_id', 'user_name': 'datadog_username'}",
							"resource_link": "datadog.com/feature/fallback_payments_test",
						},
						ChangedResource: datadogV2.ChangeEventCustomAttributesChangedResource{
							Name: "fallback_payments_test",
							Type: datadogV2.CHANGEEVENTCUSTOMATTRIBUTESCHANGEDRESOURCETYPE_FEATURE_FLAG,
						},
						ImpactedResources: []datadogV2.ChangeEventCustomAttributesImpactedResourcesItems{
							{
								Name: "payments_api",
								Type: datadogV2.CHANGEEVENTCUSTOMATTRIBUTESIMPACTEDRESOURCESITEMSTYPE_SERVICE,
							},
						},
						NewValue: map[string]interface{}{
							"enabled":    "True",
							"percentage": "50%",
							"rule":       "{'datacenter': 'devcycle.us1.prod'}",
						},
						PrevValue: map[string]interface{}{
							"enabled":    "True",
							"percentage": "10%",
							"rule":       "{'datacenter': 'devcycle.us1.prod'}",
						},
					}},
				Category:      datadogV2.EVENTCATEGORY_CHANGE,
				IntegrationId: datadogV2.EVENTPAYLOADINTEGRATIONID_CUSTOM_EVENTS.Ptr(),
				Host:          datadog.PtrString("test-host"),
				Message:       datadog.PtrString("payment_processed feature flag has been enabled"),
				Tags: []string{
					"env:api_client_test",
				},
				Title: "payment_processed feature flag updated",
			},
			Type: datadogV2.EVENTCREATEREQUESTTYPE_EVENT,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewEventsApi(apiClient)
	resp, r, err := api.CreateEvent(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EventsApi.CreateEvent`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `EventsApi.CreateEvent`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Post an event returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.EventsApi;
import com.datadog.api.client.v2.model.ChangeEventCustomAttributes;
import com.datadog.api.client.v2.model.ChangeEventCustomAttributesAuthor;
import com.datadog.api.client.v2.model.ChangeEventCustomAttributesAuthorType;
import com.datadog.api.client.v2.model.ChangeEventCustomAttributesChangedResource;
import com.datadog.api.client.v2.model.ChangeEventCustomAttributesChangedResourceType;
import com.datadog.api.client.v2.model.ChangeEventCustomAttributesImpactedResourcesItems;
import com.datadog.api.client.v2.model.ChangeEventCustomAttributesImpactedResourcesItemsType;
import com.datadog.api.client.v2.model.EventCategory;
import com.datadog.api.client.v2.model.EventCreateRequest;
import com.datadog.api.client.v2.model.EventCreateRequestPayload;
import com.datadog.api.client.v2.model.EventCreateRequestType;
import com.datadog.api.client.v2.model.EventCreateResponsePayload;
import com.datadog.api.client.v2.model.EventPayload;
import com.datadog.api.client.v2.model.EventPayloadAttributes;
import com.datadog.api.client.v2.model.EventPayloadIntegrationId;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    EventsApi apiInstance = new EventsApi(defaultClient);

    EventCreateRequestPayload body =
        new EventCreateRequestPayload()
            .data(
                new EventCreateRequest()
                    .attributes(
                        new EventPayload()
                            .aggregationKey("aggregation_key_123")
                            .attributes(
                                new EventPayloadAttributes(
                                    new ChangeEventCustomAttributes()
                                        .author(
                                            new ChangeEventCustomAttributesAuthor()
                                                .name("example@datadog.com")
                                                .type(ChangeEventCustomAttributesAuthorType.USER))
                                        .changeMetadata(
                                            Map.ofEntries(
                                                Map.entry(
                                                    "dd",
                                                    "{'team': 'datadog_team', 'user_email':"
                                                        + " 'datadog@datadog.com', 'user_id':"
                                                        + " 'datadog_user_id', 'user_name':"
                                                        + " 'datadog_username'}"),
                                                Map.entry(
                                                    "resource_link",
                                                    "datadog.com/feature/fallback_payments_test")))
                                        .changedResource(
                                            new ChangeEventCustomAttributesChangedResource()
                                                .name("fallback_payments_test")
                                                .type(
                                                    ChangeEventCustomAttributesChangedResourceType
                                                        .FEATURE_FLAG))
                                        .impactedResources(
                                            Collections.singletonList(
                                                new ChangeEventCustomAttributesImpactedResourcesItems()
                                                    .name("payments_api")
                                                    .type(
                                                        ChangeEventCustomAttributesImpactedResourcesItemsType
                                                            .SERVICE)))
                                        .newValue(
                                            Map.ofEntries(
                                                Map.entry("enabled", "True"),
                                                Map.entry("percentage", "50%"),
                                                Map.entry(
                                                    "rule", "{'datacenter': 'devcycle.us1.prod'}")))
                                        .prevValue(
                                            Map.ofEntries(
                                                Map.entry("enabled", "True"),
                                                Map.entry("percentage", "10%"),
                                                Map.entry(
                                                    "rule",
                                                    "{'datacenter': 'devcycle.us1.prod'}")))))
                            .category(EventCategory.CHANGE)
                            .integrationId(EventPayloadIntegrationId.CUSTOM_EVENTS)
                            .host("test-host")
                            .message("payment_processed feature flag has been enabled")
                            .tags(Collections.singletonList("env:api_client_test"))
                            .title("payment_processed feature flag updated"))
                    .type(EventCreateRequestType.EVENT));

    try {
      EventCreateResponsePayload result = apiInstance.createEvent(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#createEvent");
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

```python
"""
Post an event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.change_event_custom_attributes import ChangeEventCustomAttributes
from datadog_api_client.v2.model.change_event_custom_attributes_author import ChangeEventCustomAttributesAuthor
from datadog_api_client.v2.model.change_event_custom_attributes_author_type import ChangeEventCustomAttributesAuthorType
from datadog_api_client.v2.model.change_event_custom_attributes_changed_resource import (
    ChangeEventCustomAttributesChangedResource,
)
from datadog_api_client.v2.model.change_event_custom_attributes_changed_resource_type import (
    ChangeEventCustomAttributesChangedResourceType,
)
from datadog_api_client.v2.model.change_event_custom_attributes_impacted_resources_items import (
    ChangeEventCustomAttributesImpactedResourcesItems,
)
from datadog_api_client.v2.model.change_event_custom_attributes_impacted_resources_items_type import (
    ChangeEventCustomAttributesImpactedResourcesItemsType,
)
from datadog_api_client.v2.model.event_category import EventCategory
from datadog_api_client.v2.model.event_create_request import EventCreateRequest
from datadog_api_client.v2.model.event_create_request_payload import EventCreateRequestPayload
from datadog_api_client.v2.model.event_create_request_type import EventCreateRequestType
from datadog_api_client.v2.model.event_payload import EventPayload
from datadog_api_client.v2.model.event_payload_integration_id import EventPayloadIntegrationId

body = EventCreateRequestPayload(
    data=EventCreateRequest(
        attributes=EventPayload(
            aggregation_key="aggregation_key_123",
            attributes=ChangeEventCustomAttributes(
                author=ChangeEventCustomAttributesAuthor(
                    name="example@datadog.com",
                    type=ChangeEventCustomAttributesAuthorType.USER,
                ),
                change_metadata=dict(
                    [
                        (
                            "dd",
                            "{'team': 'datadog_team', 'user_email': 'datadog@datadog.com', 'user_id': 'datadog_user_id', 'user_name': 'datadog_username'}",
                        ),
                        ("resource_link", "datadog.com/feature/fallback_payments_test"),
                    ]
                ),
                changed_resource=ChangeEventCustomAttributesChangedResource(
                    name="fallback_payments_test",
                    type=ChangeEventCustomAttributesChangedResourceType.FEATURE_FLAG,
                ),
                impacted_resources=[
                    ChangeEventCustomAttributesImpactedResourcesItems(
                        name="payments_api",
                        type=ChangeEventCustomAttributesImpactedResourcesItemsType.SERVICE,
                    ),
                ],
                new_value=dict(
                    [("enabled", "True"), ("percentage", "50%"), ("rule", "{'datacenter': 'devcycle.us1.prod'}")]
                ),
                prev_value=dict(
                    [("enabled", "True"), ("percentage", "10%"), ("rule", "{'datacenter': 'devcycle.us1.prod'}")]
                ),
            ),
            category=EventCategory.CHANGE,
            integration_id=EventPayloadIntegrationId.CUSTOM_EVENTS,
            host="test-host",
            message="payment_processed feature flag has been enabled",
            tags=[
                "env:api_client_test",
            ],
            title="payment_processed feature flag updated",
        ),
        type=EventCreateRequestType.EVENT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.create_event(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Post an event returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::EventsAPI.new

body = DatadogAPIClient::V2::EventCreateRequestPayload.new({
  data: DatadogAPIClient::V2::EventCreateRequest.new({
    attributes: DatadogAPIClient::V2::EventPayload.new({
      aggregation_key: "aggregation_key_123",
      attributes: DatadogAPIClient::V2::ChangeEventCustomAttributes.new({
        author: DatadogAPIClient::V2::ChangeEventCustomAttributesAuthor.new({
          name: "example@datadog.com",
          type: DatadogAPIClient::V2::ChangeEventCustomAttributesAuthorType::USER,
        }),
        change_metadata: {
          "dd": "{'team': 'datadog_team', 'user_email': 'datadog@datadog.com', 'user_id': 'datadog_user_id', 'user_name': 'datadog_username'}", "resource_link": "datadog.com/feature/fallback_payments_test",
        },
        changed_resource: DatadogAPIClient::V2::ChangeEventCustomAttributesChangedResource.new({
          name: "fallback_payments_test",
          type: DatadogAPIClient::V2::ChangeEventCustomAttributesChangedResourceType::FEATURE_FLAG,
        }),
        impacted_resources: [
          DatadogAPIClient::V2::ChangeEventCustomAttributesImpactedResourcesItems.new({
            name: "payments_api",
            type: DatadogAPIClient::V2::ChangeEventCustomAttributesImpactedResourcesItemsType::SERVICE,
          }),
        ],
        new_value: {
          "enabled": "True", "percentage": "50%", "rule": "{'datacenter': 'devcycle.us1.prod'}",
        },
        prev_value: {
          "enabled": "True", "percentage": "10%", "rule": "{'datacenter': 'devcycle.us1.prod'}",
        },
      }),
      category: DatadogAPIClient::V2::EventCategory::CHANGE,
      integration_id: DatadogAPIClient::V2::EventPayloadIntegrationId::CUSTOM_EVENTS,
      host: "test-host",
      message: "payment_processed feature flag has been enabled",
      tags: [
        "env:api_client_test",
      ],
      title: "payment_processed feature flag updated",
    }),
    type: DatadogAPIClient::V2::EventCreateRequestType::EVENT,
  }),
})
p api_instance.create_event(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Post an event returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_events::EventsAPI;
use datadog_api_client::datadogV2::model::ChangeEventCustomAttributes;
use datadog_api_client::datadogV2::model::ChangeEventCustomAttributesAuthor;
use datadog_api_client::datadogV2::model::ChangeEventCustomAttributesAuthorType;
use datadog_api_client::datadogV2::model::ChangeEventCustomAttributesChangedResource;
use datadog_api_client::datadogV2::model::ChangeEventCustomAttributesChangedResourceType;
use datadog_api_client::datadogV2::model::ChangeEventCustomAttributesImpactedResourcesItems;
use datadog_api_client::datadogV2::model::ChangeEventCustomAttributesImpactedResourcesItemsType;
use datadog_api_client::datadogV2::model::EventCategory;
use datadog_api_client::datadogV2::model::EventCreateRequest;
use datadog_api_client::datadogV2::model::EventCreateRequestPayload;
use datadog_api_client::datadogV2::model::EventCreateRequestType;
use datadog_api_client::datadogV2::model::EventPayload;
use datadog_api_client::datadogV2::model::EventPayloadAttributes;
use datadog_api_client::datadogV2::model::EventPayloadIntegrationId;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = EventCreateRequestPayload::new(EventCreateRequest::new(
        EventPayload::new(
            EventPayloadAttributes::ChangeEventCustomAttributes(Box::new(
                ChangeEventCustomAttributes::new(ChangeEventCustomAttributesChangedResource::new(
                    "fallback_payments_test".to_string(),
                    ChangeEventCustomAttributesChangedResourceType::FEATURE_FLAG,
                ))
                .author(ChangeEventCustomAttributesAuthor::new(
                    "example@datadog.com".to_string(),
                    ChangeEventCustomAttributesAuthorType::USER,
                ))
                .change_metadata(BTreeMap::from([(
                    "resource_link".to_string(),
                    Value::from("datadog.com/feature/fallback_payments_test"),
                )]))
                .impacted_resources(vec![
                    ChangeEventCustomAttributesImpactedResourcesItems::new(
                        "payments_api".to_string(),
                        ChangeEventCustomAttributesImpactedResourcesItemsType::SERVICE,
                    ),
                ])
                .new_value(BTreeMap::from([
                    ("enabled".to_string(), Value::from("True")),
                    ("percentage".to_string(), Value::from("50%")),
                ]))
                .prev_value(BTreeMap::from([
                    ("enabled".to_string(), Value::from("True")),
                    ("percentage".to_string(), Value::from("10%")),
                ])),
            )),
            EventCategory::CHANGE,
            "payment_processed feature flag updated".to_string(),
        )
        .aggregation_key("aggregation_key_123".to_string())
        .host("test-host".to_string())
        .integration_id(EventPayloadIntegrationId::CUSTOM_EVENTS)
        .message("payment_processed feature flag has been enabled".to_string())
        .tags(vec!["env:api_client_test".to_string()]),
        EventCreateRequestType::EVENT,
    ));
    let configuration = datadog::Configuration::new();
    let api = EventsAPI::with_config(configuration);
    let resp = api.create_event(body).await;
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
 * Post an event returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.EventsApi(configuration);

const params: v2.EventsApiCreateEventRequest = {
  body: {
    data: {
      attributes: {
        aggregationKey: "aggregation_key_123",
        attributes: {
          author: {
            name: "example@datadog.com",
            type: "user",
          },
          changeMetadata: {
            dd: "{'team': 'datadog_team', 'user_email': 'datadog@datadog.com', 'user_id': 'datadog_user_id', 'user_name': 'datadog_username'}",
            resource_link: "datadog.com/feature/fallback_payments_test",
          },
          changedResource: {
            name: "fallback_payments_test",
            type: "feature_flag",
          },
          impactedResources: [
            {
              name: "payments_api",
              type: "service",
            },
          ],
          newValue: {
            enabled: "True",
            percentage: "50%",
            rule: "{'datacenter': 'devcycle.us1.prod'}",
          },
          prevValue: {
            enabled: "True",
            percentage: "10%",
            rule: "{'datacenter': 'devcycle.us1.prod'}",
          },
        },
        category: "change",
        integrationId: "custom-events",
        host: "test-host",
        message: "payment_processed feature flag has been enabled",
        tags: ["env:api_client_test"],
        title: "payment_processed feature flag updated",
      },
      type: "event",
    },
  },
};

apiInstance
  .createEvent(params)
  .then((data: v2.EventCreateResponsePayload) => {
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

## Get an event{% #get-an-event %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/events/{event_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/events/{event_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/events/{event_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/events/{event_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/events/{event_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/events/{event_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/events/{event_id} |

### Overview



This endpoint allows you to query for event details.

**Note**: If the event you're querying contains markdown formatting of any kind, you may see characters such as `%`,`\`,`n` in your output.
This endpoint requires the `events_read` permission.
OAuth apps require the `events_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#events) to access this endpoint.



### Arguments

#### Path Parameters

| Name                       | Type    | Description          |
| -------------------------- | ------- | -------------------- |
| event_id [*required*] | integer | The ID of the event. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Object containing an event response.

| Parent field | Field            | Type     | Description                                                                                                                                                                                                                                                                 |
| ------------ | ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | event            | object   | Object representing an event.                                                                                                                                                                                                                                               |
| event        | alert_type       | enum     | If an alert event is enabled, set its type. For example, `error`, `warning`, `info`, `success`, `user_update`, `recommendation`, and `snapshot`. Allowed enum values: `error,warning,info,success,user_update,recommendation,snapshot`                                      |
| event        | date_happened    | int64    | POSIX timestamp of the event. Must be sent as an integer (that is no quotes). Limited to events up to 18 hours in the past and two hours in the future.                                                                                                                     |
| event        | device_name      | string   | A device name.                                                                                                                                                                                                                                                              |
| event        | host             | string   | Host name to associate with the event. Any tags associated with the host are also applied to this event.                                                                                                                                                                    |
| event        | id               | int64    | Integer ID of the event.                                                                                                                                                                                                                                                    |
| event        | id_str           | string   | Handling IDs as large 64-bit numbers can cause loss of accuracy issues with some programming languages. Instead, use the string representation of the Event ID to avoid losing accuracy.                                                                                    |
| event        | payload          | string   | Payload of the event.                                                                                                                                                                                                                                                       |
| event        | priority         | enum     | The priority of the event. For example, `normal` or `low`. Allowed enum values: `normal,low`                                                                                                                                                                                |
| event        | source_type_name | string   | The type of event being posted. Option examples include nagios, hudson, jenkins, my_apps, chef, puppet, git, bitbucket, etc. The list of standard source attribute values [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). |
| event        | tags             | [string] | A list of tags to apply to the event.                                                                                                                                                                                                                                       |
| event        | text             | string   | The body of the event. Limited to 4000 characters. The text supports markdown. To use markdown in the event text, start the text block with `%%% \n` and end the text block with `\n %%%`. Use `msg_text` with the Datadog Ruby library.                                    |
| event        | title            | string   | The event title.                                                                                                                                                                                                                                                            |
| event        | url              | string   | URL of the event.                                                                                                                                                                                                                                                           |
|              | status           | string   | A status.                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "event": {
    "alert_type": "info",
    "date_happened": "integer",
    "device_name": "string",
    "host": "string",
    "id": "integer",
    "id_str": "string",
    "payload": "{}",
    "priority": "normal",
    "source_type_name": "string",
    "tags": [
      "environment:test"
    ],
    "text": "Oh boy!",
    "title": "Did you hear the news today?",
    "url": "string"
  },
  "status": "string"
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
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
Item Not Found
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
                  \# Path parametersexport event_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/events/${event_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get an event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.events_api import EventsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.get_event(
        event_id=9223372036854775807,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get an event returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::EventsAPI.new
p api_instance.get_event(9223372036854775807)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

event_id = '1375909614428331251'
dog.get_event(event_id)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get an event returns "OK" response

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
	api := datadogV1.NewEventsApi(apiClient)
	resp, r, err := api.GetEvent(ctx, 9223372036854775807)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EventsApi.GetEvent`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `EventsApi.GetEvent`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get an event returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.EventsApi;
import com.datadog.api.client.v1.model.EventResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    EventsApi apiInstance = new EventsApi(defaultClient);

    try {
      EventResponse result = apiInstance.getEvent(9223372036854775807L);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#getEvent");
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

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.Event.get(2603387619536318140)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
##### 

```rust
// Get an event returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_events::EventsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = EventsAPI::with_config(configuration);
    let resp = api.get_event(9223372036854775807).await;
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
 * Get an event returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.EventsApi(configuration);

const params: v1.EventsApiGetEventRequest = {
  eventId: 9223372036854775807,
};

apiInstance
  .getEvent(params)
  .then((data: v1.EventResponse) => {
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

{% tab title="v2" %}

| Datadog site      | API endpoint                                               |
| ----------------- | ---------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/events/{event_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/events/{event_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/events/{event_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/events/{event_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/events/{event_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/events/{event_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/events/{event_id} |

### Overview

Get the details of an event by `event_id`. This endpoint requires the `events_read` permission.

OAuth apps require the `events_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#events) to access this endpoint.



### Arguments

#### Path Parameters

| Name                       | Type   | Description           |
| -------------------------- | ------ | --------------------- |
| event_id [*required*] | string | The UID of the event. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Get an event response.

| Parent field       | Field              | Type          | Description                                                                                                      |
| ------------------ | ------------------ | ------------- | ---------------------------------------------------------------------------------------------------------------- |
|                    | data               | object        | An event object.                                                                                                 |
| data               | attributes         | object        | Event attributes.                                                                                                |
| attributes         | attributes         |  <oneOf> | JSON object for category-specific attributes.                                                                    |
| attributes         | Option 1           | object        | Change event attributes.                                                                                         |
| Option 1           | aggregation_key    | string        | Aggregation key of the event.                                                                                    |
| Option 1           | author             | object        | The entity that made the change.                                                                                 |
| author             | name               | string        | The name of the user or system that made the change.                                                             |
| author             | type               | enum          | The type of the author. Allowed enum values: `user,system,api,automation`                                        |
| Option 1           | change_metadata    | object        | JSON object of change metadata.                                                                                  |
| Option 1           | changed_resource   | object        | A uniquely identified resource.                                                                                  |
| changed_resource   | name               | string        | The name of the changed resource.                                                                                |
| changed_resource   | type               | enum          | The type of the changed resource. Allowed enum values: `feature_flag,configuration`                              |
| Option 1           | evt                | object        | JSON object of event system attributes.                                                                          |
| evt                | category           | enum          | Event category identifying the type of event. Allowed enum values: `change,alert`                                |
| evt                | id                 | string        | Event identifier. This field is deprecated and will be removed in a future version. Use the `uid` field instead. |
| evt                | integration_id     | enum          | Integration ID sourced from integration manifests. Allowed enum values: `custom-events`                          |
| evt                | source_id          | int64         | The source type ID of the event.                                                                                 |
| evt                | uid                | string        | A unique identifier for the event. You can use this identifier to query or reference the event.                  |
| Option 1           | impacted_resources | [object]      | A list of resources impacted by this change.                                                                     |
| impacted_resources | name               | string        | The name of the impacted resource.                                                                               |
| impacted_resources | type               | enum          | The type of the impacted resource. Allowed enum values: `service`                                                |
| Option 1           | new_value          | object        | The new state of the changed resource.                                                                           |
| Option 1           | prev_value         | object        | The previous state of the changed resource.                                                                      |
| Option 1           | service            | string        | Service that triggered the event.                                                                                |
| Option 1           | timestamp          | int64         | POSIX timestamp of the event.                                                                                    |
| Option 1           | title              | string        | The title of the event.                                                                                          |
| attributes         | Option 2           | object        | Alert event attributes.                                                                                          |
| Option 2           | aggregation_key    | string        | Aggregation key of the event.                                                                                    |
| Option 2           | custom             | object        | JSON object of custom attributes.                                                                                |
| Option 2           | evt                | object        | JSON object of event system attributes.                                                                          |
| evt                | category           | enum          | Event category identifying the type of event. Allowed enum values: `change,alert`                                |
| evt                | id                 | string        | Event identifier. This field is deprecated and will be removed in a future version. Use the `uid` field instead. |
| evt                | integration_id     | enum          | Integration ID sourced from integration manifests. Allowed enum values: `custom-events`                          |
| evt                | source_id          | int64         | The source type ID of the event.                                                                                 |
| evt                | uid                | string        | A unique identifier for the event. You can use this identifier to query or reference the event.                  |
| Option 2           | links              | [object]      | The links related to the event.                                                                                  |
| links              | category           | enum          | The category of the link. Allowed enum values: `runbook,documentation,dashboard`                                 |
| links              | title              | string        | The display text of the link.                                                                                    |
| links              | url                | string        | The URL of the link.                                                                                             |
| Option 2           | priority           | enum          | The priority of the alert. Allowed enum values: `1,2,3,4,5`                                                      |
| Option 2           | service            | string        | Service that triggered the event.                                                                                |
| Option 2           | status             | enum          | The status of the alert. Allowed enum values: `warn,error,ok`                                                    |
| Option 2           | timestamp          | int64         | POSIX timestamp of the event.                                                                                    |
| Option 2           | title              | string        | The title of the event.                                                                                          |
| attributes         | message            | string        | Free-form text associated with the event.                                                                        |
| attributes         | tags               | [string]      | A list of tags associated with the event.                                                                        |
| attributes         | timestamp          | string        | Timestamp when the event occurred.                                                                               |
| data               | id                 | string        | The event's ID.                                                                                                  |
| data               | type               | string        | Entity type.                                                                                                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "attributes": {
        "aggregation_key": "aggregation-key",
        "author": {
          "name": "example@datadog.com",
          "type": "user"
        },
        "change_metadata": {
          "dd": {
            "team": "datadog_team",
            "user_email": "datadog@datadog.com",
            "user_id": "datadog_user_id",
            "user_name": "datadog_username"
          }
        },
        "changed_resource": {
          "name": "string",
          "type": "feature_flag"
        },
        "evt": {
          "category": "change",
          "id": "string",
          "integration_id": "custom-events",
          "source_id": "integer",
          "uid": "string"
        },
        "impacted_resources": [
          {
            "name": "service-name",
            "type": "service"
          }
        ],
        "new_value": {
          "enabled": true,
          "percentage": "50%",
          "rule": {
            "datacenter": "devcycle.us1.prod"
          }
        },
        "prev_value": {
          "enabled": true,
          "percentage": "10%",
          "rule": {
            "datacenter": "devcycle.us1.prod"
          }
        },
        "service": "service-name",
        "timestamp": 175019386627,
        "title": "The event title"
      },
      "message": "The event message",
      "tags": [
        "env:api_client_test"
      ],
      "timestamp": "2017-01-15T01:30:15.010000Z"
    },
    "id": "",
    "type": "event"
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

{% tab title="401" %}
Unauthorized
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
Forbidden
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport event_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/events/${event_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get an event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.get_event(
        event_id="AZeF-nTCAABzkAgGXzYPtgAA",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get an event returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::EventsAPI.new
p api_instance.get_event("AZeF-nTCAABzkAgGXzYPtgAA")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get an event returns "OK" response

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
	api := datadogV2.NewEventsApi(apiClient)
	resp, r, err := api.GetEvent(ctx, "AZeF-nTCAABzkAgGXzYPtgAA")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EventsApi.GetEvent`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `EventsApi.GetEvent`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get an event returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.EventsApi;
import com.datadog.api.client.v2.model.V2EventResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    EventsApi apiInstance = new EventsApi(defaultClient);

    try {
      V2EventResponse result = apiInstance.getEvent("AZeF-nTCAABzkAgGXzYPtgAA");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#getEvent");
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
// Get an event returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_events::EventsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = EventsAPI::with_config(configuration);
    let resp = api.get_event("AZeF-nTCAABzkAgGXzYPtgAA".to_string()).await;
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
 * Get an event returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.EventsApi(configuration);

const params: v2.EventsApiGetEventRequest = {
  eventId: "AZeF-nTCAABzkAgGXzYPtgAA",
};

apiInstance
  .getEvent(params)
  .then((data: v2.V2EventResponse) => {
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

## Search events{% #search-events %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/events/search |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/events/search |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/events/search      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/events/search      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/events/search     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/events/search |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/events/search |

### Overview



List endpoint returns events that match an events search query. [Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).

Use this endpoint to build complex events filtering and search.
This endpoint requires the `events_read` permission.


### Request

#### Body Data 



{% tab title="Model" %}

| Parent field | Field      | Type   | Description                                                                                                                               |
| ------------ | ---------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
|              | filter     | object | The search and filter query settings.                                                                                                     |
| filter       | from       | string | The minimum time for the requested events. Supports date math and regular timestamps in milliseconds.                                     |
| filter       | query      | string | The search query following the event search syntax.                                                                                       |
| filter       | to         | string | The maximum time for the requested events. Supports date math and regular timestamps in milliseconds.                                     |
|              | options    | object | The global query options that are used. Either provide a timezone or a time offset but not both, otherwise the query fails.               |
| options      | timeOffset | int64  | The time offset to apply to the query in seconds.                                                                                         |
| options      | timezone   | string | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York). |
|              | page       | object | Pagination settings.                                                                                                                      |
| page         | cursor     | string | The returned paging point to use to get the next results.                                                                                 |
| page         | limit      | int32  | The maximum number of logs in the response.                                                                                               |
|              | sort       | enum   | The sort parameters when querying events. Allowed enum values: `timestamp,-timestamp`                                                     |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "filter": {
    "query": "datadog-agent",
    "from": "2020-09-17T11:48:36+01:00",
    "to": "2020-09-17T12:48:36+01:00"
  },
  "sort": "timestamp",
  "page": {
    "limit": 5
  }
}
```

##### 

```json
{
  "filter": {
    "from": "now-15m",
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The response object with all events matching the request and pagination information.

| Parent field | Field            | Type      | Description                                                                                                                                                                                                                                                                      |
| ------------ | ---------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data             | [object]  | An array of events matching the request.                                                                                                                                                                                                                                         |
| data         | attributes       | object    | The object description of an event response attribute.                                                                                                                                                                                                                           |
| attributes   | attributes       | object    | Object description of attributes from your event.                                                                                                                                                                                                                                |
| attributes   | aggregation_key  | string    | Aggregation key of the event.                                                                                                                                                                                                                                                    |
| attributes   | date_happened    | int64     | POSIX timestamp of the event. Must be sent as an integer (no quotation marks). Limited to events no older than 18 hours.                                                                                                                                                         |
| attributes   | device_name      | string    | A device name.                                                                                                                                                                                                                                                                   |
| attributes   | duration         | int64     | The duration between the triggering of the event and its recovery in nanoseconds.                                                                                                                                                                                                |
| attributes   | event_object     | string    | The event title.                                                                                                                                                                                                                                                                 |
| attributes   | evt              | object    | The metadata associated with a request.                                                                                                                                                                                                                                          |
| evt          | id               | string    | Event ID.                                                                                                                                                                                                                                                                        |
| evt          | name             | string    | The event name.                                                                                                                                                                                                                                                                  |
| evt          | source_id        | int64     | Event source ID.                                                                                                                                                                                                                                                                 |
| evt          | type             | string    | Event type.                                                                                                                                                                                                                                                                      |
| attributes   | hostname         | string    | Host name to associate with the event. Any tags associated with the host are also applied to this event.                                                                                                                                                                         |
| attributes   | monitor          | object    | Attributes from the monitor that triggered the event.                                                                                                                                                                                                                            |
| monitor      | created_at       | int64     | The POSIX timestamp of the monitor's creation in nanoseconds.                                                                                                                                                                                                                    |
| monitor      | group_status     | int32     | Monitor group status used when there is no `result_groups`.                                                                                                                                                                                                                      |
| monitor      | groups           | [string]  | Groups to which the monitor belongs.                                                                                                                                                                                                                                             |
| monitor      | id               | int64     | The monitor ID.                                                                                                                                                                                                                                                                  |
| monitor      | message          | string    | The monitor message.                                                                                                                                                                                                                                                             |
| monitor      | modified         | int64     | The monitor's last-modified timestamp.                                                                                                                                                                                                                                           |
| monitor      | name             | string    | The monitor name.                                                                                                                                                                                                                                                                |
| monitor      | query            | string    | The query that triggers the alert.                                                                                                                                                                                                                                               |
| monitor      | tags             | [string]  | A list of tags attached to the monitor.                                                                                                                                                                                                                                          |
| monitor      | templated_name   | string    | The templated name of the monitor before resolving any template variables.                                                                                                                                                                                                       |
| monitor      | type             | string    | The monitor type.                                                                                                                                                                                                                                                                |
| attributes   | monitor_groups   | [string]  | List of groups referred to in the event.                                                                                                                                                                                                                                         |
| attributes   | monitor_id       | int64     | ID of the monitor that triggered the event. When an event isn't related to a monitor, this field is empty.                                                                                                                                                                       |
| attributes   | priority         | enum      | The priority of the event's monitor. For example, `normal` or `low`. Allowed enum values: `normal,low`                                                                                                                                                                           |
| attributes   | related_event_id | int64     | Related event ID.                                                                                                                                                                                                                                                                |
| attributes   | service          | string    | Service that triggered the event.                                                                                                                                                                                                                                                |
| attributes   | source_type_name | string    | The type of event being posted. For example, `nagios`, `hudson`, `jenkins`, `my_apps`, `chef`, `puppet`, `git` or `bitbucket`. The list of standard source attribute values is [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). |
| attributes   | sourcecategory   | string    | Identifier for the source of the event, such as a monitor alert, an externally-submitted event, or an integration.                                                                                                                                                               |
| attributes   | status           | enum      | If an alert event is enabled, its status is one of the following: `failure`, `error`, `warning`, `info`, `success`, `user_update`, `recommendation`, or `snapshot`. Allowed enum values: `failure,error,warning,info,success,user_update,recommendation,snapshot`                |
| attributes   | tags             | [string]  | A list of tags to apply to the event.                                                                                                                                                                                                                                            |
| attributes   | timestamp        | int64     | POSIX timestamp of your event in milliseconds.                                                                                                                                                                                                                                   |
| attributes   | title            | string    | The event title.                                                                                                                                                                                                                                                                 |
| attributes   | message          | string    | The message of the event.                                                                                                                                                                                                                                                        |
| attributes   | tags             | [string]  | An array of tags associated with the event.                                                                                                                                                                                                                                      |
| attributes   | timestamp        | date-time | The timestamp of the event.                                                                                                                                                                                                                                                      |
| data         | id               | string    | the unique ID of the event.                                                                                                                                                                                                                                                      |
| data         | type             | enum      | Type of the event. Allowed enum values: `event`                                                                                                                                                                                                                                  |
|              | links            | object    | Links attributes.                                                                                                                                                                                                                                                                |
| links        | next             | string    | Link for the next set of results. Note that the request can also be made using the POST endpoint.                                                                                                                                                                                |
|              | meta             | object    | The metadata associated with a request.                                                                                                                                                                                                                                          |
| meta         | elapsed          | int64     | The time elapsed in milliseconds.                                                                                                                                                                                                                                                |
| meta         | page             | object    | Pagination attributes.                                                                                                                                                                                                                                                           |
| page         | after            | string    | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of the `page[cursor]`.                                                                                                                                    |
| meta         | request_id       | string    | The identifier of the request.                                                                                                                                                                                                                                                   |
| meta         | status           | string    | The request status.                                                                                                                                                                                                                                                              |
| meta         | warnings         | [object]  | A list of warnings (non-fatal errors) encountered. Partial results might be returned if warnings are present in the response.                                                                                                                                                    |
| warnings     | code             | string    | A unique code for this type of warning.                                                                                                                                                                                                                                          |
| warnings     | detail           | string    | A detailed explanation of this specific warning.                                                                                                                                                                                                                                 |
| warnings     | title            | string    | A short human-readable summary of the warning.                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "attributes": {
          "aggregation_key": "string",
          "date_happened": "integer",
          "device_name": "string",
          "duration": "integer",
          "event_object": "Did you hear the news today?",
          "evt": {
            "id": "6509751066204996294",
            "name": "string",
            "source_id": 36,
            "type": "error_tracking_alert"
          },
          "hostname": "string",
          "monitor": {
            "created_at": 1646318692000,
            "group_status": "integer",
            "groups": [],
            "id": "integer",
            "message": "string",
            "modified": "integer",
            "name": "string",
            "query": "string",
            "tags": [
              "environment:test"
            ],
            "templated_name": "string",
            "type": "string"
          },
          "monitor_groups": [],
          "monitor_id": "integer",
          "priority": "normal",
          "related_event_id": "integer",
          "service": "datadog-api",
          "source_type_name": "string",
          "sourcecategory": "string",
          "status": "info",
          "tags": [
            "environment:test"
          ],
          "timestamp": 1652274265000,
          "title": "Oh boy!"
        },
        "message": "string",
        "tags": [
          "team:A"
        ],
        "timestamp": "2019-01-02T09:42:36.320Z"
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "event"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/events?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
  },
  "meta": {
    "elapsed": 132,
    "page": {
      "after": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
    },
    "request_id": "MWlFUjVaWGZTTTZPYzM0VXp1OXU2d3xLSVpEMjZKQ0VKUTI0dEYtM3RSOFVR",
    "status": "done",
    "warnings": [
      {
        "code": "unknown_index",
        "detail": "indexes: foo, bar",
        "title": "One or several indexes are missing or invalid. Results hold data from the other indexes."
      }
    ]
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
Not Authorized
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "query": "datadog-agent",
    "from": "2020-09-17T11:48:36+01:00",
    "to": "2020-09-17T12:48:36+01:00"
  },
  "sort": "timestamp",
  "page": {
    "limit": 5
  }
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "from": "now-15m",
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
EOF
                        
##### 

```go
// Search events returns "OK" response

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
	body := datadogV2.EventsListRequest{
		Filter: &datadogV2.EventsQueryFilter{
			Query: datadog.PtrString("datadog-agent"),
			From:  datadog.PtrString("2020-09-17T11:48:36+01:00"),
			To:    datadog.PtrString("2020-09-17T12:48:36+01:00"),
		},
		Sort: datadogV2.EVENTSSORT_TIMESTAMP_ASCENDING.Ptr(),
		Page: &datadogV2.EventsRequestPage{
			Limit: datadog.PtrInt32(5),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewEventsApi(apiClient)
	resp, r, err := api.SearchEvents(ctx, *datadogV2.NewSearchEventsOptionalParameters().WithBody(body))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EventsApi.SearchEvents`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `EventsApi.SearchEvents`:\n%s\n", responseContent)
}
```

##### 

```go
// Search events returns "OK" response with pagination

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
	body := datadogV2.EventsListRequest{
		Filter: &datadogV2.EventsQueryFilter{
			From: datadog.PtrString("now-15m"),
			To:   datadog.PtrString("now"),
		},
		Options: &datadogV2.EventsQueryOptions{
			Timezone: datadog.PtrString("GMT"),
		},
		Page: &datadogV2.EventsRequestPage{
			Limit: datadog.PtrInt32(2),
		},
		Sort: datadogV2.EVENTSSORT_TIMESTAMP_ASCENDING.Ptr(),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewEventsApi(apiClient)
	resp, _ := api.SearchEventsWithPagination(ctx, *datadogV2.NewSearchEventsOptionalParameters().WithBody(body))

	for paginationResult := range resp {
		if paginationResult.Error != nil {
			fmt.Fprintf(os.Stderr, "Error when calling `EventsApi.SearchEvents`: %v\n", paginationResult.Error)
		}
		responseContent, _ := json.MarshalIndent(paginationResult.Item, "", "  ")
		fmt.Fprintf(os.Stdout, "%s\n", responseContent)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Search events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.EventsApi;
import com.datadog.api.client.v2.api.EventsApi.SearchEventsOptionalParameters;
import com.datadog.api.client.v2.model.EventsListRequest;
import com.datadog.api.client.v2.model.EventsListResponse;
import com.datadog.api.client.v2.model.EventsQueryFilter;
import com.datadog.api.client.v2.model.EventsRequestPage;
import com.datadog.api.client.v2.model.EventsSort;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    EventsApi apiInstance = new EventsApi(defaultClient);

    EventsListRequest body =
        new EventsListRequest()
            .filter(
                new EventsQueryFilter()
                    .query("datadog-agent")
                    .from("2020-09-17T11:48:36+01:00")
                    .to("2020-09-17T12:48:36+01:00"))
            .sort(EventsSort.TIMESTAMP_ASCENDING)
            .page(new EventsRequestPage().limit(5));

    try {
      EventsListResponse result =
          apiInstance.searchEvents(new SearchEventsOptionalParameters().body(body));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#searchEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

##### 

```java
// Search events returns "OK" response with pagination

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.PaginationIterable;
import com.datadog.api.client.v2.api.EventsApi;
import com.datadog.api.client.v2.api.EventsApi.SearchEventsOptionalParameters;
import com.datadog.api.client.v2.model.EventResponse;
import com.datadog.api.client.v2.model.EventsListRequest;
import com.datadog.api.client.v2.model.EventsQueryFilter;
import com.datadog.api.client.v2.model.EventsQueryOptions;
import com.datadog.api.client.v2.model.EventsRequestPage;
import com.datadog.api.client.v2.model.EventsSort;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    EventsApi apiInstance = new EventsApi(defaultClient);

    EventsListRequest body =
        new EventsListRequest()
            .filter(new EventsQueryFilter().from("now-15m").to("now"))
            .options(new EventsQueryOptions().timezone("GMT"))
            .page(new EventsRequestPage().limit(2))
            .sort(EventsSort.TIMESTAMP_ASCENDING);

    try {
      PaginationIterable<EventResponse> iterable =
          apiInstance.searchEventsWithPagination(new SearchEventsOptionalParameters().body(body));

      for (EventResponse item : iterable) {
        System.out.println(item);
      }
    } catch (RuntimeException e) {
      System.err.println("Exception when calling EventsApi#searchEventsWithPagination");
      System.err.println("Reason: " + e.getMessage());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
##### 

```python
"""
Search events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.events_list_request import EventsListRequest
from datadog_api_client.v2.model.events_query_filter import EventsQueryFilter
from datadog_api_client.v2.model.events_request_page import EventsRequestPage
from datadog_api_client.v2.model.events_sort import EventsSort

body = EventsListRequest(
    filter=EventsQueryFilter(
        query="datadog-agent",
        _from="2020-09-17T11:48:36+01:00",
        to="2020-09-17T12:48:36+01:00",
    ),
    sort=EventsSort.TIMESTAMP_ASCENDING,
    page=EventsRequestPage(
        limit=5,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.search_events(body=body)

    print(response)
```

##### 

```python
"""
Search events returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.events_list_request import EventsListRequest
from datadog_api_client.v2.model.events_query_filter import EventsQueryFilter
from datadog_api_client.v2.model.events_query_options import EventsQueryOptions
from datadog_api_client.v2.model.events_request_page import EventsRequestPage
from datadog_api_client.v2.model.events_sort import EventsSort

body = EventsListRequest(
    filter=EventsQueryFilter(
        _from="now-15m",
        to="now",
    ),
    options=EventsQueryOptions(
        timezone="GMT",
    ),
    page=EventsRequestPage(
        limit=2,
    ),
    sort=EventsSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    items = api_instance.search_events_with_pagination(body=body)
    for item in items:
        print(item)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Search events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::EventsAPI.new

body = DatadogAPIClient::V2::EventsListRequest.new({
  filter: DatadogAPIClient::V2::EventsQueryFilter.new({
    query: "datadog-agent",
    from: "2020-09-17T11:48:36+01:00",
    to: "2020-09-17T12:48:36+01:00",
  }),
  sort: DatadogAPIClient::V2::EventsSort::TIMESTAMP_ASCENDING,
  page: DatadogAPIClient::V2::EventsRequestPage.new({
    limit: 5,
  }),
})
opts = {
  body: body,
}
p api_instance.search_events(opts)
```

##### 

```ruby
# Search events returns "OK" response with pagination

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::EventsAPI.new

body = DatadogAPIClient::V2::EventsListRequest.new({
  filter: DatadogAPIClient::V2::EventsQueryFilter.new({
    from: "now-15m",
    to: "now",
  }),
  options: DatadogAPIClient::V2::EventsQueryOptions.new({
    timezone: "GMT",
  }),
  page: DatadogAPIClient::V2::EventsRequestPage.new({
    limit: 2,
  }),
  sort: DatadogAPIClient::V2::EventsSort::TIMESTAMP_ASCENDING,
})
opts = {
  body: body,
}
api_instance.search_events_with_pagination(opts) { |item| puts item }
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Search events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_events::EventsAPI;
use datadog_api_client::datadogV2::api_events::SearchEventsOptionalParams;
use datadog_api_client::datadogV2::model::EventsListRequest;
use datadog_api_client::datadogV2::model::EventsQueryFilter;
use datadog_api_client::datadogV2::model::EventsRequestPage;
use datadog_api_client::datadogV2::model::EventsSort;

#[tokio::main]
async fn main() {
    let body = EventsListRequest::new()
        .filter(
            EventsQueryFilter::new()
                .from("2020-09-17T11:48:36+01:00".to_string())
                .query("datadog-agent".to_string())
                .to("2020-09-17T12:48:36+01:00".to_string()),
        )
        .page(EventsRequestPage::new().limit(5))
        .sort(EventsSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = EventsAPI::with_config(configuration);
    let resp = api
        .search_events(SearchEventsOptionalParams::default().body(body))
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Search events returns "OK" response with pagination
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_events::EventsAPI;
use datadog_api_client::datadogV2::api_events::SearchEventsOptionalParams;
use datadog_api_client::datadogV2::model::EventsListRequest;
use datadog_api_client::datadogV2::model::EventsQueryFilter;
use datadog_api_client::datadogV2::model::EventsQueryOptions;
use datadog_api_client::datadogV2::model::EventsRequestPage;
use datadog_api_client::datadogV2::model::EventsSort;
use futures_util::pin_mut;
use futures_util::stream::StreamExt;

#[tokio::main]
async fn main() {
    let body = EventsListRequest::new()
        .filter(
            EventsQueryFilter::new()
                .from("now-15m".to_string())
                .to("now".to_string()),
        )
        .options(EventsQueryOptions::new().timezone("GMT".to_string()))
        .page(EventsRequestPage::new().limit(2))
        .sort(EventsSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = EventsAPI::with_config(configuration);
    let response =
        api.search_events_with_pagination(SearchEventsOptionalParams::default().body(body));
    pin_mut!(response);
    while let Some(resp) = response.next().await {
        if let Ok(value) = resp {
            println!("{:#?}", value);
        } else {
            println!("{:#?}", resp.unwrap_err());
        }
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
##### 

```typescript
/**
 * Search events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.EventsApi(configuration);

const params: v2.EventsApiSearchEventsRequest = {
  body: {
    filter: {
      query: "datadog-agent",
      from: "2020-09-17T11:48:36+01:00",
      to: "2020-09-17T12:48:36+01:00",
    },
    sort: "timestamp",
    page: {
      limit: 5,
    },
  },
};

apiInstance
  .searchEvents(params)
  .then((data: v2.EventsListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Search events returns "OK" response with pagination
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.EventsApi(configuration);

const params: v2.EventsApiSearchEventsRequest = {
  body: {
    filter: {
      from: "now-15m",
      to: "now",
    },
    options: {
      timezone: "GMT",
    },
    page: {
      limit: 2,
    },
    sort: "timestamp",
  },
};

(async () => {
  try {
    for await (const item of apiInstance.searchEventsWithPagination(params)) {
      console.log(item);
    }
  } catch (error) {
    console.error(error);
  }
})();
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
