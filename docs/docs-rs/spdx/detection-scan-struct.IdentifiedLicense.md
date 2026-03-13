spdx::detection::scan
# Struct IdentifiedLicense 
Source 

```
pub struct IdentifiedLicense<'a> {
    pub name: &'a str,
    pub kind: LicenseType,
    pub data: &'a TextData,
}
```
Available on **crate feature `detection`** only.
## Fields§
§`name: &'a str`

The identifier of the license.
§`kind: LicenseType`

The type of the license that was matched.
§`data: &'a TextData`

A reference to the license data inside the store.

## Trait Implementations§