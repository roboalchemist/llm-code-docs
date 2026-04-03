# Source: https://firebase.google.com/docs/reference/js/vertexai.schemashared.md.txt

# SchemaShared interface

Basic [Schema](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schema_class) properties shared across several Schema-related types.

**Signature:**  

    export interface SchemaShared<T> 

## Properties

|                                                   Property                                                    |         Type          |                                                                                                                                 Description                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [description](https://firebase.google.com/docs/reference/js/vertexai.schemashared.md#schemashareddescription) | string                | Optional. The description of the property.                                                                                                                                                                                                                                   |
| [enum](https://firebase.google.com/docs/reference/js/vertexai.schemashared.md#schemasharedenum)               | string\[\]            | Optional. The enum of the property.                                                                                                                                                                                                                                          |
| [example](https://firebase.google.com/docs/reference/js/vertexai.schemashared.md#schemasharedexample)         | unknown               | Optional. The example of the property.                                                                                                                                                                                                                                       |
| [format](https://firebase.google.com/docs/reference/js/vertexai.schemashared.md#schemasharedformat)           | string                | Optional. The format of the property. When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this must be either `'enum'` or `'date-time'`, otherwise requests will fail. |
| [items](https://firebase.google.com/docs/reference/js/vertexai.schemashared.md#schemashareditems)             | T                     | Optional. The items of the property.                                                                                                                                                                                                                                         |
| [nullable](https://firebase.google.com/docs/reference/js/vertexai.schemashared.md#schemasharednullable)       | boolean               | Optional. Whether the property is nullable.                                                                                                                                                                                                                                  |
| [properties](https://firebase.google.com/docs/reference/js/vertexai.schemashared.md#schemasharedproperties)   | { \[k: string\]: T; } | Optional. Map of `Schema` objects.                                                                                                                                                                                                                                           |

## SchemaShared.description

Optional. The description of the property.

**Signature:**  

    description?: string;

## SchemaShared.enum

Optional. The enum of the property.

**Signature:**  

    enum?: string[];

## SchemaShared.example

Optional. The example of the property.

**Signature:**  

    example?: unknown;

## SchemaShared.format

Optional. The format of the property. When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this must be either `'enum'` or `'date-time'`, otherwise requests will fail.

**Signature:**  

    format?: string;

## SchemaShared.items

Optional. The items of the property.

**Signature:**  

    items?: T;

## SchemaShared.nullable

Optional. Whether the property is nullable.

**Signature:**  

    nullable?: boolean;

## SchemaShared.properties

Optional. Map of `Schema` objects.

**Signature:**  

    properties?: {
            [k: string]: T;
        };