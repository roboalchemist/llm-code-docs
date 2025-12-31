# Source: https://firebase.google.com/docs/reference/js/vertexai.objectschemainterface.md.txt

# ObjectSchemaInterface interface

Interface for [ObjectSchema](https://firebase.google.com/docs/reference/js/vertexai.objectschema.md#objectschema_class) class.

**Signature:**  

    export interface ObjectSchemaInterface extends SchemaInterface 

**Extends:** [SchemaInterface](https://firebase.google.com/docs/reference/js/vertexai.schemainterface.md#schemainterface_interface)

## Properties

|                                                                   Property                                                                    |                                                    Type                                                    | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------|
| [optionalProperties](https://firebase.google.com/docs/reference/js/vertexai.objectschemainterface.md#objectschemainterfaceoptionalproperties) | string\[\]                                                                                                 |             |
| [type](https://firebase.google.com/docs/reference/js/vertexai.objectschemainterface.md#objectschemainterfacetype)                             | [SchemaType.OBJECT](https://firebase.google.com/docs/reference/js/vertexai.md#schematypeobject_enummember) |             |

## ObjectSchemaInterface.optionalProperties

**Signature:**  

    optionalProperties?: string[];

## ObjectSchemaInterface.type

**Signature:**  

    type: SchemaType.OBJECT;