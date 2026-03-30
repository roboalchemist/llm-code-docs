Package org.apache.commons.validator

# Class GenericValidator

java.lang.Object
org.apache.commons.validator.GenericValidator

All Implemented Interfaces:
`Serializable`

---

public class GenericValidator
extends Object
implements Serializable
This class contains basic methods for performing validations.

See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`GenericValidator()`

Deprecated.
Will be private in the next major version.

- 

## Method Summary

Modifier and Type
Method
Description
`static boolean`
`isBlankOrNull(String value)`

Checks if the field isn't null and length of the field is greater
 than zero not including whitespace.

`static boolean`
`isByte(String value)`

Checks if the value can safely be converted to a byte primitive.

`static boolean`
`isCreditCard(String value)`

Checks if the field is a valid credit card number.

`static boolean`
`isDate(String value,
 String datePattern,
 boolean strict)`

Checks if the field is a valid date.

`static boolean`
`isDate(String value,
 Locale locale)`

Checks if the field is a valid date.

`static boolean`
`isDouble(String value)`

Checks if the value can safely be converted to a double primitive.

`static boolean`
`isEmail(String value)`

Checks if a field has a valid e-mail address.

`static boolean`
`isFloat(String value)`

Checks if the value can safely be converted to a float primitive.

`static boolean`
`isInRange(byte value,
 byte min,
 byte max)`

Checks if a value is within a range (min & max specified
 in the vars attribute).

`static boolean`
`isInRange(double value,
 double min,
 double max)`

Checks if a value is within a range (min & max specified
 in the vars attribute).

`static boolean`
`isInRange(float value,
 float min,
 float max)`

Checks if a value is within a range (min & max specified
 in the vars attribute).

`static boolean`
`isInRange(int value,
 int min,
 int max)`

Checks if a value is within a range (min & max specified
 in the vars attribute).

`static boolean`
`isInRange(long value,
 long min,
 long max)`

Checks if a value is within a range (min & max specified
 in the vars attribute).

`static boolean`
`isInRange(short value,
 short min,
 short max)`

Checks if a value is within a range (min & max specified
 in the vars attribute).

`static boolean`
`isInt(String value)`

Checks if the value can safely be converted to an int primitive.

`static boolean`
`isLong(String value)`

Checks if the value can safely be converted to a long primitive.

`static boolean`
`isShort(String value)`

Checks if the value can safely be converted to a short primitive.

`static boolean`
`isUrl(String value)`

Checks if a field is a valid URL address.

`static boolean`
`matchRegexp(String value,
 String regexp)`

Checks if the value matches the regular expression.

`static boolean`
`maxLength(String value,
 int max)`

Checks if the value's length is less than or equal to the max.

`static boolean`
`maxLength(String value,
 int max,
 int lineEndLength)`

Checks if the value's adjusted length is less than or equal to the max.

`static boolean`
`maxValue(double value,
 double max)`

Checks if the value is less than or equal to the max.

`static boolean`
`maxValue(float value,
 float max)`

Checks if the value is less than or equal to the max.

`static boolean`
`maxValue(int value,
 int max)`

Checks if the value is less than or equal to the max.

`static boolean`
`maxValue(long value,
 long max)`

Checks if the value is less than or equal to the max.

`static boolean`
`minLength(String value,
 int min)`

Checks if the value's length is greater than or equal to the min.

`static boolean`
`minLength(String value,
 int min,
 int lineEndLength)`

Checks if the value's adjusted length is greater than or equal to the min.

`static boolean`
`minValue(double value,
 double min)`

Checks if the value is greater than or equal to the min.

`static boolean`
`minValue(float value,
 float min)`

Checks if the value is greater than or equal to the min.

`static boolean`
`minValue(int value,
 int min)`

Checks if the value is greater than or equal to the min.

`static boolean`
`minValue(long value,
 long min)`

Checks if the value is greater than or equal to the min.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### GenericValidator

@Deprecated
public GenericValidator()
Deprecated.
Will be private in the next major version.

Constructs a new instance.

- 

## Method Details

  - 

### isBlankOrNull

public static boolean isBlankOrNull(String value)

Checks if the field isn't null and length of the field is greater
 than zero not including whitespace.

Parameters:
`value` - The value validation is being performed on.
Returns:
true if blank or null.

  - 

### isByte

public static boolean isByte(String value)

Checks if the value can safely be converted to a byte primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
true if the value can be converted to a Byte.

  - 

### isCreditCard

public static boolean isCreditCard(String value)
Checks if the field is a valid credit card number.

Parameters:
`value` - The value validation is being performed on.
Returns:
true if the value is valid Credit Card Number.

  - 

### isDate

public static boolean isDate(String value,
 Locale locale)

Checks if the field is a valid date.  The `Locale` is
 used with `DateFormat`.  The setLenient method
 is set to `false` for all.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use for the date format, defaults to the
 system default if null.
Returns:
true if the value can be converted to a Date.

  - 

### isDate

public static boolean isDate(String value,
 String datePattern,
 boolean strict)

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
true if the value can be converted to a Date.

  - 

### isDouble

public static boolean isDouble(String value)

Checks if the value can safely be converted to a double primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
true if the value can be converted to a Double.

  - 

### isEmail

public static boolean isEmail(String value)

Checks if a field has a valid e-mail address.

Parameters:
`value` - The value validation is being performed on.
Returns:
true if the value is valid Email Address.

  - 

### isFloat

public static boolean isFloat(String value)

Checks if the value can safely be converted to a float primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
true if the value can be converted to a Float.

  - 

### isInRange

public static boolean isInRange(byte value,
 byte min,
 byte max)

Checks if a value is within a range (min & max specified
 in the vars attribute).

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum value of the range.
`max` - The maximum value of the range.
Returns:
true if the value is in the specified range.

  - 

### isInRange

public static boolean isInRange(double value,
 double min,
 double max)

Checks if a value is within a range (min & max specified
 in the vars attribute).

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum value of the range.
`max` - The maximum value of the range.
Returns:
true if the value is in the specified range.

  - 

### isInRange

public static boolean isInRange(float value,
 float min,
 float max)

Checks if a value is within a range (min & max specified
 in the vars attribute).

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum value of the range.
`max` - The maximum value of the range.
Returns:
true if the value is in the specified range.

  - 

### isInRange

public static boolean isInRange(int value,
 int min,
 int max)

Checks if a value is within a range (min & max specified
 in the vars attribute).

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum value of the range.
`max` - The maximum value of the range.
Returns:
true if the value is in the specified range.

  - 

### isInRange

public static boolean isInRange(long value,
 long min,
 long max)

Checks if a value is within a range (min & max specified
 in the vars attribute).

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum value of the range.
`max` - The maximum value of the range.
Returns:
true if the value is in the specified range.

  - 

### isInRange

public static boolean isInRange(short value,
 short min,
 short max)

Checks if a value is within a range (min & max specified
 in the vars attribute).

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum value of the range.
`max` - The maximum value of the range.
Returns:
true if the value is in the specified range.

  - 

### isInt

public static boolean isInt(String value)

Checks if the value can safely be converted to an int primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
true if the value can be converted to an Integer.

  - 

### isLong

public static boolean isLong(String value)

Checks if the value can safely be converted to a long primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
true if the value can be converted to a Long.

  - 

### isShort

public static boolean isShort(String value)

Checks if the value can safely be converted to a short primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
true if the value can be converted to a Short.

  - 

### isUrl

public static boolean isUrl(String value)

Checks if a field is a valid URL address.
 If you need to modify what is considered valid then
 consider using the UrlValidator directly.

Parameters:
`value` - The value validation is being performed on.
Returns:
true if the value is valid Url.

  - 

### matchRegexp

public static boolean matchRegexp(String value,
 String regexp)

Checks if the value matches the regular expression.

Parameters:
`value` - The value validation is being performed on.
`regexp` - The regular expression.
Returns:
true if matches the regular expression.

  - 

### maxLength

public static boolean maxLength(String value,
 int max)

Checks if the value's length is less than or equal to the max.

Parameters:
`value` - The value validation is being performed on.
`max` - The maximum length.
Returns:
true if the value's length is less than the specified maximum.

  - 

### maxLength

public static boolean maxLength(String value,
 int max,
 int lineEndLength)

Checks if the value's adjusted length is less than or equal to the max.

Parameters:
`value` - The value validation is being performed on.
`max` - The maximum length.
`lineEndLength` - The length to use for line endings.
Returns:
true if the value's length is less than the specified maximum.

  - 

### maxValue

public static boolean maxValue(double value,
 double max)

Checks if the value is less than or equal to the max.

Parameters:
`value` - The value validation is being performed on.
`max` - The maximum numeric value.
Returns:
true if the value is <= the specified maximum.

  - 

### maxValue

public static boolean maxValue(float value,
 float max)

Checks if the value is less than or equal to the max.

Parameters:
`value` - The value validation is being performed on.
`max` - The maximum numeric value.
Returns:
true if the value is <= the specified maximum.

  - 

### maxValue

public static boolean maxValue(int value,
 int max)

Checks if the value is less than or equal to the max.

Parameters:
`value` - The value validation is being performed on.
`max` - The maximum numeric value.
Returns:
true if the value is <= the specified maximum.

  - 

### maxValue

public static boolean maxValue(long value,
 long max)

Checks if the value is less than or equal to the max.

Parameters:
`value` - The value validation is being performed on.
`max` - The maximum numeric value.
Returns:
true if the value is <= the specified maximum.

  - 

### minLength

public static boolean minLength(String value,
 int min)

Checks if the value's length is greater than or equal to the min.

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum length.
Returns:
true if the value's length is more than the specified minimum.

  - 

### minLength

public static boolean minLength(String value,
 int min,
 int lineEndLength)

Checks if the value's adjusted length is greater than or equal to the min.

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum length.
`lineEndLength` - The length to use for line endings.
Returns:
true if the value's length is more than the specified minimum.

  - 

### minValue

public static boolean minValue(double value,
 double min)

Checks if the value is greater than or equal to the min.

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum numeric value.
Returns:
true if the value is >= the specified minimum.

  - 

### minValue

public static boolean minValue(float value,
 float min)

Checks if the value is greater than or equal to the min.

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum numeric value.
Returns:
true if the value is >= the specified minimum.

  - 

### minValue

public static boolean minValue(int value,
 int min)

Checks if the value is greater than or equal to the min.

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum numeric value.
Returns:
true if the value is >= the specified minimum.

  - 

### minValue

public static boolean minValue(long value,
 long min)

Checks if the value is greater than or equal to the min.

Parameters:
`value` - The value validation is being performed on.
`min` - The minimum numeric value.
Returns:
true if the value is >= the specified minimum.