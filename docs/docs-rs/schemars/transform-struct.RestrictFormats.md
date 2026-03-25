schemars::transform

# Struct RestrictFormats

Source

```
#[non_exhaustive]pub struct RestrictFormats {
    pub infer_from_meta_schema: bool,
    pub allowed_formats: BTreeSet<Cow<'static, str>>,
}
```

## Fields (Non-exhaustive)§

§`infer_from_meta_schema: bool`

Whether to read the schema’s `$schema` property to determine which version of JSON Schema
is being used, and allow only formats defined in that standard. If this is `true` but the
JSON Schema version can’t be determined because `$schema` is missing or unknown, then no
`format` values will be removed.

If this is set to `false`, then only the formats explicitly included in
`allowed_formats` will be allowed.

By default, this is `true`.
§`allowed_formats: BTreeSet<Cow<'static, str>>`

Values of the `format` property in schemas that will always be allowed, regardless of the
inferred version of JSON Schema.

## Trait Implementations§
