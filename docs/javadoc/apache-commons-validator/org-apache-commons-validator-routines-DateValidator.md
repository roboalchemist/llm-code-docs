Package org.apache.commons.validator.routines

# Class DateValidator

java.lang.Object
org.apache.commons.validator.routines.AbstractFormatValidator
org.apache.commons.validator.routines.AbstractCalendarValidator
org.apache.commons.validator.routines.DateValidator

All Implemented Interfaces:
`Serializable`

---

public class DateValidator
extends AbstractCalendarValidator

**Date Validation** and Conversion routines (`java.util.Date`).

 

This validator provides a number of methods for validating/converting
    a `String` date value to a `java.util.Date` using
    `DateFormat` to parse either:
    

       
- using the default format for the default `Locale`
       
- using a specified pattern with the default `Locale`
       
- using the default format for a specified `Locale`
       
- using a specified pattern with a specified `Locale`
    

 

For each of the above mechanisms, conversion method (that is, the
    `validate` methods) implementations are provided which
    either use the default `TimeZone` or allow the
    `TimeZone` to be specified.

 

Use one of the `isValid()` methods to just validate or
    one of the `validate()` methods to validate and receive a
    *converted* `Date` value.

 

Implementations of the `validate()` method are provided
    to create `Date` objects for different *time zones*
    if the system default is not appropriate.

 

Once a value has been successfully converted the following
    methods can be used to perform various date comparison checks:
    

       
- `compareDates()` compares the day, month and
           year of two dates, returning 0, -1 or +1 indicating
           whether the first date is equal, before or after the second.
       
- `compareWeeks()` compares the week and
           year of two dates, returning 0, -1 or +1 indicating
           whether the first week is equal, before or after the second.
       
- `compareMonths()` compares the month and
           year of two dates, returning 0, -1 or +1 indicating
           whether the first month is equal, before or after the second.
       
- `compareQuarters()` compares the quarter and
           year of two dates, returning 0, -1 or +1 indicating
           whether the first quarter is equal, before or after the second.
       
- `compareYears()` compares the
           year of two dates, returning 0, -1 or +1 indicating
           whether the first year is equal, before or after the second.
    

 

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

## Constructor Summary

Constructors

Constructor
Description
`DateValidator()`

Constructs a *strict* instance with *short*
 date style.

`DateValidator(boolean strict,
 int dateStyle)`

Constructs an instance with the specified *strict*
 and *date style* parameters.

- 

## Method Summary

Modifier and Type
Method
Description
`int`
`compareDates(Date value,
 Date compare,
 TimeZone timeZone)`

Compare Dates (day, month and year - not time).

`int`
`compareMonths(Date value,
 Date compare,
 TimeZone timeZone)`

Compare Months (month and year).

`int`
`compareQuarters(Date value,
 Date compare,
 TimeZone timeZone)`

Compare Quarters (quarter and year).

`int`
`compareQuarters(Date value,
 Date compare,
 TimeZone timeZone,
 int monthOfFirstQuarter)`

Compare Quarters (quarter and year).

`int`
`compareWeeks(Date value,
 Date compare,
 TimeZone timeZone)`

Compare Weeks (week and year).

`int`
`compareYears(Date value,
 Date compare,
 TimeZone timeZone)`

Compare Years.

`static DateValidator`
`getInstance()`

Gets the singleton instance of this validator.

`protected Object`
`processParsedValue(Object value,
 Format formatter)`

Returns the parsed `Date` unchanged.

`Date`
`validate(String value)`

Validate/convert a `Date` using the default
    `Locale` and `TimeZone`.

`Date`
`validate(String value,
 String pattern)`

Validate/convert a `Date` using the specified
    *pattern* and default `TimeZone`.

`Date`
`validate(String value,
 String pattern,
 Locale locale)`

Validate/convert a `Date` using the specified pattern
    and `Locale` and the default `TimeZone`.

`Date`
`validate(String value,
 String pattern,
 Locale locale,
 TimeZone timeZone)`

Validate/convert a `Date` using the specified
    pattern, and `Locale` and `TimeZone`.

`Date`
`validate(String value,
 String pattern,
 TimeZone timeZone)`

Validate/convert a `Date` using the specified
    *pattern* and `TimeZone`.

`Date`
`validate(String value,
 Locale locale)`

Validate/convert a `Date` using the specified
    `Locale` and default `TimeZone`.

`Date`
`validate(String value,
 Locale locale,
 TimeZone timeZone)`

Validate/convert a `Date` using the specified
    `Locale` and `TimeZone`.

`Date`
`validate(String value,
 TimeZone timeZone)`

Validate/convert a `Date` using the specified
    `TimeZone` and default `Locale`.

### Methods inherited from class org.apache.commons.validator.routines.AbstractCalendarValidator

`compare, compareQuarters, compareTime, format, format, format, format, format, format, getFormat, getFormat, isValid, parse`

### Methods inherited from class org.apache.commons.validator.routines.AbstractFormatValidator

`format, format, format, isStrict, isValid, isValid, isValid, parse`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### DateValidator

public DateValidator()
Constructs a *strict* instance with *short*
 date style.

  - 

### DateValidator

public DateValidator(boolean strict,
 int dateStyle)
Constructs an instance with the specified *strict*
 and *date style* parameters.

Parameters:
`strict` - `true` if strict
        `Format` parsing should be used.
`dateStyle` - the date style to use for Locale validation.

- 

## Method Details

  - 

### getInstance

public static DateValidator getInstance()
Gets the singleton instance of this validator.

Returns:
A singleton instance of the DateValidator.

  - 

### compareDates

public int compareDates(Date value,
 Date compare,
 TimeZone timeZone)

Compare Dates (day, month and year - not time).

Parameters:
`value` - The `Calendar` value to check.
`compare` - The `Calendar` to compare the value to.
`timeZone` - The Time Zone used to compare the dates, system default if null.
Returns:
Zero if the dates are equal, -1 if first
 date is less than the seconds and +1 if the first
 date is greater than.

  - 

### compareMonths

public int compareMonths(Date value,
 Date compare,
 TimeZone timeZone)

Compare Months (month and year).

Parameters:
`value` - The `Date` value to check.
`compare` - The `Date` to compare the value to.
`timeZone` - The Time Zone used to compare the dates, system default if null.
Returns:
Zero if the months are equal, -1 if first
 parameter's month is less than the seconds and +1 if the first
 parameter's month is greater than.

  - 

### compareQuarters

public int compareQuarters(Date value,
 Date compare,
 TimeZone timeZone)

Compare Quarters (quarter and year).

Parameters:
`value` - The `Date` value to check.
`compare` - The `Date` to compare the value to.
`timeZone` - The Time Zone used to compare the dates, system default if null.
Returns:
Zero if the months are equal, -1 if first
 parameter's quarter is less than the seconds and +1 if the first
 parameter's quarter is greater than.

  - 

### compareQuarters

public int compareQuarters(Date value,
 Date compare,
 TimeZone timeZone,
 int monthOfFirstQuarter)

Compare Quarters (quarter and year).

Parameters:
`value` - The `Date` value to check.
`compare` - The `Date` to compare the value to.
`timeZone` - The Time Zone used to compare the dates, system default if null.
`monthOfFirstQuarter` - The  month that the first quarter starts.
Returns:
Zero if the quarters are equal, -1 if first
 parameter's quarter is less than the seconds and +1 if the first
 parameter's quarter is greater than.

  - 

### compareWeeks

public int compareWeeks(Date value,
 Date compare,
 TimeZone timeZone)

Compare Weeks (week and year).

Parameters:
`value` - The `Date` value to check.
`compare` - The `Date` to compare the value to.
`timeZone` - The Time Zone used to compare the dates, system default if null.
Returns:
Zero if the weeks are equal, -1 if first
 parameter's week is less than the seconds and +1 if the first
 parameter's week is greater than.

  - 

### compareYears

public int compareYears(Date value,
 Date compare,
 TimeZone timeZone)

Compare Years.

Parameters:
`value` - The `Date` value to check.
`compare` - The `Date` to compare the value to.
`timeZone` - The Time Zone used to compare the dates, system default if null.
Returns:
Zero if the years are equal, -1 if first
 parameter's year is less than the seconds and +1 if the first
 parameter's year is greater than.

  - 

### processParsedValue

protected Object processParsedValue(Object value,
 Format formatter)

Returns the parsed `Date` unchanged.

Specified by:
`processParsedValue` in class `AbstractCalendarValidator`
Parameters:
`value` - The parsed `Date` object created.
`formatter` - The Format used to parse the value with.
Returns:
The parsed value converted to a `Calendar`.

  - 

### validate

public Date validate(String value)

Validate/convert a `Date` using the default
    `Locale` and `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
Returns:
The parsed `Date` if valid or `null`
  if invalid.

  - 

### validate

public Date validate(String value,
 Locale locale)

Validate/convert a `Date` using the specified
    `Locale` and default `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use for the date format, system default if null.
Returns:
The parsed `Date` if valid or `null` if invalid.

  - 

### validate

public Date validate(String value,
 Locale locale,
 TimeZone timeZone)

Validate/convert a `Date` using the specified
    `Locale` and `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use for the date format, system default if null.
`timeZone` - The Time Zone used to parse the date, system default if null.
Returns:
The parsed `Date` if valid or `null` if invalid.

  - 

### validate

public Date validate(String value,
 String pattern)

Validate/convert a `Date` using the specified
    *pattern* and default `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against, or the
        default for the `Locale` if `null`.
Returns:
The parsed `Date` if valid or `null` if invalid.

  - 

### validate

public Date validate(String value,
 String pattern,
 Locale locale)

Validate/convert a `Date` using the specified pattern
    and `Locale` and the default `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against, or the
        default for the `Locale` if `null`.
`locale` - The locale to use for the date format, system default if null.
Returns:
The parsed `Date` if valid or `null` if invalid.

  - 

### validate

public Date validate(String value,
 String pattern,
 Locale locale,
 TimeZone timeZone)

Validate/convert a `Date` using the specified
    pattern, and `Locale` and `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against, or the
        default for the `Locale` if `null`.
`locale` - The locale to use for the date format, system default if null.
`timeZone` - The Time Zone used to parse the date, system default if null.
Returns:
The parsed `Date` if valid or `null` if invalid.

  - 

### validate

public Date validate(String value,
 String pattern,
 TimeZone timeZone)

Validate/convert a `Date` using the specified
    *pattern* and `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against, or the
        default for the `Locale` if `null`.
`timeZone` - The Time Zone used to parse the date, system default if null.
Returns:
The parsed `Date` if valid or `null` if invalid.

  - 

### validate

public Date validate(String value,
 TimeZone timeZone)

Validate/convert a `Date` using the specified
    `TimeZone` and default `Locale`.

Parameters:
`value` - The value validation is being performed on.
`timeZone` - The Time Zone used to parse the date, system default if null.
Returns:
The parsed `Date` if valid or `null` if invalid.