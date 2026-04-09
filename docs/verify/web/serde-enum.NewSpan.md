verify::serde
# Enum NewSpan 
Source 

```
pub enum NewSpan<S: Span> {
    Add(Option<S>),
    Reset(Option<S>),
    NoChange,
}
```
Available on **crate feature `serde`** only.
## Variants§
§
### Add(Option<S>)