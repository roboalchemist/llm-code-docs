# Source: https://docs.datadoghq.com/api/latest/dashboard-lists

# Dashboard Lists
Interact with your dashboard lists through the API to organize, find, and share all of your dashboards with your team and organization.
## [Get all dashboard lists](https://docs.datadoghq.com/api/latest/dashboard-lists/#get-all-dashboard-lists)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/dashboard-lists/#get-all-dashboard-lists-v1)


GET https://api.ap1.datadoghq.com/api/v1/dashboard/lists/manualhttps://api.ap2.datadoghq.com/api/v1/dashboard/lists/manualhttps://api.datadoghq.eu/api/v1/dashboard/lists/manualhttps://api.ddog-gov.com/api/v1/dashboard/lists/manualhttps://api.datadoghq.com/api/v1/dashboard/lists/manualhttps://api.us3.datadoghq.com/api/v1/dashboard/lists/manualhttps://api.us5.datadoghq.com/api/v1/dashboard/lists/manual
### Overview
Fetch all of your existing dashboard list definitions. This endpoint requires the `dashboards_read` permission.
OAuth apps require the `dashboards_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/dashboard-lists/#ListDashboardLists-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/dashboard-lists/#ListDashboardLists-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/dashboard-lists/#ListDashboardLists-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Information on your dashboard lists.
Field
Type
Description
dashboard_lists
[object]
List of all your dashboard lists.
author
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
created
date-time
Date of creation of the dashboard list.
dashboard_count
int64
The number of dashboards in the list.
id
int64
The ID of the dashboard list.
is_favorite
boolean
Whether or not the list is in the favorites.
modified
date-time
Date of last edition of the dashboard list.
name [_required_]
string
The name of the dashboard list.
type
string
The type of dashboard list.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python-legacy)


#####  Get all dashboard lists
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all dashboard lists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all dashboard lists
```
# Get all dashboard lists returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DashboardListsAPI.new
p api_instance.list_dashboard_lists()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all dashboard lists
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

result = dog.get_all_dashboard_lists()
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all dashboard lists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all dashboard lists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get all dashboard lists
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.DashboardList.get_all()
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get all dashboard lists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get all dashboard lists
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get items of a Dashboard List](https://docs.datadoghq.com/api/latest/dashboard-lists/#get-items-of-a-dashboard-list)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dashboard-lists/#get-items-of-a-dashboard-list-v2)


GET https://api.ap1.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.ap2.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.datadoghq.eu/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.ddog-gov.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.us3.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards
### Overview
Fetch the dashboard list’s dashboard definitions. This endpoint requires the `dashboards_read` permission.
OAuth apps require the `dashboards_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
dashboard_list_id [_required_]
integer
ID of the dashboard list to get items from.
### Response
  * [200](https://docs.datadoghq.com/api/latest/dashboard-lists/#GetDashboardListItems-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/dashboard-lists/#GetDashboardListItems-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/dashboard-lists/#GetDashboardListItems-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/dashboard-lists/#GetDashboardListItems-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Dashboards within a list.
Field
Type
Description
dashboards [_required_]
[object]
List of dashboards in the dashboard list.
author
object
Creator of the object.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
created
date-time
Date of creation of the dashboard.
icon
string
URL to the icon of the dashboard.
id [_required_]
string
ID of the dashboard.
integration_id
string
The short name of the integration.
is_favorite
boolean
Whether or not the dashboard is in the favorites.
is_read_only
boolean
Whether or not the dashboard is read only.
is_shared
boolean
Whether the dashboard is publicly shared or not.
modified
date-time
Date of last edition of the dashboard.
popularity
int32
Popularity of the dashboard.
tags
[string]
List of team names representing ownership of a dashboard.
title
string
Title of the dashboard.
type [_required_]
enum
The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard`
url
string
URL path to the dashboard.
total
int64
Number of dashboards in the dashboard list.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python-legacy)


#####  Get items of a Dashboard List
Copy
```
                  # Path parameters  
export dashboard_list_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get items of a Dashboard List
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get items of a Dashboard List
```
# Get items of a Dashboard List returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]
p api_instance.get_dashboard_list_items(DASHBOARD_LIST_ID.to_i)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get items of a Dashboard List
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

result = dog.v2.get_items_of_dashboard_list(4741)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get items of a Dashboard List
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get items of a Dashboard List
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get items of a Dashboard List
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.DashboardList.v2.get_items(4741)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get items of a Dashboard List
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get items of a Dashboard List
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Add Items to a Dashboard List](https://docs.datadoghq.com/api/latest/dashboard-lists/#add-items-to-a-dashboard-list)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dashboard-lists/#add-items-to-a-dashboard-list-v2)


POST https://api.ap1.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.ap2.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.datadoghq.eu/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.ddog-gov.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.us3.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards
### Overview
Add dashboards to an existing dashboard list.
### Arguments
#### Path Parameters
Name
Type
Description
dashboard_list_id [_required_]
integer
ID of the dashboard list to add items to.
### Request
#### Body Data (required)
Dashboards to add to the dashboard list.
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Field
Type
Description
dashboards
[object]
List of dashboards to add the dashboard list.
id [_required_]
string
ID of the dashboard.
type [_required_]
enum
The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard`
#####  Add custom screenboard dashboard to an existing dashboard list returns "OK" response
```
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_screenboard"
    }
  ]
}
```

Copy
#####  Add custom timeboard dashboard to an existing dashboard list returns "OK" response
```
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_timeboard"
    }
  ]
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/dashboard-lists/#CreateDashboardListItems-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/dashboard-lists/#CreateDashboardListItems-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dashboard-lists/#CreateDashboardListItems-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/dashboard-lists/#CreateDashboardListItems-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/dashboard-lists/#CreateDashboardListItems-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Response containing a list of added dashboards.
Field
Type
Description
added_dashboards_to_list
[object]
List of dashboards added to the dashboard list.
id [_required_]
string
ID of the dashboard.
type [_required_]
enum
The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard`
```
{
  "added_dashboards_to_list": [
    {
      "id": "q5j-nti-fv6",
      "type": "host_timeboard"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python-legacy)


#####  Add custom screenboard dashboard to an existing dashboard list returns "OK" response
Copy
```
                          # Path parameters  
export dashboard_list_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
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

                        
```

#####  Add custom timeboard dashboard to an existing dashboard list returns "OK" response
Copy
```
                          # Path parameters  
export dashboard_list_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
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

                        
```

#####  Add custom screenboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#####  Add custom timeboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Add custom screenboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#####  Add custom timeboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Add custom screenboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#####  Add custom timeboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Add custom screenboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#####  Add custom timeboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Add custom screenboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#####  Add custom timeboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Add custom screenboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#####  Add custom timeboard dashboard to an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Create a dashboard list](https://docs.datadoghq.com/api/latest/dashboard-lists/#create-a-dashboard-list)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/dashboard-lists/#create-a-dashboard-list-v1)


POST https://api.ap1.datadoghq.com/api/v1/dashboard/lists/manualhttps://api.ap2.datadoghq.com/api/v1/dashboard/lists/manualhttps://api.datadoghq.eu/api/v1/dashboard/lists/manualhttps://api.ddog-gov.com/api/v1/dashboard/lists/manualhttps://api.datadoghq.com/api/v1/dashboard/lists/manualhttps://api.us3.datadoghq.com/api/v1/dashboard/lists/manualhttps://api.us5.datadoghq.com/api/v1/dashboard/lists/manual
### Overview
Create an empty dashboard list. This endpoint requires the `dashboards_write` permission.
OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.
### Request
#### Body Data (required)
Create a dashboard list request body.
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Field
Type
Description
author
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
created
date-time
Date of creation of the dashboard list.
dashboard_count
int64
The number of dashboards in the list.
id
int64
The ID of the dashboard list.
is_favorite
boolean
Whether or not the list is in the favorites.
modified
date-time
Date of last edition of the dashboard list.
name [_required_]
string
The name of the dashboard list.
type
string
The type of dashboard list.
```
{
  "name": "Example-Dashboard-List"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/dashboard-lists/#CreateDashboardList-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/dashboard-lists/#CreateDashboardList-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/dashboard-lists/#CreateDashboardList-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/dashboard-lists/#CreateDashboardList-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Your Datadog Dashboards.
Field
Type
Description
author
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
created
date-time
Date of creation of the dashboard list.
dashboard_count
int64
The number of dashboards in the list.
id
int64
The ID of the dashboard list.
is_favorite
boolean
Whether or not the list is in the favorites.
modified
date-time
Date of last edition of the dashboard list.
name [_required_]
string
The name of the dashboard list.
type
string
The type of dashboard list.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=typescript)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python-legacy)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby-legacy)


#####  Create a dashboard list returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "Example-Dashboard-List"
}
EOF  

                        
```

#####  Create a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Create a dashboard list returns "OK" response
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

name = 'My Dashboard List'

api.DashboardList.create(name=name)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Create a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a dashboard list returns "OK" response
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

name = 'My Dashboard List'

result = dog.create_dashboard_list(name)
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a dashboard list returns "OK" response
```
# Create a dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DashboardListsAPI.new

body = DatadogAPIClient::V1::DashboardList.new({
  name: "Example-Dashboard-List",
})
p api_instance.create_dashboard_list(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Create a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a dashboard list](https://docs.datadoghq.com/api/latest/dashboard-lists/#get-a-dashboard-list)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/dashboard-lists/#get-a-dashboard-list-v1)


GET https://api.ap1.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.ap2.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.datadoghq.eu/api/v1/dashboard/lists/manual/{list_id}https://api.ddog-gov.com/api/v1/dashboard/lists/manual/{list_id}https://api.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.us3.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}
### Overview
Fetch an existing dashboard list’s definition. This endpoint requires the `dashboards_read` permission.
OAuth apps require the `dashboards_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
list_id [_required_]
integer
ID of the dashboard list to fetch.
### Response
  * [200](https://docs.datadoghq.com/api/latest/dashboard-lists/#GetDashboardList-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/dashboard-lists/#GetDashboardList-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/dashboard-lists/#GetDashboardList-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/dashboard-lists/#GetDashboardList-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Your Datadog Dashboards.
Field
Type
Description
author
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
created
date-time
Date of creation of the dashboard list.
dashboard_count
int64
The number of dashboards in the list.
id
int64
The ID of the dashboard list.
is_favorite
boolean
Whether or not the list is in the favorites.
modified
date-time
Date of last edition of the dashboard list.
name [_required_]
string
The name of the dashboard list.
type
string
The type of dashboard list.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python-legacy)


#####  Get a dashboard list
Copy
```
                  # Path parameters  
export list_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/${list_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a dashboard list
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a dashboard list
```
# Get a dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]
p api_instance.get_dashboard_list(DASHBOARD_LIST_ID.to_i)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a dashboard list
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

result = dog.get_dashboard_list(4741)
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a dashboard list
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a dashboard list
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Get a dashboard list
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.DashboardList.get(4741)
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get a dashboard list
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Get a dashboard list
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Update items of a dashboard list](https://docs.datadoghq.com/api/latest/dashboard-lists/#update-items-of-a-dashboard-list)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dashboard-lists/#update-items-of-a-dashboard-list-v2)


PUT https://api.ap1.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.ap2.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.datadoghq.eu/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.ddog-gov.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.us3.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards
### Overview
Update dashboards of an existing dashboard list.
### Arguments
#### Path Parameters
Name
Type
Description
dashboard_list_id [_required_]
integer
ID of the dashboard list to update items from.
### Request
#### Body Data (required)
New dashboards of the dashboard list.
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Field
Type
Description
dashboards
[object]
List of dashboards to update the dashboard list to.
id [_required_]
string
ID of the dashboard.
type [_required_]
enum
The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard`
```
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_screenboard"
    }
  ]
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/dashboard-lists/#UpdateDashboardListItems-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/dashboard-lists/#UpdateDashboardListItems-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dashboard-lists/#UpdateDashboardListItems-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/dashboard-lists/#UpdateDashboardListItems-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/dashboard-lists/#UpdateDashboardListItems-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Response containing a list of updated dashboards.
Field
Type
Description
dashboards
[object]
List of dashboards in the dashboard list.
id [_required_]
string
ID of the dashboard.
type [_required_]
enum
The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard`
```
{
  "dashboards": [
    {
      "id": "q5j-nti-fv6",
      "type": "host_timeboard"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=typescript)


#####  Update items of a dashboard list returns "OK" response
Copy
```
                          # Path parameters  
export dashboard_list_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
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

                        
```

#####  Update items of a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update items of a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update items of a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update items of a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update items of a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update items of a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete items from a dashboard list](https://docs.datadoghq.com/api/latest/dashboard-lists/#delete-items-from-a-dashboard-list)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/dashboard-lists/#delete-items-from-a-dashboard-list-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.ap2.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.datadoghq.eu/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.ddog-gov.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.us3.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboardshttps://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards
### Overview
Delete dashboards from an existing dashboard list.
### Arguments
#### Path Parameters
Name
Type
Description
dashboard_list_id [_required_]
integer
ID of the dashboard list to delete items from.
### Request
#### Body Data (required)
Dashboards to delete from the dashboard list.
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Field
Type
Description
dashboards
[object]
List of dashboards to delete from the dashboard list.
id [_required_]
string
ID of the dashboard.
type [_required_]
enum
The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard`
#####  Delete custom screenboard dashboard from an existing dashboard list returns "OK" response
```
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_screenboard"
    }
  ]
}
```

Copy
#####  Delete custom timeboard dashboard from an existing dashboard list returns "OK" response
```
{
  "dashboards": [
    {
      "id": "123-abc-456",
      "type": "custom_timeboard"
    }
  ]
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/dashboard-lists/#DeleteDashboardListItems-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/dashboard-lists/#DeleteDashboardListItems-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/dashboard-lists/#DeleteDashboardListItems-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/dashboard-lists/#DeleteDashboardListItems-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/dashboard-lists/#DeleteDashboardListItems-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Response containing a list of deleted dashboards.
Field
Type
Description
deleted_dashboards_from_list
[object]
List of dashboards deleted from the dashboard list.
id [_required_]
string
ID of the dashboard.
type [_required_]
enum
The type of the dashboard. Allowed enum values: `custom_timeboard,custom_screenboard,integration_screenboard,integration_timeboard,host_timeboard`
```
{
  "deleted_dashboards_from_list": [
    {
      "id": "q5j-nti-fv6",
      "type": "host_timeboard"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python-legacy)


#####  Delete custom screenboard dashboard from an existing dashboard list returns "OK" response
Copy
```
                          # Path parameters  
export dashboard_list_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
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

                        
```

#####  Delete custom timeboard dashboard from an existing dashboard list returns "OK" response
Copy
```
                          # Path parameters  
export dashboard_list_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/dashboard/lists/manual/${dashboard_list_id}/dashboards" \
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

                        
```

#####  Delete custom screenboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#####  Delete custom timeboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete custom screenboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#####  Delete custom timeboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete custom screenboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#####  Delete custom timeboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete custom screenboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#####  Delete custom timeboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete custom screenboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#####  Delete custom timeboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete custom screenboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#####  Delete custom timeboard dashboard from an existing dashboard list returns "OK" response 
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update a dashboard list](https://docs.datadoghq.com/api/latest/dashboard-lists/#update-a-dashboard-list)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/dashboard-lists/#update-a-dashboard-list-v1)


PUT https://api.ap1.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.ap2.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.datadoghq.eu/api/v1/dashboard/lists/manual/{list_id}https://api.ddog-gov.com/api/v1/dashboard/lists/manual/{list_id}https://api.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.us3.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}
### Overview
Update the name of a dashboard list. This endpoint requires the `dashboards_write` permission.
OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
list_id [_required_]
integer
ID of the dashboard list to update.
### Request
#### Body Data (required)
Update a dashboard list request body.
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Field
Type
Description
author
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
created
date-time
Date of creation of the dashboard list.
dashboard_count
int64
The number of dashboards in the list.
id
int64
The ID of the dashboard list.
is_favorite
boolean
Whether or not the list is in the favorites.
modified
date-time
Date of last edition of the dashboard list.
name [_required_]
string
The name of the dashboard list.
type
string
The type of dashboard list.
```
{
  "name": "updated Example-Dashboard-List"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/dashboard-lists/#UpdateDashboardList-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/dashboard-lists/#UpdateDashboardList-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/dashboard-lists/#UpdateDashboardList-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/dashboard-lists/#UpdateDashboardList-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/dashboard-lists/#UpdateDashboardList-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Your Datadog Dashboards.
Field
Type
Description
author
object
Object describing the creator of the shared element.
email
string
Email of the creator.
handle
string
Handle of the creator.
name
string
Name of the creator.
created
date-time
Date of creation of the dashboard list.
dashboard_count
int64
The number of dashboards in the list.
id
int64
The ID of the dashboard list.
is_favorite
boolean
Whether or not the list is in the favorites.
modified
date-time
Date of last edition of the dashboard list.
name [_required_]
string
The name of the dashboard list.
type
string
The type of dashboard list.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=typescript)


#####  Update a dashboard list returns "OK" response
Copy
```
                          # Path parameters  
export list_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/${list_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "updated Example-Dashboard-List"
}
EOF  

                        
```

#####  Update a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Update a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Update a dashboard list returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Delete a dashboard list](https://docs.datadoghq.com/api/latest/dashboard-lists/#delete-a-dashboard-list)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/dashboard-lists/#delete-a-dashboard-list-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.ap2.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.datadoghq.eu/api/v1/dashboard/lists/manual/{list_id}https://api.ddog-gov.com/api/v1/dashboard/lists/manual/{list_id}https://api.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.us3.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/{list_id}
### Overview
Delete a dashboard list. This endpoint requires the `dashboards_write` permission.
OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#dashboard-lists) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
list_id [_required_]
integer
ID of the dashboard list to delete.
### Response
  * [200](https://docs.datadoghq.com/api/latest/dashboard-lists/#DeleteDashboardList-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/dashboard-lists/#DeleteDashboardList-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/dashboard-lists/#DeleteDashboardList-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/dashboard-lists/#DeleteDashboardList-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Deleted dashboard details.
Expand All
Field
Type
Description
deleted_dashboard_list_id
int64
ID of the deleted dashboard list.
```
{
  "deleted_dashboard_list_id": "integer"
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/dashboard-lists/)
  * [Example](https://docs.datadoghq.com/api/latest/dashboard-lists/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/dashboard-lists/?code-lang=python-legacy)


#####  Delete a dashboard list
Copy
```
                  # Path parameters  
export list_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/dashboard/lists/manual/${list_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a dashboard list
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a dashboard list
```
# Delete a dashboard list returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::DashboardListsAPI.new

# there is a valid "dashboard_list" in the system
DASHBOARD_LIST_ID = ENV["DASHBOARD_LIST_ID"]
p api_instance.delete_dashboard_list(DASHBOARD_LIST_ID.to_i)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a dashboard list
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

result = dog.delete_dashboard_list(4741)
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a dashboard list
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete a dashboard list
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"


```

#####  Delete a dashboard list
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.DashboardList.delete(4741)
```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Delete a dashboard list
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run


```

#####  Delete a dashboard list
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=dff4be51-f862-4abb-b14c-0ef8615697c6&bo=1&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Dashboard%20Lists&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdashboard-lists%2F&r=&evt=pageLoad&sv=2&cdb=AQAA&rn=261057)
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=a0ee916e-9018-443c-80a7-14dda7823f52&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=4da4c407-18d9-4b01-9e64-abef1cd313f2&pt=Dashboard%20Lists&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdashboard-lists%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=a0ee916e-9018-443c-80a7-14dda7823f52&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=4da4c407-18d9-4b01-9e64-abef1cd313f2&pt=Dashboard%20Lists&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fdashboard-lists%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
