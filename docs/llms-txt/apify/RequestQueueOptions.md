# Source: https://docs.apify.com/sdk/js/reference/interface/RequestQueueOptions.md

# externalRequestQueueOptions<!-- -->

* **@deprecated**

  Use RequestProviderOptions instead.

### Hierarchy

* RequestProviderOptions
  * *RequestQueueOptions*

## Index[**](#Index)

### Properties

* [**client](#client)
* [**id](#id)
* [**name](#name)
* [**proxyConfiguration](#proxyConfiguration)

## Properties<!-- -->[**](#Properties)

### [**](#client)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/request_provider.d.ts#L221)externalinheritedclient

**client: StorageClient

Inherited from RequestProviderOptions.client

### [**](#id)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/request_provider.d.ts#L219)externalinheritedid

**id: string

Inherited from RequestProviderOptions.id

### [**](#name)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/request_provider.d.ts#L220)externaloptionalinheritedname

**name?

<!-- -->

: string

Inherited from RequestProviderOptions.name

### [**](#proxyConfiguration)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/request_provider.d.ts#L227)externaloptionalinheritedproxyConfiguration

**proxyConfiguration?

<!-- -->

: ProxyConfiguration

Inherited from RequestProviderOptions.proxyConfiguration

Used to pass the proxy configuration for the `requestsFromUrl` objects. Takes advantage of the internal address rotation and authentication process. If undefined, the `requestsFromUrl` requests will be made without proxy.
