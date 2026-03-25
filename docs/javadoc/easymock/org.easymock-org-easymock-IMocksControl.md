Module org.easymock
Package org.easymock

## Interface IMocksControl

- 

All Known Implementing Classes:
`MocksControl`

---

```
public interface IMocksControl
```

Controls all the mock objects created by it. For details, see the EasyMock
 documentation.

Author:
OFFIS, Tammo Freese

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods Default Methods 

Modifier and Type
Method
Description

`void`
`checkIsUsedInOneThread​(boolean shouldBeUsedInOneThread)`

Check that the mock is called from only one thread

`void`
`checkOrder​(boolean state)`

Switches order checking on and off.

`<T,​R>
R`
`createMock​(Class<T> toMock)`

Same as `mock(Class)` but using the old naming.

`<T,​R>
R`
`createMock​(String name,
          Class<T> toMock)`

Same as `mock(String, Class)` but using the old naming.

`<T,​R>
R`
`createMock​(String name,
          Class<T> toMock,
          ConstructorArgs constructorArgs,
          Method... mockedMethods)`

Same as `mock(String, Class, ConstructorArgs, Method...)` but using the old naming

`void`
`makeThreadSafe​(boolean threadSafe)`

Makes the mock thread safe.

`default <T,​R>
R`
`mock​(Class<T> toMock)`

Creates a mock object that implements the given interface.

`default <T,​R>
R`
`mock​(String name,
    Class<T> toMock)`

Creates a mock object that implements the given interface.

`default <T,​R>
R`
`mock​(String name,
    Class<T> toMock,
    ConstructorArgs constructorArgs,
    Method... mockedMethods)`

Creates a mock object that implements the given class.

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

  - 

### Method Detail

    - 

#### mock

```
default <T,​R> R mock​(Class<T> toMock)
```

Creates a mock object that implements the given interface.

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
Since:
4.0

    - 

#### mock

```
default <T,​R> R mock​(String name,
                           Class<T> toMock)
```

Creates a mock object that implements the given interface.

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
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.
Since:
4.0

    - 

#### mock

```
default <T,​R> R mock​(String name,
                           Class<T> toMock,
                           ConstructorArgs constructorArgs,
                           Method... mockedMethods)
```

Creates a mock object that implements the given class. Using this method directly in a test class
 is not recommended. Only frameworks extending EasyMock should use it. Final users should use
 the more convenient `EasyMock.partialMockBuilder(Class)` method instead

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
Since:
4.0

    - 

#### createMock

```
<T,​R> R createMock​(Class<T> toMock)
```

Same as `mock(Class)` but using the old naming.

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
<T,​R> R createMock​(String name,
                         Class<T> toMock)
```

Same as `mock(String, Class)` but using the old naming.

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
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.

    - 

#### createMock

```
<T,​R> R createMock​(String name,
                         Class<T> toMock,
                         ConstructorArgs constructorArgs,
                         Method... mockedMethods)
```

Same as `mock(String, Class, ConstructorArgs, Method...)` but using the old naming

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

#### reset

```
void reset()
```

Removes all expectations for the mock objects of this control.

    - 

#### resetToNice

```
void resetToNice()
```

Removes all expectations for the mock objects of this control and turn
 them to nice mocks.

    - 

#### resetToDefault

```
void resetToDefault()
```

Removes all expectations for the mock objects of this control and turn
 them to default mocks.

    - 

#### resetToStrict

```
void resetToStrict()
```

Removes all expectations for the mock objects of this control and turn
 them to strict mocks.

    - 

#### replay

```
void replay()
```

Switches the control from record mode to replay mode.

    - 

#### verify

```
void verify()
```

Verifies that all expectations were met and that no unexpected
 call was performed. It has the same effect as calling `verifyRecording()`
 followed by `verifyUnexpectedCalls()`.

    - 

#### verifyRecording

```
void verifyRecording()
```

Verifies that all expectations were met.

Since:
3.5

    - 

#### verifyUnexpectedCalls

```
void verifyUnexpectedCalls()
```

Verifies that no unexpected call was performed.

Since:
3.5

    - 

#### checkOrder

```
void checkOrder​(boolean state)
```

Switches order checking on and off.

Parameters:
`state` - `true` switches order checking on,
            `false` switches it off.

    - 

#### makeThreadSafe

```
void makeThreadSafe​(boolean threadSafe)
```

Makes the mock thread safe.

Parameters:
`threadSafe` - If the mock should be thread safe or not

    - 

#### checkIsUsedInOneThread

```
void checkIsUsedInOneThread​(boolean shouldBeUsedInOneThread)
```

Check that the mock is called from only one thread

Parameters:
`shouldBeUsedInOneThread` - If it should be used in one thread only or not