Package org.apache.commons.validator.routines.checkdigit

# Class ISBNCheckDigit

java.lang.Object
org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit

All Implemented Interfaces:
`Serializable`, `CheckDigit`

---

public final class ISBNCheckDigit
extends Object
implements Serializable
Combined **ISBN-10** / **ISBN-13** Check Digit calculation/validation.
 

 This implementation validates/calculates ISBN check digits
 based on the length of the code passed to it - delegating
 either to the `ISBN10_CHECK_DIGIT` or the
 `ISBN13_CHECK_DIGIT` routines to perform the actual
 validation/calculation.
 

 **N.B.** From 1st January 2007 the book industry will start to use a new 13 digit
 ISBN number (rather than this 10 digit ISBN number) which uses the EAN-13 / UPC
 standard.

Since:
1.4
See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final CheckDigit`
`ISBN_CHECK_DIGIT`

Singleton combined ISBN-10 / ISBN-13 Check Digit instance

`static final CheckDigit`
`ISBN10_CHECK_DIGIT`

Singleton ISBN-10 Check Digit instance

`static final CheckDigit`
`ISBN13_CHECK_DIGIT`

Singleton ISBN-13 Check Digit instance

- 

## Constructor Summary

Constructors

Constructor
Description
`ISBNCheckDigit()`

Constructs a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`calculate(String code)`

Calculate an ISBN-10 or ISBN-13 check digit, depending
 on the length of the code.

`boolean`
`isValid(String code)`

Validate an ISBN-10 or ISBN-13 check digit, depending
 on the length of the code.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### ISBN10_CHECK_DIGIT

public static final CheckDigit ISBN10_CHECK_DIGIT
Singleton ISBN-10 Check Digit instance

  - 

### ISBN13_CHECK_DIGIT

public static final CheckDigit ISBN13_CHECK_DIGIT
Singleton ISBN-13 Check Digit instance

  - 

### ISBN_CHECK_DIGIT

public static final CheckDigit ISBN_CHECK_DIGIT
Singleton combined ISBN-10 / ISBN-13 Check Digit instance

- 

## Constructor Details

  - 

### ISBNCheckDigit

public ISBNCheckDigit()
Constructs a new instance.

- 

## Method Details

  - 

### calculate

public String calculate(String code)
                 throws CheckDigitException
Calculate an ISBN-10 or ISBN-13 check digit, depending
 on the length of the code.
 

 If the length of the code is 9, it is treated as an ISBN-10
 code or if the length of the code is 12, it is treated as an ISBN-13
 code.

Specified by:
`calculate` in interface `CheckDigit`
Parameters:
`code` - The ISBN code to validate (should have a length of
 9 or 12)
Returns:
The ISBN-10 check digit if the length is 9 or an ISBN-13
 check digit if the length is 12.
Throws:
`CheckDigitException` - if the code is missing, or an invalid
 length (that is, not 9 or 12) or if there is an error calculating the
 check digit.

  - 

### isValid

public boolean isValid(String code)

Validate an ISBN-10 or ISBN-13 check digit, depending
 on the length of the code.
 

 If the length of the code is 10, it is treated as an ISBN-10
 code or ff the length of the code is 13, it is treated as an ISBN-13
 code.

Specified by:
`isValid` in interface `CheckDigit`
Parameters:
`code` - The ISBN code to validate (should have a length of
 10 or 13)
Returns:
`true` if the code has a length of 10 and is
 a valid ISBN-10 check digit or the code has a length of 13 and is
 a valid ISBN-13 check digit - otherwise `false`.