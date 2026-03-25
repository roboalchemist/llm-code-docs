spdx::detection
# Struct LicenseEntry 
Source 

```
pub struct LicenseEntry {
    pub original: TextData,
    pub aliases: Vec<String>,
    pub headers: Vec<TextData>,
    pub alternates: Vec<TextData>,
}
```
Available on **crate feature `detection`** only.
## Fields§
§`original: TextData`

The original license text
§`aliases: Vec<String>`

Set of license identifiers that are aliases (ie. same license text) as
this entry
§`headers: Vec<TextData>`

Set of headers that can be used to specify this license applies to a larger file
§`alternates: Vec<TextData>`

Similar license texts that will also be scored as this license if detected

## Implementations§