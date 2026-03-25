lopdf
# Struct Document 
Source 

```
pub struct Document {
    pub version: String,
    pub binary_mark: Vec<u8>,
    pub trailer: Dictionary,
    pub reference_table: Xref,
    pub objects: BTreeMap<ObjectId, Object>,
    pub max_id: u32,
    pub max_bookmark_id: u32,
    pub bookmarks: Vec<u32>,
    pub bookmark_table: HashMap<u32, Bookmark>,
    pub xref_start: usize,
    pub encryption_state: Option<EncryptionState>,
}
```

## Fields§
§`version: String`

The version of the PDF specification to which the file conforms.
§`binary_mark: Vec<u8>`

The binary mark important for PDF A/2,3 tells various software tools to classify
the file as containing 8-bit binary that should be preserved during processing
§`trailer: Dictionary`

The trailer gives the location of the cross-reference table and of certain special objects.
§`reference_table: Xref`

The cross-reference table contains locations of the indirect objects.
§`objects: BTreeMap<ObjectId, Object>`

The objects that make up the document contained in the file.
§`max_id: u32`

Current maximum object id within the document.
§`max_bookmark_id: u32`

Current maximum object id within Bookmarks.
§`bookmarks: Vec<u32>`

The bookmarks in the document. Render at the very end of document after renumbering objects.
§`bookmark_table: HashMap<u32, Bookmark>`

used to locate a stored Bookmark so children can be appended to it via its id. Otherwise we
need to do recursive lookups and returns on the bookmarks internal layout Vec
§`xref_start: usize`

The byte the cross-reference table starts at.
This value is only set during reading, but not when writing the file.
It is used to support incremental updates in PDFs.
Default value is `0`.
§`encryption_state: Option<EncryptionState>`

The encryption state stores the parameters that were used to decrypt this document if the
document has been decrypted.

## Implementations§