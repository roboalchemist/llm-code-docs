Module org.easymock
Package org.easymock.internal

## Class Injection

- java.lang.Object

- 

  - org.easymock.internal.Injection

- 

---

```
public class Injection
extends Object
```

Described mock instance for injection.

Since:
3.3
Author:
Alistair Todd

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`Injection​(Object mock,
         Mock annotation)`

Create instance containing the given mock and annotation.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`Mock`
`getAnnotation()`

Gets the annotation describing this mock instance.

`Object`
`getMock()`

Gets the mock instance for this injection.

`String`
`getQualifier()`

Get the field name qualifier for this injection.

`boolean`
`isMatched()`

Is this injection matched by some injection target?

`void`
`setMatched()`

Change the status to indicate that this injection was matched to some target.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Injection

```
public Injection​(Object mock,
                 Mock annotation)
```

Create instance containing the given mock and annotation.

Parameters:
`mock` - a mock object instance
`annotation` - Mock annotation describing the mock

  - 

### Method Detail

    - 

#### getMock

```
public Object getMock()
```

Gets the mock instance for this injection.

Returns:
a mock object instance

    - 

#### getAnnotation

```
public Mock getAnnotation()
```

Gets the annotation describing this mock instance.

Returns:
annotation describing the mock instance

    - 

#### getQualifier

```
public String getQualifier()
```

Get the field name qualifier for this injection.

Returns:
the field name qualifier for this injection which may be empty string where not set.

    - 

#### setMatched

```
public void setMatched()
```

Change the status to indicate that this injection was matched to some target.

    - 

#### isMatched

```
public boolean isMatched()
```

Is this injection matched by some injection target?

Returns:
true if setMatched was called, indicating that a matching injection target was found