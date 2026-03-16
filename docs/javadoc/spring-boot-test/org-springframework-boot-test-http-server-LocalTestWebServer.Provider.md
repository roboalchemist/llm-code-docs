# Interface LocalTestWebServer.Provider

Enclosing class:
`LocalTestWebServer`

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

@FunctionalInterface
public static interface LocalTestWebServer.Provider
Internal strategy used to provide the running `LocalTestWebServer`.
Implementations can be registered in `spring.factories` and may accept an
`ApplicationContext` constructor argument.

Since:
4.0.0

- 

## Method Summary

Modifier and Type
Method
Description
`@Nullable LocalTestWebServer`
`getLocalTestWebServer()`

Return the provided `LocalTestWebServer` or `null`.

- 

## Method Details

  - 

### getLocalTestWebServer

@Nullable LocalTestWebServer getLocalTestWebServer()
Return the provided `LocalTestWebServer` or `null`.

Returns:
the local test web server