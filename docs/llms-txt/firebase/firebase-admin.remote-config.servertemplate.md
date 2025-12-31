# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md.txt

# ServerTemplate interface

Represents a stateful abstraction for a Remote Config server template.

**Signature:**  

    export interface ServerTemplate 

## Methods

|                                                                      Method                                                                      |                                                                                                           Description                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [evaluate(context)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplateevaluate) | Evaluates the current template to produce a [ServerConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.serverconfig.md#serverconfig_interface).                                          |
| [load()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplateload)                | Fetches and caches the current active version of the project's [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface).                 |
| [set(template)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplateset)          | Sets and caches a [ServerTemplateData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedata_interface) or a JSON string representing the server template |
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplatetojson)            | Returns a JSON representation of [ServerTemplateData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedata_interface)                                    |

## ServerTemplate.evaluate()

Evaluates the current template to produce a [ServerConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.serverconfig.md#serverconfig_interface).

**Signature:**  

    evaluate(context?: EvaluationContext): ServerConfig;

### Parameters

| Parameter |                                                             Type                                                             | Description |
|-----------|------------------------------------------------------------------------------------------------------------------------------|-------------|
| context   | [EvaluationContext](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#evaluationcontext) |             |

**Returns:**

[ServerConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.serverconfig.md#serverconfig_interface)

## ServerTemplate.load()

Fetches and caches the current active version of the project's [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface).

**Signature:**  

    load(): Promise<void>;

**Returns:**

Promise\<void\>

## ServerTemplate.set()

Sets and caches a [ServerTemplateData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedata_interface) or a JSON string representing the server template

**Signature:**  

    set(template: ServerTemplateDataType): void;

### Parameters

| Parameter |                                                                  Type                                                                  | Description |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------|-------------|
| template  | [ServerTemplateDataType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#servertemplatedatatype) |             |

**Returns:**

void

## ServerTemplate.toJSON()

Returns a JSON representation of [ServerTemplateData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedata_interface)

**Signature:**  

    toJSON(): ServerTemplateData;

**Returns:**

[ServerTemplateData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedata_interface)