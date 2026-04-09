Package org.apache.commons.validator.routines

# Class TimeValidator

java.lang.Object
org.apache.commons.validator.routines.AbstractFormatValidator
org.apache.commons.validator.routines.AbstractCalendarValidator
org.apache.commons.validator.routines.TimeValidator

All Implemented Interfaces:
`Serializable`

---

public class TimeValidator
extends AbstractCalendarValidator

**Time Validation** and Conversion routines (`java.util.Calendar`).

 

This validator provides a number of methods for validating/converting
    a `String` time value to a `java.util.Calendar` using
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
    *converted* `Calendar` value for the time.

 

Implementations of the `validate()` method are provided
    to create `Calendar` objects for different *time zones*
    if the system default is not appropriate.

 

Alternatively the CalendarValidator's `adjustToTimeZone()` method
    can be used to adjust the `TimeZone` of the `Calendar`
    object afterwards.

 

Once a value has been successfully converted the following
    methods can be used to perform various time comparison checks:
    

       
- `compareTime()` compares the hours, minutes, seconds
           and milliseconds of two calendars, returning 0, -1 or +1 indicating
           whether the first time is equal, before or after the second.
       
- `compareSeconds()` compares the hours, minutes and
           seconds of two times, returning 0, -1 or +1 indicating
           whether the first is equal to, before or after the second.
       
- `compareMinutes()` compares the hours and minutes
           two times, returning 0, -1 or +1 indicating
           whether the first is equal to, before or after the second.
       
- `compareHours()` compares the hours
           of two times, returning 0, -1 or +1 indicating
           whether the first is equal to, before or after the second.
    

 

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
`TimeValidator()`

Constructs a *strict* instance with *short*
 time style.

`TimeValidator(boolean strict,
 int timeStyle)`

Constructs an instance with the specified *strict*
 and *time style* parameters.

- 

## Method Summary

Modifier and Type
Method
Description
`int`
`compareHours(Calendar value,
 Calendar compare)`

Compare Hours.

`int`
`compareMinutes(Calendar value,
 Calendar compare)`

Compare Minutes (hours and minutes).

`int`
`compareSeconds(Calendar value,
 Calendar compare)`

Compare Seconds (hours, minutes and seconds).

`int`
`compareTime(Calendar value,
 Calendar compare)`

Compare Times (hour, minute, second and millisecond - not date).

`static TimeValidator`
`getInstance()`

Gets the singleton instance of this validator.

`protected Object`
`processParsedValue(Object value,
 Format formatter)`

Convert the parsed `Date` to a `Calendar`.

`Calendar`
`validate(String value)`

Validate/convert a time using the default `Locale`
    and `TimeZone`.

`Calendar`
`validate(String value,
 String pattern)`

Validate/convert a time using the specified *pattern* and
    default `TimeZone`.

`Calendar`
`validate(String value,
 String pattern,
 Locale locale)`

Validate/convert a time using the specified pattern and `Locale`
    and the default `TimeZone`.

`Calendar`
`validate(String value,
 String pattern,
 Locale locale,
 TimeZone timeZone)`

Validate/convert a time using the specified pattern, `Locale`
    and `TimeZone`.

`Calendar`
`validate(String value,
 String pattern,
 TimeZone timeZone)`

Validate/convert a time using the specified *pattern*
    and `TimeZone`.

`Calendar`
`validate(String value,
 Locale locale)`

Validate/convert a time using the specified `Locale`
    default `TimeZone`.

`Calendar`
`validate(String value,
 Locale locale,
 TimeZone timeZone)`

Validate/convert a time using the specified `Locale`
    and `TimeZone`.

`Calendar`
`validate(String value,
 TimeZone timeZone)`

Validate/convert a time using the specified `TimeZone`
    and default `Locale`.

### Methods inherited from class org.apache.commons.validator.routines.AbstractCalendarValidator

`compare, compareQuarters, compareTime, format, format, format, format, format, format, getFormat, getFormat, isValid, parse`

### Methods inherited from class org.apache.commons.validator.routines.AbstractFormatValidator

`format, format, format, isStrict, isValid, isValid, isValid, parse`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### TimeValidator

public TimeValidator()
Constructs a *strict* instance with *short*
 time style.

  - 

### TimeValidator

public TimeValidator(boolean strict,
 int timeStyle)
Constructs an instance with the specified *strict*
 and *time style* parameters.

Parameters:
`strict` - `true` if strict
        `Format` parsing should be used.
`timeStyle` - the time style to use for Locale validation.

- 

## Method Details

  - 

### getInstance

public static TimeValidator getInstance()
Gets the singleton instance of this validator.

Returns:
A singleton instance of the TimeValidator.

  - 

### compareHours

public int compareHours(Calendar value,
 Calendar compare)

Compare Hours.

Parameters:
`value` - The `Calendar` value to check.
`compare` - The `Calendar` to compare the value to.
Returns:
Zero if the hours are equal, -1 if first
 parameter's hour is less than the seconds and +1 if the first
 parameter's hour is greater than.

  - 

### compareMinutes

public int compareMinutes(Calendar value,
 Calendar compare)

Compare Minutes (hours and minutes).

Parameters:
`value` - The `Calendar` value to check.
`compare` - The `Calendar` to compare the value to.
Returns:
Zero if the hours are equal, -1 if first
 parameter's minutes are less than the seconds and +1 if the first
 parameter's minutes are greater than.

  - 

### compareSeconds

public int compareSeconds(Calendar value,
 Calendar compare)

Compare Seconds (hours, minutes and seconds).

Parameters:
`value` - The `Calendar` value to check.
`compare` - The `Calendar` to compare the value to.
Returns:
Zero if the hours are equal, -1 if first
 parameter's seconds are less than the seconds and +1 if the first
 parameter's seconds are greater than.

  - 

### compareTime

public int compareTime(Calendar value,
 Calendar compare)

Compare Times (hour, minute, second and millisecond - not date).

Parameters:
`value` - The `Calendar` value to check.
`compare` - The `Calendar` to compare the value to.
Returns:
Zero if the hours are equal, -1 if first
 time is less than the seconds and +1 if the first
 time is greater than.

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

Validate/convert a time using the default `Locale`
    and `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
Returns:
The parsed `Calendar` if valid or `null`
  if invalid.

  - 

### validate

public Calendar validate(String value,
 Locale locale)

Validate/convert a time using the specified `Locale`
    default `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use for the time format, system default if null.
Returns:
The parsed `Calendar` if valid or `null` if invalid.

  - 

### validate

public Calendar validate(String value,
 Locale locale,
 TimeZone timeZone)

Validate/convert a time using the specified `Locale`
    and `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use for the time format, system default if null.
`timeZone` - The Time Zone used to parse the time, system default if null.
Returns:
The parsed `Calendar` if valid or `null` if invalid.

  - 

### validate

public Calendar validate(String value,
 String pattern)

Validate/convert a time using the specified *pattern* and
    default `TimeZone`.

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

Validate/convert a time using the specified pattern and `Locale`
    and the default `TimeZone`.

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

Validate/convert a time using the specified pattern, `Locale`
    and `TimeZone`.

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

Validate/convert a time using the specified *pattern*
    and `TimeZone`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against.
`timeZone` - The Time Zone used to parse the time, system default if null.
Returns:
The parsed `Calendar` if valid or `null` if invalid.

  - 

### validate

public Calendar validate(String value,
 TimeZone timeZone)

Validate/convert a time using the specified `TimeZone`
    and default `Locale`.

Parameters:
`value` - The value validation is being performed on.
`timeZone` - The Time Zone used to parse the time, system default if null.
Returns:
The parsed `Calendar` if valid or `null` if invalid.