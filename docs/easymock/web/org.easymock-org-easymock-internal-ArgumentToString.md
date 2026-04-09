Module org.easymock
Package org.easymock.internal

## Class ArgumentToString

- java.lang.Object

- 

  - org.easymock.internal.ArgumentToString

- 

---

```
public final class ArgumentToString
extends Object
```

Utility class to convert method arguments to Strings

Author:
Henri Tremblay

- 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method
Description

`static void`
`appendArgument​(Object value,
              StringBuffer buffer)`
 

`static String`
`argumentsToString​(Object... arguments)`

Returns a string representation of the arguments.

`static String`
`argumentToString​(Object argument)`

Converts an argument to a String using
 `appendArgument(Object, StringBuffer)`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Method Detail

    - 

#### appendArgument

```
public static void appendArgument​(Object value,
                                  StringBuffer buffer)
```

    - 

#### argumentToString

```
public static String argumentToString​(Object argument)
```

Converts an argument to a String using
 `appendArgument(Object, StringBuffer)`

Parameters:
`argument` - the argument to convert to a String.
Returns:
a `String` representation of the argument.

    - 

#### argumentsToString

```
public static String argumentsToString​(Object... arguments)
```

Returns a string representation of the arguments. This convenience
 implementation calls `argumentToString(Object)` for every argument
 in the given array and returns the string representations of the
 arguments separated by commas.

Parameters:
`arguments` - the arguments to be used in the string representation.
Returns:
a string representation of the matcher.