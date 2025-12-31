# Source: https://lingui.dev/ref/locale-detector.md

# Locale Detection

The `@lingui/detect-locale` is a lightweight package *(only \~1 kB Gzip)* providing several methods and helpers to determine the user's locale using different detection strategies.

Most of the detectors accept custom document, location or window objects as parameters, which is especially useful for testing purposes or when implementing server-side detection strategies.

## Installation[​](#installation "Direct link to Installation")

* npm
* Yarn
* pnpm

```
npm install --save @lingui/detect-locale
```

```
yarn add @lingui/detect-locale
```

```
pnpm add @lingui/detect-locale
```

## Reference[​](#reference "Direct link to Reference")

### `detect`[​](#detect "Direct link to detect")

The `detect` method accepts multiple detectors as arguments and returns the first valid locale detected.

### `multipleDetect`[​](#multipledetect "Direct link to multipledetect")

The `multipleDetect` method also accepts multiple detectors as arguments and returns an array with all locales detected by each detector.

### `fromCookie(key: string)`[​](#fromCookie "Direct link to fromCookie")

Accepts a key as a parameter and retrieves the locale value from the browser's cookies based on that key.

### `fromHtmlTag(tag: string)`[​](#fromHtmlTag "Direct link to fromHtmlTag")

Looks for the specified attribute in the HTML document (commonly `lang` or `xml:lang`) to detect the locale.

### `fromNavigator()`[​](#fromNavigator "Direct link to fromNavigator")

Retrieves the user's language setting from the browser, compatible with older browsers such as IE11.

### `fromPath(localePathIndex: number)`[​](#fromPath "Direct link to fromPath")

Splits `location.pathname` into an array, requiring you to specify the index where the locale is located.

### `fromStorage(key: string, { useSessionStorage: boolean })`[​](#fromStorage "Direct link to fromStorage")

Searches for the item with the specified key in `localStorage` by default. If the `useSessionStorage` parameter is passed, it will search in `sessionStorage`.

### `fromSubdomain(localeSubdomainIndex: number)`[​](#fromSubdomain "Direct link to fromSubdomain")

Splits `location.href` by subdomain segments, requiring the index where the locale is specified.

### `fromUrl(parameter: string)`[​](#fromUrl "Direct link to fromUrl")

Uses a query string parser to find the locale by the specified parameter in the URL.

## Usage Examples[​](#usage-examples "Direct link to Usage Examples")

### Usage with `detect`[​](#usage-with-detect "Direct link to usage-with-detect")

```
import { detect, fromUrl, fromStorage, fromNavigator } from "@lingui/detect-locale";

// can be a function with custom logic or just a string, `detect` method will handle it
const DEFAULT_FALLBACK = () => "en";

const result = detect(fromUrl("lang"), fromStorage("lang"), fromNavigator(), DEFAULT_FALLBACK);

console.log(result); // "en"
```

### Usage with `multipleDetect`[​](#usage-with-multipledetect "Direct link to usage-with-multipledetect")

```
import { multipleDetect, fromUrl, fromStorage, fromNavigator } from "@lingui/detect-locale";

// can be a function with custom logic or just a string, `detect` method will handle it
const DEFAULT_FALLBACK = () => "en";

const result = multipleDetect(fromUrl("lang"), fromStorage("lang"), fromNavigator(), DEFAULT_FALLBACK);

console.log(result); // ["en", "es"]
```
