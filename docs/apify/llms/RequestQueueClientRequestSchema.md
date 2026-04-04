# Source: https://docs.apify.com/api/client/js/reference/interface/RequestQueueClientRequestSchema.md

# RequestQueueClientRequestSchema<!-- -->

Complete schema for a request in the queue.

Represents a URL to be crawled along with its metadata, retry information, and custom data.

## Index[**](#Index)

### Properties

* [**errorMessages](#errorMessages)
* [**handledAt](#handledAt)
* [**headers](#headers)
* [**id](#id)
* [**loadedUrl](#loadedUrl)
* [**method](#method)
* [**noRetry](#noRetry)
* [**payload](#payload)
* [**retryCount](#retryCount)
* [**uniqueKey](#uniqueKey)
* [**url](#url)
* [**userData](#userData)

## Properties<!-- -->[**](#Properties)

### [**](#errorMessages)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L957)optionalerrorMessages

**errorMessages?

<!-- -->

: string\[]

### [**](#handledAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L960)optionalhandledAt

**handledAt?

<!-- -->

: string

### [**](#headers)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L958)optionalheaders

**headers?

<!-- -->

: Record\<string, string>

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L951)id

**id: string

### [**](#loadedUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L962)optionalloadedUrl

**loadedUrl?

<!-- -->

: string

### [**](#method)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L954)optionalmethod

**method?

<!-- -->

: [AllowedHttpMethods](https://docs.apify.com/api/client/js/api/client/js/reference.md#AllowedHttpMethods)

### [**](#noRetry)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L961)optionalnoRetry

**noRetry?

<!-- -->

: boolean

### [**](#payload)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L955)optionalpayload

**payload?

<!-- -->

: string

### [**](#retryCount)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L956)optionalretryCount

**retryCount?

<!-- -->

: number

### [**](#uniqueKey)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L952)uniqueKey

**uniqueKey: string

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L953)url

**url: string

### [**](#userData)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L959)optionaluserData

**userData?

<!-- -->

: Record\<string, unknown>
