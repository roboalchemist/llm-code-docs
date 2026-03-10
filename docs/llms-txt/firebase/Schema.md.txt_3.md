# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.md.txt

# FirebaseVertexAI Framework Reference

# Schema

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public final class Schema : Sendable

    extension Schema: Encodable

A `Schema` object allows the definition of input and output data types.

These types can be objects, but also primitives and arrays. Represents a select subset of an
[OpenAPI 3.0 schema object](https://spec.openapis.org/oas/v3.0.3#schema).
- `


  ### [StringFormat](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/StringFormat.html)


  ` Modifiers describing the expected format of a string `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html`.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct StringFormat : EncodableProtoEnum

- `


  ### [IntegerFormat](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/IntegerFormat.html)


  ` Modifiers describing the expected format of an integer `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html`.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct IntegerFormat : EncodableProtoEnum, Sendable

- `


  ### [type](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC4typeSSvp)


  ` The data type.

  #### Declaration

  Swift

      public var type: String { get }

- `


  ### [format](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC6formatSSSgvp)


  ` The format of the data.

  #### Declaration

  Swift

      public let format: String?

- `


  ### [description](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC11descriptionSSSgvp)


  ` A human-readable explanation of the purpose of the schema or property. While not strictly
  enforced on the value itself, good descriptions significantly help the model understand the
  context and generate more relevant and accurate output.

  #### Declaration

  Swift

      public let description: String?

- `


  ### [title](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC5titleSSSgvp)


  ` A human-readable name/summary for the schema or a specific property. This helps document the
  schema's purpose but doesn't typically constrain the generated value. It can subtly guide the
  model by clarifying the intent of a field.

  #### Declaration

  Swift

      public let title: String?

- `


  ### [nullable](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC8nullableSbSgvp)


  ` Indicates if the value may be null.

  #### Declaration

  Swift

      public let nullable: Bool?

- `


  ### [enumValues](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC10enumValuesSaySSGSgvp)


  ` Possible values of the element of type "STRING" with "enum" format.

  #### Declaration

  Swift

      public let enumValues: [String]?

- `


  ### [items](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC5itemsACSgvp)


  ` Defines the schema for the elements within the `"ARRAY"`. All items in the generated array
  must conform to this schema definition. This can be a simple type (like .string) or a complex
  nested object schema.

  #### Declaration

  Swift

      public let items: Schema?

- `


  ### [minItems](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC8minItemsSiSgvp)


  ` An integer specifying the minimum number of items the generated `"ARRAY"` must contain.

  #### Declaration

  Swift

      public let minItems: Int?

- `


  ### [maxItems](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC8maxItemsSiSgvp)


  ` An integer specifying the maximum number of items the generated `"ARRAY"` must contain.

  #### Declaration

  Swift

      public let maxItems: Int?

- `


  ### [minimum](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC7minimumSdSgvp)


  ` The minimum value of a numeric type.

  #### Declaration

  Swift

      public let minimum: Double?

- `


  ### [maximum](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC7maximumSdSgvp)


  ` The maximum value of a numeric type.

  #### Declaration

  Swift

      public let maximum: Double?

- `


  ### [properties](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC10propertiesSDySSACGSgvp)


  ` Defines the members (key-value pairs) expected within an object. It's a dictionary where keys
  are the property names (strings) and values are nested `Schema` definitions describing each
  property's type and constraints.

  #### Declaration

  Swift

      public let properties: [String : Schema]?

- `


  ### [anyOf](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC5anyOfSayACGSgvp)


  ` An array of `Schema` objects. The generated data must be valid against *any* (one or more)
  of the schemas listed in this array. This allows specifying multiple possible structures or
  types for a single field.

  For example, a value could be either a `String` or an `Integer`:

      Schema.anyOf(schemas: [.string(), .integer()])

  #### Declaration

  Swift

      public let anyOf: [Schema]?

- `


  ### [requiredProperties](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC18requiredPropertiesSaySSGSgvp)


  ` An array of strings, where each string is the name of a property defined in the `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC10propertiesSDySSACGSgvp`
  dictionary that must be present in the generated object. If a property is listed here, the
  model must include it in the output.

  #### Declaration

  Swift

      public let requiredProperties: [String]?

- `


  ### [propertyOrdering](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC16propertyOrderingSaySSGSgvp)


  ` A specific hint provided to the Gemini model, suggesting the order in which the keys should
  appear in the generated JSON string. Important: Standard JSON objects are inherently unordered
  collections of key-value pairs. While the model will try to respect propertyOrdering in its
  textual JSON output, subsequent parsing into native Swift objects (like Dictionaries or
  Structs) might not preserve this order. This parameter primarily affects the raw JSON string
  serialization.

  #### Declaration

  Swift

      public let propertyOrdering: [String]?

- `


  ### [string(description:nullable:format:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC6string11description8nullable6formatACSSSg_SbAC12StringFormatVSgtFZ)


  ` Returns a `Schema` representing a string value.

  This schema instructs the model to produce data of type `"STRING"`, which is suitable for
  decoding into a Swift `String` (or `String?`, if `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC8nullableSbSgvp` is set to `true`).
  Tip

  If a specific set of string values should be generated by the model (for example,
  "north", "south", "east", or "west"), use `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC11enumeration6values11description8nullableACSaySSG_SSSgSbtFZ`
  instead to constrain the generated values.

  #### Declaration

  Swift

      public static func string(description: String? = nil, nullable: Bool = false,
                                format: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/StringFormat.html? = nil) -> Schema

  #### Parameters

  |---|---|
  | ` description ` | An optional description of what the string should contain or represent; may use Markdown format. |
  | ` nullable ` | If `true`, instructs the model that it *may* generate `null` instead of a string; defaults to `false`, enforcing that a string value is generated. |
  | ` format ` | An optional modifier describing the expected format of the string. Currently no formats are officially supported for strings but custom values may be specified using `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/StringFormat.html#/s:16FirebaseVertexAI6SchemaC12StringFormatV6customyAESSFZ`, for example `.custom("email")` or `.custom("byte")`; these provide additional hints for how the model should respond but are not guaranteed to be adhered to. |

- `


  ### [enumeration(values:description:nullable:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC11enumeration6values11description8nullableACSaySSG_SSSgSbtFZ)


  ` Returns a `Schema` representing an enumeration of string values.

  This schema instructs the model to produce data of type `"STRING"` with the `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC6formatSSSgvp` `"enum"`.
  This data is suitable for decoding into a Swift `String` (or `String?`, if `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC8nullableSbSgvp` is set
  to `true`), or an `enum` with strings as raw values.

  **Example:**
  The values `["north", "south", "east", "west"]` for an enumeration of directions.

      enum Direction: String, Decodable {
        case north, south, east, west
      }

  #### Declaration

  Swift

      public static func enumeration(values: [String], description: String? = nil,
                                     nullable: Bool = false) -> Schema

  #### Parameters

  |---|---|
  | ` values ` | The list of string values that may be generated by the model. |
  | ` description ` | An optional description of what the `values` contain or represent; may use Markdown format. |
  | ` nullable ` | If `true`, instructs the model that it *may* generate `null` instead of one of the strings specified in `values`; defaults to `false`, enforcing that one of the string values is generated. |

- `


  ### [float(description:nullable:minimum:maximum:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC5float11description8nullable7minimum7maximumACSSSg_SbSfSgAJtFZ)


  ` Returns a `Schema` representing a single-precision floating-point number.

  This schema instructs the model to produce data of type `"NUMBER"` with the `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC6formatSSSgvp`
  `"float"`, which is suitable for decoding into a Swift `Float` (or `Float?`, if `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC8nullableSbSgvp` is
  set to `true`).
  Important

  This `Schema` provides a hint to the model that it should generate a
  single-precision floating-point number, a `float`, but only guarantees that the value will
  be a number.

  #### Declaration

  Swift

      public static func float(description: String? = nil, nullable: Bool = false,
                               minimum: Float? = nil, maximum: Float? = nil) -> Schema

  #### Parameters

  |---|---|
  | ` description ` | An optional description of what the number should contain or represent; may use Markdown format. |
  | ` nullable ` | If `true`, instructs the model that it may generate `null` instead of a number; defaults to `false`, enforcing that a number is generated. |
  | ` minimum ` | If specified, instructs the model that the value should be greater than or equal to the specified minimum. |
  | ` maximum ` | If specified, instructs the model that the value should be less than or equal to the specified maximum. |

- `


  ### [double(description:nullable:minimum:maximum:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC6double11description8nullable7minimum7maximumACSSSg_SbSdSgAJtFZ)


  ` Returns a `Schema` representing a floating-point number.

  This schema instructs the model to produce data of type `"NUMBER"`, which is suitable for
  decoding into a Swift `Double` (or `Double?`, if `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC8nullableSbSgvp` is set to `true`).

  #### Declaration

  Swift

      public static func double(description: String? = nil, nullable: Bool = false,
                                minimum: Double? = nil, maximum: Double? = nil) -> Schema

  #### Parameters

  |---|---|
  | ` description ` | An optional description of what the number should contain or represent; may use Markdown format. |
  | ` nullable ` | If `true`, instructs the model that it may return `null` instead of a number; defaults to `false`, enforcing that a number is returned. |
  | ` minimum ` | If specified, instructs the model that the value should be greater than or equal to the specified minimum. |
  | ` maximum ` | If specified, instructs the model that the value should be less than or equal to the specified maximum. |

- `


  ### [integer(description:nullable:format:minimum:maximum:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC7integer11description8nullable6format7minimum7maximumACSSSg_SbAC13IntegerFormatVSgSiSgANtFZ)


  ` Returns a `Schema` representing an integer value.

  This schema instructs the model to produce data of type `"INTEGER"`, which is suitable for
  decoding into a Swift `Int` (or `Int?`, if `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC8nullableSbSgvp` is set to `true`) or other integer types
  (such as `Int32`) based on the expected size of values being generated.
  Important

  If a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC6formatSSSgvp` of `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/IntegerFormat.html#/s:16FirebaseVertexAI6SchemaC13IntegerFormatV5int32AEvpZ` or `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/IntegerFormat.html#/s:16FirebaseVertexAI6SchemaC13IntegerFormatV5int64AEvpZ` is
  specified, this provides a hint to the model that it should generate 32-bit or 64-bit
  integers but this `Schema` only guarantees that the value will be an integer. Therefore, it
  is *possible* that decoding into an `Int32` could overflow even if a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC6formatSSSgvp` of
  `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/IntegerFormat.html#/s:16FirebaseVertexAI6SchemaC13IntegerFormatV5int32AEvpZ` is specified.

  #### Declaration

  Swift

      public static func integer(description: String? = nil, nullable: Bool = false,
                                 format: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/IntegerFormat.html? = nil,
                                 minimum: Int? = nil, maximum: Int? = nil) -> Schema

  #### Parameters

  |---|---|
  | ` description ` | An optional description of what the integer should contain or represent; may use Markdown format. |
  | ` nullable ` | If `true`, instructs the model that it may return `null` instead of an integer; defaults to `false`, enforcing that an integer is returned. |
  | ` format ` | An optional modifier describing the expected format of the integer. Currently the formats `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/IntegerFormat.html#/s:16FirebaseVertexAI6SchemaC13IntegerFormatV5int32AEvpZ` and `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/IntegerFormat.html#/s:16FirebaseVertexAI6SchemaC13IntegerFormatV5int64AEvpZ` are supported; custom values may be specified using `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/IntegerFormat.html#/s:16FirebaseVertexAI6SchemaC13IntegerFormatV6customyAESSFZ` but may be ignored by the model. |
  | ` minimum ` | If specified, instructs the model that the value should be greater than or equal to the specified minimum. |
  | ` maximum ` | If specified, instructs the model that the value should be less than or equal to the specified maximum. |

- `


  ### [boolean(description:nullable:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC7boolean11description8nullableACSSSg_SbtFZ)


  ` Returns a `Schema` representing a boolean value.

  This schema instructs the model to produce data of type `"BOOLEAN"`, which is suitable for
  decoding into a Swift `Bool` (or `Bool?`, if `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC8nullableSbSgvp` is set to `true`).

  #### Declaration

  Swift

      public static func boolean(description: String? = nil, nullable: Bool = false) -> Schema

  #### Parameters

  |---|---|
  | ` description ` | An optional description of what the boolean should contain or represent; may use Markdown format. |
  | ` nullable ` | If `true`, instructs the model that it may return `null` instead of a boolean; defaults to `false`, enforcing that a boolean is returned. |

- `


  ### [array(items:description:nullable:minItems:maxItems:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC5array5items11description8nullable8minItems03maxJ0A2C_SSSgSbSiSgAKtFZ)


  ` Returns a `Schema` representing an array.

  This schema instructs the model to produce data of type `"ARRAY"`, which has elements of any
  other data type (including nested `"ARRAY"`s). This data is suitable for decoding into many
  Swift collection types, including `Array`, holding elements of types suitable for decoding
  from the respective `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC5itemsACSgvp` type.

  #### Declaration

  Swift

      public static func array(items: Schema, description: String? = nil, nullable: Bool = false,
                               minItems: Int? = nil, maxItems: Int? = nil) -> Schema

  #### Parameters

  |---|---|
  | ` items ` | The `Schema` of the elements that the array will hold. |
  | ` description ` | An optional description of what the array should contain or represent; may use Markdown format. |
  | ` nullable ` | If `true`, instructs the model that it may return `null` instead of an array; defaults to `false`, enforcing that an array is returned. |
  | ` minItems ` | Instructs the model to produce at least the specified minimum number of elements in the array; defaults to `nil`, meaning any number. |
  | ` maxItems ` | Instructs the model to produce at most the specified maximum number of elements in the array. |

- `


  ### [object(properties:optionalProperties:propertyOrdering:description:title:nullable:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC6object10properties18optionalProperties16propertyOrdering11description5title8nullableACSDySSACG_SaySSGALSgSSSgANSbtFZ)


  ` Returns a `Schema` representing an object.

  This schema instructs the model to produce data of type `"OBJECT"`, which has keys of type
  `"STRING"` and values of any other data type (including nested `"OBJECT"`s). This data is
  suitable for decoding into Swift keyed collection types, including `Dictionary`, or other
  custom `struct` or `class` types.

  **Example:** A `City` could be represented with the following object `Schema`.

      Schema.object(properties: [
        "name" : .string(),
        "population": .integer()
      ])

  The generated data could be decoded into a Swift native type:

      struct City: Decodable {
        let name: String
        let population: Int
      }

  #### Declaration

  Swift

      public static func object(properties: [String: Schema], optionalProperties: [String] = [],
                                propertyOrdering: [String]? = nil,
                                description: String? = nil, title: String? = nil,
                                nullable: Bool = false) -> Schema

  #### Parameters

  |---|---|
  | ` properties ` | A dictionary containing the object's property names as keys and their respective `Schema`s as values. |
  | ` optionalProperties ` | A list of property names that may be be omitted in objects generated by the model; these names must correspond to the keys provided in the `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC10propertiesSDySSACGSgvp` dictionary and may be an empty list. |
  | ` propertyOrdering ` | An optional hint to the model suggesting the order for keys in the generated JSON string. See `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.html#/s:16FirebaseVertexAI6SchemaC16propertyOrderingSaySSGSgvp` for details. |
  | ` description ` | An optional description of what the object should contain or represent; may use Markdown format. |
  | ` title ` | An optional human-readable name/summary for the object schema. |
  | ` nullable ` | If `true`, instructs the model that it may return `null` instead of an object; defaults to `false`, enforcing that an object is returned. |

- `


  ### [anyOf(schemas:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema#/s:16FirebaseVertexAI6SchemaC5anyOf7schemasACSayACG_tFZ)


  ` Returns a `Schema` representing a value that must conform to *any* (one or more) of the
  provided sub-schemas.

  This schema instructs the model to produce data that is valid against at least one of the
  schemas listed in the `schemas` array. This is useful when a field can accept multiple
  distinct types or structures.

  **Example:** A field that can hold either a simple user ID (integer) or a detailed user
  object.

      Schema.anyOf(schemas: [
        .integer(description: "User ID"),
        .object(properties: [
          "userId": .integer(),
          "userName": .string()
        ], description: "Detailed User Object")
      ])

  The generated data could be decoded based on which schema it matches.

  #### Declaration

  Swift

      public static func anyOf(schemas: [Schema]) -> Schema

  #### Parameters

  |---|---|
  | ` schemas ` | An array of `Schema` objects. The generated data must be valid against at least one of these schemas. The array must not be empty. |