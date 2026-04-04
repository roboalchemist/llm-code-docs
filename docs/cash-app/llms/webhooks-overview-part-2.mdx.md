# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/webhooks/webhooks-overview-part-2.mdx

***

## stoplight-id: 6r66kled8wsfi

# Webhooks: Steps

## Step 1: Create a Webhook Endpoint To Subscribe to Cash App Pay Webhook Events

The webhook endpoint URL must expect JSON data from a POST request and confirm the successful receipt of that data. To subscribe to our webhook events see [Create a webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/create-webhook-endpoint). For a list of all Cash App Pay API events that you can subscribe to, see `event_type` under [List Webhook Events](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events).

The webhook endpoint must do the following:

* Receive a POST event notification.
* Respond with a 2xx HTTP status within the specified `delivery_timeout` (default 5 seconds).
* Accept HTTPS connections.
* Store the event notification data safely.
* Use the `event_id` field in the body of each event notification as an idempotency value. Your application should ignore any duplicate values.
* Use message versioning. If your application passes Cash App Pay event data to another application, you should add versioning to the data to avoid duplication and to make auditing of the data transfer easier.

<Note Title="Note">
  You can use a server endpoint as a webhook endpoint URL or you can create a serverless endpoint on services such as Amazon Web Services (AWS) or Google Cloud Platform. You can test a webhook endpoint URL with websites such as [https://webhook.site](https://webhook.site).
</Note>

### Format of an event notification

The following headers are included when making a POST request to the webhook endpoint to deliver the webhook event:

| Header                      | Value                                                                                                                                    | Description                                                                                                                                                                                                                                                         | Example                                                                                                                                           |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accept                      | `*/*`                                                                                                                                    | This [standard header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) ensures that the API client and Cash App Pay API are communicating using the same MIME type in the response payload.                                                 | `*/*`                                                                                                                                             |
| Accept-Encoding             | `gzip`                                                                                                                                   | The Accept-Encoding request HTTP header indicates the content encoding (usually a compression algorithm) that the client can understand                                                                                                                             | `gzip`  \`                                                                                                                                        |
| Authorization               | `Client {CLIENT_ID} {KEY_ID}`                                                                                                            | This [standard header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) is used to authenticate your API client with the                                                                                                                     | `Client CA-CI_CLIENT KEY_2f6cd0d5cc26b34ac878502`                                                                                                 |
| Content-Type                | `application/json; charset=utf-8`                                                                                                        | This [standard header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) ensures that the API client and Cash App Pay API are communicating using the same MIME type in the request payload                                                   | `application/json; charset=utf-8`                                                                                                                 |
| Date                        | `{DATETIME_IN_RFC_1123_FORMAT}`                                                                                                          | Contains the date and time at which the message originated.                                                                                                                                                                                                         | Sun, 21 Oct 2018 12:16:24 GMT                                                                                                                     |
| Host                        | `{DOMAIN_OF_ENDPOINT_URL}`                                                                                                               | Specifies the host and port number of the server to which the request is being sent.                                                                                                                                                                                | `api.cash.app`                                                                                                                                    |
| X-Retry-Count               | `{NUMBER_OF_RETRIES}`                                                                                                                    | The number of times Cash App Pay has resent a notification for the given event (including the current retry) as an integer. The retry number does not include the original notification and is only present when there has been at least one unsuccessful delivery. | 3                                                                                                                                                 |
| X-Signed-Headers            | `Accept: */*, Content-Type: application/json; charset=utf-8, Host: {DOMAIN_OF_ENDPOINT_URL}, Authorization: Client {CLIENT_ID} {KEY_ID}` | The headers used to generate the X-Signature.                                                                                                                                                                                                                       | `Accept: */*, Content-Type: application/json; charset=utf-8, Host: api.cash.app, Authorization: Client CA-CI_CLIENT KEY_2f6cd0d5cc26b34ac878502 ` |
| X-Signature                 | `V1 hash({METHOD}\n{URL_PATH}\n{HEADERS}\n{BODY_DIGEST}) `                                                                               | An HMAC-SHA-256 signature used to validate the event authenticity. See more at [X-Signature](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/signing-requests) header.                                                                  | `V1 2bc29db277b0e2949f478691d33fe1f535a9832da90037a853ebb9d4a351cc1b`                                                                             |
| X-Delivery-Configuration-Id | `{WEBHOOK_ENDPOINT_ID} `                                                                                                                 | The Cash App Pay-provided ID of the webhook endpoint. This is returned when calling the [Create Webhook Endpoint](/cash-app-pay-partner-api/api-reference/management-api/create-webhook-endpoint) API.                                                              | `WC_2f6cd0d5cc26b34ac8785026b14979 `                                                                                                              |

> **Webhook signatures:** Webhook deliveries also contain an X-Signature header that is computed using the same process as signing regular requests. This allows webhooks delivered by Cash App to be validated by computing the signature from the request payload and verifying that it matches the X-Signature header. See [Signing Requests](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/signing-requests) for more details.

The body of the webhook event has the following JSON schema:

|              |                                                                                                                                                                                         |                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Field        | Description                                                                                                                                                                             | Example                                                     |
| `type`       | The type of event that occurred.                                                                                                                                                        | `merchant.status.updated`                                   |
| `event_id`   | A unique identifier provided by Cash App for the event.                                                                                                                                 | `WE_78lusoltpu8r9shziq5hdnx96`                              |
| `created_at` | When this event occurred in RFC 3339 format (UTC).The time that the event is delivered may be significantly later than this timestamp due to webhooks being retried for up to 72 hours. | 2022-12-07T20:21:46.282Z                                    |
| `data`       | The data about the object that has a status change.                                                                                                                                     | See the next table for the attributes of the `data` object. |

The event’s `data` object contains the following attributes:

|          |                                                                            |                                |
| -------- | -------------------------------------------------------------------------- | ------------------------------ |
| Field    | Description                                                                | Example                        |
| `type`   | The name of the affected object's type.                                    | merchant                       |
| `id`     | The ID of the affected object.                                             | MMI\_4vxs5egfk7hmta3qx2h6rp91x |
| `object` | A JSON object containing the affected object's data relevant to the event. | See example code below         |

### Example code for the object

```json
{
      "id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
      "brand_id": "BRAND_8ereg0tug2yiik8vx24xpe5br",
      "name": "Example Business Name",
      "country": "US",
      "currency": "USD",
      "category": "5432",
      "reference_id": "external-id",
      "status": "ACTIVE",
      "created_at": "2022-01-01T12:00:00Z",
      "updated_at": "2022-01-05T12:00:00Z",
      "address": {
        "address_line_1": "1215 4th Ave",
        "address_line_2": "Suite 2300",
        "locality": "Seattle",
        "country": "US",
        "postal_code": "98161-1001",
        "administrative_district_level_1": "Washington"
      },
      "site_url": "http://example.com",
      "metadata": {}
}
```

### Example code for event notification `body`

```json
{
 "type": "merchant.status.updated",
 "event_id": "WE_78lusoltpu8r9shziq5hdnx96",
 "created_at": "2022-12-07T20:21:46.282Z",
 "data": {
   "id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
   "object": {
     "id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
     "brand_id": "BRAND_8ereg0tug2yiik8vx24xpe5br",
     "name": "Example Business Name",
     "country": "US",
     "currency": "USD",
     "category": "5432",
     "reference_id": "external-id",
     "status": "ACTIVE",
     "created_at": "2022-01-01T12:00:00Z",
     "updated_at": "2022-01-05T12:00:00Z",
     "address": {
       "address_line_1": "1215 4th Ave",
       "address_line_2": "Suite 2300",
       "locality": "Seattle",
       "country": "US",
       "postal_code": "98161-1001",
       "administrative_district_level_1": "Washington"
     },
     "site_url": "http://example.com",
     "metadata": {}
   },
   "type": "merchant"
 }
}
```

<br />

<br />

## Step 2: Verify and Validate Event Notifications in Sandbox

You can test webhook endpoints in our Sandbox environments both on an App and on the web. Go to the following links to learn more:

* [Sandbox App](/cash-app-pay-partner-api/guides/technical-guides/sandbox/sandbox-app)
* [Sandbox Web](/cash-app-pay-partner-api/guides/technical-guides/sandbox/developer-sandbox)

## Step 3: Manage Webhook Operations

There are two aspects of Cash App Pay webhook events that you must understand:

* When are events triggered?
* How to manage event notifications?

For a list of all Cash App Pay API events that you can subscribe to, see `event_type` under [List webhook events](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events).

### Understand when events are triggered

Events that you can subscribe to using webhooks are generated by the various Cash App Pay applications and APIs. For example, during a sales transaction, several events could be generated including an updated payment received, customer created, grant declined, etc.

### Manage event notifications

When your webhook endpoint URL receives an event notification, you must respond within the specified delivery timeout (or default 5 seconds) to the POST and store the event information securely.

<Note>
   Cloud-based serverless applications, microservices, and function as a service (FaaS) applications let you handle event notifications without setting up a server. 
</Note>

## Step 4: Move Webhook Event Notifications to Production

When your application is ready to be moved from the Sandbox environment to production, there are several tasks you must complete to manage webhook event notifications in production. These include the following:

* Get production application credentials from the Cash App Pay Partner Engineering team.
  > The base URL for calling Sandbox endpoints is `sandbox.api.cash.app`. When you move your application to production, you need production credentials and you must use `api.cash.app` as the base URL.
* Update API calls to use the new credentials. Update your code to make API calls to Cash App Pay production endpoints.
* Use the `event_id` field in the body of each event notification as an idempotency value. Your application should ignore any duplicate values.
* Use message versioning. If your application passes Cash App Pay data to another application, you should add versioning to the data before passing it to avoid duplication and to make auditing of the data transfer easier.
* Validate the webhook event notification. A non-Cash App Pay POST can potentially compromise your application. All webhook notifications from Cash App Pay include an `X-Signed-Headers` and `X-Signature` header. See [Signing Requests](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/signing-requests) for more information.

## Handling a deleted customer webhook

The `customer.deleted` webhook event is delivered when a Cash App customer account is deleted.
This operation is often related to requests to forget a customer's data (for example, CCPA/GDPR), so that the customer
data in the webhook event does not contain any data that the customer provided (for example, a Cashtag). Since the
customer reference ID is provided by the API client, not the customer, any reference ID previously
attached to the customer will be included in the webhook event data.

When a customer account is deleted, all active grants for that customer are automatically revoked. Any
future attempts to use grants associated with that customer will fail. Any attempt to retrieve the customer
through the API will return a `CUSTOMER_DELETED_ACCOUNT` error.

<Note>
   As a best practice, when they receive a deleted customer webhook event, developers must delete any customer PII associated with the Cash App customer that was deleted. 
</Note>
