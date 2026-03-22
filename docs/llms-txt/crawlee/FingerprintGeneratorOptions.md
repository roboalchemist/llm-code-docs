# Source: https://crawlee.dev/js/api/browser-pool/interface/FingerprintGeneratorOptions.md

# FingerprintGeneratorOptions<!-- -->

### Hierarchy

* Partial\<FingerprintOptionsOriginal>
  * *FingerprintGeneratorOptions*

## Index[**](#Index)

### Properties

* [**browserListQuery](#browserListQuery)
* [**browsers](#browsers)
* [**devices](#devices)
* [**httpVersion](#httpVersion)
* [**locales](#locales)
* [**mockWebRTC](#mockWebRTC)
* [**operatingSystems](#operatingSystems)
* [**screen](#screen)
* [**slim](#slim)
* [**strict](#strict)

## Properties<!-- -->[**](#Properties)

### [**](#browserListQuery)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/header-generator/header-generator.d.ts#L66)externaloptionalinheritedbrowserListQuery

**browserListQuery?

<!-- -->

: string

Inherited from Partial.browserListQuery

Browser generation query based on the real world data. For more info see the [query docs](https://github.com/browserslist/browserslist#full-list). If `browserListQuery` is passed the `browsers` array is ignored.

### [**](#browsers)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/header-generator/header-generator.d.ts#L60)externaloptionalinheritedbrowsers

**browsers?

<!-- -->

: BrowsersType

Inherited from Partial.browsers

List of BrowserSpecifications to generate the headers for, or one of `chrome`, `edge`, `firefox` and `safari`.

### [**](#devices)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/header-generator/header-generator.d.ts#L74)externaloptionalinheriteddevices

**devices?

<!-- -->

: (desktop | mobile)\[]

Inherited from Partial.devices

List of devices to generate the headers for.

### [**](#httpVersion)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/header-generator/header-generator.d.ts#L85)externaloptionalinheritedhttpVersion

**httpVersion?

<!-- -->

: 1 | 2

Inherited from Partial.httpVersion

Http version to be used to generate headers (the headers differ depending on the version). Can be either 1 or 2. Default value is 2.

### [**](#locales)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/header-generator/header-generator.d.ts#L80)externaloptionalinheritedlocales

**locales?

<!-- -->

: string\[]

Inherited from Partial.locales

List of at most 10 languages to include in the [Accept-Language](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language) request header in the language format accepted by that header, for example `en`, `en-US` or `de`.

### [**](#mockWebRTC)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/fingerprint-generator/fingerprint-generator.d.ts#L99)externaloptionalinheritedmockWebRTC

**mockWebRTC?

<!-- -->

: boolean

Inherited from Partial.mockWebRTC

### [**](#operatingSystems)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/header-generator/header-generator.d.ts#L70)externaloptionalinheritedoperatingSystems

**operatingSystems?

<!-- -->

: (windows | macos | linux | android | ios)\[]

Inherited from Partial.operatingSystems

List of operating systems to generate the headers for.

### [**](#screen)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/fingerprint-generator/fingerprint-generator.d.ts#L93)externaloptionalinheritedscreen

**screen?

<!-- -->

: { maxHeight?

<!-- -->

: number; maxWidth?

<!-- -->

: number; minHeight?

<!-- -->

: number; minWidth?

<!-- -->

: number }

Inherited from Partial.screen

Defines the screen dimensions of the generated fingerprint.

**Note:** Using this option can lead to a substantial performance drop (\~0.0007s/fingerprint -> \~0.03s/fingerprint)

***

#### Type declaration

* ##### externaloptionalmaxHeight?<!-- -->: number
* ##### externaloptionalmaxWidth?<!-- -->: number
* ##### externaloptionalminHeight?<!-- -->: number
* ##### externaloptionalminWidth?<!-- -->: number

### [**](#slim)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/fingerprint-generator/fingerprint-generator.d.ts#L106)externaloptionalinheritedslim

**slim?

<!-- -->

: boolean

Inherited from Partial.slim

Enables the slim mode for the fingerprint injection. This disables some performance-heavy evasions, but might decrease benchmark scores.

Try enabling this if you are experiencing performance issues with the fingerprint injection.

### [**](#strict)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/header-generator/header-generator.d.ts#L91)externaloptionalinheritedstrict

**strict?

<!-- -->

: boolean

Inherited from Partial.strict

If true, the generator will throw an error if it cannot generate headers based on the input.

By default (strict: false), the generator will try to relax some requirements and generate headers based on the relaxed input.
