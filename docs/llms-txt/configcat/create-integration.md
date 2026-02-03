# Source: https://configcat.com/docs/api/reference/create-integration.md

# Create Integration

Copy page

This endpoint creates a new Integration in a specified Product identified by the `productId` parameter, which can be obtained from the [List Products](https://configcat.com/docs/api/reference/get-products.md) endpoint.

The Parameters dictionary differs for each IntegrationType:

* Datadog

  <!-- -->

  * `apikey`: Required. Datadog API key.
  * `site`: Datadog site. Available values: `Us`, `Eu`, `Us1Fed`, `Us3`, `Us5`. Default: `Us`.

* Slack

  <br />

  <!-- -->

  Connecting the Slack integration through the Public Management API will not post messages with the ConfigCat Feature Flags Slack app but with an incoming webhook.

  <!-- -->

  * `incoming_webhook.url`: Required. The [incoming webhook URL](https://api.slack.com/messaging/webhooks) where the integration should post messages.
  * `includeSensitiveData`: Set to "true" to include [sensitive (hashed) comparison values](https://configcat.com/docs/targeting/targeting-rule/user-condition.md#confidential-text-comparators). By default, the integration will mask these values in the posted messages. We recommend hiding sensitive comparison values for shared or public Slack channels.

* Amplitude

  <!-- -->

  * `apiKey`: Required. Amplitude API Key.
  * `secretKey`: Required. Amplitude Secret Key.

* Mixpanel

  <!-- -->

  * `serviceAccountUserName`: Required. Mixpanel Service Account Username.
  * `serviceAccountSecret`: Required. Mixpanel Service Account Secret.
  * `projectId`: Required. Mixpanel Project ID.
  * `server`: Mixpanel Server. Available values: `StandardServer`, `EUResidencyServer`. Default: `StandardServer`.

* Twilio Segment

  <!-- -->

  * `writeKey`: Required. Twilio Segment Write Key.
  * `server`: Twilio Segment Server. Available values: `Us`, `Eu`. Default: `Us`.

* PubNub (work in progress)

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 201
* 400
* 404
* 429

When the creation was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
