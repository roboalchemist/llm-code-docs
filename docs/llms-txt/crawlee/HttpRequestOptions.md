# Source: https://crawlee.dev/js/api/core/interface/HttpRequestOptions.md

# HttpRequestOptions<!-- --> \<TResponseType>

Additional options for HTTP requests that need to be handled separately before passing to [BaseHttpClient](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md).

### Hierarchy

* [HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)\<TResponseType>
  * *HttpRequestOptions*

## Index[**](#Index)

### Properties

* [**body](#body)
* [**cookieJar](#cookieJar)
* [**encoding](#encoding)
* [**followRedirect](#followRedirect)
* [**form](#form)
* [**headerGenerator](#headerGenerator)
* [**headerGeneratorOptions](#headerGeneratorOptions)
* [**headers](#headers)
* [**insecureHTTPParser](#insecureHTTPParser)
* [**json](#json)
* [**maxRedirects](#maxRedirects)
* [**method](#method)
* [**password](#password)
* [**proxyUrl](#proxyUrl)
* [**responseType](#responseType)
* [**searchParams](#searchParams)
* [**sessionToken](#sessionToken)
* [**signal](#signal)
* [**throwHttpErrors](#throwHttpErrors)
* [**timeout](#timeout)
* [**url](#url)
* [**useHeaderGenerator](#useHeaderGenerator)
* [**username](#username)

## Properties<!-- -->[**](#Properties)

### [**](#body)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L84)optionalinheritedbody

**body?

<!-- -->

: string | Buffer\<ArrayBufferLike> | Readable | Generator\<unknown, any, any> | AsyncGenerator\<unknown, any, any> | FormDataLike

Inherited from HttpRequest.body

### [**](#cookieJar)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L89)optionalinheritedcookieJar

**cookieJar?

<!-- -->

: ToughCookieJar | PromiseCookieJar

Inherited from HttpRequest.cookieJar

### [**](#encoding)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L93)optionalinheritedencoding

**encoding?

<!-- -->

: BufferEncoding

Inherited from HttpRequest.encoding

### [**](#followRedirect)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L90)optionalinheritedfollowRedirect

**followRedirect?

<!-- -->

: boolean | (response) => boolean

Inherited from HttpRequest.followRedirect

### [**](#form)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L117)optionalform

**form?

<!-- -->

: Record\<string, string>

A form to be sent in the HTTP request body (URL encoding will be used)

### [**](#headerGenerator)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L101)optionalinheritedheaderGenerator

**headerGenerator?

<!-- -->

: { getHeaders: (options) => Record\<string, string> }

Inherited from HttpRequest.headerGenerator

#### Type declaration

* ##### getHeaders: (options) => Record\<string, string>

  * * **(options): Record\<string, string>

    - #### Parameters

      * ##### options: Record\<string, unknown>

      #### Returns Record\<string, string>

### [**](#headerGeneratorOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L99)optionalinheritedheaderGeneratorOptions

**headerGeneratorOptions?

<!-- -->

: Record\<string, unknown>

Inherited from HttpRequest.headerGeneratorOptions

### [**](#headers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L83)optionalinheritedheaders

**headers?

<!-- -->

: SimpleHeaders

Inherited from HttpRequest.headers

### [**](#insecureHTTPParser)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L104)optionalinheritedinsecureHTTPParser

**insecureHTTPParser?

<!-- -->

: boolean

Inherited from HttpRequest.insecureHTTPParser

### [**](#json)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L119)optionaljson

**json?

<!-- -->

: unknown

Artbitrary object to be JSON-serialized and sent as the HTTP request body

### [**](#maxRedirects)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L91)optionalinheritedmaxRedirects

**maxRedirects?

<!-- -->

: number

Inherited from HttpRequest.maxRedirects

### [**](#method)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L82)optionalinheritedmethod

**method?

<!-- -->

: Method

Inherited from HttpRequest.method

### [**](#password)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L124)optionalpassword

**password?

<!-- -->

: string

Basic HTTP Auth password

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L98)optionalinheritedproxyUrl

**proxyUrl?

<!-- -->

: string

Inherited from HttpRequest.proxyUrl

### [**](#responseType)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L94)optionalinheritedresponseType

**responseType?

<!-- -->

: TResponseType

Inherited from HttpRequest.responseType

### [**](#searchParams)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L114)optionalsearchParams

**searchParams?

<!-- -->

: [SearchParams](https://crawlee.dev/js/api/utils.md#SearchParams)

Search (query string) parameters to be appended to the request URL

### [**](#sessionToken)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L105)optionalinheritedsessionToken

**sessionToken?

<!-- -->

: object

Inherited from HttpRequest.sessionToken

### [**](#signal)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L86)optionalinheritedsignal

**signal?

<!-- -->

: AbortSignal

Inherited from HttpRequest.signal

### [**](#throwHttpErrors)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L95)optionalinheritedthrowHttpErrors

**throwHttpErrors?

<!-- -->

: boolean

Inherited from HttpRequest.throwHttpErrors

### [**](#timeout)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L87)optionalinheritedtimeout

**timeout?

<!-- -->

: Partial\<Timeout>

Inherited from HttpRequest.timeout

### [**](#url)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L81)inheritedurl

**url: string | URL

Inherited from HttpRequest.url

### [**](#useHeaderGenerator)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L100)optionalinheriteduseHeaderGenerator

**useHeaderGenerator?

<!-- -->

: boolean

Inherited from HttpRequest.useHeaderGenerator

### [**](#username)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L122)optionalusername

**username?

<!-- -->

: string

Basic HTTP Auth username
