# Source: https://firebase.google.com/docs/reference/js/ai.objectschema.md.txt

# ObjectSchema class

Schema class for "object" types. The `properties` param must be a map of `Schema` objects.

**Signature:**  

    export declare class ObjectSchema extends Schema 

**Extends:** [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class)

## Constructors

|                                                                       Constructor                                                                       | Modifiers |                      Description                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------|
| [(constructor)(schemaParams, properties, optionalProperties)](https://firebase.google.com/docs/reference/js/ai.objectschema.md#objectschemaconstructor) |           | Constructs a new instance of the `ObjectSchema` class |

## Properties

|                                                       Property                                                        | Modifiers |                                                Type                                                | Description |
|-----------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------|-------------|
| [optionalProperties](https://firebase.google.com/docs/reference/js/ai.objectschema.md#objectschemaoptionalproperties) |           | string\[\]                                                                                         |             |
| [properties](https://firebase.google.com/docs/reference/js/ai.objectschema.md#objectschemaproperties)                 |           | { \[k: string\]: [TypedSchema](https://firebase.google.com/docs/reference/js/ai.md#typedschema); } |             |

## ObjectSchema.(constructor)

Constructs a new instance of the `ObjectSchema` class

**Signature:**  

    constructor(schemaParams: SchemaParams, properties: {
            [k: string]: TypedSchema;
        }, optionalProperties?: string[]);

#### Parameters

|     Parameter      |                                                  Type                                                   | Description |
|--------------------|---------------------------------------------------------------------------------------------------------|-------------|
| schemaParams       | [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) |             |
| properties         | { \[k: string\]: [TypedSchema](https://firebase.google.com/docs/reference/js/ai.md#typedschema); }      |             |
| optionalProperties | string\[\]                                                                                              |             |

## ObjectSchema.optionalProperties

**Signature:**  

    optionalProperties: string[];

## ObjectSchema.properties

**Signature:**  

    properties: {
            [k: string]: TypedSchema;
        };