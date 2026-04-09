Package org.jbake.model

# Class DocumentModel

java.lang.Object
java.util.AbstractMap<K,V>
java.util.HashMap<String,Object>
org.jbake.model.BaseModel
org.jbake.model.DocumentModel

All Implemented Interfaces:
`Serializable`, `Cloneable`, `Map<String,Object>`

---

public class DocumentModel
extends BaseModel

See Also:

- Serialized Form

- 

## Nested Class Summary

## Nested classes/interfaces inherited from class java.util.AbstractMap

`AbstractMap.SimpleEntry<K extends Object,V extends Object>, AbstractMap.SimpleImmutableEntry<K extends Object,V extends Object>`

## Nested classes/interfaces inherited from interface java.util.Map

`Map.Entry<K extends Object,V extends Object>`

- 

## Constructor Summary

Constructors

Constructor
Description
`DocumentModel()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static DocumentModel`
`createDefaultDocumentModel()`
 
`String`
`getBody()`
 
`Boolean`
`getCached()`
 
`Date`
`getDate()`
 
`String`
`getFile()`
 
`String`
`getNoExtensionUri()`
 
`Boolean`
`getRendered()`
 
`String`
`getRootPath()`
 
`String`
`getSha1()`
 
`String`
`getSourceuri()`
 
`String`
`getStatus()`
 
`String[]`
`getTags()`
 
`String`
`getTitle()`
 
`String`
`getType()`
 
`void`
`setBody(String body)`
 
`void`
`setCached(boolean cached)`
 
`void`
`setDate(Date date)`
 
`void`
`setFile(String path)`
 
`void`
`setNextContent(DocumentModel nextDocumentModel)`
 
`void`
`setNoExtensionUri(String noExtensionUri)`
 
`void`
`setPreviousContent(DocumentModel previousDocumentModel)`
 
`void`
`setRendered(boolean rendered)`
 
`void`
`setRootPath(String pathToRoot)`
 
`void`
`setSha1(String sha1)`
 
`void`
`setSourceUri(String uri)`
 
`void`
`setStatus(String status)`
 
`void`
`setTags(String[] tags)`
 
`void`
`setTitle(String title)`
 
`void`
`setType(String type)`
 

### Methods inherited from class org.jbake.model.BaseModel

`getUri, setName, setUri`

### Methods inherited from class java.util.HashMap

`clear, clone, compute, computeIfAbsent, computeIfPresent, containsKey, containsValue, entrySet, forEach, get, getOrDefault, isEmpty, keySet, merge, put, putAll, putIfAbsent, remove, remove, replace, replace, replaceAll, size, values`

### Methods inherited from class java.util.AbstractMap

`equals, hashCode, toString`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.util.Map

`equals, hashCode`

- 

## Constructor Details

  - 

### DocumentModel

public DocumentModel()

- 

## Method Details

  - 

### createDefaultDocumentModel

public static DocumentModel createDefaultDocumentModel()

  - 

### getBody

public String getBody()

  - 

### setBody

public void setBody(String body)

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

### setStatus

public void setStatus(String status)

  - 

### getType

public String getType()

  - 

### setType

public void setType(String type)

  - 

### getTags

public String[] getTags()

  - 

### setTags

public void setTags(String[] tags)

  - 

### getSha1

public String getSha1()

  - 

### setSha1

public void setSha1(String sha1)

  - 

### getSourceuri

public String getSourceuri()

  - 

### setSourceUri

public void setSourceUri(String uri)

  - 

### getRootPath

public String getRootPath()

  - 

### setRootPath

public void setRootPath(String pathToRoot)

  - 

### getRendered

public Boolean getRendered()

  - 

### setRendered

public void setRendered(boolean rendered)

  - 

### getFile

public String getFile()

  - 

### setFile

public void setFile(String path)

  - 

### getNoExtensionUri

public String getNoExtensionUri()

  - 

### setNoExtensionUri

public void setNoExtensionUri(String noExtensionUri)

  - 

### getTitle

public String getTitle()

  - 

### setTitle

public void setTitle(String title)

  - 

### getCached

public Boolean getCached()

  - 

### setCached

public void setCached(boolean cached)

  - 

### setNextContent

public void setNextContent(DocumentModel nextDocumentModel)

  - 

### setPreviousContent

public void setPreviousContent(DocumentModel previousDocumentModel)