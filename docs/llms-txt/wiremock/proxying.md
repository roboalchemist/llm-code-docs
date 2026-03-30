# Source: https://docs.wiremock.io/proxying.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Proxying

> Proxying requests to other systems

When working with an existing API it can be useful to pass some requests through to it for testing, while
serving stubbed responses for others.

For instance, if an API is not yet fully implemented then testing progress can still be made
for the calling application by stubbing the parts not yet completed.

Additionally, proxying all but a selection of requests enables testing of edge and failure cases that would be hard to
replicate predictably in the target API.

## Usage

Proxying is configured per-stub. When a stub is configured to serve a proxy response, all of the normal request matching rules
apply, but instead of returning a canned response, the request is forwarded to the target.

Proxying is enabled by selecting the Proxy tab in the stub's Response section and completing (at a minimum) the base URL field.

Additional request headers can optionally be specified. These will be added to the proxy request if not already present,
or will override the existing value if present.

<img src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/plain-proxy-response.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=102f83e8059669d909b44bab4bb5a775" title="Proxy response" data-og-width="799" width="799" data-og-height="254" height="254" data-path="images/screenshots/plain-proxy-response.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/plain-proxy-response.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=6511418f76725fa8b230e2dc08fdb0f2 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/plain-proxy-response.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=db8cf1ab75189f245535ca142c8ca9f9 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/plain-proxy-response.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=988ce5ec0eef7f2c2181638680cebc7f 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/plain-proxy-response.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=31802ee5e3c0d5d804a225643236f417 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/plain-proxy-response.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=baf7ad9d41f1c2924dddf376171ec488 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/plain-proxy-response.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=cfbfd2668d0e83e275d4be8aa8efe5d7 2500w" />

The relative part of a request's URL will be appended onto the base URL, so given a proxy base URL of `http://my-site.com/base`, a
request made to `http://my-mock-api.wiremockapi.cloud/things/1` would result in a proxy request to `http://my-site.com/base/things/1`.

## Templating the base URL

When the Enable templating check box is ticked, the base URL can be a handlebars template, meaning that properties from the
incoming request can be used to determine the URL. See [Response Templating](/response-templating/basics/) for details of the
model and syntax used.

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/templated-proxy-response.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=0acd8f60bc9c559f94f63ec5948e6eb6" title="Proxy response with templating" data-og-width="798" width="798" data-og-height="201" height="201" data-path="images/screenshots/templated-proxy-response.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/templated-proxy-response.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=f1fff1231f7b7ba6572538a00feb0127 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/templated-proxy-response.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=ee4c0acfe4624d63be95c95a7621378f 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/templated-proxy-response.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=502fef7cf287efce0b216c4c3e643eee 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/templated-proxy-response.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=b1eecffbd25af8d6fa1b443731726f4f 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/templated-proxy-response.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=ff91b34795370011a4cd89febc0f9967 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/templated-proxy-response.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=ebd43e8c20eab125a4918cdaecf4c1ef 2500w" />

## Hostname rewriting

Often API responses contain absolute links and other content that refers to the domain name of the API's origin.
When proxying to another API this can be undesirable as the mock API's domain is different from the proxy target and thus a client following such a link would make its next request directly to the proxy target rather than the mock API.

To remedy this issue we can enable hostname rewriting, which will replace any instances of the proxy target's domain name in the response headers or body with the mock API's domain name.

For instance, if we configured a stub in a mock API `https://my-mock-api.wiremockapi.cloud` to with a proxy target of `https://api.github.com` and a proxied response body contained `"self": "https://api.github.com/users/123"`, with hostname rewriting enabled this would be changed to `"self": "https://my-mock-api.wiremockapi.cloud/users/123"`.

<img src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/proxy-hostname-rewriting.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=ada33c1f5f07b0ec2a34dde0f6dde33b" title="Proxy hostname rewriting" data-og-width="2004" width="2004" data-og-height="712" height="712" data-path="images/screenshots/proxy-hostname-rewriting.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/proxy-hostname-rewriting.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=7f20d02ad01d3006a502aa31ec7b36bc 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/proxy-hostname-rewriting.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=70be51ca7426f181d99eff84ec276652 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/proxy-hostname-rewriting.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=fed434079696182b48e07c864a932618 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/proxy-hostname-rewriting.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=17020c68eb78d980d9d0146516737013 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/proxy-hostname-rewriting.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=e2a20302a4371d9db3afeda3a056992a 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/proxy-hostname-rewriting.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=9a3f6d06b0c14971a2c9588d210e2444 2500w" />

## The proxy/intercept pattern

It is often desirable to proxy requests by default while stubbing a few specific cases. This can be achieved using a variation
of the [Default Responses](./default-responses/) approach.

In summary, the proxy stub is created to be the default, with broad request matching criteria and a low priority value. Then
individual stubs are created at higher priorities with specific request URLs, bodies or anything else distinguishing.

Examples of things these specific stubs can be used for are:

* Return an HTTP 503 response
* Return response data in a format not expected by your app's client
* Close the connection prematurely without sending a response (see [Simulating Faults](./simulating-faults/))
