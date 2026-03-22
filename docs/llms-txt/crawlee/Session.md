# Source: https://crawlee.dev/js/api/core/class/Session.md

# Session<!-- -->

Sessions are used to store information such as cookies and can be used for generating fingerprints and proxy sessions. You can imagine each session as a specific user, with its own cookies, IP (via proxy) and potentially a unique browser fingerprint. Session internal state can be enriched with custom user data for example some authorization tokens and specific headers in general.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**id](#id)
* [**userData](#userData)

### Accessors

* [**cookieJar](#cookieJar)
* [**createdAt](#createdAt)
* [**errorScore](#errorScore)
* [**errorScoreDecrement](#errorScoreDecrement)
* [**expiresAt](#expiresAt)
* [**maxErrorScore](#maxErrorScore)
* [**maxUsageCount](#maxUsageCount)
* [**usageCount](#usageCount)

### Methods

* [**getCookies](#getCookies)
* [**getCookieString](#getCookieString)
* [**getState](#getState)
* [**isBlocked](#isBlocked)
* [**isExpired](#isExpired)
* [**isMaxUsageCountReached](#isMaxUsageCountReached)
* [**isUsable](#isUsable)
* [**markBad](#markBad)
* [**markGood](#markGood)
* [**retire](#retire)
* [**retireOnBlockedStatusCodes](#retireOnBlockedStatusCodes)
* [**setCookie](#setCookie)
* [**setCookies](#setCookies)
* [**setCookiesFromResponse](#setCookiesFromResponse)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L150)constructor

* ****new Session**(options): [Session](https://crawlee.dev/js/api/core/class/Session.md)

- Session configuration.

  ***

  #### Parameters

  * ##### options: [SessionOptions](https://crawlee.dev/js/api/core/interface/SessionOptions.md)

  #### Returns [Session](https://crawlee.dev/js/api/core/class/Session.md)

## Properties<!-- -->[**](#Properties)

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L101)readonlyid

**id: string

### [**](#userData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L103)userData

**userData: Dictionary

## Accessors<!-- -->[**](#Accessors)

### [**](#cookieJar)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L143)cookieJar

* **get cookieJar(): CookieJar

- #### Returns CookieJar

### [**](#createdAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L135)createdAt

* **get createdAt(): Date

- #### Returns Date

### [**](#errorScore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L115)errorScore

* **get errorScore(): number

- #### Returns number

### [**](#errorScoreDecrement)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L127)errorScoreDecrement

* **get errorScoreDecrement(): number

- #### Returns number

### [**](#expiresAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L131)expiresAt

* **get expiresAt(): Date

- #### Returns Date

### [**](#maxErrorScore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L123)maxErrorScore

* **get maxErrorScore(): number

- #### Returns number

### [**](#maxUsageCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L139)maxUsageCount

* **get maxUsageCount(): number

- #### Returns number

### [**](#usageCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L119)usageCount

* **get usageCount(): number

- #### Returns number

## Methods<!-- -->[**](#Methods)

### [**](#getCookies)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L374)getCookies

* ****getCookies**(url): [Cookie](https://crawlee.dev/js/api/core/interface/Cookie.md)\[]

- Returns cookies in a format compatible with puppeteer/playwright and ready to be used with `page.setCookie`.

  ***

  #### Parameters

  * ##### url: string

    website url. Only cookies stored for this url will be returned

  #### Returns [Cookie](https://crawlee.dev/js/api/core/interface/Cookie.md)\[]

### [**](#getCookieString)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L385)getCookieString

* ****getCookieString**(url): string

- Returns cookies saved with the session in the typical key1=value1; key2=value2 format, ready to be used in a cookie header or elsewhere.

  ***

  #### Parameters

  * ##### url: string

  #### Returns string

  Represents `Cookie` header.

### [**](#getState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L256)getState

* ****getState**(): [SessionState](https://crawlee.dev/js/api/core/interface/SessionState.md)

- Gets session state for persistence in KeyValueStore.

  ***

  #### Returns [SessionState](https://crawlee.dev/js/api/core/interface/SessionState.md)

  Represents session internal state.

### [**](#isBlocked)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L209)isBlocked

* ****isBlocked**(): boolean

- Indicates whether the session is blocked. Session is blocked once it reaches the `maxErrorScore`.

  ***

  #### Returns boolean

### [**](#isExpired)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L218)isExpired

* ****isExpired**(): boolean

- Indicates whether the session is expired. Session expiration is determined by the `maxAgeSecs`. Once the session is older than `createdAt + maxAgeSecs` the session is considered expired.

  ***

  #### Returns boolean

### [**](#isMaxUsageCountReached)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L226)isMaxUsageCountReached

* ****isMaxUsageCountReached**(): boolean

- Indicates whether the session is used maximum number of times. Session maximum usage count can be changed by `maxUsageCount` parameter.

  ***

  #### Returns boolean

### [**](#isUsable)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L234)isUsable

* ****isUsable**(): boolean

- Indicates whether the session can be used for next requests. Session is usable when it is not expired, not blocked and the maximum usage count has not be reached.

  ***

  #### Returns boolean

### [**](#markBad)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L291)markBad

* ****markBad**(): void

- Increases usage and error count. Should be used when the session has been used unsuccessfully. For example because of timeouts.

  ***

  #### Returns void

### [**](#markGood)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L242)markGood

* ****markGood**(): void

- This method should be called after a successful session usage. It increases `usageCount` and potentially lowers the `errorScore` by the `errorScoreDecrement`.

  ***

  #### Returns void

### [**](#retire)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L278)retire

* ****retire**(): void

- Marks session as blocked and emits event on the `SessionPool` This method should be used if the session usage was unsuccessful and you are sure that it is because of the session configuration and not any external matters. For example when server returns 403 status code. If the session does not work due to some external factors as server error such as 5XX you probably want to use `markBad` method.

  ***

  #### Returns void

### [**](#retireOnBlockedStatusCodes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L306)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L321)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L323)retireOnBlockedStatusCodes

* ****retireOnBlockedStatusCodes**(statusCode): boolean
* ****retireOnBlockedStatusCodes**(statusCode, additionalBlockedStatusCodes): boolean

- With certain status codes: `401`, `403` or `429` we can be certain that the target website is blocking us. This function helps to do this conveniently by retiring the session when such code is received. Optionally the default status codes can be extended in the second parameter.

  ***

  #### Parameters

  * ##### statusCode: number

    HTTP status code.

  #### Returns boolean

  Whether the session was retired.

### [**](#setCookie)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L392)setCookie

* ****setCookie**(rawCookie, url): void

- Sets a cookie within this session for the specific URL.

  ***

  #### Parameters

  * ##### rawCookie: string
  * ##### url: string

  #### Returns void

### [**](#setCookies)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L365)setCookies

* ****setCookies**(cookies, url): void

- Saves an array with cookie objects to be used with the session. The objects should be in the format that [Puppeteer uses](https://pptr.dev/#?product=Puppeteer\&version=v2.0.0\&show=api-pagecookiesurls), but you can also use this function to set cookies manually:

  ```
  [
    { name: 'cookie1', value: 'my-cookie' },
    { name: 'cookie2', value: 'your-cookie' }
  ]
  ```

  ***

  #### Parameters

  * ##### cookies: [Cookie](https://crawlee.dev/js/api/core/interface/Cookie.md)\[]
  * ##### url: string

  #### Returns void

### [**](#setCookiesFromResponse)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L341)setCookiesFromResponse

* ****setCookiesFromResponse**(response): void

- Saves cookies from an HTTP response to be used with the session. It expects an object with a `headers` property that's either an `Object` (typical Node.js responses) or a `Function` (Puppeteer Response).

  It then parses and saves the cookies from the `set-cookie` header, if available.

  ***

  #### Parameters

  * ##### response: [ResponseLike](https://crawlee.dev/js/api/core/interface/ResponseLike.md)

  #### Returns void
