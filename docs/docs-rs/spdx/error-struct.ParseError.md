spdx::error
# Struct ParseError 
Source 

```
pub struct ParseError {
    pub original: String,
    pub span: Range<usize>,
    pub reason: Reason,
}
```

## Fields§
§`original: String`

The string that was attempting to be parsed
§`span: Range<usize>`

The range of characters in the original string that result
in this error
§`reason: Reason`

The specific reason for the error

## Trait Implementations§