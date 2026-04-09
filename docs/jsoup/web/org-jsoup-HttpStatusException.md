Package org.jsoup

# Class HttpStatusException

java.lang.Object
java.lang.Throwable
java.lang.Exception
java.io.IOException
org.jsoup.HttpStatusException

All Implemented Interfaces:
`Serializable`

---

public class HttpStatusException
extends IOException
Signals that a HTTP request resulted in a not OK HTTP response.

See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`HttpStatusException(String message,
 int statusCode,
 String url)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`int`
`getStatusCode()`
 
`String`
`getUrl()`
 

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### HttpStatusException

public HttpStatusException(String message,
 int statusCode,
 String url)

- 

## Method Details

  - 

### getStatusCode

public int getStatusCode()

  - 

### getUrl

public String getUrl()