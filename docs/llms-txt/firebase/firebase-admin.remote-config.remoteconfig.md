# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md.txt

# RemoteConfig class

The Firebase `RemoteConfig` service interface.

**Signature:**  

    export declare class RemoteConfig 

## Properties

|                                                         Property                                                          | Modifiers | Type | Description |
|---------------------------------------------------------------------------------------------------------------------------|-----------|------|-------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfigapp) |           | App  |             |

## Methods

|                                                                                   Method                                                                                   | Modifiers |                                                                                                                                                                 Description                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [createTemplateFromJSON(json)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfigcreatetemplatefromjson)      |           | Creates and returns a new Remote Config template from a JSON string.                                                                                                                                                                                                                                                                        |
| [getServerTemplate(options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfiggetservertemplate)             |           | Instantiates [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface) and then fetches and caches the latest template version of the project.                                                                                                        |
| [getTemplate()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfiggettemplate)                                |           | Gets the current active version of the [RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface) of the project.                                                                                                                    |
| [getTemplateAtVersion(versionNumber)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfiggettemplateatversion) |           | Gets the requested version of the [RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface) of the project.                                                                                                                         |
| [initServerTemplate(options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfiginitservertemplate)           |           | Synchronously instantiates [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface).                                                                                                                                                                 |
| [listVersions(options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfiglistversions)                       |           | Gets a list of Remote Config template versions that have been published, sorted in reverse chronological order. Only the last 300 versions are stored. All versions that correspond to non-active Remote Config templates (i.e., all except the template that is being fetched by clients) are also deleted if they are older than 90 days. |
| [publishTemplate(template, options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfigpublishtemplate)       |           | Publishes a Remote Config template.                                                                                                                                                                                                                                                                                                         |
| [rollback(versionNumber)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfigrollback)                         |           | Rolls back a project's published Remote Config template to the specified version. A rollback is equivalent to getting a previously published Remote Config template and re-publishing it using a force update.                                                                                                                              |
| [validateTemplate(template)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfigvalidatetemplate)              |           | Validates a [RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface).                                                                                                                                                              |

## RemoteConfig.app

**Signature:**  

    readonly app: App;

## RemoteConfig.createTemplateFromJSON()

Creates and returns a new Remote Config template from a JSON string.

**Signature:**  

    createTemplateFromJSON(json: string): RemoteConfigTemplate;

### Parameters

| Parameter |  Type  |                      Description                      |
|-----------|--------|-------------------------------------------------------|
| json      | string | The JSON string to populate a Remote Config template. |

**Returns:**

[RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface)

A new template instance.

## RemoteConfig.getServerTemplate()

Instantiates [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface) and then fetches and caches the latest template version of the project.

**Signature:**  

    getServerTemplate(options?: GetServerTemplateOptions): Promise<ServerTemplate>;

### Parameters

| Parameter |                                                                                     Type                                                                                      | Description |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| options   | [GetServerTemplateOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.getservertemplateoptions.md#getservertemplateoptions_interface) |             |

**Returns:**

Promise\<[ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface)\>

## RemoteConfig.getTemplate()

Gets the current active version of the [RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface) of the project.

**Signature:**  

    getTemplate(): Promise<RemoteConfigTemplate>;

**Returns:**

Promise\<[RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface)\>

A promise that fulfills with a `RemoteConfigTemplate`.

## RemoteConfig.getTemplateAtVersion()

Gets the requested version of the [RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface) of the project.

**Signature:**  

    getTemplateAtVersion(versionNumber: number | string): Promise<RemoteConfigTemplate>;

### Parameters

|   Parameter   |       Type       |                       Description                        |
|---------------|------------------|----------------------------------------------------------|
| versionNumber | number \| string | Version number of the Remote Config template to look up. |

**Returns:**

Promise\<[RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface)\>

A promise that fulfills with a `RemoteConfigTemplate`.

## RemoteConfig.initServerTemplate()

Synchronously instantiates [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface).

**Signature:**  

    initServerTemplate(options?: InitServerTemplateOptions): ServerTemplate;

### Parameters

| Parameter |                                                                                       Type                                                                                       | Description |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| options   | [InitServerTemplateOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.initservertemplateoptions.md#initservertemplateoptions_interface) |             |

**Returns:**

[ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface)

## RemoteConfig.listVersions()

Gets a list of Remote Config template versions that have been published, sorted in reverse chronological order. Only the last 300 versions are stored. All versions that correspond to non-active Remote Config templates (i.e., all except the template that is being fetched by clients) are also deleted if they are older than 90 days.

**Signature:**  

    listVersions(options?: ListVersionsOptions): Promise<ListVersionsResult>;

### Parameters

| Parameter |                                                                              Type                                                                              |                       Description                       |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| options   | [ListVersionsOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsoptions.md#listversionsoptions_interface) | Optional options object for getting a list of versions. |

**Returns:**

Promise\<[ListVersionsResult](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsresult.md#listversionsresult_interface)\>

A promise that fulfills with a `ListVersionsResult`.

## RemoteConfig.publishTemplate()

Publishes a Remote Config template.

**Signature:**  

    publishTemplate(template: RemoteConfigTemplate, options?: {
            force: boolean;
        }): Promise<RemoteConfigTemplate>;

### Parameters

| Parameter |                                                                               Type                                                                                |                                                                                                                                                                                                                                        Description                                                                                                                                                                                                                                        |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| template  | [RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface) | The Remote Config template to be published.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| options   | { force: boolean; }                                                                                                                                               | Optional options object when publishing a Remote Config template: - `force`: Setting this to `true` forces the Remote Config template to be updated and circumvent the ETag. This approach is not recommended because it risks causing the loss of updates to your Remote Config template if multiple clients are updating the Remote Config template. See [ETag usage and forced updates](https://firebase.google.com/docs/remote-config/use-config-rest#etag_usage_and_forced_updates). |

**Returns:**

Promise\<[RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface)\>

A Promise that fulfills with the published `RemoteConfigTemplate`.

## RemoteConfig.rollback()

Rolls back a project's published Remote Config template to the specified version. A rollback is equivalent to getting a previously published Remote Config template and re-publishing it using a force update.

**Signature:**  

    rollback(versionNumber: number | string): Promise<RemoteConfigTemplate>;

### Parameters

|   Parameter   |       Type       |                                                                                                                                                                                                         Description                                                                                                                                                                                                         |
|---------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| versionNumber | number \| string | The version number of the Remote Config template to roll back to. The specified version number must be lower than the current version number, and not have been deleted due to staleness. Only the last 300 versions are stored. All versions that correspond to non-active Remote Config templates (that is, all except the template that is being fetched by clients) are also deleted if they are more than 90 days old. |

**Returns:**

Promise\<[RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface)\>

A promise that fulfills with the published `RemoteConfigTemplate`.

## RemoteConfig.validateTemplate()

Validates a [RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface).

**Signature:**  

    validateTemplate(template: RemoteConfigTemplate): Promise<RemoteConfigTemplate>;

### Parameters

| Parameter |                                                                               Type                                                                                |                 Description                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| template  | [RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface) | The Remote Config template to be validated. |

**Returns:**

Promise\<[RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface)\>

A promise that fulfills with the validated `RemoteConfigTemplate`.