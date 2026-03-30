# Source: https://docs.skypack.dev/skypack-cdn/api-reference/pinned-urls-optimized.md

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
