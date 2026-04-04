# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse.md.txt

# IncomingHttpResponse

public final class **IncomingHttpResponse** extends Object  
Contains information that describes an HTTP response received by the SDK.  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [IncomingHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse#IncomingHttpResponse(com.google.api.client.http.HttpResponse, java.lang.String))(HttpResponse response, String content) Creates an `IncomingHttpResponse` from a successful response and the content read from it.                                                                                                                               |
|   | [IncomingHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse#IncomingHttpResponse(com.google.api.client.http.HttpResponseException, com.google.api.client.http.HttpRequest))(HttpResponseException e, HttpRequest request) Creates an `IncomingHttpResponse` from an HTTP error response.                                                                                                                     |
|   | [IncomingHttpResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse#IncomingHttpResponse(com.google.api.client.http.HttpResponseException, com.google.firebase.OutgoingHttpRequest))(HttpResponseException e, [OutgoingHttpRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/OutgoingHttpRequest) request) Creates an `IncomingHttpResponse` from an HTTP error response. |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| String                                                                                                                         | [getContent](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse#getContent())() Returns the content of the response as a string.    |
| Map\<String, Object\>                                                                                                          | [getHeaders](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse#getHeaders())() Returns the headers set on the response.            |
| [OutgoingHttpRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/OutgoingHttpRequest) | [getRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse#getRequest())() Returns the request that resulted in this response. |
| int                                                                                                                            | [getStatusCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/IncomingHttpResponse#getStatusCode())() Returns the status code of the response.      |

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
**IncomingHttpResponse**
(HttpResponse response, String content)

Creates an `IncomingHttpResponse` from a successful response and the content read
from it. The caller is expected to read the content from the response, and handle any errors
that may occur while reading.  

##### Parameters

| response |     A successful response.      |
| content  | Content read from the response. |
|----------|---------------------------------|

#### public
**IncomingHttpResponse**
(HttpResponseException e, HttpRequest request)

Creates an `IncomingHttpResponse` from an HTTP error response.  

##### Parameters

|    e    | The exception representing the HTTP error response. |
| request |       The request that resulted in the error.       |
|---------|-----------------------------------------------------|

#### public
**IncomingHttpResponse**
(HttpResponseException e, [OutgoingHttpRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/OutgoingHttpRequest) request)

Creates an `IncomingHttpResponse` from an HTTP error response.  

##### Parameters

|    e    | The exception representing the HTTP error response. |
| request |       The request that resulted in the error.       |
|---------|-----------------------------------------------------|

## Public Methods

#### public String
**getContent**
()

Returns the content of the response as a string.  

##### Returns

- HTTP content or null.  

#### public Map\<String, Object\>
**getHeaders**
()

Returns the headers set on the response.  

##### Returns

- An immutable map of headers (possibly empty).  

#### public [OutgoingHttpRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/OutgoingHttpRequest)
**getRequest**
()

Returns the request that resulted in this response.  

##### Returns

- An HTTP request.  

#### public int
**getStatusCode**
()

Returns the status code of the response.  

##### Returns

- An HTTP status code (e.g. 500).