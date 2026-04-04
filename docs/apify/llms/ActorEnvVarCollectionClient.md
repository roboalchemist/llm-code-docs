# Source: https://docs.apify.com/api/client/python/reference/class/ActorEnvVarCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorEnvVarCollectionClient.md

# ActorEnvVarCollectionClient<!-- -->

Client for managing the collection of environment variables for an Actor version.

Environment variables are key-value pairs that are available to the Actor during execution. This client provides methods to list and create environment variables.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const actorClient = client.actor('my-actor-id');
  const versionClient = actorClient.version('0.1');

  // List all environment variables
  const envVarsClient = versionClient.envVars();
  const { items } = await envVarsClient.list();

  // Create a new environment variable
  const newEnvVar = await envVarsClient.create({
    name: 'MY_VAR',
    value: 'my-value',
    isSecret: false
  });
  ```

* **@see**

  <https://docs.apify.com/platform/actors/development/actor-definition/environment-variables>

### Hierarchy

* ResourceCollectionClient
  * *ActorEnvVarCollectionClient*

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

* [**create](#create)
* [**list](#list)

## Properties<!-- -->[**](#Properties)

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L36)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceCollectionClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L28)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceCollectionClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L38)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceCollectionClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L24)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceCollectionClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L40)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceCollectionClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L30)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceCollectionClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L32)inheritedresourcePath

**resourcePath: string

Inherited from ResourceCollectionClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L26)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceCollectionClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L34)inheritedurl

**url: string

Inherited from ResourceCollectionClient.url

## Methods<!-- -->[**](#Methods)

### [**](#create)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_env_var_collection.ts#L77)create

* ****create**(actorEnvVar): Promise<[ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)>

- Creates a new environment variable for this Actor version.

  * **@see**

    <https://docs.apify.com/api/v2/act-version-env-vars-post>

  ***

  #### Parameters

  * ##### actorEnvVar: [ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)

    The environment variable data.

  #### Returns Promise<[ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)>

  The created environment variable object.

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_env_var_collection.ts#L64)list

* ****list**(\_options): Promise<[ActorEnvVarListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorEnvVarListResult)> & AsyncIterable<[ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md), any, any>

- Lists all environment variables of this Actor version.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list();
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list()) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/act-version-env-vars-get>

  ***

  #### Parameters

  * ##### \_options: [ActorEnvVarCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvVarCollectionListOptions.md) = <!-- -->{}

  #### Returns Promise<[ActorEnvVarListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorEnvVarListResult)> & AsyncIterable<[ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md), any, any>

  A paginated iterator of environment variables.
