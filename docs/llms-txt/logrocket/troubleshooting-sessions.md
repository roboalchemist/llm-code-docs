# Source: https://docs.logrocket.com/docs/troubleshooting-sessions.md

# Session Recording Issues

Common issues in session recordings

## Sessions are not appearing

#### Due to Content Security Policy

* After adding the script to your app, visit a page with LogRocket running and open your browser's developer tools. (make sure that you are connected to the internet, too)

* Check for any error messages mentioning LogRocket, like this:

<Image border={false} src="https://files.readme.io/3e4d2df-a0de484-Image_2017-02-15_at_10.26.11_AM.png" title="a0de484-Image_2017-02-15_at_10.26.11_AM.png" />

This can be fixed by adding the following to your site's content security policy:

```
Content-Security-Policy: child-src 'self' blob:; worker-src 'self' blob:; script-src 'self' https://cdn.logrocket.io https://cdn.lr-ingest.io https://cdn.lr-in.com https://cdn.lr-in-prod.com https://cdn.lr-ingest.com https://cdn.ingest-lr.com https://cdn.lr-intake.com https://cdn.intake-lr.com https://cdn.logr-ingest.com https://cdn.lrkt-in.com https://cdn.lgrckt-in.com https://cdn.logr-in.com; connect-src https://*.logrocket.io https://*.lr-ingest.io https://*.logrocket.com https://*.lr-in.com https://*.lr-in-prod.com https://*.lr-ingest.com https://*.ingest-lr.com https://*.lr-intake.com https://*.intake-lr.com https://*.logr-ingest.com https://*.lrkt-in.com https://*.lgrckt-in.com https://*.logr-in.com
```

Note that the [worker-src](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/worker-src) CSP directive wasn't supported in Safari or mobile Safari [before 15.5](https://developer.apple.com/documentation/safari-release-notes/safari-15_5-release-notes#Content-Security-Policy) and shouldn't be used in those older browsers. Using it anyway might prevent LogRocket from running and may prevent you from recording sessions in those browsers.

#### Due to blocked Javascript

The LogRocket recording script (SDK) might be blocked by a browser extension or network security policy. Open your browser's dev tools to check if the requests are failing. If they are, be sure to add an exception for the domain the SDK is loaded from.

#### Due to LogRocket.init() call being placed incorrectly

Ensure that `LogRocket.init()` is called before other code is loaded in your application:

```javascript
// DOES NOT WORK!
import LogRocket from 'logrocket';

LogRocket.init('foo/bar')
import './myOtherModule';
```

Instead, make sure to import a separate file which contains LogRocket:

```javascript
// in entry file
import './logrocketSetup';
import './myOtherModule';

// in logrocketSetup.js
import LogRocket from 'logrocket';
LogRocket.init('foo/bar');
```

#### Due to recording in an unsupported browser

If you are recording a session in an unsupported browser, the SDK will throw an exception which will be visible in the browser console. [See this page](https://docs.logrocket.com/docs/supported-browsers) for a list of supported browsers.

***

## Sessions ending prematurely

Like the above problem, this can be caused by a number of things:

#### Not putting LogRocket on every page

If your app is not a single-page application (SPA), the `LogRocket.init()` call must be put on every page. You can tell this is the cause if you have multiple sessions ending when a user navigates to the same page without init() called.

#### Sending too much data too quickly

Although extremely rare, this has been known to happen because of bugs which result in too many state changes that are queued to be sent to LogRocket. When this happens, LogRocket will stop recording to save on user bandwidth and print a warning to the console.

This can also happen if there are too many DOM changes. Browsers are pretty good at handling these, but LogRocket will shut down if too many happen within a reasonable period of time. Besides ruling out bugs in your app, also be sure you're not adding and mutating tags too often (also known as inlining). You can also verify that this is a problem by turning off DOM recording and seeing if sessions are recorded as normal.

#### HTML `<base>` element missing an `href` attribute

The HTML [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base) element specifies the base URL to use for all relative URLs in a document. If your HTML includes a `<base>` element with no `href` attribute, your sessions may not play correctly. To fix, add the missing `href` attribute and record new sessions.

***

## Sessions are broken up across subdomains

If you're seeing multiple sessions created as users traverse different subdomains on your site and you'd prefer to keep these contained to a single session, pass the `rootHostname` option when calling LogRocket.init().

***

## Styles are not appearing in recordings

LogRocket can sometimes take a few minutes to fetch the CSS from your website using our [asset caching bot](https://docs.logrocket.com/docs/asset-caching-bot). If you're still not seeing the styles after \~10 minutes, **then make sure the following are true**:

1. You are running on a publicly-available domain: [Testing on localhost/VPN](https://docs.logrocket.com/v1.0/docs/local-development).
2. You are **not** using `sourceMap` as an option in your Webpack `css-loader` config.
3. Your CDN keeps old versions of your assets publicly available. For example, if you have a CSS file named `main-[hash].css`, LogRocket's backend needs to be able to fetch this file to add it to the video. Alternatively, to make things simpler you could put the hash in the query part of the filename (e.g., `style.css?v=[hash]`). This should be easy to achieve using your CDN or storage provider and may already be enabled.
4. There are not `<style>selector { display: none }</style>` overridden by stylesheets later in `<head>`.  LogRocket moves all `<link>` tags to the top of the `<head>`.  Use `{ display: foo !important }` in the overriding style tag to fix this.
5. There are no `<style>` elements with more than 10,000 bytes of content.

***

## Network requests are missing or not being recorded

This is often caused by other libraries interfering with LogRocket's network capture functionality.

#### isomorphic-fetch

Some libraries like `isomorphic-fetch` will not work if you use the exported fetch:

```javascript
// DO NOT DO THIS:
import fetch from 'isomorphic-fetch';
fetch(...);
      
// DO THIS:
import 'isomorphic-fetch';
fetch(...);
```

#### whatwg-fetch

In addition, make sure that you're **not** setting `whatwg-fetch` to the window global before importing LogRocket:

```javascript
// DO NOT DO THIS
new webpack.ProvidePlugin({
  fetch: 'exports-loader?self.fetch!whatwg-fetch'
})
```

Instead, just import `whatwg-fetch` normally into your bundle:

```javascript
// DO THIS

import 'whatwg-fetch';
import LogRocket from 'logrocket';
```

`LogRocket` is a singleton, so you can load it from any place in your application after this point.

#### apollo-client

If network requests are not appearing when using apollo client, add this code to your application:

```javascript
import { ApolloClient } from 'apollo-client';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { createHttpLink } from 'apollo-link-http';

const fetcher = (...args) => {
  return window.fetch(...args);
};

const client = new ApolloClient({
  link: createHttpLink({ 
    uri: 'https://yourgraphql.api',
    fetch: fetcher,
  }),
  cache: new InMemoryCache()
});
```

#### Other network libraries

LogRocket should be imported and initialized before libraries that wrap fetch or XMLHttpRequest (e.g., [apollo-link](https://www.npmjs.com/package/apollo-link), [axios](https://github.com/axios/axios), [xhr](https://github.com/naugtur/xhr)). Libraries like these often save a reference to fetch or XHR internally. When LogRocket sets up network capture by instrumenting fetch and XHR during initialization, these libraries may not use the newly-instrumented version. As a result, requests made with these libraries may not be visible to LogRocket. Your app's requests should be consistently captured if you're able to call LogRocket.init() before any network library code is loaded.

***

## Network Responses are missing headers

By default browsers limit which response headers are available to be read in JavaScript. If headers are not captured by our SDK you may need to set an [`Access-Control-Expose-Headers` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers) on responses to enable reading those headers in JavaScript.

***

## Memory Usage data missing

Not all browsers support the [`Performance.memory`](https://developer.mozilla.org/en-US/docs/Web/API/Performance/memory#browser_compatibility) API. If you see Memory Usage data missing from a session, this is likely the reason. CPU Usage data should still be present.

***

## Capturing WebSocket errors

LogRocket doesn't record WebSockets by default. However, you can use WebSocket event listeners to send WebSocket data to LogRocket. For example, to capture WebSocket errors:

```javascript
webSocketObject.addEventListener('error', evt => LogRocket.log(evt.data));
```

## Fonts appear different on mobile or have ☒ in place of icons

Unexpected font rendering, or the presence of placeholder characters such as ☒, can sometimes occur if an app uses custom fonts. We recommend uploading your custom fonts ([iOS](https://docs.logrocket.com/reference/ios-capture-custom-fonts), [Android](https://docs.logrocket.com/reference/android-capture-custom-fonts)) to have the highest fidelity in session replay.