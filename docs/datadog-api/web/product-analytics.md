# Source: https://docs.datadoghq.com/api/latest/product-analytics/

# Product Analytics
Send server-side events to Product Analytics. Server-Side Events Ingestion allows you to collect custom events from any server-side source, and retains events for 15 months. Server-side events are helpful for understanding causes of a funnel drop-off which are external to the client-side (for example, payment processing error). See the [Product Analytics page](https://docs.datadoghq.com/product_analytics/) for more information.
## [Send server-side events](https://docs.datadoghq.com/api/latest/product-analytics/#send-server-side-events)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/product-analytics/#send-server-side-events-v2)


POST https://browser-intake.ap1.datadoghq.com/api/v2/prodlyticshttps://browser-intake.ap2.datadoghq.com/api/v2/prodlyticshttps://browser-intake.datadoghq.eu/api/v2/prodlyticshttps://browser-intake.datadoghq.com/api/v2/prodlyticshttps://browser-intake.us3.datadoghq.com/api/v2/prodlyticshttps://browser-intake.us5.datadoghq.com/api/v2/prodlyticsNot supported in the GOV region
### Overview
Send server-side events to Product Analytics. Server-side events are retained for 15 months.
Server-Side events in Product Analytics are helpful for tracking events that occur on the server, as opposed to client-side events, which are captured by Real User Monitoring (RUM) SDKs. This allows for a more comprehensive view of the user journey by including actions that happen on the server. Typical examples could be `checkout.completed` or `payment.processed`.
Ingested server-side events are integrated into Product Analytics to allow users to select and filter these events in the event picker, similar to how views or actions are handled.
**Requirements:**
  * At least one of `usr`, `account`, or `session` must be provided with a valid ID.
  * The `application.id` must reference a Product Analytics-enabled application.


**Custom Attributes:** Any additional fields in the payload are flattened and searchable as facets. For example, a payload with `{"customer": {"tier": "premium"}}` is searchable with the syntax `@customer.tier:premium` in Datadog.
The status codes answered by the HTTP API are:
  * 202: Accepted: The request has been accepted for processing
  * 400: Bad request (likely an issue in the payload formatting)
  * 401: Unauthorized (likely a missing API Key)
  * 403: Permission issue (likely using an invalid API Key)
  * 408: Request Timeout, request should be retried after some time
  * 413: Payload too large (batch is above 5MB uncompressed)
  * 429: Too Many Requests, request should be retried after some time
  * 500: Internal Server Error, the server encountered an unexpected condition that prevented it from fulfilling the request, request should be retried after some time
  * 503: Service Unavailable, the server is not ready to handle the request probably because it is overloaded, request should be retried after some time


### Request
#### Body Data (required)
Server-side event to send (JSON format).
  * [Model](https://docs.datadoghq.com/api/latest/product-analytics/)
  * [Example](https://docs.datadoghq.com/api/latest/product-analytics/)


Field
Type
Description
account
object
The account linked to your event.
id [_required_]
string
The account ID used in Datadog.
application [_required_]
object
The application in which you want to send your events.
id [_required_]
string
The application ID of your application. It can be found in your [application management page](https://app.datadoghq.com/rum/list).
event [_required_]
object
Fields used for the event.
name [_required_]
string
The name of your event, which is used for search in the same way as view or action names.
session
object
The session linked to your event.
id [_required_]
string
The session ID captured by the SDK.
type [_required_]
enum
The type of Product Analytics event. Must be `server` for server-side events. Allowed enum values: `server`
usr
object
The user linked to your event.
id [_required_]
string
The user ID used in Datadog.
```
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

Copy
### Response
  * [202](https://docs.datadoghq.com/api/latest/product-analytics/#SubmitProductAnalyticsEvent-202-v2)
  * [400](https://docs.datadoghq.com/api/latest/product-analytics/#SubmitProductAnalyticsEvent-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/product-analytics/#SubmitProductAnalyticsEvent-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/product-analytics/#SubmitProductAnalyticsEvent-403-v2)
  * [408](https://docs.datadoghq.com/api/latest/product-analytics/#SubmitProductAnalyticsEvent-408-v2)
  * [413](https://docs.datadoghq.com/api/latest/product-analytics/#SubmitProductAnalyticsEvent-413-v2)
  * [429](https://docs.datadoghq.com/api/latest/product-analytics/#SubmitProductAnalyticsEvent-429-v2)
  * [500](https://docs.datadoghq.com/api/latest/product-analytics/#SubmitProductAnalyticsEvent-500-v2)
  * [503](https://docs.datadoghq.com/api/latest/product-analytics/#SubmitProductAnalyticsEvent-503-v2)


Request accepted for processing (always 202 empty JSON).
  * [Model](https://docs.datadoghq.com/api/latest/product-analytics/)
  * [Example](https://docs.datadoghq.com/api/latest/product-analytics/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/product-analytics/)
  * [Example](https://docs.datadoghq.com/api/latest/product-analytics/)


Error response.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/product-analytics/)
  * [Example](https://docs.datadoghq.com/api/latest/product-analytics/)


Error response.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/product-analytics/)
  * [Example](https://docs.datadoghq.com/api/latest/product-analytics/)


Error response.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Request Timeout
  * [Model](https://docs.datadoghq.com/api/latest/product-analytics/)
  * [Example](https://docs.datadoghq.com/api/latest/product-analytics/)


Error response.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Payload Too Large
  * [Model](https://docs.datadoghq.com/api/latest/product-analytics/)
  * [Example](https://docs.datadoghq.com/api/latest/product-analytics/)


Error response.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Too Many Requests
  * [Model](https://docs.datadoghq.com/api/latest/product-analytics/)
  * [Example](https://docs.datadoghq.com/api/latest/product-analytics/)


Error response.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Internal Server Error
  * [Model](https://docs.datadoghq.com/api/latest/product-analytics/)
  * [Example](https://docs.datadoghq.com/api/latest/product-analytics/)


Error response.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
Service Unavailable
  * [Model](https://docs.datadoghq.com/api/latest/product-analytics/)
  * [Example](https://docs.datadoghq.com/api/latest/product-analytics/)


Error response.
Field
Type
Description
errors
[object]
Structured errors.
detail
string
Error message.
status
string
Error code.
title
string
Error title.
```
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

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/product-analytics/?code-lang=curl)


#####  Send server-side events
Copy
```
                  ## Event with account ID
# Send a server-side event linked to an account.
  
# Curl command  
curl -X POST "https://browser-intake.ap1.datadoghq.com"https://browser-intake.ap2.datadoghq.com"https://browser-intake.datadoghq.eu"https://browser-intake.datadoghq.com"https://browser-intake.us3.datadoghq.com"https://browser-intake.us5.datadoghq.com/api/v2/prodlytics" \
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
EOF  
## Event with custom attributes
# Send a server-side event with additional custom attributes.
  
# Curl command  
curl -X POST "https://browser-intake.ap1.datadoghq.com"https://browser-intake.ap2.datadoghq.com"https://browser-intake.datadoghq.eu"https://browser-intake.datadoghq.com"https://browser-intake.us3.datadoghq.com"https://browser-intake.us5.datadoghq.com/api/v2/prodlytics" \
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
EOF  
## Event with session ID
# Send a server-side event linked to a session.
  
# Curl command  
curl -X POST "https://browser-intake.ap1.datadoghq.com"https://browser-intake.ap2.datadoghq.com"https://browser-intake.datadoghq.eu"https://browser-intake.datadoghq.com"https://browser-intake.us3.datadoghq.com"https://browser-intake.us5.datadoghq.com/api/v2/prodlytics" \
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
EOF  
## Simple event with user ID
# Send a server-side event linked to a user.
  
# Curl command  
curl -X POST "https://browser-intake.ap1.datadoghq.com"https://browser-intake.ap2.datadoghq.com"https://browser-intake.datadoghq.eu"https://browser-intake.datadoghq.com"https://browser-intake.us3.datadoghq.com"https://browser-intake.us5.datadoghq.com/api/v2/prodlytics" \
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

                
```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=6a6e4900-1673-424b-852a-b36ae2a28eaa&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=f4bf989c-e978-4dba-b26d-71a49c7d98d1&pt=Product%20Analytics&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fproduct-analytics%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=6a6e4900-1673-424b-852a-b36ae2a28eaa&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=f4bf989c-e978-4dba-b26d-71a49c7d98d1&pt=Product%20Analytics&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fproduct-analytics%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=44c49a75-bee8-46ba-808f-0d7f2b6bc33d&bo=2&sid=ca97aff0f0bf11f0b225ebe7018368cd&vid=ca980060f0bf11f09385b797b877861f&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Product%20Analytics&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fproduct-analytics%2F&r=&lt=1318&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=6367)
