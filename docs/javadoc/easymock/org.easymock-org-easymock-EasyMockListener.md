Module org.easymock
Package org.easymock

## Class EasyMockListener

- java.lang.Object

- 

  - org.easymock.EasyMockListener

- 

All Implemented Interfaces:
`org.testng.IInvokedMethodListener`, `org.testng.ITestNGListener`

---

```
public class EasyMockListener
extends Object
implements org.testng.IInvokedMethodListener
```

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`EasyMockListener()`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`void`
`afterInvocation​(org.testng.IInvokedMethod method,
               org.testng.ITestResult testResult)`
 

`void`
`beforeInvocation​(org.testng.IInvokedMethod method,
                org.testng.ITestResult testResult)`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface org.testng.IInvokedMethodListener

`afterInvocation, beforeInvocation`

    - 

### Methods inherited from interface org.testng.ITestNGListener

`isEnabled`

- 

  - 

### Constructor Detail

    - 

#### EasyMockListener

```
public EasyMockListener()
```

  - 

### Method Detail

    - 

#### beforeInvocation

```
public void beforeInvocation​(org.testng.IInvokedMethod method,
                             org.testng.ITestResult testResult)
```

Specified by:
`beforeInvocation` in interface `org.testng.IInvokedMethodListener`

    - 

#### afterInvocation

```
public void afterInvocation​(org.testng.IInvokedMethod method,
                            org.testng.ITestResult testResult)
```

Specified by:
`afterInvocation` in interface `org.testng.IInvokedMethodListener`