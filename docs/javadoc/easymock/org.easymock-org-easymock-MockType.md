Module org.easymock
Package org.easymock

## Enum MockType

- java.lang.Object

- 

  - java.lang.Enum<MockType>

  - 

    - org.easymock.MockType

- 

All Implemented Interfaces:
`Serializable`, `Comparable<MockType>`

---

```
public enum MockType
extends Enum<MockType>
```

Enum describing the 3 possibles kind of mocks

Since:
3.2
Author:
Henri Tremblay

- 

  - 

### Enum Constant Summary

Enum Constants 

Enum Constant
Description

`DEFAULT`

A default mock expects only recorded calls but in any order

`NICE`

A nice mock expects recorded calls in any order and returning null for other calls

`STRICT`

A strict mock expects only recorded calls and they should be replayed in their recorded order

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method
Description

`static MockType`
`valueOf​(String name)`

Returns the enum constant of this type with the specified name.

`static MockType[]`
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

#### NICE

```
public static final MockType NICE
```

A nice mock expects recorded calls in any order and returning null for other calls

    - 

#### DEFAULT

```
public static final MockType DEFAULT
```

A default mock expects only recorded calls but in any order

    - 

#### STRICT

```
public static final MockType STRICT
```

A strict mock expects only recorded calls and they should be replayed in their recorded order

  - 

### Method Detail

    - 

#### values

```
public static MockType[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (MockType c : MockType.values())
    System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared

    - 

#### valueOf

```
public static MockType valueOf​(String name)
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