# Source: https://docs.apify.com/api/client/python/reference/class/ActorClientAsync.md

# ActorClientAsync<!-- -->

Async sub-client for manipulating a single Actor.

### Hierarchy

* [ResourceClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md)
  * *ActorClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#__init__)
* [**build](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#build)
* [**builds](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#builds)
* [**call](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#call)
* [**default\_build](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#default_build)
* [**delete](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#delete)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#get)
* [**last\_run](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#last_run)
* [**runs](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#runs)
* [**start](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#start)
* [**update](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#update)
* [**validate\_input](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#validate_input)
* [**version](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#version)
* [**versions](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#versions)
* [**webhooks](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#webhooks)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L522)\_\_init\_\_

* ****\_\_init\_\_**(\*, base\_url, root\_client, http\_client, resource\_id, resource\_path, params): None

- Overrides [ResourceClientAsync.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md#__init__)

  Initialize a new instance.

  ***

  #### Parameters

  * ##### keyword-onlybase\_url: str

    Base URL of the API server.

  * ##### keyword-onlyroot\_client: [ApifyClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md)

    The ApifyClientAsync instance under which this resource client exists.

  * ##### keyword-onlyhttp\_client: [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)

    The HTTPClientAsync instance to be used in this client.

  * ##### optionalkeyword-onlyresource\_id: str | None = <!-- -->None

    ID of the manipulated resource, in case of a single-resource client.

  * ##### keyword-onlyresource\_path: str

    Path to the resource's endpoint on the API server.

  * ##### optionalkeyword-onlyparams: dict | None = <!-- -->None

    Parameters to include in all requests from this client.

  #### Returns None

### [**](#build)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L788)build

* **async **build**(\*, version\_number, beta\_packages, tag, use\_cache, wait\_for\_finish): dict

- Build the Actor.

  <https://docs.apify.com/api/v2#/reference/actors/build-collection/build-actor>

  ***

  #### Parameters

  * ##### keyword-onlyversion\_number: str

    Actor version number to be built.

  * ##### optionalkeyword-onlybeta\_packages: bool | None = <!-- -->None

    If True, then the Actor is built with beta versions of Apify NPM packages. By default, the build uses latest stable packages.

  * ##### optionalkeyword-onlytag: str | None = <!-- -->None

    Tag to be applied to the build on success. By default, the tag is taken from the Actor version's build tag property.

  * ##### optionalkeyword-onlyuse\_cache: bool | None = <!-- -->None

    If true, the Actor's Docker container will be rebuilt using layer cache (<https://docs.docker.com/develop/develop-images/dockerfile_best-practices/`leverage`-build-cache>). This is to enable quick rebuild during development. By default, the cache is not used.

  * ##### optionalkeyword-onlywait\_for\_finish: int | None = <!-- -->None

    The maximum number of seconds the server waits for the build to finish before returning. By default it is 0, the maximum value is 60.

  #### Returns dict

### [**](#builds)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L832)builds

* ****builds**(): [BuildCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildCollectionClientAsync.md)

- Retrieve a client for the builds of this Actor.

  ***

  #### Returns [BuildCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildCollectionClientAsync.md)

### [**](#call)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L710)call

* **async **call**(\*, run\_input, content\_type, build, max\_items, max\_total\_charge\_usd, restart\_on\_error, memory\_mbytes, timeout\_secs, webhooks, force\_permission\_level, wait\_secs, logger): dict | None

- Start the Actor and wait for it to finish before returning the Run object.

  It waits indefinitely, unless the wait\_secs argument is provided.

  <https://docs.apify.com/api/v2#/reference/actors/run-collection/run-actor>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyrun\_input: Any = <!-- -->None

    The input to pass to the Actor run.

  * ##### optionalkeyword-onlycontent\_type: str | None = <!-- -->None

    The content type of the input.

  * ##### optionalkeyword-onlybuild: str | None = <!-- -->None

    Specifies the Actor build to run. It can be either a build tag or build number. By default, the run uses the build specified in the default run configuration for the Actor (typically latest).

  * ##### optionalkeyword-onlymax\_items: int | None = <!-- -->None

    Maximum number of results that will be returned by this run. If the Actor is charged per result, you will not be charged for more results than the given limit.

  * ##### optionalkeyword-onlymax\_total\_charge\_usd: Decimal | None = <!-- -->None

    A limit on the total charged amount for pay-per-event actors.

  * ##### optionalkeyword-onlyrestart\_on\_error: bool | None = <!-- -->None

    If true, the Actor run process will be restarted whenever it exits with a non-zero status code.

  * ##### optionalkeyword-onlymemory\_mbytes: int | None = <!-- -->None

    Memory limit for the run, in megabytes. By default, the run uses a memory limit specified in the default run configuration for the Actor.

  * ##### optionalkeyword-onlytimeout\_secs: int | None = <!-- -->None

    Optional timeout for the run, in seconds. By default, the run uses timeout specified in the default run configuration for the Actor.

  * ##### optionalkeyword-onlywebhooks: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict] | None = <!-- -->None

    Optional webhooks (<https://docs.apify.com/webhooks>) associated with the Actor run, which can be used to receive a notification, e.g. when the Actor finished or failed. If you already have a webhook set up for the Actor, you do not have to add it again here.

  * ##### optionalkeyword-onlyforce\_permission\_level: ActorPermissionLevel | None = <!-- -->None

    Override the Actor's permissions for this run. If not set, the Actor will run with permissions configured in the Actor settings.

  * ##### optionalkeyword-onlywait\_secs: int | None = <!-- -->None

    The maximum number of seconds the server waits for the run to finish. If not provided, waits indefinitely.

  * ##### optionalkeyword-onlylogger: (Logger | None) | Literal\[default] = <!-- -->'default'

    Logger used to redirect logs from the Actor run. Using "default" literal means that a predefined default logger will be used. Setting `None` will disable any log propagation. Passing custom logger will redirect logs to the provided logger. The logger is also used to capture status and status message of the other Actor run.

  #### Returns dict | None

### [**](#default_build)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L840)default\_build

* **async **default\_build**(\*, wait\_for\_finish): [BuildClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md)

- Retrieve Actor's default build.

  <https://docs.apify.com/api/v2/act-build-default-get>

  ***

  #### Parameters

  * ##### optionalkeyword-onlywait\_for\_finish: int | None = <!-- -->None

    The maximum number of seconds the server waits for the build to finish before returning. By default it is 0, the maximum value is 60.

  #### Returns [BuildClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md)

### [**](#delete)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L631)delete

* **async **delete**(): None

- Delete the Actor.

  <https://docs.apify.com/api/v2#/reference/actors/actor-object/delete-actor>

  ***

  #### Returns None

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L526)get

* **async **get**(): dict | None

- Retrieve the Actor.

  <https://docs.apify.com/api/v2#/reference/actors/actor-object/get-actor>

  ***

  #### Returns dict | None

### [**](#last_run)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L874)last\_run

* ****last\_run**(\*, status, origin): [RunClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md)

- Retrieve the client for the last run of this Actor.

  Last run is retrieved based on the start time of the runs.

  ***

  #### Parameters

  * ##### optionalkeyword-onlystatus: ActorJobStatus | None = <!-- -->None

    Consider only runs with this status.

  * ##### optionalkeyword-onlyorigin: MetaOrigin | None = <!-- -->None

    Consider only runs started with this origin.

  #### Returns [RunClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md)

### [**](#runs)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L836)runs

* ****runs**(): [RunCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunCollectionClientAsync.md)

- Retrieve a client for the runs of this Actor.

  ***

  #### Returns [RunCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunCollectionClientAsync.md)

### [**](#start)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L638)start

* **async **start**(\*, run\_input, content\_type, build, max\_items, max\_total\_charge\_usd, restart\_on\_error, memory\_mbytes, timeout\_secs, force\_permission\_level, wait\_for\_finish, webhooks): dict

- Start the Actor and immediately return the Run object.

  <https://docs.apify.com/api/v2#/reference/actors/run-collection/run-actor>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyrun\_input: Any = <!-- -->None

    The input to pass to the Actor run.

  * ##### optionalkeyword-onlycontent\_type: str | None = <!-- -->None

    The content type of the input.

  * ##### optionalkeyword-onlybuild: str | None = <!-- -->None

    Specifies the Actor build to run. It can be either a build tag or build number. By default, the run uses the build specified in the default run configuration for the Actor (typically latest).

  * ##### optionalkeyword-onlymax\_items: int | None = <!-- -->None

    Maximum number of results that will be returned by this run. If the Actor is charged per result, you will not be charged for more results than the given limit.

  * ##### optionalkeyword-onlymax\_total\_charge\_usd: Decimal | None = <!-- -->None

    A limit on the total charged amount for pay-per-event actors.

  * ##### optionalkeyword-onlyrestart\_on\_error: bool | None = <!-- -->None

    If true, the Actor run process will be restarted whenever it exits with a non-zero status code.

  * ##### optionalkeyword-onlymemory\_mbytes: int | None = <!-- -->None

    Memory limit for the run, in megabytes. By default, the run uses a memory limit specified in the default run configuration for the Actor.

  * ##### optionalkeyword-onlytimeout\_secs: int | None = <!-- -->None

    Optional timeout for the run, in seconds. By default, the run uses timeout specified in the default run configuration for the Actor.

  * ##### optionalkeyword-onlyforce\_permission\_level: ActorPermissionLevel | None = <!-- -->None

    Override the Actor's permissions for this run. If not set, the Actor will run with permissions configured in the Actor settings.

  * ##### optionalkeyword-onlywait\_for\_finish: int | None = <!-- -->None

    The maximum number of seconds the server waits for the run to finish. By default, it is 0, the maximum value is 60.

  * ##### optionalkeyword-onlywebhooks: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict] | None = <!-- -->None

    Optional ad-hoc webhooks (<https://docs.apify.com/webhooks/ad-hoc-webhooks>) associated with the Actor run which can be used to receive a notification, e.g. when the Actor finished or failed. If you already have a webhook set up for the Actor or task, you do not have to add it again here. Each webhook is represented by a dictionary containing these items:

    * `event_types`: List of `WebhookEventType` values which trigger the webhook.
    * `request_url`: URL to which to send the webhook HTTP request.
    * `payload_template`: Optional template for the request payload.

  #### Returns dict

### [**](#update)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L536)update

* **async **update**(\*, name, title, description, seo\_title, seo\_description, versions, restart\_on\_error, is\_public, is\_deprecated, is\_anonymously\_runnable, categories, default\_run\_build, default\_run\_max\_items, default\_run\_memory\_mbytes, default\_run\_timeout\_secs, example\_run\_input\_body, example\_run\_input\_content\_type, actor\_standby\_is\_enabled, actor\_standby\_desired\_requests\_per\_actor\_run, actor\_standby\_max\_requests\_per\_actor\_run, actor\_standby\_idle\_timeout\_secs, actor\_standby\_build, actor\_standby\_memory\_mbytes, pricing\_infos): dict

- Update the Actor with the specified fields.

  <https://docs.apify.com/api/v2#/reference/actors/actor-object/update-actor>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyname: str | None = <!-- -->None

    The name of the Actor.

  * ##### optionalkeyword-onlytitle: str | None = <!-- -->None

    The title of the Actor (human-readable).

  * ##### optionalkeyword-onlydescription: str | None = <!-- -->None

    The description for the Actor.

  * ##### optionalkeyword-onlyseo\_title: str | None = <!-- -->None

    The title of the Actor optimized for search engines.

  * ##### optionalkeyword-onlyseo\_description: str | None = <!-- -->None

    The description of the Actor optimized for search engines.

  * ##### optionalkeyword-onlyversions: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict] | None = <!-- -->None

    The list of Actor versions.

  * ##### optionalkeyword-onlyrestart\_on\_error: bool | None = <!-- -->None

    If true, the Actor run process will be restarted whenever it exits with a non-zero status code.

  * ##### optionalkeyword-onlyis\_public: bool | None = <!-- -->None

    Whether the Actor is public.

  * ##### optionalkeyword-onlyis\_deprecated: bool | None = <!-- -->None

    Whether the Actor is deprecated.

  * ##### optionalkeyword-onlyis\_anonymously\_runnable: bool | None = <!-- -->None

    Whether the Actor is anonymously runnable.

  * ##### optionalkeyword-onlycategories: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    The categories to which the Actor belongs to.

  * ##### optionalkeyword-onlydefault\_run\_build: str | None = <!-- -->None

    Tag or number of the build that you want to run by default.

  * ##### optionalkeyword-onlydefault\_run\_max\_items: int | None = <!-- -->None

    Default limit of the number of results that will be returned by runs of this Actor, if the Actor is charged per result.

  * ##### optionalkeyword-onlydefault\_run\_memory\_mbytes: int | None = <!-- -->None

    Default amount of memory allocated for the runs of this Actor, in megabytes.

  * ##### optionalkeyword-onlydefault\_run\_timeout\_secs: int | None = <!-- -->None

    Default timeout for the runs of this Actor in seconds.

  * ##### optionalkeyword-onlyexample\_run\_input\_body: Any = <!-- -->None

    Input to be prefilled as default input to new users of this Actor.

  * ##### optionalkeyword-onlyexample\_run\_input\_content\_type: str | None = <!-- -->None

    The content type of the example run input.

  * ##### optionalkeyword-onlyactor\_standby\_is\_enabled: bool | None = <!-- -->None

    Whether the Actor Standby is enabled.

  * ##### optionalkeyword-onlyactor\_standby\_desired\_requests\_per\_actor\_run: int | None = <!-- -->None

    The desired number of concurrent HTTP requests for a single Actor Standby run.

  * ##### optionalkeyword-onlyactor\_standby\_max\_requests\_per\_actor\_run: int | None = <!-- -->None

    The maximum number of concurrent HTTP requests for a single Actor Standby run.

  * ##### optionalkeyword-onlyactor\_standby\_idle\_timeout\_secs: int | None = <!-- -->None

    If the Actor run does not receive any requests for this time, it will be shut down.

  * ##### optionalkeyword-onlyactor\_standby\_build: str | None = <!-- -->None

    The build tag or number to run when the Actor is in Standby mode.

  * ##### optionalkeyword-onlyactor\_standby\_memory\_mbytes: int | None = <!-- -->None

    The memory in megabytes to use when the Actor is in Standby mode.

  * ##### optionalkeyword-onlypricing\_infos: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict] | None = <!-- -->None

    A list of objects that describes the pricing of the Actor.

  #### Returns dict

### [**](#validate_input)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L921)validate\_input

* **async **validate\_input**(run\_input, \*, build\_tag, content\_type): bool

- Validate an input for the Actor that defines an input schema.

  ***

  #### Parameters

  * ##### optionalrun\_input: Any = <!-- -->None

    The input to validate.

  * ##### optionalkeyword-onlybuild\_tag: str | None = <!-- -->None

    The actor's build tag.

  * ##### optionalkeyword-onlycontent\_type: str | None = <!-- -->None

    The content type of the input.

  #### Returns bool

### [**](#version)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L906)version

* ****version**(version\_number): [ActorVersionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md)

- Retrieve the client for the specified version of this Actor.

  ***

  #### Parameters

  * ##### version\_number: str

    The version number for which to retrieve the resource client.

  #### Returns [ActorVersionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md)

### [**](#versions)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L902)versions

* ****versions**(): [ActorVersionCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionCollectionClientAsync.md)

- Retrieve a client for the versions of this Actor.

  ***

  #### Returns [ActorVersionCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionCollectionClientAsync.md)

### [**](#webhooks)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor.py#L917)webhooks

* ****webhooks**(): [WebhookCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md)

- Retrieve a client for webhooks associated with this Actor.

  ***

  #### Returns [WebhookCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md)

## Properties<!-- -->[**](#Properties)

### [**](#http_client)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L94)http\_client

**http\_client: [HTTPClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClient.md) | [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)

Inherited from [BaseClientAsync.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClientAsync.md#http_client)

Overrides [\_BaseBaseClient.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#http_client)

### [**](#params)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L17)params

**params: dict

Inherited from [\_BaseBaseClient.params](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#params)

### [**](#resource_id)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L15)resource\_id

**resource\_id: str | None

Inherited from [\_BaseBaseClient.resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#resource_id)

### [**](#root_client)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L95)root\_client

**root\_client: [ApifyClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClient.md) | [ApifyClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md)

Inherited from [BaseClientAsync.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClientAsync.md#root_client)

Overrides [\_BaseBaseClient.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#root_client)

### [**](#url)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L16)url

**url: str

Inherited from [\_BaseBaseClient.url](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#url)
