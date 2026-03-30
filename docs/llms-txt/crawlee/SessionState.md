# Source: https://crawlee.dev/js/api/core/interface/SessionState.md

# SessionState<!-- -->

Persistable [Session](https://crawlee.dev/js/api/core/class/Session.md) state.

## Index[**](#Index)

### Properties

* [**cookieJar](#cookieJar)
* [**createdAt](#createdAt)
* [**errorScore](#errorScore)
* [**errorScoreDecrement](#errorScoreDecrement)
* [**expiresAt](#expiresAt)
* [**id](#id)
* [**maxErrorScore](#maxErrorScore)
* [**maxUsageCount](#maxUsageCount)
* [**usageCount](#usageCount)
* [**userData](#userData)

## Properties<!-- -->[**](#Properties)

### [**](#cookieJar)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L26)cookieJar

**cookieJar: SerializedCookieJar

### [**](#createdAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L34)createdAt

**createdAt: string

### [**](#errorScore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L28)errorScore

**errorScore: number

### [**](#errorScoreDecrement)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L30)errorScoreDecrement

**errorScoreDecrement: number

### [**](#expiresAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L33)expiresAt

**expiresAt: string

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L25)id

**id: string

### [**](#maxErrorScore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L29)maxErrorScore

**maxErrorScore: number

### [**](#maxUsageCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L32)maxUsageCount

**maxUsageCount: number

### [**](#usageCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L31)usageCount

**usageCount: number

### [**](#userData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L27)userData

**userData: object
