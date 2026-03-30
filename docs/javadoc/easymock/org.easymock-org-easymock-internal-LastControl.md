Module org.easymock
Package org.easymock.internal

## Class LastControl

- java.lang.Object

- 

  - org.easymock.internal.LastControl

- 

---

```
public final class LastControl
extends Object
```

The last mocks control used in the current thread.

Author:
OFFIS, Tammo Freese

- 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method
Description

`static Invocation`
`getCurrentInvocation()`
 

`static MocksControl`
`lastControl()`
 

`static void`
`popCurrentInvocation()`
 

`static List<IArgumentMatcher>`
`pullMatchers()`
 

`static void`
`pushCurrentInvocation​(Invocation invocation)`
 

`static void`
`reportAnd​(int count)`
 

`static void`
`reportLastControl​(MocksControl control)`
 

`static void`
`reportMatcher​(IArgumentMatcher matcher)`
 

`static void`
`reportNot()`
 

`static void`
`reportOr​(int count)`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Method Detail

    - 

#### reportLastControl

```
public static void reportLastControl​(MocksControl control)
```

    - 

#### lastControl

```
public static MocksControl lastControl()
```

    - 

#### reportMatcher

```
public static void reportMatcher​(IArgumentMatcher matcher)
```

    - 

#### pullMatchers

```
public static List<IArgumentMatcher> pullMatchers()
```

    - 

#### reportAnd

```
public static void reportAnd​(int count)
```

    - 

#### reportNot

```
public static void reportNot()
```

    - 

#### reportOr

```
public static void reportOr​(int count)
```

    - 

#### getCurrentInvocation

```
public static Invocation getCurrentInvocation()
```

    - 

#### pushCurrentInvocation

```
public static void pushCurrentInvocation​(Invocation invocation)
```

    - 

#### popCurrentInvocation

```
public static void popCurrentInvocation()
```