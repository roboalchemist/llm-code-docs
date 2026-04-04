# Typespec Documentation

Source: https://www.typespec.io/docs/llms-full.txt

---

# TypeSpec Documentation

# Data types

Data types exported by @typespec/json-schema

## TypeSpec.JsonSchema

### `Json` {#TypeSpec.JsonSchema.Json}

Specify that the provided template argument should be emitted as raw JSON or YAML
as opposed to a schema. Use in combination with the

```typespec
model TypeSpec.JsonSchema.Json<Data>
```

#### Template Parameters

| Name | Description                     |
| ---- | ------------------------------- |
| Data | the type to convert to raw JSON |

#### Properties

| Name  | Type   | Description |
| ----- | ------ | ----------- |
| value | `Data` |             |

### `Format` {#TypeSpec.JsonSchema.Format}

Well-known JSON Schema formats.

```typespec
enum TypeSpec.JsonSchema.Format
```

| Name                | Value                     | Description |
| ------------------- | ------------------------- | ----------- |
| dateTime            | `"date-time"`             |             |
| date                | `"date"`                  |             |
| time                | `"time"`                  |             |
| duration            | `"duration"`              |             |
| email               | `"email"`                 |             |
| idnEmail            | `"idn-email"`             |             |
| hostname            | `"hostname"`              |             |
| idnHostname         | `"idn-hostname"`          |             |
| ipv4                | `"ipv4"`                  |             |
| ipv6                | `"ipv6"`                  |             |
| uri                 | `"uri"`                   |             |
| uriReference        | `"uri-reference"`         |             |
| iri                 | `"iri"`                   |             |
| iriReference        | `"iri-reference"`         |             |
| uuid                | `"uuid"`                  |             |
| jsonPointer         | `"json-pointer"`          |             |
| relativeJsonPointer | `"relative-json-pointer"` |             |
| regex               | `"regex"`                 |             |

# Decorators

Decorators exported by @typespec/json-schema

## TypeSpec.JsonSchema

### `@baseUri` {#@TypeSpec.JsonSchema.baseUri}

Set the base URI for any schemas emitted from types within this namespace.

```typespec
@TypeSpec.JsonSchema.baseUri(baseUri: valueof string)
```

#### Target

`Namespace`

#### Parameters

| Name    | Type             | Description                                                              |
| ------- | ---------------- | ------------------------------------------------------------------------ |
| baseUri | `valueof string` | The base URI. Schema IDs inside this namespace are relative to this URI. |

### `@contains` {#@TypeSpec.JsonSchema.contains}

Specify that the array must contain at least one instance of the provided type.
Use `@minContains` and `@maxContains` to customize how many instances to expect.

```typespec
@TypeSpec.JsonSchema.contains(value: unknown)
```

#### Target

`unknown[] | ModelProperty`

#### Parameters

| Name  | Type      | Description                      |
| ----- | --------- | -------------------------------- |
| value | `unknown` | The type the array must contain. |

### `@contentEncoding` {#@TypeSpec.JsonSchema.contentEncoding}

Specify the encoding used for the contents of a string.

```typespec
@TypeSpec.JsonSchema.contentEncoding(value: valueof string)
```

#### Target

`string | ModelProperty`

#### Parameters

| Name  | Type             | Description |
| ----- | ---------------- | ----------- |
| value | `valueof string` | <br />      |

### `@contentMediaType` {#@TypeSpec.JsonSchema.contentMediaType}

Specify the content type of content stored in a string.

```typespec
@TypeSpec.JsonSchema.contentMediaType(value: valueof string)
```

#### Target

`string | ModelProperty`

#### Parameters

| Name  | Type             | Description                           |
| ----- | ---------------- | ------------------------------------- |
| value | `valueof string` | The media type of the string contents |

### `@contentSchema` {#@TypeSpec.JsonSchema.contentSchema}

Specify the schema for the contents of a string when interpreted according to the content's
media type and encoding.

```typespec
@TypeSpec.JsonSchema.contentSchema(value: unknown)
```

#### Target

`string | ModelProperty`

#### Parameters

| Name  | Type      | Description                       |
| ----- | --------- | --------------------------------- |
| value | `unknown` | The schema of the string contents |

### `@extension` {#@TypeSpec.JsonSchema.extension}

Specify a custom property to add to the emitted schema. This is useful for adding custom keywords
and other vendor-specific extensions. Scalar values need to be specified using `typeof` to be converted to a schema.

For example, `@extension("x-schema", typeof "foo")` will emit a JSON schema value for `x-schema`,
whereas `@extension("x-schema", "foo")` will emit the raw code `"foo"`.

The value will be treated as a raw value if any of the following are true:

- The value is a scalar value (e.g. string, number, boolean, etc.)
- The value is wrapped in the `Json<Data>` template
- The value is provided using the value syntax (e.g. `#{}`, `#[]`)

For example, `@extension("x-schema", { x: "value" })` will emit a JSON schema value for `x-schema`,
whereas `@extension("x-schema", #{x: "value"})` and `@extension("x-schema", Json<{x: "value"}>)`
will emit the raw JSON code `{x: "value"}`.

```typespec
@TypeSpec.JsonSchema.extension(key: valueof string, value: unknown | valueof unknown)
```

#### Target

`unknown`

#### Parameters

| Name  | Type                           | Description                                                   |
| ----- | ------------------------------ | ------------------------------------------------------------- |
| key   | `valueof string`               | The name of the keyword of vendor extension, e.g. `x-custom`. |
| value | `unknown` \| `valueof unknown` | The value of the keyword.                                     |

### `@id` {#@TypeSpec.JsonSchema.id}

Specify the JSON Schema id. If this model or a parent namespace has a base URI,
the provided ID will be relative to that base URI.

By default, the id will be constructed based on the declaration's name.

```typespec
@TypeSpec.JsonSchema.id(id: valueof string)
```

#### Target

`unknown`

#### Parameters

| Name | Type             | Description                                     |
| ---- | ---------------- | ----------------------------------------------- |
| id   | `valueof string` | The id of the JSON schema for this declaration. |

### `@jsonSchema` {#@TypeSpec.JsonSchema.jsonSchema}

Add to namespaces to emit models within that namespace to JSON schema.
Add to another declaration to emit that declaration to JSON schema.

Optionally, for namespaces, you can provide a baseUri, and for other declarations,
you can provide the id.

```typespec
@TypeSpec.JsonSchema.jsonSchema(baseUri?: valueof string)
```

#### Target

`unknown`

#### Parameters

| Name    | Type             | Description                                         |
| ------- | ---------------- | --------------------------------------------------- |
| baseUri | `valueof string` | Schema IDs are interpreted as relative to this URI. |

### `@maxContains` {#@TypeSpec.JsonSchema.maxContains}

Used in conjunction with the `@contains` decorator,
specifies that the array must contain at most a certain number of the types provided by the `@contains` decorator.

```typespec
@TypeSpec.JsonSchema.maxContains(value: valueof int32)
```

#### Target

`unknown[] | ModelProperty`

#### Parameters

| Name  | Type            | Description                                            |
| ----- | --------------- | ------------------------------------------------------ |
| value | `valueof int32` | The maximum number of instances the array must contain |

### `@maxProperties` {#@TypeSpec.JsonSchema.maxProperties}

Specify the maximum number of properties this object can have.

```typespec
@TypeSpec.JsonSchema.maxProperties(value: valueof int32)
```

#### Target

`Record<unknown> | ModelProperty`

#### Parameters

| Name  | Type            | Description                                            |
| ----- | --------------- | ------------------------------------------------------ |
| value | `valueof int32` | The maximum number of properties this object can have. |

### `@minContains` {#@TypeSpec.JsonSchema.minContains}

Used in conjunction with the `@contains` decorator,
specifies that the array must contain at least a certain number of the types provided by the `@contains` decorator.

```typespec
@TypeSpec.JsonSchema.minContains(value: valueof int32)
```

#### Target

`unknown[] | ModelProperty`

#### Parameters

| Name  | Type            | Description                                            |
| ----- | --------------- | ------------------------------------------------------ |
| value | `valueof int32` | The minimum number of instances the array must contain |

### `@minProperties` {#@TypeSpec.JsonSchema.minProperties}

Specify the minimum number of properties this object can have.

```typespec
@TypeSpec.JsonSchema.minProperties(value: valueof int32)
```

#### Target

`Record<unknown> | ModelProperty`

#### Parameters

| Name  | Type            | Description                                            |
| ----- | --------------- | ------------------------------------------------------ |
| value | `valueof int32` | The minimum number of properties this object can have. |

### `@multipleOf` {#@TypeSpec.JsonSchema.multipleOf}

Specify that the numeric type must be a multiple of some numeric value.

```typespec
@TypeSpec.JsonSchema.multipleOf(value: valueof numeric)
```

#### Target

`numeric | ModelProperty`

#### Parameters

| Name  | Type              | Description                                        |
| ----- | ----------------- | -------------------------------------------------- |
| value | `valueof numeric` | The numeric type must be a multiple of this value. |

### `@oneOf` {#@TypeSpec.JsonSchema.oneOf}

Specify that `oneOf` should be used instead of `anyOf` for that union.

```typespec
@TypeSpec.JsonSchema.oneOf
```

#### Target

`Union | ModelProperty`

#### Parameters

None

### `@prefixItems` {#@TypeSpec.JsonSchema.prefixItems}

Specify that the target array must begin with the provided types.

```typespec
@TypeSpec.JsonSchema.prefixItems(value: unknown[])
```

#### Target

`unknown[] | ModelProperty`

#### Parameters

| Name  | Type        | Description                                                                 |
| ----- | ----------- | --------------------------------------------------------------------------- |
| value | `unknown[]` | A tuple containing the types that must be present at the start of the array |

### `@uniqueItems` {#@TypeSpec.JsonSchema.uniqueItems}

Specify that every item in the array must be unique.

```typespec
@TypeSpec.JsonSchema.uniqueItems
```

#### Target

`unknown[] | ModelProperty`

#### Parameters

None

# Decorators

Decorators exported by @typespec/openapi3

## TypeSpec.OpenAPI

### `@oneOf` {#@TypeSpec.OpenAPI.oneOf}

Specify that `oneOf` should be used instead of `anyOf` for that union.

```typespec
@TypeSpec.OpenAPI.oneOf
```

#### Target

`Union | ModelProperty`

#### Parameters

None

### `@useRef` {#@TypeSpec.OpenAPI.useRef}

Specify an external reference that should be used inside of emitting this type.

```typespec
@TypeSpec.OpenAPI.useRef(ref: valueof string)
```

#### Target

`Model | ModelProperty`

#### Parameters

| Name | Type             | Description                                                          |
| ---- | ---------------- | -------------------------------------------------------------------- |
| ref  | `valueof string` | External reference(e.g. "../../common.json#/components/schemas/Foo") |

# Data types

Data types exported by @typespec/protobuf

## TypeSpec.Protobuf

### `Extern` {#TypeSpec.Protobuf.Extern}

A model that represents an external Protobuf reference. This type can be used to import and utilize Protobuf
declarations that are not declared in TypeSpec within TypeSpec sources. When the emitter encounters an `Extern`, it
will insert an `import` statement for the corresponding `Path` and refer to the type by `Name`.

#### Usage

If you have a file called `test.proto` that declares a package named `test` and a message named `Widget`, you can
use the `Extern` type to declare a model in TypeSpec that refers to your external definition of `test.Widget`. See
the example below.

When the TypeSpec definition of `Widget` is encountered, the Protobuf emitter will represent it as a reference to
`test.Widget` and insert an import for it, rather than attempt to convert the model to an equivalent message.

```typespec
model TypeSpec.Protobuf.Extern<Path, Name>
```

#### Template Parameters

| Name | Description                                                                              |
| ---- | ---------------------------------------------------------------------------------------- |
| Path | the relative path to a `.proto` file to import                                           |
| Name | the fully-qualified reference to the type this model represents within the `.proto` file |

#### Examples

```typespec
model Widget is Extern<"path/to/test.proto", "test.Widget">;
```

#### Properties

| Name     | Type    | Description |
| -------- | ------- | ----------- |
| \_extern | `never` |             |

### `Map` {#TypeSpec.Protobuf.Map}

A type representing a Protobuf `map`. Instances of this type in models will be converted to the built-in `map` type
in Protobuf.

The key type of a Protobuf `map` must be any integral type or `string`. The value type can be any type other than
another `Map`.

```typespec
model TypeSpec.Protobuf.Map<Key, Value>
```

#### Template Parameters

| Name  | Description                                      |
| ----- | ------------------------------------------------ |
| Key   | the key type (any integral type or string)       |
| Value | the value type (any type other than another map) |

#### Properties

None

### `PackageDetails` {#TypeSpec.Protobuf.PackageDetails}

Details applied to a package definition by the [`@package`](./decorators#

```typespec
model TypeSpec.Protobuf.PackageDetails
```

#### Properties

| Name     | Type                                   | Description                                                                                                                                                                                                                                           |
| -------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name?    | `string`                               | The package's name.<br /><br />By default, the package's name is constructed from the namespace it is applied to.                                                                                                                                     |
| options? | `Record<string \| boolean \| numeric>` | The package's top-level options.<br /><br />See the [Protobuf Language Guide - Options](https://protobuf.dev/programming-guides/proto3/#options) for more information.<br /><br />Currently, only string, boolean, and numeric options are supported. |

### `StreamMode` {#TypeSpec.Protobuf.StreamMode}

The streaming mode of an operation. One of:

- `Duplex`: both the input and output of the operation are streaming.
- `In`: the input of the operation is streaming.
- `Out`: the output of the operation is streaming.
- `None`: neither the input nor the output are streaming.

See the [`@stream`](./decorators#

```typespec
enum TypeSpec.Protobuf.StreamMode
```

| Name   | Value | Description                                                                                                                                                     |
| ------ | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Duplex |       | Both the input and output of the operation are streaming. Both the client and service will stream messages to each<br />other until the connections are closed. |
| In     |       | The input of the operation is streaming. The client will send a stream of events; and, once the stream is closed,<br />the service will respond with a message. |
| Out    |       | The output of the operation is streaming. The client will send a message to the service, and the service will send<br />a stream of events back to the client.  |
| None   |       | Neither the input nor the output are streaming. This is the default mode of an operation without the `@stream`<br />decorator.                                  |

### `fixed32` {#TypeSpec.Protobuf.fixed32}

An unsigned 32-bit integer that will use the `fixed32` encoding when used in a Protobuf message.

#### Protobuf binary format

Always four bytes. More efficient than `uint32` if values are often greater than 2<sup>28</sup>.

```typespec
scalar TypeSpec.Protobuf.fixed32
```

### `fixed64` {#TypeSpec.Protobuf.fixed64}

An unsigned 64-bit integer that will use the `fixed64` encoding when used in a Protobuf message.

#### Protobuf binary format

Always eight bytes. More efficient than `uint64` if values are often greater than 2<sup>56</sup>.

```typespec
scalar TypeSpec.Protobuf.fixed64
```

### `sfixed32` {#TypeSpec.Protobuf.sfixed32}

A signed 32-bit integer that will use the `sfixed32` encoding when used in a Protobuf message.

#### Protobuf binary format

Always four bytes.

```typespec
scalar TypeSpec.Protobuf.sfixed32
```

### `sfixed64` {#TypeSpec.Protobuf.sfixed64}

A signed 64-bit integer that will use the `sfixed64` encoding when used in a Protobuf message.

#### Protobuf binary format

Always eight bytes.

```typespec
scalar TypeSpec.Protobuf.sfixed64
```

### `sint32` {#TypeSpec.Protobuf.sint32}

A signed 32-bit integer that will use the `sint32` encoding when used in a Protobuf message.

#### Protobuf binary format

Uses variable-length encoding. These more efficiently encode negative numbers than regular int32s.

```typespec
scalar TypeSpec.Protobuf.sint32
```

### `sint64` {#TypeSpec.Protobuf.sint64}

A signed 64-bit integer that will use the `sint64` encoding when used in a Protobuf message.

#### Protobuf binary format

Uses variable-length encoding. These more efficiently encode negative numbers than regular `int64s`.

```typespec
scalar TypeSpec.Protobuf.sint64
```

## TypeSpec.Protobuf.WellKnown

### `Any` {#TypeSpec.Protobuf.WellKnown.Any}

Any value.

This model references `google.protobuf.Any` from `google/protobuf/any.proto`.

```typespec
model TypeSpec.Protobuf.WellKnown.Any
```

#### Properties

| Name     | Type    | Description |
| -------- | ------- | ----------- |
| \_extern | `never` |             |

### `Empty` {#TypeSpec.Protobuf.WellKnown.Empty}

An empty message.

This model references `google.protobuf.Empty` from `google/protobuf/empty.proto`.

```typespec
model TypeSpec.Protobuf.WellKnown.Empty
```

#### Properties

| Name     | Type    | Description |
| -------- | ------- | ----------- |
| \_extern | `never` |             |

### `LatLng` {#TypeSpec.Protobuf.WellKnown.LatLng}

A latitude and longitude.

This model references `google.type.LatLng` from `google/type/latlng.proto`.

```typespec
model TypeSpec.Protobuf.WellKnown.LatLng
```

#### Properties

| Name     | Type    | Description |
| -------- | ------- | ----------- |
| \_extern | `never` |             |

### `Timestamp` {#TypeSpec.Protobuf.WellKnown.Timestamp}

A timestamp.

This model references `google.protobuf.Timestamp` from `google/protobuf/timestamp.proto`.

```typespec
model TypeSpec.Protobuf.WellKnown.Timestamp
```

#### Properties

| Name     | Type    | Description |
| -------- | ------- | ----------- |
| \_extern | `never` |             |

# Decorators

Decorators exported by @typespec/protobuf

## TypeSpec.Protobuf

### `@field` {#@TypeSpec.Protobuf.field}

Defines the field index of a model property for conversion to a Protobuf
message.

The field index of a Protobuf message must:

- fall between 1 and 2<sup>29</sup> - 1, inclusive.
- not fall within the implementation reserved range of 19000 to 19999, inclusive.
- not fall within any range that was [marked reserved](#

```typespec
@TypeSpec.Protobuf.field(index: valueof uint32)
```

#### Target

`ModelProperty`

#### Parameters

| Name  | Type             | Description                          |
| ----- | ---------------- | ------------------------------------ |
| index | `valueof uint32` | The whole-number index of the field. |

#### Examples

```typespec
model ExampleMessage {
  @field(1)
  test: string;
}
```

### `@message` {#@TypeSpec.Protobuf.message}

Declares that a model is a Protobuf message.

Messages can be detected automatically if either of the following two conditions are met:

- The model has a `@field` annotation on all of its properties.
- The model is referenced by any service operation.

This decorator will force the emitter to check and emit a model.

```typespec
@TypeSpec.Protobuf.message
```

#### Target

`{}`

#### Parameters

None

### `@package` {#@TypeSpec.Protobuf.package}

Declares that a TypeSpec namespace constitutes a Protobuf package. The contents of the namespace will be emitted to a
single Protobuf file.

```typespec
@TypeSpec.Protobuf.package(details?: TypeSpec.Protobuf.PackageDetails)
```

#### Target

`Namespace`

#### Parameters

| Name    | Type                                                                 | Description                         |
| ------- | -------------------------------------------------------------------- | ----------------------------------- |
| details | [`PackageDetails`](./data-types.md#TypeSpec.Protobuf.PackageDetails) | the optional details of the package |

### `@reserve` {#@TypeSpec.Protobuf.reserve}

Reserve a field index, range, or name. If a field definition collides with a reservation, the emitter will produce
an error.

This decorator accepts multiple reservations. Each reservation is one of the following:

- a `string`, in which case the reservation refers to a field name.
- a `uint32`, in which case the reservation refers to a field index.
- a tuple `[uint32, uint32]`, in which case the reservation refers to a field range that is _inclusive_ of both ends.

Unlike in Protobuf, where field name and index reservations must be separated, you can mix string and numeric field
reservations in a single `@reserve` call in TypeSpec.

#### API Compatibility Note

Field reservations prevent users of your Protobuf specification from using the given field names or indices. This can
be useful if a field is removed, as it will further prevent adding a new, incompatible field and will prevent users
from utilizing the field index at runtime in a way that may break compatibility with users of older specifications.

See _[Protobuf Language Guide - Reserved Fields](https://protobuf.dev/programming-guides/proto3/#reserved)_ for more
information.

```typespec
@TypeSpec.Protobuf.reserve(...reservations: valueof string | [uint32, uint32] | uint32[])
```

#### Target

`{}`

#### Parameters

| Name         | Type                                             | Description                  |
| ------------ | ------------------------------------------------ | ---------------------------- |
| reservations | `valueof string \| [uint32, uint32] \| uint32[]` | a list of field reservations |

#### Examples

```typespec
// Reserve the fields 8-15 inclusive, 100, and the field name "test" within a model.
@reserve([8, 15], 100, "test")
model Example {
  // ...
}
```

### `@service` {#@TypeSpec.Protobuf.service}

Declares that a TypeSpec interface constitutes a Protobuf service. The contents of the interface will be converted to
a `service` declaration in the resulting Protobuf file.

```typespec
@TypeSpec.Protobuf.service
```

#### Target

`Interface`

#### Parameters

None

### `@stream` {#@TypeSpec.Protobuf.stream}

Set the streaming mode of an operation. See [StreamMode](./data-types#TypeSpec.Protobuf.StreamMode) for more information.

```typespec
@TypeSpec.Protobuf.stream(mode: TypeSpec.Protobuf.StreamMode)
```

#### Target

`Operation`

#### Parameters

| Name | Type                                                         | Description                                    |
| ---- | ------------------------------------------------------------ | ---------------------------------------------- |
| mode | [`StreamMode`](./data-types.md#TypeSpec.Protobuf.StreamMode) | The streaming mode to apply to this operation. |

#### Examples

```typespec
@stream(StreamMode.Out)
op logs(...LogsRequest): LogEvent;
```

```typespec
@stream(StreamMode.Duplex)
op connectToMessageService(...Message): Message;
```

# Getting Started with TypeSpec For REST APIs

Getting started with REST - 01 setup basic syntax

import { FileTree } from "@astrojs/starlight/components";

## Introduction

Welcome to our tutorial on using TypeSpec to define REST APIs with HTTP. In this section, we'll introduce you to TypeSpec, help you set up your development environment, and cover the basic syntax and structure of TypeSpec. By the end of this section, you'll have a solid foundation to build upon in the subsequent sections.

### What is TypeSpec?

TypeSpec is a language and toolset developed by Microsoft for defining data models and service APIs. It provides a structured way to describe the shape and behavior of data and services, ensuring consistency and reducing errors in API development. With TypeSpec, you can generate code, documentation, and other artifacts from your API definitions, making it easier to maintain and evolve your services. Microsoft uses TypeSpec internally to define APIs for various products and services, including Azure.

TypeSpec is used to define the **interface** of your API, which clients will use to interact with resources provided by your service. This includes specifying the operations, request and response models, and error handling mechanisms. The actual API logic is implemented in the backend service, which processes the requests and communicates with the database.

Before we start writing TypeSpec code, we need to set up our development environment. For detailed instructions on setting up your environment, please refer to the [Installation Guide](../../../).

### Summary of Setup and Installation

1. **Install Node.js**: Download and install Node.js from [nodejs.org](https://nodejs.org/). This will also install npm, the Node.js package manager. The minimum versions required are Node.js 20.0.0 and npm 7.0.0.
2. **Install TypeSpec CLI**: Run `npm install -g @typespec/compiler` to install the TypeSpec CLI.
3. **Verify Installation**: Run `tsp --version` to verify that the TypeSpec CLI is installed correctly.
4. **Create a New Project**:
   - Run `tsp init` and select the `Generic REST API` template.
   - Run `tsp install` to install dependencies.
   - Run `tsp compile .` to compile the initial file.
   - Run `tsp compile . --watch` to automatically compile changes on save.

### Project Structure Overview

Once you've completed these steps, you'll have a basic TypeSpec project set up. Here's an overview of the files and directories in your TypeSpec project:

{/* prettier-ignore */}
<FileTree>
- main.tsp
- tspconfig.yaml
- package.json
- node_modules/
- tsp-output/
  - @typespec/
    - openapi3/
      - openapi.yaml
</FileTree>

- **main.tsp**: Entry point for TypeSpec definitions.
- **tspconfig.yaml**: TypeSpec compiler configuration.
- **package.json**: Project metadata and dependencies.
- **node_modules/**: Installed dependencies.
- **tsp-output/**: Generated files.
- **openapi.yaml**: Generated OpenAPI specification.

As we work through the tutorial, keep the openapi.yaml file open in Visual Studio or VS Code to watch the API specification evolve as we make changes.

## Basic Syntax and Structure

Now that we have our environment set up, let's dive into the basic syntax and structure of TypeSpec. We'll create a simple REST API for a pet store by introducing concepts in a layered fashion, increasing complexity as we progress through the tutorial.

As the tutorial advances and the code examples grow more complex, we'll highlight changes in the code to help you easily spot where new lines have been added.

### Import and Using Statements

Before defining models and services, we need to import the necessary TypeSpec libraries and make them available in our namespace.

As we progress through the tutorial, you can follow along by updating the `main.tsp` file in your project and compiling the changes to see the results reflected in the generated `openapi.yaml` specification.

You can also alternatively use the `Try it` feature with the code samples to quickly view the generated OpenAPI spec in your browser via the TypeSpec Playground.

Let's begin by adding the following import and using statements to the `main.tsp` file:

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}"
import "@typespec/http";

using Http;
```

In this example:

- `import` statement brings in the [TypeSpec HTTP library](../../../libraries/http/reference/), which provides the decorators and models we'll be using to define our REST API.
- `using` statement makes the imported library available in the current namespace, allowing us to use its features and decorators.

**NOTE: Your generated project file likely already has these import/using statements, plus import/using for the `@typespec/openapi3` library. The `@typespec/openapi3` library is necessary for emitting the OpenAPI specification file but is not required for creating our Pet Store API in TypeSpec. Remove them from your `main.tsp` file so your code matches the example above.**

## Defining a REST Service

A REST service in TypeSpec is defined using the [`@service`](../../../standard-library/built-in-decorators/#@service) decorator. This decorator allows you to specify metadata about your service, such as its title. Additionally, you can use the [`@server`](../../../libraries/http/reference/decorators/#@TypeSpec.Http.server) decorator to define the server endpoint where your service will be hosted.

### Example: Defining a Service with a Title and Server Endpoint

Let's start by defining a simple REST service for a Pet Store:

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={4-7}
import "@typespec/http";

using Http;
@service(#{
  title: "Pet Store",
})
@server("https://example.com", "Single server endpoint")
```

In this example:

- The `@service` decorator is used to define a service with the title "Pet Store".
- The `@server` decorator specifies the server endpoint for the service, which is "https://example.com".

**OpenAPI Comparison**: In OpenAPI, this is similar to defining the `info` object (which includes the title) and the `servers` array (which includes the server URL).

**NOTE: This code will not compile as-is because we've not yet defined a `namespace` for these decorators to apply to. We'll cover that topic next.**

## Organizing with Namespaces

[Namespaces](../../language-basics/namespaces.md) in TypeSpec help you organize your models and operations logically. They act as containers for related definitions, making your API easier to manage and understand.

### Example: Creating a Namespace

Let's create a namespace for our Pet Store service:

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={8}
import "@typespec/http";

using Http;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
namespace PetStore;
```

In this example:

- The `namespace` keyword is used to define a top-level namespace named `PetStore`.
- All models and operations related to the Pet Store service will be defined within this namespace.
- The first use of namespace defines the top-level namespace and does not require brackets. This is because it serves as the primary container for all related definitions.
- Any subsequent namespaces defined within this top-level namespace will require brackets {} to indicate that they are nested within the top-level namespace.

**OpenAPI Comparison**: In OpenAPI, namespaces are similar to using tags to group related operations and definitions.

## Defining Models

In TypeSpec, a [model](../../language-basics/models.md) is a fundamental building block used to define the structure of data. Models are used to represent entities, such as a `Pet`, with various properties that describe the entity's attributes.

### Example: Defining a Simple Model

Let's define a simple model for a `Pet`:

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={9-22}
import "@typespec/http";

using Http;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
namespace PetStore;

model Pet {
  id: int32;
  name: string;
  age: int32;
  kind: petType;
}

enum petType {
  dog: "dog",
  cat: "cat",
  fish: "fish",
  bird: "bird",
  reptile: "reptile",
}
```

In this example:

- The `model` keyword is used to define a new model named `Pet`.
- The `Pet` model has four properties: `id`, `name`, `age`, and `kind`.
- The `petType` [`enum`](../../language-basics/enums.md) defines possible values for the `kind` property.

**OpenAPI Comparison**: In OpenAPI, this is similar to defining a `schema` object under the `components` section, where you define the structure and properties of your data models.

### Example: Adding Validation Annotations

We can add [validation](../../../language-basics/values/#validation) annotations to our model properties to enforce certain constraints:

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={12,15-16}
import "@typespec/http";

using Http;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
namespace PetStore;

model Pet {
  id: int32;

  @minLength(1)
  name: string;

  @minValue(0)
  @maxValue(100)
  age: int32;

  kind: petType;
}

enum petType {
  dog: "dog",
  cat: "cat",
  fish: "fish",
  bird: "bird",
  reptile: "reptile",
}
```

In this example:

- `@minLength(1)` ensures that the `name` property has at least one character.
- `@minValue(0)` and `@maxValue(100)` ensure that the `age` property is between 0 and 100.

**OpenAPI Comparison**: In OpenAPI, this is similar to using `minLength`, `minimum`, and `maximum` constraints within the `schema` object.

## Conclusion

In this section, we introduced you to TypeSpec, set up the development environment, and covered basic language syntax and structure. We defined a simple REST service, organized our API using namespaces, and defined a model with validation annotations.

With this foundational knowledge, you're now ready to dive deeper into defining operations and handling different types of responses in your REST API. In the next section, we'll expand our API by adding CRUD operations.

# Operations and Responses

Getting started with REST - 02 defining CRUD operations

## Introduction

In this section, we'll build upon the basics we covered in the previous section. We'll define CRUD operations (Create, Read, Update, Delete) for our Pet Store API and discuss the benefits of using nested namespaces.

## Defining CRUD Operations

Next, we'll discuss how to define CRUD operations for our API. We'll cover operations for `Creating`, `Reading`, `Updating`, and `Deleting` pets, all within a nested namespace for better organization.

### Example: Adding CRUD Operations

Let's define the CRUD operations for our `Pet` model:

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={30-60}
import "@typespec/http";

using Http;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
namespace PetStore;

model Pet {
  id: int32;

  @minLength(1)
  name: string;

  @minValue(0)
  @maxValue(100)
  age: int32;

  kind: petType;
}

enum petType {
  dog: "dog",
  cat: "cat",
  fish: "fish",
  bird: "bird",
  reptile: "reptile",
}

@route("/pets")
namespace Pets {
  @get
  op listPets(): {
    @statusCode statusCode: 200;
    @body pets: Pet[];
  };

  @get
  op getPet(@path petId: int32): {
    @statusCode statusCode: 200;
    @body pet: Pet;
  };

  @post
  op createPet(@body pet: Pet): {
    @statusCode statusCode: 201;
    @body newPet: Pet;
  };

  @put
  op updatePet(@path petId: int32, @body pet: Pet): {
    @statusCode statusCode: 200;
    @body updatedPet: Pet;
  };

  @delete
  op deletePet(@path petId: int32): {
    @statusCode statusCode: 204;
  };
}
```

In this example:

- The `@route` decorator defines the base path for the `Pets` namespace.
- The `listPets` operation lists all pets.
- The `getPet` operation retrieves a specific pet by its `petId`.
- The `createPet` operation creates a new pet.
- The `updatePet` operation updates an existing pet.
- The `deletePet` operation deletes an existing pet.

### Benefits of Nested Namespaces

Using nested namespaces in TypeSpec provides several benefits:

1. **Organization**: Grouping related operations under a common namespace makes the API easier to manage and understand.
2. **Operation IDs**: The TypeSpec compiler appends the namespace name to the `operationId` in the OpenAPI spec, making it clear which resource each operation is intended to operate on.
3. **Clarity**: It helps in avoiding naming conflicts and provides a clear structure for the API.

#### Example: Operation ID in OpenAPI Spec

For the `listPets` operation defined in the `Pets` namespace, the OpenAPI spec will generate an `operationId` like `Pets_listPets`, making it clear that this operation is related to the `Pets` resource.

### Example: Route URLs for CRUD Operations

Here's what the route URLs will look like for the CRUD operations defined in the `Pets` namespace:

- **List Pets**: `GET https://example.com/pets`
  - Retrieves a list of all pets.
- **Get Pet by ID**: `GET https://example.com/pets/{petId}`
  - Retrieves a specific pet by its `petId`.
- **Create Pet**: `POST https://example.com/pets`
  - Creates a new pet.
- **Update Pet by ID**: `PUT https://example.com/pets/{petId}`
  - Updates an existing pet by its `petId`.
- **Delete Pet by ID**: `DELETE https://example.com/pets/{petId}`
  - Deletes an existing pet by its `petId`.

### Operation Flowchart

For clarity, here's a flowchart that depicts the flow of data and operations within the API:

```
[Client] --> [API Gateway] --> [listPets Operation] --> [Database] --> [Response: List of Pets]
[Client] --> [API Gateway] --> [getPet Operation] --> [Database] --> [Response: Pet Details]
[Client] --> [API Gateway] --> [createPet Operation] --> [Database] --> [Response: Created Pet]
[Client] --> [API Gateway] --> [updatePet Operation] --> [Database] --> [Response: Updated Pet]
[Client] --> [API Gateway] --> [deletePet Operation] --> [Database] --> [Response: Deletion Confirmation]
```

## Handling Different Types of Responses

In a real-world API, different operations might return different types of successful responses. Let's see how we can handle various response scenarios in TypeSpec.

### Example: Handling Different Status Codes

Let's update our pet operations to return different status codes based on the outcome.

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={42-43,50-52,59-60}
import "@typespec/http";

using Http;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
namespace PetStore;

model Pet {
  id: int32;

  @minLength(1)
  name: string;

  @minValue(0)
  @maxValue(100)
  age: int32;

  kind: petType;
}

enum petType {
  dog: "dog",
  cat: "cat",
  fish: "fish",
  bird: "bird",
  reptile: "reptile",
}

@route("/pets")
namespace Pets {
  @get
  op listPets(): {
    @statusCode statusCode: 200;
    @body pets: Pet[];
  };

  @get
  op getPet(@path petId: int32): {
    @statusCode statusCode: 200;
    @body pet: Pet;
  } | {
    @statusCode statusCode: 404;
  };

  @post
  op createPet(@body pet: Pet): {
    @statusCode statusCode: 201;
    @body newPet: Pet;
  } | {
    @statusCode statusCode: 202;
    @body acceptedPet: Pet;
  };

  @put
  op updatePet(@path petId: int32, @body pet: Pet): {
    @statusCode statusCode: 200;
    @body updatedPet: Pet;
  } | {
    @statusCode statusCode: 404;
  };

  @delete
  op deletePet(@path petId: int32): {
    @statusCode statusCode: 204;
  };
}
```

In this example:

- The pet operations are updated to handle different status codes, depending on the outcome of the operation reported by the backend service.

**Explanation of the `|` Operator**:

- The `|` operator is used to define multiple possible responses for an operation. Each response block specifies a different status code and response body.
- In the `createPet` operation, for example, the `|` operator allows the operation to return either a 201 status code with a `newPet` object or a 202 status code with an `acceptedPet` object.

### OpenAPI Spec Mapping

Here is how the TypeSpec operation definitions map to the OpenAPI specification:

<table>
<tr>
<td>TypeSpec Definition</td>
<td>OpenAPI Spec</td>
</tr>
<td>

```tsp
@route("/pets")
namespace Pets {
@get
op listPets(): {
@statusCode statusCode: 200;
@body pets: Pet[];
};

@get
op getPet(@path petId: int32): {
@statusCode statusCode: 200;
@body pet: Pet;
} | {
@statusCode statusCode: 404;
};

@post
op createPet(@body pet: Pet): {
@statusCode statusCode: 201;
@body newPet: Pet;
} | {
@statusCode statusCode: 202;
@body acceptedPet: Pet;
};

@put
op updatePet(@path petId: int32, @body pet: Pet):{
@statusCode statusCode: 200;
@body updatedPet: Pet;
} | {
@statusCode statusCode: 404;
} | {
@statusCode statusCode: 500;
};

@delete
op deletePet(@path petId: int32): {
@statusCode statusCode: 204;
@body NoContentResponse;
} | {
@statusCode statusCode: 404;
};
}
```

</td>
<td>

```yml
paths:
  /pets:
    get:
      operationId: Pets_listPets
      parameters: []
      responses:
        "200":
          description: The request has succeeded.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/Pet"
    post:
      operationId: Pets_createPet
      parameters: []
      responses:
        "201":
          description: The request has succeeded and a new resource has been created as a result.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Pet"
        "202":
          description: The request has been accepted for processing, but processing has not yet completed.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Pet"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Pet"
  /pets/{petId}:
    get:
      operationId: Pets_getPet
      parameters:
        - name: petId
          in: path
          required: true
          schema:
            type: integer
            format: int32
      responses:
        "200":
          description: The request has succeeded.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Pet"
        "404":
          description: The server cannot find the requested resource.
    put:
      operationId: Pets_updatePet
      parameters:
        - name: petId
          in: path
          required: true
          schema:
            type: integer
            format: int32
      responses:
        "200":
          description: The request has succeeded.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Pet"
        "404":
          description: The server cannot find the requested resource.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Pet"
    delete:
      operationId: Pets_deletePet
      parameters:
        - name: petId
          in: path
          required: true
          schema:
            type: integer
            format: int32
      responses:
        "204":
          description: "There is no content to send for this request, but the headers may be useful. "
```

</td>
</table>

**Note**: As you can see, TypeSpec is much more compact and easier to read compared to the equivalent OpenAPI specification.

## Conclusion

In this section, we demonstrated how to define CRUD operations for your REST API using TypeSpec and discussed the benefits of using nested namespaces. We also covered how to handle different types of successful responses.

In the next section, we'll dive deeper into handling errors in your REST API, including defining custom response models for error handling.

# Handling Errors

Getting started with REST - 03 handling errors in your API

## Introduction

In this section, we'll focus on handling errors in your REST API. We'll define error models and demonstrate how to add them as possible responses to your CRUD operations.

## Why Use Error Models?

Using error models instead of raw status codes offers several advantages:

1. **Consistency**: Error models ensure that error responses are consistent across your API. This makes it easier for clients to handle errors predictably.
2. **Clarity**: Error models provide clear, structured information about the error, including error codes, messages, and additional details. This helps developers understand what went wrong and how to fix it.
3. **Extensibility**: Error models can be extended to include additional information, such as error details, validation issues, or links to documentation. This makes it easier to provide comprehensive error information.
4. **Documentation**: Error models improve the generated API documentation by clearly defining the structure of error responses. This helps API consumers understand the possible error responses and how to handle them.
5. **Type Safety**: In strongly-typed languages, using error models can provide type safety, ensuring that error responses conform to the expected structure.

## Defining Error Models

Error models can be used to represent different types of errors that your API might return. Let's start by defining some common error models.

### Example: Defining Common Error Models

We'll define models to represent validation errors, not-found errors, and internal server errors:

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={45,55-58,65-76,85-102}
import "@typespec/http";

using Http;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
namespace PetStore;

model Pet {
  id: int32;

  @minLength(1)
  name: string;

  @minValue(0)
  @maxValue(100)
  age: int32;

  kind: petType;
}

enum petType {
  dog: "dog",
  cat: "cat",
  fish: "fish",
  bird: "bird",
  reptile: "reptile",
}

@route("/pets")
namespace Pets {
  @get
  op listPets(): {
    @statusCode statusCode: 200;
    @body pets: Pet[];
  };

  @get
  op getPet(@path petId: int32): {
    @statusCode statusCode: 200;
    @body pet: Pet;
  } | {
    @statusCode statusCode: 404;
    @body error: NotFoundError;
  };

  @post
  op createPet(@body pet: Pet): {
    @statusCode statusCode: 201;
    @body newPet: Pet;
  } | {
    @statusCode statusCode: 202;
    @body acceptedPet: Pet;
  } | {
    @statusCode statusCode: 400;
    @body error: ValidationError;
  };

  @put
  op updatePet(@path petId: int32, @body pet: Pet):
    | {
        @statusCode statusCode: 200;
        @body updatedPet: Pet;
      }
    | {
        @statusCode statusCode: 400;
        @body error: ValidationError;
      }
    | {
        @statusCode statusCode: 404;
        @body error: NotFoundError;
      }
    | {
        @statusCode statusCode: 500;
        @body error: InternalServerError;
      };

  @delete
  op deletePet(@path petId: int32): {
    @statusCode statusCode: 204;
  };
}

@error
model NotFoundError {
  code: "NOT_FOUND";
  message: string;
}

@error
model ValidationError {
  code: "VALIDATION_ERROR";
  message: string;
  details: string[];
}

@error
model InternalServerError {
  code: "INTERNAL_SERVER_ERROR";
  message: string;
}
```

In this example:

- The `NotFoundError`, `ValidationError`, and `InternalServerError` models are defined to represent different types of errors.
- The `@error` decorator is used to indicate that these models represent error responses.
- The Pet Store operations are updated to return the appropriate error models when the service can't perform the requested operation.

## Conclusion

In this section, we focused on defining error handling in your REST API. We introduced error models and demonstrated how to represent different operation response scenarios in TypeSpec.

In the next section, we'll dive into reusing common parameters in your REST API.

# Common Parameters

Getting started with REST - 04 reuse common parameters

## Introduction

In this section, we'll focus on reusing common parameters in your REST API. Common parameters are parameters that are used across multiple operations. By defining these parameters once and reusing them, we can make our API more consistent, easier to read, and easier to maintain.

## Creating a Common Parameters Model

Let's start by defining a model for common parameters. This model will include parameters that will be used across all Pet Store operations.

### Example: Defining Common Parameters

For the sake of demonstration, we're going to require each API call in our Pet Store service to include a request ID, a locale, and a client version. Let's define a model for these common parameters, which we'll label `requestID`, `locale`, and `clientVersion`:

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={30-39}
import "@typespec/http";

using Http;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
namespace PetStore;

model Pet {
  id: int32;

  @minLength(1)
  name: string;

  @minValue(0)
  @maxValue(100)
  age: int32;

  kind: petType;
}

enum petType {
  dog: "dog",
  cat: "cat",
  fish: "fish",
  bird: "bird",
  reptile: "reptile",
}

model CommonParameters {
  @header
  requestID: string;

  @query
  locale?: string;

  @header
  clientVersion?: string;
}
```

In this example:

- The `@header` decorator is used to indicate that `requestID` and `clientVersion` are header parameters.
- The `@query` decorator is used to indicate that `locale` is a query parameter.

## Reusing Common Parameters Across Multiple Operations

Now that we have defined our common parameters model, let's reuse it across multiple operations in our API.

### Example: Reusing Common Parameters in Operations

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={44,50,59,71,90}
import "@typespec/http";

using Http;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
namespace PetStore;

model Pet {
  id: int32;

  @minLength(1)
  name: string;

  @minValue(0)
  @maxValue(100)
  age: int32;

  kind: petType;
}

enum petType {
  dog: "dog",
  cat: "cat",
  fish: "fish",
  bird: "bird",
  reptile: "reptile",
}

model CommonParameters {
  @header
  requestID: string;

  @query
  locale?: string;

  @header
  clientVersion?: string;
}

@route("/pets")
namespace Pets {
  @get
  op listPets(...CommonParameters): {
    @statusCode statusCode: 200;
    @body pets: Pet[];
  };

  @get
  op getPet(@path petId: int32, ...CommonParameters): {
    @statusCode statusCode: 200;
    @body pet: Pet;
  } | {
    @statusCode statusCode: 404;
    @body error: NotFoundError;
  };

  @post
  op createPet(@body pet: Pet, ...CommonParameters): {
    @statusCode statusCode: 201;
    @body newPet: Pet;
  } | {
    @statusCode statusCode: 202;
    @body acceptedPet: Pet;
  } | {
    @statusCode statusCode: 400;
    @body error: ValidationError;
  };

  @put
  op updatePet(@path petId: int32, @body pet: Pet, ...CommonParameters):
    | {
        @statusCode statusCode: 200;
        @body updatedPet: Pet;
      }
    | {
        @statusCode statusCode: 400;
        @body error: ValidationError;
      }
    | {
        @statusCode statusCode: 404;
        @body error: NotFoundError;
      }
    | {
        @statusCode statusCode: 500;
        @body error: InternalServerError;
      };

  @delete
  op deletePet(@path petId: int32, ...CommonParameters): {
    @statusCode statusCode: 204;
  };
}

@error
model NotFoundError {
  code: "NOT_FOUND";
  message: string;
}

@error
model ValidationError {
  code: "VALIDATION_ERROR";
  message: string;
  details: string[];
}

@error
model InternalServerError {
  code: "INTERNAL_SERVER_ERROR";
  message: string;
}
```

In this example:

- The `CommonParameters` model is reused across multiple operations using the [spread operator](../../../language-basics/models/#spread) `(...)`, which tells the TypeSpec compiler to expand the model definition inline.
- This approach ensures that the common parameters are consistently applied to all relevant operations, making the API more maintainable and reducing redundancy.

### Example: OpenAPI Specification for Common Parameters

Let's take a closer look at how the common parameters model with the `spread` operator is represented in the generated OpenAPI specification by looking at the `deletePet` operation:

```yaml ins={14-16,28-45}
#### Generated OpenAPI Specification:

paths:
  /pets/{petId}:
    delete:
      operationId: Pets_deletePet
      parameters:
        - name: petId
          in: path
          required: true
          schema:
            type: integer
            format: int32
        - $ref: "#/components/parameters/CommonParameters.requestID"
        - $ref: "#/components/parameters/CommonParameters.locale"
        - $ref: "#/components/parameters/CommonParameters.clientVersion"
      responses:
        "204":
          description: "There is no content to send for this request, but the headers may be useful."
        "404":
          description: "Not Found"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/NotFoundError"
components:
  parameters:
    CommonParameters.clientVersion:
      name: client-version
      in: header
      required: false
      schema:
        type: string
    CommonParameters.locale:
      name: locale
      in: query
      required: false
      schema:
        type: string
    CommonParameters.requestID:
      name: request-id
      in: header
      required: true
      schema:
        type: string
  schemas:
    NotFoundError:
      type: object
      properties:
        code:
          type: string
          example: "NOT_FOUND"
        message:
          type: string
```

In this example:

- **Parameters Section**: The `deletePet` operation includes the `petId` path parameter and the common parameters (`requestID`, `locale`, and `clientVersion`). The common parameters are referenced using `$ref` to ensure they are consistently defined and reused across multiple operations.
- **Components Section**: The common parameters are defined under the `components` section, ensuring they are reusable and maintainable. Each parameter is specified with its name, location (`in` indicating header or query), whether it is required, and its schema.

### Benefits

1. **Consistency**: Ensures that common parameters are applied consistently across all relevant operations.
2. **Maintainability**: Changes to common parameters need to be made only once in the `CommonParameters` model, reducing redundancy and potential errors.
3. **Clarity**: The generated OpenAPI specification clearly shows which parameters are required for each operation, improving the documentation and usability of the API.

## Conclusion

In this section, we focused on reusing common parameters in your REST API. By defining a common parameters model and reusing it across multiple operations, we can make our API more consistent, easier to read, and easier to maintain.

Next, we'll learn how to add authentication to our REST API.

# Authentication

Getting started with REST - 05 adding authentication

## Introduction

In this section, we'll focus on adding [authentication](../../../libraries/http/authentication/) to your REST API. We'll introduce the `@useAuth` decorator, show how to enforce authentication on specific operations, and provide an example using Bearer authentication.

## Introduction to the `@useAuth` Decorator

The [@useAuth](../../../libraries/http/reference/decorators/#@TypeSpec.Http.useAuth) decorator is used to enforce authentication on specific operations in your REST API. This decorator allows you to specify the authentication mechanism that should be used for the operation. The TypeSpec HTTP library provides support for several authentication models, including `BearerAuth` for Bearer authentication.

Bearer authentication uses tokens for access control. The server generates a token upon login, and the client includes it in the Authorization header for protected resource requests. The server validates the token to grant access to the resource.

### Example: Enforcing Authentication on Specific Operations

Let's update our existing operations by enforcing authentication using the `@useAuth` decorator.We'll add authentication to the operations that modify pet data, such as creating, updating, and deleting pets. We'll also add a new error model for unauthorized access.

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={59,72-75,79,90-92,103,107-109,126-130}
import "@typespec/http";

using Http;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
namespace PetStore;

model Pet {
  id: int32;

  @minLength(1)
  name: string;

  @minValue(0)
  @maxValue(100)
  age: int32;

  kind: petType;
}

enum petType {
  dog: "dog",
  cat: "cat",
  fish: "fish",
  bird: "bird",
  reptile: "reptile",
}

model CommonParameters {
  @header
  requestID: string;

  @query
  locale?: string;

  @header
  clientVersion?: string;
}

@route("/pets")
namespace Pets {
  @get
  op listPets(...CommonParameters): {
    @statusCode statusCode: 200;
    @body pets: Pet[];
  };

  @get
  op getPet(@path petId: int32, ...CommonParameters): {
    @statusCode statusCode: 200;
    @body pet: Pet;
  } | {
    @statusCode statusCode: 404;
    @body error: NotFoundError;
  };

  @post
  @useAuth(BearerAuth)
  op createPet(@body pet: Pet, ...CommonParameters):
    | {
        @statusCode statusCode: 201;
        @body newPet: Pet;
      }
    | {
        @statusCode statusCode: 202;
        @body acceptedPet: Pet;
      }
    | {
        @statusCode statusCode: 400;
        @body error: ValidationError;
      }
    | {
        @statusCode statusCode: 401;
        @body error: UnauthorizedError;
      };

  @put
  @useAuth(BearerAuth)
  op updatePet(@path petId: int32, @body pet: Pet, ...CommonParameters):
    | {
        @statusCode statusCode: 200;
        @body updatedPet: Pet;
      }
    | {
        @statusCode statusCode: 400;
        @body error: ValidationError;
      }
    | {
        @statusCode statusCode: 401;
        @body error: UnauthorizedError;
      }
    | {
        @statusCode statusCode: 404;
        @body error: NotFoundError;
      }
    | {
        @statusCode statusCode: 500;
        @body error: InternalServerError;
      };

  @delete
  @useAuth(BearerAuth)
  op deletePet(@path petId: int32, ...CommonParameters): {
    @statusCode statusCode: 204;
  } | {
    @statusCode statusCode: 401;
    @body error: UnauthorizedError;
  };
}

@error
model NotFoundError {
  code: "NOT_FOUND";
  message: string;
}

@error
model ValidationError {
  code: "VALIDATION_ERROR";
  message: string;
  details: string[];
}

@error
model UnauthorizedError {
  code: "UNAUTHORIZED";
  message: string;
}

@error
model InternalServerError {
  code: "INTERNAL_SERVER_ERROR";
  message: string;
}

model InternalServerErrorResponse {
  @statusCode statusCode: 500;
  @body error: InternalServerError;
}
```

In this example:

- The `@useAuth(BearerAuth)` decorator is applied to the `createPet`, `updatePet`, and `deletePet` operations to enforce authentication using the Bearer authentication mechanism.
- A new error model, `UnauthorizedError`, is defined to handle unauthorized access errors.
- The `UnauthorizedError` model is used in the `createPet`, `updatePet`, and `deletePet` operations to indicate unauthorized access.

### Example: OpenAPI Specification with Authentication

Let's take a closer look at how the `@useAuth` decorator affects the generated OpenAPI specification for the `deletePet` operation.

```yaml ins={15-16,46-49}
paths:
  /pets/{petId}:
    delete:
      operationId: Pets_deletePet
      parameters:
        - name: petId
          in: path
          required: true
          schema:
            type: integer
            format: int32
        - $ref: "#/components/parameters/CommonParameters.requestID"
        - $ref: "#/components/parameters/CommonParameters.locale"
        - $ref: "#/components/parameters/CommonParameters.clientVersion"
      security:
        - BearerAuth: []
      responses:
        "204":
          description: "There is no content to send for this request, but the headers may be useful."
        "404":
          description: "Not Found"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/NotFoundError"
components:
  parameters:
    CommonParameters.clientVersion:
      name: client-version
      in: header
      required: false
      schema:
        type: string
    CommonParameters.locale:
      name: locale
      in: query
      required: false
      schema:
        type: string
    CommonParameters.requestID:
      name: request-id
      in: header
      required: true
      schema:
        type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
  schemas:
    NotFoundError:
      type: object
      properties:
        code:
          type: string
          example: "NOT_FOUND"
        message:
          type: string
```

### Explanation

- **Security Section**: The `security` section in the `deletePet` operation specifies that Bearer authentication is required. This is indicated by the `BearerAuth` security scheme.
- **Security Schemes**: The `components` section includes a `securitySchemes` definition for `BearerAuth`, specifying that it uses the HTTP bearer authentication scheme.

### Benefits

1. **Security**: Ensures that only authorized clients can perform certain actions by enforcing authentication on specific operations.
2. **Consistency**: The use of common parameters and authentication mechanisms is consistently applied across relevant operations.
3. **Clarity**: The generated OpenAPI specification clearly shows which operations require authentication and which parameters are needed, improving the documentation and usability of the API.

## Conclusion

In this section, we focused on adding authentication to your REST API using TypeSpec. By using the `@useAuth` decorator, we can enforce authentication on specific operations, ensuring that only authorized clients can perform certain actions.

In the next section, we'll dive into versioning your REST API. Versioning allows you to introduce new features and improvements while maintaining backward compatibility for existing clients.

# Versioning

Getting started with REST - 06 versioning your REST API

import { FileTree } from "@astrojs/starlight/components";

## Introduction

In this section, we'll focus on implementing versioning in your REST API. Versioning allows you to manage changes to your API over time without breaking existing clients. We'll introduce the `@versioned` decorator, show how to define versions with enums, and demonstrate how to use the `@added` decorator to specify version-specific models and operations.

## Adding the Versioning Library

Before we can use the versioning decorators, we need to add the `@typespec/versioning` library to our project. This involves updating the `package.json` file and installing the necessary dependencies.

### Step 1: Update `package.json`

Add the `@typespec/versioning` library to your `package.json` file, in both the `peerDependencies` and `devDependencies` sections. Your updated `package.json` should look like this:

```json ins={9,15}
{
  "name": "typespec-petstore",
  "version": "0.1.0",
  "type": "module",
  "peerDependencies": {
    "@typespec/compiler": "latest",
    "@typespec/http": "latest",
    "@typespec/openapi3": "latest",
    "@typespec/versioning": "latest"
  },
  "devDependencies": {
    "@typespec/compiler": "latest",
    "@typespec/http": "latest",
    "@typespec/openapi3": "latest",
    "@typespec/versioning": "latest"
  },
  "private": true
}
```

### Step 2: Install Dependencies

Run the following command to install the new dependencies:

```sh
tsp install
```

## Introduction to the `@versioned` Decorator

The [`@versioned`](../../../libraries/versioning/reference/decorators/#@TypeSpec.Versioning.versioned) decorator is used to define different versions of your API. This decorator allows you to specify the versions that your API supports and manage changes across these versions.

### Example: Defining API Versions

Let's define two versions of our API, `v1` and `v2`:

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={2,5,9,12-15}
import "@typespec/http";
import "@typespec/versioning";

using Http;
using Versioning;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
@versioned(Versions)
namespace PetStore;

enum Versions {
  v1: "1.0",
  v2: "2.0",
}
```

In this example:

- We're importing and using a new module, `@typespec/versioning`, which provides versioning support.
- The `@versioned` decorator is used to define the versions supported by the API, defined in the `Versions` enum.
- The `Versions` enum specifies two versions: `v1` (1.0) and `v2` (2.0).

### Generating OpenAPI Specifications for Different Versions

Once versions are added, the TypeSpec compiler generates individual OpenAPI specifications for each version.

{/* prettier-ignore */}
<FileTree>
- main.tsp
- tspconfig.yaml
- package.json
- node_modules/
- tsp-output/
  - @typespec/
    - openapi3
      - openapi.1.0.yaml
      - openapi.2.0.yaml
</FileTree>

Generating separate specs for each version ensures backward compatibility, provides clear documentation for developers to understand differences between versions, and simplifies maintenance by allowing independent updates to each version's specifications.

By encapsulating different versions of the API within the context of the same TypeSpec project, we can manage all versions in a unified manner. This approach makes it easier to maintain consistency, apply updates, and ensure that all versions are properly documented and aligned with the overall API strategy.

## Using the `@added` Decorator

The [`@added`](../../../libraries/versioning/reference/decorators/#@TypeSpec.Versioning.added) decorator is used to indicate that a model or operation was added in a specific version of the API. This allows you to manage changes and additions to your API over time.

### Example: Adding a New Model in a Specific Version

Let's add a `Toy` model that is only available in version 2 of the API:

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={38-42}
import "@typespec/http";
import "@typespec/versioning";

using Http;
using Versioning;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
@versioned(Versions)
namespace PetStore;

enum Versions {
  v1: "1.0",
  v2: "2.0",
}

model Pet {
  id: int32;

  @minLength(1)
  name: string;

  @minValue(0)
  @maxValue(100)
  age: int32;

  kind: petType;
}

enum petType {
  dog: "dog",
  cat: "cat",
  fish: "fish",
  bird: "bird",
  reptile: "reptile",
}

@added(Versions.v2)
model Toy {
  id: int32;
  name: string;
}
```

In this example:

- The `Toy` model is defined with the `@added(Versions.v2)` decorator to indicate that it was added in version 2 of the API.

## Version-Specific Operations

Let's define version-specific operations to manage toys for pets. These operations will only be available in version 2 of the API.

### Example: Adding Version-Specific Operations

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={125-180}
import "@typespec/http";
import "@typespec/versioning";

using Http;
using Versioning;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
@versioned(Versions)
namespace PetStore;

enum Versions {
  v1: "1.0",
  v2: "2.0",
}

model Pet {
  id: int32;

  @minLength(1)
  name: string;

  @minValue(0)
  @maxValue(100)
  age: int32;

  kind: petType;
}

enum petType {
  dog: "dog",
  cat: "cat",
  fish: "fish",
  bird: "bird",
  reptile: "reptile",
}

@added(Versions.v2)
model Toy {
  id: int32;
  name: string;
}

model CommonParameters {
  @header
  requestID: string;

  @query
  locale?: string;

  @header
  clientVersion?: string;
}

@route("/pets")
namespace Pets {
  @get
  op listPets(...CommonParameters): {
    @statusCode statusCode: 200;
    @body pets: Pet[];
  };

  @get
  op getPet(@path petId: int32, ...CommonParameters): {
    @statusCode statusCode: 200;
    @body pet: Pet;
  } | {
    @statusCode statusCode: 404;
    @body error: NotFoundError;
  };

  @post
  @useAuth(BearerAuth)
  op createPet(@body pet: Pet, ...CommonParameters):
    | {
        @statusCode statusCode: 201;
        @body newPet: Pet;
      }
    | {
        @statusCode statusCode: 202;
        @body acceptedPet: Pet;
      }
    | {
        @statusCode statusCode: 400;
        @body error: ValidationError;
      }
    | {
        @statusCode statusCode: 401;
        @body error: UnauthorizedError;
      };

  @put
  @useAuth(BearerAuth)
  op updatePet(@path petId: int32, @body pet: Pet, ...CommonParameters):
    | {
        @statusCode statusCode: 200;
        @body updatedPet: Pet;
      }
    | {
        @statusCode statusCode: 400;
        @body error: ValidationError;
      }
    | {
        @statusCode statusCode: 401;
        @body error: UnauthorizedError;
      }
    | {
        @statusCode statusCode: 404;
        @body error: NotFoundError;
      }
    | {
        @statusCode statusCode: 500;
        @body error: InternalServerError;
      };

  @delete
  @useAuth(BearerAuth)
  op deletePet(@path petId: int32, ...CommonParameters): {
    @statusCode statusCode: 204;
  } | {
    @statusCode statusCode: 401;
    @body error: UnauthorizedError;
  };

  @route("{petId}/toys")
  namespace Toys {
    @added(Versions.v2)
    @get
    op listToys(@path petId: int32, ...CommonParameters): {
      @statusCode statusCode: 200;
      @body toys: Toy[];
    } | {
      @statusCode statusCode: 404;
      @body error: NotFoundError;
    };

    @added(Versions.v2)
    @post
    @useAuth(BearerAuth)
    op createToy(@path petId: int32, @body toy: Toy, ...CommonParameters): {
      @statusCode statusCode: 201;
      @body newToy: Toy;
    } | {
      @statusCode statusCode: 400;
      @body error: ValidationError;
    } | {
      @statusCode statusCode: 401;
      @body error: UnauthorizedError;
    };

    @added(Versions.v2)
    @put
    @useAuth(BearerAuth)
    op updateToy(@path petId: int32, @path toyId: int32, @body toy: Toy, ...CommonParameters):
      | {
          @body updatedToy: Toy;
        }
      | {
          @statusCode statusCode: 400;
          @body error: ValidationError;
        }
      | {
          @statusCode statusCode: 401;
          @body error: UnauthorizedError;
        }
      | {
          @statusCode statusCode: 404;
          @body error: NotFoundError;
        };

    @added(Versions.v2)
    @delete
    @useAuth(BearerAuth)
    op deleteToy(@path petId: int32, @path toyId: int32, ...CommonParameters): {
      @statusCode statusCode: 204;
    } | {
      @statusCode statusCode: 401;
      @body error: UnauthorizedError;
    };
  }
}

@error
model NotFoundError {
  code: "NOT_FOUND";
  message: string;
}

@error
model ValidationError {
  code: "VALIDATION_ERROR";
  message: string;
  details: string[];
}

@error
model UnauthorizedError {
  code: "UNAUTHORIZED";
  message: string;
}

@error
model InternalServerError {
  code: "INTERNAL_SERVER_ERROR";
  message: string;
}

model InternalServerErrorResponse {
  @statusCode statusCode: 500;
  @body error: InternalServerError;
}
```

In this example:

- The `Toys` namespace is defined under the `Pets` namespace.
- The `@added(Versions.v2)` decorator is applied to the operations within the `Toys` namespace to indicate that they were added in version 2 of the API.
- The `Toys` namespace includes operations to list, create, update, and delete toys for a specific pet. These operations are only available in version 2 of the API.

## Conclusion

In the next section, we'll dive into creating custom response models for your REST API.

# Custom Response Models

Getting started with REST - 07 customize API response models

## Introduction

In this section, we'll focus on creating custom response models and demonstrate how to use them in your API operations. We'll also incorporate predefined response models from the TypeSpec HTTP library.

## Introduction to Custom Response Models

Custom response models allow you to define structured responses for your API operations. They help ensure consistency and clarity in your API responses. TypeSpec defines response models for common HTTP responses in the [HTTP library](https://typespec.io/docs/libraries/http/reference), which we can incorporate into our custom response models.

### Common HTTP Status Codes and TypeSpec Response Models

Here are some common HTTP status codes and their equivalent TypeSpec response models from the TypeSpec HTTP library:

| **HTTP Status Code** | **Meaning**                                                                 | **TypeSpec Response Model** |
| -------------------- | --------------------------------------------------------------------------- | --------------------------- |
| 200 OK               | The request was successful, and the server returned the requested resource. | `OkResponse`                |
| 201 Created          | The request was successful, and a new resource was created.                 | `CreatedResponse`           |
| 204 No Content       | The request was successful, but there is no content to return.              | `NoContentResponse`         |
| 400 Bad Request      | The server could not understand the request due to invalid syntax.          | `BadRequestResponse`        |
| 401 Unauthorized     | The client must authenticate itself to get the requested response.          | `UnauthorizedResponse`      |
| 403 Forbidden        | The client does not have access rights to the content.                      | `ForbiddenResponse`         |
| 404 Not Found        | The server cannot find the requested resource.                              | `NotFoundResponse`          |

### Benefits of Using Custom Response Models

- **Reducing Duplication**: By defining common response structures once, you can reuse them across multiple operations.
- **Improving Readability**: Custom response models make your API definitions clearer and easier to understand.
- **Minimizing Errors**: Consistent response models help reduce the likelihood of errors in your API responses.

## Creating Custom Response Models

Let's start by defining and extending some custom response models. These models will incorporate existing response models from the TypeSpec HTTP library to ensure consistency.

### Example: Defining and Extending Custom Response Models

```tsp
model PetListResponse {
  ...OkResponse;
  ...Body<Pet[]>;
}

model PetResponse {
  ...OkResponse;
  ...Body<Pet>;
}

model PetCreatedResponse {
  ...CreatedResponse;
  ...Body<Pet>;
}

model PetErrorResponse {
  ...BadRequestResponse;
  ...Body<ValidationError>;
}

model PetNotFoundResponse {
  ...NotFoundResponse;
  ...Body<NotFoundError>;
}

model PetUnauthorizedResponse {
  ...UnauthorizedResponse;
  ...Body<UnauthorizedError>;
}

model PetSuccessResponse {
  ...OkResponse;
  ...Body<string>;
}

model PetNoContentResponse {
  ...NoContentResponse;
}
```

In this example:

- `PetListResponse` extends `OkResponse` and includes a body with an array of `Pet` objects.
- `PetResponse` extends `OkResponse` and includes a body with a single `Pet` object.
- `PetCreatedResponse` extends `CreatedResponse` and includes a body with a newly created `Pet` object.
- `PetErrorResponse` extends `BadRequestResponse` and includes a body with a `ValidationError` object.
- `PetNotFoundResponse` extends `NotFoundResponse` and includes a body with a `NotFoundError` object.
- `PetUnauthorizedResponse` extends `UnauthorizedResponse` and includes a body with an `UnauthorizedError` object.
- `PetSuccessResponse` extends `OkResponse` and includes a body with a success message.
- `PetNoContentResponse` extends `NoContentResponse` for situations where the request succeeded but there is no content to return.

**Note**: Base response models like `OkResponse`, `CreatedResponse`, `BadRequestResponse`, `NotFoundResponse`, and `UnauthorizedResponse` are imported from the TypeSpec [HTTP data types library](../../../libraries/http/reference/data-types/), which we're importing in our project as `@typespec/http`.

## Using Custom Response Models in Operations

Now that we have defined our custom response models, let's use them in our API operations.

### Example: Applying Custom Response Models to Operations

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}" ins={55-97,102,105,108-112,116-121,125}
import "@typespec/http";
import "@typespec/versioning";

using Http;
using Versioning;

@service(#{ title: "Pet Store" })
@server("https://example.com", "Single server endpoint")
@versioned(Versions)
namespace PetStore;

enum Versions {
  v1: "1.0",
  v2: "2.0",
}

model Pet {
  id: int32;

  @minLength(1)
  name: string;

  @minValue(0)
  @maxValue(100)
  age: int32;

  kind: petType;
}

enum petType {
  dog: "dog",
  cat: "cat",
  fish: "fish",
  bird: "bird",
  reptile: "reptile",
}

@added(Versions.v2)
model Toy {
  id: int32;
  name: string;
}

model CommonParameters {
  @header
  requestID: string;

  @query
  locale?: string;

  @header
  clientVersion?: string;
}

model PetListResponse {
  ...OkResponse;
  ...Body<Pet[]>;
}

model PetResponse {
  ...OkResponse;
  ...Body<Pet>;
}

model PetCreatedResponse {
  ...CreatedResponse;
  ...Body<Pet>;
}

model PetAcceptedResponse {
  ...AcceptedResponse;
  ...Body<Pet>;
}

model PetErrorResponse {
  ...BadRequestResponse;
  ...Body<ValidationError>;
}

model PetNotFoundResponse {
  ...NotFoundResponse;
  ...Body<NotFoundError>;
}

model PetUnauthorizedResponse {
  ...UnauthorizedResponse;
  ...Body<UnauthorizedError>;
}

model PetSuccessResponse {
  ...OkResponse;
  ...Body<string>;
}

model PetNoContentResponse {
  ...NoContentResponse;
}

@route("/pets")
namespace Pets {
  @get
  op listPets(...CommonParameters): PetListResponse;

  @get
  op getPet(@path petId: int32, @header ifMatch?: string): PetResponse | PetNotFoundResponse;
  @useAuth(BearerAuth)
  @post
  op createPet(@body pet: Pet):
    | PetCreatedResponse
    | PetAcceptedResponse
    | PetErrorResponse
    | PetUnauthorizedResponse;

  @useAuth(BearerAuth)
  @put
  op updatePet(@path petId: int32, @body pet: Pet):
    | PetResponse
    | PetErrorResponse
    | PetUnauthorizedResponse
    | PetNotFoundResponse
    | InternalServerErrorResponse;

  @useAuth(BearerAuth)
  @delete
  op deletePet(@path petId: int32): PetNoContentResponse | PetUnauthorizedResponse;

  @route("{petId}/toys")
  namespace Toys {
    @added(Versions.v2)
    @get
    op listToys(@path petId: int32, ...CommonParameters): {
      @body toys: Toy[];
    };

    @added(Versions.v2)
    @post
    @useAuth(BearerAuth)
    op createToy(@path petId: int32, @body toy: Toy, ...CommonParameters): {
      @statusCode statusCode: 201;
      @body newToy: Toy;
    };

    @added(Versions.v2)
    @put
    @useAuth(BearerAuth)
    op updateToy(@path petId: int32, @path toyId: int32, @body toy: Toy, ...CommonParameters): {
      @body updatedToy: Toy;
    };

    @added(Versions.v2)
    @delete
    @useAuth(BearerAuth)
    op deleteToy(@path petId: int32, @path toyId: int32, ...CommonParameters): {
      @statusCode statusCode: 204;
    };
  }
}

@error
model NotFoundError {
  code: "NOT_FOUND";
  message: string;
}

@error
model ValidationError {
  code: "VALIDATION_ERROR";
  message: string;
  details: string[];
}

@error
model UnauthorizedError {
  code: "UNAUTHORIZED";
  message: string;
}

@error
model InternalServerError {
  code: "INTERNAL_SERVER_ERROR";
  message: string;
}

model InternalServerErrorResponse {
  @statusCode statusCode: 500;
  @body error: InternalServerError;
}
```

In this example:

- The `listPets` operation uses the `PetListResponse` custom response model.
- The `getPet` operation uses the `PetResponse` and `PetNotFoundResponse` custom response models.
- The `createPet` operation uses the `PetCreatedResponse`, `PetAcceptedResponse`, `PetErrorResponse`, and `PetUnauthorizedResponse` custom response models.
- The `updatePet` operation uses the `PetResponse`, `PetErrorResponse`, `PetUnauthorizedResponse`, `PetNotFoundResponse`, and `InternalServerErrorResponse` custom response models.
- The `deletePet` operation uses the `PetNoContentResponse` and `PetUnauthorizedResponse` custom response models.

Note that we could also define custom response models for the `Toys` operations, similar to the `Pets` operations. But for brevity, we're omitting them in this example.

## Conclusion

In this section, we focused on creating custom response models in your REST API. By defining and extending custom response models, we can reduce duplication, improve readability, and minimize errors in our API responses. We also incorporated existing response models from the TypeSpec HTTP library to ensure consistency and clarity.

# TypeSpec for OpenAPI Developers

Getting started with TypeSpec for Open API developers

This guide introduces TypeSpec using concepts familiar to developers who build or use API definitions in OpenAPI v2 or v3.

In many cases, this will also describe how the typespec-autorest and openapi3 emitters translate
TypeSpec designs into OpenAPI.

The document is organized around the features of an OpenAPI v2 or v3 definition.
The idea is that if you know how to describe some API feature in OpenAPI, you can just navigate
to the section of this document for that feature.

## Data Types

In OpenAPI [v2](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#data-types)/[v3](https://github.com/OAI/OpenAPI-Specification/blob/3.0.3/versions/3.0.3.md#data-types), data types are specified using the `type` and `format` fields in a schema.

The TypeSpec equivalents of OpenAPI data types are the TypeSpec primitive types or [built-in models](https://typespec.io/docs/language-basics/built-in-types).

### type and format

The following table shows how common OpenAPI types map to TypeSpec types:

| `type:`   | `format:`   | TypeSpec type    | Notes                                                                     |
| --------- | ----------- | ---------------- | ------------------------------------------------------------------------- |
| `integer` | `int32`     | `int32`          |                                                                           |
| `integer` | `int64`     | `int64`          |                                                                           |
| `number`  | `float`     | `float32`        |                                                                           |
| `number`  | `double`    | `float64`        |                                                                           |
| `string`  |             | `string`         |                                                                           |
| `string`  | `byte`      | `bytes`          | for content-type == 'application/json' or 'text/plain'                    |
| `string`  | `binary`    | `bytes`          | for "binary" content types, e.g. 'application/octet-stream', 'image/jpeg' |
| `string`  | `date`      | `plainDate`      |                                                                           |
| `string`  | `date-time` | `utcDateTime`    | RFC 3339 date in coordinated universal time (UTC)                         |
| `string`  | `date-time` | `offsetDateTime` | RFC 3339 date with offset                                                 |
| `string`  | `password`  | `@secret string` |                                                                           |
| `boolean` |             | `boolean`        |                                                                           |

You can also define a property with no type specified using the TypeSpec `unknown` type.

```typespec
model Example {
  /** This property has no `type` defined. */
  noType?: unknown;
}
```

OpenAPI allows any string as a format, and there is a [registry of common formats][Format Registry].
TypeSpec supports some of these directly.

[Format Registry]: https://spec.openapis.org/registry/format

| `type:`   | `format:`    | TypeSpec type | Notes |
| --------- | ------------ | ------------- | ----- |
| `number`  | `decimal`    | `decimal`     |       |
| `number`  | `double-int` | `safeint`     |       |
| `integer` | `int8`       | `int8`        |       |
| `integer` | `int16`      | `int16`       |       |
| `integer` | `uint8`      | `uint8`       |       |
| `string`  | `uri`        | `url`         |       |

For formats that are not supported directly, you can use the built-in `@format` decorator to specify
the format explicitly.

### JSON Schema assertions

OpenAPI supports a variety of "assertions" that can be used to further restrict the values allowed for a data type.
These are actually borrowed into OpenAPI from JSON Schema.

For `type: integer` and `type: number` data types:

| OpenAPI/JSON Schema keyword | TypeSpec construct           | Notes |
| --------------------------- | ---------------------------- | ----- |
| `minimum: value`            | `@minValue(value)` decorator |       |
| `maximum: value`            | `@maxValue(value)` decorator |       |

For `type: string` data types:

| OpenAPI/JSON Schema keyword | TypeSpec construct            | Notes |
| --------------------------- | ----------------------------- | ----- |
| `minLength: value`          | `@minLength(value)` decorator |       |
| `maxLength: value`          | `@maxLength(value)` decorator |       |
| `pattern: regex`            | `@pattern(regex)` decorator   |       |

For `type: array` data types:

| OpenAPI/JSON Schema keyword | TypeSpec construct           | Notes |
| --------------------------- | ---------------------------- | ----- |
| `minItems: value`           | `@minItems(value)` decorator |       |
| `maxItems: value`           | `@maxItems(value)` decorator |       |

### enum

There are two ways to define an `enum` data type in TypeSpec. One is with the [TypeSpec `enum` statement](https://typespec.io/docs/language-basics/enums), e.g.:

<!-- To retain the quotes from the enum values -->
<!-- prettier-ignore-start -->
```typespec
enum Color {
  "red",
  "blue",
  "green",
}
```
<!-- prettier-ignore-end -->

Another is to use the union operation to define the enum values inline, e.g.:

```typespec
model Example {
  size?: "small" | "medium" | "large" | "x-large";
}
```

### default

A model property that specifies a default value using "=" will produce a `default` field in the schema for this property.

```typespec
model Example {
  answer?: int32 = 42;
  color?: string = "purple";
}
```

produces

```yaml title=openapi.yaml
answer:
  type: integer
  format: int32
  default: 42
color:
  type: string
  default: purple
```

## Host / BasePath / Servers

In OpenAPI v2, the `host` and `basePath` fields at the top-level of the API definition combine to form the base URL for the API. The paths defined in the `paths` object are appended to this base URL to form the absolute URL for an operation.

In OpenAPI v3, the top-level `servers` field specifies an array of `server` objects [[v3][v3-server]] with a base URL, which may be parameterized, to which the operation path is appended.

[v3-server]: https://github.com/OAI/OpenAPI-Specification/blob/3.0.3/versions/3.0.3.md#server-object

In TypeSpec, the `host` in OpenAPI v2 or `servers` in OpenAPI v3 can be specified with the `@server` decorator
on the namespace (from `@typespec/http` library). You can use this decorator multiple times to specify multiple servers.

## Paths Object

In OpenAPI, the `paths` object [[v2][v2-paths], [v3][v3-paths]] is the top-level structure for defining the operations of the API, organized by the "path" for the operation.

[v2-paths]: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#paths-object
[v3-paths]: https://github.com/OAI/OpenAPI-Specification/blob/3.0.3/versions/3.0.3.md#paths-object

In TypeSpec, you can specify the path for a namespace, interface, or operation using the `@route` decorator.

When the value of the `@route` decorator contains path parameters, operations within the scope of the decorator
must declare parameters with the same name and type. If an operation declares a path parameter that is not present
in the route, this defines a new path that is the value from the `@route` decorator with the path parameter appended.

```typespec
@route("/pets")
namespace Pets {
  op create(@body pet: Pet): Pet; // uses path "/pets"
  op read(@path petId: int32): Pet; // uses path "/pets/{petId}"
}
```

When the `@route` decorator is used within a namespace or interface that also has a `@route` decorator, the path is
obtained by concatenating the routes.

```typespec
@route("/widgets")
namespace Widgets {
  // widgets operations

  @route("/{id}/parts")
  namespace Parts {
    op list(@path id: string): Part[] | Error; // uses path "/widgets/{id}/parts"
  }
}
```

## Path Item Object

In OpenAPI, a path item object [[v2][v2-pathitem], [v3][v3-pathitem]] describes the operations available on a single path. A path may have at most one `get`, `put`, `post`, `patch`, `delete`, or `head` operation.

[v2-pathitem]: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#path-item-object
[v3-pathitem]: https://github.com/OAI/OpenAPI-Specification/blob/3.0.3/versions/3.0.3.md#path-item-object

In TypeSpec, operations are defined within a namespace or interface with a syntax similar to typescript functions.
The HTTP method for an operation can be specified explicitly using a decorator: `@get`, `@put`, `@post`, `@patch`, `@delete`, or `@head`.
If an HTTP method decorator is not specified then the default is `post` if there is a body and `get` otherwise.

```typespec
@tag("Gadgets")
@route("/gadgets")
namespace Gadgets {
  op create(@body gadget: Gadget): Gadget | Error; // uses "post" method
  op read(@path id: string): Gadget | Error; // uses "get" method
}
```

Other path item fields:

| OpenAPI `pathItem` field | TypeSpec construct | Notes                    |
| ------------------------ | ------------------ | ------------------------ |
| `summary`                |                    | Not currently supported. |
| `description`            |                    | Not currently supported. |
| `parameters`             |                    | Not currently supported. |

## Operation Object

In OpenAPI, an operation object [[v2][v2-operation], [v3][v3-operation]] describes an operation.

[v2-operation]: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#operation-object
[v3-operation]: https://github.com/OAI/OpenAPI-Specification/blob/3.0.3/versions/3.0.3.md#operation-object

The fields in an OpenAPI operation object are specified with the following TypeSpec constructs:

| OpenAPI `operation` field | TypeSpec construct                         | Notes                                                                        |
| ------------------------- | ------------------------------------------ | ---------------------------------------------------------------------------- |
| `tags`                    | `@tag` decorator                           |                                                                              |
| `summary`                 | `@summary` decorator                       |                                                                              |
| `description`             | `@doc` decorator or doc comment            |                                                                              |
| `externalDocs`            | `@externalDocs` decorator                  |                                                                              |
| `operationId`             | operation name or `@operationId` decorator |                                                                              |
| `parameters`              | `op` parameter list                        | see [Parameter Object](#parameter-object)                                    |
| `requestBody`             | parameter with `@body` decorator           | see [Request Body Object](#request-body-object-oas3)                         |
| `responses`               | `op` return type(s)                        | see [Responses Object](#responses-object)                                    |
| `callbacks`               |                                            | Not currently supported.                                                     |
| `deprecated`              | `#deprecated` directive                    |                                                                              |
| `security`                |                                            | see [Security Schemes Object](#securitydefinitions--securityschemes-object). |
| `servers`                 | `@server` decorator                        | Can be specified multiple times.                                             |

### Tags

Tags can be specified using the `@tag` decorator on an operation.
The `@tag` decorator can also be used on a namespace or interface to specify tags for all operations within the namespace or interface.
Tags are additive, so tags specified on an operation are added to the tags specified on the namespace or interface.
The `@tag` decorator can be used multiple times to specify multiple tags on an operation, namespace, or interface.

### Description

Use the `@doc` decorator to specify a description for an operation. The value of the `@doc` decorator can be a multi-line string
and can contain markdown formatting.

```typespec
@doc("""
  Get status info for the service.
  The status includes the current version of the service.
  The status value may be one of:
  - `ok`: the service is operating normally
  - `degraded`: the service is operating in a degraded state
  - `down`: the service is not operating
  """)
@tag("Status")
@route("/status")
@get
op status(): string;
```

You can also use a "doc comment" to specify the description for an operation. A doc comment is a comment that begins with `/**`.
Doc comments may be spread across multiple lines and may contain markdown formatting.

```typespec
/**
 * Get health info for the service.
 * The health includes the current version of the service.
 * The health value may be one of:
 * - `ok`: the service is operating normally
 * - `degraded`: the service is operating in a degraded state
 * - `down`: the service is not operating
 */
@tag("Health")
@route("/health")
@get
op health(): string;
```

[See documentation doc for more information](../language-basics/documentation.md).

### operationId

You can specify the operationId for an operation using the `@operationId` decorator.
When the `@operationId` decorator is not specified, the operationId is generated from the operation name.
For an operation defined in the top-level namespace, the operationId is the just operation name.
If the operation is defined within a inner namespace or interface, then the operationId is
prefixed with the name of the innermost namespace or interface name.

Note: this approach will generally produce unique operationIds, as required by OpenAPI,
but it is possible to create duplicate operationIds.

## Parameter Object

In OpenAPI, a parameter object [[v2][v2-parameter], [v3][v3-parameter]] describes a single operation parameter.

[v2-parameter]: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#parameter-object
[v3-parameter]: https://github.com/OAI/OpenAPI-Specification/blob/3.0.3/versions/3.0.3.md#parameter-object

The following fields of a parameter object are common to both OpenAPI v2 and v3:

| OpenAPI `parameter` field | TypeSpec construct           | Notes                                                                                                                        |
| ------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `name`                    | parameter name               |                                                                                                                              |
| `in`                      | decorator                    | `@query`, `@path`, `@header`, `@body`                                                                                        |
| `description`             | `/** */` or `@doc` decorator |                                                                                                                              |
| `required`                | from parameter "optionality" | a "?" following the parameter name indicates it is optional (`required: false`), otherwise it is required (`required: true`) |
| `allowEmptyValue`         |                              | Not supported, this field is `NOT RECOMMENDED` in OpenAPI.                                                                   |

<!-- prettier-ignore-end -->

### OpenAPI v2

The following fields of a parameter object are specific to OpenAPI v2:

| OpenAPI v2 `parameter` field | TypeSpec construct                          | Notes                         |
| ---------------------------- | ------------------------------------------- | ----------------------------- |
| `type`                       | parameter type                              | see [Data Types](#data-types) |
| `collectionFormat`           | uri template in `@route` or `expode, style` |                               |

#### Collection Formats

In OpenAPI v2, the `collectionFormat` field of a query or header parameter object specifies how multiple values are delimited.
You can use a combination of the `@encode` decorator and `explode` field of the `@query` or `@header` decorator to specify the collection format.

```typespec
op read(
  @query csv?: string[], // equivalent to collectionFormat: csv
  @query(#{ explode: false }) csvExplicit?: string[], // equivalent to collectionFormat: csv
  @query(#{ explode: true }) multi?: string[], // equivalent to collectionFormat: multi
  @query @encode(ArrayEncoding.pipeDelimited) pipes?: string[], // equivalent to collectionFormat: pipes
): Widget | Error;
```

### OpenAPI v3

The following fields of a parameter object are specific to OpenAPI v3:

| OpenAPI v3 `parameter` field | TypeSpec construct                                                                                              | Notes                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `style`                      | `explode` parameter on `@query` or `@header` and `@encode`                                                      |                                                                                 |
| `explode`                    | `explode` parameter on `@query` or `@header`                                                                    |                                                                                 |
| `schema`                     | parameter schema                                                                                                | see [Schema Object](#schema-object)                                             |
| `deprecated`                 | `#deprecated` directive.                                                                                        |                                                                                 |
| `example`                    | `@example` on data types (e.g. models, scalars), `@opExample` to describe in-line parameters of operations      | Open API 3.0 only supports a single example when using `@example` on data types |
| `examples`                   | `@example` on data types (e.g. models, scalars), `@opExample` to describe parameters/return types of operations | Open API 3.1 always outputs `examples` instead of `example`.                    |
| `content`                    |                                                                                                                 | Not currently supported.                                                        |

## Request Body Object (OAS3)

In OpenAPI v3, the operation request body is defined with a [Request Body object] rather than as a parameter.

[Request Body object]: https://github.com/OAI/OpenAPI-Specification/blob/3.0.3/versions/3.0.3.md#request-body-object

An OpenAPI v3 Request Body object corresponds to a TypeSpec `op` parameter with the `@body` decorator.

<!-- prettier-ignore-start -->
| OpenAPI `requestBody` field | TypeSpec construct      | Notes        |
| --------------------------- | ----------------------- | ------------ |
| `description`               | `@doc` decorator        |              |
| `required`                  | parameter "optionality" | a "?" following the parameter name indicates it is optional (`required: false`), otherwise it is required (`required: true`) |
| `content`                   | `@body` parameter type  |              |
<!-- prettier-ignore-end -->

The media type of the request body is specified with a `content-type` header. If `content-type` has multiple values
then `content` will have one entry for each value.

```typespec
@put op uploadImage(@header contentType: "image/png", @body image: bytes): void;
@post op analyze(
  @header contentType: "application/octet-stream" | "application/pdf" | "image/jpeg",
  @body image: bytes,
): string | Error;
```

To get multiple `content` entries with different schemas (say one structured and one binary),
you need to define two separate operations that share the same path and method.
You do with with the `@sharedRoute` decorator.

```typespec
@route(":process")
namespace Process {
  @sharedRoute
  @post
  op process(...Widget): Widget | Error;

  model CsvBody {
    @header contentType: "text/csv";
    @body _: string;
  }
  @sharedRoute
  @post
  op process2(...CsvBody): Widget | Error;
}
```

## Responses Object

In OpenAPI, the responses object [[v2][v2-responses], [v3][v3-responses]] specifies the possible responses for an operation.
The responses object maps a HTTP response code to the expected response.

[v2-responses]: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#responses-object
[v3-responses]: https://github.com/OAI/OpenAPI-Specification/blob/3.0.3/versions/3.0.3.md#responses-object

In TypeSpec, operation responses are defined by the return types of the `op`. The status code for a response can be specified as a property in the return type with the `@statusCode` decorator. The value of the property with the `@statusCode` decorator should be an HTTP status code or union of status codes. When the value is a union of status codes, a response is generated for each status code in the union.

If a return type does not contain a `statusCode`, the default is `200` except for `void` which defaults to `204`.

To get the `default` response, specify the `@error` decorator on the return type model.

```typespec
@get op read(@path id: string): Widget; // has "200" response
@delete op delete(@path id: string): void; // has "204" response
// has "200" and "201" response
@put op create(@body widget: Widget): {
  @statusCode _: "200" | "201";
  @body body: Widget;
};
// has "200" and "default" response
@post op update(@body widget: Widget): Widget | Error;
```

The TypeSpec.Http package also defines several standard response types.

| HTTP Status Code | TypeSpec construct     |
| ---------------- | ---------------------- |
| `200`            | `OkResponse`           |
| `201`            | `CreatedResponse`      |
| `202`            | `AcceptedResponse`     |
| `204`            | `NoContentResponse`    |
| `301`            | `MovedResponse`        |
| `304`            | `NotModifiedResponse`  |
| `401`            | `UnauthorizedResponse` |
| `404`            | `NotFoundResponse`     |
| `409`            | `ConflictResponse`     |

You can intersect these standard response types with your own response types.

```typespec
// has "200", '409', and "default" responses
@post op update(@body widget: Widget): Widget | (ConflictResponse & Error) | Error;
```

### Response Object

In OpenAPI, a response object [[v2][v2-response], [v3][v3-response]] describes a single response for an operation.
The structure of the response object changed significantly from OpenAPI v2 to OpenAPI v3, but there are many
elements common to both.

[v2-response]: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#response-object
[v3-response]: https://github.com/OAI/OpenAPI-Specification/blob/3.0.3/versions/3.0.3.md#response-object

The fields in an OpenAPI response object are specified with the following TypeSpec constructs:

| OpenAPI `response` field | TypeSpec construct                                  | Notes                                               |
| ------------------------ | --------------------------------------------------- | --------------------------------------------------- |
| `description`            | `@doc` decorator                                    |                                                     |
| `headers`                | fields in the return type with `@header` decorator  | Required or optional based on optionality of field. |
| `schema` (OAS2)          | return type or type of `@body`` property            |                                                     |
| `content` (OAS3)         | return type or type of `@body`` property            |                                                     |
| `examples` (OAS3)        | `@opExample` to describe return types of operations | Supported on an operation.                          |
| `links` (OAS3)           |                                                     | Not currently supported.                            |

```typespec
@get op read(@path id: string): {
  /** the widget */
  @body
  widget: Widget;

  @header xRateLimitRemaining: int32;
  @header xRateLimitReset: int32;
};
```

The media type of the request body is specified with a `content-type` header. If `content-type` has multiple values
then `content` will have one entry for each value.

To get multiple `content` entries with different schemas, use a union type.

```typespec
@tag("Response Content")
@route("/response-content")
namespace ResponseContent {
  @get op read(@path id: string): Widget | {
    @header contentType: "text/html";
    @body _: string;
  } | {
    @header contentType: "image/jpeg";
    @body _: bytes;
  };
}
```

## Schema Object

OpenAPI schemas are represented in TypeSpec by [models](https://typespec.io/docs/language-basics/models/).
Models have any number of members and can extend and be composed with other models.

Models can be defined with the `model` statement and then referenced by name, which generally results in a `$ref` to a schema for the model in the `definitions` or `components.schemas` section of the OpenAPI document.

TypeSpec supports the ["spread" operator](https://typespec.io/docs/language-basics/models/#spread) (`...`), which copies the members of the source model into the target model.
But TypeSpec processes all spread transformations before emitters are invoked, so this form of reuse is not represented in the emitted OpenAPI.

The spread operation is useful if you want one or more properties to be present in several different models but in a standard fashion. For example:

```typespec
model Legs {
  /** number of legs */
  legs: int32;
}

model Dog {
  name: string;
  ...Legs;
}

model Cat {
  name: string;
  ...Legs;
}

model Snake {
  name: string;
  // snakes have no legs
}
```

### additionalProperties/unevaluatedProperties

You can generate a schema with `additionalProperties` with the TypeSpec `Record` construct.

**Note:** `unevaluatedProperties` is used instead of `additionalProperties` when emitting Open API 3.1 specs.

```typespec
  bar: Record<unknown>;
```

is produced as

```yaml title=openapi.yaml
bar:
  type: object
  additionalProperties: {}
```

To get a schema having both `properties` and `additionalProperties`, define a model that extends `Record<unknown>`.

```typespec
model Bar extends Record<unknown> {
  bar?: string;
}
```

produces

```yaml title=openapi.yaml
Bar:
  type: object
  properties:
    bar:
      type: string
  additionalProperties: {}
```

To define a schema with `additionalProperties` that has a specific type, use the `Record` construct with a type parameter.

```typespec
  bar: Record<string>;
```

results in

```yaml title=openapi.yaml
bar:
  type: object
  additionalProperties:
    type: string
```

To define a schema that **does not** allow any additional properties, use `Record<never>`.

```typespec
  bar: Record<never>;
```

results in

```yaml title=openapi.yaml
bar:
  type: object
  additionalProperties:
    not: {}
```

In the openapi3 emitter, schemas that don't define `additionalProperties` can automatically be set to `additionalProperties: { not: {} }` by setting the `seal-object-schemas` emitter option to `true`. This will not add `additionalProperties` to object schemas that are referenced in an `allOf` of another schema.

### allOf and polymorphism using allOf

TypeSpec supports single inheritance of models with the `extends` keyword. This construct can be used to produce an `allOf` with a single element (the parent schema) in OpenAPI. For example:

```typespec title=main.tsp
model Pet {
  name: string;
}

model Cat extends Pet {
  meow: int32;
}

model Dog extends Pet {
  bark: string;
}
```

TypeSpec does not currently provide a means to produce an `allOf` with more than one element -- these are generally treated as "composition" in code generators and thus better represented in TypeSpec with the spread operator.

Models with a `@discriminator` decorator can be extended to produce polymorphic schemas in either OpenAPI v2 or v3 using `allOf`.
This schema produced for the base model will be defined with a `discriminator` property and schemas for the child models will `allOf` the base schema and add additional properties.

For example:

```typespec
@discriminator("kind")
model Pet {
  name: string;
  weight?: float32;
}
model Cat extends Pet {
  kind: "cat";
  meow?: int32;
}
model Dog extends Pet {
  kind: "dog";
  bark?: string;
}
```

generates:

```yaml title=openapi.yaml
Cat:
  type: object
  properties:
    kind:
      type: string
      enum:
        - cat
    meow:
      type: integer
      format: int32
  required:
    - kind
  allOf:
    - $ref: "#/components/schemas/Pet"
Dog:
  type: object
  properties:
    kind:
      type: string
      enum:
        - dog
    bark:
      type: string
  required:
    - kind
  allOf:
    - $ref: "#/components/schemas/Pet"
Pet:
  type: object
  properties:
    kind:
      type: string
      description: Discriminator property for Pet.
    name:
      type: string
    weight:
      type: number
      format: float
  discriminator:
    propertyName: kind
    mapping:
      cat: "#/components/schemas/Cat"
      dog: "#/components/schemas/Dog"
  required:
    - name
```

### Polymorphism using anyOf and oneOf (OAS3)

Polymorphism can also be represented in OpenAPI v3 with `anyOf` or `oneOf` constructs.
These can be represented in TypeSpec with a union type.

```typespec
union Pet {
  cat: Cat,
  dog: Dog,
}

model Cat {
  meow?: int32;
}

model Dog {
  bark?: string;
}
```

generates a Pet schema with `anyOf`.

```yaml title=openapi.yaml
Pet:
  anyOf:
    - $ref: "#/components/schemas/Cat"
    - $ref: "#/components/schemas/Dog"
```

The openapi emitter uses `anyOf` by default because the schemas may not be mutually exclusive.
But the `@oneOf` decorator of the OpenAPI library can be used to force the use of `oneOf` instead.

```typespec
import "@typespec/openapi3";
using OpenAPI;

@oneOf
union Pet {
  cat: Cat,
  dog: Dog,
}
```

produces:

```yaml title=openapi.yaml
Pet:
  oneOf:
    - $ref: "#/components/schemas/Cat"
    - $ref: "#/components/schemas/Dog"
```

To make Pet a discriminated union, add the `@discriminator` decorator and add the discriminator property
with a string literal value to each of the child schemas.
View the [`@discriminated` documentation](https://typespec.io/docs/standard-library/built-in-decorators/#@discriminated) to learn how to further customize what is emitted.

```typespec
@discriminated(#{ envelope: "none" })
union Pet {
  cat: Cat,
  dog: Dog,
}
model Cat {
  kind: "cat";
  meow?: int32;
}
model Dog {
  kind: "dog";
  bark?: string;
}
```

results in the following schema for Pet:

```yaml title=openapi.yaml
Pet:
  oneOf:
    - $ref: "#/components/schemas/Cat"
    - $ref: "#/components/schemas/Dog"
  discriminator:
    propertyName: kind
    mapping:
      cat: "#/components/schemas/Cat"
      dog: "#/components/schemas/Dog"
```

## definitions / components

OpenAPI supports reuse of schemas, parameters, responses, and other elements with the `definitions` (OAS2) or `components` (OAS3) section of an OpenAPI definition.

Referencing a model by name (not with "spread"), as an `op` parameter or return type or as the type of a property in another model, generally results in a `$ref` to a schema for the model in the `definitions` or `components.schemas` section of the OpenAPI document.

Reusable parameters can be defined as members of a model and then incorporated into an operation parameter list using the spread operator. For example:

```typespec
model PetId {
  @path petId: int32;
}

namespace Pets {
  op read(...PetId): Pet | Error;
}
```

results in a `$ref` to the named parameter `PetId` in either `parameters` or `components.parameters`.

## Info Object

In OpenAPI, the `info` object [[v2][v2-info], [v3][v3-info]] contains metadata about the API such as a `title`, `description`, `license`, and `version`.

[v2-info]: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#info-object
[v3-info]: https://github.com/OAI/OpenAPI-Specification/blob/3.0.3/versions/3.0.3.md#info-object

In TypeSpec this information is specified with [decorators on the namespace][typespec-service-metadata].

| OpenAPI `info` field | TypeSpec decorator    | Notes                       |
| -------------------- | --------------------- | --------------------------- |
| `title`              | `@service(#{title: }` | TypeSpec built-in decorator |
| `description`        | `@doc`                | TypeSpec built-in decorator |
| `version`            | `@info`               |                             |
| `license`            | `@info`               |                             |
| `contact`            | `@info`               |                             |

[typespec-service-metadata]: https://typespec.io/docs/libraries/http/reference/decorators/

```typespec
/** The Contoso Widget Service provides access to the Contoso Widget API. */
@service(#{ title: "Widget Service" })
@info(#{
  contact: #{ name: "API Support", email: "contact@contoso.com" },
  license: #{ name: "Apache 2.0", url: "https://www.apache.org/licenses/LICENSE-2.0.html" },
})
namespace DemoService;
```

## Consumes / Produces (OAS2)

In OpenAPI v2, the top-level `consumes` and `produces` fields specify a list of MIME types an operation can consume / produce
when not overridden by a `consumes` or `produces` on an individual operation.

The typespec-autorest emitter previously supported `@produces` and `@consumes` decorators on a namespace, but these are deprecated
in favor of explicit `content-type` and `accept` header properties in request and response bodies.

## securityDefinitions / securitySchemes Object

Use the `@useAuth` decorator from the `@typespec/rest" library

```typespec
using Http;
@useAuth(OAuth2Auth<["read", "write"]>)
namespace MyService;
```

## Specification Extensions

You can add arbitrary specification extensions ("x-" properties) to a model or an operation with the `@extension` decorator.
For example:

```typespec
namespace Pets {
  @extension("x-streaming-operation", true) op read(...PetId): Pet | Error;
}
```

OpenAPI decorators that map directly to an object in the openapi document also allow to provide extension.

`@tagMetadata`

```tsp
@tagMetadata("my-tag", #{
  description: "My tag",
  `x-custom`: "custom value",
})
```

- `@info`

```tsp
@info(#{
  version: 1.1.0,
  `x-custom`: "custom value",
})
```

# Access Modifiers

Language basics - controlling the visibility of declarations across libraries

Access modifiers control which declarations in a TypeSpec library are accessible to consumers of that library. They allow library authors to distinguish between the public API surface and internal implementation details.

:::caution
Access modifiers are an **experimental feature** and may change or be removed in a future release. The compiler will emit a warning when access modifiers are used.
:::

## The `internal` modifier

The `internal` modifier restricts a declaration so that it can only be accessed within the library or project where it is defined. Consumers of the library cannot reference internal declarations.

```typespec
internal model MyInternalModel {
  secret: string;
}

model MyPublicModel {
  // OK: same library can reference internal models
  details: MyInternalModel;
}
```

### Supported declarations

The `internal` modifier can be applied to the following declaration types:

| Declaration | Example                            |
| ----------- | ---------------------------------- |
| `model`     | `internal model Example {}`        |
| `scalar`    | `internal scalar Example;`         |
| `interface` | `internal interface Example {}`    |
| `union`     | `internal union Example {}`        |
| `op`        | `internal op example(): void;`     |
| `enum`      | `internal enum Example {}`         |
| `alias`     | `internal alias Example = string;` |
| `const`     | `internal const example = 1;`      |

:::note
The `internal` modifier **cannot** be applied to `namespace` declarations.
:::

### Access rules

The `internal` modifier is a property of the _symbol_ (the name that refers to a type), not a property of the type itself. The compiler prevents code in other packages from _referencing_ an internal symbol by name, but it does not prevent the underlying type from being used indirectly. A public declaration within the same package can freely reference an internal declaration, and the resulting type will be accessible to consumers through the public declaration.

When a declaration is marked `internal`, the compiler enforces the following rules:

- **Same library or project**: Code within the same library (or the same project, if not in a library) can reference internal declarations normally.
- **Different library**: Code in a different library that tries to reference an internal declaration by name will receive an error.

```typespec title="my-lib/main.tsp"
namespace MyLib;

internal model SecretHelper {
  key: string;
}

model PublicApi {
  data: SecretHelper; // ✅ OK: same library
}

// ✅ OK: a public alias can reference an internal symbol within the same package.
// Consumers can use `ExposedHelper`, even though it refers to the same type as `SecretHelper`.
alias ExposedHelper = SecretHelper;
```

```typespec title="consumer/main.tsp"
import "my-lib";

model Consumer {
  helper: MyLib.SecretHelper; // ❌ Error: SecretHelper is internal
  data: MyLib.PublicApi; // ✅ OK: PublicApi is public (even though it references SecretHelper)
  exposed: MyLib.ExposedHelper; // ✅ OK: ExposedHelper is a public alias
}
```

The error message for a direct reference to an internal symbol will read:

> Symbol 'SecretHelper' is internal and can only be accessed from within its declaring package.

### Combining with `extern`

The `internal` modifier can be combined with the `extern` modifier on decorator declarations to create internal decorator signatures:

```typespec
internal extern dec myInternalDecorator(target: unknown);
```

### Suppressing the experimental warning

Since access modifiers are currently experimental, using `internal` will emit a warning. You can suppress this warning with a `#suppress` directive:

```typespec
#suppress "experimental-feature"
internal model MyInternalModel {}
```

## Why not `namespace`?

The `internal` modifier is not supported on namespaces because namespaces in TypeSpec are **open and merged** across files. A namespace declared in one file can be extended in another file — potentially across library boundaries. Applying `internal` to a namespace would create ambiguity about which parts of the namespace are internal and which are public. Instead, mark individual declarations within a namespace as `internal`.

```typespec
namespace MyLib;

internal model InternalHelper {} // ✅ Mark individual declarations
model PublicApi {}
```

## Relationship to visibility

The `internal` access modifier is distinct from TypeSpec's [visibility](./visibility.md) system:

- **Access modifiers** (`internal`) control which _declarations_ (models, operations, etc.) can be referenced across library boundaries. They are enforced at compile time.
- **Visibility** (`@visibility`, `@removeVisibility`) controls which _model properties_ appear in different API operation contexts (e.g., create vs. read). It is a metadata system used by emitters to generate different views of a model.

These are complementary features — you can use both on the same types. For example, you might have a public model whose properties have different visibility across operations, or an internal model that is only used within your library's implementation.

# Aliases

Language basics - aliases

Aliases are a convenient way to define shorthand for types, especially when dealing with complex expressions. They simplify the syntax but don't have a representation in the type graph. As a result, you can't decorate aliases. If you need to give an alternate name to a model, use [`model is`](./models.md/#is).

You can define an alias using the `alias` keyword.

```typespec
alias Options = "one" | "two";
```

## Referencing model properties

You can reference model properties using the `.` operator for identifiers.

```tsp
alias PetName = Pet.name;
```

# Built-in types

Language basics - built-in types

TypeSpec Standard Library provide some built-in types that can be used to build more complex types.

Built in types are related to each other according to the rules described in [type relations](../language-basics/type-relations.md).

## Numeric types

| Type         | Range                                                                                                        | Description                               |
| ------------ | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| `numeric`    | [\*](#numeric-supertypes)                                                                                    | Parent type for all numeric types         |
| `integer`    | [\*](#numeric-supertypes)                                                                                    | A whole-number                            |
| `float`      | [\*](#numeric-supertypes)                                                                                    | A binary number                           |
| `int64`      | `-9,223,372,036,854,775,808` to `9,223,372,036,854,775,807`                                                  | A 64-bit integer                          |
| `int32`      | `-2,147,483,648` to `2,147,483,647`                                                                          | A 32-bit integer                          |
| `int16`      | `-32,768` to `32,767`                                                                                        | A 16-bit integer                          |
| `int8`       | `-128` to `127`                                                                                              | A 8-bit integer                           |
| `safeint`    | <code>−9007199254740991 (−(2<sup>53</sup> − 1))</code> to <code>9007199254740991 (2<sup>53</sup> − 1)</code> | An integer that can be serialized to JSON |
| `uint64`     | `0` to `18,446,744,073,709,551,615`                                                                          | Unsigned 64-bit integer                   |
| `uint32`     | `0` to `4,294,967,295`                                                                                       | Unsigned 32-bit integer                   |
| `uint16`     | `0` to `65,535`                                                                                              | Unsigned 16-bit integer                   |
| `uint8`      | `0` to `255 `                                                                                                | Unsigned 8-bit integer                    |
| `float32`    | <code>±1.5 x 10<sup>−45</sup></code> to <code>±3.4 x 10<sup>38</sup></code>                                  | A 32 bit floating point number            |
| `float64`    | <code>±5.0 × 10<sup>−324</sup></code> to <code>±1.7 × 10<sup>308</sup></code>                                | A 64 bit floating point number            |
| `decimal`    | [\*](#numeric-supertypes)                                                                                    | A decimal number                          |
| `decimal128` | 34 decimal digits with an exponent range from `-6143` to `6144`                                              | A 128 bit decimal number                  |

### Numeric supertypes

`numeric`, `integer`, `float` and `decimal` are types that represent any possible number in their category. For some emit targets, `BigInt` or `BigDecimal` might be an analogous type satisfying the TypeSpec types `integer` and `decimal` respectively. For other targets where the language, serialization format, or protocol does not support an analogous type, emitters may decide on a policy for emitting the numeric supertypes. This might involve picking the closest analogous type and reporting a warning when they are encountered.

## Date and time types

| Type             | Description                                                                         |
| ---------------- | ----------------------------------------------------------------------------------- |
| `plainDate`      | A date on a calendar without a time zone, e.g. "April 10th"                         |
| `plainTime`      | A time on a clock without a time zone, e.g. "3:00 am"                               |
| `utcDateTime`    | A date and time in coordinated universal time (UTC), e.g. "1985-04-12T23:20:50.52Z" |
| `offsetDateTime` | A date and time in a particular time zone, e.g. "April 10th at 3:00am in PST"       |
| `duration`       | A duration/time period. e.g 5s, 10h                                                 |

:::note

These types do not define any specific serialization format. They represent the concept of time. Each protocol or serialization format should define the default serialization format.

The default encodings for various protocols are defined here:

- [JSON over HTTP](../libraries/http/encoding.md#utcdatetime-and-offsetdatetime)
- [XML](../libraries/xml/guide.md)
  :::

## Other core types

| Type              | Description                                                                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bytes`           | A sequence of bytes                                                                                                                                        |
| `string`          | A sequence of textual characters                                                                                                                           |
| `boolean`         | Boolean with `true` and `false` values                                                                                                                     |
| `null`            | Null value                                                                                                                                                 |
| `Array<Element>`  | Array model type, equivalent to `Element[]`                                                                                                                |
| `Record<Element>` | Model with string keys where all the values have type `Element` (similar to `Map<string, Element>` in TypeScript or `Dictionary<string, Element>` in .Net) |
| `unknown`         | A top type in TypeSpec that all types can be assigned to. Values that can have any type should be assigned this value (similar to `any` in JavaScript)     |
| `void`            | A function/operation return type indicating the function/operation doesn't return a value.                                                                 |
| `never`           | The never type indicates the values that will never occur.                                                                                                 |

## String types

Built-in types that are known string formats

| Type  | Description  |
| ----- | ------------ |
| `url` | A url String |

# Decorators

Language basics - using decorators

Decorators in TypeSpec allow developers to attach metadata to types within a TypeSpec program. They can also be used to compute types based on their inputs. Decorators form the core of TypeSpec's extensibility, providing the flexibility to describe a wide variety of APIs and associated metadata such as documentation, constraints, samples, and more.

The vast majority of TypeSpec declarations may be decorated, including [namespaces](./namespaces.md), [interfaces](./interfaces.md), [operations](./operations.md) and their parameters, [scalars](./scalars.md), and [models](./models.md) and their members. In general, any declaration that creates a Type can be decorated. Notably, [aliases](./alias.md) cannot be decorated, as they do not create new Types, nor can any type expressions such as unions that use the `|` syntax or anonymous models, as they are not declarations.

Decorators are defined using JavaScript functions that are exported from a standard ECMAScript module. When a JavaScript file is imported, TypeSpec will look for any exported functions prefixed with `$`, and make them available as decorators within the TypeSpec syntax. When a decorated declaration is evaluated by TypeSpec, the decorator function is invoked, passing along a reference to the current compilation, an object representing the type it is attached to, and any arguments the user provided to the decorator.

## Applying decorators

Decorators are referenced using the `@` prefix and must be placed before the entity they are decorating. Arguments can be provided by using parentheses, similar to function calls in many programming languages, e.g., `@myDec1("hi", { a: string })`.

Here's an example of declaring and then using a decorator:

```typespec
@tag("Sample")
model Dog {
  @validate(false)
  name: string;
}
```

If no arguments are provided, the parentheses can be omitted.

```typespec
@mark
model Dog {}
```

## Augmenting decorators

Decorators can also be applied from a different location by referring to the type being decorated. For this, you can declare an augment decorator using the `@@` prefix. The first argument of an augment decorator is the type reference that should be decorated. As the augment decorator is a statement, it must end with a semicolon (`;`).

```typespec
model Dog {}

@@tag(Dog, "Sample");
```

This is equivalent to:

```typespec
@tag("Sample")
model Dog {}
```

Example: decorating a model property to indicate that it is read-only

```typespec
model Dog {
  name: string;
}

@@visibility(Dog.name, Lifecycle.Read);
```

## Creating decorators

For more information on creating decorators, see [Creating Decorators](../extending-typespec/create-decorators.md).

# Documentation

Language basics - documenting APIs

Documentation is a vital aspect of any API. TypeSpec offers several ways to document your API, including doc comments and decorators.

## Approaches to documenting APIs

TypeSpec provides two primary methods for documenting your API:

- `@doc` decorator
- `/** */` Doc comments

The latter is less intrusive to the specification and is often preferred.

In both cases while not required, the documentation should be written in Markdown format, TypeSpec tooling will assume so. [See Markdown](#markdown) for more information.

## The `@doc` decorator

The `@doc` decorator can be used to attach documentation to most TypeSpec declarations. It typically accepts a string argument that serves as the documentation for the declaration.

```typespec
@doc("This is a sample model")
model Dog {
  @doc("This is a sample property")
  name: string;
}
```

The `@doc` decorator can also accept a source object, which can be used to provide templated documentation for a generic type, for example.

```typespec
@doc("Templated {name}", Type)
model Template<Type extends {}>  {
}

// The documentation will read "Templated A"
model A is Template<A>
```

## Doc comments

You can annotate objects in your TypeSpec specification with doc comments. These comments are treated as if they were attached using the `@doc` decorator and can be used to generate external documentation.

Doc comments start with `/**` and continue until the closing `*/` is encountered. [Tags](#doc-comment-tags) can be used to provide additional documentation context.

```typespec
/**
 * Get a widget.
 * @param widgetId The ID of the widget to retrieve.
 */
op read(@path widgetId: string): Widget | Error;
```

This is functionally equivalent to:

```typespec
@doc("Get a widget.")
op read(
  @doc("The ID of the widget to retrieve.")
  @path
  widgetId: string,
): Widget | Error;
```

The advantage of using doc comment syntax is that it consolidates all the documentation for a declaration in one place, with distinct comment colors, making it easier to read and maintain. Additionally, it facilitates the generation of documentation using tools like TypeDoc, eliminating the need to write a custom emitter to process the @doc metadata.

### Doc comment tags

As shown in the previous example, doc comments can use certain tags to document additional elements or provide different documentation context.

| Tag                     | Description                       | Example                                             |
| ----------------------- | --------------------------------- | --------------------------------------------------- |
| `@param`                | Documents a parameter.            | `@param widgetId The ID of the widget to retrieve.` |
| `@returns`              | Documents the operation response. | `@returns The widget.`                              |
| `@template`             | Document a template parameter     | `@template T the resource type`                     |
| `@example` (unofficial) | Show examples                     | `@example \`model Foo {}\` `                        |

## Comments

TypeSpec supports both single-line and multi-line comments. Single-line comments start with `//` and continue until the end of the line. Multi-line comments start with `/*` and continue until the closing `*/` is encountered.

```typespec
// This is a single-line comment
model Dog {
  /* This is a multi-line comment
  that spans multiple lines */
  name: string;
}
```

Comments are ignored by the compiler and do not appear in the generated output. They are intended for internal documentation of your spec and are not suitable for generating external documentation.

## Markdown

TypeSpec Documentation support CommonMark markdown formatting. The tooling(IDE extensions, doc generation, etc.) will process the documentation as markdown.
Emitters can choose to render the description as it is, convert it to their preferred format or just strip any markdown information.

````tsp
@doc("This is a **bold** text")
model Dog {
  @doc("This is a _italic_ text")
  name: string;

  /**
   * This contains a bullet list
   * - one
   * - two
   * and code blocks
   *
   * ```typescript
   * dog.age = 5;
   * ```
   */
  age: int32;
}
````

# Enums

Language basics - enums

Enums, short for enumerations, provide a way for developers to define a collection of named constants. They are useful for documenting the purpose of the code or for establishing a set of distinct scenarios. Enums can be either numeric or string-based. For other data types, consider using [unions](./unions.md).

## The basics

You can declare enums using the `enum` keyword. The members of an enum are separated by commas `,` and can be either [`identifier`](./identifiers.md) TypeSpecs or `string literal`s.

```typespec
enum Direction {
  North,
  East,
  South,
  West,
}
```

In the above example, we haven't defined the representation of the constants. Depending on the context, enums might be handled differently.

## Assigning values to enums

You can assign custom values to enum members using the `:` operator.

```typespec
enum Direction {
  North: "north",
  East: "east",
  South: "south",
  West: "west",
}
```

These values can also be integers.

```typespec
enum Foo {
  One: 1,
  Ten: 10,
  Hundred: 100,
  Thousand: 1000,
}
```

Or even floating-point numbers.

```typespec
enum Hour {
  Zero: 0,
  Quarter: 0.25,
  Half: 0.5,
  ThreeQuarter: 0.75,
}
```

## Combining enums

You can combine enums using the spread `...` pattern. This copies all the members from the source enum to the target enum, but it doesn't establish any reference between the source and target enums.

```typespec
enum DirectionExt {
  ...Direction,
  `North East`,
  `North West`,
  `South East`,
  `South West`,
}
```

## How to reference enum members

You can reference enum members using the `.` operator for identifiers.

```typespec
alias North = Direction.North;
```

# Identifiers

Language basics - identifiers

Identifiers are names used to reference models, enums, operations, properties, and other entities in TypeSpec. Understanding identifier rules is essential for writing valid TypeSpec code.

## Identifier syntax rules

An identifier must follow these rules:

- **Start with**: A letter (a-z, A-Z), emoji, underscore (`_`), or dollar sign (`$`)
- **Followed by**: Any combination of letters, numbers (0-9), emoji, underscores, or dollar signs
- **Length**: One or more characters

TypeSpec implements [UAX31-R1b stable identifiers](http://www.unicode.org/reports/tr31/#R1b) with the [emoji profile](http://www.unicode.org/reports/tr31/#Emoji_Profile), providing full Unicode support for international characters.

### Examples

- ✅ `cat`
- ✅ `Dog`
- ✅ `_Item2`
- ✅ `$money$`
- ✅ `🎉`
- ✅ `🚀`
- ❌ `1cat`
- ❌ `*dog`

## Escaping identifiers

When you need to use reserved keywords or invalid identifiers, TypeSpec provides an escaping mechanism using backticks (`` ` ``). This allows you to use:

- Reserved keywords as identifiers
- Identifiers that don't follow normal syntax rules
- Identifiers with special characters or unusual formats

#### Examples

```tsp
model `enum` {}
model `interface` {}
op `import`(): void;
model `123InvalidName` {}
model `my-special-model` {}
model `User Profile` {}
```

# Imports

Language basics - importing files and libraries

Imports are used to include files or libraries into your TypeSpec program. When compiling a TypeSpec file, you specify the path to your root TypeSpec file, typically named "main.tsp". From this root file, any imported files are added to your program. If a directory is imported, TypeSpec will search for a `main.tsp` file within that directory.

The path specified in the import must either start with `"./"` or `"../"`, or be an absolute path. The path should either point to a directory, or have an extension of either ".tsp" or ".js". The examples below illustrate how to use imports to assemble a TypeSpec program from multiple files:

## Importing a TypeSpec file

```typespec
import "./models/foo.tsp";
```

## Importing a JavaScript file

```typespec
import "./decorators.js";
```

## Importing a library

The import value can be the name of one of the package dependencies.

```typespec
import "/rest";
```

```json
// ./node_modules/@typespec/rest/package.json
{
  "exports": {
    ".": { "typespec": "./lib/main.tsp" }
  }
}
```

This results in `./node_modules/@typespec/rest/lib/main.tsp` being imported.

### Package resolution algorithm

When trying to import a package TypeSpec follows the following logic

1. Parse the package name from the import specificier into `pkgName` and `subPath` (e.g. `@scope/lib/named` => pkgName: `@scope/lib` subpath: `named` )
1. Look to see if `pkgName` is itself(Containing package)
1. Otherwise lookup for a parent folder with a `node_modules/${pkgName}` sub folder
1. Reading the `package.json` of the package
   a. If `exports` is defined respect the [ESM logic](https://github.com/nodejs/node/blob/main/doc/api/esm.md) to resolve the `typespec` condition(TypeSpec will not respect the `default` condition)
   b. If `exports` is not found or for back compat the `.` export is missing the `typespec` condition fallback to checking `tspMain` or `main`

## Importing a directory

If the import value is a directory, TypeSpec will check if that directory is a Node package and follow the npm package [lookup logic](#importing-a-library), or if the directory contains a `main.tsp` file.

```typespec
import "./models"; // equivalent to `import "./models/main.tsp";
```

```typespec
import "./path/to/local/module"; // Assuming this path is a TypeSpec package, it will load it using the tspMain file.
```

# Interfaces

Language basics - grouping operations with interfaces

Interfaces are useful for grouping and reusing [operations](./operations.md).

You can declare interfaces using the `interface` keyword. Its name must be an [`identifier`](./identifiers.md).

```typespec
interface SampleInterface {
  foo(): int32;
  bar(): string;
}
```

## Composing interfaces

You can use the `extends` keyword to incorporate operations from other interfaces into a new interface.

Consider the following interfaces:

```typespec
interface A {
  a(): string;
}

interface B {
  b(): string;
}
```

You can create a new interface `C` that includes all operations from `A` and `B`:

```typespec
interface C extends A, B {
  c(): string;
}
```

This is equivalent to:

```typespec
interface C {
  a(): string;
  b(): string;
  c(): string;
}
```

## Interface templates

Interfaces can be templated. For more details on templates, [see templates](./templates.md).

```typespec
interface ReadWrite<T> {
  read(): T;
  write(t: T): void;
}
```

## Templating interface operations

Operations defined within an interface can also be templated. For more details on templates, [see templates](./templates.md).

```typespec
interface ReadWrite<T> {
  read(): T;
  write<R>(t: T): R;
}

alias MyReadWrite = ReadWrite<string>;

op myWrite is MyReadWrite.write<int32>;
```

:::caution
Any templated operation defined in an interface that is not instantiated will be omitted from the list of service operations.

This also applies when using `extends` on an interface that contains templated operations with unfilled template arguments.

```typespec
interface ReadWrite<T> {
  read(): T;
  write<R>(t: T): R;
}

interface MyReadWrite extends ReadWrite<string> {} // Here, the `read()` operation is fully instantiated and will be included in a service definition. However, `write()` is not.
```

When working with building block interfaces like this, use an alias to create your interface building block instead of `interface extends`. This way, the instantiated interface and its members will not be resolved in the service definition.

```typespec
alias MyReadWrite = ReadWrite<string>;

op myRead is MyReadWrite.read;
op myWrite is MyReadWrite.write<int32>;
```

:::

# Intersections

Language basics - composing models with intersections

Intersections in programming define a type that must encompass all the constituents of the intersection. You can declare an intersection using the `&` operator.

```typespec
alias Dog = Animal & Pet;
```

An intersection is functionally equivalent to [spreading](./models.md#spread) both types.

```typespec
alias Dog = {
  ...Animal;
  ...Pet;
};
```

# Models

Language basics - defining schemas with models

Models in TypeSpec are utilized to define the structure or schema of data.

## Types of models

Models can be categorized into two main types:

- [Record](#record)
- [Array](#array)

### Record

A Record model is a structure that consists of named fields, referred to as properties.

- The name can be an [`identifier`](./identifiers.md) or `string literal`.
- The type can be any type reference.
- Properties are arranged in a specific order. Refer to [property ordering](#property-ordering) for more details.

```typespec
model Dog {
  name: string;
  age: uint8;
}
```

#### Optional properties

Properties can be designated as optional by using the `?` symbol.

```typespec
model Dog {
  address?: string;
}
```

#### Default values

Properties can be assigned a default value using the `=` operator.

```typespec
model Dog {
  address?: string = "wild";
  age: uint8 = 0;
}
```

#### Property ordering

Properties are arranged in the order they are defined in the source. Properties acquired via `model is` are placed before properties defined in the model body. Properties obtained via `...` are inserted at the point where the spread appears in the source.

Example:

```tsp
model Pet {
  name: string;
  age: uint8;
}

model HasHome {
  address: string;
}

model Cat is Pet {
  meow: boolean;
  ...HasHome;
  furColor: string;
}

// The resulting property order for Cat is:
// name, age, meow, address, furColor
```

### Additional properties

The `Record<T>` model can be used to define a model with an arbitrary number of properties of type T. It can be combined with a named model to provide some known properties.

There are three ways to achieve this, each with slightly different semantics:

- Using the `...` operator
- Using the `is` operator
- Using the `extends` operator

#### Using the `...` operator

Spreading a Record into your model implies that your model includes all the properties you have explicitly defined, plus any additional properties defined by the Record. This means that a property in the model could be of a different and incompatible type with the Record value type.

```tsp
// In this example, the Person model has a property `age` that is an int32, but also has other properties that are all strings.
model Person {
  age: int32;
  ...Record<string>;
}
```

#### Using the `is` operator

When using `is Record<T>`, it indicates that all properties of this model are of type T. This means that each property explicitly defined in the model must also be of type T.

The example below would be invalid

```tsp
model Person is Record<string> {
  age: int32;
  //   ^ int32 is not assignable to string
}
```

But the following would be valid

```tsp
model Person is Record<string> {
  name: string;
}
```

#### Using the `extends` operator

The `extends` operator has similar semantics to `is`, but it defines the relationship between the two models. In many languages, this would probably result in the same emitted code as `is` and it is recommended to use `is Record<T>` instead.

```tsp
model Person extends Record<string> {
  name: string;
}
```

### Special property types

#### `never`

A model property can be declared as having the type `never`. This can be interpreted as the model not having that property.

This can be useful in a model template to omit a property.

```typespec
model Address<TState> {
  state: TState;
  city: string;
  street: string;
}

model UKAddress is Address<never>;
```

:::note
The responsibility of removing `never` properties lies with the emitter. The TypeSpec compiler will not automatically omit them.
:::

### Array

Arrays are models created using the `[]` syntax, which is a shorthand for using the `Array<T>` model type.

## Model composition

### Spread

The spread operator (`...`) copies the members of a source model into a target model. This operation doesn't create any nominal relationship between the source and target, making it useful when you want to reuse common properties without generating complex inheritance relationships.

```typespec
model Animal {
  species: string;
}

model Pet {
  name: string;
}

model Dog {
  ...Animal;
  ...Pet;
}

// The Dog model is equivalent to the following declaration:
model Dog {
  species: string;
  name: string;
}
```

### Extends

There are times when you want to create an explicit relationship between two models, such as when you're generating class definitions in languages that support inheritance. The `extends` keyword can be used to establish this relationship.

```typespec
model Animal {
  species: string;
}

model Dog extends Animal {}
```

### Is

There are instances when you want to create a new type that is an exact copy of an existing type but with additional properties or metadata, without creating a nominal inheritance relationship. The `is` keyword can be used for this purpose. It copies all the properties (like spread), but also copies [decorators](./decorators.md) as well. A common use case is to provide a better name to a [template](#model-templates) instantiation:

```typespec
@decorator
model Thing<T> {
  property: T;
}

model StringThing is Thing<string>;

// The StringThing declaration is equivalent to the following declaration:
@decorator
model StringThing {
  property: string;
}
```

## Model templates

Refer to [templates](./templates.md) for more details on templates.

```typespec
model Page<Item> {
  size: int32;
  item: Item[];
}

model DogPage {
  ...Page<Dog>;
}
```

## Meta type references

Some model property meta types can be referenced using `::`.

| Name | Example          | Description                              |
| ---- | ---------------- | ---------------------------------------- |
| type | `Pet.name::type` | Reference the type of the model property |

# Namespaces

Language basics - grouping declarations with namespaces

Namespaces in TypeSpec allow you to group related types together. This organization makes your types easier to locate and helps avoid naming conflicts. Namespaces are merged across files, enabling you to reference any type from anywhere in your TypeSpec program using its namespace.

## Basics

You can create a namespace using the `namespace` keyword.

```typespec
namespace SampleNamespace {
  model SampleModel {}
}
```

_Note: The namespace name must be a valid TypeSpec identifier._

You can then use `SampleNamespace` from other locations:

```typespec
model Foo {
  sample: SampleNamespace.SampleModel;
}
```

## Nested namespaces

Namespaces can contain sub-namespaces, offering additional layers of organization.

```typespec
namespace Foo {
  namespace Bar {
    namespace Baz {
      model SampleModel {}
    }
  }
}
```

Alternatively, you can simplify this using `.` notation:

```typespec
namespace Foo.Bar.Baz {
  model SampleModel {}
}
```

You can then use the sub-namespace from other locations using the fully qualified name.

```typespec
model A {
  sample: Foo.Bar.Baz.SampleModel;
}
```

## File-level namespaces

You can define a namespace for all declarations within a file at the top of the file (after any `import` statements) using a blockless namespace statement:

```typespec
namespace SampleNamespace;

model SampleModel {}
```

A file can only have one blockless namespace.

## Using namespaces

You can expose the contents of a namespace to the current scope using the `using` keyword.

```typespec
using SampleNamespace;

model Foo {
  sample: SampleModel;
}
```

The bindings introduced by a `using` statement are local to the namespace in which they are declared. They do not become part of the namespace themselves.

```typespec
namespace One {
  model A {}
}

namespace Two {
  using One;
  alias B = A; // This is valid
}

alias C = Two.A; // This is not valid
alias C = Two.B; // This is valid
```

# Operations

Language basics - defining endpoints with operations

Operations are essentially service endpoints, characterized by an operation name, parameters, and a return type.

You can declare operations using the `op` keyword. Its name must be an [`identifier`](./identifiers.md).

```typespec
op ping(): void;
```

## Parameters

The parameters of an operation represent a model. Therefore, you can perform any action with parameters that you can with a model, including the use of the spread operator:

```typespec
op feedDog(...CommonParams, name: string): void;
```

## Return type

Frequently, an endpoint may return one of several possible models. For instance, there could be a return type for when an item is located, and another for when it isn't. Unions are employed to express this scenario:

```typespec
model DogNotFound {
  error: "Not Found";
}

op getDog(name: string): Dog | DogNotFound;
```

## Reusing operations

You can reuse operation signatures with the `is` keyword. For example, given an operation

```typespec
op Delete(id: string): void;
```

You can reuse its signature like so:

```typespec
op deletePet is Delete;
```

This implies that `deletePet` will inherit the same parameters, return type, and decorators as the `Delete` operation.

This practice is typically used in conjunction with [operation templates](#operation-templates)

## Operation templates

For more information on templates, [see templates](./templates.md).

```typespec
op ReadResource<T>(id: string): T;
```

You can reference the operation template using `is`:

```typespec
op readPet is ReadResource<Pet>;
```

## Meta type references

Certain operation meta types can be referenced using `::`

| Name       | Example               | Description                                |
| ---------- | --------------------- | ------------------------------------------ |
| parameters | `readPet::parameters` | References the parameters model expression |
| returnType | `readPet::returnType` | References the operation return type       |

# Overview

Language basics - overview

This document provides a concise overview of the language concepts in TypeSpec. It serves as a quick reference guide rather than an in-depth tutorial.

## Declarations

- Names of declarations must be unique across different types within the same scope. For instance, the following is not permissible:
  <!-- prettier-ignore -->
  ```typespec
  model Dog {}
  namespace Dog {}
  ```

## Imports

_For more details, see: [Imports](./imports.md)_

| Feature              | Example                   |
| -------------------- | ------------------------- |
| Import TypeSpec file | `import "./models.tsp"`   |
| Import JS file       | `import "./models.js"`    |
| Import Library       | `import "@typespec/rest"` |

## Namespaces

_For more details, see: [Namespaces](./namespaces.md)_

| Feature           | Example                      |
| ----------------- | ---------------------------- |
| Declare namespace | `namespace PetStore {}`      |
| File namespace    | `namespace PetStore;`        |
| Nested namespace  | `namespace PetStore.Models;` |
| Using namespace   | `using PetStore.Models;`     |

## Decorators

_For more details, see: [Decorators](./decorators.md)_

| Feature                      | Example                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| Use decorator                | `@mark`                                                                             |
| Use decorator with arguments | `@tag("abc")`                                                                       |
| Declare a decorator in JS    | `export function $tag(context: DecoratorContext, target: Type, name: string) {...}` |
| Save state in decorator      | `context.program.stateMap(key).set(target, <value>)`                                |
| Augment decorator            | `@@tag(MyType, "abc");`                                                             |

## Scalars

_For more details, see: [Scalars](./scalars.md)_

| Feature            | Example                                     |
| ------------------ | ------------------------------------------- |
| Scalar declaration | `scalar ternary`                            |
| Extend scalar      | `scalar Password extends string`            |
| Template scalar    | `@doc(T) scalar Password<T extends string>` |

## Models

_For more details, see: [Models](./models.md)_

| Feature                        | Example                               |
| ------------------------------ | ------------------------------------- |
| Model declaration              | `model Pet {}`                        |
| Model inheritance              | `model Dog extends Pet {}`            |
| scalar is                      | `model uuid extends string;`          |
| Model spread                   | `model Dog {...Animal}`               |
| Property                       | `model Dog { name: string }`          |
| Optional property              | `model Dog { owner?: string }`        |
| Optional property with default | `model Dog { name?: string = "Rex" }` |
| Model template                 | `model Pet<T> { t: T }`               |

## Operations

_For more details, see: [Operations](./operations.md)_

| Feature                       | Example                                          |
| ----------------------------- | ------------------------------------------------ |
| Operation declaration         | `op ping(): void`                                |
| Operation with parameters     | `op upload(filename: string, data: bytes): void` |
| Operation with return type    | `op health(): HealthStatus`                      |
| Operation with multiple types | `op health(): HealthStatus \| ErrorResponse`     |
| Operation template            | `op getter<T>(id: string): T`                    |
| Operation is                  | `op getPet is getter<Pet>;`                      |

## Interfaces

_For more details, see: [Interfaces](./interfaces.md)_

| Feature               | Example                                |
| --------------------- | -------------------------------------- |
| Interface declaration | `interface PetStore { list(): Pet[] }` |
| Interface composition | `interface PetStore extends Store { }` |
| Interface template    | `interface Restful<T> { list(): T[] }` |

## Templates

_For more details, see: [Templates](./templates.md)_

| Feature                           | Example                                             |
| --------------------------------- | --------------------------------------------------- |
| Simple template                   | `model Response<T> {value: T}`                      |
| Template with multiple parameters | `model Response<K, V> {key: K, value: T}`           |
| Template default                  | `model Response<T = string> {value: T}`             |
| Template constraints              | `model Response<T extends {id: string}> {value: T}` |
| Template constraints and defaults | `model Response<T extends string = ""> {value: T}`  |

## Enums

_For more details, see: [Enums](./enums.md)_

| Feature            | Example                                        |
| ------------------ | ---------------------------------------------- |
| Enum declaration   | `enum Direction {Up, Down}`                    |
| Enum string values | `enum Direction {Up: "up", Down: "down"}`      |
| Enum int values    | `enum Size {Small: 1000, Large: 2000}`         |
| Enum float values  | `enum Part {Quarter: 0.25, Half: 0.5}`         |
| Enum composing     | `enum Direction2D {...Direction, Left, Right}` |

## Unions

_For more details, see: [Unions](./unions.md)_

| Feature                 | Example                          |
| ----------------------- | -------------------------------- |
| Union declaration       | `"cat" \| "dog"`                 |
| Named union declaration | `union Pet {cat: Cat, dog: Dog}` |

## Intersections

_For more details, see: [Intersections](./intersections.md)_

| Feature                  | Example        |
| ------------------------ | -------------- |
| Intersection declaration | `Pet & Animal` |

## Type literals

_For more details, see: [Type literals](./type-literals.md)_

| Feature           | Example                                                  |
| ----------------- | -------------------------------------------------------- |
| String            | `"Hello world!"`                                         |
| Multi line String | `"""\nHello world!\n"""` (\n) represent actual new lines |
| Int               | `10`                                                     |
| Float             | `10.0`                                                   |
| Boolean           | `false`                                                  |

## Aliases

_For more details, see: [Aliases](./alias.md)_

| Feature           | Example                           |
| ----------------- | --------------------------------- |
| Alias declaration | `alias Options = "one" \| "two";` |

# Scalars

Language basics - custom scalars

Scalars are simple types that don't have any fields. Examples of these include `string`, `int32`, `boolean`, and so on.

You can declare a scalar by using the `scalar` keyword. Its name must be an [`identifier`](./identifiers.md).

```typespec
scalar ternary;
```

## Extending a scalar

You can create a new scalar that extends an existing one by using the `extends` keyword.

```typespec
scalar Password extends string;
```

## Scalars with template parameters

Scalars can also support template parameters. These template parameters are primarily used for decorators.

```typespec
@doc(Type)
scalar Unreal<Type extends valueof string>;
```

## Scalar initializers

Scalars can be declared with an initializer for creating specific scalar values based on other values. For example:

```typespec
scalar ipv4 extends string {
  init fromInt(value: uint32);
}

const homeIp = ipv4.fromInt(2130706433);
```

Initializers do not have any runtime code associated with them. Instead, they merely record the scalar initializer invoked along with the arguments passed so that emitters can construct the proper value when needed.

### Date/time initializers

The built-in date and time scalars provide initializers for common use cases:

#### `fromISO`: create from ISO 8601 string

```typespec
const date = plainDate.fromISO("2024-05-06");
const time = plainTime.fromISO("12:34");
const timestamp = utcDateTime.fromISO("2024-05-06T12:20:00Z");
const offsetTime = offsetDateTime.fromISO("2024-05-06T12:20:00-07:00");
const period = duration.fromISO("P1Y1D");
```

#### `now`: current date/time

The `now()` initializer indicates that the current date or time should be used. Emitters interpret this as the appropriate runtime value (e.g., database `CURRENT_TIMESTAMP`, JavaScript `Date.now()`, etc.).

```typespec
model Record {
  createdAt: utcDateTime = utcDateTime.now();
  updatedAt: utcDateTime = utcDateTime.now();
}

model Event {
  date: plainDate = plainDate.now();
  time: plainTime = plainTime.now();
}
```

# Templates

Language basics - reusability with templates

Templates are a powerful tool that allow users to customize certain aspects of a type. Similar to generics in other programming languages, templates define template parameters that users can specify when referencing the type.

Templates can be applied to:

- [aliases](./alias.md)
- [models](./models.md)
- [operations](./operations.md)
- [interfaces](./interfaces.md)

```typespec
model Page<Item> {
  size: int32;
  item: Item[];
}

model DogPage {
  ...Page<Dog>;
}
```

## Default values

You can assign a default value to a template parameter using `= <value>`.

```typespec
model Page<Item = string> {
  size: int32;
  item: Item[];
}
```

## Parameter constraints

You can impose constraints on template parameters using the `extends` keyword. For details on how validation works, refer to the [type relations](./type-relations.md) documentation.

```typespec
alias Foo<Type extends string> = Type;
```

If you try to instantiate Foo with an argument that does not meet the `string` constraint, you will encounter an error:

```typespec
alias Bar = Foo<123>;
                ^ Type '123' is not assignable to type 'TypeSpec.string'
```

A template parameter constraint can also be a model expression:

```typespec
// Expect Type to be a model with property name: string
alias Foo<Type extends {name: string}> = Type;
```

Default values for template parameters must also adhere to the constraint:

```typespec
alias Foo<Type extends string = "Abc">  = Type;
// Invalid
alias Bar<Type extends string = 123>  = Type;
                             ^ Type '123' is not assignable to type 'TypeSpec.string'
```

Also, all optional arguments must be placed at the end of the template. A required argument cannot follow an optional argument:

```typespec
// Invalid
alias Foo<T extends string = "Abc", U> = ...;
                                    ^ Required template arguments must not follow optional template arguments
```

## Named template arguments

Template arguments can also be specified by name. This allows you to specify them out of order and omit optional arguments. This can be particularly useful when dealing with templates that have many arguments with defaults:

```typespec
alias Test<T, U extends numeric = int32, V extends string = "example"> = {
  t: T;
  v: V;
};

// Specify the argument V by name to skip argument U, since U is optional and we
// are okay with its default
alias Example1 = Test<unknown, V = "example1">;

// Even all three arguments can be specified out of order
alias Example2 = Test<V = "example2", T = unknown, U = uint64>;
```

However, once a template argument is specified by name, all subsequent arguments must also be specified by name:

```typespec
// Invalid
alias Example3 = Test<
  V = "example3",
  unknown,
  ^^^^^^^ Positional template arguments cannot follow named arguments in the same argument list.
>;
```

Since template arguments can be specified by name, the names of template parameters are part of the template's public API. **Renaming a template parameter may break existing specifications that use the template.**

**Note**: Template arguments are evaluated in the order the parameters are defined in the template _definition_, not the order in which they are written in the template _instance_. While this is usually inconsequential, it may be important in some cases where evaluating a template argument may trigger decorators with side effects.

## Templates with values

Templates can be declared to accept values using a `valueof` constraint. This is useful for providing default values and parameters for decorators that take values.

```typespec
alias TakesValue<StringType extends string, StringValue extends valueof string> = {
  @doc(StringValue)
  property: StringType;
};

alias M1 = TakesValue<"a", "b">;
```

When a passing a literal or an enum or union member reference directly as a template parameter that accepts either a type or a value, we pass the value. In particular, `StringTypeOrValue` is a value with the string literal type `"a"`.

```typespec
alias TakesTypeOrValue<StringTypeOrValue extends string | (valueof string)> = {
  @customDecorator(StringOrValue)
  property: string;
};

alias M1 = TakesValue<"a">;
```

The [`typeof` operator](./values.md#the-typeof-operator) can be used to get the declared type of a value if needed.

### Template parameter value types

When a template is instantiated with a value, the type of the value and the result of the `typeof` operator is determined based on the argument rather than the template parameter constraint. This follows the same rules as [const declaration type inference](./values.md#const-declarations). In particular, inside the template `TakesValue`, the type of `StringValue` is the string literal type `"b"`. If we passed a `const` instead, the type of the value would be the const's type. In the following example, the type of `property` in `M1` is `"a" | "b"`.

```typespec
alias TakesValue<StringValue extends valueof string> = {
  @doc(StringValue)
  property: typeof StringValue;
};

const str: "a" | "b" = "a";
alias M1 = TakesValue<str>;
```

# Type Literals

Language basics - literal types

When designing APIs, it's common to define the structure of the API in terms of specific literal values. For instance, an operation might return a specific integer status code, or a model member might be one of a few specific string values. It's also useful to pass specific literal values to decorators. TypeSpec supports string, number, and boolean literal values to cater to these needs.

## String literals

String literals are represented using double quotes `"`.

```typespec
alias Str = "Hello World!";
```

## Multi-line string literals

Multi-line string literals are denoted using three double quotes `"""`.

```typespec
alias Str = """
  This is a multi line string
   - opt 1
   - opt 2
  """;
```

- The opening `"""` must be followed by a new line.
- The closing `"""` must be preceded by a new line.

### Trimming indentation in multi-line strings

Multi-line strings automatically trim leading whitespaces on each line to align with the closing `"""`. This feature is handy for maintaining the indentation of multi-line strings within the code without worrying about undesired indentation.

All the following options will yield the same string value `"one\ntwo"`.

```typespec
model MultiLineContainer {
  prop1: """
    one
    two
    """;

  // Lines are indented at the same level as closing """"
  prop2: """
    one
    two
    """;

  prop3: """
    one
    two
    """;
}
```

Please note all lines in triple-quoted string lines must have the same indentation as closing triple quotes. The following code will be flagged with an error.

```typespec

  // lines are less indented as the closing """"
  prop4: """
    one
    two
      """;
      ^-- error triple-quote-indent All lines in triple-quoted string lines must have the same indentation as closing triple quotes.
```

## String template literal

Both single and multi-line string literals can be interpolated using `${}`.

```typespec
alias hello = "bonjour";
alias Single = "${hello} world!";

alias Multi = """
  ${hello} 
  world!
  """;
```

Any valid expression can be used in the interpolation, but only other literals will result in the template literal being assignable to a `valueof string`. Any other value will depend on the decorator/emitter receiving it for handling.

## Numeric literal

Numeric literals are declared by using the raw number.

```typespec
alias Kilo = 1000;
alias PI = 3.14;
```

## Boolean literal

Boolean literals are declared by using the `true` or `false` keywords.

```typespec
alias InTypeSpec = true;
alias Cheater = false;
```

# Type Relations

Language basics - type relations

## Type hierarchy

```mermaid
graph RL
    record["Record<Element>"] --> unknown
    customModel["Custom model with properties"] --> record["Record<T>"]
    array["Array<Element>"] --> unknown
    tuple["Tuple"] --> array
    numeric --> unknown
    subgraph numerics[For numeric types, a narrower type can be assigned to a wider one]
      integer --> numeric
        int8 --> integer
        int16 --> integer
        int32 --> integer
        safeint --> integer
        int64 --> integer
        uint8 --> integer
        uint16 --> integer
        uint32 --> integer
        uint64 --> integer
      float --> numeric
        float32 --> float
        float64 -->  float
      decimal --> numeric
        decimal128 --> decimal
    end
    string --> unknown
    boolean --> unknown
    null --> unknown
    bytes --> unknown
    plainDate --> unknown
    plainTime --> unknown
    zoneDateTime --> unknown
    duration --> unknown
```

## Model with properties

When determining if type `S` can be assigned to type `T`, if `T` is a model with properties, it checks whether all those properties are present in `S` and if their types can be assigned to the type of the corresponding property in `T`.

For instance,

```typespec
model T {
  foo: string;
  bar: int32;
}

// Valid

model S { // When properties types are the exact same
  foo: string;
  bar: int32;
}
model S { // When the properties types are literal assignable to the target type
  foo: "abc";
  bar: 123;
}
model S {
  foo: string;
  bar: int8; // int8 is assignable to int16
}
model S {
  foo: string;
  bar: int32;
  otherProp: boolean; // Additional properties are valid.
}

// Invalid
model S { // Missing property bar
  foo: string;
}
model S {
  foo: string;
  bar: int64; // int64 is NOT assignable to int32
}
```

## `Record<T>`

A record is a model indexed with a string with a value of T. It represents a model where all properties (string keys) are assignable to the type T. You can assign a model expression where all the properties are of type T or another model that `is` also a `Record<T>`.

```typespec
// Represent an object where all the values are int32.
alias T = Record<int32>;

// Valid
alias S = {
  foo: 123;
  bar: 345;
};
alias S = {
  foo: int8;
  bar: int32;
};
model S is Record<int32>;
model S is Record<int32> {
  foo: 123;
}

// Invalid
alias S = {
  foo: "abc";
  bar: 456;
};
alias S = {
  foo: int64;
  bar: int32;
};
model S {
  foo: 123;
  bar: 456;
}
```

#### Why isn't the last case assignable to `Record<int32>`?

In this scenario,

```typespec
alias T = Record<int32>;
model S {
  foo: 123;
  bar: 456;
}
```

The reason why `model S` is not assignable, but the model expression `{ foo: 123; bar: 456; }` is, is because model S could be extended with additional properties that might not be compatible.

For instance, if you add a new model,

```typespec
model Foo is S {
  otherProp: string;
}
```

Here, `Foo` is assignable to `S` following the [model with property logic](#model-with-properties), and if `S` was assignable to `Record<int32>`, `Foo` would also be passable. However, this is now invalid as `otherProp` is not an `int32` property.

# Unions

Language basics - unions

Unions define a type that must be exactly one of several possible variants. There are two types of unions:

- Union expressions
- Named unions

## Union expressions

Unnamed unions, or union expressions, can be declared by combining the variants using the `|` operator.

```typespec
alias Breed = Beagle | GermanShepherd | GoldenRetriever;
```

In this example, `Breed` can be either a `Beagle`, a `GermanShepherd`, or a `GoldenRetriever`.

## Named unions

Named unions allow you to assign a name to the union and provide explicit variant references. Named unions are somewhat similar to [enums](./enums.md), but instead of having `string` or `numeric` values, they use [record models](./models.md).

A named union can be declared with the `union` keyword. Its name must be an [`identifier`](./identifiers.md).

```typespec
union Breed {
  beagle: Beagle,
  shepherd: GermanShepherd,
  retriever: GoldenRetriever,
}
```

The above example is equivalent to the `Breed` alias mentioned earlier, with the difference that emitters can recognize `Breed` as a named entity and also identify the `beagle`, `shepherd`, and `retriever` names for the options. This format also allows the application of [decorators](./decorators.md) to each of the options.

# Values

Language basics - working with values

TypeSpec can define values in addition to types. Values are useful in an API description to define default values for types or provide example values. They are also useful when passing data to decorators, and for template parameters that are ultimately passed to decorators or used as default values.

Values cannot be used as types, and types cannot be used as values, they are completely separate. However, string, number, boolean, and null literals can be either a type or a value depending on context (see also [scalar literals](#scalar-literals)). Additionally, union and enum member references may produce a type or a value depending on context (see also [enum member &amp; union variant references](#enum-member--union-variant-references)).

## Value kinds

There are four kinds of values: objects, arrays, scalars, and null. These values can be created with object values, array values, scalar values and initializers, and the null literal respectively. Additionally, values can result from referencing enum members and union variants.

### Object values

Object values use the syntax `#{}` and can define any number of properties. For example:

```typespec
const point = #{ x: 0, y: 0 };
```

The object value's properties must refer to other values. It is an error to reference a type.

```typespec
const example = #{
  prop1: #{ nested: true }, // ok
  prop2: {
    nested: true,
  }, // error: values can't reference a type
  prop3: string, // error: values can't reference a type
};
```

### Array values

Array values use the syntax `#[]` and can define any number of items. For example:

```typespec
const points = #[#{ x: 0, y: 0 }, #{ x: 1, y: 1 }];
```

As with object values, array values cannot contain types.

If an array type defines a minimum and maximum size using the `@minValue` and `@maxValue` decorators, the compiler will validate that the array value has the appropriate number of items. For example:

```typespec
/** Can have at most 2 tags */
@maxItems(2)
model Tags is Array<string>;

const exampleTags1: Tags = #["TypeSpec", "JSON"]; // ok
const exampleTags2: Tags = #["TypeSpec", "JSON", "OpenAPI"]; // error
```

### Scalar values

There are two ways to create scalar values: with a literal syntax like `"string value"`, and with a scalar initializer like `utcDateTime.fromISO("2020-12-01T12:00:00Z")`.

#### Scalar literals

The literal syntax for strings, numerics, booleans and null can evaluate to either a type or a value depending on the surrounding context of the literal. When the literal is in _type context_ (a model property type, operation return type, alias definition, etc.) the literal becomes a literal type. When the literal is in _value context_ (a default value, property of an object value, const definition, etc.), the literal becomes a value. When the literal is in an _ambiguous context_ (e.g. an argument to a template or decorator that can accept either a type or a value) the literal becomes a value. The `typeof` operator can be used to convert the literal to a type in such ambiguous contexts.

```typespec
// Sample decorator signatures. They have no backing implementation and shown here for demonstration purposes.
extern dec setNumberValue(target: unknown, color: valueof numeric);
extern dec setNumberType(target: unknown, color: numeric);
extern dec setNumberTypeOrValue(target: unknown, color: numeric | (valueof numeric));

@setNumberValue(123) // Passes the scalar value `numeric(123)`.
@setNumberType(123) // Passes the numeric literal type 123.
@setNumberTypeOrValue(123) // passes the scalar value `numeric(123)`.
model A {}
```

#### Scalar initializers

Scalar initializers create scalar values by calling an initializer with one or more values. Scalar initializers for types extended from `numeric`, `string`, and `boolean` are called by adding parenthesis after the scalar reference:

```typespec
const n = int8(100);
const s = string("hello");
```

Any scalar can additionally be declared with named initializers that take one or more value parameters. For example, `utcDateTime` provides a `fromISO` initializer that takes an ISO string. Named scalars can be declared like so:

```typespec
scalar ipv4 extends string {
  init fromInt(value: uint32);
}

const ip = ipv4.fromInt(2341230);
```

#### Null values

Null values are created with the `null` literal.

```typespec
const value: string | null = null;
```

The `null` value, like the `null` type, doesn't have any special behavior in the TypeSpec language. It is just the value `null` like that in JSON.

## Const declarations

Const declarations allow storing values in a variable for later reference. Const declarations have an optional type annotation. When the type annotation is absent, the type is inferred from the value by constructing an exact type from the initializer.

```typespec
const stringValue: string = "hello";
//      ^-- type: string

const oneValue = 1;
//      ^-- type: 1

const objectValue = #{ x: 0, y: 0 };
//      ^-- type: { x: 0, y: 0 }
```

## The `typeof` operator

The `typeof` operator returns the declared or inferred type of a value reference. Note that the actual value being stored by the referenced variable may be more specific than the declared type of the value. For example, if a const is declared with a union type, the value will only ever store one specific variant at a time, but typeof will give you the declared union type.

```typespec
const stringValue: string = "hello";
// typeof stringValue returns `string`.

const oneValue = 1;
// typeof oneValue returns `1`

const stringOrOneValue: string | 1 = 1;
// typeof stringOrOneValue returns `string | 1`
```

## Validation

TypeSpec will validate values against built-in validation decorators like `@minLength` and `@maxValue`.

```typespec
@maxLength(3)
scalar shortString extends string;

const s1: shortString = "abc"; // ok
const s2: shortString = "abcd"; // error:

model Entity {
  a: shortString;
}

const e1: Entity = #{ a: "abcd" }; // error
```

## Enum member &amp; union variant references

References to enum members and union variants can be either types or values and follow the same rules as scalar literals. When an enum member reference is in _type context_, the reference becomes an enum member type. When in _value context_ or _ambiguous context_ the reference becomes the enum member's value.

```typespec
extern dec setColorValue(target: unknown, color: valueof string);
extern dec setColorMember(target: unknown, color: Reflection.EnumMember);

enum Color {
  red,
  green,
  blue,
}

@setColorValue(Color.red) // same as passing the literal "red"
@setColorMember(Color.red) // passes the enum member Color.red
model A {}
```

When a union variant reference is in _type context_, the reference becomes the type of the union variant. When in _value context_ or _ambiguous context_ the reference becomes the value of the union variant. It is an error to refer to a union variant whose type is not a literal type.

```typespec
extern dec setColorValue(target: unknown, color: valueof string);
extern dec setColorType(target: unknown, color: string);

union Color {
  red: "red",
  green: "green",
  blue: "blue",
  other: string,
}

@setColorValue(Color.red) // passes the scalar value `string("red")`
@setColorValue(Color.other) // error, trying to pass a type as a value.
@setColorType(Color.red) // passes the string literal type `"red"`
model A {}
```

# Visibility

Language basics - defining views of a model across operations with visibility

**Visibility** is a language feature that allows you to share a model between multiple operations and define in which contexts
properties of the model are "visible." Visibility is a very powerful feature that allows you to define different "views"
of a model within different operations or contexts.

**Note** ⚠️: Enum-based visibility as described in this document _replaces_ visibility strings that you may have used
in the past. The system is backwards-compatible with visibility strings, but you should use enum-based visibility for
new specifications. String-based visibility (e.g. `@visibility("create")`) may be deprecated and removed in future
versions of TypeSpec.

## Basic concepts

- Visibility applies to _model properties_ only. It is used to determine when an emitter should include or exclude a
  property in a certain context.
- Visibility is defined using a _visibility class_. A visibility class is an `enum` that defines the visibility modifiers
  (or flags) that can be applied to a property. Any `enum` can serve as a visibility class.
- Visibility classes have a _default_ visibility, which is the set of visibility modifiers that are applied _by default_
  to a property if the visibility is not explicitly set.

## Lifecycle visibility

TypeSpec provides a built-in visibility called "resource lifecycle visibility." This visibility allows you to declare
whether properties are visible when passing a resource to or reading a resource from an API endpoint. For example:

```typespec
model Example {
  /**
   * The unique identifier of this resource.
   *
   * The ID is automatically generated by the service, so it cannot be set when the resource is created or updated,
   * but the server will return it when the resource is read.
   */
  @visibility(Lifecycle.Read)
  id: string;

  /**
   * The name of this resource.
   *
   * The name can be set when the resource is created, but may not be changed.
   */
  @visibility(Lifecycle.Create, Lifecycle.Read)
  name: string;

  /**
   * The description of this resource.
   *
   * By default, properties are visible in all lifecycle phases, so this property
   * is present in all lifecycle phases.
   */
  description: string;
}
```

In the above example, each property of the `Example` model has a lifecycle visibility that instructs emitters to include
or exclude the property when creating, updating, or reading the `Example` resource.

TypeSpec's HTTP library, OpenAPI emitter, and other standard functionality use the `Lifecycle` visibility to create
different views of the `Example` model based on which lifecycle phase is used in a particular operation.

In the following example, the type of the input and output of each operation is affected by the lifecycle visibility
of the properties in the `Example` model.

```typespec
@route("/example")
interface Examples {
  /**
   * When an operation uses the POST verb, it uses the `Create` lifecycle visibility to determine which properties
   * are visible.
   */
  @post create(@body example: Example): Created<Example> | Error;

  /**
   * When an operation uses the GET verb, it uses the `Read` lifecycle visibility to determine which properties
   * are visible.
   */
  @get read(@path id: string): Ok<Example> | Error;

  /**
   * When an operation uses the PATCH verb, it uses the `Update` lifecycle visibility to determine which properties
   * are visible.
   */
  @patch update(@path id: string, @body example: Example): Ok<Example> | Error;
}
```

The above interface generates the following OpenAPIv3 schemas:

```yml
paths:
  /example:
    post:
      parameters: []
      responses:
        "200":
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Example"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Example"
  /example/{id}:
    get:
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Example"
    patch:
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Example"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/ExampleUpdate"
components:
  schemas:
    Example:
      type: object
      required:
        - id
        - name
        - description
      properties:
        id:
          type: string
          readOnly: true
        name:
          type: string
        description:
          type: string
    ExampleUpdate:
      type: object
      properties:
        description:
          type: string
```

Notice:

- The `id` property is marked `readOnly: true` because it is only visible when reading the resource.
- The `ExampleUpdate` schema only includes the `description` property because it is the only property that is visible
  when updating the resource.
- Each of the `paths` reference the correct schema based on the lifecycle phase that the operations use.
- The TypeSpec model is only defined _once_, and any changes in the output schemas are derived from the lifecycle
  visibility of the properties in the model.

### Lifecycle modifiers

The following visibility modifiers are available in the `Lifecycle` visibility class:

- `Create`: The property is visible when the resource is created. This visibility is checked, for example, when a property
  is a parameter in an HTTP `POST` operation.
- `Read`: The property is visible when the resource is read. This visibility is checked, for example, when a property is
  returned in an HTTP `GET` operation.
- `Update`: The property is visible when the resource is updated. This visibility is checked, for example, when a property
  is a parameter in an HTTP `PATCH` or `PUT` operation.
- `Delete`: The property is visible when a resource is deleted. This visibility is checked, for example, when a property
  is a parameter in an HTTP `DELETE` operation.
- `Query`: The property is visible when a resource is passed as a parameter in a query. This visibility is checked, for
  example, when a property is a parameter in an HTTP `GET` operation (**this should not be confused with an HTTP query
  parameter defined using `@query`**).

### Lifecycle visibility transforms

You can explicitly compute the shape of a model within a _specific_ lifecycle phase by using the four built-in
templates for lifecycle transforms:

- `Create<T extends Model>`: creates a copy of `T` with only the properties that are visible in the `Create` lifecycle
  phase, recursively.
- `Read<T extends Model>`: creates a copy of `T` with only the properties that are visible in the `Read` lifecycle phase,
  recursively.
- `Update<T extends Model>`: creates a copy of `T` with only the properties that are visible in the `Update` lifecycle
  phase, with the types of the properties set to `CreateOrUpdate<T>`, recursively.
- `CreateOrUpdate<T>`: creates a copy of `T` with only the properties that have _either_ the `Create` or `Update`
  visibility modifiers enabled, recursively.
- `Delete<T>`: creates a copy of `T` with only the properties that have the `Lifecycle.Delete` modifier enabled,
  recursively.
- `Query<T>`: creates a copy of `T` with only the properties that have the `Lifecycle.Query` modifier enabled,
  recursively.

For example:

```typespec
model Example {
  @visibility(Lifecycle.Create)
  id: string;

  @visibility(Lifecycle.Create, Lifecycle.Read)
  name: string;

  @visibility(Lifecycle.Update)
  description: string;
}

model ReadExample is Read<Example>;

model CreateExample is Create<Example>;

model UpdateExample is Update<Example>;

model CreateOrUpdateExample is CreateOrUpdate<Example>;
```

When you use these templates, the resulting models have no `Lifecycle` visibility modifiers applied, so that any
emitters or libraries that use lifecycle visibility will not alter them further.

## Visibility modifiers

Each property has its own set of _active visibility modifiers_ for each visibility class. The active modifiers can be
changed using the decorators described in this section.

**Note**: Changing the visibility for one visibility class _does not_ affect other visibility classes. If you change the
visibility for the `Lifecycle` visibility class, it will not affect the modifiers that are active for _any_ other
visibility classes.

### `@visibility`

The `@visibility` decorator _enables_ visibility modifiers. It takes a list of visibility modifiers as arguments and
sets them on the property. For example:

```typespec
@visibility(Lifecycle.Create, Lifecycle.Read)
name: string;
```

In this example, the `name` property has the `Create` and `Read` visibility modifiers enabled.

If visibility has _already_ been set explicitly on a property, the `@visibility` decorator _ADDS_ its own visibility
modifiers to the currently-active modifiers. It does not _replace_ the existing modifiers. For example:

```typespec
@visibility(Lifecycle.Create)
@visibility(Lifecycle.Read)
name: string;
```

In this example, the `name` property has both the `Create` and `Read` visibility modifiers enabled, but _not_ the `Update`
visibility modifier. The `@visibility` decorator starts from an _empty_ set of modifiers and adds the `Create` modifier,
then adds the `Read` modifier.

### `@removeVisibility`

The `@removeVisibility` decorator _disables_ visibility modifiers. It takes a list of visibility modifiers as arguments
and removes them from the property. For example:

```typespec
@removeVisibility(Lifecycle.Update)
name: string;
```

This use of `@removeVisibility` is equivalent to the above examples with the `@visibility` decorator, but it uses the `@removeVisibility`
decorator to remove the `Update` visibility modifier from the `name` property rather than adding the `Create` and `Read`
visibility modifiers. The `@removeVisibility` decorator starts from the _default_ set of visibility modifiers and removes
the `Update` modifier.

If the visibility has _already_ been set on a property, the `@removeVisibility` decorator _removes_ its visibility from
the currently-active modifiers. It does not _replace_ the existing modifiers. For example:

```typespec
@removeVisibility(Lifecycle.Update)
@removeVisibility(Lifecycle.Create)
id: string;
```

In this example, the `id` property has the `Update` and `Create` visibility modifiers removed, but it retains the `Read`
visibility modifier.

### `@invisible`

The `@invisible` decorator _disables all visibility modifiers_ on a property within a given visibility class. For example:

```typespec
@invisible(Lifecycle)
invisible: string;
```

In this example, the `invisible` property has _no_ visibility modifiers enabled in the `Lifecycle` visibility class.

## Visibility filters

The `@withVisibilityFilter` decorator allows you to transform a model by applying a visibility filter to it. A
visibility filter is an object that defines constraints on which visibility modifiers must be enabled/disabled for a
property to be visible. For example:

```typespec
model Example {
  @visibility(Lifecycle.Create)
  id: string;

  @visibility(Lifecycle.Create, Lifecycle.Read)
  name: string;

  @visibility(Lifecycle.Update)
  description: string;
}

@withVisibilityFilter(#{ all: [Lifecycle.Create, Lifecycle.Read] })
model CreateAndReadExample {
  ...Example;
}

@withVisibilityFilter(#{ any: [Lifecycle.Create, Lifecycle.Update] })
model CreateOrUpdateExample {
  ...Example;
}

@withVisibilityFilter(#{ none: [Lifecycle.Update] })
model NonUpdateExample {
  ...Example;
}
```

In the above example, the `CreateAndReadExample` model is a copy of the `Example` model with only the the properties
that have _BOTH_ the `Create` and `Read` visibility modifiers enabled (i.e. only the `name` property). The
`CreateOrUpdateExample` model is a copy of the `Example` model with only the properties that have _EITHER_ the `Create`
or `Update` visibility modifiers enabled (i.e. the `id` and `name` properties). The `NonUpdateExample` model is a copy
of the `Example` model with only the properties that _do not_ have the `Update` visibility modifier enabled (i.e. the
`id` and `name` properties).

**Note**: For `Lifecycle` visibility, you should ordinarily use the `Create`, `Read`, `Update`, and `CreateOrUpdate`
templates instead of `@withVisibilityFilter` directly, but you can use `@withVisibilityFilter` to create custom "views"
of a model that use visibility classes other than `Lifecycle` or custom filter logic.

## Visibility classes

Any TypeSpec `enum` can serve as a visibility class. The members of the `enum` define the visibility modifiers in the
class. For example, the following is the definition of the `Lifecycle` visibility class defined in the TypeSpec standard
library:

```typespec
enum Lifecycle {
  Create,
  Read,
  Update,
}
```

This visibility class defines three visibility modifiers: `Create`, `Read`, and `Update`. By default, all properties
have _ALL_ three visibilities in the `Lifecycle` enum enabled.

### Setting default visibility

You can set the default visibility for a visibility class by declaring it on the enum using the `@defaultVisibility`
decorator:

```typespec
@defaultVisibility(Example.A)
enum Example {
  A,
  B,
}
```

In this example, any property that does not declare an `Example` visibility modifier will have the `A` visibility by
default.

**Note**: While you can define your own visibility classes, emitters _will not recognize them_ unless they have been
programmed to do so. You can leverage custom visibility classes in your own emitters, but they will have no effect on
the standard emitters unless those emitters choose to adopt and recognize those visibility classes as meaningful. The
`Lifecycle` visibility class is a standard visibility class that is recognized by several emitters. You can, however,
use your own visibility classes with the built in `@withVisibilityFilter` decorator to transform your models in whatever
ways you see fit.

# Decorators

Decorators exported by @typespec/events

## TypeSpec.Events

### `@contentType` {#@TypeSpec.Events.contentType}

Specifies the content type of the event envelope, event body, or event payload.
When applied to an event payload, that field must also have a corresponding `@data`
decorator.

```typespec
@TypeSpec.Events.contentType(contentType: valueof string)
```

#### Target

`UnionVariant | ModelProperty`

#### Parameters

| Name        | Type             | Description |
| ----------- | ---------------- | ----------- |
| contentType | `valueof string` |             |

#### Examples

```typespec
@events
union MixedEvents {
  @contentType("application/json")
  message: {
    id: string,
    text: string,
  },
}
```

##### Specify the content type of the event payload.

```typespec
@events
union MixedEvents {
  {
    done: true,
  },
  {
    done: false,
    @data @contentType("text/plain") value: string,
  },
}
```

### `@data` {#@TypeSpec.Events.data}

Identifies the payload of an event.
Only one field in an event can be marked as the payload.

```typespec
@TypeSpec.Events.data
```

#### Target

`ModelProperty`

#### Parameters

None

#### Examples

```typespec
@events
union MixedEvents {
  {
    metadata: Record<string>,
    @data payload: string,
  },
}
```

### `@events` {#@TypeSpec.Events.events}

Specify that this union describes a set of events.

```typespec
@TypeSpec.Events.events
```

#### Target

`Union`

#### Parameters

None

#### Examples

```typespec
@events
union MixedEvents {
  pingEvent: string,
  doneEvent: "done",
}
```

# Authentication

Configuring HTTP authentication

## Configure

Authentication can be configured using the `@useAuth` decorator on a service namespace, sub-namespace, interface or operation.

The `@useAuth` decorator takes as input the security scheme to apply for all operations contained in the type. If another `@useAuth` was specified on a parent type, the new one will override the value of the parent. [See application hierarchy](#application-hierarchy) for more details.

The input to `@useAuth` can be:

- A single security scheme (see options [here](https://github.com/microsoft/typespec/blob/main/packages/http/lib/auth.tsp)).

  ```typespec
  @useAuth(Auth1)
  ```

- A tuple of security schemes. This creates a security group and means **all** the security schemes in the group **must** be used together to authenticate this service.

  ```typespec
  // Use BOTH Auth1 AND Auth2
  @useAuth([Auth1, Auth2])
  ```

- A union of security schemes. This means **one** of the security schemes **must** be used to authenticate this service.

  ```typespec
  // Use EITHER Auth1 OR Auth2
  @useAuth(Auth1 | Auth2)
  ```

- A union of security schemes and tuples representing security groups. This means **one** of the security groups or security schemes **must** be used to authenticate this service.

  ```typespec
  // Use EITHER (Auth1 AND Auth2) OR Auth3
  @useAuth([Auth1, Auth2] | Auth3)
  ```

## Available security schemes

Security scheme models can be found in the [TypeSpec HTTP library](https://github.com/microsoft/typespec/blob/main/packages/http/lib/auth.tsp)

### Http Auths

These are authentication methods that use the `Authorization` header. They follow the format `Authorization: <auth-scheme> <authorization-parameters>`

- `auth-scheme`: The authentication scheme that defines how the credentials are encoded.
  :::note
  This value is case insensitive ([rfc7235](https://datatracker.ietf.org/doc/html/rfc7235#section-2.1)). Emitters should handle this accordingly.
  :::
- `authorization-parameters`: Scheme-dependent parameters.

TypeSpec HTTP defines 2 commonly used authentication schemes:

- `BasicAuth` (scheme: Basic)
- `BearerAuth` (scheme: Bearer)

#### `BasicAuth`

Basic authentication is a simple authentication scheme built into the HTTP protocol.
The client sends HTTP requests with the Authorization header that contains the word Basic followed by a space and a base64-encoded string in the format `username:password`.
For example, to authorize as demo / p@55w0rd the client would send:

```http
Authorization: Basic ZGVtbzpwQDU1dzByZA==
```

In TypeSpec, you would use:

```typespec
@useAuth(BasicAuth)
```

#### `BearerAuth`

Bearer authentication (also called token authentication) is an HTTP authentication scheme that involves security tokens called bearer tokens.
The name "Bearer authentication" can be understood as "give access to the bearer of this token." The bearer token is a cryptic string, usually generated by the server in response to a login request.
The client must send this token in the Authorization header when making requests to protected resources:

```http
Authorization: Bearer <token>
```

In TypeSpec, you would use:

```typespec
@useAuth(BearerAuth)
```

#### Custom scheme

If your service uses a custom authentication scheme, you can define it as well. For example, if you use a `SharedKey` authentication scheme that would result in the following header:

```http
Authorization: SharedKey <key>
```

you can define it in TypeSpec as follows:

```tsp
model MyCustomAuth {
  type: Http.AuthType.http;
  scheme: "SharedKey";
}
```

### `ApiKeyAuth<TLocation extends ApiKeyLocation, TName extends string>`

An API key is a token that a client provides when making API calls. The key can be sent in different locations:

In the query string:

```
GET /something?api_key=abcdef12345
```

```typespec
@useAuth(ApiKeyAuth<ApiKeyLocation.query, "api_key">)
```

Or as a request header:

```
GET /something HTTP/1.1
X-API-Key: abcdef12345
```

```typespec
@useAuth(ApiKeyAuth<ApiKeyLocation.header, "X-API-KEY">)
```

Or as a cookie:

```
GET /something HTTP/1.1
Cookie: X-API-KEY=abcdef12345
```

```typespec
@useAuth(ApiKeyAuth<ApiKeyLocation.cookie, "X-API-KEY">)
```

### `OAuth2Auth<TFlows extends OAuth2Flow[]>`

OAuth 2.0 is an authorization protocol that gives an API client limited access to user data on a web server.
OAuth relies on authentication scenarios called flows, which allow the resource owner (user) to share protected content from the resource server without sharing their credentials.
For this purpose, an OAuth 2.0 server issues access tokens that client applications can use to access protected resources on behalf of the resource owner.
For more information about OAuth 2.0, see [oauth.net](https://oauth.net) and [RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749).

## Application hierarchy

The `@useAuth` decorator can be used on a service namespace, sub-namespace, interface or operation. The security scheme specified will be applied to all operations contained in the type.
A child type with a `@useAuth` will **override** the security scheme of the parent type. If you want to add a new scheme rather than override, you must re-specify all the parent's security schemes along with the new one.

### Examples

All operations of `MyService` will use `BasicAuth` to authenticate:

```typespec
@useAuth(BasicAuth)
namespace MyService;

op one(): void;
op two(): void;
```

In this example, `one` will use `ApiKey` auth and `two` will use `Basic` auth:

```typespec
@useAuth(BasicAuth)
namespace MyService;

@useAuth(ApiKeyAuth<ApiKeyLocation.query, "api_key">)
op one(): void; // Use ApiKey only
op two(): void; // Use BasicAuth
```

Here, `one` will accept either `ApiKey` or `Basic` auth, while `two` will only accept `Basic` auth:

```typespec
@useAuth(BasicAuth)
namespace MyService;

@useAuth(BasicAuth | ApiKeyAuth<ApiKeyLocation.query, "api_key">)
op one(): void; // Use either BasicAuth OR ApiKey
op two(): void; // Use BasicAuth only
```

## OAuth2 Scopes

The `OAuth2` security scheme can require specific scopes that must be granted to the OAuth2 token to access the operations the security scheme applies to.
When different operations need different scopes, you will likely want to create a template that allows providing OAuth scopes without having to respecify the other properties of the security scheme:

```tsp
@useAuth(MyOAuth2<["read"]>)
namespace DemoService;

alias MyOAuth2<Scopes extends string[]> = OAuth2Auth<
  [
    {
      type: OAuth2FlowType.implicit;
      authorizationUrl: "https://api.example.com/oauth2/authorize";
      refreshUrl: "https://api.example.com/oauth2/refresh";
    }
  ],
  Scopes
>;

// Use OAuth2 with the "read" scope
op list(): string[];

// Use OAuth2 with the "read" scope or no authentication at all
@useAuth(MyOAuth2<["read"]> | NoAuth)
op read(): string;

// Use OAuth2 with the "write" scope
@useAuth(MyOAuth2<["write"]>)
op write(value: string): void;

// Use OAuth2 with the "delete" scope
@useAuth(MyOAuth2<["delete"]>)
op delete(value: string): void;
```

# Content types

Working with HTTP content-types

## Default behavior

By default, if the content-type is not explicitly specified, the HTTP library will use the [`@mediaTypeHint`](../../standard-library/built-in-decorators.md#mediatypehint-mediatypehint) of the body type. For built-in TypeSpec types, the default content-type values are:

- `"application/json"` if the body is a Model or a union that contains `null`.
- `"application/octet-stream"` if the body is `TypeSpec.bytes` or a scalar that extends it (unless that scalar provides its own `@mediaTypeHint`).
- `"text/plain"` if the body is any other scalar type that does not have a `@mediaTypeHint`.

**Examples:**

```typespec
// Returns an application/octet-stream binary body
op download(): bytes;

// Returns a text/plain string
op getContent(): string;

// Returns an application/json body that is either a string or the `null` value
op getContentNullable(): string | null;

// Returns an application/json body with a `name` property.
op getPet(): {
  name: string;
};
```

The same logic applies to requests and response bodies, and it uses the precise type of the body if `@body` or `@bodyRoot` are used.

## Specifying Content-Type

You can specify the content type for an operation by including a header parameter named `contentType`.

### Request Content-Type

```typespec
op uploadImage(@header contentType: "image/png", @body image: bytes): void;
```

### Response Content-Type

```typespec
op downloadImage(): {
  @header contentType: "image/png";
  @body image: bytes;
};
```

### Multiple Content-Type values

If there are multiple content types for the same body, you can specify them as a union of strings.

```typespec
op uploadImage(@header contentType: "image/png" | "image/jpeg", @body image: bytes): void;
```

## Content-Type negotiation

In some cases, the same endpoint might return different content depending on the requested content type. This can be achieved in two ways:

- Using shared routes where different content responses are represented as different operations that share the same endpoint.
- Using overloads where each different content response is an overload.

For example, an API that lets you download an avatar as either `png` or `jpeg` based on the `Accept` header.

### Option 1: Using a shared route

```tsp
model PngImage {
  @header contentType: "image/png";
  @body image: bytes;
}

model JpegImage {
  @header contentType: "image/jpeg";
  @body image: bytes;
}

@route("/avatar")
@sharedRoute
op getAvatarAsPng(@header accept: "image/png"): PngImage;

@route("/avatar")
@sharedRoute
op getAvatarAsJpeg(@header accept: "image/jpeg"): JpegImage;
```

### Option 2: Using overload

```tsp
model PngImage {
  @header contentType: "image/png";
  @body image: bytes;
}

model JpegImage {
  @header contentType: "image/jpeg";
  @body image: bytes;
}

@route("/avatar")
op getAvatar(@header accept: "image/png" | "image/jpeg"): PngImage | JpegImage;

@overload(getAvatar)
op getAvatarAsPng(@header accept: "image/png"): PngImage;

@overload(getAvatar)
op getAvatarAsJpeg(@header accept: "image/jpeg"): JpegImage;
```

## Multipart request

See [the documentation of multipart requests and responses for more information](./multipart.md).

# Encoding of types

How HTTP handles encoding types

This document describe how the http library interpret TypeSpec built-in types and how to configure

## `bytes`

**Default behavior:**

- `bytes` are serialized as `base64` when used in any context that requires they be encoded to a string (such as in a model property that is serialized as JSON, or if transmitted as a string in a `"text/plain"` payload).
- In the context of a binary payload (`"application/octet-stream"`) or an [HTTP File](./operations.md#handling-files), `bytes` are not encoded. They represent the body of the request, response, or multipart field or the file's exact contents.

:::note
This behavior is only a specification and MUST be respected by the emitter. The http library DOES NOT automatically apply the `@encode("base64")` when used inside a JSON model.
:::

Use `@encode` to configure

```tsp
model Pet {
  icon: bytes; // Serialize as base64
  @encode(BytesKnownEncoding.base64url) // Serialize as base64url
  other: bytes;
}

op read(): Pet;

op download(): bytes; // Return application/octet-stream
op upload(@body data: bytes): void; // Accept application/octet-stream
```

## `utcDatetime` and `offsetDateTime`

**Default behavior:**

- Encoded as `rfc7231` when used in a header
- Encoded as `rfc3339` otherwise.

:::note
This behavior is only a specification and MUST be respected by the emitter. The http library DOES NOT automatically apply the `@encode("rfc7231")` on `utcDatetime` and `offsetDateTime` when used in a header.
:::

Use `@encode` to configure.

<table>
<tr><td>TypeSpec</td><td>Example payload</td></tr>
<tr>
<td>

```tsp
model User {
  // Headers
  @header("Created-At") createdAtHeader: utcDateTime;

  @header("Created-At-Rfc3339")
  @encode(DateTimeKnownEncoding.rfc3339)
  createdAtHeaderRfc3339Encoding: utcDateTime;

  // In Json payload
  createdAt: utcDateTime; // rfc3339

  updatedAt: offsetDateTime; // rfc3339

  @encode(DateTimeKnownEncoding.rfc7231)
  createdAtPretty: utcDateTime; // rfc7231

  @encode(DateTimeKnownEncoding.rfc7231)
  updatedAtPretty: offsetDateTime; // rfc7231

  @encode(DateTimeKnownEncoding.unixTimestamp, int32)
  createdAtUnix: utcDateTime; // unixTime in seconds
}
```

</td>
<td>

```yaml
Created-At: Wed, 12 Oct 2022 07:20:50 GMT
Created-At-Rfc3339: 2022-10-12T07:20:50.52Z
```

```json
{
  "createdAt": "2022-10-12T07:20:50.52Z",
  "updatedAt": "2022-10-25T07:20:50.52+07:00",
  "createdAtPretty": "Wed, 12 Oct 2022 07:20:50 GMT",
  "updatedAtPretty": "Tue, 25 Oct 2022 00:20:50 GMT",
  "createdAtUnix": 1493938410
}
```

</td>
</tr>
</table>

## `duration`

**Default behavior:**

- Encoded as `ISO8601`

Use `@encode` to configure.

<table>
<tr><td>TypeSpec</td><td>Example payload</td></tr>
<tr>
<td>

```tsp
model User {
  runtime: duration; // ISO8601

  @encode(DurationKnownEncoding.seconds, int32)
  runtimeInSecondsInt: duration; // in seconds as an int32

  @encode(DurationKnownEncoding.seconds, float32)
  runtimeInSecondsFloat: duration; // in seconds as a float32
}
```

</td>
<td>

```json
{
  "runtime": "PT5M5S",
  "runtimeInSecondsInt": "305",
  "runtimeInSecondsFloat": "305.0"
}
```

</td>
</tr>
</table>

## Numeric types ( `int64`, `decimal128`, `float64`, etc.)

By default numeric types are serialized as a JSON number. However for large types like `int64` or `decimal128` that cannot be represented in certain languages like JavaScript it is recommended to serialize them as string over the wire.

<table>
<tr><td>TypeSpec</td><td>Example payload</td></tr>
<tr>
<td>

```tsp
model User {
  id: int64; // JSON number

  @encode(string)
  idAsString: int64; // JSON string

  viaSalar: decimalString;
}

@encode(string)
scalar decimalString extends decimal128;
```

</td>
<td>

```json
{
  "id": 1234567890123456789012345678901234567890,
  "idAsString": "1234567890123456789012345678901234567890",
  "viaSalar": "1.3"
}
```

</td>
</tr>
</table>

# Examples

Defining HTTP operation examples

This document provides examples specific to the HTTP library in TypeSpec. For general information about how examples work in TypeSpec, see the [examples docs](../../standard-library/examples.md).

## Multiple responses

When defining HTTP operations, you often need to document different possible response types based on status codes. The `@opExample` decorator allows you to provide sample responses for each status code your operation might return.

In the example below, we define an operation that can return three different responses (200 OK, 404 Not Found, and 422 Unprocessable Entity), with examples for each:

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}"
import "@typespec/http";

using Http;

@opExample(#{ returnType: #{ statusCode: 200, name: "Max", age: 3 } })
@opExample(#{ returnType: #{ statusCode: 404, error: "Not found" } })
@opExample(#{ returnType: #{ statusCode: 422, error: "Invalid payload" } })
op read(): {
  @statusCode statusCode: 200;
  name: string;
  age: int32;
} | {
  @statusCode statusCode: 404;
  error: string;
} | {
  @statusCode statusCode: 422;
  error: string;
};
```

Each `@opExample` decorator specifies:

- the status code for this example response.
- the expected values of the response properties.

This helps API consumers understand what to expect from different response scenarios and provides more comprehensive documentation for your API.

# Files

Working with Http.File

## About `Http.File`

`@typespec/http` provides a special model, [`TypeSpec.Http.File`][typespec-http-file], that represents the concept of a file. The HTTP library has special behavior when a request, response, or multipart part body is-or-extends `TypeSpec.Http.File`.

```typespec
using TypeSpec.Http;

op exampleDownload(): File;
```

If `File` were any other ordinary model, the above operation would be interpreted as returning a structured JSON data object that represents the fields of the model. `File`, however, has special semantics. The HTTP library understands that an operation that returns a `File` or any model that extends `File` has the semantics of downloading a file with binary payload and arbitrary content-type from the server. We call these cases "file bodies" to distinguish them from ordinary bodies.

`Http.File` has three properties that are understood to have special meaning when a request, response, or multipart payload has a file body.

- `contents`: the contents of the file, which are the body of the request, response, or multipart payload. This location cannot be changed by subtypes of `Http.File`.
- `contentType`: (optional) the media (MIME) type of the file, which is sent in the `Content-Type` header of the request, response, or multipart payload. This location cannot be changed by subtypes of `Http.File`.
- `filename`: (optional) the name of the file, which is sent in the `filename` parameter of the `Content-Disposition` header of response and multipart payloads. By default, it cannot be sent in requests, as `Content-Disposition` is only valid for response and multipart payloads. This location _can_ be changed by subtypes of `Http.File` that apply HTTP metadata to the location. See [_Overriding the `filename` location_](#overriding-the-filename-location) below for more information.

## Using `Http.File` in operations

An operation payload (request, response, or multipart part) has a file body if:

- The type of the body is _effectively_ a model that is or extends `Http.File` **AND**
- there is no explicit declaration of a `Content-Type` header (see [_`File` with an explicit `Content-Type` header_ below for reasoning and more information](#file-with-an-explicit-content-type-header)).

By "effectively a model that is or extends `Http.File`," we mean cases where an explicit body property is provided and its type is or extends `Http.File` as well as cases where `Http.File` is spread into a request or response payload or `Http.File` is intersected with other models in a request or response and the only non-metadata properties in the payload are properties of `File` (see [_When a model is effectively a `File`_](#when-a-model-is-effectively-a-file) below for a more precise description with examples). The following sections contain examples of using `Http.File` in various contexts to define operations that have file bodies.

### Downloading a file

All of the following TypeSpec operation definitions have file bodies in the response:

```typespec
// The response is _exactly_ a File, so the response has a file body.
op download(): File;

// The response has an explicit body that is a File, so the response has a file body.
op download(): {
  @bodyRoot file: File;
};

// The response is _effectively_ a File (`File` is the only thing spread into it), so the response has a file body.
op download(): {
  ...File;
};

// File is intersected with other models containing only HTTP metadata, so the response has a file body.
op download(): OkResponse & File;

// The response has an explicit body that is _effectively_ a File, so the response has a file body.
op download(): {
  @bodyRoot file: {
    ...File;
  };
};
```

### Uploading a file

All of the following TypeSpec operation definitions have file bodies in the request:

```typespec
// The request has an explicit body that is _exactly_ a File, so the request has a file body.
op upload(@bodyRoot file: File): void;

alias FileRequest = {
  @header("x-request-id") requestId: string;
} & File;

// File is intersected with other models containing only HTTP metadata, so the request has a file body.
op upload(...FileRequest): void;

// The request is _effectively_ a File (`File` is the only thing spread into it), so the request has a file body.
op upload(...File): void;

// The request has an explicit body that is _effectively_ a File, so the request has a file body.
op upload(
  @bodyRoot body: {
    ...File;
  },
): void;
```

### Using files in multipart payloads

Multipart payloads are commonly used to upload files (e.g. in HTML forms). To declare a multipart part that has a file body, ensure the part's type follows the same rules as for request and response payloads: it must either _be_ a type that is effectively an instance of `Http.File`, or must have an explicit body property that _effectively_ is-or-extends `Http.File`. All of the following examples declare multipart parts that have file bodies:

```typespec
// The type of the form-data part is _exactly_ a File, so the part has a file body.
op multipartUpload(
  @multipartBody fields: {
    file: HttpPart<File>;
  },
): void;

// The type of the form-data part has an explicit body that is _exactly_ a File, so the part has a file body.
op multipartUpload(
  @multipartBody fields: {
    file: HttpPart<{
      @bodyRoot file: File;
    }>;
  },
): void;

// The type of the mixed part is _exactly_ a File, so the part has a file body.
op multipartMixedDownload(): {
  @multipartBody data: [HttpPart<File>];
};

// The type of the mixed part has an explicit body that is _exactly_ a File, so the part has a file body.
op multipartMixedDownload(): {
  @multipartBody data: [
    HttpPart<{
      @bodyRoot file: File;
    }>
  ];
};
```

All of the above examples will also have file bodies if `File` is replaced with a model that extends `File` or a model that is _effectively_ `File` (e.g. `{...File}`).

You can also mix and match parts that have file bodies with other parts. The following TypeSpec gives a more comprehensive example of uploading data alongside files:

```typespec
model Widget {
  id: string;
  name: string;
  weight: float64;
}

op multipartUpload(
  @multipartBody fields: {
    // The widget is uploaded in a part named `widget` and uses form-urlencoded serialization.
    widget: HttpPart<{
      @header contentType: "application/x-www-form-urlencoded";
      @body widget: Widget;
    }>;

    // The part named `attachments` can be sent multiple times, and each `attachments` part has a file body.
    attachments: HttpPart<File>[];
  },
): void;
```

For more information about the handling of multipart payloads in `@typespec/http`, see [Multipart](./multipart.md).

### When a model is _effectively_ a `File`

In the above sections, we used the idea of "effective" files. In the context of an HTTP operation, a model is _effectively_ a file if it has _all_ of the properties of `Http.File` (true properties of `Http.File` from a spread or intersection, not just properties that have the same shape as a `File`) **AND** after removing all of the _applicable_ metadata properties, it has _only_ properties of `Http.File`.

- A property of `Http.File` means a property that is actually sourced from the `Http.File` model, e.g. through spreading `File` into another model or using `model is` syntax.
- _Applicable metadata_ means an HTTP metadata decorator that _applies_ in context. For example, `@path` is applicable in requests, but not response or multipart payloads. `@statusCode` is applicable in responses, but not request or multipart payloads.

The following table shows which metadata annotations are applicable in which contexts:

| **Metadata** | **`@header`** | **`@query`** | **`@statusCode`** | **`@path`** |
| ------------ | ------------- | ------------ | ----------------- | ----------- |
| Request      | ✅            | ✅           | ❌                | ✅          |
| Response     | ✅            | ❌           | ✅                | ❌          |
| Multipart    | ✅            | ❌           | ❌                | ❌          |

#### Examples that are effectively a `File`

```typespec
// The parameters of this operation are effectively a file because the @header parameter
// is not considered when checking if the request is a file
op uploadFileWithHeader(@header("x-request-id") requestId: string, ...Http.File): void;

model CommonParameters {
  @query("api-version") apiVersion: string;
  @header("x-request-id") requestId: string;
}

// The parameters of this operation are effectively a file because the common parameters
// are all applicable metadata and not considered when checking if the request is a file
op uploadFileWithCommonParams(...CommonParameters, ...File): void;

// The response has a file body because the `@statusCode` property is not considered when
// checking if the response is a file
op downloadFileWithStatusCode(@path name: string): {
  @statusCode _: 200;
  ...File;
};

// The response has a file body because the `OkResponse` model only has response-applicable
// metadata that is not considered when checking if the response is a file
op downloadFileWithIntersection(@path name: string): OkResponse & File;

model OpenAPIFile extends File<"application/json" | "application/yaml", string> {
  @path filename: string;
}

// The response and request have file bodies because the common parameters are all
// applicable metadata in the request, and the `OkResponse` model only contains
// applicable metadata for the response.
op uploadAndDownload(...CommonParameters, ...OpenAPIFile): OkResponse & OpenAPIFile;

model FileData {
  @header("x-created") created: utcDateTime;
  ...File;
}

// The request has a file body because the `created` header is applicable metadata for
// responses, and the rest of `FileData` is the properties of `File`.
op upload(@bodyRoot file: FileData): OkResponse;

// The response has a file body because the `OkResponse` model only contains applicable
// metadata for the response, and the `created` header is also applicable in the response.
// The properties that are left over are the properties of `File`.
op download(): OkResponse & FileData;
```

#### Examples that are _not_ effectively a `File`

```typespec
// The request does not have a file body because the `userId` parameter is a body property,
// so this will cause the `File` to be serialized as JSON in the request.
op uploadFileWithExtraParam(userId: string, ...File): void;

model FileData {
  @query created: utcDateTime;
  ...File;
}

// The response does not have a file body because `@query` metadata is not applicable
// in responses, so the `created` property is placed in the body and the whole `FileData`
// model is serialized as JSON.
op download(): FileData;

model OpenAPIFile extends File<"application/json" | "application/yaml", string> {
  @path filename: string;
}

model OpenAPIFileResponse {
  @statusCode statusCode: 200;
  ...SpecFile;
}

// The request does not have a file body because the `statusCode` property is not
// applicable metadata for requests, so the request body would be serialized as a JSON
// object. The same model _would_ create a file body in a response, though.
op upload(@bodyRoot data: OpenAPIFileResponse): void;
```

## Creating custom `File` models

You can declare custom types of files by providing arguments to the `Http.File` template or extending it. Custom files can be used to add additional constraints on the contents of files or to override the location metadata of the `filename` property. For example, to declare a file that can contain PNG or JPEG images:

```typespec
alias ImageFile = File<"image/png" | "image/jpeg">;

// or

model ImageFile extends File<"image/png" | "image/jpeg"> {}

// or

model ImageFile extends File {
  contentType: "image/png" | "image/jpeg";
}
```

The above examples are equivalent ways to narrow the allowed media types of the file's contents. For convenience, you can specify the `ContentType` parameter of the `File` template inline, or you can override the type of the property in your own model that extends `File`.

The extra `contentType` information in these custom files provides an extra contractual guarantee about what kinds of data can be inside the file. In the above case, it is guaranteed to be either PNG or JPEG image data. The allowed `Content-Type` header values for the payload are also restricted to only allow those values that satisfy the `contentType` property's type.

**NOTE**: While you can override the type of properties within `Http.File` by extending it, you cannot define _additional_ properties.

### Overriding the `filename` location

By default, the `filename` is located in the `Content-Disposition` header of response and multipart payloads, but that header is not valid for request payloads. If you wish to send the `filename` in a request, you must override the location. For example, the follwing TypeSpec defines an `OpenAPIFile` in which the `filename` is appended to the route path when a file is uploaded, but since `@path` only applies to _requests_, the `filename` will still be returned in the `Content-Dispotion` header in responses or multipart payloads:

```typespec
model OpenAPIFile extends File<"application/json" | "application/yaml"> {
  @path filename: string;
}

@route("/specs")
interface Specs {
  upload(@bodyRoot file: OpenAPIFile): void;

  download(@path name: string): OpenAPIFile;
}
```

**NOTE**: Header metadata is applicable in all contexts, so if you use a custom header (e.g. `@header("x-filename") filename: string`) in your custom file, beware that it will apply to request, response, and multipart payloads equally.

### Textual files

The `File` template accepts a `Contents` argument that may be `TypeSpec.string`, `TypeSpec.bytes`, or any scalar that extends them. If the `Contents` argument is or extends `TypeSpec.string`, the file is considered a _textual_ file. For example:

```typespec
// Since `Contents` is `string`, this file type can only contain text data.
alias TextFile = File<Contents = string>;

// This file type can only contain text and is guaranteed to have `contentType: "application/yaml"`.
model YamlFile extends File<"application/yaml", string> {}

// This file is another way to declare YamlFile by overriding the type of `contentType`
model YamlFile extends File<Contents = string> {
  contentType: "application/yaml";
}
```

Textual files provide an extra contractual guarantee that the contents of the file must be text (i.e. the contents can be represented as a `string`).

**NOTE**: TypeSpec does not prescribe any specific text encoding. Emitters and libraries should take care to honor the `charset` of the file if one is specified, and should assume UTF-8 encoding in the absence of any protocol-level indication of the text encoding on the wire.

## `Http.File` as a structured model

In other cases, when `Http.File` is not _itself_ the body of a request or response, it is treated as a structured model just like any other ordinary model. The TypeSpec HTTP library will generally warn you in cases where the `File` _looks like_ it might indicate a file body, but does not because of the library's rules.

### `File` properties inside other models

If a property of a model is a `File`, and that model is serialized as JSON, the structure of the File will be serialized as JSON inline, with the contents encoded as Base64 data. For example, in the following operation:

```typespec
model Example {
  id: string;
  attachment?: File;
}

op getExample(@path id: string): Example;
```

The response body with the `File` serialized as JSON looks like:

```json
{
  "id": "<string>",
  "attachment": {
    "contentType": "<string?>",
    "filename": "<string?>",
    "contents": "<base64>"
  }
}
```

### `File` inside a union

If `File` is a variant of a union in an exact body, it is _not_ treated as a file body. For example:

```typespec
// Warning: An HTTP File in a union is serialized as a structured model
// instead of being treated as the contents of a file...
op uploadFileOrString(@path id: string, @body data: File | string): void;
```

The above operation accepts _either_ a `text/plain` string _or_ a JSON-serialized `File` object body, not a file body. To declare a single operation that accepts either a `text/plain` string _or_ a file body, declare two separate operations using `@sharedRoute`:

```typespec
@sharedRoute
op uploadFile(@path id: string, @body data: File): void;

@sharedRoute
op uploadString(@path id: string, @body data: string): void;
```

`File` can be in a union in an HTTP response and still create a file body, but only if the union is itself the return type and not in an explicit body property. The HTTP library recognizes the variants of a union that is returned from an operation as individual and separate responses, and it is allowed to have a response type that is a `File` alongside other non-file responses, but if a single response has a type that is a union that contains file, the same warning as above will appear and the `File` will be treated as a structured model:

```typespec
// This is allowed and creates a file body, as `File` and `string` are considered separate responses, so
// this operation has two responses; the first has a file body, and the second has a `text/plain` string body.
op downloadFileOrString(): File | string;

// The following does not create a file body, as it is only one response where the body of that single response
// may be either a file or a string.

// Warning: An HTTP File in a union is serialized as a structured model
// instead of being treated as the contents of a file...
op downloadFileOrString(): {
  @bodyRoot data: File | string;
};
```

### `File` with an explicit `Content-Type` header

Operations are only considered to have file bodies if there is no explicit declaration of a `Content-Type` header in the payload. If an explicit `Content-Type` header is present, the `File` is **always** considered a structured model and is not treated as a file body. The following operation does not have a file body:

```typespec
// Warning: HTTP File body is serialized as a structured model in 'application/json' instead of being
// treated as the contents of a file because an explicit Content-Type header is defined.
op download(): {
  @header contentType: "application/json";
  @body file: File<Contents = string>;
};
```

The explicit `Content-Type` header is not merely metadata. The HTTP library treats this header declaration as a _directive_ about how to serialize the body. In other words, the operation above says "serialize the type of the body as JSON, and the type of the body is `Http.File`." To declare an operation with a file body, where the file can only contain JSON data, provide the `ContentType` argument to the `File` template instead:

```typespec
op download(): File<"application/json", string>;
```

Similarly, and to maintain consistency, you cannot use an explicit `Content-Type` header to declare the content-type of binary files:

```typespec
// Warning: HTTP File body is serialized as a structured model in 'image/png, image/jpeg' instead of being
// treated as the contents of a file because an explicit Content-Type header is defined.
op downloadImage(): {
  @header contentType: "image/png" | "image/jpeg";
  @body file: File;
};

// Do this instead
op downloadImage(): File<"image/png" | "image/jpeg">;
```

## Library and emitter authoring notes

For library/emitter developers working with the `@typespec/http` programmatic API, you can always determine if an operation request, response, or multipart payload is a file body by checking if the `bodyKind` of an `HttpPayloadBody` is `"file"`. If the body kind is `"single"` (or any other kind), then the body _is not_ a file body.

File bodies require special handling to account for the special nature of files. When processing file bodies:

- Assume that the `contents` of the file are _always_ transmitted in the body without any further encoding.
- Assume that the `contentType` of the file _always_ comes from the `Content-Type` header of the corresponding request, response, or multipart payload.
- The `filename` should come from the `Content-Disposition` header of the response or multipart payload (there is no `filename` in requests by default), but be aware that spec authors may override this location using HTTP property metadata decorators like `@query` or `@header`.
- The `isText` field of the `HttpOperationFileBody` will be `true` if the file is contractually guaranteed to only contain text (i.e. if the `contents` property has a type that is or extends `TypeSpec.string`). Textual files are a subset of binary files, with the guarantee that the contents are plain text that can be converted to a `string`. See [_Textual files_](#textual-files) above.

See [the reference documentation of `HttpPayloadBody`](./reference/js-api/type-aliases/HttpPayloadBody.md) and [`HttpOperationFileBody`](./reference/js-api/interfaces/HttpOperationFileBody.md) for more information.

# Multipart requests

Using Http multipart requests

Multipart requests combine one or more sets of data into a single body, separated by boundaries. This is commonly used to upload files.

To define a multipart request in HTTP you must set the contentType header to `"multipart/form-data"` or `multipart/mixed` as described in the [content types doc](./content-types.md#specify-content-type) and add a multipart body property decorated with `@multipartBody`

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}"
import "@typespec/http";

using Http;

op create(
  @header contentType: "multipart/form-data",
  @multipartBody body: {
    username: HttpPart<string>;
    avatar: HttpPart<File>;
  },
): void;
```

Each property of the body represents a part of the multipart request. The name of the property is used as the name of the part. Properties in models are ordered and the order is used to determine the order of the parts in the request.
Each property part must be of type `HttpPart<T>`

The previous example would correspond to the following HTTP request:

```http
POST / HTTP/1.1
Content-Length: 428
Content-Type: multipart/form-data; boundary=abcde12345
--abcde12345
Content-Disposition: form-data; name="username"
Content-Type: text/plain
typespector
--abcde12345
Content-Disposition: form-data; name="avatar"; filename="image1.png"
Content-Type: application/octet-stream
{…file content…}
--abcde12345--
```

## Default handling

By default, the `Content-Type` of individual request parts is set automatically according to the type of the schema properties that describe the request parts:

| Schema Property Type                     | Content-Type               | Example                                                          |
| ---------------------------------------- | -------------------------- | ---------------------------------------------------------------- |
| Primitive                                | `text/plain`               | `HttpPart<string>`<br> `HttpPart<number>`<br>`HttpPart<boolean>` |
| Complex value or array of complex values | `application/json`         | `HttpPart<Address>`<br>`HttpPart<Address[]>`                     |
| `File`, `bytes`                          | `application/octet-stream` | `HttpPart<File>`<br>`HttpPart<bytes>`                            |

See [Content types](./content-types.md) for more information about how the HTTP library handles the Content-Type header.

See [Files](./files.md) for more information about how the HTTP library handles file bodies.

## Part names

There is multiple ways to define a part name. The priority is as follows:

1. Explicit name provied in the `HttpPart` options (e.g. `HttpPart<File, #{ name: "avatar" }>`)
2. Model property name (e.g. `name1: HttpPart<string>;`)

```tsp
// Part name here is name2
op create(
  @header contentType: "multipart/form-data",
  @multipartBody body: {
    name1: HttpPart<string, #{ name: "name2" }>;
  },
): void;
```

### Unamed parts

When using `multipart/mixed` parts are not required to be named. Instead of passing a model as the multipart body you can pass a tuple with each part

```tsp
model Address {
  street: string;
  city: string;
}
op create(
  @header contentType: "multipart/mixed",
  @multipartBody body: [
    HttpPart<string>,
    HttpPart<File, #{ name: "avatar" }>,  // An name can also be provided this way
    HttpPart<Address>,
    HttpPart<File>[]
  ],
): void;
```

## `HttpPart<Foo>[]` vs `HttpPart<Foo[]>`

- `HttpPart<Foo>[]` Represent multiple parts of type `Foo`
- `HttpPart<Foo[]>` Represent a single part of type `Foo[]`

## Examples

```tsp
// Upload a single file
op create(
  @header contentType: "multipart/form-data",
  @multipartBody body: {
    avatar: HttpPart<File>;
  },
): void;

// Upload multiple files
op create(
  @header contentType: "multipart/form-data",
  @multipartBody body: {
    avatar: HttpPart<File>;
    banner: HttpPart<File>;
  },
): void;

// Upload many files
op create(
  @header contentType: "multipart/form-data",
  @multipartBody body: {
    images: HttpPart<File>[];
  },
): void;

// Upload 2 form fields
op create(
  @header contentType: "multipart/form-data",
  @multipartBody body: {
    firstName: HttpPart<string>;
    lastName: HttpPart<string>;
  },
): void;

// Send a json field
model Address {
  street: string;
  city: string;
}
op create(
  @header contentType: "multipart/form-data",
  @multipartBody body: {
    address: HttpPart<Address>;
  },
): void;

// Send multiple fields - In this scenario each address is sent as an individual part
model Address {
  street: string;
  city: string;
}
op create(
  @header contentType: "multipart/form-data",
  @multipartBody body: {
    addresses: HttpPart<Address>[];
  },
): void;
```

## Custom content type

The first template parameter given to `HttpPart` follow the same logic as a property annotated with `@bodyRoot`. This means you can include headers, implicit body properties or an explicit body inside.

```tsp title=main.tsp tryit="{"emit": ["@typespec/openapi3"]}"
import "@typespec/http";

using Http;

model Png extends File {
  @header contentType: "image/png";
}
op create(
  @header contentType: "multipart/form-data",
  @multipartBody body: {
    avatar: HttpPart<Png>;
    data: HttpPart<{
      name: string;
      @header contentType: "application/xml";
    }>;
  },
): void;
```

# Operations

Defining HTTP endpoints

## Operation verb

**Default behavior:**

- If `@post` operation has a request body
- `@get` otherwise

**Configure:**

You can use one of the [verb decorators](./reference/decorators.md): `@get`, `@put`, etc.

## Route

An operation route can be specified using the `@route` decorator.

```typespec
@route("/pets") op list(): Pet[];
```

Route path parameters are declared using `{}`. Providing `@path` on the model property with the matching name is optional.

```typespec
@route("/pets/{petId}") op get(petId: string): Pet;
// or explicit @path
@route("/pets/{petId}") op get(@path petId: string): Pet;
```

Route can be specified on a parent namespace or interface. In that case all the operations, interfaces and namespaces underneath will be prefixed with it.

```typespec
@route("/store")
namespace PetStore {
  op hello(): void; // `/store`
  @route("ping") op ping(): void; // `/store/ping`

  @route("/pets")
  interface Pets {
    list(): Pet[]; // `/store/pets`
    @route("{petId}") read(petId: string): Pet; // `/store/pets/{petId}`
  }
}
```

## Path and query parameters

Model properties and parameters which should be passed as path and query parameters use the `@path` and `@query` parameters respectively. Let's modify our list operation to support pagination, and add a read operation to our Pets resource:

```typespec
@route("/pets")
namespace Pets {
  op list(@query skip: int32, @query top: int32): Pet[];
  op read(@path petId: int32): Pet;
}
```

Path parameters are appended to the URL unless a substitution with that parameter name exists on the resource path. For example, we might define a sub-resource using the following TypeSpec. Note how the path parameter for our sub-resource's list operation corresponds to the substitution in the URL.

```typespec
@route("/pets/{petId}/toys")
namespace PetToys {
  op list(@path petId: int32): Toy[];
}
```

## Request & response bodies

Request and response bodies can be declared explicitly using the `@body` decorator. Let's add an endpoint to create a pet. Let's also use this decorator for the responses, although this doesn't change anything about the API.

```typespec
@route("/pets")
namespace Pets {
  op list(@query skip: int32, @query top: int32): {
    @body pets: Pet[];
  };
  op read(@path petId: int32): {
    @body pet: Pet;
  };
  @post
  op create(@body pet: Pet): {};
}
```

### Implicit body resolution

Note that in the absence of explicit `@body`:

1. The set of parameters that are not marked @header, @query, or @path form the request body.
2. The set of properties of the return model that are not marked @header or @statusCode form the response body.
3. If the return type is not a model, then it defines the response body.

This is how we were able to return Pet and Pet[] bodies without using @body for list and read. We can actually write
create in the same terse style by spreading the Pet object into the parameter list like this:

See also [metadata](./operations.md#metadata) for more advanced details.

```typespec
@route("/pets")
namespace Pets {
  @post
  op create(...Pet): {};
}
```

### `@body` vs `@bodyRoot`

The `@body` decorator applies to a request parameter or model property. The type of that decorated property or parameter will be exactly the http request or response body. If the body type is a Model, annotating any property in that model with applicable metadata (`@header`, `@path`, `@query` for request and `@header`, `@statusCode` for response) will be ignored and log a warning.
The `@bodyRoot` decorator similarly applies to a property or parameter. The type of that decorated property or parameter is similarly used to define the request or response body. If the body type is not a model, the behavior is identical to `@body`. If the body type is a model, instead of exactly defining _only_ the body, the model may also contain properties annotated as applicable http metadata. Such properties will be treated as http metadata, will not be included in the request or response body, and will not result in a warning.

Nesting `@body` and `@bodyRoot`, while mostly pointless, can happen when using templates to build operations. A warning will be emitted if nesting happens inline.
The meaning when nesting them is as follow:

- As soon as `@body` is reached the content is exactly the body which means any nested `@bodyRoot` or `@body` will be ignored.
- if `@bodyRoot` is reached before any occurrence of `@body`, it will keep looking for nested properties decorated with `@body` or `@bodyRoot` and if found the deepest one will be used to determine the body.

Examples

<table>
<tr>
  <th>Code</th>
  <th>Example Payload</th>
</tr>
<tr>
  <td>

```typespec
op case1(
  @header foo: string, //
  name: string,
  age: int32,
): void;
```

  </td>
  <td>

```http
POST /
Foo: bar
{
  "name": "Rex",
  "age": 3
}
```

  </td>
```
  </td>
</tr>
<tr>
  <td>

```typespec
op case2(
  body: {
    @header foo: string;
    name: string;
    age: int32;
  },
): void;
```

  </td>
  <td>

```http
POST /
Foo: bar
{
  "body": {
    "name": "Rex",
    "age": 3
  }
}
```

  </td>
</tr>
<tr>
  <td>

```typespec
op case3(
  @body body: {
    @header foo: string; // warning: `@header` is ignored
    name: string;
    age: int32;
  },
): void;
```

  </td>
  <td>

```http
POST /
{
  "name": "Rex",
  "age": 3
}
```

  </td>
</tr>
<tr>
  <td>

```typespec
op case4(
  @bodyRoot body: {
    @header foo: string;
    name: string;
    age: int32;
  },
): void;
```

  </td>
  <td>

```http
POST /
Foo: bar
{
  "name": "Rex",
  "age": 3
}
```

  </td>
</tr>
<tr>
  <td>

```typespec
op case5(
  // This bodyRoot is a noop and will log a warning
  @bodyRoot body: {
    @bodyRoot reallyBody: {
      @header foo: string;
      name: string;
      age: int32;
    };
  },
): void;
```

  </td>
  <td>

```http
POST /
Foo: bar
{
  "name": "Rex",
  "age": 3
}
```

  </td>
</tr>
</table>

## Headers

Model properties and parameters that should be passed in a header use the `@header` decorator. The decorator takes the header name as a parameter. If a header name is not provided, it is inferred from the property or parameter name. Let's add `etag` support to our pet store's read operation.

```typespec
@route("/pets")
namespace Pets {
  op list(@query skip: int32, @query top: int32): {
    @body pets: Pet[];
  };
  op read(@path petId: int32, @header ifMatch?: string): {
    @header eTag: string;
    @body pet: Pet;
  };
  @post
  op create(@body pet: Pet): {};
}
```

## Status codes

**Default behavior:**

- `4xx,5xx` if response is marked with `@error`
- `200` otherwise

**Configure:**

Use the `@statusCode` decorator on a property to declare a status code for a response. Generally, setting this to just `int32` isn't particularly useful. Instead, use number literal types to create a discriminated union of response types. Let's add status codes to our responses, and add a 404 response to our read endpoint.

```typespec
@route("/pets")
namespace Pets {
  @error
  model Error {
    code: string;
  }

  op list(@query skip: int32, @query top: int32): {
    @body pets: Pet[]; // statusCode: 200 Implicit
  };
  op read(@path petId: int32, @header ifMatch?: string): {
    @statusCode statusCode: 200;
    @header eTag: string;
    @body pet: Pet;
  } | {
    @statusCode statusCode: 404;
  };
  op create(@body pet: Pet): {
    @statusCode statusCode: 204;
  } | Error; //statusCode: 4xx,5xx as Error use `@error` decorator
}
```

## Content type

[See the documentation of Content-Types](./content-types.md).

## Built-in response shapes

Since status codes are so common for REST APIs, TypeSpec comes with some built-in types for common status codes so you don't need to declare status codes so frequently.

There is also a `Body<T>` type, which can be used as a shorthand for { @body body: T } when an explicit body is required.

Lets update our sample one last time to use these built-in types:

```typespec
model ETag {
  @header eTag: string;
}
@route("/pets")
namespace Pets {
  op list(@query skip: int32, @query top: int32): OkResponse & Body<Pet[]>;
  op read(@path petId: int32, @header ifMatch?: string): (OkResponse &
    Body<Pet> &
    ETag) | NotFoundResponse;
  @post
  op create(...Pet): NoContentResponse;
}
```

Note that the default status code is 200 for non-empty bodies and 204 for empty bodies. Similarly, explicit `Body<T>` is not required when T is known to be a model. So the following terser form is equivalent:

```typespec
@route("/pets")
namespace Pets {
  op list(@query skip: int32, @query top: int32): Pet[];
  op read(@path petId: int32, @header ifMatch?: string): (Pet & ETag) | NotFoundResponse;
  @post
  op create(...Pet): {};
}
```

Finally, another common style is to make helper response types that are
shared across a larger service definition. In this style, you can be
entirely explicit while also keeping operation definitions concise.

For example, we could write :

```typespec
model ListResponse<T> {
  ...OkResponse;
  ...Body<T[]>;
}

model ReadSuccessResponse<T> {
  ...OkResponse;
  ...ETag;
  ...Body<T>;
}

alias ReadResponse<T> = ReadSuccessResponse<T> | NotFoundResponse;

model CreateResponse {
  ...NoContentResponse;
}

@route("/pets")
namespace Pets {
  op list(@query skip: int32, @query top: int32): ListResponse<Pet>;
  op read(@path petId: int32, @header ifMatch?: string): ReadResponse<Pet>;
  @post
  op create(...Pet): CreateResponse;
}
```

## Handling files

`@typespec/http` provides a special model [`TypeSpec.Http.File`](../http/reference/data-types.md#file-typespechttpfile) for handling file uploads and downloads in HTTP operations. When working with files, emitters need to implement special handling due to their binary nature.

For more information about HTTP file bodies and how to configure them, see [the documentation on Files][http-files].

[http-files][./files.md]

### Basic File Handling

When the model `Http.File` (or any model that extends `Http.File`) is the _exact_ body of an HTTP request, emitters **must** treat this model with special care:

- The `contentType` property should be used as the value for the `Content-Type` header in requests and vice-versa for responses.
- The `filename` property should be used in the `Content-Disposition` header in responses and vice-versa for multipart requests (`filename` cannot be sent in a non-multipart HTTP request because `Content-Disposition` is only valid for responses and multipart requests).
- The file content should be treated as the raw body of the request/response without any additional parsing.

See [`isHttpFile`](../http/reference/js-api/functions/isHttpFile.md) for a helper that emitters/libraries can use to detect instances of `Http.File`.

### Examples

#### Uploading and downloading files

```typespec
// Uploading and downloading
@route("/files")
interface Files {
  @post
  upload(@body file: Http.File): {
    @statusCode statusCode: 201;
  };

  download(@path fileId: string): Http.File;
}
```

#### Custom file types

If you want to declare specific types of files that are accepted, but still treated as binary files, declare the content types by extending the `Http.File` model and overriding the `contentType` field.

```typespec
// Custom file type for images
model ImageFile extends Http.File {
  contentType: "image/jpeg" | "image/png" | "image/gif";
}

@route("/images")
interface Images {
  @post
  upload(@body image: ImageFile): {
    @statusCode statusCode: 201;
  };

  download(@path imageId: string): ImageFile;
}
```

## Automatic visibility

The `@typespec/rest` library understands [Lifecycle Visibility](../../language-basics/visibility.md#lifecycle-visibility) and provides functionality for emitters to apply visibility transforms based on whether a model represents a request or response and on HTTP method usage as detailed in the table below.

See [handling visibility and metadata](../../extending-typespec/emitter-metadata-handling.md) for details on how to incorporate this information into an emitter implementation.

| Modifier         | Visible in           |
| ---------------- | -------------------- |
| Lifecycle.Read   | Any response         |
| Lifecycle.Query  | GET or HEAD request  |
| Lifecycle.Create | POST or PUT request  |
| Lifecycle.Update | PATCH or PUT request |
| Lifecycle.Delete | DELETE request       |

This allows a single logical TypeSpec model to be used as in the following example:

```typespec
model User {
  name: string;
  @visibility(Lifecycle.Read) id: string;
  @visibility(Lifecycle.Create) password: string;
}

@route("/users")
interface Users {
  @post create(@path id: string, ...User): User;
  @get get(@path id: string): User;
}
```

There is a single logical user entity represented by the single TypeSpec type `User`, but the HTTP payload for this entity varies based on context. When returned in a response, the `id` property is included, but when sent in a request, it is not. Similarly, the `password` property is only included in create requests, but not present in responses.

The OpenAPI v3 emitter will apply these visibilities automatically, without explicit use of `@withVisibility`, and it will generate separate schemas suffixed by visibility when necessary. `@visibility(Lifecycle.Read)` can be expressed in OpenAPI without generating additional schema by specifying `readOnly: true` and the OpenAPI v3 emitter will leverage this a an optimization, but other visibilities will generate additional schemas. For example, `@visibility(Lifecycle.Create)` applied to a model property of a type named Widget will generate a `WidgetCreate` schema.

Another emitter such as one generating client code can see and preserve a single logical type and deal with these HTTP payload differences by means other than type proliferation.

Modeling with logical entities rather than HTTP-specific shapes also keeps the TypeSpec spec decoupled from HTTP and REST and can allow the same spec to be used with multiple protocols.

## Metadata

The properties that designate content for the HTTP envelope (`@header`, `@path`, `@query`, `@statusCode`) rather than the content in an HTTP payload are often called "metadata".

Metadata is determined to be applicable or inapplicable based on the context that it is used:

| Context       | Applicability       |
| ------------- | ------------------- |
| `@query`      | request only        |
| `@path`       | request only        |
| `@statusCode` | response only       |
| `@header`     | request or response |

Additionally metadata that appears in an array element type always inapplicable.

When metadata is deemed "inapplicable", for example, if a `@path` property is seen in a response, it becomes part of the payload instead unless the [@includeInapplicableMetadataInPayload](./reference/decorators.md#@TypeSpec.Http.includeInapplicableMetadataInPayload) decorator is used and given a value of `false`.

The handling of metadata applicability furthers the goal of keeping a single logical model in TypeSpec. For example, this defines a logical `User` entity that has a name, ID and password, but further annotates that the ID is sent in the HTTP path and the HTTP body in responses. Also, using automatic visibility as before, we further indicate that the password is only present in create requests.

```typespec
model User {
  name: string;
  @path id: string;
  @visibility(Lifecycle.Create) password: string;
}
```

Then, we can write operations in terms of the logical entity:

```typespec
@route("/users")
interface Users {
  @post create(...User): User;
}
```

Abstractly, this expresses that a create operation that takes and returns a user. But concretely, at the HTTP protocol level, a create request and response look like this:

```
POST /Users/TypeSpecFan42 HTTP/1.1
Content-Type: application/json
{
  "name": "TypeSpec Fan",
  "password": "Y0uW1llN3v3rGu3ss!"
}

HTTP/1.1 200 OK
Content-Type: application/json
{
  name: "TypeSpec Fan",
  id: "TypeSpecFan42
}
```

### Visibility vs. Metadata applicability

Metadata properties are filtered based on visibility as [described above](#automatic-visibility). This is done independently before applicability is considered. If a a metadata property is not visible then it is neither part of the envelope nor the HTTP payload, irrespective of its applicability.

### Nested metadata

Metadata properties are not required to be top-level. They can also be nested deeper in a parameter or response model type. For example:

```typespec
model Thing {
  headers: {
    @header example: string;
  };
  name: string;
}
```

Note that nesting in this sense does not require the use of anonymous models. This is equivalent:

```typespec
model Thing {
  headers: Headers;
  name: string;
}
model Headers {
  @header example: string;
}
```

In the event that this nesting introduces duplication, then the least nested property with a given name is preferred and the duplicate metadata properties are ignored.

```typespec
model Thing {
  headers: {
    @header example: string; // preferred
    more: {
      @header example: string; // ignored
    };
  };
}
```

## JSON Merge-Patch

[RFC 7396](https://www.rfc-editor.org/rfc/rfc7396) describes a standard for interpreting
a Patch request body using content-type `application/merge-patch+json`to update an existing
resource. The TypeSpec Http library provides Model templates `MergePatchUpdate` and
`MergePatchCreateOrUpdate` for specifying a JSON merge-patch request body. The templates
recursively apply the merge-patch transformation rules to a TypeSpec resource Model, taking
into account the structure and characteristics of the resource Model.

For example, given a resource model like this:

```tsp
model Resource {
  id: string;
  name?: string;
  quantity?: safeint;
  color: "blue" | "green" | "red" = "blue";
  flavor?: "vanilla" | "chocolate" | "strawberry" = "vanilla";
  related?: Record<Resource>;
  tags?: string[];
}
```

A JSON Merge-Patch request updating this resource would have the following behavior:

- `id` may or may not occur in the request, if it does occur, the resource value can be updated to a new string, but cannot be erased by sending null.
- `name` may or may not occur in the request, if it does occur, the resource value can be updated to a new string or erased by sending null.
- `quantity` may or ay not occur in the request, if it does occur, the resource value can be updated to a new integer value or erased by sending null.
- `color` may or may not occur in the request, if it does occur, the resource value can be updated to one of the appropriate values. If set to `null` it is returned to its default value (`blue`)
- `flavor` may or may not occur in the request, if it does occur, the resource value can be updated to one of the appropriate values. If set to `null` it is returned to its default value (`vanilla`)
- `related` may or may not occur in the request, if it does occur, the resource value can be updated or erased (set to `{}`) by sending null.
  - Since `related` is a keyed type (Object), each key/value pair in the request will be treated as follows:
  - If the key exists in the 'related' field of the resource, the value is merged with the existing value.
  - If the key does not exist in the 'related' field of the resource, the key/value pair is added.
- `tags` may or may not occur in the request, if it does occur, the resource can be replaced by a new array, or erased by sending null.

### The MergePatch Transform

Generalizing these rules creates a type transform of the resource Model into a Model defining the corresponding Patch request body. The properties of a resource define the allowed properties and their types in a Patch request body for that resource as follows:

- The `type` of a property indicates the allowed type of the corresponding property in a Patch request.
- `Required` properties without a default value are _optional_ in a Patch request, but if present, the value cannot be null.
- `Optional` properties are _optional_ in a Patch request, and, if present, can contain any valid value or null.
- Properties with a default value are _optional_ in a Patch request, but have no default value in the request body. If present, they can contain any valid value or null. A _null_ value will not erase the property, but set it back to its default value.
- `Model` and `Record` typed properties, when present in a Patch request are merged with the existing resource value in accordance with the merge-patch algorithm: this transformation is recursively applied to these values.
- `Array` typed properties, when present in a Patch request replace the existing resource value in accordance with the merge-patch algorithm. This transformation is _not_ recursively applied to these values.
- Properties required to deserialize a request (for example, discriminators) are _required_ in a Patch request body.

### Constraints

Because JSON merge-patch only describes the request body of an http request, the merge-patch
transform in TypeSpec does not allow http envelope property metadata like `@query`, `@path`,
`@header`, `@cookie`, and `@statusCode` in http requests.

The merge-patch templates will **emit an error diagnostic** if a model containing Http metadata
properties is passed in. For example:

```tsp
model ResourceWithMetadata {
  @path id: string;
  @header eTag: string;
  description: string;
}

// THIS WILL RESULT IN AN ERROR
@patch op update(...MergePatchUpdate<ResourceWithMetadata>): ResourceWithMetadata;
```

### Patch Behavior of Nested Models

Model types may be nested beneath the top level of a resource. The characteristics of the ModelProperty that references a nested Model type determines the valid values for that nested model in the Patch request. Here is how the valid values are determined for each of the model property types that might reference a nested model (also depicted in the following tables):

- The property type is a (simple) Model or an intersection of models
  - if the property is optional, the MergePatch transform applies, and the visibility is `CreateOrUpdate`. This is because, in an update, the property _may or may not_ exist if the resource exists, so might need to be created or updated.
  - if the property is required, the MergePatch transform applies and the visibility matches the input visibility. This is because, in an update, the property _must_ exist if the resource exists, so it can only be updated. In a CreateOrUpdate, it could also be created with the resource.
- The property type is an array (sequence) of model type items
  - For required or optional arrays: The MergePatch transform _does not apply_ and the visibility is `Create`
- The property type is a Record (keyed collection) of model type values
  - For required or optional keyed collections, the MergePatch transform applies, and the visibility is create or update.
- The property type is a union of model type values
  - The MergePatch transform applies to each of the union variants, and because switching between variants is possible, CreateOrUpdate visibility is applied regardless of the optionality of the property. If the union is discriminated, the discriminator remains 'required' so the service can understand which variant the request was intended to apply to.

### Treatment of Nested Keyed Types in Patch Request with `Update` Visibility Filter

| Property Type | Optionality | Example                      | Apply MergePatch transform? | Visibility Filter |
| ------------- | ----------- | ---------------------------- | --------------------------- | ----------------- |
| Simple        | Required    | `fooProp: Foo`               | Yes                         | `Update`          |
| Simple        | Optional    | `fooProp?: Foo`              | Yes                         | `CreateOrUpdate`  |
| ReplaceOnly   | Required    | `@replaceOnly fooProp: Foo`  | No                          | `Create`          |
| ReplaceOnly   | Optional    | `@replaceOnly fooProp?: Foo` | No                          | `Create`          |
| Array         | \*          | `fooProp?: Foo[]`            | No                          | `Create`          |
| Record        | \*          | `fooProp?: Record<Foo>`      | Yes                         | `CreateOrUpdate`  |
| Union         | \*          | `fooProp?: Foo \| Bar`       | Yes                         | `CreateOrUpdate`  |

### Treatment of Nested Keyed Types in Patch Request with `CreateOrUpdate` Visibility Filter

| Property Type | Optionality | Example                      | Apply MergePatch transform? | Visibility Filter |
| ------------- | ----------- | ---------------------------- | --------------------------- | ----------------- |
| Simple        | Required    | `fooProp: Foo`               | Yes                         | `CreateOrUpdate`  |
| Simple        | Optional    | `fooProp?: Foo`              | Yes                         | `CreateOrUpdate`  |
| ReplaceOnly   | Required    | `@replaceOnly fooProp: Foo`  | No                          | `Create`          |
| ReplaceOnly   | Optional    | `@replaceOnly fooProp?: Foo` | No                          | `Create`          |
| Array         | \*          | `fooProp?: Foo[]`            | No                          | `Create`          |
| Record        | \*          | `fooProp?: Record<Foo>`      | Yes                         | `CreateOrUpdate`  |
| Union         | \*          | `fooProp?: Foo \| Bar`       | Yes                         | `CreateOrUpdate`  |

### Examples

#### Update

A JSON Merge Patch update operation for a Widget resource using `@body`.

```tsp
// A Json merge-patch operation to update a 'Widget' resource
// and return the updated Widget.
@patch op update(@body request: MergePatchUpdate<Widget>): Widget;
```

A JSON Merge Patch update operation for a Widget resource using the spread operator.

```tsp
// A Json merge-patch operation to update a 'Widget' resource
// and return the updated Widget.
@patch op update(...MergePatchUpdate<Widget>): Widget;
```

#### Create or Update

A JSON Merge Patch create or update operation for a Widget resource using `@body`.

```tsp
// A Json merge-patch operation to update a 'Widget' resource
// or create it if it does not exist and return the updated Widget.
@patch op update(@body request: MergePatchCreateOrUpdate<Widget>): Widget;
```

A JSON Merge Patch create or update operation for a Widget resource using the spread operator.

```tsp
// A Json merge-patch operation to update a 'Widget' resource
// or create it if it does not exist and return the updated Widget.
@patch op update(...MergePatchCreateOrUpdate<Widget>): Widget;
```

## Emitter resources

See [Handling metadata and visibility in emitters for REST API](../../extending-typespec/emitter-metadata-handling.md) for information on how to handle metadata applicability and automatic visibility in a custom emitter.

# Data types

Data types exported by @typespec/http

## TypeSpec.Http

### `AcceptedResponse` {#TypeSpec.Http.AcceptedResponse}

The request has been accepted for processing, but processing has not yet completed.

```typespec
model TypeSpec.Http.AcceptedResponse
```

#### Properties

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| statusCode | `202` | The status code. |

### `ApiKeyAuth` {#TypeSpec.Http.ApiKeyAuth}

An API key is a token that a client provides when making API calls. The key can be sent in the query string:

```
GET /something?api_key=abcdef12345
```

or as a request header

```
GET /something HTTP/1.1
X-API-Key: abcdef12345
```

or as a cookie

```
GET /something HTTP/1.1
Cookie: X-API-KEY=abcdef12345
```

```typespec
model TypeSpec.Http.ApiKeyAuth<Location, Name>
```

#### Template Parameters

| Name     | Description                 |
| -------- | --------------------------- |
| Location | The location of the API key |
| Name     | The name of the API key     |

#### Properties

| Name | Type                            | Description |
| ---- | ------------------------------- | ----------- |
| type | `TypeSpec.Http.AuthType.apiKey` |             |
| in   | `Location`                      |             |
| name | `Name`                          |             |

### `AuthorizationCodeFlow` {#TypeSpec.Http.AuthorizationCodeFlow}

Authorization Code flow

```typespec
model TypeSpec.Http.AuthorizationCodeFlow
```

#### Properties

| Name             | Type                                             | Description                       |
| ---------------- | ------------------------------------------------ | --------------------------------- |
| type             | `TypeSpec.Http.OAuth2FlowType.authorizationCode` | authorization code flow           |
| authorizationUrl | `string`                                         | the authorization URL             |
| tokenUrl         | `string`                                         | the token URL                     |
| refreshUrl?      | `string`                                         | the refresh URL                   |
| scopes?          | `string[]`                                       | list of scopes for the credential |

### `BadRequestResponse` {#TypeSpec.Http.BadRequestResponse}

The server could not understand the request due to invalid syntax.

```typespec
model TypeSpec.Http.BadRequestResponse
```

#### Properties

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| statusCode | `400` | The status code. |

### `BasicAuth` {#TypeSpec.Http.BasicAuth}

Basic authentication is a simple authentication scheme built into the HTTP protocol.
The client sends HTTP requests with the Authorization header that contains the word Basic word followed by a space and a base64-encoded string username:password.
For example, to authorize as demo / `p@55w0rd` the client would send

```
Authorization: Basic ZGVtbzpwQDU1dzByZA==
```

```typespec
model TypeSpec.Http.BasicAuth
```

#### Properties

| Name   | Type                          | Description         |
| ------ | ----------------------------- | ------------------- |
| type   | `TypeSpec.Http.AuthType.http` | Http authentication |
| scheme | `"Basic"`                     | basic auth scheme   |

### `BearerAuth` {#TypeSpec.Http.BearerAuth}

Bearer authentication (also called token authentication) is an HTTP authentication scheme that involves security tokens called bearer tokens.
The name “Bearer authentication” can be understood as “give access to the bearer of this token.” The bearer token is a cryptic string, usually generated by the server in response to a login request.
The client must send this token in the Authorization header when making requests to protected resources:

```
Authorization: Bearer <token>
```

```typespec
model TypeSpec.Http.BearerAuth
```

#### Properties

| Name   | Type                          | Description         |
| ------ | ----------------------------- | ------------------- |
| type   | `TypeSpec.Http.AuthType.http` | Http authentication |
| scheme | `"Bearer"`                    | bearer auth scheme  |

### `Body` {#TypeSpec.Http.Body}

Defines a model with a single property of the given type, marked with `@body`.

This can be useful in situations where you cannot use a bare type as the body
and it is awkward to add a property.

```typespec
model TypeSpec.Http.Body<Type>
```

#### Template Parameters

| Name | Description                              |
| ---- | ---------------------------------------- |
| Type | The type of the model's `body` property. |

#### Properties

| Name | Type   | Description |
| ---- | ------ | ----------- |
| body | `Type` |             |

### `ClientCredentialsFlow` {#TypeSpec.Http.ClientCredentialsFlow}

Client credentials flow

```typespec
model TypeSpec.Http.ClientCredentialsFlow
```

#### Properties

| Name        | Type                                             | Description                       |
| ----------- | ------------------------------------------------ | --------------------------------- |
| type        | `TypeSpec.Http.OAuth2FlowType.clientCredentials` | client credential flow            |
| tokenUrl    | `string`                                         | the token URL                     |
| refreshUrl? | `string`                                         | the refresh URL                   |
| scopes?     | `string[]`                                       | list of scopes for the credential |

### `ConflictResponse` {#TypeSpec.Http.ConflictResponse}

The request conflicts with the current state of the server.

```typespec
model TypeSpec.Http.ConflictResponse
```

#### Properties

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| statusCode | `409` | The status code. |

### `CookieOptions` {#TypeSpec.Http.CookieOptions}

Cookie Options.

```typespec
model TypeSpec.Http.CookieOptions
```

#### Properties

| Name  | Type     | Description         |
| ----- | -------- | ------------------- |
| name? | `string` | Name in the cookie. |

### `CreatedResponse` {#TypeSpec.Http.CreatedResponse}

The request has succeeded and a new resource has been created as a result.

```typespec
model TypeSpec.Http.CreatedResponse
```

#### Properties

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| statusCode | `201` | The status code. |

### `File` {#TypeSpec.Http.File}

A file in an HTTP request, response, or multipart payload.

Files have a special meaning that the HTTP library understands. When the body of an HTTP request, response,
or multipart payload is _effectively_ an instance of `TypeSpec.Http.File` or any type that extends it, the
operation is treated as a file upload or download.

When using file bodies, the fields of the file model are defined to come from particular locations by default:

- `contentType`: The `Content-Type` header of the request, response, or multipart payload (CANNOT be overridden or changed).
- `contents`: The body of the request, response, or multipart payload (CANNOT be overridden or changed).
- `filename`: The `filename` parameter value of the `Content-Disposition` header of the response or multipart payload
  (MAY be overridden or changed).

A File may be used as a normal structured JSON object in a request or response, if the request specifies an explicit
`Content-Type` header. In this case, the entire File model is serialized as if it were any other model. In a JSON payload,
it will have a structure like:

```
{
  "contentType": <string?>,
  "filename": <string?>,
  "contents": <string, base64>
}
```

The `contentType` _within_ the file defines what media types the data inside the file can be, but if the specification
defines a `Content-Type` for the payload as HTTP metadata, that `Content-Type` metadata defines _how the file is
serialized_. See the examples below for more information.

NOTE: The `filename` and `contentType` fields are optional. Furthermore, the default location of `filename`
(`Content-Disposition: <disposition>; filename=<filename>`) is only valid in HTTP responses and multipart payloads. If
you wish to send the `filename` in a request, you must use HTTP metadata decorators to describe the location of the
`filename` field. You can combine the metadata decorators with `@visibility` to control when the `filename` location
is overridden, as shown in the examples below.

```typespec
model TypeSpec.Http.File<ContentType, Contents>
```

#### Template Parameters

| Name        | Description                                                                                    |
| ----------- | ---------------------------------------------------------------------------------------------- |
| ContentType | The allowed media (MIME) types of the file contents.                                           |
| Contents    | The type of the file contents. This can be `string`, `bytes`, or any scalar that extends them. |

#### Examples

```tsp
// Download a file
@get op download(): File;

// Upload a file
@post op upload(@bodyRoot file: File): void;
```

```tsp
// Upload and download files in a multipart payload
op multipartFormDataUpload(
  @multipartBody fields: {
    files: HttpPart<File>[];
  },
): void;

op multipartFormDataDownload(): {
  @multipartBody formFields: {
    files: HttpPart<File>[];
  };
};
```

```tsp
// Declare a custom type of text file, where the filename goes in the path
// in requests.
model SpecFile extends File<"application/json" | "application/yaml", string> {
  // Provide a header that contains the name of the file when created or updated
  @header("x-filename")
  @path
  filename: string;
}

@get op downloadSpec(@path name: string): SpecFile;

@post op uploadSpec(@bodyRoot spec: SpecFile): void;
```

```tsp
// Declare a custom type of binary file
model ImageFile extends File {
  contentType: "image/png" | "image/jpeg";
  @path filename: string;
}

@get op downloadImage(@path name: string): ImageFile;

@post op uploadImage(@bodyRoot image: ImageFile): void;
```

````tsp
// Use a File as a structured JSON object. The HTTP library will warn you that the File will be serialized as JSON,
// so you should suppress the warning if it's really what you want instead of a binary file upload/download.

// The response body is a JSON object like `{"contentType":<string?>,"filename":<string?>,"contents":<string>}`
@get op downloadTextFileJson(): {
  @header contentType: "application/json",
  @body file: File<"text/plain", string>,
};

// The request body is a JSON object like `{"contentType":<string?>,"filename":<string?>,"contents":<base64>}`
@post op uploadBinaryFileJson(
  @header contentType: "application/json",
  @body file: File<"image/png", bytes>,
): void;

#### Properties
| Name | Type | Description |
|------|------|-------------|
| contentType? | `ContentType` | The allowed media (MIME) types of the file contents.<br /><br />In file bodies, this value comes from the `Content-Type` header of the request or response. In JSON bodies,<br />this value is serialized as a field in the response.<br /><br />NOTE: this is not _necessarily_ the same as the `Content-Type` header of the request or response, but<br />it will be for file bodies. It may be different if the file is serialized as a JSON object. It always refers to the<br />_contents_ of the file, and not necessarily the way the file itself is transmitted or serialized. |
| filename? | `string` | The name of the file, if any.<br /><br />In file bodies, this value comes from the `filename` parameter of the `Content-Disposition` header of the response<br />or multipart payload. In JSON bodies, this value is serialized as a field in the response.<br /><br />NOTE: By default, `filename` cannot be sent in request payloads and can only be sent in responses and multipart<br />payloads, as the `Content-Disposition` header is not valid in requests. If you want to send the `filename` in a request,<br />you must extend the `File` model and override the `filename` property with a different location defined by HTTP metadata<br />decorators. |
| contents | `Contents` | The contents of the file.<br /><br />In file bodies, this value comes from the body of the request, response, or multipart payload. In JSON bodies,<br />this value is serialized as a field in the response. |

### `ForbiddenResponse` {#TypeSpec.Http.ForbiddenResponse}

Access is forbidden.
```typespec
model TypeSpec.Http.ForbiddenResponse
````

#### Properties

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| statusCode | `403` | The status code. |

### `HeaderOptions` {#TypeSpec.Http.HeaderOptions}

Header options.

```typespec
model TypeSpec.Http.HeaderOptions
```

#### Properties

| Name     | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name?    | `string`  | Name of the header when sent over HTTP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| explode? | `boolean` | Equivalent of adding `*` in the path parameter as per [RFC-6570](https://datatracker.ietf.org/doc/html/rfc6570#section-3.2.3)<br /><br />\| Style \| Explode \| Primitive value = 5 \| Array = [3, 4, 5] \| Object = {"role": "admin", "firstName": "Alex"} \|<br />\| ------ \| ------- \| ------------------- \| ----------------- \| ----------------------------------------------- \|<br />\| simple \| false \| `5   ` \| `3,4,5` \| `role,admin,firstName,Alex` \|<br />\| simple \| true \| `5` \| `3,4,5` \| `role=admin,firstName=Alex` \| |

### `HttpPart` {#TypeSpec.Http.HttpPart}

```typespec
model TypeSpec.Http.HttpPart<Type, Options>
```

#### Template Parameters

| Name    | Description |
| ------- | ----------- |
| Type    |             |
| Options |             |

#### Properties

None

### `HttpPartOptions` {#TypeSpec.Http.HttpPartOptions}

```typespec
model TypeSpec.Http.HttpPartOptions
```

#### Properties

| Name  | Type     | Description                                 |
| ----- | -------- | ------------------------------------------- |
| name? | `string` | Name of the part when using the array form. |

### `ImplicitFlow` {#TypeSpec.Http.ImplicitFlow}

Implicit flow

```typespec
model TypeSpec.Http.ImplicitFlow
```

#### Properties

| Name             | Type                                    | Description                       |
| ---------------- | --------------------------------------- | --------------------------------- |
| type             | `TypeSpec.Http.OAuth2FlowType.implicit` | implicit flow                     |
| authorizationUrl | `string`                                | the authorization URL             |
| refreshUrl?      | `string`                                | the refresh URL                   |
| scopes?          | `string[]`                              | list of scopes for the credential |

### `Link` {#TypeSpec.Http.Link}

```typespec
model TypeSpec.Http.Link
```

#### Properties

| Name        | Type              | Description |
| ----------- | ----------------- | ----------- |
| target      | `url`             |             |
| rel         | `string`          |             |
| attributes? | `Record<unknown>` |             |

### `LocationHeader` {#TypeSpec.Http.LocationHeader}

The Location header contains the URL where the status of the long running operation can be checked.

```typespec
model TypeSpec.Http.LocationHeader
```

#### Properties

| Name     | Type     | Description                                                                                         |
| -------- | -------- | --------------------------------------------------------------------------------------------------- |
| location | `string` | The Location header contains the URL where the status of the long running operation can be checked. |

### `MovedResponse` {#TypeSpec.Http.MovedResponse}

The URL of the requested resource has been changed permanently. The new URL is given in the response.

```typespec
model TypeSpec.Http.MovedResponse
```

#### Properties

| Name       | Type     | Description                                                                                         |
| ---------- | -------- | --------------------------------------------------------------------------------------------------- |
| statusCode | `301`    | The status code.                                                                                    |
| location   | `string` | The Location header contains the URL where the status of the long running operation can be checked. |

### `NoAuth` {#TypeSpec.Http.NoAuth}

This authentication option signifies that API is not secured at all.
It might be useful when overriding authentication on interface of operation level.

```typespec
model TypeSpec.Http.NoAuth
```

#### Properties

| Name | Type                            | Description |
| ---- | ------------------------------- | ----------- |
| type | `TypeSpec.Http.AuthType.noAuth` |             |

### `NoContentResponse` {#TypeSpec.Http.NoContentResponse}

There is no content to send for this request, but the headers may be useful.

```typespec
model TypeSpec.Http.NoContentResponse
```

#### Properties

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| statusCode | `204` | The status code. |

### `NotFoundResponse` {#TypeSpec.Http.NotFoundResponse}

The server cannot find the requested resource.

```typespec
model TypeSpec.Http.NotFoundResponse
```

#### Properties

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| statusCode | `404` | The status code. |

### `NotModifiedResponse` {#TypeSpec.Http.NotModifiedResponse}

The client has made a conditional request and the resource has not been modified.

```typespec
model TypeSpec.Http.NotModifiedResponse
```

#### Properties

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| statusCode | `304` | The status code. |

### `OAuth2Auth` {#TypeSpec.Http.OAuth2Auth}

OAuth 2.0 is an authorization protocol that gives an API client limited access to user data on a web server.

OAuth relies on authentication scenarios called flows, which allow the resource owner (user) to share the protected content from the resource server without sharing their credentials.
For that purpose, an OAuth 2.0 server issues access tokens that the client applications can use to access protected resources on behalf of the resource owner.
For more information about OAuth 2.0, see oauth.net and RFC 6749.

```typespec
model TypeSpec.Http.OAuth2Auth<Flows, Scopes>
```

#### Template Parameters

| Name   | Description                                                                                                                                      |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Flows  | The list of supported OAuth2 flows                                                                                                               |
| Scopes | The list of OAuth2 scopes, which are common for every flow from `Flows`. This list is combined with the scopes defined in specific OAuth2 flows. |

#### Properties

| Name          | Type                            | Description |
| ------------- | ------------------------------- | ----------- |
| type          | `TypeSpec.Http.AuthType.oauth2` |             |
| flows         | `Flows`                         |             |
| defaultScopes | `Scopes`                        |             |

### `OkResponse` {#TypeSpec.Http.OkResponse}

The request has succeeded.

```typespec
model TypeSpec.Http.OkResponse
```

#### Properties

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| statusCode | `200` | The status code. |

### `OpenIdConnectAuth` {#TypeSpec.Http.OpenIdConnectAuth}

OpenID Connect (OIDC) is an identity layer built on top of the OAuth 2.0 protocol and supported by some OAuth 2.0 providers, such as Google and Azure Active Directory.
It defines a sign-in flow that enables a client application to authenticate a user, and to obtain information (or "claims") about that user, such as the user name, email, and so on.
User identity information is encoded in a secure JSON Web Token (JWT), called ID token.
OpenID Connect defines a discovery mechanism, called OpenID Connect Discovery, where an OpenID server publishes its metadata at a well-known URL, typically

```http
https://server.com/.well-known/openid-configuration
```

```typespec
model TypeSpec.Http.OpenIdConnectAuth<ConnectUrl>
```

#### Template Parameters

| Name       | Description |
| ---------- | ----------- |
| ConnectUrl |             |

#### Properties

| Name             | Type                                   | Description                                                 |
| ---------------- | -------------------------------------- | ----------------------------------------------------------- |
| type             | `TypeSpec.Http.AuthType.openIdConnect` | Auth type                                                   |
| openIdConnectUrl | `ConnectUrl`                           | Connect url. It can be specified relative to the server URL |

### `PasswordFlow` {#TypeSpec.Http.PasswordFlow}

Resource Owner Password flow

```typespec
model TypeSpec.Http.PasswordFlow
```

#### Properties

| Name        | Type                                    | Description                       |
| ----------- | --------------------------------------- | --------------------------------- |
| type        | `TypeSpec.Http.OAuth2FlowType.password` | password flow                     |
| tokenUrl    | `string`                                | the token URL                     |
| refreshUrl? | `string`                                | the refresh URL                   |
| scopes?     | `string[]`                              | list of scopes for the credential |

### `PatchOptions` {#TypeSpec.Http.PatchOptions}

Options for PATCH operations.

```typespec
model TypeSpec.Http.PatchOptions
```

#### Properties

| Name                 | Type      | Description                                                                                                       |
| -------------------- | --------- | ----------------------------------------------------------------------------------------------------------------- |
| implicitOptionality? | `boolean` | If set to `false`, disables the implicit transform that makes the body of a<br />PATCH operation deeply optional. |

### `PathOptions` {#TypeSpec.Http.PathOptions}

```typespec
model TypeSpec.Http.PathOptions
```

#### Properties

| Name           | Type                                                      | Description                                                                                                                                                                                                                                  |
| -------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name?          | `string`                                                  | Name of the parameter in the uri template.                                                                                                                                                                                                   |
| explode?       | `boolean`                                                 | When interpolating this parameter in the case of array or object expand each value using the given style.<br />Equivalent of adding `*` in the path parameter as per [RFC-6570](https://datatracker.ietf.org/doc/html/rfc6570#section-3.2.3) |
| style?         | `"simple" \| "label" \| "matrix" \| "fragment" \| "path"` | Different interpolating styles for the path parameter.<br />- `simple`: No special encoding.<br />- `label`: Using `.` separator.<br />- `matrix`: `;` as separator.<br />- `fragment`: `#` as separator.<br />- `path`: `/` as separator.   |
| allowReserved? | `boolean`                                                 | When interpolating this parameter do not encode reserved characters.<br />Equivalent of adding `+` in the path parameter as per [RFC-6570](https://datatracker.ietf.org/doc/html/rfc6570#section-3.2.3)                                      |

### `PlainData` {#TypeSpec.Http.PlainData}

Produces a new model with the same properties as T, but with `@query`,
`@header`, `@body`, and `@path` decorators removed from all properties.

```typespec
model TypeSpec.Http.PlainData<Data>
```

#### Template Parameters

| Name | Description                            |
| ---- | -------------------------------------- |
| Data | The model to spread as the plain data. |

#### Properties

None

### `QueryOptions` {#TypeSpec.Http.QueryOptions}

Query parameter options.

```typespec
model TypeSpec.Http.QueryOptions
```

#### Properties

| Name     | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| name?    | `string`  | Name of the query when included in the url.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| explode? | `boolean` | If true send each value in the array/object as a separate query parameter.<br />Equivalent of adding `*` in the path parameter as per [RFC-6570](https://datatracker.ietf.org/doc/html/rfc6570#section-3.2.3)<br /><br />\| Style \| Explode \| Uri Template \| Primitive value id = 5 \| Array id = [3, 4, 5] \| Object id = {"role": "admin", "firstName": "Alex"} \|<br />\| ------ \| ------- \| -------------- \| ---------------------- \| ----------------------- \| -------------------------------------------------- \|<br />\| simple \| false \| `/users{?id}` \| `/users?id=5` \| `/users?id=3,4,5` \| `/users?id=role,admin,firstName,Alex` \|<br />\| simple \| true \| `/users{?id*}` \| `/users?id=5` \| `/users?id=3&id=4&id=5` \| `/users?role=admin&firstName=Alex` \| |

### `Response` {#TypeSpec.Http.Response}

Describes an HTTP response.

```typespec
model TypeSpec.Http.Response<Status>
```

#### Template Parameters

| Name   | Description                      |
| ------ | -------------------------------- |
| Status | The status code of the response. |

#### Properties

| Name       | Type     | Description |
| ---------- | -------- | ----------- |
| statusCode | `Status` |             |

### `UnauthorizedResponse` {#TypeSpec.Http.UnauthorizedResponse}

Access is unauthorized.

```typespec
model TypeSpec.Http.UnauthorizedResponse
```

#### Properties

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| statusCode | `401` | The status code. |

### `ApiKeyLocation` {#TypeSpec.Http.ApiKeyLocation}

Describes the location of the API key

```typespec
enum TypeSpec.Http.ApiKeyLocation
```

| Name   | Value | Description                  |
| ------ | ----- | ---------------------------- |
| header |       | API key is a header value    |
| query  |       | API key is a query parameter |
| cookie |       | API key is found in a cookie |

### `AuthType` {#TypeSpec.Http.AuthType}

Authentication type

```typespec
enum TypeSpec.Http.AuthType
```

| Name          | Value | Description    |
| ------------- | ----- | -------------- |
| http          |       | HTTP           |
| apiKey        |       | API key        |
| oauth2        |       | OAuth2         |
| openIdConnect |       | OpenID connect |
| noAuth        |       | Empty auth     |

### `OAuth2FlowType` {#TypeSpec.Http.OAuth2FlowType}

Describes the OAuth2 flow type

```typespec
enum TypeSpec.Http.OAuth2FlowType
```

| Name              | Value | Description             |
| ----------------- | ----- | ----------------------- |
| authorizationCode |       | authorization code flow |
| implicit          |       | implicit flow           |
| password          |       | password flow           |
| clientCredentials |       | client credential flow  |

### `LinkHeader` {#TypeSpec.Http.LinkHeader}

```typespec
scalar TypeSpec.Http.LinkHeader
```

# Decorators

Decorators exported by @typespec/http

## TypeSpec.Http

### `@body` {#@TypeSpec.Http.body}

Explicitly specify that this property type will be exactly the HTTP body.

This means that any properties under `@body` cannot be marked as headers, query parameters, or path parameters.
If wanting to change the resolution of the body but still mix parameters, use `@bodyRoot`.

```typespec
@TypeSpec.Http.body
```

#### Target

`ModelProperty`

#### Parameters

None

#### Examples

```typespec
op upload(@body image: bytes): void;
op download(): {
  @body image: bytes;
};
```

### `@bodyIgnore` {#@TypeSpec.Http.bodyIgnore}

Specify that this property shouldn't be included in the HTTP body.
This can be useful when bundling metadata together that would result in an empty property to be included in the body.

```typespec
@TypeSpec.Http.bodyIgnore
```

#### Target

`ModelProperty`

#### Parameters

None

#### Examples

```typespec
op upload(
  name: string,
  @bodyIgnore headers: {
    @header id: string;
  },
): void;
```

### `@bodyRoot` {#@TypeSpec.Http.bodyRoot}

Specify that the body resolution should be resolved from that property.
By default the body is resolved by including all properties in the operation request/response that are not metadata.
This allows to nest the body in a property while still allowing to use headers, query parameters, and path parameters in the same model.

```typespec
@TypeSpec.Http.bodyRoot
```

#### Target

`ModelProperty`

#### Parameters

None

#### Examples

```typespec
op upload(
  @bodyRoot user: {
    name: string;
    @header id: string;
  },
): void;
op download(): {
  @bodyRoot user: {
    name: string;
    @header id: string;
  };
};
```

### `@cookie` {#@TypeSpec.Http.cookie}

Specify this property is to be sent or received in the cookie.

```typespec
@TypeSpec.Http.cookie(cookieNameOrOptions?: valueof string | TypeSpec.Http.CookieOptions)
```

#### Target

`ModelProperty`

#### Parameters

| Name                | Type                                            | Description                                                                                                                                                                                       |
| ------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cookieNameOrOptions | `valueof string \| TypeSpec.Http.CookieOptions` | Optional name of the cookie in the cookie or cookie options.<br />By default the cookie name will be the property name converted from camelCase to snake_case. (e.g. `authToken` -> `auth_token`) |

#### Examples

```typespec
op read(@cookie token: string): {
  data: string[];
};
op create(
  @cookie({
    name: "auth_token",
  })
  data: string[],
): void;
```

##### Implicit header name

```typespec
op read(): {
  @cookie authToken: string;
}; // headerName: auth_token
op update(@cookie AuthToken: string): void; // headerName: auth_token
```

### `@delete` {#@TypeSpec.Http.delete}

Specify the HTTP verb for the target operation to be `DELETE`.

```typespec
@TypeSpec.Http.delete
```

#### Target

`Operation`

#### Parameters

None

#### Examples

```typespec
@delete op set(petId: string): void;
```

### `@get` {#@TypeSpec.Http.get}

Specify the HTTP verb for the target operation to be `GET`.

```typespec
@TypeSpec.Http.get
```

#### Target

`Operation`

#### Parameters

None

#### Examples

```typespec
@get op read(): string;
```

### `@head` {#@TypeSpec.Http.head}

Specify the HTTP verb for the target operation to be `HEAD`.

```typespec
@TypeSpec.Http.head
```

#### Target

`Operation`

#### Parameters

None

#### Examples

```typespec
@head op ping(petId: string): void;
```

### `@header` {#@TypeSpec.Http.header}

Specify this property is to be sent or received as an HTTP header.

```typespec
@TypeSpec.Http.header(headerNameOrOptions?: valueof string | TypeSpec.Http.HeaderOptions)
```

#### Target

`ModelProperty`

#### Parameters

| Name                | Type                                            | Description                                                                                                                                                                                                 |
| ------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| headerNameOrOptions | `valueof string \| TypeSpec.Http.HeaderOptions` | Optional name of the header when sent over HTTP or header options.<br />By default the header name will be the property name converted from camelCase to kebab-case. (e.g. `contentType` -> `content-type`) |

#### Examples

```typespec
op read(@header accept: string): {
  @header("ETag") eTag: string;
};
op create(
  @header({
    name: "X-Color",
    format: "csv",
  })
  colors: string[],
): void;
```

##### Implicit header name

```typespec
op read(): {
  @header contentType: string;
}; // headerName: content-type
op update(@header ifMatch: string): void; // headerName: if-match
```

### `@multipartBody` {#@TypeSpec.Http.multipartBody}

```typespec
@TypeSpec.Http.multipartBody
```

#### Target

`ModelProperty`

#### Parameters

None

#### Examples

```tsp
op upload(
  @header `content-type`: "multipart/form-data",
  @multipartBody body: {
    fullName: HttpPart<string>;
    headShots: HttpPart<Image>[];
  },
): void;
```

### `@patch` {#@TypeSpec.Http.patch}

Specify the HTTP verb for the target operation to be `PATCH`.

```typespec
@TypeSpec.Http.patch(options?: valueof TypeSpec.Http.PatchOptions)
```

#### Target

`Operation`

#### Parameters

| Name    | Type                                                                 | Description                      |
| ------- | -------------------------------------------------------------------- | -------------------------------- |
| options | [valueof `PatchOptions`](./data-types.md#TypeSpec.Http.PatchOptions) | Options for the PATCH operation. |

#### Examples

```typespec
@patch op update(pet: Pet): void;
```

```typespec
// Disable implicit optionality, making the body of the PATCH operation use the
// optionality as defined in the `Pet` model.
@patch(#{ implicitOptionality: false })
op update(pet: Pet): void;
```

### `@path` {#@TypeSpec.Http.path}

Explicitly specify that this property is to be interpolated as a path parameter.

```typespec
@TypeSpec.Http.path(paramNameOrOptions?: valueof string | TypeSpec.Http.PathOptions)
```

#### Target

`ModelProperty`

#### Parameters

| Name               | Type                                          | Description                                                    |
| ------------------ | --------------------------------------------- | -------------------------------------------------------------- |
| paramNameOrOptions | `valueof string \| TypeSpec.Http.PathOptions` | Optional name of the parameter in the uri template or options. |

#### Examples

```typespec
@route("/read/{explicit}/things/{implicit}")
op read(@path explicit: string, implicit: string): void;
```

### `@post` {#@TypeSpec.Http.post}

Specify the HTTP verb for the target operation to be `POST`.

```typespec
@TypeSpec.Http.post
```

#### Target

`Operation`

#### Parameters

None

#### Examples

```typespec
@post op create(pet: Pet): void;
```

### `@put` {#@TypeSpec.Http.put}

Specify the HTTP verb for the target operation to be `PUT`.

```typespec
@TypeSpec.Http.put
```

#### Target

`Operation`

#### Parameters

None

#### Examples

```typespec
@put op set(pet: Pet): void;
```

### `@query` {#@TypeSpec.Http.query}

Specify this property is to be sent as a query parameter.

```typespec
@TypeSpec.Http.query(queryNameOrOptions?: valueof string | TypeSpec.Http.QueryOptions)
```

#### Target

`ModelProperty`

#### Parameters

| Name               | Type                                           | Description                                                                     |
| ------------------ | ---------------------------------------------- | ------------------------------------------------------------------------------- |
| queryNameOrOptions | `valueof string \| TypeSpec.Http.QueryOptions` | Optional name of the query when included in the url or query parameter options. |

#### Examples

```typespec
op read(@query select: string, @query("order-by") orderBy: string): void;
op list(@query(#{ name: "id", explode: true }) ids: string[]): void;
```

### `@route` {#@TypeSpec.Http.route}

Defines the relative route URI template for the target operation as defined by [RFC 6570](https://datatracker.ietf.org/doc/html/rfc6570#section-3.2.3)

`@route` can only be applied to operations, namespaces, and interfaces.

```typespec
@TypeSpec.Http.route(path: valueof string)
```

#### Target

`Namespace | Interface | Operation`

#### Parameters

| Name | Type             | Description |
| ---- | ---------------- | ----------- |
| path | `valueof string` |             |

#### Examples

##### Simple path parameter

```typespec
@route("/widgets/{id}") op getWidget(@path id: string): Widget;
```

##### Reserved characters

```typespec
@route("/files{+path}") op getFile(@path path: string): bytes;
```

##### Query parameter

```typespec
@route("/files") op list(select?: string, filter?: string): Files[];
@route("/files{?select,filter}") op listFullUriTemplate(select?: string, filter?: string): Files[];
```

### `@server` {#@TypeSpec.Http.server}

Specify an endpoint for this service. Multiple `@server` decorators can be used to specify multiple endpoints.

```typespec
@TypeSpec.Http.server(url: valueof string, description?: valueof string, parameters?: Record<unknown>)
```

#### Target

`Namespace`

#### Parameters

| Name        | Type              | Description                                             |
| ----------- | ----------------- | ------------------------------------------------------- |
| url         | `valueof string`  | Server endpoint                                         |
| description | `valueof string`  | Description of the endpoint                             |
| parameters  | `Record<unknown>` | Optional set of parameters used to interpolate the url. |

#### Examples

```typespec
@service
@server("https://example.com")
namespace PetStore;
```

##### With a description

```typespec
@service
@server("https://example.com", "Single server endpoint")
namespace PetStore;
```

##### Parameterized

```typespec
@server("https://{region}.foo.com", "Regional endpoint", {
  @doc("Region name")
  region?: string = "westus",
})
```

##### Multiple

```typespec
@service
@server("https://example.com", "Standard endpoint")
@server(
  "https://{project}.private.example.com",
  "Private project endpoint",
  {
    project: string,
  }
)
namespace PetStore;
```

### `@sharedRoute` {#@TypeSpec.Http.sharedRoute}

`@sharedRoute` marks the operation as sharing a route path with other operations.

When an operation is marked with `@sharedRoute`, it enables other operations to share the same
route path as long as those operations are also marked with `@sharedRoute`.

`@sharedRoute` can only be applied directly to operations.

```typespec
@sharedRoute
@route("/widgets")
op getWidget(@path id: string): Widget;
```

```typespec
@TypeSpec.Http.sharedRoute
```

#### Target

`Operation`

#### Parameters

None

### `@statusCode` {#@TypeSpec.Http.statusCode}

Specify the status code for this response. Property type must be a status code integer or a union of status code integer.

```typespec
@TypeSpec.Http.statusCode
```

#### Target

`ModelProperty`

#### Parameters

None

#### Examples

```typespec
op read(): {
  @statusCode _: 200;
  @body pet: Pet;
};
op create(): {
  @statusCode _: 201 | 202;
};
```

### `@useAuth` {#@TypeSpec.Http.useAuth}

Specify authentication for a whole service or specific methods. See the [documentation in the Http library](https://typespec.io/docs/libraries/http/authentication) for full details.

```typespec
@TypeSpec.Http.useAuth(auth: {} | Union | {}[])
```

#### Target

`Namespace | Interface | Operation`

#### Parameters

| Name | Type                  | Description                                                                                                                                                     |
| ---- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| auth | `{} \| Union \| {}[]` | Authentication configuration. Can be a single security scheme, a union(either option is valid authentication) or a tuple (must use all authentication together) |

#### Examples

```typespec
@service
@useAuth(BasicAuth)
namespace PetStore;
```

# Data types

Data types exported by @typespec/openapi

## TypeSpec.OpenAPI

### `AdditionalInfo` {#TypeSpec.OpenAPI.AdditionalInfo}

Additional information for the OpenAPI document.

```typespec
model TypeSpec.OpenAPI.AdditionalInfo
```

#### Properties

| Name            | Type                                                  | Description                                                                                                                       |
| --------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| title?          | `string`                                              | The title of the API. Overrides the `@service` title.                                                                             |
| summary?        | `string`                                              | A short summary of the API. Overrides the `@summary` provided on the service namespace.                                           |
| version?        | `string`                                              | The version of the OpenAPI document (which is distinct from the OpenAPI Specification version or the API implementation version). |
| termsOfService? | `url`                                                 | A URL to the Terms of Service for the API. MUST be in the format of a URL.                                                        |
| contact?        | [`Contact`](./data-types.md#TypeSpec.OpenAPI.Contact) | The contact information for the exposed API.                                                                                      |
| license?        | [`License`](./data-types.md#TypeSpec.OpenAPI.License) | The license information for the exposed API.                                                                                      |
|                 | `unknown`                                             | Additional properties                                                                                                             |

### `Contact` {#TypeSpec.OpenAPI.Contact}

Contact information for the exposed API.

```typespec
model TypeSpec.OpenAPI.Contact
```

#### Properties

| Name   | Type      | Description                                                                                      |
| ------ | --------- | ------------------------------------------------------------------------------------------------ |
| name?  | `string`  | The identifying name of the contact person/organization.                                         |
| url?   | `url`     | The URL pointing to the contact information. MUST be in the format of a URL.                     |
| email? | `string`  | The email address of the contact person/organization. MUST be in the format of an email address. |
|        | `unknown` | Additional properties                                                                            |

### `ExternalDocs` {#TypeSpec.OpenAPI.ExternalDocs}

External Docs information.

```typespec
model TypeSpec.OpenAPI.ExternalDocs
```

#### Properties

| Name         | Type      | Description           |
| ------------ | --------- | --------------------- |
| url          | `string`  | Documentation url     |
| description? | `string`  | Optional description  |
|              | `unknown` | Additional properties |

### `License` {#TypeSpec.OpenAPI.License}

License information for the exposed API.

```typespec
model TypeSpec.OpenAPI.License
```

#### Properties

| Name | Type      | Description                                                            |
| ---- | --------- | ---------------------------------------------------------------------- |
| name | `string`  | The license name used for the API.                                     |
| url? | `url`     | A URL to the license used for the API. MUST be in the format of a URL. |
|      | `unknown` | Additional properties                                                  |

### `TagMetadata` {#TypeSpec.OpenAPI.TagMetadata}

Metadata to a single tag that is used by operations.

```typespec
model TypeSpec.OpenAPI.TagMetadata
```

#### Properties

| Name          | Type                                                            | Description                                                                                                                            |
| ------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| description?  | `string`                                                        | A description of the API.                                                                                                              |
| externalDocs? | [`ExternalDocs`](./data-types.md#TypeSpec.OpenAPI.ExternalDocs) | An external Docs information of the API.                                                                                               |
| parent?       | `string`                                                        | The name of a tag that this tag is nested under. Only supported in OpenAPI 3.2. For 3.0 and 3.1, this will be converted to `x-parent`. |
|               | `unknown`                                                       | Additional properties                                                                                                                  |

# Decorators

Decorators exported by @typespec/openapi

## TypeSpec.OpenAPI

### `@defaultResponse` {#@TypeSpec.OpenAPI.defaultResponse}

Specify that this model is to be treated as the OpenAPI `default` response.
This differs from the compiler built-in `@error` decorator as this does not necessarily represent an error.

```typespec
@TypeSpec.OpenAPI.defaultResponse
```

#### Target

`Model`

#### Parameters

None

#### Examples

```typespec
@defaultResponse
model PetStoreResponse is object;

op listPets(): Pet[] | PetStoreResponse;
```

### `@extension` {#@TypeSpec.OpenAPI.extension}

Attach some custom data to the OpenAPI element generated from this type.

```typespec
@TypeSpec.OpenAPI.extension(key: valueof string, value: valueof unknown)
```

#### Target

`unknown`

#### Parameters

| Name  | Type              | Description      |
| ----- | ----------------- | ---------------- |
| key   | `valueof string`  | Extension key.   |
| value | `valueof unknown` | Extension value. |

#### Examples

```typespec
@extension("x-custom", "My value")
@extension("x-pageable", #{ nextLink: "x-next-link" })
op read(): string;
```

### `@externalDocs` {#@TypeSpec.OpenAPI.externalDocs}

Specify the OpenAPI `externalDocs` property for this type.

```typespec
@TypeSpec.OpenAPI.externalDocs(url: valueof string, description?: valueof string)
```

#### Target

`unknown`

#### Parameters

| Name        | Type             | Description             |
| ----------- | ---------------- | ----------------------- |
| url         | `valueof string` | Url to the docs         |
| description | `valueof string` | Description of the docs |

#### Examples

```typespec
@externalDocs(
  "https://example.com/detailed.md",
  "Detailed information on how to use this operation"
)
op listPets(): Pet[];
```

### `@info` {#@TypeSpec.OpenAPI.info}

Specify OpenAPI additional information.
The service `title` is already specified using `@service`.

```typespec
@TypeSpec.OpenAPI.info(additionalInfo: valueof TypeSpec.OpenAPI.AdditionalInfo)
```

#### Target

`Namespace`

#### Parameters

| Name           | Type                                                                        | Description            |
| -------------- | --------------------------------------------------------------------------- | ---------------------- |
| additionalInfo | [valueof `AdditionalInfo`](./data-types.md#TypeSpec.OpenAPI.AdditionalInfo) | Additional information |

### `@operationId` {#@TypeSpec.OpenAPI.operationId}

Specify the OpenAPI `operationId` property for this operation.

```typespec
@TypeSpec.OpenAPI.operationId(operationId: valueof string)
```

#### Target

`Operation`

#### Parameters

| Name        | Type             | Description         |
| ----------- | ---------------- | ------------------- |
| operationId | `valueof string` | Operation id value. |

#### Examples

```typespec
@operationId("download")
op read(): string;
```

### `@tagMetadata` {#@TypeSpec.OpenAPI.tagMetadata}

Specify OpenAPI additional information.

```typespec
@TypeSpec.OpenAPI.tagMetadata(name: valueof string, tagMetadata: valueof TypeSpec.OpenAPI.TagMetadata)
```

#### Target

`Namespace`

#### Parameters

| Name        | Type                                                                  | Description            |
| ----------- | --------------------------------------------------------------------- | ---------------------- |
| name        | `valueof string`                                                      | tag name               |
| tagMetadata | [valueof `TagMetadata`](./data-types.md#TypeSpec.OpenAPI.TagMetadata) | Additional information |

#### Examples

```typespec
@service
@tagMetadata(
  "Tag Name",
  #{
    description: "Tag description",
    externalDocs: #{ url: "https://example.com", description: "More info.", `x-custom`: "string" },
    `x-custom`: "string",
  }
)
@tagMetadata("Child Tag", #{ description: "Child tag description", parent: "Tag Name" })
namespace PetStore {

}
```

# Data types

Data types exported by @typespec/rest

## TypeSpec.Rest

### `ResourceLocation` {#TypeSpec.Rest.ResourceLocation}

A URL that points to a resource.

```typespec
scalar TypeSpec.Rest.ResourceLocation
```

## TypeSpec.Rest.Resource

### `CollectionWithNextLink` {#TypeSpec.Rest.Resource.CollectionWithNextLink}

Structure for a paging response using `value` and `nextLink` to represent pagination.

```typespec
model TypeSpec.Rest.Resource.CollectionWithNextLink<Resource>
```

#### Template Parameters

| Name     | Description                          |
| -------- | ------------------------------------ |
| Resource | The resource type of the collection. |

#### Properties

| Name      | Type                             | Description |
| --------- | -------------------------------- | ----------- |
| value     | `Array<Element>`                 |             |
| nextLink? | `TypeSpec.Rest.ResourceLocation` |             |

### `KeysOf` {#TypeSpec.Rest.Resource.KeysOf}

Dynamically gathers keys of the model type `Resource`.

```typespec
model TypeSpec.Rest.Resource.KeysOf<Resource>
```

#### Template Parameters

| Name     | Description                |
| -------- | -------------------------- |
| Resource | The target resource model. |

#### Properties

None

### `ParentKeysOf` {#TypeSpec.Rest.Resource.ParentKeysOf}

Dynamically gathers parent keys of the model type `Resource`.

```typespec
model TypeSpec.Rest.Resource.ParentKeysOf<Resource>
```

#### Template Parameters

| Name     | Description                |
| -------- | -------------------------- |
| Resource | The target resource model. |

#### Properties

None

### `ResourceCollectionParameters` {#TypeSpec.Rest.Resource.ResourceCollectionParameters}

Represents collection operation parameters for the resource of type `Resource`.

```typespec
model TypeSpec.Rest.Resource.ResourceCollectionParameters<Resource>
```

#### Template Parameters

| Name     | Description         |
| -------- | ------------------- |
| Resource | The resource model. |

#### Properties

None

### `ResourceCreatedResponse` {#TypeSpec.Rest.Resource.ResourceCreatedResponse}

Resource create operation completed successfully.

```typespec
model TypeSpec.Rest.Resource.ResourceCreatedResponse<Resource>
```

#### Template Parameters

| Name     | Description                          |
| -------- | ------------------------------------ |
| Resource | The resource model that was created. |

#### Properties

| Name       | Type       | Description      |
| ---------- | ---------- | ---------------- |
| statusCode | `201`      | The status code. |
| body       | `Resource` |                  |

### `ResourceCreateModel` {#TypeSpec.Rest.Resource.ResourceCreateModel}

Resource create operation model.

```typespec
model TypeSpec.Rest.Resource.ResourceCreateModel<Resource>
```

#### Template Parameters

| Name     | Description                   |
| -------- | ----------------------------- |
| Resource | The resource model to create. |

#### Properties

None

### `ResourceCreateOrUpdateModel` {#TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel}

Resource create or update operation model.

```typespec
model TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel<Resource>
```

#### Template Parameters

| Name     | Description                             |
| -------- | --------------------------------------- |
| Resource | The resource model to create or update. |

#### Properties

None

### `ResourceDeletedResponse` {#TypeSpec.Rest.Resource.ResourceDeletedResponse}

Resource deleted successfully.

```typespec
model TypeSpec.Rest.Resource.ResourceDeletedResponse
```

#### Properties

| Name | Type  | Description      |
| ---- | ----- | ---------------- |
| \_   | `200` | The status code. |

### `ResourceError` {#TypeSpec.Rest.Resource.ResourceError}

The default error response for resource operations.

```typespec
model TypeSpec.Rest.Resource.ResourceError
```

#### Properties

| Name    | Type     | Description        |
| ------- | -------- | ------------------ |
| code    | `int32`  | The error code.    |
| message | `string` | The error message. |

### `ResourceParameters` {#TypeSpec.Rest.Resource.ResourceParameters}

Represents operation parameters for the resource of type `Resource`.

```typespec
model TypeSpec.Rest.Resource.ResourceParameters<Resource>
```

#### Template Parameters

| Name     | Description         |
| -------- | ------------------- |
| Resource | The resource model. |

#### Properties

None

# Decorators

Decorators exported by @typespec/rest

## TypeSpec.Rest

### `@action` {#@TypeSpec.Rest.action}

Specify this operation is an action. (Scoped to a resource item /pets/{petId}/my-action)

```typespec
@TypeSpec.Rest.action(name?: valueof string)
```

#### Target

`Operation`

#### Parameters

| Name | Type             | Description                                                                   |
| ---- | ---------------- | ----------------------------------------------------------------------------- |
| name | `valueof string` | Name of the action. If not specified, the name of the operation will be used. |

### `@actionSeparator` {#@TypeSpec.Rest.actionSeparator}

Defines the separator string that is inserted before the action name in auto-generated routes for actions.

When applied to a namespace, the separator applies to all action operations in that namespace and its sub-namespaces.
When applied to an interface, the separator applies to all action operations in that interface and overrides any namespace-level separator.
When applied to an operation, the separator applies only to that operation and overrides any interface or namespace-level separator.

```typespec
@TypeSpec.Rest.actionSeparator(seperator: valueof "/" | ":" | "/:")
```

#### Target

`Operation | Interface | Namespace`

#### Parameters

| Name      | Type                         | Description                                                      |
| --------- | ---------------------------- | ---------------------------------------------------------------- |
| seperator | `valueof "/" \| ":" \| "/:"` | Seperator seperating the action segment from the rest of the url |

### `@autoRoute` {#@TypeSpec.Rest.autoRoute}

This interface or operation should resolve its route automatically. To be used with resource types where the route segments area defined on the models.

```typespec
@TypeSpec.Rest.autoRoute
```

#### Target

`Interface | Operation`

#### Parameters

None

#### Examples

```typespec
@autoRoute
interface Pets {
  get(@segment("pets") @path id: string): void; //-> route: /pets/{id}
}
```

### `@collectionAction` {#@TypeSpec.Rest.collectionAction}

Specify this operation is a collection action. (Scopped to a resource, /pets/my-action)

```typespec
@TypeSpec.Rest.collectionAction(resourceType: Model, name?: valueof string)
```

#### Target

`Operation`

#### Parameters

| Name         | Type             | Description                                                                   |
| ------------ | ---------------- | ----------------------------------------------------------------------------- |
| resourceType | `Model`          | Resource marked with                                                          |
| name         | `valueof string` | Name of the action. If not specified, the name of the operation will be used. |

### `@copyResourceKeyParameters` {#@TypeSpec.Rest.copyResourceKeyParameters}

Copy the resource key parameters on the model

```typespec
@TypeSpec.Rest.copyResourceKeyParameters(filter?: valueof string)
```

#### Target

`Model`

#### Parameters

| Name   | Type             | Description                           |
| ------ | ---------------- | ------------------------------------- |
| filter | `valueof string` | Filter to exclude certain properties. |

### `@createsOrReplacesResource` {#@TypeSpec.Rest.createsOrReplacesResource}

Specify that this is a CreateOrReplace operation for a given resource.

```typespec
@TypeSpec.Rest.createsOrReplacesResource(resourceType: Model)
```

#### Target

`Operation`

#### Parameters

| Name         | Type    | Description          |
| ------------ | ------- | -------------------- |
| resourceType | `Model` | Resource marked with |

### `@createsOrUpdatesResource` {#@TypeSpec.Rest.createsOrUpdatesResource}

Specify that this is a CreatesOrUpdate operation for a given resource.

```typespec
@TypeSpec.Rest.createsOrUpdatesResource(resourceType: Model)
```

#### Target

`Operation`

#### Parameters

| Name         | Type    | Description          |
| ------------ | ------- | -------------------- |
| resourceType | `Model` | Resource marked with |

### `@createsResource` {#@TypeSpec.Rest.createsResource}

Specify that this is a Create operation for a given resource.

```typespec
@TypeSpec.Rest.createsResource(resourceType: Model)
```

#### Target

`Operation`

#### Parameters

| Name         | Type    | Description          |
| ------------ | ------- | -------------------- |
| resourceType | `Model` | Resource marked with |

### `@deletesResource` {#@TypeSpec.Rest.deletesResource}

Specify that this is a Delete operation for a given resource.

```typespec
@TypeSpec.Rest.deletesResource(resourceType: Model)
```

#### Target

`Operation`

#### Parameters

| Name         | Type    | Description          |
| ------------ | ------- | -------------------- |
| resourceType | `Model` | Resource marked with |

### `@listsResource` {#@TypeSpec.Rest.listsResource}

Specify that this is a List operation for a given resource.

```typespec
@TypeSpec.Rest.listsResource(resourceType: Model)
```

#### Target

`Operation`

#### Parameters

| Name         | Type    | Description          |
| ------------ | ------- | -------------------- |
| resourceType | `Model` | Resource marked with |

### `@parentResource` {#@TypeSpec.Rest.parentResource}

Mark model as a child of the given parent resource.

```typespec
@TypeSpec.Rest.parentResource(parent: Model)
```

#### Target

`Model`

#### Parameters

| Name   | Type    | Description   |
| ------ | ------- | ------------- |
| parent | `Model` | Parent model. |

### `@readsResource` {#@TypeSpec.Rest.readsResource}

Specify that this is a Read operation for a given resource.

```typespec
@TypeSpec.Rest.readsResource(resourceType: Model)
```

#### Target

`Operation`

#### Parameters

| Name         | Type    | Description          |
| ------------ | ------- | -------------------- |
| resourceType | `Model` | Resource marked with |

### `@resource` {#@TypeSpec.Rest.resource}

Mark this model as a resource type with a name.

```typespec
@TypeSpec.Rest.resource(collectionName: valueof string)
```

#### Target

`Model`

#### Parameters

| Name           | Type             | Description            |
| -------------- | ---------------- | ---------------------- |
| collectionName | `valueof string` | type's collection name |

### `@segment` {#@TypeSpec.Rest.segment}

Defines the preceding path segment for a

```typespec
@TypeSpec.Rest.segment(name: valueof string)
```

#### Target

`Model | ModelProperty | Operation`

#### Parameters

| Name | Type             | Description                                                                                    |
| ---- | ---------------- | ---------------------------------------------------------------------------------------------- |
| name | `valueof string` | Segment that will be inserted into the operation route before the path parameter's name field. |

#### Examples

### `@segmentOf` {#@TypeSpec.Rest.segmentOf}

Returns the URL segment of a given model if it has `@segment` and `@key` decorator.

```typespec
@TypeSpec.Rest.segmentOf(type: Model)
```

#### Target

`Operation`

#### Parameters

| Name | Type    | Description  |
| ---- | ------- | ------------ |
| type | `Model` | Target model |

### `@updatesResource` {#@TypeSpec.Rest.updatesResource}

Specify that this is a Update operation for a given resource.

```typespec
@TypeSpec.Rest.updatesResource(resourceType: Model)
```

#### Target

`Operation`

#### Parameters

| Name         | Type    | Description          |
| ------------ | ------- | -------------------- |
| resourceType | `Model` | Resource marked with |

# Interfaces and Operations

Interfaces and Operations exported by @typespec/rest

## TypeSpec.Rest.Resource

### `ExtensionResourceCollectionOperations` {#TypeSpec.Rest.Resource.ExtensionResourceCollectionOperations}

Extension resource operation templates for extension resource collections.

```typespec
interface TypeSpec.Rest.Resource.ExtensionResourceCollectionOperations<Extension, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Extension | The extension resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `ExtensionResourceCollectionOperations.create` {#TypeSpec.Rest.Resource.ExtensionResourceCollectionOperations<Extension, Resource, Error>.create}

Creates a new instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceCollectionOperations<Extension, Resource, Error>.create(resource: TypeSpec.Rest.Resource.ResourceCreateModel<Resource>): Extension | TypeSpec.Rest.Resource.ResourceCreatedResponse<Resource> | Error
```

#### `ExtensionResourceCollectionOperations.list` {#TypeSpec.Rest.Resource.ExtensionResourceCollectionOperations<Extension, Resource, Error>.list}

Lists all instances of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceCollectionOperations<Extension, Resource, Error>.list(): TypeSpec.Rest.Resource.CollectionWithNextLink<Resource> | Error
```

### `ExtensionResourceCreate` {#TypeSpec.Rest.Resource.ExtensionResourceCreate}

Extension resource create operation template.

```typespec
interface TypeSpec.Rest.Resource.ExtensionResourceCreate<Extension, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Extension | The extension resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `ExtensionResourceCreate.create` {#TypeSpec.Rest.Resource.ExtensionResourceCreate<Extension, Resource, Error>.create}

Creates a new instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceCreate<Extension, Resource, Error>.create(resource: TypeSpec.Rest.Resource.ResourceCreateModel<Resource>): Extension | TypeSpec.Rest.Resource.ResourceCreatedResponse<Resource> | Error
```

### `ExtensionResourceCreateOrUpdate` {#TypeSpec.Rest.Resource.ExtensionResourceCreateOrUpdate}

Extension resource create or update operation template.

```typespec
interface TypeSpec.Rest.Resource.ExtensionResourceCreateOrUpdate<Extension, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Extension | The extension resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `ExtensionResourceCreateOrUpdate.createOrUpdate` {#TypeSpec.Rest.Resource.ExtensionResourceCreateOrUpdate<Extension, Resource, Error>.createOrUpdate}

Creates or update an instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceCreateOrUpdate<Extension, Resource, Error>.createOrUpdate(resource: TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel<Resource>): Extension | TypeSpec.Rest.Resource.ResourceCreatedResponse<Resource> | Error
```

### `ExtensionResourceDelete` {#TypeSpec.Rest.Resource.ExtensionResourceDelete}

Extension resource delete operation template.

```typespec
interface TypeSpec.Rest.Resource.ExtensionResourceDelete<Extension, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Extension | The extension resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `ExtensionResourceDelete.delete` {#TypeSpec.Rest.Resource.ExtensionResourceDelete<Extension, Resource, Error>.delete}

Deletes an existing instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceDelete<Extension, Resource, Error>.delete(): TypeSpec.Rest.Resource.ResourceDeletedResponse | Error
```

### `ExtensionResourceInstanceOperations` {#TypeSpec.Rest.Resource.ExtensionResourceInstanceOperations}

Extension resource operation templates for extension resource instances.

```typespec
interface TypeSpec.Rest.Resource.ExtensionResourceInstanceOperations<Extension, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Extension | The extension resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `ExtensionResourceInstanceOperations.get` {#TypeSpec.Rest.Resource.ExtensionResourceInstanceOperations<Extension, Resource, Error>.get}

Gets an instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceInstanceOperations<Extension, Resource, Error>.get(): Extension | Error
```

#### `ExtensionResourceInstanceOperations.update` {#TypeSpec.Rest.Resource.ExtensionResourceInstanceOperations<Extension, Resource, Error>.update}

Updates an existing instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceInstanceOperations<Extension, Resource, Error>.update(properties: TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel<Resource>): Extension | Error
```

#### `ExtensionResourceInstanceOperations.delete` {#TypeSpec.Rest.Resource.ExtensionResourceInstanceOperations<Extension, Resource, Error>.delete}

Deletes an existing instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceInstanceOperations<Extension, Resource, Error>.delete(): TypeSpec.Rest.Resource.ResourceDeletedResponse | Error
```

### `ExtensionResourceList` {#TypeSpec.Rest.Resource.ExtensionResourceList}

Extension resource list operation template.

```typespec
interface TypeSpec.Rest.Resource.ExtensionResourceList<Extension, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Extension | The extension resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `ExtensionResourceList.list` {#TypeSpec.Rest.Resource.ExtensionResourceList<Extension, Resource, Error>.list}

Lists all instances of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceList<Extension, Resource, Error>.list(): TypeSpec.Rest.Resource.CollectionWithNextLink<Resource> | Error
```

### `ExtensionResourceOperations` {#TypeSpec.Rest.Resource.ExtensionResourceOperations}

Extension resource operation templates for extension resource instances and collections.

```typespec
interface TypeSpec.Rest.Resource.ExtensionResourceOperations<Extension, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Extension | The extension resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `ExtensionResourceOperations.get` {#TypeSpec.Rest.Resource.ExtensionResourceOperations<Extension, Resource, Error>.get}

Gets an instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceOperations<Extension, Resource, Error>.get(): Extension | Error
```

#### `ExtensionResourceOperations.update` {#TypeSpec.Rest.Resource.ExtensionResourceOperations<Extension, Resource, Error>.update}

Updates an existing instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceOperations<Extension, Resource, Error>.update(properties: TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel<Resource>): Extension | Error
```

#### `ExtensionResourceOperations.delete` {#TypeSpec.Rest.Resource.ExtensionResourceOperations<Extension, Resource, Error>.delete}

Deletes an existing instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceOperations<Extension, Resource, Error>.delete(): TypeSpec.Rest.Resource.ResourceDeletedResponse | Error
```

#### `ExtensionResourceOperations.create` {#TypeSpec.Rest.Resource.ExtensionResourceOperations<Extension, Resource, Error>.create}

Creates a new instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceOperations<Extension, Resource, Error>.create(resource: TypeSpec.Rest.Resource.ResourceCreateModel<Resource>): Extension | TypeSpec.Rest.Resource.ResourceCreatedResponse<Resource> | Error
```

#### `ExtensionResourceOperations.list` {#TypeSpec.Rest.Resource.ExtensionResourceOperations<Extension, Resource, Error>.list}

Lists all instances of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceOperations<Extension, Resource, Error>.list(): TypeSpec.Rest.Resource.CollectionWithNextLink<Resource> | Error
```

### `ExtensionResourceRead` {#TypeSpec.Rest.Resource.ExtensionResourceRead}

Extension resource read operation template.

```typespec
interface TypeSpec.Rest.Resource.ExtensionResourceRead<Extension, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Extension | The extension resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `ExtensionResourceRead.get` {#TypeSpec.Rest.Resource.ExtensionResourceRead<Extension, Resource, Error>.get}

Gets an instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceRead<Extension, Resource, Error>.get(): Extension | Error
```

### `ExtensionResourceUpdate` {#TypeSpec.Rest.Resource.ExtensionResourceUpdate}

Extension resource update operation template.

```typespec
interface TypeSpec.Rest.Resource.ExtensionResourceUpdate<Extension, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Extension | The extension resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `ExtensionResourceUpdate.update` {#TypeSpec.Rest.Resource.ExtensionResourceUpdate<Extension, Resource, Error>.update}

Updates an existing instance of the extension resource.

```typespec
op TypeSpec.Rest.Resource.ExtensionResourceUpdate<Extension, Resource, Error>.update(properties: TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel<Resource>): Extension | Error
```

### `ResourceCollectionOperations` {#TypeSpec.Rest.Resource.ResourceCollectionOperations}

Resource operation templates for resource collections.

```typespec
interface TypeSpec.Rest.Resource.ResourceCollectionOperations<Resource, Error>
```

#### Template Parameters

| Name     | Description         |
| -------- | ------------------- |
| Resource | The resource model. |
| Error    | The error response. |

#### `ResourceCollectionOperations.create` {#TypeSpec.Rest.Resource.ResourceCollectionOperations<Resource, Error>.create}

Creates a new instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceCollectionOperations<Resource, Error>.create(resource: TypeSpec.Rest.Resource.ResourceCreateModel<Resource>): Resource | TypeSpec.Rest.Resource.ResourceCreatedResponse<Resource> | Error
```

#### `ResourceCollectionOperations.list` {#TypeSpec.Rest.Resource.ResourceCollectionOperations<Resource, Error>.list}

Lists all instances of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceCollectionOperations<Resource, Error>.list(): TypeSpec.Rest.Resource.CollectionWithNextLink<Resource> | Error
```

### `ResourceCreate` {#TypeSpec.Rest.Resource.ResourceCreate}

Resource create operation template.

```typespec
interface TypeSpec.Rest.Resource.ResourceCreate<Resource, Error>
```

#### Template Parameters

| Name     | Description                   |
| -------- | ----------------------------- |
| Resource | The resource model to create. |
| Error    | The error response.           |

#### `ResourceCreate.create` {#TypeSpec.Rest.Resource.ResourceCreate<Resource, Error>.create}

Creates a new instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceCreate<Resource, Error>.create(resource: TypeSpec.Rest.Resource.ResourceCreateModel<Resource>): Resource | TypeSpec.Rest.Resource.ResourceCreatedResponse<Resource> | Error
```

### `ResourceCreateOrReplace` {#TypeSpec.Rest.Resource.ResourceCreateOrReplace}

Resource create or replace operation template.

```typespec
interface TypeSpec.Rest.Resource.ResourceCreateOrReplace<Resource, Error>
```

#### Template Parameters

| Name     | Description                              |
| -------- | ---------------------------------------- |
| Resource | The resource model to create or replace. |
| Error    | The error response.                      |

#### `ResourceCreateOrReplace.createOrReplace` {#TypeSpec.Rest.Resource.ResourceCreateOrReplace<Resource, Error>.createOrReplace}

Creates or replaces a instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceCreateOrReplace<Resource, Error>.createOrReplace(resource: TypeSpec.Rest.Resource.ResourceCreateModel<Resource>): Resource | TypeSpec.Rest.Resource.ResourceCreatedResponse<Resource> | Error
```

### `ResourceCreateOrUpdate` {#TypeSpec.Rest.Resource.ResourceCreateOrUpdate}

Resource create or update operation template.

```typespec
interface TypeSpec.Rest.Resource.ResourceCreateOrUpdate<Resource, Error>
```

#### Template Parameters

| Name     | Description                             |
| -------- | --------------------------------------- |
| Resource | The resource model to create or update. |
| Error    | The error response.                     |

#### `ResourceCreateOrUpdate.createOrUpdate` {#TypeSpec.Rest.Resource.ResourceCreateOrUpdate<Resource, Error>.createOrUpdate}

Creates or update an instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceCreateOrUpdate<Resource, Error>.createOrUpdate(resource: TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel<Resource>): Resource | TypeSpec.Rest.Resource.ResourceCreatedResponse<Resource> | Error
```

### `ResourceDelete` {#TypeSpec.Rest.Resource.ResourceDelete}

Resource delete operation template.

```typespec
interface TypeSpec.Rest.Resource.ResourceDelete<Resource, Error>
```

#### Template Parameters

| Name     | Description                   |
| -------- | ----------------------------- |
| Resource | The resource model to delete. |
| Error    | The error response.           |

#### `ResourceDelete.delete` {#TypeSpec.Rest.Resource.ResourceDelete<Resource, Error>.delete}

Deletes an existing instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceDelete<Resource, Error>.delete(): TypeSpec.Rest.Resource.ResourceDeletedResponse | Error
```

### `ResourceInstanceOperations` {#TypeSpec.Rest.Resource.ResourceInstanceOperations}

Resource operation templates for resource instances.

```typespec
interface TypeSpec.Rest.Resource.ResourceInstanceOperations<Resource, Error>
```

#### Template Parameters

| Name     | Description         |
| -------- | ------------------- |
| Resource | The resource model. |
| Error    | The error response. |

#### `ResourceInstanceOperations.get` {#TypeSpec.Rest.Resource.ResourceInstanceOperations<Resource, Error>.get}

Gets an instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceInstanceOperations<Resource, Error>.get(): Resource | Error
```

#### `ResourceInstanceOperations.update` {#TypeSpec.Rest.Resource.ResourceInstanceOperations<Resource, Error>.update}

Updates an existing instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceInstanceOperations<Resource, Error>.update(properties: TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel<Resource>): Resource | Error
```

#### `ResourceInstanceOperations.delete` {#TypeSpec.Rest.Resource.ResourceInstanceOperations<Resource, Error>.delete}

Deletes an existing instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceInstanceOperations<Resource, Error>.delete(): TypeSpec.Rest.Resource.ResourceDeletedResponse | Error
```

### `ResourceList` {#TypeSpec.Rest.Resource.ResourceList}

Resource list operation template.

```typespec
interface TypeSpec.Rest.Resource.ResourceList<Resource, Error>
```

#### Template Parameters

| Name     | Description                 |
| -------- | --------------------------- |
| Resource | The resource model to list. |
| Error    | The error response.         |

#### `ResourceList.list` {#TypeSpec.Rest.Resource.ResourceList<Resource, Error>.list}

Lists all instances of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceList<Resource, Error>.list(): TypeSpec.Rest.Resource.CollectionWithNextLink<Resource> | Error
```

### `ResourceOperations` {#TypeSpec.Rest.Resource.ResourceOperations}

Resource operation templates for resources.

```typespec
interface TypeSpec.Rest.Resource.ResourceOperations<Resource, Error>
```

#### Template Parameters

| Name     | Description         |
| -------- | ------------------- |
| Resource | The resource model. |
| Error    | The error response. |

#### `ResourceOperations.get` {#TypeSpec.Rest.Resource.ResourceOperations<Resource, Error>.get}

Gets an instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceOperations<Resource, Error>.get(): Resource | Error
```

#### `ResourceOperations.update` {#TypeSpec.Rest.Resource.ResourceOperations<Resource, Error>.update}

Updates an existing instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceOperations<Resource, Error>.update(properties: TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel<Resource>): Resource | Error
```

#### `ResourceOperations.delete` {#TypeSpec.Rest.Resource.ResourceOperations<Resource, Error>.delete}

Deletes an existing instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceOperations<Resource, Error>.delete(): TypeSpec.Rest.Resource.ResourceDeletedResponse | Error
```

#### `ResourceOperations.create` {#TypeSpec.Rest.Resource.ResourceOperations<Resource, Error>.create}

Creates a new instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceOperations<Resource, Error>.create(resource: TypeSpec.Rest.Resource.ResourceCreateModel<Resource>): Resource | TypeSpec.Rest.Resource.ResourceCreatedResponse<Resource> | Error
```

#### `ResourceOperations.list` {#TypeSpec.Rest.Resource.ResourceOperations<Resource, Error>.list}

Lists all instances of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceOperations<Resource, Error>.list(): TypeSpec.Rest.Resource.CollectionWithNextLink<Resource> | Error
```

### `ResourceRead` {#TypeSpec.Rest.Resource.ResourceRead}

Represents the resource GET operation.

```typespec
interface TypeSpec.Rest.Resource.ResourceRead<Resource, Error>
```

#### Template Parameters

| Name     | Description         |
| -------- | ------------------- |
| Resource | The resource model. |
| Error    | The error response. |

#### `ResourceRead.get` {#TypeSpec.Rest.Resource.ResourceRead<Resource, Error>.get}

Gets an instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceRead<Resource, Error>.get(): Resource | Error
```

### `ResourceUpdate` {#TypeSpec.Rest.Resource.ResourceUpdate}

Resource update operation template.

```typespec
interface TypeSpec.Rest.Resource.ResourceUpdate<Resource, Error>
```

#### Template Parameters

| Name     | Description                   |
| -------- | ----------------------------- |
| Resource | The resource model to update. |
| Error    | The error response.           |

#### `ResourceUpdate.update` {#TypeSpec.Rest.Resource.ResourceUpdate<Resource, Error>.update}

Updates an existing instance of the resource.

```typespec
op TypeSpec.Rest.Resource.ResourceUpdate<Resource, Error>.update(properties: TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel<Resource>): Resource | Error
```

### `SingletonResourceOperations` {#TypeSpec.Rest.Resource.SingletonResourceOperations}

Singleton resource operation templates for singleton resource instances.

```typespec
interface TypeSpec.Rest.Resource.SingletonResourceOperations<Singleton, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Singleton | The singleton resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `SingletonResourceOperations.get` {#TypeSpec.Rest.Resource.SingletonResourceOperations<Singleton, Resource, Error>.get}

Gets the singleton resource.

```typespec
op TypeSpec.Rest.Resource.SingletonResourceOperations<Singleton, Resource, Error>.get(): Singleton | Error
```

#### `SingletonResourceOperations.update` {#TypeSpec.Rest.Resource.SingletonResourceOperations<Singleton, Resource, Error>.update}

Updates the singleton resource.

```typespec
op TypeSpec.Rest.Resource.SingletonResourceOperations<Singleton, Resource, Error>.update(properties: TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel<Resource>): Singleton | Error
```

### `SingletonResourceRead` {#TypeSpec.Rest.Resource.SingletonResourceRead}

Singleton resource read operation template.

```typespec
interface TypeSpec.Rest.Resource.SingletonResourceRead<Singleton, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Singleton | The singleton resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `SingletonResourceRead.get` {#TypeSpec.Rest.Resource.SingletonResourceRead<Singleton, Resource, Error>.get}

Gets the singleton resource.

```typespec
op TypeSpec.Rest.Resource.SingletonResourceRead<Singleton, Resource, Error>.get(): Singleton | Error
```

### `SingletonResourceUpdate` {#TypeSpec.Rest.Resource.SingletonResourceUpdate}

Singleton resource update operation template.

```typespec
interface TypeSpec.Rest.Resource.SingletonResourceUpdate<Singleton, Resource, Error>
```

#### Template Parameters

| Name      | Description                   |
| --------- | ----------------------------- |
| Singleton | The singleton resource model. |
| Resource  | The resource model.           |
| Error     | The error response.           |

#### `SingletonResourceUpdate.update` {#TypeSpec.Rest.Resource.SingletonResourceUpdate<Singleton, Resource, Error>.update}

Updates the singleton resource.

```typespec
op TypeSpec.Rest.Resource.SingletonResourceUpdate<Singleton, Resource, Error>.update(properties: TypeSpec.Rest.Resource.ResourceCreateOrUpdateModel<Resource>): Singleton | Error
```

# Resource and routes

Defining REST resources and endpoints

Resources are operations that are grouped in a namespace. You declare such a namespace by adding the `@route` decorator to provide the path to that resource:

```typespec
using Http;

@route("/pets")
namespace Pets {

}
```

To define an operation on this resource, you need to provide the HTTP verb for the route using the `@get`, `@head` `@post`, `@put`, `@patch`, or `@delete` decorators. If an HTTP method decorator is not specified then the default is post if there is a body and get otherwise. Lets add an operation to our `Pets` resource:

```typespec
@route("/pets")
namespace Pets {
  op list(): Pet[];

  // or you could also use
  @get op listPets(): Pet[];
}
```

If `@route` is applied to an interface, that route is not "portable". It will be applied to that interface but will not carry over if another interface extends it.

```typespec
// Operations prepended with /pets
@route("/pets")
interface PetOps {
  list(): Pet[]
}

// Operations will *not* be prepended with /pets
interface MyPetOps extends PetOps {
  ...
}
```

### Automatic route generation

Instead of manually specifying routes using the `@route` decorator, you automatically generate routes from operation parameters by applying the `@autoRoute` decorator to an operation or interface containing operations.

For this to work, an operation's path parameters (those marked with `@path`) must also be marked with
the `@segment` decorator to define the preceding path segment.

This is especially useful when reusing common parameter sets defined as model types.

For example:

```typespec
model CommonParameters {
  @path
  @segment("tenants")
  tenantId: string;

  @path
  @segment("users")
  userName: string;
}

@autoRoute
interface UserOperations {
  @get
  getUser(...CommonParameters): User | Error;

  @put
  updateUser(...CommonParameters, user: User): User | Error;
}
```

This will result in the following route for both operations

```text
/tenants/{tenantId}/users/{userName}
```

If `@autoRoute` is applied to an interface, it is not "portable". It will be applied to that interface but will not carry over if another interface extends it.

```typespec
// Operations prepended with /pets
@autoRoute
interface PetOps {
  action(@path @segment("pets") id: string): void;
}

// Operations will *not* be prepended with /pets
interface MyPetOps extends PetOps {
  ...
}
```

### Customizing Automatic Route Generation

Instead of manually specifying routes using the `@route` decorator, you automatically generate
routes from operation parameters by applying the `@autoRoute` decorator to an operation, namespace,
or interface containing operations.

# Data types

Data types exported by @typespec/streams

## TypeSpec.Streams

### `Stream` {#TypeSpec.Streams.Stream}

Defines a model that represents a stream protocol type whose data is described
by `Type`.

This can be useful when the underlying data type is not relevant, or to serve as
a base type for custom streams.

```typespec
model TypeSpec.Streams.Stream<Type>
```

#### Template Parameters

| Name | Description                    |
| ---- | ------------------------------ |
| Type | The type of the stream's data. |

#### Properties

None

# Decorators

Decorators exported by @typespec/streams

## TypeSpec.Streams

### `@streamOf` {#@TypeSpec.Streams.streamOf}

Specify that a model represents a stream protocol type whose data is described
by `Type`.

```typespec
@TypeSpec.Streams.streamOf(type: unknown)
```

#### Target

`Model`

#### Parameters

| Name | Type      | Description                                             |
| ---- | --------- | ------------------------------------------------------- |
| type | `unknown` | The type that models the underlying data of the stream. |

#### Examples

```typespec
model Message {
  id: string;
  text: string;
}

@streamOf(Message)
model Response {
  @body body: string;
}
```

# Tutorial

Guide to versioning APIs authored in TypeSpec

## Implementing versioned APIs

The primary role of the TypeSpec.Versioning library is to enable API versioning. Let's start with an API that lacks versioning.

```typespec
@service(#{ title: "Contoso Widget Manager" })
namespace Contoso.WidgetManager;
```

To introduce versioning to this API, we need to use the `@versioned` decorator on the namespace and define an enum that outlines the supported versions.

```typespec
@service(#{ title: "Contoso Widget Manager" })
@versioned(Contoso.WidgetManager.Versions)
namespace Contoso.WidgetManager;

enum Versions {
  v1,
}
```

## Declaring versioned dependencies

Both versioned and unversioned services can declare their dependencies on versioned TypeSpec libraries. This is achieved using the `@useDependency` decorator. For unversioned services, this is declared on the namespace. For versioned services, it's declared on the versioned enum.

For example, if our unversioned WidgetManager service depends on the Azure.Core library, we would declare it like this:

```typespec
@service(#{ title: "Contoso Widget Manager Unversioned" })
@useDependency(Azure.Core.v1_0_Preview_1)
namespace Contoso.WidgetManager.Unversioned;
```

If our versioned WidgetManager service depends on the Azure.Core library, we would declare it like this:

```typespec
@service(#{ title: "Contoso Widget Manager" })
@versioned(Contoso.WidgetManager.Versions)
namespace Contoso.WidgetManager;

enum Versions {
  @useDependency(Azure.Core.v1_0_Preview_1)
  v1,
}
```

Let's say we introduce a new version to our service, and it uses features from a newer version of the Azure.Core library. We can declare that dependency like this:

```typespec
@service(#{ title: "Contoso Widget Manager" })
@versioned(Contoso.WidgetManager.Versions)
namespace Contoso.WidgetManager;

enum Versions {
  @useDependency(Azure.Core.v1_0_Preview_1)
  v1,

  @useDependency(Azure.Core.v1_0_Preview_2)
  v2,
}
```

## Versioning APIs

The versioning library simplifies the process of versioning APIs. Let's start with a basic example. Assume we have a service with a single API that returns a list of widgets. We can define that API like this:

```typespec
using Versioning;
using Rest;
using Http;

@service(#{ title: "Contoso Widget Manager" })
@versioned(Contoso.WidgetManager.Versions)
namespace Contoso.WidgetManager;

enum Versions {
  v1,
}

@error
model Error {
  code: string;
  message?: string;
}

model Widget {
  @key
  id: string;

  name: string;
}

op list(): Widget[] | Error;
```

Now, let's suppose that in version 2 of the service, we add a get operation to retrieve a single widget. We can add that like this:

```typespec
enum Versions {
  v1,
  v2,
}

model Widget {
  @key
  id: string;

  name: string;
}

@route("/widget")
op list(): Widget[] | Error;

@added(Versions.v2)
@route("/widget/{id}")
op get(...Resource.KeysOf<Widget>): Widget | Error;
```

Now, let's suppose that in version 3 of the service, we realize that `name` is not accurate and that this field should be called `description`. Also, we decide that the description should be optional, not mandatory. We can implement these changes like this:

```typespec
model Widget {
  @key
  widgetId: string;

  @renamedFrom(Versions.v3, "name")
  @madeOptional(Versions.v3)
  description?: string;
}
```

We made the change to the actual model property so that it now reflects the correct name and optional nature of the property. Both the `@renamedFrom` and `@madeOptional` decorators indicate the version in which the change was made, and the `@renamedFrom` decorator also identifies the previous name of the property. This allows us to generate code that is aware of the change and can handle it appropriately.

The OpenAPI definition of `Widget` for version 3 reflects the change:

```yaml
Widget:
  type: object
  properties:
    id:
      type: string
    description:
      type: string
  required:
    - id
```

However, the OpenAPI definition for versions 1 and 2 still reflect the original name and the mandatory nature of the property:

```yaml
Widget:
  type: object
  properties:
    id:
      type: string
    name:
      type: string
  required:
    - id
    - name
```

This is a common pattern with the versioning decorators. The TypeSpec should represent the _current state_ of the API. The decorators indicate the version at which this definition became accurate and, depending on the decorator, the other parameters reflect the previous values to retain that information.

# Decorators

Decorators exported by @typespec/versioning

## TypeSpec.Versioning

### `@added` {#@TypeSpec.Versioning.added}

Identifies when the target was added.

```typespec
@TypeSpec.Versioning.added(version: EnumMember)
```

#### Target

`Model | ModelProperty | Operation | Enum | EnumMember | Union | UnionVariant | Scalar | Interface`

#### Parameters

| Name    | Type         | Description                               |
| ------- | ------------ | ----------------------------------------- |
| version | `EnumMember` | The version that the target was added in. |

#### Examples

```tsp
@added(Versions.v2)
op addedInV2(): void;

@added(Versions.v2)
model AlsoAddedInV2 {}

model Foo {
  name: string;

  @added(Versions.v3)
  addedInV3: string;
}
```

### `@madeOptional` {#@TypeSpec.Versioning.madeOptional}

Identifies when a target was made optional.

```typespec
@TypeSpec.Versioning.madeOptional(version: EnumMember)
```

#### Target

`ModelProperty`

#### Parameters

| Name    | Type         | Description                                       |
| ------- | ------------ | ------------------------------------------------- |
| version | `EnumMember` | The version that the target was made optional in. |

#### Examples

```tsp
model Foo {
  name: string;

  @madeOptional(Versions.v2)
  nickname?: string;
}
```

### `@madeRequired` {#@TypeSpec.Versioning.madeRequired}

Identifies when a target was made required.

```typespec
@TypeSpec.Versioning.madeRequired(version: EnumMember)
```

#### Target

`ModelProperty`

#### Parameters

| Name    | Type         | Description                                       |
| ------- | ------------ | ------------------------------------------------- |
| version | `EnumMember` | The version that the target was made required in. |

#### Examples

```tsp
model Foo {
  name: string;

  @madeRequired(Versions.v2)
  nickname: string;
}
```

### `@removed` {#@TypeSpec.Versioning.removed}

Identifies when the target was removed.

```typespec
@TypeSpec.Versioning.removed(version: EnumMember)
```

#### Target

`Model | ModelProperty | Operation | Enum | EnumMember | Union | UnionVariant | Scalar | Interface`

#### Parameters

| Name    | Type         | Description                                 |
| ------- | ------------ | ------------------------------------------- |
| version | `EnumMember` | The version that the target was removed in. |

#### Examples

```tsp
@removed(Versions.v2)
op removedInV2(): void;

@removed(Versions.v2)
model AlsoRemovedInV2 {}

model Foo {
  name: string;

  @removed(Versions.v3)
  removedInV3: string;
}
```

### `@renamedFrom` {#@TypeSpec.Versioning.renamedFrom}

Identifies when the target has been renamed.

```typespec
@TypeSpec.Versioning.renamedFrom(version: EnumMember, oldName: valueof string)
```

#### Target

`Model | ModelProperty | Operation | Enum | EnumMember | Union | UnionVariant | Scalar | Interface`

#### Parameters

| Name    | Type             | Description                                 |
| ------- | ---------------- | ------------------------------------------- |
| version | `EnumMember`     | The version that the target was renamed in. |
| oldName | `valueof string` | The previous name of the target.            |

#### Examples

```tsp
@renamedFrom(Versions.v2, "oldName")
op newName(): void;
```

### `@returnTypeChangedFrom` {#@TypeSpec.Versioning.returnTypeChangedFrom}

Declares that the return type of an operation has changed starting at a given version,
while keeping earlier versions consistent with the previous return type.

This decorator is used to track return type changes across API versions. When applied,
the operation will return `oldType` in versions before the specified `version`,
and the current return type definition in the specified version and later.

```typespec
@TypeSpec.Versioning.returnTypeChangedFrom(version: EnumMember, oldType: unknown)
```

#### Target

`Operation`

#### Parameters

| Name    | Type         | Description                                                                                                                                                              |
| ------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| version | `EnumMember` | The version when the return type change takes effect. The new return type applies<br />from this version onwards, while the old return type applies to earlier versions. |
| oldType | `unknown`    | The previous return type used before the specified version.                                                                                                              |

#### Examples

```tsp
// In v1: returns a string
// In v2+: returns an int32
@returnTypeChangedFrom(Versions.v2, string)
op getUserId(): int32;
```

### `@typeChangedFrom` {#@TypeSpec.Versioning.typeChangedFrom}

Declares that the type of a model property has changed starting at a given version,
while keeping earlier versions consistent with the previous type.

This decorator is used to track type changes across API versions. When applied,
the property will use `oldType` in versions before the specified `version`,
and the current type definition in the specified version and later.

```typespec
@TypeSpec.Versioning.typeChangedFrom(version: EnumMember, oldType: unknown)
```

#### Target

`ModelProperty`

#### Parameters

| Name    | Type         | Description                                                                                                                                         |
| ------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| version | `EnumMember` | The version when the type change takes effect. The new type applies<br />from this version onwards, while the old type applies to earlier versions. |
| oldType | `unknown`    | The previous type used before the specified version.                                                                                                |

#### Examples

```tsp
model Foo {
  // In v1: id is a string
  // In v2+: id is an int32
  @typeChangedFrom(Versions.v2, string)
  id: int32;
}
```

### `@useDependency` {#@TypeSpec.Versioning.useDependency}

Identifies that a namespace or a given versioning enum member relies upon a versioned package.

```typespec
@TypeSpec.Versioning.useDependency(...versionRecords: EnumMember[])
```

#### Target

`EnumMember | Namespace`

#### Parameters

| Name           | Type           | Description                                                           |
| -------------- | -------------- | --------------------------------------------------------------------- |
| versionRecords | `EnumMember[]` | The dependent library version(s) for the target namespace or version. |

#### Examples

##### Select a single version of `MyLib` to use

```tsp
@useDependency(MyLib.Versions.v1_1)
namespace NonVersionedService;
```

##### Select which version of the library match to which version of the service.

```tsp
@versioned(Versions)
namespace MyService1;
enum Version {
  @useDependency(MyLib.Versions.v1_1) // V1 use lib v1_1
  v1,
  @useDependency(MyLib.Versions.v1_1) // V2 use lib v1_1
  v2,
  @useDependency(MyLib.Versions.v2) // V3 use lib v2
  v3,
}
```

### `@versioned` {#@TypeSpec.Versioning.versioned}

Identifies that the decorated namespace is versioned by the provided enum.

```typespec
@TypeSpec.Versioning.versioned(versions: Enum)
```

#### Target

`Namespace`

#### Parameters

| Name     | Type   | Description                                     |
| -------- | ------ | ----------------------------------------------- |
| versions | `Enum` | The enum that describes the supported versions. |

#### Examples

```tsp
@versioned(Versions)
namespace MyService;
enum Versions {
  v1,
  v2,
  v3,
}
```

# Discriminated Types

Standard library reference to describing discriminated types

TypeSpec allows for the expression of unions and inheritance. However, when transmitting types over the network, many languages require a mechanism to distinguish between different union variants or models within an inheritance hierarchy.

### Implementing Discriminated Unions

Unions can be marked as discriminated using the `@discriminated` decorator. This discriminator will assume the variant name is the discriminator value.

#### Default serialization

```typespec
@discriminated
union Pet {
  cat: Cat,
  dog: Dog,
}
```

Serialize as

```json
{
  "kind": "cat",
  "value": {
    "name": "Whiskers",
    "meow": true
  }
}
// or
{
  "kind": "dog",
  "value": {
    "name": "Rex",
    "bark": false
  }
}
```

#### Customize properties names

```typespec
@discriminated(#{ discriminatorPropertyName: "dataKind", envelopePropertyName: "data" })
union Pet {
  cat: Cat,
  dog: Dog,
}

model Cat {
  name: string;
  meow: int32;
}

model Dog {
  name: string;
  bark: string;
}
```

serialize as

```json
{
  "dataKind": "cat",
  "data": {
    "name": "Whiskers",
    "meow": true
  }
}
// or
{
  "dataKind": "dog",
  "data": {
    "name": "Rex",
    "bark": false
  }
}
```

### Inject discriminator inline

```tsp
@discriminated(#{ envelope: "none" })
union Pet {
  cat: Cat,
  dog: Dog,
}

model Cat {
  name: string;
  meow: boolean;
}

model Dog {
  name: string;
  bark: boolean;
}
```

serialize as

```json
{
  "kind": "cat",
  "name": "Whiskers",
  "meow": true
}
// or
{
  "kind": "dog",
  "name": "Rex",
  "bark": false
}
```

### Implementing Polymorphism

#### `string` Discriminator

```typespec
@discriminator("kind")
model Pet {
  name: string;
  weight?: float32;
}
model Cat extends Pet {
  kind: "cat";
  meow: int32;
}
model Dog extends Pet {
  kind: "dog";
  bark: string;
}
```

#### `enum` Discriminator

```typespec
enum PetKind {
  cat,
  dog,
}

@discriminator("kind")
model Pet {
  kind: PetKind;
  name: string;
  weight?: float32;
}
model Cat extends Pet {
  kind: PetKind.cat;
  meow: int32;
}
model Dog extends Pet {
  kind: PetKind.dog;
  bark: string;
}
```

#### Nested Discriminator

```tsp
@discriminator("kind")
model Pet {
  kind: string;
  name: string;
  weight?: float32;
}

@discriminator("breed")
model Cat extends Pet {
  kind: "cat";
  breed: string;
  meow: int32;
}

@discriminator("breed")
model Siamese extends Cat {
  breed: "siamese";
}

@discriminator("breed")
model Bengal extends Cat {
  breed: "bengal";
}

model Dog extends Pet {
  kind: "dog";
  bark: string;
}
```

# Encoded names

Standard library reference to encoding names sent over the wire

There is some cases where the name you have in TypeSpec might differ from the name over the wire or for a certain language.

## Update name for a given target

To update the name of a TypeSpec entity you can use the `@encodedName` decorator. This decorator takes 2 parameters:

| Parameter     | Type     | Description                                                                                                                                                                                                            |
| ------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mimeType`    | `string` | Mime type this should apply to. The mime type should be a known mime type as described here https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types without any suffix (e.g. `+json`) |
| `encodedName` | `string` | The name should be when serialized to the given mime type.                                                                                                                                                             |

Example:

```typespec
model Foo {
  // Specify that when serializing to JSON `expireAt` property should be named `exp`
  @encodedName("json", "exp")
  expireAt: string;
}
```

## Example

```typespec
model CertificateAttributes {
  @encodedName("application/json", "nbf")
  notBefore: int32;

  @encodedName("application/json", "exp")
  @encodedName("application/xml", "ExpireAt")
  expires: int32;

  created: int32;
  updated: int32;
}
```

<table>
<thead>
<tr>
<th>Json</th>
<th>Xml</th>
<th>Yaml</th>
</tr>
</thead>
<tr>
<td>When serialized to `application/json` properties will use the encodedName for `application/json` if available or default to the property name.</td>
<td>When serialized to `application/xml` properties will use the encodedName for `application/xml` if available or default to the property name.</td>
<td>Yaml didn't provide any different names so it will serialize using the property names.</td>
</tr>
<tr>
<td>

```json
{
  "nbf": 1430344421,
  "exp": 2208988799,
  "created": 1493938289,
  "updated": 1493938291
}
```

</td>
<td>

```xml
<CertificateAttributes>
  <notBefore>1430344421</notBefore>
  <ExpireAt>2208988799</ExpireAt>
  <created>1493938289</created>
  <updated>1493938291</updated>
</CertificateAttributes>
```

</td>

<td>

```yaml
notBefore: 1430344421
expires: 2208988799
created: 1493938289
updated: 1493938291
```

</td>
</tr>
</table>

## Use in library/emitter

To consume the value of `@encodedName` in your library or emitter you can use `resolveEncodedName(target: Type, mimeType: string): string` from the compiler.

```ts
import { resolveEncodedName } from "@typespec/compiler";

// Resolve the encoded name for the given property and mime type. If the property doesn't have a encoded name for the given mime type it will return the property name.
const encodedName = resolveEncodedName(property, "application/json");

// You can also pass a full http mime type and `resolveEncodedName` will automatically resolve it to the base mime type.
const encodedName = resolveEncodedName(property, "application/merge-patch+json");
```

# Examples

Standard library reference to defining API examples

TypeSpec provide 2 decorators `@example` and `@opExample` to provide some examples for the types and operations.
With those decorators the examples must be provided as TypeSpec values that should be assignable to the type or operation parameter/return types.

### Type Examples

To give an example for a type you can use the `@example` decorator. The decorator first argument is the example value it MUST be assignable to the type it is targetting.
Additionally a title and/or description can be provided in the options.

### Simple primitive types

```tsp
@example(#{ name: "Max", age: 3 })
model Pet {
  name: string;
  age: int32;
}
```

### Scalar types

For scalar types the value must be defined with the scalar constructor.
This allows emitters to render the example in the correct protocol following the encoding of those scalar and the values set by `@encode`.

```tsp
@example(#{
  id: "item-1",
  createdAt: plainDate.fromISO("2020-01-01T00:00:00Z"),
  timeout: duration.fromISO("PT1M"),
})
model Item {
  id: string;
  createdAt: utcDateTime;
  @encode("seconds", int32) timeout: duration;
}
```

### Provide title or description

```tsp
@example(#{ name: "Max", age: 3 }, #{ title: "Pet example", description: "Simple pet example" })
model Pet {
  name: string;
  age: int32;
}
```

### Multiple examples

```tsp
@example(#{ name: "Max", age: 3 }, #{ title: "Minimal examples", description: "Minimal examples" })
@example(
  #{ name: "Rex", age: 8, bark: true },
  #{ title: "With optional properties", description: "Example where the pet barks" }
)
model Pet {
  name: string;
  age: int32;
  bark?: boolean;
}
```

### Define typed examples using `const`

```tsp
const petExample: Pet = #{ name: "Max", age: 3 };

@example(petExample)
model Pet {
  name: string;
  age: int32;
}
```

## Operation examples

Operation example are provided with the `@opExample` decorator. Similar to the `@example` decorator the first argument is the example value however it takes both the `parameters` and `returnType` example.
The values passed to `parameters` MUST be assignable to the operation parameters and the value passed to `returnType` MUST be assignable to the operation return type.
Additionally a title and/or description can be provided in the options.

:::note
Operation example will not validate additional properties as the applicable parameters might depend on the protocol and applied visibility.
:::

### Simple operation parameters

```tsp
@opExample(#{ parameters: #{ name: "Max", age: 3 } })
op write(name: string, age: int32): void;
```

### Simple operation return types

```tsp
@opExample(#{ returnType: #{ name: "Max", age: 3 } })
op read(): {
  name: string;
  age: int32;
};
```

### Specify title and/or description

```tsp
@opExample(
  #{ parameters: #{ name: "Max", age: 3 } },
  #{ title: "Simple write example", description: "Write a pet" }
)
op write(name: string, age: int32): void;
```

# Pagination

Standard library reference to using built-in pagination patterns

TypeSpec provide built-in support for some of the common pagination pattern used.

Pagination can be categorized into two types:

- Client driven pagination: In this pattern, the client is responsible for managing the pagination state(figuring out the next page, previous page, etc).
- Server driven pagination: In this pattern the server gives the client information on how to navigate to the next, previous, first, last page, etc.

## Basics

To enable pagination for an operation the first step is to decorate it with the `@list` decorator and have the return type contain a property decorated with `@pageItems`

```tsp
@list op listPets(): {
  @pageItems pets: Pet[];
};
```

## Client driven pagination

For client driven pagination there are 3 decorators that can be used to annotate the operation parameters.

- `@pageSize`: Number of items to return per page.
- `@offset`: Number of items to skip
- `@pageIndex`: Page index.

`@offset` and `@pageIndex` are not necessary mutually exclusive but they are used to achieve the same goal.

### Example 1: Fixed page size and offset

```tsp
@list op listPets(@offset skip?: int32 = 0): {
  @pageItems pets: Pet[];
};
```

### Example 2: Custom page size and offset

```tsp
@list op listPets(@offset skip?: int32, @pageSize perPage?: int32 = 100): {
  @pageItems pets: Pet[];
};
```

### Example 2: Custom page size and page index

```tsp
@list op listPets(@pageIndex page?: int32 = 1, @pageSize perPage?: int32 = 100): {
  @pageItems pets: Pet[];
};
```

## Server driven pagination

For server driven pagination, the server returns information on how to navigate to other pages. There is 5 decorators that can be used to annotate the corersonding properties:

- `@nextLink`: Link to the next page.
- `@prevLink`: Link to the previous page.
- `@firstLink`: Link to the first page.
- `@lastLink`: Link to the last page.
- `@continuationToken`: Should be specified in both the parameters and return type of the operation. In the return type it is the token to navigate to the next page and in the parameters it mark which parameter to use to pass the next continuation token.

:::note
It is possible to use server driven pagination on top of client driven pagination.
:::

### Example 1: Using continuation token for an HTTP service

```tsp
@list op listPets(@query @continuationToken token?: string): {
  @pageItems pets: Pet[];
  @continuationToken nextToken?: string;
};
```

In this case, the body of the server response for a page has a property marked as continuation token, which can be used to fetch the next page. When fetching the next page, request will include the continuation token as a query parameter.

The continuation token can be in other locations as well, for instance, the below spec indicates that the server response for a page can have a header containing the continuation token. When fetching the next page, request will include the continuation token as a query parameter.

```tsp
@list op listPets(@query @continuationToken token?: string): {
  @pageItems pets: Pet[];
  @continuationToken @header nextToken?: string;
};
```

### Example 2: Using links for an HTTP service

```tsp
@list op listPets(): {
  @pageItems pets: Pet[];
  links: {
    @nextLink next?: url;
    @prevLink prev?: url;
    @firstLink first?: url;
    @lastLink last?: url;
  };
};
```

:::note
For HTTP services, `@nextLink` (and other link decorators like `@prevLink`, `@firstLink`, `@lastLink`) should be followed using a GET request by default. The link URIs are expected to be treated as opaque URLs that contain all necessary information to navigate to the respective page.
:::

### Example 3: Combining client and server driven pagination for an HTTP service

```tsp
@list op listPets(@query @pageIndex page?: int32 = 1, @query @pageSize perPage?: int32 = 100): {
  @pageItems pets: Pet[];

  // Links would return the url resolve with page and perPage set
  links: {
    @nextLink next?: url;
    @prevLink prev?: url;
    @firstLink first?: url;
    @lastLink last?: url;
  };
};
```

## Handling of additional parameters

A paged operation can offer additional parameters that are not used as paging control parameters like a filter parameter for example.
The expectation is those would be carried over to the next page requests with the exception of the link cases(next, prev, first and last links) where each protocol might have a different interpretation of what the link exactly represents. The link may encode parameters such as query parameters in HTTP. In such cases those parameters must be passed.

For example, HTTP links are expected to be opaque and contain all the necessary information for the next page URL. When following these links (such as `@nextLink`, `@prevLink`, `@firstLink`, `@lastLink`), clients should use a GET request by default. This means that query and path parameters are expected to already have been included in the link. On the other hand, any header parameters are expected to be resent in the next request as those cannot be represented in the link.

### Examples

#### Next link pagination in Http

```tsp
@route("pets")
@list
op listPets(
  @query filter?: string,
  @query expand?: string,
  @query @pageIndex page?: int32 = 1,
  @query @pageSize perPage?: int32 = 100,
  @header specialHeader?: "x-special-value",
): {
  @pageItems pets: Pet[];
  @nextLink next?: url;
};
```

```http
// First request
GET /pets?filter=dog
Special-Header: x-special-value

{"pets": [...], "nextLink": "/pets?filter=dog&page=2&perPage=100"}

---
// Second request
GET /pets?filter=dog&page=2&perPage=100
Special-Header: x-special-value

{"pets": [...], "nextLink": "/pets?filter=dog&page=3&perPage=100"}
```

#### Continuation token pagination in Http

```tsp
@route("pets")
@list
op listPets(
  @query filter?: string,
  @query expand?: string,
  @query @continuationToken token?: string,
  @header specialHeader?: "x-special-value",
): {
  @pageItems pets: Pet[];
  @continuationToken next?: url;
};
```

```http
// First request
GET /pets?filter=dog
Special-Header: x-special-value

{"pets": [...], "continuationToken": "token2"}

---
// Second request
GET /pets?filter=dog&token=token2
Special-Header: x-special-value

{"pets": [...], "continuationToken": "token3"}
```