Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Interface TyrusConfiguration

---

public interface TyrusConfiguration
Inner Tyrus configuration properties holder object.

Since:
2.1

-

## Nested Class Summary

Nested Classes

Modifier and Type
Interface
Description
`static class`
`TyrusConfiguration.Builder`

-

## Field Summary

Fields

Modifier and Type
Field
Description
`static final TyrusConfiguration`
`EMPTY_CONFIGURATION`

-

## Method Summary

Modifier and Type
Method
Description
`Map<String,Object>`
`tyrusProperties()`

Get an immutable map of properties provided by

`Map<String,Object>`
`userProperties()`

Get a mutable copy of user properties first obtained by `EndpointConfig.getUserProperties()`.

-

## Field Details

-

### EMPTY_CONFIGURATION

static final TyrusConfiguration EMPTY_CONFIGURATION

-

## Method Details

-

### tyrusProperties

Map<String,Object> tyrusProperties()
Get an immutable map of properties provided by

Returns:
immutable property `Map` for optional Tyrus behavior

-

### userProperties

Map<String,Object> userProperties()
Get a mutable copy of user properties first obtained by `EndpointConfig.getUserProperties()`.

Returns:
a mutable `Map` of user properties.
