# Source: https://crawlee.dev/js/api/core/interface/Cookie.md

# Cookie<!-- -->

## Index[**](#Index)

### Properties

* [**domain](#domain)
* [**expires](#expires)
* [**httpOnly](#httpOnly)
* [**name](#name)
* [**path](#path)
* [**priority](#priority)
* [**sameParty](#sameParty)
* [**sameSite](#sameSite)
* [**secure](#secure)
* [**sourcePort](#sourcePort)
* [**sourceScheme](#sourceScheme)
* [**url](#url)
* [**value](#value)

## Properties<!-- -->[**](#Properties)

### [**](#domain)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L20)optionaldomain

**domain?

<!-- -->

: string

Cookie domain.

### [**](#expires)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L40)optionalexpires

**expires?

<!-- -->

: number

Cookie expiration date, session cookie if not set

### [**](#httpOnly)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L32)optionalhttpOnly

**httpOnly?

<!-- -->

: boolean

True if cookie is http-only.

### [**](#name)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L7)name

**name: string

Cookie name.

### [**](#path)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L24)optionalpath

**path?

<!-- -->

: string

Cookie path.

### [**](#priority)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L44)optionalpriority

**priority?

<!-- -->

: Low | Medium | High

Cookie Priority.

### [**](#sameParty)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L48)optionalsameParty

**sameParty?

<!-- -->

: boolean

True if cookie is SameParty.

### [**](#sameSite)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L36)optionalsameSite

**sameSite?

<!-- -->

: Strict | Lax | None

Cookie SameSite type.

### [**](#secure)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L28)optionalsecure

**secure?

<!-- -->

: boolean

True if cookie is secure.

### [**](#sourcePort)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L58)optionalsourcePort

**sourcePort?

<!-- -->

: number

Cookie source port. Valid values are `-1` or `1-65535`, `-1` indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future.

### [**](#sourceScheme)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L52)optionalsourceScheme

**sourceScheme?

<!-- -->

: Unset | NonSecure | Secure

Cookie source scheme type.

### [**](#url)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L16)optionalurl

**url?

<!-- -->

: string

The request-URI to associate with the setting of the cookie. This value can affect the default domain, path, source port, and source scheme values of the created cookie.

### [**](#value)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/browser.ts#L11)value

**value: string

Cookie value.
