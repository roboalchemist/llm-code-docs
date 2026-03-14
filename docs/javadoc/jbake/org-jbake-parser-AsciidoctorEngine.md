Package org.jbake.parser

# Class AsciidoctorEngine

java.lang.Object
org.jbake.parser.MarkupEngine
org.jbake.parser.AsciidoctorEngine

All Implemented Interfaces:
`ParserEngine`

---

public class AsciidoctorEngine
extends MarkupEngine
Renders documents in the asciidoc format using the Asciidoctor engine.

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`JBAKE_PREFIX`
 
`static final String`
`REVDATE_KEY`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`AsciidoctorEngine()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`processBody(ParserContext context)`

Processes the body of the document.

`void`
`processHeader(ParserContext context)`

Processes the document header.

### Methods inherited from class org.jbake.parser.MarkupEngine

`parse, parse, validate`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### JBAKE_PREFIX

public static final String JBAKE_PREFIX

See Also:

    - Constant Field Values

  - 

### REVDATE_KEY

public static final String REVDATE_KEY

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### AsciidoctorEngine

public AsciidoctorEngine()

- 

## Method Details

  - 

### processHeader

public void processHeader(ParserContext context)
Description copied from class: `MarkupEngine`
Processes the document header. Usually subclasses will parse the document body and look for
 specific header metadata and export it into `contents` map.

Overrides:
`processHeader` in class `MarkupEngine`
Parameters:
`context` - the parser context

  - 

### processBody

public void processBody(ParserContext context)
Description copied from class: `MarkupEngine`
Processes the body of the document. Usually subclasses will parse the document body and render
 it, exporting the result using the `ParserContext.setBody(String)` method.

Overrides:
`processBody` in class `MarkupEngine`
Parameters:
`context` - the parser context