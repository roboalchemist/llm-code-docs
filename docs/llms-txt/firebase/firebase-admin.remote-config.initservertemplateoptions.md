# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.initservertemplateoptions.md.txt

# InitServerTemplateOptions interface

Represents optional arguments that can be used when instantiating [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface) synchronously.

**Signature:**  

    export interface InitServerTemplateOptions extends GetServerTemplateOptions 

**Extends:** [GetServerTemplateOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.getservertemplateoptions.md#getservertemplateoptions_interface)

## Properties

|                                                                           Property                                                                            |                                                                  Type                                                                  |                                                                                                             Description                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [template](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.initservertemplateoptions.md#initservertemplateoptionstemplate) | [ServerTemplateDataType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#servertemplatedatatype) | Enables integrations to use template data loaded independently. For example, customers can reduce initialization latency by pre-fetching and caching template data and then using this option to initialize the SDK with that data. |

## InitServerTemplateOptions.template

Enables integrations to use template data loaded independently. For example, customers can reduce initialization latency by pre-fetching and caching template data and then using this option to initialize the SDK with that data.

**Signature:**  

    template?: ServerTemplateDataType;