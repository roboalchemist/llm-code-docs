# Source: https://crawlee.dev/js/api/core/interface/SessionOptions.md

# SessionOptions<!-- -->

## Index[**](#Index)

### Properties

* [**cookieJar](#cookieJar)
* [**createdAt](#createdAt)
* [**errorScore](#errorScore)
* [**errorScoreDecrement](#errorScoreDecrement)
* [**expiresAt](#expiresAt)
* [**id](#id)
* [**log](#log)
* [**maxAgeSecs](#maxAgeSecs)
* [**maxErrorScore](#maxErrorScore)
* [**maxUsageCount](#maxUsageCount)
* [**sessionPool](#sessionPool)
* [**usageCount](#usageCount)
* [**userData](#userData)

## Properties<!-- -->[**](#Properties)

### [**](#cookieJar)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L91)optionalcookieJar

**cookieJar?

<!-- -->

: CookieJar

### [**](#createdAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L68)optionalcreatedAt

**createdAt?

<!-- -->

: Date

Date of creation.

### [**](#errorScore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L90)optionalerrorScore

**errorScore?

<!-- -->

: number

### [**](#errorScoreDecrement)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L65)optionalerrorScoreDecrement

**errorScoreDecrement?

<!-- -->

: number = 0.5

It is used for healing the session. For example: if your session is marked bad two times, but it is successful on the third attempt it's errorScore is decremented by this number.

### [**](#expiresAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L71)optionalexpiresAt

**expiresAt?

<!-- -->

: Date

Date of expiration.

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L39)optionalid

**id?

<!-- -->

: string

Id of session used for generating fingerprints. It is used as proxy session name.

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L89)optionallog

**log?

<!-- -->

: [Log](https://crawlee.dev/js/api/core/class/Log.md)

### [**](#maxAgeSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L45)optionalmaxAgeSecs

**maxAgeSecs?

<!-- -->

: number = 3000

Number of seconds after which the session is considered as expired.

### [**](#maxErrorScore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L57)optionalmaxErrorScore

**maxErrorScore?

<!-- -->

: number = 3

Maximum number of marking session as blocked usage. If the `errorScore` reaches the `maxErrorScore` session is marked as block and it is thrown away. It starts at 0. Calling the `markBad` function increases the `errorScore` by 1. Calling the `markGood` will decrease the `errorScore` by `errorScoreDecrement`

### [**](#maxUsageCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L84)optionalmaxUsageCount

**maxUsageCount?

<!-- -->

: number = 50

Session should be used only a limited amount of times. This number indicates how many times the session is going to be used, before it is thrown away.

### [**](#sessionPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L87)optionalsessionPool

**sessionPool?

<!-- -->

: [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md)

SessionPool instance. Session will emit the `sessionRetired` event on this instance.

### [**](#usageCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L77)optionalusageCount

**usageCount?

<!-- -->

: number = 0

Indicates how many times the session has been used.

### [**](#userData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L48)optionaluserData

**userData?

<!-- -->

: Dictionary

Object where custom user data can be stored. For example custom headers.
