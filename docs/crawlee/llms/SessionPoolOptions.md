# Source: https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md

# SessionPoolOptions<!-- -->

## Index[**](#Index)

### Properties

* [**blockedStatusCodes](#blockedStatusCodes)
* [**createSessionFunction](#createSessionFunction)
* [**maxPoolSize](#maxPoolSize)
* [**persistenceOptions](#persistenceOptions)
* [**persistStateKey](#persistStateKey)
* [**persistStateKeyValueStoreId](#persistStateKeyValueStoreId)
* [**sessionOptions](#sessionOptions)

## Properties<!-- -->[**](#Properties)

### [**](#blockedStatusCodes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L61)optionalblockedStatusCodes

**blockedStatusCodes?

<!-- -->

: number\[] = \[401, 403, 429]

Specifies which response status codes are considered as blocked. Session connected to such request will be marked as retired.

### [**](#createSessionFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L54)optionalcreateSessionFunction

**createSessionFunction?

<!-- -->

: [CreateSession](https://crawlee.dev/js/api/core/interface/CreateSession.md)

Custom function that should return `Session` instance. Any error thrown from this function will terminate the process. Function receives `SessionPool` instance as a parameter

### [**](#maxPoolSize)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L35)optionalmaxPoolSize

**maxPoolSize?

<!-- -->

: number = 1000

Maximum size of the pool. Indicates how many sessions are rotated.

### [**](#persistenceOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L69)optionalpersistenceOptions

**persistenceOptions?

<!-- -->

: [PersistenceOptions](https://crawlee.dev/js/api/core/interface/PersistenceOptions.md)

Control how and when to persist the state of the session pool.

### [**](#persistStateKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L47)optionalpersistStateKey

**persistStateKey?

<!-- -->

: string = SESSION\_POOL\_STATE

Session pool persists it's state under this key in Key value store.

### [**](#persistStateKeyValueStoreId)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L41)optionalpersistStateKeyValueStoreId

**persistStateKeyValueStoreId?

<!-- -->

: string

Name or Id of `KeyValueStore` where is the `SessionPool` state stored.

### [**](#sessionOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L38)optionalsessionOptions

**sessionOptions?

<!-- -->

: [SessionOptions](https://crawlee.dev/js/api/core/interface/SessionOptions.md)

The configuration options for [Session](https://crawlee.dev/js/api/core/class/Session.md) instances.
