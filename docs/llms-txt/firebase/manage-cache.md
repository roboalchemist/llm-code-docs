# Source: https://firebase.google.com/docs/hosting/manage-cache.md.txt

<br />

<br />

Firebase Hostinguses a powerful global CDN to make your site as fast as possible.

Any requested***static content*is automatically cached on the CDN** . If you redeploy your site's content,Firebase Hostingautomatically clears all your cached content across the CDN until the next request.

However, becauseCloud FunctionsandCloud Runservices generate content dynamically, the content for a given URL can vary based on such things as user input or the user's identity. To account for this, requests that are handled by backend code do*not*cache on the CDN by default.

You can, though,**configure caching behavior for dynamic content**. For example, if a function generates new content only periodically, you can speed up your app by caching the generated content for at least a short period of time.

You can similarly configure caching behavior to potentially reduce function execution costs because the content is served from the CDN rather than from a triggered function. Read more about optimizing function execution and services in the[Cloud Functions](https://firebase.google.com/docs/functions/tips)and[Cloud Run](https://cloud.google.com/run/docs/tips)documentation.

The exception is requests that return 404 errors. The CDN caches your service's 404 response to a nonexistent URL for 10 minutes, so that subsequent requests for that URL are served out of the CDN. If you change your service so that content now exists at this URL, the CDN continues serving any cached 404s for 10 minutes (at most), and then serves content from that URL normally.

If a 404 response already contains caching headers set by yourCloud FunctionsorCloud Runservice, they override the default of 10 minutes and fully determine the caching behavior of the CDN.

Learn more about caching behavior in Google's[web developer documentation](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching).

## Set Cache-Control

The main tool that you use to manage cache for dynamic content is the`Cache-Control`header. By configuring this header, you can communicate both to the browser and the CDN how long your content can be cached. In your function, you set`Cache-Control`like so:  

    res.set('Cache-Control', 'public, max-age=300, s-maxage=600');

In this example header, the directives do three things:

- `public`--- Marks the response as`public`. This means that both the browser*and* intermediate caches (including the CDN forFirebase Hosting) can cache the content.

  | **Note:** By default,Firebase Hostingsets`Cache-Control`to`private`for dynamic content. This means that if you don't explicitly set`Cache-Control`to`public`, only the browser of the requesting user is allowed to cache the content.
- `max-age`--- Sets how many seconds old a response can be before it should be revalidated with the origin server. This applies to browsers; if there is no`s-maxage`header, it also applies to all other caches (including the CDN).

- `s-maxage`--- Overrides the`max-age`directive for shared caches (such as the CDN). When the CDN finds a response older than`s-maxage`seconds, the CDN will revalidate it with the origin server. In the example header, browsers can cache the response for 5 minutes, but the CDN and any other intermediate caches can cache it for 10 minutes.

For`max-age`and`s-maxage`, set their values to the longest amount of time that you're comfortable with users receiving stale content. If a page changes every few seconds, use a small time value. However, other types of content can be safely cached for hours, days, or even months.

If you want to prevent caching entirely (for example, to always serve the freshest version of static content), you can configure this in`firebase.json`using the[`headers`](https://firebase.google.com/docs/hosting/full-config#headers)setting:  

    "hosting": {
      // ...

      // Disables caching for the /posts route
      "headers": [ {
        // Change source to match your dynamically-rendered routes
        "source": "/posts/**",
        "headers": [ {
          "key": "Cache-Control",
          "value": "no-cache, no-store"
        } ]
      } ]
    }

You can learn more about the`Cache-Control`header on the[Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control)and in Google's[web developer documentation](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching#cache-control).

## When is cached content served?

The browser and the CDN cache your content based on:

- The hostname
- The path
- The query string
- The content of the request headers specified in the[`Vary`header](https://firebase.google.com/docs/hosting/manage-cache#vary_headers)

### Vary headers

The[`Vary`header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Vary)determines which request headers should be used to provide an appropriate response (whether the cached content is valid or if the content should be revalidated with the origin server).

Firebase Hostingautomatically sets an appropriate`Vary`header on your response for common situations.**Most of the time, you don't need to worry about the`Vary`header.** However, in some advanced use cases, you might have other headers that you need to affect the cache. When that's the case, you can set the`Vary`header on your response. For example:  

    res.set('Vary', 'Accept-Encoding, X-My-Custom-Header');

In this case, the value of the`Vary`header is:  

    vary: X-My-Custom-Header, x-fh-requested-host, accept-encoding, cookie, authorization

With these settings, two otherwise identical requests with different`X-My-Custom-Header`headers are cached separately. Note thatHostingadds`Cookie`and`Authorization`to the`Vary`header by default when a request is made for dynamic content. This ensures that any session or cookie authorization header you use is made part of the cache key, which prevents accidental leaks of content.

Also note:

- Only`GET`and`HEAD`requests can be cached. HTTPS requests using other methods are never cached.

- Be careful when adding settings to the`Vary`header. The more settings that you add, the less likely it is that the CDN can serve cached content. Also remember that`Vary`is based on**request** headers, not**response**headers.

## Using cookies

When usingFirebase Hostingtogether withCloud FunctionsorCloud Run, cookies are generally stripped from incoming requests. This is necessary to allow for efficient CDN[cache behavior](https://firebase.google.com/docs/hosting/manage-cache#set_cache-control). Only the specially-named`__session`cookie is permitted to pass through to the execution of your app.

When present, the`__session`cookie is automatically made a part of the cache key, meaning that it's impossible for two users with different cookies to receive the other's cached response. Only use the`__session`cookie if your app serves different content depending on user authorization.