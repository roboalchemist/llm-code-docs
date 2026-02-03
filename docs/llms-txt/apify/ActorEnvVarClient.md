# Source: https://docs.apify.com/api/client/python/reference/class/ActorEnvVarClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorEnvVarClient.md

# ActorEnvVarClient<!-- -->

Client for managing a specific Actor environment variable.

Environment variables are key-value pairs that are available to the Actor during execution. This client provides methods to get, update, and delete environment variables.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const actorClient = client.actor('my-actor-id');
  const versionClient = actorClient.version('0.1');

  // Get an environment variable
  const envVarClient = versionClient.envVar('MY_VAR');
  const envVar = await envVarClient.get();

  // Update environment variable
  await envVarClient.update({ value: 'new-value' });
  ```

* **@see**

  <https://docs.apify.com/platform/actors/development/actor-definition/environment-variables>

### Hierarchy

* ResourceClient
  * *ActorEnvVarClient*

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

* [**delete](#delete)
* [**get](#get)
* [**update](#update)

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

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_env_var.ts#L67)delete

* ****delete**(): Promise\<void>

- Deletes the environment variable.

  * **@see**

    <https://docs.apify.com/api/v2/act-version-env-var-delete>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_env_var.ts#L46)get

* ****get**(): Promise\<undefined | [ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)>

- Retrieves the environment variable.

  * **@see**

    <https://docs.apify.com/api/v2/act-version-env-var-get>

  ***

  #### Returns Promise\<undefined | [ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)>

  The environment variable object, or `undefined` if it does not exist.

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_env_var.ts#L57)update

* ****update**(actorEnvVar): Promise<[ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)>

- Updates the environment variable.

  * **@see**

    <https://docs.apify.com/api/v2/act-version-env-var-put>

  ***

  #### Parameters

  * ##### actorEnvVar: [ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)

    The updated environment variable data.

  #### Returns Promise<[ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)>

  The updated environment variable object.
