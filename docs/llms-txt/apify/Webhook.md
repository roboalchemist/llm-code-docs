# Source: https://docs.apify.com/sdk/python/reference/class/Webhook.md

# Source: https://docs.apify.com/api/client/js/reference/interface/Webhook.md

# Webhook<!-- -->

Represents a webhook for receiving notifications about Actor events.

Webhooks send HTTP POST requests to specified URLs when certain events occur (e.g., Actor run succeeds, fails, or times out).

## Index[**](#Index)

### Properties

* [**condition](#condition)
* [**createdAt](#createdAt)
* [**description](#description)
* [**doNotRetry](#doNotRetry)
* [**eventTypes](#eventTypes)
* [**headersTemplate](#headersTemplate)
* [**id](#id)
* [**ignoreSslErrors](#ignoreSslErrors)
* [**isAdHoc](#isAdHoc)
* [**isApifyIntegration](#isApifyIntegration)
* [**lastDispatch](#lastDispatch)
* [**modifiedAt](#modifiedAt)
* [**payloadTemplate](#payloadTemplate)
* [**requestUrl](#requestUrl)
* [**shouldInterpolateStrings](#shouldInterpolateStrings)
* [**stats](#stats)
* [**userId](#userId)

## Properties<!-- -->[**](#Properties)

### [**](#condition)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L135)condition

**condition: [WebhookCondition](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookCondition)

### [**](#createdAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L131)createdAt

**createdAt: Date

### [**](#description)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L145)optionaldescription

**description?

<!-- -->

: string

### [**](#doNotRetry)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L137)doNotRetry

**doNotRetry: boolean

### [**](#eventTypes)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L134)eventTypes

**eventTypes: [WebhookEventType](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookEventType)\[]

### [**](#headersTemplate)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L144)optionalheadersTemplate

**headersTemplate?

<!-- -->

: string

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L129)id

**id: string

### [**](#ignoreSslErrors)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L136)ignoreSslErrors

**ignoreSslErrors: boolean

### [**](#isAdHoc)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L133)isAdHoc

**isAdHoc: boolean

### [**](#isApifyIntegration)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L143)optionalisApifyIntegration

**isApifyIntegration?

<!-- -->

: boolean

### [**](#lastDispatch)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L140)lastDispatch

**lastDispatch: string

### [**](#modifiedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L132)modifiedAt

**modifiedAt: Date

### [**](#payloadTemplate)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L139)payloadTemplate

**payloadTemplate: string

### [**](#requestUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L138)requestUrl

**requestUrl: string

### [**](#shouldInterpolateStrings)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L142)shouldInterpolateStrings

**shouldInterpolateStrings: boolean

### [**](#stats)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L141)stats

**stats: [WebhookStats](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookStats.md)

### [**](#userId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L130)userId

**userId: string
