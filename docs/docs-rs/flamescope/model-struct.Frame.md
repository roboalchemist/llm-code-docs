flamescope::model
# Struct Frame 
Source 

```
pub struct Frame {
    pub name: Cow<'static, str>,
    pub file: Option<String>,
    pub line: Option<u32>,
    pub col: Option<u32>,
}
```

## Fields§
§`name: Cow<'static, str>`§`file: Option<String>`§`line: Option<u32>`§`col: Option<u32>`
## Implementations§