schemars::transform

# Struct AddNullable

Source

```
#[non_exhaustive]pub struct AddNullable {
    pub remove_null_type: bool,
    pub add_const_null: bool,
}
```

## Fields (Non-exhaustive)§

§`remove_null_type: bool`

When set to `true` (the default), `"null"` will also be removed from the schemas `type`.
§`add_const_null: bool`

When set to `true` (the default), a schema that has a type only allowing `null` will also
have the equivalent `"const": null` inserted.

## Trait Implementations§
