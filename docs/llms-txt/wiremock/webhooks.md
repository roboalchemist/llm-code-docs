# Source: https://docs.wiremock.io/webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Configure Webhooks and Callbacks

> Triggering asynchronous outbound HTTP calls

WireMock Cloud offers the ability to make highly configurable asynchronous outbound HTTP calls triggered by inbound
requests.
This pattern is commonly referred to as webhooks or callbacks and is a common design in APIs that need to proactively
notify their clients of events or perform long-running processing asynchronously without blocking.

## Usage

Webhooks are triggered when a configured stub is matched.
Each stub may have any number of webhooks configured on it.
To add a webhook to a stub in WireMock Cloud, navigate to the stub you wish to configure, scroll down to the webhooks
section of the stub form, underneath the response section, and click "Add webhook".

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/stub-form-webhook-section.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=69cad36e890a9f36bf038ed7e2190680" alt="Stub form webhook section" data-og-width="1067" width="1067" data-og-height="736" height="736" data-path="images/screenshots/webhooks/stub-form-webhook-section.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/stub-form-webhook-section.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=c18c1ad0eb60577e132dba2bd02db68a 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/stub-form-webhook-section.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=ea418894b207772fc7b43b1ce06f06b7 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/stub-form-webhook-section.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=aed44d5739d06090311f4b940f0ee018 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/stub-form-webhook-section.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=162653f8e2648cfbb5aadc9566b619ab 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/stub-form-webhook-section.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=a9cb28b260077307ffc21396d6faf5bf 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/stub-form-webhook-section.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=34d2a4ddd171052f4b426ddb620e9db0 2500w" />

Once you have added a webhook to your stub, you can configure each attribute of the request that will be sent when the
webhook is triggered, including the request method (e.g. `POST`, `GET`, `PUT`), URL, headers, and body.
A delay can also be set on the webhook, in the same fashion as [response delays](/delays), to stop the webhook's
requests from firing until some time after the triggering request is received.

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-form.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=8457c7d0fa08ccbd59a3aa4fdfb7ace1" alt="Webhook request form" data-og-width="998" width="998" data-og-height="690" height="690" data-path="images/screenshots/webhooks/webhook-request-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-form.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=af4e14efd045fa323e31fadce8b24d9e 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-form.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=3753b478baa1c74961d66e9871c63661 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-form.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=a75846472d9213b366c25146e1c156c7 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-form.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=8e867fcddf40bf766f65d183c2195bd1 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-form.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=e172e2b8023d0f5d4590c217d138a971 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-form.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=ab13b21a35a5e03c834f141d9325f033 2500w" />

### Templating

The request URL, header values and body attributes of a webhook can all be [templated](/response-templating), allowing
for request attributes to be set dynamically using the content of the triggering request, as well as other contexts like
[dynamic state](/dynamic-state) and [data sources](/data-sources).
All data and helpers that are available to the response body template are also available to the webhook request
attribute templates, **with the caveat that the triggering request is referenced by `originalRequest`, rather than
`request`.**

## Observing webhooks

All webhook request and responses are logged as events under the request that triggered them, and can be viewed in your
mock API's request log page.

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-log.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=99461c62037c0466e714f056ca943417" alt="Webhook request log" data-og-width="896" width="896" data-og-height="345" height="345" data-path="images/screenshots/webhooks/webhook-request-log.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-log.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=95d6fccd906180341f1f2dadb7a42584 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-log.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=4b2531822098dc7c12a53b6ff26ceaf0 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-log.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=70863a0fea2673e568534bf296982de0 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-log.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=e86cdf5cca77ff95ed591b8d8d8820b2 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-log.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=824287a7a93d12c70c2a21616068204e 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/webhooks/webhook-request-log.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=2b9bd673d82060c9e012b955012fa0e4 2500w" />

## Asynchronous timing

Webhooks are fired asynchronously, outside the lifetime of the request that triggered them, so may not have completed by
the time the triggering request has completed.
There is also no guarantee of the order that webhooks will be fired if multiple webhooks are configured on a stub.
