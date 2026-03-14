Package org.apache.commons.validator

# Class DateValidator

java.lang.Object
org.apache.commons.validator.DateValidator

---

@Deprecated
public class DateValidator
extends Object
Deprecated.
Use the new DateValidator, CalendarValidator or TimeValidator in the
 routines package. This class will be removed in a future release.

Perform date validations.
 

 This class is a Singleton; you can retrieve the instance via the
 getInstance() method.
 

Since:
1.1

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`DateValidator()`

Deprecated.
Protected constructor for subclasses to use.

- 

## Method Summary

Modifier and Type
Method
Description
`static DateValidator`
`getInstance()`

Deprecated.
Returns the Singleton instance of this validator.

`boolean`
`isValid(String value,
 String datePattern,
 boolean strict)`

Deprecated.
Checks if the field is a valid date.

`boolean`
`isValid(String value,
 Locale locale)`

Deprecated.
Checks if the field is a valid date.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### DateValidator

protected DateValidator()
Deprecated.
Protected constructor for subclasses to use.

- 

## Method Details

  - 

### getInstance

public static DateValidator getInstance()
Deprecated.
Returns the Singleton instance of this validator.

Returns:
A singleton instance of the DateValidator.

  - 

### isValid

public boolean isValid(String value,
 Locale locale)
Deprecated.

Checks if the field is a valid date.  The `Locale` is
 used with `DateFormat`.  The setLenient method
 is set to `false` for all.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use for the date format, defaults to the default
 system default if null.
Returns:
true if the date is valid.

  - 

### isValid

public boolean isValid(String value,
 String datePattern,
 boolean strict)
Deprecated.

Checks if the field is a valid date.  The pattern is used with
 `SimpleDateFormat`.  If strict is true, then the
 length will be checked so '2/12/1999' will not pass validation with
 the format 'MM/dd/yyyy' because the month isn't two digits.
 The setLenient method is set to `false` for all.

Parameters:
`value` - The value validation is being performed on.
`datePattern` - The pattern passed to `SimpleDateFormat`.
`strict` - Whether or not to have an exact match of the datePattern.
Returns:
true if the date is valid.