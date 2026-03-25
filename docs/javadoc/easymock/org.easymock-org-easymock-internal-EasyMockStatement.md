Module org.easymock
Package org.easymock.internal

## Class EasyMockStatement

- java.lang.Object

- 

  - org.junit.runners.model.Statement

  - 

    - org.easymock.internal.EasyMockStatement

- 

---

```
public class EasyMockStatement
extends org.junit.runners.model.Statement
```

JUnit Statement for use by JUnit Rule or JUnit Runner to process `Mock` and `TestSubject` annotations.

Since:
3.3
Author:
Henri Tremblay

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`EasyMockStatement​(org.junit.runners.model.Statement originalStatement,
                 Object test)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`void`
`evaluate()`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### EasyMockStatement

```
public EasyMockStatement​(org.junit.runners.model.Statement originalStatement,
                         Object test)
```

  - 

### Method Detail

    - 

#### evaluate

```
public void evaluate()
              throws Throwable
```

Specified by:
`evaluate` in class `org.junit.runners.model.Statement`
Throws:
`Throwable`