Package org.jbake.parser

# Class ParserContext

java.lang.Object
org.jbake.parser.ParserContext

---

public class ParserContext
extends Object

- 

## Constructor Summary

Constructors

Constructor
Description
`ParserContext(File file,
 List<String> fileLines,
 JBakeConfiguration config,
 boolean hasHeader)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`getBody()`
 
`JBakeConfiguration`
`getConfig()`
 
`Date`
`getDate()`
 
`DocumentModel`
`getDocumentModel()`
 
`File`
`getFile()`
 
`List<String>`
`getFileLines()`
 
`String`
`getStatus()`
 
`Object`
`getTags()`
 
`String`
`getType()`
 
`boolean`
`hasHeader()`
 
`void`
`setBody(String str)`
 
`void`
`setDate(Date date)`
 
`void`
`setDefaultStatus()`
 
`void`
`setDefaultType()`
 
`void`
`setTags(String[] tags)`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### ParserContext

public ParserContext(File file,
 List<String> fileLines,
 JBakeConfiguration config,
 boolean hasHeader)

- 

## Method Details

  - 

### getFile

public File getFile()

  - 

### getFileLines

public List<String> getFileLines()

  - 

### getConfig

public JBakeConfiguration getConfig()

  - 

### getDocumentModel

public DocumentModel getDocumentModel()

  - 

### hasHeader

public boolean hasHeader()

  - 

### getBody

public String getBody()

  - 

### setBody

public void setBody(String str)

  - 

### getDate

public Date getDate()

  - 

### setDate

public void setDate(Date date)

  - 

### getStatus

public String getStatus()

  - 

### setDefaultStatus

public void setDefaultStatus()

  - 

### getType

public String getType()

  - 

### setDefaultType

public void setDefaultType()

  - 

### getTags

public Object getTags()

  - 

### setTags

public void setTags(String[] tags)