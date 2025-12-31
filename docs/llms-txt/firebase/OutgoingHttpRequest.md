# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/OutgoingHttpRequest.md.txt

# OutgoingHttpRequest

public final class **OutgoingHttpRequest** extends Object  
Contains the information that describe an HTTP request made by the SDK.  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [OutgoingHttpRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/OutgoingHttpRequest#OutgoingHttpRequest(java.lang.String, java.lang.String))(String method, String url) Creates an `OutgoingHttpRequest` from the HTTP method and URL. |

### Public Method Summary

|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HttpContent           | [getContent](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/OutgoingHttpRequest#getContent())() Returns any content that was sent with the request. |
| Map\<String, Object\> | [getHeaders](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/OutgoingHttpRequest#getHeaders())() Returns the headers set on the request.             |
| String                | [getMethod](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/OutgoingHttpRequest#getMethod())() Returns the HTTP method of the request.               |
| String                | [getUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/OutgoingHttpRequest#getUrl())() Returns the URL of the request.                             |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Constructors

#### public
**OutgoingHttpRequest**
(String method, String url)

Creates an `OutgoingHttpRequest` from the HTTP method and URL.  

##### Parameters

| method |        HTTP method name.        |
|  url   | Target HTTP URL of the request. |
|--------|---------------------------------|

## Public Methods

#### public HttpContent
**getContent**
()

Returns any content that was sent with the request.  

##### Returns

- HTTP content or null.  

#### public Map\<String, Object\>
**getHeaders**
()

Returns the headers set on the request.  

##### Returns

- An immutable map of headers (possibly empty).  

#### public String
**getMethod**
()

Returns the HTTP method of the request.  

##### Returns

- An HTTP method string (e.g. GET).  

#### public String
**getUrl**
()

Returns the URL of the request.  

##### Returns

- An absolute HTTP URL.