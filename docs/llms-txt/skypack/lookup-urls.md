# Source: https://docs.skypack.dev/skypack-cdn/api-reference/lookup-urls.md

# Lookup URLs

```javascript
import React from "https://cdn.skypack.dev/react";
```

Lookup URLs are the easiest way to load JavaScript packages in your application. All you need is a package name to get started.

## Behavior

Lookup URLs perform a live lookup on the npm registry, and will always return the latest package available data from npm. You can provide a version range in the URL to customize or restrict this version lookup behavior.

When you find a package that you are happy with, we recommend committing Pinned URL to your codebase so they can skip the slower lookup and prevent unexpected changes over time as new packages are released to npm.

## API - Package Matching

### Lookup by Package Name

{% tabs %}
{% tab title="Example URL" %}

```
https://cdn.skypack.dev/react
```

{% endtab %}

{% tab title="Static Import" %}

```javascript
import React, {useState} from 'https://cdn.skypack.dev/react';
```

{% endtab %}

{% tab title="Dynamic Import" %}

```javascript
// Run this directly in the browser!
const pkg = await import('https://cdn.skypack.dev/react');
console.log('React Loaded:', pkg);
```

{% endtab %}
{% endtabs %}

If only a package name is given, Skypack will check npm and return the latest version of the package. This is the equivalent of running `npm install [package-name]` or `yarn add [package-name]`  without a version in a Node.js project.

### Lookup by Package + Version Range (Semver)

```
https://cdn.skypack.dev/react@16.13.1   // Matches react v16.13.1 
https://cdn.skypack.dev/react@~16.13.0  // Matches the latest react v16.13.x
https://cdn.skypack.dev/react@^16.13.0  // Matches the latest react v16.x 
```

Returns the latest package release that matches that version. Basic SemVer matchers (`~` & `^`) are supported to automatically accept future releases to the package within a range.&#x20;

### **Lookup by Package + Dist Tag**

```
https://cdn.skypack.dev/react@latest  // Equivilent to "cdn.skypack.dev/react"
https://cdn.skypack.dev/react@next
```

Returns the package release that matches that "dist-tag" in npm. [Learn more about dist-tags.](https://docs.npmjs.com/adding-dist-tags-to-packages)

## API - Resource Matching

By default, Lookup URLs return the main entrypoint of a package, just like if you had imported the package by name alone in Node.js.

However, some packages are designed to import custom files and entrypoints deep within a package. Skypack supports most uses of this as well.

### Lookup a Package Export

```
https://cdn.skypack.dev/preact@latest/hooks
```

[Export Maps](https://nodejs.org/api/esm.html#esm_package_entry_points) are the latest standard from the Node.js team for documenting the specific interface of a package. Any files not documented in the export map are meant to be private, and inaccessible from Node.js and other tools.

Skypack ships with support for Export Maps and will use them to optimize a package if one exists.

### Lookup a Package File

```
https://cdn.skypack.dev/lodash-es@latest/snakeCase.js
https://cdn.skypack.dev/bulma@latest/css/bulma.css
```

If no export map exists, it is still possible to lookup any file within Skypack.

**Limitation:** When a JavaScript file is loaded this way, Skypack won't run automatic Common.js (CJS) -> ESM transformation on the file. Legacy packages are only able to be handled when a package is imported by name (aka the main entrypoint) or when an Export Map exists for that package.

## API - Customizing the Response

### Minification

```
https://cdn.skypack.dev/preact?min
https://cdn.skypack.dev/preact@^10.0.0?min
https://cdn.skypack.dev/preact@^10.0.0/hooks?min
```

By default, Lookup URLs will return code unminified. You can add the `minify` URL param to reduce the number of bytes sent over the wire. &#x20;

### Forced Browser Support

```
https://cdn.skypack.dev/preact@^10.0.0?dist=es2017
https://cdn.skypack.dev/preact@^10.0.0?dist=es2018
https://cdn.skypack.dev/preact@^10.0.0?dist=es2019
https://cdn.skypack.dev/preact@^10.0.0?dist=es2020
```

By default, Lookup URLs will return code optimized to the specific browser that loads it. Modern browsers will get less unnecessary transpilation and polyfills than legacy browsers, and load faster as a result.

You can disable this automatic browser detection by hardcoding your own `?dist` param into the URL.

### TypeScript Declarations

```
https://cdn.skypack.dev/preact?dts
https://cdn.skypack.dev/preact@^10.0.0?dts
https://cdn.skypack.dev/preact@^10.0.0/hooks?dts
```

If you're using Skypack with Deno or any other Typescript-first environment, you can add the `?dts` query param to the URL to return `X-TypeScrpt-Declarations` that Deno will read automatically.

## Package Metadata

See [Package Metadata API](https://docs.skypack.dev/skypack-cdn/api-reference/package-metadata).
