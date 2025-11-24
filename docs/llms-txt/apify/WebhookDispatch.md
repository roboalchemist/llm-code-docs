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

### [**](#calls)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_dispatch.ts#L31)calls

**calls: [WebhookDispatchCall](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatchCall.md)\[]

### [**](#createdAt)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_dispatch.ts#L28)createdAt

**createdAt: Date

### [**](#eventData)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_dispatch.ts#L33)eventData

**eventData: null | [WebhookDispatchEventData](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatchEventData.md)

### [**](#eventType)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_dispatch.ts#L30)eventType

**eventType: [WebhookEventType](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookEventType)

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_dispatch.ts#L25)id

**id: string

### [**](#status)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_dispatch.ts#L29)status

**status: [WebhookDispatchStatus](https://docs.apify.com/api/client/js/api/client/js/reference/enum/WebhookDispatchStatus.md)

### [**](#userId)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_dispatch.ts#L26)userId

**userId: string

### [**](#webhook)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_dispatch.ts#L32)webhook

**webhook: Pick<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md), isAdHoc | requestUrl>

### [**](#webhookId)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_dispatch.ts#L27)webhookId

**webhookId: string
