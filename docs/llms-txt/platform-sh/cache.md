# Source: https://docs.upsun.com/define-routes/cache.md

# HTTP cache


Upsun supports HTTP caching at the server level. Caching is enabled by default, but is only applied to ``GET`` and ``HEAD`` requests.

The cache can be controlled using the `cache` key in your `.upsun/config.yaml` file.

If a request can be cached, Upsun builds a cache key from several request properties and stores the response associated with this key.
When a request comes with the same cache key, the cached response is reused.

When caching is on...

* you can configure cache behavior for different location blocks in your `.upsun/config.yaml`;
* the router respects whatever cache headers are sent by the application;
* cookies bypass the cache;
* responses with the `Cache-Control` header set to `Private`, `No-Cache`, or `No-Store` aren't cached.

You should _not_ use the Upsun HTTP cache if you're using [Varnish](https://docs.upsun.com../add-services/varnish.md) or an external CDN
such as [Fastly](https://docs.upsun.com../domains/cdn/fastly.md) or [Cloudflare](https://docs.upsun.com../domains/cdn/cloudflare.md).
Mixing cache services together most likely results in caches that are stale and can't be cleared.
For more details, see [best practices on HTTP caching](https://docs.upsun.com/learn/bestpractices/http-caching.md).

## Basic usage

The HTTP cache is enabled by default, however you may wish to override this behavior.

To configure the HTTP cache, add a `cache` key to your route. You may like to start with the defaults:

```yaml  {location=".upsun/config.yaml"}
routes:
  https://{default}/:
    type: upstream
    upstream: myapp:http
    cache:
      enabled: true
      default_ttl: 0
      cookies: ['*']
      headers: ['Accept', 'Accept-Language']
```

## Example

In this example, requests are cached based on the URI, the `Accept` header, `Accept-Language` header, and `X-Language-Locale` header.
Any response that lacks a `Cache-Control` header is cached for 60 seconds.
The presence of any cookie in the request disables caching of that response.

```yaml  {location=".upsun/config.yaml"}
routes:
  https://{default}/:
    type: upstream
    upstream: myapp:http
    cache:
      enabled: true
      headers: ['Accept', 'Accept-Language', 'X-Language-Locale']
      cookies: ['*']
      default_ttl: 60
```

## How it works

### The cache key

If a request can be cached, Upsun builds a cache key from several request properties and stores the response associated with this key. When a request comes with the same cache key, the cached response is reused.

There are two parameters that let you control this key: `headers` and `cookies`.

The default value for these keys are the following:

```yaml  {location=".upsun/config.yaml"}
routes:
  https://{default}/:
    # ...
    cache:
      enabled: true
      cookies: ['*']
      headers: ['Accept', 'Accept-Language']
```

### Duration

The cache duration is decided based on the `Cache-Control` response header value. If no `Cache-Control` header is in the response, then the value of `default_ttl` key is used.

### Conditional requests

Conditional requests using `If-Modified-Since` and `If-None-Match` are both supported. The web server doesn't honor the `Pragma` request header.

### Cache revalidation

When the cache is expired (indicated by `Last-Modified` header in the response) the web server sends a request to your application with `If-Modified-Since` header.

If the `If-None-Match` header is sent in the conditional request when `Etag` header is set in the cached response, your application can extend the validity of the cache by replying `HTTP 304 Not Modified`.

### Flushing

The HTTP cache doesn't support a complete cache flush, but you can invalidate the cache by setting `cache: false`. Alternatively, the cache clears on a rebuild, so triggering a rebuild (pushing a new commit) effectively causes a complete cache flush.

## Cache configuration properties

### `enabled`

Turns the cache on or off for a route.

**Note**: 

Regular expressions in routes are **not** supported.

### Allowing only specific cookies

Some applications use cookies to invalidate cache responses, but expect other cookies to be ignored.
This is a case of allowing only a subset of cookies to invalidate the cache.

```yaml  {location=".upsun/config.yaml"}
routes:
  https://{default}/:
    # ...
    cache:
      enabled: true
      cookies: ["MYCOOKIE"]
```

### Cache HTTP and HTTPS separately using the `Vary` header

Set the Vary header to `X-Forwarded-Proto` [custom request header](https://docs.upsun.com/development/headers.md) to render content based on the request protocol (i.e. HTTP or HTTPS). By adding `Vary: X-Forwarded-Proto` to the response header, HTTP and HTTPS content would be cached separately.

### Cache zipped content separately

Use `Vary: Accept-Encoding` to serve different content depending on the encoding. Useful for ensuring that gzipped content isn't served to clients that can't read it.

