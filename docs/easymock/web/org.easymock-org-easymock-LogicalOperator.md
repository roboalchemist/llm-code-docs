Module org.easymock
Package org.easymock

## Enum LogicalOperator

- java.lang.Object

- 

  - java.lang.Enum<LogicalOperator>

  - 

    - org.easymock.LogicalOperator

- 

All Implemented Interfaces:
`Serializable`, `Comparable<LogicalOperator>`

---

```
public enum LogicalOperator
extends Enum<LogicalOperator>
```

See `EasyMock.cmp(T, java.util.Comparator<? super T>, org.easymock.LogicalOperator)`

Author:
Henri Tremblay

- 

  - 

### Enum Constant Summary

Enum Constants 

Enum Constant
Description

`EQUAL`
 

`GREATER`
 

`GREATER_OR_EQUAL`
 

`LESS_OR_EQUAL`
 

`LESS_THAN`
 

  - 

### Method Summary

All Methods Static Methods Instance Methods Abstract Methods Concrete Methods 

Modifier and Type
Method
Description

`String`
`getSymbol()`
 

`abstract boolean`
`matchResult​(int result)`
 

`static LogicalOperator`
`valueOf​(String name)`

Returns the enum constant of this type with the specified name.

`static LogicalOperator[]`
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

#### LESS_THAN

```
public static final LogicalOperator LESS_THAN
```

    - 

#### LESS_OR_EQUAL

```
public static final LogicalOperator LESS_OR_EQUAL
```

    - 

#### EQUAL

```
public static final LogicalOperator EQUAL
```

    - 

#### GREATER_OR_EQUAL

```
public static final LogicalOperator GREATER_OR_EQUAL
```

    - 

#### GREATER

```
public static final LogicalOperator GREATER
```

  - 

### Method Detail

    - 

#### values

```
public static LogicalOperator[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (LogicalOperator c : LogicalOperator.values())
    System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared

    - 

#### valueOf

```
public static LogicalOperator valueOf​(String name)
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

    - 

#### getSymbol

```
public String getSymbol()
```

    - 

#### matchResult

```
public abstract boolean matchResult​(int result)
```