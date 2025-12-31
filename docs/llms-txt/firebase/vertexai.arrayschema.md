# Source: https://firebase.google.com/docs/reference/js/vertexai.arrayschema.md.txt

# ArraySchema class

Schema class for "array" types. The `items` param should refer to the type of item that can be a member of the array.

**Signature:**  

    export declare class ArraySchema extends Schema 

**Extends:** [Schema](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schema_class)

## Constructors

|                                                            Constructor                                                             | Modifiers |                     Description                      |
|------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------|
| [(constructor)(schemaParams, items)](https://firebase.google.com/docs/reference/js/vertexai.arrayschema.md#arrayschemaconstructor) |           | Constructs a new instance of the `ArraySchema` class |

## Properties

|                                            Property                                             | Modifiers |                                         Type                                         | Description |
|-------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------|-------------|
| [items](https://firebase.google.com/docs/reference/js/vertexai.arrayschema.md#arrayschemaitems) |           | [TypedSchema](https://firebase.google.com/docs/reference/js/vertexai.md#typedschema) |             |

## ArraySchema.(constructor)

Constructs a new instance of the `ArraySchema` class

**Signature:**  

    constructor(schemaParams: SchemaParams, items: TypedSchema);

#### Parameters

|  Parameter   |                                                     Type                                                      | Description |
|--------------|---------------------------------------------------------------------------------------------------------------|-------------|
| schemaParams | [SchemaParams](https://firebase.google.com/docs/reference/js/vertexai.schemaparams.md#schemaparams_interface) |             |
| items        | [TypedSchema](https://firebase.google.com/docs/reference/js/vertexai.md#typedschema)                          |             |

## ArraySchema.items

**Signature:**  

    items: TypedSchema;