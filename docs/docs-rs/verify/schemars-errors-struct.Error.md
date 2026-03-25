verify::schemars::errors
# Struct Error 
Source 

```
pub struct Error<S: Span> {
    pub meta: Option<Box<Metadata>>,
    pub span: Option<S>,
    pub value: ErrorValue<S>,
}
```
Available on **crate feature `schemars`** only.
## Fields§
§`meta: Option<Box<Metadata>>`

Information about the schema that caused the validation
error.
§`span: Option<S>`

The span of the invalid value.
§`value: ErrorValue<S>`

The actual error details.

## Trait Implementations§