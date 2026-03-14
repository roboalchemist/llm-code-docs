Package org.apache.commons.validator.routines

# Class CurrencyValidator

java.lang.Object
org.apache.commons.validator.routines.AbstractFormatValidator
org.apache.commons.validator.routines.AbstractNumberValidator
org.apache.commons.validator.routines.BigDecimalValidator
org.apache.commons.validator.routines.CurrencyValidator

All Implemented Interfaces:
`Serializable`

---

public class CurrencyValidator
extends BigDecimalValidator

**Currency Validation** and Conversion routines (`java.math.BigDecimal`).

 

This is one implementation of a currency validator that has the following features:
    

       
- It is *lenient* about the presence of the *currency symbol*
       
- It converts the currency to a `java.math.BigDecimal`
    

 

However any of the *number* validators can be used for *currency* validation.
    For example, if you wanted a *currency* validator that converts to a
    `Integer` then you can simply instantiate an
    `IntegerValidator` with the appropriate *format type*:

    

`... = new IntegerValidator(false, IntegerValidator.CURRENCY_FORMAT);`

 

Pick the appropriate validator, depending on the type (for example, Float, Double, Integer, Long and so on)
    you want the currency converted to. One thing to note - only the CurrencyValidator
    implements *lenient* behavior regarding the currency symbol.

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
`CurrencyValidator()`

Constructs a *strict* instance.

`CurrencyValidator(boolean strict,
 boolean allowFractions)`

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

### CurrencyValidator

public CurrencyValidator()
Constructs a *strict* instance.

  - 

### CurrencyValidator

public CurrencyValidator(boolean strict,
 boolean allowFractions)
Constructs an instance with the specified strict setting.

Parameters:
`strict` - `true` if strict
        `Format` parsing should be used.
`allowFractions` - `true` if fractions are
        allowed or `false` if integers only.

- 

## Method Details

  - 

### getInstance

public static BigDecimalValidator getInstance()
Gets the singleton instance of this validator.

Returns:
A singleton instance of the CurrencyValidator.

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