# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.md.txt

# remoteConfig namespace

## Functions

|                                                                              Function                                                                              |                              Description                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [onConfigUpdated(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.md#remoteconfigonconfigupdated)       | Event handler which triggers when data is updated in a Remote Config. |
| [onConfigUpdated(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.md#remoteconfigonconfigupdated) | Event handler which triggers when data is updated in a Remote Config. |

## Interfaces

|                                                                                    Interface                                                                                     |                                          Description                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [ConfigUpdateData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedata_interface) | The data within Firebase Remote Config update events.                                          |
| [ConfigUser](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configuser.md#remoteconfigconfiguser_interface)                   | All the fields associated with the person/service account that wrote a Remote Config template. |

## Type Aliases

|                                                                        Type Alias                                                                         |                                 Description                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [ConfigUpdateOrigin](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.md#remoteconfigconfigupdateorigin) | What type of update was associated with the Remote Config template version. |
| [ConfigUpdateType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.md#remoteconfigconfigupdatetype)     | Where the Remote Config update action originated.                           |

## remoteConfig.onConfigUpdated()

Event handler which triggers when data is updated in a Remote Config.

**Signature:**  

    export declare function onConfigUpdated(handler: (event: CloudEvent<ConfigUpdateData>) => any | Promise<any>): CloudFunction<CloudEvent<ConfigUpdateData>>;

### Parameters

| Parameter |                                                                                                                                                                             Type                                                                                                                                                                             |                             Description                              |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| handler   | (event: [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[ConfigUpdateData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedata_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time a Remote Config update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[ConfigUpdateData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedata_interface)\>\>

A function that you can export and deploy.

## remoteConfig.onConfigUpdated()

Event handler which triggers when data is updated in a Remote Config.

**Signature:**  

    export declare function onConfigUpdated(opts: EventHandlerOptions, handler: (event: CloudEvent<ConfigUpdateData>) => any | Promise<any>): CloudFunction<CloudEvent<ConfigUpdateData>>;

### Parameters

| Parameter |                                                                                                                                                                             Type                                                                                                                                                                             |                             Description                              |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| opts      | [EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)                                                                                                                                                                                             | Options that can be set on an individual event-handling function.    |
| handler   | (event: [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[ConfigUpdateData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedata_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time a Remote Config update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[ConfigUpdateData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedata_interface)\>\>

A function that you can export and deploy.

## remoteConfig.ConfigUpdateOrigin

What type of update was associated with the Remote Config template version.

**Signature:**  

    export type ConfigUpdateOrigin = 
    /** Catch-all for unrecognized values. */
    "REMOTE_CONFIG_UPDATE_ORIGIN_UNSPECIFIED"
    /** The update came from the Firebase UI. */
     | "CONSOLE"
    /** The update came from the Remote Config REST API. */
     | "REST_API"
    /** The update came from the Firebase Admin Node SDK. */
     | "ADMIN_SDK_NODE";

## remoteConfig.ConfigUpdateType

Where the Remote Config update action originated.

**Signature:**  

    export type ConfigUpdateType = 
    /** Catch-all for unrecognized enum values */
    "REMOTE_CONFIG_UPDATE_TYPE_UNSPECIFIED"
    /** A regular incremental update */
     | "INCREMENTAL_UPDATE"
    /** A forced update. The ETag was specified as "*" in an UpdateRemoteConfigRequest request or the "Force Update" button was pressed on the console */
     | "FORCED_UPDATE"
    /** A rollback to a previous Remote Config template */
     | "ROLLBACK";