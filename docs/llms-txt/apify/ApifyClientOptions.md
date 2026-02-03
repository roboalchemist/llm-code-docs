# Source: https://docs.apify.com/sdk/js/reference/interface/ApifyClientOptions.md

# Source: https://docs.apify.com/api/client/js/reference/interface/ApifyClientOptions.md

# ApifyClientOptions<!-- -->

Configuration options for ApifyClient.

## Index[**](#Index)

### Properties

* [**baseUrl](#baseUrl)
* [**maxRetries](#maxRetries)
* [**minDelayBetweenRetriesMillis](#minDelayBetweenRetriesMillis)
* [**publicBaseUrl](#publicBaseUrl)
* [**requestInterceptors](#requestInterceptors)
* [**timeoutSecs](#timeoutSecs)
* [**token](#token)
* [**userAgentSuffix](#userAgentSuffix)

## Properties<!-- -->[**](#Properties)

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L570)optionalbaseUrl

**baseUrl?

<!-- -->

: string = https\://api.apify.com

### [**](#maxRetries)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L574)optionalmaxRetries

**maxRetries?

<!-- -->

: number = 8

### [**](#minDelayBetweenRetriesMillis)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L576)optionalminDelayBetweenRetriesMillis

**minDelayBetweenRetriesMillis?

<!-- -->

: number = 500

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L572)optionalpublicBaseUrl

**publicBaseUrl?

<!-- -->

: string = https\://api.apify.com

### [**](#requestInterceptors)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L578)optionalrequestInterceptors

**requestInterceptors?

<!-- -->

: (undefined | null | (value) => ApifyRequestConfig | Promise\<ApifyRequestConfig>)\[] = \[]

### [**](#timeoutSecs)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L580)optionaltimeoutSecs

**timeoutSecs?

<!-- -->

: number = 360

### [**](#token)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L581)optionaltoken

**token?

<!-- -->

: string

### [**](#userAgentSuffix)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L582)optionaluserAgentSuffix

**userAgentSuffix?

<!-- -->

: string | string\[]
