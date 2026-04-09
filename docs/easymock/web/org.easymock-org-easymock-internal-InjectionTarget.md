Module org.easymock
Package org.easymock.internal

## Class InjectionTarget

- java.lang.Object

- 

  - org.easymock.internal.InjectionTarget

- 

---

```
public class InjectionTarget
extends Object
```

Applies an `Injection` to a target field.

Since:
3.3
Author:
Henri Tremblay, Alistair Todd

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`InjectionTarget​(Field f)`

Create instance for injection to the given field.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`boolean`
`accepts​(Injection injection)`

Can the given Injection be applied to this InjectionTarget?

`Field`
`getTargetField()`

Get the field to which injections will be assigned.

`void`
`inject​(Object obj,
      Injection injection)`

Perform the injection against the given object set the "matched" status of the injection when successful.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### InjectionTarget

```
public InjectionTarget​(Field f)
```

Create instance for injection to the given field.

Parameters:
`f` - Field that will receive the `Injection`

  - 

### Method Detail

    - 

#### accepts

```
public boolean accepts​(Injection injection)
```

Can the given Injection be applied to this InjectionTarget?

Parameters:
`injection` - candidate Injection
Returns:
true if injection represents a mock that can be applied to this InjectionTarget,
 false if the mock is of a type that cannot be assigned

    - 

#### inject

```
public void inject​(Object obj,
                   Injection injection)
```

Perform the injection against the given object set the "matched" status of the injection when successful.

Parameters:
`obj` - Object instance on which to perform injection.
`injection` - Injection containing mock to assign.

    - 

#### getTargetField

```
public Field getTargetField()
```

Get the field to which injections will be assigned.

Returns:
target field for injection assignment.