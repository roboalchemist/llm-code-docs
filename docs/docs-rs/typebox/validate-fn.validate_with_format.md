typebox::validate
# Function validate_with_format 
Source 

```
pub fn validate_with_format(
    schema: &Schema,
    value: &Value,
    registry: Option<&SchemaRegistry>,
    formats: Option<&FormatRegistry>,
) -> Result<(), ValidationError>
```