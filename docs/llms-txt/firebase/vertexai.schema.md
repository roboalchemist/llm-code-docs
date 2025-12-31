# Source: https://firebase.google.com/docs/reference/js/vertexai.schema.md.txt

# Schema class

Parent class encompassing all Schema types, with static methods that allow building specific Schema types. This class can be converted with `JSON.stringify()` into a JSON string accepted by Vertex AI REST endpoints. (This string conversion is automatically done when calling SDK methods.)

**Signature:**  

    export declare abstract class Schema implements SchemaInterface 

**Implements:** [SchemaInterface](https://firebase.google.com/docs/reference/js/vertexai.schemainterface.md#schemainterface_interface)

## Constructors

|                                                    Constructor                                                    | Modifiers |                   Description                   |
|-------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------|
| [(constructor)(schemaParams)](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemaconstructor) |           | Constructs a new instance of the `Schema` class |

## Properties

|                                             Property                                              | Modifiers |                                        Type                                        |                                                                                Description                                                                                 |
|---------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [description](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemadescription) |           | string                                                                             | Optional. The description of the property.                                                                                                                                 |
| [example](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemaexample)         |           | unknown                                                                            | Optional. The example of the property.                                                                                                                                     |
| [format](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemaformat)           |           | string                                                                             | Optional. The format of the property. Supported formats: - for NUMBER type: "float", "double" - for INTEGER type: "int32", "int64" - for STRING type: "email", "byte", etc |
| [nullable](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemanullable)       |           | boolean                                                                            | Optional. Whether the property is nullable. Defaults to false.                                                                                                             |
| [type](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schematype)               |           | [SchemaType](https://firebase.google.com/docs/reference/js/vertexai.md#schematype) | Optional. The type of the property. [SchemaType](https://firebase.google.com/docs/reference/js/vertexai.md#schematype).                                                    |

## Methods

|                                                    Method                                                     | Modifiers | Description |
|---------------------------------------------------------------------------------------------------------------|-----------|-------------|
| [array(arrayParams)](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemaarray)            | `static`  |             |
| [boolean(booleanParams)](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemaboolean)      | `static`  |             |
| [enumString(stringParams)](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemaenumstring) | `static`  |             |
| [integer(integerParams)](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemainteger)      | `static`  |             |
| [number(numberParams)](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemanumber)         | `static`  |             |
| [object(objectParams)](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemaobject)         | `static`  |             |
| [string(stringParams)](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schemastring)         | `static`  |             |

## Schema.(constructor)

Constructs a new instance of the `Schema` class

**Signature:**  

    constructor(schemaParams: SchemaInterface);

#### Parameters

|  Parameter   |                                                          Type                                                          | Description |
|--------------|------------------------------------------------------------------------------------------------------------------------|-------------|
| schemaParams | [SchemaInterface](https://firebase.google.com/docs/reference/js/vertexai.schemainterface.md#schemainterface_interface) |             |

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

## Schema.nullable

Optional. Whether the property is nullable. Defaults to false.

**Signature:**  

    nullable: boolean;

## Schema.type

Optional. The type of the property. [SchemaType](https://firebase.google.com/docs/reference/js/vertexai.md#schematype).

**Signature:**  

    type: SchemaType;

## Schema.array()

**Signature:**  

    static array(arrayParams: SchemaParams & {
            items: Schema;
        }): ArraySchema;

#### Parameters

|  Parameter  |                                                                                                         Type                                                                                                         | Description |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| arrayParams | [SchemaParams](https://firebase.google.com/docs/reference/js/vertexai.schemaparams.md#schemaparams_interface) \& { items: [Schema](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schema_class); } |             |

**Returns:**

[ArraySchema](https://firebase.google.com/docs/reference/js/vertexai.arrayschema.md#arrayschema_class)

## Schema.boolean()

**Signature:**  

    static boolean(booleanParams?: SchemaParams): BooleanSchema;

#### Parameters

|   Parameter   |                                                     Type                                                      | Description |
|---------------|---------------------------------------------------------------------------------------------------------------|-------------|
| booleanParams | [SchemaParams](https://firebase.google.com/docs/reference/js/vertexai.schemaparams.md#schemaparams_interface) |             |

**Returns:**

[BooleanSchema](https://firebase.google.com/docs/reference/js/vertexai.booleanschema.md#booleanschema_class)

## Schema.enumString()

**Signature:**  

    static enumString(stringParams: SchemaParams & {
            enum: string[];
        }): StringSchema;

#### Parameters

|  Parameter   |                                                                  Type                                                                  | Description |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------|
| stringParams | [SchemaParams](https://firebase.google.com/docs/reference/js/vertexai.schemaparams.md#schemaparams_interface) \& { enum: string\[\]; } |             |

**Returns:**

[StringSchema](https://firebase.google.com/docs/reference/js/vertexai.stringschema.md#stringschema_class)

## Schema.integer()

**Signature:**  

    static integer(integerParams?: SchemaParams): IntegerSchema;

#### Parameters

|   Parameter   |                                                     Type                                                      | Description |
|---------------|---------------------------------------------------------------------------------------------------------------|-------------|
| integerParams | [SchemaParams](https://firebase.google.com/docs/reference/js/vertexai.schemaparams.md#schemaparams_interface) |             |

**Returns:**

[IntegerSchema](https://firebase.google.com/docs/reference/js/vertexai.integerschema.md#integerschema_class)

## Schema.number()

**Signature:**  

    static number(numberParams?: SchemaParams): NumberSchema;

#### Parameters

|  Parameter   |                                                     Type                                                      | Description |
|--------------|---------------------------------------------------------------------------------------------------------------|-------------|
| numberParams | [SchemaParams](https://firebase.google.com/docs/reference/js/vertexai.schemaparams.md#schemaparams_interface) |             |

**Returns:**

[NumberSchema](https://firebase.google.com/docs/reference/js/vertexai.numberschema.md#numberschema_class)

## Schema.object()

**Signature:**  

    static object(objectParams: SchemaParams & {
            properties: {
                [k: string]: Schema;
            };
            optionalProperties?: string[];
        }): ObjectSchema;

#### Parameters

|  Parameter   |                                                                                                                                      Type                                                                                                                                      | Description |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| objectParams | [SchemaParams](https://firebase.google.com/docs/reference/js/vertexai.schemaparams.md#schemaparams_interface) \& { properties: { \[k: string\]: [Schema](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schema_class); }; optionalProperties?: string\[\]; } |             |

**Returns:**

[ObjectSchema](https://firebase.google.com/docs/reference/js/vertexai.objectschema.md#objectschema_class)

## Schema.string()

**Signature:**  

    static string(stringParams?: SchemaParams): StringSchema;

#### Parameters

|  Parameter   |                                                     Type                                                      | Description |
|--------------|---------------------------------------------------------------------------------------------------------------|-------------|
| stringParams | [SchemaParams](https://firebase.google.com/docs/reference/js/vertexai.schemaparams.md#schemaparams_interface) |             |

**Returns:**

[StringSchema](https://firebase.google.com/docs/reference/js/vertexai.stringschema.md#stringschema_class)