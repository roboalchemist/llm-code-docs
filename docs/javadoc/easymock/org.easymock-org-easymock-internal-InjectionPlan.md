Module org.easymock
Package org.easymock.internal

## Class InjectionPlan

- java.lang.Object

- 

  - org.easymock.internal.InjectionPlan

- 

---

```
public class InjectionPlan
extends Object
```

Container for mock injections and test subject injection targets.

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

`InjectionPlan()`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`void`
`addInjection​(Injection injection)`

Add an `Injection` to this container.

`void`
`addTestSubjectField​(Field f)`

Add a field that should be treated as a test subject injection target.

`List<Injection>`
`getQualifiedInjections()`

Get all injections having fieldName qualifiers.

`List<Field>`
`getTestSubjectFields()`

Get fields identified as test subjects to which injection of mocks should be attempted.

`List<Injection>`
`getUnqualifiedInjections()`

Get all injections that do not have fieldName qualifiers.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### InjectionPlan

```
public InjectionPlan()
```

  - 

### Method Detail

    - 

#### addInjection

```
public void addInjection​(Injection injection)
```

Add an `Injection` to this container. It will be managed according to the presence
 of a fieldName qualifier, and attempting to add an Injection with a duplicate fieldName
 qualifier will cause an error.

Parameters:
`injection` - Injection to manage as part of this plan

    - 

#### addTestSubjectField

```
public void addTestSubjectField​(Field f)
```

Add a field that should be treated as a test subject injection target.

Parameters:
`f` - Field representing a test subject to which injection of mocks will be attempted

    - 

#### getTestSubjectFields

```
public List<Field> getTestSubjectFields()
```

Get fields identified as test subjects to which injection of mocks should be attempted.

Returns:
fields representing test subjects

    - 

#### getQualifiedInjections

```
public List<Injection> getQualifiedInjections()
```

Get all injections having fieldName qualifiers.

Returns:
list of Injections having fieldName qualifiers

    - 

#### getUnqualifiedInjections

```
public List<Injection> getUnqualifiedInjections()
```

Get all injections that do not have fieldName qualifiers.

Returns:
list of Injections that do not have fieldName qualifiers.