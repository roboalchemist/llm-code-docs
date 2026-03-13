schemars::generate

# Struct SchemaSettings

Source

```
#[non_exhaustive]pub struct SchemaSettings {
    pub definitions_path: Cow<'static, str>,
    pub meta_schema: Option<Cow<'static, str>>,
    pub transforms: Vec<Box<dyn GenTransform>>,
    pub inline_subschemas: bool,
    pub contract: Contract,
    pub untagged_enum_variant_titles: bool,
}
```

## Fields (Non-exhaustive)§

§`definitions_path: Cow<'static, str>`

A JSON pointer to the expected location of referenceable subschemas within the resulting
root schema.

A single leading `#` and/or single trailing `/` are ignored.

Defaults to `"/$defs"`.
§`meta_schema: Option<Cow<'static, str>>`

The URI of the meta-schema describing the structure of the generated schemas.

Defaults to `meta_schemas::DRAFT2020_12` (`https://json-schema.org/draft/2020-12/schema`).
§`transforms: Vec<Box<dyn GenTransform>>`

A list of `Transform`s that get applied to generated root schemas.

Defaults to an empty vec (no transforms).
§`inline_subschemas: bool`

Inline all subschemas instead of using references.

Some references may still be generated in schemas for recursive types.

Defaults to `false`.
§`contract: Contract`

Whether the generated schemas should describe how types are serialized or *de*serialized.

Defaults to `Contract::Deserialize`.
§`untagged_enum_variant_titles: bool`

Whether to include enum variant names in their schema’s `title` when using the untagged
enum representation.

This setting is respected by `#[derive(JsonSchema)]` on enums, but manual implementations
of `JsonSchema` may ignore this setting.

Defaults to `false`.

## Implementations§
