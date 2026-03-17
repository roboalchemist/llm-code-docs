lopdf
# Struct PdfMetadata 
Source 

```
pub struct PdfMetadata {
    pub title: Option<String>,
    pub author: Option<String>,
    pub subject: Option<String>,
    pub keywords: Option<String>,
    pub creator: Option<String>,
    pub producer: Option<String>,
    pub creation_date: Option<String>,
    pub modification_date: Option<String>,
    pub page_count: u32,
    pub version: String,
}
```

## Fields§
§`title: Option<String>`

Document title from Info dictionary
§`author: Option<String>`

Document author from Info dictionary
§`subject: Option<String>`

Document subject from Info dictionary
§`keywords: Option<String>`

Document keywords from Info dictionary
§`creator: Option<String>`

Application that created the document
§`producer: Option<String>`

Application that produced the document
§`creation_date: Option<String>`

Document creation date (PDF date format: D:YYYYMMDDHHmmSSOHH’mm’)
§`modification_date: Option<String>`

Document modification date (PDF date format: D:YYYYMMDDHHmmSSOHH’mm’)
§`page_count: u32`

Number of pages in the document
§`version: String`

PDF version

## Trait Implementations§