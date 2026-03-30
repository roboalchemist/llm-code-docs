typebox::layout
# Struct Layout 
Source 

```
pub struct Layout {
    pub size: usize,
    pub align: usize,
    pub offsets: Vec<usize>,
}
```

## Fields§
§`size: usize`

Total size in bytes.
§`align: usize`

Alignment requirement in bytes.
§`offsets: Vec<usize>`

Field offsets for struct members.

## Implementations§