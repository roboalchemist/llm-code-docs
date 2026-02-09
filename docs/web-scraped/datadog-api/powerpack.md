# Source: https://docs.datadoghq.com/api/latest/powerpack

# Powerpack
The Powerpack endpoints allow you to:
  * Get a Powerpack
  * Create a Powerpack
  * Delete a Powerpack
  * Get a list of all Powerpacks


The Patch and Delete API methods can only be performed on a Powerpack by a user who has the powerpack create permission for that specific Powerpack.
Read [Scale Graphing Expertise with Powerpacks](https://docs.datadoghq.com/dashboards/guide/powerpacks-best-practices/) for more information.
## [Get all powerpacks](https://docs.datadoghq.com/api/latest/powerpack/#get-all-powerpacks)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/powerpack/#get-all-powerpacks-v2)


GET https://api.ap1.datadoghq.com/api/v2/powerpackshttps://api.ap2.datadoghq.com/api/v2/powerpackshttps://api.datadoghq.eu/api/v2/powerpackshttps://api.ddog-gov.com/api/v2/powerpackshttps://api.datadoghq.com/api/v2/powerpackshttps://api.us3.datadoghq.com/api/v2/powerpackshttps://api.us5.datadoghq.com/api/v2/powerpacks
### Overview
Get a list of all powerpacks. This endpoint requires the `dashboards_read` permission.
OAuth apps require the `dashboards_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#powerpack) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
page[limit]
integer
Maximum number of powerpacks in the response.
page[offset]
integer
Specific offset to use as the beginning of the returned page.
### Response
  * [200](https://docs.datadoghq.com/api/latest/powerpack/#ListPowerpacks-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/powerpack/#ListPowerpacks-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


Response object which includes all powerpack configurations.
Field
Type
Description
data
[object]
List of powerpack definitions.
attributes
object
Powerpack attribute object.
description
string
Description of this powerpack.
group_widget [_required_]
object
Powerpack group widget definition object.
definition [_required_]
object
Powerpack group widget object.
layout_type [_required_]
string
Layout type of widgets.
show_title
boolean
Boolean indicating whether powerpack group title should be visible or not.
title
string
Name for the group widget.
type [_required_]
string
Type of widget, must be group.
widgets [_required_]
[object]
Widgets inside the powerpack.
definition [_required_]
object
Information about widget.
layout
object
Powerpack inner widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
layout
object
Powerpack group widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert`
name [_required_]
string
Name of the powerpack.
tags
[string]
List of tags to identify this powerpack.
template_variables
[object]
List of template variables for this powerpack.
available_values
[string]
The list of values that the template variable drop-down is limited to.
defaults
[string]
One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.
name [_required_]
string
The name of the variable.
prefix
string
The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.
id
string
ID of the powerpack.
relationships
object
Powerpack relationship object.
author
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type
string
Type of widget, must be powerpack.
included
[object]
Array of objects related to the users.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
object
Relationship to users.
data [_required_]
[object]
Relationships to user objects.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
links
object
Links attributes.
first
string
Link to last page.
last
string
Link to first page.
next
string
Link for the next set of results.
prev
string
Link for the previous set of results.
self
string
Link to current page.
meta
object
Powerpack response metadata.
pagination
object
Powerpack response pagination metadata.
first_offset
int64
The first offset.
last_offset
int64
The last offset.
limit
int64
Pagination limit.
next_offset
int64
The next offset.
offset
int64
The offset.
prev_offset
int64
The previous offset.
total
int64
Total results.
type
string
Offset type.
```
{
  "data": [
    {
      "attributes": {
        "description": "Powerpack for ABC",
        "group_widget": {
          "definition": {
            "layout_type": "ordered",
            "show_title": true,
            "title": "Sample Powerpack",
            "type": "group",
            "widgets": [
              {
                "definition": {
                  "definition": {
                    "content": "example",
                    "type": "note"
                  }
                },
                "layout": {
                  "height": 0,
                  "width": 0,
                  "x": 0,
                  "y": 0
                }
              }
            ]
          },
          "layout": {
            "height": 0,
            "width": 0,
            "x": 0,
            "y": 0
          },
          "live_span": "5m"
        },
        "name": "Sample Powerpack",
        "tags": [
          "tag:foo1"
        ],
        "template_variables": [
          {
            "available_values": [
              "my-host",
              "host1",
              "host2"
            ],
            "defaults": [
              "*"
            ],
            "name": "datacenter",
            "prefix": "host"
          }
        ]
      },
      "id": "string",
      "relationships": {
        "author": {
          "data": {
            "id": "00000000-0000-0000-2345-000000000000",
            "type": "users"
          }
        }
      },
      "type": "powerpack"
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
  "links": {
    "first": "string",
    "last": "https://app.datadoghq.com/api/v2/powerpacks?page[offset]=0\u0026page[limit]=25",
    "next": "https://app.datadoghq.com/api/v2/powerpacks?page[offset]=25\u0026page[limit]=25",
    "prev": "string",
    "self": "https://app.datadoghq.com/api/v2/powerpacks"
  },
  "meta": {
    "pagination": {
      "first_offset": "integer",
      "last_offset": "integer",
      "limit": "integer",
      "next_offset": "integer",
      "offset": "integer",
      "prev_offset": "integer",
      "total": "integer",
      "type": "string"
    }
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=typescript)


#####  Get all powerpacks
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/powerpacks" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all powerpacks
```
"""
Get all powerpacks returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.powerpack_api import PowerpackApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PowerpackApi(api_client)
    response = api_instance.list_powerpacks(
        page_limit=1000,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all powerpacks
```
# Get all powerpacks returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::PowerpackAPI.new
opts = {
  page_limit: 1000,
}
p api_instance.list_powerpacks(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all powerpacks
```
// Get all powerpacks returns "OK" response

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
	api := datadogV2.NewPowerpackApi(apiClient)
	resp, r, err := api.ListPowerpacks(ctx, *datadogV2.NewListPowerpacksOptionalParameters().WithPageLimit(1000))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PowerpackApi.ListPowerpacks`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `PowerpackApi.ListPowerpacks`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all powerpacks
```
// Get all powerpacks returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.PowerpackApi;
import com.datadog.api.client.v2.api.PowerpackApi.ListPowerpacksOptionalParameters;
import com.datadog.api.client.v2.model.ListPowerpacksResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    PowerpackApi apiInstance = new PowerpackApi(defaultClient);

    try {
      ListPowerpacksResponse result =
          apiInstance.listPowerpacks(new ListPowerpacksOptionalParameters().pageLimit(1000L));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PowerpackApi#listPowerpacks");
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

#####  Get all powerpacks
```
// Get all powerpacks returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_powerpack::ListPowerpacksOptionalParams;
use datadog_api_client::datadogV2::api_powerpack::PowerpackAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = PowerpackAPI::with_config(configuration);
    let resp = api
        .list_powerpacks(ListPowerpacksOptionalParams::default().page_limit(1000))
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

#####  Get all powerpacks
```
/**
 * Get all powerpacks returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.PowerpackApi(configuration);

const params: v2.PowerpackApiListPowerpacksRequest = {
  pageLimit: 1000,
};

apiInstance
  .listPowerpacks(params)
  .then((data: v2.ListPowerpacksResponse) => {
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
## [Create a new powerpack](https://docs.datadoghq.com/api/latest/powerpack/#create-a-new-powerpack)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/powerpack/#create-a-new-powerpack-v2)


POST https://api.ap1.datadoghq.com/api/v2/powerpackshttps://api.ap2.datadoghq.com/api/v2/powerpackshttps://api.datadoghq.eu/api/v2/powerpackshttps://api.ddog-gov.com/api/v2/powerpackshttps://api.datadoghq.com/api/v2/powerpackshttps://api.us3.datadoghq.com/api/v2/powerpackshttps://api.us5.datadoghq.com/api/v2/powerpacks
### Overview
Create a powerpack. This endpoint requires the `dashboards_write` permission.
OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#powerpack) to access this endpoint.
### Request
#### Body Data (required)
Create a powerpack request body.
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


Field
Type
Description
data
object
Powerpack data object.
attributes
object
Powerpack attribute object.
description
string
Description of this powerpack.
group_widget [_required_]
object
Powerpack group widget definition object.
definition [_required_]
object
Powerpack group widget object.
layout_type [_required_]
string
Layout type of widgets.
show_title
boolean
Boolean indicating whether powerpack group title should be visible or not.
title
string
Name for the group widget.
type [_required_]
string
Type of widget, must be group.
widgets [_required_]
[object]
Widgets inside the powerpack.
definition [_required_]
object
Information about widget.
layout
object
Powerpack inner widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
layout
object
Powerpack group widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert`
name [_required_]
string
Name of the powerpack.
tags
[string]
List of tags to identify this powerpack.
template_variables
[object]
List of template variables for this powerpack.
available_values
[string]
The list of values that the template variable drop-down is limited to.
defaults
[string]
One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.
name [_required_]
string
The name of the variable.
prefix
string
The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.
id
string
ID of the powerpack.
relationships
object
Powerpack relationship object.
author
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type
string
Type of widget, must be powerpack.
```
{
  "data": {
    "attributes": {
      "description": "Sample powerpack",
      "group_widget": {
        "definition": {
          "layout_type": "ordered",
          "show_title": true,
          "title": "Sample Powerpack",
          "type": "group",
          "widgets": [
            {
              "definition": {
                "content": "test",
                "type": "note"
              }
            }
          ]
        },
        "layout": {
          "height": 3,
          "width": 12,
          "x": 0,
          "y": 0
        },
        "live_span": "1h"
      },
      "name": "Example-Powerpack",
      "tags": [
        "tag:sample"
      ],
      "template_variables": [
        {
          "defaults": [
            "*"
          ],
          "name": "sample"
        }
      ]
    },
    "type": "powerpack"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/powerpack/#CreatePowerpack-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/powerpack/#CreatePowerpack-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/powerpack/#CreatePowerpack-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


Response object which includes a single powerpack configuration.
Field
Type
Description
data
object
Powerpack data object.
attributes
object
Powerpack attribute object.
description
string
Description of this powerpack.
group_widget [_required_]
object
Powerpack group widget definition object.
definition [_required_]
object
Powerpack group widget object.
layout_type [_required_]
string
Layout type of widgets.
show_title
boolean
Boolean indicating whether powerpack group title should be visible or not.
title
string
Name for the group widget.
type [_required_]
string
Type of widget, must be group.
widgets [_required_]
[object]
Widgets inside the powerpack.
definition [_required_]
object
Information about widget.
layout
object
Powerpack inner widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
layout
object
Powerpack group widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert`
name [_required_]
string
Name of the powerpack.
tags
[string]
List of tags to identify this powerpack.
template_variables
[object]
List of template variables for this powerpack.
available_values
[string]
The list of values that the template variable drop-down is limited to.
defaults
[string]
One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.
name [_required_]
string
The name of the variable.
prefix
string
The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.
id
string
ID of the powerpack.
relationships
object
Powerpack relationship object.
author
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type
string
Type of widget, must be powerpack.
included
[object]
Array of objects related to the users.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
object
Relationship to users.
data [_required_]
[object]
Relationships to user objects.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "description": "Powerpack for ABC",
      "group_widget": {
        "definition": {
          "layout_type": "ordered",
          "show_title": true,
          "title": "Sample Powerpack",
          "type": "group",
          "widgets": [
            {
              "definition": {
                "definition": {
                  "content": "example",
                  "type": "note"
                }
              },
              "layout": {
                "height": 0,
                "width": 0,
                "x": 0,
                "y": 0
              }
            }
          ]
        },
        "layout": {
          "height": 0,
          "width": 0,
          "x": 0,
          "y": 0
        },
        "live_span": "5m"
      },
      "name": "Sample Powerpack",
      "tags": [
        "tag:foo1"
      ],
      "template_variables": [
        {
          "available_values": [
            "my-host",
            "host1",
            "host2"
          ],
          "defaults": [
            "*"
          ],
          "name": "datacenter",
          "prefix": "host"
        }
      ]
    },
    "id": "string",
    "relationships": {
      "author": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "powerpack"
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


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
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=typescript)


#####  Create a new powerpack returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/powerpacks" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Sample powerpack",
      "group_widget": {
        "definition": {
          "layout_type": "ordered",
          "show_title": true,
          "title": "Sample Powerpack",
          "type": "group",
          "widgets": [
            {
              "definition": {
                "content": "test",
                "type": "note"
              }
            }
          ]
        },
        "layout": {
          "height": 3,
          "width": 12,
          "x": 0,
          "y": 0
        },
        "live_span": "1h"
      },
      "name": "Example-Powerpack",
      "tags": [
        "tag:sample"
      ],
      "template_variables": [
        {
          "defaults": [
            "*"
          ],
          "name": "sample"
        }
      ]
    },
    "type": "powerpack"
  }
}
EOF  

                        
```

#####  Create a new powerpack returns "OK" response
```
// Create a new powerpack returns "OK" response

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
	body := datadogV2.Powerpack{
		Data: &datadogV2.PowerpackData{
			Attributes: &datadogV2.PowerpackAttributes{
				Description: datadog.PtrString("Sample powerpack"),
				GroupWidget: datadogV2.PowerpackGroupWidget{
					Definition: datadogV2.PowerpackGroupWidgetDefinition{
						LayoutType: "ordered",
						ShowTitle:  datadog.PtrBool(true),
						Title:      datadog.PtrString("Sample Powerpack"),
						Type:       "group",
						Widgets: []datadogV2.PowerpackInnerWidgets{
							{
								Definition: map[string]interface{}{
									"content": "test",
									"type":    "note",
								},
							},
						},
					},
					Layout: &datadogV2.PowerpackGroupWidgetLayout{
						Height: 3,
						Width:  12,
						X:      0,
						Y:      0,
					},
					LiveSpan: datadogV2.WIDGETLIVESPAN_PAST_ONE_HOUR.Ptr(),
				},
				Name: "Example-Powerpack",
				Tags: []string{
					"tag:sample",
				},
				TemplateVariables: []datadogV2.PowerpackTemplateVariable{
					{
						Defaults: []string{
							"*",
						},
						Name: "sample",
					},
				},
			},
			Type: datadog.PtrString("powerpack"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewPowerpackApi(apiClient)
	resp, r, err := api.CreatePowerpack(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PowerpackApi.CreatePowerpack`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `PowerpackApi.CreatePowerpack`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a new powerpack returns "OK" response
```
// Create a new powerpack returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.PowerpackApi;
import com.datadog.api.client.v2.model.Powerpack;
import com.datadog.api.client.v2.model.PowerpackAttributes;
import com.datadog.api.client.v2.model.PowerpackData;
import com.datadog.api.client.v2.model.PowerpackGroupWidget;
import com.datadog.api.client.v2.model.PowerpackGroupWidgetDefinition;
import com.datadog.api.client.v2.model.PowerpackGroupWidgetLayout;
import com.datadog.api.client.v2.model.PowerpackInnerWidgets;
import com.datadog.api.client.v2.model.PowerpackResponse;
import com.datadog.api.client.v2.model.PowerpackTemplateVariable;
import com.datadog.api.client.v2.model.WidgetLiveSpan;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    PowerpackApi apiInstance = new PowerpackApi(defaultClient);

    Powerpack body =
        new Powerpack()
            .data(
                new PowerpackData()
                    .attributes(
                        new PowerpackAttributes()
                            .description("Sample powerpack")
                            .groupWidget(
                                new PowerpackGroupWidget()
                                    .definition(
                                        new PowerpackGroupWidgetDefinition()
                                            .layoutType("ordered")
                                            .showTitle(true)
                                            .title("Sample Powerpack")
                                            .type("group")
                                            .widgets(
                                                Collections.singletonList(
                                                    new PowerpackInnerWidgets()
                                                        .definition(
                                                            Map.ofEntries(
                                                                Map.entry("content", "test"),
                                                                Map.entry("type", "note"))))))
                                    .layout(
                                        new PowerpackGroupWidgetLayout()
                                            .height(3L)
                                            .width(12L)
                                            .x(0L)
                                            .y(0L))
                                    .liveSpan(WidgetLiveSpan.PAST_ONE_HOUR))
                            .name("Example-Powerpack")
                            .tags(Collections.singletonList("tag:sample"))
                            .templateVariables(
                                Collections.singletonList(
                                    new PowerpackTemplateVariable()
                                        .defaults(Collections.singletonList("*"))
                                        .name("sample"))))
                    .type("powerpack"));

    try {
      PowerpackResponse result = apiInstance.createPowerpack(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PowerpackApi#createPowerpack");
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

#####  Create a new powerpack returns "OK" response
```
"""
Create a new powerpack returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.powerpack_api import PowerpackApi
from datadog_api_client.v2.model.powerpack import Powerpack
from datadog_api_client.v2.model.powerpack_attributes import PowerpackAttributes
from datadog_api_client.v2.model.powerpack_data import PowerpackData
from datadog_api_client.v2.model.powerpack_group_widget import PowerpackGroupWidget
from datadog_api_client.v2.model.powerpack_group_widget_definition import PowerpackGroupWidgetDefinition
from datadog_api_client.v2.model.powerpack_group_widget_layout import PowerpackGroupWidgetLayout
from datadog_api_client.v2.model.powerpack_inner_widgets import PowerpackInnerWidgets
from datadog_api_client.v2.model.powerpack_template_variable import PowerpackTemplateVariable
from datadog_api_client.v2.model.widget_live_span import WidgetLiveSpan

body = Powerpack(
    data=PowerpackData(
        attributes=PowerpackAttributes(
            description="Sample powerpack",
            group_widget=PowerpackGroupWidget(
                definition=PowerpackGroupWidgetDefinition(
                    layout_type="ordered",
                    show_title=True,
                    title="Sample Powerpack",
                    type="group",
                    widgets=[
                        PowerpackInnerWidgets(
                            definition=dict([("content", "test"), ("type", "note")]),
                        ),
                    ],
                ),
                layout=PowerpackGroupWidgetLayout(
                    height=3,
                    width=12,
                    x=0,
                    y=0,
                ),
                live_span=WidgetLiveSpan.PAST_ONE_HOUR,
            ),
            name="Example-Powerpack",
            tags=[
                "tag:sample",
            ],
            template_variables=[
                PowerpackTemplateVariable(
                    defaults=[
                        "*",
                    ],
                    name="sample",
                ),
            ],
        ),
        type="powerpack",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PowerpackApi(api_client)
    response = api_instance.create_powerpack(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a new powerpack returns "OK" response
```
# Create a new powerpack returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::PowerpackAPI.new

body = DatadogAPIClient::V2::Powerpack.new({
  data: DatadogAPIClient::V2::PowerpackData.new({
    attributes: DatadogAPIClient::V2::PowerpackAttributes.new({
      description: "Sample powerpack",
      group_widget: DatadogAPIClient::V2::PowerpackGroupWidget.new({
        definition: DatadogAPIClient::V2::PowerpackGroupWidgetDefinition.new({
          layout_type: "ordered",
          show_title: true,
          title: "Sample Powerpack",
          type: "group",
          widgets: [
            DatadogAPIClient::V2::PowerpackInnerWidgets.new({
              definition: {
                "content": "test", "type": "note",
              },
            }),
          ],
        }),
        layout: DatadogAPIClient::V2::PowerpackGroupWidgetLayout.new({
          height: 3,
          width: 12,
          x: 0,
          y: 0,
        }),
        live_span: DatadogAPIClient::V2::WidgetLiveSpan::PAST_ONE_HOUR,
      }),
      name: "Example-Powerpack",
      tags: [
        "tag:sample",
      ],
      template_variables: [
        DatadogAPIClient::V2::PowerpackTemplateVariable.new({
          defaults: [
            "*",
          ],
          name: "sample",
        }),
      ],
    }),
    type: "powerpack",
  }),
})
p api_instance.create_powerpack(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a new powerpack returns "OK" response
```
// Create a new powerpack returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_powerpack::PowerpackAPI;
use datadog_api_client::datadogV2::model::Powerpack;
use datadog_api_client::datadogV2::model::PowerpackAttributes;
use datadog_api_client::datadogV2::model::PowerpackData;
use datadog_api_client::datadogV2::model::PowerpackGroupWidget;
use datadog_api_client::datadogV2::model::PowerpackGroupWidgetDefinition;
use datadog_api_client::datadogV2::model::PowerpackGroupWidgetLayout;
use datadog_api_client::datadogV2::model::PowerpackInnerWidgets;
use datadog_api_client::datadogV2::model::PowerpackTemplateVariable;
use datadog_api_client::datadogV2::model::WidgetLiveSpan;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = Powerpack::new().data(
        PowerpackData::new()
            .attributes(
                PowerpackAttributes::new(
                    PowerpackGroupWidget::new(
                        PowerpackGroupWidgetDefinition::new(
                            "ordered".to_string(),
                            "group".to_string(),
                            vec![PowerpackInnerWidgets::new(BTreeMap::from([
                                ("content".to_string(), Value::from("test")),
                                ("type".to_string(), Value::from("note")),
                            ]))],
                        )
                        .show_title(true)
                        .title("Sample Powerpack".to_string()),
                    )
                    .layout(PowerpackGroupWidgetLayout::new(3, 12, 0, 0))
                    .live_span(WidgetLiveSpan::PAST_ONE_HOUR),
                    "Example-Powerpack".to_string(),
                )
                .description("Sample powerpack".to_string())
                .tags(vec!["tag:sample".to_string()])
                .template_variables(vec![PowerpackTemplateVariable::new("sample".to_string())
                    .defaults(vec!["*".to_string()])]),
            )
            .type_("powerpack".to_string()),
    );
    let configuration = datadog::Configuration::new();
    let api = PowerpackAPI::with_config(configuration);
    let resp = api.create_powerpack(body).await;
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

#####  Create a new powerpack returns "OK" response
```
/**
 * Create a new powerpack returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.PowerpackApi(configuration);

const params: v2.PowerpackApiCreatePowerpackRequest = {
  body: {
    data: {
      attributes: {
        description: "Sample powerpack",
        groupWidget: {
          definition: {
            layoutType: "ordered",
            showTitle: true,
            title: "Sample Powerpack",
            type: "group",
            widgets: [
              {
                definition: {
                  content: "test",
                  type: "note",
                },
              },
            ],
          },
          layout: {
            height: 3,
            width: 12,
            x: 0,
            y: 0,
          },
          liveSpan: "1h",
        },
        name: "Example-Powerpack",
        tags: ["tag:sample"],
        templateVariables: [
          {
            defaults: ["*"],
            name: "sample",
          },
        ],
      },
      type: "powerpack",
    },
  },
};

apiInstance
  .createPowerpack(params)
  .then((data: v2.PowerpackResponse) => {
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
## [Delete a powerpack](https://docs.datadoghq.com/api/latest/powerpack/#delete-a-powerpack)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/powerpack/#delete-a-powerpack-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.ap2.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.datadoghq.eu/api/v2/powerpacks/{powerpack_id}https://api.ddog-gov.com/api/v2/powerpacks/{powerpack_id}https://api.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.us3.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.us5.datadoghq.com/api/v2/powerpacks/{powerpack_id}
### Overview
Delete a powerpack. This endpoint requires the `dashboards_write` permission.
OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#powerpack) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
powerpack_id [_required_]
string
Powerpack id
### Response
  * [204](https://docs.datadoghq.com/api/latest/powerpack/#DeletePowerpack-204-v2)
  * [404](https://docs.datadoghq.com/api/latest/powerpack/#DeletePowerpack-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/powerpack/#DeletePowerpack-429-v2)


OK
Powerpack Not Found
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


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
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=typescript)


#####  Delete a powerpack
Copy
```
                  # Path parameters  
export powerpack_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/powerpacks/${powerpack_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a powerpack
```
"""
Delete a powerpack returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.powerpack_api import PowerpackApi

# there is a valid "powerpack" in the system
POWERPACK_DATA_ID = environ["POWERPACK_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PowerpackApi(api_client)
    api_instance.delete_powerpack(
        powerpack_id=POWERPACK_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a powerpack
```
# Delete a powerpack returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::PowerpackAPI.new

# there is a valid "powerpack" in the system
POWERPACK_DATA_ID = ENV["POWERPACK_DATA_ID"]
api_instance.delete_powerpack(POWERPACK_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a powerpack
```
// Delete a powerpack returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "powerpack" in the system
	PowerpackDataID := os.Getenv("POWERPACK_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewPowerpackApi(apiClient)
	r, err := api.DeletePowerpack(ctx, PowerpackDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PowerpackApi.DeletePowerpack`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete a powerpack
```
// Delete a powerpack returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.PowerpackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    PowerpackApi apiInstance = new PowerpackApi(defaultClient);

    // there is a valid "powerpack" in the system
    String POWERPACK_DATA_ID = System.getenv("POWERPACK_DATA_ID");

    try {
      apiInstance.deletePowerpack(POWERPACK_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling PowerpackApi#deletePowerpack");
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

#####  Delete a powerpack
```
// Delete a powerpack returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_powerpack::PowerpackAPI;

#[tokio::main]
async fn main() {
    // there is a valid "powerpack" in the system
    let powerpack_data_id = std::env::var("POWERPACK_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = PowerpackAPI::with_config(configuration);
    let resp = api.delete_powerpack(powerpack_data_id.clone()).await;
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

#####  Delete a powerpack
```
/**
 * Delete a powerpack returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.PowerpackApi(configuration);

// there is a valid "powerpack" in the system
const POWERPACK_DATA_ID = process.env.POWERPACK_DATA_ID as string;

const params: v2.PowerpackApiDeletePowerpackRequest = {
  powerpackId: POWERPACK_DATA_ID,
};

apiInstance
  .deletePowerpack(params)
  .then((data: any) => {
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
## [Get a Powerpack](https://docs.datadoghq.com/api/latest/powerpack/#get-a-powerpack)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/powerpack/#get-a-powerpack-v2)


GET https://api.ap1.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.ap2.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.datadoghq.eu/api/v2/powerpacks/{powerpack_id}https://api.ddog-gov.com/api/v2/powerpacks/{powerpack_id}https://api.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.us3.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.us5.datadoghq.com/api/v2/powerpacks/{powerpack_id}
### Overview
Get a powerpack. This endpoint requires the `dashboards_read` permission.
OAuth apps require the `dashboards_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#powerpack) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
powerpack_id [_required_]
string
ID of the powerpack.
### Response
  * [200](https://docs.datadoghq.com/api/latest/powerpack/#GetPowerpack-200-v2)
  * [404](https://docs.datadoghq.com/api/latest/powerpack/#GetPowerpack-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/powerpack/#GetPowerpack-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


Response object which includes a single powerpack configuration.
Field
Type
Description
data
object
Powerpack data object.
attributes
object
Powerpack attribute object.
description
string
Description of this powerpack.
group_widget [_required_]
object
Powerpack group widget definition object.
definition [_required_]
object
Powerpack group widget object.
layout_type [_required_]
string
Layout type of widgets.
show_title
boolean
Boolean indicating whether powerpack group title should be visible or not.
title
string
Name for the group widget.
type [_required_]
string
Type of widget, must be group.
widgets [_required_]
[object]
Widgets inside the powerpack.
definition [_required_]
object
Information about widget.
layout
object
Powerpack inner widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
layout
object
Powerpack group widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert`
name [_required_]
string
Name of the powerpack.
tags
[string]
List of tags to identify this powerpack.
template_variables
[object]
List of template variables for this powerpack.
available_values
[string]
The list of values that the template variable drop-down is limited to.
defaults
[string]
One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.
name [_required_]
string
The name of the variable.
prefix
string
The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.
id
string
ID of the powerpack.
relationships
object
Powerpack relationship object.
author
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type
string
Type of widget, must be powerpack.
included
[object]
Array of objects related to the users.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
object
Relationship to users.
data [_required_]
[object]
Relationships to user objects.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "description": "Powerpack for ABC",
      "group_widget": {
        "definition": {
          "layout_type": "ordered",
          "show_title": true,
          "title": "Sample Powerpack",
          "type": "group",
          "widgets": [
            {
              "definition": {
                "definition": {
                  "content": "example",
                  "type": "note"
                }
              },
              "layout": {
                "height": 0,
                "width": 0,
                "x": 0,
                "y": 0
              }
            }
          ]
        },
        "layout": {
          "height": 0,
          "width": 0,
          "x": 0,
          "y": 0
        },
        "live_span": "5m"
      },
      "name": "Sample Powerpack",
      "tags": [
        "tag:foo1"
      ],
      "template_variables": [
        {
          "available_values": [
            "my-host",
            "host1",
            "host2"
          ],
          "defaults": [
            "*"
          ],
          "name": "datacenter",
          "prefix": "host"
        }
      ]
    },
    "id": "string",
    "relationships": {
      "author": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "powerpack"
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

Copy
Powerpack Not Found.
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


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
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=typescript)


#####  Get a Powerpack
Copy
```
                  # Path parameters  
export powerpack_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/powerpacks/${powerpack_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a Powerpack
```
"""
Get a Powerpack returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.powerpack_api import PowerpackApi

# there is a valid "powerpack" in the system
POWERPACK_DATA_ID = environ["POWERPACK_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PowerpackApi(api_client)
    response = api_instance.get_powerpack(
        powerpack_id=POWERPACK_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a Powerpack
```
# Get a Powerpack returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::PowerpackAPI.new

# there is a valid "powerpack" in the system
POWERPACK_DATA_ID = ENV["POWERPACK_DATA_ID"]
p api_instance.get_powerpack(POWERPACK_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a Powerpack
```
// Get a Powerpack returns "OK" response

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
	// there is a valid "powerpack" in the system
	PowerpackDataID := os.Getenv("POWERPACK_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewPowerpackApi(apiClient)
	resp, r, err := api.GetPowerpack(ctx, PowerpackDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PowerpackApi.GetPowerpack`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `PowerpackApi.GetPowerpack`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a Powerpack
```
// Get a Powerpack returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.PowerpackApi;
import com.datadog.api.client.v2.model.PowerpackResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    PowerpackApi apiInstance = new PowerpackApi(defaultClient);

    // there is a valid "powerpack" in the system
    String POWERPACK_DATA_ID = System.getenv("POWERPACK_DATA_ID");

    try {
      PowerpackResponse result = apiInstance.getPowerpack(POWERPACK_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PowerpackApi#getPowerpack");
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

#####  Get a Powerpack
```
// Get a Powerpack returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_powerpack::PowerpackAPI;

#[tokio::main]
async fn main() {
    // there is a valid "powerpack" in the system
    let powerpack_data_id = std::env::var("POWERPACK_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = PowerpackAPI::with_config(configuration);
    let resp = api.get_powerpack(powerpack_data_id.clone()).await;
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

#####  Get a Powerpack
```
/**
 * Get a Powerpack returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.PowerpackApi(configuration);

// there is a valid "powerpack" in the system
const POWERPACK_DATA_ID = process.env.POWERPACK_DATA_ID as string;

const params: v2.PowerpackApiGetPowerpackRequest = {
  powerpackId: POWERPACK_DATA_ID,
};

apiInstance
  .getPowerpack(params)
  .then((data: v2.PowerpackResponse) => {
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
## [Update a powerpack](https://docs.datadoghq.com/api/latest/powerpack/#update-a-powerpack)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/powerpack/#update-a-powerpack-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.ap2.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.datadoghq.eu/api/v2/powerpacks/{powerpack_id}https://api.ddog-gov.com/api/v2/powerpacks/{powerpack_id}https://api.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.us3.datadoghq.com/api/v2/powerpacks/{powerpack_id}https://api.us5.datadoghq.com/api/v2/powerpacks/{powerpack_id}
### Overview
Update a powerpack. This endpoint requires the `dashboards_write` permission.
OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#powerpack) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
powerpack_id [_required_]
string
ID of the powerpack.
### Request
#### Body Data (required)
Update a powerpack request body.
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


Field
Type
Description
data
object
Powerpack data object.
attributes
object
Powerpack attribute object.
description
string
Description of this powerpack.
group_widget [_required_]
object
Powerpack group widget definition object.
definition [_required_]
object
Powerpack group widget object.
layout_type [_required_]
string
Layout type of widgets.
show_title
boolean
Boolean indicating whether powerpack group title should be visible or not.
title
string
Name for the group widget.
type [_required_]
string
Type of widget, must be group.
widgets [_required_]
[object]
Widgets inside the powerpack.
definition [_required_]
object
Information about widget.
layout
object
Powerpack inner widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
layout
object
Powerpack group widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert`
name [_required_]
string
Name of the powerpack.
tags
[string]
List of tags to identify this powerpack.
template_variables
[object]
List of template variables for this powerpack.
available_values
[string]
The list of values that the template variable drop-down is limited to.
defaults
[string]
One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.
name [_required_]
string
The name of the variable.
prefix
string
The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.
id
string
ID of the powerpack.
relationships
object
Powerpack relationship object.
author
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type
string
Type of widget, must be powerpack.
```
{
  "data": {
    "attributes": {
      "description": "Sample powerpack",
      "group_widget": {
        "definition": {
          "layout_type": "ordered",
          "show_title": true,
          "title": "Sample Powerpack",
          "type": "group",
          "widgets": [
            {
              "definition": {
                "content": "test",
                "type": "note"
              }
            }
          ]
        },
        "layout": {
          "height": 3,
          "width": 12,
          "x": 0,
          "y": 0
        },
        "live_span": "1h"
      },
      "name": "Example-Powerpack",
      "tags": [
        "tag:sample"
      ],
      "template_variables": [
        {
          "defaults": [
            "*"
          ],
          "name": "sample"
        }
      ]
    },
    "type": "powerpack"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/powerpack/#UpdatePowerpack-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/powerpack/#UpdatePowerpack-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/powerpack/#UpdatePowerpack-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/powerpack/#UpdatePowerpack-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


Response object which includes a single powerpack configuration.
Field
Type
Description
data
object
Powerpack data object.
attributes
object
Powerpack attribute object.
description
string
Description of this powerpack.
group_widget [_required_]
object
Powerpack group widget definition object.
definition [_required_]
object
Powerpack group widget object.
layout_type [_required_]
string
Layout type of widgets.
show_title
boolean
Boolean indicating whether powerpack group title should be visible or not.
title
string
Name for the group widget.
type [_required_]
string
Type of widget, must be group.
widgets [_required_]
[object]
Widgets inside the powerpack.
definition [_required_]
object
Information about widget.
layout
object
Powerpack inner widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
layout
object
Powerpack group widget layout.
height [_required_]
int64
The height of the widget. Should be a non-negative integer.
width [_required_]
int64
The width of the widget. Should be a non-negative integer.
x [_required_]
int64
The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
y [_required_]
int64
The position of the widget on the y (vertical) axis. Should be a non-negative integer.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert`
name [_required_]
string
Name of the powerpack.
tags
[string]
List of tags to identify this powerpack.
template_variables
[object]
List of template variables for this powerpack.
available_values
[string]
The list of values that the template variable drop-down is limited to.
defaults
[string]
One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.
name [_required_]
string
The name of the variable.
prefix
string
The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.
id
string
ID of the powerpack.
relationships
object
Powerpack relationship object.
author
object
Relationship to user.
data [_required_]
object
Relationship to user object.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
type
string
Type of widget, must be powerpack.
included
[object]
Array of objects related to the users.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
object
Relationship to users.
data [_required_]
[object]
Relationships to user objects.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "description": "Powerpack for ABC",
      "group_widget": {
        "definition": {
          "layout_type": "ordered",
          "show_title": true,
          "title": "Sample Powerpack",
          "type": "group",
          "widgets": [
            {
              "definition": {
                "definition": {
                  "content": "example",
                  "type": "note"
                }
              },
              "layout": {
                "height": 0,
                "width": 0,
                "x": 0,
                "y": 0
              }
            }
          ]
        },
        "layout": {
          "height": 0,
          "width": 0,
          "x": 0,
          "y": 0
        },
        "live_span": "5m"
      },
      "name": "Sample Powerpack",
      "tags": [
        "tag:foo1"
      ],
      "template_variables": [
        {
          "available_values": [
            "my-host",
            "host1",
            "host2"
          ],
          "defaults": [
            "*"
          ],
          "name": "datacenter",
          "prefix": "host"
        }
      ]
    },
    "id": "string",
    "relationships": {
      "author": {
        "data": {
          "id": "00000000-0000-0000-2345-000000000000",
          "type": "users"
        }
      }
    },
    "type": "powerpack"
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


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
Powerpack Not Found
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


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
  * [Model](https://docs.datadoghq.com/api/latest/powerpack/)
  * [Example](https://docs.datadoghq.com/api/latest/powerpack/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/powerpack/?code-lang=typescript)


#####  Update a powerpack returns "OK" response
Copy
```
                          # Path parameters  
export powerpack_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/powerpacks/${powerpack_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "Sample powerpack",
      "group_widget": {
        "definition": {
          "layout_type": "ordered",
          "show_title": true,
          "title": "Sample Powerpack",
          "type": "group",
          "widgets": [
            {
              "definition": {
                "content": "test",
                "type": "note"
              }
            }
          ]
        },
        "layout": {
          "height": 3,
          "width": 12,
          "x": 0,
          "y": 0
        },
        "live_span": "1h"
      },
      "name": "Example-Powerpack",
      "tags": [
        "tag:sample"
      ],
      "template_variables": [
        {
          "defaults": [
            "*"
          ],
          "name": "sample"
        }
      ]
    },
    "type": "powerpack"
  }
}
EOF  

                        
```

#####  Update a powerpack returns "OK" response
```
// Update a powerpack returns "OK" response

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
	// there is a valid "powerpack" in the system
	PowerpackDataID := os.Getenv("POWERPACK_DATA_ID")

	body := datadogV2.Powerpack{
		Data: &datadogV2.PowerpackData{
			Attributes: &datadogV2.PowerpackAttributes{
				Description: datadog.PtrString("Sample powerpack"),
				GroupWidget: datadogV2.PowerpackGroupWidget{
					Definition: datadogV2.PowerpackGroupWidgetDefinition{
						LayoutType: "ordered",
						ShowTitle:  datadog.PtrBool(true),
						Title:      datadog.PtrString("Sample Powerpack"),
						Type:       "group",
						Widgets: []datadogV2.PowerpackInnerWidgets{
							{
								Definition: map[string]interface{}{
									"content": "test",
									"type":    "note",
								},
							},
						},
					},
					Layout: &datadogV2.PowerpackGroupWidgetLayout{
						Height: 3,
						Width:  12,
						X:      0,
						Y:      0,
					},
					LiveSpan: datadogV2.WIDGETLIVESPAN_PAST_ONE_HOUR.Ptr(),
				},
				Name: "Example-Powerpack",
				Tags: []string{
					"tag:sample",
				},
				TemplateVariables: []datadogV2.PowerpackTemplateVariable{
					{
						Defaults: []string{
							"*",
						},
						Name: "sample",
					},
				},
			},
			Type: datadog.PtrString("powerpack"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewPowerpackApi(apiClient)
	resp, r, err := api.UpdatePowerpack(ctx, PowerpackDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PowerpackApi.UpdatePowerpack`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `PowerpackApi.UpdatePowerpack`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Update a powerpack returns "OK" response
```
// Update a powerpack returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.PowerpackApi;
import com.datadog.api.client.v2.model.Powerpack;
import com.datadog.api.client.v2.model.PowerpackAttributes;
import com.datadog.api.client.v2.model.PowerpackData;
import com.datadog.api.client.v2.model.PowerpackGroupWidget;
import com.datadog.api.client.v2.model.PowerpackGroupWidgetDefinition;
import com.datadog.api.client.v2.model.PowerpackGroupWidgetLayout;
import com.datadog.api.client.v2.model.PowerpackInnerWidgets;
import com.datadog.api.client.v2.model.PowerpackResponse;
import com.datadog.api.client.v2.model.PowerpackTemplateVariable;
import com.datadog.api.client.v2.model.WidgetLiveSpan;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    PowerpackApi apiInstance = new PowerpackApi(defaultClient);

    // there is a valid "powerpack" in the system
    String POWERPACK_DATA_ID = System.getenv("POWERPACK_DATA_ID");

    Powerpack body =
        new Powerpack()
            .data(
                new PowerpackData()
                    .attributes(
                        new PowerpackAttributes()
                            .description("Sample powerpack")
                            .groupWidget(
                                new PowerpackGroupWidget()
                                    .definition(
                                        new PowerpackGroupWidgetDefinition()
                                            .layoutType("ordered")
                                            .showTitle(true)
                                            .title("Sample Powerpack")
                                            .type("group")
                                            .widgets(
                                                Collections.singletonList(
                                                    new PowerpackInnerWidgets()
                                                        .definition(
                                                            Map.ofEntries(
                                                                Map.entry("content", "test"),
                                                                Map.entry("type", "note"))))))
                                    .layout(
                                        new PowerpackGroupWidgetLayout()
                                            .height(3L)
                                            .width(12L)
                                            .x(0L)
                                            .y(0L))
                                    .liveSpan(WidgetLiveSpan.PAST_ONE_HOUR))
                            .name("Example-Powerpack")
                            .tags(Collections.singletonList("tag:sample"))
                            .templateVariables(
                                Collections.singletonList(
                                    new PowerpackTemplateVariable()
                                        .defaults(Collections.singletonList("*"))
                                        .name("sample"))))
                    .type("powerpack"));

    try {
      PowerpackResponse result = apiInstance.updatePowerpack(POWERPACK_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PowerpackApi#updatePowerpack");
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

#####  Update a powerpack returns "OK" response
```
"""
Update a powerpack returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.powerpack_api import PowerpackApi
from datadog_api_client.v2.model.powerpack import Powerpack
from datadog_api_client.v2.model.powerpack_attributes import PowerpackAttributes
from datadog_api_client.v2.model.powerpack_data import PowerpackData
from datadog_api_client.v2.model.powerpack_group_widget import PowerpackGroupWidget
from datadog_api_client.v2.model.powerpack_group_widget_definition import PowerpackGroupWidgetDefinition
from datadog_api_client.v2.model.powerpack_group_widget_layout import PowerpackGroupWidgetLayout
from datadog_api_client.v2.model.powerpack_inner_widgets import PowerpackInnerWidgets
from datadog_api_client.v2.model.powerpack_template_variable import PowerpackTemplateVariable
from datadog_api_client.v2.model.widget_live_span import WidgetLiveSpan

# there is a valid "powerpack" in the system
POWERPACK_DATA_ID = environ["POWERPACK_DATA_ID"]

body = Powerpack(
    data=PowerpackData(
        attributes=PowerpackAttributes(
            description="Sample powerpack",
            group_widget=PowerpackGroupWidget(
                definition=PowerpackGroupWidgetDefinition(
                    layout_type="ordered",
                    show_title=True,
                    title="Sample Powerpack",
                    type="group",
                    widgets=[
                        PowerpackInnerWidgets(
                            definition=dict([("content", "test"), ("type", "note")]),
                        ),
                    ],
                ),
                layout=PowerpackGroupWidgetLayout(
                    height=3,
                    width=12,
                    x=0,
                    y=0,
                ),
                live_span=WidgetLiveSpan.PAST_ONE_HOUR,
            ),
            name="Example-Powerpack",
            tags=[
                "tag:sample",
            ],
            template_variables=[
                PowerpackTemplateVariable(
                    defaults=[
                        "*",
                    ],
                    name="sample",
                ),
            ],
        ),
        type="powerpack",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PowerpackApi(api_client)
    response = api_instance.update_powerpack(powerpack_id=POWERPACK_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Update a powerpack returns "OK" response
```
# Update a powerpack returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::PowerpackAPI.new

# there is a valid "powerpack" in the system
POWERPACK_DATA_ID = ENV["POWERPACK_DATA_ID"]

body = DatadogAPIClient::V2::Powerpack.new({
  data: DatadogAPIClient::V2::PowerpackData.new({
    attributes: DatadogAPIClient::V2::PowerpackAttributes.new({
      description: "Sample powerpack",
      group_widget: DatadogAPIClient::V2::PowerpackGroupWidget.new({
        definition: DatadogAPIClient::V2::PowerpackGroupWidgetDefinition.new({
          layout_type: "ordered",
          show_title: true,
          title: "Sample Powerpack",
          type: "group",
          widgets: [
            DatadogAPIClient::V2::PowerpackInnerWidgets.new({
              definition: {
                "content": "test", "type": "note",
              },
            }),
          ],
        }),
        layout: DatadogAPIClient::V2::PowerpackGroupWidgetLayout.new({
          height: 3,
          width: 12,
          x: 0,
          y: 0,
        }),
        live_span: DatadogAPIClient::V2::WidgetLiveSpan::PAST_ONE_HOUR,
      }),
      name: "Example-Powerpack",
      tags: [
        "tag:sample",
      ],
      template_variables: [
        DatadogAPIClient::V2::PowerpackTemplateVariable.new({
          defaults: [
            "*",
          ],
          name: "sample",
        }),
      ],
    }),
    type: "powerpack",
  }),
})
p api_instance.update_powerpack(POWERPACK_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Update a powerpack returns "OK" response
```
// Update a powerpack returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_powerpack::PowerpackAPI;
use datadog_api_client::datadogV2::model::Powerpack;
use datadog_api_client::datadogV2::model::PowerpackAttributes;
use datadog_api_client::datadogV2::model::PowerpackData;
use datadog_api_client::datadogV2::model::PowerpackGroupWidget;
use datadog_api_client::datadogV2::model::PowerpackGroupWidgetDefinition;
use datadog_api_client::datadogV2::model::PowerpackGroupWidgetLayout;
use datadog_api_client::datadogV2::model::PowerpackInnerWidgets;
use datadog_api_client::datadogV2::model::PowerpackTemplateVariable;
use datadog_api_client::datadogV2::model::WidgetLiveSpan;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    // there is a valid "powerpack" in the system
    let powerpack_data_id = std::env::var("POWERPACK_DATA_ID").unwrap();
    let body = Powerpack::new().data(
        PowerpackData::new()
            .attributes(
                PowerpackAttributes::new(
                    PowerpackGroupWidget::new(
                        PowerpackGroupWidgetDefinition::new(
                            "ordered".to_string(),
                            "group".to_string(),
                            vec![PowerpackInnerWidgets::new(BTreeMap::from([
                                ("content".to_string(), Value::from("test")),
                                ("type".to_string(), Value::from("note")),
                            ]))],
                        )
                        .show_title(true)
                        .title("Sample Powerpack".to_string()),
                    )
                    .layout(PowerpackGroupWidgetLayout::new(3, 12, 0, 0))
                    .live_span(WidgetLiveSpan::PAST_ONE_HOUR),
                    "Example-Powerpack".to_string(),
                )
                .description("Sample powerpack".to_string())
                .tags(vec!["tag:sample".to_string()])
                .template_variables(vec![PowerpackTemplateVariable::new("sample".to_string())
                    .defaults(vec!["*".to_string()])]),
            )
            .type_("powerpack".to_string()),
    );
    let configuration = datadog::Configuration::new();
    let api = PowerpackAPI::with_config(configuration);
    let resp = api.update_powerpack(powerpack_data_id.clone(), body).await;
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

#####  Update a powerpack returns "OK" response
```
/**
 * Update a powerpack returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.PowerpackApi(configuration);

// there is a valid "powerpack" in the system
const POWERPACK_DATA_ID = process.env.POWERPACK_DATA_ID as string;

const params: v2.PowerpackApiUpdatePowerpackRequest = {
  body: {
    data: {
      attributes: {
        description: "Sample powerpack",
        groupWidget: {
          definition: {
            layoutType: "ordered",
            showTitle: true,
            title: "Sample Powerpack",
            type: "group",
            widgets: [
              {
                definition: {
                  content: "test",
                  type: "note",
                },
              },
            ],
          },
          layout: {
            height: 3,
            width: 12,
            x: 0,
            y: 0,
          },
          liveSpan: "1h",
        },
        name: "Example-Powerpack",
        tags: ["tag:sample"],
        templateVariables: [
          {
            defaults: ["*"],
            name: "sample",
          },
        ],
      },
      type: "powerpack",
    },
  },
  powerpackId: POWERPACK_DATA_ID,
};

apiInstance
  .updatePowerpack(params)
  .then((data: v2.PowerpackResponse) => {
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=289dfeab-3fe9-4031-a595-03898aef71bd&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=085ea75a-fdc7-4372-ba9c-2485f8229214&pt=Powerpack&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fpowerpack%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=289dfeab-3fe9-4031-a595-03898aef71bd&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=085ea75a-fdc7-4372-ba9c-2485f8229214&pt=Powerpack&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fpowerpack%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=5c0929c0-e53f-4df8-ba00-68e8b1cb84ad&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Powerpack&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fpowerpack%2F&r=&lt=14307&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=45383)
