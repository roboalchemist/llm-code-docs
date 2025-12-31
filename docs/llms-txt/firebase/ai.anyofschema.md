# Source: https://firebase.google.com/docs/reference/js/ai.anyofschema.md.txt

# AnyOfSchema class

Schema class representing a value that can conform to any of the provided sub-schemas. This is useful when a field can accept multiple distinct types or structures.

**Signature:**  

    export declare class AnyOfSchema extends Schema 

**Extends:** [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class)

## Constructors

|                                                      Constructor                                                      | Modifiers |                     Description                      |
|-----------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------|
| [(constructor)(schemaParams)](https://firebase.google.com/docs/reference/js/ai.anyofschema.md#anyofschemaconstructor) |           | Constructs a new instance of the `AnyOfSchema` class |

## Properties

|                                         Property                                          | Modifiers |                                        Type                                        | Description |
|-------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------|-------------|
| [anyOf](https://firebase.google.com/docs/reference/js/ai.anyofschema.md#anyofschemaanyof) |           | [TypedSchema](https://firebase.google.com/docs/reference/js/ai.md#typedschema)\[\] |             |

## AnyOfSchema.(constructor)

Constructs a new instance of the `AnyOfSchema` class

**Signature:**  

    constructor(schemaParams: SchemaParams & {
            anyOf: TypedSchema[];
        });

#### Parameters

|  Parameter   |                                                                                                   Type                                                                                                    | Description |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| schemaParams | [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) \& { anyOf: [TypedSchema](https://firebase.google.com/docs/reference/js/ai.md#typedschema)\[\]; } |             |

## AnyOfSchema.anyOf

**Signature:**  

    anyOf: TypedSchema[];