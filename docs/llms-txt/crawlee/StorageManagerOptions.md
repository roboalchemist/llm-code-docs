# Source: https://crawlee.dev/js/api/core/interface/StorageManagerOptions.md

# StorageManagerOptions<!-- -->

## Index[**](#Index)

### Properties

* [**config](#config)
* [**proxyConfiguration](#proxyConfiguration)
* [**storageClient](#storageClient)

## Properties<!-- -->[**](#Properties)

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/storage_manager.ts#L162)optionalconfig

**config?

<!-- -->

: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

SDK configuration instance, defaults to the static register.

### [**](#proxyConfiguration)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/storage_manager.ts#L174)optionalproxyConfiguration

**proxyConfiguration?

<!-- -->

: [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)

Used to pass the proxy configuration for the `requestsFromUrl` objects. Takes advantage of the internal address rotation and authentication process. If undefined, the `requestsFromUrl` requests will be made without proxy.

### [**](#storageClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/storage_manager.ts#L167)optionalstorageClient

**storageClient?

<!-- -->

: [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)

Optional storage client that should be used to open storages.
