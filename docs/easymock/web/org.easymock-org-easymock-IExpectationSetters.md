Module org.easymock
Package org.easymock

## Interface IExpectationSetters<T>

- 

Type Parameters:
`T` - type of what should be returned by this expected call

All Known Implementing Classes:
`MocksControl`

---

```
public interface IExpectationSetters<T>
```

Allows setting expectations for an associated expected invocation.
 Implementations of this interface are returned by
 `EasyMock.expect(Object)`, and by `EasyMock.expectLastCall()`.

Author:
OFFIS, Tammo Freese

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description

`IExpectationSetters<T>`
`andAnswer​(IAnswer<? extends T> answer)`

Sets an object that will be used to calculate the answer for the expected
 invocation (either return a value, or throw an exception).

`IExpectationSetters<T>`
`andDelegateTo​(Object delegateTo)`

Sets an object implementing the same interface as the mock.

`IExpectationSetters<T>`
`andReturn​(T value)`

Sets a return value that will be returned for the expected invocation.

`void`
`andStubAnswer​(IAnswer<? extends T> answer)`

Sets a stub object that will be used to calculate the answer for the
 expected invocation (either return a value, or throw an exception).

`void`
`andStubDelegateTo​(Object delegateTo)`

Sets a stub object implementing the same interface as the mock.

`void`
`andStubReturn​(T value)`

Sets a stub return value that will be returned for the expected
 invocation.

`void`
`andStubThrow​(Throwable throwable)`

Sets a stub throwable that will be thrown for the expected invocation.

`IExpectationSetters<T>`
`andThrow​(Throwable throwable)`

Sets a throwable that will be thrown for the expected invocation.

`IExpectationSetters<T>`
`andVoid()`

Records a call but returns nothing.

`IExpectationSetters<T>`
`anyTimes()`

Expect the last invocation any times.

`void`
`asStub()`

Sets stub behavior for the expected invocation (this is needed for void
 methods).

`IExpectationSetters<T>`
`atLeastOnce()`

Expect the last invocation at least once.

`IExpectationSetters<T>`
`once()`

Expect the last invocation once.

`IExpectationSetters<T>`
`times​(int count)`

Expect the last invocation `count` times.

`IExpectationSetters<T>`
`times​(int min,
     int max)`

Expect the last invocation between `min` and `max`
 times.

- 

  - 

### Method Detail

    - 

#### andReturn

```
IExpectationSetters<T> andReturn​(T value)
```

Sets a return value that will be returned for the expected invocation.

Parameters:
`value` - the value to return.
Returns:
this object to allow method call chaining.

    - 

#### andThrow

```
IExpectationSetters<T> andThrow​(Throwable throwable)
```

Sets a throwable that will be thrown for the expected invocation.

Parameters:
`throwable` - the throwable to throw.
Returns:
this object to allow method call chaining.

    - 

#### andAnswer

```
IExpectationSetters<T> andAnswer​(IAnswer<? extends T> answer)
```

Sets an object that will be used to calculate the answer for the expected
 invocation (either return a value, or throw an exception).

Parameters:
`answer` - the object used to answer the invocation.
Returns:
this object to allow method call chaining.

    - 

#### andDelegateTo

```
IExpectationSetters<T> andDelegateTo​(Object delegateTo)
```

Sets an object implementing the same interface as the mock. The expected
 method call will be delegated to it with the actual arguments. The answer
 returned by this call will then be the answer returned by the mock
 (either return a value, or throw an exception).

Parameters:
`delegateTo` - the object the call is delegated to.
Returns:
the value returned by the delegated call.

    - 

#### andVoid

```
IExpectationSetters<T> andVoid()
```

Records a call but returns nothing. Used to chain calls on void methods
 `expectLastCall().andThrow(e).andVoid()`

Returns:
this object to allow method call chaining.

    - 

#### andStubReturn

```
void andStubReturn​(T value)
```

Sets a stub return value that will be returned for the expected
 invocation.

Parameters:
`value` - the value to return.

    - 

#### andStubThrow

```
void andStubThrow​(Throwable throwable)
```

Sets a stub throwable that will be thrown for the expected invocation.

Parameters:
`throwable` - the throwable to throw.

    - 

#### andStubAnswer

```
void andStubAnswer​(IAnswer<? extends T> answer)
```

Sets a stub object that will be used to calculate the answer for the
 expected invocation (either return a value, or throw an exception).

Parameters:
`answer` - the object used to answer the invocation.

    - 

#### andStubDelegateTo

```
void andStubDelegateTo​(Object delegateTo)
```

Sets a stub object implementing the same interface as the mock. The
 expected method call will be delegated to it with the actual arguments.
 The answer returned by this call will then be the answer returned by the
 mock (either return a value, or throw an exception).

Parameters:
`delegateTo` - the object the call is delegated to.

    - 

#### asStub

```
void asStub()
```

Sets stub behavior for the expected invocation (this is needed for void
 methods).

    - 

#### times

```
IExpectationSetters<T> times​(int count)
```

Expect the last invocation `count` times.

Parameters:
`count` - the number of invocations expected
Returns:
this object to allow method call chaining.

    - 

#### times

```
IExpectationSetters<T> times​(int min,
                             int max)
```

Expect the last invocation between `min` and `max`
 times.

Parameters:
`min` - the minimum number of invocations expected.
`max` - the maximum number of invocations expected.
Returns:
this object to allow method call chaining.

    - 

#### once

```
IExpectationSetters<T> once()
```

Expect the last invocation once. This is default in EasyMock.

Returns:
this object to allow method call chaining.

    - 

#### atLeastOnce

```
IExpectationSetters<T> atLeastOnce()
```

Expect the last invocation at least once.

Returns:
this object to allow method call chaining.

    - 

#### anyTimes

```
IExpectationSetters<T> anyTimes()
```

Expect the last invocation any times.

Returns:
this object to allow method call chaining.