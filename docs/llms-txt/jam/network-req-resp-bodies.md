# Source: https://jam.dev/docs/debug-a-jam/devtools/network-req-resp-bodies.md

# Network req/resp bodies

Jam captures request and response bodies for all XHR and fetch requests, but there are a couple of exceptions where you will find XHR/fetch requests for which Jam was not able to capture the request/response body content:

* **Timing:** If the request happened before Jam was initialized on the page. This happens depending on when scripts are loaded in your application vs when Jam's scripts are loaded by your browser.
* **CORS issue:** If the browser performed a preflighted OPTIONS check for this request, which did not pass, then we have a request body that was never sent.
* **Static assets:** images, scripts, and other non-programmatic assets (i.e., not XHR/fetch/websockets) are not captured by Jam.
