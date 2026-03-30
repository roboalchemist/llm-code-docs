# Source: https://docs.skypack.dev/master.md

# Introduction

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
