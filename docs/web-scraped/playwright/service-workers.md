# Source: https://playwright.dev/docs/service-workers

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Service Workers]

On this page

<div>

# Service Workers

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

Service workers are only supported on Chromium-based browsers.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

If you\'re looking to do general network mocking, routing, and interception, please see the [Network Guide](/docs/network) first. Playwright provides built-in APIs for this use case that don\'t require the information below. However, if you\'re interested in requests made by Service Workers themselves, please read below.

[Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) provide a browser-native method of handling requests made by a page with the native [Fetch API (`fetch`)](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) along with other network-requested assets (like scripts, css, and images).

They can act as a **network proxy** between the page and the external network to perform caching logic or can provide users with an offline experience if the Service Worker adds a [FetchEvent](https://developer.mozilla.org/en-US/docs/Web/API/FetchEvent#examples) listener.

Many sites that use Service Workers simply use them as a transparent optimization technique. While users might notice a faster experience, the app\'s implementation is unaware of their existence. Running the app with or without Service Workers enabled appears functionally equivalent.

## How to Disable Service Workers[​](#how-to-disable-service-workers "Direct link to How to Disable Service Workers") 

Playwright allows to disable Service Workers during testing. This makes tests more predictable and performant. However, if your actual page uses a Service Worker, the behavior might be different.

To disable service workers, set [testOptions.serviceWorkers](/docs/api/class-testoptions#test-options-service-workers) to `'block'`.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

## Accessing Service Workers and Waiting for Activation[​](#accessing-service-workers-and-waiting-for-activation "Direct link to Accessing Service Workers and Waiting for Activation") 

You can use [browserContext.serviceWorkers()](/docs/api/class-browsercontext#browser-context-service-workers) to list the Service [Worker](/docs/api/class-worker "Worker")s, or specifically watch for the Service [Worker](/docs/api/class-worker "Worker") if you anticipate a page will trigger its [registration](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register):

``` 
const serviceWorkerPromise = context.waitForEvent('serviceworker');
await page.goto('/example-with-a-service-worker.html');
const serviceworker = await serviceWorkerPromise;
```

[browserContext.on(\'serviceworker\')](/docs/api/class-browsercontext#browser-context-event-service-worker) event is fired ***before*** the Service Worker has taken control over the page, so ***before*** evaluating in the worker with [worker.evaluate()](/docs/api/class-worker#worker-evaluate) you should wait on its activation.

There are more idiomatic methods of waiting for a Service Worker to be activated, but the following is an implementation agnostic method:

``` 
await page.evaluate(async () => );
});
```

## Network Events and Routing[​](#network-events-and-routing "Direct link to Network Events and Routing") 

Any network request made by the **Service Worker** is reported through the [BrowserContext](/docs/api/class-browsercontext "BrowserContext") object:

-   [browserContext.on(\'request\')](/docs/api/class-browsercontext#browser-context-event-request), [browserContext.on(\'requestfinished\')](/docs/api/class-browsercontext#browser-context-event-request-finished), [browserContext.on(\'response\')](/docs/api/class-browsercontext#browser-context-event-response) and [browserContext.on(\'requestfailed\')](/docs/api/class-browsercontext#browser-context-event-request-failed) are fired
-   [browserContext.route()](/docs/api/class-browsercontext#browser-context-route) sees the request
-   [request.serviceWorker()](/docs/api/class-request#request-service-worker) will be set to the Service [Worker](/docs/api/class-worker "Worker") instance, and [request.frame()](/docs/api/class-request#request-frame) will **throw**

Additionally, for any network request made by the **Page**, method [response.fromServiceWorker()](/docs/api/class-response#response-from-service-worker) return `true` when the request was handled a Service Worker\'s fetch handler.

Consider a simple service worker that fetches every request made by the page:

transparent-service-worker.js

``` 
self.addEventListener('fetch', event => );

self.addEventListener('activate', event => );
```

If `index.html` registers this service worker, and then fetches `data.json`, the following Request/Response events would be emitted (along with the corresponding network lifecycle events):

Event

Owner

URL

Routed

[response.fromServiceWorker()](/docs/api/class-response#response-from-service-worker)

[browserContext.on(\'request\')](/docs/api/class-browsercontext#browser-context-event-request)

[Frame](/docs/api/class-frame "Frame")

index.html

Yes

[page.on(\'request\')](/docs/api/class-page#page-event-request)

[Frame](/docs/api/class-frame "Frame")

index.html

Yes

[browserContext.on(\'request\')](/docs/api/class-browsercontext#browser-context-event-request)

Service [Worker](/docs/api/class-worker "Worker")

transparent-service-worker.js

Yes

[browserContext.on(\'request\')](/docs/api/class-browsercontext#browser-context-event-request)

Service [Worker](/docs/api/class-worker "Worker")

data.json

Yes

[browserContext.on(\'request\')](/docs/api/class-browsercontext#browser-context-event-request)

[Frame](/docs/api/class-frame "Frame")

data.json

Yes

[page.on(\'request\')](/docs/api/class-page#page-event-request)

[Frame](/docs/api/class-frame "Frame")

data.json

Yes

Since the example Service Worker just acts a basic transparent \"proxy\":

-   There\'s 2 [browserContext.on(\'request\')](/docs/api/class-browsercontext#browser-context-event-request) events for `data.json`; one [Frame](/docs/api/class-frame "Frame")-owned, the other Service [Worker](/docs/api/class-worker "Worker")-owned.
-   Only the Service [Worker](/docs/api/class-worker "Worker")-owned request for the resource was routable via [browserContext.route()](/docs/api/class-browsercontext#browser-context-route); the [Frame](/docs/api/class-frame "Frame")-owned events for `data.json` are not routeable, as they would not have even had the possibility to hit the external network since the Service Worker has a fetch handler registered.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

It\'s important to note: calling [request.frame()](/docs/api/class-request#request-frame) or [response.frame()](/docs/api/class-response#response-frame) will **throw** an exception, if called on a [Request](/docs/api/class-request "Request")/[Response](/docs/api/class-response "Response") that has a non-null [request.serviceWorker()](/docs/api/class-request#request-service-worker).

## Routing Service Worker Requests Only[​](#routing-service-worker-requests-only "Direct link to Routing Service Worker Requests Only") 

``` 
await context.route('**', async route => );
  } else 
});
```

## Known Limitations[​](#known-limitations "Direct link to Known Limitations") 

Requests for updated Service Worker main script code currently cannot be routed ([https://github.com/microsoft/playwright/issues/14711](https://github.com/microsoft/playwright/issues/14711)).