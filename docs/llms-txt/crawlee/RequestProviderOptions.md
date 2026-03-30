# Source: https://crawlee.dev/js/api/core/interface/RequestProviderOptions.md

# RequestProviderOptions<!-- -->

### Hierarchy

* *RequestProviderOptions*
  * [RequestQueueOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOptions.md)

## Index[**](#Index)

### Properties

* [**client](#client)
* [**id](#id)
* [**name](#name)
* [**proxyConfiguration](#proxyConfiguration)

## Properties<!-- -->[**](#Properties)

### [**](#client)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L912)client

**client: [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L910)id

**id: string

### [**](#name)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L911)optionalname

**name?

<!-- -->

: string

### [**](#proxyConfiguration)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L919)optionalproxyConfiguration

**proxyConfiguration?

<!-- -->

: [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)

Used to pass the proxy configuration for the `requestsFromUrl` objects. Takes advantage of the internal address rotation and authentication process. If undefined, the `requestsFromUrl` requests will be made without proxy.
