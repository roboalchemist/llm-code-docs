Package org.apache.commons.validator.routines

# Class CalendarValidator

java.lang.Object
org.apache.commons.validator.routines.AbstractFormatValidator
org.apache.commons.validator.routines.AbstractCalendarValidator
org.apache.commons.validator.routines.CalendarValidator

All Implemented Interfaces:
`Serializable`

---

public class CalendarValidator
extends AbstractCalendarValidator

**Calendar Validation** and Conversion routines (`java.util.Calendar`).

 

This validator provides a number of methods for validating/converting
    a `String` date value to a `java.util.Calendar` using
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
    *converted* `Calendar` value.

 

Implementations of the `validate()` method are provided
    to create `Calendar` objects for different *time zones*
    if the system default is not appropriate.

 

Alternatively the CalendarValidator's `adjustToTimeZone()` method
    can be used to adjust the `TimeZone` of the `Calendar`
    object afterward.

 

Once a value has been successfully converted the following
    methods can be used to perform various date comparison checks:
    

       
- `compareDates()` compares the day, month and
           year of two calendars, returning 0, -1 or +1 indicating
           whether the first date is equal, before or after the second.
       
- `compareWeeks()` compares the week and
           year of two calendars, returning 0, -1 or +1 indicating
           whether the first week is equal, before or after the second.
       
- `compareMonths()` compares the month and
           year of two calendars, returning 0, -1 or +1 indicating
           whether the first month is equal, before or after the second.
       
- `compareQuarters()` compares the quarter and
           year of two calendars, returning 0, -1 or +1 indicating
           whether the first quarter is equal, before or after the second.
       
- `compareYears()` compares the
           year of two calendars, returning 0, -1 or +1 indicating
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
`CalendarValidator()`

Constructs a *strict* instance with *short*
 date style.

`CalendarValidator(boolean strict,
 int dateStyle)`

Constructs an instance with the specified *strict*
 and *date style* parameters.

- 

## Method Summary

Modifier and Type
Method
Description
`static void`
`adjustToTimeZone(Calendar value,
 TimeZone timeZone)`

Adjusts a Calendar's value to a different TimeZone.

`int`
`compareDates(Calendar value,
 Calendar compare)`

Compare Dates (day, month and year - not time).

`int`
`compareMonths(Calendar value,
 Calendar compare)`

Compare Months (month and year).

`int`
`compareQuarters(Calendar value,
 Calendar compare)`

Compare Quarters (quarter and year).

`int`
`compareQuarters(Calendar value,
 Calendar compare,
 int monthOfFirstQuarter)`

Compare Quarters (quarter and year).

`int`
`compareWeeks(Calendar value,
 Calendar compare)`

Compare Weeks (week and year).

`int`
`compareYears(Calendar value,
 Calendar compare)`

Compare Years.

`static CalendarValidator`
`getInstance()`

Gets the singleton instance of this validator.

`protected Object`
`processParsedValue(Object value,
 Format formatter)`

Convert the parsed `Date` to a `Calendar`.

`Calendar`
`validate(String value)`

Validate/convert a `Calendar` using the default
    `Locale` and `TimeZone`.

`Calendar`
`validate(String value,
 String pattern)`

Validate/convert a `Calendar` using the specified
    *pattern* and default `TimeZone`.

`Calendar`
`validate(String value,
 String pattern,
 Locale locale)`

Validate/convert a `Calendar` using the specified pattern
    and `Locale` and the default `TimeZone`.

`Calendar`
`validate(String value,
 String pattern,
 Locale locale,
 TimeZone timeZone)`

Validate/convert a `Calendar` using the specified
    pattern, and `Locale` and `TimeZone`.

`Calendar`
`validate(String value,
 String pattern,
 TimeZone timeZone)`

Validate/convert a `Calendar` using the specified
    *pattern* and `TimeZone`.

`Calendar`
`validate(String value,
 Locale locale)`

Validate/convert a `Calendar` using the specified
    `Locale` and default `TimeZone`.

`Calendar`
`validate(String value,
 Locale locale,
 TimeZone timeZone)`

Validate/convert a `Calendar` using the specified
    `Locale` and `TimeZone`.

`Calendar`
`validate(String value,
 TimeZone timeZone)`

Validate/convert a `Calendar` using the specified
    `TimeZone` and default `Locale`.

### Methods inherited from class org.apache.commons.validator.routines.AbstractCalendarValidator

`compare, compareTime, format, format, format, format, format, format, getFormat, getFormat, isValid, parse`

### Methods inherited from class org.apache.commons.validator.routines.AbstractFormatValidator

`format, format, format, isStrict, isValid, isValid, isValid, parse`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### CalendarValidator

public CalendarValidator()
Constructs a *strict* instance with *short*
 date style.

  - 

### CalendarValidator

public CalendarValidator(boolean strict,
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

### adjustToTimeZone

public static void adjustToTimeZone(Calendar value,
 TimeZone timeZone)

Adjusts a Calendar's value to a different TimeZone.

Parameters:
`value` - The value to adjust.
`timeZone` - The new time zone to use to adjust the Calendar to.

  - 

### getInstance

public static CalendarValidator getInstance()
Gets the singleton instance of this validator.

Returns:
A singleton instance of the CalendarValidator.

  - 

### compareDates

public int compareDates(Calendar value,
 Calendar compare)

Compare Dates (day, month and year - not time).

Parameters:
`value` - The `Calendar` value to check.
`compare` - The `Calendar` to compare the value to.
Returns:
Zero if the dates are equal, -1 if first
 date is less than the seconds and +1 if the first
 date is greater than.

  - 

### compareMonths

public int compareMonths(Calendar value,
 Calendar compare)

Compare Months (month and year).

Parameters:
`value` - The `Calendar` value to check.
`compare` - The `Calendar` to compare the value to.
Returns:
Zero if the months are equal, -1 if first
 parameter's month is less than the seconds and +1 if the first
 parameter's month is greater than.

  - 

### compareQuarters

public int compareQuarters(Calendar value,
 Calendar compare)

Compare Quarters (quarter and year).

Parameters:
`value` - The `Calendar` value to check.
`compare` - The `Calendar` to check the value against.
Returns:
Zero if the quarters are equal, -1 if first
 parameter's quarter is less than the seconds and +1 if the first
 parameter's quarter is greater than.

  - 

### compareQuarters

public int compareQuarters(Calendar value,
 Calendar compare,
 int monthOfFirstQuarter)

Compare Quarters (quarter and year).

Overrides:
`compareQuarters` in class `AbstractCalendarValidator`
Parameters:
`value` - The `Calendar` value to check.
`compare` - The `Calendar` to compare the value to.
`monthOfFirstQuarter` - The  month that the first quarter starts.
Returns:
Zero if the quarters are equal, -1 if first
 parameter's quarter is less than the seconds and +1 if the first
 parameter's quarter is greater than.

  - 

### compareWeeks

public int compareWeeks(Calendar value,
 Calendar compare)

Compare Weeks (week and year).

Parameters:
`value` - The `Calendar` value to check.
`compare` - The `Calendar` to compare the value to.
Returns:
Zero if the weeks are equal, -1 if first
 parameter's week is less than the seconds and +1 if the first
 parameter's week is greater than.

  - 

### compareYears

public int compareYears(Calendar value,
 Calendar compare)

Compare Years.

Parameters:
`value` - The `Calendar` value to check.
`compare` - The `Calendar` to compare the value to.
Returns:
Zero if the years are equal, -1 if first
 parameter's year is less than the seconds and +1 if the first
 parameter's year is greater than.

  - 

### processParsedValue

protected Object processParsedValue(Object value,
 Format formatter)

Convert the parsed `Date` to a `Calendar`.

Specified by:
`processParsedValue` in class `AbstractCalendarValidator`
Parameters:
`value` - The parsed `Date` object created.
`formatter` - The Format used to parse the value with.
Returns:
The parsed value converted to a `Calendar`.

  - 

### validate

public Calendar validate(String value)

Validate/convert a `Calendar` using the default
    `Locale` and `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
Returns:
The parsed `Calendar` if valid or `null`
  if invalid.

  - 

### validate

public Calendar validate(String value,
 Locale locale)

Validate/convert a `Calendar` using the specified
    `Locale` and default `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use for the date format, system default if null.
Returns:
The parsed `Calendar` if valid or `null` if invalid.

  - 

### validate

public Calendar validate(String value,
 Locale locale,
 TimeZone timeZone)

Validate/convert a `Calendar` using the specified
    `Locale` and `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use for the date format, system default if null.
`timeZone` - The Time Zone used to parse the date, system default if null.
Returns:
The parsed `Calendar` if valid or `null` if invalid.

  - 

### validate

public Calendar validate(String value,
 String pattern)

Validate/convert a `Calendar` using the specified
    *pattern* and default `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against.
Returns:
The parsed `Calendar` if valid or `null` if invalid.

  - 

### validate

public Calendar validate(String value,
 String pattern,
 Locale locale)

Validate/convert a `Calendar` using the specified pattern
    and `Locale` and the default `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against, or the
        default for the `Locale` if `null`.
`locale` - The locale to use for the date format, system default if null.
Returns:
The parsed `Calendar` if valid or `null` if invalid.

  - 

### validate

public Calendar validate(String value,
 String pattern,
 Locale locale,
 TimeZone timeZone)

Validate/convert a `Calendar` using the specified
    pattern, and `Locale` and `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against, or the
        default for the `Locale` if `null`.
`locale` - The locale to use for the date format, system default if null.
`timeZone` - The Time Zone used to parse the date, system default if null.
Returns:
The parsed `Calendar` if valid or `null` if invalid.

  - 

### validate

public Calendar validate(String value,
 String pattern,
 TimeZone timeZone)

Validate/convert a `Calendar` using the specified
    *pattern* and `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against.
`timeZone` - The Time Zone used to parse the date, system default if null.
Returns:
The parsed `Calendar` if valid or `null` if invalid.

  - 

### validate

public Calendar validate(String value,
 TimeZone timeZone)

Validate/convert a `Calendar` using the specified
    `TimeZone` and default `Locale`.

Parameters:
`value` - The value validation is being performed on.
`timeZone` - The Time Zone used to parse the date, system default if null.
Returns:
The parsed `Calendar` if valid or `null`
  if invalid.