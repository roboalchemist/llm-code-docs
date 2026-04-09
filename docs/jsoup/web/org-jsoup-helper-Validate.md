Package org.jsoup.helper

# Class Validate

java.lang.Object
org.jsoup.helper.Validate

---

public final class Validate
extends Object
Validators to check that method arguments meet expectations.

- 

## Method Summary

Modifier and Type
Method
Description
`static Object`
`ensureNotNull(@Nullable Object obj)`

Deprecated.
prefer to use `expectNotNull(Object, String, Object...)` instead; will be removed in jsoup 1.24.1

`static Object`
`ensureNotNull(@Nullable Object obj,
 String msg,
 Object... args)`

Deprecated.
prefer to use `expectNotNull(Object, String, Object...)` instead; will be removed in jsoup 1.24.1

`static <T> T`
`expectNotNull(@Nullable T obj)`

Verifies the input object is not null, and returns that object, maintaining its type.

`static <T> T`
`expectNotNull(@Nullable T obj,
 String msg,
 Object... args)`

Verifies the input object is not null, and returns that object, maintaining its type.

`static void`
`fail(String msg)`

Cause a failure.

`static void`
`fail(String msg,
 Object... args)`

Cause a failure.

`static void`
`isFalse(boolean val)`

Validates that the value is false

`static void`
`isFalse(boolean val,
 String msg)`

Validates that the value is false

`static void`
`isTrue(boolean val)`

Validates that the value is true

`static void`
`isTrue(boolean val,
 String msg)`

Validates that the value is true

`static void`
`noNullElements(Object[] objects)`

Validates that the array contains no null elements

`static void`
`noNullElements(Object[] objects,
 String msg)`

Validates that the array contains no null elements

`static void`
`notEmpty(@Nullable String string)`

Validates that the string is not null and is not empty

`static void`
`notEmpty(@Nullable String string,
 String msg)`

Validates that the string is not null and is not empty

`static void`
`notEmptyParam(@Nullable String string,
 String param)`

Validates that the string parameter is not null and is not empty

`static void`
`notNull(@Nullable Object obj)`

Validates that the object is not null

`static void`
`notNull(@Nullable Object obj,
 String msg)`

Validates that the object is not null

`static void`
`notNullParam(@Nullable Object obj,
 String param)`

Validates that the parameter is not null

`static void`
`wtf(String msg)`

Blow up if we reach an unexpected state.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### notNull

public static void notNull(@Nullable Object obj)
Validates that the object is not null

Parameters:
`obj` - object to test
Throws:
`ValidationException` - if the object is null

  - 

### notNullParam

public static void notNullParam(@Nullable Object obj,
 String param)
Validates that the parameter is not null

Parameters:
`obj` - the parameter to test
`param` - the name of the parameter, for presentation in the validation exception.
Throws:
`ValidationException` - if the object is null

  - 

### notNull

public static void notNull(@Nullable Object obj,
 String msg)
Validates that the object is not null

Parameters:
`obj` - object to test
`msg` - message to include in the Exception if validation fails
Throws:
`ValidationException` - if the object is null

  - 

### ensureNotNull

@Deprecated
public static Object ensureNotNull(@Nullable Object obj)
Deprecated.
prefer to use `expectNotNull(Object, String, Object...)` instead; will be removed in jsoup 1.24.1

Verifies the input object is not null, and returns that object. Effectively this casts a nullable object to a non-
     null object. (Works around lack of Objects.requestNonNull in Android version.)

Parameters:
`obj` - nullable object to cast to not-null
Returns:
the object, or throws an exception if it is null
Throws:
`ValidationException` - if the object is null

  - 

### ensureNotNull

@Deprecated
public static Object ensureNotNull(@Nullable Object obj,
 String msg,
 Object... args)
Deprecated.
prefer to use `expectNotNull(Object, String, Object...)` instead; will be removed in jsoup 1.24.1

Verifies the input object is not null, and returns that object. Effectively this casts a nullable object to a non-
     null object. (Works around lack of Objects.requestNonNull in Android version.)

Parameters:
`obj` - nullable object to cast to not-null
`msg` - the String format message to include in the validation exception when thrown
`args` - the arguments to the msg
Returns:
the object, or throws an exception if it is null
Throws:
`ValidationException` - if the object is null

  - 

### expectNotNull

public static <T> T expectNotNull(@Nullable T obj)
Verifies the input object is not null, and returns that object, maintaining its type. Effectively this casts a
     nullable object to a non-null object.

Parameters:
`obj` - nullable object to cast to not-null
Returns:
the object, or throws an exception if it is null
Throws:
`ValidationException` - if the object is null

  - 

### expectNotNull

public static <T> T expectNotNull(@Nullable T obj,
 String msg,
 Object... args)
Verifies the input object is not null, and returns that object, maintaining its type. Effectively this casts a
     nullable object to a non-null object.

Parameters:
`obj` - nullable object to cast to not-null
`msg` - the String format message to include in the validation exception when thrown
`args` - the arguments to the msg
Returns:
the object, or throws an exception if it is null
Throws:
`ValidationException` - if the object is null

  - 

### isTrue

public static void isTrue(boolean val)
Validates that the value is true

Parameters:
`val` - object to test
Throws:
`ValidationException` - if the object is not true

  - 

### isTrue

public static void isTrue(boolean val,
 String msg)
Validates that the value is true

Parameters:
`val` - object to test
`msg` - message to include in the Exception if validation fails
Throws:
`ValidationException` - if the object is not true

  - 

### isFalse

public static void isFalse(boolean val)
Validates that the value is false

Parameters:
`val` - object to test
Throws:
`ValidationException` - if the object is not false

  - 

### isFalse

public static void isFalse(boolean val,
 String msg)
Validates that the value is false

Parameters:
`val` - object to test
`msg` - message to include in the Exception if validation fails
Throws:
`ValidationException` - if the object is not false

  - 

### noNullElements

public static void noNullElements(Object[] objects)
Validates that the array contains no null elements

Parameters:
`objects` - the array to test
Throws:
`ValidationException` - if the array contains a null element

  - 

### noNullElements

public static void noNullElements(Object[] objects,
 String msg)
Validates that the array contains no null elements

Parameters:
`objects` - the array to test
`msg` - message to include in the Exception if validation fails
Throws:
`ValidationException` - if the array contains a null element

  - 

### notEmpty

public static void notEmpty(@Nullable String string)
Validates that the string is not null and is not empty

Parameters:
`string` - the string to test
Throws:
`ValidationException` - if the string is null or empty

  - 

### notEmptyParam

public static void notEmptyParam(@Nullable String string,
 String param)
Validates that the string parameter is not null and is not empty

Parameters:
`string` - the string to test
`param` - the name of the parameter, for presentation in the validation exception.
Throws:
`ValidationException` - if the string is null or empty

  - 

### notEmpty

public static void notEmpty(@Nullable String string,
 String msg)
Validates that the string is not null and is not empty

Parameters:
`string` - the string to test
`msg` - message to include in the Exception if validation fails
Throws:
`ValidationException` - if the string is null or empty

  - 

### wtf

public static void wtf(String msg)
Blow up if we reach an unexpected state.

Parameters:
`msg` - message to think about
Throws:
`IllegalStateException` - if we reach this state

  - 

### fail

public static void fail(String msg)
Cause a failure.

Parameters:
`msg` - message to output.
Throws:
`IllegalStateException` - if we reach this state

  - 

### fail

public static void fail(String msg,
 Object... args)
Cause a failure.

Parameters:
`msg` - message to output.
`args` - the format arguments to the msg
Throws:
`IllegalStateException` - if we reach this state