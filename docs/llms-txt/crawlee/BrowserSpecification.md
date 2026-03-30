# Source: https://crawlee.dev/js/api/browser-pool/interface/BrowserSpecification.md

# BrowserSpecification<!-- -->

## Index[**](#Index)

### Properties

* [**httpVersion](#httpVersion)
* [**maxVersion](#maxVersion)
* [**minVersion](#minVersion)
* [**name](#name)

## Properties<!-- -->[**](#Properties)

### [**](#httpVersion)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/fingerprinting/types.ts#L46)optionalhttpVersion

**httpVersion?

<!-- -->

: 1 | 2

HTTP version to be used for header generation (the headers differ depending on the version).

### [**](#maxVersion)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/fingerprinting/types.ts#L42)optionalmaxVersion

**maxVersion?

<!-- -->

: number

Maximum version of browser used.

### [**](#minVersion)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/fingerprinting/types.ts#L38)optionalminVersion

**minVersion?

<!-- -->

: number

Minimum version of browser used.

### [**](#name)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/fingerprinting/types.ts#L34)name

**name: [BrowserName](https://crawlee.dev/js/api/browser-pool/enum/BrowserName.md)

String representing the browser name.
