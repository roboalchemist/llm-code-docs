Package org.apache.commons.validator

# Class ValidatorResult

java.lang.Object
org.apache.commons.validator.ValidatorResult

All Implemented Interfaces:
`Serializable`

---

public class ValidatorResult
extends Object
implements Serializable
This contains the results of a set of validation rules processed
 on a JavaBean.

See Also:

- Serialized Form

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`protected static class `
`ValidatorResult.ResultStatus`

Contains the status of the validation.

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`protected Field`
`field`

`Field` being validated.

`protected Map<String,ValidatorResult.ResultStatus>`
`hAction`

Map of results.

- 

## Constructor Summary

Constructors

Constructor
Description
`ValidatorResult(Field field)`

Constructs a `ValidatorResult` with the associated field being
 validated.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`add(String validatorName,
 boolean result)`

Add the result of a validator action.

`void`
`add(String validatorName,
 boolean result,
 Object value)`

Add the result of a validator action.

`boolean`
`containsAction(String validatorName)`

Indicate whether a specified validator is in the Result.

`Map<String,ValidatorResult.ResultStatus>`
`getActionMap()`

Deprecated.
Use getActions() to return the set of actions
             the isValid(name) and getResult(name) methods
             to determine the contents of ResultStatus.

`Iterator<String>`
`getActions()`

Gets an Iterator of the action names contained in this Result.

`Field`
`getField()`

Returns the Field that was validated.

`Object`
`getResult(String validatorName)`

Gets the result of a validation.

`boolean`
`isValid(String validatorName)`

Indicate whether a specified validation passed.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### hAction

protected Map<String,ValidatorResult.ResultStatus> hAction
Map of results.  The key is the name of the `ValidatorAction`
 and the value is whether or not this field passed or not.

  - 

### field

protected Field field
`Field` being validated.
 TODO This variable is not used.  Need to investigate removing it.

- 

## Constructor Details

  - 

### ValidatorResult

public ValidatorResult(Field field)
Constructs a `ValidatorResult` with the associated field being
 validated.

Parameters:
`field` - Field that was validated.

- 

## Method Details

  - 

### add

public void add(String validatorName,
 boolean result)
Add the result of a validator action.

Parameters:
`validatorName` - Name of the validator.
`result` - Whether the validation passed or failed.

  - 

### add

public void add(String validatorName,
 boolean result,
 Object value)
Add the result of a validator action.

Parameters:
`validatorName` - Name of the validator.
`result` - Whether the validation passed or failed.
`value` - Value returned by the validator.

  - 

### containsAction

public boolean containsAction(String validatorName)
Indicate whether a specified validator is in the Result.

Parameters:
`validatorName` - Name of the validator.
Returns:
true if the validator is in the result.

  - 

### getActionMap

@Deprecated
public Map<String,ValidatorResult.ResultStatus> getActionMap()
Deprecated.
Use getActions() to return the set of actions
             the isValid(name) and getResult(name) methods
             to determine the contents of ResultStatus.

Gets a Map of the validator actions in this Result.

Returns:
Map of validator actions.

  - 

### getActions

public Iterator<String> getActions()
Gets an Iterator of the action names contained in this Result.

Returns:
The set of action names.

  - 

### getField

public Field getField()
Returns the Field that was validated.

Returns:
The Field associated with this result.

  - 

### getResult

public Object getResult(String validatorName)
Gets the result of a validation.

Parameters:
`validatorName` - Name of the validator.
Returns:
The validation result.

  - 

### isValid

public boolean isValid(String validatorName)
Indicate whether a specified validation passed.

Parameters:
`validatorName` - Name of the validator.
Returns:
true if the validation passed.