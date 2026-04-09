Package org.jbake.parser

# Class YamlEngine

java.lang.Object
org.jbake.parser.MarkupEngine
org.jbake.parser.YamlEngine

All Implemented Interfaces:
`ParserEngine`

---

public class YamlEngine
extends MarkupEngine

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`JBAKE_PREFIX`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`YamlEngine()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`DocumentModel`
`parse(JBakeConfiguration config,
 File file)`

Parse given file to extract as much infos as possible

`void`
`processBody(ParserContext context)`

This method implements the contract allowing use of Yaml files as content files.

`void`
`processHeader(ParserContext context)`

This method implements the contract allowing use of Yaml files as content files

### Methods inherited from class org.jbake.parser.MarkupEngine

`parse, validate`

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

## Constructor Details

  - 

### YamlEngine

public YamlEngine()

- 

## Method Details

  - 

### parse

public DocumentModel parse(JBakeConfiguration config,
 File file)
Description copied from class: `MarkupEngine`
Parse given file to extract as much infos as possible

Specified by:
`parse` in interface `ParserEngine`
Overrides:
`parse` in class `MarkupEngine`
Parameters:
`config` - The project configuration
`file` - file to process
Returns:
a map containing all infos. Returning null indicates an error, even if an exception would be better.

  - 

### processHeader

public void processHeader(ParserContext context)
This method implements the contract allowing use of Yaml files as content files

Overrides:
`processHeader` in class `MarkupEngine`
Parameters:
`context` - the parser context

  - 

### processBody

public void processBody(ParserContext context)
This method implements the contract allowing use of Yaml files as content files. As such there is
 no body for Yaml files so this method just sets an empty String as the body.

Overrides:
`processBody` in class `MarkupEngine`
Parameters:
`context` - the parser context