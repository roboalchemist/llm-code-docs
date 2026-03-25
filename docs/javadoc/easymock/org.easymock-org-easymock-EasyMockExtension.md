Module org.easymock
Package org.easymock

## Class EasyMockExtension

- java.lang.Object

- 

  - org.easymock.EasyMockExtension

- 

All Implemented Interfaces:
`org.junit.jupiter.api.extension.Extension`, `org.junit.jupiter.api.extension.TestInstancePostProcessor`

---

```
public class EasyMockExtension
extends Object
implements org.junit.jupiter.api.extension.TestInstancePostProcessor
```

JUnit 5 replaced the previous `RunWith` annotation
 (which made use of `EasyMockRunner`) with the new
 `ExtendWith` annotation. @ExtendWith
 allows for multiple extensions to be mixed and used together. This is only
 relevant for JUnit 5.

 This is retrieved from https://stackoverflow.com/a/47243856/2152081
 StackOverflow answer provided by https://stackoverflow.com/users/4126968/eee

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`EasyMockExtension()`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`void`
`postProcessTestInstance​(Object testInstance,
                       org.junit.jupiter.api.extension.ExtensionContext context)`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### EasyMockExtension

```
public EasyMockExtension()
```

  - 

### Method Detail

    - 

#### postProcessTestInstance

```
public void postProcessTestInstance​(Object testInstance,
                                    org.junit.jupiter.api.extension.ExtensionContext context)
                             throws Exception
```

Specified by:
`postProcessTestInstance` in interface `org.junit.jupiter.api.extension.TestInstancePostProcessor`
Throws:
`Exception`