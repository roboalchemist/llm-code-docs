Package org.apache.commons.validator.routines

# Class PercentValidator

java.lang.Object
org.apache.commons.validator.routines.AbstractFormatValidator
org.apache.commons.validator.routines.AbstractNumberValidator
org.apache.commons.validator.routines.BigDecimalValidator
org.apache.commons.validator.routines.PercentValidator

All Implemented Interfaces:
`Serializable`

---

public class PercentValidator
extends BigDecimalValidator

**Percentage Validation** and Conversion routines (`java.math.BigDecimal`).

 

This is one implementation of a percent validator that has the following features:
    

       
- It is *lenient* about the presence of the *percent symbol*
       
- It converts the percent to a `java.math.BigDecimal`
    

 

However any of the *number* validators can be used for *percent* validation.
    For example, if you wanted a *percent* validator that converts to a
    {`Float` then you can simply instantiate an
    `FloatValidator` with the appropriate *format type*:

    

`... = new FloatValidator(false, FloatValidator.PERCENT_FORMAT);`

 

Pick the appropriate validator, depending on the type (that is, Float, Double or BigDecimal)
    you want the percent converted to. Please note, it makes no sense to use
    one of the validators that doesn't handle fractions (such as byte, short, integer, long
    and BigInteger) since percentages are converted to fractions (for example, `50%` is
    converted to `0.5`).

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
`PercentValidator()`

Constructs a *strict* instance.

`PercentValidator(boolean strict)`

Constructs an instance with the specified strict setting.

- 

## Method Summary

Modifier and Type
Method
Description
`static BigDecimalValidator`
`getInstance()`

Gets the singleton instance of this validator.

`protected Object`
`parse(String value,
 Format formatter)`

Parse the value with the specified `Format`.

### Methods inherited from class org.apache.commons.validator.routines.BigDecimalValidator

`isInRange, maxValue, minValue, processParsedValue, validate, validate, validate, validate`

### Methods inherited from class org.apache.commons.validator.routines.AbstractNumberValidator

`determineScale, getFormat, getFormat, getFormatType, isAllowFractions, isInRange, isValid, maxValue, minValue, parse`

### Methods inherited from class org.apache.commons.validator.routines.AbstractFormatValidator

`format, format, format, format, format, isStrict, isValid, isValid, isValid`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### PercentValidator

public PercentValidator()
Constructs a *strict* instance.

  - 

### PercentValidator

public PercentValidator(boolean strict)
Constructs an instance with the specified strict setting.

Parameters:
`strict` - `true` if strict
        `Format` parsing should be used.

- 

## Method Details

  - 

### getInstance

public static BigDecimalValidator getInstance()
Gets the singleton instance of this validator.

Returns:
A singleton instance of the PercentValidator.

  - 

### parse

protected Object parse(String value,
 Format formatter)

Parse the value with the specified `Format`.

 

This implementation is lenient whether the currency symbol
    is present or not. The default `NumberFormat`
    behavior is for the parsing to "fail" if the currency
    symbol is missing. This method re-parses with a format
    without the currency symbol if it fails initially.

Overrides:
`parse` in class `AbstractFormatValidator`
Parameters:
`value` - The value to be parsed.
`formatter` - The Format to parse the value with.
Returns:
The parsed value if valid or `null` if invalid.