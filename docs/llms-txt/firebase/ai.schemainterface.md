# Source: https://firebase.google.com/docs/reference/js/ai.schemainterface.md.txt

# SchemaInterface interface

Interface for [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class) class.

**Signature:**  

    export interface SchemaInterface extends SchemaShared<SchemaInterface> 

**Extends:** [SchemaShared](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemashared_interface)\<[SchemaInterface](https://firebase.google.com/docs/reference/js/ai.schemainterface.md#schemainterface_interface)\>

## Properties

|                                            Property                                             |                                     Type                                     |                                                                                                           Description                                                                                                            |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [type](https://firebase.google.com/docs/reference/js/ai.schemainterface.md#schemainterfacetype) | [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) | The type of the property. this can only be undefined when using `anyof` schemas, which do not have an explicit type in the [OpenAPI Specification](https://swagger.io/docs/specification/v3_0/data-models/data-types/#any-type). |

## SchemaInterface.type

The type of the property. this can only be undefined when using `anyof` schemas, which do not have an explicit type in the [OpenAPI Specification](https://swagger.io/docs/specification/v3_0/data-models/data-types/#any-type).

**Signature:**  

    type?: SchemaType;