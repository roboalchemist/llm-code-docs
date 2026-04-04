# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.md.txt

# remoteConfig namespace

## Functions

| Function | Description |
|---|---|
| [onUpdate(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.md#remoteconfigonupdate) | Registers a function that triggers on Firebase Remote Config template update events. |

## Classes

| Class | Description |
|---|---|
| [UpdateBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.updatebuilder.md#remoteconfigupdatebuilder_class) | Builder used to create Cloud Functions for Remote Config. |

## Interfaces

| Interface | Description |
|---|---|
| [RemoteConfigUser](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.remoteconfiguser.md#remoteconfigremoteconfiguser_interface) | An interface representing metadata for a Remote Config account that performed the update. Contains the same fields as \[`RemoteConfigUser`\](/docs/reference/remote-config/rest/v1/Version#remoteconfiguser). |
| [TemplateVersion](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversion_interface) | An interface representing a Remote Config template version metadata object emitted when a project is updated. |

## remoteConfig.onUpdate()

Registers a function that triggers on Firebase Remote Config template update events.

**Signature:**

    export declare function onUpdate(handler: (version: TemplateVersion, context: EventContext) => PromiseLike<any> | any): CloudFunction<TemplateVersion>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| handler | (version: [TemplateVersion](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversion_interface), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any | A function that takes the updated Remote Config template version metadata as an argument. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[TemplateVersion](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversion_interface)\>

A function that you can export and deploy.