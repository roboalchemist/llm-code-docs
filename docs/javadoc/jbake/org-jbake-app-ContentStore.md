Package org.jbake.app

# Class ContentStore

java.lang.Object
org.jbake.app.ContentStore

---

public class ContentStore
extends Object

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`protected class `
`ContentStore.Schema`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`ContentStore(String type,
 String name)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`addDocument(DocumentModel document)`
 
`void`
`close()`
 
`void`
`deleteAllByDocType(String docType)`
 
`void`
`deleteContent(String uri)`
 
`void`
`drop()`
 
`DocumentList<DocumentModel>`
`getAllContent(String docType)`
 
`DocumentList<DocumentModel>`
`getAllContent(String docType,
 boolean applyPaging)`
 
`Set<String>`
`getAllTags()`
 
`DocumentList<DocumentModel>`
`getDocumentByUri(String uri)`
 
`long`
`getDocumentCount(String docType)`
 
`DocumentList<DocumentModel>`
`getDocumentStatus(String uri)`
 
`long`
`getLimit()`
 
`DocumentList<DocumentModel>`
`getPublishedContent(String docType)`
 
`long`
`getPublishedCount(String docType)`
 
`DocumentList<DocumentModel>`
`getPublishedDocumentsByTag(String tag)`
 
`DocumentList<DocumentModel>`
`getPublishedPages()`
 
`DocumentList<DocumentModel>`
`getPublishedPosts()`
 
`DocumentList<DocumentModel>`
`getPublishedPosts(boolean applyPaging)`
 
`DocumentList<DocumentModel>`
`getPublishedPostsByTag(String tag)`
 
`long`
`getStart()`
 
`Set<String>`
`getTags()`
 
`DocumentList<DocumentModel>`
`getUnrenderedContent()`
 
`boolean`
`isActive()`
 
`void`
`markContentAsRendered(DocumentModel document)`
 
`void`
`resetPagination()`
 
`void`
`setLimit(int limit)`
 
`void`
`setStart(int start)`
 
`void`
`shutdown()`
 
`void`
`startup()`
 
`void`
`updateAndClearCacheIfNeeded(boolean needed,
 File templateFolder)`
 
`final void`
`updateSchema()`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### ContentStore

public ContentStore(String type,
 String name)

- 

## Method Details

  - 

### startup

public void startup()

  - 

### getStart

public long getStart()

  - 

### setStart

public void setStart(int start)

  - 

### getLimit

public long getLimit()

  - 

### setLimit

public void setLimit(int limit)

  - 

### resetPagination

public void resetPagination()

  - 

### updateSchema

public final void updateSchema()

  - 

### close

public void close()

  - 

### shutdown

public void shutdown()

  - 

### drop

public void drop()

  - 

### getDocumentCount

public long getDocumentCount(String docType)

  - 

### getPublishedCount

public long getPublishedCount(String docType)

  - 

### getDocumentByUri

public DocumentList<DocumentModel> getDocumentByUri(String uri)

  - 

### getDocumentStatus

public DocumentList<DocumentModel> getDocumentStatus(String uri)

  - 

### getPublishedPosts

public DocumentList<DocumentModel> getPublishedPosts()

  - 

### getPublishedPosts

public DocumentList<DocumentModel> getPublishedPosts(boolean applyPaging)

  - 

### getPublishedPostsByTag

public DocumentList<DocumentModel> getPublishedPostsByTag(String tag)

  - 

### getPublishedDocumentsByTag

public DocumentList<DocumentModel> getPublishedDocumentsByTag(String tag)

  - 

### getPublishedPages

public DocumentList<DocumentModel> getPublishedPages()

  - 

### getPublishedContent

public DocumentList<DocumentModel> getPublishedContent(String docType)

  - 

### getAllContent

public DocumentList<DocumentModel> getAllContent(String docType)

  - 

### getAllContent

public DocumentList<DocumentModel> getAllContent(String docType,
 boolean applyPaging)

  - 

### getUnrenderedContent

public DocumentList<DocumentModel> getUnrenderedContent()

  - 

### deleteContent

public void deleteContent(String uri)

  - 

### markContentAsRendered

public void markContentAsRendered(DocumentModel document)

  - 

### deleteAllByDocType

public void deleteAllByDocType(String docType)

  - 

### getTags

public Set<String> getTags()

  - 

### getAllTags

public Set<String> getAllTags()

  - 

### updateAndClearCacheIfNeeded

public void updateAndClearCacheIfNeeded(boolean needed,
 File templateFolder)

  - 

### isActive

public boolean isActive()

  - 

### addDocument

public void addDocument(DocumentModel document)