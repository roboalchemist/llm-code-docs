# Source: https://docs.skypack.dev/skypack-cdn/api-reference/private-urls.md

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
