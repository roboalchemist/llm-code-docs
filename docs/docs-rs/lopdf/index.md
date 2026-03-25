# Crate lopdf 
Source 
## Re-exports§
`pub use encryption::EncryptionState;``pub use encryption::EncryptionVersion;``pub use encryption::Permissions;`
## Modules§
contentencryptionfiltersxobjectxref
## Macros§
dictionary
## Structs§
BookmarkDestinationDictionaryDictionary object.DocumentA PDF document.FontDataThis struct represents the data of a font.
It contains information about the font’s bounding box, ascent, descent, cap height, italic angle, and stemV.
Reference: https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/pdfreference1.5_v6.pdfIncrementalDocumentObjectStreamObjectStreamBuilderObjectStreamConfigPdfMetadataPDF metadata extracted without loading the entire document.
This is useful for quickly getting basic information about large PDFs.ReaderSaveOptionsOptions for saving PDF documentsSaveOptionsBuilderBuilder for SaveOptionsStreamStream object
Warning - all streams must be indirect objects, while
the stream dictionary may be a direct objectToc
## Enums§
EncodingErrorObjectBasic PDF object types defined in an enum.OutlineStringFormatString objects can be written in two formats.
## Functions§
decode_text_stringDecodes a text string.
Depending on the BOM at the start of the string, a different encoding is chosen.
All encodings specified in PDF2.0 are supported (PDFDocEncoding, UTF-16BE,
and UTF-8).encode_utf8Encodes the given `str` to UTF-8. This method of encoding text strings
is first specified in PDF2.0 and reader support is still lacking
(notably, Adobe Acrobat Reader doesn’t support it at the time of writing).
Thus, using it is **NOT RECOMMENDED**.encode_utf16_beEncodes the given `str` to UTF-16BE.
The recommended way to encode text strings, as it supports all of
unicode and all major PDF readers support it.substrsubstringtext_stringCreates a text string.
If the input only contains ASCII characters, the string is encoded
in PDFDocEncoding, otherwise in UTF-16BE.
## Type Aliases§
ObjectIdObject identifier consists of two parts: object number and generation number.Result