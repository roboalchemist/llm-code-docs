# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.getservertemplateoptions.md.txt

# GetServerTemplateOptions interface

Represents optional arguments that can be used when instantiating [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface).

**Signature:**  

    export interface GetServerTemplateOptions 

## Properties

|                                                                               Property                                                                                |                                                         Type                                                         |                                                                                               Description                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [defaultConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.getservertemplateoptions.md#getservertemplateoptionsdefaultconfig) | [DefaultConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#defaultconfig) | Defines in-app default parameter values, so that your app behaves as intended before it connects to the Remote Config backend, and so that default values are available if none are set on the backend. |

## GetServerTemplateOptions.defaultConfig

Defines in-app default parameter values, so that your app behaves as intended before it connects to the Remote Config backend, and so that default values are available if none are set on the backend.

**Signature:**  

    defaultConfig?: DefaultConfig;