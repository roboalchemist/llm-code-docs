Package org.jsoup.helper

# Class ValidationException

java.lang.Object
java.lang.Throwable
java.lang.Exception
java.lang.RuntimeException
java.lang.IllegalArgumentException
org.jsoup.helper.ValidationException

All Implemented Interfaces:
`Serializable`

---

public class ValidationException
extends IllegalArgumentException
Validation exceptions, as thrown by the methods in `Validate`.

See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`Validator`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`ValidationException(String msg)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`Throwable`
`fillInStackTrace()`
 

### Methods inherited from class java.lang.Throwable

`addSuppressed, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### Validator

public static final String Validator

- 

## Constructor Details

  - 

### ValidationException

public ValidationException(String msg)

- 

## Method Details

  - 

### fillInStackTrace

public Throwable fillInStackTrace()

Overrides:
`fillInStackTrace` in class `Throwable`