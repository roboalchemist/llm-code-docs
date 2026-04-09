Package org.jbake.app

# Class Parser

java.lang.Object
org.jbake.app.Parser

---

public class Parser
extends Object
Parses a File for content.

- 

## Constructor Summary

Constructors

Constructor
Description
`Parser(JBakeConfiguration config)`

Creates a new instance of Parser.

- 

## Method Summary

Modifier and Type
Method
Description
`DocumentModel`
`processFile(File file)`

Process the file by parsing the contents.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### Parser

public Parser(JBakeConfiguration config)
Creates a new instance of Parser.

Parameters:
`config` - Project configuration

- 

## Method Details

  - 

### processFile

public DocumentModel processFile(File file)
Process the file by parsing the contents.

Parameters:
`file` - File input for parsing
Returns:
The contents of the file