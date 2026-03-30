# Source: https://crawlee.dev/js/api/core/interface/HttpRequest.md

# HttpRequest<!-- --> \<TResponseType>

HTTP Request as accepted by [BaseHttpClient](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md) methods.

### Hierarchy

* *HttpRequest*
  * [HttpRequestOptions](https://crawlee.dev/js/api/core/interface/HttpRequestOptions.md)

## Index[**](#Index)

### Properties

* [**body](#body)
* [**cookieJar](#cookieJar)
* [**encoding](#encoding)
* [**followRedirect](#followRedirect)
* [**headerGenerator](#headerGenerator)
* [**headerGeneratorOptions](#headerGeneratorOptions)
* [**headers](#headers)
* [**insecureHTTPParser](#insecureHTTPParser)
* [**maxRedirects](#maxRedirects)
* [**method](#method)
* [**proxyUrl](#proxyUrl)
* [**responseType](#responseType)
* [**sessionToken](#sessionToken)
* [**signal](#signal)
* [**throwHttpErrors](#throwHttpErrors)
* [**timeout](#timeout)
* [**url](#url)
* [**useHeaderGenerator](#useHeaderGenerator)

## Properties<!-- -->[**](#Properties)

### [**](#body)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L84)optionalbody

**body?

<!-- -->

: string | Buffer\<ArrayBufferLike> | Readable | Generator\<unknown, any, any> | AsyncGenerator\<unknown, any, any> | FormDataLike

### [**](#cookieJar)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L89)optionalcookieJar

**cookieJar?

<!-- -->

: ToughCookieJar | PromiseCookieJar

### [**](#encoding)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L93)optionalencoding

**encoding?

<!-- -->

: BufferEncoding

### [**](#followRedirect)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L90)optionalfollowRedirect

**followRedirect?

<!-- -->

: boolean | (response) => boolean

### [**](#headerGenerator)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L101)optionalheaderGenerator

**headerGenerator?

<!-- -->

: { getHeaders: (options) => Record\<string, string> }

#### Type declaration

* ##### getHeaders: (options) => Record\<string, string>

  * * **(options): Record\<string, string>

    - #### Parameters

      * ##### options: Record\<string, unknown>

      #### Returns Record\<string, string>

### [**](#headerGeneratorOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L99)optionalheaderGeneratorOptions

**headerGeneratorOptions?

<!-- -->

: Record\<string, unknown>

### [**](#headers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L83)optionalheaders

**headers?

<!-- -->

: SimpleHeaders

### [**](#insecureHTTPParser)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L104)optionalinsecureHTTPParser

**insecureHTTPParser?

<!-- -->

: boolean

### [**](#maxRedirects)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L91)optionalmaxRedirects

**maxRedirects?

<!-- -->

: number

### [**](#method)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L82)optionalmethod

**method?

<!-- -->

: Method

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L98)optionalproxyUrl

**proxyUrl?

<!-- -->

: string

### [**](#responseType)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L94)optionalresponseType

**responseType?

<!-- -->

: TResponseType

### [**](#sessionToken)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L105)optionalsessionToken

**sessionToken?

<!-- -->

: object

### [**](#signal)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L86)optionalsignal

**signal?

<!-- -->

: AbortSignal

### [**](#throwHttpErrors)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L95)optionalthrowHttpErrors

**throwHttpErrors?

<!-- -->

: boolean

### [**](#timeout)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L87)optionaltimeout

**timeout?

<!-- -->

: Partial\<Timeout>

### [**](#url)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L81)url

**url: string | URL

### [**](#useHeaderGenerator)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L100)optionaluseHeaderGenerator

**useHeaderGenerator?

<!-- -->

: boolean
