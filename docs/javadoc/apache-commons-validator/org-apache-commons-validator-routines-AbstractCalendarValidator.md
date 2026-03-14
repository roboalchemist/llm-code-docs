Package org.apache.commons.validator.routines

# Class AbstractCalendarValidator

java.lang.Object
org.apache.commons.validator.routines.AbstractFormatValidator
org.apache.commons.validator.routines.AbstractCalendarValidator

All Implemented Interfaces:
`Serializable`

Direct Known Subclasses:
`CalendarValidator`, `DateValidator`, `TimeValidator`

---

public abstract class AbstractCalendarValidator
extends AbstractFormatValidator

Abstract class for Date/Time/Calendar validation.

 

This is a *base* class for building Date / Time
    Validators using format parsing.

Since:
1.3.0
See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`AbstractCalendarValidator(boolean strict,
 int dateStyle,
 int timeStyle)`

Constructs an instance with the specified *strict*,
 *time* and *date* style parameters.

- 

## Method Summary

Modifier and Type
Method
Description
`protected int`
`compare(Calendar value,
 Calendar compare,
 int field)`

Compares a calendar value to another, indicating whether it is
    equal, less than or more than at a specified level.

`protected int`
`compareQuarters(Calendar value,
 Calendar compare,
 int monthOfFirstQuarter)`

Compares a calendar's quarter value to another, indicating whether it is
    equal, less than or more than the specified quarter.

`protected int`
`compareTime(Calendar value,
 Calendar compare,
 int field)`

Compares a calendar time value to another, indicating whether it is
    equal, less than or more than at a specified level.

`String`
`format(Object value,
 String pattern,
 Locale locale)`

Format an object using the specified pattern and/or
    `Locale`.

`String`
`format(Object value,
 String pattern,
 Locale locale,
 TimeZone timeZone)`

Format an object using the specified pattern and/or
    `Locale`.

`String`
`format(Object value,
 String pattern,
 TimeZone timeZone)`

Format an object into a `String` using
 the specified pattern.

`protected String`
`format(Object value,
 Format formatter)`

Format a value with the specified `DateFormat`.

`String`
`format(Object value,
 Locale locale,
 TimeZone timeZone)`

Format an object into a `String` using
 the specified Locale.

`String`
`format(Object value,
 TimeZone timeZone)`

Format an object into a `String` using
 the default Locale.

`protected Format`
`getFormat(String pattern,
 Locale locale)`

Returns a `DateFormat` for the specified *pattern*
    and/or `Locale`.

`protected Format`
`getFormat(Locale locale)`

Returns a `DateFormat` for the specified Locale.

`boolean`
`isValid(String value,
 String pattern,
 Locale locale)`

Validate using the specified `Locale`.

`protected Object`
`parse(String value,
 String pattern,
 Locale locale,
 TimeZone timeZone)`

Checks if the value is valid against a specified pattern.

`protected abstract Object`
`processParsedValue(Object value,
 Format formatter)`

Process the parsed value, performing any further validation
    and type conversion required.

### Methods inherited from class org.apache.commons.validator.routines.AbstractFormatValidator

`format, format, format, isStrict, isValid, isValid, isValid, parse`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### AbstractCalendarValidator

public AbstractCalendarValidator(boolean strict,
 int dateStyle,
 int timeStyle)
Constructs an instance with the specified *strict*,
 *time* and *date* style parameters.

Parameters:
`strict` - `true` if strict
        `Format` parsing should be used.
`dateStyle` - the date style to use for Locale validation.
`timeStyle` - the time style to use for Locale validation.

- 

## Method Details

  - 

### compare

protected int compare(Calendar value,
 Calendar compare,
 int field)

Compares a calendar value to another, indicating whether it is
    equal, less than or more than at a specified level.

Parameters:
`value` - The Calendar value.
`compare` - The `Calendar` to check the value against.
`field` - The field *level* to compare to - for example, specifying
        `Calendar.MONTH` will compare the year and month
        portions of the calendar.
Returns:
Zero if the first value is equal to the second, -1
         if it is less than the second or +1 if it is greater than the second.

  - 

### compareQuarters

protected int compareQuarters(Calendar value,
 Calendar compare,
 int monthOfFirstQuarter)

Compares a calendar's quarter value to another, indicating whether it is
    equal, less than or more than the specified quarter.

Parameters:
`value` - The Calendar value.
`compare` - The `Calendar` to check the value against.
`monthOfFirstQuarter` - The  month that the first quarter starts.
Returns:
Zero if the first quarter is equal to the second, -1
         if it is less than the second or +1 if it is greater than the second.

  - 

### compareTime

protected int compareTime(Calendar value,
 Calendar compare,
 int field)

Compares a calendar time value to another, indicating whether it is
    equal, less than or more than at a specified level.

Parameters:
`value` - The Calendar value.
`compare` - The `Calendar` to check the value against.
`field` - The field *level* to compare to - for example, specifying
        `Calendar.MINUTE` will compare the hours and minutes
        portions of the calendar.
Returns:
Zero if the first value is equal to the second, -1
         if it is less than the second or +1 if it is greater than the second.

  - 

### format

protected String format(Object value,
 Format formatter)

Format a value with the specified `DateFormat`.

Overrides:
`format` in class `AbstractFormatValidator`
Parameters:
`value` - The value to be formatted.
`formatter` - The Format to use.
Returns:
The formatted value.

  - 

### format

public String format(Object value,
 Locale locale,
 TimeZone timeZone)

Format an object into a `String` using
 the specified Locale.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use for the Format.
`timeZone` - The Time Zone used to format the date,
  system default if null unless value is a `Calendar`.
Returns:
The value formatted as a `String`.

  - 

### format

public String format(Object value,
 String pattern,
 Locale locale)

Format an object using the specified pattern and/or
    `Locale`.

Overrides:
`format` in class `AbstractFormatValidator`
Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to format the value.
`locale` - The locale to use for the Format.
Returns:
The value formatted as a `String`.

  - 

### format

public String format(Object value,
 String pattern,
 Locale locale,
 TimeZone timeZone)

Format an object using the specified pattern and/or
    `Locale`.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to format the value.
`locale` - The locale to use for the Format.
`timeZone` - The Time Zone used to format the date,
  system default if null unless value is a `Calendar`.
Returns:
The value formatted as a `String`.

  - 

### format

public String format(Object value,
 String pattern,
 TimeZone timeZone)

Format an object into a `String` using
 the specified pattern.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to format the value.
`timeZone` - The Time Zone used to format the date,
  system default if null unless value is a `Calendar`.
Returns:
The value formatted as a `String`.

  - 

### format

public String format(Object value,
 TimeZone timeZone)

Format an object into a `String` using
 the default Locale.

Parameters:
`value` - The value validation is being performed on.
`timeZone` - The Time Zone used to format the date,
  system default if null unless value is a `Calendar`.
Returns:
The value formatted as a `String`.

  - 

### getFormat

protected Format getFormat(Locale locale)

Returns a `DateFormat` for the specified Locale.

Parameters:
`locale` - The locale a `DateFormat` is required for,
        system default if null.
Returns:
The `DateFormat` to created.

  - 

### getFormat

protected Format getFormat(String pattern,
 Locale locale)

Returns a `DateFormat` for the specified *pattern*
    and/or `Locale`.

Specified by:
`getFormat` in class `AbstractFormatValidator`
Parameters:
`pattern` - The pattern used to validate the value against or
        `null` to use the default for the `Locale`.
`locale` - The locale to use for the currency format, system default if null.
Returns:
The `DateFormat` to created.

  - 

### isValid

public boolean isValid(String value,
 String pattern,
 Locale locale)

Validate using the specified `Locale`.

Specified by:
`isValid` in class `AbstractFormatValidator`
Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to format the value.
`locale` - The locale to use for the Format, defaults to the default
Returns:
`true` if the value is valid.

  - 

### parse

protected Object parse(String value,
 String pattern,
 Locale locale,
 TimeZone timeZone)

Checks if the value is valid against a specified pattern.

Parameters:
`value` - The value validation is being performed on.
`pattern` - The pattern used to validate the value against, or the
        default for the `Locale` if `null`.
`locale` - The locale to use for the date format, system default if null.
`timeZone` - The Time Zone used to parse the date, system default if null.
Returns:
The parsed value if valid or `null` if invalid.

  - 

### processParsedValue

protected abstract Object processParsedValue(Object value,
 Format formatter)

Process the parsed value, performing any further validation
    and type conversion required.

Specified by:
`processParsedValue` in class `AbstractFormatValidator`
Parameters:
`value` - The parsed object created.
`formatter` - The Format used to parse the value with.
Returns:
The parsed value converted to the appropriate type
         if valid or `null` if invalid.