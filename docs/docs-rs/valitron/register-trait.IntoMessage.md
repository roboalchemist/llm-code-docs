valitron::register

# Trait IntoMessage

Source

```
pub trait IntoMessage {
    // Required method
    fn into_message(
        rule: &'static str,
        field: &FieldNames,
        value: &Value,
    ) -> Self;
}
```

## Required Methods§

Source

#### fn into_message(rule: &'static str, field: &FieldNames, value: &Value) -> Self
