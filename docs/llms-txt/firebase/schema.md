# Source: https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema.md.txt

# Firebase.AI.Schema Class Reference

# Firebase.AI.Schema

A [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) object allows the definition of input and output data types.

## Summary

These types can be objects, but also primitives and arrays. Represents a select subset of an [OpenAPI 3.0 schema object](https://spec.openapis.org/oas/v3.0.3#schema).

|                                                                                                                                                ### Public types                                                                                                                                                 ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [SchemaType](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1ae6f6ef6b9ee8b8c2cc95faacc8a96758) | enum The value type of a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema). |

|                                                                                                                                                                                                                         ### Properties                                                                                                                                                                                                                         ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AnyOfSchemas](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a92a6a20ccb54c893f003fc0da626df1c)       | `IReadOnlyList< `[Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema)` >` An array of [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) objects. |
| [Description](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a0bff1bc51a36a8d2336f742453bc520f)        | `string` A human-readable explanation of the purpose of the schema or property.                                                                                                                                                                                                         |
| [EnumValues](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a412d55ce8fb9d8f9e1b5899058da0ba5)         | `IReadOnlyList< string >` Possible values of the element of type "String" with "enum" format.                                                                                                                                                                                           |
| [Format](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1afa9a5fa8019fd600d2d5e34f36e46973)             | `string` The format of the data.                                                                                                                                                                                                                                                        |
| [Items](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a5420dc1ccd0f7069412536b698d6988a)              | [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) of the elements of type "Array".          |
| [MaxItems](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1af177ea2d18696e810fe32de1ad265a54)           | `int` An integer specifying the maximum number of items the generated "Array" must contain.                                                                                                                                                                                             |
| [Maximum](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a22939a7eb02e377a4a4673d7ca8df89c)            | `double` The maximum value of a numeric type.                                                                                                                                                                                                                                           |
| [MinItems](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1acfaa60d5f8ce07c3b3aa770ba8aeacb1)           | `int` An integer specifying the minimum number of items the generated "Array" must contain.                                                                                                                                                                                             |
| [Minimum](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1aab9f18f707df9c9ef30394d43bc7e1bb)            | `double` The minimum value of a numeric type.                                                                                                                                                                                                                                           |
| [Nullable](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a22fd1c21b3651d6ec03950cd14724816)           | `bool` Indicates if the value may be null.                                                                                                                                                                                                                                              |
| [Properties](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1af91be30943614b2a0012902593104206)         | `IReadOnlyDictionary< string, `[Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema)` >` Properties of type "Object".                                                                                                  |
| [PropertyOrdering](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a7a8bc294e9ca024d765e9646d0a91c59)   | `IReadOnlyList< string >` A specific hint provided to the Gemini model, suggesting the order in which the keys should appear in the generated JSON string.                                                                                                                              |
| [RequiredProperties](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1ab9fe3cfb103ef0b5022831e00c528b05) | `IReadOnlyList< string >` Required properties of type "Object".                                                                                                                                                                                                                         |
| [Title](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a92e0e88021b8ea6c5dbc2c41f2f81244)              | `string` A human-readable name/summary for the schema or a specific property.                                                                                                                                                                                                           |
| [Type](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a5d816e8f3ac3842e10ea77ae44063d0d)               | [SchemaType](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1ae6f6ef6b9ee8b8c2cc95faacc8a96758) The data type.                                                                                                            |

|                                                                                                                                                                                                                                                                                                                                                                                          ### Public static functions                                                                                                                                                                                                                                                                                                                                                                                           ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AnyOf](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1aa040a1561d51185d673dc62af565deba)`(IEnumerable< `[Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema)` > schemas)`                                                                                                                                                | [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) representing a value that must conform to *any* (one or more) of the provided sub-schemas. |
| [Array](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1ad8db1af11dd43f679fbb07771480af4b)`(`[Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema)` items, string description, bool nullable, int? minItems, int? maxItems)`                                                                                                | [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for an array.                                                                              |
| [Boolean](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a4b321f99adc83cb2d93ae3f0b150e753)`(string description, bool nullable)`                                                                                                                                                                                                                                                            | [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) representing a boolean value.                                                              |
| [Double](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a03b28dd8253b20029a796ef2ef5d9ab0)`(string description, bool nullable, double? minimum, double? maximum)`                                                                                                                                                                                                                           | [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for a double-precision floating-point number.                                              |
| [Enum](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a2b95566441cec918f9e9d97f53cf6819)`(IEnumerable< string > values, string description, bool nullable)`                                                                                                                                                                                                                                 | [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for an enumeration.                                                                        |
| [Float](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1aafb80c62c39bd4116177ccaf9560f8d1)`(string description, bool nullable, float? minimum, float? maximum)`                                                                                                                                                                                                                              | [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for a single-precision floating-point number.                                              |
| [Int](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a4c6762d0f20722324b8bc4f1d5bbc009)`(string description, bool nullable, int? minimum, int? maximum)`                                                                                                                                                                                                                                    | [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for a 32-bit signed integer number.                                                        |
| [Long](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1ad68ba08e385120abd7f2ad6bed37db0e)`(string description, bool nullable, long? minimum, long? maximum)`                                                                                                                                                                                                                                 | [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for a 64-bit signed integer number.                                                        |
| [Object](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1af1ee9a675e8dd8acd763624dda86e765)`(IDictionary< string, `[Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema)` > properties, IEnumerable< string > optionalProperties, IEnumerable< string > propertyOrdering, string description, string title, bool nullable)` | [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) representing an object.                                                                    |
| [String](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1ab1cd731a5a14449ab5336b251d05617e)`(string description, bool nullable, `[StringFormat](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/schema/string-format#struct_firebase_1_1_a_i_1_1_schema_1_1_string_format)`? format)`                                                                                   | [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for a string.                                                                              |

|                                                                                                                                                ### Structs                                                                                                                                                 ||
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Firebase.AI.Schema.StringFormat](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/schema/string-format) | Modifiers describing the expected format of a string [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema). |

## Public types

### SchemaType

```c#
 SchemaType
```  
The value type of a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema).

## Properties

### AnyOfSchemas

```c#
IReadOnlyList< Schema > AnyOfSchemas
```  
An array of [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) objects.

The generated data must be valid against *any* (one or more) of the schemas listed in this array. This allows specifying multiple possible structures or types for a single field.

For example, a value could be either a `String` or an `Int`: \`\`\` [Schema.AnyOf](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1aa040a1561d51185d673dc62af565deba)(new \[\] { [Schema.String()](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1ab1cd731a5a14449ab5336b251d05617e), [Schema.Int()](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a4c6762d0f20722324b8bc4f1d5bbc009) }) \`\`\`  

### Description

```c#
string Description
```  
A human-readable explanation of the purpose of the schema or property.

While not strictly enforced on the value itself, good descriptions significantly help the model understand the context and generate more relevant and accurate output.  

### EnumValues

```c#
IReadOnlyList< string > EnumValues
```  
Possible values of the element of type "String" with "enum" format.  

### Format

```c#
string Format
```  
The format of the data.  

### Items

```c#
Schema Items
```  
[Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) of the elements of type "Array".  

### MaxItems

```c#
int MaxItems
```  
An integer specifying the maximum number of items the generated "Array" must contain.  

### Maximum

```c#
double Maximum
```  
The maximum value of a numeric type.  

### MinItems

```c#
int MinItems
```  
An integer specifying the minimum number of items the generated "Array" must contain.  

### Minimum

```c#
double Minimum
```  
The minimum value of a numeric type.  

### Nullable

```c#
bool Nullable
```  
Indicates if the value may be null.  

### Properties

```c#
IReadOnlyDictionary< string, Schema > Properties
```  
Properties of type "Object".  

### PropertyOrdering

```c#
IReadOnlyList< string > PropertyOrdering
```  
A specific hint provided to the Gemini model, suggesting the order in which the keys should appear in the generated JSON string.

Important: Standard JSON objects are inherently unordered collections of key-value pairs. While the model will try to respect PropertyOrdering in its textual JSON output, subsequent parsing into native C# objects (like Dictionaries) might not preserve this order. This parameter primarily affects the raw JSON string serialization.  

### RequiredProperties

```c#
IReadOnlyList< string > RequiredProperties
```  
Required properties of type "Object".  

### Title

```c#
string Title
```  
A human-readable name/summary for the schema or a specific property.

This helps document the schema's purpose but doesn't typically constrain the generated value. It can subtly guide the model by clarifying the intent of a field.  

### Type

```c#
SchemaType Type
```  
The data type.

## Public static functions

### AnyOf

```c#
Schema AnyOf(
  IEnumerable< Schema > schemas
)
```  
Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) representing a value that must conform to *any* (one or more) of the provided sub-schemas.

This schema instructs the model to produce data that is valid against at least one of the schemas listed in the `schemas` array. This is useful when a field can accept multiple distinct types or structures.

<br />

|                                                                                                                                                                                                                                                                    Details                                                                                                                                                                                                                                                                    ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `schemas` | An array of [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) objects. The generated data must be valid against at least one of these schemas. The array must not be empty. | |

### Array

```c#
Schema Array(
  Schema items,
  string description,
  bool nullable,
  int? minItems,
  int? maxItems
)
```  
Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for an array.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------| | `items`       | The [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) of the elements stored in the array. | | `description` | An optional description of what the array represents.                                                                                                           | | `nullable`    | Indicates whether the value can be `null`. Defaults to `false`.                                                                                                 | | `minItems`    | Instructs the model to produce at least the specified minimum number of elements in the array.                                                                  | | `maxItems`    | Instructs the model to produce at most the specified minimum number of elements in the array.                                                                   | |

### Boolean

```c#
Schema Boolean(
  string description,
  bool nullable
)
```  
Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) representing a boolean value.

<br />

|                                                                                                                                              Details                                                                                                                                               ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|--------------------------------------------------------------------------| | `description` | An optional description of what the boolean should contain or represent. | | `nullable`    | Indicates whether the value can be `null`. Defaults to `false`.          | |

### Double

```c#
Schema Double(
  string description,
  bool nullable,
  double? minimum,
  double? maximum
)
```  
Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for a double-precision floating-point number.

<br />

|                                                                                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                                                                                 ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|------------------------------------------------------------------------------------------------------------| | `description` | An optional description of what the number should contain or represent.                                    | | `nullable`    | Indicates whether the value can be `null`. Defaults to `false`.                                            | | `minimum`     | If specified, instructs the model that the value should be greater than or equal to the specified minimum. | | `maximum`     | If specified, instructs the model that the value should be less than or equal to the specified maximum.    | |

### Enum

```c#
Schema Enum(
  IEnumerable< string > values,
  string description,
  bool nullable
)
```  
Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for an enumeration.

For example, the cardinal directions can be represented as: \`\`\` [Schema.Enum](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1a2b95566441cec918f9e9d97f53cf6819)(new string\[\]{ "North", "East", "South", "West" }, "Cardinal directions") \`\`\`

<br />

|                                                                                                                                                                           Details                                                                                                                                                                           ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|-----------------------------------------------------------------| | `values`      | The list of valid values for this enumeration.                  | | `description` | An optional description of what the enum represents.            | | `nullable`    | Indicates whether the value can be `null`. Defaults to `false`. | |

### Float

```c#
Schema Float(
  string description,
  bool nullable,
  float? minimum,
  float? maximum
)
```  
Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for a single-precision floating-point number.

**Important:** This [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) provides a hint to the model that it should generate a single-precision floating-point number, but only guarantees that the value will be a number. Therefore it's *possible* that decoding it as a `float` could overflow.

<br />

|                                                                                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                                                                                 ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|------------------------------------------------------------------------------------------------------------| | `description` | An optional description of what the number should contain or represent.                                    | | `nullable`    | Indicates whether the value can be `null`. Defaults to `false`.                                            | | `minimum`     | If specified, instructs the model that the value should be greater than or equal to the specified minimum. | | `maximum`     | If specified, instructs the model that the value should be less than or equal to the specified maximum.    | |

### Int

```c#
Schema Int(
  string description,
  bool nullable,
  int? minimum,
  int? maximum
)
```  
Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for a 32-bit signed integer number.

**Important:** This [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) provides a hint to the model that it should generate a 32-bit integer, but only guarantees that the value will be an integer. Therefore it's *possible* that decoding it as an `int` could overflow.

<br />

|                                                                                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                                                                                 ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|------------------------------------------------------------------------------------------------------------| | `description` | An optional description of what the integer should contain or represent.                                   | | `nullable`    | Indicates whether the value can be `null`. Defaults to `false`.                                            | | `minimum`     | If specified, instructs the model that the value should be greater than or equal to the specified minimum. | | `maximum`     | If specified, instructs the model that the value should be less than or equal to the specified maximum.    | |

### Long

```c#
Schema Long(
  string description,
  bool nullable,
  long? minimum,
  long? maximum
)
```  
Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for a 64-bit signed integer number.

<br />

|                                                                                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                                                                                 ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|------------------------------------------------------------------------------------------------------------| | `description` | An optional description of what the number should contain or represent.                                    | | `nullable`    | Indicates whether the value can be `null`. Defaults to `false`.                                            | | `minimum`     | If specified, instructs the model that the value should be greater than or equal to the specified minimum. | | `maximum`     | If specified, instructs the model that the value should be less than or equal to the specified maximum.    | |

### Object

```c#
Schema Object(
  IDictionary< string, Schema > properties,
  IEnumerable< string > optionalProperties,
  IEnumerable< string > propertyOrdering,
  string description,
  string title,
  bool nullable
)
```  
Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) representing an object.

This schema instructs the model to produce data of type "Object", which has keys of type "String" and values of any other data type (including nested "Objects"s).

**Example:** A `City` could be represented with the following object [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema). \`\`\` [Schema.Object](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1af1ee9a675e8dd8acd763624dda86e765)(properties: new Dictionary() { { "name", [Schema.String()](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema_1ab1cd731a5a14449ab5336b251d05617e) }, { "population", Schema.Integer() } }) \`\`\`

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `properties`         | The map of the object's property names to their [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema)s.               | | `optionalProperties` | The list of optional properties. They must correspond to the keys provided in the `properties` map. By default it's empty, signaling the model that all properties are to be included. | | `propertyOrdering`   | An optional hint to the model suggesting the order for keys in the generated JSON string.                                                                                              | | `description`        | An optional description of what the object represents.                                                                                                                                 | | `title`              | An optional human-readable name/summary for the object schema.                                                                                                                         | | `nullable`           | Indicates whether the value can be `null`. Defaults to `false`.                                                                                                                        | |

### String

```c#
Schema String(
  string description,
  bool nullable,
  StringFormat? format
)
```  
Returns a [Schema](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/schema#class_firebase_1_1_a_i_1_1_schema) for a string.

<br />

|                                                                                                                                                                                           Details                                                                                                                                                                                           ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|-------------------------------------------------------------------------| | `description` | An optional description of what the string should contain or represent. | | `nullable`    | Indicates whether the value can be `null`. Defaults to `false`.         | | `format`      | An optional pattern that values need to adhere to.                      | |