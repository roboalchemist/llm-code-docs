Module org.easymock
Package org.easymock.internal

## Interface IMocksBehavior

- 

All Known Implementing Classes:
`MocksBehavior`

---

```
public interface IMocksBehavior
```

The behavior of a mock. I.e. ordered or not, thread safe or not, expectations, etc.

Author:
OFFIS, Tammo Freese

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description

`Result`
`addActual​(Invocation invocation)`
 

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

  - 

### Method Detail

    - 

#### addExpected

```
void addExpected​(ExpectedInvocation expected,
                 Result result,
                 Range count)
```

    - 

#### addStub

```
void addStub​(ExpectedInvocation expected,
             Result result)
```

    - 

#### checkOrder

```
void checkOrder​(boolean value)
```

    - 

#### makeThreadSafe

```
void makeThreadSafe​(boolean isThreadSafe)
```

    - 

#### shouldBeUsedInOneThread

```
void shouldBeUsedInOneThread​(boolean shouldBeUsedInOneThread)
```

    - 

#### addActual

```
Result addActual​(Invocation invocation)
```

    - 

#### isThreadSafe

```
boolean isThreadSafe()
```

    - 

#### checkThreadSafety

```
void checkThreadSafety()
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