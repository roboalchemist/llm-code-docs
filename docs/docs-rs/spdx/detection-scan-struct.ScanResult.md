spdx::detection::scan
# Struct ScanResult 
Source 

```
pub struct ScanResult<'a> {
    pub score: f32,
    pub license: Option<IdentifiedLicense<'a>>,
    pub containing: Vec<ContainedResult<'a>>,
}
```
Available on **crate feature `detection`** only.
## Fields§
§`score: f32`

The confidence of the match from 0.0 to 1.0.
§`license: Option<IdentifiedLicense<'a>>`

The identified license of the overall text, or None if nothing met the
confidence threshold.
§`containing: Vec<ContainedResult<'a>>`

Any licenses discovered inside the text, if `optimize` was enabled.

## Trait Implementations§