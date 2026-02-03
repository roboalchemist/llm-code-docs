# Source: https://docs.datadoghq.com/api/latest/dashboard-lists.md

---
title: Dashboard Lists
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Dashboard Lists
---

# Dashboard Lists

Interact with your dashboard lists through the API to organize, find, and share all of your dashboards with your team and organization.

## Get all dashboard lists{% #get-all-dashboard-lists %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/dashboard/lists/manual |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/dashboard/lists/manual |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/dashboard/lists/manual      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/dashboard/lists/manual      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/dashboard/lists/manual     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/dashboard/lists/manual |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual |

### Overview

Fetch all of your existing dashboard list definitions. This endpoint requires the `dashboards_read` permission.

OAuth apps require the `dashboards_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.



### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Information on your dashboard lists.

| Parent field    | Field                  | Type      | Description                                          |
| --------------- | ---------------------- | --------- | ---------------------------------------------------- |
|                 | dashboard_lists        | [object]  | List of all your dashboard lists.                    |
| dashboard_lists | author                 | object    | Object describing the creator of the shared element. |
| author          | email                  | string    | Email of the creator.                                |
| author          | handle                 | string    | Handle of the creator.                               |
| author          | name                   | string    | Name of the creator.                                 |
| dashboard_lists | created                | date-time | Date of creation of the dashboard list.              |
| dashboard_lists | dashboard_count        | int64     | The number of dashboards in the list.                |
| dashboard_lists | id                     | int64     | The ID of the dashboard list.                        |
| dashboard_lists | is_favorite            | boolean   | Whether or not the list is in the favorites.         |
| dashboard_lists | modified               | date-time | Date of last edition of the dashboard list.          |
| dashboard_lists | name [*required*] | string    | The name of the dashboard list.                      |
| dashboard_lists | type                   | string    | The type of dashboard list.                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "dashboard_lists": [
    {
      "author": {
        "email": "string",
        "handle": "string",
        "name": "string"
      },
      "created": "2019-09-19T10:00:00.000Z",
      "dashboard_count": "integer",
      "id": "integer",
      "is_favorite": false,
      "modified": "2019-09-19T10:00:00.000Z",
      "name": "My Dashboard",
      "type": "manual_dashboard_list"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get all dashboard lists returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.list_dashboard_lists()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get all dashboard lists returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DashboardListsAPI.new
p api_instance.list_dashboard_lists()
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

result = dog.get_all_dashboard_lists()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get all dashboard lists returns "OK" response

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
	api := datadogV1.NewDashboardListsApi(apiClient)
	resp, r, err := api.ListDashboardLists(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DashboardListsApi.ListDashboardLists`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DashboardListsApi.ListDashboardLists`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get all dashboard lists returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DashboardListsApi;
import com.datadog.api.client.v1.model.DashboardListListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DashboardListsApi apiInstance = new DashboardListsApi(defaultClient);

    try {
      DashboardListListResponse result = apiInstance.listDashboardLists();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardListsApi#listDashboardLists");
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

api.DashboardList.get_all()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
##### 

```rust
// Get all dashboard lists returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_dashboard_lists::DashboardListsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = DashboardListsAPI::with_config(configuration);
    let resp = api.list_dashboard_lists().await;
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
 * Get all dashboard lists returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DashboardListsApi(configuration);

apiInstance
  .listDashboardLists()
  .then((data: v1.DashboardListListResponse) => {
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

## Get items of a Dashboard List{% #get-items-of-a-dashboard-list %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |

### Overview

Fetch the dashboard list's dashboard definitions. This endpoint requires the `dashboards_read` permission.

OAuth apps require the `dashboards_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.



### Arguments

#### Path Parameters

| Name                                | Type    | Description                                 |
| ----------------------------------- | ------- | ------------------------------------------- |
| dashboard_list_id [*required*] | integer | ID of the dashboard list to get items from. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Dashboards within a list.

| Parent field | Field                        | Type      | Description                                                                                                                                        |
| ------------ | ---------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | dashboards [*required*] | [object]  | List of dashboards in the dashboard list.                                                                                                          |
| dashboards   | author                       | object    | Creator of the object.                                                                                                                             |
| author       | email                        | string    | Email of the creator.                                                                                                                              |
| author       | handle                       | string    | Handle of the creator.                                                                                                                             |
| author       | name                         | string    | Name of the creator.                                                                                                                               |
| dashboards   | created                      | date-time | Date of creation of the dashboard.                                                                                                                 |
| dashboards   | icon                         | string    | URL to the icon of the dashboard.                                                                                                                  |
| dashboards   | id [*required*]         | string    | ID of the dashboard.                                                                                                                               |
| dashboards   | integration_id               | string    | The short name of the integration.                                                                                                                 |
| dashboards   | is_favorite                  | boolean   | Whether or not the dashboard is in the favorites.                                                                                                  |
| dashboards   | is_read_only                 | boolean   | Whether or not the dashboard is read only.                                                                                                         |
| dashboards   | is_shared                    | boolean   | Whether the dashboard is publicly shared or not.                                                                                                   |
| dashboards   | modified                     | date-time | Date of last edition of the dashboard.                                                                                                             |
| dashboards   | popularity                   | int32     | Popularity of the dashboard.                                                                                                                       |
| dashboards   | tags                         | [string]  | List of team names representing ownership of a dashboard.                                                                                          |
| dashboards   | title                        | string    | Title of the dashboard.                                                                                                                            |
| dashboards   | type [*required*]       | enum      | The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard` |
| dashboards   | url                          | string    | URL path to the dashboard.                                                                                                                         |
|              | total                        | int64     | Number of dashboards in the dashboard list.                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "dashboards": [
    {
      "author": {
        "email": "string",
        "handle": "string",
        "name": "string"
      },
      "created": "2019-09-19T10:00:00.000Z",
      "icon": "string",
      "id": "q5j-nti-fv6",
      "integration_id": "string",
      "is_favorite": false,
      "is_read_only": false,
      "is_shared": false,
      "modified": "2019-09-19T10:00:00.000Z",
      "popularity": "integer",
      "tags": [],
      "title": "string",
      "type": "host_timeboard",
      "url": "string"
    }
  ],
  "total": "integer"
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
                  \# Path parametersexport dashboard_list_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get items of a Dashboard List returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = environ["DASHBOARD_LIST_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.get_dashboard_list_items(
        dashboard_list_id=int(DASHBOARD_LIST_ID),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get items of a Dashboard List returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]
p api_instance.get_dashboard_list_items(DASHBOARD_LIST_ID.to_i)
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

result = dog.v2.get_items_of_dashboard_list(4741)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get items of a Dashboard List returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "dashboard_list" in the system
	DashboardListID, _ := strconv.ParseInt(os.Getenv("DASHBOARD_LIST_ID"), 10, 64)

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDashboardListsApi(apiClient)
	resp, r, err := api.GetDashboardListItems(ctx, DashboardListID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DashboardListsApi.GetDashboardListItems`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DashboardListsApi.GetDashboardListItems`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get items of a Dashboard List returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DashboardListsApi;
import com.datadog.api.client.v2.model.DashboardListItems;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DashboardListsApi apiInstance = new DashboardListsApi(defaultClient);

    // there is a valid "dashboard_list" in the system
    Long DASHBOARD_LIST_ID = Long.parseLong(System.getenv("DASHBOARD_LIST_ID"));

    try {
      DashboardListItems result = apiInstance.getDashboardListItems(DASHBOARD_LIST_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardListsApi#getDashboardListItems");
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

api.DashboardList.v2.get_items(4741)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
##### 

```rust
// Get items of a Dashboard List returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dashboard_lists::DashboardListsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dashboard_list" in the system
    let dashboard_list_id: i64 = std::env::var("DASHBOARD_LIST_ID").unwrap().parse().unwrap();
    let configuration = datadog::Configuration::new();
    let api = DashboardListsAPI::with_config(configuration);
    let resp = api
        .get_dashboard_list_items(dashboard_list_id.clone())
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
 * Get items of a Dashboard List returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DashboardListsApi(configuration);

// there is a valid "dashboard_list" in the system
const DASHBOARD_LIST_ID = parseInt(process.env.DASHBOARD_LIST_ID as string);

const params: v2.DashboardListsApiGetDashboardListItemsRequest = {
  dashboardListId: DASHBOARD_LIST_ID,
};

apiInstance
  .getDashboardListItems(params)
  .then((data: v2.DashboardListItems) => {
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

## Add Items to a Dashboard List{% #add-items-to-a-dashboard-list %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |

### Overview

Add dashboards to an existing dashboard list.

### Arguments

#### Path Parameters

| Name                                | Type    | Description                               |
| ----------------------------------- | ------- | ----------------------------------------- |
| dashboard_list_id [*required*] | integer | ID of the dashboard list to add items to. |

### Request

#### Body Data (required)

Dashboards to add to the dashboard list.

{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                                                                                        |
| ------------ | ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | dashboards             | [object] | List of dashboards to add the dashboard list.                                                                                                      |
| dashboards   | id [*required*]   | string   | ID of the dashboard.                                                                                                                               |
| dashboards   | type [*required*] | enum     | The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard` |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_screenboard"
    }
  ]
}
```

##### 

```json
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_timeboard"
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a list of added dashboards.

| Parent field             | Field                    | Type     | Description                                                                                                                                        |
| ------------------------ | ------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|                          | added_dashboards_to_list | [object] | List of dashboards added to the dashboard list.                                                                                                    |
| added_dashboards_to_list | id [*required*]     | string   | ID of the dashboard.                                                                                                                               |
| added_dashboards_to_list | type [*required*]   | enum     | The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "added_dashboards_to_list": [
    {
      "id": "q5j-nti-fv6",
      "type": "host_timeboard"
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
                          \# Path parametersexport dashboard_list_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_screenboard"
    }
  ]
}
EOF
                        
##### 
                          \# Path parametersexport dashboard_list_id="CHANGE_ME"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_timeboard"
    }
  ]
}
EOF
                        
##### 

```go
// Add custom screenboard dashboard to an existing dashboard list returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "dashboard_list" in the system
	DashboardListID, _ := strconv.ParseInt(os.Getenv("DASHBOARD_LIST_ID"), 10, 64)

	// there is a valid "screenboard_dashboard" in the system
	ScreenboardDashboardID := os.Getenv("SCREENBOARD_DASHBOARD_ID")

	body := datadogV2.DashboardListAddItemsRequest{
		Dashboards: []datadogV2.DashboardListItemRequest{
			{
				Id:   ScreenboardDashboardID,
				Type: datadogV2.DASHBOARDTYPE_CUSTOM_SCREENBOARD,
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDashboardListsApi(apiClient)
	resp, r, err := api.CreateDashboardListItems(ctx, DashboardListID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DashboardListsApi.CreateDashboardListItems`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DashboardListsApi.CreateDashboardListItems`:\n%s\n", responseContent)
}
```

##### 

```go
// Add custom timeboard dashboard to an existing dashboard list returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "dashboard_list" in the system
	DashboardListID, _ := strconv.ParseInt(os.Getenv("DASHBOARD_LIST_ID"), 10, 64)

	// there is a valid "dashboard" in the system
	DashboardID := os.Getenv("DASHBOARD_ID")

	body := datadogV2.DashboardListAddItemsRequest{
		Dashboards: []datadogV2.DashboardListItemRequest{
			{
				Id:   DashboardID,
				Type: datadogV2.DASHBOARDTYPE_CUSTOM_TIMEBOARD,
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDashboardListsApi(apiClient)
	resp, r, err := api.CreateDashboardListItems(ctx, DashboardListID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DashboardListsApi.CreateDashboardListItems`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DashboardListsApi.CreateDashboardListItems`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Add custom screenboard dashboard to an existing dashboard list returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DashboardListsApi;
import com.datadog.api.client.v2.model.DashboardListAddItemsRequest;
import com.datadog.api.client.v2.model.DashboardListAddItemsResponse;
import com.datadog.api.client.v2.model.DashboardListItemRequest;
import com.datadog.api.client.v2.model.DashboardType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DashboardListsApi apiInstance = new DashboardListsApi(defaultClient);

    // there is a valid "dashboard_list" in the system
    Long DASHBOARD_LIST_ID = Long.parseLong(System.getenv("DASHBOARD_LIST_ID"));

    // there is a valid "screenboard_dashboard" in the system
    String SCREENBOARD_DASHBOARD_ID = System.getenv("SCREENBOARD_DASHBOARD_ID");

    DashboardListAddItemsRequest body =
        new DashboardListAddItemsRequest()
            .dashboards(
                Collections.singletonList(
                    new DashboardListItemRequest()
                        .id(SCREENBOARD_DASHBOARD_ID)
                        .type(DashboardType.CUSTOM_SCREENBOARD)));

    try {
      DashboardListAddItemsResponse result =
          apiInstance.createDashboardListItems(DASHBOARD_LIST_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardListsApi#createDashboardListItems");
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
// Add custom timeboard dashboard to an existing dashboard list returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DashboardListsApi;
import com.datadog.api.client.v2.model.DashboardListAddItemsRequest;
import com.datadog.api.client.v2.model.DashboardListAddItemsResponse;
import com.datadog.api.client.v2.model.DashboardListItemRequest;
import com.datadog.api.client.v2.model.DashboardType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DashboardListsApi apiInstance = new DashboardListsApi(defaultClient);

    // there is a valid "dashboard_list" in the system
    Long DASHBOARD_LIST_ID = Long.parseLong(System.getenv("DASHBOARD_LIST_ID"));

    // there is a valid "dashboard" in the system
    String DASHBOARD_ID = System.getenv("DASHBOARD_ID");

    DashboardListAddItemsRequest body =
        new DashboardListAddItemsRequest()
            .dashboards(
                Collections.singletonList(
                    new DashboardListItemRequest()
                        .id(DASHBOARD_ID)
                        .type(DashboardType.CUSTOM_TIMEBOARD)));

    try {
      DashboardListAddItemsResponse result =
          apiInstance.createDashboardListItems(DASHBOARD_LIST_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardListsApi#createDashboardListItems");
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
Add custom screenboard dashboard to an existing dashboard list returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v2.model.dashboard_list_add_items_request import DashboardListAddItemsRequest
from datadog_api_client.v2.model.dashboard_list_item_request import DashboardListItemRequest
from datadog_api_client.v2.model.dashboard_type import DashboardType

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = environ["DASHBOARD_LIST_ID"]

# there is a valid "screenboard_dashboard" in the system
SCREENBOARD_DASHBOARD_ID = environ["SCREENBOARD_DASHBOARD_ID"]

body = DashboardListAddItemsRequest(
    dashboards=[
        DashboardListItemRequest(
            id=SCREENBOARD_DASHBOARD_ID,
            type=DashboardType.CUSTOM_SCREENBOARD,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.create_dashboard_list_items(dashboard_list_id=int(DASHBOARD_LIST_ID), body=body)

    print(response)
```

##### 

```python
"""
Add custom timeboard dashboard to an existing dashboard list returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v2.model.dashboard_list_add_items_request import DashboardListAddItemsRequest
from datadog_api_client.v2.model.dashboard_list_item_request import DashboardListItemRequest
from datadog_api_client.v2.model.dashboard_type import DashboardType

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = environ["DASHBOARD_LIST_ID"]

# there is a valid "dashboard" in the system
DASHBOARD_ID = environ["DASHBOARD_ID"]

body = DashboardListAddItemsRequest(
    dashboards=[
        DashboardListItemRequest(
            id=DASHBOARD_ID,
            type=DashboardType.CUSTOM_TIMEBOARD,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.create_dashboard_list_items(dashboard_list_id=int(DASHBOARD_LIST_ID), body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Add custom screenboard dashboard to an existing dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]

# there is a valid "screenboard_dashboard" in the system
SCREENBOARD_DASHBOARD_ID = ENV["SCREENBOARD_DASHBOARD_ID"]

body = DatadogAPIClient::V2::DashboardListAddItemsRequest.new({
  dashboards: [
    DatadogAPIClient::V2::DashboardListItemRequest.new({
      id: SCREENBOARD_DASHBOARD_ID,
      type: DatadogAPIClient::V2::DashboardType::CUSTOM_SCREENBOARD,
    }),
  ],
})
p api_instance.create_dashboard_list_items(DASHBOARD_LIST_ID.to_i, body)
```

##### 

```ruby
# Add custom timeboard dashboard to an existing dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]

# there is a valid "dashboard" in the system
DASHBOARD_ID = ENV["DASHBOARD_ID"]

body = DatadogAPIClient::V2::DashboardListAddItemsRequest.new({
  dashboards: [
    DatadogAPIClient::V2::DashboardListItemRequest.new({
      id: DASHBOARD_ID,
      type: DatadogAPIClient::V2::DashboardType::CUSTOM_TIMEBOARD,
    }),
  ],
})
p api_instance.create_dashboard_list_items(DASHBOARD_LIST_ID.to_i, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Add custom screenboard dashboard to an existing dashboard list returns "OK"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dashboard_lists::DashboardListsAPI;
use datadog_api_client::datadogV2::model::DashboardListAddItemsRequest;
use datadog_api_client::datadogV2::model::DashboardListItemRequest;
use datadog_api_client::datadogV2::model::DashboardType;

#[tokio::main]
async fn main() {
    // there is a valid "dashboard_list" in the system
    let dashboard_list_id: i64 = std::env::var("DASHBOARD_LIST_ID").unwrap().parse().unwrap();

    // there is a valid "screenboard_dashboard" in the system
    let screenboard_dashboard_id = std::env::var("SCREENBOARD_DASHBOARD_ID").unwrap();
    let body = DashboardListAddItemsRequest::new().dashboards(vec![DashboardListItemRequest::new(
        screenboard_dashboard_id.clone(),
        DashboardType::CUSTOM_SCREENBOARD,
    )]);
    let configuration = datadog::Configuration::new();
    let api = DashboardListsAPI::with_config(configuration);
    let resp = api
        .create_dashboard_list_items(dashboard_list_id.clone(), body)
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
// Add custom timeboard dashboard to an existing dashboard list returns "OK"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dashboard_lists::DashboardListsAPI;
use datadog_api_client::datadogV2::model::DashboardListAddItemsRequest;
use datadog_api_client::datadogV2::model::DashboardListItemRequest;
use datadog_api_client::datadogV2::model::DashboardType;

#[tokio::main]
async fn main() {
    // there is a valid "dashboard_list" in the system
    let dashboard_list_id: i64 = std::env::var("DASHBOARD_LIST_ID").unwrap().parse().unwrap();

    // there is a valid "dashboard" in the system
    let dashboard_id = std::env::var("DASHBOARD_ID").unwrap();
    let body = DashboardListAddItemsRequest::new().dashboards(vec![DashboardListItemRequest::new(
        dashboard_id.clone(),
        DashboardType::CUSTOM_TIMEBOARD,
    )]);
    let configuration = datadog::Configuration::new();
    let api = DashboardListsAPI::with_config(configuration);
    let resp = api
        .create_dashboard_list_items(dashboard_list_id.clone(), body)
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
 * Add custom screenboard dashboard to an existing dashboard list returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DashboardListsApi(configuration);

// there is a valid "dashboard_list" in the system
const DASHBOARD_LIST_ID = parseInt(process.env.DASHBOARD_LIST_ID as string);

// there is a valid "screenboard_dashboard" in the system
const SCREENBOARD_DASHBOARD_ID = process.env.SCREENBOARD_DASHBOARD_ID as string;

const params: v2.DashboardListsApiCreateDashboardListItemsRequest = {
  body: {
    dashboards: [
      {
        id: SCREENBOARD_DASHBOARD_ID,
        type: "custom_screenboard",
      },
    ],
  },
  dashboardListId: DASHBOARD_LIST_ID,
};

apiInstance
  .createDashboardListItems(params)
  .then((data: v2.DashboardListAddItemsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Add custom timeboard dashboard to an existing dashboard list returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DashboardListsApi(configuration);

// there is a valid "dashboard_list" in the system
const DASHBOARD_LIST_ID = parseInt(process.env.DASHBOARD_LIST_ID as string);

// there is a valid "dashboard" in the system
const DASHBOARD_ID = process.env.DASHBOARD_ID as string;

const params: v2.DashboardListsApiCreateDashboardListItemsRequest = {
  body: {
    dashboards: [
      {
        id: DASHBOARD_ID,
        type: "custom_timeboard",
      },
    ],
  },
  dashboardListId: DASHBOARD_LIST_ID,
};

apiInstance
  .createDashboardListItems(params)
  .then((data: v2.DashboardListAddItemsResponse) => {
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

## Create a dashboard list{% #create-a-dashboard-list %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/dashboard/lists/manual |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/dashboard/lists/manual |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/dashboard/lists/manual      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/dashboard/lists/manual      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/dashboard/lists/manual     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/dashboard/lists/manual |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual |

### Overview

Create an empty dashboard list. This endpoint requires the `dashboards_write` permission.

OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.



### Request

#### Body Data (required)

Create a dashboard list request body.

{% tab title="Model" %}

| Parent field | Field                  | Type      | Description                                          |
| ------------ | ---------------------- | --------- | ---------------------------------------------------- |
|              | author                 | object    | Object describing the creator of the shared element. |
| author       | email                  | string    | Email of the creator.                                |
| author       | handle                 | string    | Handle of the creator.                               |
| author       | name                   | string    | Name of the creator.                                 |
|              | created                | date-time | Date of creation of the dashboard list.              |
|              | dashboard_count        | int64     | The number of dashboards in the list.                |
|              | id                     | int64     | The ID of the dashboard list.                        |
|              | is_favorite            | boolean   | Whether or not the list is in the favorites.         |
|              | modified               | date-time | Date of last edition of the dashboard list.          |
|              | name [*required*] | string    | The name of the dashboard list.                      |
|              | type                   | string    | The type of dashboard list.                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "name": "Example-Dashboard-List"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Your Datadog Dashboards.

| Parent field | Field                  | Type      | Description                                          |
| ------------ | ---------------------- | --------- | ---------------------------------------------------- |
|              | author                 | object    | Object describing the creator of the shared element. |
| author       | email                  | string    | Email of the creator.                                |
| author       | handle                 | string    | Handle of the creator.                               |
| author       | name                   | string    | Name of the creator.                                 |
|              | created                | date-time | Date of creation of the dashboard list.              |
|              | dashboard_count        | int64     | The number of dashboards in the list.                |
|              | id                     | int64     | The ID of the dashboard list.                        |
|              | is_favorite            | boolean   | Whether or not the list is in the favorites.         |
|              | modified               | date-time | Date of last edition of the dashboard list.          |
|              | name [*required*] | string    | The name of the dashboard list.                      |
|              | type                   | string    | The type of dashboard list.                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "author": {
    "email": "string",
    "handle": "string",
    "name": "string"
  },
  "created": "2019-09-19T10:00:00.000Z",
  "dashboard_count": "integer",
  "id": "integer",
  "is_favorite": false,
  "modified": "2019-09-19T10:00:00.000Z",
  "name": "My Dashboard",
  "type": "manual_dashboard_list"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "Example-Dashboard-List"
}
EOF
                        
##### 

```go
// Create a dashboard list returns "OK" response

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
	body := datadogV1.DashboardList{
		Name: "Example-Dashboard-List",
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewDashboardListsApi(apiClient)
	resp, r, err := api.CreateDashboardList(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DashboardListsApi.CreateDashboardList`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DashboardListsApi.CreateDashboardList`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create a dashboard list returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DashboardListsApi;
import com.datadog.api.client.v1.model.DashboardList;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DashboardListsApi apiInstance = new DashboardListsApi(defaultClient);

    DashboardList body = new DashboardList().name("Example-Dashboard-List");

    try {
      DashboardList result = apiInstance.createDashboardList(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardListsApi#createDashboardList");
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

name = 'My Dashboard List'

api.DashboardList.create(name=name)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
##### 

```python
"""
Create a dashboard list returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v1.model.dashboard_list import DashboardList

body = DashboardList(
    name="Example-Dashboard-List",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.create_dashboard_list(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

name = 'My Dashboard List'

result = dog.create_dashboard_list(name)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```ruby
# Create a dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DashboardListsAPI.new

body = DatadogAPIClient::V1::DashboardList.new({
  name: "Example-Dashboard-List",
})
p api_instance.create_dashboard_list(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Create a dashboard list returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_dashboard_lists::DashboardListsAPI;
use datadog_api_client::datadogV1::model::DashboardList;

#[tokio::main]
async fn main() {
    let body = DashboardList::new("Example-Dashboard-List".to_string());
    let configuration = datadog::Configuration::new();
    let api = DashboardListsAPI::with_config(configuration);
    let resp = api.create_dashboard_list(body).await;
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
 * Create a dashboard list returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DashboardListsApi(configuration);

const params: v1.DashboardListsApiCreateDashboardListRequest = {
  body: {
    name: "Example-Dashboard-List",
  },
};

apiInstance
  .createDashboardList(params)
  .then((data: v1.DashboardList) => {
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

## Get a dashboard list{% #get-a-dashboard-list %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/dashboard/lists/manual/{list_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/dashboard/lists/manual/{list_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |

### Overview

Fetch an existing dashboard list's definition. This endpoint requires the `dashboards_read` permission.

OAuth apps require the `dashboards_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type    | Description                        |
| ------------------------- | ------- | ---------------------------------- |
| list_id [*required*] | integer | ID of the dashboard list to fetch. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Your Datadog Dashboards.

| Parent field | Field                  | Type      | Description                                          |
| ------------ | ---------------------- | --------- | ---------------------------------------------------- |
|              | author                 | object    | Object describing the creator of the shared element. |
| author       | email                  | string    | Email of the creator.                                |
| author       | handle                 | string    | Handle of the creator.                               |
| author       | name                   | string    | Name of the creator.                                 |
|              | created                | date-time | Date of creation of the dashboard list.              |
|              | dashboard_count        | int64     | The number of dashboards in the list.                |
|              | id                     | int64     | The ID of the dashboard list.                        |
|              | is_favorite            | boolean   | Whether or not the list is in the favorites.         |
|              | modified               | date-time | Date of last edition of the dashboard list.          |
|              | name [*required*] | string    | The name of the dashboard list.                      |
|              | type                   | string    | The type of dashboard list.                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "author": {
    "email": "string",
    "handle": "string",
    "name": "string"
  },
  "created": "2019-09-19T10:00:00.000Z",
  "dashboard_count": "integer",
  "id": "integer",
  "is_favorite": false,
  "modified": "2019-09-19T10:00:00.000Z",
  "name": "My Dashboard",
  "type": "manual_dashboard_list"
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
                  \# Path parametersexport list_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/${list_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a dashboard list returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = environ["DASHBOARD_LIST_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.get_dashboard_list(
        list_id=int(DASHBOARD_LIST_ID),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]
p api_instance.get_dashboard_list(DASHBOARD_LIST_ID.to_i)
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

result = dog.get_dashboard_list(4741)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a dashboard list returns "OK" response

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
	// there is a valid "dashboard_list" in the system
	DashboardListID, _ := strconv.ParseInt(os.Getenv("DASHBOARD_LIST_ID"), 10, 64)

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewDashboardListsApi(apiClient)
	resp, r, err := api.GetDashboardList(ctx, DashboardListID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DashboardListsApi.GetDashboardList`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DashboardListsApi.GetDashboardList`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a dashboard list returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DashboardListsApi;
import com.datadog.api.client.v1.model.DashboardList;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DashboardListsApi apiInstance = new DashboardListsApi(defaultClient);

    // there is a valid "dashboard_list" in the system
    Long DASHBOARD_LIST_ID = Long.parseLong(System.getenv("DASHBOARD_LIST_ID"));

    try {
      DashboardList result = apiInstance.getDashboardList(DASHBOARD_LIST_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardListsApi#getDashboardList");
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

api.DashboardList.get(4741)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
##### 

```rust
// Get a dashboard list returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_dashboard_lists::DashboardListsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dashboard_list" in the system
    let dashboard_list_id: i64 = std::env::var("DASHBOARD_LIST_ID").unwrap().parse().unwrap();
    let configuration = datadog::Configuration::new();
    let api = DashboardListsAPI::with_config(configuration);
    let resp = api.get_dashboard_list(dashboard_list_id.clone()).await;
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
 * Get a dashboard list returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DashboardListsApi(configuration);

// there is a valid "dashboard_list" in the system
const DASHBOARD_LIST_ID = parseInt(process.env.DASHBOARD_LIST_ID as string);

const params: v1.DashboardListsApiGetDashboardListRequest = {
  listId: DASHBOARD_LIST_ID,
};

apiInstance
  .getDashboardList(params)
  .then((data: v1.DashboardList) => {
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

## Update items of a dashboard list{% #update-items-of-a-dashboard-list %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |

### Overview

Update dashboards of an existing dashboard list.

### Arguments

#### Path Parameters

| Name                                | Type    | Description                                    |
| ----------------------------------- | ------- | ---------------------------------------------- |
| dashboard_list_id [*required*] | integer | ID of the dashboard list to update items from. |

### Request

#### Body Data (required)

New dashboards of the dashboard list.

{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                                                                                        |
| ------------ | ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | dashboards             | [object] | List of dashboards to update the dashboard list to.                                                                                                |
| dashboards   | id [*required*]   | string   | ID of the dashboard.                                                                                                                               |
| dashboards   | type [*required*] | enum     | The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_screenboard"
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a list of updated dashboards.

| Parent field | Field                  | Type     | Description                                                                                                                                        |
| ------------ | ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | dashboards             | [object] | List of dashboards in the dashboard list.                                                                                                          |
| dashboards   | id [*required*]   | string   | ID of the dashboard.                                                                                                                               |
| dashboards   | type [*required*] | enum     | The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "dashboards": [
    {
      "id": "q5j-nti-fv6",
      "type": "host_timeboard"
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
                          \# Path parametersexport dashboard_list_id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_screenboard"
    }
  ]
}
EOF
                        
##### 

```go
// Update items of a dashboard list returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "dashboard_list" in the system
	DashboardListID, _ := strconv.ParseInt(os.Getenv("DASHBOARD_LIST_ID"), 10, 64)

	// there is a valid "screenboard_dashboard" in the system
	ScreenboardDashboardID := os.Getenv("SCREENBOARD_DASHBOARD_ID")

	body := datadogV2.DashboardListUpdateItemsRequest{
		Dashboards: []datadogV2.DashboardListItemRequest{
			{
				Id:   ScreenboardDashboardID,
				Type: datadogV2.DASHBOARDTYPE_CUSTOM_SCREENBOARD,
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDashboardListsApi(apiClient)
	resp, r, err := api.UpdateDashboardListItems(ctx, DashboardListID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DashboardListsApi.UpdateDashboardListItems`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DashboardListsApi.UpdateDashboardListItems`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Update items of a dashboard list returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DashboardListsApi;
import com.datadog.api.client.v2.model.DashboardListItemRequest;
import com.datadog.api.client.v2.model.DashboardListUpdateItemsRequest;
import com.datadog.api.client.v2.model.DashboardListUpdateItemsResponse;
import com.datadog.api.client.v2.model.DashboardType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DashboardListsApi apiInstance = new DashboardListsApi(defaultClient);

    // there is a valid "dashboard_list" in the system
    Long DASHBOARD_LIST_ID = Long.parseLong(System.getenv("DASHBOARD_LIST_ID"));

    // there is a valid "screenboard_dashboard" in the system
    String SCREENBOARD_DASHBOARD_ID = System.getenv("SCREENBOARD_DASHBOARD_ID");

    DashboardListUpdateItemsRequest body =
        new DashboardListUpdateItemsRequest()
            .dashboards(
                Collections.singletonList(
                    new DashboardListItemRequest()
                        .id(SCREENBOARD_DASHBOARD_ID)
                        .type(DashboardType.CUSTOM_SCREENBOARD)));

    try {
      DashboardListUpdateItemsResponse result =
          apiInstance.updateDashboardListItems(DASHBOARD_LIST_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardListsApi#updateDashboardListItems");
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
Update items of a dashboard list returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v2.model.dashboard_list_item_request import DashboardListItemRequest
from datadog_api_client.v2.model.dashboard_list_update_items_request import DashboardListUpdateItemsRequest
from datadog_api_client.v2.model.dashboard_type import DashboardType

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = environ["DASHBOARD_LIST_ID"]

# there is a valid "screenboard_dashboard" in the system
SCREENBOARD_DASHBOARD_ID = environ["SCREENBOARD_DASHBOARD_ID"]

body = DashboardListUpdateItemsRequest(
    dashboards=[
        DashboardListItemRequest(
            id=SCREENBOARD_DASHBOARD_ID,
            type=DashboardType.CUSTOM_SCREENBOARD,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.update_dashboard_list_items(dashboard_list_id=int(DASHBOARD_LIST_ID), body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Update items of a dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]

# there is a valid "screenboard_dashboard" in the system
SCREENBOARD_DASHBOARD_ID = ENV["SCREENBOARD_DASHBOARD_ID"]

body = DatadogAPIClient::V2::DashboardListUpdateItemsRequest.new({
  dashboards: [
    DatadogAPIClient::V2::DashboardListItemRequest.new({
      id: SCREENBOARD_DASHBOARD_ID,
      type: DatadogAPIClient::V2::DashboardType::CUSTOM_SCREENBOARD,
    }),
  ],
})
p api_instance.update_dashboard_list_items(DASHBOARD_LIST_ID.to_i, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Update items of a dashboard list returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dashboard_lists::DashboardListsAPI;
use datadog_api_client::datadogV2::model::DashboardListItemRequest;
use datadog_api_client::datadogV2::model::DashboardListUpdateItemsRequest;
use datadog_api_client::datadogV2::model::DashboardType;

#[tokio::main]
async fn main() {
    // there is a valid "dashboard_list" in the system
    let dashboard_list_id: i64 = std::env::var("DASHBOARD_LIST_ID").unwrap().parse().unwrap();

    // there is a valid "screenboard_dashboard" in the system
    let screenboard_dashboard_id = std::env::var("SCREENBOARD_DASHBOARD_ID").unwrap();
    let body =
        DashboardListUpdateItemsRequest::new().dashboards(vec![DashboardListItemRequest::new(
            screenboard_dashboard_id.clone(),
            DashboardType::CUSTOM_SCREENBOARD,
        )]);
    let configuration = datadog::Configuration::new();
    let api = DashboardListsAPI::with_config(configuration);
    let resp = api
        .update_dashboard_list_items(dashboard_list_id.clone(), body)
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
 * Update items of a dashboard list returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DashboardListsApi(configuration);

// there is a valid "dashboard_list" in the system
const DASHBOARD_LIST_ID = parseInt(process.env.DASHBOARD_LIST_ID as string);

// there is a valid "screenboard_dashboard" in the system
const SCREENBOARD_DASHBOARD_ID = process.env.SCREENBOARD_DASHBOARD_ID as string;

const params: v2.DashboardListsApiUpdateDashboardListItemsRequest = {
  body: {
    dashboards: [
      {
        id: SCREENBOARD_DASHBOARD_ID,
        type: "custom_screenboard",
      },
    ],
  },
  dashboardListId: DASHBOARD_LIST_ID,
};

apiInstance
  .updateDashboardListItems(params)
  .then((data: v2.DashboardListUpdateItemsResponse) => {
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

## Delete items from a dashboard list{% #delete-items-from-a-dashboard-list %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards |

### Overview

Delete dashboards from an existing dashboard list.

### Arguments

#### Path Parameters

| Name                                | Type    | Description                                    |
| ----------------------------------- | ------- | ---------------------------------------------- |
| dashboard_list_id [*required*] | integer | ID of the dashboard list to delete items from. |

### Request

#### Body Data (required)

Dashboards to delete from the dashboard list.

{% tab title="Model" %}

| Parent field | Field                  | Type     | Description                                                                                                                                        |
| ------------ | ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | dashboards             | [object] | List of dashboards to delete from the dashboard list.                                                                                              |
| dashboards   | id [*required*]   | string   | ID of the dashboard.                                                                                                                               |
| dashboards   | type [*required*] | enum     | The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard` |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_screenboard"
    }
  ]
}
```

##### 

```json
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_timeboard"
    }
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a list of deleted dashboards.

| Parent field                 | Field                        | Type     | Description                                                                                                                                        |
| ---------------------------- | ---------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|                              | deleted_dashboards_from_list | [object] | List of dashboards deleted from the dashboard list.                                                                                                |
| deleted_dashboards_from_list | id [*required*]         | string   | ID of the dashboard.                                                                                                                               |
| deleted_dashboards_from_list | type [*required*]       | enum     | The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "deleted_dashboards_from_list": [
    {
      "id": "q5j-nti-fv6",
      "type": "host_timeboard"
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
                          \# Path parametersexport dashboard_list_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_screenboard"
    }
  ]
}
EOF
                        
##### 
                          \# Path parametersexport dashboard_list_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_timeboard"
    }
  ]
}
EOF
                        
##### 

```go
// Delete custom screenboard dashboard from an existing dashboard list returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "dashboard_list" in the system
	DashboardListID, _ := strconv.ParseInt(os.Getenv("DASHBOARD_LIST_ID"), 10, 64)

	// there is a valid "screenboard_dashboard" in the system
	ScreenboardDashboardID := os.Getenv("SCREENBOARD_DASHBOARD_ID")

	body := datadogV2.DashboardListDeleteItemsRequest{
		Dashboards: []datadogV2.DashboardListItemRequest{
			{
				Id:   ScreenboardDashboardID,
				Type: datadogV2.DASHBOARDTYPE_CUSTOM_SCREENBOARD,
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDashboardListsApi(apiClient)
	resp, r, err := api.DeleteDashboardListItems(ctx, DashboardListID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DashboardListsApi.DeleteDashboardListItems`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DashboardListsApi.DeleteDashboardListItems`:\n%s\n", responseContent)
}
```

##### 

```go
// Delete custom timeboard dashboard from an existing dashboard list returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "dashboard_list" in the system
	DashboardListID, _ := strconv.ParseInt(os.Getenv("DASHBOARD_LIST_ID"), 10, 64)

	// there is a valid "dashboard" in the system
	DashboardID := os.Getenv("DASHBOARD_ID")

	body := datadogV2.DashboardListDeleteItemsRequest{
		Dashboards: []datadogV2.DashboardListItemRequest{
			{
				Id:   DashboardID,
				Type: datadogV2.DASHBOARDTYPE_CUSTOM_TIMEBOARD,
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewDashboardListsApi(apiClient)
	resp, r, err := api.DeleteDashboardListItems(ctx, DashboardListID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DashboardListsApi.DeleteDashboardListItems`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DashboardListsApi.DeleteDashboardListItems`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
##### 

```java
// Delete custom screenboard dashboard from an existing dashboard list returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DashboardListsApi;
import com.datadog.api.client.v2.model.DashboardListDeleteItemsRequest;
import com.datadog.api.client.v2.model.DashboardListDeleteItemsResponse;
import com.datadog.api.client.v2.model.DashboardListItemRequest;
import com.datadog.api.client.v2.model.DashboardType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DashboardListsApi apiInstance = new DashboardListsApi(defaultClient);

    // there is a valid "dashboard_list" in the system
    Long DASHBOARD_LIST_ID = Long.parseLong(System.getenv("DASHBOARD_LIST_ID"));

    // there is a valid "screenboard_dashboard" in the system
    String SCREENBOARD_DASHBOARD_ID = System.getenv("SCREENBOARD_DASHBOARD_ID");

    DashboardListDeleteItemsRequest body =
        new DashboardListDeleteItemsRequest()
            .dashboards(
                Collections.singletonList(
                    new DashboardListItemRequest()
                        .id(SCREENBOARD_DASHBOARD_ID)
                        .type(DashboardType.CUSTOM_SCREENBOARD)));

    try {
      DashboardListDeleteItemsResponse result =
          apiInstance.deleteDashboardListItems(DASHBOARD_LIST_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardListsApi#deleteDashboardListItems");
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
// Delete custom timeboard dashboard from an existing dashboard list returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.DashboardListsApi;
import com.datadog.api.client.v2.model.DashboardListDeleteItemsRequest;
import com.datadog.api.client.v2.model.DashboardListDeleteItemsResponse;
import com.datadog.api.client.v2.model.DashboardListItemRequest;
import com.datadog.api.client.v2.model.DashboardType;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DashboardListsApi apiInstance = new DashboardListsApi(defaultClient);

    // there is a valid "dashboard_list" in the system
    Long DASHBOARD_LIST_ID = Long.parseLong(System.getenv("DASHBOARD_LIST_ID"));

    // there is a valid "dashboard" in the system
    String DASHBOARD_ID = System.getenv("DASHBOARD_ID");

    DashboardListDeleteItemsRequest body =
        new DashboardListDeleteItemsRequest()
            .dashboards(
                Collections.singletonList(
                    new DashboardListItemRequest()
                        .id(DASHBOARD_ID)
                        .type(DashboardType.CUSTOM_TIMEBOARD)));

    try {
      DashboardListDeleteItemsResponse result =
          apiInstance.deleteDashboardListItems(DASHBOARD_LIST_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardListsApi#deleteDashboardListItems");
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
Delete custom screenboard dashboard from an existing dashboard list returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v2.model.dashboard_list_delete_items_request import DashboardListDeleteItemsRequest
from datadog_api_client.v2.model.dashboard_list_item_request import DashboardListItemRequest
from datadog_api_client.v2.model.dashboard_type import DashboardType

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = environ["DASHBOARD_LIST_ID"]

# there is a valid "screenboard_dashboard" in the system
SCREENBOARD_DASHBOARD_ID = environ["SCREENBOARD_DASHBOARD_ID"]

body = DashboardListDeleteItemsRequest(
    dashboards=[
        DashboardListItemRequest(
            id=SCREENBOARD_DASHBOARD_ID,
            type=DashboardType.CUSTOM_SCREENBOARD,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.delete_dashboard_list_items(dashboard_list_id=int(DASHBOARD_LIST_ID), body=body)

    print(response)
```

##### 

```python
"""
Delete custom timeboard dashboard from an existing dashboard list returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v2.model.dashboard_list_delete_items_request import DashboardListDeleteItemsRequest
from datadog_api_client.v2.model.dashboard_list_item_request import DashboardListItemRequest
from datadog_api_client.v2.model.dashboard_type import DashboardType

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = environ["DASHBOARD_LIST_ID"]

# there is a valid "dashboard" in the system
DASHBOARD_ID = environ["DASHBOARD_ID"]

body = DashboardListDeleteItemsRequest(
    dashboards=[
        DashboardListItemRequest(
            id=DASHBOARD_ID,
            type=DashboardType.CUSTOM_TIMEBOARD,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.delete_dashboard_list_items(dashboard_list_id=int(DASHBOARD_LIST_ID), body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
##### 

```ruby
# Delete custom screenboard dashboard from an existing dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]

# there is a valid "screenboard_dashboard" in the system
SCREENBOARD_DASHBOARD_ID = ENV["SCREENBOARD_DASHBOARD_ID"]

body = DatadogAPIClient::V2::DashboardListDeleteItemsRequest.new({
  dashboards: [
    DatadogAPIClient::V2::DashboardListItemRequest.new({
      id: SCREENBOARD_DASHBOARD_ID,
      type: DatadogAPIClient::V2::DashboardType::CUSTOM_SCREENBOARD,
    }),
  ],
})
p api_instance.delete_dashboard_list_items(DASHBOARD_LIST_ID.to_i, body)
```

##### 

```ruby
# Delete custom timeboard dashboard from an existing dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]

# there is a valid "dashboard" in the system
DASHBOARD_ID = ENV["DASHBOARD_ID"]

body = DatadogAPIClient::V2::DashboardListDeleteItemsRequest.new({
  dashboards: [
    DatadogAPIClient::V2::DashboardListItemRequest.new({
      id: DASHBOARD_ID,
      type: DatadogAPIClient::V2::DashboardType::CUSTOM_TIMEBOARD,
    }),
  ],
})
p api_instance.delete_dashboard_list_items(DASHBOARD_LIST_ID.to_i, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
##### 

```rust
// Delete custom screenboard dashboard from an existing dashboard list returns
// "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dashboard_lists::DashboardListsAPI;
use datadog_api_client::datadogV2::model::DashboardListDeleteItemsRequest;
use datadog_api_client::datadogV2::model::DashboardListItemRequest;
use datadog_api_client::datadogV2::model::DashboardType;

#[tokio::main]
async fn main() {
    // there is a valid "dashboard_list" in the system
    let dashboard_list_id: i64 = std::env::var("DASHBOARD_LIST_ID").unwrap().parse().unwrap();

    // there is a valid "screenboard_dashboard" in the system
    let screenboard_dashboard_id = std::env::var("SCREENBOARD_DASHBOARD_ID").unwrap();
    let body =
        DashboardListDeleteItemsRequest::new().dashboards(vec![DashboardListItemRequest::new(
            screenboard_dashboard_id.clone(),
            DashboardType::CUSTOM_SCREENBOARD,
        )]);
    let configuration = datadog::Configuration::new();
    let api = DashboardListsAPI::with_config(configuration);
    let resp = api
        .delete_dashboard_list_items(dashboard_list_id.clone(), body)
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
// Delete custom timeboard dashboard from an existing dashboard list returns "OK"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_dashboard_lists::DashboardListsAPI;
use datadog_api_client::datadogV2::model::DashboardListDeleteItemsRequest;
use datadog_api_client::datadogV2::model::DashboardListItemRequest;
use datadog_api_client::datadogV2::model::DashboardType;

#[tokio::main]
async fn main() {
    // there is a valid "dashboard_list" in the system
    let dashboard_list_id: i64 = std::env::var("DASHBOARD_LIST_ID").unwrap().parse().unwrap();

    // there is a valid "dashboard" in the system
    let dashboard_id = std::env::var("DASHBOARD_ID").unwrap();
    let body =
        DashboardListDeleteItemsRequest::new().dashboards(vec![DashboardListItemRequest::new(
            dashboard_id.clone(),
            DashboardType::CUSTOM_TIMEBOARD,
        )]);
    let configuration = datadog::Configuration::new();
    let api = DashboardListsAPI::with_config(configuration);
    let resp = api
        .delete_dashboard_list_items(dashboard_list_id.clone(), body)
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
 * Delete custom screenboard dashboard from an existing dashboard list returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DashboardListsApi(configuration);

// there is a valid "dashboard_list" in the system
const DASHBOARD_LIST_ID = parseInt(process.env.DASHBOARD_LIST_ID as string);

// there is a valid "screenboard_dashboard" in the system
const SCREENBOARD_DASHBOARD_ID = process.env.SCREENBOARD_DASHBOARD_ID as string;

const params: v2.DashboardListsApiDeleteDashboardListItemsRequest = {
  body: {
    dashboards: [
      {
        id: SCREENBOARD_DASHBOARD_ID,
        type: "custom_screenboard",
      },
    ],
  },
  dashboardListId: DASHBOARD_LIST_ID,
};

apiInstance
  .deleteDashboardListItems(params)
  .then((data: v2.DashboardListDeleteItemsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Delete custom timeboard dashboard from an existing dashboard list returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.DashboardListsApi(configuration);

// there is a valid "dashboard_list" in the system
const DASHBOARD_LIST_ID = parseInt(process.env.DASHBOARD_LIST_ID as string);

// there is a valid "dashboard" in the system
const DASHBOARD_ID = process.env.DASHBOARD_ID as string;

const params: v2.DashboardListsApiDeleteDashboardListItemsRequest = {
  body: {
    dashboards: [
      {
        id: DASHBOARD_ID,
        type: "custom_timeboard",
      },
    ],
  },
  dashboardListId: DASHBOARD_LIST_ID,
};

apiInstance
  .deleteDashboardListItems(params)
  .then((data: v2.DashboardListDeleteItemsResponse) => {
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

## Update a dashboard list{% #update-a-dashboard-list %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/dashboard/lists/manual/{list_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/dashboard/lists/manual/{list_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |

### Overview

Update the name of a dashboard list. This endpoint requires the `dashboards_write` permission.

OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type    | Description                         |
| ------------------------- | ------- | ----------------------------------- |
| list_id [*required*] | integer | ID of the dashboard list to update. |

### Request

#### Body Data (required)

Update a dashboard list request body.

{% tab title="Model" %}

| Parent field | Field                  | Type      | Description                                          |
| ------------ | ---------------------- | --------- | ---------------------------------------------------- |
|              | author                 | object    | Object describing the creator of the shared element. |
| author       | email                  | string    | Email of the creator.                                |
| author       | handle                 | string    | Handle of the creator.                               |
| author       | name                   | string    | Name of the creator.                                 |
|              | created                | date-time | Date of creation of the dashboard list.              |
|              | dashboard_count        | int64     | The number of dashboards in the list.                |
|              | id                     | int64     | The ID of the dashboard list.                        |
|              | is_favorite            | boolean   | Whether or not the list is in the favorites.         |
|              | modified               | date-time | Date of last edition of the dashboard list.          |
|              | name [*required*] | string    | The name of the dashboard list.                      |
|              | type                   | string    | The type of dashboard list.                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "name": "updated Example-Dashboard-List"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Your Datadog Dashboards.

| Parent field | Field                  | Type      | Description                                          |
| ------------ | ---------------------- | --------- | ---------------------------------------------------- |
|              | author                 | object    | Object describing the creator of the shared element. |
| author       | email                  | string    | Email of the creator.                                |
| author       | handle                 | string    | Handle of the creator.                               |
| author       | name                   | string    | Name of the creator.                                 |
|              | created                | date-time | Date of creation of the dashboard list.              |
|              | dashboard_count        | int64     | The number of dashboards in the list.                |
|              | id                     | int64     | The ID of the dashboard list.                        |
|              | is_favorite            | boolean   | Whether or not the list is in the favorites.         |
|              | modified               | date-time | Date of last edition of the dashboard list.          |
|              | name [*required*] | string    | The name of the dashboard list.                      |
|              | type                   | string    | The type of dashboard list.                          |

{% /tab %}

{% tab title="Example" %}

```json
{
  "author": {
    "email": "string",
    "handle": "string",
    "name": "string"
  },
  "created": "2019-09-19T10:00:00.000Z",
  "dashboard_count": "integer",
  "id": "integer",
  "is_favorite": false,
  "modified": "2019-09-19T10:00:00.000Z",
  "name": "My Dashboard",
  "type": "manual_dashboard_list"
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
                          \# Path parametersexport list_id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/${list_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "updated Example-Dashboard-List"
}
EOF
                        
##### 

```go
// Update a dashboard list returns "OK" response

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
	// there is a valid "dashboard_list" in the system
	DashboardListID, _ := strconv.ParseInt(os.Getenv("DASHBOARD_LIST_ID"), 10, 64)

	body := datadogV1.DashboardList{
		Name: "updated Example-Dashboard-List",
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewDashboardListsApi(apiClient)
	resp, r, err := api.UpdateDashboardList(ctx, DashboardListID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DashboardListsApi.UpdateDashboardList`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DashboardListsApi.UpdateDashboardList`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Update a dashboard list returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DashboardListsApi;
import com.datadog.api.client.v1.model.DashboardList;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DashboardListsApi apiInstance = new DashboardListsApi(defaultClient);

    // there is a valid "dashboard_list" in the system
    Long DASHBOARD_LIST_ID = Long.parseLong(System.getenv("DASHBOARD_LIST_ID"));

    DashboardList body = new DashboardList().name("updated Example-Dashboard-List");

    try {
      DashboardList result = apiInstance.updateDashboardList(DASHBOARD_LIST_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardListsApi#updateDashboardList");
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
Update a dashboard list returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v1.model.dashboard_list import DashboardList

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = environ["DASHBOARD_LIST_ID"]

body = DashboardList(
    name="updated Example-Dashboard-List",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.update_dashboard_list(list_id=int(DASHBOARD_LIST_ID), body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Update a dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]

body = DatadogAPIClient::V1::DashboardList.new({
  name: "updated Example-Dashboard-List",
})
p api_instance.update_dashboard_list(DASHBOARD_LIST_ID.to_i, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Update a dashboard list returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_dashboard_lists::DashboardListsAPI;
use datadog_api_client::datadogV1::model::DashboardList;

#[tokio::main]
async fn main() {
    // there is a valid "dashboard_list" in the system
    let dashboard_list_id: i64 = std::env::var("DASHBOARD_LIST_ID").unwrap().parse().unwrap();
    let body = DashboardList::new("updated Example-Dashboard-List".to_string());
    let configuration = datadog::Configuration::new();
    let api = DashboardListsAPI::with_config(configuration);
    let resp = api
        .update_dashboard_list(dashboard_list_id.clone(), body)
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
 * Update a dashboard list returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DashboardListsApi(configuration);

// there is a valid "dashboard_list" in the system
const DASHBOARD_LIST_ID = parseInt(process.env.DASHBOARD_LIST_ID as string);

const params: v1.DashboardListsApiUpdateDashboardListRequest = {
  body: {
    name: "updated Example-Dashboard-List",
  },
  listId: DASHBOARD_LIST_ID,
};

apiInstance
  .updateDashboardList(params)
  .then((data: v1.DashboardList) => {
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

## Delete a dashboard list{% #delete-a-dashboard-list %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                                 |
| ----------------- | ---------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/dashboard/lists/manual/{list_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/dashboard/lists/manual/{list_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/{list_id} |

### Overview

Delete a dashboard list. This endpoint requires the `dashboards_write` permission.

OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.



### Arguments

#### Path Parameters

| Name                      | Type    | Description                         |
| ------------------------- | ------- | ----------------------------------- |
| list_id [*required*] | integer | ID of the dashboard list to delete. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Deleted dashboard details.

| Field                     | Type  | Description                       |
| ------------------------- | ----- | --------------------------------- |
| deleted_dashboard_list_id | int64 | ID of the deleted dashboard list. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "deleted_dashboard_list_id": "integer"
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
                  \# Path parametersexport list_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/${list_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Delete a dashboard list returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = environ["DASHBOARD_LIST_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.delete_dashboard_list(
        list_id=int(DASHBOARD_LIST_ID),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Delete a dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]
p api_instance.delete_dashboard_list(DASHBOARD_LIST_ID.to_i)
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

result = dog.delete_dashboard_list(4741)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Delete a dashboard list returns "OK" response

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
	// there is a valid "dashboard_list" in the system
	DashboardListID, _ := strconv.ParseInt(os.Getenv("DASHBOARD_LIST_ID"), 10, 64)

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewDashboardListsApi(apiClient)
	resp, r, err := api.DeleteDashboardList(ctx, DashboardListID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DashboardListsApi.DeleteDashboardList`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `DashboardListsApi.DeleteDashboardList`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Delete a dashboard list returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.DashboardListsApi;
import com.datadog.api.client.v1.model.DashboardListDeleteResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    DashboardListsApi apiInstance = new DashboardListsApi(defaultClient);

    // there is a valid "dashboard_list" in the system
    Long DASHBOARD_LIST_ID = Long.parseLong(System.getenv("DASHBOARD_LIST_ID"));

    try {
      DashboardListDeleteResponse result = apiInstance.deleteDashboardList(DASHBOARD_LIST_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardListsApi#deleteDashboardList");
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

api.DashboardList.delete(4741)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
##### 

```rust
// Delete a dashboard list returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_dashboard_lists::DashboardListsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "dashboard_list" in the system
    let dashboard_list_id: i64 = std::env::var("DASHBOARD_LIST_ID").unwrap().parse().unwrap();
    let configuration = datadog::Configuration::new();
    let api = DashboardListsAPI::with_config(configuration);
    let resp = api.delete_dashboard_list(dashboard_list_id.clone()).await;
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
 * Delete a dashboard list returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.DashboardListsApi(configuration);

// there is a valid "dashboard_list" in the system
const DASHBOARD_LIST_ID = parseInt(process.env.DASHBOARD_LIST_ID as string);

const params: v1.DashboardListsApiDeleteDashboardListRequest = {
  listId: DASHBOARD_LIST_ID,
};

apiInstance
  .deleteDashboardList(params)
  .then((data: v1.DashboardListDeleteResponse) => {
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
