spdx::detection::scan
# Struct ContainedResult 
Source 

```
pub struct ContainedResult<'a> {
    pub score: f32,
    pub license: IdentifiedLicense<'a>,
    pub line_range: (usize, usize),
}
```
Available on **crate feature `detection`** only.
## Fields§
§`score: f32`

The confidence of the match within the line range from 0.0 to 1.0.
§`license: IdentifiedLicense<'a>`

The license identified in this portion of the text.
§`line_range: (usize, usize)`

A 0-indexed (inclusive, exclusive) range of line numbers identifying
where in the overall text a license was identified.

See `TextData.lines_view()` for more information.

## Trait Implementations§