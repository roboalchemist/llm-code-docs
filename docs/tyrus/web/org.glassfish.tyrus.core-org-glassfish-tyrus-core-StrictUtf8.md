Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class StrictUtf8

java.lang.Object
java.nio.charset.Charset
org.glassfish.tyrus.core.StrictUtf8

All Implemented Interfaces:
`Comparable<Charset>`

---

public class StrictUtf8
extends Charset

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class`
`StrictUtf8.Parser`

Surrogate parsing support.

-

## Constructor Summary

Constructors

Constructor
Description
`StrictUtf8()`

-

## Method Summary

Modifier and Type
Method
Description
`boolean`
`contains(Charset cs)`

`CharsetDecoder`
`newDecoder()`

`CharsetEncoder`
`newEncoder()`

### Methods inherited from class java.nio.charset.Charset

`aliases, availableCharsets, canEncode, compareTo, decode, defaultCharset, displayName, displayName, encode, encode, equals, forName, forName, hashCode, isRegistered, isSupported, name, toString`

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

-

## Constructor Details

-

### StrictUtf8

public StrictUtf8()

-

## Method Details

-

### newDecoder

public CharsetDecoder newDecoder()

Specified by:
`newDecoder` in class `Charset`

-

### newEncoder

public CharsetEncoder newEncoder()

Specified by:
`newEncoder` in class `Charset`

-

### contains

public boolean contains(Charset cs)

Specified by:
`contains` in class `Charset`
