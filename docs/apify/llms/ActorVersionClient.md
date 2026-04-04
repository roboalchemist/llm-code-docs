# Source: https://docs.apify.com/api/client/python/reference/class/ActorVersionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorVersionClient.md

# ActorVersionClient<!-- -->

Client for managing a specific Actor version.

Actor versions represent specific builds or snapshots of an Actor's code. This client provides methods to get, update, and delete versions, as well as manage their environment variables.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const actorClient = client.actor('my-actor-id');

  // Get a specific version
  const versionClient = actorClient.version('0.1');
  const version = await versionClient.get();

  // Update version
  await versionClient.update({ buildTag: 'latest' });
  ```

* **@see**

  <https://docs.apify.com/platform/actors/development/actor-definition/versions>

### Hierarchy

* ResourceClient
  * *ActorVersionClient*

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
* [**envVar](#envVar)
* [**envVars](#envVars)
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

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_version.ts#L68)delete

* ****delete**(): Promise\<void>

- Deletes the Actor version.

  * **@see**

    <https://docs.apify.com/api/v2/act-version-delete>

  ***

  #### Returns Promise\<void>

### [**](#envVar)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_version.ts#L79)envVar

* ****envVar**(envVarName): [ActorEnvVarClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorEnvVarClient.md)

- Returns a client for the specified environment variable of this Actor version.

  * **@see**

    <https://docs.apify.com/api/v2/act-version-env-var-get>

  ***

  #### Parameters

  * ##### envVarName: string

    Name of the environment variable.

  #### Returns [ActorEnvVarClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorEnvVarClient.md)

  A client for the environment variable.

### [**](#envVars)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_version.ts#L94)envVars

* ****envVars**(): [ActorEnvVarCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorEnvVarCollectionClient.md)

- Returns a client for the environment variables of this Actor version.

  * **@see**

    <https://docs.apify.com/api/v2/act-version-env-vars-get>

  ***

  #### Returns [ActorEnvVarCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorEnvVarCollectionClient.md)

  A client for the Actor version's environment variables.

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_version.ts#L46)get

* ****get**(): Promise\<undefined | [FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion)>

- Retrieves the Actor version.

  * **@see**

    <https://docs.apify.com/api/v2/act-version-get>

  ***

  #### Returns Promise\<undefined | [FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion)>

  The Actor version object, or `undefined` if it does not exist.

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_version.ts#L57)update

* ****update**(newFields): Promise<[FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion)>

- Updates the Actor version with the specified fields.

  * **@see**

    <https://docs.apify.com/api/v2/act-version-put>

  ***

  #### Parameters

  * ##### newFields: [ActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorVersion)

    Fields to update.

  #### Returns Promise<[FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion)>

  The updated Actor version object.
