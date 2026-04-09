Package org.jbake.parser

# Class MarkdownEngine

java.lang.Object
org.jbake.parser.MarkupEngine
org.jbake.parser.MarkdownEngine

All Implemented Interfaces:
`ParserEngine`

---

public class MarkdownEngine
extends MarkupEngine
Renders documents in the Markdown format.

- 

## Constructor Summary

Constructors

Constructor
Description
`MarkdownEngine()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`processBody(ParserContext context)`

Processes the body of the document.

### Methods inherited from class org.jbake.parser.MarkupEngine

`parse, parse, processHeader, validate`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### MarkdownEngine

public MarkdownEngine()

- 

## Method Details

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