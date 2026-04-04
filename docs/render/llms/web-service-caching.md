# Source: https://render.com/docs/web-service-caching.md

# Edge Caching for Web Services — Serve static content from a global edge cache for faster delivery.

Render provides *edge caching* for static assets (documents, images, etc.) served by paid [web services](web-services). With edge caching enabled, you can speed up response times and reduce load on your web service:

[image: Diagram illustrating an edge cache hit]

Edge caching is powered by the same global CDN as Render [static sites](static-sites).

## Setup

> *Edge caching is not available for [free web services](free).*

1. In the [Render Dashboard](https://dashboard.render.com), open your web service's *Settings* page and scroll down to the *Edge Caching* section:

   [image: Enabling edge caching in the Render Dashboard]

2. Under *Cacheable file types*, click the dropdown and select an option:

3. After you select an option, a confirmation dialog appears. Review and *Confirm* the notices, then click *Save changes*.

You're all set! Render begins caching your web service's [cache-eligible responses.](#cache-eligibility)

## How edge caching works

Whenever a client sends an HTTP request to your cache-enabled web service, Render determines whether the request is eligible to serve from the edge cache. (For details, see [Cache eligibility](#cache-eligibility).)

If the request is cache-eligible, Render checks the edge cache for the corresponding resource.

- *If the requested resource is in the cache* (and the entry isn't stale), Render serves the cached version:

  [image: Diagram illustrating an edge cache hit]

  In this case, the request never reaches your web service. This speeds up the response and reduces load.

- *Otherwise,* Render fetches the resource from your web service and—if it's _also_ cache-eligible—caches it for future requests:

  [image: Diagram illustrating an edge cache miss]

### Cache eligibility

When serving a request from your web service, Render uses the following logic to determine whether the response can be cached for future requests:

[diagram]

<sup>\* See details below.</sup></p>

To summarize, *all* of the following must be true for a response to be cache-eligible:

- The originating request *must* use the `GET` or `HEAD` HTTP method.
- The requested resource *must* have a [cacheable file type](#cacheable-file-types) based on your settings.
- The response *must either* include a `Cache-Control` header that allows caching *or* have a [default-cacheable status code](#default-cacheable-status-codes).
- Additionally, the response *must not* include a `Set-Cookie` header.

#### Cacheable file types

When you [enable edge caching](#setup) for your web service, you select one of the following options for *Cacheable file types*:

#### Default-cacheable status codes

If your web service returns a cache-eligible response _without_ a [`Cache-Control` header](#setting-cache-control-headers), Render caches the response if it has one of the following status codes (and applies the corresponding default TTL):

| Status code   | Default TTL |
| ------------- | ----------- |
| 200, 206, 301 | 120 minutes |
| 302, 303      | 20 minutes  |
| 404, 410      | 3 minutes   |

### Invalidation and expiration

To help ensure that clients receive up-to-date content, Render invalidates edge cache entries in the following scenarios:

| Scenario | Description |
| --- | --- |
| *New deploys* | Each time you successfully deploy a new version of your web service, Render purges _all_ of the service's edge cache entries. This way, the cache doesn't serve stale content from the service's previous version. Render waits until all of the previous version's instances have shut down before purging the cache (learn more about [zero-downtime deploys](/deploys#zero-downtime-deploys)). Failed deploys do _not_ trigger a purge. Purging the cache might briefly increase your web service's request volume, but only slightly. [See details.](#load-protection-on-cache-purge) |
| *TTL expiration* | Each cache entry has a corresponding time-to-live (TTL). When an entry's TTL expires, the entry is considered stale. The next request for a stale entry is sent to your web service, which refreshes the entry. |
| *Manual purge* | You can trigger a cache purge for your web service from its *Settings* page in the [Render Dashboard](https://dashboard.render.com):  [image: Triggering a cache purge in the Render Dashboard]  As with a new deploy, this purges _all_ of your web service's associated edge cache entries. Purging the cache might briefly increase your web service's request volume, but only slightly. [See details.](#load-protection-on-cache-purge) |

#### Load protection on cache purge

Whenever you purge your web service's edge cache (either manually or by triggering a new deploy), Render's CDN automatically protects your web service from receiving a sudden influx of requests.

If multiple clients request the same uncached resource, Render's CDN forwards only _one_ of those requests along to your web service. The CDN caches your web service's response, then serves it to all waiting clients. This pattern is called *request collapsing*.

Your web service might experience a brief traffic increase after a cache purge, but thanks to request collapsing, the size of that increase is roughly equal to the number of _unique resources_ being requested. This is usually a small fraction of your service's total request volume.

## Setting `Cache-Control` headers

You can customize Render's edge caching behavior for a particular resource by including a [`Cache-Control`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) (or `CDN-Cache-Control`) header in your web service's response:

```http
Cache-Control: public, max-age=7200
```

> *New to cache control headers?*
>
> Learn more about supported [response directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control#response_directives).

------

###### Customization

*Set a TTL (time-to-live)*

###### Description

Do *both* of the following in your response's `Cache-Control` header:

- Include the `public` directive.
- Set the `max-age` or `s-maxage` directive to a value greater than `0`.

```http
Cache-Control: public, max-age=3600
```

---

###### Customization

*Disable caching*

###### Description

Do *either* of the following in your response's `Cache-Control` header:

- Include the `no-store` directive to prevent storage in all caches.
- Include `private, max-age=0, no-transform` to prevent storage in the edge cache while allowing browser storage with revalidation.

```http
Cache-Control: private, max-age=0, no-transform
```

---

###### Customization

*Set revalidation behavior*

###### Description

Include a combination of the `must-revalidate`, `stale-while-revalidate`, and `stale-if-error` directives. ```http
Cache-Control: stale-while-revalidate=60, stale-if-error=3600, public, max-age=1200
```

------

### Precedence rules

Render applies the following precedence rules to cache control headers:

- The `CDN-Cache-Control` header takes precedence over the `Cache-Control` header if both are present.
- The `s-maxage` directive takes precedence over the `max-age` directive if both are present.

## Inspecting cache behavior

Each response from a cache-enabled web service includes a `CF-Cache-Status` header:

```http
CF-Cache-Status: HIT
```

The value of this header indicates whether the response interacted with the edge cache and in what way. The most common values are:

------

###### Value

`HIT`

###### Description

The response was served from the edge cache.

---

###### Value

`MISS`

###### Description

The response was not found in the edge cache. It was served from your web service and cached if eligible.

---

###### Value

`DYNAMIC`

###### Description

Some element of the incoming HTTP request was not [cache-eligible](#cache-eligibility), and the response was served from your web service. Most commonly indicates one of the following:

- The request used an HTTP method other than `GET` or `HEAD`.
- The requested resource did not have a [cacheable file type](#cacheable-file-types) based on your settings.

---

###### Value

`EXPIRED`

###### Description

The response was found in the edge cache, but its TTL had expired. It was served from your web service and the edge cache was updated with the new response.

---

###### Value

`BYPASS`

###### Description

The response was served directly from your web service and was _not_ stored in the edge cache, usually for one of the following reasons:

- The response included a `Cache-Control` header that disabled caching.
- The response did _not_ include a `Cache-Control` header, and it returned a status code that is not [default-cacheable](#default-cacheable-status-codes).
- The response included a `Set-Cookie` header.

------
