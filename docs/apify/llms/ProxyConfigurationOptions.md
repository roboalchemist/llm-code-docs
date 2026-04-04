# Source: https://docs.apify.com/sdk/js/reference/interface/ProxyConfigurationOptions.md

# ProxyConfigurationOptions<!-- -->

### Hierarchy

* ProxyConfigurationOptions
  * *ProxyConfigurationOptions*

## Index[**](#Index)

### Properties

* [**apifyProxyCountry](#apifyProxyCountry)
* [**apifyProxyGroups](#apifyProxyGroups)
* [**countryCode](#countryCode)
* [**groups](#groups)
* [**newUrlFunction](#newUrlFunction)
* [**password](#password)
* [**proxyUrls](#proxyUrls)
* [**tieredProxyConfig](#tieredProxyConfig)
* [**tieredProxyUrls](#tieredProxyUrls)

## Properties<!-- -->[**](#Properties)

### [**](#apifyProxyCountry)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L59)optionalapifyProxyCountry

**apifyProxyCountry?

<!-- -->

: string

Same option as `countryCode` which can be used to configurate the proxy by UI input schema. You should use the `countryCode` option in your crawler code.

### [**](#apifyProxyGroups)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L53)optionalapifyProxyGroups

**apifyProxyGroups?

<!-- -->

: string\[]

Same option as `groups` which can be used to configurate the proxy by UI input schema. You should use the `groups` option in your crawler code.

### [**](#countryCode)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L47)optionalcountryCode

**countryCode?

<!-- -->

: string

If set and relevant proxies are available in your Apify account, all proxied requests will use IP addresses that are geolocated to the specified country. For example `GB` for IPs from Great Britain. Note that online services often have their own rules for handling geolocation and thus the country selection is a best attempt at geolocation, rather than a guaranteed hit. This parameter is optional, by default, each proxied request is assigned an IP address from a random country. The country code needs to be a two letter ISO country code. See the [full list of available country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements). This parameter is optional, by default, the proxy uses all available proxy servers from all countries. on the Apify cloud, or when using the [Apify CLI](https://github.com/apify/apify-cli).

### [**](#groups)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L34)optionalgroups

**groups?

<!-- -->

: string\[]

An array of proxy groups to be used by the [Apify Proxy](https://docs.apify.com/proxy). If not provided, the proxy will select the groups automatically.

### [**](#newUrlFunction)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/proxy_configuration.d.ts#L20)externaloptionalinheritednewUrlFunction

**newUrlFunction?

<!-- -->

: ProxyConfigurationFunction

Inherited from CoreProxyConfigurationOptions.newUrlFunction

Custom function that allows you to generate the new proxy URL dynamically. It gets the `sessionId` as a parameter and an optional parameter with the `Request` object when applicable. Can return either stringified proxy URL or `null` if the proxy should not be used. Can be asynchronous.

This function is used to generate the URL when [ProxyConfiguration.newUrl](https://docs.apify.com/sdk/js/sdk/js/reference/class/ProxyConfiguration.md#newUrl) or [ProxyConfiguration.newProxyInfo](https://docs.apify.com/sdk/js/sdk/js/reference/class/ProxyConfiguration.md#newProxyInfo) is called.

### [**](#password)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L28)optionalpassword

**password?

<!-- -->

: string

User's password for the proxy. By default, it is taken from the `APIFY_PROXY_PASSWORD` environment variable, which is automatically set by the system when running the Actors.

### [**](#proxyUrls)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/proxy_configuration.d.ts#L13)externaloptionalinheritedproxyUrls

**proxyUrls?

<!-- -->

: string\[]

Inherited from CoreProxyConfigurationOptions.proxyUrls

An array of custom proxy URLs to be rotated. Custom proxies are not compatible with Apify Proxy and an attempt to use both configuration options will cause an error to be thrown on initialize.

### [**](#tieredProxyConfig)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/proxy_configuration.ts#L65)optionaltieredProxyConfig

**tieredProxyConfig?

<!-- -->

: Omit<[ProxyConfigurationOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ProxyConfigurationOptions.md), keyof ProxyConfigurationOptions | tieredProxyConfig>\[]

Multiple different ProxyConfigurationOptions stratified into tiers. Crawlee crawlers will switch between those tiers based on the blocked request statistics.

### [**](#tieredProxyUrls)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/proxy_configuration.d.ts#L32)externaloptionalinheritedtieredProxyUrls

**tieredProxyUrls?

<!-- -->

: (null | string)\[]\[]

Inherited from CoreProxyConfigurationOptions.tieredProxyUrls

An array of custom proxy URLs to be rotated stratified in tiers. This is a more advanced version of `proxyUrls` that allows you to define a hierarchy of proxy URLs If everything goes well, all the requests will be sent through the first proxy URL in the list. Whenever the crawler encounters a problem with the current proxy on the given domain, it will switch to the higher tier for this domain. The crawler probes lower-level proxies at intervals to check if it can make the tier downshift.

This feature is useful when you have a set of proxies with different performance characteristics (speed, price, antibot performance etc.) and you want to use the best one for each domain.

Use `null` as a proxy URL to disable the proxy for the given tier.
