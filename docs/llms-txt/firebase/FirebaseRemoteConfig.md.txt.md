# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig.md.txt

# FirebaseRemoteConfig

public final class **FirebaseRemoteConfig** extends Object  
This class is the entry point for all server-side Firebase Remote Config actions.

You can get an instance of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig` via `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getInstance(com.google.firebase.FirebaseApp)`,
and then use it to manage Remote Config templates.

### Public Method Summary

|---|---|
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) | [forcePublishTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#forcePublishTemplate(com.google.firebase.remoteconfig.Template))([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template) Force publishes a Remote Config template. |
| ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\> | [forcePublishTemplateAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#forcePublishTemplateAsync(com.google.firebase.remoteconfig.Template))([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#forcePublishTemplate(com.google.firebase.remoteconfig.Template)` but performs the operation asynchronously. |
| static [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getInstance())() Gets the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance for the default `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`. |
| synchronized static [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getInstance(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app) Gets the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance for the specified `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`. |
| [ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate) | [getServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getServerTemplate())() Initializes a template instance without any defaults and loads the latest template data. |
| [ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate) | [getServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getServerTemplate(com.google.firebase.remoteconfig.KeysAndValues))([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) defaultConfig) Initializes a template instance and loads the latest template data. |
| ApiFuture\<[ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate)\> | [getServerTemplateAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getServerTemplateAsync())() Initializes a template instance without any defaults and asynchronously loads the latest template data. |
| ApiFuture\<[ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate)\> | [getServerTemplateAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getServerTemplateAsync(com.google.firebase.remoteconfig.KeysAndValues))([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) defaultConfig) Initializes a template instance and asynchronously loads the latest template data. |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) | [getTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplate())() Gets the current active version of the Remote Config template. |
| ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\> | [getTemplateAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplateAsync())() Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplate()` but performs the operation asynchronously. |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) | [getTemplateAtVersion](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplateAtVersion(java.lang.String))(String versionNumber) Gets the requested version of the of the Remote Config template. |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) | [getTemplateAtVersion](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplateAtVersion(long))(long versionNumber) Gets the requested version of the of the Remote Config template. |
| ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\> | [getTemplateAtVersionAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplateAtVersionAsync(long))(long versionNumber) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplateAtVersion(long)` but performs the operation asynchronously. |
| ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\> | [getTemplateAtVersionAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplateAtVersionAsync(java.lang.String))(String versionNumber) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplateAtVersion(java.lang.String)` but performs the operation asynchronously. |
| [ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage) | [listVersions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#listVersions())() Gets a list of Remote Config template versions that have been published, sorted in reverse chronological order. |
| [ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage) | [listVersions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#listVersions(com.google.firebase.remoteconfig.ListVersionsOptions))([ListVersionsOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions) options) Gets a list of Remote Config template versions that have been published, sorted in reverse chronological order. |
| ApiFuture\<[ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage)\> | [listVersionsAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#listVersionsAsync(com.google.firebase.remoteconfig.ListVersionsOptions))([ListVersionsOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions) options) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#listVersions(com.google.firebase.remoteconfig.ListVersionsOptions)` but performs the operation asynchronously. |
| ApiFuture\<[ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage)\> | [listVersionsAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#listVersionsAsync())() Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#listVersions()` but performs the operation asynchronously. |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) | [publishTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#publishTemplate(com.google.firebase.remoteconfig.Template))([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template) Publishes a Remote Config template. |
| ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\> | [publishTemplateAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#publishTemplateAsync(com.google.firebase.remoteconfig.Template))([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#publishTemplate(com.google.firebase.remoteconfig.Template)` but performs the operation asynchronously. |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) | [rollback](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#rollback(long))(long versionNumber) Rolls back a project's published Remote Config template to the specified version. |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) | [rollback](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#rollback(java.lang.String))(String versionNumber) Rolls back a project's published Remote Config template to the specified version. |
| ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\> | [rollbackAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#rollbackAsync(long))(long versionNumber) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#rollback(long)` but performs the operation asynchronously. |
| ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\> | [rollbackAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#rollbackAsync(java.lang.String))(String versionNumber) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#rollback(java.lang.String)` but performs the operation asynchronously. |
| [ServerTemplateImpl.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder) | [serverTemplateBuilder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#serverTemplateBuilder())() Alternative to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getServerTemplate()` where developers can initialize with a pre-cached template or config. |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) | [validateTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#validateTemplate(com.google.firebase.remoteconfig.Template))([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template) Validates a Remote Config template. |
| ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\> | [validateTemplateAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#validateTemplateAsync(com.google.firebase.remoteconfig.Template))([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#validateTemplate(com.google.firebase.remoteconfig.Template)` but performs the operation asynchronously. |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Methods

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**forcePublishTemplate**
([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template)

Force publishes a Remote Config template.

This method forces the Remote Config template to be updated without evaluating the ETag
values. This approach is not recommended because it risks causing the loss of updates to your
Remote Config template if multiple clients are updating the Remote Config template.
See [ETag usage and forced updates](https://firebase.google.com/docs/remote-config/use-config-rest#etag_usage_and_forced_updates).

##### Parameters

| template | The Remote Config template to be forcefully published. |
|---|---|

##### Returns

- The published `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | If an error occurs while publishing the template. |
|---|---|

#### public ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\>
**forcePublishTemplateAsync**
([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#forcePublishTemplate(com.google.firebase.remoteconfig.Template)` but performs the operation
asynchronously.

##### Parameters

| template | The Remote Config template to be forcefully published. |
|---|---|

##### Returns

- An `ApiFuture` that completes with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` when the provided template is published.

#### public static [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig)
**getInstance**
()

Gets the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance for the default `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`.

##### Returns

- The `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance for the default `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`.

#### public static synchronized [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig)
**getInstance**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app)

Gets the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance for the specified `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`.

##### Returns

- The `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance for the specified `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`.

#### public [ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate)
**getServerTemplate**
()

Initializes a template instance without any defaults and loads the latest template data.

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` instance with the latest template data.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |   |
|---|---|

#### public [ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate)
**getServerTemplate**
([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) defaultConfig)

Initializes a template instance and loads the latest template data.

##### Parameters

| defaultConfig | Default parameter values to use if a getter references a parameter not found in the template. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` instance with the latest template data.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |   |
|---|---|

#### public ApiFuture\<[ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate)\>
**getServerTemplateAsync**
()

Initializes a template instance without any defaults and asynchronously loads the latest
template data.

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` instance with the latest template data.

#### public ApiFuture\<[ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate)\>
**getServerTemplateAsync**
([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) defaultConfig)

Initializes a template instance and asynchronously loads the latest template data.

##### Parameters

| defaultConfig | Default parameter values to use if a getter references a parameter not found in the template. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` instance with the latest template data.

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**getTemplate**
()

Gets the current active version of the Remote Config template.

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | If an error occurs while getting the template. |
|---|---|

#### public ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\>
**getTemplateAsync**
()

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplate()` but performs the operation asynchronously.

##### Returns

- An `ApiFuture` that completes with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` when the template is available.

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**getTemplateAtVersion**
(String versionNumber)

Gets the requested version of the of the Remote Config template.

##### Parameters

| versionNumber | The version number of the Remote Config template to get. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | If an error occurs while getting the template. |
|---|---|

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**getTemplateAtVersion**
(long versionNumber)

Gets the requested version of the of the Remote Config template.

##### Parameters

| versionNumber | The version number of the Remote Config template to get. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | If an error occurs while getting the template. |
|---|---|

#### public ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\>
**getTemplateAtVersionAsync**
(long versionNumber)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplateAtVersion(long)` but performs the operation
asynchronously.

##### Parameters

| versionNumber | The version number of the Remote Config template to get. |
|---|---|

##### Returns

- An `ApiFuture` that completes with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` when the requested template is available.

#### public ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\>
**getTemplateAtVersionAsync**
(String versionNumber)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getTemplateAtVersion(java.lang.String)` but performs the operation
asynchronously.

##### Parameters

| versionNumber | The version number of the Remote Config template to get. |
|---|---|

##### Returns

- An `ApiFuture` that completes with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` when the requested template is available.

#### public [ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage)
**listVersions**
()

Gets a list of Remote Config template versions that have been published, sorted in reverse
chronological order. Only the last 300 versions are stored.

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage` instance.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | If an error occurs while retrieving versions list. |
|---|---|

#### public [ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage)
**listVersions**
([ListVersionsOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions) options)

Gets a list of Remote Config template versions that have been published, sorted in reverse
chronological order. Only the last 300 versions are stored.

##### Parameters

| options | List version options. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage` instance.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | If an error occurs while retrieving versions list. |
|---|---|

#### public ApiFuture\<[ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage)\>
**listVersionsAsync**
([ListVersionsOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions) options)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#listVersions(com.google.firebase.remoteconfig.ListVersionsOptions)` but performs the operation
asynchronously.

##### Parameters

| options | List version options. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage` instance.

#### public ApiFuture\<[ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage)\>
**listVersionsAsync**
()

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#listVersions()` but performs the operation
asynchronously.

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage` instance.

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**publishTemplate**
([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template)

Publishes a Remote Config template.

##### Parameters

| template | The Remote Config template to be published. |
|---|---|

##### Returns

- The published `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | If an error occurs while publishing the template. |
|---|---|

#### public ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\>
**publishTemplateAsync**
([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#publishTemplate(com.google.firebase.remoteconfig.Template)` but performs the operation
asynchronously.

##### Parameters

| template | The Remote Config template to be published. |
|---|---|

##### Returns

- An `ApiFuture` that completes with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` when the provided template is published.

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**rollback**
(long versionNumber)

Rolls back a project's published Remote Config template to the specified version.

A rollback is equivalent to getting a previously published Remote Config
template and re-publishing it using a force update.

##### Parameters

| versionNumber | The version number of the Remote Config template to roll back to. The specified version number must be lower than the current version number, and not have been deleted due to staleness. Only the last 300 versions are stored. All versions that correspond to non-active Remote Config templates (that is, all except the template that is being fetched by clients) are also deleted if they are more than 90 days old. |
|---|---|

##### Returns

- The rolled back `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | If an error occurs while rolling back the template. |
|---|---|

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**rollback**
(String versionNumber)

Rolls back a project's published Remote Config template to the specified version.

A rollback is equivalent to getting a previously published Remote Config
template and re-publishing it using a force update.

##### Parameters

| versionNumber | The version number of the Remote Config template to roll back to. The specified version number must be lower than the current version number, and not have been deleted due to staleness. Only the last 300 versions are stored. All versions that correspond to non-active Remote Config templates (that is, all except the template that is being fetched by clients) are also deleted if they are more than 90 days old. |
|---|---|

##### Returns

- The rolled back `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | If an error occurs while rolling back the template. |
|---|---|

#### public ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\>
**rollbackAsync**
(long versionNumber)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#rollback(long)` but performs the operation
asynchronously.

##### Parameters

| versionNumber | The version number of the Remote Config template to roll back to. |
|---|---|

##### Returns

- An `ApiFuture` that completes with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` once the rollback operation is successful.

#### public ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\>
**rollbackAsync**
(String versionNumber)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#rollback(java.lang.String)` but performs the operation
asynchronously.

##### Parameters

| versionNumber | The version number of the Remote Config template to roll back to. |
|---|---|

##### Returns

- An `ApiFuture` that completes with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` once the rollback operation is successful.

#### public [ServerTemplateImpl.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder)
**serverTemplateBuilder**
()

Alternative to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getServerTemplate()` where developers can initialize with a pre-cached
template or config.

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**validateTemplate**
([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template)

Validates a Remote Config template.

##### Parameters

| template | The Remote Config template to be validated. |
|---|---|

##### Returns

- The validated `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | If an error occurs while validating the template. |
|---|---|

#### public ApiFuture\<[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)\>
**validateTemplateAsync**
([Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) template)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig#validateTemplate(com.google.firebase.remoteconfig.Template)` but performs the operation
asynchronously.

##### Parameters

| template | The Remote Config template to be validated. |
|---|---|

##### Returns

- An `ApiFuture` that completes with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template` when the provided template is validated.