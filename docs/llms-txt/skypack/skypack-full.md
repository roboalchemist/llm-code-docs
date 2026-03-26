# Skypack Documentation

Source: https://docs.skypack.dev/llms-full.txt

---

# Introduction

Skypack is a JavaScript Delivery Network for modern web apps

## What’s old is new again

Skypack is the world’s first CDN designed and optimized for modern JavaScript applications. To use it, just use a Skypack URL whenever you want to load a package:

```javascript
import React from 'https://cdn.skypack.dev/react';
```

Loading JavaScript from a third-party CDN isn't a groundbreaking concept. In the past, it was even recommended to load popular libraries like jQuery from a public CDN like Skypack to take advantage of shared caching across sites. As more and more sites join, cache hits become more likely, making all connected sites load faster as a result. Win win!

But JavaScript CDNs of the past don't integrate well with modern web development. Developers today expect clear dependency management and explicit dependency loading via `import` statements. Older CDNs required lots, and lots (and lots) of `<script>` tags that had to be loaded in a magically-correct (and sometimes hard to understand) order.

Now that all modern browsers support [ES Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) (`import` statements), we can load our favorite libraries from a CDN directly in our code, without the round-about `<script>` tags and confusing `window.React` references.&#x20;

With Skypack you can build a fast, modern web site or application without ever touching a single build tool  or line of bundler configuration.

## Skypack vs. Traditional CDNs

Skypack is designed to help you build a faster site with less effort. Skypack brings you best-in-class production performance features like:

* HTTP/2  & HTTP/3 Support
* Brotli Compression
* Global CDN Speeds
* Optimized Cache Headers

But that's not all. We've also designed Skypack to connect directly into production website and web applications. This brings some major benefits over your traditional public JavaScript CDN:

### A reliable URL for every package

Skypack doesn't force you to consult a README every time you load a package to figure out the correct file to reference. Every package, regardless of how it was written, is served from Skypack using a consistent URL API: `https://cdn.skypack.dev/PACKAGE_NAME`

Want the minified version? [Add a `?min` param for automatic minification.](https://docs.skypack.dev/skypack-cdn/api-reference/lookup-urls#minification)

### More packages supported, less code served

Traditional CDNs usually only serve single, static JavaScript files. This forces complex packages like React & React-DOM to manually bundle all of their code into a single file that the CDN can host, resulting in more code overall. Few packages do this extra work for you, resulting in a hit-or-miss story for users.

Any package that runs on the web can run on Skypack, with zero extra effort from the package authors. When a package does reference another module (e.g. the way `react-dom` references `react`) Skypack will automatically resolve that reference to a common, shared URL resulting in less code served as a result.

### Faster code for modern browsers

A huge problem facing JavaScript developers today is the over-transpilation and over-polyfilling of most applications, resulting in unnecessary code bloat and slower sites. Most JavaScript CDNs have to serve one file to all users, so modern browsers get stuck with the backwards-compatible bloat that they don't even need.

Skypack is the first CDN to automatically address this problem by skipping unnecessary compilation & polyfilling for modern browsers. When a user visits your site with a modern, up-to-date browser they'll get a smaller, faster JavaScript response optimized for their exact browser. &#x20;

### Production-ready guarantees

Skypack was specifically designed to connect with production websites, and we guarantee stability & security fit for production websites to serve millions of users. Few, (if any) public CDNs offer these same production guarantees.

* Custom domains & subdomains
* SLAs for guaranteed uptime
* [Pinned URLs](https://docs.skypack.dev/skypack-cdn/api-reference/pinned-urls-optimized) guarantee that your code won't change over time

## Get Started

This is a broad overview of Skypack: it’s a build-time optimization that serves your site faster by taking over serving all your npm dependencies. Head to the next section, [**Getting Started**](https://docs.skypack.dev/skypack-cdn/getting-started), to start kicking the tires.


# Getting Started

Start using Skypack today

If you haven’t familiarized yourself with the main concepts of the Skypack CDN, please visit the [Introduction](https://docs.skypack.dev/master) section.

If you’ve decided to use Skypack to boost your app’s speed, there are 2 main ways to start using it: either manually, using **code**. Or automatically, using **plugins**.

## Code

Because Skypack works with [ES Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), you can start using Skypack today with a simple change to your codebase:

```diff
-import React from "react";
+import React from "https://cdn.skypack.dev/react";
```

Basically, for any package you used to install locally via `npm`, you now load from Skypack. Simply prepend `https://cdn.skypack.dev/` before any npm-loaded package to start loading that package from anywhere. You can even try this today in [CodePen](https://codepen.io), or your favorite online editor.

### Demo

{% embed url="<https://codepen.io/dangodev/full/eYJKoXj>" %}

### Learn more

Use Skypack in the following languages:

* [JavaScript](https://docs.skypack.dev/skypack-cdn/code/javascript)
* [Node.js](https://docs.skypack.dev/skypack-cdn/code/node)
* [Deno](https://docs.skypack.dev/skypack-cdn/code/deno)

## Plugins (Coming soon)

Skypack’s plugins are currently under development, but when finished will allow easy drop-in support for:

* Next.js
* Create React App
* Gatsby&#x20;
* webpack
* Parcel
* Rollup
* Nuxt

To be notified of when these release, [please sign up for our mailing list](http://eepurl.com/g-czY9).


# Code

Use Skypack manually today

You can use Skypack’s next-generation JS CDN today using your language of choice:&#x20;

* [JavaScript / TypeScript](https://docs.skypack.dev/skypack-cdn/code/javascript)
* [Deno](https://docs.skypack.dev/skypack-cdn/code/deno)
* [Node.js](https://docs.skypack.dev/skypack-cdn/code/node)


# JavaScript / TypeScript

Use Skypack in any JS or TS app

## Hello, React!

Skypack will load code in any JavaScript environment, without any tooling or setup needed. To see it yourself, [open up the Skypack REPL](https://www.skypack.dev/npm/react) to run some JavaScript in your browser:

```javascript
// 👋 Welcome to Skypack! 

// Skypack is a Package Delivery Network (PDN) for everything on npm.
// Load any JavaScript package directly in the browser.

// Try loading the "react" package in the example below. 
// When you have something you like, copy the code onto your website!

import * as pkg from 'https://cdn.skypack.dev/react@^16.13.1';
console.log('react loaded:', pkg);
```

Open up your browser's dev console, and you should see `"react loaded: Module {...}"` (or something similar) printed to the console. Feel free to inspect the module object in your console log, if it's supported.

You can play around with this example as much as you like, replacing the `/react` in the URL with whatever package name you'd like.

## Getting Started

In this example, we'll start by using Preact and a helpful templating library called HTM. These two libraries were built to run directly in the browser, so they'll let us get pretty far without more complex tooling.

To run through these examples locally, you'll need a local dev server to serve files to the browser. We recommend [servor](https://github.com/lukejacksonn/servor) for it's light footprint and ability to run in any directory without an install step via `npx servor`.

### Step 1: A Single HTML File

```markup
<!-- Example 1: Preact in HTML (no build tooling required!) -->
<!-- View Code: https://glitch.com/edit/#!/familiar-warm-monday -->
<!DOCTYPE html>
<html>
  <body>
    <script type="module">
      import { h, Component, render } from 'https://cdn.skypack.dev/preact';
      import htm from 'https://cdn.skypack.dev/htm';
      const html = htm.bind(h);

      const app = html`<h1>Hello World!</h1>`;
      render(app, document.body);
    </script>
  </body>
</html>
```

### Step 2: Separating the JavaScript

A single HTML file may be all you need, but complex sites and applications will usually pull their JavaScript files out of HTML and into their own file tree:

{% tabs %}
{% tab title="index.html" %}

```markup
<!-- Example 2: Preact in JS (still... no build tooling required!) -->
<!DOCTYPE html>
<html>
  <body>
    <script type="module" src="/src/index.js"></script>
  </body>
</html>
```

{% endtab %}

{% tab title="src/index.js" %}

```javascript
import { h, Component, render } from 'https://cdn.skypack.dev/preact';
import htm from 'https://cdn.skypack.dev/htm';
const html = htm.bind(h);

const app = html`<h1>Hello World!</h1>`;
render(app, document.body);
```

{% endtab %}
{% endtabs %}

### Step 3: Adding More Files, Dependencies

From there, you can keep expanding your application. Start using new libraries and create more and more files in your application.

```
TODO: Example with multiple files, some preact component library.
```

### Step 4: Moving to Snowpack for TypeScript, Babel, Sass, etc.

At a certain point, you will probably run into limitations with your static dev server:

* No React support (JSX)
* No build tool support (Babel, Sass, etc.)
* No TypeScript support
* No production optimization support

For application development of any size, we recommend using Snowpack as your ESM-powered dev environment & build tool. It supports TypeScript, JSX, React, and more out of the box. You can learn more about it here: <https://www.snowpack.dev/>

## Using Skypack URLs in TypeScript

To use Skypack URLs directly, first create a `types/skypack.d.ts` file in the root of your project:

```typescript
// First, let TypeScript allow all module names starting with "https://". This will suppress TS errors.
declare module 'https://*';

// Second, list out all your dependencies. For every URL, you must map it to its local module.
declare module 'https://cdn.skypack.dev/preact' {
  export * from 'preact';
}

declare module 'https://cdn.skypack.dev/preact-router' {
  export * from 'preact-router';
}
```

{% hint style="info" %}
**Note**: you must have types installed locally for all your packages for this to work. Even though you’ll be using Skypack URLs in the end, TypeScript still needs to read these types from your local machine, so you’ll have to `npm install` them just like you would have before.
{% endhint %}

Lastly, add the `types/` folder to your `tsconfig.json` “includes” like so:

```diff
  {
    "compilerOptions": { … },
    "include": [
      "src",
+     "types"
    ],
    "exclude": ["node_modules"]
  }
```

Now you can use Skypack URLs directly in your projects, and have full TypeScript typings:

```diff
- import preact from 'preact';
+ import preact from 'https://cdn.skypack.dev/preact';
```

### Using Pinned URLs

You may want to just go ahead and use [Pinned URLs](https://docs.skypack.dev/skypack-cdn/api-reference/pinned-urls-optimized) directly in your app. You can do this by simply adding them to `types/skypack.d.ts` the same you would a basic lookup URL. In fact, you can have both in there side-by-side without any problem. Once you have them set up as aliases, TypeScript will treat them as such.


# Deno

## Hello, Deno!

Deno is a TypeScript runtime based heavily on ESM. It ships without a package manager, and instead relies on import URLs like Skypack for loading dependencies.&#x20;

Skypack is the best that you can import npm packages from in Deno.

```
deno
> const pkg = await import('https://cdn.skypack.dev/foo');
```

### A Note on Node.js Compatability

Skypack automatically converts legacy npm packages to modern ESM and polyfills some common Node.js built-in modules that they might depend on.

However, some modules (like the "fs" file system API) cannot be polyfilled and thus can't run on Deno (or anywhere outside of Node.js). Any packages on npm that rely on these dependencies won't run on Deno.

* fs
* crypto
* http
* https

### Automatic TypeScript Declarations

Skypack supports Deno's `X-TypeScript-Types` header to return TypeScript type declarations with loaded package. This gives you an extra level of safety with built-in Deno type warnings when your code breaks from the provided type declarations.

To enable TypeScript declarations, add the `?dts` query param to your lookup URL

```javascript
import React from 'https://cdn.skypack.dev/react?dts';
```


# Node.js

Node.js shipped native ESM support earlier this year. Unfortunately, this does not yet include support for importing files by URL. You can follow their progress on the [new loader API](https://nodejs.org/api/esm.html#esm_experimental_loaders) which would add this required URL loading support.

Until Node.js supports this, Skypack will stay focused on [web](https://docs.skypack.dev/skypack-cdn/code/javascript) & [Deno](https://docs.skypack.dev/skypack-cdn/code/deno) users.


# Migrate Existing Apps

## Webpack Plugin (Coming soon)

See [Plugins](https://docs.skypack.dev/skypack-cdn/code/broken-reference)

## deps.js

This is a pattern already popular within the Deno community. To manage multiple dependency URLs in one place, you can create a `deps.js` file somewhere in your application.

```javascript
// src/deps.js
export {default as React} from 'https://cdn.skypack.dev/react';
export {default as ReactDOM} from 'https://cdn.skypack.dev/react-dom';
```

Then, anywhere in your application you can do:

```javascript
// src/index.js
import {React, ReactDOM} from './deps.js';
```

## Import Maps (Experimental)


# Optimize for Production

## Pinned URLs

{% hint style="info" %}
**Pinned URLs are generated for you automatically by a successful lookup.** \
You should never need to write one yourself.&#x20;
{% endhint %}

```
https://cdn.pika.dev/pin/react@16.13.1-HASH/react.pin.js
```

While Lookup URLs are the easiest way to use Skypack, they aren't the fastest. When you're ready for production-optimized speed and safety, use **Pinned URLs.**

### Pinned URL vs. Lookup URL

Lookup URLs and Pinned URLs are both valid methods to load a package from Skypack. Lookup URLs are great for development, but Pinned URLs are faster and better suited for production use.

Lookup URLs are the recommended way to load a package during development:

* **Human Writeable -** You can write a Lookup URL yourself.
* **Version Resolution -** Lookup URLs resolve by version, SemVer, dist-tag, etc.
* **New Packages -** Lookup URLs will build new packages if none exists.

Pinned URLs, however, have several benefits over Lookup URLs:

* **Faster -** Runs on the edge, and responds in just a few milliseconds.
* **Pinned to a specific version -** Won't change over time (including sub-dependencies).

**If you can, replace all Lookup URLs with Pinned URLs in your codebase.** When new package versions are published to npm, Lookup URLs will automatically point to those new versions. Pinned URLs, by contrast, include a `HASH` in the URL that is always locked to a single version of your package ***and***  all package-dependencies. No matter what changes on npm, Pinned URL will always point to the exact same code.

### How to Get a Pinned URL

Pinned URLs are returned in the response of a successful Lookup URL. You should never need to write one yourself.

There are a few ways to get one:

* **Manual:** Via the package lookup tool on [www.skypack.dev\&#x20](http://www.skypack.dev\&#x20);
* **Manual:** Via the body of a successful Lookup URL.
* **Automatic:** Via tooling like Snowpack or a Skypack bundler plugin (see below).

## Content Security Policy (CSP)

When deploying your site with Skypack, be sure to inspect your site’s [Content Security Policy (CSP) headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP). You’ll want to make sure `script-src cdn.skypack.dev` is part of your site’s CSP.

## Build tools

Build tools for Skypack are coming soon! In the meantime, check out these community resources:

### Community tools

* **Rollup:** [rollup-plugin-skypack-resolver](https://www.npmjs.com/package/@vinicius73/rollup-plugin-skypack-resolver)


# API Reference

Skypack is a CDN at heart, but it can help to think of its interface as an API. Each request follows a specific format, and every response is valid JavaScript code. This lets you to load anything from our CDN via a JavaScript `import` statement.&#x20;

### Public URLs

There are two URLs designed for public use in your application:

* [Lookup URLs](https://docs.skypack.dev/skypack-cdn/api-reference/lookup-urls) are the easiest way to load code from Skypack. All you need is the name of the package you want to load, but you can also provide a package version, SemVer version range, and/or internal path of a file to load within the package.
* [Pinned URLs](https://docs.skypack.dev/skypack-cdn/api-reference/pinned-urls-optimized) (`/pin/*`) also load code from Skypack but optimized for performance and stability in production. Unlike Lookup URLs, they are always locked to an exact package build with an exact set of dependencies, so you can trust that the response won't change over time.

### Private URLs

Skypack supports a few other URLs internally. These should never be used directly in your application, but it can still help to familiarize yourself with how they work.

* `/-/*` [Resource URLs](https://docs.skypack.dev/skypack-cdn/private-urls#resource-urls)
* `/new/*` [New Build URLs](https://docs.skypack.dev/skypack-cdn/private-urls#new-new-package-urls)
* `/error/*` [Error URLs](https://docs.skypack.dev/skypack-cdn/private-urls#error-package-error-urls)


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


# Pinned URLs (Optimized)

{% hint style="info" %}
**Pinned URLs are generated for you automatically by a successful Lookup URL.** \
You should never need to write one yourself.
{% endhint %}

```
Pinned:            https://cdn.skypack.dev/pin/react@v16.13.1-zjOHmKoBShdi3wIQWY2z/react.js
Pinned + Minified: https://cdn.skypack.dev/pin/react@v16.13.1-zjOHmKoBShdi3wIQWY2z/min/react.js
```

**Pinned URLs are the recommended way to load packages in production.** Pinned URLs lock your response (and any dependencies) to a specific version to guarantee that the response will never change over time. Skipping the live lookup makes Pinned URLs a faster, more stable choice in production.

## Generate a Pinned URL

1. Visit a normal, lookup CDN response (Example: <http://cdn.skypack.dev/preact>)
2. In the response, find the "Pinned URL" section of the top comment. It should look something like this:

```
 *
 * Pinned URL: (Optimized for Production)
 *   Normal: https://cdn.skypack.dev/pin/preact@v10.5.5-zWGbvQRMya5StgDc7dPs/preact.js
 *   Minified: https://cdn.skypack.dev/pin/preact@v10.5.5-zWGbvQRMya5StgDc7dPs/min/preact.js
 *
```

There you have it! Use that URL anywhere in your application. It is guaranteed to be faster and safer, with zero changed dependencies over time.&#x20;

## Behavior

Pinned URLs include a `HASH` in the URL that is keyed to a specific build of the package. This hash accomplishes a few things:

1. **Fast:** Your response is generated on an edge worker in milliseconds (no database lookup required).&#x20;
2. **Stable:** Your response is locked to a specific version of the package so that your response never changes over time. This locks both your package and any of its dependencies. A pinned URL will return the same value this year as it does next year.
3. **Cache Friendly:** Since the response never changes, Pinned URLs can be cached locally in the browser forever so that a user only needs to request your resource once.&#x20;

### Performance

Pinned URLs were specifically designed to load code as fast as possible from anywhere in the world, on any device.

* **Run on the edge:** Pinned URLs are handled by Cloudflare Edge Workers, meaning they run as close to your users device as possible and respond in just a few milliseconds.
* **Optimized for each device:** Pinned URLs customize an optimized response for every browser, including only the necessary polyfills & transpilation needed to run.
* **Deep import resolution:** Pinned URLs include preload imports for every import needed by a package, protecting you from request waterfalls.


# Other (Internal Only)

{% hint style="danger" %}
**These URLs are internal only!**

Always use a Lookup URL or Pinned URL to access Skypack resources in your application. Internal URLs are reserved for internal use only and are never meant to be used directly in your application. This documentation exists solely as a reference for curious users.
{% endhint %}

## \`/-/\` - Resource URLs

{% hint style="info" %}
**Psst... Pinned URLs are faster than Resource URLs!**

You may be tempted to load a resource URL directly from your application and reduce the total number of requests. However, Pinned URLs are specifically optimized for applications and will result in a faster load time overall. [Learn more.](https://docs.skypack.dev/skypack-cdn/code/optimize-for-production)
{% endhint %}

```
https://cdn.skypack.dev/-/react@16.13.1-HASH/dist=es2020/react.js
```

Resource URLs power all of the JavaScript code served to your application. They are responsible for loading code from a package, transforming it to your specific browser, minifying the code (if requested) and resolving all imports to other package dependencies.

**Cached at the CDN edge:** Response code only needs to be transformed once and can then be reused & served statically out of the cache for all future requests.

**Cached in the browser:** Your browser will cache the response locally for up to a year, so that it only needs to be requested once by your users. Your user's browser knows to reuse the in-memory cached response for all future requests.

Remember: Resource URLs should never be loaded directly in your application. Not only will you miss out on important performance optimizations provided by Lookup & Pinned URLs, but some browsers will also fail to properly cache resource URLs when loaded directly in your site.

## \`/new/\` - New Package URLs

```
https://cdn.skypack.dev/new/preact@v1.2.3
```

Skypack will import from a `/new/` URL whenever a new package is requested. There are a few reasons that this can happen:

* This is the first time the package was loaded.
* This is the first time the specific package version was loaded.
* The package failed to build previously, but should be retried.

This URL can take a couple of seconds to resolve (or even several seconds for some large, complex packages). Behind the scenes, the server is installing the given npm package and optimizing it for the web.

When the build is complete, this URL will redirect to either an Error URL (if failed) or the newly created Resource URL (if succeeded). Browsers will automatically follow this redirect.

## \`/error/\` - Package Error URLs

```
https://cdn.skypack.dev/error/node:fs
```

If Skypack detects a problem with a package ahead-of-time, it will redirect its imports to an `/error/` URL. This allows Snowpack to report informative, more user-friendly errors back to the browser.


# Package Metadata

View metadata about a particular package.

## Package Meta

<mark style="color:blue;">`GET`</mark> `https://cdn.skypack.dev/:packageSpecifier?meta`

View metadata about any package. Replace `:packageSpecifier` with any package name and optionally a version, like so: `https://cdn.skypack.dev/preact?meta` or `https://cdn.skypack.dev/preact@10.5.7?meta`.

#### Path Parameters

| Name             | Type   | Description                                                     |
| ---------------- | ------ | --------------------------------------------------------------- |
| packageSpecifier | string | Specify `[package]@[version]`or simply `[package]` for “latest“ |

#### Query Parameters

| Name | Type    | Description                                                                            |
| ---- | ------- | -------------------------------------------------------------------------------------- |
| meta | boolean | This is required in order to display metadata (without, you’ll trigger the Lookup URL) |

{% tabs %}
{% tab title="200 Cake successfully retrieved." %}

```javascript
{
  "name": "preact",
  "version": "10.5.7",
  "buildId": "apbTSlqiCbFCw96Kpm6e",
  "buildStatus": "SUCCESS",
  "packageExports": {  
    ".": {
      "id": "./dist/preact.module.js",
      "optimized": true,
      "hasDefaultExport": false,
      "namedExports": [
        "__u",
        "cloneElement",
        "Component",
        "createContext",
        "createElement",
        "createRef",
        "Fragment",
        "h",
        "hydrate",
        "isValidElement",
        "options",
        "render",
        "toChildArray"
      ],
      "type": "JS"
    },
    "./compat": {
      "id": "./compat/dist/compat.module.js",
      "namedExports": [
        "__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED",
        "Children",
        "cloneElement",
        "Component",
        "createContext",
        "createElement",
        "createFactory",
        "createPortal",
        "createRef",
        "findDOMNode",
        "forwardRef",
        "Fragment",
        "hydrate",
        "isValidElement",
        "lazy",
        "memo",
        "PureComponent",
        "render",
        "StrictMode",
        "Suspense",
        "SuspenseList",
        "unmountComponentAtNode",
        "unstable_batchedUpdates",
        "useCallback",
        "useContext",
        "useDebugValue",
        "useEffect",
        "useErrorBoundary",
        "useImperativeHandle",
        "useLayoutEffect",
        "useMemo",
        "useReducer",
        "useRef",
        "useState",
        "version"
      ],
      "hasDefaultExport": true,
      "type": "JS",
      "optimized": true
    },
    "./debug": {
      "namedExports": [
        "resetPropWarnings"
      ],
      "type": "JS",
      "hasDefaultExport": false,
      "id": "./debug/dist/debug.module.js",
      "optimized": true
    },
    "./devtools": {
      "hasDefaultExport": false,
      "type": "JS",
      "id": "./devtools/dist/devtools.module.js",
      "namedExports": [],
      "optimized": true
    },
    "./hooks": {
      "id": "./hooks/dist/hooks.module.js",
      "optimized": true,
      "hasDefaultExport": false,
      "type": "JS",
      "namedExports": [
        "useCallback",
        "useContext",
        "useDebugValue",
        "useEffect",
        "useErrorBoundary",
        "useImperativeHandle",
        "useLayoutEffect",
        "useMemo",
        "useReducer",
        "useRef",
        "useState"
      ]
    },
    "./jsx-dev-runtime": {
      "optimized": true,
      "namedExports": [
        "Fragment",
        "jsx",
        "jsxDEV",
        "jsxs"
      ],
      "type": "JS",
      "id": "./jsx-runtime/dist/jsxRuntime.module.js",
      "hasDefaultExport": false
    },
    "./jsx-runtime": {
      "hasDefaultExport": false,
      "optimized": true,
      "id": "./jsx-runtime/dist/jsxRuntime.module.js",
      "namedExports": [
        "Fragment",
        "jsx",
        "jsxDEV",
        "jsxs"
      ],
      "type": "JS"
    },
    "./package.json": {
      "type": "ASSET",
      "id": "./package.json"
    },
    "./test-utils": {
      "hasDefaultExport": false,
      "type": "JS",
      "namedExports": [
        "act",
        "setupRerender",
        "teardown"
      ],
      "id": "./test-utils/dist/testUtils.module.js",
      "optimized": true
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Even though this API shares a base URL with the [Lookup API](https://docs.skypack.dev/skypack-cdn/api-reference/lookup-urls), not all functions of the Lookup API are supported (e.g. you can‘t specify `?meta&min`). For this reason, it‘s considered its own API.
{% endhint %}


# Skypack Pro

**Skypack Pro is currently in invite-only beta.** Pro features let you customize Skypack to your organization, including:

* Private Registry Support
* Private Asset Hosting
* Custom Subdomain Support
* Service Level Agreement (SLA)
* Audit Logs & Customer Support

[You can sign up to join the waitlist here.](http://eepurl.com/g-czY9)


# Security

An overview of different security pros & cons for using Skypack in production.

## Zero Package System Access

When you install your npm packages locally, most package managers will grant every package permission to run unknown, third-party scripts on your machine. With Skypack, this potential security vector is removed because packages are never installed directly on your machine. Instead, every package is installed and built inside of our very own sandboxed builder function.

## Lack of Subresource Integrity (SRI)

SRI is a security concept that exists for consumers of Skypack to implement. When you load JavaScript from a third-party source like npm or Skypack, you can check that the response matches a known hash (known as the integrity hash) to guarantee that the response has not been changed/interfered with.

&#x20;**Browsers don't yet support SRI for ESM imports.** This opens Skypack imports up to a man-in-the-middle attack if Skypack's origin were ever compromised. Because SRI is a browser feature, there is nothing that we can do to add this without browser support. Support is planned, but does not yet exist in any major browsers.

Non-browser applications like Deno and Snowpack are open and encouraged to implement SRI & integrity hash checks themselves by maintaining their own integrity hash as a part of installation.


# Skypack Discover

Skypack Discover is our take on package discovery. Discover offers human-curated, expert-recommended packages and reference links to learn more about any package.

>


# Package Quality Score

Skypack features a section on each package page called the Package Quality Score. This section features a list of checks on a package manifest that give insight into the quality of any given package. The goal of this is to **increase package quality and help package authors create a better JS ecosystem** (similar to [GitHub’s community checklist](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/about-community-profiles-for-public-repositories)).

**Didn't score a 100 on your package? That's okay!**\
Think of Package Quality like a [Lighthouse](https://developers.google.com/web/tools/lighthouse) score. Achieving 100 out of 100 points is meant to be difficult, and require perfect configuration and distribution. Skypack's Quality Score is a lot like that, where a 100 represents the "perfect" package where nothing could be improved as far as how the package is configured and distributed. We have a high bar to hit on purpose!&#x20;

Below you’ll find documentation on each individual check: what they mean and how to pass each check in your own package. **We recommend passing all checks!** Every check is significant and will improve package quality, package discovery, developer experience and the final deployment size for all of your users.

## Check your score before publishing

{% hint style="success" %}
[**@skypack/package-check**](https://github.com/skypackjs/package-check) **is now available as an npm package!**

* Check your package quality score locally before publishing to npm.&#x20;
* Integrate the CLI into your test suite to find and fix future regressions.
* Get it today → <https://github.com/skypackjs/package-check>
  {% endhint %}

## ESM

ESM stands for *ES Modules* a.k.a [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), which is the new standard for JavaScript modules. This check ensures that at least one of the following conditions are met:

* **Recommended:** Your `package.json` contains an ESM export, e.g.:`"exports": { "import": "./path/to/entry.js" }` or `"exports": { ".": { "import": "…" } }` ([docs](https://nodejs.org/api/packages.html#packages_approach_1_use_an_es_module_wrapper))
* Your `package.json` contains `"type": "module"` ([docs](https://nodejs.org/api/packages.html#packages_type))
* Your `package.json` contains a `"module": "./path/to/entry.js"` entry (not officially supported by Node.js, but [an organic community convention](https://github.com/rollup/rollup/wiki/pkg.module) we respect).
* *Supported, but not recommended:* Your `package.json` contains a `"main"` field that ends in `.mjs` ([this mimics Node behavior](https://nodejs.org/api/packages.html#packages_determining_module_system)). We’d recommend adding `"exports.import"` as well if this is your only indicator.

#### Why?

This field ensures that you’re shipping modern, standards-compliant JavaScript that works best for users. This ensures your package has more longevity and can be used in more environments, from browsers to Node to newer projects like [Deno](https://deno.land/). Even traditional web bundlers can benefit from ESM for more accurate tree-shaking and code analysis.

*Tip: by using the `"exports": …` approach, you can knock out the* [*Export Map check*](#has-export-map) *below as well!*

#### How to Fix

You can pass this check by meeting any one of the conditions above. Below is our recommended configuration for a package to support ESM using the "module" method for compatibility with older bundlers and an Export Map for compatibility with Node.js v12+ and future bundlers. ([docs](https://nodejs.org/api/packages.html#packages_approach_1_use_an_es_module_wrapper))

```javascript
// recommended: web-only package.json
{
  "module": "./esm/index.js",
  "exports": {
    ".": "./esm/index.js"
  }
}
```

```javascript
// recommended: web + node.js package.json
{
  "main": "./index-cjs.js",
  "module": "./index-esm.js",
  "exports": {
    "require": "./index-cjs.js",
    "import": "./index-esm.js"
  }
}
```

## Export Map

This check ensures that your package.json contains an `"exports"` top-level field ([docs](https://nodejs.org/api/packages.html#packages_subpath_exports)).

#### Why?

Export Maps help package authors accomplish two things: transition from Common.js (CJS)  to ESM & make a package's internal files private.

Historically, it has been impossible for some packages to reliably support multiple module systems (UMD, CJS, ESM) ***and*** multiple environments (Web, Node.js, Deno). Past efforts to standardize have relied solely on community buy-in, with little official support from Node.js or npm. Export Maps aim to solve this problem as the official Node.js standard to define package entrypoints per-environment.

```javascript
{
  "exports": {
    "require": "./index-cjs.js",
    "import": "./index-esm.js",
    "default": "./index-esm.js",
    // "node", "browser", "deno", etc. (env-specific entrypoints, as needed)
  }
}
```

Export maps also solve the problem of unexpected file access within a package. Packages can make up thousands of files, and it's not clear which files are meant to be imported directly or not. When you specify an export map, Node.js v12+ (and other tools) will prevent access to any files not listed in that export map. This makes your package file layout explicit, and locks down private, internal files that may move across non-breaking versions.

Take, for example, the [preact package](http://skypack.dev/view/preact) and how they use export maps:

```javascript
{
  "exports": {
    ".": {
      "import": "./dist/preact.mjs"
    },
    "./hooks": {
      "import": "./hooks/dist/hooks.mjs"
    }
    // ...
  }
}
```

This allows users to import from either `import preact from 'preact'` or `import { useState } from 'preact/hooks'` but not `from 'preact/super-secret-internal-file';`. This helps to protect users from accidental breaking changes, while allowing bundlers and CDNs like Skypack to better optimize package code around these explicit entrypoints.

#### How to Fix

Add something like one of the following to your `package.json`: ([docs](https://nodejs.org/api/packages.html#packages_approach_1_use_an_es_module_wrapper))

```javascript
{
  "exports": {
    ".": {
      "require": "./index-cjs.js",
      "import": "./index-esm.js",
    },
    // add more entrypoints here, only if needed
  }
}
```

## Keywords

This check ensures that your `package.json` contains a `"keywords"` top-level field ([docs](https://docs.npmjs.com/files/package.json#keywords)).

#### Why?

Popular npm search engines like npmjs.org, npms.io, yarnpkg.com, and more will only match your search term against the `name`, `description`, and `keywords`fields of each package. Adding a `keywords` field is a simple way to make sure that you are reaching as many users as possible, without relying on an exact match on the package name or description.

#### How to Fix

Add something like the following to your `package.json`: ([docs](https://docs.npmjs.com/files/package.json#keywords))

```javascript
{
  "keywords": [
    "ui",
    "svelte",
    "svelte-component"
  ]
}
```

## License

This check ensures that your `package.json` contains a `"license"` top-level field ([docs](https://docs.npmjs.com/files/package.json#license)).

#### Why?

Open-source software needs a license to use! Without a license, your package can’t be meaningfully used by companies or individuals. Even if you already have a license file included in your package files, many tools are unable to detect this automatically.

#### How to Fix

Add something like the following to your `package.json`: ([docs](https://docs.npmjs.com/files/package.json#license))

```javascript
{
  "license": "MIT"
}
```

## README

This check ensures you shipped a `README.md` file in the root directory along with your code ([docs](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/about-readmes)).

#### Why?

Open source packages need documentation! Help your users understand how to use your library by adding a README.

#### How to Fix

Simply add a `README.md` file in the root of your project. If you’re new to READMEs in general, [please see GitHub’s guide](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/about-readmes).

## Types

This check ensures that your `package.json` contains a `"types"` or `"typings"` top-level field, pointing to TypeScript types for your package ([docs](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html#including-declarations-in-your-npm-package)).

*Note: having an  `index.d.ts` in the root of your project isn’t enough; `types` must be present in `package.json`* [*as recommended in the TypeScript documentation*](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html#including-declarations-in-your-npm-package)*.*

#### Why?

In the State of JS 2019 survey, over half of all JavaScript developers said that they had worked with TypeScript. Even if you don’t use TypeScript yourself, authoring declaration files will make your package easier to use for a significant portion of your user-base.&#x20;

If you're looking for help to get started,  you can ask open source contributors to help!

#### How to Fix

Add something like the following to your `package.json`: ([docs](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html#including-declarations-in-your-npm-package))

```javascript
{
  "types": "./index.d.ts"
}
```

To generate your `.d.ts` types file(s), check out the following helpful resources:

* [Generate from TypeScript code](https://medium.com/cameron-nokes/the-30-second-guide-to-publishing-a-typescript-package-to-npm-89d93ff7bccd) (automatic)
* [Generate from JavaScript code](https://humanwhocodes.com/snippets/2020/10/create-typescript-declarations-from-javascript-jsdoc/) (automatic, with JSDoc)
* [Author manually](https://www.typescriptlang.org/docs/handbook/declaration-files/by-example.html)

## Repository

This check ensures that your `package.json` contains a `"repository"` top-level field ([docs](https://docs.npmjs.com/files/package.json#repository)).

#### Why?

A good open source package’s source code can be inspected to better examine its contents. It’s also important to see contributors’ additions to the codebase.

#### How to Fix

Add something like the following to your `package.json`: ([docs](https://docs.npmjs.com/files/package.json#repository))

```javascript
{
  "repository": {
    "type": "git",
    "url": "https://github.com/[username]/[project]"
  }
}
```


# Troubleshooting & FAQ

If you're having trouble with anything on Skypack, you can [file an issue](https://github.com/pikapkg/cdn) with us in the official GitHub repo.

Below are some common question & answers to help you troubleshoot Skypack CDN, the Skypack search catalog, and more.

### Q: How do I publish to skypack.dev?

Simply [publish to npm](https://docs.npmjs.com/cli/v7/commands/npm-publish) as you would normally! As soon as you publish, your package can be served from `https://cdn.skypack.dev/[my-package]` using the exact same name you published to npm (*note that in some cases it may take a while for* [*our metadata to update*](#q-why-is-my-package-missing-or-outdated-on-skypack-dev)*, but your package is still available instantly*).

### Q: I’m having trouble with Vue!

If you’re using `.vue` components, we’d recommend using [Snowpack + Vue](https://www.snowpack.dev/guides/vue/) to build your app. But if you‘re using the pure JS version of Vue, then you’ll want to use Vue’s CDN distribution ([docs](https://v3.vuejs.org/guide/installation.html#from-cdn-or-without-a-bundler)):

```javascript
import * as Vue from 'https://cdn.skypack.dev/vue@next/dist/vue.esm-browser.prod.js';

const App = {
  template: `
    <div>
     <h1>Hello Vue3</h1>
     <p>{{ message }}</p>
    </div>
  `,
  data() {
    return {
      message: 'Oh hi from the component',
    };
  },
};
Vue.createApp(App).mount('#app');
```

*Note: the code above is for Vue 3.x. For 2.x, use the following import instead:*

```javascript
import * as Vue from 'https://cdn.skypack.dev/vue/dist/vue.esm.browser.min.js';
```

### Q: Why is my package missing or outdated on skypack.dev?

The metadata for the skypack.dev search catalog works a little differently than cdn.skypack.dev. Whereas cdn.skypack.dev *actively* fetches updates, [www.skypack.dev](http://www.skypack.dev) *passively* receives updates from  [npm’s public registry API notifier](https://github.com/npm/registry). Sometimes this can lag behind a bit, but we always post updates as soon as npm notifies us of the update. Usually this happens within minutes, but in rare cases it can take up to an hour or more.

The same issue can happen with package updates. Sometimes you may publish a new version to npm,  package is present on skypack.dev, but it takes us longer than expected to receive an update for skypack.dev.

In both cases it’s important to know that **cdn.skypack.dev will always serve the most up-to-date versions.** This problem is limited only to the search catalog metadata, not the actual serving of your package.

If your package is missing from Skypack, [please open an issue](https://github.com/snowpackjs/skypack-cdn/issues)!

### Q: What registries does Skypack support?

At this time, Skypack only supports the npm registry. If you’d like to see us expand support to multiple registries, [please also open an issue](https://github.com/snowpackjs/skypack-cdn/issues).


