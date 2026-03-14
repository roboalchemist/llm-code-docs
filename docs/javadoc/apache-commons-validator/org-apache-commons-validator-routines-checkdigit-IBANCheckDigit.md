Package org.apache.commons.validator.routines.checkdigit

# Class IBANCheckDigit

java.lang.Object
org.apache.commons.validator.routines.checkdigit.IBANCheckDigit

All Implemented Interfaces:
`Serializable`, `CheckDigit`

---

public final class IBANCheckDigit
extends Object
implements Serializable
**IBAN** (International Bank Account Number) Check Digit calculation/validation.
 

 This routine is based on the ISO 7064 Mod 97,10 check digit calculation routine.
 

 The two check digit characters in a IBAN number are the third and fourth characters
 in the code. For *check digit* calculation/validation the first four characters are moved
 to the end of the code.
  So `CCDDnnnnnnn` becomes `nnnnnnnCCDD` (where
  `CC` is the country code and `DD` is the check digit). For
  check digit calculation the check digit value should be set to zero (such as
  `CC00nnnnnnn` in this example).
 

 Note: the class does not check the format of the IBAN number, only the check digits.
 

 For further information see
  Wikipedia -
  IBAN number.

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
`IBAN_CHECK_DIGIT`

Singleton IBAN Number Check Digit instance

- 

## Constructor Summary

Constructors

Constructor
Description
`IBANCheckDigit()`

Constructs Check Digit routine for IBAN Numbers.

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`calculate(String code)`

Calculate the *Check Digit* for an IBAN code.

`boolean`
`isValid(String code)`

Validate the check digit of an IBAN code.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### IBAN_CHECK_DIGIT

public static final CheckDigit IBAN_CHECK_DIGIT
Singleton IBAN Number Check Digit instance

- 

## Constructor Details

  - 

### IBANCheckDigit

public IBANCheckDigit()
Constructs Check Digit routine for IBAN Numbers.

- 

## Method Details

  - 

### calculate

public String calculate(String code)
                 throws CheckDigitException
Calculate the *Check Digit* for an IBAN code.
 

 **Note:** The check digit is the third and fourth
 characters and is set to the value "`00`".

Specified by:
`calculate` in interface `CheckDigit`
Parameters:
`code` - The code to calculate the Check Digit for
Returns:
The calculated Check Digit as 2 numeric decimal characters, for example, "42"
Throws:
`CheckDigitException` - if an error occurs calculating
 the check digit for the specified code

  - 

### isValid

public boolean isValid(String code)
Validate the check digit of an IBAN code.

Specified by:
`isValid` in interface `CheckDigit`
Parameters:
`code` - The code to validate
Returns:
`true` if the check digit is valid, otherwise
 `false`