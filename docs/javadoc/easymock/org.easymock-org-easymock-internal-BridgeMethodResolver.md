Module org.easymock
Package org.easymock.internal

## Class BridgeMethodResolver

- java.lang.Object

- 

  - org.easymock.internal.BridgeMethodResolver

- 

---

```
public final class BridgeMethodResolver
extends Object
```

Code taken from the Spring
 framework.

 Helper for resolving synthetic `bridge Methods` to the
 `Method` being bridged.

 

 Given a synthetic `bridge Method` returns the
 `Method` being bridged. A bridge method may be created by the compiler
 when extending a parameterized type whose methods have parameterized
 arguments. During runtime invocation the bridge `Method` may be invoked
 and/or used via reflection. When attempting to locate annotations on
 `Methods`, it is wise to check for bridge `Methods`
 as appropriate and find the bridged `Method`.

 

 See  The Java Language Specification for more details on the use of bridge
 methods.

Author:
Rob Harrop, Juergen Hoeller

- 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method
Description

`static Method`
`findBridgedMethod​(Method bridgeMethod)`

Find the original method for the supplied `bridge Method`.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Method Detail

    - 

#### findBridgedMethod

```
public static Method findBridgedMethod​(Method bridgeMethod)
```

Find the original method for the supplied `bridge Method`.
 

 It is safe to call this method passing in a non-bridge `Method`
 instance. In such a case, the supplied `Method` instance is
 returned directly to the caller. Callers are **not**
 required to check for bridging before calling this method.

Parameters:
`bridgeMethod` - the bridge method
Returns:
the original method for the bridge
Throws:
`IllegalStateException` - if no bridged `Method` can be found