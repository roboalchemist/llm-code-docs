Package org.jsoup

# Class UnsupportedMimeTypeException

java.lang.Object
java.lang.Throwable
java.lang.Exception
java.io.IOException
org.jsoup.UnsupportedMimeTypeException

All Implemented Interfaces:
`Serializable`

---

public class UnsupportedMimeTypeException
extends IOException
Signals that a HTTP response returned a mime type that is not supported.

See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`UnsupportedMimeTypeException(String message,
 String mimeType,
 String url)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`getMimeType()`
 
`String`
`getUrl()`
 
`String`
`toString()`
 

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### UnsupportedMimeTypeException

public UnsupportedMimeTypeException(String message,
 String mimeType,
 String url)

- 

## Method Details

  - 

### getMimeType

public String getMimeType()

  - 

### getUrl

public String getUrl()

  - 

### toString

public String toString()

Overrides:
`toString` in class `Throwable`