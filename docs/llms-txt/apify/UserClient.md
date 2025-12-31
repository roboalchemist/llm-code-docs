# Source: https://docs.apify.com/api/client/python/reference/class/UserClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/UserClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/UserClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/UserClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/UserClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/UserClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/UserClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/UserClient.md

# UserClient<!-- -->

### Hierarchy

* ResourceClient
  * *UserClient*

## Index[**](#Index)

### Properties

* [**apifyClient](#apifyClient)
* [**baseUrl](#baseUrl)
* [**httpClient](#httpClient)
* [**id](#id)
* [**params](#params)
* [**publicBaseUrl](#publicBaseUrl)
* [**resourcePath](#resourcePath)
* [**safeId](#safeId)
* [**url](#url)

### Methods

* [**get](#get)
* [**limits](#limits)
* [**monthlyUsage](#monthlyUsage)
* [**updateLimits](#updateLimits)

## Properties<!-- -->[**](#Properties)

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L35)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L27)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L37)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L23)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L39)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L29)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L31)inheritedresourcePath

**resourcePath: string

Inherited from ResourceClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L25)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L33)inheritedurl

**url: string

Inherited from ResourceClient.url

## Methods<!-- -->[**](#Methods)

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/user.ts#L23)get

* ****get**(): Promise<[User](https://docs.apify.com/api/client/js/api/client/js/reference/interface/User.md)>

- Depending on whether ApifyClient was created with a token, the method will either return public or private user data. <https://docs.apify.com/api/v2#/reference/users>

  ***

  #### Returns Promise<[User](https://docs.apify.com/api/client/js/api/client/js/reference/interface/User.md)>

### [**](#limits)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/user.ts#L55)limits

* ****limits**(): Promise\<undefined | [AccountAndUsageLimits](https://docs.apify.com/api/client/js/api/client/js/reference/interface/AccountAndUsageLimits.md)>

- <https://docs.apify.com/api/v2/#/reference/users/account-and-usage-limits>

  ***

  #### Returns Promise\<undefined | [AccountAndUsageLimits](https://docs.apify.com/api/client/js/api/client/js/reference/interface/AccountAndUsageLimits.md)>

### [**](#monthlyUsage)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/user.ts#L30)monthlyUsage

* ****monthlyUsage**(): Promise\<undefined | [MonthlyUsage](https://docs.apify.com/api/client/js/api/client/js/reference/interface/MonthlyUsage.md)>

- <https://docs.apify.com/api/v2/#/reference/users/monthly-usage>

  ***

  #### Returns Promise\<undefined | [MonthlyUsage](https://docs.apify.com/api/client/js/api/client/js/reference/interface/MonthlyUsage.md)>

### [**](#updateLimits)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/user.ts#L74)updateLimits

* ****updateLimits**(options): Promise\<void>

- <https://docs.apify.com/api/v2/#/reference/users/account-and-usage-limits>

  ***

  #### Parameters

  * ##### options: [LimitsUpdateOptions](https://docs.apify.com/api/client/js/api/client/js/reference.md#LimitsUpdateOptions)

  #### Returns Promise\<void>
