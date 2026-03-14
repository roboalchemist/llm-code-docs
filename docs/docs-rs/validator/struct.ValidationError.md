validator
# Struct ValidationError 
Source 

```
pub struct ValidationError {
    pub code: Cow<'static, str>,
    pub message: Option<Cow<'static, str>>,
    pub params: HashMap<Cow<'static, str>, Value>,
}
```

## Fields§
§`code: Cow<'static, str>`§`message: Option<Cow<'static, str>>`§`params: HashMap<Cow<'static, str>, Value>`
## Implementations§