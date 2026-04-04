# Source: https://crawlee.dev/js/api/core/interface/ProxyConfigurationOptions.md

# ProxyConfigurationOptions<!-- -->

## Index[**](#Index)

### Properties

* [**newUrlFunction](#newUrlFunction)
* [**proxyUrls](#proxyUrls)
* [**tieredProxyUrls](#tieredProxyUrls)

## Properties<!-- -->[**](#Properties)

### [**](#newUrlFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L29)optionalnewUrlFunction

**newUrlFunction?

<!-- -->

: [ProxyConfigurationFunction](https://crawlee.dev/js/api/core/interface/ProxyConfigurationFunction.md)

Custom function that allows you to generate the new proxy URL dynamically. It gets the `sessionId` as a parameter and an optional parameter with the `Request` object when applicable. Can return either stringified proxy URL or `null` if the proxy should not be used. Can be asynchronous.

This function is used to generate the URL when [ProxyConfiguration.newUrl](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md#newUrl) or [ProxyConfiguration.newProxyInfo](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md#newProxyInfo) is called.

### [**](#proxyUrls)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L21)optionalproxyUrls

**proxyUrls?

<!-- -->

: UrlList

An array of custom proxy URLs to be rotated. Custom proxies are not compatible with Apify Proxy and an attempt to use both configuration options will cause an error to be thrown on initialize.

### [**](#tieredProxyUrls)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L42)optionaltieredProxyUrls

**tieredProxyUrls?

<!-- -->

: UrlList\[]

An array of custom proxy URLs to be rotated stratified in tiers. This is a more advanced version of `proxyUrls` that allows you to define a hierarchy of proxy URLs If everything goes well, all the requests will be sent through the first proxy URL in the list. Whenever the crawler encounters a problem with the current proxy on the given domain, it will switch to the higher tier for this domain. The crawler probes lower-level proxies at intervals to check if it can make the tier downshift.

This feature is useful when you have a set of proxies with different performance characteristics (speed, price, antibot performance etc.) and you want to use the best one for each domain.

Use `null` as a proxy URL to disable the proxy for the given tier.
