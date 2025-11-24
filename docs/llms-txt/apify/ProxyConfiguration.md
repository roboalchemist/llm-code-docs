# Source: https://docs.apify.com/sdk/python/reference/class/ProxyConfiguration.md

# Source: https://docs.apify.com/sdk/js/reference/class/ProxyConfiguration.md

# ProxyConfiguration<!-- -->

Configures connection to a proxy server with the provided options. Proxy servers are used to prevent target websites from blocking your crawlers based on IP address rate limits or blacklists. Setting proxy configuration in your crawlers automatically configures them to use the selected proxies for all connections. You can get information about the currently used proxy by inspecting the [ProxyInfo](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ProxyInfo.md) property in your crawler's page function. There, you can inspect the proxy's URL and other attributes.

The proxy servers are managed by [Apify Proxy](https://docs.apify.com/proxy). To be able to use Apify Proxy, you need an Apify account and access to the selected proxies. If you provide no configuration option, the proxies will be managed automatically using a smart algorithm.

If you want to use your own proxies, use the [ProxyConfigurationOptions.proxyUrls](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ProxyConfigurationOptions.md#proxyUrls) option. Your list of proxy URLs will be rotated by the configuration if this option is provided.

**Example usage:**

```

const proxyConfiguration = await Actor.createProxyConfiguration({
  groups: ['GROUP1', 'GROUP2'] // List of Apify Proxy groups
  countryCode: 'US',
});

const crawler = new CheerioCrawler({
  // ...
  proxyConfiguration,
  requestHandler({ proxyInfo }) {
     const usedProxyUrl = proxyInfo.url; // Getting the proxy URL
  }
})
```

### Hierarchy

* ProxyConfiguration
  * *ProxyConfiguration*

## Index[**](#Index)

### Properties

* [**config](#config)
* [**isManInTheMiddle](#isManInTheMiddle)

### Methods

* [**initialize](#initialize)
* [**newProxyInfo](#newProxyInfo)
* [**newUrl](#newUrl)

## Properties<!-- -->[**](#Properties)

### [**](#config)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L171)readonlyconfig

**config: [Configuration](https://docs.apify.com/sdk/js/sdk/js/reference/class/Configuration.md) =

<!-- -->

...

### [**](#isManInTheMiddle)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/proxy_configuration.d.ts#L157)externalinheritedisManInTheMiddle

**isManInTheMiddle: boolean

Inherited from CoreProxyConfiguration.isManInTheMiddle

## Methods<!-- -->[**](#Methods)

### [**](#initialize)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L234)initialize

* ****initialize**(): Promise\<boolean>

- Loads proxy password if token is provided and checks access to Apify Proxy and provided proxy groups if Apify Proxy configuration is used. Also checks if country has access to Apify Proxy groups if the country code is provided.

  You should use the createProxyConfiguration function to create a pre-initialized `ProxyConfiguration` instance instead of calling this manually.

  ***

  #### Returns Promise\<boolean>

### [**](#newProxyInfo)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L260)newProxyInfo

* ****newProxyInfo**(sessionId, options): Promise\<undefined | [ProxyInfo](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ProxyInfo.md)>

- Overrides CoreProxyConfiguration.newProxyInfo

  This function creates a new [ProxyInfo](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ProxyInfo.md) info object. It is used by CheerioCrawler and PuppeteerCrawler to generate proxy URLs and also to allow the user to inspect the currently used proxy via the requestHandler parameter `proxyInfo`. Use it if you want to work with a rich representation of a proxy URL. If you need the URL string only, use [ProxyConfiguration.newUrl](https://docs.apify.com/sdk/js/sdk/js/reference/class/ProxyConfiguration.md#newUrl).

  ***

  #### Parameters

  * ##### optionalsessionId: string | number

    Represents the identifier of user Session that can be managed by the SessionPool or you can use the Apify Proxy [Session](https://docs.apify.com/proxy#sessions) identifier. When the provided sessionId is a number, it's converted to a string. Property sessionId of [ProxyInfo](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ProxyInfo.md) is always returned as a type string.

    All the HTTP requests going through the proxy with the same session identifier will use the same target proxy server (i.e. the same IP address). The identifier must not be longer than 50 characters and include only the following: `0-9`, `a-z`, `A-Z`, `"."`, `"_"` and `"~"`.

  * ##### optionaloptions: TieredProxyOptions

  #### Returns Promise\<undefined | [ProxyInfo](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ProxyInfo.md)>

  Represents information about used proxy and its configuration.

### [**](#newUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L294)newUrl

* ****newUrl**(sessionId, options): Promise\<undefined | string>

- Overrides CoreProxyConfiguration.newUrl

  Returns a new proxy URL based on provided configuration options and the `sessionId` parameter.

  ***

  #### Parameters

  * ##### optionalsessionId: string | number

    Represents the identifier of user Session that can be managed by the SessionPool or you can use the Apify Proxy [Session](https://docs.apify.com/proxy#sessions) identifier. When the provided sessionId is a number, it's converted to a string.

    All the HTTP requests going through the proxy with the same session identifier will use the same target proxy server (i.e. the same IP address). The identifier must not be longer than 50 characters and include only the following: `0-9`, `a-z`, `A-Z`, `"."`, `"_"` and `"~"`.

  * ##### optionaloptions: TieredProxyOptions

  #### Returns Promise\<undefined | string>

  A string with a proxy URL, including authentication credentials and port number. For example, `http://bob:password123@proxy.example.com:8000`
