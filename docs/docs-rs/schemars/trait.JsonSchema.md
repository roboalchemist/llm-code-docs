schemars

# Trait JsonSchema

Source

```
pub trait JsonSchema {
    // Required methods
    fn schema_name() -> Cow<'static, str>;
    fn json_schema(generator: &mut SchemaGenerator) -> Schema;

    // Provided methods
    fn inline_schema() -> bool { ... }
    fn schema_id() -> Cow<'static, str> { ... }
}
```

## Required Methods§
