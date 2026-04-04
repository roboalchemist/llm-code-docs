# Source: https://docs.datadoghq.com/api/latest/status-pages.md

---
title: Status Pages
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Status Pages
---

Manage your status pages and communicate service disruptions to stakeholders via Datadog's API. See the [Status Pages documentation](https://docs.datadoghq.com/incident_response/status_pages/) for more information.

## Create status page{% #create-status-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/statuspages |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/statuspages |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/statuspages      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/statuspages      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/statuspages     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/statuspages |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/statuspages |

### Overview

Creates a new status page. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Query Strings

| Name    | Type   | Description                                                                                             |
| ------- | ------ | ------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user. |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                                | Type     | Description                                                                                                                                             |
| ------------ | ------------------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                                 | object   |
| data         | attributes [*required*]         | object   | The supported attributes for creating a status page.                                                                                                    |
| attributes   | company_logo                         | string   | The base64-encoded image data displayed on the status page.                                                                                             |
| attributes   | components                           | [object] | The components displayed on the status page.                                                                                                            |
| components   | components                           | [object] | If creating a component of type `group`, the components to create within the group.                                                                     |
| components   | id                                   | uuid     | The ID of the grouped component.                                                                                                                        |
| components   | name                                 | string   | The name of the grouped component.                                                                                                                      |
| components   | position                             | int64    | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components   | status                               | enum     | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components   | type                                 | enum     | The type of the component. Allowed enum values: `component`                                                                                             |
| components   | id                                   | uuid     | The ID of the component.                                                                                                                                |
| components   | name                                 | string   | The name of the component.                                                                                                                              |
| components   | position                             | int64    | The zero-indexed position of the component.                                                                                                             |
| components   | status                               | enum     | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components   | type                                 | enum     | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes   | domain_prefix [*required*]      | string   | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes   | email_header_image                   | string   | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes   | enabled [*required*]            | boolean  | Whether the status page is enabled.                                                                                                                     |
| attributes   | favicon                              | string   | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes   | name [*required*]               | string   | The name of the status page.                                                                                                                            |
| attributes   | subscriptions_enabled                | boolean  | Whether users can subscribe to the status page.                                                                                                         |
| attributes   | type [*required*]               | enum     | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes   | visualization_type [*required*] | enum     | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data         | type [*required*]               | enum     | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "A Status Page",
      "domain_prefix": "5e2fd69be33e79aa",
      "components": [
        {
          "name": "Login",
          "type": "component",
          "position": 0
        },
        {
          "name": "Settings",
          "type": "component",
          "position": 1
        }
      ],
      "enabled": true,
      "type": "internal",
      "visualization_type": "bars_and_uptime_percentage"
    },
    "type": "status_pages"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | Base64-encoded image data displayed on the status page.                                                                                                 |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component. Relative to the other components in the group.                                                              |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data                  | id                     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
|                       | included               | [ <oneOf>] | The included related resources of a status page. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "company_logo": "string",
      "components": [
        {
          "components": [
            {
              "id": "string",
              "name": "string",
              "position": "integer",
              "status": "string",
              "type": "component"
            }
          ],
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_domain": "string",
      "custom_domain_enabled": false,
      "domain_prefix": "string",
      "email_header_image": "string",
      "enabled": false,
      "favicon": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "page_url": "string",
      "subscriptions_enabled": false,
      "type": "public",
      "visualization_type": "bars_and_uptime_percentage"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      }
    },
    "type": "status_pages"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "A Status Page",
      "domain_prefix": "5e2fd69be33e79aa",
      "components": [
        {
          "name": "Login",
          "type": "component",
          "position": 0
        },
        {
          "name": "Settings",
          "type": "component",
          "position": 1
        }
      ],
      "enabled": true,
      "type": "internal",
      "visualization_type": "bars_and_uptime_percentage"
    },
    "type": "status_pages"
  }
}
EOF

#####

```go
// Create status page returns "Created" response

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
    body := datadogV2.CreateStatusPageRequest{
        Data: &datadogV2.CreateStatusPageRequestData{
            Attributes: datadogV2.CreateStatusPageRequestDataAttributes{
                Name:         "A Status Page",
                DomainPrefix: "5e2fd69be33e79aa",
                Components: []datadogV2.CreateStatusPageRequestDataAttributesComponentsItems{
                    {
                        Name:     datadog.PtrString("Login"),
                        Type:     datadogV2.CREATECOMPONENTREQUESTDATAATTRIBUTESTYPE_COMPONENT.Ptr(),
                        Position: datadog.PtrInt64(0),
                    },
                    {
                        Name:     datadog.PtrString("Settings"),
                        Type:     datadogV2.CREATECOMPONENTREQUESTDATAATTRIBUTESTYPE_COMPONENT.Ptr(),
                        Position: datadog.PtrInt64(1),
                    },
                },
                Enabled:           true,
                Type:              datadogV2.CREATESTATUSPAGEREQUESTDATAATTRIBUTESTYPE_INTERNAL,
                VisualizationType: datadogV2.CREATESTATUSPAGEREQUESTDATAATTRIBUTESVISUALIZATIONTYPE_BARS_AND_UPTIME_PERCENTAGE,
            },
            Type: datadogV2.STATUSPAGEDATATYPE_STATUS_PAGES,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.CreateStatusPage(ctx, body, *datadogV2.NewCreateStatusPageOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.CreateStatusPage`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.CreateStatusPage`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create status page returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.CreateComponentRequestDataAttributesType;
import com.datadog.api.client.v2.model.CreateStatusPageRequest;
import com.datadog.api.client.v2.model.CreateStatusPageRequestData;
import com.datadog.api.client.v2.model.CreateStatusPageRequestDataAttributes;
import com.datadog.api.client.v2.model.CreateStatusPageRequestDataAttributesComponentsItems;
import com.datadog.api.client.v2.model.CreateStatusPageRequestDataAttributesType;
import com.datadog.api.client.v2.model.CreateStatusPageRequestDataAttributesVisualizationType;
import com.datadog.api.client.v2.model.StatusPage;
import com.datadog.api.client.v2.model.StatusPageDataType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    CreateStatusPageRequest body =
        new CreateStatusPageRequest()
            .data(
                new CreateStatusPageRequestData()
                    .attributes(
                        new CreateStatusPageRequestDataAttributes()
                            .name("A Status Page")
                            .domainPrefix("5e2fd69be33e79aa")
                            .components(
                                Arrays.asList(
                                    new CreateStatusPageRequestDataAttributesComponentsItems()
                                        .name("Login")
                                        .type(CreateComponentRequestDataAttributesType.COMPONENT)
                                        .position(0L),
                                    new CreateStatusPageRequestDataAttributesComponentsItems()
                                        .name("Settings")
                                        .type(CreateComponentRequestDataAttributesType.COMPONENT)
                                        .position(1L)))
                            .enabled(true)
                            .type(CreateStatusPageRequestDataAttributesType.INTERNAL)
                            .visualizationType(
                                CreateStatusPageRequestDataAttributesVisualizationType
                                    .BARS_AND_UPTIME_PERCENTAGE))
                    .type(StatusPageDataType.STATUS_PAGES));

    try {
      StatusPage result = apiInstance.createStatusPage(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#createStatusPage");
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
Create status page returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_component_request_data_attributes_type import (
    CreateComponentRequestDataAttributesType,
)
from datadog_api_client.v2.model.create_status_page_request import CreateStatusPageRequest
from datadog_api_client.v2.model.create_status_page_request_data import CreateStatusPageRequestData
from datadog_api_client.v2.model.create_status_page_request_data_attributes import CreateStatusPageRequestDataAttributes
from datadog_api_client.v2.model.create_status_page_request_data_attributes_components_items import (
    CreateStatusPageRequestDataAttributesComponentsItems,
)
from datadog_api_client.v2.model.create_status_page_request_data_attributes_type import (
    CreateStatusPageRequestDataAttributesType,
)
from datadog_api_client.v2.model.create_status_page_request_data_attributes_visualization_type import (
    CreateStatusPageRequestDataAttributesVisualizationType,
)
from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType

body = CreateStatusPageRequest(
    data=CreateStatusPageRequestData(
        attributes=CreateStatusPageRequestDataAttributes(
            name="A Status Page",
            domain_prefix="5e2fd69be33e79aa",
            components=[
                CreateStatusPageRequestDataAttributesComponentsItems(
                    name="Login",
                    type=CreateComponentRequestDataAttributesType.COMPONENT,
                    position=0,
                ),
                CreateStatusPageRequestDataAttributesComponentsItems(
                    name="Settings",
                    type=CreateComponentRequestDataAttributesType.COMPONENT,
                    position=1,
                ),
            ],
            enabled=True,
            type=CreateStatusPageRequestDataAttributesType.INTERNAL,
            visualization_type=CreateStatusPageRequestDataAttributesVisualizationType.BARS_AND_UPTIME_PERCENTAGE,
        ),
        type=StatusPageDataType.STATUS_PAGES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_status_page(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create status page returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

body = DatadogAPIClient::V2::CreateStatusPageRequest.new({
  data: DatadogAPIClient::V2::CreateStatusPageRequestData.new({
    attributes: DatadogAPIClient::V2::CreateStatusPageRequestDataAttributes.new({
      name: "A Status Page",
      domain_prefix: "5e2fd69be33e79aa",
      components: [
        DatadogAPIClient::V2::CreateStatusPageRequestDataAttributesComponentsItems.new({
          name: "Login",
          type: DatadogAPIClient::V2::CreateComponentRequestDataAttributesType::COMPONENT,
          position: 0,
        }),
        DatadogAPIClient::V2::CreateStatusPageRequestDataAttributesComponentsItems.new({
          name: "Settings",
          type: DatadogAPIClient::V2::CreateComponentRequestDataAttributesType::COMPONENT,
          position: 1,
        }),
      ],
      enabled: true,
      type: DatadogAPIClient::V2::CreateStatusPageRequestDataAttributesType::INTERNAL,
      visualization_type: DatadogAPIClient::V2::CreateStatusPageRequestDataAttributesVisualizationType::BARS_AND_UPTIME_PERCENTAGE,
    }),
    type: DatadogAPIClient::V2::StatusPageDataType::STATUS_PAGES,
  }),
})
p api_instance.create_status_page(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create status page returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::CreateStatusPageOptionalParams;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;
use datadog_api_client::datadogV2::model::CreateComponentRequestDataAttributesType;
use datadog_api_client::datadogV2::model::CreateStatusPageRequest;
use datadog_api_client::datadogV2::model::CreateStatusPageRequestData;
use datadog_api_client::datadogV2::model::CreateStatusPageRequestDataAttributes;
use datadog_api_client::datadogV2::model::CreateStatusPageRequestDataAttributesComponentsItems;
use datadog_api_client::datadogV2::model::CreateStatusPageRequestDataAttributesType;
use datadog_api_client::datadogV2::model::CreateStatusPageRequestDataAttributesVisualizationType;
use datadog_api_client::datadogV2::model::StatusPageDataType;

#[tokio::main]
async fn main() {
    let body = CreateStatusPageRequest::new().data(CreateStatusPageRequestData::new(
        CreateStatusPageRequestDataAttributes::new(
            "5e2fd69be33e79aa".to_string(),
            true,
            "A Status Page".to_string(),
            CreateStatusPageRequestDataAttributesType::INTERNAL,
            CreateStatusPageRequestDataAttributesVisualizationType::BARS_AND_UPTIME_PERCENTAGE,
        )
        .components(vec![
            CreateStatusPageRequestDataAttributesComponentsItems::new()
                .name("Login".to_string())
                .position(0)
                .type_(CreateComponentRequestDataAttributesType::COMPONENT),
            CreateStatusPageRequestDataAttributesComponentsItems::new()
                .name("Settings".to_string())
                .position(1)
                .type_(CreateComponentRequestDataAttributesType::COMPONENT),
        ]),
        StatusPageDataType::STATUS_PAGES,
    ));
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .create_status_page(body, CreateStatusPageOptionalParams::default())
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
 * Create status page returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

const params: v2.StatusPagesApiCreateStatusPageRequest = {
  body: {
    data: {
      attributes: {
        name: "A Status Page",
        domainPrefix: "5e2fd69be33e79aa",
        components: [
          {
            name: "Login",
            type: "component",
            position: 0,
          },
          {
            name: "Settings",
            type: "component",
            position: 1,
          },
        ],
        enabled: true,
        type: "internal",
        visualizationType: "bars_and_uptime_percentage",
      },
      type: "status_pages",
    },
  },
};

apiInstance
  .createStatusPage(params)
  .then((data: v2.StatusPage) => {
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

## Update status page{% #update-status-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/statuspages/{page_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/statuspages/{page_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/statuspages/{page_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/statuspages/{page_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/statuspages/{page_id} |

### Overview

Updates an existing status page's attributes. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

#### Query Strings

| Name               | Type    | Description                                                                                             |
| ------------------ | ------- | ------------------------------------------------------------------------------------------------------- |
| delete_subscribers | boolean | Whether to delete existing subscribers when updating a status page's type.                              |
| include            | string  | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user. |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                                                                                                             |
| ------------ | ---------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object  |
| data         | attributes [*required*] | object  | The supported attributes for updating a status page.                                                                                                    |
| attributes   | company_logo                 | string  | The base64-encoded image data displayed on the status page.                                                                                             |
| attributes   | domain_prefix                | string  | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes   | email_header_image           | string  | The base64-encoded image data displayed in email notifications sent to status page subscribers.                                                         |
| attributes   | enabled                      | boolean | Whether the status page is enabled.                                                                                                                     |
| attributes   | favicon                      | string  | The base64-encoded image data displayed in the browser tab.                                                                                             |
| attributes   | name                         | string  | The name of the status page.                                                                                                                            |
| attributes   | subscriptions_enabled        | boolean | Whether users can subscribe to the status page.                                                                                                         |
| attributes   | type                         | enum    | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes   | visualization_type           | enum    | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data         | id [*required*]         | uuid    | The ID of the status page.                                                                                                                              |
| data         | type [*required*]       | enum    | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "A Status Page in US1"
    },
    "id": "string",
    "type": "status_pages"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | Base64-encoded image data displayed on the status page.                                                                                                 |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component. Relative to the other components in the group.                                                              |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data                  | id                     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
|                       | included               | [ <oneOf>] | The included related resources of a status page. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "company_logo": "string",
      "components": [
        {
          "components": [
            {
              "id": "string",
              "name": "string",
              "position": "integer",
              "status": "string",
              "type": "component"
            }
          ],
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_domain": "string",
      "custom_domain_enabled": false,
      "domain_prefix": "string",
      "email_header_image": "string",
      "enabled": false,
      "favicon": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "page_url": "string",
      "subscriptions_enabled": false,
      "type": "public",
      "visualization_type": "bars_and_uptime_percentage"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      }
    },
    "type": "status_pages"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "A Status Page in US1"
    },
    "id": "string",
    "type": "status_pages"
  }
}
EOF

#####

```go
// Update status page returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    body := datadogV2.PatchStatusPageRequest{
        Data: &datadogV2.PatchStatusPageRequestData{
            Attributes: datadogV2.PatchStatusPageRequestDataAttributes{
                Name: datadog.PtrString("A Status Page in US1"),
            },
            Id:   StatusPageDataID,
            Type: datadogV2.STATUSPAGEDATATYPE_STATUS_PAGES,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.UpdateStatusPage(ctx, StatusPageDataID, body, *datadogV2.NewUpdateStatusPageOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.UpdateStatusPage`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.UpdateStatusPage`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update status page returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.PatchStatusPageRequest;
import com.datadog.api.client.v2.model.PatchStatusPageRequestData;
import com.datadog.api.client.v2.model.PatchStatusPageRequestDataAttributes;
import com.datadog.api.client.v2.model.StatusPage;
import com.datadog.api.client.v2.model.StatusPageDataType;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    PatchStatusPageRequest body =
        new PatchStatusPageRequest()
            .data(
                new PatchStatusPageRequestData()
                    .attributes(
                        new PatchStatusPageRequestDataAttributes().name("A Status Page in US1"))
                    .id(STATUS_PAGE_DATA_ID)
                    .type(StatusPageDataType.STATUS_PAGES));

    try {
      StatusPage result = apiInstance.updateStatusPage(STATUS_PAGE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#updateStatusPage");
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
Update status page returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.patch_status_page_request import PatchStatusPageRequest
from datadog_api_client.v2.model.patch_status_page_request_data import PatchStatusPageRequestData
from datadog_api_client.v2.model.patch_status_page_request_data_attributes import PatchStatusPageRequestDataAttributes
from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

body = PatchStatusPageRequest(
    data=PatchStatusPageRequestData(
        attributes=PatchStatusPageRequestDataAttributes(
            name="A Status Page in US1",
        ),
        id=STATUS_PAGE_DATA_ID,
        type=StatusPageDataType.STATUS_PAGES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.update_status_page(page_id=STATUS_PAGE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update status page returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]

body = DatadogAPIClient::V2::PatchStatusPageRequest.new({
  data: DatadogAPIClient::V2::PatchStatusPageRequestData.new({
    attributes: DatadogAPIClient::V2::PatchStatusPageRequestDataAttributes.new({
      name: "A Status Page in US1",
    }),
    id: STATUS_PAGE_DATA_ID,
    type: DatadogAPIClient::V2::StatusPageDataType::STATUS_PAGES,
  }),
})
p api_instance.update_status_page(STATUS_PAGE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update status page returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;
use datadog_api_client::datadogV2::api_status_pages::UpdateStatusPageOptionalParams;
use datadog_api_client::datadogV2::model::PatchStatusPageRequest;
use datadog_api_client::datadogV2::model::PatchStatusPageRequestData;
use datadog_api_client::datadogV2::model::PatchStatusPageRequestDataAttributes;
use datadog_api_client::datadogV2::model::StatusPageDataType;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let body = PatchStatusPageRequest::new().data(PatchStatusPageRequestData::new(
        PatchStatusPageRequestDataAttributes::new().name("A Status Page in US1".to_string()),
        status_page_data_id.clone(),
        StatusPageDataType::STATUS_PAGES,
    ));
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .update_status_page(
            status_page_data_id.clone(),
            body,
            UpdateStatusPageOptionalParams::default(),
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
 * Update status page returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

const params: v2.StatusPagesApiUpdateStatusPageRequest = {
  body: {
    data: {
      attributes: {
        name: "A Status Page in US1",
      },
      id: STATUS_PAGE_DATA_ID,
      type: "status_pages",
    },
  },
  pageId: STATUS_PAGE_DATA_ID,
};

apiInstance
  .updateStatusPage(params)
  .then((data: v2.StatusPage) => {
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

## List status pages{% #list-status-pages %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages |

### Overview

Lists all status pages for the organization. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Query Strings

| Name         | Type    | Description                                                                                             |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------- |
| page[offset] | integer | Offset to use as the start of the page.                                                                 |
| page[limit]  | integer | The number of status pages to return per page.                                                          |
| include      | string  | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data [*required*] | [object]        |
| data                  | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | Base64-encoded image data displayed on the status page.                                                                                                 |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component. Relative to the other components in the group.                                                              |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data                  | id                     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
|                       | included               | [ <oneOf>] | The included related resources of a status page. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
|                       | meta                   | object          | Response metadata.                                                                                                                                      |
| meta                  | page                   | object          | Offset-based pagination schema.                                                                                                                         |
| page                  | first_offset           | int64           | Integer representing the offset to fetch the first page of results.                                                                                     |
| page                  | last_offset            | int64           | Integer representing the offset to fetch the last page of results.                                                                                      |
| page                  | limit                  | int64           | Integer representing the number of elements to returned in the results.                                                                                 |
| page                  | next_offset            | int64           | Integer representing the index of the first element in the next page of results. Equal to page size added to the current offset.                        |
| page                  | offset                 | int64           | Integer representing the index of the first element in the results.                                                                                     |
| page                  | prev_offset            | int64           | Integer representing the index of the first element in the previous page of results.                                                                    |
| page                  | total                  | int64           | Integer representing the total number of elements available.                                                                                            |
| page                  | type                   | enum            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "company_logo": "string",
        "components": [
          {
            "components": [
              {
                "id": "string",
                "name": "string",
                "position": "integer",
                "status": "string",
                "type": "component"
              }
            ],
            "id": "string",
            "name": "string",
            "position": "integer",
            "status": "string",
            "type": "component"
          }
        ],
        "created_at": "2019-09-19T10:00:00.000Z",
        "custom_domain": "string",
        "custom_domain_enabled": false,
        "domain_prefix": "string",
        "email_header_image": "string",
        "enabled": false,
        "favicon": "string",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "page_url": "string",
        "subscriptions_enabled": false,
        "type": "public",
        "visualization_type": "bars_and_uptime_percentage"
      },
      "id": "string",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        }
      },
      "type": "status_pages"
    }
  ],
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
    }
  ],
  "meta": {
    "page": {
      "first_offset": 0,
      "last_offset": 900,
      "limit": 100,
      "next_offset": 100,
      "offset": 0,
      "prev_offset": 100,
      "total": 1000,
      "type": "offset_limit"
    }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List status pages returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.list_status_pages()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new
p api_instance.list_status_pages()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List status pages returns "OK" response

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
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.ListStatusPages(ctx, *datadogV2.NewListStatusPagesOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.ListStatusPages`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.ListStatusPages`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List status pages returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.StatusPageArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    try {
      StatusPageArray result = apiInstance.listStatusPages();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#listStatusPages");
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
// List status pages returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::ListStatusPagesOptionalParams;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .list_status_pages(ListStatusPagesOptionalParams::default())
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
 * List status pages returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

apiInstance
  .listStatusPages()
  .then((data: v2.StatusPageArray) => {
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

## Get status page{% #get-status-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages/{page_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages/{page_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages/{page_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages/{page_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages/{page_id} |

### Overview

Retrieves a specific status page by its ID. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

#### Query Strings

| Name    | Type   | Description                                                                                             |
| ------- | ------ | ------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | Base64-encoded image data displayed on the status page.                                                                                                 |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component. Relative to the other components in the group.                                                              |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data                  | id                     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
|                       | included               | [ <oneOf>] | The included related resources of a status page. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "company_logo": "string",
      "components": [
        {
          "components": [
            {
              "id": "string",
              "name": "string",
              "position": "integer",
              "status": "string",
              "type": "component"
            }
          ],
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_domain": "string",
      "custom_domain_enabled": false,
      "domain_prefix": "string",
      "email_header_image": "string",
      "enabled": false,
      "favicon": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "page_url": "string",
      "subscriptions_enabled": false,
      "type": "public",
      "visualization_type": "bars_and_uptime_percentage"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      }
    },
    "type": "status_pages"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get status page returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.get_status_page(
        page_id=STATUS_PAGE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get status page returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]
p api_instance.get_status_page(STATUS_PAGE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get status page returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.GetStatusPage(ctx, StatusPageDataID, *datadogV2.NewGetStatusPageOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.GetStatusPage`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.GetStatusPage`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get status page returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.StatusPage;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      StatusPage result = apiInstance.getStatusPage(STATUS_PAGE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#getStatusPage");
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
// Get status page returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::GetStatusPageOptionalParams;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .get_status_page(
            status_page_data_id.clone(),
            GetStatusPageOptionalParams::default(),
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
 * Get status page returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

const params: v2.StatusPagesApiGetStatusPageRequest = {
  pageId: STATUS_PAGE_DATA_ID,
};

apiInstance
  .getStatusPage(params)
  .then((data: v2.StatusPage) => {
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

## Delete status page{% #delete-status-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/statuspages/{page_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/statuspages/{page_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/statuspages/{page_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/statuspages/{page_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/statuspages/{page_id} |

### Overview

Deletes a status page by its ID. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete status page returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    api_instance.delete_status_page(
        page_id=STATUS_PAGE_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete status page returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]
api_instance.delete_status_page(STATUS_PAGE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete status page returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    r, err := api.DeleteStatusPage(ctx, StatusPageDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.DeleteStatusPage`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete status page returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      apiInstance.deleteStatusPage(STATUS_PAGE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#deleteStatusPage");
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
// Delete status page returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api.delete_status_page(status_page_data_id.clone()).await;
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
 * Delete status page returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

const params: v2.StatusPagesApiDeleteStatusPageRequest = {
  pageId: STATUS_PAGE_DATA_ID,
};

apiInstance
  .deleteStatusPage(params)
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

## Create component{% #create-component %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/components |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/components |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/statuspages/{page_id}/components      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/statuspages/{page_id}/components      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/statuspages/{page_id}/components     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/components |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/components |

### Overview

Creates a new component. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

#### Query Strings

| Name    | Type   | Description                                                                                                                 |
| ------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group. |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field  | Field                        | Type     | Description                                                                                       |
| ------------- | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------- |
|               | data                         | object   |
| data          | attributes [*required*] | object   | The supported attributes for creating a component.                                                |
| attributes    | components                   | [object] | If creating a component of type `group`, the components to create within the group.               |
| components    | name [*required*]       | string   | The name of the grouped component.                                                                |
| components    | position [*required*]   | int64    | The zero-indexed position of the grouped component relative to the other components in the group. |
| components    | type [*required*]       | enum     | The type of the component. Allowed enum values: `component`                                       |
| attributes    | name [*required*]       | string   | The name of the component.                                                                        |
| attributes    | position [*required*]   | int64    | The zero-indexed position of the component.                                                       |
| attributes    | type [*required*]       | enum     | The type of the component. Allowed enum values: `component,group`                                 |
| data          | relationships                | object   | The supported relationships for creating a component.                                             |
| relationships | group                        | object   | The group to create the component within.                                                         |
| group         | data [*required*]       | object   |
| data          | id [*required*]         | uuid     | The ID of the group.                                                                              |
| data          | type [*required*]       | enum     | Components resource type. Allowed enum values: `components`                                       |
| data          | type [*required*]       | enum     | Components resource type. Allowed enum values: `components`                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "Logs",
      "position": 0,
      "type": "component"
    },
    "type": "components"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a component.                                                                                                                          |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            |
| components            | name                   | string          |
| components            | position               | int64           |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| data                  | id                     | uuid            | The ID of the component.                                                                                                                                |
| data                  | relationships          | object          | The relationships of a component.                                                                                                                       |
| relationships         | created_by_user        | object          | The Datadog user who created the component.                                                                                                             |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component.                                                                                                   |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component belongs to.                                                                                                                     |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the group the component belongs to.                                                                                                           |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component.                                                                                                       |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component belongs to.                                                                                                               |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page the component belongs to.                                                                                                     |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
|                       | included               | [ <oneOf>] | The included related resources of a component. Client must explicitly request these resources by name in the `include` query parameter.                 |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2               | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                     | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| included              | Option 3               | object          | The included component group resource.                                                                                                                  |
| Option 3              | attributes             | object          | The attributes of a component group.                                                                                                                    |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| Option 3              | id                     | uuid            | The ID of the component.                                                                                                                                |
| Option 3              | relationships          | object          | The relationships of a component group.                                                                                                                 |
| relationships         | created_by_user        | object          | The Datadog user who created the component group.                                                                                                       |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component group.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component group belongs to.                                                                                                               |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component group.                                                                                                 |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component group.                                                                                       |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component group belongs to.                                                                                                         |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| Option 3              | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components": [
        {
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "position": "integer",
      "status": "operational",
      "type": "component"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "group": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "components"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "components"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/components" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Logs",
      "position": 0,
      "type": "component"
    },
    "type": "components"
  }
}
EOF

#####

```go
// Create component returns "Created" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    body := datadogV2.CreateComponentRequest{
        Data: &datadogV2.CreateComponentRequestData{
            Attributes: datadogV2.CreateComponentRequestDataAttributes{
                Name:     "Logs",
                Position: 0,
                Type:     datadogV2.CREATECOMPONENTREQUESTDATAATTRIBUTESTYPE_COMPONENT,
            },
            Type: datadogV2.STATUSPAGESCOMPONENTGROUPTYPE_COMPONENTS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.CreateComponent(ctx, StatusPageDataID, body, *datadogV2.NewCreateComponentOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.CreateComponent`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.CreateComponent`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create component returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.CreateComponentRequest;
import com.datadog.api.client.v2.model.CreateComponentRequestData;
import com.datadog.api.client.v2.model.CreateComponentRequestDataAttributes;
import com.datadog.api.client.v2.model.CreateComponentRequestDataAttributesType;
import com.datadog.api.client.v2.model.StatusPagesComponent;
import com.datadog.api.client.v2.model.StatusPagesComponentGroupType;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    CreateComponentRequest body =
        new CreateComponentRequest()
            .data(
                new CreateComponentRequestData()
                    .attributes(
                        new CreateComponentRequestDataAttributes()
                            .name("Logs")
                            .position(0L)
                            .type(CreateComponentRequestDataAttributesType.COMPONENT))
                    .type(StatusPagesComponentGroupType.COMPONENTS));

    try {
      StatusPagesComponent result = apiInstance.createComponent(STATUS_PAGE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#createComponent");
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
Create component returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_component_request import CreateComponentRequest
from datadog_api_client.v2.model.create_component_request_data import CreateComponentRequestData
from datadog_api_client.v2.model.create_component_request_data_attributes import CreateComponentRequestDataAttributes
from datadog_api_client.v2.model.create_component_request_data_attributes_type import (
    CreateComponentRequestDataAttributesType,
)
from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

body = CreateComponentRequest(
    data=CreateComponentRequestData(
        attributes=CreateComponentRequestDataAttributes(
            name="Logs",
            position=0,
            type=CreateComponentRequestDataAttributesType.COMPONENT,
        ),
        type=StatusPagesComponentGroupType.COMPONENTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_component(page_id=STATUS_PAGE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create component returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]

body = DatadogAPIClient::V2::CreateComponentRequest.new({
  data: DatadogAPIClient::V2::CreateComponentRequestData.new({
    attributes: DatadogAPIClient::V2::CreateComponentRequestDataAttributes.new({
      name: "Logs",
      position: 0,
      type: DatadogAPIClient::V2::CreateComponentRequestDataAttributesType::COMPONENT,
    }),
    type: DatadogAPIClient::V2::StatusPagesComponentGroupType::COMPONENTS,
  }),
})
p api_instance.create_component(STATUS_PAGE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create component returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::CreateComponentOptionalParams;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;
use datadog_api_client::datadogV2::model::CreateComponentRequest;
use datadog_api_client::datadogV2::model::CreateComponentRequestData;
use datadog_api_client::datadogV2::model::CreateComponentRequestDataAttributes;
use datadog_api_client::datadogV2::model::CreateComponentRequestDataAttributesType;
use datadog_api_client::datadogV2::model::StatusPagesComponentGroupType;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let body = CreateComponentRequest::new().data(CreateComponentRequestData::new(
        CreateComponentRequestDataAttributes::new(
            "Logs".to_string(),
            0,
            CreateComponentRequestDataAttributesType::COMPONENT,
        ),
        StatusPagesComponentGroupType::COMPONENTS,
    ));
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .create_component(
            status_page_data_id.clone(),
            body,
            CreateComponentOptionalParams::default(),
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
 * Create component returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

const params: v2.StatusPagesApiCreateComponentRequest = {
  body: {
    data: {
      attributes: {
        name: "Logs",
        position: 0,
        type: "component",
      },
      type: "components",
    },
  },
  pageId: STATUS_PAGE_DATA_ID,
};

apiInstance
  .createComponent(params)
  .then((data: v2.StatusPagesComponent) => {
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

## Update component{% #update-component %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |

### Overview

Updates an existing component's attributes. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                |
| ------------------------------ | ------ | -------------------------- |
| page_id [*required*]      | string | The ID of the status page. |
| component_id [*required*] | string | The ID of the component.   |

#### Query Strings

| Name    | Type   | Description                                                                                                                 |
| ------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group. |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                                                        |
| ------------ | ---------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object |
| data         | attributes [*required*] | object | The supported attributes for updating a component.                                                                                 |
| attributes   | name                         | string | The name of the component.                                                                                                         |
| attributes   | position                     | int64  | The position of the component. If the component belongs to a group, the position is relative to the other components in the group. |
| data         | id [*required*]         | uuid   | The ID of the component.                                                                                                           |
| data         | type [*required*]       | enum   | Components resource type. Allowed enum values: `components`                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "Logs Indexing"
    },
    "id": "c34e5b83-90fe-4de2-087b-ea1f64387277",
    "type": "components"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a component.                                                                                                                          |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            |
| components            | name                   | string          |
| components            | position               | int64           |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| data                  | id                     | uuid            | The ID of the component.                                                                                                                                |
| data                  | relationships          | object          | The relationships of a component.                                                                                                                       |
| relationships         | created_by_user        | object          | The Datadog user who created the component.                                                                                                             |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component.                                                                                                   |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component belongs to.                                                                                                                     |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the group the component belongs to.                                                                                                           |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component.                                                                                                       |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component belongs to.                                                                                                               |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page the component belongs to.                                                                                                     |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
|                       | included               | [ <oneOf>] | The included related resources of a component. Client must explicitly request these resources by name in the `include` query parameter.                 |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2               | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                     | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| included              | Option 3               | object          | The included component group resource.                                                                                                                  |
| Option 3              | attributes             | object          | The attributes of a component group.                                                                                                                    |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| Option 3              | id                     | uuid            | The ID of the component.                                                                                                                                |
| Option 3              | relationships          | object          | The relationships of a component group.                                                                                                                 |
| relationships         | created_by_user        | object          | The Datadog user who created the component group.                                                                                                       |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component group.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component group belongs to.                                                                                                               |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component group.                                                                                                 |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component group.                                                                                       |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component group belongs to.                                                                                                         |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| Option 3              | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components": [
        {
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "position": "integer",
      "status": "operational",
      "type": "component"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "group": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "components"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "components"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export component_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/components/${component_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Logs Indexing"
    },
    "id": "c34e5b83-90fe-4de2-087b-ea1f64387277",
    "type": "components"
  }
}
EOF

#####

```go
// Update component returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataAttributesComponents0ID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"))
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    body := datadogV2.PatchComponentRequest{
        Data: &datadogV2.PatchComponentRequestData{
            Attributes: datadogV2.PatchComponentRequestDataAttributes{
                Name: datadog.PtrString("Logs Indexing"),
            },
            Id:   StatusPageDataAttributesComponents0ID,
            Type: datadogV2.STATUSPAGESCOMPONENTGROUPTYPE_COMPONENTS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.UpdateComponent(ctx, StatusPageDataID, StatusPageDataAttributesComponents0ID, body, *datadogV2.NewUpdateComponentOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.UpdateComponent`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.UpdateComponent`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update component returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.PatchComponentRequest;
import com.datadog.api.client.v2.model.PatchComponentRequestData;
import com.datadog.api.client.v2.model.PatchComponentRequestDataAttributes;
import com.datadog.api.client.v2.model.StatusPagesComponent;
import com.datadog.api.client.v2.model.StatusPagesComponentGroupType;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = null;
    try {
      STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID =
          UUID.fromString(System.getenv("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    PatchComponentRequest body =
        new PatchComponentRequest()
            .data(
                new PatchComponentRequestData()
                    .attributes(new PatchComponentRequestDataAttributes().name("Logs Indexing"))
                    .id(STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID)
                    .type(StatusPagesComponentGroupType.COMPONENTS));

    try {
      StatusPagesComponent result =
          apiInstance.updateComponent(
              STATUS_PAGE_DATA_ID, STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#updateComponent");
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
Update component returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.patch_component_request import PatchComponentRequest
from datadog_api_client.v2.model.patch_component_request_data import PatchComponentRequestData
from datadog_api_client.v2.model.patch_component_request_data_attributes import PatchComponentRequestDataAttributes
from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = environ["STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"]
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

body = PatchComponentRequest(
    data=PatchComponentRequestData(
        attributes=PatchComponentRequestDataAttributes(
            name="Logs Indexing",
        ),
        id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID,
        type=StatusPagesComponentGroupType.COMPONENTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.update_component(
        page_id=STATUS_PAGE_DATA_ID, component_id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID, body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update component returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = ENV["STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"]
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]

body = DatadogAPIClient::V2::PatchComponentRequest.new({
  data: DatadogAPIClient::V2::PatchComponentRequestData.new({
    attributes: DatadogAPIClient::V2::PatchComponentRequestDataAttributes.new({
      name: "Logs Indexing",
    }),
    id: STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID,
    type: DatadogAPIClient::V2::StatusPagesComponentGroupType::COMPONENTS,
  }),
})
p api_instance.update_component(STATUS_PAGE_DATA_ID, STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update component returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;
use datadog_api_client::datadogV2::api_status_pages::UpdateComponentOptionalParams;
use datadog_api_client::datadogV2::model::PatchComponentRequest;
use datadog_api_client::datadogV2::model::PatchComponentRequestData;
use datadog_api_client::datadogV2::model::PatchComponentRequestDataAttributes;
use datadog_api_client::datadogV2::model::StatusPagesComponentGroupType;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_attributes_components_0_id = uuid::Uuid::parse_str(
        &std::env::var("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID").unwrap(),
    )
    .expect("Invalid UUID");
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let body = PatchComponentRequest::new().data(PatchComponentRequestData::new(
        PatchComponentRequestDataAttributes::new().name("Logs Indexing".to_string()),
        status_page_data_attributes_components_0_id.clone(),
        StatusPagesComponentGroupType::COMPONENTS,
    ));
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .update_component(
            status_page_data_id.clone(),
            status_page_data_attributes_components_0_id.clone(),
            body,
            UpdateComponentOptionalParams::default(),
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
 * Update component returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = process.env
  .STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID as string;
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

const params: v2.StatusPagesApiUpdateComponentRequest = {
  body: {
    data: {
      attributes: {
        name: "Logs Indexing",
      },
      id: STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID,
      type: "components",
    },
  },
  pageId: STATUS_PAGE_DATA_ID,
  componentId: STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID,
};

apiInstance
  .updateComponent(params)
  .then((data: v2.StatusPagesComponent) => {
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

## List components{% #list-components %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/components |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/components |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages/{page_id}/components      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages/{page_id}/components      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages/{page_id}/components     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/components |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/components |

### Overview

Lists all components for a status page. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

#### Query Strings

| Name    | Type   | Description                                                                                                                 |
| ------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data [*required*] | [object]        |
| data                  | attributes             | object          | The attributes of a component.                                                                                                                          |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            |
| components            | name                   | string          |
| components            | position               | int64           |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| data                  | id                     | uuid            | The ID of the component.                                                                                                                                |
| data                  | relationships          | object          | The relationships of a component.                                                                                                                       |
| relationships         | created_by_user        | object          | The Datadog user who created the component.                                                                                                             |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component.                                                                                                   |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component belongs to.                                                                                                                     |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the group the component belongs to.                                                                                                           |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component.                                                                                                       |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component belongs to.                                                                                                               |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page the component belongs to.                                                                                                     |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
|                       | included               | [ <oneOf>] | The included related resources of a component. Client must explicitly request these resources by name in the `include` query parameter.                 |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2               | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                     | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| included              | Option 3               | object          | The included component group resource.                                                                                                                  |
| Option 3              | attributes             | object          | The attributes of a component group.                                                                                                                    |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| Option 3              | id                     | uuid            | The ID of the component.                                                                                                                                |
| Option 3              | relationships          | object          | The relationships of a component group.                                                                                                                 |
| relationships         | created_by_user        | object          | The Datadog user who created the component group.                                                                                                       |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component group.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component group belongs to.                                                                                                               |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component group.                                                                                                 |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component group.                                                                                       |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component group belongs to.                                                                                                         |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| Option 3              | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "components": [
          {
            "id": "string",
            "name": "string",
            "position": "integer",
            "status": "string",
            "type": "component"
          }
        ],
        "created_at": "2019-09-19T10:00:00.000Z",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "position": "integer",
        "status": "operational",
        "type": "component"
      },
      "id": "string",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        },
        "group": {
          "data": {
            "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
            "type": "components"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        },
        "status_page": {
          "data": {
            "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
            "type": "status_pages"
          }
        }
      },
      "type": "components"
    }
  ],
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/components" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List components returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.list_components(
        page_id=STATUS_PAGE_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List components returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]
p api_instance.list_components(STATUS_PAGE_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List components returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.ListComponents(ctx, StatusPageDataID, *datadogV2.NewListComponentsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.ListComponents`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.ListComponents`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List components returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.StatusPagesComponentArray;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      StatusPagesComponentArray result = apiInstance.listComponents(STATUS_PAGE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#listComponents");
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
// List components returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::ListComponentsOptionalParams;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .list_components(
            status_page_data_id.clone(),
            ListComponentsOptionalParams::default(),
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
 * List components returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

const params: v2.StatusPagesApiListComponentsRequest = {
  pageId: STATUS_PAGE_DATA_ID,
};

apiInstance
  .listComponents(params)
  .then((data: v2.StatusPagesComponentArray) => {
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

## Get component{% #get-component %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |

### Overview

Retrieves a specific component by its ID. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                |
| ------------------------------ | ------ | -------------------------- |
| page_id [*required*]      | string | The ID of the status page. |
| component_id [*required*] | string | The ID of the component.   |

#### Query Strings

| Name    | Type   | Description                                                                                                                 |
| ------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a component.                                                                                                                          |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            |
| components            | name                   | string          |
| components            | position               | int64           |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| data                  | id                     | uuid            | The ID of the component.                                                                                                                                |
| data                  | relationships          | object          | The relationships of a component.                                                                                                                       |
| relationships         | created_by_user        | object          | The Datadog user who created the component.                                                                                                             |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component.                                                                                                   |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component belongs to.                                                                                                                     |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the group the component belongs to.                                                                                                           |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component.                                                                                                       |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component belongs to.                                                                                                               |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page the component belongs to.                                                                                                     |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
|                       | included               | [ <oneOf>] | The included related resources of a component. Client must explicitly request these resources by name in the `include` query parameter.                 |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2               | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                     | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| included              | Option 3               | object          | The included component group resource.                                                                                                                  |
| Option 3              | attributes             | object          | The attributes of a component group.                                                                                                                    |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| Option 3              | id                     | uuid            | The ID of the component.                                                                                                                                |
| Option 3              | relationships          | object          | The relationships of a component group.                                                                                                                 |
| relationships         | created_by_user        | object          | The Datadog user who created the component group.                                                                                                       |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component group.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component group belongs to.                                                                                                               |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component group.                                                                                                 |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component group.                                                                                       |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component group belongs to.                                                                                                         |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| Option 3              | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components": [
        {
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "position": "integer",
      "status": "operational",
      "type": "component"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "group": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "components"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "components"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export component_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/components/${component_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get component returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = environ["STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"]
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.get_component(
        page_id=STATUS_PAGE_DATA_ID,
        component_id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get component returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = ENV["STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"]
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]
p api_instance.get_component(STATUS_PAGE_DATA_ID, STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get component returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataAttributesComponents0ID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"))
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.GetComponent(ctx, StatusPageDataID, StatusPageDataAttributesComponents0ID, *datadogV2.NewGetComponentOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.GetComponent`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.GetComponent`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get component returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.StatusPagesComponent;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = null;
    try {
      STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID =
          UUID.fromString(System.getenv("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      StatusPagesComponent result =
          apiInstance.getComponent(
              STATUS_PAGE_DATA_ID, STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#getComponent");
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
// Get component returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::GetComponentOptionalParams;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_attributes_components_0_id = uuid::Uuid::parse_str(
        &std::env::var("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID").unwrap(),
    )
    .expect("Invalid UUID");
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .get_component(
            status_page_data_id.clone(),
            status_page_data_attributes_components_0_id.clone(),
            GetComponentOptionalParams::default(),
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
 * Get component returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = process.env
  .STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID as string;
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

const params: v2.StatusPagesApiGetComponentRequest = {
  pageId: STATUS_PAGE_DATA_ID,
  componentId: STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID,
};

apiInstance
  .getComponent(params)
  .then((data: v2.StatusPagesComponent) => {
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

## Delete component{% #delete-component %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |

### Overview

Deletes a component by its ID. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                |
| ------------------------------ | ------ | -------------------------- |
| page_id [*required*]      | string | The ID of the status page. |
| component_id [*required*] | string | The ID of the component.   |

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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export component_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/components/${component_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete component returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = environ["STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"]
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    api_instance.delete_component(
        page_id=STATUS_PAGE_DATA_ID,
        component_id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete component returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = ENV["STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"]
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]
api_instance.delete_component(STATUS_PAGE_DATA_ID, STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete component returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataAttributesComponents0ID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"))
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    r, err := api.DeleteComponent(ctx, StatusPageDataID, StatusPageDataAttributesComponents0ID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.DeleteComponent`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete component returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = null;
    try {
      STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID =
          UUID.fromString(System.getenv("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      apiInstance.deleteComponent(STATUS_PAGE_DATA_ID, STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#deleteComponent");
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
// Delete component returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_attributes_components_0_id = uuid::Uuid::parse_str(
        &std::env::var("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID").unwrap(),
    )
    .expect("Invalid UUID");
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .delete_component(
            status_page_data_id.clone(),
            status_page_data_attributes_components_0_id.clone(),
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
 * Delete component returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID = process.env
  .STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID as string;
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

const params: v2.StatusPagesApiDeleteComponentRequest = {
  pageId: STATUS_PAGE_DATA_ID,
  componentId: STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_ID,
};

apiInstance
  .deleteComponent(params)
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

## Create degradation{% #create-degradation %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                 |
| ----------------- | ---------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/degradations |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/degradations |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/statuspages/{page_id}/degradations      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/statuspages/{page_id}/degradations      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/statuspages/{page_id}/degradations     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/degradations |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/degradations |

### Overview

Creates a new degradation. This endpoint requires the `status_pages_incident_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

#### Query Strings

| Name               | Type    | Description                                                                                                          |
| ------------------ | ------- | -------------------------------------------------------------------------------------------------------------------- |
| notify_subscribers | boolean | Whether to notify page subscribers of the degradation.                                                               |
| include            | string  | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page. |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field        | Field                                 | Type     | Description                                                                                          |
| ------------------- | ------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
|                     | data                                  | object   |
| data                | attributes [*required*]          | object   | The supported attributes for creating a degradation.                                                 |
| attributes          | components_affected [*required*] | [object] | The components affected by the degradation.                                                          |
| components_affected | id [*required*]                  | uuid     | The ID of the component. Must be a component of type `component`.                                    |
| components_affected | name                                  | string   |
| components_affected | status [*required*]              | enum     | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage` |
| attributes          | description                           | string   | The description of the degradation.                                                                  |
| attributes          | status [*required*]              | enum     | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`   |
| attributes          | title [*required*]               | string   | The title of the degradation.                                                                        |
| data                | type [*required*]                | enum     | Degradations resource type. Allowed enum values: `degradations`                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components_affected": [
        {
          "id": "4e9d3726-bdd7-0079-613c-e9aaba89eb01",
          "status": "major_outage"
        }
      ],
      "description": "Our API is experiencing elevated latency. We are investigating the issue.",
      "status": "investigating",
      "title": "Elevated API Latency"
    },
    "type": "degradations"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field          | Field                    | Type            | Description                                                                                                                                             |
| --------------------- | ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                     | object          |
| data                  | attributes               | object          | The attributes of a degradation.                                                                                                                        |
| attributes            | components_affected      | [object]        | Components affected by the degradation.                                                                                                                 |
| components_affected   | id [*required*]     | uuid            | The ID of the component.                                                                                                                                |
| components_affected   | name                     | string          | The name of the component.                                                                                                                              |
| components_affected   | status [*required*] | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | created_at               | date-time       | Timestamp of when the degradation was created.                                                                                                          |
| attributes            | description              | string          | Description of the degradation.                                                                                                                         |
| attributes            | modified_at              | date-time       | Timestamp of when the degradation was last modified.                                                                                                    |
| attributes            | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| attributes            | title                    | string          | Title of the degradation.                                                                                                                               |
| attributes            | updates                  | [object]        | Past updates made to the degradation.                                                                                                                   |
| updates               | components_affected      | [object]        | The components affected at the time of the update.                                                                                                      |
| components_affected   | id [*required*]     | uuid            | Identifier of the component affected at the time of the update.                                                                                         |
| components_affected   | name                     | string          | The name of the component affected at the time of the update.                                                                                           |
| components_affected   | status [*required*] | enum            | The status of the component affected at the time of the update. Allowed enum values: `operational,degraded,partial_outage,major_outage`                 |
| updates               | created_at               | date-time       | Timestamp of when the update was created.                                                                                                               |
| updates               | description              | string          | Description of the update.                                                                                                                              |
| updates               | id                       | uuid            | Identifier of the update.                                                                                                                               |
| updates               | modified_at              | date-time       | Timestamp of when the update was last modified.                                                                                                         |
| updates               | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| data                  | id                       | uuid            | The ID of the degradation.                                                                                                                              |
| data                  | relationships            | object          | The relationships of a degradation.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the degradation.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the degradation.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the degradation.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the degradation.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page              | object          | The status page the degradation belongs to.                                                                                                             |
| status_page           | data [*required*]   | object          |
| data                  | id [*required*]     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*]   | enum            | Degradations resource type. Allowed enum values: `degradations`                                                                                         |
|                       | included                 | [ <oneOf>] | The included related resources of a degradation. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1                 | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes               | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                    | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                   | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                     | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                     | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                     | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                       | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2                 | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes               | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo             | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components               | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components               | [object]        |
| components            | id                       | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                     | string          | The name of the grouped component.                                                                                                                      |
| components            | position                 | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                       | uuid            | The ID of the component.                                                                                                                                |
| components            | name                     | string          | The name of the component.                                                                                                                              |
| components            | position                 | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at               | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain            | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled    | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix            | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image       | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                  | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                  | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at              | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                     | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url                 | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled    | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                     | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type       | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                       | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships            | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components_affected": [
        {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "name": "string",
          "status": "operational"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "status": "investigating",
      "title": "string",
      "updates": [
        {
          "components_affected": [
            {
              "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
              "name": "string",
              "status": "operational"
            }
          ],
          "created_at": "2019-09-19T10:00:00.000Z",
          "description": "string",
          "id": "string",
          "modified_at": "2019-09-19T10:00:00.000Z",
          "status": "investigating"
        }
      ]
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "degradations"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/degradations" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "components_affected": [
        {
          "id": "4e9d3726-bdd7-0079-613c-e9aaba89eb01",
          "status": "major_outage"
        }
      ],
      "description": "Our API is experiencing elevated latency. We are investigating the issue.",
      "status": "investigating",
      "title": "Elevated API Latency"
    },
    "type": "degradations"
  }
}
EOF

#####

```go
// Create degradation returns "Created" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataAttributesComponents0Components0ID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID"))
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    body := datadogV2.CreateDegradationRequest{
        Data: &datadogV2.CreateDegradationRequestData{
            Attributes: datadogV2.CreateDegradationRequestDataAttributes{
                ComponentsAffected: []datadogV2.CreateDegradationRequestDataAttributesComponentsAffectedItems{
                    {
                        Id:     StatusPageDataAttributesComponents0Components0ID,
                        Status: datadogV2.STATUSPAGESCOMPONENTDATAATTRIBUTESSTATUS_MAJOR_OUTAGE,
                    },
                },
                Description: datadog.PtrString("Our API is experiencing elevated latency. We are investigating the issue."),
                Status:      datadogV2.CREATEDEGRADATIONREQUESTDATAATTRIBUTESSTATUS_INVESTIGATING,
                Title:       "Elevated API Latency",
            },
            Type: datadogV2.PATCHDEGRADATIONREQUESTDATATYPE_DEGRADATIONS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.CreateDegradation(ctx, StatusPageDataID, body, *datadogV2.NewCreateDegradationOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.CreateDegradation`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.CreateDegradation`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create degradation returns "Created" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.CreateDegradationRequest;
import com.datadog.api.client.v2.model.CreateDegradationRequestData;
import com.datadog.api.client.v2.model.CreateDegradationRequestDataAttributes;
import com.datadog.api.client.v2.model.CreateDegradationRequestDataAttributesComponentsAffectedItems;
import com.datadog.api.client.v2.model.CreateDegradationRequestDataAttributesStatus;
import com.datadog.api.client.v2.model.Degradation;
import com.datadog.api.client.v2.model.PatchDegradationRequestDataType;
import com.datadog.api.client.v2.model.StatusPagesComponentDataAttributesStatus;
import java.util.Collections;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID = null;
    try {
      STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID =
          UUID.fromString(
              System.getenv("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    CreateDegradationRequest body =
        new CreateDegradationRequest()
            .data(
                new CreateDegradationRequestData()
                    .attributes(
                        new CreateDegradationRequestDataAttributes()
                            .componentsAffected(
                                Collections.singletonList(
                                    new CreateDegradationRequestDataAttributesComponentsAffectedItems()
                                        .id(
                                            STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID)
                                        .status(
                                            StatusPagesComponentDataAttributesStatus.MAJOR_OUTAGE)))
                            .description(
                                "Our API is experiencing elevated latency. We are investigating the"
                                    + " issue.")
                            .status(CreateDegradationRequestDataAttributesStatus.INVESTIGATING)
                            .title("Elevated API Latency"))
                    .type(PatchDegradationRequestDataType.DEGRADATIONS));

    try {
      Degradation result = apiInstance.createDegradation(STATUS_PAGE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#createDegradation");
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
Create degradation returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_degradation_request import CreateDegradationRequest
from datadog_api_client.v2.model.create_degradation_request_data import CreateDegradationRequestData
from datadog_api_client.v2.model.create_degradation_request_data_attributes import (
    CreateDegradationRequestDataAttributes,
)
from datadog_api_client.v2.model.create_degradation_request_data_attributes_components_affected_items import (
    CreateDegradationRequestDataAttributesComponentsAffectedItems,
)
from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
    CreateDegradationRequestDataAttributesStatus,
)
from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType
from datadog_api_client.v2.model.status_pages_component_data_attributes_status import (
    StatusPagesComponentDataAttributesStatus,
)

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID = environ[
    "STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID"
]
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

body = CreateDegradationRequest(
    data=CreateDegradationRequestData(
        attributes=CreateDegradationRequestDataAttributes(
            components_affected=[
                CreateDegradationRequestDataAttributesComponentsAffectedItems(
                    id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID,
                    status=StatusPagesComponentDataAttributesStatus.MAJOR_OUTAGE,
                ),
            ],
            description="Our API is experiencing elevated latency. We are investigating the issue.",
            status=CreateDegradationRequestDataAttributesStatus.INVESTIGATING,
            title="Elevated API Latency",
        ),
        type=PatchDegradationRequestDataType.DEGRADATIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_degradation(page_id=STATUS_PAGE_DATA_ID, body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Create degradation returns "Created" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID = ENV["STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID"]
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]

body = DatadogAPIClient::V2::CreateDegradationRequest.new({
  data: DatadogAPIClient::V2::CreateDegradationRequestData.new({
    attributes: DatadogAPIClient::V2::CreateDegradationRequestDataAttributes.new({
      components_affected: [
        DatadogAPIClient::V2::CreateDegradationRequestDataAttributesComponentsAffectedItems.new({
          id: STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID,
          status: DatadogAPIClient::V2::StatusPagesComponentDataAttributesStatus::MAJOR_OUTAGE,
        }),
      ],
      description: "Our API is experiencing elevated latency. We are investigating the issue.",
      status: DatadogAPIClient::V2::CreateDegradationRequestDataAttributesStatus::INVESTIGATING,
      title: "Elevated API Latency",
    }),
    type: DatadogAPIClient::V2::PatchDegradationRequestDataType::DEGRADATIONS,
  }),
})
p api_instance.create_degradation(STATUS_PAGE_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create degradation returns "Created" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::CreateDegradationOptionalParams;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;
use datadog_api_client::datadogV2::model::CreateDegradationRequest;
use datadog_api_client::datadogV2::model::CreateDegradationRequestData;
use datadog_api_client::datadogV2::model::CreateDegradationRequestDataAttributes;
use datadog_api_client::datadogV2::model::CreateDegradationRequestDataAttributesComponentsAffectedItems;
use datadog_api_client::datadogV2::model::CreateDegradationRequestDataAttributesStatus;
use datadog_api_client::datadogV2::model::PatchDegradationRequestDataType;
use datadog_api_client::datadogV2::model::StatusPagesComponentDataAttributesStatus;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_attributes_components_0_components_0_id = uuid::Uuid::parse_str(
        &std::env::var("STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID").unwrap(),
    )
    .expect("Invalid UUID");
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let body = CreateDegradationRequest::new().data(CreateDegradationRequestData::new(
        CreateDegradationRequestDataAttributes::new(
            vec![
                CreateDegradationRequestDataAttributesComponentsAffectedItems::new(
                    status_page_data_attributes_components_0_components_0_id.clone(),
                    StatusPagesComponentDataAttributesStatus::MAJOR_OUTAGE,
                ),
            ],
            CreateDegradationRequestDataAttributesStatus::INVESTIGATING,
            "Elevated API Latency".to_string(),
        )
        .description(
            "Our API is experiencing elevated latency. We are investigating the issue.".to_string(),
        ),
        PatchDegradationRequestDataType::DEGRADATIONS,
    ));
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .create_degradation(
            status_page_data_id.clone(),
            body,
            CreateDegradationOptionalParams::default(),
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
 * Create degradation returns "Created" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID = process.env
  .STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID as string;
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

const params: v2.StatusPagesApiCreateDegradationRequest = {
  body: {
    data: {
      attributes: {
        componentsAffected: [
          {
            id: STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID,
            status: "major_outage",
          },
        ],
        description:
          "Our API is experiencing elevated latency. We are investigating the issue.",
        status: "investigating",
        title: "Elevated API Latency",
      },
      type: "degradations",
    },
  },
  pageId: STATUS_PAGE_DATA_ID,
};

apiInstance
  .createDegradation(params)
  .then((data: v2.Degradation) => {
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

## Update degradation{% #update-degradation %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |

### Overview

Updates an existing degradation's attributes. This endpoint requires the `status_pages_incident_write` permission.

### Arguments

#### Path Parameters

| Name                             | Type   | Description                |
| -------------------------------- | ------ | -------------------------- |
| page_id [*required*]        | string | The ID of the status page. |
| degradation_id [*required*] | string | The ID of the degradation. |

#### Query Strings

| Name               | Type    | Description                                                                                                          |
| ------------------ | ------- | -------------------------------------------------------------------------------------------------------------------- |
| notify_subscribers | boolean | Whether to notify page subscribers of the degradation.                                                               |
| include            | string  | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page. |

### Request

#### Body Data (required)

{% tab title="Model" %}

| Parent field        | Field                        | Type     | Description                                                                                          |
| ------------------- | ---------------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
|                     | data                         | object   |
| data                | attributes [*required*] | object   | The supported attributes for updating a degradation.                                                 |
| attributes          | components_affected          | [object] | The components affected by the degradation.                                                          |
| components_affected | id [*required*]         | uuid     | The ID of the component. Must be a component of type `component`.                                    |
| components_affected | name                         | string   |
| components_affected | status [*required*]     | enum     | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage` |
| attributes          | description                  | string   | The description of the degradation.                                                                  |
| attributes          | status                       | enum     | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`   |
| attributes          | title                        | string   | The title of the degradation.                                                                        |
| data                | id [*required*]         | uuid     | The ID of the degradation.                                                                           |
| data                | type [*required*]       | enum     | Degradations resource type. Allowed enum values: `degradations`                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "title": "Elevated API Latency in US1"
    },
    "id": "81335836-b858-2e64-43d6-5b27ba1e6d8e",
    "type": "degradations"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                    | Type            | Description                                                                                                                                             |
| --------------------- | ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                     | object          |
| data                  | attributes               | object          | The attributes of a degradation.                                                                                                                        |
| attributes            | components_affected      | [object]        | Components affected by the degradation.                                                                                                                 |
| components_affected   | id [*required*]     | uuid            | The ID of the component.                                                                                                                                |
| components_affected   | name                     | string          | The name of the component.                                                                                                                              |
| components_affected   | status [*required*] | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | created_at               | date-time       | Timestamp of when the degradation was created.                                                                                                          |
| attributes            | description              | string          | Description of the degradation.                                                                                                                         |
| attributes            | modified_at              | date-time       | Timestamp of when the degradation was last modified.                                                                                                    |
| attributes            | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| attributes            | title                    | string          | Title of the degradation.                                                                                                                               |
| attributes            | updates                  | [object]        | Past updates made to the degradation.                                                                                                                   |
| updates               | components_affected      | [object]        | The components affected at the time of the update.                                                                                                      |
| components_affected   | id [*required*]     | uuid            | Identifier of the component affected at the time of the update.                                                                                         |
| components_affected   | name                     | string          | The name of the component affected at the time of the update.                                                                                           |
| components_affected   | status [*required*] | enum            | The status of the component affected at the time of the update. Allowed enum values: `operational,degraded,partial_outage,major_outage`                 |
| updates               | created_at               | date-time       | Timestamp of when the update was created.                                                                                                               |
| updates               | description              | string          | Description of the update.                                                                                                                              |
| updates               | id                       | uuid            | Identifier of the update.                                                                                                                               |
| updates               | modified_at              | date-time       | Timestamp of when the update was last modified.                                                                                                         |
| updates               | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| data                  | id                       | uuid            | The ID of the degradation.                                                                                                                              |
| data                  | relationships            | object          | The relationships of a degradation.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the degradation.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the degradation.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the degradation.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the degradation.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page              | object          | The status page the degradation belongs to.                                                                                                             |
| status_page           | data [*required*]   | object          |
| data                  | id [*required*]     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*]   | enum            | Degradations resource type. Allowed enum values: `degradations`                                                                                         |
|                       | included                 | [ <oneOf>] | The included related resources of a degradation. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1                 | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes               | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                    | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                   | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                     | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                     | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                     | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                       | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2                 | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes               | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo             | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components               | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components               | [object]        |
| components            | id                       | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                     | string          | The name of the grouped component.                                                                                                                      |
| components            | position                 | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                       | uuid            | The ID of the component.                                                                                                                                |
| components            | name                     | string          | The name of the component.                                                                                                                              |
| components            | position                 | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at               | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain            | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled    | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix            | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image       | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                  | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                  | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at              | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                     | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url                 | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled    | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                     | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type       | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                       | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships            | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components_affected": [
        {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "name": "string",
          "status": "operational"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "status": "investigating",
      "title": "string",
      "updates": [
        {
          "components_affected": [
            {
              "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
              "name": "string",
              "status": "operational"
            }
          ],
          "created_at": "2019-09-19T10:00:00.000Z",
          "description": "string",
          "id": "string",
          "modified_at": "2019-09-19T10:00:00.000Z",
          "status": "investigating"
        }
      ]
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "degradations"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export degradation_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/degradations/${degradation_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "title": "Elevated API Latency in US1"
    },
    "id": "81335836-b858-2e64-43d6-5b27ba1e6d8e",
    "type": "degradations"
  }
}
EOF

#####

```go
// Update degradation returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    // there is a valid "degradation" in the system
    DegradationDataID := uuid.MustParse(os.Getenv("DEGRADATION_DATA_ID"))

    body := datadogV2.PatchDegradationRequest{
        Data: &datadogV2.PatchDegradationRequestData{
            Attributes: datadogV2.PatchDegradationRequestDataAttributes{
                Title: datadog.PtrString("Elevated API Latency in US1"),
            },
            Id:   DegradationDataID,
            Type: datadogV2.PATCHDEGRADATIONREQUESTDATATYPE_DEGRADATIONS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.UpdateDegradation(ctx, StatusPageDataID, DegradationDataID, body, *datadogV2.NewUpdateDegradationOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.UpdateDegradation`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.UpdateDegradation`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Update degradation returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.Degradation;
import com.datadog.api.client.v2.model.PatchDegradationRequest;
import com.datadog.api.client.v2.model.PatchDegradationRequestData;
import com.datadog.api.client.v2.model.PatchDegradationRequestDataAttributes;
import com.datadog.api.client.v2.model.PatchDegradationRequestDataType;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    // there is a valid "degradation" in the system
    UUID DEGRADATION_DATA_ID = null;
    try {
      DEGRADATION_DATA_ID = UUID.fromString(System.getenv("DEGRADATION_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    PatchDegradationRequest body =
        new PatchDegradationRequest()
            .data(
                new PatchDegradationRequestData()
                    .attributes(
                        new PatchDegradationRequestDataAttributes()
                            .title("Elevated API Latency in US1"))
                    .id(DEGRADATION_DATA_ID)
                    .type(PatchDegradationRequestDataType.DEGRADATIONS));

    try {
      Degradation result =
          apiInstance.updateDegradation(STATUS_PAGE_DATA_ID, DEGRADATION_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#updateDegradation");
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
Update degradation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.patch_degradation_request import PatchDegradationRequest
from datadog_api_client.v2.model.patch_degradation_request_data import PatchDegradationRequestData
from datadog_api_client.v2.model.patch_degradation_request_data_attributes import PatchDegradationRequestDataAttributes
from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

# there is a valid "degradation" in the system
DEGRADATION_DATA_ID = environ["DEGRADATION_DATA_ID"]

body = PatchDegradationRequest(
    data=PatchDegradationRequestData(
        attributes=PatchDegradationRequestDataAttributes(
            title="Elevated API Latency in US1",
        ),
        id=DEGRADATION_DATA_ID,
        type=PatchDegradationRequestDataType.DEGRADATIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.update_degradation(
        page_id=STATUS_PAGE_DATA_ID, degradation_id=DEGRADATION_DATA_ID, body=body
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Update degradation returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]

# there is a valid "degradation" in the system
DEGRADATION_DATA_ID = ENV["DEGRADATION_DATA_ID"]

body = DatadogAPIClient::V2::PatchDegradationRequest.new({
  data: DatadogAPIClient::V2::PatchDegradationRequestData.new({
    attributes: DatadogAPIClient::V2::PatchDegradationRequestDataAttributes.new({
      title: "Elevated API Latency in US1",
    }),
    id: DEGRADATION_DATA_ID,
    type: DatadogAPIClient::V2::PatchDegradationRequestDataType::DEGRADATIONS,
  }),
})
p api_instance.update_degradation(STATUS_PAGE_DATA_ID, DEGRADATION_DATA_ID, body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Update degradation returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;
use datadog_api_client::datadogV2::api_status_pages::UpdateDegradationOptionalParams;
use datadog_api_client::datadogV2::model::PatchDegradationRequest;
use datadog_api_client::datadogV2::model::PatchDegradationRequestData;
use datadog_api_client::datadogV2::model::PatchDegradationRequestDataAttributes;
use datadog_api_client::datadogV2::model::PatchDegradationRequestDataType;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");

    // there is a valid "degradation" in the system
    let degradation_data_id = uuid::Uuid::parse_str(&std::env::var("DEGRADATION_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let body = PatchDegradationRequest::new().data(PatchDegradationRequestData::new(
        PatchDegradationRequestDataAttributes::new()
            .title("Elevated API Latency in US1".to_string()),
        degradation_data_id.clone(),
        PatchDegradationRequestDataType::DEGRADATIONS,
    ));
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .update_degradation(
            status_page_data_id.clone(),
            degradation_data_id.clone(),
            body,
            UpdateDegradationOptionalParams::default(),
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
 * Update degradation returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

// there is a valid "degradation" in the system
const DEGRADATION_DATA_ID = process.env.DEGRADATION_DATA_ID as string;

const params: v2.StatusPagesApiUpdateDegradationRequest = {
  body: {
    data: {
      attributes: {
        title: "Elevated API Latency in US1",
      },
      id: DEGRADATION_DATA_ID,
      type: "degradations",
    },
  },
  pageId: STATUS_PAGE_DATA_ID,
  degradationId: DEGRADATION_DATA_ID,
};

apiInstance
  .updateDegradation(params)
  .then((data: v2.Degradation) => {
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

## List degradations{% #list-degradations %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages/degradations |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages/degradations |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages/degradations      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages/degradations      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages/degradations     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages/degradations |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages/degradations |

### Overview

Lists all degradations for the organization. Optionally filter by status and page. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Query Strings

| Name            | Type    | Description                                                                                                          |
| --------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
| filter[page_id] | string  | Optional page id filter.                                                                                             |
| page[offset]    | integer | Offset to use as the start of the page.                                                                              |
| page[limit]     | integer | The number of degradations to return per page.                                                                       |
| include         | string  | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page. |
| filter[status]  | string  | Optional degradation status filter. Supported values: investigating, identified, monitoring, resolved.               |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                    | Type            | Description                                                                                                                                             |
| --------------------- | ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data [*required*]   | [object]        |
| data                  | attributes               | object          | The attributes of a degradation.                                                                                                                        |
| attributes            | components_affected      | [object]        | Components affected by the degradation.                                                                                                                 |
| components_affected   | id [*required*]     | uuid            | The ID of the component.                                                                                                                                |
| components_affected   | name                     | string          | The name of the component.                                                                                                                              |
| components_affected   | status [*required*] | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | created_at               | date-time       | Timestamp of when the degradation was created.                                                                                                          |
| attributes            | description              | string          | Description of the degradation.                                                                                                                         |
| attributes            | modified_at              | date-time       | Timestamp of when the degradation was last modified.                                                                                                    |
| attributes            | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| attributes            | title                    | string          | Title of the degradation.                                                                                                                               |
| attributes            | updates                  | [object]        | Past updates made to the degradation.                                                                                                                   |
| updates               | components_affected      | [object]        | The components affected at the time of the update.                                                                                                      |
| components_affected   | id [*required*]     | uuid            | Identifier of the component affected at the time of the update.                                                                                         |
| components_affected   | name                     | string          | The name of the component affected at the time of the update.                                                                                           |
| components_affected   | status [*required*] | enum            | The status of the component affected at the time of the update. Allowed enum values: `operational,degraded,partial_outage,major_outage`                 |
| updates               | created_at               | date-time       | Timestamp of when the update was created.                                                                                                               |
| updates               | description              | string          | Description of the update.                                                                                                                              |
| updates               | id                       | uuid            | Identifier of the update.                                                                                                                               |
| updates               | modified_at              | date-time       | Timestamp of when the update was last modified.                                                                                                         |
| updates               | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| data                  | id                       | uuid            | The ID of the degradation.                                                                                                                              |
| data                  | relationships            | object          | The relationships of a degradation.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the degradation.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the degradation.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the degradation.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the degradation.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page              | object          | The status page the degradation belongs to.                                                                                                             |
| status_page           | data [*required*]   | object          |
| data                  | id [*required*]     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*]   | enum            | Degradations resource type. Allowed enum values: `degradations`                                                                                         |
|                       | included                 | [ <oneOf>] | The included related resources of a degradation. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1                 | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes               | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                    | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                   | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                     | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                     | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                     | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                       | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2                 | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes               | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo             | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components               | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components               | [object]        |
| components            | id                       | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                     | string          | The name of the grouped component.                                                                                                                      |
| components            | position                 | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                       | uuid            | The ID of the component.                                                                                                                                |
| components            | name                     | string          | The name of the component.                                                                                                                              |
| components            | position                 | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at               | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain            | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled    | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix            | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image       | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                  | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                  | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at              | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                     | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url                 | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled    | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                     | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type       | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                       | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships            | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
|                       | meta                     | object          | Response metadata.                                                                                                                                      |
| meta                  | page                     | object          | Offset-based pagination schema.                                                                                                                         |
| page                  | first_offset             | int64           | Integer representing the offset to fetch the first page of results.                                                                                     |
| page                  | last_offset              | int64           | Integer representing the offset to fetch the last page of results.                                                                                      |
| page                  | limit                    | int64           | Integer representing the number of elements to returned in the results.                                                                                 |
| page                  | next_offset              | int64           | Integer representing the index of the first element in the next page of results. Equal to page size added to the current offset.                        |
| page                  | offset                   | int64           | Integer representing the index of the first element in the results.                                                                                     |
| page                  | prev_offset              | int64           | Integer representing the index of the first element in the previous page of results.                                                                    |
| page                  | total                    | int64           | Integer representing the total number of elements available.                                                                                            |
| page                  | type                     | enum            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "components_affected": [
          {
            "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
            "name": "string",
            "status": "operational"
          }
        ],
        "created_at": "2019-09-19T10:00:00.000Z",
        "description": "string",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "status": "investigating",
        "title": "string",
        "updates": [
          {
            "components_affected": [
              {
                "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
                "name": "string",
                "status": "operational"
              }
            ],
            "created_at": "2019-09-19T10:00:00.000Z",
            "description": "string",
            "id": "string",
            "modified_at": "2019-09-19T10:00:00.000Z",
            "status": "investigating"
          }
        ]
      },
      "id": "string",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        },
        "status_page": {
          "data": {
            "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
            "type": "status_pages"
          }
        }
      },
      "type": "degradations"
    }
  ],
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
    }
  ],
  "meta": {
    "page": {
      "first_offset": 0,
      "last_offset": 900,
      "limit": 100,
      "next_offset": 100,
      "offset": 0,
      "prev_offset": 100,
      "total": 1000,
      "type": "offset_limit"
    }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/degradations" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List degradations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.list_degradations()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# List degradations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new
p api_instance.list_degradations()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// List degradations returns "OK" response

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
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.ListDegradations(ctx, *datadogV2.NewListDegradationsOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.ListDegradations`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.ListDegradations`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// List degradations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.DegradationArray;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    try {
      DegradationArray result = apiInstance.listDegradations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#listDegradations");
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
// List degradations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::ListDegradationsOptionalParams;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .list_degradations(ListDegradationsOptionalParams::default())
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
 * List degradations returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

apiInstance
  .listDegradations()
  .then((data: v2.DegradationArray) => {
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

## Get degradation{% #get-degradation %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |

### Overview

Retrieves a specific degradation by its ID. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Path Parameters

| Name                             | Type   | Description                |
| -------------------------------- | ------ | -------------------------- |
| page_id [*required*]        | string | The ID of the status page. |
| degradation_id [*required*] | string | The ID of the degradation. |

#### Query Strings

| Name    | Type   | Description                                                                                                          |
| ------- | ------ | -------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                    | Type            | Description                                                                                                                                             |
| --------------------- | ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                     | object          |
| data                  | attributes               | object          | The attributes of a degradation.                                                                                                                        |
| attributes            | components_affected      | [object]        | Components affected by the degradation.                                                                                                                 |
| components_affected   | id [*required*]     | uuid            | The ID of the component.                                                                                                                                |
| components_affected   | name                     | string          | The name of the component.                                                                                                                              |
| components_affected   | status [*required*] | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | created_at               | date-time       | Timestamp of when the degradation was created.                                                                                                          |
| attributes            | description              | string          | Description of the degradation.                                                                                                                         |
| attributes            | modified_at              | date-time       | Timestamp of when the degradation was last modified.                                                                                                    |
| attributes            | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| attributes            | title                    | string          | Title of the degradation.                                                                                                                               |
| attributes            | updates                  | [object]        | Past updates made to the degradation.                                                                                                                   |
| updates               | components_affected      | [object]        | The components affected at the time of the update.                                                                                                      |
| components_affected   | id [*required*]     | uuid            | Identifier of the component affected at the time of the update.                                                                                         |
| components_affected   | name                     | string          | The name of the component affected at the time of the update.                                                                                           |
| components_affected   | status [*required*] | enum            | The status of the component affected at the time of the update. Allowed enum values: `operational,degraded,partial_outage,major_outage`                 |
| updates               | created_at               | date-time       | Timestamp of when the update was created.                                                                                                               |
| updates               | description              | string          | Description of the update.                                                                                                                              |
| updates               | id                       | uuid            | Identifier of the update.                                                                                                                               |
| updates               | modified_at              | date-time       | Timestamp of when the update was last modified.                                                                                                         |
| updates               | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| data                  | id                       | uuid            | The ID of the degradation.                                                                                                                              |
| data                  | relationships            | object          | The relationships of a degradation.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the degradation.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the degradation.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the degradation.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the degradation.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page              | object          | The status page the degradation belongs to.                                                                                                             |
| status_page           | data [*required*]   | object          |
| data                  | id [*required*]     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*]   | enum            | Degradations resource type. Allowed enum values: `degradations`                                                                                         |
|                       | included                 | [ <oneOf>] | The included related resources of a degradation. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1                 | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes               | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                    | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                   | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                     | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                     | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                     | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                       | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2                 | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes               | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo             | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components               | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components               | [object]        |
| components            | id                       | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                     | string          | The name of the grouped component.                                                                                                                      |
| components            | position                 | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                       | uuid            | The ID of the component.                                                                                                                                |
| components            | name                     | string          | The name of the component.                                                                                                                              |
| components            | position                 | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at               | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain            | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled    | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix            | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image       | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                  | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                  | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at              | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                     | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url                 | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled    | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                     | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type       | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                       | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships            | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components_affected": [
        {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "name": "string",
          "status": "operational"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "status": "investigating",
      "title": "string",
      "updates": [
        {
          "components_affected": [
            {
              "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
              "name": "string",
              "status": "operational"
            }
          ],
          "created_at": "2019-09-19T10:00:00.000Z",
          "description": "string",
          "id": "string",
          "modified_at": "2019-09-19T10:00:00.000Z",
          "status": "investigating"
        }
      ]
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "degradations"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export degradation_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/degradations/${degradation_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get degradation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

# there is a valid "degradation" in the system
DEGRADATION_DATA_ID = environ["DEGRADATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.get_degradation(
        page_id=STATUS_PAGE_DATA_ID,
        degradation_id=DEGRADATION_DATA_ID,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get degradation returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]

# there is a valid "degradation" in the system
DEGRADATION_DATA_ID = ENV["DEGRADATION_DATA_ID"]
p api_instance.get_degradation(STATUS_PAGE_DATA_ID, DEGRADATION_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get degradation returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    // there is a valid "degradation" in the system
    DegradationDataID := uuid.MustParse(os.Getenv("DEGRADATION_DATA_ID"))

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    resp, r, err := api.GetDegradation(ctx, StatusPageDataID, DegradationDataID, *datadogV2.NewGetDegradationOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.GetDegradation`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `StatusPagesApi.GetDegradation`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get degradation returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import com.datadog.api.client.v2.model.Degradation;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    // there is a valid "degradation" in the system
    UUID DEGRADATION_DATA_ID = null;
    try {
      DEGRADATION_DATA_ID = UUID.fromString(System.getenv("DEGRADATION_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      Degradation result = apiInstance.getDegradation(STATUS_PAGE_DATA_ID, DEGRADATION_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#getDegradation");
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
// Get degradation returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::GetDegradationOptionalParams;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");

    // there is a valid "degradation" in the system
    let degradation_data_id = uuid::Uuid::parse_str(&std::env::var("DEGRADATION_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .get_degradation(
            status_page_data_id.clone(),
            degradation_data_id.clone(),
            GetDegradationOptionalParams::default(),
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
 * Get degradation returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

// there is a valid "degradation" in the system
const DEGRADATION_DATA_ID = process.env.DEGRADATION_DATA_ID as string;

const params: v2.StatusPagesApiGetDegradationRequest = {
  pageId: STATUS_PAGE_DATA_ID,
  degradationId: DEGRADATION_DATA_ID,
};

apiInstance
  .getDegradation(params)
  .then((data: v2.Degradation) => {
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

## Delete degradation{% #delete-degradation %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |

### Overview

Deletes a degradation by its ID. This endpoint requires the `status_pages_incident_write` permission.

### Arguments

#### Path Parameters

| Name                             | Type   | Description                |
| -------------------------------- | ------ | -------------------------- |
| page_id [*required*]        | string | The ID of the status page. |
| degradation_id [*required*] | string | The ID of the degradation. |

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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export degradation_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/degradations/${degradation_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Delete degradation returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

# there is a valid "degradation" in the system
DEGRADATION_DATA_ID = environ["DEGRADATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    api_instance.delete_degradation(
        page_id=STATUS_PAGE_DATA_ID,
        degradation_id=DEGRADATION_DATA_ID,
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete degradation returns "No Content" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::StatusPagesAPI.new

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = ENV["STATUS_PAGE_DATA_ID"]

# there is a valid "degradation" in the system
DEGRADATION_DATA_ID = ENV["DEGRADATION_DATA_ID"]
api_instance.delete_degradation(STATUS_PAGE_DATA_ID, DEGRADATION_DATA_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Delete degradation returns "No Content" response

package main

import (
    "context"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
    "github.com/google/uuid"
)

func main() {
    // there is a valid "status_page" in the system
    StatusPageDataID := uuid.MustParse(os.Getenv("STATUS_PAGE_DATA_ID"))

    // there is a valid "degradation" in the system
    DegradationDataID := uuid.MustParse(os.Getenv("DEGRADATION_DATA_ID"))

    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewStatusPagesApi(apiClient)
    r, err := api.DeleteDegradation(ctx, StatusPageDataID, DegradationDataID)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StatusPagesApi.DeleteDegradation`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Delete degradation returns "No Content" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.StatusPagesApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    StatusPagesApi apiInstance = new StatusPagesApi(defaultClient);

    // there is a valid "status_page" in the system
    UUID STATUS_PAGE_DATA_ID = null;
    try {
      STATUS_PAGE_DATA_ID = UUID.fromString(System.getenv("STATUS_PAGE_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    // there is a valid "degradation" in the system
    UUID DEGRADATION_DATA_ID = null;
    try {
      DEGRADATION_DATA_ID = UUID.fromString(System.getenv("DEGRADATION_DATA_ID"));
    } catch (IllegalArgumentException e) {
      System.err.println("Error parsing UUID: " + e.getMessage());
    }

    try {
      apiInstance.deleteDegradation(STATUS_PAGE_DATA_ID, DEGRADATION_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusPagesApi#deleteDegradation");
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
// Delete degradation returns "No Content" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_status_pages::StatusPagesAPI;

#[tokio::main]
async fn main() {
    // there is a valid "status_page" in the system
    let status_page_data_id = uuid::Uuid::parse_str(&std::env::var("STATUS_PAGE_DATA_ID").unwrap())
        .expect("Invalid UUID");

    // there is a valid "degradation" in the system
    let degradation_data_id = uuid::Uuid::parse_str(&std::env::var("DEGRADATION_DATA_ID").unwrap())
        .expect("Invalid UUID");
    let configuration = datadog::Configuration::new();
    let api = StatusPagesAPI::with_config(configuration);
    let resp = api
        .delete_degradation(status_page_data_id.clone(), degradation_data_id.clone())
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
 * Delete degradation returns "No Content" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.StatusPagesApi(configuration);

// there is a valid "status_page" in the system
const STATUS_PAGE_DATA_ID = process.env.STATUS_PAGE_DATA_ID as string;

// there is a valid "degradation" in the system
const DEGRADATION_DATA_ID = process.env.DEGRADATION_DATA_ID as string;

const params: v2.StatusPagesApiDeleteDegradationRequest = {
  pageId: STATUS_PAGE_DATA_ID,
  degradationId: DEGRADATION_DATA_ID,
};

apiInstance
  .deleteDegradation(params)
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
