# Source: https://docs.apify.com/sdk/js/reference/interface/WebhookOptions.md

# WebhookOptions<!-- -->

## Index[**](#Index)

### Properties

* [**eventTypes](#eventTypes)
* [**idempotencyKey](#idempotencyKey)
* [**payloadTemplate](#payloadTemplate)
* [**requestUrl](#requestUrl)

## Properties<!-- -->[**](#Properties)

### [**](#eventTypes)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1920)eventTypes

**eventTypes: readonly

<!-- -->

WebhookEventType\[]

Array of event types, which you can set for Actor run, see the [Actor run events](https://docs.apify.com/webhooks/events#actor-run) in the Apify doc.

### [**](#idempotencyKey)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1943)optionalidempotencyKey

**idempotencyKey?

<!-- -->

: string

Idempotency key enables you to ensure that a webhook will not be added multiple times in case of an Actor restart or other situation that would cause the `addWebhook()` function to be called again. We suggest using the Actor run ID as the idempotency key. You can get the run ID by calling [Actor.getEnv](https://docs.apify.com/sdk/js/sdk/js/reference/class/Actor.md#getEnv) function.

### [**](#payloadTemplate)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1935)optionalpayloadTemplate

**payloadTemplate?

<!-- -->

: string

Payload template is a JSON-like string that describes the structure of the webhook POST request payload. It uses JSON syntax, extended with a double curly braces syntax for injecting variables `{{variable}}`. Those variables are resolved at the time of the webhook's dispatch, and a list of available variables with their descriptions is available in the [Apify webhook documentation](https://docs.apify.com/webhooks). If `payloadTemplate` is omitted, the default payload template is used ([view docs](https://docs.apify.com/webhooks/actions#payload-template)).

### [**](#requestUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1925)requestUrl

**requestUrl: string

URL which will be requested using HTTP POST request, when Actor run will reach the set event type.
