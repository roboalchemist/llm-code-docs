# Source: https://firebase.google.com/docs/reference/js/vertexai.schemarequest.md.txt

# SchemaRequest interface

Final format for [Schema](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schema_class) params passed to backend requests.

**Signature:**  

    export interface SchemaRequest extends SchemaShared<SchemaRequest> 

**Extends:** [SchemaShared](https://firebase.google.com/docs/reference/js/vertexai.schemashared.md#schemashared_interface)\<[SchemaRequest](https://firebase.google.com/docs/reference/js/vertexai.schemarequest.md#schemarequest_interface)\>

## Properties

|                                                 Property                                                  |                                        Type                                        |                                                  Description                                                  |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [required](https://firebase.google.com/docs/reference/js/vertexai.schemarequest.md#schemarequestrequired) | string\[\]                                                                         | Optional. Array of required property.                                                                         |
| [type](https://firebase.google.com/docs/reference/js/vertexai.schemarequest.md#schemarequesttype)         | [SchemaType](https://firebase.google.com/docs/reference/js/vertexai.md#schematype) | The type of the property. [SchemaType](https://firebase.google.com/docs/reference/js/vertexai.md#schematype). |

## SchemaRequest.required

Optional. Array of required property.

**Signature:**  

    required?: string[];

## SchemaRequest.type

The type of the property. [SchemaType](https://firebase.google.com/docs/reference/js/vertexai.md#schematype).

**Signature:**  

    type: SchemaType;