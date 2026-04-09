Module org.easymock
Package org.easymock

## Enum CaptureType

- java.lang.Object

- 

  - java.lang.Enum<CaptureType>

  - 

    - org.easymock.CaptureType

- 

All Implemented Interfaces:
`Serializable`, `Comparable<CaptureType>`

---

```
public enum CaptureType
extends Enum<CaptureType>
```

Defines how arguments will be captured by a `Capture` object.

Author:
Henri Tremblay
See Also:
`Capture`

- 

  - 

### Enum Constant Summary

Enum Constants 

Enum Constant
Description

`ALL`

Will capture, in order, the arguments of each matching calls.

`FIRST`

Will capture the argument of the first matching call.

`LAST`

Will capture the argument of the last matching call.

`NONE`

Do not capture anything.

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method
Description

`static CaptureType`
`valueOf​(String name)`

Returns the enum constant of this type with the specified name.

`static CaptureType[]`
`values()`

Returns an array containing the constants of this enum type, in
the order they are declared.

    - 

### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`

    - 

### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

- 

  - 

### Enum Constant Detail

    - 

#### NONE

```
public static final CaptureType NONE
```

Do not capture anything.

    - 

#### FIRST

```
public static final CaptureType FIRST
```

Will capture the argument of the first matching call.

    - 

#### LAST

```
public static final CaptureType LAST
```

Will capture the argument of the last matching call.

    - 

#### ALL

```
public static final CaptureType ALL
```

Will capture, in order, the arguments of each matching calls.

  - 

### Method Detail

    - 

#### values

```
public static CaptureType[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (CaptureType c : CaptureType.values())
    System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared

    - 

#### valueOf

```
public static CaptureType valueOf​(String name)
```

Returns the enum constant of this type with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this type.  (Extraneous whitespace characters are 
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`IllegalArgumentException` - if this enum type has no constant with the specified name
`NullPointerException` - if the argument is null