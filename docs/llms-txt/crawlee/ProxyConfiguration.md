# Source: https://crawlee.dev/js/api/core/class/ProxyConfiguration.md

# ProxyConfiguration<!-- -->

Configures connection to a proxy server with the provided options. Proxy servers are used to prevent target websites from blocking your crawlers based on IP address rate limits or blacklists. Setting proxy configuration in your crawlers automatically configures them to use the selected proxies for all connections. You can get information about the currently used proxy by inspecting the [ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md) property in your crawler's page function. There, you can inspect the proxy's URL and other attributes.

If you want to use your own proxies, use the [ProxyConfigurationOptions.proxyUrls](https://crawlee.dev/js/api/core/interface/ProxyConfigurationOptions.md#proxyUrls) option. Your list of proxy URLs will be rotated by the configuration if this option is provided.

**Example usage:**

```

const proxyConfiguration = new ProxyConfiguration({
  proxyUrls: ['...', '...'],
});

const crawler = new CheerioCrawler({
  // ...
  proxyConfiguration,
  requestHandler({ proxyInfo }) {
     const usedProxyUrl = proxyInfo.url; // Getting the proxy URL
  }
})
```

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**isManInTheMiddle](#isManInTheMiddle)

### Methods

* [**newProxyInfo](#newProxyInfo)
* [**newUrl](#newUrl)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L233)constructor

* ****new ProxyConfiguration**(options): [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)

- Creates a [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md) instance based on the provided options. Proxy servers are used to prevent target websites from blocking your crawlers based on IP address rate limits or blacklists. Setting proxy configuration in your crawlers automatically configures them to use the selected proxies for all connections.

  ```
  const proxyConfiguration = new ProxyConfiguration({
      proxyUrls: ['http://user:pass@proxy-1.com', 'http://user:pass@proxy-2.com'],
  });

  const crawler = new CheerioCrawler({
    // ...
    proxyConfiguration,
    requestHandler({ proxyInfo }) {
        const usedProxyUrl = proxyInfo.url; // Getting the proxy URL
    }
  })
  ```

  ***

  #### Parameters

  * ##### options: [ProxyConfigurationOptions](https://crawlee.dev/js/api/core/interface/ProxyConfigurationOptions.md) = <!-- -->{}

  #### Returns [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)

## Properties<!-- -->[**](#Properties)

### [**](#isManInTheMiddle)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L204)isManInTheMiddle

**isManInTheMiddle: boolean =

<!-- -->

false

## Methods<!-- -->[**](#Methods)

### [**](#newProxyInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L274)newProxyInfo

* ****newProxyInfo**(sessionId, options): Promise\<undefined | [ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md)>

- This function creates a new [ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md) info object. It is used by CheerioCrawler and PuppeteerCrawler to generate proxy URLs and also to allow the user to inspect the currently used proxy via the requestHandler parameter `proxyInfo`. Use it if you want to work with a rich representation of a proxy URL. If you need the URL string only, use [ProxyConfiguration.newUrl](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md#newUrl).

  ***

  #### Parameters

  * ##### optionalsessionId: string | number

    Represents the identifier of user [Session](https://crawlee.dev/js/api/core/class/Session.md) that can be managed by the [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) or you can use the Apify Proxy [Session](https://docs.apify.com/proxy#sessions) identifier. When the provided sessionId is a number, it's converted to a string. Property sessionId of [ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md) is always returned as a type string.

    All the HTTP requests going through the proxy with the same session identifier will use the same target proxy server (i.e. the same IP address). The identifier must not be longer than 50 characters and include only the following: `0-9`, `a-z`, `A-Z`, `"."`, `"_"` and `"~"`.

  * ##### optionaloptions: TieredProxyOptions

  #### Returns Promise\<undefined | [ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md)>

  Represents information about used proxy and its configuration.

### [**](#newUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L383)newUrl

* ****newUrl**(sessionId, options): Promise\<undefined | string>

- Returns a new proxy URL based on provided configuration options and the `sessionId` parameter.

  ***

  #### Parameters

  * ##### optionalsessionId: string | number

    Represents the identifier of user [Session](https://crawlee.dev/js/api/core/class/Session.md) that can be managed by the [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) or you can use the Apify Proxy [Session](https://docs.apify.com/proxy#sessions) identifier. When the provided sessionId is a number, it's converted to a string.

    All the HTTP requests going through the proxy with the same session identifier will use the same target proxy server (i.e. the same IP address). The identifier must not be longer than 50 characters and include only the following: `0-9`, `a-z`, `A-Z`, `"."`, `"_"` and `"~"`.

  * ##### optionaloptions: TieredProxyOptions

  #### Returns Promise\<undefined | string>

  A string with a proxy URL, including authentication credentials and port number. For example, `http://bob:password123@proxy.example.com:8000`
