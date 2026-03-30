Module org.easymock
Package org.easymock.internal

## Class MockBuilder<T>

- java.lang.Object

- 

  - org.easymock.internal.MockBuilder<T>

- 

Type Parameters:
`T` - type of the mock created

All Implemented Interfaces:
`IMockBuilder<T>`

---

```
public class MockBuilder<T>
extends Object
implements IMockBuilder<T>
```

Default implementation of IMockBuilder.
 

 *The original idea and part of the code where contributed by Rodrigo
 Damazio and Bruno Fonseca at Google*

Author:
Henri Tremblay

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`MockBuilder​(Class<?> toMock)`
 

`MockBuilder​(Class<?> toMock,
           EasyMockSupport support)`

Used by EasyMockSupport to allow the mock registration in the list of
 controls

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`IMockBuilder<T>`
`addMockedMethod​(Method method)`

Adds a method to be mocked in the testing class.

`IMockBuilder<T>`
`addMockedMethod​(String methodName)`

Adds a method to be mocked in the testing class.

`IMockBuilder<T>`
`addMockedMethod​(String methodName,
               Class<?>... parameterTypes)`

Adds a method to be mocked in the testing class.

`IMockBuilder<T>`
`addMockedMethods​(Method... methods)`

Adds methods to be mocked in the testing class.

`IMockBuilder<T>`
`addMockedMethods​(String... methodNames)`

Adds methods to be mocked in the testing class.

`<R> R`
`createMock()`

Create a default mock from this builder.

`<R> R`
`createMock​(String name)`

Create named mock from the provided mock control using the arguments
 passed to the builder.

`<R> R`
`createMock​(String name,
          IMocksControl control)`

Create named mock from the provided mock control using the arguments
 passed to the builder.

`<R> R`
`createMock​(String name,
          MockType type)`

Create a named mock of the request type from this builder.

`<R> R`
`createMock​(IMocksControl control)`

Create mock from the provided mock control using the arguments passed to
 the builder.

`<R> R`
`createMock​(MockType type)`

Create mock of the request type from this builder.

`<R> R`
`createNiceMock()`

Create a nice mock from this builder.

`<R> R`
`createNiceMock​(String name)`

Create a named nice mock from this builder.

`<R> R`
`createStrictMock()`

Create a strict mock from this builder.

`<R> R`
`createStrictMock​(String name)`

Create a named strict mock from this builder.

`IMockBuilder<T>`
`withArgs​(Object... initArgs)`

Defines the arguments to be passed to the constructor of the class.

`IMockBuilder<T>`
`withConstructor()`

Defines the empty constructor should be called.

`IMockBuilder<T>`
`withConstructor​(Class<?>... argTypes)`

Defines the exact argument types for the constructor to use.

`IMockBuilder<T>`
`withConstructor​(Object... initArgs)`

Defines the constructor parameters for the mocked class.

`IMockBuilder<T>`
`withConstructor​(Constructor<?> constructor)`

Defines the constructor to use to instantiate the mock.

`IMockBuilder<T>`
`withConstructor​(ConstructorArgs constructorArgs)`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface org.easymock.IMockBuilder

`mock, mock, mock, mock, mock, mock, niceMock, niceMock, strictMock, strictMock`

- 

  - 

### Constructor Detail

    - 

#### MockBuilder

```
public MockBuilder​(Class<?> toMock)
```

    - 

#### MockBuilder

```
public MockBuilder​(Class<?> toMock,
                   EasyMockSupport support)
```

Used by EasyMockSupport to allow the mock registration in the list of
 controls

Parameters:
`toMock` - The class of the mock to create
`support` - The EasyMockSupport used to create mocks. Null if none

  - 

### Method Detail

    - 

#### addMockedMethod

```
public IMockBuilder<T> addMockedMethod​(Method method)
```

Description copied from interface: `IMockBuilder`
Adds a method to be mocked in the testing class. Each call will add a new
 method to the result mock.

 The method is searched for in the class itself as well as superclasses.

Specified by:
`addMockedMethod` in interface `IMockBuilder<T>`
Parameters:
`method` - method to be mocked
Returns:
this

    - 

#### addMockedMethod

```
public IMockBuilder<T> addMockedMethod​(String methodName)
```

Description copied from interface: `IMockBuilder`
Adds a method to be mocked in the testing class. Each call will add a new
 method to the result mock.

 The method is searched for in the class itself as well as superclasses.

 There must be no overload of the method. You will have to rely on the
 other `addMockedMethod`s in this class if that is the case.

Specified by:
`addMockedMethod` in interface `IMockBuilder<T>`
Parameters:
`methodName` - name of the method to be mocked
Returns:
this

    - 

#### addMockedMethod

```
public IMockBuilder<T> addMockedMethod​(String methodName,
                                       Class<?>... parameterTypes)
```

Description copied from interface: `IMockBuilder`
Adds a method to be mocked in the testing class. Each call will add a new
 method to the result mock.

 The method is searched for in the class itself as well as superclasses.

Specified by:
`addMockedMethod` in interface `IMockBuilder<T>`
Parameters:
`methodName` - name of the method to be mocked
`parameterTypes` - types of the parameters of the method
Returns:
this

    - 

#### addMockedMethods

```
public IMockBuilder<T> addMockedMethods​(String... methodNames)
```

Description copied from interface: `IMockBuilder`
Adds methods to be mocked in the testing class. Same as
 `IMockBuilder.addMockedMethod(String)` but to mock many methods at once.

Specified by:
`addMockedMethods` in interface `IMockBuilder<T>`
Parameters:
`methodNames` - names of the methods to be mocked
Returns:
this

    - 

#### addMockedMethods

```
public IMockBuilder<T> addMockedMethods​(Method... methods)
```

Description copied from interface: `IMockBuilder`
Adds methods to be mocked in the testing class. Same as
 `IMockBuilder.addMockedMethod(Method)` but to mock many methods at once.

Specified by:
`addMockedMethods` in interface `IMockBuilder<T>`
Parameters:
`methods` - methods to be mocked
Returns:
this

    - 

#### withConstructor

```
public IMockBuilder<T> withConstructor​(Constructor<?> constructor)
```

Description copied from interface: `IMockBuilder`
Defines the constructor to use to instantiate the mock. It is expected
 that you call `IMockBuilder.withArgs(java.lang.Object...)` with the actual constructor argument
 values after this.

Specified by:
`withConstructor` in interface `IMockBuilder<T>`
Parameters:
`constructor` - the constructor to be called
Returns:
this

    - 

#### withConstructor

```
public IMockBuilder<T> withConstructor​(ConstructorArgs constructorArgs)
```

    - 

#### withConstructor

```
public IMockBuilder<T> withConstructor()
```

Description copied from interface: `IMockBuilder`
Defines the empty constructor should be called.

Specified by:
`withConstructor` in interface `IMockBuilder<T>`
Returns:
this

    - 

#### withConstructor

```
public IMockBuilder<T> withConstructor​(Object... initArgs)
```

Description copied from interface: `IMockBuilder`
Defines the constructor parameters for the mocked class. The builder will
 automatically find a constructor with compatible argument types. This
 throws an exception if there is more than one constructor which would
 accept the given parameters.

Specified by:
`withConstructor` in interface `IMockBuilder<T>`
Parameters:
`initArgs` - arguments of the constructor
Returns:
this

    - 

#### withConstructor

```
public IMockBuilder<T> withConstructor​(Class<?>... argTypes)
```

Description copied from interface: `IMockBuilder`
Defines the exact argument types for the constructor to use. It is
 expected that you call `IMockBuilder.withArgs(java.lang.Object...)` with the actual constructor
 argument values after this.

Specified by:
`withConstructor` in interface `IMockBuilder<T>`
Parameters:
`argTypes` - the exact argument types of the constructor
Returns:
this

    - 

#### withArgs

```
public IMockBuilder<T> withArgs​(Object... initArgs)
```

Description copied from interface: `IMockBuilder`
Defines the arguments to be passed to the constructor of the class. The
 types of the arguments must match those previously defined with
 `IMockBuilder.withConstructor(Class...)` or
 `IMockBuilder.withConstructor(Constructor)`.

Specified by:
`withArgs` in interface `IMockBuilder<T>`
Parameters:
`initArgs` - the arguments to pass to the constructor
Returns:
this

    - 

#### createMock

```
public <R> R createMock​(MockType type)
```

Description copied from interface: `IMockBuilder`
Create mock of the request type from this builder. The same builder can be called to
 create multiple mocks.

Specified by:
`createMock` in interface `IMockBuilder<T>`
Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`type` - the mock type
Returns:
the newly created mock

    - 

#### createMock

```
public <R> R createMock​(String name,
                        MockType type)
```

Description copied from interface: `IMockBuilder`
Create a named mock of the request type from this builder. The same builder can be
 called to create multiple mocks.

Specified by:
`createMock` in interface `IMockBuilder<T>`
Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
`type` - the mock type
Returns:
the newly created mock

    - 

#### createMock

```
public <R> R createMock​(IMocksControl control)
```

Description copied from interface: `IMockBuilder`
Create mock from the provided mock control using the arguments passed to
 the builder.

Specified by:
`createMock` in interface `IMockBuilder<T>`
Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`control` - `IMocksControl` used to create the object
Returns:
the newly created mock

    - 

#### createMock

```
public <R> R createMock()
```

Description copied from interface: `IMockBuilder`
Create a default mock from this builder. The same builder can be called
 to create multiple mocks.

Specified by:
`createMock` in interface `IMockBuilder<T>`
Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Returns:
the newly created mock

    - 

#### createNiceMock

```
public <R> R createNiceMock()
```

Description copied from interface: `IMockBuilder`
Create a nice mock from this builder. The same builder can be called to
 create multiple mocks.

Specified by:
`createNiceMock` in interface `IMockBuilder<T>`
Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Returns:
the newly created mock

    - 

#### createStrictMock

```
public <R> R createStrictMock()
```

Description copied from interface: `IMockBuilder`
Create a strict mock from this builder. The same builder can be called to
 create multiple mocks.

Specified by:
`createStrictMock` in interface `IMockBuilder<T>`
Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Returns:
the newly created mock

    - 

#### createMock

```
public <R> R createMock​(String name,
                        IMocksControl control)
```

Description copied from interface: `IMockBuilder`
Create named mock from the provided mock control using the arguments
 passed to the builder.

Specified by:
`createMock` in interface `IMockBuilder<T>`
Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
`control` - `IMocksControl` used to create the object
Returns:
the newly created mock

    - 

#### createMock

```
public <R> R createMock​(String name)
```

Description copied from interface: `IMockBuilder`
Create named mock from the provided mock control using the arguments
 passed to the builder.

Specified by:
`createMock` in interface `IMockBuilder<T>`
Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
Returns:
the newly created mock

    - 

#### createNiceMock

```
public <R> R createNiceMock​(String name)
```

Description copied from interface: `IMockBuilder`
Create a named nice mock from this builder. The same builder can be
 called to create multiple mocks.

Specified by:
`createNiceMock` in interface `IMockBuilder<T>`
Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
Returns:
the newly created mock

    - 

#### createStrictMock

```
public <R> R createStrictMock​(String name)
```

Description copied from interface: `IMockBuilder`
Create a named strict mock from this builder. The same builder can be
 called to create multiple mocks.

Specified by:
`createStrictMock` in interface `IMockBuilder<T>`
Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
Returns:
the newly created mock