Module org.easymock
Package org.easymock

## Class EasyMockRule

- java.lang.Object

- 

  - org.easymock.EasyMockRule

- 

All Implemented Interfaces:
`org.junit.rules.TestRule`

---

```
public class EasyMockRule
extends Object
implements org.junit.rules.TestRule
```

JUnit Rule used to process `Mock` and `TestSubject` annotations.

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

`EasyMockRule​(Object test)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`org.junit.runners.model.Statement`
`apply​(org.junit.runners.model.Statement base,
     org.junit.runner.Description description)`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### EasyMockRule

```
public EasyMockRule​(Object test)
```

  - 

### Method Detail

    - 

#### apply

```
public org.junit.runners.model.Statement apply​(org.junit.runners.model.Statement base,
                                               org.junit.runner.Description description)
```

Specified by:
`apply` in interface `org.junit.rules.TestRule`