# Source: https://firebase.google.com/docs/reference/js/ai.schema.md.txt

# Schema class

Parent class encompassing all Schema types, with static methods that allow building specific Schema types. This class can be converted with `JSON.stringify()` into a JSON string accepted by Vertex AI REST endpoints. (This string conversion is automatically done when calling SDK methods.)

**Signature:**  

    export declare abstract class Schema implements SchemaInterface 

**Implements:** [SchemaInterface](https://firebase.google.com/docs/reference/js/ai.schemainterface.md#schemainterface_interface)

## Constructors

|                                                 Constructor                                                 | Modifiers |                   Description                   |
|-------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------|
| [(constructor)(schemaParams)](https://firebase.google.com/docs/reference/js/ai.schema.md#schemaconstructor) |           | Constructs a new instance of the `Schema` class |

## Properties

|                                          Property                                           | Modifiers |                                                       Type                                                       |                                                                                                                Description                                                                                                                 |
|---------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [description](https://firebase.google.com/docs/reference/js/ai.schema.md#schemadescription) |           | string                                                                                                           | Optional. The description of the property.                                                                                                                                                                                                 |
| [example](https://firebase.google.com/docs/reference/js/ai.schema.md#schemaexample)         |           | unknown                                                                                                          | Optional. The example of the property.                                                                                                                                                                                                     |
| [format](https://firebase.google.com/docs/reference/js/ai.schema.md#schemaformat)           |           | string                                                                                                           | Optional. The format of the property. Supported formats: - for NUMBER type: "float", "double" - for INTEGER type: "int32", "int64" - for STRING type: "email", "byte", etc                                                                 |
| [items](https://firebase.google.com/docs/reference/js/ai.schema.md#schemaitems)             |           | [SchemaInterface](https://firebase.google.com/docs/reference/js/ai.schemainterface.md#schemainterface_interface) | Optional. The items of the property.                                                                                                                                                                                                       |
| [maxItems](https://firebase.google.com/docs/reference/js/ai.schema.md#schemamaxitems)       |           | number                                                                                                           | The maximum number of items (elements) in a schema of [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) `array`.                                                                                                |
| [minItems](https://firebase.google.com/docs/reference/js/ai.schema.md#schemaminitems)       |           | number                                                                                                           | The minimum number of items (elements) in a schema of [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) `array`.                                                                                                |
| [nullable](https://firebase.google.com/docs/reference/js/ai.schema.md#schemanullable)       |           | boolean                                                                                                          | Optional. Whether the property is nullable. Defaults to false.                                                                                                                                                                             |
| [type](https://firebase.google.com/docs/reference/js/ai.schema.md#schematype)               |           | [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype)                                     | Optional. The type of the property. This can only be undefined when using `anyOf` schemas, which do not have an explicit type in the [OpenAPI specification](https://swagger.io/docs/specification/v3_0/data-models/data-types/#any-type). |

## Methods

|                                                 Method                                                  | Modifiers | Description |
|---------------------------------------------------------------------------------------------------------|-----------|-------------|
| [anyOf(anyOfParams)](https://firebase.google.com/docs/reference/js/ai.schema.md#schemaanyof)            | `static`  |             |
| [array(arrayParams)](https://firebase.google.com/docs/reference/js/ai.schema.md#schemaarray)            | `static`  |             |
| [boolean(booleanParams)](https://firebase.google.com/docs/reference/js/ai.schema.md#schemaboolean)      | `static`  |             |
| [enumString(stringParams)](https://firebase.google.com/docs/reference/js/ai.schema.md#schemaenumstring) | `static`  |             |
| [integer(integerParams)](https://firebase.google.com/docs/reference/js/ai.schema.md#schemainteger)      | `static`  |             |
| [number(numberParams)](https://firebase.google.com/docs/reference/js/ai.schema.md#schemanumber)         | `static`  |             |
| [object(objectParams)](https://firebase.google.com/docs/reference/js/ai.schema.md#schemaobject)         | `static`  |             |
| [string(stringParams)](https://firebase.google.com/docs/reference/js/ai.schema.md#schemastring)         | `static`  |             |

## Schema.(constructor)

Constructs a new instance of the `Schema` class

**Signature:**  

    constructor(schemaParams: SchemaInterface);

#### Parameters

|  Parameter   |                                                       Type                                                       | Description |
|--------------|------------------------------------------------------------------------------------------------------------------|-------------|
| schemaParams | [SchemaInterface](https://firebase.google.com/docs/reference/js/ai.schemainterface.md#schemainterface_interface) |             |

## Schema.description

Optional. The description of the property.

**Signature:**  

    description?: string;

## Schema.example

Optional. The example of the property.

**Signature:**  

    example?: unknown;

## Schema.format

Optional. The format of the property. Supported formats:  

- for NUMBER type: "float", "double"
- for INTEGER type: "int32", "int64"
- for STRING type: "email", "byte", etc

<br />

**Signature:**  

    format?: string;

## Schema.items

Optional. The items of the property.

**Signature:**  

    items?: SchemaInterface;

## Schema.maxItems

The maximum number of items (elements) in a schema of [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) `array`.

**Signature:**  

    maxItems?: number;

## Schema.minItems

The minimum number of items (elements) in a schema of [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) `array`.

**Signature:**  

    minItems?: number;

## Schema.nullable

Optional. Whether the property is nullable. Defaults to false.

**Signature:**  

    nullable: boolean;

## Schema.type

Optional. The type of the property. This can only be undefined when using `anyOf` schemas, which do not have an explicit type in the [OpenAPI specification](https://swagger.io/docs/specification/v3_0/data-models/data-types/#any-type).

**Signature:**  

    type?: SchemaType;

## Schema.anyOf()

**Signature:**  

    static anyOf(anyOfParams: SchemaParams & {
            anyOf: TypedSchema[];
        }): AnyOfSchema;

#### Parameters

|  Parameter  |                                                                                                   Type                                                                                                    | Description |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| anyOfParams | [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) \& { anyOf: [TypedSchema](https://firebase.google.com/docs/reference/js/ai.md#typedschema)\[\]; } |             |

**Returns:**

[AnyOfSchema](https://firebase.google.com/docs/reference/js/ai.anyofschema.md#anyofschema_class)

## Schema.array()

**Signature:**  

    static array(arrayParams: SchemaParams & {
            items: Schema;
        }): ArraySchema;

#### Parameters

|  Parameter  |                                                                                                   Type                                                                                                   | Description |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| arrayParams | [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) \& { items: [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class); } |             |

**Returns:**

[ArraySchema](https://firebase.google.com/docs/reference/js/ai.arrayschema.md#arrayschema_class)

## Schema.boolean()

**Signature:**  

    static boolean(booleanParams?: SchemaParams): BooleanSchema;

#### Parameters

|   Parameter   |                                                  Type                                                   | Description |
|---------------|---------------------------------------------------------------------------------------------------------|-------------|
| booleanParams | [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) |             |

**Returns:**

[BooleanSchema](https://firebase.google.com/docs/reference/js/ai.booleanschema.md#booleanschema_class)

## Schema.enumString()

**Signature:**  

    static enumString(stringParams: SchemaParams & {
            enum: string[];
        }): StringSchema;

#### Parameters

|  Parameter   |                                                               Type                                                               | Description |
|--------------|----------------------------------------------------------------------------------------------------------------------------------|-------------|
| stringParams | [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) \& { enum: string\[\]; } |             |

**Returns:**

[StringSchema](https://firebase.google.com/docs/reference/js/ai.stringschema.md#stringschema_class)

## Schema.integer()

**Signature:**  

    static integer(integerParams?: SchemaParams): IntegerSchema;

#### Parameters

|   Parameter   |                                                  Type                                                   | Description |
|---------------|---------------------------------------------------------------------------------------------------------|-------------|
| integerParams | [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) |             |

**Returns:**

[IntegerSchema](https://firebase.google.com/docs/reference/js/ai.integerschema.md#integerschema_class)

## Schema.number()

**Signature:**  

    static number(numberParams?: SchemaParams): NumberSchema;

#### Parameters

|  Parameter   |                                                  Type                                                   | Description |
|--------------|---------------------------------------------------------------------------------------------------------|-------------|
| numberParams | [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) |             |

**Returns:**

[NumberSchema](https://firebase.google.com/docs/reference/js/ai.numberschema.md#numberschema_class)

## Schema.object()

**Signature:**  

    static object(objectParams: SchemaParams & {
            properties: {
                [k: string]: Schema;
            };
            optionalProperties?: string[];
        }): ObjectSchema;

#### Parameters

|  Parameter   |                                                                                                                                Type                                                                                                                                | Description |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| objectParams | [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) \& { properties: { \[k: string\]: [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class); }; optionalProperties?: string\[\]; } |             |

**Returns:**

[ObjectSchema](https://firebase.google.com/docs/reference/js/ai.objectschema.md#objectschema_class)

## Schema.string()

**Signature:**  

    static string(stringParams?: SchemaParams): StringSchema;

#### Parameters

|  Parameter   |                                                  Type                                                   | Description |
|--------------|---------------------------------------------------------------------------------------------------------|-------------|
| stringParams | [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) |             |

**Returns:**

[StringSchema](https://firebase.google.com/docs/reference/js/ai.stringschema.md#stringschema_class)