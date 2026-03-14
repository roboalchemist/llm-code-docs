Package org.jbake.parser

# Class ErrorEngine

java.lang.Object
org.jbake.parser.MarkupEngine
org.jbake.parser.ErrorEngine

All Implemented Interfaces:
`ParserEngine`

---

public class ErrorEngine
extends MarkupEngine
An internal rendering engine used to notify the user that the markup format he used requires an engine that couldn't
 be loaded.

- 

## Constructor Summary

Constructors

Constructor
Description
`ErrorEngine()`
 
`ErrorEngine(String name)`
 

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

## Constructor Details

  - 

### ErrorEngine

public ErrorEngine()

  - 

### ErrorEngine

public ErrorEngine(String name)

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