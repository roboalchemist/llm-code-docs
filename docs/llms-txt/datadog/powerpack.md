# Source: https://docs.datadoghq.com/api/latest/powerpack.md

---
title: Powerpack
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Powerpack
---

# Powerpack

The Powerpack endpoints allow you to:

- Get a Powerpack
- Create a Powerpack
- Delete a Powerpack
- Get a list of all Powerpacks

The Patch and Delete API methods can only be performed on a Powerpack by a user who has the powerpack create permission for that specific Powerpack.

Read [Scale Graphing Expertise with Powerpacks](https://docs.datadoghq.com/dashboards/guide/powerpacks-best-practices/) for more information.

## Get all powerpacks{% #get-all-powerpacks %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                        |
| ----------------- | --------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/powerpacks |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/powerpacks |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/powerpacks      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/powerpacks      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/powerpacks     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/powerpacks |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/powerpacks |

### Overview

Get a list of all powerpacks. This endpoint requires the `dashboards_read` permission.

OAuth apps require the `dashboards_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#powerpack) to access this endpoint.



### Arguments

#### Query Strings

| Name         | Type    | Description                                                   |
| ------------ | ------- | ------------------------------------------------------------- |
| page[limit]  | integer | Maximum number of powerpacks in the response.                 |
| page[offset] | integer | Specific offset to use as the beginning of the returned page. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object which includes all powerpack configurations.

| Parent field       | Field                          | Type      | Description                                                                                                                               |
| ------------------ | ------------------------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                           | [object]  | List of powerpack definitions.                                                                                                            |
| data               | attributes                     | object    | Powerpack attribute object.                                                                                                               |
| attributes         | description                    | string    | Description of this powerpack.                                                                                                            |
| attributes         | group_widget [*required*] | object    | Powerpack group widget definition object.                                                                                                 |
| group_widget       | definition [*required*]   | object    | Powerpack group widget object.                                                                                                            |
| definition         | layout_type [*required*]  | string    | Layout type of widgets.                                                                                                                   |
| definition         | show_title                     | boolean   | Boolean indicating whether powerpack group title should be visible or not.                                                                |
| definition         | title                          | string    | Name for the group widget.                                                                                                                |
| definition         | type [*required*]         | string    | Type of widget, must be group.                                                                                                            |
| definition         | widgets [*required*]      | [object]  | Widgets inside the powerpack.                                                                                                             |
| widgets            | definition [*required*]   | object    | Information about widget.                                                                                                                 |
| widgets            | layout                         | object    | Powerpack inner widget layout.                                                                                                            |
| layout             | height [*required*]       | int64     | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64     | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64     | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64     | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | layout                         | object    | Powerpack group widget layout.                                                                                                            |
| layout             | height [*required*]       | int64     | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64     | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64     | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64     | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | live_span                      | enum      | The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert` |
| attributes         | name [*required*]         | string    | Name of the powerpack.                                                                                                                    |
| attributes         | tags                           | [string]  | List of tags to identify this powerpack.                                                                                                  |
| attributes         | template_variables             | [object]  | List of template variables for this powerpack.                                                                                            |
| template_variables | available_values               | [string]  | The list of values that the template variable drop-down is limited to.                                                                    |
| template_variables | defaults                       | [string]  | One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.  |
| template_variables | name [*required*]         | string    | The name of the variable.                                                                                                                 |
| template_variables | prefix                         | string    | The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.                                 |
| data               | id                             | string    | ID of the powerpack.                                                                                                                      |
| data               | relationships                  | object    | Powerpack relationship object.                                                                                                            |
| relationships      | author                         | object    | Relationship to user.                                                                                                                     |
| author             | data [*required*]         | object    | Relationship to user object.                                                                                                              |
| data               | id [*required*]           | string    | A unique identifier that represents the user.                                                                                             |
| data               | type [*required*]         | enum      | Users resource type. Allowed enum values: `users`                                                                                         |
| data               | type                           | string    | Type of widget, must be powerpack.                                                                                                        |
|                    | included                       | [object]  | Array of objects related to the users.                                                                                                    |
| included           | attributes                     | object    | Attributes of user object returned by the API.                                                                                            |
| attributes         | created_at                     | date-time | Creation time of the user.                                                                                                                |
| attributes         | disabled                       | boolean   | Whether the user is disabled.                                                                                                             |
| attributes         | email                          | string    | Email of the user.                                                                                                                        |
| attributes         | handle                         | string    | Handle of the user.                                                                                                                       |
| attributes         | icon                           | string    | URL of the user's icon.                                                                                                                   |
| attributes         | last_login_time                | date-time | The last time the user logged in.                                                                                                         |
| attributes         | mfa_enabled                    | boolean   | If user has MFA enabled.                                                                                                                  |
| attributes         | modified_at                    | date-time | Time that the user was last modified.                                                                                                     |
| attributes         | name                           | string    | Name of the user.                                                                                                                         |
| attributes         | service_account                | boolean   | Whether the user is a service account.                                                                                                    |
| attributes         | status                         | string    | Status of the user.                                                                                                                       |
| attributes         | title                          | string    | Title of the user.                                                                                                                        |
| attributes         | verified                       | boolean   | Whether the user is verified.                                                                                                             |
| included           | id                             | string    | ID of the user.                                                                                                                           |
| included           | relationships                  | object    | Relationships of the user object returned by the API.                                                                                     |
| relationships      | org                            | object    | Relationship to an organization.                                                                                                          |
| org                | data [*required*]         | object    | Relationship to organization object.                                                                                                      |
| data               | id [*required*]           | string    | ID of the organization.                                                                                                                   |
| data               | type [*required*]         | enum      | Organizations resource type. Allowed enum values: `orgs`                                                                                  |
| relationships      | other_orgs                     | object    | Relationship to organizations.                                                                                                            |
| other_orgs         | data [*required*]         | [object]  | Relationships to organization objects.                                                                                                    |
| data               | id [*required*]           | string    | ID of the organization.                                                                                                                   |
| data               | type [*required*]         | enum      | Organizations resource type. Allowed enum values: `orgs`                                                                                  |
| relationships      | other_users                    | object    | Relationship to users.                                                                                                                    |
| other_users        | data [*required*]         | [object]  | Relationships to user objects.                                                                                                            |
| data               | id [*required*]           | string    | A unique identifier that represents the user.                                                                                             |
| data               | type [*required*]         | enum      | Users resource type. Allowed enum values: `users`                                                                                         |
| relationships      | roles                          | object    | Relationship to roles.                                                                                                                    |
| roles              | data                           | [object]  | An array containing type and the unique identifier of a role.                                                                             |
| data               | id                             | string    | The unique identifier of the role.                                                                                                        |
| data               | type                           | enum      | Roles type. Allowed enum values: `roles`                                                                                                  |
| included           | type                           | enum      | Users resource type. Allowed enum values: `users`                                                                                         |
|                    | links                          | object    | Links attributes.                                                                                                                         |
| links              | first                          | string    | Link to last page.                                                                                                                        |
| links              | last                           | string    | Link to first page.                                                                                                                       |
| links              | next                           | string    | Link for the next set of results.                                                                                                         |
| links              | prev                           | string    | Link for the previous set of results.                                                                                                     |
| links              | self                           | string    | Link to current page.                                                                                                                     |
|                    | meta                           | object    | Powerpack response metadata.                                                                                                              |
| meta               | pagination                     | object    | Powerpack response pagination metadata.                                                                                                   |
| pagination         | first_offset                   | int64     | The first offset.                                                                                                                         |
| pagination         | last_offset                    | int64     | The last offset.                                                                                                                          |
| pagination         | limit                          | int64     | Pagination limit.                                                                                                                         |
| pagination         | next_offset                    | int64     | The next offset.                                                                                                                          |
| pagination         | offset                         | int64     | The offset.                                                                                                                               |
| pagination         | prev_offset                    | int64     | The previous offset.                                                                                                                      |
| pagination         | total                          | int64     | Total results.                                                                                                                            |
| pagination         | type                           | string    | Offset type.                                                                                                                              |

{% /tab %}

{% tab title="Example" %}

```json
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/powerpacks" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get all powerpacks returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::PowerpackAPI.new
opts = {
  page_limit: 1000,
}
p api_instance.list_powerpacks(opts)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create a new powerpack{% #create-a-new-powerpack %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/powerpacks |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/powerpacks |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/powerpacks      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/powerpacks      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/powerpacks     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/powerpacks |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/powerpacks |

### Overview

Create a powerpack. This endpoint requires the `dashboards_write` permission.

OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#powerpack) to access this endpoint.



### Request

#### Body Data (required)

Create a powerpack request body.

{% tab title="Model" %}

| Parent field       | Field                          | Type     | Description                                                                                                                               |
| ------------------ | ------------------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                           | object   | Powerpack data object.                                                                                                                    |
| data               | attributes                     | object   | Powerpack attribute object.                                                                                                               |
| attributes         | description                    | string   | Description of this powerpack.                                                                                                            |
| attributes         | group_widget [*required*] | object   | Powerpack group widget definition object.                                                                                                 |
| group_widget       | definition [*required*]   | object   | Powerpack group widget object.                                                                                                            |
| definition         | layout_type [*required*]  | string   | Layout type of widgets.                                                                                                                   |
| definition         | show_title                     | boolean  | Boolean indicating whether powerpack group title should be visible or not.                                                                |
| definition         | title                          | string   | Name for the group widget.                                                                                                                |
| definition         | type [*required*]         | string   | Type of widget, must be group.                                                                                                            |
| definition         | widgets [*required*]      | [object] | Widgets inside the powerpack.                                                                                                             |
| widgets            | definition [*required*]   | object   | Information about widget.                                                                                                                 |
| widgets            | layout                         | object   | Powerpack inner widget layout.                                                                                                            |
| layout             | height [*required*]       | int64    | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64    | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64    | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64    | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | layout                         | object   | Powerpack group widget layout.                                                                                                            |
| layout             | height [*required*]       | int64    | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64    | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64    | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64    | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | live_span                      | enum     | The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert` |
| attributes         | name [*required*]         | string   | Name of the powerpack.                                                                                                                    |
| attributes         | tags                           | [string] | List of tags to identify this powerpack.                                                                                                  |
| attributes         | template_variables             | [object] | List of template variables for this powerpack.                                                                                            |
| template_variables | available_values               | [string] | The list of values that the template variable drop-down is limited to.                                                                    |
| template_variables | defaults                       | [string] | One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.  |
| template_variables | name [*required*]         | string   | The name of the variable.                                                                                                                 |
| template_variables | prefix                         | string   | The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.                                 |
| data               | id                             | string   | ID of the powerpack.                                                                                                                      |
| data               | relationships                  | object   | Powerpack relationship object.                                                                                                            |
| relationships      | author                         | object   | Relationship to user.                                                                                                                     |
| author             | data [*required*]         | object   | Relationship to user object.                                                                                                              |
| data               | id [*required*]           | string   | A unique identifier that represents the user.                                                                                             |
| data               | type [*required*]         | enum     | Users resource type. Allowed enum values: `users`                                                                                         |
| data               | type                           | string   | Type of widget, must be powerpack.                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
```text

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object which includes a single powerpack configuration.

| Parent field       | Field                          | Type      | Description                                                                                                                               |
| ------------------ | ------------------------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                           | object    | Powerpack data object.                                                                                                                    |
| data               | attributes                     | object    | Powerpack attribute object.                                                                                                               |
| attributes         | description                    | string    | Description of this powerpack.                                                                                                            |
| attributes         | group_widget [*required*] | object    | Powerpack group widget definition object.                                                                                                 |
| group_widget       | definition [*required*]   | object    | Powerpack group widget object.                                                                                                            |
| definition         | layout_type [*required*]  | string    | Layout type of widgets.                                                                                                                   |
| definition         | show_title                     | boolean   | Boolean indicating whether powerpack group title should be visible or not.                                                                |
| definition         | title                          | string    | Name for the group widget.                                                                                                                |
| definition         | type [*required*]         | string    | Type of widget, must be group.                                                                                                            |
| definition         | widgets [*required*]      | [object]  | Widgets inside the powerpack.                                                                                                             |
| widgets            | definition [*required*]   | object    | Information about widget.                                                                                                                 |
| widgets            | layout                         | object    | Powerpack inner widget layout.                                                                                                            |
| layout             | height [*required*]       | int64     | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64     | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64     | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64     | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | layout                         | object    | Powerpack group widget layout.                                                                                                            |
| layout             | height [*required*]       | int64     | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64     | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64     | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64     | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | live_span                      | enum      | The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert` |
| attributes         | name [*required*]         | string    | Name of the powerpack.                                                                                                                    |
| attributes         | tags                           | [string]  | List of tags to identify this powerpack.                                                                                                  |
| attributes         | template_variables             | [object]  | List of template variables for this powerpack.                                                                                            |
| template_variables | available_values               | [string]  | The list of values that the template variable drop-down is limited to.                                                                    |
| template_variables | defaults                       | [string]  | One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.  |
| template_variables | name [*required*]         | string    | The name of the variable.                                                                                                                 |
| template_variables | prefix                         | string    | The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.                                 |
| data               | id                             | string    | ID of the powerpack.                                                                                                                      |
| data               | relationships                  | object    | Powerpack relationship object.                                                                                                            |
| relationships      | author                         | object    | Relationship to user.                                                                                                                     |
| author             | data [*required*]         | object    | Relationship to user object.                                                                                                              |
| data               | id [*required*]           | string    | A unique identifier that represents the user.                                                                                             |
| data               | type [*required*]         | enum      | Users resource type. Allowed enum values: `users`                                                                                         |
| data               | type                           | string    | Type of widget, must be powerpack.                                                                                                        |
|                    | included                       | [object]  | Array of objects related to the users.                                                                                                    |
| included           | attributes                     | object    | Attributes of user object returned by the API.                                                                                            |
| attributes         | created_at                     | date-time | Creation time of the user.                                                                                                                |
| attributes         | disabled                       | boolean   | Whether the user is disabled.                                                                                                             |
| attributes         | email                          | string    | Email of the user.                                                                                                                        |
| attributes         | handle                         | string    | Handle of the user.                                                                                                                       |
| attributes         | icon                           | string    | URL of the user's icon.                                                                                                                   |
| attributes         | last_login_time                | date-time | The last time the user logged in.                                                                                                         |
| attributes         | mfa_enabled                    | boolean   | If user has MFA enabled.                                                                                                                  |
| attributes         | modified_at                    | date-time | Time that the user was last modified.                                                                                                     |
| attributes         | name                           | string    | Name of the user.                                                                                                                         |
| attributes         | service_account                | boolean   | Whether the user is a service account.                                                                                                    |
| attributes         | status                         | string    | Status of the user.                                                                                                                       |
| attributes         | title                          | string    | Title of the user.                                                                                                                        |
| attributes         | verified                       | boolean   | Whether the user is verified.                                                                                                             |
| included           | id                             | string    | ID of the user.                                                                                                                           |
| included           | relationships                  | object    | Relationships of the user object returned by the API.                                                                                     |
| relationships      | org                            | object    | Relationship to an organization.                                                                                                          |
| org                | data [*required*]         | object    | Relationship to organization object.                                                                                                      |
| data               | id [*required*]           | string    | ID of the organization.                                                                                                                   |
| data               | type [*required*]         | enum      | Organizations resource type. Allowed enum values: `orgs`                                                                                  |
| relationships      | other_orgs                     | object    | Relationship to organizations.                                                                                                            |
| other_orgs         | data [*required*]         | [object]  | Relationships to organization objects.                                                                                                    |
| data               | id [*required*]           | string    | ID of the organization.                                                                                                                   |
| data               | type [*required*]         | enum      | Organizations resource type. Allowed enum values: `orgs`                                                                                  |
| relationships      | other_users                    | object    | Relationship to users.                                                                                                                    |
| other_users        | data [*required*]         | [object]  | Relationships to user objects.                                                                                                            |
| data               | id [*required*]           | string    | A unique identifier that represents the user.                                                                                             |
| data               | type [*required*]         | enum      | Users resource type. Allowed enum values: `users`                                                                                         |
| relationships      | roles                          | object    | Relationship to roles.                                                                                                                    |
| roles              | data                           | [object]  | An array containing type and the unique identifier of a role.                                                                             |
| data               | id                             | string    | The unique identifier of the role.                                                                                                        |
| data               | type                           | enum      | Roles type. Allowed enum values: `roles`                                                                                                  |
| included           | type                           | enum      | Users resource type. Allowed enum values: `users`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
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
```text

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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/powerpacks" \
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

#####

```go
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete a powerpack{% #delete-a-powerpack %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                          |
| ----------------- | --------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/powerpacks/{powerpack_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/powerpacks/{powerpack_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/powerpacks/{powerpack_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/powerpacks/{powerpack_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/powerpacks/{powerpack_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/powerpacks/{powerpack_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/powerpacks/{powerpack_id} |

### Overview

Delete a powerpack. This endpoint requires the `dashboards_write` permission.

OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#powerpack) to access this endpoint.



### Arguments

#### Path Parameters

| Name                           | Type   | Description  |
| ------------------------------ | ------ | ------------ |
| powerpack_id [*required*] | string | Powerpack id |

### Response

{% tab title="204" %}
OK
{% /tab %}

{% tab title="404" %}
Powerpack Not Found
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
                  \# Path parametersexport powerpack_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/powerpacks/${powerpack_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete a powerpack returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::PowerpackAPI.new

# there is a valid "powerpack" in the system
POWERPACK_DATA_ID = ENV["POWERPACK_DATA_ID"]
api_instance.delete_powerpack(POWERPACK_DATA_ID)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get a Powerpack{% #get-a-powerpack %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/powerpacks/{powerpack_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/powerpacks/{powerpack_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/powerpacks/{powerpack_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/powerpacks/{powerpack_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/powerpacks/{powerpack_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/powerpacks/{powerpack_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/powerpacks/{powerpack_id} |

### Overview

Get a powerpack. This endpoint requires the `dashboards_read` permission.

OAuth apps require the `dashboards_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#powerpack) to access this endpoint.



### Arguments

#### Path Parameters

| Name                           | Type   | Description          |
| ------------------------------ | ------ | -------------------- |
| powerpack_id [*required*] | string | ID of the powerpack. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object which includes a single powerpack configuration.

| Parent field       | Field                          | Type      | Description                                                                                                                               |
| ------------------ | ------------------------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                           | object    | Powerpack data object.                                                                                                                    |
| data               | attributes                     | object    | Powerpack attribute object.                                                                                                               |
| attributes         | description                    | string    | Description of this powerpack.                                                                                                            |
| attributes         | group_widget [*required*] | object    | Powerpack group widget definition object.                                                                                                 |
| group_widget       | definition [*required*]   | object    | Powerpack group widget object.                                                                                                            |
| definition         | layout_type [*required*]  | string    | Layout type of widgets.                                                                                                                   |
| definition         | show_title                     | boolean   | Boolean indicating whether powerpack group title should be visible or not.                                                                |
| definition         | title                          | string    | Name for the group widget.                                                                                                                |
| definition         | type [*required*]         | string    | Type of widget, must be group.                                                                                                            |
| definition         | widgets [*required*]      | [object]  | Widgets inside the powerpack.                                                                                                             |
| widgets            | definition [*required*]   | object    | Information about widget.                                                                                                                 |
| widgets            | layout                         | object    | Powerpack inner widget layout.                                                                                                            |
| layout             | height [*required*]       | int64     | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64     | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64     | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64     | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | layout                         | object    | Powerpack group widget layout.                                                                                                            |
| layout             | height [*required*]       | int64     | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64     | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64     | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64     | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | live_span                      | enum      | The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert` |
| attributes         | name [*required*]         | string    | Name of the powerpack.                                                                                                                    |
| attributes         | tags                           | [string]  | List of tags to identify this powerpack.                                                                                                  |
| attributes         | template_variables             | [object]  | List of template variables for this powerpack.                                                                                            |
| template_variables | available_values               | [string]  | The list of values that the template variable drop-down is limited to.                                                                    |
| template_variables | defaults                       | [string]  | One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.  |
| template_variables | name [*required*]         | string    | The name of the variable.                                                                                                                 |
| template_variables | prefix                         | string    | The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.                                 |
| data               | id                             | string    | ID of the powerpack.                                                                                                                      |
| data               | relationships                  | object    | Powerpack relationship object.                                                                                                            |
| relationships      | author                         | object    | Relationship to user.                                                                                                                     |
| author             | data [*required*]         | object    | Relationship to user object.                                                                                                              |
| data               | id [*required*]           | string    | A unique identifier that represents the user.                                                                                             |
| data               | type [*required*]         | enum      | Users resource type. Allowed enum values: `users`                                                                                         |
| data               | type                           | string    | Type of widget, must be powerpack.                                                                                                        |
|                    | included                       | [object]  | Array of objects related to the users.                                                                                                    |
| included           | attributes                     | object    | Attributes of user object returned by the API.                                                                                            |
| attributes         | created_at                     | date-time | Creation time of the user.                                                                                                                |
| attributes         | disabled                       | boolean   | Whether the user is disabled.                                                                                                             |
| attributes         | email                          | string    | Email of the user.                                                                                                                        |
| attributes         | handle                         | string    | Handle of the user.                                                                                                                       |
| attributes         | icon                           | string    | URL of the user's icon.                                                                                                                   |
| attributes         | last_login_time                | date-time | The last time the user logged in.                                                                                                         |
| attributes         | mfa_enabled                    | boolean   | If user has MFA enabled.                                                                                                                  |
| attributes         | modified_at                    | date-time | Time that the user was last modified.                                                                                                     |
| attributes         | name                           | string    | Name of the user.                                                                                                                         |
| attributes         | service_account                | boolean   | Whether the user is a service account.                                                                                                    |
| attributes         | status                         | string    | Status of the user.                                                                                                                       |
| attributes         | title                          | string    | Title of the user.                                                                                                                        |
| attributes         | verified                       | boolean   | Whether the user is verified.                                                                                                             |
| included           | id                             | string    | ID of the user.                                                                                                                           |
| included           | relationships                  | object    | Relationships of the user object returned by the API.                                                                                     |
| relationships      | org                            | object    | Relationship to an organization.                                                                                                          |
| org                | data [*required*]         | object    | Relationship to organization object.                                                                                                      |
| data               | id [*required*]           | string    | ID of the organization.                                                                                                                   |
| data               | type [*required*]         | enum      | Organizations resource type. Allowed enum values: `orgs`                                                                                  |
| relationships      | other_orgs                     | object    | Relationship to organizations.                                                                                                            |
| other_orgs         | data [*required*]         | [object]  | Relationships to organization objects.                                                                                                    |
| data               | id [*required*]           | string    | ID of the organization.                                                                                                                   |
| data               | type [*required*]         | enum      | Organizations resource type. Allowed enum values: `orgs`                                                                                  |
| relationships      | other_users                    | object    | Relationship to users.                                                                                                                    |
| other_users        | data [*required*]         | [object]  | Relationships to user objects.                                                                                                            |
| data               | id [*required*]           | string    | A unique identifier that represents the user.                                                                                             |
| data               | type [*required*]         | enum      | Users resource type. Allowed enum values: `users`                                                                                         |
| relationships      | roles                          | object    | Relationship to roles.                                                                                                                    |
| roles              | data                           | [object]  | An array containing type and the unique identifier of a role.                                                                             |
| data               | id                             | string    | The unique identifier of the role.                                                                                                        |
| data               | type                           | enum      | Roles type. Allowed enum values: `roles`                                                                                                  |
| included           | type                           | enum      | Users resource type. Allowed enum values: `users`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
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
```text

{% /tab %}

{% /tab %}

{% tab title="404" %}
Powerpack Not Found.
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
                  \# Path parametersexport powerpack_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/powerpacks/${powerpack_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get a Powerpack returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::PowerpackAPI.new

# there is a valid "powerpack" in the system
POWERPACK_DATA_ID = ENV["POWERPACK_DATA_ID"]
p api_instance.get_powerpack(POWERPACK_DATA_ID)
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update a powerpack{% #update-a-powerpack %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/powerpacks/{powerpack_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/powerpacks/{powerpack_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/powerpacks/{powerpack_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/powerpacks/{powerpack_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/powerpacks/{powerpack_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/powerpacks/{powerpack_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/powerpacks/{powerpack_id} |

### Overview

Update a powerpack. This endpoint requires the `dashboards_write` permission.

OAuth apps require the `dashboards_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#powerpack) to access this endpoint.



### Arguments

#### Path Parameters

| Name                           | Type   | Description          |
| ------------------------------ | ------ | -------------------- |
| powerpack_id [*required*] | string | ID of the powerpack. |

### Request

#### Body Data (required)

Update a powerpack request body.

{% tab title="Model" %}

| Parent field       | Field                          | Type     | Description                                                                                                                               |
| ------------------ | ------------------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                           | object   | Powerpack data object.                                                                                                                    |
| data               | attributes                     | object   | Powerpack attribute object.                                                                                                               |
| attributes         | description                    | string   | Description of this powerpack.                                                                                                            |
| attributes         | group_widget [*required*] | object   | Powerpack group widget definition object.                                                                                                 |
| group_widget       | definition [*required*]   | object   | Powerpack group widget object.                                                                                                            |
| definition         | layout_type [*required*]  | string   | Layout type of widgets.                                                                                                                   |
| definition         | show_title                     | boolean  | Boolean indicating whether powerpack group title should be visible or not.                                                                |
| definition         | title                          | string   | Name for the group widget.                                                                                                                |
| definition         | type [*required*]         | string   | Type of widget, must be group.                                                                                                            |
| definition         | widgets [*required*]      | [object] | Widgets inside the powerpack.                                                                                                             |
| widgets            | definition [*required*]   | object   | Information about widget.                                                                                                                 |
| widgets            | layout                         | object   | Powerpack inner widget layout.                                                                                                            |
| layout             | height [*required*]       | int64    | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64    | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64    | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64    | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | layout                         | object   | Powerpack group widget layout.                                                                                                            |
| layout             | height [*required*]       | int64    | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64    | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64    | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64    | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | live_span                      | enum     | The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert` |
| attributes         | name [*required*]         | string   | Name of the powerpack.                                                                                                                    |
| attributes         | tags                           | [string] | List of tags to identify this powerpack.                                                                                                  |
| attributes         | template_variables             | [object] | List of template variables for this powerpack.                                                                                            |
| template_variables | available_values               | [string] | The list of values that the template variable drop-down is limited to.                                                                    |
| template_variables | defaults                       | [string] | One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.  |
| template_variables | name [*required*]         | string   | The name of the variable.                                                                                                                 |
| template_variables | prefix                         | string   | The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.                                 |
| data               | id                             | string   | ID of the powerpack.                                                                                                                      |
| data               | relationships                  | object   | Powerpack relationship object.                                                                                                            |
| relationships      | author                         | object   | Relationship to user.                                                                                                                     |
| author             | data [*required*]         | object   | Relationship to user object.                                                                                                              |
| data               | id [*required*]           | string   | A unique identifier that represents the user.                                                                                             |
| data               | type [*required*]         | enum     | Users resource type. Allowed enum values: `users`                                                                                         |
| data               | type                           | string   | Type of widget, must be powerpack.                                                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
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
```text

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object which includes a single powerpack configuration.

| Parent field       | Field                          | Type      | Description                                                                                                                               |
| ------------------ | ------------------------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|                    | data                           | object    | Powerpack data object.                                                                                                                    |
| data               | attributes                     | object    | Powerpack attribute object.                                                                                                               |
| attributes         | description                    | string    | Description of this powerpack.                                                                                                            |
| attributes         | group_widget [*required*] | object    | Powerpack group widget definition object.                                                                                                 |
| group_widget       | definition [*required*]   | object    | Powerpack group widget object.                                                                                                            |
| definition         | layout_type [*required*]  | string    | Layout type of widgets.                                                                                                                   |
| definition         | show_title                     | boolean   | Boolean indicating whether powerpack group title should be visible or not.                                                                |
| definition         | title                          | string    | Name for the group widget.                                                                                                                |
| definition         | type [*required*]         | string    | Type of widget, must be group.                                                                                                            |
| definition         | widgets [*required*]      | [object]  | Widgets inside the powerpack.                                                                                                             |
| widgets            | definition [*required*]   | object    | Information about widget.                                                                                                                 |
| widgets            | layout                         | object    | Powerpack inner widget layout.                                                                                                            |
| layout             | height [*required*]       | int64     | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64     | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64     | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64     | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | layout                         | object    | Powerpack group widget layout.                                                                                                            |
| layout             | height [*required*]       | int64     | The height of the widget. Should be a non-negative integer.                                                                               |
| layout             | width [*required*]        | int64     | The width of the widget. Should be a non-negative integer.                                                                                |
| layout             | x [*required*]            | int64     | The position of the widget on the x (horizontal) axis. Should be a non-negative integer.                                                  |
| layout             | y [*required*]            | int64     | The position of the widget on the y (vertical) axis. Should be a non-negative integer.                                                    |
| group_widget       | live_span                      | enum      | The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,1y,alert` |
| attributes         | name [*required*]         | string    | Name of the powerpack.                                                                                                                    |
| attributes         | tags                           | [string]  | List of tags to identify this powerpack.                                                                                                  |
| attributes         | template_variables             | [object]  | List of template variables for this powerpack.                                                                                            |
| template_variables | available_values               | [string]  | The list of values that the template variable drop-down is limited to.                                                                    |
| template_variables | defaults                       | [string]  | One or many template variable default values within the saved view, which are unioned together using `OR` if more than one is specified.  |
| template_variables | name [*required*]         | string    | The name of the variable.                                                                                                                 |
| template_variables | prefix                         | string    | The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.                                 |
| data               | id                             | string    | ID of the powerpack.                                                                                                                      |
| data               | relationships                  | object    | Powerpack relationship object.                                                                                                            |
| relationships      | author                         | object    | Relationship to user.                                                                                                                     |
| author             | data [*required*]         | object    | Relationship to user object.                                                                                                              |
| data               | id [*required*]           | string    | A unique identifier that represents the user.                                                                                             |
| data               | type [*required*]         | enum      | Users resource type. Allowed enum values: `users`                                                                                         |
| data               | type                           | string    | Type of widget, must be powerpack.                                                                                                        |
|                    | included                       | [object]  | Array of objects related to the users.                                                                                                    |
| included           | attributes                     | object    | Attributes of user object returned by the API.                                                                                            |
| attributes         | created_at                     | date-time | Creation time of the user.                                                                                                                |
| attributes         | disabled                       | boolean   | Whether the user is disabled.                                                                                                             |
| attributes         | email                          | string    | Email of the user.                                                                                                                        |
| attributes         | handle                         | string    | Handle of the user.                                                                                                                       |
| attributes         | icon                           | string    | URL of the user's icon.                                                                                                                   |
| attributes         | last_login_time                | date-time | The last time the user logged in.                                                                                                         |
| attributes         | mfa_enabled                    | boolean   | If user has MFA enabled.                                                                                                                  |
| attributes         | modified_at                    | date-time | Time that the user was last modified.                                                                                                     |
| attributes         | name                           | string    | Name of the user.                                                                                                                         |
| attributes         | service_account                | boolean   | Whether the user is a service account.                                                                                                    |
| attributes         | status                         | string    | Status of the user.                                                                                                                       |
| attributes         | title                          | string    | Title of the user.                                                                                                                        |
| attributes         | verified                       | boolean   | Whether the user is verified.                                                                                                             |
| included           | id                             | string    | ID of the user.                                                                                                                           |
| included           | relationships                  | object    | Relationships of the user object returned by the API.                                                                                     |
| relationships      | org                            | object    | Relationship to an organization.                                                                                                          |
| org                | data [*required*]         | object    | Relationship to organization object.                                                                                                      |
| data               | id [*required*]           | string    | ID of the organization.                                                                                                                   |
| data               | type [*required*]         | enum      | Organizations resource type. Allowed enum values: `orgs`                                                                                  |
| relationships      | other_orgs                     | object    | Relationship to organizations.                                                                                                            |
| other_orgs         | data [*required*]         | [object]  | Relationships to organization objects.                                                                                                    |
| data               | id [*required*]           | string    | ID of the organization.                                                                                                                   |
| data               | type [*required*]         | enum      | Organizations resource type. Allowed enum values: `orgs`                                                                                  |
| relationships      | other_users                    | object    | Relationship to users.                                                                                                                    |
| other_users        | data [*required*]         | [object]  | Relationships to user objects.                                                                                                            |
| data               | id [*required*]           | string    | A unique identifier that represents the user.                                                                                             |
| data               | type [*required*]         | enum      | Users resource type. Allowed enum values: `users`                                                                                         |
| relationships      | roles                          | object    | Relationship to roles.                                                                                                                    |
| roles              | data                           | [object]  | An array containing type and the unique identifier of a role.                                                                             |
| data               | id                             | string    | The unique identifier of the role.                                                                                                        |
| data               | type                           | enum      | Roles type. Allowed enum values: `roles`                                                                                                  |
| included           | type                           | enum      | Users resource type. Allowed enum values: `users`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
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
```text

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
```text

{% /tab %}

{% /tab %}

{% tab title="404" %}
Powerpack Not Found
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
                          \# Path parametersexport powerpack_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/powerpacks/${powerpack_id}" \
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

#####

```go
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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
```text

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
