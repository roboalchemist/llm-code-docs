Package org.jbake.model

# Class DocumentTypes

java.lang.Object
org.jbake.model.DocumentTypes

---

public class DocumentTypes
extends Object

Utility class used to determine the list of document types. Currently only supports "page", "post", "index",
 "archive" and "feed".
 

Additional document types are added at runtime based on the types found in the configuration.

- 

## Method Summary

Modifier and Type
Method
Description
`static void`
`addDocumentType(String docType)`
 
`static void`
`addListener(DocumentTypeListener listener)`
 
`static boolean`
`contains(String documentType)`
 
`static String[]`
`getDocumentTypes()`

Notice additional document types are added automagically before returning them

`static void`
`resetDocumentTypes()`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### resetDocumentTypes

public static void resetDocumentTypes()

  - 

### addDocumentType

public static void addDocumentType(String docType)

  - 

### addListener

public static void addListener(DocumentTypeListener listener)

  - 

### getDocumentTypes

public static String[] getDocumentTypes()
Notice additional document types are added automagically before returning them

Returns:
all supported document types

  - 

### contains

public static boolean contains(String documentType)