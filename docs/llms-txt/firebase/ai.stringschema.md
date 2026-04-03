# Source: https://firebase.google.com/docs/reference/js/ai.stringschema.md.txt

# StringSchema class

Schema class for "string" types. Can be used with or without enum values.

**Signature:**  

    export declare class StringSchema extends Schema 

**Extends:** [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class)

## Constructors

|                                                             Constructor                                                             | Modifiers |                      Description                      |
|-------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------|
| [(constructor)(schemaParams, enumValues)](https://firebase.google.com/docs/reference/js/ai.stringschema.md#stringschemaconstructor) |           | Constructs a new instance of the `StringSchema` class |

## Properties

|                                         Property                                          | Modifiers |    Type    | Description |
|-------------------------------------------------------------------------------------------|-----------|------------|-------------|
| [enum](https://firebase.google.com/docs/reference/js/ai.stringschema.md#stringschemaenum) |           | string\[\] |             |

## StringSchema.(constructor)

Constructs a new instance of the `StringSchema` class

**Signature:**  

    constructor(schemaParams?: SchemaParams, enumValues?: string[]);

#### Parameters

|  Parameter   |                                                  Type                                                   | Description |
|--------------|---------------------------------------------------------------------------------------------------------|-------------|
| schemaParams | [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) |             |
| enumValues   | string\[\]                                                                                              |             |

## StringSchema.enum

**Signature:**  

    enum?: string[];