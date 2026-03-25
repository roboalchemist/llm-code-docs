Module org.easymock
Package org.easymock.internal

## Interface IMocksControlState

- 

All Known Implementing Classes:
`RecordState`, `ReplayState`

---

```
public interface IMocksControlState
```

Current state of a mocks control. In practice there are two implementations: record and replay.

Author:
OFFIS, Tammo Freese

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description

`void`
`andAnswer​(IAnswer<?> answer)`
 

`void`
`andDelegateTo​(Object answer)`
 

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

  - 

### Method Detail

    - 

#### invoke

```
Object invoke​(Invocation invocation)
       throws Throwable
```

Throws:
`Throwable`

    - 

#### assertRecordState

```
void assertRecordState()
```

    - 

#### andReturn

```
void andReturn​(Object value)
```

    - 

#### andThrow

```
void andThrow​(Throwable throwable)
```

    - 

#### andAnswer

```
void andAnswer​(IAnswer<?> answer)
```

    - 

#### andDelegateTo

```
void andDelegateTo​(Object answer)
```

    - 

#### andVoid

```
void andVoid()
```

    - 

#### andStubReturn

```
void andStubReturn​(Object value)
```

    - 

#### andStubThrow

```
void andStubThrow​(Throwable throwable)
```

    - 

#### andStubAnswer

```
void andStubAnswer​(IAnswer<?> answer)
```

    - 

#### andStubDelegateTo

```
void andStubDelegateTo​(Object delegateTo)
```

    - 

#### asStub

```
void asStub()
```

    - 

#### times

```
void times​(Range range)
```

    - 

#### checkOrder

```
void checkOrder​(boolean value)
```

    - 

#### makeThreadSafe

```
void makeThreadSafe​(boolean threadSafe)
```

    - 

#### checkIsUsedInOneThread

```
void checkIsUsedInOneThread​(boolean shouldBeUsedInOneThread)
```

    - 

#### replay

```
void replay()
```

    - 

#### verifyRecording

```
void verifyRecording()
```

    - 

#### verifyUnexpectedCalls

```
void verifyUnexpectedCalls()
```

    - 

#### verify

```
void verify()
```