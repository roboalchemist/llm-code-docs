# Source: https://docs.skypack.dev/skypack-cdn/api-reference.md

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
