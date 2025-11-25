# Source: https://docs.apify.com/sdk/python/reference/class/ProxyInfo.md

# Source: https://docs.apify.com/sdk/js/reference/interface/ProxyInfo.md

# Source: https://docs.apify.com/sdk/python/reference/class/ProxyInfo.md

# Source: https://docs.apify.com/sdk/js/reference/interface/ProxyInfo.md

# ProxyInfo<!-- -->

The main purpose of the ProxyInfo object is to provide information about the current proxy connection used by the crawler for the request. Outside of crawlers, you can get this object by calling [ProxyConfiguration.newProxyInfo](https://docs.apify.com/sdk/js/sdk/js/reference/class/ProxyConfiguration.md#newProxyInfo).

**Example usage:**

```

const proxyConfiguration = await Actor.createProxyConfiguration({
  groups: ['GROUP1', 'GROUP2'] // List of Apify Proxy groups
  countryCode: 'US',
});

// Getting proxyInfo object by calling class method directly
const proxyInfo = proxyConfiguration.newProxyInfo();

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

### Hierarchy

* ProxyInfo
  * *ProxyInfo*

## Index[**](#Index)

### Properties

* [**countryCode](#countryCode)
* [**groups](#groups)
* [**hostname](#hostname)
* [**password](#password)
* [**port](#port)
* [**proxyTier](#proxyTier)
* [**sessionId](#sessionId)
* [**url](#url)
* [**username](#username)

## Properties<!-- -->[**](#Properties)

### [**](#countryCode)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L117)optionalcountryCode

**countryCode?

<!-- -->

: string

If set and relevant proxies are available in your Apify account, all proxied requests will use IP addresses that are geolocated to the specified country. For example `GB` for IPs from Great Britain. Note that online services often have their own rules for handling geolocation and thus the country selection is a best attempt at geolocation, rather than a guaranteed hit. This parameter is optional, by default, each proxied request is assigned an IP address from a random country. The country code needs to be a two letter ISO country code. See the [full list of available country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements). This parameter is optional, by default, the proxy uses all available proxy servers from all countries.

### [**](#groups)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L105)groups

**groups: string\[]

An array of proxy groups to be used by the [Apify Proxy](https://docs.apify.com/proxy). If not provided, the proxy will select the groups automatically.

### [**](#hostname)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/proxy_configuration.d.ts#L88)externalinheritedhostname

**hostname: string

Inherited from CoreProxyInfo.hostname

Hostname of your proxy.

### [**](#password)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L124)password

**password: string

Overrides CoreProxyInfo.password

User's password for the proxy. By default, it is taken from the `APIFY_PROXY_PASSWORD` environment variable, which is automatically set by the system when running the Actors on the Apify cloud, or when using the [Apify CLI](https://github.com/apify/apify-cli).

### [**](#port)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/proxy_configuration.d.ts#L92)externalinheritedport

**port: string | number

Inherited from CoreProxyInfo.port

Proxy port.

### [**](#proxyTier)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/proxy_configuration.d.ts#L96)externaloptionalinheritedproxyTier

**proxyTier?

<!-- -->

: number

Inherited from CoreProxyInfo.proxyTier

Proxy tier for the current proxy, if applicable (only for `tieredProxyUrls`).

### [**](#sessionId)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/proxy_configuration.d.ts#L72)externaloptionalinheritedsessionId

**sessionId?

<!-- -->

: string

Inherited from CoreProxyInfo.sessionId

The identifier of used Session, if used.

### [**](#url)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/proxy_configuration.d.ts#L76)externalinheritedurl

**url: string

Inherited from CoreProxyInfo.url

The URL of the proxy.

### [**](#username)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/proxy_configuration.d.ts#L80)externaloptionalinheritedusername

**username?

<!-- -->

: string

Inherited from CoreProxyInfo.username

Username for the proxy.
