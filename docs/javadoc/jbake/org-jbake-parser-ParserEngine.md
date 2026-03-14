Package org.jbake.parser

# Interface ParserEngine

All Known Implementing Classes:
`AsciidoctorEngine`, `ErrorEngine`, `MarkdownEngine`, `MarkupEngine`, `RawMarkupEngine`, `YamlEngine`

---

public interface ParserEngine

- 

## Method Summary

Modifier and Type
Method
Description
`Map<String,Object>`
`parse(org.apache.commons.configuration2.Configuration config,
 File file,
 String contentPath)`

Deprecated.
use `parse(JBakeConfiguration, File)` instead

`DocumentModel`
`parse(JBakeConfiguration config,
 File file)`

Parse a given file and transform to a model representation used by `MarkdownEngine` implementations
 to render the file content.

- 

## Method Details

  - 

### parse

DocumentModel parse(JBakeConfiguration config,
 File file)
Parse a given file and transform to a model representation used by `MarkdownEngine` implementations
 to render the file content.

Parameters:
`config` - The project configuration
`file` - The file to be parsed
Returns:
A model representation of the given file

  - 

### parse

@Deprecated
Map<String,Object> parse(org.apache.commons.configuration2.Configuration config,
 File file,
 String contentPath)
Deprecated.
use `parse(JBakeConfiguration, File)` instead

Parameters:
`config` - The project configuration
`file` - The file to be parsed
`contentPath` - unknown
Returns:
A model representation of the given file