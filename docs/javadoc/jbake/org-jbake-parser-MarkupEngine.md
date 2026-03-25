Package org.jbake.parser

# Class MarkupEngine

java.lang.Object
org.jbake.parser.MarkupEngine

All Implemented Interfaces:
`ParserEngine`

Direct Known Subclasses:
`AsciidoctorEngine`, `ErrorEngine`, `MarkdownEngine`, `RawMarkupEngine`, `YamlEngine`

---

public abstract class MarkupEngine
extends Object
implements ParserEngine
Base class for markup engine wrappers. A markup engine is responsible for rendering
 markup in a source file and exporting the result into the `contents` map.
 

 This specific engine does nothing, meaning that the body is rendered as raw contents.

- 

## Constructor Summary

Constructors

Constructor
Description
`MarkupEngine()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`Map<String,Object>`
`parse(org.apache.commons.configuration2.Configuration config,
 File file,
 String contentPath)`
 
`DocumentModel`
`parse(JBakeConfiguration config,
 File file)`

Parse given file to extract as much infos as possible

`void`
`processBody(ParserContext context)`

Processes the body of the document.

`void`
`processHeader(ParserContext context)`

Processes the document header.

`boolean`
`validate(ParserContext context)`

Tests if this markup engine can process the document.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### MarkupEngine

public MarkupEngine()

- 

## Method Details

  - 

### validate

public boolean validate(ParserContext context)
Tests if this markup engine can process the document.

Parameters:
`context` - the parser context
Returns:
true if this markup engine has enough context to process this document. false otherwise

  - 

### processHeader

public void processHeader(ParserContext context)
Processes the document header. Usually subclasses will parse the document body and look for
 specific header metadata and export it into `contents` map.

Parameters:
`context` - the parser context

  - 

### processBody

public void processBody(ParserContext context)
Processes the body of the document. Usually subclasses will parse the document body and render
 it, exporting the result using the `ParserContext.setBody(String)` method.

Parameters:
`context` - the parser context

  - 

### parse

public Map<String,Object> parse(org.apache.commons.configuration2.Configuration config,
 File file,
 String contentPath)

Specified by:
`parse` in interface `ParserEngine`
Parameters:
`config` - The project configuration
`file` - The file to be parsed
`contentPath` - unknown
Returns:
A model representation of the given file

  - 

### parse

public DocumentModel parse(JBakeConfiguration config,
 File file)
Parse given file to extract as much infos as possible

Specified by:
`parse` in interface `ParserEngine`
Parameters:
`file` - file to process
`config` - The project configuration
Returns:
a map containing all infos. Returning null indicates an error, even if an exception would be better.