# Source: https://firebase.google.com/docs/reference/js/ai.schemarequest.md.txt

# SchemaRequest interface

Final format for [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class) params passed to backend requests.

**Signature:**  

    export interface SchemaRequest extends SchemaShared<SchemaRequest> 

**Extends:** [SchemaShared](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemashared_interface)\<[SchemaRequest](https://firebase.google.com/docs/reference/js/ai.schemarequest.md#schemarequest_interface)\>

## Properties

|                                              Property                                               |                                     Type                                     |                                                                                                           Description                                                                                                            |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [required](https://firebase.google.com/docs/reference/js/ai.schemarequest.md#schemarequestrequired) | string\[\]                                                                   | Optional. Array of required property.                                                                                                                                                                                            |
| [type](https://firebase.google.com/docs/reference/js/ai.schemarequest.md#schemarequesttype)         | [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) | The type of the property. this can only be undefined when using `anyOf` schemas, which do not have an explicit type in the [OpenAPI specification](https://swagger.io/docs/specification/v3_0/data-models/data-types/#any-type). |

## SchemaRequest.required

Optional. Array of required property.

**Signature:**  

    required?: string[];

## SchemaRequest.type

The type of the property. this can only be undefined when using `anyOf` schemas, which do not have an explicit type in the [OpenAPI specification](https://swagger.io/docs/specification/v3_0/data-models/data-types/#any-type).

**Signature:**  

    type?: SchemaType;