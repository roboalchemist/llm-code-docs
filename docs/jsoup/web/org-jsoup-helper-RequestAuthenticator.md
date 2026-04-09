Package org.jsoup.helper

# Interface RequestAuthenticator

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

@FunctionalInterface
public interface RequestAuthenticator
A `RequestAuthenticator` is used in `Connection` to authenticate if required to proxies and web
 servers. See `Connection.auth(RequestAuthenticator)`.

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Interface
Description
`static class `
`RequestAuthenticator.Context`

Provides details for the request, to determine the appropriate credentials to return.

- 

## Method Summary

Modifier and Type
Method
Description
`@Nullable PasswordAuthentication`
`authenticate(RequestAuthenticator.Context auth)`

Provide authentication credentials for the provided Request Context.

- 

## Method Details

  - 

### authenticate

@Nullable PasswordAuthentication authenticate(RequestAuthenticator.Context auth)
Provide authentication credentials for the provided Request Context.

Parameters:
`auth` - the request context including URL, type (Server or Proxy), and realm.
Returns:
credentials for the request. May return `null` if they are not applicable -- but the request will
 likely fail, as this method is only called if the request asked for authentication.