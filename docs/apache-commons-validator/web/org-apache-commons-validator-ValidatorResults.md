Package org.apache.commons.validator

# Class ValidatorResults

java.lang.Object
org.apache.commons.validator.ValidatorResults

All Implemented Interfaces:
`Serializable`

---

public class ValidatorResults
extends Object
implements Serializable
This contains the results of a set of validation rules processed
 on a JavaBean.

See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`protected Map<String,ValidatorResult>`
`hResults`

Map of validation results.

- 

## Constructor Summary

Constructors

Constructor
Description
`ValidatorResults()`

Constructs a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`add(Field field,
 String validatorName,
 boolean result)`

Add the result of a validator action.

`void`
`add(Field field,
 String validatorName,
 boolean result,
 Object value)`

Add the result of a validator action.

`void`
`clear()`

Clear all results recorded by this object.

`Set<String>`
`getPropertyNames()`

Gets the set of property names for which at least one message has
 been recorded.

`Map<String,Object>`
`getResultValueMap()`

Gets a `Map` of any `Object`s returned from
 validation routines.

`ValidatorResult`
`getValidatorResult(String key)`

Gets the `ValidatorResult` associated
 with the key passed in.

`boolean`
`isEmpty()`

Gets `true` if there are no messages recorded
 in this collection, or `false` otherwise.

`void`
`merge(ValidatorResults results)`

Merge another ValidatorResults into mine.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### hResults

protected Map<String,ValidatorResult> hResults
Map of validation results.

- 

## Constructor Details

  - 

### ValidatorResults

public ValidatorResults()
Constructs a new instance.

- 

## Method Details

  - 

### add

public void add(Field field,
 String validatorName,
 boolean result)
Add the result of a validator action.

Parameters:
`field` - The field validated.
`validatorName` - The name of the validator.
`result` - The result of the validation.

  - 

### add

public void add(Field field,
 String validatorName,
 boolean result,
 Object value)
Add the result of a validator action.

Parameters:
`field` - The field validated.
`validatorName` - The name of the validator.
`result` - The result of the validation.
`value` - The value returned by the validator.

  - 

### clear

public void clear()
Clear all results recorded by this object.

  - 

### getPropertyNames

public Set<String> getPropertyNames()
Gets the set of property names for which at least one message has
 been recorded.

Returns:
An unmodifiable Set of the property names.

  - 

### getResultValueMap

public Map<String,Object> getResultValueMap()
Gets a `Map` of any `Object`s returned from
 validation routines.

Returns:
Map of objections returned by validators.

  - 

### getValidatorResult

public ValidatorResult getValidatorResult(String key)
Gets the `ValidatorResult` associated
 with the key passed in.  The key the `ValidatorResult`
 is stored under is the `Field`'s getKey method.

Parameters:
`key` - The key generated from `Field` (this is often just
 the field name).
Returns:
The result of a specified key.

  - 

### isEmpty

public boolean isEmpty()
Gets `true` if there are no messages recorded
 in this collection, or `false` otherwise.

Returns:
Whether these results are empty.

  - 

### merge

public void merge(ValidatorResults results)
Merge another ValidatorResults into mine.

Parameters:
`results` - ValidatorResults to merge.