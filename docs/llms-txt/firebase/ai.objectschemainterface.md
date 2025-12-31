# Source: https://firebase.google.com/docs/reference/js/ai.objectschemainterface.md.txt

# ObjectSchemaInterface interface

Interface for [ObjectSchema](https://firebase.google.com/docs/reference/js/ai.objectschema.md#objectschema_class) class.

**Signature:**  

    export interface ObjectSchemaInterface extends SchemaInterface 

**Extends:** [SchemaInterface](https://firebase.google.com/docs/reference/js/ai.schemainterface.md#schemainterface_interface)

## Properties

|                                                                Property                                                                 |                                                 Type                                                 | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------|
| [optionalProperties](https://firebase.google.com/docs/reference/js/ai.objectschemainterface.md#objectschemainterfaceoptionalproperties) | string\[\]                                                                                           |             |
| [type](https://firebase.google.com/docs/reference/js/ai.objectschemainterface.md#objectschemainterfacetype)                             | [SchemaType.OBJECT](https://firebase.google.com/docs/reference/js/ai.md#schematypeobject_enummember) |             |

## ObjectSchemaInterface.optionalProperties

**Signature:**  

    optionalProperties?: string[];

## ObjectSchemaInterface.type

**Signature:**  

    type: SchemaType.OBJECT;