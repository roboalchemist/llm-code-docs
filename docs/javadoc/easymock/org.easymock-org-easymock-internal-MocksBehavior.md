Module org.easymock
Package org.easymock.internal

## Class MocksBehavior

- java.lang.Object

- 

  - org.easymock.internal.MocksBehavior

- 

All Implemented Interfaces:
`Serializable`, `IMocksBehavior`

---

```
public class MocksBehavior
extends Object
implements IMocksBehavior, Serializable
```

Default implementation of `IMocksBehavior`. It keeps the full behavior of mocks from the same `IMocksControl`.

Author:
OFFIS, Tammo Freese
See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`MocksBehavior​(boolean nice)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`Result`
`addActual​(Invocation actual)`
 

`void`
`addExpected​(ExpectedInvocation expected,
           Result result,
           Range count)`
 

`void`
`addStub​(ExpectedInvocation expected,
       Result result)`
 

`void`
`checkOrder​(boolean value)`
 

`void`
`checkThreadSafety()`
 

`boolean`
`isThreadSafe()`
 

`void`
`makeThreadSafe​(boolean isThreadSafe)`
 

`void`
`shouldBeUsedInOneThread​(boolean shouldBeUsedInOneThread)`
 

`void`
`verify()`
 

`void`
`verifyRecording()`
 

`void`
`verifyUnexpectedCalls()`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### MocksBehavior

```
public MocksBehavior​(boolean nice)
```

  - 

### Method Detail

    - 

#### addStub

```
public final void addStub​(ExpectedInvocation expected,
                          Result result)
```

Specified by:
`addStub` in interface `IMocksBehavior`

    - 

#### addExpected

```
public void addExpected​(ExpectedInvocation expected,
                        Result result,
                        Range count)
```

Specified by:
`addExpected` in interface `IMocksBehavior`

    - 

#### addActual

```
public final Result addActual​(Invocation actual)
```

Specified by:
`addActual` in interface `IMocksBehavior`

    - 

#### verifyRecording

```
public void verifyRecording()
```

Specified by:
`verifyRecording` in interface `IMocksBehavior`

    - 

#### verifyUnexpectedCalls

```
public void verifyUnexpectedCalls()
```

Specified by:
`verifyUnexpectedCalls` in interface `IMocksBehavior`

    - 

#### verify

```
public void verify()
```

Specified by:
`verify` in interface `IMocksBehavior`

    - 

#### checkOrder

```
public void checkOrder​(boolean value)
```

Specified by:
`checkOrder` in interface `IMocksBehavior`

    - 

#### makeThreadSafe

```
public void makeThreadSafe​(boolean isThreadSafe)
```

Specified by:
`makeThreadSafe` in interface `IMocksBehavior`

    - 

#### shouldBeUsedInOneThread

```
public void shouldBeUsedInOneThread​(boolean shouldBeUsedInOneThread)
```

Specified by:
`shouldBeUsedInOneThread` in interface `IMocksBehavior`

    - 

#### isThreadSafe

```
public boolean isThreadSafe()
```

Specified by:
`isThreadSafe` in interface `IMocksBehavior`

    - 

#### checkThreadSafety

```
public void checkThreadSafety()
```

Specified by:
`checkThreadSafety` in interface `IMocksBehavior`