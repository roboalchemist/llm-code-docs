# Source: https://transloadit.com/docs/robots/file-serve.md

When you want Transloadit to tranform files on the fly, you can use this Robot to determine which Step of a Template should be served to the end-user (via a CDN), as well as set extra information on the served files, such as headers. This way you can for instance suggest the CDN for how long to keep cached copies of the result around. By default, as you can see in the `headers` parameter, we instruct browsers to cache the result for 72h (`259200` seconds) and CDNs to cache the content for 24h (`86400` seconds). These values should be adjusted to suit your use case.

🤖/file/serve merely acts as the glue layer between our Assembly engine and serving files over HTTP. It let's you pick the proper result of a series of Steps via the `use` parameter and configure headers on the original content. That is where its responsibilies end, and 🤖/tlcdn/deliver, then takes over to globally distribute this original content across the globe, and make sure that is cached close to your end-users, when they make requests such as <https://my-app.tlcdn.com/resize-img/canoe.jpg?w=500>, another. 🤖/tlcdn/deliver is not a part of your Assembly Instructions, but it may appear on your invoices as bandwidth charges incur when distributing the cached copies. 🤖/file/serve only charges when the CDN does not have a cached copy and requests to regenerate the original content, which depending on your caching settings could be just once a month, or year, per file/transformation.

While theoretically possible, you could use [🤖/file/serve](/docs/robots/file-serve.md) directly in HTML files, but we strongly recommend against this, because if your site gets popular and the media URL that /file/serve is handling gets hit one million times, that is one million new image resizes. Wrapping it with a CDN (and thanks to the caching that comes with it) makes sure encoding charges stay low, as well as latencies.

Also consider configuring caching headers and cache-control directives to control how content is cached and invalidated on the CDN edge servers, balancing between freshness and efficiency.

## Smart CDN Security with Signature Authentication

You can leverage [Signature Authentication](/docs/api/authentication.md#smart-cdn) to avoid abuse of our encoding platform. Below is a quick Node.js example using our Node SDK, but there are [examples for other languages and SDKs](/docs/api/authentication.md#example-code) as well.

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```javascript
// yarn add transloadit
// or
// npm install --save transloadit

import { Transloadit } from 'transloadit'

const transloadit = new Transloadit({
  authKey: 'YOUR_TRANSLOADIT_KEY',
  authSecret: 'YOUR_TRANSLOADIT_SECRET',
})

const url = transloadit.getSignedSmartCDNUrl({
  workspace: 'YOUR_WORKSPACE',
  template: 'YOUR_TEMPLATE',
  input: 'image.png',
  urlParams: { height: 100, width: 100 },
})

console.log(url)

```

This will generate a signed Smart CDN URL that includes authentication parameters, preventing unauthorized access to your transformation endpoints.

## More information

* [Content Delivery](/services/content-delivery/)
* [🤖/file/serve](/docs/robots/file-serve.md) pricing
* [🤖/tlcdn/deliver](/docs/robots/tlcdn-deliver.md) pricing
* [File Preview Feature](/blog/2024/06/file-preview-with-smart-cdn/) blog post
