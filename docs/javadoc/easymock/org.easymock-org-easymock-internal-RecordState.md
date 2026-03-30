Module org.easymock
Package org.easymock.internal

## Class RecordState

- java.lang.Object

- 

  - org.easymock.internal.RecordState

- 

All Implemented Interfaces:
`Serializable`, `IMocksControlState`

---

```
public class RecordState
extends Object
implements IMocksControlState, Serializable
```

State in which a mock is recording its behavior.

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

`RecordState​(IMocksBehavior behavior)`
 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`void`
`andAnswer​(IAnswer<?> answer)`
 

`void`
`andDelegateTo​(Object delegateTo)`
 

`void`
`andReturn​(Object value)`
 

`void`
`andStubAnswer​(IAnswer<?> answer)`
 

`void`
`andStubDelegateTo​(Object delegateTo)`
 

`void`
`andStubReturn​(Object value)`
 

`void`
`andStubThrow​(Throwable throwable)`
 

`void`
`andThrow​(Throwable throwable)`
 

`void`
`andVoid()`
 

`void`
`assertRecordState()`
 

`void`
`asStub()`
 

`void`
`checkIsUsedInOneThread​(boolean shouldBeUsedInOneThread)`
 

`void`
`checkOrder​(boolean value)`
 

`static Object`
`emptyReturnValueFor​(Class<?> type)`
 

`Object`
`invoke​(Invocation invocation)`
 

`void`
`makeThreadSafe​(boolean threadSafe)`
 

`void`
`replay()`
 

`void`
`times​(Range range)`
 

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

#### RecordState

```
public RecordState​(IMocksBehavior behavior)
```

  - 

### Method Detail

    - 

#### assertRecordState

```
public void assertRecordState()
```

Specified by:
`assertRecordState` in interface `IMocksControlState`

    - 

#### invoke

```
public Object invoke​(Invocation invocation)
```

Specified by:
`invoke` in interface `IMocksControlState`

    - 

#### replay

```
public void replay()
```

Specified by:
`replay` in interface `IMocksControlState`

    - 

#### verifyRecording

```
public void verifyRecording()
```

Specified by:
`verifyRecording` in interface `IMocksControlState`

    - 

#### verifyUnexpectedCalls

```
public void verifyUnexpectedCalls()
```

Specified by:
`verifyUnexpectedCalls` in interface `IMocksControlState`

    - 

#### verify

```
public void verify()
```

Specified by:
`verify` in interface `IMocksControlState`

    - 

#### andReturn

```
public void andReturn​(Object value)
```

Specified by:
`andReturn` in interface `IMocksControlState`

    - 

#### andThrow

```
public void andThrow​(Throwable throwable)
```

Specified by:
`andThrow` in interface `IMocksControlState`

    - 

#### andAnswer

```
public void andAnswer​(IAnswer<?> answer)
```

Specified by:
`andAnswer` in interface `IMocksControlState`

    - 

#### andDelegateTo

```
public void andDelegateTo​(Object delegateTo)
```

Specified by:
`andDelegateTo` in interface `IMocksControlState`

    - 

#### andVoid

```
public void andVoid()
```

Specified by:
`andVoid` in interface `IMocksControlState`

    - 

#### andStubReturn

```
public void andStubReturn​(Object value)
```

Specified by:
`andStubReturn` in interface `IMocksControlState`

    - 

#### asStub

```
public void asStub()
```

Specified by:
`asStub` in interface `IMocksControlState`

    - 

#### andStubThrow

```
public void andStubThrow​(Throwable throwable)
```

Specified by:
`andStubThrow` in interface `IMocksControlState`

    - 

#### andStubAnswer

```
public void andStubAnswer​(IAnswer<?> answer)
```

Specified by:
`andStubAnswer` in interface `IMocksControlState`

    - 

#### andStubDelegateTo

```
public void andStubDelegateTo​(Object delegateTo)
```

Specified by:
`andStubDelegateTo` in interface `IMocksControlState`

    - 

#### times

```
public void times​(Range range)
```

Specified by:
`times` in interface `IMocksControlState`

    - 

#### emptyReturnValueFor

```
public static Object emptyReturnValueFor​(Class<?> type)
```

    - 

#### checkOrder

```
public void checkOrder​(boolean value)
```

Specified by:
`checkOrder` in interface `IMocksControlState`

    - 

#### makeThreadSafe

```
public void makeThreadSafe​(boolean threadSafe)
```

Specified by:
`makeThreadSafe` in interface `IMocksControlState`

    - 

#### checkIsUsedInOneThread

```
public void checkIsUsedInOneThread​(boolean shouldBeUsedInOneThread)
```

Specified by:
`checkIsUsedInOneThread` in interface `IMocksControlState`