Package org.jsoup.helper

# Class RequestAuthenticator.Context

java.lang.Object
org.jsoup.helper.RequestAuthenticator.Context

Enclosing interface:
RequestAuthenticator

---

public static class RequestAuthenticator.Context
extends Object
Provides details for the request, to determine the appropriate credentials to return.

- 

## Method Summary

Modifier and Type
Method
Description
`PasswordAuthentication`
`credentials(String username,
 String password)`

Helper method to return a PasswordAuthentication object.

`boolean`
`isProxy()`

Gets if the authentication request is for a proxy.

`boolean`
`isServer()`

Gets if the authentication request is for a server.

`String`
`realm()`

Get the realm of the authentication request.

`Authenticator.RequestorType`
`type()`

Get the requestor type: `PROXY` if a proxy is requesting
         authentication, or `SERVER` if the URL's server is requesting.

`URL`
`url()`

Get the URL that is being requested.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### url

public URL url()
Get the URL that is being requested.

Returns:
URL

  - 

### type

public Authenticator.RequestorType type()
Get the requestor type: `PROXY` if a proxy is requesting
         authentication, or `SERVER` if the URL's server is requesting.

Returns:
requestor type

  - 

### realm

public String realm()
Get the realm of the authentication request.

Returns:
realm of the authentication request

  - 

### isProxy

public boolean isProxy()
Gets if the authentication request is for a proxy.

Returns:
true if type==proxy.

  - 

### isServer

public boolean isServer()
Gets if the authentication request is for a server.

Returns:
true if type==server.

  - 

### credentials

public PasswordAuthentication credentials(String username,
 String password)
Helper method to return a PasswordAuthentication object.

Parameters:
`username` - username credential
`password` - password credential
Returns:
a constructed PasswordAuthentication