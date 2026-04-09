Package org.apache.commons.validator.routines

# Class LongValidator

java.lang.Object
org.apache.commons.validator.routines.AbstractFormatValidator
org.apache.commons.validator.routines.AbstractNumberValidator
org.apache.commons.validator.routines.LongValidator

All Implemented Interfaces:
`Serializable`

---

public class LongValidator
extends AbstractNumberValidator

**Long Validation** and Conversion routines (`Long`).

 

This validator provides a number of methods for
    validating/converting a `String` value to
    a `Long` using `NumberFormat`
    to parse either:
    

       
- using the default format for the default `Locale`
       
- using a specified pattern with the default `Locale`
       
- using the default format for a specified `Locale`
       
- using a specified pattern with a specified `Locale`
    

 

Use one of the `isValid()` methods to just validate or
    one of the `validate()` methods to validate and receive a
    *converted* `Long` value.

 

Once a value has been successfully converted the following
    methods can be used to perform minimum, maximum and range checks:
    

       
- `minValue()` checks whether the value is greater
           than or equal to a specified minimum.
       
- `maxValue()` checks whether the value is less
           than or equal to a specified maximum.
       
- `isInRange()` checks whether the value is within
           a specified range of values.
    

 

So that the same mechanism used for parsing an *input* value
    for validation can be used to format *output*, corresponding
    `format()` methods are also provided. That is you can
    format either:
    

       
- using a specified pattern
       
- using the format for a specified `Locale`
       
- using the format for the *default* `Locale`
    

Since:
1.3.0
See Also:

- Serialized Form

- 

## Field Summary

### Fields inherited from class org.apache.commons.validator.routines.AbstractNumberValidator

`CURRENCY_FORMAT, PERCENT_FORMAT, STANDARD_FORMAT`

- 

## Constructor Summary

Constructors

Constructor
Description
`LongValidator()`

Constructs a *strict* instance.

`LongValidator(boolean strict,
 int formatType)`

Construct an instance with the specified strict setting
    and format type.

- 

## Method Summary

Modifier and Type
Method
Description
`static LongValidator`
`getInstance()`

Gets the singleton instance of this validator.

`boolean`
`isInRange(long value,
 long min,
 long max)`

Check if the value is within a specified range.

`boolean`
`isInRange(Long value,
 long min,
 long max)`

Check if the value is within a specified range.

`boolean`
`maxValue(long value,
 long max)`

Check if the value is less than or equal to a maximum.

`boolean`
`maxValue(Long value,
 long max)`

Check if the value is less than or equal to a maximum.

`boolean`
`minValue(long value,
 long min)`

Check if the value is greater than or equal to a minimum.

`boolean`
`minValue(Long value,
 long min)`

Check if the value is greater than or equal to a minimum.

`protected Object`
`processParsedValue(Object value,
 Format formatter)`

Convert the parsed value to a `Long`.

`Long`
`validate(String value)`

Validate/convert a `Long` using the default
    `Locale`.

`Long`
`validate(String value,
 String pattern)`

Validate/convert a `Long` using the
    specified *pattern*.

`Long`
`validate(String value,
 String pattern,
 Locale locale)`

Validate/convert a `Long` using the
    specified pattern and/ or `Locale`.

`Long`
`validate(String value,
 Locale locale)`

Validate/convert a `Long` using the
    specified `Locale`.

### Methods inherited from class org.apache.commons.validator.routines.AbstractNumberValidator

`determineScale, getFormat, getFormat, getFormatType, isAllowFractions, isInRange, isValid, maxValue, minValue, parse`

### Methods inherited from class org.apache.commons.validator.routines.AbstractFormatValidator

`format, format, format, format, format, isStrict, isValid, isValid, isValid, parse`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### LongValidator

public LongValidator()
Constructs a *strict* instance.

  - 

### LongValidator

public LongValidator(boolean strict,
 int formatType)

Construct an instance with the specified strict setting
    and format type.

 

The `formatType` specified what type of
    `NumberFormat` is created - valid types
    are:
    

       
    - AbstractNumberValidator.STANDARD_FORMAT -to create
           *standard* number formats (the default).
       
    - AbstractNumberValidator.CURRENCY_FORMAT -to create
           *currency* number formats.
       
    - AbstractNumberValidator.PERCENT_FORMAT -to create
           *percent* number formats (the default).
    

Parameters:
`strict` - `true` if strict
        `Format` parsing should be used.
`formatType` - The `NumberFormat` type to
        create for validation, default is STANDARD_FORMAT.

- 

## Method Details

  - 

### getInstance

public static LongValidator getInstance()
Gets the singleton instance of this validator.

Returns:
A singleton instance of the LongValidator.

  - 

### isInRange

public boolean isInRange(long value,
 long min,
 long max)
Check if the value is within a specified range.

Parameters:
`value` - The `Number` value to check.
`min` - The minimum value of the range.
`max` - The maximum value of the range.
Returns:
`true` if the value is within the
         specified range.

  - 

### isInRange

public boolean isInRange(Long value,
 long min,
 long max)
Check if the value is within a specified range.

Parameters:
`value` - The `Number` value to check.
`min` - The minimum value of the range.
`max` - The maximum value of the range.
Returns:
`true` if the value is within the
         specified range.

  - 

### maxValue

public boolean maxValue(long value,
 long max)
Check if the value is less than or equal to a maximum.

Parameters:
`value` - The value validation is being performed on.
`max` - The maximum value.
Returns:
`true` if the value is less than
         or equal to the maximum.

  - 

### maxValue

public boolean maxValue(Long value,
 long max)
Check if the value is less than or equal to a maximum.

Parameters:
`value` - The value validation is being performed on.
`max` - The maximum value.
Returns:
`true` if the value is less than
         or equal to the maximum.

  - 

### minValue

public boolean minValue(long value,
 long min)
Check if the value is greater than or equal to a minimum.

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum value.
Returns:
`true` if the value is greater than
         or equal to the minimum.

  - 

### minValue

public boolean minValue(Long value,
 long min)
Check if the value is greater than or equal to a minimum.

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum value.
Returns:
`true` if the value is greater than
         or equal to the minimum.

  - 

### processParsedValue

protected Object processParsedValue(Object value,
 Format formatter)
Convert the parsed value to a `Long`.

Specified by:
`processParsedValue` in class `AbstractNumberValidator`
Parameters:
`value` - The parsed `Number` object created.
`formatter` - The Format used to parse the value with.
Returns:
The parsed `Number` converted to a
         `Long`.

  - 

### validate

public Long validate(String value)

Validate/convert a `Long` using the default
    `Locale`.

Parameters:
`value` - The value validation is being performed on.
Returns:
The parsed `Long` if valid or `null`
  if invalid.

  - 

### validate

public Long validate(String value,
 Locale locale)

Validate/convert a `Long` using the
    specified `Locale`.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use for the number format, system default if null.
Returns:
The parsed `Long` if valid or `null` if invalid.

  - 

### validate

public Long validate(String value,
 String pattern)

Validate/convert a `Long` using the
    specified *pattern*.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against.
Returns:
The parsed `Long` if valid or `null` if invalid.

  - 

### validate

public Long validate(String value,
 String pattern,
 Locale locale)

Validate/convert a `Long` using the
    specified pattern and/ or `Locale`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against, or the
        default for the `Locale` if `null`.
`locale` - The locale to use for the date format, system default if null.
Returns:
The parsed `Long` if valid or `null` if invalid.