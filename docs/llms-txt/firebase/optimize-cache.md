# Source: https://firebase.google.com/docs/app-hosting/optimize-cache.md.txt

<br />

Cloud CDN is a critical part ofApp Hosting's support for your web app. Every request to your backend goes through Cloud CDN first. Content that is already cached in the CDN is served immediately back to the user, skipping a trip to the Cloud Run service running your web app's server code. You can learn more about the general benefits of CDNs at[web.dev](https://web.dev/articles/content-delivery-networks).

Though the basic Cloud CDN configuration is set byApp Hostingand cannot be modified, there are a number of things you can do to optimize your caching in order to increase page load speeds, reduce billed uncached content, and minimize traffic to Cloud Run.

## Cacheable content

Cloud CDN stores responses in cache if**ALL**of the following conditions are true:

1. The request is a GET

2. The response has a status code of`200`,`203`,`204`,`206`,`300`,`301`,`302`,`307`,`308`,`404`,`405`,`410`,`421`,`451`, or`501`.

3. The response has a`Cache-Control`header with a`max-age`or`s-maxage`directive, or an`Expires`header with a timestamp in the future.

4. The response has an`Age`header or a`Cache-Control`header with an explicit`public`directive.

5. The response is less than or equal to 10 MiB in size.

and**NONE**of the following are true:

1. The response has a`Set-Cookie`header

2. The response has a`Vary`header with a value other than`Accept`,`Accept-Encoding`,`Access-Control-Request-Headers`,`Access-Control-Request-Method`,`Origin`,`Sec-Fetch-Dest`,`Sec-Fetch-Mode`,`Sec-Fetch-Site`,`X-Goog-Allowed-Resources`,`X-Origin`,`RSC`,`Next-Router-State-Tree`,`Next-Router-Prefetch`, or`Next-Router-Segment-Prefetch`.

3. The response has a`Cache-Control`header with the`no-store`or`private`directive.

4. The request has a`Cache-Control`header with a`no-store`directive.

5. The request has an`Authorization`header, unless the response has an explicit cache control directive.

| **Note:** Next.js will automatically append headers that you read in your components to`Vary`; use`next/headers`with caution.
| **Note:** Routes affected by Next.js middleware are not cached.

## Customize behavior with cache control directives

### Next.js

Next.js sets cache-control directives implicitly[based on a number of factors](https://nextjs.org/docs/app/deep-dive/caching#apis). However, you can override these by manually[setting the header](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)in your`next.config.js`file. For example, to ensure a page is not cached in Cloud CDN:  

      /** @type {import('next').NextConfig} */
      const nextConfig = {
          headers: async () => [{
              source: "/YOUR_PRIVATE_PAGE",
              headers: [{
                  key: "Cache-Control",
                  value: "private"
              }],
          }],
      };

### Angular

Angular SSR does not set explicit cache-control directives out of the box. You can add your own by[specifying cache-control headers](https://angular.dev/guide/hybrid-rendering#setting-headers-and-status-codes)in your server routes. For example, to allow Cloud CDN to cache all pages for an hour:  

    import { RenderMode, ServerRoute } from '@angular/ssr';

    export const serverRoutes: ServerRoute[] = [
      {
        path: '**',
        renderMode: RenderMode.Prerender,
        headers: {
          'Cache-Control': 'public, max-age=3600',
        }
      }
    ];

Or to ensure a specific page will*not*be cached:  

    import { RenderMode, ServerRoute } from '@angular/ssr';

    export const serverRoutes: ServerRoute[] = [
      // ... other routes
      {
        path: 'YOUR_PRIVATE_PAGE',
        renderMode: RenderMode.Server,
        headers: {
          'Cache-Control': 'private',
        }
      }
    ];

### Respected directives

FirebaseApp Hosting's Cloud CDN instance respects the following cache control directives:

|            Directive             |                                                                                                                                                     Request                                                                                                                                                     |                                                                                                                                 Response                                                                                                                                  |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `no-store`                       | When present in a request, the response will not be cached.                                                                                                                                                                                                                                                     | A response with`no-store`isn't cached.                                                                                                                                                                                                                                    |
| `no-cache`                       | The`no-cache`request directive is ignored to prevent clients from potentially initiating or forcing revalidation to the origin.                                                                                                                                                                                 | A response with`no-cache`is cached but must be revalidated with the origin before being served.                                                                                                                                                                           |
| `public`                         | N/A                                                                                                                                                                                                                                                                                                             | This directive is not required for cacheability, but it is a best practice to include it for content that should be cached by proxies.                                                                                                                                    |
| `private`                        | N/A                                                                                                                                                                                                                                                                                                             | A response with the`private`directive isn't cached by Cloud CDN, even if the response is otherwise considered cacheable. Clients (such as browsers) might still cache the result. Use`no-store`to prevent all caching of responses.                                       |
| `max-age=SECONDS`                | The`max-age`request directive is ignored. A cached response is returned as if this header was not included in the request.                                                                                                                                                                                      | A response with the`max-age`directive is cached up to the defined SECONDS.                                                                                                                                                                                                |
| `s-maxage=SECONDS`               | N/A                                                                                                                                                                                                                                                                                                             | A response with the`s-maxage`directive is cached up to the defined SECONDS. If both`max-age`and`s-maxage`are present,`sâmaxage`is used by Cloud CDN. Responses with this directive aren't served stale.`s-max-age`(two hyphens) is not valid for the purposes of caching. |
| `max-stale=SECONDS`              | The`max-stale`request directive dictates the maximum*staleness* (in seconds) that the client is willing to accept. Cloud CDN honors this, and returns a stale cached response only if the staleness of the response is less than the`max-stale`directive. Otherwise, it revalidates before serving the request. | N/A                                                                                                                                                                                                                                                                       |
| `stale-while-revalidate=SECONDS` | N/A                                                                                                                                                                                                                                                                                                             | A response with`stale-while-revalidate`is served to a client for up to SECONDS while revalidation takes place asynchronously.                                                                                                                                             |
| `must-revalidate`                | N/A                                                                                                                                                                                                                                                                                                             | A response with`must-revalidate`is revalidated with the origin server after it expires. Responses with this directive aren't served stale.                                                                                                                                |
| `proxy-revalidate`               |                                                                                                                                                                                                                                                                                                                 | A response with`proxy-revalidate`is revalidated with the origin server after it expires. Responses with this directive aren't served stale.                                                                                                                               |
| `no-transform`                   | N/A                                                                                                                                                                                                                                                                                                             | No transforms are applied by Cloud CDN.                                                                                                                                                                                                                                   |

## Measure cached and uncached traffic

The "Cloud CDN - Outgoing Bandwidth" graph in the**Usage** tab of theApp Hostingconsole shows cached and uncached bytes served, and has a mark for each rollout. You can use this graph to measure the effectiveness of your cache optimization efforts.

You can also view the cache hit rate for specific routes in your web app with[Route-based Monitoring](https://firebase.google.com/docs/app-hosting/monitor-routes).