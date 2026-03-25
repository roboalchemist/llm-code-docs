# Source: https://crawlee.dev/js/api/types/interface/RequestQueueOptions.md

# Source: https://crawlee.dev/js/api/core/interface/RequestQueueOptions.md

# RequestQueueOptions<!-- -->

* **@deprecated**

  Use [RequestProviderOptions](https://crawlee.dev/js/api/core/interface/RequestProviderOptions.md) instead.

### Hierarchy

* [RequestProviderOptions](https://crawlee.dev/js/api/core/interface/RequestProviderOptions.md)
  * *RequestQueueOptions*

## Index[**](#Index)

### Properties

* [**client](#client)
* [**id](#id)
* [**name](#name)
* [**proxyConfiguration](#proxyConfiguration)

## Properties<!-- -->[**](#Properties)

### [**](#client)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L912)inheritedclient

**client: [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)

Inherited from RequestProviderOptions.client

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L910)inheritedid

**id: string

Inherited from RequestProviderOptions.id

### [**](#name)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L911)optionalinheritedname

**name?

<!-- -->

: string

Inherited from RequestProviderOptions.name

### [**](#proxyConfiguration)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L919)optionalinheritedproxyConfiguration

**proxyConfiguration?

<!-- -->

: [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)

Inherited from RequestProviderOptions.proxyConfiguration

Used to pass the proxy configuration for the `requestsFromUrl` objects. Takes advantage of the internal address rotation and authentication process. If undefined, the `requestsFromUrl` requests will be made without proxy.
