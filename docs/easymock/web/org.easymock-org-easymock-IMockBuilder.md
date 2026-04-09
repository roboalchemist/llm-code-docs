Module org.easymock
Package org.easymock

## Interface IMockBuilder<T>

- 

Type Parameters:
`T` - type of the object being created

All Known Implementing Classes:
`MockBuilder`

---

```
public interface IMockBuilder<T>
```

Helps the creation of partial mocks with `EasyMock`.

 

 Example of usage:

 

```

 public class MyClass {
     public MyClass(A a, B b) {
     }
 }

 public class MyClassTest {
     @Test
     public void testFoo() throws Exception {
         IMocksControl mockControl = createControl();
         A a = mockControl.createMock(A.class);
         B b = mockControl.createMock(B.class);

         MyClass myClass = createMockBuilder(MyClass.class)
                 .withConstructor(a, b).createMock(mockControl);

         // Set the expectations of A and B and test some method in MyClass
     }
 }
 
```

 

 This class also has support for partial mocks as shown by the example below:

 

```

 public class MyMockedClass {
     // Empty class is also valid for IMockBuilder.
     public MyMockedClass() {
     }

     public void foo(int a) {
         blah(a);
         bleh();
     }

     public void blah(int a) {
     }

     public void bleh() {
     }
 }

 public class MyMockedClassTest {
     @Test
     public void testFoo() throws Exception {
         MyMockedClass myMockedClass = createMockBuilder(MyMockedClass.class)
                 .withConstructor().addMockedMethod("blah", int.class)
                 .addMockedMethod("bleh").createMock();

         // These are the expectations.
         myMockedClass.blah(1);
         myMockedClass.bleh();
         replay(myMockedClass);

         myMockedClass.foo(1);
         verify(myMockedClass);
     }
 }
 
```

 

 Warning: There may be ambiguities when there are two different constructors
 with compatible types. For instance:

 

```

 public class A {
 }

 public class B extends A {
 }

 public class ClassWithAmbiguity {
     public ClassWithAmbiguity(A a) {
     }

     public ClassWithAmbiguity(B b) {
     }
 }
 
```

 will cause problems if using `withConstructor(Object...)`. To solve
 this, you can explicitly define the constructor parameter types to use by
 calling `withConstructor(Class...)` and then
 `withArgs(Object...)`, like this:

 

```

 createMockBuilder(MyMockedClass.class).withConstructor(A.class).withArgs(
         new A()).createMock();
 
```

Author:
Henri Tremblay

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods Default Methods 

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

`default <R> R`
`mock()`

Create a default mock from this builder.

`default <R> R`
`mock​(String name)`

Create named mock from the provided mock control using the arguments
 passed to the builder.

`default <R> R`
`mock​(String name,
    IMocksControl control)`

Create named mock from the provided mock control using the arguments
 passed to the builder.

`default <R> R`
`mock​(String name,
    MockType type)`

Create a named mock of the request type from this builder.

`default <R> R`
`mock​(IMocksControl control)`

Create mock from the provided mock control using the arguments passed to
 the builder.

`default <R> R`
`mock​(MockType type)`

Create mock of the request type from this builder.

`default <R> R`
`niceMock()`

Create a nice mock from this builder.

`default <R> R`
`niceMock​(String name)`

Create a named nice mock from this builder.

`default <R> R`
`strictMock()`

Create a strict mock from this builder.

`default <R> R`
`strictMock​(String name)`

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

- 

  - 

### Method Detail

    - 

#### addMockedMethod

```
IMockBuilder<T> addMockedMethod​(Method method)
```

Adds a method to be mocked in the testing class. Each call will add a new
 method to the result mock.

 The method is searched for in the class itself as well as superclasses.

Parameters:
`method` - method to be mocked
Returns:
this

    - 

#### addMockedMethod

```
IMockBuilder<T> addMockedMethod​(String methodName)
```

Adds a method to be mocked in the testing class. Each call will add a new
 method to the result mock.

 The method is searched for in the class itself as well as superclasses.

 There must be no overload of the method. You will have to rely on the
 other `addMockedMethod`s in this class if that is the case.

Parameters:
`methodName` - name of the method to be mocked
Returns:
this

    - 

#### addMockedMethod

```
IMockBuilder<T> addMockedMethod​(String methodName,
                                Class<?>... parameterTypes)
```

Adds a method to be mocked in the testing class. Each call will add a new
 method to the result mock.

 The method is searched for in the class itself as well as superclasses.

Parameters:
`methodName` - name of the method to be mocked
`parameterTypes` - types of the parameters of the method
Returns:
this

    - 

#### addMockedMethods

```
IMockBuilder<T> addMockedMethods​(String... methodNames)
```

Adds methods to be mocked in the testing class. Same as
 `addMockedMethod(String)` but to mock many methods at once.

Parameters:
`methodNames` - names of the methods to be mocked
Returns:
this

    - 

#### addMockedMethods

```
IMockBuilder<T> addMockedMethods​(Method... methods)
```

Adds methods to be mocked in the testing class. Same as
 `addMockedMethod(Method)` but to mock many methods at once.

Parameters:
`methods` - methods to be mocked
Returns:
this

    - 

#### withConstructor

```
IMockBuilder<T> withConstructor​(Constructor<?> constructor)
```

Defines the constructor to use to instantiate the mock. It is expected
 that you call `withArgs(java.lang.Object...)` with the actual constructor argument
 values after this.

Parameters:
`constructor` - the constructor to be called
Returns:
this

    - 

#### withConstructor

```
IMockBuilder<T> withConstructor()
```

Defines the empty constructor should be called.

Returns:
this

    - 

#### withConstructor

```
IMockBuilder<T> withConstructor​(Object... initArgs)
```

Defines the constructor parameters for the mocked class. The builder will
 automatically find a constructor with compatible argument types. This
 throws an exception if there is more than one constructor which would
 accept the given parameters.

Parameters:
`initArgs` - arguments of the constructor
Returns:
this

    - 

#### withConstructor

```
IMockBuilder<T> withConstructor​(Class<?>... argTypes)
```

Defines the exact argument types for the constructor to use. It is
 expected that you call `withArgs(java.lang.Object...)` with the actual constructor
 argument values after this.

Parameters:
`argTypes` - the exact argument types of the constructor
Returns:
this

    - 

#### withArgs

```
IMockBuilder<T> withArgs​(Object... initArgs)
```

Defines the arguments to be passed to the constructor of the class. The
 types of the arguments must match those previously defined with
 `withConstructor(Class...)` or
 `withConstructor(Constructor)`.

Parameters:
`initArgs` - the arguments to pass to the constructor
Returns:
this

    - 

#### createMock

```
<R> R createMock​(MockType type)
```

Create mock of the request type from this builder. The same builder can be called to
 create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`type` - the mock type
Returns:
the newly created mock
Since:
3.2

    - 

#### createStrictMock

```
<R> R createStrictMock()
```

Create a strict mock from this builder. The same builder can be called to
 create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Returns:
the newly created mock

    - 

#### createMock

```
<R> R createMock()
```

Create a default mock from this builder. The same builder can be called
 to create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Returns:
the newly created mock

    - 

#### createNiceMock

```
<R> R createNiceMock()
```

Create a nice mock from this builder. The same builder can be called to
 create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Returns:
the newly created mock

    - 

#### createMock

```
<R> R createMock​(IMocksControl control)
```

Create mock from the provided mock control using the arguments passed to
 the builder.

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
<R> R createMock​(String name,
                 MockType type)
```

Create a named mock of the request type from this builder. The same builder can be
 called to create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
`type` - the mock type
Returns:
the newly created mock
Since:
3.2

    - 

#### createStrictMock

```
<R> R createStrictMock​(String name)
```

Create a named strict mock from this builder. The same builder can be
 called to create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
Returns:
the newly created mock

    - 

#### createMock

```
<R> R createMock​(String name)
```

Create named mock from the provided mock control using the arguments
 passed to the builder.

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
<R> R createNiceMock​(String name)
```

Create a named nice mock from this builder. The same builder can be
 called to create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
Returns:
the newly created mock

    - 

#### createMock

```
<R> R createMock​(String name,
                 IMocksControl control)
```

Create named mock from the provided mock control using the arguments
 passed to the builder.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
`control` - `IMocksControl` used to create the object
Returns:
the newly created mock

    - 

#### mock

```
default <R> R mock​(MockType type)
```

Create mock of the request type from this builder. The same builder can be called to
 create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`type` - the mock type
Returns:
the newly created mock
Since:
4.0

    - 

#### strictMock

```
default <R> R strictMock()
```

Create a strict mock from this builder. The same builder can be called to
 create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Returns:
the newly created mock
Since:
4.0

    - 

#### mock

```
default <R> R mock()
```

Create a default mock from this builder. The same builder can be called
 to create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Returns:
the newly created mock
Since:
4.0

    - 

#### niceMock

```
default <R> R niceMock()
```

Create a nice mock from this builder. The same builder can be called to
 create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Returns:
the newly created mock
Since:
4.0

    - 

#### mock

```
default <R> R mock​(IMocksControl control)
```

Create mock from the provided mock control using the arguments passed to
 the builder.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`control` - `IMocksControl` used to create the object
Returns:
the newly created mock
Since:
4.0

    - 

#### mock

```
default <R> R mock​(String name,
                   MockType type)
```

Create a named mock of the request type from this builder. The same builder can be
 called to create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
`type` - the mock type
Returns:
the newly created mock
Since:
4.0

    - 

#### strictMock

```
default <R> R strictMock​(String name)
```

Create a named strict mock from this builder. The same builder can be
 called to create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
Returns:
the newly created mock
Since:
4.0

    - 

#### mock

```
default <R> R mock​(String name)
```

Create named mock from the provided mock control using the arguments
 passed to the builder.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
Returns:
the newly created mock
Since:
4.0

    - 

#### niceMock

```
default <R> R niceMock​(String name)
```

Create a named nice mock from this builder. The same builder can be
 called to create multiple mocks.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
Returns:
the newly created mock
Since:
4.0

    - 

#### mock

```
default <R> R mock​(String name,
                   IMocksControl control)
```

Create named mock from the provided mock control using the arguments
 passed to the builder.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the mock name
`control` - `IMocksControl` used to create the object
Returns:
the newly created mock
Since:
4.0