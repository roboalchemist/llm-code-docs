Module org.easymock
Package org.easymock.internal

## Class MocksControl

- java.lang.Object

- 

  - org.easymock.internal.MocksControl

- 

All Implemented Interfaces:
`Serializable`, `IExpectationSetters<Object>`, `IMocksControl`

---

```
public class MocksControl
extends Object
implements IMocksControl, IExpectationSetters<Object>, Serializable
```

Controls all the mocks created by `EasyMock`. It contains the state of the mocks.

Author:
OFFIS, Tammo Freese
See Also:
Serialized Form

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field
Description

`static Range`
`AT_LEAST_ONCE`

One or more calls.

`static Range`
`ONCE`

Exactly one call.

`static Range`
`ZERO_OR_MORE`

Zero or more calls.

  - 

### Constructor Summary

Constructors 

Constructor
Description

`MocksControl​(MockType type)`
 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`IExpectationSetters<Object>`
`andAnswer​(IAnswer<?> answer)`

Sets an object that will be used to calculate the answer for the expected
 invocation (either return a value, or throw an exception).

`IExpectationSetters<Object>`
`andDelegateTo​(Object answer)`

Sets an object implementing the same interface as the mock.

`IExpectationSetters<Object>`
`andReturn​(Object value)`

Sets a return value that will be returned for the expected invocation.

`void`
`andStubAnswer​(IAnswer<?> answer)`

Sets a stub object that will be used to calculate the answer for the
 expected invocation (either return a value, or throw an exception).

`void`
`andStubDelegateTo​(Object delegateTo)`

Sets a stub object implementing the same interface as the mock.

`void`
`andStubReturn​(Object value)`

Sets a stub return value that will be returned for the expected
 invocation.

`void`
`andStubThrow​(Throwable throwable)`

Sets a stub throwable that will be thrown for the expected invocation.

`IExpectationSetters<Object>`
`andThrow​(Throwable throwable)`

Sets a throwable that will be thrown for the expected invocation.

`IExpectationSetters<Object>`
`andVoid()`

Records a call but returns nothing.

`IExpectationSetters<Object>`
`anyTimes()`

Expect the last invocation any times.

`void`
`asStub()`

Sets stub behavior for the expected invocation (this is needed for void
 methods).

`IExpectationSetters<Object>`
`atLeastOnce()`

Expect the last invocation at least once.

`void`
`checkIsUsedInOneThread​(boolean shouldBeUsedInOneThread)`

Check that the mock is called from only one thread

`void`
`checkOrder​(boolean value)`

Switches order checking on and off.

`<T,​R>
R`
`createMock​(Class<T> toMock)`

Same as `IMocksControl.mock(Class)` but using the old naming.

`<T,​R>
R`
`createMock​(String name,
          Class<T> toMock)`

Same as `IMocksControl.mock(String, Class)` but using the old naming.

`<T,​R>
R`
`createMock​(String name,
          Class<T> toMock,
          ConstructorArgs constructorArgs,
          Method... mockedMethods)`

Same as `IMocksControl.mock(String, Class, ConstructorArgs, Method...)` but using the old naming

`static MocksControl`
`getControl​(Object mock)`
 

`static InvocationHandler`
`getInvocationHandler​(Object mock)`
 

`static <T,​R extends T>
Class<R>`
`getMockedClass​(T proxy)`

Return the class of interface (depending on the mock type) that was
 mocked

`static IProxyFactory`
`getProxyFactory​(Object o)`
 

`IMocksControlState`
`getState()`
 

`MockType`
`getType()`
 

`void`
`makeThreadSafe​(boolean threadSafe)`

Makes the mock thread safe.

`IExpectationSetters<Object>`
`once()`

Expect the last invocation once.

`void`
`replay()`

Switches the control from record mode to replay mode.

`void`
`reset()`

Removes all expectations for the mock objects of this control.

`void`
`resetToDefault()`

Removes all expectations for the mock objects of this control and turn
 them to default mocks.

`void`
`resetToNice()`

Removes all expectations for the mock objects of this control and turn
 them to nice mocks.

`void`
`resetToStrict()`

Removes all expectations for the mock objects of this control and turn
 them to strict mocks.

`IExpectationSetters<Object>`
`times​(int times)`

Expect the last invocation `count` times.

`IExpectationSetters<Object>`
`times​(int min,
     int max)`

Expect the last invocation between `min` and `max`
 times.

`void`
`verify()`

Verifies that all expectations were met and that no unexpected
 call was performed.

`void`
`verifyRecording()`

Verifies that all expectations were met.

`void`
`verifyUnexpectedCalls()`

Verifies that no unexpected call was performed.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface org.easymock.IMocksControl

`mock, mock, mock`

- 

  - 

### Field Detail

    - 

#### ONCE

```
public static final Range ONCE
```

Exactly one call.

    - 

#### AT_LEAST_ONCE

```
public static final Range AT_LEAST_ONCE
```

One or more calls.

    - 

#### ZERO_OR_MORE

```
public static final Range ZERO_OR_MORE
```

Zero or more calls.

  - 

### Constructor Detail

    - 

#### MocksControl

```
public MocksControl​(MockType type)
```

  - 

### Method Detail

    - 

#### getType

```
public MockType getType()
```

    - 

#### getState

```
public IMocksControlState getState()
```

    - 

#### createMock

```
public <T,​R> R createMock​(Class<T> toMock)
```

Description copied from interface: `IMocksControl`
Same as `IMocksControl.mock(Class)` but using the old naming.

Specified by:
`createMock` in interface `IMocksControl`
Type Parameters:
`T` - the interface or class that the mock object should
            implement/extend.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`toMock` - the interface or class that the mock object should
            implement/extend.
Returns:
the mock object.

    - 

#### createMock

```
public <T,​R> R createMock​(String name,
                                Class<T> toMock)
```

Description copied from interface: `IMocksControl`
Same as `IMocksControl.mock(String, Class)` but using the old naming.

Specified by:
`createMock` in interface `IMocksControl`
Type Parameters:
`T` - the interface or class that the mock object should
            implement/extend.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the name of the mock object.
`toMock` - the interface or class that the mock object should
            implement/extend.
Returns:
the mock object.

    - 

#### createMock

```
public <T,​R> R createMock​(String name,
                                Class<T> toMock,
                                ConstructorArgs constructorArgs,
                                Method... mockedMethods)
```

Description copied from interface: `IMocksControl`
Same as `IMocksControl.mock(String, Class, ConstructorArgs, Method...)` but using the old naming

Specified by:
`createMock` in interface `IMocksControl`
Type Parameters:
`T` - the class that the mock object should extend.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the name of the mock object.
`toMock` - the class that the mock object should extend.
`constructorArgs` - constructor and parameters used to instantiate the mock. If null, no constructor will be called
`mockedMethods` - methods that will be mocked, other methods will behave
            normally. If empty, all methods will be mocked
Returns:
the mock object.

    - 

#### getProxyFactory

```
public static IProxyFactory getProxyFactory​(Object o)
```

    - 

#### getControl

```
public static MocksControl getControl​(Object mock)
```

    - 

#### getInvocationHandler

```
public static InvocationHandler getInvocationHandler​(Object mock)
```

    - 

#### getMockedClass

```
public static <T,​R extends T> Class<R> getMockedClass​(T proxy)
```

Return the class of interface (depending on the mock type) that was
 mocked

Type Parameters:
`T` - Mocked class
`R` - Mock class
Parameters:
`proxy` - Mock object
Returns:
the mocked class or interface

    - 

#### reset

```
public void reset()
```

Description copied from interface: `IMocksControl`
Removes all expectations for the mock objects of this control.

Specified by:
`reset` in interface `IMocksControl`

    - 

#### resetToNice

```
public void resetToNice()
```

Description copied from interface: `IMocksControl`
Removes all expectations for the mock objects of this control and turn
 them to nice mocks.

Specified by:
`resetToNice` in interface `IMocksControl`

    - 

#### resetToDefault

```
public void resetToDefault()
```

Description copied from interface: `IMocksControl`
Removes all expectations for the mock objects of this control and turn
 them to default mocks.

Specified by:
`resetToDefault` in interface `IMocksControl`

    - 

#### resetToStrict

```
public void resetToStrict()
```

Description copied from interface: `IMocksControl`
Removes all expectations for the mock objects of this control and turn
 them to strict mocks.

Specified by:
`resetToStrict` in interface `IMocksControl`

    - 

#### replay

```
public void replay()
```

Description copied from interface: `IMocksControl`
Switches the control from record mode to replay mode.

Specified by:
`replay` in interface `IMocksControl`

    - 

#### verifyRecording

```
public void verifyRecording()
```

Description copied from interface: `IMocksControl`
Verifies that all expectations were met.

Specified by:
`verifyRecording` in interface `IMocksControl`

    - 

#### verifyUnexpectedCalls

```
public void verifyUnexpectedCalls()
```

Description copied from interface: `IMocksControl`
Verifies that no unexpected call was performed.

Specified by:
`verifyUnexpectedCalls` in interface `IMocksControl`

    - 

#### verify

```
public void verify()
```

Description copied from interface: `IMocksControl`
Verifies that all expectations were met and that no unexpected
 call was performed. It has the same effect as calling `IMocksControl.verifyRecording()`
 followed by `IMocksControl.verifyUnexpectedCalls()`.

Specified by:
`verify` in interface `IMocksControl`

    - 

#### checkOrder

```
public void checkOrder​(boolean value)
```

Description copied from interface: `IMocksControl`
Switches order checking on and off.

Specified by:
`checkOrder` in interface `IMocksControl`
Parameters:
`value` - `true` switches order checking on,
            `false` switches it off.

    - 

#### makeThreadSafe

```
public void makeThreadSafe​(boolean threadSafe)
```

Description copied from interface: `IMocksControl`
Makes the mock thread safe.

Specified by:
`makeThreadSafe` in interface `IMocksControl`
Parameters:
`threadSafe` - If the mock should be thread safe or not

    - 

#### checkIsUsedInOneThread

```
public void checkIsUsedInOneThread​(boolean shouldBeUsedInOneThread)
```

Description copied from interface: `IMocksControl`
Check that the mock is called from only one thread

Specified by:
`checkIsUsedInOneThread` in interface `IMocksControl`
Parameters:
`shouldBeUsedInOneThread` - If it should be used in one thread only or not

    - 

#### andReturn

```
public IExpectationSetters<Object> andReturn​(Object value)
```

Description copied from interface: `IExpectationSetters`
Sets a return value that will be returned for the expected invocation.

Specified by:
`andReturn` in interface `IExpectationSetters<Object>`
Parameters:
`value` - the value to return.
Returns:
this object to allow method call chaining.

    - 

#### andThrow

```
public IExpectationSetters<Object> andThrow​(Throwable throwable)
```

Description copied from interface: `IExpectationSetters`
Sets a throwable that will be thrown for the expected invocation.

Specified by:
`andThrow` in interface `IExpectationSetters<Object>`
Parameters:
`throwable` - the throwable to throw.
Returns:
this object to allow method call chaining.

    - 

#### andAnswer

```
public IExpectationSetters<Object> andAnswer​(IAnswer<?> answer)
```

Description copied from interface: `IExpectationSetters`
Sets an object that will be used to calculate the answer for the expected
 invocation (either return a value, or throw an exception).

Specified by:
`andAnswer` in interface `IExpectationSetters<Object>`
Parameters:
`answer` - the object used to answer the invocation.
Returns:
this object to allow method call chaining.

    - 

#### andDelegateTo

```
public IExpectationSetters<Object> andDelegateTo​(Object answer)
```

Description copied from interface: `IExpectationSetters`
Sets an object implementing the same interface as the mock. The expected
 method call will be delegated to it with the actual arguments. The answer
 returned by this call will then be the answer returned by the mock
 (either return a value, or throw an exception).

Specified by:
`andDelegateTo` in interface `IExpectationSetters<Object>`
Parameters:
`answer` - the object the call is delegated to.
Returns:
the value returned by the delegated call.

    - 

#### andVoid

```
public IExpectationSetters<Object> andVoid()
```

Description copied from interface: `IExpectationSetters`
Records a call but returns nothing. Used to chain calls on void methods
 `expectLastCall().andThrow(e).andVoid()`

Specified by:
`andVoid` in interface `IExpectationSetters<Object>`
Returns:
this object to allow method call chaining.

    - 

#### andStubReturn

```
public void andStubReturn​(Object value)
```

Description copied from interface: `IExpectationSetters`
Sets a stub return value that will be returned for the expected
 invocation.

Specified by:
`andStubReturn` in interface `IExpectationSetters<Object>`
Parameters:
`value` - the value to return.

    - 

#### andStubThrow

```
public void andStubThrow​(Throwable throwable)
```

Description copied from interface: `IExpectationSetters`
Sets a stub throwable that will be thrown for the expected invocation.

Specified by:
`andStubThrow` in interface `IExpectationSetters<Object>`
Parameters:
`throwable` - the throwable to throw.

    - 

#### andStubAnswer

```
public void andStubAnswer​(IAnswer<?> answer)
```

Description copied from interface: `IExpectationSetters`
Sets a stub object that will be used to calculate the answer for the
 expected invocation (either return a value, or throw an exception).

Specified by:
`andStubAnswer` in interface `IExpectationSetters<Object>`
Parameters:
`answer` - the object used to answer the invocation.

    - 

#### andStubDelegateTo

```
public void andStubDelegateTo​(Object delegateTo)
```

Description copied from interface: `IExpectationSetters`
Sets a stub object implementing the same interface as the mock. The
 expected method call will be delegated to it with the actual arguments.
 The answer returned by this call will then be the answer returned by the
 mock (either return a value, or throw an exception).

Specified by:
`andStubDelegateTo` in interface `IExpectationSetters<Object>`
Parameters:
`delegateTo` - the object the call is delegated to.

    - 

#### asStub

```
public void asStub()
```

Description copied from interface: `IExpectationSetters`
Sets stub behavior for the expected invocation (this is needed for void
 methods).

Specified by:
`asStub` in interface `IExpectationSetters<Object>`

    - 

#### times

```
public IExpectationSetters<Object> times​(int times)
```

Description copied from interface: `IExpectationSetters`
Expect the last invocation `count` times.

Specified by:
`times` in interface `IExpectationSetters<Object>`
Parameters:
`times` - the number of invocations expected
Returns:
this object to allow method call chaining.

    - 

#### times

```
public IExpectationSetters<Object> times​(int min,
                                         int max)
```

Description copied from interface: `IExpectationSetters`
Expect the last invocation between `min` and `max`
 times.

Specified by:
`times` in interface `IExpectationSetters<Object>`
Parameters:
`min` - the minimum number of invocations expected.
`max` - the maximum number of invocations expected.
Returns:
this object to allow method call chaining.

    - 

#### once

```
public IExpectationSetters<Object> once()
```

Description copied from interface: `IExpectationSetters`
Expect the last invocation once. This is default in EasyMock.

Specified by:
`once` in interface `IExpectationSetters<Object>`
Returns:
this object to allow method call chaining.

    - 

#### atLeastOnce

```
public IExpectationSetters<Object> atLeastOnce()
```

Description copied from interface: `IExpectationSetters`
Expect the last invocation at least once.

Specified by:
`atLeastOnce` in interface `IExpectationSetters<Object>`
Returns:
this object to allow method call chaining.

    - 

#### anyTimes

```
public IExpectationSetters<Object> anyTimes()
```

Description copied from interface: `IExpectationSetters`
Expect the last invocation any times.

Specified by:
`anyTimes` in interface `IExpectationSetters<Object>`
Returns:
this object to allow method call chaining.