Module org.easymock
Package org.easymock.internal

## Class Injector

- java.lang.Object

- 

  - org.easymock.internal.Injector

- 

---

```
public class Injector
extends Object
```

Performs creation of mocks and injection into test subjects in accordance with annotations present in the host object.

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

`Injector()`
 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method
Description

`static void`
`injectMocks​(Object host)`

Inject a mock to every fields annotated with `Mock` on the class passed
 in parameter.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Injector

```
public Injector()
```

  - 

### Method Detail

    - 

#### injectMocks

```
public static void injectMocks​(Object host)
```

Inject a mock to every fields annotated with `Mock` on the class passed
 in parameter. Then, inject these mocks to the fields of every class annotated with `TestSubject`.
 

 The rules are
 

     
      - Static and final fields are ignored
     
      - If two mocks have the same field name, return an error
     
      - If a mock has a field name and no matching field is found, return an error
 

 Then, ignoring all fields and mocks matched by field name
 

     
      - If a mock without field name can be assigned to a field, do it. The same mock can be assigned more than once
     
      - If no mock can be assigned to a field, skip the field silently
     
      - If the mock cannot be assigned to any field, skip the mock silently
     
      - If two mocks can be assigned to the same field, return an error
 

 Fields are searched recursively on the superclasses
 

 **Note:** If the parameter extends `EasyMockSupport`, the mocks will be created using it to allow
 `replayAll/verifyAll` to work afterwards

Parameters:
`host` - the object on which to inject mocks
Since:
3.2