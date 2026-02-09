# Source: https://docs.datadoghq.com/api/latest/downtimes.md

---
title: Downtimes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Downtimes
---

# Downtimes

[Downtiming](https://docs.datadoghq.com/monitors/notify/downtimes) gives you greater control over monitor notifications by allowing you to globally exclude scopes from alerting. Downtime settings, which can be scheduled with start and end times, prevent all alerting related to specified Datadog tags.

**Note:** `curl` commands require [url encoding](https://curl.se/docs/url-syntax.html).

## Get all downtimes{% #get-all-downtimes %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                      |
| ----------------- | ------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/downtime |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/downtime |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/downtime      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/downtime      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/downtime     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/downtime |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/downtime |

### Overview

Get all scheduled downtimes. **Note:** This endpoint has been deprecated. Please use v2 endpoints. This endpoint requires the `monitors_read` permission.

OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Arguments

#### Query Strings

| Name         | Type    | Description                                                     |
| ------------ | ------- | --------------------------------------------------------------- |
| current_only | boolean | Only return downtimes that are active when the request is made. |
| with_creator | boolean | Return creator information.                                     |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                            | Type     | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | -------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
|              | active_child                     | object   | The downtime object definition of the active child for the original parent recurring downtime. This field will only exist on recurring downtimes.                                                                                                                                                                                                                |
| active_child | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
| active_child | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
| active_child | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
| active_child | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
| active_child | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
| active_child | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
| active_child | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
| active_child | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
| active_child | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
| active_child | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
| active_child | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
| active_child | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
| active_child | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
| active_child | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
| active_child | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
| active_child | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
| active_child | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
| active_child | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
| active_child | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |
|              | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
|              | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
|              | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
|              | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
|              | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
|              | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
|              | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
|              | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
|              | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
|              | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
|              | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
|              | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
|              | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
|              | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
|              | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
|              | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
|              | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
|              | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "active": true,
  "active_child": {
    "active": true,
    "canceled": 1412799983,
    "creator_id": 123456,
    "disabled": false,
    "downtime_type": 2,
    "end": 1412793983,
    "id": 1626,
    "message": "Message on the downtime",
    "monitor_id": 123456,
    "monitor_tags": [
      "*"
    ],
    "mute_first_recovery_notification": false,
    "notify_end_states": [
      "alert",
      "no data",
      "warn"
    ],
    "notify_end_types": [
      "canceled",
      "expired"
    ],
    "parent_id": 123,
    "recurrence": {
      "period": 1,
      "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
      "type": "weeks",
      "until_date": 1447786293,
      "until_occurrences": 2,
      "week_days": [
        "Mon",
        "Tue"
      ]
    },
    "scope": [
      "env:staging"
    ],
    "start": 1412792983,
    "timezone": "America/New_York",
    "updater_id": 123456
  },
  "canceled": 1412799983,
  "creator_id": 123456,
  "disabled": false,
  "downtime_type": 2,
  "end": 1412793983,
  "id": 1625,
  "message": "Message on the downtime",
  "monitor_id": 123456,
  "monitor_tags": [
    "*"
  ],
  "mute_first_recovery_notification": false,
  "notify_end_states": [
    "alert",
    "no data",
    "warn"
  ],
  "notify_end_types": [
    "canceled",
    "expired"
  ],
  "parent_id": 123,
  "recurrence": {
    "period": 1,
    "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
    "type": "weeks",
    "until_date": 1447786293,
    "until_occurrences": 2,
    "week_days": [
      "Mon",
      "Tue"
    ]
  },
  "scope": [
    "env:staging"
  ],
  "start": 1412792983,
  "timezone": "America/New_York",
  "updater_id": 123456
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/downtime" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all downtimes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.list_downtimes(
        with_creator=True,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get all downtimes returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DowntimesAPI.new
opts = {
  with_creator: true,
}
p api_instance.list_downtimes(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```ruby
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Get all downtimes
dog.get_all_downtimes
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Get all downtimes returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_downtimes::DowntimesAPI;
use datadog_api_client::datadogV1::api_downtimes::ListDowntimesOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api
        .list_downtimes(ListDowntimesOptionalParams::default().with_creator(true))
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

```go
// Get all downtimes returns "OK" response

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
	api := datadogV1.NewDowntimesApi(apiClient)
	resp, r, err := api.ListDowntimes(ctx, *datadogV1.NewListDowntimesOptionalParameters().WithWithCreator(true))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.ListDowntimes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.ListDowntimes`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get all downtimes returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DowntimesApi;
import com.datadog.api.client.v1.api.DowntimesApi.ListDowntimesOptionalParameters;
import com.datadog.api.client.v1.model.Downtime;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    try {
      List<Downtime> result =
          apiInstance.listDowntimes(new ListDowntimesOptionalParameters().withCreator(true));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#listDowntimes");
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

# Get all downtimes
print(api.Downtime.get_all())
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
##### 

```typescript
/**
 * Get all downtimes returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DowntimesApi(configuration);

const params: v1.DowntimesApiListDowntimesRequest = {
  withCreator: true,
};

apiInstance
  .listDowntimes(params)
  .then((data: v1.Downtime[]) => {
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

| Datadog site      | API endpoint                                      |
| ----------------- | ------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/downtime |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/downtime |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/downtime      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/downtime      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/downtime     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/downtime |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/downtime |

### Overview

Get all scheduled downtimes. This endpoint requires the `monitors_downtime` permission.

OAuth apps require the `monitors_downtime` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Arguments

#### Query Strings

| Name         | Type    | Description                                                                                                                                       |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| current_only | boolean | Only return downtimes that are active when the request is made.                                                                                   |
| include      | string  | Comma-separated list of resource paths for related resources to include in the response. Supported resource paths are `created_by` and `monitor`. |
| page[offset] | integer | Specific offset to use as the beginning of the returned page.                                                                                     |
| page[limit]  | integer | Maximum number of downtimes in the response.                                                                                                      |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for retrieving all downtimes.

| Parent field       | Field                            | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | -------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                             | [object]        | An array of downtimes.                                                                                                                                                                                                                                                                                                                                                                        |
| data               | attributes                       | object          | Downtime details.                                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | canceled                         | date-time       | Time that the downtime was canceled.                                                                                                                                                                                                                                                                                                                                                          |
| attributes         | created                          | date-time       | Creation time of the downtime.                                                                                                                                                                                                                                                                                                                                                                |
| attributes         | display_timezone                 | string          | The timezone in which to display the downtime's start and end times in Datadog applications. This is not used as an offset for scheduling.                                                                                                                                                                                                                                                    |
| attributes         | message                          | string          | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                                                |
| attributes         | modified                         | date-time       | Time that the downtime was last modified.                                                                                                                                                                                                                                                                                                                                                     |
| attributes         | monitor_identifier               |  <oneOf>   | Monitor identifier for the downtime.                                                                                                                                                                                                                                                                                                                                                          |
| monitor_identifier | Option 1                         | object          | Object of the monitor identifier.                                                                                                                                                                                                                                                                                                                                                             |
| Option 1           | monitor_id [*required*]     | int64           | ID of the monitor to prevent notifications.                                                                                                                                                                                                                                                                                                                                                   |
| monitor_identifier | Option 2                         | object          | Object of the monitor tags.                                                                                                                                                                                                                                                                                                                                                                   |
| Option 2           | monitor_tags [*required*]   | [string]        | A list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match **all** provided monitor tags. Setting `monitor_tags` to `[*]` configures the downtime to mute all monitors for the given scope. |
| attributes         | mute_first_recovery_notification | boolean         | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                                                         |
| attributes         | notify_end_states                | [string]        | States that will trigger a monitor notification when the `notify_end_types` action occurs.                                                                                                                                                                                                                                                                                                    |
| attributes         | notify_end_types                 | [string]        | Actions that will trigger a monitor notification if the downtime is in the `notify_end_types` state.                                                                                                                                                                                                                                                                                          |
| attributes         | schedule                         |  <oneOf>   | The schedule that defines when the monitor starts, stops, and recurs. There are two types of schedules: one-time and recurring. Recurring schedules may have up to five RRULE-based recurrences. If no schedules are provided, the downtime will begin immediately and never end.                                                                                                             |
| schedule           | Option 1                         | object          | A recurring downtime schedule definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1           | current_downtime                 | object          | The most recent actual start and end dates for a recurring downtime. For a canceled downtime, this is the previously occurring downtime. For active downtimes, this is the ongoing downtime, and for scheduled downtimes it is the upcoming downtime.                                                                                                                                         |
| current_downtime   | end                              | date-time       | The end of the current downtime.                                                                                                                                                                                                                                                                                                                                                              |
| current_downtime   | start                            | date-time       | The start of the current downtime.                                                                                                                                                                                                                                                                                                                                                            |
| Option 1           | recurrences [*required*]    | [object]        | A list of downtime recurrences.                                                                                                                                                                                                                                                                                                                                                               |
| recurrences        | duration                         | string          | The length of the downtime. Must begin with an integer and end with one of 'm', 'h', d', or 'w'.                                                                                                                                                                                                                                                                                              |
| recurrences        | rrule                            | string          | The `RRULE` standard for defining recurring events. For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.                                                                         | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api). |
| recurrences        | start                            | string          | ISO-8601 Datetime to start the downtime. Must not include a UTC offset. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                        |
| Option 1           | timezone                         | string          | The timezone in which to schedule the downtime. This affects recurring start and end dates. Must match `display_timezone`.                                                                                                                                                                                                                                                                    |
| schedule           | Option 2                         | object          | A one-time downtime definition.                                                                                                                                                                                                                                                                                                                                                               |
| Option 2           | end                              | date-time       | ISO-8601 Datetime to end the downtime.                                                                                                                                                                                                                                                                                                                                                        |
| Option 2           | start [*required*]          | date-time       | ISO-8601 Datetime to start the downtime.                                                                                                                                                                                                                                                                                                                                                      |
| attributes         | scope                            | string          | The scope to which the downtime applies. Must follow the [common search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/).                                                                                                                                                                                                                                                     |
| attributes         | status                           | enum            | The current status of the downtime. Allowed enum values: `active,canceled,ended,scheduled`                                                                                                                                                                                                                                                                                                    |
| data               | id                               | string          | The downtime ID.                                                                                                                                                                                                                                                                                                                                                                              |
| data               | relationships                    | object          | All relationships associated with downtime.                                                                                                                                                                                                                                                                                                                                                   |
| relationships      | created_by                       | object          | The user who created the downtime.                                                                                                                                                                                                                                                                                                                                                            |
| created_by         | data                             | object          | Data for the user who created the downtime.                                                                                                                                                                                                                                                                                                                                                   |
| data               | id                               | string          | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                                              |
| data               | type                             | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| relationships      | monitor                          | object          | The monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                                       |
| monitor            | data                             | object          | Data for the monitor.                                                                                                                                                                                                                                                                                                                                                                         |
| data               | id                               | string          | Monitor ID of the downtime.                                                                                                                                                                                                                                                                                                                                                                   |
| data               | type                             | enum            | Monitor resource type. Allowed enum values: `monitors`                                                                                                                                                                                                                                                                                                                                        |
| data               | type                             | enum            | Downtime resource type. Allowed enum values: `downtime`                                                                                                                                                                                                                                                                                                                                       |
|                    | included                         | [ <oneOf>] | Array of objects related to the downtimes.                                                                                                                                                                                                                                                                                                                                                    |
| included           | Option 1                         | object          | User object returned by the API.                                                                                                                                                                                                                                                                                                                                                              |
| Option 1           | attributes                       | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                                                                                                                |
| attributes         | created_at                       | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                                                                                                                    |
| attributes         | disabled                         | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                                                                                                                 |
| attributes         | email                            | string          | Email of the user.                                                                                                                                                                                                                                                                                                                                                                            |
| attributes         | handle                           | string          | Handle of the user.                                                                                                                                                                                                                                                                                                                                                                           |
| attributes         | icon                             | string          | URL of the user's icon.                                                                                                                                                                                                                                                                                                                                                                       |
| attributes         | last_login_time                  | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | mfa_enabled                      | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                                                                                                                      |
| attributes         | modified_at                      | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                                                                                                                         |
| attributes         | name                             | string          | Name of the user.                                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | service_account                  | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                                                                                                                        |
| attributes         | status                           | string          | Status of the user.                                                                                                                                                                                                                                                                                                                                                                           |
| attributes         | title                            | string          | Title of the user.                                                                                                                                                                                                                                                                                                                                                                            |
| attributes         | verified                         | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                                                                                                                 |
| Option 1           | id                               | string          | ID of the user.                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1           | relationships                    | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                                                                                                                         |
| relationships      | org                              | object          | Relationship to an organization.                                                                                                                                                                                                                                                                                                                                                              |
| org                | data [*required*]           | object          | Relationship to organization object.                                                                                                                                                                                                                                                                                                                                                          |
| data               | id [*required*]             | string          | ID of the organization.                                                                                                                                                                                                                                                                                                                                                                       |
| data               | type [*required*]           | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                                                                                                                      |
| relationships      | other_orgs                       | object          | Relationship to organizations.                                                                                                                                                                                                                                                                                                                                                                |
| other_orgs         | data [*required*]           | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                                                                                                                        |
| data               | id [*required*]             | string          | ID of the organization.                                                                                                                                                                                                                                                                                                                                                                       |
| data               | type [*required*]           | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                                                                                                                      |
| relationships      | other_users                      | object          | Relationship to users.                                                                                                                                                                                                                                                                                                                                                                        |
| other_users        | data [*required*]           | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                                                                                                                |
| data               | id [*required*]             | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                                                                                                                 |
| data               | type [*required*]           | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| relationships      | roles                            | object          | Relationship to roles.                                                                                                                                                                                                                                                                                                                                                                        |
| roles              | data                             | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                                                                                                                 |
| data               | id                               | string          | The unique identifier of the role.                                                                                                                                                                                                                                                                                                                                                            |
| data               | type                             | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                                                                                                                      |
| Option 1           | type                             | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| included           | Option 2                         | object          | Information about the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                     |
| Option 2           | attributes                       | object          | Attributes of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                         |
| attributes         | name                             | string          | The name of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                           |
| Option 2           | id                               | int64           | ID of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                                 |
| Option 2           | type                             | enum            | Monitor resource type. Allowed enum values: `monitors`                                                                                                                                                                                                                                                                                                                                        |
|                    | meta                             | object          | Pagination metadata returned by the API.                                                                                                                                                                                                                                                                                                                                                      |
| meta               | page                             | object          | Object containing the total filtered count.                                                                                                                                                                                                                                                                                                                                                   |
| page               | total_filtered_count             | int64           | Total count of elements matched by the filter.                                                                                                                                                                                                                                                                                                                                                |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "canceled": "2020-01-02T03:04:05.282979+0000",
        "created": "2020-01-02T03:04:05.282979+0000",
        "display_timezone": "America/New_York",
        "message": "Message about the downtime",
        "modified": "2020-01-02T03:04:05.282979+0000",
        "monitor_identifier": {
          "monitor_id": 123
        },
        "mute_first_recovery_notification": false,
        "notify_end_states": [
          "alert",
          "warn"
        ],
        "notify_end_types": [
          "canceled",
          "expired"
        ],
        "schedule": {
          "current_downtime": {
            "end": "2020-01-02T03:04:00.000Z",
            "start": "2020-01-02T03:04:00.000Z"
          },
          "recurrences": [
            {
              "duration": "123d",
              "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
              "start": "2020-01-02T03:04"
            }
          ],
          "timezone": "America/New_York"
        },
        "scope": "env:(staging OR prod) AND datacenter:us-east-1",
        "status": "active"
      },
      "id": "00000000-0000-1234-0000-000000000000",
      "relationships": {
        "created_by": {
          "data": {
            "id": "00000000-0000-1234-0000-000000000000",
            "type": "users"
          }
        },
        "monitor": {
          "data": {
            "id": "12345",
            "type": "monitors"
          }
        }
      },
      "type": "downtime"
    }
  ],
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ],
  "meta": {
    "page": {
      "total_filtered_count": "integer"
    }
  }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/downtime" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all downtimes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.list_downtimes()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get all downtimes returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DowntimesAPI.new
p api_instance.list_downtimes()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get all downtimes returns "OK" response

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
	api := datadogV2.NewDowntimesApi(apiClient)
	resp, r, err := api.ListDowntimes(ctx, *datadogV2.NewListDowntimesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.ListDowntimes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.ListDowntimes`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get all downtimes returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DowntimesApi;
import com.datadog.api.client.v2.model.ListDowntimesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    try {
      ListDowntimesResponse result = apiInstance.listDowntimes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#listDowntimes");
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
// Get all downtimes returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_downtimes::DowntimesAPI;
use datadog_api_client::datadogV2::api_downtimes::ListDowntimesOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api
        .list_downtimes(ListDowntimesOptionalParams::default())
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
 * Get all downtimes returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DowntimesApi(configuration);

apiInstance
  .listDowntimes()
  .then((data: v2.ListDowntimesResponse) => {
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

## Schedule a downtime{% #schedule-a-downtime %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                       |
| ----------------- | -------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/downtime |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/downtime |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/downtime      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/downtime      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/downtime     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/downtime |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/downtime |

### Overview

Schedule a downtime. **Note:** This endpoint has been deprecated. Please use v2 endpoints. This endpoint requires the `monitors_downtime` permission.

OAuth apps require the `monitors_downtime` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Request

#### Body Data (required)

Schedule a downtime request body.

{% tab title="Model" %}

| Parent field | Field                            | Type     | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | -------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
|              | active_child                     | object   | The downtime object definition of the active child for the original parent recurring downtime. This field will only exist on recurring downtimes.                                                                                                                                                                                                                |
| active_child | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
| active_child | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
| active_child | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
| active_child | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
| active_child | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
| active_child | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
| active_child | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
| active_child | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
| active_child | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
| active_child | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
| active_child | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
| active_child | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
| active_child | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
| active_child | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
| active_child | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
| active_child | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
| active_child | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
| active_child | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
| active_child | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |
|              | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
|              | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
|              | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
|              | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
|              | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
|              | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
|              | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
|              | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
|              | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
|              | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
|              | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
|              | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
|              | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
|              | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
|              | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
|              | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
|              | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
|              | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "message": "Example-Downtime",
  "recurrence": {
    "period": 1,
    "type": "years"
  },
  "scope": [
    "*"
  ],
  "start": 1636629071,
  "end": 1636632671,
  "timezone": "Etc/UTC",
  "mute_first_recovery_notification": true,
  "monitor_tags": [
    "tag0"
  ],
  "notify_end_states": [
    "alert",
    "warn"
  ],
  "notify_end_types": [
    "expired"
  ]
}
```

##### 

```json
{
  "message": "Example-Downtime",
  "start": 1636629071,
  "end": 1636632671,
  "timezone": "Etc/UTC",
  "scope": [
    "test:exampledowntime"
  ],
  "recurrence": {
    "type": "weeks",
    "period": 1,
    "week_days": [
      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri"
    ],
    "until_date": 1638443471
  },
  "notify_end_states": [
    "alert",
    "no data",
    "warn"
  ],
  "notify_end_types": [
    "canceled",
    "expired"
  ]
}
```

##### 

```json
{
  "message": "Example-Downtime",
  "recurrence": {
    "period": 1,
    "type": "weeks",
    "until_date": 1638443471,
    "week_days": [
      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri"
    ]
  },
  "scope": [
    "*"
  ],
  "start": 1636629071,
  "end": 1636632671,
  "timezone": "Etc/UTC",
  "mute_first_recovery_notification": true,
  "monitor_tags": [
    "tag0"
  ],
  "notify_end_states": [
    "alert"
  ],
  "notify_end_types": [
    "canceled"
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Downtiming gives you greater control over monitor notifications by allowing you to globally exclude scopes from alerting. Downtime settings, which can be scheduled with start and end times, prevent all alerting related to specified Datadog tags.

| Parent field | Field                            | Type     | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | -------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
|              | active_child                     | object   | The downtime object definition of the active child for the original parent recurring downtime. This field will only exist on recurring downtimes.                                                                                                                                                                                                                |
| active_child | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
| active_child | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
| active_child | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
| active_child | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
| active_child | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
| active_child | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
| active_child | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
| active_child | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
| active_child | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
| active_child | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
| active_child | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
| active_child | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
| active_child | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
| active_child | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
| active_child | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
| active_child | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
| active_child | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
| active_child | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
| active_child | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |
|              | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
|              | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
|              | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
|              | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
|              | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
|              | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
|              | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
|              | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
|              | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
|              | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
|              | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
|              | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
|              | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
|              | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
|              | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
|              | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
|              | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
|              | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "active": true,
  "active_child": {
    "active": true,
    "canceled": 1412799983,
    "creator_id": 123456,
    "disabled": false,
    "downtime_type": 2,
    "end": 1412793983,
    "id": 1626,
    "message": "Message on the downtime",
    "monitor_id": 123456,
    "monitor_tags": [
      "*"
    ],
    "mute_first_recovery_notification": false,
    "notify_end_states": [
      "alert",
      "no data",
      "warn"
    ],
    "notify_end_types": [
      "canceled",
      "expired"
    ],
    "parent_id": 123,
    "recurrence": {
      "period": 1,
      "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
      "type": "weeks",
      "until_date": 1447786293,
      "until_occurrences": 2,
      "week_days": [
        "Mon",
        "Tue"
      ]
    },
    "scope": [
      "env:staging"
    ],
    "start": 1412792983,
    "timezone": "America/New_York",
    "updater_id": 123456
  },
  "canceled": 1412799983,
  "creator_id": 123456,
  "disabled": false,
  "downtime_type": 2,
  "end": 1412793983,
  "id": 1625,
  "message": "Message on the downtime",
  "monitor_id": 123456,
  "monitor_tags": [
    "*"
  ],
  "mute_first_recovery_notification": false,
  "notify_end_states": [
    "alert",
    "no data",
    "warn"
  ],
  "notify_end_types": [
    "canceled",
    "expired"
  ],
  "parent_id": 123,
  "recurrence": {
    "period": 1,
    "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
    "type": "weeks",
    "until_date": 1447786293,
    "until_occurrences": 2,
    "week_days": [
      "Mon",
      "Tue"
    ]
  },
  "scope": [
    "env:staging"
  ],
  "start": 1412792983,
  "timezone": "America/New_York",
  "updater_id": 123456
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/downtime" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "message": "Example-Downtime",
  "recurrence": {
    "period": 1,
    "type": "years"
  },
  "scope": [
    "*"
  ],
  "start": 1636629071,
  "end": 1636632671,
  "timezone": "Etc/UTC",
  "mute_first_recovery_notification": true,
  "monitor_tags": [
    "tag0"
  ],
  "notify_end_states": [
    "alert",
    "warn"
  ],
  "notify_end_types": [
    "expired"
  ]
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/downtime" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "message": "Example-Downtime",
  "start": 1636629071,
  "end": 1636632671,
  "timezone": "Etc/UTC",
  "scope": [
    "test:exampledowntime"
  ],
  "recurrence": {
    "type": "weeks",
    "period": 1,
    "week_days": [
      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri"
    ],
    "until_date": 1638443471
  },
  "notify_end_states": [
    "alert",
    "no data",
    "warn"
  ],
  "notify_end_types": [
    "canceled",
    "expired"
  ]
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/downtime" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "message": "Example-Downtime",
  "recurrence": {
    "period": 1,
    "type": "weeks",
    "until_date": 1638443471,
    "week_days": [
      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri"
    ]
  },
  "scope": [
    "*"
  ],
  "start": 1636629071,
  "end": 1636632671,
  "timezone": "Etc/UTC",
  "mute_first_recovery_notification": true,
  "monitor_tags": [
    "tag0"
  ],
  "notify_end_states": [
    "alert"
  ],
  "notify_end_types": [
    "canceled"
  ]
}
EOF
                        
##### 

```go
// Schedule a downtime once a year

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := datadogV1.Downtime{
		Message: *datadog.NewNullableString(datadog.PtrString("Example-Downtime")),
		Recurrence: *datadogV1.NewNullableDowntimeRecurrence(&datadogV1.DowntimeRecurrence{
			Period: datadog.PtrInt32(1),
			Type:   datadog.PtrString("years"),
		}),
		Scope: []string{
			"*",
		},
		Start:                         datadog.PtrInt64(time.Now().Unix()),
		End:                           *datadog.NewNullableInt64(datadog.PtrInt64(time.Now().Add(time.Hour * 1).Unix())),
		Timezone:                      datadog.PtrString("Etc/UTC"),
		MuteFirstRecoveryNotification: datadog.PtrBool(true),
		MonitorTags: []string{
			"tag0",
		},
		NotifyEndStates: []datadogV1.NotifyEndState{
			datadogV1.NOTIFYENDSTATE_ALERT,
			datadogV1.NOTIFYENDSTATE_WARN,
		},
		NotifyEndTypes: []datadogV1.NotifyEndType{
			datadogV1.NOTIFYENDTYPE_EXPIRED,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewDowntimesApi(apiClient)
	resp, r, err := api.CreateDowntime(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.CreateDowntime`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.CreateDowntime`:\n%s\n", responseContent)
}
```

##### 

```go
// Schedule a downtime returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := datadogV1.Downtime{
		Message:  *datadog.NewNullableString(datadog.PtrString("Example-Downtime")),
		Start:    datadog.PtrInt64(time.Now().Unix()),
		End:      *datadog.NewNullableInt64(datadog.PtrInt64(time.Now().Add(time.Hour * 1).Unix())),
		Timezone: datadog.PtrString("Etc/UTC"),
		Scope: []string{
			"test:exampledowntime",
		},
		Recurrence: *datadogV1.NewNullableDowntimeRecurrence(&datadogV1.DowntimeRecurrence{
			Type:   datadog.PtrString("weeks"),
			Period: datadog.PtrInt32(1),
			WeekDays: *datadog.NewNullableList(&[]string{
				"Mon",
				"Tue",
				"Wed",
				"Thu",
				"Fri",
			}),
			UntilDate: *datadog.NewNullableInt64(datadog.PtrInt64(time.Now().AddDate(0, 0, 21).Unix())),
		}),
		NotifyEndStates: []datadogV1.NotifyEndState{
			datadogV1.NOTIFYENDSTATE_ALERT,
			datadogV1.NOTIFYENDSTATE_NO_DATA,
			datadogV1.NOTIFYENDSTATE_WARN,
		},
		NotifyEndTypes: []datadogV1.NotifyEndType{
			datadogV1.NOTIFYENDTYPE_CANCELED,
			datadogV1.NOTIFYENDTYPE_EXPIRED,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewDowntimesApi(apiClient)
	resp, r, err := api.CreateDowntime(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.CreateDowntime`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.CreateDowntime`:\n%s\n", responseContent)
}
```

##### 

```go
// Schedule a downtime until date

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := datadogV1.Downtime{
		Message: *datadog.NewNullableString(datadog.PtrString("Example-Downtime")),
		Recurrence: *datadogV1.NewNullableDowntimeRecurrence(&datadogV1.DowntimeRecurrence{
			Period:    datadog.PtrInt32(1),
			Type:      datadog.PtrString("weeks"),
			UntilDate: *datadog.NewNullableInt64(datadog.PtrInt64(time.Now().AddDate(0, 0, 21).Unix())),
			WeekDays: *datadog.NewNullableList(&[]string{
				"Mon",
				"Tue",
				"Wed",
				"Thu",
				"Fri",
			}),
		}),
		Scope: []string{
			"*",
		},
		Start:                         datadog.PtrInt64(time.Now().Unix()),
		End:                           *datadog.NewNullableInt64(datadog.PtrInt64(time.Now().Add(time.Hour * 1).Unix())),
		Timezone:                      datadog.PtrString("Etc/UTC"),
		MuteFirstRecoveryNotification: datadog.PtrBool(true),
		MonitorTags: []string{
			"tag0",
		},
		NotifyEndStates: []datadogV1.NotifyEndState{
			datadogV1.NOTIFYENDSTATE_ALERT,
		},
		NotifyEndTypes: []datadogV1.NotifyEndType{
			datadogV1.NOTIFYENDTYPE_CANCELED,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewDowntimesApi(apiClient)
	resp, r, err := api.CreateDowntime(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.CreateDowntime`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.CreateDowntime`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Schedule a downtime once a year
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DowntimesApi;
import com.datadog.api.client.v1.model.Downtime;
import com.datadog.api.client.v1.model.DowntimeRecurrence;
import com.datadog.api.client.v1.model.NotifyEndState;
import com.datadog.api.client.v1.model.NotifyEndType;
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    Downtime body =
        new Downtime()
            .message("Example-Downtime")
            .recurrence(new DowntimeRecurrence().period(1).type("years"))
            .scope(Collections.singletonList("*"))
            .start(OffsetDateTime.now().toInstant().getEpochSecond())
            .end(OffsetDateTime.now().plusHours(1).toInstant().getEpochSecond())
            .timezone("Etc/UTC")
            .muteFirstRecoveryNotification(true)
            .monitorTags(Collections.singletonList("tag0"))
            .notifyEndStates(Arrays.asList(NotifyEndState.ALERT, NotifyEndState.WARN))
            .notifyEndTypes(Collections.singletonList(NotifyEndType.EXPIRED));

    try {
      Downtime result = apiInstance.createDowntime(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#createDowntime");
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
// Schedule a downtime returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DowntimesApi;
import com.datadog.api.client.v1.model.Downtime;
import com.datadog.api.client.v1.model.DowntimeRecurrence;
import com.datadog.api.client.v1.model.NotifyEndState;
import com.datadog.api.client.v1.model.NotifyEndType;
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    Downtime body =
        new Downtime()
            .message("Example-Downtime")
            .start(OffsetDateTime.now().toInstant().getEpochSecond())
            .end(OffsetDateTime.now().plusHours(1).toInstant().getEpochSecond())
            .timezone("Etc/UTC")
            .scope(Collections.singletonList("test:exampledowntime"))
            .recurrence(
                new DowntimeRecurrence()
                    .type("weeks")
                    .period(1)
                    .weekDays(Arrays.asList("Mon", "Tue", "Wed", "Thu", "Fri"))
                    .untilDate(OffsetDateTime.now().plusDays(21).toInstant().getEpochSecond()))
            .notifyEndStates(
                Arrays.asList(NotifyEndState.ALERT, NotifyEndState.NO_DATA, NotifyEndState.WARN))
            .notifyEndTypes(Arrays.asList(NotifyEndType.CANCELED, NotifyEndType.EXPIRED));

    try {
      Downtime result = apiInstance.createDowntime(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#createDowntime");
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
// Schedule a downtime until date
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DowntimesApi;
import com.datadog.api.client.v1.model.Downtime;
import com.datadog.api.client.v1.model.DowntimeRecurrence;
import com.datadog.api.client.v1.model.NotifyEndState;
import com.datadog.api.client.v1.model.NotifyEndType;
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    Downtime body =
        new Downtime()
            .message("Example-Downtime")
            .recurrence(
                new DowntimeRecurrence()
                    .period(1)
                    .type("weeks")
                    .untilDate(OffsetDateTime.now().plusDays(21).toInstant().getEpochSecond())
                    .weekDays(Arrays.asList("Mon", "Tue", "Wed", "Thu", "Fri")))
            .scope(Collections.singletonList("*"))
            .start(OffsetDateTime.now().toInstant().getEpochSecond())
            .end(OffsetDateTime.now().plusHours(1).toInstant().getEpochSecond())
            .timezone("Etc/UTC")
            .muteFirstRecoveryNotification(true)
            .monitorTags(Collections.singletonList("tag0"))
            .notifyEndStates(Collections.singletonList(NotifyEndState.ALERT))
            .notifyEndTypes(Collections.singletonList(NotifyEndType.CANCELED));

    try {
      Downtime result = apiInstance.createDowntime(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#createDowntime");
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

# Repeat for 3 hours (starting now) on every week day for 4 weeks.
start_ts = int(time.time())
end_ts = start_ts + (3 * 60 * 60)
end_reccurrence_ts = start_ts + (4 * 7 * 24 * 60 * 60)  # 4 weeks from now

recurrence = {
    'type': 'weeks',
    'period': 1,
    'week_days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'until_date': end_reccurrence_ts
}

# Schedule downtime
api.Downtime.create(
    scope='env:staging',
    start=start_ts,
    end=end_ts,
    recurrence=recurrence
)

# OR use RRULE reccurence
rrule_recurrence = {
    'type': 'rrule',
    'rrule': 'FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1',
}

# Schedule downtime
api.Downtime.create(
    scope='env:staging',
    start=start_ts,
    end=end_ts,
    recurrence=rrule_recurrence
)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
##### 

```python
"""
Schedule a downtime once a year
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime
from datadog_api_client.v1.model.downtime_recurrence import DowntimeRecurrence
from datadog_api_client.v1.model.notify_end_state import NotifyEndState
from datadog_api_client.v1.model.notify_end_type import NotifyEndType

body = Downtime(
    message="Example-Downtime",
    recurrence=DowntimeRecurrence(
        period=1,
        type="years",
    ),
    scope=[
        "*",
    ],
    start=int(datetime.now().timestamp()),
    end=int((datetime.now() + relativedelta(hours=1)).timestamp()),
    timezone="Etc/UTC",
    mute_first_recovery_notification=True,
    monitor_tags=[
        "tag0",
    ],
    notify_end_states=[
        NotifyEndState.ALERT,
        NotifyEndState.WARN,
    ],
    notify_end_types=[
        NotifyEndType.EXPIRED,
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.create_downtime(body=body)

    print(response)
```

##### 

```python
"""
Schedule a downtime returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime
from datadog_api_client.v1.model.downtime_recurrence import DowntimeRecurrence
from datadog_api_client.v1.model.notify_end_state import NotifyEndState
from datadog_api_client.v1.model.notify_end_type import NotifyEndType

body = Downtime(
    message="Example-Downtime",
    start=int(datetime.now().timestamp()),
    end=int((datetime.now() + relativedelta(hours=1)).timestamp()),
    timezone="Etc/UTC",
    scope=[
        "test:exampledowntime",
    ],
    recurrence=DowntimeRecurrence(
        type="weeks",
        period=1,
        week_days=[
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
        ],
        until_date=int((datetime.now() + relativedelta(days=21)).timestamp()),
    ),
    notify_end_states=[
        NotifyEndState.ALERT,
        NotifyEndState.NO_DATA,
        NotifyEndState.WARN,
    ],
    notify_end_types=[
        NotifyEndType.CANCELED,
        NotifyEndType.EXPIRED,
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.create_downtime(body=body)

    print(response)
```

##### 

```python
"""
Schedule a downtime until date
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime
from datadog_api_client.v1.model.downtime_recurrence import DowntimeRecurrence
from datadog_api_client.v1.model.notify_end_state import NotifyEndState
from datadog_api_client.v1.model.notify_end_type import NotifyEndType

body = Downtime(
    message="Example-Downtime",
    recurrence=DowntimeRecurrence(
        period=1,
        type="weeks",
        until_date=int((datetime.now() + relativedelta(days=21)).timestamp()),
        week_days=[
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
        ],
    ),
    scope=[
        "*",
    ],
    start=int(datetime.now().timestamp()),
    end=int((datetime.now() + relativedelta(hours=1)).timestamp()),
    timezone="Etc/UTC",
    mute_first_recovery_notification=True,
    monitor_tags=[
        "tag0",
    ],
    notify_end_states=[
        NotifyEndState.ALERT,
    ],
    notify_end_types=[
        NotifyEndType.CANCELED,
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.create_downtime(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Repeat for 3 hours (starting now) on every week day for 4 weeks.
start_ts = Time.now.to_i
end_ts = start_ts + (3 * 60 * 60)
end_reccurrence_ts = start_ts + (4 * 7 * 24 * 60 * 60) # 4 weeks from now

recurrence = {
    'type' => 'weeks',
    'period' => 1,
    'week_days' => %w[Mon Tue Wed Thu Fri],
    'until_date' => end_reccurrence_ts
}

# Schedule downtime
dog.Downtime.create(
    'env:staging',
    start: start_ts,
    end: end_ts,
    recurrence: recurrence
)

# OR use RRULE reccurence
rrule_recurrence = {
    'type' => 'rrule',
    'rrule' => 'FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1',
}

# Schedule downtime
dog.Downtime.create(
    'env:staging',
    start: start_ts,
    end: end_ts,
    recurrence: rrule_recurrence
)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```ruby
# Schedule a downtime once a year

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DowntimesAPI.new

body = DatadogAPIClient::V1::Downtime.new({
  message: "Example-Downtime",
  recurrence: DatadogAPIClient::V1::DowntimeRecurrence.new({
    period: 1,
    type: "years",
  }),
  scope: [
    "*",
  ],
  start: Time.now.to_i,
  _end: (Time.now + 1 * 3600).to_i,
  timezone: "Etc/UTC",
  mute_first_recovery_notification: true,
  monitor_tags: [
    "tag0",
  ],
  notify_end_states: [
    DatadogAPIClient::V1::NotifyEndState::ALERT,
    DatadogAPIClient::V1::NotifyEndState::WARN,
  ],
  notify_end_types: [
    DatadogAPIClient::V1::NotifyEndType::EXPIRED,
  ],
})
p api_instance.create_downtime(body)
```

##### 

```ruby
# Schedule a downtime returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DowntimesAPI.new

body = DatadogAPIClient::V1::Downtime.new({
  message: "Example-Downtime",
  start: Time.now.to_i,
  _end: (Time.now + 1 * 3600).to_i,
  timezone: "Etc/UTC",
  scope: [
    "test:exampledowntime",
  ],
  recurrence: DatadogAPIClient::V1::DowntimeRecurrence.new({
    type: "weeks",
    period: 1,
    week_days: [
      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri",
    ],
    until_date: (Time.now + 21 * 86400).to_i,
  }),
  notify_end_states: [
    DatadogAPIClient::V1::NotifyEndState::ALERT,
    DatadogAPIClient::V1::NotifyEndState::NO_DATA,
    DatadogAPIClient::V1::NotifyEndState::WARN,
  ],
  notify_end_types: [
    DatadogAPIClient::V1::NotifyEndType::CANCELED,
    DatadogAPIClient::V1::NotifyEndType::EXPIRED,
  ],
})
p api_instance.create_downtime(body)
```

##### 

```ruby
# Schedule a downtime until date

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DowntimesAPI.new

body = DatadogAPIClient::V1::Downtime.new({
  message: "Example-Downtime",
  recurrence: DatadogAPIClient::V1::DowntimeRecurrence.new({
    period: 1,
    type: "weeks",
    until_date: (Time.now + 21 * 86400).to_i,
    week_days: [
      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri",
    ],
  }),
  scope: [
    "*",
  ],
  start: Time.now.to_i,
  _end: (Time.now + 1 * 3600).to_i,
  timezone: "Etc/UTC",
  mute_first_recovery_notification: true,
  monitor_tags: [
    "tag0",
  ],
  notify_end_states: [
    DatadogAPIClient::V1::NotifyEndState::ALERT,
  ],
  notify_end_types: [
    DatadogAPIClient::V1::NotifyEndType::CANCELED,
  ],
})
p api_instance.create_downtime(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Schedule a downtime once a year
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_downtimes::DowntimesAPI;
use datadog_api_client::datadogV1::model::Downtime;
use datadog_api_client::datadogV1::model::DowntimeRecurrence;
use datadog_api_client::datadogV1::model::NotifyEndState;
use datadog_api_client::datadogV1::model::NotifyEndType;

#[tokio::main]
async fn main() {
    let body = Downtime::new()
        .end(Some(1636632671))
        .message(Some("Example-Downtime".to_string()))
        .monitor_tags(vec!["tag0".to_string()])
        .mute_first_recovery_notification(true)
        .notify_end_states(vec![NotifyEndState::ALERT, NotifyEndState::WARN])
        .notify_end_types(vec![NotifyEndType::EXPIRED])
        .recurrence(Some(
            DowntimeRecurrence::new()
                .period(1)
                .type_("years".to_string()),
        ))
        .scope(vec!["*".to_string()])
        .start(1636629071)
        .timezone("Etc/UTC".to_string());
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api.create_downtime(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Schedule a downtime returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_downtimes::DowntimesAPI;
use datadog_api_client::datadogV1::model::Downtime;
use datadog_api_client::datadogV1::model::DowntimeRecurrence;
use datadog_api_client::datadogV1::model::NotifyEndState;
use datadog_api_client::datadogV1::model::NotifyEndType;

#[tokio::main]
async fn main() {
    let body = Downtime::new()
        .end(Some(1636632671))
        .message(Some("Example-Downtime".to_string()))
        .notify_end_states(vec![
            NotifyEndState::ALERT,
            NotifyEndState::NO_DATA,
            NotifyEndState::WARN,
        ])
        .notify_end_types(vec![NotifyEndType::CANCELED, NotifyEndType::EXPIRED])
        .recurrence(Some(
            DowntimeRecurrence::new()
                .period(1)
                .type_("weeks".to_string())
                .until_date(Some(1638443471))
                .week_days(Some(vec![
                    "Mon".to_string(),
                    "Tue".to_string(),
                    "Wed".to_string(),
                    "Thu".to_string(),
                    "Fri".to_string(),
                ])),
        ))
        .scope(vec!["test:exampledowntime".to_string()])
        .start(1636629071)
        .timezone("Etc/UTC".to_string());
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api.create_downtime(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Schedule a downtime until date
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_downtimes::DowntimesAPI;
use datadog_api_client::datadogV1::model::Downtime;
use datadog_api_client::datadogV1::model::DowntimeRecurrence;
use datadog_api_client::datadogV1::model::NotifyEndState;
use datadog_api_client::datadogV1::model::NotifyEndType;

#[tokio::main]
async fn main() {
    let body = Downtime::new()
        .end(Some(1636632671))
        .message(Some("Example-Downtime".to_string()))
        .monitor_tags(vec!["tag0".to_string()])
        .mute_first_recovery_notification(true)
        .notify_end_states(vec![NotifyEndState::ALERT])
        .notify_end_types(vec![NotifyEndType::CANCELED])
        .recurrence(Some(
            DowntimeRecurrence::new()
                .period(1)
                .type_("weeks".to_string())
                .until_date(Some(1638443471))
                .week_days(Some(vec![
                    "Mon".to_string(),
                    "Tue".to_string(),
                    "Wed".to_string(),
                    "Thu".to_string(),
                    "Fri".to_string(),
                ])),
        ))
        .scope(vec!["*".to_string()])
        .start(1636629071)
        .timezone("Etc/UTC".to_string());
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api.create_downtime(body).await;
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
 * Schedule a downtime once a year
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DowntimesApi(configuration);

const params: v1.DowntimesApiCreateDowntimeRequest = {
  body: {
    message: "Example-Downtime",
    recurrence: {
      period: 1,
      type: "years",
    },
    scope: ["*"],
    start: Math.round(new Date().getTime() / 1000),
    end: Math.round(
      new Date(new Date().getTime() + 1 * 3600 * 1000).getTime() / 1000
    ),
    timezone: "Etc/UTC",
    muteFirstRecoveryNotification: true,
    monitorTags: ["tag0"],
    notifyEndStates: ["alert", "warn"],
    notifyEndTypes: ["expired"],
  },
};

apiInstance
  .createDowntime(params)
  .then((data: v1.Downtime) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Schedule a downtime returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DowntimesApi(configuration);

const params: v1.DowntimesApiCreateDowntimeRequest = {
  body: {
    message: "Example-Downtime",
    start: Math.round(new Date().getTime() / 1000),
    end: Math.round(
      new Date(new Date().getTime() + 1 * 3600 * 1000).getTime() / 1000
    ),
    timezone: "Etc/UTC",
    scope: ["test:exampledowntime"],
    recurrence: {
      type: "weeks",
      period: 1,
      weekDays: ["Mon", "Tue", "Wed", "Thu", "Fri"],
      untilDate: Math.round(
        new Date(new Date().getTime() + 21 * 86400 * 1000).getTime() / 1000
      ),
    },
    notifyEndStates: ["alert", "no data", "warn"],
    notifyEndTypes: ["canceled", "expired"],
  },
};

apiInstance
  .createDowntime(params)
  .then((data: v1.Downtime) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Schedule a downtime until date
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DowntimesApi(configuration);

const params: v1.DowntimesApiCreateDowntimeRequest = {
  body: {
    message: "Example-Downtime",
    recurrence: {
      period: 1,
      type: "weeks",
      untilDate: Math.round(
        new Date(new Date().getTime() + 21 * 86400 * 1000).getTime() / 1000
      ),
      weekDays: ["Mon", "Tue", "Wed", "Thu", "Fri"],
    },
    scope: ["*"],
    start: Math.round(new Date().getTime() / 1000),
    end: Math.round(
      new Date(new Date().getTime() + 1 * 3600 * 1000).getTime() / 1000
    ),
    timezone: "Etc/UTC",
    muteFirstRecoveryNotification: true,
    monitorTags: ["tag0"],
    notifyEndStates: ["alert"],
    notifyEndTypes: ["canceled"],
  },
};

apiInstance
  .createDowntime(params)
  .then((data: v1.Downtime) => {
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

| Datadog site      | API endpoint                                       |
| ----------------- | -------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/downtime |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/downtime |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/downtime      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/downtime      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/downtime     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/downtime |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/downtime |

### Overview

Schedule a downtime. This endpoint requires the `monitors_downtime` permission.

OAuth apps require the `monitors_downtime` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Request

#### Body Data (required)

Schedule a downtime request body.

{% tab title="Model" %}

| Parent field       | Field                                | Type          | Description                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | ------------------------------------ | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data [*required*]               | object        | Object to create a downtime.                                                                                                                                                                                                                                                                                                                                                                  |
| data               | attributes [*required*]         | object        | Downtime details.                                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | display_timezone                     | string        | The timezone in which to display the downtime's start and end times in Datadog applications. This is not used as an offset for scheduling.                                                                                                                                                                                                                                                    |
| attributes         | message                              | string        | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                                                |
| attributes         | monitor_identifier [*required*] |  <oneOf> | Monitor identifier for the downtime.                                                                                                                                                                                                                                                                                                                                                          |
| monitor_identifier | Option 1                             | object        | Object of the monitor identifier.                                                                                                                                                                                                                                                                                                                                                             |
| Option 1           | monitor_id [*required*]         | int64         | ID of the monitor to prevent notifications.                                                                                                                                                                                                                                                                                                                                                   |
| monitor_identifier | Option 2                             | object        | Object of the monitor tags.                                                                                                                                                                                                                                                                                                                                                                   |
| Option 2           | monitor_tags [*required*]       | [string]      | A list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match **all** provided monitor tags. Setting `monitor_tags` to `[*]` configures the downtime to mute all monitors for the given scope. |
| attributes         | mute_first_recovery_notification     | boolean       | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                                                         |
| attributes         | notify_end_states                    | [string]      | States that will trigger a monitor notification when the `notify_end_types` action occurs.                                                                                                                                                                                                                                                                                                    |
| attributes         | notify_end_types                     | [string]      | Actions that will trigger a monitor notification if the downtime is in the `notify_end_types` state.                                                                                                                                                                                                                                                                                          |
| attributes         | schedule                             |  <oneOf> | Schedule for the downtime.                                                                                                                                                                                                                                                                                                                                                                    |
| schedule           | Option 1                             | object        | A recurring downtime schedule definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1           | recurrences [*required*]        | [object]      | A list of downtime recurrences.                                                                                                                                                                                                                                                                                                                                                               |
| recurrences        | duration [*required*]           | string        | The length of the downtime. Must begin with an integer and end with one of 'm', 'h', d', or 'w'.                                                                                                                                                                                                                                                                                              |
| recurrences        | rrule [*required*]              | string        | The `RRULE` standard for defining recurring events. For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.                                                                         | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api). |
| recurrences        | start                                | string        | ISO-8601 Datetime to start the downtime. Must not include a UTC offset. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                        |
| Option 1           | timezone                             | string        | The timezone in which to schedule the downtime.                                                                                                                                                                                                                                                                                                                                               |
| schedule           | Option 2                             | object        | A one-time downtime definition.                                                                                                                                                                                                                                                                                                                                                               |
| Option 2           | end                                  | date-time     | ISO-8601 Datetime to end the downtime. Must include a UTC offset of zero. If not provided, the downtime continues forever.                                                                                                                                                                                                                                                                    |
| Option 2           | start                                | date-time     | ISO-8601 Datetime to start the downtime. Must include a UTC offset of zero. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                    |
| attributes         | scope [*required*]              | string        | The scope to which the downtime applies. Must follow the [common search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/).                                                                                                                                                                                                                                                     |
| data               | type [*required*]               | enum          | Downtime resource type. Allowed enum values: `downtime`                                                                                                                                                                                                                                                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "message": "dark forest",
      "monitor_identifier": {
        "monitor_tags": [
          "cat:hat"
        ]
      },
      "scope": "test:exampledowntime",
      "schedule": {
        "start": null
      }
    },
    "type": "downtime"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Downtiming gives you greater control over monitor notifications by allowing you to globally exclude scopes from alerting. Downtime settings, which can be scheduled with start and end times, prevent all alerting related to specified Datadog tags.

| Parent field       | Field                            | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | -------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                             | object          | Downtime data.                                                                                                                                                                                                                                                                                                                                                                                |
| data               | attributes                       | object          | Downtime details.                                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | canceled                         | date-time       | Time that the downtime was canceled.                                                                                                                                                                                                                                                                                                                                                          |
| attributes         | created                          | date-time       | Creation time of the downtime.                                                                                                                                                                                                                                                                                                                                                                |
| attributes         | display_timezone                 | string          | The timezone in which to display the downtime's start and end times in Datadog applications. This is not used as an offset for scheduling.                                                                                                                                                                                                                                                    |
| attributes         | message                          | string          | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                                                |
| attributes         | modified                         | date-time       | Time that the downtime was last modified.                                                                                                                                                                                                                                                                                                                                                     |
| attributes         | monitor_identifier               |  <oneOf>   | Monitor identifier for the downtime.                                                                                                                                                                                                                                                                                                                                                          |
| monitor_identifier | Option 1                         | object          | Object of the monitor identifier.                                                                                                                                                                                                                                                                                                                                                             |
| Option 1           | monitor_id [*required*]     | int64           | ID of the monitor to prevent notifications.                                                                                                                                                                                                                                                                                                                                                   |
| monitor_identifier | Option 2                         | object          | Object of the monitor tags.                                                                                                                                                                                                                                                                                                                                                                   |
| Option 2           | monitor_tags [*required*]   | [string]        | A list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match **all** provided monitor tags. Setting `monitor_tags` to `[*]` configures the downtime to mute all monitors for the given scope. |
| attributes         | mute_first_recovery_notification | boolean         | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                                                         |
| attributes         | notify_end_states                | [string]        | States that will trigger a monitor notification when the `notify_end_types` action occurs.                                                                                                                                                                                                                                                                                                    |
| attributes         | notify_end_types                 | [string]        | Actions that will trigger a monitor notification if the downtime is in the `notify_end_types` state.                                                                                                                                                                                                                                                                                          |
| attributes         | schedule                         |  <oneOf>   | The schedule that defines when the monitor starts, stops, and recurs. There are two types of schedules: one-time and recurring. Recurring schedules may have up to five RRULE-based recurrences. If no schedules are provided, the downtime will begin immediately and never end.                                                                                                             |
| schedule           | Option 1                         | object          | A recurring downtime schedule definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1           | current_downtime                 | object          | The most recent actual start and end dates for a recurring downtime. For a canceled downtime, this is the previously occurring downtime. For active downtimes, this is the ongoing downtime, and for scheduled downtimes it is the upcoming downtime.                                                                                                                                         |
| current_downtime   | end                              | date-time       | The end of the current downtime.                                                                                                                                                                                                                                                                                                                                                              |
| current_downtime   | start                            | date-time       | The start of the current downtime.                                                                                                                                                                                                                                                                                                                                                            |
| Option 1           | recurrences [*required*]    | [object]        | A list of downtime recurrences.                                                                                                                                                                                                                                                                                                                                                               |
| recurrences        | duration                         | string          | The length of the downtime. Must begin with an integer and end with one of 'm', 'h', d', or 'w'.                                                                                                                                                                                                                                                                                              |
| recurrences        | rrule                            | string          | The `RRULE` standard for defining recurring events. For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.                                                                         | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api). |
| recurrences        | start                            | string          | ISO-8601 Datetime to start the downtime. Must not include a UTC offset. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                        |
| Option 1           | timezone                         | string          | The timezone in which to schedule the downtime. This affects recurring start and end dates. Must match `display_timezone`.                                                                                                                                                                                                                                                                    |
| schedule           | Option 2                         | object          | A one-time downtime definition.                                                                                                                                                                                                                                                                                                                                                               |
| Option 2           | end                              | date-time       | ISO-8601 Datetime to end the downtime.                                                                                                                                                                                                                                                                                                                                                        |
| Option 2           | start [*required*]          | date-time       | ISO-8601 Datetime to start the downtime.                                                                                                                                                                                                                                                                                                                                                      |
| attributes         | scope                            | string          | The scope to which the downtime applies. Must follow the [common search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/).                                                                                                                                                                                                                                                     |
| attributes         | status                           | enum            | The current status of the downtime. Allowed enum values: `active,canceled,ended,scheduled`                                                                                                                                                                                                                                                                                                    |
| data               | id                               | string          | The downtime ID.                                                                                                                                                                                                                                                                                                                                                                              |
| data               | relationships                    | object          | All relationships associated with downtime.                                                                                                                                                                                                                                                                                                                                                   |
| relationships      | created_by                       | object          | The user who created the downtime.                                                                                                                                                                                                                                                                                                                                                            |
| created_by         | data                             | object          | Data for the user who created the downtime.                                                                                                                                                                                                                                                                                                                                                   |
| data               | id                               | string          | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                                              |
| data               | type                             | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| relationships      | monitor                          | object          | The monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                                       |
| monitor            | data                             | object          | Data for the monitor.                                                                                                                                                                                                                                                                                                                                                                         |
| data               | id                               | string          | Monitor ID of the downtime.                                                                                                                                                                                                                                                                                                                                                                   |
| data               | type                             | enum            | Monitor resource type. Allowed enum values: `monitors`                                                                                                                                                                                                                                                                                                                                        |
| data               | type                             | enum            | Downtime resource type. Allowed enum values: `downtime`                                                                                                                                                                                                                                                                                                                                       |
|                    | included                         | [ <oneOf>] | Array of objects related to the downtime that the user requested.                                                                                                                                                                                                                                                                                                                             |
| included           | Option 1                         | object          | User object returned by the API.                                                                                                                                                                                                                                                                                                                                                              |
| Option 1           | attributes                       | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                                                                                                                |
| attributes         | created_at                       | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                                                                                                                    |
| attributes         | disabled                         | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                                                                                                                 |
| attributes         | email                            | string          | Email of the user.                                                                                                                                                                                                                                                                                                                                                                            |
| attributes         | handle                           | string          | Handle of the user.                                                                                                                                                                                                                                                                                                                                                                           |
| attributes         | icon                             | string          | URL of the user's icon.                                                                                                                                                                                                                                                                                                                                                                       |
| attributes         | last_login_time                  | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | mfa_enabled                      | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                                                                                                                      |
| attributes         | modified_at                      | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                                                                                                                         |
| attributes         | name                             | string          | Name of the user.                                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | service_account                  | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                                                                                                                        |
| attributes         | status                           | string          | Status of the user.                                                                                                                                                                                                                                                                                                                                                                           |
| attributes         | title                            | string          | Title of the user.                                                                                                                                                                                                                                                                                                                                                                            |
| attributes         | verified                         | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                                                                                                                 |
| Option 1           | id                               | string          | ID of the user.                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1           | relationships                    | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                                                                                                                         |
| relationships      | org                              | object          | Relationship to an organization.                                                                                                                                                                                                                                                                                                                                                              |
| org                | data [*required*]           | object          | Relationship to organization object.                                                                                                                                                                                                                                                                                                                                                          |
| data               | id [*required*]             | string          | ID of the organization.                                                                                                                                                                                                                                                                                                                                                                       |
| data               | type [*required*]           | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                                                                                                                      |
| relationships      | other_orgs                       | object          | Relationship to organizations.                                                                                                                                                                                                                                                                                                                                                                |
| other_orgs         | data [*required*]           | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                                                                                                                        |
| data               | id [*required*]             | string          | ID of the organization.                                                                                                                                                                                                                                                                                                                                                                       |
| data               | type [*required*]           | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                                                                                                                      |
| relationships      | other_users                      | object          | Relationship to users.                                                                                                                                                                                                                                                                                                                                                                        |
| other_users        | data [*required*]           | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                                                                                                                |
| data               | id [*required*]             | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                                                                                                                 |
| data               | type [*required*]           | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| relationships      | roles                            | object          | Relationship to roles.                                                                                                                                                                                                                                                                                                                                                                        |
| roles              | data                             | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                                                                                                                 |
| data               | id                               | string          | The unique identifier of the role.                                                                                                                                                                                                                                                                                                                                                            |
| data               | type                             | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                                                                                                                      |
| Option 1           | type                             | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| included           | Option 2                         | object          | Information about the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                     |
| Option 2           | attributes                       | object          | Attributes of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                         |
| attributes         | name                             | string          | The name of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                           |
| Option 2           | id                               | int64           | ID of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                                 |
| Option 2           | type                             | enum            | Monitor resource type. Allowed enum values: `monitors`                                                                                                                                                                                                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "canceled": "2020-01-02T03:04:05.282979+0000",
      "created": "2020-01-02T03:04:05.282979+0000",
      "display_timezone": "America/New_York",
      "message": "Message about the downtime",
      "modified": "2020-01-02T03:04:05.282979+0000",
      "monitor_identifier": {
        "monitor_id": 123
      },
      "mute_first_recovery_notification": false,
      "notify_end_states": [
        "alert",
        "warn"
      ],
      "notify_end_types": [
        "canceled",
        "expired"
      ],
      "schedule": {
        "current_downtime": {
          "end": "2020-01-02T03:04:00.000Z",
          "start": "2020-01-02T03:04:00.000Z"
        },
        "recurrences": [
          {
            "duration": "123d",
            "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
            "start": "2020-01-02T03:04"
          }
        ],
        "timezone": "America/New_York"
      },
      "scope": "env:(staging OR prod) AND datacenter:us-east-1",
      "status": "active"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-1234-0000-000000000000",
          "type": "users"
        }
      },
      "monitor": {
        "data": {
          "id": "12345",
          "type": "monitors"
        }
      }
    },
    "type": "downtime"
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ]
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/downtime" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "message": "dark forest",
      "monitor_identifier": {
        "monitor_tags": [
          "cat:hat"
        ]
      },
      "scope": "test:exampledowntime",
      "schedule": {
        "start": null
      }
    },
    "type": "downtime"
  }
}
EOF
                        
##### 

```go
// Schedule a downtime returns "OK" response

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
	body := datadogV2.DowntimeCreateRequest{
		Data: datadogV2.DowntimeCreateRequestData{
			Attributes: datadogV2.DowntimeCreateRequestAttributes{
				Message: *datadog.NewNullableString(datadog.PtrString("dark forest")),
				MonitorIdentifier: datadogV2.DowntimeMonitorIdentifier{
					DowntimeMonitorIdentifierTags: &datadogV2.DowntimeMonitorIdentifierTags{
						MonitorTags: []string{
							"cat:hat",
						},
					}},
				Scope: "test:exampledowntime",
				Schedule: &datadogV2.DowntimeScheduleCreateRequest{
					DowntimeScheduleOneTimeCreateUpdateRequest: &datadogV2.DowntimeScheduleOneTimeCreateUpdateRequest{
						Start: *datadog.NewNullableTime(nil),
					}},
			},
			Type: datadogV2.DOWNTIMERESOURCETYPE_DOWNTIME,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDowntimesApi(apiClient)
	resp, r, err := api.CreateDowntime(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.CreateDowntime`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.CreateDowntime`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Schedule a downtime returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DowntimesApi;
import com.datadog.api.client.v2.model.DowntimeCreateRequest;
import com.datadog.api.client.v2.model.DowntimeCreateRequestAttributes;
import com.datadog.api.client.v2.model.DowntimeCreateRequestData;
import com.datadog.api.client.v2.model.DowntimeMonitorIdentifier;
import com.datadog.api.client.v2.model.DowntimeMonitorIdentifierTags;
import com.datadog.api.client.v2.model.DowntimeResourceType;
import com.datadog.api.client.v2.model.DowntimeResponse;
import com.datadog.api.client.v2.model.DowntimeScheduleCreateRequest;
import com.datadog.api.client.v2.model.DowntimeScheduleOneTimeCreateUpdateRequest;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    DowntimeCreateRequest body =
        new DowntimeCreateRequest()
            .data(
                new DowntimeCreateRequestData()
                    .attributes(
                        new DowntimeCreateRequestAttributes()
                            .message("dark forest")
                            .monitorIdentifier(
                                new DowntimeMonitorIdentifier(
                                    new DowntimeMonitorIdentifierTags()
                                        .monitorTags(Collections.singletonList("cat:hat"))))
                            .scope("test:exampledowntime")
                            .schedule(
                                new DowntimeScheduleCreateRequest(
                                    new DowntimeScheduleOneTimeCreateUpdateRequest().start(null))))
                    .type(DowntimeResourceType.DOWNTIME));

    try {
      DowntimeResponse result = apiInstance.createDowntime(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#createDowntime");
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
Schedule a downtime returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi
from datadog_api_client.v2.model.downtime_create_request import DowntimeCreateRequest
from datadog_api_client.v2.model.downtime_create_request_attributes import DowntimeCreateRequestAttributes
from datadog_api_client.v2.model.downtime_create_request_data import DowntimeCreateRequestData
from datadog_api_client.v2.model.downtime_monitor_identifier_tags import DowntimeMonitorIdentifierTags
from datadog_api_client.v2.model.downtime_resource_type import DowntimeResourceType
from datadog_api_client.v2.model.downtime_schedule_one_time_create_update_request import (
    DowntimeScheduleOneTimeCreateUpdateRequest,
)

body = DowntimeCreateRequest(
    data=DowntimeCreateRequestData(
        attributes=DowntimeCreateRequestAttributes(
            message="dark forest",
            monitor_identifier=DowntimeMonitorIdentifierTags(
                monitor_tags=[
                    "cat:hat",
                ],
            ),
            scope="test:exampledowntime",
            schedule=DowntimeScheduleOneTimeCreateUpdateRequest(
                start=None,
            ),
        ),
        type=DowntimeResourceType.DOWNTIME,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.create_downtime(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Schedule a downtime returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DowntimesAPI.new

body = DatadogAPIClient::V2::DowntimeCreateRequest.new({
  data: DatadogAPIClient::V2::DowntimeCreateRequestData.new({
    attributes: DatadogAPIClient::V2::DowntimeCreateRequestAttributes.new({
      message: "dark forest",
      monitor_identifier: DatadogAPIClient::V2::DowntimeMonitorIdentifierTags.new({
        monitor_tags: [
          "cat:hat",
        ],
      }),
      scope: "test:exampledowntime",
      schedule: DatadogAPIClient::V2::DowntimeScheduleOneTimeCreateUpdateRequest.new({
        start: nil,
      }),
    }),
    type: DatadogAPIClient::V2::DowntimeResourceType::DOWNTIME,
  }),
})
p api_instance.create_downtime(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Schedule a downtime returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_downtimes::DowntimesAPI;
use datadog_api_client::datadogV2::model::DowntimeCreateRequest;
use datadog_api_client::datadogV2::model::DowntimeCreateRequestAttributes;
use datadog_api_client::datadogV2::model::DowntimeCreateRequestData;
use datadog_api_client::datadogV2::model::DowntimeMonitorIdentifier;
use datadog_api_client::datadogV2::model::DowntimeMonitorIdentifierTags;
use datadog_api_client::datadogV2::model::DowntimeResourceType;
use datadog_api_client::datadogV2::model::DowntimeScheduleCreateRequest;
use datadog_api_client::datadogV2::model::DowntimeScheduleOneTimeCreateUpdateRequest;

#[tokio::main]
async fn main() {
    let body = DowntimeCreateRequest::new(DowntimeCreateRequestData::new(
        DowntimeCreateRequestAttributes::new(
            DowntimeMonitorIdentifier::DowntimeMonitorIdentifierTags(Box::new(
                DowntimeMonitorIdentifierTags::new(vec!["cat:hat".to_string()]),
            )),
            "test:exampledowntime".to_string(),
        )
        .message(Some("dark forest".to_string()))
        .schedule(
            DowntimeScheduleCreateRequest::DowntimeScheduleOneTimeCreateUpdateRequest(Box::new(
                DowntimeScheduleOneTimeCreateUpdateRequest::new().start(None),
            )),
        ),
        DowntimeResourceType::DOWNTIME,
    ));
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api.create_downtime(body).await;
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
 * Schedule a downtime returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DowntimesApi(configuration);

const params: v2.DowntimesApiCreateDowntimeRequest = {
  body: {
    data: {
      attributes: {
        message: "dark forest",
        monitorIdentifier: {
          monitorTags: ["cat:hat"],
        },
        scope: "test:exampledowntime",
        schedule: {
          start: undefined,
        },
      },
      type: "downtime",
    },
  },
};

apiInstance
  .createDowntime(params)
  .then((data: v2.DowntimeResponse) => {
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

## Cancel downtimes by scope{% #cancel-downtimes-by-scope %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/downtime/cancel/by_scope |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/downtime/cancel/by_scope |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/downtime/cancel/by_scope      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/downtime/cancel/by_scope      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/downtime/cancel/by_scope     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/downtime/cancel/by_scope |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/downtime/cancel/by_scope |

### Overview

Delete all downtimes that match the scope of `X`. **Note:** This only interacts with Downtimes created using v1 endpoints. This endpoint has been deprecated and will not be replaced. Please use v2 endpoints to find and cancel downtimes. This endpoint requires the `monitors_downtime` permission.

OAuth apps require the `monitors_downtime` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Request

#### Body Data (required)

Scope to cancel downtimes for.

{% tab title="Model" %}

| Field                   | Type   | Description                                                                                                                                                                                                                                                                                   |
| ----------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scope [*required*] | string | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`). |

{% /tab %}

{% tab title="Example" %}

```json
{
  "scope": "string"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Object containing array of IDs of canceled downtimes.

| Field         | Type      | Description                         |
| ------------- | --------- | ----------------------------------- |
| cancelled_ids | [integer] | ID of downtimes that were canceled. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "cancelled_ids": [
    123456789,
    123456790
  ]
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
Downtimes not found
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/downtime/cancel/by_scope" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "scope": "string"
}
EOF
                        
##### 

```go
// Cancel downtimes by scope returns "OK" response

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
	// there is a valid "downtime" in the system
	DowntimeScope0 := os.Getenv("DOWNTIME_SCOPE_0")

	body := datadogV1.CancelDowntimesByScopeRequest{
		Scope: DowntimeScope0,
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewDowntimesApi(apiClient)
	resp, r, err := api.CancelDowntimesByScope(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.CancelDowntimesByScope`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.CancelDowntimesByScope`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Cancel downtimes by scope returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DowntimesApi;
import com.datadog.api.client.v1.model.CancelDowntimesByScopeRequest;
import com.datadog.api.client.v1.model.CanceledDowntimesIds;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    // there is a valid "downtime" in the system
    String DOWNTIME_SCOPE_0 = System.getenv("DOWNTIME_SCOPE_0");

    CancelDowntimesByScopeRequest body =
        new CancelDowntimesByScopeRequest().scope(DOWNTIME_SCOPE_0);

    try {
      CanceledDowntimesIds result = apiInstance.cancelDowntimesByScope(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#cancelDowntimesByScope");
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

# Cancel all downtimes with scope
api.Downtime.cancel_downtime_by_scope('env:testing')
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
##### 

```python
"""
Cancel downtimes by scope returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.cancel_downtimes_by_scope_request import CancelDowntimesByScopeRequest

# there is a valid "downtime" in the system
DOWNTIME_SCOPE_0 = environ["DOWNTIME_SCOPE_0"]

body = CancelDowntimesByScopeRequest(
    scope=DOWNTIME_SCOPE_0,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.cancel_downtimes_by_scope(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Cancel all downtimes with the given scope
dog.cancel_downtime_by_scope('env:testing')
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```ruby
# Cancel downtimes by scope returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DowntimesAPI.new

# there is a valid "downtime" in the system
DOWNTIME_SCOPE_0 = ENV["DOWNTIME_SCOPE_0"]

body = DatadogAPIClient::V1::CancelDowntimesByScopeRequest.new({
  scope: DOWNTIME_SCOPE_0,
})
p api_instance.cancel_downtimes_by_scope(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Cancel downtimes by scope returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_downtimes::DowntimesAPI;
use datadog_api_client::datadogV1::model::CancelDowntimesByScopeRequest;

#[tokio::main]
async fn main() {
    // there is a valid "downtime" in the system
    let downtime_scope_0 = std::env::var("DOWNTIME_SCOPE_0").unwrap();
    let body = CancelDowntimesByScopeRequest::new(downtime_scope_0.clone());
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api.cancel_downtimes_by_scope(body).await;
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
 * Cancel downtimes by scope returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DowntimesApi(configuration);

// there is a valid "downtime" in the system
const DOWNTIME_SCOPE_0 = process.env.DOWNTIME_SCOPE_0 as string;

const params: v1.DowntimesApiCancelDowntimesByScopeRequest = {
  body: {
    scope: DOWNTIME_SCOPE_0,
  },
};

apiInstance
  .cancelDowntimesByScope(params)
  .then((data: v1.CanceledDowntimesIds) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
## Cancel a downtime{% #cancel-a-downtime %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/downtime/{downtime_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/downtime/{downtime_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/downtime/{downtime_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/downtime/{downtime_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/downtime/{downtime_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/downtime/{downtime_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/downtime/{downtime_id} |

### Overview

Cancel a downtime. **Note:** This endpoint has been deprecated. Please use v2 endpoints. This endpoint requires the `monitors_downtime` permission.

OAuth apps require the `monitors_downtime` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Arguments

#### Path Parameters

| Name                          | Type    | Description                   |
| ----------------------------- | ------- | ----------------------------- |
| downtime_id [*required*] | integer | ID of the downtime to cancel. |

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
Downtime not found
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
                  \# Path parametersexport downtime_id="123456"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/downtime/${downtime_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Cancel a downtime returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi

# there is a valid "downtime" in the system
DOWNTIME_ID = environ["DOWNTIME_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    api_instance.cancel_downtime(
        downtime_id=int(DOWNTIME_ID),
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Cancel a downtime returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DowntimesAPI.new

# there is a valid "downtime" in the system
DOWNTIME_ID = ENV["DOWNTIME_ID"]
api_instance.cancel_downtime(DOWNTIME_ID.to_i)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Cancel a downtime returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	// there is a valid "downtime" in the system
	DowntimeID, _ := strconv.ParseInt(os.Getenv("DOWNTIME_ID"), 10, 64)

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewDowntimesApi(apiClient)
	r, err := api.CancelDowntime(ctx, DowntimeID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.CancelDowntime`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Cancel a downtime returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DowntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    // there is a valid "downtime" in the system
    Long DOWNTIME_ID = Long.parseLong(System.getenv("DOWNTIME_ID"));

    try {
      apiInstance.cancelDowntime(DOWNTIME_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#cancelDowntime");
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
// Cancel a downtime returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_downtimes::DowntimesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "downtime" in the system
    let downtime_id: i64 = std::env::var("DOWNTIME_ID").unwrap().parse().unwrap();
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api.cancel_downtime(downtime_id.clone()).await;
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
 * Cancel a downtime returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DowntimesApi(configuration);

// there is a valid "downtime" in the system
const DOWNTIME_ID = parseInt(process.env.DOWNTIME_ID as string);

const params: v1.DowntimesApiCancelDowntimeRequest = {
  downtimeId: DOWNTIME_ID,
};

apiInstance
  .cancelDowntime(params)
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

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/downtime/{downtime_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/downtime/{downtime_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/downtime/{downtime_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/downtime/{downtime_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/downtime/{downtime_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/downtime/{downtime_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/downtime/{downtime_id} |

### Overview



Cancel a downtime.

**Note**: Downtimes canceled through the API are no longer active, but are retained for approximately two days before being permanently removed. The downtime may still appear in search results until it is permanently removed.
This endpoint requires the `monitors_downtime` permission.
OAuth apps require the `monitors_downtime` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Arguments

#### Path Parameters

| Name                          | Type   | Description                   |
| ----------------------------- | ------ | ----------------------------- |
| downtime_id [*required*] | string | ID of the downtime to cancel. |

### Response

{% tab title="204" %}
OK
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
Downtime not found
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
                  \# Path parametersexport downtime_id="00000000-0000-1234-0000-000000000000"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/downtime/${downtime_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Cancel a downtime returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi

# there is a valid "downtime_v2" in the system
DOWNTIME_V2_DATA_ID = environ["DOWNTIME_V2_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    api_instance.cancel_downtime(
        downtime_id=DOWNTIME_V2_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Cancel a downtime returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DowntimesAPI.new

# there is a valid "downtime_v2" in the system
DOWNTIME_V2_DATA_ID = ENV["DOWNTIME_V2_DATA_ID"]
api_instance.cancel_downtime(DOWNTIME_V2_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Cancel a downtime returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "downtime_v2" in the system
	DowntimeV2DataID := os.Getenv("DOWNTIME_V2_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDowntimesApi(apiClient)
	r, err := api.CancelDowntime(ctx, DowntimeV2DataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.CancelDowntime`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Cancel a downtime returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DowntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    // there is a valid "downtime_v2" in the system
    String DOWNTIME_V2_DATA_ID = System.getenv("DOWNTIME_V2_DATA_ID");

    try {
      apiInstance.cancelDowntime(DOWNTIME_V2_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#cancelDowntime");
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
// Cancel a downtime returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_downtimes::DowntimesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "downtime_v2" in the system
    let downtime_v2_data_id = std::env::var("DOWNTIME_V2_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api.cancel_downtime(downtime_v2_data_id.clone()).await;
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
 * Cancel a downtime returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DowntimesApi(configuration);

// there is a valid "downtime_v2" in the system
const DOWNTIME_V2_DATA_ID = process.env.DOWNTIME_V2_DATA_ID as string;

const params: v2.DowntimesApiCancelDowntimeRequest = {
  downtimeId: DOWNTIME_V2_DATA_ID,
};

apiInstance
  .cancelDowntime(params)
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

## Get a downtime{% #get-a-downtime %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/downtime/{downtime_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/downtime/{downtime_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/downtime/{downtime_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/downtime/{downtime_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/downtime/{downtime_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/downtime/{downtime_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/downtime/{downtime_id} |

### Overview

Get downtime detail by `downtime_id`. **Note:** This endpoint has been deprecated. Please use v2 endpoints. This endpoint requires the `monitors_read` permission.

OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Arguments

#### Path Parameters

| Name                          | Type    | Description                  |
| ----------------------------- | ------- | ---------------------------- |
| downtime_id [*required*] | integer | ID of the downtime to fetch. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Downtiming gives you greater control over monitor notifications by allowing you to globally exclude scopes from alerting. Downtime settings, which can be scheduled with start and end times, prevent all alerting related to specified Datadog tags.

| Parent field | Field                            | Type     | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | -------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
|              | active_child                     | object   | The downtime object definition of the active child for the original parent recurring downtime. This field will only exist on recurring downtimes.                                                                                                                                                                                                                |
| active_child | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
| active_child | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
| active_child | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
| active_child | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
| active_child | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
| active_child | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
| active_child | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
| active_child | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
| active_child | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
| active_child | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
| active_child | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
| active_child | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
| active_child | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
| active_child | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
| active_child | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
| active_child | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
| active_child | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
| active_child | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
| active_child | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |
|              | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
|              | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
|              | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
|              | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
|              | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
|              | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
|              | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
|              | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
|              | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
|              | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
|              | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
|              | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
|              | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
|              | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
|              | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
|              | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
|              | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
|              | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "active": true,
  "active_child": {
    "active": true,
    "canceled": 1412799983,
    "creator_id": 123456,
    "disabled": false,
    "downtime_type": 2,
    "end": 1412793983,
    "id": 1626,
    "message": "Message on the downtime",
    "monitor_id": 123456,
    "monitor_tags": [
      "*"
    ],
    "mute_first_recovery_notification": false,
    "notify_end_states": [
      "alert",
      "no data",
      "warn"
    ],
    "notify_end_types": [
      "canceled",
      "expired"
    ],
    "parent_id": 123,
    "recurrence": {
      "period": 1,
      "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
      "type": "weeks",
      "until_date": 1447786293,
      "until_occurrences": 2,
      "week_days": [
        "Mon",
        "Tue"
      ]
    },
    "scope": [
      "env:staging"
    ],
    "start": 1412792983,
    "timezone": "America/New_York",
    "updater_id": 123456
  },
  "canceled": 1412799983,
  "creator_id": 123456,
  "disabled": false,
  "downtime_type": 2,
  "end": 1412793983,
  "id": 1625,
  "message": "Message on the downtime",
  "monitor_id": 123456,
  "monitor_tags": [
    "*"
  ],
  "mute_first_recovery_notification": false,
  "notify_end_states": [
    "alert",
    "no data",
    "warn"
  ],
  "notify_end_types": [
    "canceled",
    "expired"
  ],
  "parent_id": 123,
  "recurrence": {
    "period": 1,
    "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
    "type": "weeks",
    "until_date": 1447786293,
    "until_occurrences": 2,
    "week_days": [
      "Mon",
      "Tue"
    ]
  },
  "scope": [
    "env:staging"
  ],
  "start": 1412792983,
  "timezone": "America/New_York",
  "updater_id": 123456
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
Downtime not found
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
                  \# Path parametersexport downtime_id="123456"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/downtime/${downtime_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a downtime returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi

# there is a valid "downtime" in the system
DOWNTIME_ID = environ["DOWNTIME_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.get_downtime(
        downtime_id=int(DOWNTIME_ID),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a downtime returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DowntimesAPI.new

# there is a valid "downtime" in the system
DOWNTIME_ID = ENV["DOWNTIME_ID"]
p api_instance.get_downtime(DOWNTIME_ID.to_i)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```ruby
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Get a downtime object
downtime_id = 1625
dog.get_downtime(downtime_id)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a downtime returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	// there is a valid "downtime" in the system
	DowntimeID, _ := strconv.ParseInt(os.Getenv("DOWNTIME_ID"), 10, 64)

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewDowntimesApi(apiClient)
	resp, r, err := api.GetDowntime(ctx, DowntimeID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.GetDowntime`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.GetDowntime`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a downtime returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DowntimesApi;
import com.datadog.api.client.v1.model.Downtime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    // there is a valid "downtime" in the system
    Long DOWNTIME_ID = Long.parseLong(System.getenv("DOWNTIME_ID"));

    try {
      Downtime result = apiInstance.getDowntime(DOWNTIME_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#getDowntime");
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

# Get a downtime
api.Downtime.get(2910)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
##### 

```rust
// Get a downtime returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_downtimes::DowntimesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "downtime" in the system
    let downtime_id: i64 = std::env::var("DOWNTIME_ID").unwrap().parse().unwrap();
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api.get_downtime(downtime_id.clone()).await;
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
 * Get a downtime returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DowntimesApi(configuration);

// there is a valid "downtime" in the system
const DOWNTIME_ID = parseInt(process.env.DOWNTIME_ID as string);

const params: v1.DowntimesApiGetDowntimeRequest = {
  downtimeId: DOWNTIME_ID,
};

apiInstance
  .getDowntime(params)
  .then((data: v1.Downtime) => {
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

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/downtime/{downtime_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/downtime/{downtime_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/downtime/{downtime_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/downtime/{downtime_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/downtime/{downtime_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/downtime/{downtime_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/downtime/{downtime_id} |

### Overview

Get downtime detail by `downtime_id`. This endpoint requires the `monitors_downtime` permission.

OAuth apps require the `monitors_downtime` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Arguments

#### Path Parameters

| Name                          | Type   | Description                  |
| ----------------------------- | ------ | ---------------------------- |
| downtime_id [*required*] | string | ID of the downtime to fetch. |

#### Query Strings

| Name    | Type   | Description                                                                                                                                       |
| ------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resource paths for related resources to include in the response. Supported resource paths are `created_by` and `monitor`. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Downtiming gives you greater control over monitor notifications by allowing you to globally exclude scopes from alerting. Downtime settings, which can be scheduled with start and end times, prevent all alerting related to specified Datadog tags.

| Parent field       | Field                            | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | -------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                             | object          | Downtime data.                                                                                                                                                                                                                                                                                                                                                                                |
| data               | attributes                       | object          | Downtime details.                                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | canceled                         | date-time       | Time that the downtime was canceled.                                                                                                                                                                                                                                                                                                                                                          |
| attributes         | created                          | date-time       | Creation time of the downtime.                                                                                                                                                                                                                                                                                                                                                                |
| attributes         | display_timezone                 | string          | The timezone in which to display the downtime's start and end times in Datadog applications. This is not used as an offset for scheduling.                                                                                                                                                                                                                                                    |
| attributes         | message                          | string          | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                                                |
| attributes         | modified                         | date-time       | Time that the downtime was last modified.                                                                                                                                                                                                                                                                                                                                                     |
| attributes         | monitor_identifier               |  <oneOf>   | Monitor identifier for the downtime.                                                                                                                                                                                                                                                                                                                                                          |
| monitor_identifier | Option 1                         | object          | Object of the monitor identifier.                                                                                                                                                                                                                                                                                                                                                             |
| Option 1           | monitor_id [*required*]     | int64           | ID of the monitor to prevent notifications.                                                                                                                                                                                                                                                                                                                                                   |
| monitor_identifier | Option 2                         | object          | Object of the monitor tags.                                                                                                                                                                                                                                                                                                                                                                   |
| Option 2           | monitor_tags [*required*]   | [string]        | A list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match **all** provided monitor tags. Setting `monitor_tags` to `[*]` configures the downtime to mute all monitors for the given scope. |
| attributes         | mute_first_recovery_notification | boolean         | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                                                         |
| attributes         | notify_end_states                | [string]        | States that will trigger a monitor notification when the `notify_end_types` action occurs.                                                                                                                                                                                                                                                                                                    |
| attributes         | notify_end_types                 | [string]        | Actions that will trigger a monitor notification if the downtime is in the `notify_end_types` state.                                                                                                                                                                                                                                                                                          |
| attributes         | schedule                         |  <oneOf>   | The schedule that defines when the monitor starts, stops, and recurs. There are two types of schedules: one-time and recurring. Recurring schedules may have up to five RRULE-based recurrences. If no schedules are provided, the downtime will begin immediately and never end.                                                                                                             |
| schedule           | Option 1                         | object          | A recurring downtime schedule definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1           | current_downtime                 | object          | The most recent actual start and end dates for a recurring downtime. For a canceled downtime, this is the previously occurring downtime. For active downtimes, this is the ongoing downtime, and for scheduled downtimes it is the upcoming downtime.                                                                                                                                         |
| current_downtime   | end                              | date-time       | The end of the current downtime.                                                                                                                                                                                                                                                                                                                                                              |
| current_downtime   | start                            | date-time       | The start of the current downtime.                                                                                                                                                                                                                                                                                                                                                            |
| Option 1           | recurrences [*required*]    | [object]        | A list of downtime recurrences.                                                                                                                                                                                                                                                                                                                                                               |
| recurrences        | duration                         | string          | The length of the downtime. Must begin with an integer and end with one of 'm', 'h', d', or 'w'.                                                                                                                                                                                                                                                                                              |
| recurrences        | rrule                            | string          | The `RRULE` standard for defining recurring events. For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.                                                                         | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api). |
| recurrences        | start                            | string          | ISO-8601 Datetime to start the downtime. Must not include a UTC offset. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                        |
| Option 1           | timezone                         | string          | The timezone in which to schedule the downtime. This affects recurring start and end dates. Must match `display_timezone`.                                                                                                                                                                                                                                                                    |
| schedule           | Option 2                         | object          | A one-time downtime definition.                                                                                                                                                                                                                                                                                                                                                               |
| Option 2           | end                              | date-time       | ISO-8601 Datetime to end the downtime.                                                                                                                                                                                                                                                                                                                                                        |
| Option 2           | start [*required*]          | date-time       | ISO-8601 Datetime to start the downtime.                                                                                                                                                                                                                                                                                                                                                      |
| attributes         | scope                            | string          | The scope to which the downtime applies. Must follow the [common search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/).                                                                                                                                                                                                                                                     |
| attributes         | status                           | enum            | The current status of the downtime. Allowed enum values: `active,canceled,ended,scheduled`                                                                                                                                                                                                                                                                                                    |
| data               | id                               | string          | The downtime ID.                                                                                                                                                                                                                                                                                                                                                                              |
| data               | relationships                    | object          | All relationships associated with downtime.                                                                                                                                                                                                                                                                                                                                                   |
| relationships      | created_by                       | object          | The user who created the downtime.                                                                                                                                                                                                                                                                                                                                                            |
| created_by         | data                             | object          | Data for the user who created the downtime.                                                                                                                                                                                                                                                                                                                                                   |
| data               | id                               | string          | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                                              |
| data               | type                             | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| relationships      | monitor                          | object          | The monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                                       |
| monitor            | data                             | object          | Data for the monitor.                                                                                                                                                                                                                                                                                                                                                                         |
| data               | id                               | string          | Monitor ID of the downtime.                                                                                                                                                                                                                                                                                                                                                                   |
| data               | type                             | enum            | Monitor resource type. Allowed enum values: `monitors`                                                                                                                                                                                                                                                                                                                                        |
| data               | type                             | enum            | Downtime resource type. Allowed enum values: `downtime`                                                                                                                                                                                                                                                                                                                                       |
|                    | included                         | [ <oneOf>] | Array of objects related to the downtime that the user requested.                                                                                                                                                                                                                                                                                                                             |
| included           | Option 1                         | object          | User object returned by the API.                                                                                                                                                                                                                                                                                                                                                              |
| Option 1           | attributes                       | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                                                                                                                |
| attributes         | created_at                       | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                                                                                                                    |
| attributes         | disabled                         | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                                                                                                                 |
| attributes         | email                            | string          | Email of the user.                                                                                                                                                                                                                                                                                                                                                                            |
| attributes         | handle                           | string          | Handle of the user.                                                                                                                                                                                                                                                                                                                                                                           |
| attributes         | icon                             | string          | URL of the user's icon.                                                                                                                                                                                                                                                                                                                                                                       |
| attributes         | last_login_time                  | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | mfa_enabled                      | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                                                                                                                      |
| attributes         | modified_at                      | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                                                                                                                         |
| attributes         | name                             | string          | Name of the user.                                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | service_account                  | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                                                                                                                        |
| attributes         | status                           | string          | Status of the user.                                                                                                                                                                                                                                                                                                                                                                           |
| attributes         | title                            | string          | Title of the user.                                                                                                                                                                                                                                                                                                                                                                            |
| attributes         | verified                         | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                                                                                                                 |
| Option 1           | id                               | string          | ID of the user.                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1           | relationships                    | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                                                                                                                         |
| relationships      | org                              | object          | Relationship to an organization.                                                                                                                                                                                                                                                                                                                                                              |
| org                | data [*required*]           | object          | Relationship to organization object.                                                                                                                                                                                                                                                                                                                                                          |
| data               | id [*required*]             | string          | ID of the organization.                                                                                                                                                                                                                                                                                                                                                                       |
| data               | type [*required*]           | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                                                                                                                      |
| relationships      | other_orgs                       | object          | Relationship to organizations.                                                                                                                                                                                                                                                                                                                                                                |
| other_orgs         | data [*required*]           | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                                                                                                                        |
| data               | id [*required*]             | string          | ID of the organization.                                                                                                                                                                                                                                                                                                                                                                       |
| data               | type [*required*]           | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                                                                                                                      |
| relationships      | other_users                      | object          | Relationship to users.                                                                                                                                                                                                                                                                                                                                                                        |
| other_users        | data [*required*]           | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                                                                                                                |
| data               | id [*required*]             | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                                                                                                                 |
| data               | type [*required*]           | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| relationships      | roles                            | object          | Relationship to roles.                                                                                                                                                                                                                                                                                                                                                                        |
| roles              | data                             | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                                                                                                                 |
| data               | id                               | string          | The unique identifier of the role.                                                                                                                                                                                                                                                                                                                                                            |
| data               | type                             | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                                                                                                                      |
| Option 1           | type                             | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| included           | Option 2                         | object          | Information about the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                     |
| Option 2           | attributes                       | object          | Attributes of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                         |
| attributes         | name                             | string          | The name of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                           |
| Option 2           | id                               | int64           | ID of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                                 |
| Option 2           | type                             | enum            | Monitor resource type. Allowed enum values: `monitors`                                                                                                                                                                                                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "canceled": "2020-01-02T03:04:05.282979+0000",
      "created": "2020-01-02T03:04:05.282979+0000",
      "display_timezone": "America/New_York",
      "message": "Message about the downtime",
      "modified": "2020-01-02T03:04:05.282979+0000",
      "monitor_identifier": {
        "monitor_id": 123
      },
      "mute_first_recovery_notification": false,
      "notify_end_states": [
        "alert",
        "warn"
      ],
      "notify_end_types": [
        "canceled",
        "expired"
      ],
      "schedule": {
        "current_downtime": {
          "end": "2020-01-02T03:04:00.000Z",
          "start": "2020-01-02T03:04:00.000Z"
        },
        "recurrences": [
          {
            "duration": "123d",
            "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
            "start": "2020-01-02T03:04"
          }
        ],
        "timezone": "America/New_York"
      },
      "scope": "env:(staging OR prod) AND datacenter:us-east-1",
      "status": "active"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-1234-0000-000000000000",
          "type": "users"
        }
      },
      "monitor": {
        "data": {
          "id": "12345",
          "type": "monitors"
        }
      }
    },
    "type": "downtime"
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ]
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
                  \# Path parametersexport downtime_id="00000000-0000-1234-0000-000000000000"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/downtime/${downtime_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a downtime returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi

# there is a valid "downtime_v2" in the system
DOWNTIME_V2_DATA_ID = environ["DOWNTIME_V2_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.get_downtime(
        downtime_id=DOWNTIME_V2_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a downtime returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DowntimesAPI.new

# there is a valid "downtime_v2" in the system
DOWNTIME_V2_DATA_ID = ENV["DOWNTIME_V2_DATA_ID"]
p api_instance.get_downtime(DOWNTIME_V2_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a downtime returns "OK" response

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
	// there is a valid "downtime_v2" in the system
	DowntimeV2DataID := os.Getenv("DOWNTIME_V2_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDowntimesApi(apiClient)
	resp, r, err := api.GetDowntime(ctx, DowntimeV2DataID, *datadogV2.NewGetDowntimeOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.GetDowntime`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.GetDowntime`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a downtime returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DowntimesApi;
import com.datadog.api.client.v2.model.DowntimeResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    // there is a valid "downtime_v2" in the system
    String DOWNTIME_V2_DATA_ID = System.getenv("DOWNTIME_V2_DATA_ID");

    try {
      DowntimeResponse result = apiInstance.getDowntime(DOWNTIME_V2_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#getDowntime");
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
// Get a downtime returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_downtimes::DowntimesAPI;
use datadog_api_client::datadogV2::api_downtimes::GetDowntimeOptionalParams;

#[tokio::main]
async fn main() {
    // there is a valid "downtime_v2" in the system
    let downtime_v2_data_id = std::env::var("DOWNTIME_V2_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api
        .get_downtime(
            downtime_v2_data_id.clone(),
            GetDowntimeOptionalParams::default(),
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
 * Get a downtime returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DowntimesApi(configuration);

// there is a valid "downtime_v2" in the system
const DOWNTIME_V2_DATA_ID = process.env.DOWNTIME_V2_DATA_ID as string;

const params: v2.DowntimesApiGetDowntimeRequest = {
  downtimeId: DOWNTIME_V2_DATA_ID,
};

apiInstance
  .getDowntime(params)
  .then((data: v2.DowntimeResponse) => {
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

## Update a downtime{% #update-a-downtime %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/downtime/{downtime_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/downtime/{downtime_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/downtime/{downtime_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/downtime/{downtime_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/downtime/{downtime_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/downtime/{downtime_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/downtime/{downtime_id} |

### Overview

Update a single downtime by `downtime_id`. **Note:** This endpoint has been deprecated. Please use v2 endpoints. This endpoint requires the `monitors_downtime` permission.

OAuth apps require the `monitors_downtime` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Arguments

#### Path Parameters

| Name                          | Type    | Description                   |
| ----------------------------- | ------- | ----------------------------- |
| downtime_id [*required*] | integer | ID of the downtime to update. |

### Request

#### Body Data (required)

Update a downtime request body.

{% tab title="Model" %}

| Parent field | Field                            | Type     | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | -------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
|              | active_child                     | object   | The downtime object definition of the active child for the original parent recurring downtime. This field will only exist on recurring downtimes.                                                                                                                                                                                                                |
| active_child | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
| active_child | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
| active_child | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
| active_child | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
| active_child | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
| active_child | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
| active_child | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
| active_child | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
| active_child | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
| active_child | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
| active_child | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
| active_child | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
| active_child | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
| active_child | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
| active_child | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
| active_child | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
| active_child | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
| active_child | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
| active_child | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |
|              | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
|              | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
|              | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
|              | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
|              | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
|              | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
|              | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
|              | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
|              | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
|              | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
|              | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
|              | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
|              | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
|              | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
|              | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
|              | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
|              | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
|              | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "message": "Example-Downtime-updated",
  "mute_first_recovery_notification": true,
  "notify_end_states": [
    "alert",
    "no data",
    "warn"
  ],
  "notify_end_types": [
    "canceled",
    "expired"
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Downtiming gives you greater control over monitor notifications by allowing you to globally exclude scopes from alerting. Downtime settings, which can be scheduled with start and end times, prevent all alerting related to specified Datadog tags.

| Parent field | Field                            | Type     | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | -------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
|              | active_child                     | object   | The downtime object definition of the active child for the original parent recurring downtime. This field will only exist on recurring downtimes.                                                                                                                                                                                                                |
| active_child | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
| active_child | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
| active_child | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
| active_child | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
| active_child | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
| active_child | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
| active_child | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
| active_child | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
| active_child | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
| active_child | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
| active_child | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
| active_child | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
| active_child | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
| active_child | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
| active_child | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
| active_child | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
| active_child | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
| active_child | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
| active_child | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |
|              | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
|              | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
|              | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
|              | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
|              | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
|              | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
|              | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
|              | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
|              | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
|              | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
|              | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
|              | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
|              | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
|              | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
|              | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
|              | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
|              | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
|              | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "active": true,
  "active_child": {
    "active": true,
    "canceled": 1412799983,
    "creator_id": 123456,
    "disabled": false,
    "downtime_type": 2,
    "end": 1412793983,
    "id": 1626,
    "message": "Message on the downtime",
    "monitor_id": 123456,
    "monitor_tags": [
      "*"
    ],
    "mute_first_recovery_notification": false,
    "notify_end_states": [
      "alert",
      "no data",
      "warn"
    ],
    "notify_end_types": [
      "canceled",
      "expired"
    ],
    "parent_id": 123,
    "recurrence": {
      "period": 1,
      "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
      "type": "weeks",
      "until_date": 1447786293,
      "until_occurrences": 2,
      "week_days": [
        "Mon",
        "Tue"
      ]
    },
    "scope": [
      "env:staging"
    ],
    "start": 1412792983,
    "timezone": "America/New_York",
    "updater_id": 123456
  },
  "canceled": 1412799983,
  "creator_id": 123456,
  "disabled": false,
  "downtime_type": 2,
  "end": 1412793983,
  "id": 1625,
  "message": "Message on the downtime",
  "monitor_id": 123456,
  "monitor_tags": [
    "*"
  ],
  "mute_first_recovery_notification": false,
  "notify_end_states": [
    "alert",
    "no data",
    "warn"
  ],
  "notify_end_types": [
    "canceled",
    "expired"
  ],
  "parent_id": 123,
  "recurrence": {
    "period": 1,
    "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
    "type": "weeks",
    "until_date": 1447786293,
    "until_occurrences": 2,
    "week_days": [
      "Mon",
      "Tue"
    ]
  },
  "scope": [
    "env:staging"
  ],
  "start": 1412792983,
  "timezone": "America/New_York",
  "updater_id": 123456
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
Downtime not found
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
                          \# Path parametersexport downtime_id="123456"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/downtime/${downtime_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "message": "Example-Downtime-updated",
  "mute_first_recovery_notification": true,
  "notify_end_states": [
    "alert",
    "no data",
    "warn"
  ],
  "notify_end_types": [
    "canceled",
    "expired"
  ]
}
EOF
                        
##### 

```go
// Update a downtime returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	// there is a valid "downtime" in the system
	DowntimeID, _ := strconv.ParseInt(os.Getenv("DOWNTIME_ID"), 10, 64)

	body := datadogV1.Downtime{
		Message:                       *datadog.NewNullableString(datadog.PtrString("Example-Downtime-updated")),
		MuteFirstRecoveryNotification: datadog.PtrBool(true),
		NotifyEndStates: []datadogV1.NotifyEndState{
			datadogV1.NOTIFYENDSTATE_ALERT,
			datadogV1.NOTIFYENDSTATE_NO_DATA,
			datadogV1.NOTIFYENDSTATE_WARN,
		},
		NotifyEndTypes: []datadogV1.NotifyEndType{
			datadogV1.NOTIFYENDTYPE_CANCELED,
			datadogV1.NOTIFYENDTYPE_EXPIRED,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewDowntimesApi(apiClient)
	resp, r, err := api.UpdateDowntime(ctx, DowntimeID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.UpdateDowntime`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.UpdateDowntime`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update a downtime returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DowntimesApi;
import com.datadog.api.client.v1.model.Downtime;
import com.datadog.api.client.v1.model.NotifyEndState;
import com.datadog.api.client.v1.model.NotifyEndType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    // there is a valid "downtime" in the system
    Long DOWNTIME_ID = Long.parseLong(System.getenv("DOWNTIME_ID"));

    Downtime body =
        new Downtime()
            .message("Example-Downtime-updated")
            .muteFirstRecoveryNotification(true)
            .notifyEndStates(
                Arrays.asList(NotifyEndState.ALERT, NotifyEndState.NO_DATA, NotifyEndState.WARN))
            .notifyEndTypes(Arrays.asList(NotifyEndType.CANCELED, NotifyEndType.EXPIRED));

    try {
      Downtime result = apiInstance.updateDowntime(DOWNTIME_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#updateDowntime");
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
Update a downtime returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime
from datadog_api_client.v1.model.notify_end_state import NotifyEndState
from datadog_api_client.v1.model.notify_end_type import NotifyEndType

# there is a valid "downtime" in the system
DOWNTIME_ID = environ["DOWNTIME_ID"]

body = Downtime(
    message="Example-Downtime-updated",
    mute_first_recovery_notification=True,
    notify_end_states=[
        NotifyEndState.ALERT,
        NotifyEndState.NO_DATA,
        NotifyEndState.WARN,
    ],
    notify_end_types=[
        NotifyEndType.CANCELED,
        NotifyEndType.EXPIRED,
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.update_downtime(downtime_id=int(DOWNTIME_ID), body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update a downtime returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DowntimesAPI.new

# there is a valid "downtime" in the system
DOWNTIME_ID = ENV["DOWNTIME_ID"]

body = DatadogAPIClient::V1::Downtime.new({
  message: "Example-Downtime-updated",
  mute_first_recovery_notification: true,
  notify_end_states: [
    DatadogAPIClient::V1::NotifyEndState::ALERT,
    DatadogAPIClient::V1::NotifyEndState::NO_DATA,
    DatadogAPIClient::V1::NotifyEndState::WARN,
  ],
  notify_end_types: [
    DatadogAPIClient::V1::NotifyEndType::CANCELED,
    DatadogAPIClient::V1::NotifyEndType::EXPIRED,
  ],
})
p api_instance.update_downtime(DOWNTIME_ID.to_i, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Update a downtime returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_downtimes::DowntimesAPI;
use datadog_api_client::datadogV1::model::Downtime;
use datadog_api_client::datadogV1::model::NotifyEndState;
use datadog_api_client::datadogV1::model::NotifyEndType;

#[tokio::main]
async fn main() {
    // there is a valid "downtime" in the system
    let downtime_id: i64 = std::env::var("DOWNTIME_ID").unwrap().parse().unwrap();
    let body = Downtime::new()
        .message(Some("Example-Downtime-updated".to_string()))
        .mute_first_recovery_notification(true)
        .notify_end_states(vec![
            NotifyEndState::ALERT,
            NotifyEndState::NO_DATA,
            NotifyEndState::WARN,
        ])
        .notify_end_types(vec![NotifyEndType::CANCELED, NotifyEndType::EXPIRED]);
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api.update_downtime(downtime_id.clone(), body).await;
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
 * Update a downtime returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DowntimesApi(configuration);

// there is a valid "downtime" in the system
const DOWNTIME_ID = parseInt(process.env.DOWNTIME_ID as string);

const params: v1.DowntimesApiUpdateDowntimeRequest = {
  body: {
    message: "Example-Downtime-updated",
    muteFirstRecoveryNotification: true,
    notifyEndStates: ["alert", "no data", "warn"],
    notifyEndTypes: ["canceled", "expired"],
  },
  downtimeId: DOWNTIME_ID,
};

apiInstance
  .updateDowntime(params)
  .then((data: v1.Downtime) => {
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

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/downtime/{downtime_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/downtime/{downtime_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/downtime/{downtime_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/downtime/{downtime_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/downtime/{downtime_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/downtime/{downtime_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/downtime/{downtime_id} |

### Overview

Update a downtime by `downtime_id`. This endpoint requires the `monitors_downtime` permission.

OAuth apps require the `monitors_downtime` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Arguments

#### Path Parameters

| Name                          | Type   | Description                   |
| ----------------------------- | ------ | ----------------------------- |
| downtime_id [*required*] | string | ID of the downtime to update. |

### Request

#### Body Data (required)

Update a downtime request body.

{% tab title="Model" %}

| Parent field       | Field                            | Type          | Description                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | -------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data [*required*]           | object        | Object to update a downtime.                                                                                                                                                                                                                                                                                                                                                                  |
| data               | attributes [*required*]     | object        | Attributes of the downtime to update.                                                                                                                                                                                                                                                                                                                                                         |
| attributes         | display_timezone                 | string        | The timezone in which to display the downtime's start and end times in Datadog applications. This is not used as an offset for scheduling.                                                                                                                                                                                                                                                    |
| attributes         | message                          | string        | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                                                |
| attributes         | monitor_identifier               |  <oneOf> | Monitor identifier for the downtime.                                                                                                                                                                                                                                                                                                                                                          |
| monitor_identifier | Option 1                         | object        | Object of the monitor identifier.                                                                                                                                                                                                                                                                                                                                                             |
| Option 1           | monitor_id [*required*]     | int64         | ID of the monitor to prevent notifications.                                                                                                                                                                                                                                                                                                                                                   |
| monitor_identifier | Option 2                         | object        | Object of the monitor tags.                                                                                                                                                                                                                                                                                                                                                                   |
| Option 2           | monitor_tags [*required*]   | [string]      | A list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match **all** provided monitor tags. Setting `monitor_tags` to `[*]` configures the downtime to mute all monitors for the given scope. |
| attributes         | mute_first_recovery_notification | boolean       | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                                                         |
| attributes         | notify_end_states                | [string]      | States that will trigger a monitor notification when the `notify_end_types` action occurs.                                                                                                                                                                                                                                                                                                    |
| attributes         | notify_end_types                 | [string]      | Actions that will trigger a monitor notification if the downtime is in the `notify_end_types` state.                                                                                                                                                                                                                                                                                          |
| attributes         | schedule                         |  <oneOf> | Schedule for the downtime.                                                                                                                                                                                                                                                                                                                                                                    |
| schedule           | Option 1                         | object        | A recurring downtime schedule definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1           | recurrences                      | [object]      | A list of downtime recurrences.                                                                                                                                                                                                                                                                                                                                                               |
| recurrences        | duration [*required*]       | string        | The length of the downtime. Must begin with an integer and end with one of 'm', 'h', d', or 'w'.                                                                                                                                                                                                                                                                                              |
| recurrences        | rrule [*required*]          | string        | The `RRULE` standard for defining recurring events. For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.                                                                         | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api). |
| recurrences        | start                            | string        | ISO-8601 Datetime to start the downtime. Must not include a UTC offset. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                        |
| Option 1           | timezone                         | string        | The timezone in which to schedule the downtime.                                                                                                                                                                                                                                                                                                                                               |
| schedule           | Option 2                         | object        | A one-time downtime definition.                                                                                                                                                                                                                                                                                                                                                               |
| Option 2           | end                              | date-time     | ISO-8601 Datetime to end the downtime. Must include a UTC offset of zero. If not provided, the downtime continues forever.                                                                                                                                                                                                                                                                    |
| Option 2           | start                            | date-time     | ISO-8601 Datetime to start the downtime. Must include a UTC offset of zero. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                    |
| attributes         | scope                            | string        | The scope to which the downtime applies. Must follow the [common search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/).                                                                                                                                                                                                                                                     |
| data               | id [*required*]             | string        | ID of this downtime.                                                                                                                                                                                                                                                                                                                                                                          |
| data               | type [*required*]           | enum          | Downtime resource type. Allowed enum values: `downtime`                                                                                                                                                                                                                                                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "message": "light speed"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "downtime"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Downtiming gives you greater control over monitor notifications by allowing you to globally exclude scopes from alerting. Downtime settings, which can be scheduled with start and end times, prevent all alerting related to specified Datadog tags.

| Parent field       | Field                            | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | -------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                             | object          | Downtime data.                                                                                                                                                                                                                                                                                                                                                                                |
| data               | attributes                       | object          | Downtime details.                                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | canceled                         | date-time       | Time that the downtime was canceled.                                                                                                                                                                                                                                                                                                                                                          |
| attributes         | created                          | date-time       | Creation time of the downtime.                                                                                                                                                                                                                                                                                                                                                                |
| attributes         | display_timezone                 | string          | The timezone in which to display the downtime's start and end times in Datadog applications. This is not used as an offset for scheduling.                                                                                                                                                                                                                                                    |
| attributes         | message                          | string          | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                                                |
| attributes         | modified                         | date-time       | Time that the downtime was last modified.                                                                                                                                                                                                                                                                                                                                                     |
| attributes         | monitor_identifier               |  <oneOf>   | Monitor identifier for the downtime.                                                                                                                                                                                                                                                                                                                                                          |
| monitor_identifier | Option 1                         | object          | Object of the monitor identifier.                                                                                                                                                                                                                                                                                                                                                             |
| Option 1           | monitor_id [*required*]     | int64           | ID of the monitor to prevent notifications.                                                                                                                                                                                                                                                                                                                                                   |
| monitor_identifier | Option 2                         | object          | Object of the monitor tags.                                                                                                                                                                                                                                                                                                                                                                   |
| Option 2           | monitor_tags [*required*]   | [string]        | A list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match **all** provided monitor tags. Setting `monitor_tags` to `[*]` configures the downtime to mute all monitors for the given scope. |
| attributes         | mute_first_recovery_notification | boolean         | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                                                         |
| attributes         | notify_end_states                | [string]        | States that will trigger a monitor notification when the `notify_end_types` action occurs.                                                                                                                                                                                                                                                                                                    |
| attributes         | notify_end_types                 | [string]        | Actions that will trigger a monitor notification if the downtime is in the `notify_end_types` state.                                                                                                                                                                                                                                                                                          |
| attributes         | schedule                         |  <oneOf>   | The schedule that defines when the monitor starts, stops, and recurs. There are two types of schedules: one-time and recurring. Recurring schedules may have up to five RRULE-based recurrences. If no schedules are provided, the downtime will begin immediately and never end.                                                                                                             |
| schedule           | Option 1                         | object          | A recurring downtime schedule definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1           | current_downtime                 | object          | The most recent actual start and end dates for a recurring downtime. For a canceled downtime, this is the previously occurring downtime. For active downtimes, this is the ongoing downtime, and for scheduled downtimes it is the upcoming downtime.                                                                                                                                         |
| current_downtime   | end                              | date-time       | The end of the current downtime.                                                                                                                                                                                                                                                                                                                                                              |
| current_downtime   | start                            | date-time       | The start of the current downtime.                                                                                                                                                                                                                                                                                                                                                            |
| Option 1           | recurrences [*required*]    | [object]        | A list of downtime recurrences.                                                                                                                                                                                                                                                                                                                                                               |
| recurrences        | duration                         | string          | The length of the downtime. Must begin with an integer and end with one of 'm', 'h', d', or 'w'.                                                                                                                                                                                                                                                                                              |
| recurrences        | rrule                            | string          | The `RRULE` standard for defining recurring events. For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.                                                                         | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api). |
| recurrences        | start                            | string          | ISO-8601 Datetime to start the downtime. Must not include a UTC offset. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                        |
| Option 1           | timezone                         | string          | The timezone in which to schedule the downtime. This affects recurring start and end dates. Must match `display_timezone`.                                                                                                                                                                                                                                                                    |
| schedule           | Option 2                         | object          | A one-time downtime definition.                                                                                                                                                                                                                                                                                                                                                               |
| Option 2           | end                              | date-time       | ISO-8601 Datetime to end the downtime.                                                                                                                                                                                                                                                                                                                                                        |
| Option 2           | start [*required*]          | date-time       | ISO-8601 Datetime to start the downtime.                                                                                                                                                                                                                                                                                                                                                      |
| attributes         | scope                            | string          | The scope to which the downtime applies. Must follow the [common search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/).                                                                                                                                                                                                                                                     |
| attributes         | status                           | enum            | The current status of the downtime. Allowed enum values: `active,canceled,ended,scheduled`                                                                                                                                                                                                                                                                                                    |
| data               | id                               | string          | The downtime ID.                                                                                                                                                                                                                                                                                                                                                                              |
| data               | relationships                    | object          | All relationships associated with downtime.                                                                                                                                                                                                                                                                                                                                                   |
| relationships      | created_by                       | object          | The user who created the downtime.                                                                                                                                                                                                                                                                                                                                                            |
| created_by         | data                             | object          | Data for the user who created the downtime.                                                                                                                                                                                                                                                                                                                                                   |
| data               | id                               | string          | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                                              |
| data               | type                             | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| relationships      | monitor                          | object          | The monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                                       |
| monitor            | data                             | object          | Data for the monitor.                                                                                                                                                                                                                                                                                                                                                                         |
| data               | id                               | string          | Monitor ID of the downtime.                                                                                                                                                                                                                                                                                                                                                                   |
| data               | type                             | enum            | Monitor resource type. Allowed enum values: `monitors`                                                                                                                                                                                                                                                                                                                                        |
| data               | type                             | enum            | Downtime resource type. Allowed enum values: `downtime`                                                                                                                                                                                                                                                                                                                                       |
|                    | included                         | [ <oneOf>] | Array of objects related to the downtime that the user requested.                                                                                                                                                                                                                                                                                                                             |
| included           | Option 1                         | object          | User object returned by the API.                                                                                                                                                                                                                                                                                                                                                              |
| Option 1           | attributes                       | object          | Attributes of user object returned by the API.                                                                                                                                                                                                                                                                                                                                                |
| attributes         | created_at                       | date-time       | Creation time of the user.                                                                                                                                                                                                                                                                                                                                                                    |
| attributes         | disabled                         | boolean         | Whether the user is disabled.                                                                                                                                                                                                                                                                                                                                                                 |
| attributes         | email                            | string          | Email of the user.                                                                                                                                                                                                                                                                                                                                                                            |
| attributes         | handle                           | string          | Handle of the user.                                                                                                                                                                                                                                                                                                                                                                           |
| attributes         | icon                             | string          | URL of the user's icon.                                                                                                                                                                                                                                                                                                                                                                       |
| attributes         | last_login_time                  | date-time       | The last time the user logged in.                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | mfa_enabled                      | boolean         | If user has MFA enabled.                                                                                                                                                                                                                                                                                                                                                                      |
| attributes         | modified_at                      | date-time       | Time that the user was last modified.                                                                                                                                                                                                                                                                                                                                                         |
| attributes         | name                             | string          | Name of the user.                                                                                                                                                                                                                                                                                                                                                                             |
| attributes         | service_account                  | boolean         | Whether the user is a service account.                                                                                                                                                                                                                                                                                                                                                        |
| attributes         | status                           | string          | Status of the user.                                                                                                                                                                                                                                                                                                                                                                           |
| attributes         | title                            | string          | Title of the user.                                                                                                                                                                                                                                                                                                                                                                            |
| attributes         | verified                         | boolean         | Whether the user is verified.                                                                                                                                                                                                                                                                                                                                                                 |
| Option 1           | id                               | string          | ID of the user.                                                                                                                                                                                                                                                                                                                                                                               |
| Option 1           | relationships                    | object          | Relationships of the user object returned by the API.                                                                                                                                                                                                                                                                                                                                         |
| relationships      | org                              | object          | Relationship to an organization.                                                                                                                                                                                                                                                                                                                                                              |
| org                | data [*required*]           | object          | Relationship to organization object.                                                                                                                                                                                                                                                                                                                                                          |
| data               | id [*required*]             | string          | ID of the organization.                                                                                                                                                                                                                                                                                                                                                                       |
| data               | type [*required*]           | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                                                                                                                      |
| relationships      | other_orgs                       | object          | Relationship to organizations.                                                                                                                                                                                                                                                                                                                                                                |
| other_orgs         | data [*required*]           | [object]        | Relationships to organization objects.                                                                                                                                                                                                                                                                                                                                                        |
| data               | id [*required*]             | string          | ID of the organization.                                                                                                                                                                                                                                                                                                                                                                       |
| data               | type [*required*]           | enum            | Organizations resource type. Allowed enum values: `orgs`                                                                                                                                                                                                                                                                                                                                      |
| relationships      | other_users                      | object          | Relationship to users.                                                                                                                                                                                                                                                                                                                                                                        |
| other_users        | data [*required*]           | [object]        | Relationships to user objects.                                                                                                                                                                                                                                                                                                                                                                |
| data               | id [*required*]             | string          | A unique identifier that represents the user.                                                                                                                                                                                                                                                                                                                                                 |
| data               | type [*required*]           | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| relationships      | roles                            | object          | Relationship to roles.                                                                                                                                                                                                                                                                                                                                                                        |
| roles              | data                             | [object]        | An array containing type and the unique identifier of a role.                                                                                                                                                                                                                                                                                                                                 |
| data               | id                               | string          | The unique identifier of the role.                                                                                                                                                                                                                                                                                                                                                            |
| data               | type                             | enum            | Roles type. Allowed enum values: `roles`                                                                                                                                                                                                                                                                                                                                                      |
| Option 1           | type                             | enum            | Users resource type. Allowed enum values: `users`                                                                                                                                                                                                                                                                                                                                             |
| included           | Option 2                         | object          | Information about the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                     |
| Option 2           | attributes                       | object          | Attributes of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                         |
| attributes         | name                             | string          | The name of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                           |
| Option 2           | id                               | int64           | ID of the monitor identified by the downtime.                                                                                                                                                                                                                                                                                                                                                 |
| Option 2           | type                             | enum            | Monitor resource type. Allowed enum values: `monitors`                                                                                                                                                                                                                                                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "canceled": "2020-01-02T03:04:05.282979+0000",
      "created": "2020-01-02T03:04:05.282979+0000",
      "display_timezone": "America/New_York",
      "message": "Message about the downtime",
      "modified": "2020-01-02T03:04:05.282979+0000",
      "monitor_identifier": {
        "monitor_id": 123
      },
      "mute_first_recovery_notification": false,
      "notify_end_states": [
        "alert",
        "warn"
      ],
      "notify_end_types": [
        "canceled",
        "expired"
      ],
      "schedule": {
        "current_downtime": {
          "end": "2020-01-02T03:04:00.000Z",
          "start": "2020-01-02T03:04:00.000Z"
        },
        "recurrences": [
          {
            "duration": "123d",
            "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
            "start": "2020-01-02T03:04"
          }
        ],
        "timezone": "America/New_York"
      },
      "scope": "env:(staging OR prod) AND datacenter:us-east-1",
      "status": "active"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-1234-0000-000000000000",
          "type": "users"
        }
      },
      "monitor": {
        "data": {
          "id": "12345",
          "type": "monitors"
        }
      }
    },
    "type": "downtime"
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ]
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
Downtime not found
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
                          \# Path parametersexport downtime_id="00e000000-0000-1234-0000-000000000000"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/downtime/${downtime_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "message": "light speed"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "downtime"
  }
}
EOF
                        
##### 

```go
// Update a downtime returns "OK" response

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
	// there is a valid "downtime_v2" in the system
	DowntimeV2DataID := os.Getenv("DOWNTIME_V2_DATA_ID")

	body := datadogV2.DowntimeUpdateRequest{
		Data: datadogV2.DowntimeUpdateRequestData{
			Attributes: datadogV2.DowntimeUpdateRequestAttributes{
				Message: *datadog.NewNullableString(datadog.PtrString("light speed")),
			},
			Id:   DowntimeV2DataID,
			Type: datadogV2.DOWNTIMERESOURCETYPE_DOWNTIME,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDowntimesApi(apiClient)
	resp, r, err := api.UpdateDowntime(ctx, DowntimeV2DataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.UpdateDowntime`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.UpdateDowntime`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update a downtime returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DowntimesApi;
import com.datadog.api.client.v2.model.DowntimeResourceType;
import com.datadog.api.client.v2.model.DowntimeResponse;
import com.datadog.api.client.v2.model.DowntimeUpdateRequest;
import com.datadog.api.client.v2.model.DowntimeUpdateRequestAttributes;
import com.datadog.api.client.v2.model.DowntimeUpdateRequestData;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    // there is a valid "downtime_v2" in the system
    String DOWNTIME_V2_DATA_ID = System.getenv("DOWNTIME_V2_DATA_ID");

    DowntimeUpdateRequest body =
        new DowntimeUpdateRequest()
            .data(
                new DowntimeUpdateRequestData()
                    .attributes(new DowntimeUpdateRequestAttributes().message("light speed"))
                    .id(DOWNTIME_V2_DATA_ID)
                    .type(DowntimeResourceType.DOWNTIME));

    try {
      DowntimeResponse result = apiInstance.updateDowntime(DOWNTIME_V2_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#updateDowntime");
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
Update a downtime returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi
from datadog_api_client.v2.model.downtime_resource_type import DowntimeResourceType
from datadog_api_client.v2.model.downtime_update_request import DowntimeUpdateRequest
from datadog_api_client.v2.model.downtime_update_request_attributes import DowntimeUpdateRequestAttributes
from datadog_api_client.v2.model.downtime_update_request_data import DowntimeUpdateRequestData

# there is a valid "downtime_v2" in the system
DOWNTIME_V2_DATA_ID = environ["DOWNTIME_V2_DATA_ID"]

body = DowntimeUpdateRequest(
    data=DowntimeUpdateRequestData(
        attributes=DowntimeUpdateRequestAttributes(
            message="light speed",
        ),
        id=DOWNTIME_V2_DATA_ID,
        type=DowntimeResourceType.DOWNTIME,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.update_downtime(downtime_id=DOWNTIME_V2_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update a downtime returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DowntimesAPI.new

# there is a valid "downtime_v2" in the system
DOWNTIME_V2_DATA_ID = ENV["DOWNTIME_V2_DATA_ID"]

body = DatadogAPIClient::V2::DowntimeUpdateRequest.new({
  data: DatadogAPIClient::V2::DowntimeUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::DowntimeUpdateRequestAttributes.new({
      message: "light speed",
    }),
    id: DOWNTIME_V2_DATA_ID,
    type: DatadogAPIClient::V2::DowntimeResourceType::DOWNTIME,
  }),
})
p api_instance.update_downtime(DOWNTIME_V2_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Update a downtime returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_downtimes::DowntimesAPI;
use datadog_api_client::datadogV2::model::DowntimeResourceType;
use datadog_api_client::datadogV2::model::DowntimeUpdateRequest;
use datadog_api_client::datadogV2::model::DowntimeUpdateRequestAttributes;
use datadog_api_client::datadogV2::model::DowntimeUpdateRequestData;

#[tokio::main]
async fn main() {
    // there is a valid "downtime_v2" in the system
    let downtime_v2_data_id = std::env::var("DOWNTIME_V2_DATA_ID").unwrap();
    let body = DowntimeUpdateRequest::new(DowntimeUpdateRequestData::new(
        DowntimeUpdateRequestAttributes::new().message(Some("light speed".to_string())),
        downtime_v2_data_id.clone(),
        DowntimeResourceType::DOWNTIME,
    ));
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api.update_downtime(downtime_v2_data_id.clone(), body).await;
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
 * Update a downtime returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DowntimesApi(configuration);

// there is a valid "downtime_v2" in the system
const DOWNTIME_V2_DATA_ID = process.env.DOWNTIME_V2_DATA_ID as string;

const params: v2.DowntimesApiUpdateDowntimeRequest = {
  body: {
    data: {
      attributes: {
        message: "light speed",
      },
      id: DOWNTIME_V2_DATA_ID,
      type: "downtime",
    },
  },
  downtimeId: DOWNTIME_V2_DATA_ID,
};

apiInstance
  .updateDowntime(params)
  .then((data: v2.DowntimeResponse) => {
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

## Get active downtimes for a monitor{% #get-active-downtimes-for-a-monitor %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/monitor/{monitor_id}/downtimes |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/monitor/{monitor_id}/downtimes |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/monitor/{monitor_id}/downtimes      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/monitor/{monitor_id}/downtimes      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/monitor/{monitor_id}/downtimes     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/monitor/{monitor_id}/downtimes |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/monitor/{monitor_id}/downtimes |

### Overview

Get all active v1 downtimes for the specified monitor. **Note:** This endpoint has been deprecated. Please use v2 endpoints. This endpoint requires the `monitors_read` permission.

OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type    | Description           |
| ---------------------------- | ------- | --------------------- |
| monitor_id [*required*] | integer | The id of the monitor |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                            | Type     | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | -------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
|              | active_child                     | object   | The downtime object definition of the active child for the original parent recurring downtime. This field will only exist on recurring downtimes.                                                                                                                                                                                                                |
| active_child | active                           | boolean  | If a scheduled downtime currently exists.                                                                                                                                                                                                                                                                                                                        |
| active_child | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
| active_child | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
| active_child | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
| active_child | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
| active_child | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
| active_child | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
| active_child | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
| active_child | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
| active_child | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
| active_child | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
| active_child | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
| active_child | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
| active_child | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
| active_child | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
| active_child | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
| active_child | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
| active_child | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
| active_child | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |
|              | canceled                         | int64    | If a scheduled downtime is canceled.                                                                                                                                                                                                                                                                                                                             |
|              | creator_id                       | int32    | User ID of the downtime creator.                                                                                                                                                                                                                                                                                                                                 |
|              | disabled                         | boolean  | If a downtime has been disabled.                                                                                                                                                                                                                                                                                                                                 |
|              | downtime_type                    | int32    | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts.                                                                                                                                                                                                               |
|              | end                              | int64    | POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely until you cancel it.                                                                                                                                                                                                                                                |
|              | id                               | int64    | The downtime ID.                                                                                                                                                                                                                                                                                                                                                 |
|              | message                          | string   | A message to include with notifications for this downtime. Email notifications can be sent to specific users by using the same `@username` notation as events.                                                                                                                                                                                                   |
|              | monitor_id                       | int64    | A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.                                                                                                                                                                                                                                                           |
|              | monitor_tags                     | [string] | A comma-separated list of monitor tags. For example, tags that are applied directly to monitors, not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags. For example, `service:postgres` **AND** `team:frontend`. |
|              | mute_first_recovery_notification | boolean  | If the first recovery notification during a downtime should be muted.                                                                                                                                                                                                                                                                                            |
|              | notify_end_states                | [string] | States for which `notify_end_types` sends out notifications for.                                                                                                                                                                                                                                                                                                 |
|              | notify_end_types                 | [string] | If set, notifies if a monitor is in an alert-worthy state (`ALERT`, `WARNING`, or `NO DATA`) when this downtime expires or is canceled. Applied to monitors that change states during the downtime (such as from `OK` to `ALERT`, `WARNING`, or `NO DATA`), and to monitors that already have an alert-worthy state when downtime begins.                        |
|              | parent_id                        | int64    | ID of the parent Downtime.                                                                                                                                                                                                                                                                                                                                       |
|              | recurrence                       | object   | An object defining the recurrence of the downtime.                                                                                                                                                                                                                                                                                                               |
| recurrence   | period                           | int32    | How often to repeat as an integer. For example, to repeat every 3 days, select a type of `days` and a period of `3`.                                                                                                                                                                                                                                             |
| recurrence   | rrule                            | string   | The `RRULE` standard for defining recurring events (**requires to set "type" to rrule**) For example, to have a recurring event on the first day of each month, set the type to `rrule` and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`. Most common `rrule` options from the [iCalendar Spec](https://tools.ietf.org/html/rfc5545) are supported.       | **Note**: Attributes specifying the duration in `RRULE` are not supported (for example, `DTSTART`, `DTEND`, `DURATION`). More examples available in this [downtime guide](https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api) |
| recurrence   | type                             | string   | The type of recurrence. Choose from `days`, `weeks`, `months`, `years`, `rrule`.                                                                                                                                                                                                                                                                                 |
| recurrence   | until_date                       | int64    | The date at which the recurrence should end as a POSIX timestamp. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                    |
| recurrence   | until_occurrences                | int32    | How many times the downtime is rescheduled. `until_occurences` and `until_date` are mutually exclusive.                                                                                                                                                                                                                                                          |
| recurrence   | week_days                        | [string] | A list of week days to repeat on. Choose from `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` or `Sun`. Only applicable when type is weeks. First letter must be capitalized.                                                                                                                                                                                           |
|              | scope                            | [string] | The scope(s) to which the downtime applies and must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).                                                                    |
|              | start                            | int64    | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.                                                                                                                                                                                                                                                            |
|              | timezone                         | string   | The timezone in which to display the downtime's start and end times in Datadog applications.                                                                                                                                                                                                                                                                     |
|              | updater_id                       | int32    | ID of the last user that updated the downtime.                                                                                                                                                                                                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "active": true,
  "active_child": {
    "active": true,
    "canceled": 1412799983,
    "creator_id": 123456,
    "disabled": false,
    "downtime_type": 2,
    "end": 1412793983,
    "id": 1626,
    "message": "Message on the downtime",
    "monitor_id": 123456,
    "monitor_tags": [
      "*"
    ],
    "mute_first_recovery_notification": false,
    "notify_end_states": [
      "alert",
      "no data",
      "warn"
    ],
    "notify_end_types": [
      "canceled",
      "expired"
    ],
    "parent_id": 123,
    "recurrence": {
      "period": 1,
      "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
      "type": "weeks",
      "until_date": 1447786293,
      "until_occurrences": 2,
      "week_days": [
        "Mon",
        "Tue"
      ]
    },
    "scope": [
      "env:staging"
    ],
    "start": 1412792983,
    "timezone": "America/New_York",
    "updater_id": 123456
  },
  "canceled": 1412799983,
  "creator_id": 123456,
  "disabled": false,
  "downtime_type": 2,
  "end": 1412793983,
  "id": 1625,
  "message": "Message on the downtime",
  "monitor_id": 123456,
  "monitor_tags": [
    "*"
  ],
  "mute_first_recovery_notification": false,
  "notify_end_states": [
    "alert",
    "no data",
    "warn"
  ],
  "notify_end_types": [
    "canceled",
    "expired"
  ],
  "parent_id": 123,
  "recurrence": {
    "period": 1,
    "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
    "type": "weeks",
    "until_date": 1447786293,
    "until_occurrences": 2,
    "week_days": [
      "Mon",
      "Tue"
    ]
  },
  "scope": [
    "env:staging"
  ],
  "start": 1412792983,
  "timezone": "America/New_York",
  "updater_id": 123456
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

{% tab title="404" %}
Monitor Not Found error
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
                  \# Path parametersexport monitor_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/${monitor_id}/downtimes" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get active downtimes for a monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.list_monitor_downtimes(
        monitor_id=9223372036854775807,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get active downtimes for a monitor returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DowntimesAPI.new
p api_instance.list_monitor_downtimes(9223372036854775807)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get active downtimes for a monitor returns "OK" response

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
	api := datadogV1.NewDowntimesApi(apiClient)
	resp, r, err := api.ListMonitorDowntimes(ctx, 9223372036854775807)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.ListMonitorDowntimes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.ListMonitorDowntimes`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get active downtimes for a monitor returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DowntimesApi;
import com.datadog.api.client.v1.model.Downtime;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    try {
      List<Downtime> result = apiInstance.listMonitorDowntimes(9223372036854775807L);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#listMonitorDowntimes");
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
// Get active downtimes for a monitor returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_downtimes::DowntimesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api.list_monitor_downtimes(9223372036854775807).await;
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
 * Get active downtimes for a monitor returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DowntimesApi(configuration);

const params: v1.DowntimesApiListMonitorDowntimesRequest = {
  monitorId: 9223372036854775807,
};

apiInstance
  .listMonitorDowntimes(params)
  .then((data: v1.Downtime[]) => {
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

| Datadog site      | API endpoint                                                                   |
| ----------------- | ------------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/monitor/{monitor_id}/downtime_matches |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/monitor/{monitor_id}/downtime_matches |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/monitor/{monitor_id}/downtime_matches      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/monitor/{monitor_id}/downtime_matches      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/monitor/{monitor_id}/downtime_matches     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/monitor/{monitor_id}/downtime_matches |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/monitor/{monitor_id}/downtime_matches |

### Overview

Get all active downtimes for the specified monitor. This endpoint requires the `monitors_downtime` permission.

OAuth apps require the `monitors_downtime` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#downtimes) to access this endpoint.



### Arguments

#### Path Parameters

| Name                         | Type    | Description            |
| ---------------------------- | ------- | ---------------------- |
| monitor_id [*required*] | integer | The id of the monitor. |

#### Query Strings

| Name         | Type    | Description                                                   |
| ------------ | ------- | ------------------------------------------------------------- |
| page[offset] | integer | Specific offset to use as the beginning of the returned page. |
| page[limit]  | integer | Maximum number of downtimes in the response.                  |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response for retrieving all downtime matches for a monitor.

| Parent field | Field                | Type      | Description                                                                                                                               |
| ------------ | -------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                 | [object]  | An array of downtime matches.                                                                                                             |
| data         | attributes           | object    | Downtime match details.                                                                                                                   |
| attributes   | end                  | date-time | The end of the downtime.                                                                                                                  |
| attributes   | groups               | [string]  | An array of groups associated with the downtime.                                                                                          |
| attributes   | scope                | string    | The scope to which the downtime applies. Must follow the [common search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/). |
| attributes   | start                | date-time | The start of the downtime.                                                                                                                |
| data         | id                   | string    | The downtime ID.                                                                                                                          |
| data         | type                 | enum      | Monitor Downtime Match resource type. Allowed enum values: `downtime_match`                                                               |
|              | meta                 | object    | Pagination metadata returned by the API.                                                                                                  |
| meta         | page                 | object    | Object containing the total filtered count.                                                                                               |
| page         | total_filtered_count | int64     | Total count of elements matched by the filter.                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "end": "2020-01-02T03:04:00.000Z",
        "groups": [
          "service:postgres",
          "team:frontend"
        ],
        "scope": "env:(staging OR prod) AND datacenter:us-east-1",
        "start": "2020-01-02T03:04:00.000Z"
      },
      "id": "00000000-0000-1234-0000-000000000000",
      "type": "downtime_match"
    }
  ],
  "meta": {
    "page": {
      "total_filtered_count": "integer"
    }
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Monitor Not Found error
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
                  \# Path parametersexport monitor_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/${monitor_id}/downtime_matches" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get active downtimes for a monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.list_monitor_downtimes(
        monitor_id=35534610,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get active downtimes for a monitor returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DowntimesAPI.new
p api_instance.list_monitor_downtimes(35534610)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get active downtimes for a monitor returns "OK" response

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
	api := datadogV2.NewDowntimesApi(apiClient)
	resp, r, err := api.ListMonitorDowntimes(ctx, 35534610, *datadogV2.NewListMonitorDowntimesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DowntimesApi.ListMonitorDowntimes`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DowntimesApi.ListMonitorDowntimes`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get active downtimes for a monitor returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DowntimesApi;
import com.datadog.api.client.v2.model.MonitorDowntimeMatchResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DowntimesApi apiInstance = new DowntimesApi(defaultClient);

    try {
      MonitorDowntimeMatchResponse result = apiInstance.listMonitorDowntimes(35534610L);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DowntimesApi#listMonitorDowntimes");
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
// Get active downtimes for a monitor returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_downtimes::DowntimesAPI;
use datadog_api_client::datadogV2::api_downtimes::ListMonitorDowntimesOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = DowntimesAPI::with_config(configuration);
    let resp = api
        .list_monitor_downtimes(35534610, ListMonitorDowntimesOptionalParams::default())
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
 * Get active downtimes for a monitor returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DowntimesApi(configuration);

const params: v2.DowntimesApiListMonitorDowntimesRequest = {
  monitorId: 35534610,
};

apiInstance
  .listMonitorDowntimes(params)
  .then((data: v2.MonitorDowntimeMatchResponse) => {
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
