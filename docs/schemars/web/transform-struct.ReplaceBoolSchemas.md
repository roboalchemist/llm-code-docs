schemars::transform

# Struct ReplaceBoolSchemas

Source

```
#[non_exhaustive]pub struct ReplaceBoolSchemas {
    pub skip_additional_properties: bool,
}
```

## Fields (Non-exhaustive)§

§`skip_additional_properties: bool`

When set to `true`, a schema’s `additionalProperties` property will not be changed from a
boolean.

Defaults to `false`.

## Trait Implementations§
