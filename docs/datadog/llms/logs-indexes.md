# Source: https://docs.datadoghq.com/api/latest/logs-indexes.md

---
title: Logs Indexes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Logs Indexes
---

# Logs Indexes

Manage configuration of [log indexes](https://docs.datadoghq.com/logs/indexes/).

## Get all indexes{% #get-all-indexes %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/logs/config/indexes |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/logs/config/indexes |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/logs/config/indexes      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/logs/config/indexes      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/logs/config/indexes     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/logs/config/indexes |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/logs/config/indexes |

### Overview

The Index object describes the configuration of a log index. This endpoint returns an array of the `LogIndex` objects of your organization. This endpoint requires the `logs_read_config` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Object with all Index configurations for a given organization.

| Parent field      | Field                                    | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------- | ---------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | indexes                                  | [object] | Array of Log index configurations.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| indexes           | daily_limit                              | int64    | The number of log events you can send in this index per day before you are rate-limited.                                                                                                                                                                                                                                                                                                                                                                                         |
| indexes           | daily_limit_reset                        | object   | Object containing options to override the default daily limit reset time.                                                                                                                                                                                                                                                                                                                                                                                                        |
| daily_limit_reset | reset_time                               | string   | String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).                                                                                                                                                                                                                                                                                                                                          |
| daily_limit_reset | reset_utc_offset                         | string   | String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).                                                                                                                                                                                                                                                                                                                                   |
| indexes           | daily_limit_warning_threshold_percentage | double   | A percentage threshold of the daily quota at which a Datadog warning event is generated.                                                                                                                                                                                                                                                                                                                                                                                         |
| indexes           | exclusion_filters                        | [object] | An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.                                                                                                                                                                                                                                                                            |
| exclusion_filters | filter                                   | object   | Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.                                                                                                                                                                                                                                                                                                                                                                                           |
| filter            | query                                    | string   | Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.                                                                                                                                                                                                                                                                                                                            |
| filter            | sample_rate [*required*]            | double   | Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.                                                                                                                                                                                                                                                                                                                                                           |
| exclusion_filters | is_enabled                               | boolean  | Whether or not the exclusion filter is active.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| exclusion_filters | name [*required*]                   | string   | Name of the index exclusion filter.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| indexes           | filter [*required*]                 | object   | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| filter            | query                                    | string   | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| indexes           | is_rate_limited                          | boolean  | A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. Rate limit is reset every-day at 2pm UTC.                                                                                                                                                                                                                                                                                                                                 |
| indexes           | name [*required*]                   | string   | The name of the index.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| indexes           | num_flex_logs_retention_days             | int64    | The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions. |
| indexes           | num_retention_days                       | int64    | The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.                                                                                                                                                                                                                                                     |
| indexes           | tags                                     | [string] | A list of tags associated with the index. Tags must be in `key:value` format.                                                                                                                                                                                                                                                                                                                                                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "indexes": [
    {
      "daily_limit": 300000000,
      "daily_limit_reset": {
        "reset_time": "14:00",
        "reset_utc_offset": "+02:00"
      },
      "daily_limit_warning_threshold_percentage": 70,
      "exclusion_filters": [
        {
          "filter": {
            "query": "*",
            "sample_rate": 1
          },
          "is_enabled": false,
          "name": "payment"
        }
      ],
      "filter": {
        "query": "source:python"
      },
      "is_rate_limited": false,
      "name": "main",
      "num_flex_logs_retention_days": 360,
      "num_retention_days": 15,
      "tags": [
        "team:backend",
        "env:production"
      ]
    }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/indexes" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all indexes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.list_log_indexes()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get all indexes returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new
p api_instance.list_log_indexes()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get all indexes returns "OK" response

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
    api := datadogV1.NewLogsIndexesApi(apiClient)
    resp, r, err := api.ListLogIndexes(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.ListLogIndexes`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.ListLogIndexes`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get all indexes returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsIndexListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    try {
      LogsIndexListResponse result = apiInstance.listLogIndexes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#listLogIndexes");
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
// Get all indexes returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.list_log_indexes().await;
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
 * Get all indexes returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

apiInstance
  .listLogIndexes()
  .then((data: v1.LogsIndexListResponse) => {
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

## Get an index{% #get-an-index %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/logs/config/indexes/{name} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/logs/config/indexes/{name} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/logs/config/indexes/{name}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/logs/config/indexes/{name}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/logs/config/indexes/{name}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/logs/config/indexes/{name} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/logs/config/indexes/{name} |

### Overview

Get one log index from your organization. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.

### Arguments

#### Path Parameters

| Name                   | Type   | Description            |
| ---------------------- | ------ | ---------------------- |
| name [*required*] | string | Name of the log index. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Object describing a Datadog Log index.

| Parent field      | Field                                    | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------- | ---------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | daily_limit                              | int64    | The number of log events you can send in this index per day before you are rate-limited.                                                                                                                                                                                                                                                                                                                                                                                         |
|                   | daily_limit_reset                        | object   | Object containing options to override the default daily limit reset time.                                                                                                                                                                                                                                                                                                                                                                                                        |
| daily_limit_reset | reset_time                               | string   | String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).                                                                                                                                                                                                                                                                                                                                          |
| daily_limit_reset | reset_utc_offset                         | string   | String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).                                                                                                                                                                                                                                                                                                                                   |
|                   | daily_limit_warning_threshold_percentage | double   | A percentage threshold of the daily quota at which a Datadog warning event is generated.                                                                                                                                                                                                                                                                                                                                                                                         |
|                   | exclusion_filters                        | [object] | An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.                                                                                                                                                                                                                                                                            |
| exclusion_filters | filter                                   | object   | Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.                                                                                                                                                                                                                                                                                                                                                                                           |
| filter            | query                                    | string   | Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.                                                                                                                                                                                                                                                                                                                            |
| filter            | sample_rate [*required*]            | double   | Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.                                                                                                                                                                                                                                                                                                                                                           |
| exclusion_filters | is_enabled                               | boolean  | Whether or not the exclusion filter is active.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| exclusion_filters | name [*required*]                   | string   | Name of the index exclusion filter.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                   | filter [*required*]                 | object   | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| filter            | query                                    | string   | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                   | is_rate_limited                          | boolean  | A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. Rate limit is reset every-day at 2pm UTC.                                                                                                                                                                                                                                                                                                                                 |
|                   | name [*required*]                   | string   | The name of the index.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                   | num_flex_logs_retention_days             | int64    | The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions. |
|                   | num_retention_days                       | int64    | The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.                                                                                                                                                                                                                                                     |
|                   | tags                                     | [string] | A list of tags associated with the index. Tags must be in `key:value` format.                                                                                                                                                                                                                                                                                                                                                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "daily_limit": 300000000,
  "daily_limit_reset": {
    "reset_time": "14:00",
    "reset_utc_offset": "+02:00"
  },
  "daily_limit_warning_threshold_percentage": 70,
  "exclusion_filters": [
    {
      "filter": {
        "query": "*",
        "sample_rate": 1
      },
      "is_enabled": false,
      "name": "payment"
    }
  ],
  "filter": {
    "query": "source:python"
  },
  "is_rate_limited": false,
  "name": "main",
  "num_flex_logs_retention_days": 360,
  "num_retention_days": 15,
  "tags": [
    "team:backend",
    "env:production"
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
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
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
                  \# Path parametersexport name="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/indexes/${name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get an index returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.get_logs_index(
        name="name",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get an index returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new
p api_instance.get_logs_index("name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get an index returns "OK" response

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
    api := datadogV1.NewLogsIndexesApi(apiClient)
    resp, r, err := api.GetLogsIndex(ctx, "name")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.GetLogsIndex`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.GetLogsIndex`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get an index returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsIndex;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    try {
      LogsIndex result = apiInstance.getLogsIndex("name");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#getLogsIndex");
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
// Get an index returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.get_logs_index("name".to_string()).await;
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
 * Get an index returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

const params: v1.LogsIndexesApiGetLogsIndexRequest = {
  name: "name",
};

apiInstance
  .getLogsIndex(params)
  .then((data: v1.LogsIndex) => {
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

## Create an index{% #create-an-index %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/logs/config/indexes |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/logs/config/indexes |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/logs/config/indexes      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/logs/config/indexes      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/logs/config/indexes     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/logs/config/indexes |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/logs/config/indexes |

### Overview

Creates a new index. Returns the Index object passed in the request body when the request is successful. This endpoint requires the `logs_modify_indexes` permission.

### Request

#### Body Data (required)

Object containing the new index.

{% tab title="Model" %}

| Parent field      | Field                                    | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------- | ---------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | daily_limit                              | int64    | The number of log events you can send in this index per day before you are rate-limited.                                                                                                                                                                                                                                                                                                                                                                                         |
|                   | daily_limit_reset                        | object   | Object containing options to override the default daily limit reset time.                                                                                                                                                                                                                                                                                                                                                                                                        |
| daily_limit_reset | reset_time                               | string   | String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).                                                                                                                                                                                                                                                                                                                                          |
| daily_limit_reset | reset_utc_offset                         | string   | String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).                                                                                                                                                                                                                                                                                                                                   |
|                   | daily_limit_warning_threshold_percentage | double   | A percentage threshold of the daily quota at which a Datadog warning event is generated.                                                                                                                                                                                                                                                                                                                                                                                         |
|                   | exclusion_filters                        | [object] | An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.                                                                                                                                                                                                                                                                            |
| exclusion_filters | filter                                   | object   | Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.                                                                                                                                                                                                                                                                                                                                                                                           |
| filter            | query                                    | string   | Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.                                                                                                                                                                                                                                                                                                                            |
| filter            | sample_rate [*required*]            | double   | Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.                                                                                                                                                                                                                                                                                                                                                           |
| exclusion_filters | is_enabled                               | boolean  | Whether or not the exclusion filter is active.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| exclusion_filters | name [*required*]                   | string   | Name of the index exclusion filter.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                   | filter [*required*]                 | object   | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| filter            | query                                    | string   | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                   | is_rate_limited                          | boolean  | A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. Rate limit is reset every-day at 2pm UTC.                                                                                                                                                                                                                                                                                                                                 |
|                   | name [*required*]                   | string   | The name of the index.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                   | num_flex_logs_retention_days             | int64    | The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions. |
|                   | num_retention_days                       | int64    | The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.                                                                                                                                                                                                                                                     |
|                   | tags                                     | [string] | A list of tags associated with the index. Tags must be in `key:value` format.                                                                                                                                                                                                                                                                                                                                                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "daily_limit": 300000000,
  "daily_limit_reset": {
    "reset_time": "14:00",
    "reset_utc_offset": "+02:00"
  },
  "daily_limit_warning_threshold_percentage": 70,
  "exclusion_filters": [
    {
      "filter": {
        "query": "*",
        "sample_rate": 1
      },
      "is_enabled": false,
      "name": "payment"
    }
  ],
  "filter": {
    "query": "source:python"
  },
  "name": "main",
  "num_flex_logs_retention_days": 360,
  "num_retention_days": 15,
  "tags": [
    "team:backend",
    "env:production"
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Object describing a Datadog Log index.

| Parent field      | Field                                    | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------- | ---------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | daily_limit                              | int64    | The number of log events you can send in this index per day before you are rate-limited.                                                                                                                                                                                                                                                                                                                                                                                         |
|                   | daily_limit_reset                        | object   | Object containing options to override the default daily limit reset time.                                                                                                                                                                                                                                                                                                                                                                                                        |
| daily_limit_reset | reset_time                               | string   | String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).                                                                                                                                                                                                                                                                                                                                          |
| daily_limit_reset | reset_utc_offset                         | string   | String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).                                                                                                                                                                                                                                                                                                                                   |
|                   | daily_limit_warning_threshold_percentage | double   | A percentage threshold of the daily quota at which a Datadog warning event is generated.                                                                                                                                                                                                                                                                                                                                                                                         |
|                   | exclusion_filters                        | [object] | An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.                                                                                                                                                                                                                                                                            |
| exclusion_filters | filter                                   | object   | Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.                                                                                                                                                                                                                                                                                                                                                                                           |
| filter            | query                                    | string   | Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.                                                                                                                                                                                                                                                                                                                            |
| filter            | sample_rate [*required*]            | double   | Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.                                                                                                                                                                                                                                                                                                                                                           |
| exclusion_filters | is_enabled                               | boolean  | Whether or not the exclusion filter is active.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| exclusion_filters | name [*required*]                   | string   | Name of the index exclusion filter.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                   | filter [*required*]                 | object   | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| filter            | query                                    | string   | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                   | is_rate_limited                          | boolean  | A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. Rate limit is reset every-day at 2pm UTC.                                                                                                                                                                                                                                                                                                                                 |
|                   | name [*required*]                   | string   | The name of the index.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                   | num_flex_logs_retention_days             | int64    | The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions. |
|                   | num_retention_days                       | int64    | The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.                                                                                                                                                                                                                                                     |
|                   | tags                                     | [string] | A list of tags associated with the index. Tags must be in `key:value` format.                                                                                                                                                                                                                                                                                                                                                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "daily_limit": 300000000,
  "daily_limit_reset": {
    "reset_time": "14:00",
    "reset_utc_offset": "+02:00"
  },
  "daily_limit_warning_threshold_percentage": 70,
  "exclusion_filters": [
    {
      "filter": {
        "query": "*",
        "sample_rate": 1
      },
      "is_enabled": false,
      "name": "payment"
    }
  ],
  "filter": {
    "query": "source:python"
  },
  "is_rate_limited": false,
  "name": "main",
  "num_flex_logs_retention_days": 360,
  "num_retention_days": 15,
  "tags": [
    "team:backend",
    "env:production"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Invalid Parameter Error
{% tab title="Model" %}
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
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

{% tab title="422" %}
Unprocessable Entity
{% tab title="Model" %}
Response returned by the Logs API when the max limit has been reached.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/indexes" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "exclusion_filters": [
    {
      "filter": {
        "sample_rate": 1
      },
      "name": "payment"
    }
  ],
  "filter": {},
  "name": "main"
}
EOF

#####

```python
"""
Create an index returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi
from datadog_api_client.v1.model.logs_daily_limit_reset import LogsDailyLimitReset
from datadog_api_client.v1.model.logs_exclusion import LogsExclusion
from datadog_api_client.v1.model.logs_exclusion_filter import LogsExclusionFilter
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_index import LogsIndex

body = LogsIndex(
    daily_limit=300000000,
    daily_limit_reset=LogsDailyLimitReset(
        reset_time="14:00",
        reset_utc_offset="+02:00",
    ),
    daily_limit_warning_threshold_percentage=70.0,
    exclusion_filters=[
        LogsExclusion(
            filter=LogsExclusionFilter(
                query="*",
                sample_rate=1.0,
            ),
            name="payment",
        ),
    ],
    filter=LogsFilter(
        query="source:python",
    ),
    name="main",
    num_flex_logs_retention_days=360,
    num_retention_days=15,
    tags=[
        "team:backend",
        "env:production",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.create_logs_index(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create an index returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new

body = DatadogAPIClient::V1::LogsIndex.new({
  daily_limit: 300000000,
  daily_limit_reset: DatadogAPIClient::V1::LogsDailyLimitReset.new({
    reset_time: "14:00",
    reset_utc_offset: "+02:00",
  }),
  daily_limit_warning_threshold_percentage: 70,
  exclusion_filters: [
    DatadogAPIClient::V1::LogsExclusion.new({
      filter: DatadogAPIClient::V1::LogsExclusionFilter.new({
        query: "*",
        sample_rate: 1.0,
      }),
      name: "payment",
    }),
  ],
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  name: "main",
  num_flex_logs_retention_days: 360,
  num_retention_days: 15,
  tags: [
    "team:backend",
    "env:production",
  ],
})
p api_instance.create_logs_index(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Create an index returns "OK" response

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
    body := datadogV1.LogsIndex{
        DailyLimit: datadog.PtrInt64(300000000),
        DailyLimitReset: &datadogV1.LogsDailyLimitReset{
            ResetTime:      datadog.PtrString("14:00"),
            ResetUtcOffset: datadog.PtrString("+02:00"),
        },
        DailyLimitWarningThresholdPercentage: datadog.PtrFloat64(70),
        ExclusionFilters: []datadogV1.LogsExclusion{
            {
                Filter: &datadogV1.LogsExclusionFilter{
                    Query:      datadog.PtrString("*"),
                    SampleRate: 1.0,
                },
                Name: "payment",
            },
        },
        Filter: datadogV1.LogsFilter{
            Query: datadog.PtrString("source:python"),
        },
        Name:                     "main",
        NumFlexLogsRetentionDays: datadog.PtrInt64(360),
        NumRetentionDays:         datadog.PtrInt64(15),
        Tags: []string{
            "team:backend",
            "env:production",
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewLogsIndexesApi(apiClient)
    resp, r, err := api.CreateLogsIndex(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.CreateLogsIndex`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.CreateLogsIndex`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create an index returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsDailyLimitReset;
import com.datadog.api.client.v1.model.LogsExclusion;
import com.datadog.api.client.v1.model.LogsExclusionFilter;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsIndex;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    LogsIndex body =
        new LogsIndex()
            .dailyLimit(300000000L)
            .dailyLimitReset(new LogsDailyLimitReset().resetTime("14:00").resetUtcOffset("+02:00"))
            .dailyLimitWarningThresholdPercentage(70.0)
            .exclusionFilters(
                Collections.singletonList(
                    new LogsExclusion()
                        .filter(new LogsExclusionFilter().query("*").sampleRate(1.0))
                        .name("payment")))
            .filter(new LogsFilter().query("source:python"))
            .name("main")
            .numFlexLogsRetentionDays(360L)
            .numRetentionDays(15L)
            .tags(Arrays.asList("team:backend", "env:production"));

    try {
      LogsIndex result = apiInstance.createLogsIndex(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#createLogsIndex");
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
// Create an index returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;
use datadog_api_client::datadogV1::model::LogsDailyLimitReset;
use datadog_api_client::datadogV1::model::LogsExclusion;
use datadog_api_client::datadogV1::model::LogsExclusionFilter;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsIndex;

#[tokio::main]
async fn main() {
    let body = LogsIndex::new(
        LogsFilter::new().query("source:python".to_string()),
        "main".to_string(),
    )
    .daily_limit(300000000)
    .daily_limit_reset(
        LogsDailyLimitReset::new()
            .reset_time("14:00".to_string())
            .reset_utc_offset("+02:00".to_string()),
    )
    .daily_limit_warning_threshold_percentage(70.0 as f64)
    .exclusion_filters(vec![LogsExclusion::new("payment".to_string())
        .filter(LogsExclusionFilter::new(1.0).query("*".to_string()))])
    .num_flex_logs_retention_days(360)
    .num_retention_days(15)
    .tags(vec![
        "team:backend".to_string(),
        "env:production".to_string(),
    ]);
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.create_logs_index(body).await;
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
 * Create an index returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

const params: v1.LogsIndexesApiCreateLogsIndexRequest = {
  body: {
    dailyLimit: 300000000,
    dailyLimitReset: {
      resetTime: "14:00",
      resetUtcOffset: "+02:00",
    },
    dailyLimitWarningThresholdPercentage: 70,
    exclusionFilters: [
      {
        filter: {
          query: "*",
          sampleRate: 1.0,
        },
        name: "payment",
      },
    ],
    filter: {
      query: "source:python",
    },
    name: "main",
    numFlexLogsRetentionDays: 360,
    numRetentionDays: 15,
    tags: ["team:backend", "env:production"],
  },
};

apiInstance
  .createLogsIndex(params)
  .then((data: v1.LogsIndex) => {
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

## Update an index{% #update-an-index %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/logs/config/indexes/{name} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/logs/config/indexes/{name} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/logs/config/indexes/{name}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/logs/config/indexes/{name}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/logs/config/indexes/{name}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/logs/config/indexes/{name} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/logs/config/indexes/{name} |

### Overview



Update an index as identified by its name. Returns the Index object passed in the request body when the request is successful.

Using the `PUT` method updates your index's configuration by **replacing** your current configuration with the new one sent to your Datadog organization.



### Arguments

#### Path Parameters

| Name                   | Type   | Description            |
| ---------------------- | ------ | ---------------------- |
| name [*required*] | string | Name of the log index. |

### Request

#### Body Data (required)

Object containing the new `LogsIndexUpdateRequest`.

{% tab title="Model" %}

| Parent field      | Field                                    | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------- | ---------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | daily_limit                              | int64    | The number of log events you can send in this index per day before you are rate-limited.                                                                                                                                                                                                                                                                                                                                                                                         |
|                   | daily_limit_reset                        | object   | Object containing options to override the default daily limit reset time.                                                                                                                                                                                                                                                                                                                                                                                                        |
| daily_limit_reset | reset_time                               | string   | String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).                                                                                                                                                                                                                                                                                                                                          |
| daily_limit_reset | reset_utc_offset                         | string   | String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).                                                                                                                                                                                                                                                                                                                                   |
|                   | daily_limit_warning_threshold_percentage | double   | A percentage threshold of the daily quota at which a Datadog warning event is generated.                                                                                                                                                                                                                                                                                                                                                                                         |
|                   | disable_daily_limit                      | boolean  | If true, sets the `daily_limit` value to null and the index is not limited on a daily basis (any specified `daily_limit` value in the request is ignored). If false or omitted, the index's current `daily_limit` is maintained.                                                                                                                                                                                                                                                 |
|                   | exclusion_filters                        | [object] | An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.                                                                                                                                                                                                                                                                            |
| exclusion_filters | filter                                   | object   | Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.                                                                                                                                                                                                                                                                                                                                                                                           |
| filter            | query                                    | string   | Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.                                                                                                                                                                                                                                                                                                                            |
| filter            | sample_rate [*required*]            | double   | Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.                                                                                                                                                                                                                                                                                                                                                           |
| exclusion_filters | is_enabled                               | boolean  | Whether or not the exclusion filter is active.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| exclusion_filters | name [*required*]                   | string   | Name of the index exclusion filter.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                   | filter [*required*]                 | object   | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| filter            | query                                    | string   | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                   | num_flex_logs_retention_days             | int64    | The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions. | **Note**: Changing this value affects all logs already in this index. It may also affect billing. |
|                   | num_retention_days                       | int64    | The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.                                                                                                                                                                                                                                                     | **Note**: Changing this value affects all logs already in this index. It may also affect billing. |
|                   | tags                                     | [string] | A list of tags associated with the index. Tags must be in `key:value` format.                                                                                                                                                                                                                                                                                                                                                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "daily_limit": 300000000,
  "daily_limit_reset": {
    "reset_time": "14:00",
    "reset_utc_offset": "+02:00"
  },
  "daily_limit_warning_threshold_percentage": 70,
  "disable_daily_limit": false,
  "exclusion_filters": [
    {
      "filter": {
        "query": "*",
        "sample_rate": 1
      },
      "is_enabled": false,
      "name": "payment"
    }
  ],
  "filter": {
    "query": "source:python"
  },
  "num_flex_logs_retention_days": 360,
  "num_retention_days": 15,
  "tags": [
    "team:backend",
    "env:production"
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Object describing a Datadog Log index.

| Parent field      | Field                                    | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------- | ---------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                   | daily_limit                              | int64    | The number of log events you can send in this index per day before you are rate-limited.                                                                                                                                                                                                                                                                                                                                                                                         |
|                   | daily_limit_reset                        | object   | Object containing options to override the default daily limit reset time.                                                                                                                                                                                                                                                                                                                                                                                                        |
| daily_limit_reset | reset_time                               | string   | String in `HH:00` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).                                                                                                                                                                                                                                                                                                                                          |
| daily_limit_reset | reset_utc_offset                         | string   | String in `(-|+)HH:00` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).                                                                                                                                                                                                                                                                                                                                   |
|                   | daily_limit_warning_threshold_percentage | double   | A percentage threshold of the daily quota at which a Datadog warning event is generated.                                                                                                                                                                                                                                                                                                                                                                                         |
|                   | exclusion_filters                        | [object] | An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored.                                                                                                                                                                                                                                                                            |
| exclusion_filters | filter                                   | object   | Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.                                                                                                                                                                                                                                                                                                                                                                                           |
| filter            | query                                    | string   | Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.                                                                                                                                                                                                                                                                                                                            |
| filter            | sample_rate [*required*]            | double   | Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.                                                                                                                                                                                                                                                                                                                                                           |
| exclusion_filters | is_enabled                               | boolean  | Whether or not the exclusion filter is active.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| exclusion_filters | name [*required*]                   | string   | Name of the index exclusion filter.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                   | filter [*required*]                 | object   | Filter for logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| filter            | query                                    | string   | The filter query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                   | is_rate_limited                          | boolean  | A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. Rate limit is reset every-day at 2pm UTC.                                                                                                                                                                                                                                                                                                                                 |
|                   | name [*required*]                   | string   | The name of the index.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                   | num_flex_logs_retention_days             | int64    | The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through `num_retention_days`, and then stored in Flex Tier until the number of days specified in `num_flex_logs_retention_days` is reached. The available values depend on retention plans specified in your organization's contract/subscriptions. |
|                   | num_retention_days                       | int64    | The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. The available values depend on retention plans specified in your organization's contract/subscriptions.                                                                                                                                                                                                                                                     |
|                   | tags                                     | [string] | A list of tags associated with the index. Tags must be in `key:value` format.                                                                                                                                                                                                                                                                                                                                                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "daily_limit": 300000000,
  "daily_limit_reset": {
    "reset_time": "14:00",
    "reset_utc_offset": "+02:00"
  },
  "daily_limit_warning_threshold_percentage": 70,
  "exclusion_filters": [
    {
      "filter": {
        "query": "*",
        "sample_rate": 1
      },
      "is_enabled": false,
      "name": "payment"
    }
  ],
  "filter": {
    "query": "source:python"
  },
  "is_rate_limited": false,
  "name": "main",
  "num_flex_logs_retention_days": 360,
  "num_retention_days": 15,
  "tags": [
    "team:backend",
    "env:production"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Invalid Parameter Error
{% tab title="Model" %}
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
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

{% tab title="429" %}
Too Many Requests
{% tab title="Model" %}
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport name="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/indexes/${name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "exclusion_filters": [
    {
      "filter": {
        "sample_rate": 1
      },
      "name": "payment"
    }
  ],
  "filter": {}
}
EOF

#####

```python
"""
Update an index returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi
from datadog_api_client.v1.model.logs_daily_limit_reset import LogsDailyLimitReset
from datadog_api_client.v1.model.logs_exclusion import LogsExclusion
from datadog_api_client.v1.model.logs_exclusion_filter import LogsExclusionFilter
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_index_update_request import LogsIndexUpdateRequest

body = LogsIndexUpdateRequest(
    daily_limit=300000000,
    daily_limit_reset=LogsDailyLimitReset(
        reset_time="14:00",
        reset_utc_offset="+02:00",
    ),
    daily_limit_warning_threshold_percentage=70.0,
    disable_daily_limit=False,
    exclusion_filters=[
        LogsExclusion(
            filter=LogsExclusionFilter(
                query="*",
                sample_rate=1.0,
            ),
            name="payment",
        ),
    ],
    filter=LogsFilter(
        query="source:python",
    ),
    num_flex_logs_retention_days=360,
    num_retention_days=15,
    tags=[
        "team:backend",
        "env:production",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.update_logs_index(name="name", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update an index returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new

body = DatadogAPIClient::V1::LogsIndexUpdateRequest.new({
  daily_limit: 300000000,
  daily_limit_reset: DatadogAPIClient::V1::LogsDailyLimitReset.new({
    reset_time: "14:00",
    reset_utc_offset: "+02:00",
  }),
  daily_limit_warning_threshold_percentage: 70,
  disable_daily_limit: false,
  exclusion_filters: [
    DatadogAPIClient::V1::LogsExclusion.new({
      filter: DatadogAPIClient::V1::LogsExclusionFilter.new({
        query: "*",
        sample_rate: 1.0,
      }),
      name: "payment",
    }),
  ],
  filter: DatadogAPIClient::V1::LogsFilter.new({
    query: "source:python",
  }),
  num_flex_logs_retention_days: 360,
  num_retention_days: 15,
  tags: [
    "team:backend",
    "env:production",
  ],
})
p api_instance.update_logs_index("name", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Update an index returns "OK" response

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
    body := datadogV1.LogsIndexUpdateRequest{
        DailyLimit: datadog.PtrInt64(300000000),
        DailyLimitReset: &datadogV1.LogsDailyLimitReset{
            ResetTime:      datadog.PtrString("14:00"),
            ResetUtcOffset: datadog.PtrString("+02:00"),
        },
        DailyLimitWarningThresholdPercentage: datadog.PtrFloat64(70),
        DisableDailyLimit:                    datadog.PtrBool(false),
        ExclusionFilters: []datadogV1.LogsExclusion{
            {
                Filter: &datadogV1.LogsExclusionFilter{
                    Query:      datadog.PtrString("*"),
                    SampleRate: 1.0,
                },
                Name: "payment",
            },
        },
        Filter: datadogV1.LogsFilter{
            Query: datadog.PtrString("source:python"),
        },
        NumFlexLogsRetentionDays: datadog.PtrInt64(360),
        NumRetentionDays:         datadog.PtrInt64(15),
        Tags: []string{
            "team:backend",
            "env:production",
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewLogsIndexesApi(apiClient)
    resp, r, err := api.UpdateLogsIndex(ctx, "name", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.UpdateLogsIndex`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.UpdateLogsIndex`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update an index returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsDailyLimitReset;
import com.datadog.api.client.v1.model.LogsExclusion;
import com.datadog.api.client.v1.model.LogsExclusionFilter;
import com.datadog.api.client.v1.model.LogsFilter;
import com.datadog.api.client.v1.model.LogsIndex;
import com.datadog.api.client.v1.model.LogsIndexUpdateRequest;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    LogsIndexUpdateRequest body =
        new LogsIndexUpdateRequest()
            .dailyLimit(300000000L)
            .dailyLimitReset(new LogsDailyLimitReset().resetTime("14:00").resetUtcOffset("+02:00"))
            .dailyLimitWarningThresholdPercentage(70.0)
            .disableDailyLimit(false)
            .exclusionFilters(
                Collections.singletonList(
                    new LogsExclusion()
                        .filter(new LogsExclusionFilter().query("*").sampleRate(1.0))
                        .name("payment")))
            .filter(new LogsFilter().query("source:python"))
            .numFlexLogsRetentionDays(360L)
            .numRetentionDays(15L)
            .tags(Arrays.asList("team:backend", "env:production"));

    try {
      LogsIndex result = apiInstance.updateLogsIndex("name", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#updateLogsIndex");
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
// Update an index returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;
use datadog_api_client::datadogV1::model::LogsDailyLimitReset;
use datadog_api_client::datadogV1::model::LogsExclusion;
use datadog_api_client::datadogV1::model::LogsExclusionFilter;
use datadog_api_client::datadogV1::model::LogsFilter;
use datadog_api_client::datadogV1::model::LogsIndexUpdateRequest;

#[tokio::main]
async fn main() {
    let body = LogsIndexUpdateRequest::new(LogsFilter::new().query("source:python".to_string()))
        .daily_limit(300000000)
        .daily_limit_reset(
            LogsDailyLimitReset::new()
                .reset_time("14:00".to_string())
                .reset_utc_offset("+02:00".to_string()),
        )
        .daily_limit_warning_threshold_percentage(70.0 as f64)
        .disable_daily_limit(false)
        .exclusion_filters(vec![LogsExclusion::new("payment".to_string())
            .filter(LogsExclusionFilter::new(1.0).query("*".to_string()))])
        .num_flex_logs_retention_days(360)
        .num_retention_days(15)
        .tags(vec![
            "team:backend".to_string(),
            "env:production".to_string(),
        ]);
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.update_logs_index("name".to_string(), body).await;
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
 * Update an index returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

const params: v1.LogsIndexesApiUpdateLogsIndexRequest = {
  body: {
    dailyLimit: 300000000,
    dailyLimitReset: {
      resetTime: "14:00",
      resetUtcOffset: "+02:00",
    },
    dailyLimitWarningThresholdPercentage: 70,
    disableDailyLimit: false,
    exclusionFilters: [
      {
        filter: {
          query: "*",
          sampleRate: 1.0,
        },
        name: "payment",
      },
    ],
    filter: {
      query: "source:python",
    },
    numFlexLogsRetentionDays: 360,
    numRetentionDays: 15,
    tags: ["team:backend", "env:production"],
  },
  name: "name",
};

apiInstance
  .updateLogsIndex(params)
  .then((data: v1.LogsIndex) => {
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

## Delete an index{% #delete-an-index %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/logs/config/indexes/{name} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/logs/config/indexes/{name} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/logs/config/indexes/{name}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/logs/config/indexes/{name}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/logs/config/indexes/{name}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/logs/config/indexes/{name} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/logs/config/indexes/{name} |

### Overview

Delete an existing index from your organization. Index deletions are permanent and cannot be reverted. You cannot recreate an index with the same name as deleted ones. This endpoint requires the `logs_modify_indexes` permission.

### Arguments

#### Path Parameters

| Name                   | Type   | Description            |
| ---------------------- | ------ | ---------------------- |
| name [*required*] | string | Name of the log index. |

### Response

{% tab title="200" %}
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
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
  }
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
                  \# Path parametersexport name="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/indexes/${name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete an index returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    api_instance.delete_logs_index(
        name="name",
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete an index returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new
p api_instance.delete_logs_index("name")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete an index returns "OK" response

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
    api := datadogV1.NewLogsIndexesApi(apiClient)
    r, err := api.DeleteLogsIndex(ctx, "name")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.DeleteLogsIndex`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete an index returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    try {
      apiInstance.deleteLogsIndex("name");
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#deleteLogsIndex");
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
// Delete an index returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.delete_logs_index("name".to_string()).await;
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
 * Delete an index returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

const params: v1.LogsIndexesApiDeleteLogsIndexRequest = {
  name: "name",
};

apiInstance
  .deleteLogsIndex(params)
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

## Get indexes order{% #get-indexes-order %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/logs/config/index-order |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/logs/config/index-order |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/logs/config/index-order      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/logs/config/index-order      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/logs/config/index-order     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/logs/config/index-order |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/logs/config/index-order |

### Overview

Get the current order of your log indexes. This endpoint takes no JSON arguments. This endpoint requires the `logs_read_config` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Object containing the ordered list of log index names.

| Field                         | Type     | Description                                                                                                                                                                                                                                    |
| ----------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| index_names [*required*] | [string] | Array of strings identifying by their name(s) the index(es) of your organization. Logs are tested against the query filter of each index one by one, following the order of the array. Logs are eventually stored in the first matching index. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "index_names": [
    "main",
    "payments",
    "web"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/index-order" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get indexes order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.get_logs_index_order()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get indexes order returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new
p api_instance.get_logs_index_order()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get indexes order returns "OK" response

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
    api := datadogV1.NewLogsIndexesApi(apiClient)
    resp, r, err := api.GetLogsIndexOrder(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.GetLogsIndexOrder`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.GetLogsIndexOrder`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get indexes order returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsIndexesOrder;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    try {
      LogsIndexesOrder result = apiInstance.getLogsIndexOrder();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#getLogsIndexOrder");
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
// Get indexes order returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.get_logs_index_order().await;
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
 * Get indexes order returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

apiInstance
  .getLogsIndexOrder()
  .then((data: v1.LogsIndexesOrder) => {
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

## Update indexes order{% #update-indexes-order %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/logs/config/index-order |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/logs/config/index-order |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/logs/config/index-order      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/logs/config/index-order      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/logs/config/index-order     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/logs/config/index-order |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/logs/config/index-order |

### Overview

This endpoint updates the index order of your organization. It returns the index order object passed in the request body when the request is successful. This endpoint requires the `logs_modify_indexes` permission.

### Request

#### Body Data (required)

Object containing the new ordered list of index names

{% tab title="Model" %}

| Field                         | Type     | Description                                                                                                                                                                                                                                    |
| ----------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| index_names [*required*] | [string] | Array of strings identifying by their name(s) the index(es) of your organization. Logs are tested against the query filter of each index one by one, following the order of the array. Logs are eventually stored in the first matching index. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "index_names": [
    "main",
    "payments",
    "web"
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Object containing the ordered list of log index names.

| Field                         | Type     | Description                                                                                                                                                                                                                                    |
| ----------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| index_names [*required*] | [string] | Array of strings identifying by their name(s) the index(es) of your organization. Logs are tested against the query filter of each index one by one, following the order of the array. Logs are eventually stored in the first matching index. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "index_names": [
    "main",
    "payments",
    "web"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Response returned by the Logs API when errors occur.

| Parent field | Field   | Type     | Description                    |
| ------------ | ------- | -------- | ------------------------------ |
|              | error   | object   | Error returned by the Logs API |
| error        | code    | string   | Code identifying the error     |
| error        | details | [object] | Additional error details       |
| error        | message | string   | Error message                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "error": {
    "code": "string",
    "details": [],
    "message": "string"
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
                  \# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/logs/config/index-order" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "index_names": [
    "main",
    "payments",
    "web"
  ]
}
EOF

#####

```python
"""
Update indexes order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi
from datadog_api_client.v1.model.logs_indexes_order import LogsIndexesOrder

body = LogsIndexesOrder(
    index_names=[
        "main",
        "payments",
        "web",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.update_logs_index_order(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update indexes order returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::LogsIndexesAPI.new

body = DatadogAPIClient::V1::LogsIndexesOrder.new({
  index_names: [
    "main",
    "payments",
    "web",
  ],
})
p api_instance.update_logs_index_order(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Update indexes order returns "OK" response

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
    body := datadogV1.LogsIndexesOrder{
        IndexNames: []string{
            "main",
            "payments",
            "web",
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewLogsIndexesApi(apiClient)
    resp, r, err := api.UpdateLogsIndexOrder(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsIndexesApi.UpdateLogsIndexOrder`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsIndexesApi.UpdateLogsIndexOrder`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update indexes order returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.LogsIndexesApi;
import com.datadog.api.client.v1.model.LogsIndexesOrder;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    LogsIndexesApi apiInstance = new LogsIndexesApi(defaultClient);

    LogsIndexesOrder body =
        new LogsIndexesOrder().indexNames(Arrays.asList("main", "payments", "web"));

    try {
      LogsIndexesOrder result = apiInstance.updateLogsIndexOrder(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsIndexesApi#updateLogsIndexOrder");
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
// Update indexes order returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_logs_indexes::LogsIndexesAPI;
use datadog_api_client::datadogV1::model::LogsIndexesOrder;

#[tokio::main]
async fn main() {
    let body = LogsIndexesOrder::new(vec![
        "main".to_string(),
        "payments".to_string(),
        "web".to_string(),
    ]);
    let configuration = datadog::Configuration::new();
    let api = LogsIndexesAPI::with_config(configuration);
    let resp = api.update_logs_index_order(body).await;
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
 * Update indexes order returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.LogsIndexesApi(configuration);

const params: v1.LogsIndexesApiUpdateLogsIndexOrderRequest = {
  body: {
    indexNames: ["main", "payments", "web"],
  },
};

apiInstance
  .updateLogsIndexOrder(params)
  .then((data: v1.LogsIndexesOrder) => {
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
