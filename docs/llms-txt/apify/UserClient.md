# Source: https://docs.apify.com/api/client/python/reference/class/UserClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/UserClient.md

# UserClient<!-- -->

Client for managing user account information.

Provides methods to retrieve user details, monthly usage statistics, and account limits. When using an API token, you can access your own user information or public information about other users.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const userClient = client.user('my-user-id');

  // Get user information
  const user = await userClient.get();

  // Get monthly usage
  const usage = await userClient.monthlyUsage();

  // Get account limits
  const limits = await userClient.limits();
  ```

* **@see**

  <https://docs.apify.com/platform/actors/running>

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

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L36)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L28)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L38)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L24)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L40)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L30)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L32)inheritedresourcePath

**resourcePath: string

Inherited from ResourceClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L26)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L34)inheritedurl

**url: string

Inherited from ResourceClient.url

## Methods<!-- -->[**](#Methods)

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/user.ts#L51)get

* ****get**(): Promise<[User](https://docs.apify.com/api/client/js/api/client/js/reference/interface/User.md)>

- Retrieves the user data.

  Depending on whether ApifyClient was created with a token, the method will either return public or private user data.

  * **@see**

    <https://docs.apify.com/api/v2/user-get>

  ***

  #### Returns Promise<[User](https://docs.apify.com/api/client/js/api/client/js/reference/interface/User.md)>

  The user object.

### [**](#limits)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/user.ts#L89)limits

* ****limits**(): Promise\<undefined | [AccountAndUsageLimits](https://docs.apify.com/api/client/js/api/client/js/reference/interface/AccountAndUsageLimits.md)>

- Retrieves the user's account and usage limits.

  * **@see**

    <https://docs.apify.com/api/v2/user-limits-get>

  ***

  #### Returns Promise\<undefined | [AccountAndUsageLimits](https://docs.apify.com/api/client/js/api/client/js/reference/interface/AccountAndUsageLimits.md)>

  The account and usage limits object, or `undefined` if it does not exist.

### [**](#monthlyUsage)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/user.ts#L61)monthlyUsage

* ****monthlyUsage**(): Promise\<undefined | [MonthlyUsage](https://docs.apify.com/api/client/js/api/client/js/reference/interface/MonthlyUsage.md)>

- Retrieves the user's monthly usage data.

  * **@see**

    <https://docs.apify.com/api/v2/user-usage-monthly-get>

  ***

  #### Returns Promise\<undefined | [MonthlyUsage](https://docs.apify.com/api/client/js/api/client/js/reference/interface/MonthlyUsage.md)>

  The monthly usage object, or `undefined` if it does not exist.

### [**](#updateLimits)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/user.ts#L111)updateLimits

* ****updateLimits**(options): Promise\<void>

- Updates the user's account and usage limits.

  * **@see**

    <https://docs.apify.com/api/v2/user-limits-put>

  ***

  #### Parameters

  * ##### options: [LimitsUpdateOptions](https://docs.apify.com/api/client/js/api/client/js/reference.md#LimitsUpdateOptions)

    The new limits to set.

  #### Returns Promise\<void>
