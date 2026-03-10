# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/webhooks/webhooks-overview-part-1.mdx

# Webhooks Overview

Cash App Pay has created webhooks so that you can subscribe to our events and get notified about them. When an event occurs, Cash App Pay collects data about the event, creates an event notification, and sends the event notification to the webhook endpoints that are subscribed to the event type.
<br /> <br />We currently support around 10 different webhook event types you can subscribe to. A single webhook endpoint can subscribe to many event types. Some examples of webhook events that you can subscribe to are: payment state changes, customer is created/updated, grants are created/updated, etc. For each event that occurs, Cash App Pay sends a POST request to your webhook endpoint URL with the event details (in JSON format).
<br /> <br />Examples of ways you can use webhooks as a third-party developer include:

* Subscribe to `dispute.created` and `dispute.state.updated` webhooks to process Cash App Pay disputes as they're created and updated in real time.
* Subscribe to `grant.status.updated` webhooks to process grant updates such as a customer revoking an on-file grant within Cash App.
  <br /> The webhook endpoint URL must expect JSON data from a POST request and confirm the successful receipt of that data.  To subscribe to our webhook events see [Create a webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/create-webhook-endpoint).
  For a list of all Cash App Pay API events that you can subscribe to, see `event_type` under [List Webhook Events](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events).

## Webhooks API Operations

Cash App Pay provides the following webhook-related operations:

|           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Endpoints | [List webhook endpoints](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-endpoints) <br />[Create webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/create-webhook-endpoint) <br />[Retrieve webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/retrieve-webhook-endpoint)<br /> [Update webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/update-webhook-endpoint) <br />[Delete webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/delete-webhook-endpoint) |
| Events    | [List webhook events](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events)                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Static IP address

Webhooks from Cash App Pay originate from the following IP addresses. These are provided so you can allow access by these addresses through a firewall you are using.

* 52.43.5.66
* 35.160.162.127
* 35.164.233.105
* 52.201.69.179
* 18.215.196.131
* 18.235.28.71

## Before you start

* Define a URL that points to your application. Define an endpoint that directs webhook event notifications to your application.
* Allow traffic to ingress from Cash App Pay into the endpoint that you have defined so that it can receive the webhook events.
* Find out the Cash App Pay API version that your integration uses.
  <Note> The webhook events that you subscribe to must be supported by the API version you select. </Note>

## Requirements and limitations

To acknowledge the receipt of the event notification, the webhook endpoint URL must:

* accept HTTPS connection requests
* respond with a 2xx HTTP status code to Cash App Pay within the configured delivery timeout (defaults to 5 seconds)

You must update webhook endpoints with a new `api_key_id` when the previously assigned API key is rotated. See [Using API Keys](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/using-api-keys) for more details.

> Webhook events will not be successfully delivered for new domains until the new domain is allowlisted. New domains must be manually reviewed and allowlisted. It will typically take 1 business day to allowlist new domains. Contact Cash App Pay Partner Engineering Team if your URL is not allowlisted within the specified timeframe.

### SLA

Cash App Pay provides the following SLA for webhook event notifications:

* The initial event notification delivery will occur as soon as possible after the originating event
  > If the delivery times out, Cash App Pay will retry based on the table in Notification Retries.
* There is no guarantee of the delivery order of event notices.

### Notification retries

Cash App Pay assumes the delivery is unsuccessful in the following scenarios:

* A 2xx HTTP status code is not received within the delivery timeout field of the webhook endpoint subscription.
* A status code other than 2xx is returned.
  Cash App Pay retries the delivery of the event notification using exponential backoff for up to 72 hours after the originating event. After 72 hours, the notification is discarded and Cash App Pay does not attempt to resend the notification.

> Although this is true, you can still obtain the event notification by polling the [List Webhook Events endpoint](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events).

Cash App Pay uses exponential backoff to avoid spamming applications and retries notifications according to the schedule listed in the table below.

As an example, if Cash App Pay fails to deliver the event, it will try to send the event again in 1 second. If it fails again, it will try to send the event again in 1.15 seconds, which means that 2.15 seconds have elapsed since the initial attempt at delivery. Subsequent retries follow the retry schedule in the table below.

The exponential backoff retry policy is as follows:

* Interval: 1 second
* Exponent: 1.15
* Max Retries: 75

|               |                       |                          |              |              |
| ------------- | --------------------- | ------------------------ | ------------ | ------------ |
| Retry attempt | Time between attempts | Time since webhook event |              |              |
| 1             | 1 second              | 1 second                 |              |              |
| 2             | 1.15 seconds          |                          | 2.15 seconds |              |
| 3             |                       | 1.32 seconds             |              | 3.47 seconds |
| 4             |                       | 1.52 seconds             |              | 5.02 seconds |
| 5             | 1.75 seconds          | 6.77 seconds             |              |              |
| 6             | 2 seconds             | 8.77 seconds             |              |              |
| 7 – 75        | \~72 hours            | 72 hours                 |              |              |
