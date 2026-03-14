Module org.easymock
Package org.easymock

## Class EasyMockSupport

- java.lang.Object

- 

  - org.easymock.EasyMockSupport

- 

---

```
public class EasyMockSupport
extends Object
```

Helper class to keep track of mocks easily. See EasyMock
 documentation and SupportTest sample.
 

 Example of usage:

 

```

 public class SupportTest extends EasyMockSupport {
     @Test
     public void test() {
         firstMock = createMock(A.class);
         secondMock = createMock(B.class);

         replayAll(); // put both mocks in replay mode

         // ... use mocks ..

         verifyAll(); // verify both mocks
     }
 }
 
```

Author:
Henri Tremblay

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field
Description

`protected List<IMocksControl>`
`controls`

List of all controls created

  - 

### Constructor Summary

Constructors 

Constructor
Description

`EasyMockSupport()`
 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`IMocksControl`
`createControl()`

Creates a control, order checking is disabled by default.

`IMocksControl`
`createControl​(MockType type)`

Creates a control of the given type.

`<T,​R>
R`
`createMock​(Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default.

`<T,​R>
R`
`createMock​(String name,
          Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default.

`<T,​R>
R`
`createMock​(String name,
          MockType type,
          Class<T> toMock)`

Creates a mock object of the requested type that implements the given interface or extends
 the given class

`<T,​R>
R`
`createMock​(MockType type,
          Class<T> toMock)`

Creates a mock object of the requested type that implements the given interface or extends
 the given class

`<T> IMockBuilder<T>`
`createMockBuilder​(Class<T> toMock)`

Create a mock builder allowing to create a partial mock for the given
 class or interface.

`IMocksControl`
`createNiceControl()`

Creates a control, order checking is disabled by default, and the mock
 objects created by this control will return `0`,
 `null` or `false` for unexpected invocations.

`<T,​R>
R`
`createNiceMock​(Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

`<T,​R>
R`
`createNiceMock​(String name,
              Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

`IMocksControl`
`createStrictControl()`

Creates a control, order checking is enabled by default.

`<T,​R>
R`
`createStrictMock​(Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is enabled by default.

`<T,​R>
R`
`createStrictMock​(String name,
                Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is enabled by default.

`static <T,​R extends T>
Class<R>`
`getMockedClass​(T possibleMock)`

Will return the class that was mocked if it's a mock or `null` otherwise.

`static void`
`injectMocks​(Object obj)`

Inject a mock to every fields annotated with `Mock` on the class passed
 in parameter.

`static boolean`
`isAMock​(Object possibleMock)`

Tells if this mock is an EasyMock mock.

`<T,​R>
R`
`mock​(Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default.

`<T,​R>
R`
`mock​(String name,
    Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default.

`<T,​R>
R`
`mock​(String name,
    MockType type,
    Class<T> toMock)`

Creates a mock object of the requested type that implements the given interface or extends
 the given class

`<T,​R>
R`
`mock​(MockType type,
    Class<T> toMock)`

Creates a mock object of the requested type that implements the given interface or extends
 the given class

`<T,​R>
R`
`niceMock​(Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

`<T,​R>
R`
`niceMock​(String name,
        Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

`<T> IMockBuilder<T>`
`partialMockBuilder​(Class<T> toMock)`

Create a mock builder allowing to create a partial mock for the given
 class or interface.

`void`
`replayAll()`

Switches all registered mock objects (more exactly: the controls of the
 mock objects) to replay mode.

`void`
`resetAll()`

Resets all registered mock objects (more exactly: the controls of the
 mock objects).

`void`
`resetAllToDefault()`

Resets all registered mock objects (more exactly: the controls of the
 mock objects) and turn them to a mock with default behavior.

`void`
`resetAllToNice()`

Resets all registered mock objects (more exactly: the controls of the
 mock objects) and turn them to a mock with nice behavior.

`void`
`resetAllToStrict()`

Resets all registered mock objects (more exactly: the controls of the
 mock objects) and turn them to a mock with strict behavior.

`<T,​R>
R`
`strictMock​(Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is enabled by default.

`<T,​R>
R`
`strictMock​(String name,
          Class<T> toMock)`

Creates a mock object that implements the given interface, order checking
 is enabled by default.

`void`
`verifyAll()`

Verifies all registered mock objects have their expectations met and that no
 unexpected call was performed.

`void`
`verifyAllRecordings()`

Verifies all registered mock objects have their expectations met.

`void`
`verifyAllUnexpectedCalls()`

Verifies that no registered mock objects had
 unexpected calls.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### controls

```
protected final List<IMocksControl> controls
```

List of all controls created

  - 

### Constructor Detail

    - 

#### EasyMockSupport

```
public EasyMockSupport()
```

  - 

### Method Detail

    - 

#### mock

```
public <T,​R> R mock​(Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default.

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Since:
${project.version}

    - 

#### mock

```
public <T,​R> R mock​(String name,
                          Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default.

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the name of the mock object.
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.
Since:
${project.version}

    - 

#### mock

```
public <T,​R> R mock​(MockType type,
                          Class<T> toMock)
```

Creates a mock object of the requested type that implements the given interface or extends
 the given class

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`type` - the type of the mock to be created.
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.
Since:
${project.version}

    - 

#### mock

```
public <T,​R> R mock​(String name,
                          MockType type,
                          Class<T> toMock)
```

Creates a mock object of the requested type that implements the given interface or extends
 the given class

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the name of the mock object.
`type` - the type of the mock to be created.
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.
Since:
${project.version}

    - 

#### strictMock

```
public <T,​R> R strictMock​(Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is enabled by default.

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Since:
${project.version}

    - 

#### strictMock

```
public <T,​R> R strictMock​(String name,
                                Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is enabled by default.

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the name of the mock object.
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.
Since:
${project.version}

    - 

#### niceMock

```
public <T,​R> R niceMock​(Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Since:
${project.version}

    - 

#### niceMock

```
public <T,​R> R niceMock​(String name,
                              Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the name of the mock object.
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.
Since:
${project.version}

    - 

#### partialMockBuilder

```
public <T> IMockBuilder<T> partialMockBuilder​(Class<T> toMock)
```

Create a mock builder allowing to create a partial mock for the given
 class or interface.

Type Parameters:
`T` - the interface that the mock object should implement.
Parameters:
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
a mock builder to create a partial mock
Since:
${project.version}

    - 

#### createMock

```
public <T,​R> R createMock​(MockType type,
                                Class<T> toMock)
```

Creates a mock object of the requested type that implements the given interface or extends
 the given class

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`type` - the type of the mock to be created.
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.

    - 

#### createMock

```
public <T,​R> R createMock​(String name,
                                MockType type,
                                Class<T> toMock)
```

Creates a mock object of the requested type that implements the given interface or extends
 the given class

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the name of the mock object.
`type` - the type of the mock to be created.
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.

    - 

#### createStrictMock

```
public <T,​R> R createStrictMock​(Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is enabled by default.

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.

    - 

#### createStrictMock

```
public <T,​R> R createStrictMock​(String name,
                                      Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is enabled by default.

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the name of the mock object.
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.

    - 

#### createMock

```
public <T,​R> R createMock​(Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default.

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.

    - 

#### createMock

```
public <T,​R> R createMock​(String name,
                                Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default.

Type Parameters:
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
`T` - the interface that the mock object should implement.
Parameters:
`name` - the name of the mock object.
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.

    - 

#### createNiceMock

```
public <T,​R> R createNiceMock​(Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.

    - 

#### createNiceMock

```
public <T,​R> R createNiceMock​(String name,
                                    Class<T> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

Type Parameters:
`T` - the interface that the mock object should implement.
`R` - the returned type. In general T == R but when mocking a generic type, it won't so to be nice with the
            caller, we return a different type
Parameters:
`name` - the name of the mock object.
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.

    - 

#### createStrictControl

```
public IMocksControl createStrictControl()
```

Creates a control, order checking is enabled by default.

Returns:
the control.

    - 

#### createMockBuilder

```
public <T> IMockBuilder<T> createMockBuilder​(Class<T> toMock)
```

Create a mock builder allowing to create a partial mock for the given
 class or interface.

Type Parameters:
`T` - the interface that the mock object should implement.
Parameters:
`toMock` - the class of the interface that the mock object should
            implement.
Returns:
a mock builder to create a partial mock

    - 

#### createControl

```
public IMocksControl createControl​(MockType type)
```

Creates a control of the given type.

Parameters:
`type` - the mock type.
Returns:
the control.
Since:
3.2

    - 

#### createControl

```
public IMocksControl createControl()
```

Creates a control, order checking is disabled by default.

Returns:
the control.

    - 

#### createNiceControl

```
public IMocksControl createNiceControl()
```

Creates a control, order checking is disabled by default, and the mock
 objects created by this control will return `0`,
 `null` or `false` for unexpected invocations.

Returns:
the control.

    - 

#### replayAll

```
public void replayAll()
```

Switches all registered mock objects (more exactly: the controls of the
 mock objects) to replay mode. For details, see the EasyMock
 documentation.

    - 

#### resetAll

```
public void resetAll()
```

Resets all registered mock objects (more exactly: the controls of the
 mock objects). For details, see the EasyMock documentation.

    - 

#### verifyAll

```
public void verifyAll()
```

Verifies all registered mock objects have their expectations met and that no
 unexpected call was performed.
 

 This method as same effect as calling `verifyAllRecordings()`
 followed by `verifyAllUnexpectedCalls()`.

    - 

#### verifyAllRecordings

```
public void verifyAllRecordings()
```

Verifies all registered mock objects have their expectations met.

Since:
3.5

    - 

#### verifyAllUnexpectedCalls

```
public void verifyAllUnexpectedCalls()
```

Verifies that no registered mock objects had
 unexpected calls.

Since:
3.5

    - 

#### resetAllToNice

```
public void resetAllToNice()
```

Resets all registered mock objects (more exactly: the controls of the
 mock objects) and turn them to a mock with nice behavior. For details,
 see the EasyMock documentation.

    - 

#### resetAllToDefault

```
public void resetAllToDefault()
```

Resets all registered mock objects (more exactly: the controls of the
 mock objects) and turn them to a mock with default behavior. For details,
 see the EasyMock documentation.

    - 

#### resetAllToStrict

```
public void resetAllToStrict()
```

Resets all registered mock objects (more exactly: the controls of the
 mock objects) and turn them to a mock with strict behavior. For details,
 see the EasyMock documentation.

    - 

#### injectMocks

```
public static void injectMocks​(Object obj)
```

Inject a mock to every fields annotated with `Mock` on the class passed
 in parameter. Then, inject these mocks to the fields of every class annotated with `TestSubject`.
 

 The rules are
 

     
      - Static and final fields are ignored
     
      - If two mocks have the same field name, return an error
     
      - If a mock has a field name and no matching field is found, return an error
 

 Then, ignoring all fields and mocks matched by field name
 

     
      - If a mock without field name can be assigned to a field, do it. The same mock can be assigned more than once
     
      - If no mock can be assigned to a field, skip the field silently
     
      - If the mock cannot be assigned to any field, skip the mock silently
     
      - If two mocks can be assigned to the same field, return an error
 

 Fields are searched recursively on the superclasses
 

 **Note:** If the parameter extends `EasyMockSupport`, the mocks will be created using it to allow
 `replayAll/verifyAll` to work afterwards

Parameters:
`obj` - the object on which to inject mocks
Since:
3.2

    - 

#### getMockedClass

```
public static <T,​R extends T> Class<R> getMockedClass​(T possibleMock)
```

Will return the class that was mocked if it's a mock or `null` otherwise.

Type Parameters:
`T` - type of the possible mock
`R` - type of mocked class
Parameters:
`possibleMock` - mock we want the type of
Returns:
the mocked type or null of not a mock
Since:
3.5

    - 

#### isAMock

```
public static boolean isAMock​(Object possibleMock)
```

Tells if this mock is an EasyMock mock.

Parameters:
`possibleMock` - the object that might be a mock
Returns:
true if it's a mock