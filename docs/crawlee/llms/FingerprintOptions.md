# Source: https://crawlee.dev/js/api/browser-pool/interface/FingerprintOptions.md

# FingerprintOptions<!-- -->

Settings for the fingerprint generator and virtual session management system.

> To set the specific fingerprint generation options (operating system, device type, screen dimensions), use the `fingerprintGeneratorOptions` property.

## Index[**](#Index)

### Properties

* [**fingerprintCacheSize](#fingerprintCacheSize)
* [**fingerprintGeneratorOptions](#fingerprintGeneratorOptions)
* [**useFingerprintCache](#useFingerprintCache)

## Properties<!-- -->[**](#Properties)

### [**](#fingerprintCacheSize)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L58)optionalfingerprintCacheSize

**fingerprintCacheSize?

<!-- -->

: number = 10000

The maximum number of fingerprints that can be stored in the cache.

Only relevant if `useFingerprintCache` is set to `true`.

### [**](#fingerprintGeneratorOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L45)optionalfingerprintGeneratorOptions

**fingerprintGeneratorOptions?

<!-- -->

: [FingerprintGeneratorOptions](https://crawlee.dev/js/api/browser-pool/interface/FingerprintGeneratorOptions.md)

Customizes the fingerprint generation by setting e.g. the device type, operating system or screen size.

### [**](#useFingerprintCache)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L51)optionaluseFingerprintCache

**useFingerprintCache?

<!-- -->

: boolean = true

Enables the virtual session management system. This ties every Crawlee session with a specific browser fingerprint, so your scraping activity seems more natural to the target website.
