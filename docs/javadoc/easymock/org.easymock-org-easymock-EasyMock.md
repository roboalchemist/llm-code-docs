Module org.easymock
Package org.easymock

## Class EasyMock

- java.lang.Object

- 

  - org.easymock.EasyMock

- 

---

```
public class EasyMock
extends Object
```

Main EasyMock class. Contains methods to create, replay and verify mocks and
 a list of standard matchers.

Author:
OFFIS, Tammo Freese, Henri Tremblay

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field
Description

`static String`
`DISABLE_CLASS_MOCKING`

Since EasyMock 3.0, EasyMock can perform class mocking directly without
 using the class extension.

`static String`
`ENABLE_THREAD_SAFETY_CHECK_BY_DEFAULT`

Since EasyMock 2.4, by default, a mock wasn't allowed to be called in
 multiple threads unless it was made thread-safe (See
 `makeThreadSafe(Object, boolean)` method).

`static String`
`NOT_THREAD_SAFE_BY_DEFAULT`

Since EasyMock 2.5, by default a mock is thread-safe.

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method
Description

`static boolean`
`and​(boolean first,
   boolean second)`

Expects a boolean that matches both given expectations.

`static byte`
`and​(byte first,
   byte second)`

Expects a byte that matches both given expectations.

`static char`
`and​(char first,
   char second)`

Expects a char that matches both given expectations.

`static double`
`and​(double first,
   double second)`

Expects a double that matches both given expectations.

`static float`
`and​(float first,
   float second)`

Expects a float that matches both given expectations.

`static int`
`and​(int first,
   int second)`

Expects an int that matches both given expectations.

`static long`
`and​(long first,
   long second)`

Expects a long that matches both given expectations.

`static short`
`and​(short first,
   short second)`

Expects a short that matches both given expectations.

`static <T> T`
`and​(T first,
   T second)`

Expects an Object that matches both given expectations.

`static boolean`
`anyBoolean()`

Expects any boolean argument.

`static byte`
`anyByte()`

Expects any byte argument.

`static char`
`anyChar()`

Expects any char argument.

`static double`
`anyDouble()`

Expects any double argument.

`static float`
`anyFloat()`

Expects any float argument.

`static int`
`anyInt()`

Expects any int argument.

`static long`
`anyLong()`

Expects any long argument.

`static <T> T`
`anyObject()`

Expects any Object argument.

`static <T> T`
`anyObject​(Class<T> clazz)`

Expects any Object argument.

`static short`
`anyShort()`

Expects any short argument.

`static String`
`anyString()`

Expect any string whatever its content is.

`static boolean[]`
`aryEq​(boolean[] value)`

Expects a boolean array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

`static byte[]`
`aryEq​(byte[] value)`

Expects a byte array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

`static char[]`
`aryEq​(char[] value)`

Expects a char array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

`static double[]`
`aryEq​(double[] value)`

Expects a double array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

`static float[]`
`aryEq​(float[] value)`

Expects a float array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

`static int[]`
`aryEq​(int[] value)`

Expects an int array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

`static long[]`
`aryEq​(long[] value)`

Expects a long array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

`static short[]`
`aryEq​(short[] value)`

Expects a short array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

`static <T> T[]`
`aryEq​(T[] value)`

Expects an Object array that is equal to the given array, i.e. it has to
 have the same type, length, and each element has to be equal.

`static <T> T`
`capture​(Capture<T> captured)`

Expect any object but captures it for later use.

`static boolean`
`captureBoolean​(Capture<Boolean> captured)`

Expect any boolean but captures it for later use.

`static byte`
`captureByte​(Capture<Byte> captured)`

Expect any byte but captures it for later use.

`static char`
`captureChar​(Capture<Character> captured)`

Expect any char but captures it for later use.

`static double`
`captureDouble​(Capture<Double> captured)`

Expect any double but captures it for later use.

`static float`
`captureFloat​(Capture<Float> captured)`

Expect any float but captures it for later use.

`static int`
`captureInt​(Capture<Integer> captured)`

Expect any int but captures it for later use.

`static long`
`captureLong​(Capture<Long> captured)`

Expect any long but captures it for later use.

`static void`
`checkIsUsedInOneThread​(Object mock,
                      boolean shouldBeUsedInOneThread)`

Tell that the mock should be used in only one thread.

`static void`
`checkOrder​(Object mock,
          boolean state)`

Switches order checking of the given mock object (more exactly: the
 control of the mock object) the on and off.

`static <T> T`
`cmp​(T value,
   Comparator<? super T> comparator,
   LogicalOperator operator)`

Expects an argument that will be compared using the provided comparator.

`static <T extends Comparable<T>>
T`
`cmpEq​(T value)`

Expects a comparable argument equals to the given value according to
 their compareTo method.

`static String`
`contains​(String substring)`

Expects a string that contains the given substring.

`static IMocksControl`
`createControl()`

Creates a control, order checking is disabled by default.

`static IMocksControl`
`createControl​(MockType type)`

Creates a control of the requested type.

`static <T> T`
`createMock​(Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default.

`static <T> T`
`createMock​(String name,
          Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default.

`static <T> T`
`createMock​(String name,
          MockType type,
          Class<?> toMock)`

Creates a mock object, of the requested type and name, that implements the given interface
 or extends the given class

`static <T> T`
`createMock​(MockType type,
          Class<?> toMock)`

Creates a mock object, of the requested type, that implements the given interface
 or extends the given class.

`static <T> IMockBuilder<T>`
`createMockBuilder​(Class<?> toMock)`

Create a mock builder allowing to create a partial mock for the given
 class or interface.

`static IMocksControl`
`createNiceControl()`

Creates a control, order checking is disabled by default, and the mock
 objects created by this control will return `0`,
 `null` or `false` for unexpected invocations.

`static <T> T`
`createNiceMock​(Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

`static <T> T`
`createNiceMock​(String name,
              Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

`static IMocksControl`
`createStrictControl()`

Creates a control, order checking is enabled by default.

`static <T> T`
`createStrictMock​(Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is enabled by default.

`static <T> T`
`createStrictMock​(String name,
                Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is enabled by default.

`static String`
`endsWith​(String suffix)`

Expects a string that ends with the given suffix.

`static boolean`
`eq​(boolean value)`

Expects a boolean that is equal to the given value.

`static byte`
`eq​(byte value)`

Expects a byte that is equal to the given value.

`static char`
`eq​(char value)`

Expects a char that is equal to the given value.

`static double`
`eq​(double value)`

Expects a double that is equal to the given value.

`static double`
`eq​(double value,
  double delta)`

Expects a double that has an absolute difference to the given value that
 is less than the given delta.

`static float`
`eq​(float value)`

Expects a float that is equal to the given value.

`static float`
`eq​(float value,
  float delta)`

Expects a float that has an absolute difference to the given value that
 is less than the given delta.

`static int`
`eq​(int value)`

Expects an int that is equal to the given value.

`static long`
`eq​(long value)`

Expects a long that is equal to the given value.

`static short`
`eq​(short value)`

Expects a short that is equal to the given value.

`static <T> T`
`eq​(T value)`

Expects an Object that is equal to the given value.

`static <T> IExpectationSetters<T>`
`expect​(T value)`

Returns the expectation setter for the last expected invocation in the
 current thread.

`static <T> IExpectationSetters<T>`
`expectLastCall()`

Returns the expectation setter for the last expected invocation in the
 current thread.

`static String`
`find​(String regex)`

Expects a string that contains a substring that matches the given regular
 expression.

`static byte`
`geq​(byte value)`

Expects a byte argument greater than or equal to the given value.

`static double`
`geq​(double value)`

Expects a double argument greater than or equal to the given value.

`static float`
`geq​(float value)`

Expects a float argument greater than or equal to the given value.

`static int`
`geq​(int value)`

Expects an int argument greater than or equal to the given value.

`static long`
`geq​(long value)`

Expects a long argument greater than or equal to the given value.

`static short`
`geq​(short value)`

Expects a short argument greater than or equal to the given value.

`static <T extends Comparable<T>>
T`
`geq​(T value)`

Expects a comparable argument greater than or equal the given value.

`static <T> T`
`getCurrentArgument​(int index)`
 

`static Object[]`
`getCurrentArguments()`

Returns the arguments of the current mock method call, if inside an
 `IAnswer` callback - be careful here, reordering parameters of
 method changes the semantics of your tests.

`static String`
`getEasyMockProperty​(String key)`

Get the current value for an EasyMock property

`static byte`
`gt​(byte value)`

Expects a byte argument greater than the given value.

`static double`
`gt​(double value)`

Expects a double argument greater than the given value.

`static float`
`gt​(float value)`

Expects a float argument greater than the given value.

`static int`
`gt​(int value)`

Expects an int argument greater than the given value.

`static long`
`gt​(long value)`

Expects a long argument greater than the given value.

`static short`
`gt​(short value)`

Expects a short argument greater than the given value.

`static <T extends Comparable<T>>
T`
`gt​(T value)`

Expects a comparable argument greater than the given value.

`static <T> T`
`isA​(Class<T> clazz)`

Expects an object implementing the given class.

`static <T> T`
`isNull()`

Expects null.

`static <T> T`
`isNull​(Class<T> clazz)`

Expects null.

`static byte`
`leq​(byte value)`

Expects a byte argument less than or equal to the given value.

`static double`
`leq​(double value)`

Expects a double argument less than or equal to the given value.

`static float`
`leq​(float value)`

Expects a float argument less than or equal to the given value.

`static int`
`leq​(int value)`

Expects an int argument less than or equal to the given value.

`static long`
`leq​(long value)`

Expects a long argument less than or equal to the given value.

`static short`
`leq​(short value)`

Expects a short argument less than or equal to the given value.

`static <T extends Comparable<T>>
T`
`leq​(T value)`

Expects a comparable argument less than or equal the given value.

`static byte`
`lt​(byte value)`

Expects a byte argument less than the given value.

`static double`
`lt​(double value)`

Expects a double argument less than the given value.

`static float`
`lt​(float value)`

Expects a float argument less than the given value.

`static int`
`lt​(int value)`

Expects an int argument less than the given value.

`static long`
`lt​(long value)`

Expects a long argument less than the given value.

`static short`
`lt​(short value)`

Expects a short argument less than the given value.

`static <T extends Comparable<T>>
T`
`lt​(T value)`

Expects a comparable argument less than the given value.

`static void`
`makeThreadSafe​(Object mock,
              boolean threadSafe)`

By default, a mock is thread safe (unless
 `NOT_THREAD_SAFE_BY_DEFAULT` is set).

`static String`
`matches​(String regex)`

Expects a string that matches the given regular expression.

`static <T> T`
`mock​(Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default.

`static <T> T`
`mock​(String name,
    Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default.

`static <T> T`
`mock​(String name,
    MockType type,
    Class<?> toMock)`

Creates a mock object, of the requested type and name, that implements the given interface
 or extends the given class

`static <T> T`
`mock​(MockType type,
    Class<?> toMock)`

Creates a mock object, of the requested type, that implements the given interface
 or extends the given class

`static <T> Capture<T>`
`newCapture()`

Create a new capture instance that will keep only the last captured value.

`static <T> Capture<T>`
`newCapture​(UnaryOperator<T> transform)`

Create a new capture instance with a specific and a specific transformation
 function to change the values into a different value.

`static <T> Capture<T>`
`newCapture​(CaptureType type)`

Create a new capture instance with a specific `CaptureType`

`static <T> Capture<T>`
`newCapture​(CaptureType type,
          UnaryOperator<T> transform)`

Create a new capture instance with a specific `CaptureType`
 and a specific transformation function to change the values into a different value.

`static <T> T`
`niceMock​(Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

`static <T> T`
`niceMock​(String name,
        Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

`static boolean`
`not​(boolean first)`

Expects a boolean that does not match the given expectation.

`static byte`
`not​(byte first)`

Expects a byte that does not match the given expectation.

`static char`
`not​(char first)`

Expects a char that does not match the given expectation.

`static double`
`not​(double first)`

Expects a double that does not match the given expectation.

`static float`
`not​(float first)`

Expects a float that does not match the given expectation.

`static int`
`not​(int first)`

Expects an int that does not match the given expectation.

`static long`
`not​(long first)`

Expects a long that does not match the given expectation.

`static short`
`not​(short first)`

Expects a short that does not match the given expectation.

`static <T> T`
`not​(T first)`

Expects an Object that does not match the given expectation.

`static <T> T`
`notNull()`

Expects not null.

`static <T> T`
`notNull​(Class<T> clazz)`

Expects not null.

`static boolean`
`or​(boolean first,
  boolean second)`

Expects a boolean that matches one of the given expectations.

`static byte`
`or​(byte first,
  byte second)`

Expects a byte that matches one of the given expectations.

`static char`
`or​(char first,
  char second)`

Expects a char that matches one of the given expectations.

`static double`
`or​(double first,
  double second)`

Expects a double that matches one of the given expectations.

`static float`
`or​(float first,
  float second)`

Expects a float that matches one of the given expectations.

`static int`
`or​(int first,
  int second)`

Expects an int that matches one of the given expectations.

`static long`
`or​(long first,
  long second)`

Expects a long that matches one of the given expectations.

`static short`
`or​(short first,
  short second)`

Expects a short that matches one of the given expectations.

`static <T> T`
`or​(T first,
  T second)`

Expects an Object that matches one of the given expectations.

`static <T> IMockBuilder<T>`
`partialMockBuilder​(Class<?> toMock)`

Create a mock builder allowing to create a partial mock for the given
 class or interface.

`static void`
`replay​(Object... mocks)`

Switches the given mock objects (more exactly: the controls of the mock
 objects) to replay mode.

`static void`
`reportMatcher​(IArgumentMatcher matcher)`

Reports an argument matcher.

`static void`
`reset​(Object... mocks)`

Resets the given mock objects (more exactly: the controls of the mock
 objects).

`static void`
`resetToDefault​(Object... mocks)`

Resets the given mock objects (more exactly: the controls of the mock
 objects) and turn them to a mock with default behavior.

`static void`
`resetToNice​(Object... mocks)`

Resets the given mock objects (more exactly: the controls of the mock
 objects) and turn them to a mock with nice behavior.

`static void`
`resetToStrict​(Object... mocks)`

Resets the given mock objects (more exactly: the controls of the mock
 objects) and turn them to a mock with strict behavior.

`static <T> T`
`same​(T value)`

Expects an Object that is the same as the given value.

`static String`
`setEasyMockProperty​(String key,
                   String value)`

Set a property to modify the default EasyMock behavior.

`static String`
`startsWith​(String prefix)`

Expects a string that starts with the given prefix.

`static <T> T`
`strictMock​(Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is enabled by default.

`static <T> T`
`strictMock​(String name,
          Class<?> toMock)`

Creates a mock object that implements the given interface, order checking
 is enabled by default.

`static void`
`verify​(Object... mocks)`

Verifies that all expectations were met and that no unexpected
 call was performed on the mock objects.

`static void`
`verifyRecording​(Object... mocks)`

Verifies that all expectations were met.

`static void`
`verifyUnexpectedCalls​(Object... mocks)`

Verifies that no unexpected call was performed.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### ENABLE_THREAD_SAFETY_CHECK_BY_DEFAULT

```
public static final String ENABLE_THREAD_SAFETY_CHECK_BY_DEFAULT
```

Since EasyMock 2.4, by default, a mock wasn't allowed to be called in
 multiple threads unless it was made thread-safe (See
 `makeThreadSafe(Object, boolean)` method). Since EasyMock 2.5,
 this isn't the default anymore. For backward compatibility, this property
 can bring EasyMock 2.4 behavior back.

See Also:
Constant Field Values

    - 

#### NOT_THREAD_SAFE_BY_DEFAULT

```
public static final String NOT_THREAD_SAFE_BY_DEFAULT
```

Since EasyMock 2.5, by default a mock is thread-safe. For backward
 compatibility, this property can change the default. A given mock still
 can be made thread-safe by calling
 `makeThreadSafe(Object, boolean)`.

See Also:
Constant Field Values

    - 

#### DISABLE_CLASS_MOCKING

```
public static final String DISABLE_CLASS_MOCKING
```

Since EasyMock 3.0, EasyMock can perform class mocking directly without
 using the class extension. If you want to disable any class mocking, turn
 this to true.

See Also:
Constant Field Values

  - 

### Method Detail

    - 

#### mock

```
public static <T> T mock​(Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default.

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Since:
3.4

    - 

#### mock

```
public static <T> T mock​(String name,
                         Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default.

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`name` - the name of the mock object.
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.
Since:
3.4

    - 

#### mock

```
public static <T> T mock​(MockType type,
                         Class<?> toMock)
```

Creates a mock object, of the requested type, that implements the given interface
 or extends the given class

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`type` - the type of the mock to be created.
`toMock` - the class or interface that should be mocked.
Returns:
the mock object
Since:
3.4

    - 

#### mock

```
public static <T> T mock​(String name,
                         MockType type,
                         Class<?> toMock)
```

Creates a mock object, of the requested type and name, that implements the given interface
 or extends the given class

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`name` - the name of the mock object.
`type` - the type of the mock to be created.
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Since:
3.4

    - 

#### strictMock

```
public static <T> T strictMock​(Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is enabled by default.

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Since:
3.4

    - 

#### strictMock

```
public static <T> T strictMock​(String name,
                               Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is enabled by default.

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`name` - the name of the mock object.
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.
Since:
3.4

    - 

#### niceMock

```
public static <T> T niceMock​(Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Since:
3.4

    - 

#### niceMock

```
public static <T> T niceMock​(String name,
                             Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`name` - the name of the mock object.
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.
Since:
3.4

    - 

#### partialMockBuilder

```
public static <T> IMockBuilder<T> partialMockBuilder​(Class<?> toMock)
```

Create a mock builder allowing to create a partial mock for the given
 class or interface.

Type Parameters:
`T` - the class that the mock object should extend.
Parameters:
`toMock` - the class or interface that should be mocked.
Returns:
a mock builder to create a partial mock
Since:
3.4

    - 

#### createMock

```
public static <T> T createMock​(MockType type,
                               Class<?> toMock)
```

Creates a mock object, of the requested type, that implements the given interface
 or extends the given class.
 

 **Note:** This is the old version of `mock(MockType, Class)`, which is more completion friendly

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`type` - the type of the mock to be created.
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Since:
3.2

    - 

#### createMock

```
public static <T> T createMock​(String name,
                               MockType type,
                               Class<?> toMock)
```

Creates a mock object, of the requested type and name, that implements the given interface
 or extends the given class
 

 **Note:** This is the old version of `mock(String, MockType, Class)`, which is more completion friendly

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`name` - the name of the mock object.
`type` - the type of the mock to be created.
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Since:
3.2

    - 

#### createStrictMock

```
public static <T> T createStrictMock​(Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is enabled by default.
 

 **Note:** This is the old version of `strictMock(Class)`, which is more completion friendly

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.

    - 

#### createStrictMock

```
public static <T> T createStrictMock​(String name,
                                     Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is enabled by default.
 

 **Note:** This is the old version of `strictMock(String, Class)`, which is more completion friendly

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`name` - the name of the mock object.
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.

    - 

#### createMock

```
public static <T> T createMock​(Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default.
 

 **Note:** This is the old version of `mock(Class)`, which is more completion friendly

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.

    - 

#### createMock

```
public static <T> T createMock​(String name,
                               Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default.
 

 **Note:** This is the old version of `mock(String, Class)`, which is more completion friendly

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`name` - the name of the mock object.
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.

    - 

#### createNiceMock

```
public static <T> T createNiceMock​(Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.
 

 **Note:** This is the old version of `niceMock(Class)`, which is more completion friendly

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.

    - 

#### createNiceMock

```
public static <T> T createNiceMock​(String name,
                                   Class<?> toMock)
```

Creates a mock object that implements the given interface, order checking
 is disabled by default, and the mock object will return `0`,
 `null` or `false` for unexpected invocations.
 

 **Note:** This is the old version of `niceMock(String, Class)`, which is more completion friendly

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`name` - the name of the mock object.
`toMock` - the class or interface that should be mocked.
Returns:
the mock object.
Throws:
`IllegalArgumentException` - if the name is not a valid Java identifier.

    - 

#### createMockBuilder

```
public static <T> IMockBuilder<T> createMockBuilder​(Class<?> toMock)
```

Create a mock builder allowing to create a partial mock for the given
 class or interface.
 

 **Note:** This is the old version of `partialMockBuilder(Class)`, which is more completion friendly

Type Parameters:
`T` - the class or interface that the mock object should extend/implement. It is expected to be of
            class `toMock`.
Parameters:
`toMock` - the class or interface that should be mocked.
Returns:
a mock builder to create a partial mock

    - 

#### createControl

```
public static IMocksControl createControl​(MockType type)
```

Creates a control of the requested type.

Parameters:
`type` - the mock type
Returns:
the control.
Since:
3.2

    - 

#### createStrictControl

```
public static IMocksControl createStrictControl()
```

Creates a control, order checking is enabled by default.

Returns:
the control.

    - 

#### createControl

```
public static IMocksControl createControl()
```

Creates a control, order checking is disabled by default.

Returns:
the control.

    - 

#### createNiceControl

```
public static IMocksControl createNiceControl()
```

Creates a control, order checking is disabled by default, and the mock
 objects created by this control will return `0`,
 `null` or `false` for unexpected invocations.

Returns:
the control.

    - 

#### expect

```
public static <T> IExpectationSetters<T> expect​(T value)
```

Returns the expectation setter for the last expected invocation in the
 current thread.

Type Parameters:
`T` - type returned by the expected method
Parameters:
`value` - the parameter is used to transport the type to the
            ExpectationSetter. It allows writing the expected call as
            argument, i.e. expect(mock.getName()).andReturn("John Doe").
Returns:
the expectation setter.

    - 

#### expectLastCall

```
public static <T> IExpectationSetters<T> expectLastCall()
```

Returns the expectation setter for the last expected invocation in the
 current thread. This method is used for expected invocations on void
 methods.

Type Parameters:
`T` - type returned by the expected method
Returns:
the expectation setter.

    - 

#### anyBoolean

```
public static boolean anyBoolean()
```

Expects any boolean argument. For details, see the EasyMock
 documentation.

Returns:
`false`.

    - 

#### anyByte

```
public static byte anyByte()
```

Expects any byte argument. For details, see the EasyMock documentation.

Returns:
`0`.

    - 

#### anyChar

```
public static char anyChar()
```

Expects any char argument. For details, see the EasyMock documentation.

Returns:
`0`.

    - 

#### anyInt

```
public static int anyInt()
```

Expects any int argument. For details, see the EasyMock documentation.

Returns:
`0`.

    - 

#### anyLong

```
public static long anyLong()
```

Expects any long argument. For details, see the EasyMock documentation.

Returns:
`0`.

    - 

#### anyFloat

```
public static float anyFloat()
```

Expects any float argument. For details, see the EasyMock documentation.

Returns:
`0`.

    - 

#### anyDouble

```
public static double anyDouble()
```

Expects any double argument. For details, see the EasyMock documentation.

Returns:
`0`.

    - 

#### anyShort

```
public static short anyShort()
```

Expects any short argument. For details, see the EasyMock documentation.

Returns:
`0`.

    - 

#### anyObject

```
public static <T> T anyObject()
```

Expects any Object argument. For details, see the EasyMock documentation.
 This matcher (and `anyObject(Class)`) can be used in these three
 ways:
 

 
      - `(T)EasyMock.anyObject() // explicit cast`
 
      - 
 `EasyMock.<T> anyObject() // fixing the returned generic`
 
 
      - 
 `EasyMock.anyObject(T.class) // pass the returned type in parameter`
 
 

Type Parameters:
`T` - type of the method argument to match
Returns:
`null`.

    - 

#### anyObject

```
public static <T> T anyObject​(Class<T> clazz)
```

Expects any Object argument. For details, see the EasyMock documentation.
 To work well with generics, this matcher can be used in three different
 ways. See `anyObject()`.

Type Parameters:
`T` - type of the method argument to match
Parameters:
`clazz` - the class of the argument to match
Returns:
`null`.

    - 

#### anyString

```
public static String anyString()
```

Expect any string whatever its content is. Exactly the same as
 `anyObject()` but prevents typing issues for the much used String
 type. Consider this method to be a syntactic sugar.

Returns:
`null`.

    - 

#### geq

```
public static <T extends Comparable<T>> T geq​(T value)
```

Expects a comparable argument greater than or equal the given value. For
 details, see the EasyMock documentation.

Type Parameters:
`T` - type of the method argument to match
Parameters:
`value` - the given value.
Returns:
`null`.

    - 

#### geq

```
public static byte geq​(byte value)
```

Expects a byte argument greater than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### geq

```
public static double geq​(double value)
```

Expects a double argument greater than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### geq

```
public static float geq​(float value)
```

Expects a float argument greater than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### geq

```
public static int geq​(int value)
```

Expects an int argument greater than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### geq

```
public static long geq​(long value)
```

Expects a long argument greater than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### geq

```
public static short geq​(short value)
```

Expects a short argument greater than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### leq

```
public static <T extends Comparable<T>> T leq​(T value)
```

Expects a comparable argument less than or equal the given value. For
 details, see the EasyMock documentation.

Type Parameters:
`T` - type of the method argument to match
Parameters:
`value` - the given value.
Returns:
`null`.

    - 

#### leq

```
public static byte leq​(byte value)
```

Expects a byte argument less than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### leq

```
public static double leq​(double value)
```

Expects a double argument less than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### leq

```
public static float leq​(float value)
```

Expects a float argument less than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### leq

```
public static int leq​(int value)
```

Expects an int argument less than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### leq

```
public static long leq​(long value)
```

Expects a long argument less than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### leq

```
public static short leq​(short value)
```

Expects a short argument less than or equal to the given value. For
 details, see the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### gt

```
public static <T extends Comparable<T>> T gt​(T value)
```

Expects a comparable argument greater than the given value. For details,
 see the EasyMock documentation.

Type Parameters:
`T` - type of the method argument to match
Parameters:
`value` - the given value.
Returns:
`null`.

    - 

#### gt

```
public static byte gt​(byte value)
```

Expects a byte argument greater than the given value. For details, see
 the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### gt

```
public static double gt​(double value)
```

Expects a double argument greater than the given value. For details, see
 the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### gt

```
public static float gt​(float value)
```

Expects a float argument greater than the given value. For details, see
 the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### gt

```
public static int gt​(int value)
```

Expects an int argument greater than the given value. For details, see
 the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### gt

```
public static long gt​(long value)
```

Expects a long argument greater than the given value. For details, see
 the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### gt

```
public static short gt​(short value)
```

Expects a short argument greater than the given value. For details, see
 the EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### lt

```
public static <T extends Comparable<T>> T lt​(T value)
```

Expects a comparable argument less than the given value. For details, see
 the EasyMock documentation.

Type Parameters:
`T` - type of the method argument to match
Parameters:
`value` - the given value.
Returns:
`null`.

    - 

#### lt

```
public static byte lt​(byte value)
```

Expects a byte argument less than the given value. For details, see the
 EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### lt

```
public static double lt​(double value)
```

Expects a double argument less than the given value. For details, see the
 EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### lt

```
public static float lt​(float value)
```

Expects a float argument less than the given value. For details, see the
 EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### lt

```
public static int lt​(int value)
```

Expects an int argument less than the given value. For details, see the
 EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### lt

```
public static long lt​(long value)
```

Expects a long argument less than the given value. For details, see the
 EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### lt

```
public static short lt​(short value)
```

Expects a short argument less than the given value. For details, see the
 EasyMock documentation.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### isA

```
public static <T> T isA​(Class<T> clazz)
```

Expects an object implementing the given class. For details, see the
 EasyMock documentation.

Type Parameters:
`T` - the accepted type.
Parameters:
`clazz` - the class of the accepted type.
Returns:
`null`.

    - 

#### contains

```
public static String contains​(String substring)
```

Expects a string that contains the given substring. For details, see the
 EasyMock documentation.

Parameters:
`substring` - the substring.
Returns:
`null`.

    - 

#### and

```
public static boolean and​(boolean first,
                          boolean second)
```

Expects a boolean that matches both given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`false`.

    - 

#### and

```
public static byte and​(byte first,
                       byte second)
```

Expects a byte that matches both given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### and

```
public static char and​(char first,
                       char second)
```

Expects a char that matches both given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### and

```
public static double and​(double first,
                         double second)
```

Expects a double that matches both given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### and

```
public static float and​(float first,
                        float second)
```

Expects a float that matches both given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### and

```
public static int and​(int first,
                      int second)
```

Expects an int that matches both given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### and

```
public static long and​(long first,
                       long second)
```

Expects a long that matches both given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### and

```
public static short and​(short first,
                        short second)
```

Expects a short that matches both given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### and

```
public static <T> T and​(T first,
                        T second)
```

Expects an Object that matches both given expectations.

Type Parameters:
`T` - the type of the object, it is passed through to prevent casts.
Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`null`.

    - 

#### or

```
public static boolean or​(boolean first,
                         boolean second)
```

Expects a boolean that matches one of the given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`false`.

    - 

#### or

```
public static byte or​(byte first,
                      byte second)
```

Expects a byte that matches one of the given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### or

```
public static char or​(char first,
                      char second)
```

Expects a char that matches one of the given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### or

```
public static double or​(double first,
                        double second)
```

Expects a double that matches one of the given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### or

```
public static float or​(float first,
                       float second)
```

Expects a float that matches one of the given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### or

```
public static int or​(int first,
                     int second)
```

Expects an int that matches one of the given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### or

```
public static long or​(long first,
                      long second)
```

Expects a long that matches one of the given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### or

```
public static short or​(short first,
                       short second)
```

Expects a short that matches one of the given expectations.

Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`0`.

    - 

#### or

```
public static <T> T or​(T first,
                       T second)
```

Expects an Object that matches one of the given expectations.

Type Parameters:
`T` - the type of the object, it is passed through to prevent casts.
Parameters:
`first` - placeholder for the first expectation.
`second` - placeholder for the second expectation.
Returns:
`null`.

    - 

#### not

```
public static boolean not​(boolean first)
```

Expects a boolean that does not match the given expectation.

Parameters:
`first` - placeholder for the expectation.
Returns:
`false`.

    - 

#### not

```
public static byte not​(byte first)
```

Expects a byte that does not match the given expectation.

Parameters:
`first` - placeholder for the expectation.
Returns:
`0`.

    - 

#### not

```
public static char not​(char first)
```

Expects a char that does not match the given expectation.

Parameters:
`first` - placeholder for the expectation.
Returns:
`0`.

    - 

#### not

```
public static double not​(double first)
```

Expects a double that does not match the given expectation.

Parameters:
`first` - placeholder for the expectation.
Returns:
`0`.

    - 

#### not

```
public static float not​(float first)
```

Expects a float that does not match the given expectation.

Parameters:
`first` - placeholder for the expectation.
Returns:
`0`.

    - 

#### not

```
public static int not​(int first)
```

Expects an int that does not match the given expectation.

Parameters:
`first` - placeholder for the expectation.
Returns:
`0`.

    - 

#### not

```
public static long not​(long first)
```

Expects a long that does not match the given expectation.

Parameters:
`first` - placeholder for the expectation.
Returns:
`0`.

    - 

#### not

```
public static short not​(short first)
```

Expects a short that does not match the given expectation.

Parameters:
`first` - placeholder for the expectation.
Returns:
`0`.

    - 

#### not

```
public static <T> T not​(T first)
```

Expects an Object that does not match the given expectation.

Type Parameters:
`T` - the type of the object, it is passed through to prevent casts.
Parameters:
`first` - placeholder for the expectation.
Returns:
`null`.

    - 

#### eq

```
public static boolean eq​(boolean value)
```

Expects a boolean that is equal to the given value.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### eq

```
public static byte eq​(byte value)
```

Expects a byte that is equal to the given value.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### eq

```
public static char eq​(char value)
```

Expects a char that is equal to the given value.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### eq

```
public static double eq​(double value)
```

Expects a double that is equal to the given value.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### eq

```
public static float eq​(float value)
```

Expects a float that is equal to the given value.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### eq

```
public static int eq​(int value)
```

Expects an int that is equal to the given value.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### eq

```
public static long eq​(long value)
```

Expects a long that is equal to the given value.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### eq

```
public static short eq​(short value)
```

Expects a short that is equal to the given value.

Parameters:
`value` - the given value.
Returns:
`0`.

    - 

#### eq

```
public static <T> T eq​(T value)
```

Expects an Object that is equal to the given value.

Type Parameters:
`T` - type of the method argument to match
Parameters:
`value` - the given value.
Returns:
`null`.

    - 

#### aryEq

```
public static boolean[] aryEq​(boolean[] value)
```

Expects a boolean array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

Parameters:
`value` - the given array.
Returns:
`null`.

    - 

#### aryEq

```
public static byte[] aryEq​(byte[] value)
```

Expects a byte array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

Parameters:
`value` - the given array.
Returns:
`null`.

    - 

#### aryEq

```
public static char[] aryEq​(char[] value)
```

Expects a char array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

Parameters:
`value` - the given array.
Returns:
`null`.

    - 

#### aryEq

```
public static double[] aryEq​(double[] value)
```

Expects a double array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

Parameters:
`value` - the given array.
Returns:
`null`.

    - 

#### aryEq

```
public static float[] aryEq​(float[] value)
```

Expects a float array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

Parameters:
`value` - the given array.
Returns:
`null`.

    - 

#### aryEq

```
public static int[] aryEq​(int[] value)
```

Expects an int array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

Parameters:
`value` - the given array.
Returns:
`null`.

    - 

#### aryEq

```
public static long[] aryEq​(long[] value)
```

Expects a long array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

Parameters:
`value` - the given array.
Returns:
`null`.

    - 

#### aryEq

```
public static short[] aryEq​(short[] value)
```

Expects a short array that is equal to the given array, i.e. it has to
 have the same length, and each element has to be equal.

Parameters:
`value` - the given array.
Returns:
`null`.

    - 

#### aryEq

```
public static <T> T[] aryEq​(T[] value)
```

Expects an Object array that is equal to the given array, i.e. it has to
 have the same type, length, and each element has to be equal.

Type Parameters:
`T` - the type of the array, it is passed through to prevent casts.
Parameters:
`value` - the given array.
Returns:
`null`.

    - 

#### isNull

```
public static <T> T isNull()
```

Expects null. To work well with generics, this matcher (and
 `isNull(Class)`) can be used in these three ways:
 

 
      - `(T)EasyMock.isNull() // explicit cast`
 
      - 
 `EasyMock.<T> isNull() // fixing the returned generic`
 
      - 
 `EasyMock.isNull(T.class) // pass the returned type in parameter`
 
 

Type Parameters:
`T` - type of the method argument to match
Returns:
`null`.

    - 

#### isNull

```
public static <T> T isNull​(Class<T> clazz)
```

Expects null. To work well with generics, this matcher can be used in
 three different ways. See `isNull()`.

Type Parameters:
`T` - type of the method argument to match
Parameters:
`clazz` - the class of the argument to match
Returns:
`null`.
See Also:
`isNull()`

    - 

#### notNull

```
public static <T> T notNull()
```

Expects not null. To work well with generics, this matcher (and
 `notNull(Class)`) can be used in these three ways:
 

 
      - `(T)EasyMock.notNull() // explicit cast`
 
      - 
 `EasyMock.<T> notNull() // fixing the returned generic`
 
      - 
 `EasyMock.notNull(T.class) // pass the returned type in parameter`
 
 

Type Parameters:
`T` - type of the method argument to match
Returns:
`null`.

    - 

#### notNull

```
public static <T> T notNull​(Class<T> clazz)
```

Expects not null. To work well with generics, this matcher can be used in
 three different ways. See `notNull()`.

Type Parameters:
`T` - type of the method argument to match
Parameters:
`clazz` - the class of the argument to match
Returns:
`null`.
See Also:
`notNull()`

    - 

#### find

```
public static String find​(String regex)
```

Expects a string that contains a substring that matches the given regular
 expression. For details, see the EasyMock documentation.

Parameters:
`regex` - the regular expression.
Returns:
`null`.

    - 

#### matches

```
public static String matches​(String regex)
```

Expects a string that matches the given regular expression. For details,
 see the EasyMock documentation.

Parameters:
`regex` - the regular expression.
Returns:
`null`.

    - 

#### startsWith

```
public static String startsWith​(String prefix)
```

Expects a string that starts with the given prefix. For details, see the
 EasyMock documentation.

Parameters:
`prefix` - the prefix.
Returns:
`null`.

    - 

#### endsWith

```
public static String endsWith​(String suffix)
```

Expects a string that ends with the given suffix. For details, see the
 EasyMock documentation.

Parameters:
`suffix` - the suffix.
Returns:
`null`.

    - 

#### eq

```
public static double eq​(double value,
                        double delta)
```

Expects a double that has an absolute difference to the given value that
 is less than the given delta. For details, see the EasyMock
 documentation.

Parameters:
`value` - the given value.
`delta` - the given delta.
Returns:
`0`.

    - 

#### eq

```
public static float eq​(float value,
                       float delta)
```

Expects a float that has an absolute difference to the given value that
 is less than the given delta. For details, see the EasyMock
 documentation.

Parameters:
`value` - the given value.
`delta` - the given delta.
Returns:
`0`.

    - 

#### same

```
public static <T> T same​(T value)
```

Expects an Object that is the same as the given value. For details, see
 the EasyMock documentation.

Type Parameters:
`T` - the type of the object, it is passed through to prevent casts.
Parameters:
`value` - the given value.
Returns:
`null`.

    - 

#### cmpEq

```
public static <T extends Comparable<T>> T cmpEq​(T value)
```

Expects a comparable argument equals to the given value according to
 their compareTo method. For details, see the EasMock documentation.

Type Parameters:
`T` - type of the method argument to match
Parameters:
`value` - the given value.
Returns:
`null`.

    - 

#### cmp

```
public static <T> T cmp​(T value,
                        Comparator<? super T> comparator,
                        LogicalOperator operator)
```

Expects an argument that will be compared using the provided comparator.
 The following comparison will take place:
 

 `comparator.compare(actual, expected) operator 0`
 
 For details, see the EasyMock documentation.

Type Parameters:
`T` - type of the method argument to match
Parameters:
`value` - the given value.
`comparator` - Comparator used to compare the actual with expected value.
`operator` - The comparison operator.
Returns:
`null`

    - 

#### newCapture

```
public static <T> Capture<T> newCapture()
```

Create a new capture instance that will keep only the last captured value.

Type Parameters:
`T` - type of the class to be captured
Returns:
the new capture object

    - 

#### newCapture

```
public static <T> Capture<T> newCapture​(CaptureType type)
```

Create a new capture instance with a specific `CaptureType`

Type Parameters:
`T` - type of the class to be captured
Parameters:
`type` - capture type wanted
Returns:
the new capture object

    - 

#### newCapture

```
public static <T> Capture<T> newCapture​(CaptureType type,
                                        UnaryOperator<T> transform)
```

Create a new capture instance with a specific `CaptureType`
 and a specific transformation function to change the values into a different value.
 

 One useful usage for the transformation is when the captured argument will be mutated
 after the capture, and you would like to save it before mutation.

Type Parameters:
`T` - type of the class to be captured
Parameters:
`type` - capture type wanted
`transform` - the transform function
Returns:
the new capture object

    - 

#### newCapture

```
public static <T> Capture<T> newCapture​(UnaryOperator<T> transform)
```

Create a new capture instance with a specific and a specific transformation
 function to change the values into a different value.
 

 One useful usage for the transformation is when the captured argument will be mutated
 after the capture, and you would like to save it before mutation.

Type Parameters:
`T` - type of the class to be captured
Parameters:
`transform` - the transform function
Returns:
the new capture object

    - 

#### capture

```
public static <T> T capture​(Capture<T> captured)
```

Expect any object but captures it for later use.

Type Parameters:
`T` - Type of the captured object
Parameters:
`captured` - Where the parameter is captured
Returns:
`null`

    - 

#### captureBoolean

```
public static boolean captureBoolean​(Capture<Boolean> captured)
```

Expect any boolean but captures it for later use.

Parameters:
`captured` - Where the parameter is captured
Returns:
`false`

    - 

#### captureInt

```
public static int captureInt​(Capture<Integer> captured)
```

Expect any int but captures it for later use.

Parameters:
`captured` - Where the parameter is captured
Returns:
`0`

    - 

#### captureLong

```
public static long captureLong​(Capture<Long> captured)
```

Expect any long but captures it for later use.

Parameters:
`captured` - Where the parameter is captured
Returns:
`0`

    - 

#### captureFloat

```
public static float captureFloat​(Capture<Float> captured)
```

Expect any float but captures it for later use.

Parameters:
`captured` - Where the parameter is captured
Returns:
`0`

    - 

#### captureDouble

```
public static double captureDouble​(Capture<Double> captured)
```

Expect any double but captures it for later use.

Parameters:
`captured` - Where the parameter is captured
Returns:
`0`

    - 

#### captureByte

```
public static byte captureByte​(Capture<Byte> captured)
```

Expect any byte but captures it for later use.

Parameters:
`captured` - Where the parameter is captured
Returns:
`0`

    - 

#### captureChar

```
public static char captureChar​(Capture<Character> captured)
```

Expect any char but captures it for later use.

Parameters:
`captured` - Where the parameter is captured
Returns:
`0`

    - 

#### replay

```
public static void replay​(Object... mocks)
```

Switches the given mock objects (more exactly: the controls of the mock
 objects) to replay mode. For details, see the EasyMock documentation.

Parameters:
`mocks` - the mock objects.

    - 

#### reset

```
public static void reset​(Object... mocks)
```

Resets the given mock objects (more exactly: the controls of the mock
 objects). For details, see the EasyMock documentation.

Parameters:
`mocks` - the mock objects.

    - 

#### resetToNice

```
public static void resetToNice​(Object... mocks)
```

Resets the given mock objects (more exactly: the controls of the mock
 objects) and turn them to a mock with nice behavior. For details, see the
 EasyMock documentation.

Parameters:
`mocks` - the mock objects

    - 

#### resetToDefault

```
public static void resetToDefault​(Object... mocks)
```

Resets the given mock objects (more exactly: the controls of the mock
 objects) and turn them to a mock with default behavior. For details, see
 the EasyMock documentation.

Parameters:
`mocks` - the mock objects

    - 

#### resetToStrict

```
public static void resetToStrict​(Object... mocks)
```

Resets the given mock objects (more exactly: the controls of the mock
 objects) and turn them to a mock with strict behavior. For details, see
 the EasyMock documentation.

Parameters:
`mocks` - the mock objects

    - 

#### verify

```
public static void verify​(Object... mocks)
```

Verifies that all expectations were met and that no unexpected
 call was performed on the mock objects. Or more precisely, verifies the
 underlying `IMocksControl` linked to the mock objects.
 

 This method as same effect as calling `verifyRecording(Object...)`
 followed by `verifyUnexpectedCalls(Object...)`.

Parameters:
`mocks` - the mock objects.

    - 

#### verifyRecording

```
public static void verifyRecording​(Object... mocks)
```

Verifies that all expectations were met.

Parameters:
`mocks` - the mock objects.
Since:
3.5

    - 

#### verifyUnexpectedCalls

```
public static void verifyUnexpectedCalls​(Object... mocks)
```

Verifies that no unexpected call was performed.

Parameters:
`mocks` - the mock objects.
Since:
3.5

    - 

#### checkOrder

```
public static void checkOrder​(Object mock,
                              boolean state)
```

Switches order checking of the given mock object (more exactly: the
 control of the mock object) the on and off. For details, see the EasyMock
 documentation.

Parameters:
`mock` - the mock object.
`state` - `true` switches order checking on,
            `false` switches it off.

    - 

#### reportMatcher

```
public static void reportMatcher​(IArgumentMatcher matcher)
```

Reports an argument matcher. This method is needed to define own argument
 matchers. For details, see the EasyMock documentation.

Parameters:
`matcher` - the matcher to use to match currently mocked method argument

    - 

#### getCurrentArguments

```
public static Object[] getCurrentArguments()
```

Returns the arguments of the current mock method call, if inside an
 `IAnswer` callback - be careful here, reordering parameters of
 method changes the semantics of your tests.

Returns:
the arguments of the current mock method call.
Throws:
`IllegalStateException` - if called outside of `IAnswer` callbacks.

    - 

#### getCurrentArgument

```
public static <T> T getCurrentArgument​(int index)
```

    - 

#### makeThreadSafe

```
public static void makeThreadSafe​(Object mock,
                                  boolean threadSafe)
```

By default, a mock is thread safe (unless
 `NOT_THREAD_SAFE_BY_DEFAULT` is set). This method can change this
 behavior. Two reasons are known for someone to do that: Performance or
 dead-locking issues.

Parameters:
`mock` - the mock to make thread safe
`threadSafe` - If the mock should be thread safe or not

    - 

#### checkIsUsedInOneThread

```
public static void checkIsUsedInOneThread​(Object mock,
                                          boolean shouldBeUsedInOneThread)
```

Tell that the mock should be used in only one thread. An exception will
 be thrown if that's not the case. This can be useful when mocking an
 object that isn't thread safe to make sure it is used correctly in a
 multithreaded environment. By default, no check is done unless
 `ENABLE_THREAD_SAFETY_CHECK_BY_DEFAULT` was set to true.

Parameters:
`mock` - the mock
`shouldBeUsedInOneThread` - If the mock should be used in only one thread

    - 

#### getEasyMockProperty

```
public static String getEasyMockProperty​(String key)
```

Get the current value for an EasyMock property

Parameters:
`key` - key for the property
Returns:
the property value

    - 

#### setEasyMockProperty

```
public static String setEasyMockProperty​(String key,
                                         String value)
```

Set a property to modify the default EasyMock behavior. These properties
 can also be set as System properties or in easymock.properties. This
 method can then be called to overload them. For details and a list of
 available properties see the EasyMock documentation.
 

 **Note:** This method is static. Setting a property will change the
 entire EasyMock behavior.

Parameters:
`key` - property key
`value` - property value. A null value will remove the property
Returns:
the previous property value