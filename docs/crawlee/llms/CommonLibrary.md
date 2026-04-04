# Source: https://crawlee.dev/js/api/browser-pool/interface/CommonLibrary.md

# CommonLibrary<!-- -->

Each plugin expects an instance of the object with the `.launch()` property. For Puppeteer, it is the `puppeteer` module itself, whereas for Playwright it is one of the browser types, such as `puppeteer.chromium`. `BrowserPlugin` does not include the library. You can choose any version or fork of the library. It also keeps `browser-pool` installation small.

## Index[**](#Index)

### Properties

* [**name](#name)
* [**product](#product)

### Methods

* [**launch](#launch)

## Properties<!-- -->[**](#Properties)

### [**](#name)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L33)optionalname

**name?

<!-- -->

: () => string

#### Type declaration

* * **(): string

  - #### Returns string

### [**](#product)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L31)optionalproduct

**product?

<!-- -->

: string

## Methods<!-- -->[**](#Methods)

### [**](#launch)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L32)launch

* ****launch**(opts): Promise\<CommonBrowser>

- #### Parameters

  * ##### optionalopts: Dictionary

  #### Returns Promise\<CommonBrowser>
