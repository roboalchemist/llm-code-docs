# Source: https://docs.datadoghq.com/api/latest/product-analytics.md

---
title: Product Analytics
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Product Analytics
---

# Product Analytics

Send server-side events to Product Analytics. Server-Side Events Ingestion allows you to collect custom events from any server-side source, and retains events for 15 months. Server-side events are helpful for understanding causes of a funnel drop-off which are external to the client-side (for example, payment processing error). See the [Product Analytics page](https://docs.datadoghq.com/product_analytics/) for more information.

## Send server-side events{% #send-server-side-events %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://browser-intake.ap1.datadoghq.com/api/v2/prodlytics |
| ap2.datadoghq.com | POST https://browser-intake.ap2.datadoghq.com/api/v2/prodlytics |
| app.datadoghq.eu  | POST https://browser-intake.datadoghq.eu/api/v2/prodlytics      |
| app.datadoghq.com | POST https://browser-intake.datadoghq.com/api/v2/prodlytics     |
| us3.datadoghq.com | POST https://browser-intake.us3.datadoghq.com/api/v2/prodlytics |
| us5.datadoghq.com | POST https://browser-intake.us5.datadoghq.com/api/v2/prodlytics |
| app.ddog-gov.com  | POST Not supported in the GOV region                            |

### Overview



Send server-side events to Product Analytics. Server-side events are retained for 15 months.

Server-Side events in Product Analytics are helpful for tracking events that occur on the server, as opposed to client-side events, which are captured by Real User Monitoring (RUM) SDKs. This allows for a more comprehensive view of the user journey by including actions that happen on the server. Typical examples could be `checkout.completed` or `payment.processed`.

Ingested server-side events are integrated into Product Analytics to allow users to select and filter these events in the event picker, similar to how views or actions are handled.

**Requirements:**

- At least one of `usr`, `account`, or `session` must be provided with a valid ID.
- The `application.id` must reference a Product Analytics-enabled application.

**Custom Attributes:** Any additional fields in the payload are flattened and searchable as facets. For example, a payload with `{"customer": {"tier": "premium"}}` is searchable with the syntax `@customer.tier:premium` in Datadog.

The status codes answered by the HTTP API are:

- 202: Accepted: The request has been accepted for processing
- 400: Bad request (likely an issue in the payload formatting)
- 401: Unauthorized (likely a missing API Key)
- 403: Permission issue (likely using an invalid API Key)
- 408: Request Timeout, request should be retried after some time
- 413: Payload too large (batch is above 5MB uncompressed)
- 429: Too Many Requests, request should be retried after some time
- 500: Internal Server Error, the server encountered an unexpected condition that prevented it from fulfilling the request, request should be retried after some time
- 503: Service Unavailable, the server is not ready to handle the request probably because it is overloaded, request should be retried after some time



### Request

#### Body Data (required)

Server-side event to send (JSON format).

{% tab title="Model" %}

| Parent field | Field                         | Type   | Description                                                                                                                        |
| ------------ | ----------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------- |
|              | account                       | object | The account linked to your event.                                                                                                  |
| account      | id [*required*]          | string | The account ID used in Datadog.                                                                                                    |
|              | application [*required*] | object | The application in which you want to send your events.                                                                             |
| application  | id [*required*]          | string | The application ID of your application. It can be found in your [application management page](https://app.datadoghq.com/rum/list). |
|              | event [*required*]       | object | Fields used for the event.                                                                                                         |
| event        | name [*required*]        | string | The name of your event, which is used for search in the same way as view or action names.                                          |
|              | session                       | object | The session linked to your event.                                                                                                  |
| session      | id [*required*]          | string | The session ID captured by the SDK.                                                                                                |
|              | type [*required*]        | enum   | The type of Product Analytics event. Must be `server` for server-side events. Allowed enum values: `server`                        |
|              | usr                           | object | The user linked to your event.                                                                                                     |
| usr          | id [*required*]          | string | The user ID used in Datadog.                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "account": {
    "id": "account-67890"
  },
  "application": {
    "id": "123abcde-123a-123b-1234-123456789abc"
  },
  "event": {
    "name": "payment.processed"
  },
  "session": {
    "id": "session-abcdef"
  },
  "type": "server",
  "usr": {
    "id": "user-12345"
  }
}
```

{% /tab %}

### Response

{% tab title="202" %}
Request accepted for processing (always 202 empty JSON).
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
Error response.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
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
Error response.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="408" %}
Request Timeout
{% tab title="Model" %}
Error response.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="413" %}
Payload Too Large
{% tab title="Model" %}
Error response.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too Many Requests
{% tab title="Model" %}
Error response.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Error response.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="503" %}
Service Unavailable
{% tab title="Model" %}
Error response.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \## Event with account ID
# Send a server-side event linked to an account.
\# Curl commandcurl -X POST "https://browser-intake.ap1.datadoghq.com"https://browser-intake.ap2.datadoghq.com"https://browser-intake.datadoghq.eu"https://browser-intake.datadoghq.com"https://browser-intake.us3.datadoghq.com"https://browser-intake.us5.datadoghq.com/api/v2/prodlytics" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "account": {
    "id": "account-456"
  },
  "application": {
    "id": "123abcde-123a-123b-1234-123456789abc"
  },
  "event": {
    "name": "checkout.completed"
  },
  "type": "server"
}
EOF\## Event with custom attributes
# Send a server-side event with additional custom attributes.
\# Curl commandcurl -X POST "https://browser-intake.ap1.datadoghq.com"https://browser-intake.ap2.datadoghq.com"https://browser-intake.datadoghq.eu"https://browser-intake.datadoghq.com"https://browser-intake.us3.datadoghq.com"https://browser-intake.us5.datadoghq.com/api/v2/prodlytics" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "application": {
    "id": "123abcde-123a-123b-1234-123456789abc"
  },
  "customer": {
    "tier": "premium"
  },
  "event": {
    "name": "payment.processed"
  },
  "type": "server",
  "usr": {
    "id": "123"
  }
}
EOF\## Event with session ID
# Send a server-side event linked to a session.
\# Curl commandcurl -X POST "https://browser-intake.ap1.datadoghq.com"https://browser-intake.ap2.datadoghq.com"https://browser-intake.datadoghq.eu"https://browser-intake.datadoghq.com"https://browser-intake.us3.datadoghq.com"https://browser-intake.us5.datadoghq.com/api/v2/prodlytics" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "application": {
    "id": "123abcde-123a-123b-1234-123456789abc"
  },
  "event": {
    "name": "form.submitted"
  },
  "session": {
    "id": "session-789"
  },
  "type": "server"
}
EOF\## Simple event with user ID
# Send a server-side event linked to a user.
\# Curl commandcurl -X POST "https://browser-intake.ap1.datadoghq.com"https://browser-intake.ap2.datadoghq.com"https://browser-intake.datadoghq.eu"https://browser-intake.datadoghq.com"https://browser-intake.us3.datadoghq.com"https://browser-intake.us5.datadoghq.com/api/v2/prodlytics" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "application": {
    "id": "123abcde-123a-123b-1234-123456789abc"
  },
  "event": {
    "name": "payment.processed"
  },
  "type": "server",
  "usr": {
    "id": "123"
  }
}
EOF

#####

```python
"""
Send server-side events returns "Request accepted for processing (always 202 empty JSON)." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_server_side_event_item import ProductAnalyticsServerSideEventItem
from datadog_api_client.v2.model.product_analytics_server_side_event_item_account import (
    ProductAnalyticsServerSideEventItemAccount,
)
from datadog_api_client.v2.model.product_analytics_server_side_event_item_application import (
    ProductAnalyticsServerSideEventItemApplication,
)
from datadog_api_client.v2.model.product_analytics_server_side_event_item_event import (
    ProductAnalyticsServerSideEventItemEvent,
)
from datadog_api_client.v2.model.product_analytics_server_side_event_item_session import (
    ProductAnalyticsServerSideEventItemSession,
)
from datadog_api_client.v2.model.product_analytics_server_side_event_item_type import (
    ProductAnalyticsServerSideEventItemType,
)
from datadog_api_client.v2.model.product_analytics_server_side_event_item_usr import (
    ProductAnalyticsServerSideEventItemUsr,
)

body = ProductAnalyticsServerSideEventItem(
    account=ProductAnalyticsServerSideEventItemAccount(
        id="account-67890",
    ),
    application=ProductAnalyticsServerSideEventItemApplication(
        id="123abcde-123a-123b-1234-123456789abc",
    ),
    event=ProductAnalyticsServerSideEventItemEvent(
        name="payment.processed",
    ),
    session=ProductAnalyticsServerSideEventItemSession(
        id="session-abcdef",
    ),
    type=ProductAnalyticsServerSideEventItemType.SERVER,
    usr=ProductAnalyticsServerSideEventItemUsr(
        id="user-12345",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.submit_product_analytics_event(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comNot supported in the US1-FED region" DD_API_KEY="<DD_API_KEY>" python3 "example.py"
#####

```ruby
# Send server-side events returns "Request accepted for processing (always 202 empty JSON)." response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::ProductAnalyticsAPI.new

body = DatadogAPIClient::V2::ProductAnalyticsServerSideEventItem.new({
  account: DatadogAPIClient::V2::ProductAnalyticsServerSideEventItemAccount.new({
    id: "account-67890",
  }),
  application: DatadogAPIClient::V2::ProductAnalyticsServerSideEventItemApplication.new({
    id: "123abcde-123a-123b-1234-123456789abc",
  }),
  event: DatadogAPIClient::V2::ProductAnalyticsServerSideEventItemEvent.new({
    name: "payment.processed",
  }),
  session: DatadogAPIClient::V2::ProductAnalyticsServerSideEventItemSession.new({
    id: "session-abcdef",
  }),
  type: DatadogAPIClient::V2::ProductAnalyticsServerSideEventItemType::SERVER,
  usr: DatadogAPIClient::V2::ProductAnalyticsServerSideEventItemUsr.new({
    id: "user-12345",
  }),
})
p api_instance.submit_product_analytics_event(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comNot supported in the US1-FED region" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
#####

```go
// Send server-side events returns "Request accepted for processing (always 202 empty JSON)." response

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
    body := datadogV2.ProductAnalyticsServerSideEventItem{
        Account: &datadogV2.ProductAnalyticsServerSideEventItemAccount{
            Id: "account-67890",
        },
        Application: datadogV2.ProductAnalyticsServerSideEventItemApplication{
            Id: "123abcde-123a-123b-1234-123456789abc",
        },
        Event: datadogV2.ProductAnalyticsServerSideEventItemEvent{
            Name: "payment.processed",
        },
        Session: &datadogV2.ProductAnalyticsServerSideEventItemSession{
            Id: "session-abcdef",
        },
        Type: datadogV2.PRODUCTANALYTICSSERVERSIDEEVENTITEMTYPE_SERVER,
        Usr: &datadogV2.ProductAnalyticsServerSideEventItemUsr{
            Id: "user-12345",
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewProductAnalyticsApi(apiClient)
    resp, r, err := api.SubmitProductAnalyticsEvent(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ProductAnalyticsApi.SubmitProductAnalyticsEvent`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ProductAnalyticsApi.SubmitProductAnalyticsEvent`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comNot supported in the US1-FED region" DD_API_KEY="<DD_API_KEY>" go run "main.go"
#####

```java
// Send server-side events returns "Request accepted for processing (always 202 empty JSON)."
// response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ProductAnalyticsApi;
import com.datadog.api.client.v2.model.ProductAnalyticsServerSideEventItem;
import com.datadog.api.client.v2.model.ProductAnalyticsServerSideEventItemAccount;
import com.datadog.api.client.v2.model.ProductAnalyticsServerSideEventItemApplication;
import com.datadog.api.client.v2.model.ProductAnalyticsServerSideEventItemEvent;
import com.datadog.api.client.v2.model.ProductAnalyticsServerSideEventItemSession;
import com.datadog.api.client.v2.model.ProductAnalyticsServerSideEventItemType;
import com.datadog.api.client.v2.model.ProductAnalyticsServerSideEventItemUsr;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    ProductAnalyticsApi apiInstance = new ProductAnalyticsApi(defaultClient);

    ProductAnalyticsServerSideEventItem body =
        new ProductAnalyticsServerSideEventItem()
            .account(new ProductAnalyticsServerSideEventItemAccount().id("account-67890"))
            .application(
                new ProductAnalyticsServerSideEventItemApplication()
                    .id("123abcde-123a-123b-1234-123456789abc"))
            .event(new ProductAnalyticsServerSideEventItemEvent().name("payment.processed"))
            .session(new ProductAnalyticsServerSideEventItemSession().id("session-abcdef"))
            .type(ProductAnalyticsServerSideEventItemType.SERVER)
            .usr(new ProductAnalyticsServerSideEventItemUsr().id("user-12345"));

    try {
      apiInstance.submitProductAnalyticsEvent(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductAnalyticsApi#submitProductAnalyticsEvent");
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
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comNot supported in the US1-FED region" DD_API_KEY="<DD_API_KEY>" java "Example.java"
#####

```rust
// Send server-side events returns "Request accepted for processing (always 202
// empty JSON)." response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_product_analytics::ProductAnalyticsAPI;
use datadog_api_client::datadogV2::model::ProductAnalyticsServerSideEventItem;
use datadog_api_client::datadogV2::model::ProductAnalyticsServerSideEventItemAccount;
use datadog_api_client::datadogV2::model::ProductAnalyticsServerSideEventItemApplication;
use datadog_api_client::datadogV2::model::ProductAnalyticsServerSideEventItemEvent;
use datadog_api_client::datadogV2::model::ProductAnalyticsServerSideEventItemSession;
use datadog_api_client::datadogV2::model::ProductAnalyticsServerSideEventItemType;
use datadog_api_client::datadogV2::model::ProductAnalyticsServerSideEventItemUsr;

#[tokio::main]
async fn main() {
    let body = ProductAnalyticsServerSideEventItem::new(
        ProductAnalyticsServerSideEventItemApplication::new(
            "123abcde-123a-123b-1234-123456789abc".to_string(),
        ),
        ProductAnalyticsServerSideEventItemEvent::new("payment.processed".to_string()),
        ProductAnalyticsServerSideEventItemType::SERVER,
    )
    .account(ProductAnalyticsServerSideEventItemAccount::new(
        "account-67890".to_string(),
    ))
    .session(ProductAnalyticsServerSideEventItemSession::new(
        "session-abcdef".to_string(),
    ))
    .usr(ProductAnalyticsServerSideEventItemUsr::new(
        "user-12345".to_string(),
    ));
    let configuration = datadog::Configuration::new();
    let api = ProductAnalyticsAPI::with_config(configuration);
    let resp = api.submit_product_analytics_event(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comNot supported in the US1-FED region" DD_API_KEY="<DD_API_KEY>" cargo run
#####

```typescript
/**
 * Send server-side events returns "Request accepted for processing (always 202 empty JSON)." response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.ProductAnalyticsApi(configuration);

const params: v2.ProductAnalyticsApiSubmitProductAnalyticsEventRequest = {
  body: {
    account: {
      id: "account-67890",
    },
    application: {
      id: "123abcde-123a-123b-1234-123456789abc",
    },
    event: {
      name: "payment.processed",
    },
    session: {
      id: "session-abcdef",
    },
    type: "server",
    usr: {
      id: "user-12345",
    },
  },
};

apiInstance
  .submitProductAnalyticsEvent(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comNot supported in the US1-FED region" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"
{% /tab %}
