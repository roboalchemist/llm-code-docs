Module org.easymock
Package org.easymock.internal

## Class ErrorMessage

- java.lang.Object

- 

  - org.easymock.internal.ErrorMessage

- 

---

```
public class ErrorMessage
extends Object
```

The full content of an error message reporting to the user.

Author:
OFFIS, Tammo Freese

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`ErrorMessage​(boolean matching,
            String message,
            int actualCount)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`void`
`appendTo​(StringBuilder buffer,
        int matches)`

Add the error message to the buffer.

`int`
`getActualCount()`

How many time an expected invocation was actually invoked.

`String`
`getMessage()`

The actual invocation and its result.

`boolean`
`isMatching()`

If the actual invocation matched the expected invocation.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ErrorMessage

```
public ErrorMessage​(boolean matching,
                    String message,
                    int actualCount)
```

  - 

### Method Detail

    - 

#### isMatching

```
public boolean isMatching()
```

If the actual invocation matched the expected invocation. It will be used to write the final error message telling
 that some recording are matching but were already used.

Returns:
if the actual invocation matched the expected invocation

    - 

#### getMessage

```
public String getMessage()
```

The actual invocation and its result.

Returns:
the actual invocation and its result

    - 

#### getActualCount

```
public int getActualCount()
```

How many time an expected invocation was actually invoked.

Returns:
how many time an expected invocation was actually invoked

    - 

#### appendTo

```
public void appendTo​(StringBuilder buffer,
                     int matches)
```

Add the error message to the buffer.

Parameters:
`buffer` - the buffer to append to
`matches` - how many times an actual invocation matched expected invocation