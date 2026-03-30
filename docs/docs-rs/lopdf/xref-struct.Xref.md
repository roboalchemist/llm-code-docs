lopdf::xref
# Struct Xref 
Source 

```
pub struct Xref {
    pub cross_reference_type: XrefType,
    pub entries: BTreeMap<u32, XrefEntry>,
    pub size: u32,
}
```

## Fields§
§`cross_reference_type: XrefType`

Type of Cross-Reference used in the last incremental version.
This method of cross-referencing will also be used when saving the file.
PDFs with Incremental Updates should alway use the same cross-reference type.
§`entries: BTreeMap<u32, XrefEntry>`

Entries for indirect object.
§`size: u32`

Total number of entries (including free entries), equal to the highest object number plus 1.

## Implementations§