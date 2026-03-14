Package org.apache.commons.validator.routines

# Class BigDecimalValidator

java.lang.Object
org.apache.commons.validator.routines.AbstractFormatValidator
org.apache.commons.validator.routines.AbstractNumberValidator
org.apache.commons.validator.routines.BigDecimalValidator

All Implemented Interfaces:
`Serializable`

Direct Known Subclasses:
`CurrencyValidator`, `PercentValidator`

---

public class BigDecimalValidator
extends AbstractNumberValidator

**BigDecimal Validation** and Conversion routines (`java.math.BigDecimal`).

 

This validator provides a number of methods for
    validating/converting a `String` value to
    a `BigDecimal` using `NumberFormat`
    to parse either:
    

       
- using the default format for the default `Locale`
       
- using a specified pattern with the default `Locale`
       
- using the default format for a specified `Locale`
       
- using a specified pattern with a specified `Locale`
    

 

Use one of the `isValid()` methods to just validate or
    one of the `validate()` methods to validate and receive a
    *converted* `BigDecimal` value.

 

Fraction/decimal values are automatically trimmed to the appropriate length.

 

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
    

       
- using the default format for the default `Locale`
       
- using a specified pattern with the default `Locale`
       
- using the default format for a specified `Locale`
       
- using a specified pattern with a specified `Locale`
    

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

Modifier
Constructor
Description
` `
`BigDecimalValidator()`

Constructs a *strict* instance.

` `
`BigDecimalValidator(boolean strict)`

Construct an instance with the specified strict setting.

`protected `
`BigDecimalValidator(boolean strict,
 int formatType,
 boolean allowFractions)`

Construct an instance with the specified strict setting
    and format type.

- 

## Method Summary

Modifier and Type
Method
Description
`static BigDecimalValidator`
`getInstance()`

Gets the singleton instance of this validator.

`boolean`
`isInRange(BigDecimal value,
 double min,
 double max)`

Check if the value is within a specified range.

`boolean`
`maxValue(BigDecimal value,
 double max)`

Check if the value is less than or equal to a maximum.

`boolean`
`minValue(BigDecimal value,
 double min)`

Check if the value is greater than or equal to a minimum.

`protected Object`
`processParsedValue(Object value,
 Format formatter)`

Convert the parsed value to a `BigDecimal`.

`BigDecimal`
`validate(String value)`

Validate/convert a `BigDecimal` using the default
    `Locale`.

`BigDecimal`
`validate(String value,
 String pattern)`

Validate/convert a `BigDecimal` using the
    specified *pattern*.

`BigDecimal`
`validate(String value,
 String pattern,
 Locale locale)`

Validate/convert a `BigDecimal` using the
    specified pattern and/ or `Locale`.

`BigDecimal`
`validate(String value,
 Locale locale)`

Validate/convert a `BigDecimal` using the
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

### BigDecimalValidator

public BigDecimalValidator()
Constructs a *strict* instance.

  - 

### BigDecimalValidator

public BigDecimalValidator(boolean strict)

Construct an instance with the specified strict setting.

Parameters:
`strict` - `true` if strict
        `Format` parsing should be used.

  - 

### BigDecimalValidator

protected BigDecimalValidator(boolean strict,
 int formatType,
 boolean allowFractions)

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
`allowFractions` - `true` if fractions are
        allowed or `false` if integers only.

- 

## Method Details

  - 

### getInstance

public static BigDecimalValidator getInstance()
Gets the singleton instance of this validator.

Returns:
A singleton instance of the BigDecimalValidator.

  - 

### isInRange

public boolean isInRange(BigDecimal value,
 double min,
 double max)
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

public boolean maxValue(BigDecimal value,
 double max)
Check if the value is less than or equal to a maximum.

Parameters:
`value` - The value validation is being performed on.
`max` - The maximum value.
Returns:
`true` if the value is less than
         or equal to the maximum.

  - 

### minValue

public boolean minValue(BigDecimal value,
 double min)
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
Convert the parsed value to a `BigDecimal`.

Specified by:
`processParsedValue` in class `AbstractNumberValidator`
Parameters:
`value` - The parsed `Number` object created.
`formatter` - The Format used to parse the value with.
Returns:
The parsed `Number` converted to a
         `BigDecimal`.

  - 

### validate

public BigDecimal validate(String value)

Validate/convert a `BigDecimal` using the default
    `Locale`.

Parameters:
`value` - The value validation is being performed on.
Returns:
The parsed `BigDecimal` if valid or `null`
  if invalid.

  - 

### validate

public BigDecimal validate(String value,
 Locale locale)

Validate/convert a `BigDecimal` using the
    specified `Locale`.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use for the number format, system default if null.
Returns:
The parsed `BigDecimal` if valid or `null` if invalid.

  - 

### validate

public BigDecimal validate(String value,
 String pattern)

Validate/convert a `BigDecimal` using the
    specified *pattern*.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against, or the
        default for the `Locale` if `null`.
Returns:
The parsed `BigDecimal` if valid or `null` if invalid.

  - 

### validate

public BigDecimal validate(String value,
 String pattern,
 Locale locale)

Validate/convert a `BigDecimal` using the
    specified pattern and/ or `Locale`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against, or the
        default for the `Locale` if `null`.
`locale` - The locale to use for the date format, system default if null.
Returns:
The parsed `BigDecimal` if valid or `null` if invalid.