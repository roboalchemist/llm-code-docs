# Source: https://docs.wiremock.io/default-responses.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Serving a Default Response

> Configuring a stub to serve a default response when a specific match for the request is not is found

By default, WireMock Cloud will serve a generic 404 page if an incoming HTTP request is not matched to any stub mapping.
Often this is not a problem, but in some instances it is desirable to serve your own response.

This can be achieved using the Priority parameter when creating stubs. By creating a stub which has loose (non-specific)
matching criteria and a low priority setting, requests will "fall through" to this if they're not matched to a more specific stub.

## Example

Suppose you want to serve a `403 Unauthorized` response with a meaningful response body when a request is not matched rather than the default 404. Additionally you
want to serve 200 response when a `GET` request is made to `/examples/12`.

Start by creating a stub with `ANY` as the method. Open the Advanced section and change the URL match type to `Any URL`.
Also in the Advanced section set the Priority to 10 (the lowest).

<img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-request.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=a5dbe93be479d6b60b104b421377e272" title="Default request" data-og-width="1892" width="1892" data-og-height="822" height="822" data-path="images/screenshots/default-response-example-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-request.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=0773e347180686aba2a49db488d9d351 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-request.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=48d865dfd42474e30c1aaf173e9d3d1c 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-request.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=beb96edcf56f7addd46b05bfcbd58370 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-request.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=8b4ed6891583b209b08c84d7c7e00930 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-request.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=fa0feea477b3a455a48f14a0ac07c044 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-request.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=59cc9747bf615421279d3311158e4f4c 2500w" />

In the Response section, set the Status to `403` and the body content to `"Sorry, you can't do that"`.

<img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-response.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=a15b2112e16db9eadc0fd9d829bb3f1f" title="Default response" data-og-width="1884" width="1884" data-og-height="982" height="982" data-path="images/screenshots/default-response-example-response.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-response.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=2a79c0c8b0b51efa62ade59eae5c6bad 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-response.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=92e6195cfa1e1bf735876a68f58865a5 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-response.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=a543894e39a91ec1dbd9ceb9ed37d47f 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-response.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=1c49c65c09ab0fade57511c1b08f7b3c 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-response.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=c640a027f23ed586e0ed1a89e6cef456 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-response-example-response.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=3674d5dd50806f6c356c2e426aaec429 2500w" />

Create a second stub with the method set to `GET`, the URL to `/examples/12` and the response body to `"Example 12 body"` (keeping the Status as `200`).

Now if you make a request that matches the specific stub you will see a response with a `200` status and the success message:

```
$ curl -v http://example.wiremockapi.cloud/examples/12

> GET /examples/12 HTTP/1.1
> Host: example.wiremockapi.cloud
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Transfer-Encoding: chunked
<
Example 12 body
```

Whereas if you make a request to a URL with no stub to match you will see the default `403` response.

```
$ curl -v http://example.wiremockapi.cloud/examples/12222222

> GET /examples/12222222 HTTP/1.1
> Host: example.wiremockapi.cloud
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< Transfer-Encoding: chunked
<
Sorry, you can't do that
```
