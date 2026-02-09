# Source: https://docs.datadoghq.com/api/latest/on-call-paging.md

---
title: On-Call Paging
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > On-Call Paging
---

# On-Call Paging

Trigger and manage [Datadog On-Call](https://docs.datadoghq.com/service_management/on-call/) pages directly through the Datadog API.

## Create On-Call Page{% #create-on-call-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://saffron.oncall.datadoghq.com/api/v2/on-call/pages |
| ap2.datadoghq.com | POST https://lava.oncall.datadoghq.com/api/v2/on-call/pages    |
| app.datadoghq.eu  | POST https://beige.oncall.datadoghq.eu/api/v2/on-call/pages    |
| app.ddog-gov.com  | POST https://navy.oncall.datadoghq.com/api/v2/on-call/pages    |
| app.datadoghq.com | POST https://navy.oncall.datadoghq.com/api/v2/on-call/pages    |
| us3.datadoghq.com | POST https://teal.oncall.datadoghq.com/api/v2/on-call/pages    |
| us5.datadoghq.com | POST https://coral.oncall.datadoghq.com/api/v2/on-call/pages   |

### Overview

Trigger a new On-Call Page.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                     | Type     | Description                                                                                                   |
| ------------ | ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------- |
|              | data                      | object   | The main request body, including attributes and resource type.                                                |
| data         | attributes                | object   | Details about the On-Call Page you want to create.                                                            |
| attributes   | description               | string   | A short summary of the issue or context.                                                                      |
| attributes   | tags                      | [string] | Tags to help categorize or filter the page.                                                                   |
| attributes   | target [*required*]  | object   | Information about the target to notify (such as a team or user).                                              |
| target       | identifier                | string   | Identifier for the target (for example, team handle or user ID).                                              |
| target       | type                      | enum     | The kind of target, `team_id` | `team_handle` | `user_id`. Allowed enum values: `team_id,team_handle,user_id` |
| attributes   | title [*required*]   | string   | The title of the page.                                                                                        |
| attributes   | urgency [*required*] | enum     | On-Call Page urgency level. Allowed enum values: `low,high`                                                   |
| data         | type [*required*]    | enum     | The type of resource used when creating an On-Call Page. Allowed enum values: `pages`                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "string",
      "tags": [],
      "target": {
        "identifier": "string",
        "type": "team_id"
      },
      "title": "Service: Test is down",
      "urgency": "high"
    },
    "type": "pages"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK.
{% tab title="Model" %}
The full response object after creating a new On-Call Page.

| Parent field | Field                  | Type   | Description                                                                           |
| ------------ | ---------------------- | ------ | ------------------------------------------------------------------------------------- |
|              | data                   | object | The information returned after successfully creating a page.                          |
| data         | id                     | string | The unique ID of the created page.                                                    |
| data         | type [*required*] | enum   | The type of resource used when creating an On-Call Page. Allowed enum values: `pages` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "15e74b8b-f865-48d0-bcc5-453323ed2c8f",
    "type": "pages"
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
                  \# Curl commandcurl -X POST "https://saffron.oncall.datadoghq.com"https://lava.oncall.datadoghq.com"https://beige.oncall.datadoghq.eu"https://navy.oncall.datadoghq.com"https://navy.oncall.datadoghq.com"https://teal.oncall.datadoghq.com"https://coral.oncall.datadoghq.com/api/v2/on-call/pages" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "target": {},
      "title": "Service: Test is down",
      "urgency": "high"
    },
    "type": "pages"
  }
}
EOF
                
##### 

```python
"""
Create On-Call Page returns "OK." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_paging_api import OnCallPagingApi
from datadog_api_client.v2.model.create_page_request import CreatePageRequest
from datadog_api_client.v2.model.create_page_request_data import CreatePageRequestData
from datadog_api_client.v2.model.create_page_request_data_attributes import CreatePageRequestDataAttributes
from datadog_api_client.v2.model.create_page_request_data_attributes_target import CreatePageRequestDataAttributesTarget
from datadog_api_client.v2.model.create_page_request_data_type import CreatePageRequestDataType
from datadog_api_client.v2.model.on_call_page_target_type import OnCallPageTargetType
from datadog_api_client.v2.model.page_urgency import PageUrgency

body = CreatePageRequest(
    data=CreatePageRequestData(
        attributes=CreatePageRequestDataAttributes(
            description="Page details.",
            tags=[
                "service:test",
            ],
            target=CreatePageRequestDataAttributesTarget(
                identifier="my-team",
                type=OnCallPageTargetType.TEAM_HANDLE,
            ),
            title="Page title",
            urgency=PageUrgency.LOW,
        ),
        type=CreatePageRequestDataType.PAGES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallPagingApi(api_client)
    response = api_instance.create_on_call_page(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Create On-Call Page returns "OK." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallPagingAPI.new

body = DatadogAPIClient::V2::CreatePageRequest.new({
  data: DatadogAPIClient::V2::CreatePageRequestData.new({
    attributes: DatadogAPIClient::V2::CreatePageRequestDataAttributes.new({
      description: "Page details.",
      tags: [
        "service:test",
      ],
      target: DatadogAPIClient::V2::CreatePageRequestDataAttributesTarget.new({
        identifier: "my-team",
        type: DatadogAPIClient::V2::OnCallPageTargetType::TEAM_HANDLE,
      }),
      title: "Page title",
      urgency: DatadogAPIClient::V2::PageUrgency::LOW,
    }),
    type: DatadogAPIClient::V2::CreatePageRequestDataType::PAGES,
  }),
})
p api_instance.create_on_call_page(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Create On-Call Page returns "OK." response

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
	body := datadogV2.CreatePageRequest{
		Data: &datadogV2.CreatePageRequestData{
			Attributes: &datadogV2.CreatePageRequestDataAttributes{
				Description: datadog.PtrString("Page details."),
				Tags: []string{
					"service:test",
				},
				Target: datadogV2.CreatePageRequestDataAttributesTarget{
					Identifier: datadog.PtrString("my-team"),
					Type:       datadogV2.ONCALLPAGETARGETTYPE_TEAM_HANDLE.Ptr(),
				},
				Title:   "Page title",
				Urgency: datadogV2.PAGEURGENCY_LOW,
			},
			Type: datadogV2.CREATEPAGEREQUESTDATATYPE_PAGES,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallPagingApi(apiClient)
	resp, r, err := api.CreateOnCallPage(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallPagingApi.CreateOnCallPage`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `OnCallPagingApi.CreateOnCallPage`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Create On-Call Page returns "OK." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallPagingApi;
import com.datadog.api.client.v2.model.CreatePageRequest;
import com.datadog.api.client.v2.model.CreatePageRequestData;
import com.datadog.api.client.v2.model.CreatePageRequestDataAttributes;
import com.datadog.api.client.v2.model.CreatePageRequestDataAttributesTarget;
import com.datadog.api.client.v2.model.CreatePageRequestDataType;
import com.datadog.api.client.v2.model.CreatePageResponse;
import com.datadog.api.client.v2.model.OnCallPageTargetType;
import com.datadog.api.client.v2.model.PageUrgency;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallPagingApi apiInstance = new OnCallPagingApi(defaultClient);

    CreatePageRequest body =
        new CreatePageRequest()
            .data(
                new CreatePageRequestData()
                    .attributes(
                        new CreatePageRequestDataAttributes()
                            .description("Page details.")
                            .tags(Collections.singletonList("service:test"))
                            .target(
                                new CreatePageRequestDataAttributesTarget()
                                    .identifier("my-team")
                                    .type(OnCallPageTargetType.TEAM_HANDLE))
                            .title("Page title")
                            .urgency(PageUrgency.LOW))
                    .type(CreatePageRequestDataType.PAGES));

    try {
      CreatePageResponse result = apiInstance.createOnCallPage(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallPagingApi#createOnCallPage");
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
// Create On-Call Page returns "OK." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call_paging::OnCallPagingAPI;
use datadog_api_client::datadogV2::model::CreatePageRequest;
use datadog_api_client::datadogV2::model::CreatePageRequestData;
use datadog_api_client::datadogV2::model::CreatePageRequestDataAttributes;
use datadog_api_client::datadogV2::model::CreatePageRequestDataAttributesTarget;
use datadog_api_client::datadogV2::model::CreatePageRequestDataType;
use datadog_api_client::datadogV2::model::OnCallPageTargetType;
use datadog_api_client::datadogV2::model::PageUrgency;

#[tokio::main]
async fn main() {
    let body = CreatePageRequest::new().data(
        CreatePageRequestData::new(CreatePageRequestDataType::PAGES).attributes(
            CreatePageRequestDataAttributes::new(
                CreatePageRequestDataAttributesTarget::new()
                    .identifier("my-team".to_string())
                    .type_(OnCallPageTargetType::TEAM_HANDLE),
                "Page title".to_string(),
                PageUrgency::LOW,
            )
            .description("Page details.".to_string())
            .tags(vec!["service:test".to_string()]),
        ),
    );
    let configuration = datadog::Configuration::new();
    let api = OnCallPagingAPI::with_config(configuration);
    let resp = api.create_on_call_page(body).await;
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
 * Create On-Call Page returns "OK." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallPagingApi(configuration);

const params: v2.OnCallPagingApiCreateOnCallPageRequest = {
  body: {
    data: {
      attributes: {
        description: "Page details.",
        tags: ["service:test"],
        target: {
          identifier: "my-team",
          type: "team_handle",
        },
        title: "Page title",
        urgency: "low",
      },
      type: "pages",
    },
  },
};

apiInstance
  .createOnCallPage(params)
  .then((data: v2.CreatePageResponse) => {
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

## Acknowledge On-Call Page{% #acknowledge-on-call-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                         |
| ----------------- | ------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://saffron.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/acknowledge |
| ap2.datadoghq.com | POST https://lava.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/acknowledge    |
| app.datadoghq.eu  | POST https://beige.oncall.datadoghq.eu/api/v2/on-call/pages/{page_id}/acknowledge    |
| app.ddog-gov.com  | POST https://navy.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/acknowledge    |
| app.datadoghq.com | POST https://navy.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/acknowledge    |
| us3.datadoghq.com | POST https://teal.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/acknowledge    |
| us5.datadoghq.com | POST https://coral.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/acknowledge   |

### Overview

Acknowledges an On-Call Page.

### Arguments

#### Path Parameters

| Name                      | Type   | Description  |
| ------------------------- | ------ | ------------ |
| page_id [*required*] | string | The page ID. |

### Response

{% tab title="202" %}
Accepted.
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
                  \# Path parametersexport page_id="15e74b8b-f865-48d0-bcc5-453323ed2c8f"\# Curl commandcurl -X POST "https://saffron.oncall.datadoghq.com"https://lava.oncall.datadoghq.com"https://beige.oncall.datadoghq.eu"https://navy.oncall.datadoghq.com"https://navy.oncall.datadoghq.com"https://teal.oncall.datadoghq.com"https://coral.oncall.datadoghq.com/api/v2/on-call/pages/${page_id}/acknowledge" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Acknowledge On-Call Page returns "Accepted." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_paging_api import OnCallPagingApi
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallPagingApi(api_client)
    api_instance.acknowledge_on_call_page(
        page_id=UUID("15e74b8b-f865-48d0-bcc5-453323ed2c8f"),
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Acknowledge On-Call Page returns "Accepted." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallPagingAPI.new
p api_instance.acknowledge_on_call_page("15e74b8b-f865-48d0-bcc5-453323ed2c8f")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Acknowledge On-Call Page returns "Accepted." response

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
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallPagingApi(apiClient)
	r, err := api.AcknowledgeOnCallPage(ctx, uuid.MustParse("15e74b8b-f865-48d0-bcc5-453323ed2c8f"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallPagingApi.AcknowledgeOnCallPage`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Acknowledge On-Call Page returns "Accepted." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallPagingApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallPagingApi apiInstance = new OnCallPagingApi(defaultClient);

    try {
      apiInstance.acknowledgeOnCallPage(UUID.fromString("15e74b8b-f865-48d0-bcc5-453323ed2c8f"));
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallPagingApi#acknowledgeOnCallPage");
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
// Acknowledge On-Call Page returns "Accepted." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call_paging::OnCallPagingAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OnCallPagingAPI::with_config(configuration);
    let resp = api
        .acknowledge_on_call_page(
            Uuid::parse_str("15e74b8b-f865-48d0-bcc5-453323ed2c8f").expect("invalid UUID"),
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
 * Acknowledge On-Call Page returns "Accepted." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallPagingApi(configuration);

const params: v2.OnCallPagingApiAcknowledgeOnCallPageRequest = {
  pageId: "15e74b8b-f865-48d0-bcc5-453323ed2c8f",
};

apiInstance
  .acknowledgeOnCallPage(params)
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

## Escalate On-Call Page{% #escalate-on-call-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                      |
| ----------------- | --------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://saffron.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/escalate |
| ap2.datadoghq.com | POST https://lava.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/escalate    |
| app.datadoghq.eu  | POST https://beige.oncall.datadoghq.eu/api/v2/on-call/pages/{page_id}/escalate    |
| app.ddog-gov.com  | POST https://navy.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/escalate    |
| app.datadoghq.com | POST https://navy.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/escalate    |
| us3.datadoghq.com | POST https://teal.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/escalate    |
| us5.datadoghq.com | POST https://coral.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/escalate   |

### Overview

Escalates an On-Call Page.

### Arguments

#### Path Parameters

| Name                      | Type   | Description  |
| ------------------------- | ------ | ------------ |
| page_id [*required*] | string | The page ID. |

### Response

{% tab title="202" %}
Accepted.
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
                  \# Path parametersexport page_id="15e74b8b-f865-48d0-bcc5-453323ed2c8f"\# Curl commandcurl -X POST "https://saffron.oncall.datadoghq.com"https://lava.oncall.datadoghq.com"https://beige.oncall.datadoghq.eu"https://navy.oncall.datadoghq.com"https://navy.oncall.datadoghq.com"https://teal.oncall.datadoghq.com"https://coral.oncall.datadoghq.com/api/v2/on-call/pages/${page_id}/escalate" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Escalate On-Call Page returns "Accepted." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_paging_api import OnCallPagingApi
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallPagingApi(api_client)
    api_instance.escalate_on_call_page(
        page_id=UUID("15e74b8b-f865-48d0-bcc5-453323ed2c8f"),
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Escalate On-Call Page returns "Accepted." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallPagingAPI.new
p api_instance.escalate_on_call_page("15e74b8b-f865-48d0-bcc5-453323ed2c8f")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Escalate On-Call Page returns "Accepted." response

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
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallPagingApi(apiClient)
	r, err := api.EscalateOnCallPage(ctx, uuid.MustParse("15e74b8b-f865-48d0-bcc5-453323ed2c8f"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallPagingApi.EscalateOnCallPage`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Escalate On-Call Page returns "Accepted." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallPagingApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallPagingApi apiInstance = new OnCallPagingApi(defaultClient);

    try {
      apiInstance.escalateOnCallPage(UUID.fromString("15e74b8b-f865-48d0-bcc5-453323ed2c8f"));
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallPagingApi#escalateOnCallPage");
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
// Escalate On-Call Page returns "Accepted." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call_paging::OnCallPagingAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OnCallPagingAPI::with_config(configuration);
    let resp = api
        .escalate_on_call_page(
            Uuid::parse_str("15e74b8b-f865-48d0-bcc5-453323ed2c8f").expect("invalid UUID"),
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
 * Escalate On-Call Page returns "Accepted." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallPagingApi(configuration);

const params: v2.OnCallPagingApiEscalateOnCallPageRequest = {
  pageId: "15e74b8b-f865-48d0-bcc5-453323ed2c8f",
};

apiInstance
  .escalateOnCallPage(params)
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

## Resolve On-Call Page{% #resolve-on-call-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://saffron.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/resolve |
| ap2.datadoghq.com | POST https://lava.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/resolve    |
| app.datadoghq.eu  | POST https://beige.oncall.datadoghq.eu/api/v2/on-call/pages/{page_id}/resolve    |
| app.ddog-gov.com  | POST https://navy.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/resolve    |
| app.datadoghq.com | POST https://navy.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/resolve    |
| us3.datadoghq.com | POST https://teal.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/resolve    |
| us5.datadoghq.com | POST https://coral.oncall.datadoghq.com/api/v2/on-call/pages/{page_id}/resolve   |

### Overview

Resolves an On-Call Page.

### Arguments

#### Path Parameters

| Name                      | Type   | Description  |
| ------------------------- | ------ | ------------ |
| page_id [*required*] | string | The page ID. |

### Response

{% tab title="202" %}
Accepted.
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
                  \# Path parametersexport page_id="15e74b8b-f865-48d0-bcc5-453323ed2c8f"\# Curl commandcurl -X POST "https://saffron.oncall.datadoghq.com"https://lava.oncall.datadoghq.com"https://beige.oncall.datadoghq.eu"https://navy.oncall.datadoghq.com"https://navy.oncall.datadoghq.com"https://teal.oncall.datadoghq.com"https://coral.oncall.datadoghq.com/api/v2/on-call/pages/${page_id}/resolve" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Resolve On-Call Page returns "Accepted." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_paging_api import OnCallPagingApi
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallPagingApi(api_client)
    api_instance.resolve_on_call_page(
        page_id=UUID("15e74b8b-f865-48d0-bcc5-453323ed2c8f"),
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Resolve On-Call Page returns "Accepted." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OnCallPagingAPI.new
p api_instance.resolve_on_call_page("15e74b8b-f865-48d0-bcc5-453323ed2c8f")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Resolve On-Call Page returns "Accepted." response

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
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewOnCallPagingApi(apiClient)
	r, err := api.ResolveOnCallPage(ctx, uuid.MustParse("15e74b8b-f865-48d0-bcc5-453323ed2c8f"))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OnCallPagingApi.ResolveOnCallPage`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Resolve On-Call Page returns "Accepted." response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OnCallPagingApi;
import java.util.UUID;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OnCallPagingApi apiInstance = new OnCallPagingApi(defaultClient);

    try {
      apiInstance.resolveOnCallPage(UUID.fromString("15e74b8b-f865-48d0-bcc5-453323ed2c8f"));
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallPagingApi#resolveOnCallPage");
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
// Resolve On-Call Page returns "Accepted." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_on_call_paging::OnCallPagingAPI;
use uuid::Uuid;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OnCallPagingAPI::with_config(configuration);
    let resp = api
        .resolve_on_call_page(
            Uuid::parse_str("15e74b8b-f865-48d0-bcc5-453323ed2c8f").expect("invalid UUID"),
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
 * Resolve On-Call Page returns "Accepted." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OnCallPagingApi(configuration);

const params: v2.OnCallPagingApiResolveOnCallPageRequest = {
  pageId: "15e74b8b-f865-48d0-bcc5-453323ed2c8f",
};

apiInstance
  .resolveOnCallPage(params)
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
