# Source: https://firebase.google.com/docs/reference/js/ai.schemashared.md.txt

# SchemaShared interface

Basic [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class) properties shared across several Schema-related types.

**Signature:**  

    export interface SchemaShared<T> 

## Properties

|                                                     Property                                                      |         Type          |                                                                                                                              Description                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [anyOf](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharedanyof)                       | T\[\]                 | An array of [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class). The generated data must be valid against any of the schemas listed in this array. This allows specifying multiple possible structures or types for a single field.      |
| [description](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemashareddescription)           | string                | Optional. The description of the property.                                                                                                                                                                                                                             |
| [enum](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharedenum)                         | string\[\]            | Optional. The enum of the property.                                                                                                                                                                                                                                    |
| [example](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharedexample)                   | unknown               | Optional. The example of the property.                                                                                                                                                                                                                                 |
| [format](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharedformat)                     | string                | Optional. The format of the property. When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)), this must be either `'enum'` or `'date-time'`, otherwise requests will fail. |
| [items](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemashareditems)                       | T                     | Optional. The items of the property.                                                                                                                                                                                                                                   |
| [maximum](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharedmaximum)                   | number                | The maximum value of a numeric type.                                                                                                                                                                                                                                   |
| [maxItems](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharedmaxitems)                 | number                | The maximum number of items (elements) in a schema of [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) `array`.                                                                                                                            |
| [minimum](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharedminimum)                   | number                | The minimum value of a numeric type.                                                                                                                                                                                                                                   |
| [minItems](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharedminitems)                 | number                | The minimum number of items (elements) in a schema of [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) `array`.                                                                                                                            |
| [nullable](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharednullable)                 | boolean               | Optional. Whether the property is nullable.                                                                                                                                                                                                                            |
| [properties](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharedproperties)             | { \[k: string\]: T; } | Optional. Map of `Schema` objects.                                                                                                                                                                                                                                     |
| [propertyOrdering](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharedpropertyordering) | string\[\]            | A hint suggesting the order in which the keys should appear in the generated JSON string.                                                                                                                                                                              |
| [title](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemasharedtitle)                       | string                | The title of the property. This helps document the schema's purpose but does not typically constrain the generated value. It can subtly guide the model by clarifying the intent of a field.                                                                           |

## SchemaShared.anyOf

An array of [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class). The generated data must be valid against any of the schemas listed in this array. This allows specifying multiple possible structures or types for a single field.

**Signature:**  

    anyOf?: T[];

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

Optional. The format of the property. When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)), this must be either `'enum'` or `'date-time'`, otherwise requests will fail.

**Signature:**  

    format?: string;

## SchemaShared.items

Optional. The items of the property.

**Signature:**  

    items?: T;

## SchemaShared.maximum

The maximum value of a numeric type.

**Signature:**  

    maximum?: number;

## SchemaShared.maxItems

The maximum number of items (elements) in a schema of [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) `array`.

**Signature:**  

    maxItems?: number;

## SchemaShared.minimum

The minimum value of a numeric type.

**Signature:**  

    minimum?: number;

## SchemaShared.minItems

The minimum number of items (elements) in a schema of [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) `array`.

**Signature:**  

    minItems?: number;

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

## SchemaShared.propertyOrdering

A hint suggesting the order in which the keys should appear in the generated JSON string.

**Signature:**  

    propertyOrdering?: string[];

## SchemaShared.title

The title of the property. This helps document the schema's purpose but does not typically constrain the generated value. It can subtly guide the model by clarifying the intent of a field.

**Signature:**  

    title?: string;