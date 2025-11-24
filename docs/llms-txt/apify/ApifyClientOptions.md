# Source: https://docs.apify.com/sdk/js/reference/interface/ApifyClientOptions.md

# Source: https://docs.apify.com/api/client/js/reference/interface/ApifyClientOptions.md

# ApifyClientOptions<!-- -->

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

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L358)optionalbaseUrl

**baseUrl?

<!-- -->

: string = https\://api.apify.com

### [**](#maxRetries)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L362)optionalmaxRetries

**maxRetries?

<!-- -->

: number = 8

### [**](#minDelayBetweenRetriesMillis)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L364)optionalminDelayBetweenRetriesMillis

**minDelayBetweenRetriesMillis?

<!-- -->

: number = 500

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L360)optionalpublicBaseUrl

**publicBaseUrl?

<!-- -->

: string = https\://api.apify.com

### [**](#requestInterceptors)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L366)optionalrequestInterceptors

**requestInterceptors?

<!-- -->

: (undefined | null | (value) => ApifyRequestConfig | Promise\<ApifyRequestConfig>)\[] = \[]

### [**](#timeoutSecs)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L368)optionaltimeoutSecs

**timeoutSecs?

<!-- -->

: number = 360

### [**](#token)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L369)optionaltoken

**token?

<!-- -->

: string

### [**](#userAgentSuffix)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L370)optionaluserAgentSuffix

**userAgentSuffix?

<!-- -->

: string | string\[]
