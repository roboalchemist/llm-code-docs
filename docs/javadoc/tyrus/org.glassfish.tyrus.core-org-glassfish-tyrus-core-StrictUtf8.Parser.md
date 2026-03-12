Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class StrictUtf8.Parser

java.lang.Object
org.glassfish.tyrus.core.StrictUtf8.Parser

Enclosing class:
`StrictUtf8`

---

public static class StrictUtf8.Parser
extends Object
Surrogate parsing support.  Charset implementations may use instances of this class to handle the details of
 parsing UTF-16 surrogate pairs.

-

## Constructor Summary

Constructors

Constructor
Description
`Parser()`

-

## Method Summary

Modifier and Type
Method
Description
`CoderResult`
`error()`

If the previous parse operation detected an error, return the object describing that error.

`int`
`parse(char c,
 char[] ia,
 int ip,
 int il)`

Parses a UCS-4 character from the given source buffer, handling surrogates.

`int`
`parse(char c,
 CharBuffer in)`

Parses a UCS-4 character from the given source buffer, handling surrogates.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### Parser

public Parser()

-

## Method Details

-

### error

public CoderResult error()
If the previous parse operation detected an error, return the object describing that error.

Returns:
object describing encountered parse error.

-

### parse

public int parse(char c,
 CharBuffer in)
Parses a UCS-4 character from the given source buffer, handling surrogates.

Parameters:
`c` - The first character
`in` - The source buffer, from which one more character will be consumed if c is a high surrogate
Returns:
Either a parsed UCS-4 character, in which case the isPair() and increment() methods will return
 meaningful values, or -1, in which case error() will return a descriptive result object

-

### parse

public int parse(char c,
 char[] ia,
 int ip,
 int il)
Parses a UCS-4 character from the given source buffer, handling surrogates.

Parameters:
`c` - The first character
`ia` - The input array, from which one more character will be consumed if c is a high surrogate
`ip` - The input index
`il` - The input limit
Returns:
Either a parsed UCS-4 character, in which case the isPair() and increment() methods will return
 meaningful values, or -1, in which case error() will return a descriptive result object
