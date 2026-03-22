# Source: https://crawlee.dev/js/api/core/interface/ProxyInfo.md

# ProxyInfo<!-- -->

The main purpose of the ProxyInfo object is to provide information about the current proxy connection used by the crawler for the request. Outside of crawlers, you can get this object by calling [ProxyConfiguration.newProxyInfo](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md#newProxyInfo).

**Example usage:**

```
const proxyConfiguration = new ProxyConfiguration({
  proxyUrls: ['...', '...'] // List of Proxy URLs to rotate
});

// Getting proxyInfo object by calling class method directly
const proxyInfo = await proxyConfiguration.newProxyInfo();

// In crawler
const crawler = new CheerioCrawler({
  // ...
  proxyConfiguration,
  requestHandler({ proxyInfo }) {
     // Getting used proxy URL
      const proxyUrl = proxyInfo.url;

     // Getting ID of used Session
      const sessionIdentifier = proxyInfo.sessionId;
  }
})
```

## Index[**](#Index)

### Properties

* [**hostname](#hostname)
* [**password](#password)
* [**port](#port)
* [**proxyTier](#proxyTier)
* [**sessionId](#sessionId)
* [**url](#url)
* [**username](#username)

## Properties<!-- -->[**](#Properties)

### [**](#hostname)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L104)hostname

**hostname: string

Hostname of your proxy.

### [**](#password)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L99)password

**password: string

User's password for the proxy.

### [**](#port)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L109)port

**port: string | number

Proxy port.

### [**](#proxyTier)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L114)optionalproxyTier

**proxyTier?

<!-- -->

: number

Proxy tier for the current proxy, if applicable (only for `tieredProxyUrls`).

### [**](#sessionId)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L84)optionalsessionId

**sessionId?

<!-- -->

: string

The identifier of used [Session](https://crawlee.dev/js/api/core/class/Session.md), if used.

### [**](#url)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L89)url

**url: string

The URL of the proxy.

### [**](#username)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L94)optionalusername

**username?

<!-- -->

: string

Username for the proxy.
