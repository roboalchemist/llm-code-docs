# Source: https://docs.datadoghq.com/api/latest/logs-restriction-queries.md

---
title: Logs Restriction Queries
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Logs Restriction Queries
---

# Logs Restriction Queries

**Note: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).**

A Restriction Query is a logs query that restricts which logs the `logs_read_data` permission grants read access to. For users whose roles have Restriction Queries, any log query they make only returns those log events that also match one of their Restriction Queries. This is true whether the user queries log events from any log-related feature, including the log explorer, Live Tail, re-hydration, or a dashboard widget.

Restriction Queries currently only support use of the following components of log events:

- Reserved attributes
- The log message
- Tags

To restrict read access on log data, add a team tag to log events to indicate which teams own them, and then scope Restriction Queries to the relevant values of the team tag. Tags can be applied to log events in many ways, and a log event can have multiple tags with the same key (like team) and different values. This means the same log event can be visible to roles whose restriction queries are scoped to different team values.

See [How to Set Up RBAC for Logs](https://docs.datadoghq.com/logs/guide/logs-rbac/?tab=api#restrict-access-to-logs) for details on how to add restriction queries.

## List restriction queries{% #list-restriction-queries %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/restriction_queries      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/restriction_queries      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/restriction_queries     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries |

### Overview

Returns all restriction queries, including their names and IDs. This endpoint requires the `logs_read_config` permission.

### Arguments

#### Query Strings

| Name         | Type    | Description                                              |
| ------------ | ------- | -------------------------------------------------------- |
| page[size]   | integer | Size for a given page. The maximum allowed value is 100. |
| page[number] | integer | Specific page number to return.                          |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about multiple restriction queries.

| Parent field | Field               | Type      | Description                                                                                  |
| ------------ | ------------------- | --------- | -------------------------------------------------------------------------------------------- |
|              | data                | [object]  | Array of returned restriction queries.                                                       |
| data         | attributes          | object    | Attributes of the restriction query.                                                         |
| attributes   | created_at          | date-time | Creation time of the restriction query.                                                      |
| attributes   | last_modifier_email | string    | Email of the user who last modified this restriction query.                                  |
| attributes   | last_modifier_name  | string    | Name of the user who last modified this restriction query.                                   |
| attributes   | modified_at         | date-time | Time of last restriction query modification.                                                 |
| attributes   | restriction_query   | string    | The query that defines the restriction. Only the content matching the query can be returned. |
| attributes   | role_count          | int64     | Number of roles associated with this restriction query.                                      |
| attributes   | user_count          | int64     | Number of users associated with this restriction query.                                      |
| data         | id                  | string    | ID of the restriction query.                                                                 |
| data         | type                | string    | Restriction queries type.                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_at": "2020-03-17T21:06:44.000Z",
        "last_modifier_email": "user@example.com",
        "last_modifier_name": "John Doe",
        "modified_at": "2020-03-17T21:15:15.000Z",
        "restriction_query": "env:sandbox",
        "role_count": 3,
        "user_count": 5
      },
      "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
      "type": "logs_restriction_queries"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication error
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List restriction queries returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

configuration = Configuration()
configuration.unstable_operations["list_restriction_queries"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.list_restriction_queries()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List restriction queries returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_restriction_queries".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new
p api_instance.list_restriction_queries()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List restriction queries returns "OK" response

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
    configuration.SetUnstableOperationEnabled("v2.ListRestrictionQueries", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
    resp, r, err := api.ListRestrictionQueries(ctx, *datadogV2.NewListRestrictionQueriesOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.ListRestrictionQueries`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.ListRestrictionQueries`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List restriction queries returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RestrictionQueryListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listRestrictionQueries", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    try {
      RestrictionQueryListResponse result = apiInstance.listRestrictionQueries();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsRestrictionQueriesApi#listRestrictionQueries");
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
// List restriction queries returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::ListRestrictionQueriesOptionalParams;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListRestrictionQueries", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .list_restriction_queries(ListRestrictionQueriesOptionalParams::default())
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
 * List restriction queries returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listRestrictionQueries"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

apiInstance
  .listRestrictionQueries()
  .then((data: v2.RestrictionQueryListResponse) => {
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

## Create a restriction query{% #create-a-restriction-query %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/logs/config/restriction_queries      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/logs/config/restriction_queries      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/logs/config/restriction_queries     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries |

### Overview

Create a new restriction query for your organization. This endpoint requires the `user_access_manage` permission.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                               | Type   | Description                                                                      |
| ------------ | ----------------------------------- | ------ | -------------------------------------------------------------------------------- |
|              | data                                | object | Data related to the creation of a restriction query.                             |
| data         | attributes                          | object | Attributes of the created restriction query.                                     |
| attributes   | restriction_query [*required*] | string | The restriction query.                                                           |
| data         | type                                | enum   | Restriction query resource type. Allowed enum values: `logs_restriction_queries` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    },
    "type": "logs_restriction_queries"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about a single restriction query.

| Parent field | Field               | Type      | Description                                                                                  |
| ------------ | ------------------- | --------- | -------------------------------------------------------------------------------------------- |
|              | data                | object    | Restriction query object returned by the API.                                                |
| data         | attributes          | object    | Attributes of the restriction query.                                                         |
| attributes   | created_at          | date-time | Creation time of the restriction query.                                                      |
| attributes   | last_modifier_email | string    | Email of the user who last modified this restriction query.                                  |
| attributes   | last_modifier_name  | string    | Name of the user who last modified this restriction query.                                   |
| attributes   | modified_at         | date-time | Time of last restriction query modification.                                                 |
| attributes   | restriction_query   | string    | The query that defines the restriction. Only the content matching the query can be returned. |
| attributes   | role_count          | int64     | Number of roles associated with this restriction query.                                      |
| attributes   | user_count          | int64     | Number of users associated with this restriction query.                                      |
| data         | id                  | string    | ID of the restriction query.                                                                 |
| data         | type                | string    | Restriction queries type.                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2020-03-17T21:06:44.000Z",
      "last_modifier_email": "user@example.com",
      "last_modifier_name": "John Doe",
      "modified_at": "2020-03-17T21:15:15.000Z",
      "restriction_query": "env:sandbox",
      "role_count": 3,
      "user_count": 5
    },
    "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
    "type": "logs_restriction_queries"
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
Authentication error
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    },
    "type": "logs_restriction_queries"
  }
}
EOF

#####

```go
// Create a restriction query returns "OK" response

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
    body := datadogV2.RestrictionQueryCreatePayload{
        Data: &datadogV2.RestrictionQueryCreateData{
            Attributes: &datadogV2.RestrictionQueryCreateAttributes{
                RestrictionQuery: "env:sandbox",
            },
            Type: datadogV2.LOGSRESTRICTIONQUERIESTYPE_LOGS_RESTRICTION_QUERIES.Ptr(),
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.CreateRestrictionQuery", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
    resp, r, err := api.CreateRestrictionQuery(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.CreateRestrictionQuery`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.CreateRestrictionQuery`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.LogsRestrictionQueriesType;
import com.datadog.api.client.v2.model.RestrictionQueryCreateAttributes;
import com.datadog.api.client.v2.model.RestrictionQueryCreateData;
import com.datadog.api.client.v2.model.RestrictionQueryCreatePayload;
import com.datadog.api.client.v2.model.RestrictionQueryWithoutRelationshipsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    RestrictionQueryCreatePayload body =
        new RestrictionQueryCreatePayload()
            .data(
                new RestrictionQueryCreateData()
                    .attributes(
                        new RestrictionQueryCreateAttributes().restrictionQuery("env:sandbox"))
                    .type(LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES));

    try {
      RestrictionQueryWithoutRelationshipsResponse result =
          apiInstance.createRestrictionQuery(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsRestrictionQueriesApi#createRestrictionQuery");
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

```python
"""
Create a restriction query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType
from datadog_api_client.v2.model.restriction_query_create_attributes import RestrictionQueryCreateAttributes
from datadog_api_client.v2.model.restriction_query_create_data import RestrictionQueryCreateData
from datadog_api_client.v2.model.restriction_query_create_payload import RestrictionQueryCreatePayload

body = RestrictionQueryCreatePayload(
    data=RestrictionQueryCreateData(
        attributes=RestrictionQueryCreateAttributes(
            restriction_query="env:sandbox",
        ),
        type=LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.create_restriction_query(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

body = DatadogAPIClient::V2::RestrictionQueryCreatePayload.new({
  data: DatadogAPIClient::V2::RestrictionQueryCreateData.new({
    attributes: DatadogAPIClient::V2::RestrictionQueryCreateAttributes.new({
      restriction_query: "env:sandbox",
    }),
    type: DatadogAPIClient::V2::LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES,
  }),
})
p api_instance.create_restriction_query(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Create a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;
use datadog_api_client::datadogV2::model::LogsRestrictionQueriesType;
use datadog_api_client::datadogV2::model::RestrictionQueryCreateAttributes;
use datadog_api_client::datadogV2::model::RestrictionQueryCreateData;
use datadog_api_client::datadogV2::model::RestrictionQueryCreatePayload;

#[tokio::main]
async fn main() {
    let body = RestrictionQueryCreatePayload::new().data(
        RestrictionQueryCreateData::new()
            .attributes(RestrictionQueryCreateAttributes::new(
                "env:sandbox".to_string(),
            ))
            .type_(LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api.create_restriction_query(body).await;
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
 * Create a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

const params: v2.LogsRestrictionQueriesApiCreateRestrictionQueryRequest = {
  body: {
    data: {
      attributes: {
        restrictionQuery: "env:sandbox",
      },
      type: "logs_restriction_queries",
    },
  },
};

apiInstance
  .createRestrictionQuery(params)
  .then((data: v2.RestrictionQueryWithoutRelationshipsResponse) => {
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

## Get a restriction query{% #get-a-restriction-query %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |

### Overview

Get a restriction query in the organization specified by the restriction query's `restriction_query_id`. This endpoint requires the `logs_read_config` permission.

### Arguments

#### Path Parameters

| Name                                   | Type   | Description                      |
| -------------------------------------- | ------ | -------------------------------- |
| restriction_query_id [*required*] | string | The ID of the restriction query. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about a single restriction query.

| Parent field  | Field                        | Type            | Description                                                                                  |
| ------------- | ---------------------------- | --------------- | -------------------------------------------------------------------------------------------- |
|               | data                         | object          | Restriction query object returned by the API.                                                |
| data          | attributes                   | object          | Attributes of the restriction query.                                                         |
| attributes    | created_at                   | date-time       | Creation time of the restriction query.                                                      |
| attributes    | last_modifier_email          | string          | Email of the user who last modified this restriction query.                                  |
| attributes    | last_modifier_name           | string          | Name of the user who last modified this restriction query.                                   |
| attributes    | modified_at                  | date-time       | Time of last restriction query modification.                                                 |
| attributes    | restriction_query            | string          | The query that defines the restriction. Only the content matching the query can be returned. |
| attributes    | role_count                   | int64           | Number of roles associated with this restriction query.                                      |
| attributes    | user_count                   | int64           | Number of users associated with this restriction query.                                      |
| data          | id                           | string          | ID of the restriction query.                                                                 |
| data          | relationships                | object          | Relationships of the user object.                                                            |
| relationships | roles                        | object          | Relationship to roles.                                                                       |
| roles         | data                         | [object]        | An array containing type and the unique identifier of a role.                                |
| data          | id                           | string          | The unique identifier of the role.                                                           |
| data          | type                         | enum            | Roles type. Allowed enum values: `roles`                                                     |
| data          | type                         | enum            | Restriction query resource type. Allowed enum values: `logs_restriction_queries`             |
|               | included                     | [ <oneOf>] | Array of objects related to the restriction query.                                           |
| included      | Option 1                     | object          | Partial role object.                                                                         |
| Option 1      | attributes [*required*] | object          | Attributes of the role for a restriction query.                                              |
| attributes    | name                         | string          | The role name.                                                                               |
| Option 1      | id [*required*]         | string          | ID of the role.                                                                              |
| Option 1      | type [*required*]       | enum            | Roles type. Allowed enum values: `roles`                                                     |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2020-03-17T21:06:44.000Z",
      "last_modifier_email": "user@example.com",
      "last_modifier_name": "John Doe",
      "modified_at": "2020-03-17T21:15:15.000Z",
      "restriction_query": "env:sandbox",
      "role_count": 3,
      "user_count": 5
    },
    "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
    "relationships": {
      "roles": {
        "data": [
          {
            "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
            "type": "roles"
          }
        ]
      }
    },
    "type": "logs_restriction_queries"
  },
  "included": [
    {
      "attributes": {
        "name": "Datadog Admin Role"
      },
      "id": "<ROLE_ID>",
      "type": "roles"
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
Authentication error
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
Not found
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
                  \# Path parametersexport restriction_query_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.get_restriction_query(
        restriction_query_id=RESTRICTION_QUERY_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]
p api_instance.get_restriction_query(RESTRICTION_QUERY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a restriction query returns "OK" response

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
    // there is a valid "restriction_query" in the system
    RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.GetRestrictionQuery", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
    resp, r, err := api.GetRestrictionQuery(ctx, RestrictionQueryDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.GetRestrictionQuery`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.GetRestrictionQuery`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RestrictionQueryWithRelationshipsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    try {
      RestrictionQueryWithRelationshipsResponse result =
          apiInstance.getRestrictionQuery(RESTRICTION_QUERY_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsRestrictionQueriesApi#getRestrictionQuery");
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
// Get a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .get_restriction_query(restriction_query_data_id.clone())
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
 * Get a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiGetRestrictionQueryRequest = {
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .getRestrictionQuery(params)
  .then((data: v2.RestrictionQueryWithRelationshipsResponse) => {
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

## Replace a restriction query{% #replace-a-restriction-query %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |

### Overview

Replace a restriction query. This endpoint requires the `user_access_manage` permission.

### Arguments

#### Path Parameters

| Name                                   | Type   | Description                      |
| -------------------------------------- | ------ | -------------------------------- |
| restriction_query_id [*required*] | string | The ID of the restriction query. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                               | Type   | Description                                                                      |
| ------------ | ----------------------------------- | ------ | -------------------------------------------------------------------------------- |
|              | data                                | object | Data related to the update of a restriction query.                               |
| data         | attributes                          | object | Attributes of the edited restriction query.                                      |
| attributes   | restriction_query [*required*] | string | The restriction query.                                                           |
| data         | type                                | enum   | Restriction query resource type. Allowed enum values: `logs_restriction_queries` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    },
    "type": "logs_restriction_queries"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about a single restriction query.

| Parent field | Field               | Type      | Description                                                                                  |
| ------------ | ------------------- | --------- | -------------------------------------------------------------------------------------------- |
|              | data                | object    | Restriction query object returned by the API.                                                |
| data         | attributes          | object    | Attributes of the restriction query.                                                         |
| attributes   | created_at          | date-time | Creation time of the restriction query.                                                      |
| attributes   | last_modifier_email | string    | Email of the user who last modified this restriction query.                                  |
| attributes   | last_modifier_name  | string    | Name of the user who last modified this restriction query.                                   |
| attributes   | modified_at         | date-time | Time of last restriction query modification.                                                 |
| attributes   | restriction_query   | string    | The query that defines the restriction. Only the content matching the query can be returned. |
| attributes   | role_count          | int64     | Number of roles associated with this restriction query.                                      |
| attributes   | user_count          | int64     | Number of users associated with this restriction query.                                      |
| data         | id                  | string    | ID of the restriction query.                                                                 |
| data         | type                | string    | Restriction queries type.                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2020-03-17T21:06:44.000Z",
      "last_modifier_email": "user@example.com",
      "last_modifier_name": "John Doe",
      "modified_at": "2020-03-17T21:15:15.000Z",
      "restriction_query": "env:sandbox",
      "role_count": 3,
      "user_count": 5
    },
    "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
    "type": "logs_restriction_queries"
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
Authentication error
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
Not found
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
                  \# Path parametersexport restriction_query_id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    }
  }
}
EOF

#####

```python
"""
Replace a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType
from datadog_api_client.v2.model.restriction_query_update_attributes import RestrictionQueryUpdateAttributes
from datadog_api_client.v2.model.restriction_query_update_data import RestrictionQueryUpdateData
from datadog_api_client.v2.model.restriction_query_update_payload import RestrictionQueryUpdatePayload

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

body = RestrictionQueryUpdatePayload(
    data=RestrictionQueryUpdateData(
        attributes=RestrictionQueryUpdateAttributes(
            restriction_query="env:staging",
        ),
        type=LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["replace_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.replace_restriction_query(restriction_query_id=RESTRICTION_QUERY_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Replace a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.replace_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]

body = DatadogAPIClient::V2::RestrictionQueryUpdatePayload.new({
  data: DatadogAPIClient::V2::RestrictionQueryUpdateData.new({
    attributes: DatadogAPIClient::V2::RestrictionQueryUpdateAttributes.new({
      restriction_query: "env:staging",
    }),
    type: DatadogAPIClient::V2::LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES,
  }),
})
p api_instance.replace_restriction_query(RESTRICTION_QUERY_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Replace a restriction query returns "OK" response

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
    // there is a valid "restriction_query" in the system
    RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

    body := datadogV2.RestrictionQueryUpdatePayload{
        Data: &datadogV2.RestrictionQueryUpdateData{
            Attributes: &datadogV2.RestrictionQueryUpdateAttributes{
                RestrictionQuery: "env:staging",
            },
            Type: datadogV2.LOGSRESTRICTIONQUERIESTYPE_LOGS_RESTRICTION_QUERIES.Ptr(),
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.ReplaceRestrictionQuery", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
    resp, r, err := api.ReplaceRestrictionQuery(ctx, RestrictionQueryDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.ReplaceRestrictionQuery`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.ReplaceRestrictionQuery`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Replace a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.LogsRestrictionQueriesType;
import com.datadog.api.client.v2.model.RestrictionQueryUpdateAttributes;
import com.datadog.api.client.v2.model.RestrictionQueryUpdateData;
import com.datadog.api.client.v2.model.RestrictionQueryUpdatePayload;
import com.datadog.api.client.v2.model.RestrictionQueryWithoutRelationshipsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.replaceRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    RestrictionQueryUpdatePayload body =
        new RestrictionQueryUpdatePayload()
            .data(
                new RestrictionQueryUpdateData()
                    .attributes(
                        new RestrictionQueryUpdateAttributes().restrictionQuery("env:staging"))
                    .type(LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES));

    try {
      RestrictionQueryWithoutRelationshipsResponse result =
          apiInstance.replaceRestrictionQuery(RESTRICTION_QUERY_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#replaceRestrictionQuery");
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
// Replace a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;
use datadog_api_client::datadogV2::model::LogsRestrictionQueriesType;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdateAttributes;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdateData;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdatePayload;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();
    let body = RestrictionQueryUpdatePayload::new().data(
        RestrictionQueryUpdateData::new()
            .attributes(RestrictionQueryUpdateAttributes::new(
                "env:staging".to_string(),
            ))
            .type_(LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ReplaceRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .replace_restriction_query(restriction_query_data_id.clone(), body)
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
 * Replace a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.replaceRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiReplaceRestrictionQueryRequest = {
  body: {
    data: {
      attributes: {
        restrictionQuery: "env:staging",
      },
      type: "logs_restriction_queries",
    },
  },
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .replaceRestrictionQuery(params)
  .then((data: v2.RestrictionQueryWithoutRelationshipsResponse) => {
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

## Update a restriction query{% #update-a-restriction-query %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |

### Overview

Edit a restriction query. This endpoint requires the `user_access_manage` permission.

### Arguments

#### Path Parameters

| Name                                   | Type   | Description                      |
| -------------------------------------- | ------ | -------------------------------- |
| restriction_query_id [*required*] | string | The ID of the restriction query. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                               | Type   | Description                                                                      |
| ------------ | ----------------------------------- | ------ | -------------------------------------------------------------------------------- |
|              | data                                | object | Data related to the update of a restriction query.                               |
| data         | attributes                          | object | Attributes of the edited restriction query.                                      |
| attributes   | restriction_query [*required*] | string | The restriction query.                                                           |
| data         | type                                | enum   | Restriction query resource type. Allowed enum values: `logs_restriction_queries` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    },
    "type": "logs_restriction_queries"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about a single restriction query.

| Parent field | Field               | Type      | Description                                                                                  |
| ------------ | ------------------- | --------- | -------------------------------------------------------------------------------------------- |
|              | data                | object    | Restriction query object returned by the API.                                                |
| data         | attributes          | object    | Attributes of the restriction query.                                                         |
| attributes   | created_at          | date-time | Creation time of the restriction query.                                                      |
| attributes   | last_modifier_email | string    | Email of the user who last modified this restriction query.                                  |
| attributes   | last_modifier_name  | string    | Name of the user who last modified this restriction query.                                   |
| attributes   | modified_at         | date-time | Time of last restriction query modification.                                                 |
| attributes   | restriction_query   | string    | The query that defines the restriction. Only the content matching the query can be returned. |
| attributes   | role_count          | int64     | Number of roles associated with this restriction query.                                      |
| attributes   | user_count          | int64     | Number of users associated with this restriction query.                                      |
| data         | id                  | string    | ID of the restriction query.                                                                 |
| data         | type                | string    | Restriction queries type.                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "created_at": "2020-03-17T21:06:44.000Z",
      "last_modifier_email": "user@example.com",
      "last_modifier_name": "John Doe",
      "modified_at": "2020-03-17T21:15:15.000Z",
      "restriction_query": "env:sandbox",
      "role_count": 3,
      "user_count": 5
    },
    "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
    "type": "logs_restriction_queries"
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
Authentication error
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
Not found
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
                  \# Path parametersexport restriction_query_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "restriction_query": "env:sandbox"
    }
  }
}
EOF

#####

```python
"""
Update a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType
from datadog_api_client.v2.model.restriction_query_update_attributes import RestrictionQueryUpdateAttributes
from datadog_api_client.v2.model.restriction_query_update_data import RestrictionQueryUpdateData
from datadog_api_client.v2.model.restriction_query_update_payload import RestrictionQueryUpdatePayload

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

body = RestrictionQueryUpdatePayload(
    data=RestrictionQueryUpdateData(
        attributes=RestrictionQueryUpdateAttributes(
            restriction_query="env:production",
        ),
        type=LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.update_restriction_query(restriction_query_id=RESTRICTION_QUERY_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]

body = DatadogAPIClient::V2::RestrictionQueryUpdatePayload.new({
  data: DatadogAPIClient::V2::RestrictionQueryUpdateData.new({
    attributes: DatadogAPIClient::V2::RestrictionQueryUpdateAttributes.new({
      restriction_query: "env:production",
    }),
    type: DatadogAPIClient::V2::LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES,
  }),
})
p api_instance.update_restriction_query(RESTRICTION_QUERY_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Update a restriction query returns "OK" response

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
    // there is a valid "restriction_query" in the system
    RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

    body := datadogV2.RestrictionQueryUpdatePayload{
        Data: &datadogV2.RestrictionQueryUpdateData{
            Attributes: &datadogV2.RestrictionQueryUpdateAttributes{
                RestrictionQuery: "env:production",
            },
            Type: datadogV2.LOGSRESTRICTIONQUERIESTYPE_LOGS_RESTRICTION_QUERIES.Ptr(),
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.UpdateRestrictionQuery", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
    resp, r, err := api.UpdateRestrictionQuery(ctx, RestrictionQueryDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.UpdateRestrictionQuery`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.UpdateRestrictionQuery`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.LogsRestrictionQueriesType;
import com.datadog.api.client.v2.model.RestrictionQueryUpdateAttributes;
import com.datadog.api.client.v2.model.RestrictionQueryUpdateData;
import com.datadog.api.client.v2.model.RestrictionQueryUpdatePayload;
import com.datadog.api.client.v2.model.RestrictionQueryWithoutRelationshipsResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    RestrictionQueryUpdatePayload body =
        new RestrictionQueryUpdatePayload()
            .data(
                new RestrictionQueryUpdateData()
                    .attributes(
                        new RestrictionQueryUpdateAttributes().restrictionQuery("env:production"))
                    .type(LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES));

    try {
      RestrictionQueryWithoutRelationshipsResponse result =
          apiInstance.updateRestrictionQuery(RESTRICTION_QUERY_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsRestrictionQueriesApi#updateRestrictionQuery");
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
// Update a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;
use datadog_api_client::datadogV2::model::LogsRestrictionQueriesType;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdateAttributes;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdateData;
use datadog_api_client::datadogV2::model::RestrictionQueryUpdatePayload;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();
    let body = RestrictionQueryUpdatePayload::new().data(
        RestrictionQueryUpdateData::new()
            .attributes(RestrictionQueryUpdateAttributes::new(
                "env:production".to_string(),
            ))
            .type_(LogsRestrictionQueriesType::LOGS_RESTRICTION_QUERIES),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .update_restriction_query(restriction_query_data_id.clone(), body)
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
 * Update a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiUpdateRestrictionQueryRequest = {
  body: {
    data: {
      attributes: {
        restrictionQuery: "env:production",
      },
      type: "logs_restriction_queries",
    },
  },
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .updateRestrictionQuery(params)
  .then((data: v2.RestrictionQueryWithoutRelationshipsResponse) => {
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

## Delete a restriction query{% #delete-a-restriction-query %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id} |

### Overview

Deletes a restriction query. This endpoint requires the `user_access_manage` permission.

### Arguments

#### Path Parameters

| Name                                   | Type   | Description                      |
| -------------------------------------- | ------ | -------------------------------- |
| restriction_query_id [*required*] | string | The ID of the restriction query. |

### Response

{% tab title="204" %}
OK
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
Authentication error
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
Not found
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
                  \# Path parametersexport restriction_query_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    api_instance.delete_restriction_query(
        restriction_query_id=RESTRICTION_QUERY_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Delete a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]
api_instance.delete_restriction_query(RESTRICTION_QUERY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Delete a restriction query returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "restriction_query" in the system
    RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.DeleteRestrictionQuery", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
    r, err := api.DeleteRestrictionQuery(ctx, RestrictionQueryDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.DeleteRestrictionQuery`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Delete a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    try {
      apiInstance.deleteRestrictionQuery(RESTRICTION_QUERY_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsRestrictionQueriesApi#deleteRestrictionQuery");
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
// Delete a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .delete_restriction_query(restriction_query_data_id.clone())
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
 * Delete a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiDeleteRestrictionQueryRequest = {
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .deleteRestrictionQuery(params)
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

## List roles for a restriction query{% #list-roles-for-a-restriction-query %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                          |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |

### Overview

Returns all roles that have a given restriction query. This endpoint requires the `logs_read_config` permission.

### Arguments

#### Path Parameters

| Name                                   | Type   | Description                      |
| -------------------------------------- | ------ | -------------------------------- |
| restriction_query_id [*required*] | string | The ID of the restriction query. |

#### Query Strings

| Name         | Type    | Description                                              |
| ------------ | ------- | -------------------------------------------------------- |
| page[size]   | integer | Size for a given page. The maximum allowed value is 100. |
| page[number] | integer | Specific page number to return.                          |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about roles attached to a restriction query.

| Parent field | Field                        | Type     | Description                                     |
| ------------ | ---------------------------- | -------- | ----------------------------------------------- |
|              | data                         | [object] | Array of roles.                                 |
| data         | attributes [*required*] | object   | Attributes of the role for a restriction query. |
| attributes   | name                         | string   | The role name.                                  |
| data         | id [*required*]         | string   | ID of the role.                                 |
| data         | type [*required*]       | enum     | Roles type. Allowed enum values: `roles`        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "name": "Datadog Admin Role"
      },
      "id": "<ROLE_ID>",
      "type": "roles"
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
Authentication error
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
Not found
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
                  \# Path parametersexport restriction_query_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}/roles" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List roles for a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["list_restriction_query_roles"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.list_restriction_query_roles(
        restriction_query_id=RESTRICTION_QUERY_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List roles for a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_restriction_query_roles".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]
p api_instance.list_restriction_query_roles(RESTRICTION_QUERY_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List roles for a restriction query returns "OK" response

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
    // there is a valid "restriction_query" in the system
    RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.ListRestrictionQueryRoles", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
    resp, r, err := api.ListRestrictionQueryRoles(ctx, RestrictionQueryDataID, *datadogV2.NewListRestrictionQueryRolesOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.ListRestrictionQueryRoles`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.ListRestrictionQueryRoles`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List roles for a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RestrictionQueryRolesResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listRestrictionQueryRoles", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    try {
      RestrictionQueryRolesResponse result =
          apiInstance.listRestrictionQueryRoles(RESTRICTION_QUERY_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#listRestrictionQueryRoles");
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
// List roles for a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::ListRestrictionQueryRolesOptionalParams;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListRestrictionQueryRoles", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .list_restriction_query_roles(
            restriction_query_data_id.clone(),
            ListRestrictionQueryRolesOptionalParams::default(),
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
 * List roles for a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listRestrictionQueryRoles"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiListRestrictionQueryRolesRequest = {
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .listRestrictionQueryRoles(params)
  .then((data: v2.RestrictionQueryRolesResponse) => {
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

## Grant role to a restriction query{% #grant-role-to-a-restriction-query %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |

### Overview



Adds a role to a restriction query.

**Note**: This operation automatically grants the `logs_read_data` permission to the role if it doesn't already have it.
This endpoint requires the `user_access_manage` permission.


### Arguments

#### Path Parameters

| Name                                   | Type   | Description                      |
| -------------------------------------- | ------ | -------------------------------- |
| restriction_query_id [*required*] | string | The ID of the restriction query. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field | Type   | Description                              |
| ------------ | ----- | ------ | ---------------------------------------- |
|              | data  | object | Relationship to role object.             |
| data         | id    | string | The unique identifier of the role.       |
| data         | type  | enum   | Roles type. Allowed enum values: `roles` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "string",
    "type": "roles"
  }
}
```

{% /tab %}

### Response

{% tab title="204" %}
OK
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
Authentication error
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
Not found
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
                          \# Path parametersexport restriction_query_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}/roles" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "id": "string",
    "type": "roles"
  }
}
EOF

#####

```go
// Grant role to a restriction query returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "restriction_query" in the system
    RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

    // there is a valid "role" in the system
    RoleDataID := os.Getenv("ROLE_DATA_ID")

    body := datadogV2.RelationshipToRole{
        Data: &datadogV2.RelationshipToRoleData{
            Id:   datadog.PtrString(RoleDataID),
            Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.AddRoleToRestrictionQuery", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
    r, err := api.AddRoleToRestrictionQuery(ctx, RestrictionQueryDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.AddRoleToRestrictionQuery`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Grant role to a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RelationshipToRole;
import com.datadog.api.client.v2.model.RelationshipToRoleData;
import com.datadog.api.client.v2.model.RolesType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.addRoleToRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    RelationshipToRole body =
        new RelationshipToRole()
            .data(new RelationshipToRoleData().id(ROLE_DATA_ID).type(RolesType.ROLES));

    try {
      apiInstance.addRoleToRestrictionQuery(RESTRICTION_QUERY_DATA_ID, body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#addRoleToRestrictionQuery");
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

```python
"""
Grant role to a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = RelationshipToRole(
    data=RelationshipToRoleData(
        id=ROLE_DATA_ID,
        type=RolesType.ROLES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["add_role_to_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    api_instance.add_role_to_restriction_query(restriction_query_id=RESTRICTION_QUERY_DATA_ID, body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Grant role to a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.add_role_to_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

body = DatadogAPIClient::V2::RelationshipToRole.new({
  data: DatadogAPIClient::V2::RelationshipToRoleData.new({
    id: ROLE_DATA_ID,
    type: DatadogAPIClient::V2::RolesType::ROLES,
  }),
})
api_instance.add_role_to_restriction_query(RESTRICTION_QUERY_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Grant role to a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;
use datadog_api_client::datadogV2::model::RelationshipToRole;
use datadog_api_client::datadogV2::model::RelationshipToRoleData;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();

    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let body = RelationshipToRole::new().data(
        RelationshipToRoleData::new()
            .id(role_data_id.clone())
            .type_(RolesType::ROLES),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.AddRoleToRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .add_role_to_restriction_query(restriction_query_data_id.clone(), body)
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
 * Grant role to a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.addRoleToRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiAddRoleToRestrictionQueryRequest = {
  body: {
    data: {
      id: ROLE_DATA_ID,
      type: "roles",
    },
  },
  restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
};

apiInstance
  .addRoleToRestrictionQuery(params)
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

## Revoke role from a restriction query{% #revoke-role-from-a-restriction-query %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                             |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles |

### Overview

Removes a role from a restriction query. This endpoint requires the `user_access_manage` permission.

### Arguments

#### Path Parameters

| Name                                   | Type   | Description                      |
| -------------------------------------- | ------ | -------------------------------- |
| restriction_query_id [*required*] | string | The ID of the restriction query. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field | Type   | Description                              |
| ------------ | ----- | ------ | ---------------------------------------- |
|              | data  | object | Relationship to role object.             |
| data         | id    | string | The unique identifier of the role.       |
| data         | type  | enum   | Roles type. Allowed enum values: `roles` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
    "type": "roles"
  }
}
```

{% /tab %}

### Response

{% tab title="204" %}
OK
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
Authentication error
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
Not found
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
                  \# Path parametersexport restriction_query_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/${restriction_query_id}/roles" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF

#####

```python
"""
Revoke role from a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = RelationshipToRole(
    data=RelationshipToRoleData(
        id=ROLE_DATA_ID,
        type=RolesType.ROLES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["remove_role_from_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    api_instance.remove_role_from_restriction_query(restriction_query_id=RESTRICTION_QUERY_DATA_ID, body=body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Revoke role from a restriction query returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.remove_role_from_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = ENV["RESTRICTION_QUERY_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]

body = DatadogAPIClient::V2::RelationshipToRole.new({
  data: DatadogAPIClient::V2::RelationshipToRoleData.new({
    id: ROLE_DATA_ID,
    type: DatadogAPIClient::V2::RolesType::ROLES,
  }),
})
api_instance.remove_role_from_restriction_query(RESTRICTION_QUERY_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Revoke role from a restriction query returns "OK" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    // there is a valid "restriction_query" in the system
    RestrictionQueryDataID := os.Getenv("RESTRICTION_QUERY_DATA_ID")

    // there is a valid "role" in the system
    RoleDataID := os.Getenv("ROLE_DATA_ID")

    body := datadogV2.RelationshipToRole{
        Data: &datadogV2.RelationshipToRoleData{
            Id:   datadog.PtrString(RoleDataID),
            Type: datadogV2.ROLESTYPE_ROLES.Ptr(),
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.RemoveRoleFromRestrictionQuery", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
    r, err := api.RemoveRoleFromRestrictionQuery(ctx, RestrictionQueryDataID, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.RemoveRoleFromRestrictionQuery`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Revoke role from a restriction query returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RelationshipToRole;
import com.datadog.api.client.v2.model.RelationshipToRoleData;
import com.datadog.api.client.v2.model.RolesType;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.removeRoleFromRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "restriction_query" in the system
    String RESTRICTION_QUERY_DATA_ID = System.getenv("RESTRICTION_QUERY_DATA_ID");

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    RelationshipToRole body =
        new RelationshipToRole()
            .data(new RelationshipToRoleData().id(ROLE_DATA_ID).type(RolesType.ROLES));

    try {
      apiInstance.removeRoleFromRestrictionQuery(RESTRICTION_QUERY_DATA_ID, body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#removeRoleFromRestrictionQuery");
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
// Revoke role from a restriction query returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;
use datadog_api_client::datadogV2::model::RelationshipToRole;
use datadog_api_client::datadogV2::model::RelationshipToRoleData;
use datadog_api_client::datadogV2::model::RolesType;

#[tokio::main]
async fn main() {
    // there is a valid "restriction_query" in the system
    let restriction_query_data_id = std::env::var("RESTRICTION_QUERY_DATA_ID").unwrap();

    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let body = RelationshipToRole::new().data(
        RelationshipToRoleData::new()
            .id(role_data_id.clone())
            .type_(RolesType::ROLES),
    );
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.RemoveRoleFromRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .remove_role_from_restriction_query(restriction_query_data_id.clone(), body)
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
 * Revoke role from a restriction query returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.removeRoleFromRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "restriction_query" in the system
const RESTRICTION_QUERY_DATA_ID = process.env
  .RESTRICTION_QUERY_DATA_ID as string;

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiRemoveRoleFromRestrictionQueryRequest =
  {
    body: {
      data: {
        id: ROLE_DATA_ID,
        type: "roles",
      },
    },
    restrictionQueryId: RESTRICTION_QUERY_DATA_ID,
  };

apiInstance
  .removeRoleFromRestrictionQuery(params)
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

## Get all restriction queries for a given user{% #get-all-restriction-queries-for-a-given-user %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                            |
| ----------------- | --------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/user/{user_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/user/{user_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/user/{user_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/user/{user_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/restriction_queries/user/{user_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/user/{user_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/user/{user_id} |

### Overview

Get all restriction queries for a given user. This endpoint requires the `logs_read_config` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description         |
| ------------------------- | ------ | ------------------- |
| user_id [*required*] | string | The ID of the user. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about multiple restriction queries.

| Parent field | Field               | Type      | Description                                                                                  |
| ------------ | ------------------- | --------- | -------------------------------------------------------------------------------------------- |
|              | data                | [object]  | Array of returned restriction queries.                                                       |
| data         | attributes          | object    | Attributes of the restriction query.                                                         |
| attributes   | created_at          | date-time | Creation time of the restriction query.                                                      |
| attributes   | last_modifier_email | string    | Email of the user who last modified this restriction query.                                  |
| attributes   | last_modifier_name  | string    | Name of the user who last modified this restriction query.                                   |
| attributes   | modified_at         | date-time | Time of last restriction query modification.                                                 |
| attributes   | restriction_query   | string    | The query that defines the restriction. Only the content matching the query can be returned. |
| attributes   | role_count          | int64     | Number of roles associated with this restriction query.                                      |
| attributes   | user_count          | int64     | Number of users associated with this restriction query.                                      |
| data         | id                  | string    | ID of the restriction query.                                                                 |
| data         | type                | string    | Restriction queries type.                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_at": "2020-03-17T21:06:44.000Z",
        "last_modifier_email": "user@example.com",
        "last_modifier_name": "John Doe",
        "modified_at": "2020-03-17T21:15:15.000Z",
        "restriction_query": "env:sandbox",
        "role_count": 3,
        "user_count": 5
      },
      "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
      "type": "logs_restriction_queries"
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
Authentication error
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
Not found
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
                  \# Path parametersexport user_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/user/${user_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get all restriction queries for a given user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["list_user_restriction_queries"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.list_user_restriction_queries(
        user_id=USER_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get all restriction queries for a given user returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_user_restriction_queries".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "user" in the system
USER_DATA_ID = ENV["USER_DATA_ID"]
p api_instance.list_user_restriction_queries(USER_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get all restriction queries for a given user returns "OK" response

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
    // there is a valid "user" in the system
    UserDataID := os.Getenv("USER_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.ListUserRestrictionQueries", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
    resp, r, err := api.ListUserRestrictionQueries(ctx, UserDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.ListUserRestrictionQueries`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.ListUserRestrictionQueries`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get all restriction queries for a given user returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RestrictionQueryListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listUserRestrictionQueries", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "user" in the system
    String USER_DATA_ID = System.getenv("USER_DATA_ID");

    try {
      RestrictionQueryListResponse result = apiInstance.listUserRestrictionQueries(USER_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#listUserRestrictionQueries");
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
// Get all restriction queries for a given user returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "user" in the system
    let user_data_id = std::env::var("USER_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListUserRestrictionQueries", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api
        .list_user_restriction_queries(user_data_id.clone())
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
 * Get all restriction queries for a given user returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listUserRestrictionQueries"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "user" in the system
const USER_DATA_ID = process.env.USER_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiListUserRestrictionQueriesRequest = {
  userId: USER_DATA_ID,
};

apiInstance
  .listUserRestrictionQueries(params)
  .then((data: v2.RestrictionQueryListResponse) => {
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

## Get restriction query for a given role{% #get-restriction-query-for-a-given-role %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                            |
| ----------------- | --------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/logs/config/restriction_queries/role/{role_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/logs/config/restriction_queries/role/{role_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/logs/config/restriction_queries/role/{role_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/logs/config/restriction_queries/role/{role_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/logs/config/restriction_queries/role/{role_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/logs/config/restriction_queries/role/{role_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/role/{role_id} |

### Overview

Get restriction query for a given role. This endpoint requires the `logs_read_config` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description         |
| ------------------------- | ------ | ------------------- |
| role_id [*required*] | string | The ID of the role. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing information about multiple restriction queries.

| Parent field | Field               | Type      | Description                                                                                  |
| ------------ | ------------------- | --------- | -------------------------------------------------------------------------------------------- |
|              | data                | [object]  | Array of returned restriction queries.                                                       |
| data         | attributes          | object    | Attributes of the restriction query.                                                         |
| attributes   | created_at          | date-time | Creation time of the restriction query.                                                      |
| attributes   | last_modifier_email | string    | Email of the user who last modified this restriction query.                                  |
| attributes   | last_modifier_name  | string    | Name of the user who last modified this restriction query.                                   |
| attributes   | modified_at         | date-time | Time of last restriction query modification.                                                 |
| attributes   | restriction_query   | string    | The query that defines the restriction. Only the content matching the query can be returned. |
| attributes   | role_count          | int64     | Number of roles associated with this restriction query.                                      |
| attributes   | user_count          | int64     | Number of users associated with this restriction query.                                      |
| data         | id                  | string    | ID of the restriction query.                                                                 |
| data         | type                | string    | Restriction queries type.                                                                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "created_at": "2020-03-17T21:06:44.000Z",
        "last_modifier_email": "user@example.com",
        "last_modifier_name": "John Doe",
        "modified_at": "2020-03-17T21:15:15.000Z",
        "restriction_query": "env:sandbox",
        "role_count": 3,
        "user_count": 5
      },
      "id": "79a0e60a-644a-11ea-ad29-43329f7f58b5",
      "type": "logs_restriction_queries"
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
Authentication error
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
Not found
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
                  \# Path parametersexport role_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/logs/config/restriction_queries/role/${role_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get restriction query for a given role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_role_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.get_role_restriction_query(
        role_id=ROLE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get restriction query for a given role returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_role_restriction_query".to_sym] = true
end
api_instance = DatadogAPIClient::V2::LogsRestrictionQueriesAPI.new

# there is a valid "role" in the system
ROLE_DATA_ID = ENV["ROLE_DATA_ID"]
p api_instance.get_role_restriction_query(ROLE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get restriction query for a given role returns "OK" response

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
    // there is a valid "role" in the system
    RoleDataID := os.Getenv("ROLE_DATA_ID")

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    configuration.SetUnstableOperationEnabled("v2.GetRoleRestrictionQuery", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewLogsRestrictionQueriesApi(apiClient)
    resp, r, err := api.GetRoleRestrictionQuery(ctx, RoleDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `LogsRestrictionQueriesApi.GetRoleRestrictionQuery`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `LogsRestrictionQueriesApi.GetRoleRestrictionQuery`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get restriction query for a given role returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.LogsRestrictionQueriesApi;
import com.datadog.api.client.v2.model.RestrictionQueryListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getRoleRestrictionQuery", true);
    LogsRestrictionQueriesApi apiInstance = new LogsRestrictionQueriesApi(defaultClient);

    // there is a valid "role" in the system
    String ROLE_DATA_ID = System.getenv("ROLE_DATA_ID");

    try {
      RestrictionQueryListResponse result = apiInstance.getRoleRestrictionQuery(ROLE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling LogsRestrictionQueriesApi#getRoleRestrictionQuery");
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
// Get restriction query for a given role returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_logs_restriction_queries::LogsRestrictionQueriesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "role" in the system
    let role_data_id = std::env::var("ROLE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetRoleRestrictionQuery", true);
    let api = LogsRestrictionQueriesAPI::with_config(configuration);
    let resp = api.get_role_restriction_query(role_data_id.clone()).await;
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
 * Get restriction query for a given role returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getRoleRestrictionQuery"] = true;
const apiInstance = new v2.LogsRestrictionQueriesApi(configuration);

// there is a valid "role" in the system
const ROLE_DATA_ID = process.env.ROLE_DATA_ID as string;

const params: v2.LogsRestrictionQueriesApiGetRoleRestrictionQueryRequest = {
  roleId: ROLE_DATA_ID,
};

apiInstance
  .getRoleRestrictionQuery(params)
  .then((data: v2.RestrictionQueryListResponse) => {
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
