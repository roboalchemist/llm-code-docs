# Source: https://firebase.google.com/docs/reference/js/ai.objectschemarequest.md.txt

# ObjectSchemaRequest interface

Interface for JSON parameters in a schema of [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) "object" when not using the `Schema.object()` helper.

**Signature:**  

    export interface ObjectSchemaRequest extends SchemaRequest 

**Extends:** [SchemaRequest](https://firebase.google.com/docs/reference/js/ai.schemarequest.md#schemarequest_interface)

## Properties

|                                                              Property                                                               |   Type   |                                                                                                                                                    Description                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [optionalProperties](https://firebase.google.com/docs/reference/js/ai.objectschemarequest.md#objectschemarequestoptionalproperties) | never    | This is not a property accepted in the final request to the backend, but is a client-side convenience property that is only usable by constructing a schema through the `Schema.object()` helper method. Populating this property will cause response errors if the object is not wrapped with `Schema.object()`. |
| [type](https://firebase.google.com/docs/reference/js/ai.objectschemarequest.md#objectschemarequesttype)                             | 'object' |                                                                                                                                                                                                                                                                                                                   |

## ObjectSchemaRequest.optionalProperties

This is not a property accepted in the final request to the backend, but is a client-side convenience property that is only usable by constructing a schema through the `Schema.object()` helper method. Populating this property will cause response errors if the object is not wrapped with `Schema.object()`.

**Signature:**  

    optionalProperties?: never;

## ObjectSchemaRequest.type

**Signature:**  

    type: 'object';