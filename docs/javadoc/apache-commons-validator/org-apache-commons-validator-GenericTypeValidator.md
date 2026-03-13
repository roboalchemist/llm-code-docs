Package org.apache.commons.validator

# Class GenericTypeValidator

java.lang.Object
org.apache.commons.validator.GenericTypeValidator

All Implemented Interfaces:
`Serializable`

---

public class GenericTypeValidator
extends Object
implements Serializable
This class contains basic methods for performing validations that return the
 correctly typed class based on the validation performed.

See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`GenericTypeValidator()`

Deprecated.
Will be private in the next major version.

- 

## Method Summary

Modifier and Type
Method
Description
`static Byte`
`formatByte(String value)`

Checks if the value can safely be converted to a byte primitive.

`static Byte`
`formatByte(String value,
 Locale locale)`

Checks if the value can safely be converted to a byte primitive.

`static Long`
`formatCreditCard(String value)`

Checks if the field is a valid credit card number.

`static Date`
`formatDate(String value,
 String datePattern,
 boolean strict)`

Checks if the field is a valid date.

`static Date`
`formatDate(String value,
 Locale locale)`

Checks if the field is a valid date.

`static Double`
`formatDouble(String value)`

Checks if the value can safely be converted to a double primitive.

`static Double`
`formatDouble(String value,
 Locale locale)`

Checks if the value can safely be converted to a double primitive.

`static Float`
`formatFloat(String value)`

Checks if the value can safely be converted to a float primitive.

`static Float`
`formatFloat(String value,
 Locale locale)`

Checks if the value can safely be converted to a float primitive.

`static Integer`
`formatInt(String value)`

Checks if the value can safely be converted to an int primitive.

`static Integer`
`formatInt(String value,
 Locale locale)`

Checks if the value can safely be converted to an int primitive.

`static Long`
`formatLong(String value)`

Checks if the value can safely be converted to a long primitive.

`static Long`
`formatLong(String value,
 Locale locale)`

Checks if the value can safely be converted to a long primitive.

`static Short`
`formatShort(String value)`

Checks if the value can safely be converted to a short primitive.

`static Short`
`formatShort(String value,
 Locale locale)`

Checks if the value can safely be converted to a short primitive.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### GenericTypeValidator

@Deprecated
public GenericTypeValidator()
Deprecated.
Will be private in the next major version.

Constructs a new instance.

- 

## Method Details

  - 

### formatByte

public static Byte formatByte(String value)
Checks if the value can safely be converted to a byte primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
the converted Byte value.

  - 

### formatByte

public static Byte formatByte(String value,
 Locale locale)
Checks if the value can safely be converted to a byte primitive.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use to parse the number (system default if
               null)
Returns:
the converted Byte value.

  - 

### formatCreditCard

public static Long formatCreditCard(String value)
Checks if the field is a valid credit card number.

 

Reference Sean M. Burke's 
 script.

Parameters:
`value` - The value validation is being performed on.
Returns:
the converted Credit Card number.

  - 

### formatDate

public static Date formatDate(String value,
 Locale locale)
Checks if the field is a valid date.

 

The `Locale` is used with `DateFormat`. The `DateFormat.setLenient(boolean)`
 method is set to `false` for all.
 

Parameters:
`value` - The value validation is being performed on.
`locale` - The Locale to use to parse the date (system default if null)
Returns:
the converted Date value.

  - 

### formatDate

public static Date formatDate(String value,
 String datePattern,
 boolean strict)
Checks if the field is a valid date.

 

The pattern is used with `SimpleDateFormat`.
 If strict is true, then the length will be checked so '2/12/1999' will
 not pass validation with the format 'MM/dd/yyyy' because the month isn't
 two digits. The `DateFormat.setLenient(boolean)`
 method is set to `false` for all.
 

Parameters:
`value` - The value validation is being performed on.
`datePattern` - The pattern passed to `SimpleDateFormat`.
`strict` - Whether or not to have an exact match of the
                    datePattern.
Returns:
the converted Date value.

  - 

### formatDouble

public static Double formatDouble(String value)
Checks if the value can safely be converted to a double primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
the converted Double value.

  - 

### formatDouble

public static Double formatDouble(String value,
 Locale locale)
Checks if the value can safely be converted to a double primitive.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use to parse the number (system default if
               null)
Returns:
the converted Double value.

  - 

### formatFloat

public static Float formatFloat(String value)
Checks if the value can safely be converted to a float primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
the converted Float value.

  - 

### formatFloat

public static Float formatFloat(String value,
 Locale locale)
Checks if the value can safely be converted to a float primitive.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use to parse the number (system default if
               null)
Returns:
the converted Float value.

  - 

### formatInt

public static Integer formatInt(String value)
Checks if the value can safely be converted to an int primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
the converted Integer value.

  - 

### formatInt

public static Integer formatInt(String value,
 Locale locale)
Checks if the value can safely be converted to an int primitive.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use to parse the number (system default if
               null)
Returns:
the converted Integer value.

  - 

### formatLong

public static Long formatLong(String value)
Checks if the value can safely be converted to a long primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
the converted Long value.

  - 

### formatLong

public static Long formatLong(String value,
 Locale locale)
Checks if the value can safely be converted to a long primitive.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use to parse the number (system default if
               null)
Returns:
the converted Long value.

  - 

### formatShort

public static Short formatShort(String value)
Checks if the value can safely be converted to a short primitive.

Parameters:
`value` - The value validation is being performed on.
Returns:
the converted Short value.

  - 

### formatShort

public static Short formatShort(String value,
 Locale locale)
Checks if the value can safely be converted to a short primitive.

Parameters:
`value` - The value validation is being performed on.
`locale` - The locale to use to parse the number (system default if
               null)
Returns:
the converted Short value.