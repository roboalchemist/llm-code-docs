Package org.apache.commons.validator

# Class ValidatorResult.ResultStatus

java.lang.Object
org.apache.commons.validator.ValidatorResult.ResultStatus

All Implemented Interfaces:
`Serializable`

Enclosing class:
`ValidatorResult`

---

protected static class ValidatorResult.ResultStatus
extends Object
implements Serializable
Contains the status of the validation.

See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`ResultStatus(boolean valid,
 Object result)`

Constructs a Result status.

`ResultStatus(ValidatorResult ignored,
 boolean valid,
 Object result)`

Deprecated.
Use `ResultStatus(boolean, Object)` instead

- 

## Method Summary

Modifier and Type
Method
Description
`Object`
`getResult()`

Gets the result returned by a validation method.

`boolean`
`isValid()`

Tests whether or not the validation passed.

`void`
`setResult(Object result)`

Sets the result returned by a validation method.

`void`
`setValid(boolean valid)`

Sets whether or not the validation passed.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### ResultStatus

public ResultStatus(boolean valid,
 Object result)
Constructs a Result status.

Parameters:
`valid` - Whether the validator passed or failed.
`result` - Value returned by the validator.

  - 

### ResultStatus

@Deprecated
public ResultStatus(ValidatorResult ignored,
 boolean valid,
 Object result)
Deprecated.
Use `ResultStatus(boolean, Object)` instead

Provided for backwards binary compatibility only.

Parameters:
`ignored` - ignored by this method
`valid` - Whether the validator passed or failed.
`result` - Value returned by the validator.

- 

## Method Details

  - 

### getResult

public Object getResult()
Gets the result returned by a validation method.
 This can be used to retrieve to the correctly
 typed value of a date validation for example.

Returns:
The value returned by the validation.

  - 

### isValid

public boolean isValid()
Tests whether or not the validation passed.

Returns:
true if the result was good.

  - 

### setResult

public void setResult(Object result)
Sets the result returned by a validation method.
 This can be used to retrieve to the correctly
 typed value of a date validation for example.

Parameters:
`result` - The value returned by the validation.

  - 

### setValid

public void setValid(boolean valid)
Sets whether or not the validation passed.

Parameters:
`valid` - Whether the validation passed.