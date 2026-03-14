# Crate schemars

Source

## Modules§

constsConstants associated with JSON Schema generation.generateJSON Schema generator and settings.transformContains the `Transform` trait, used to modify a constructed schema and optionally its subschemas.
This trait is automatically implemented for functions of the form `fn(&mut Schema) -> ()`.

## Macros§

json_schemaConstruct a `Schema` from a JSON literal. This can either be a JSON object, or
a boolean (`true` or `false`).schema_forGenerates a `Schema` for the given type using default settings.
The default settings currently conform to JSON Schema 2020-12, but this is liable to change in a future version of Schemars if support for other JSON Schema versions is added.schema_for_valueGenerates a `Schema` for the given example value using default settings.
The default settings currently conform to JSON Schema 2020-12, but this is liable to change in a future version of Schemars if support for other JSON Schema versions is added.

## Structs§

SchemaA JSON Schema.SchemaGeneratorThe main type used to generate JSON Schemas.

## Traits§

JsonSchemaA type which can be described as a JSON Schema document.

## Derive Macros§

JsonSchemaDerive macro for `JsonSchema` trait.JsonSchema_repr
