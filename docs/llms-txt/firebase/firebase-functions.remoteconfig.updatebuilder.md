# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.updatebuilder.md.txt

# remoteConfig.UpdateBuilder class

Builder used to create Cloud Functions for Remote Config.

**Signature:**  

    export declare class UpdateBuilder 

## Methods

|                                                                            Method                                                                            | Modifiers |                                  Description                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------|
| [onUpdate(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.updatebuilder.md#remoteconfigupdatebuilderonupdate) |           | Handle all updates (including rollbacks) that affect a Remote Config project. |

## remoteConfig.UpdateBuilder.onUpdate()

Handle all updates (including rollbacks) that affect a Remote Config project.

**Signature:**  

    onUpdate(handler: (version: TemplateVersion, context: EventContext) => PromiseLike<any> | any): CloudFunction<TemplateVersion>;

### Parameters

| Parameter |                                                                                                                                                                        Type                                                                                                                                                                        |                                        Description                                        |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| handler   | (version: [TemplateVersion](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversion_interface), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any | A function that takes the updated Remote Config template version metadata as an argument. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[TemplateVersion](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversion_interface)\>