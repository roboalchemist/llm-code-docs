# Source: https://docs.apify.com/api/client/js/reference/interface/WebhookDispatch.md

# WebhookDispatch<!-- -->

## Index[**](#Index)

### Properties

* [**calls](#calls)
* [**createdAt](#createdAt)
* [**eventData](#eventData)
* [**eventType](#eventType)
* [**id](#id)
* [**status](#status)
* [**userId](#userId)
* [**webhook](#webhook)
* [**webhookId](#webhookId)

## Properties<!-- -->[**](#Properties)

### [**](#calls)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch.ts#L52)calls

**calls: [WebhookDispatchCall](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatchCall.md)\[]

### [**](#createdAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch.ts#L49)createdAt

**createdAt: Date

### [**](#eventData)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch.ts#L54)eventData

**eventData: null | [WebhookDispatchEventData](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatchEventData.md)

### [**](#eventType)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch.ts#L51)eventType

**eventType: [WebhookEventType](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookEventType)

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch.ts#L46)id

**id: string

### [**](#status)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch.ts#L50)status

**status: [WebhookDispatchStatus](https://docs.apify.com/api/client/js/api/client/js/reference/enum/WebhookDispatchStatus.md)

### [**](#userId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch.ts#L47)userId

**userId: string

### [**](#webhook)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch.ts#L53)webhook

**webhook: Pick<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md), isAdHoc | requestUrl>

### [**](#webhookId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch.ts#L48)webhookId

**webhookId: string
