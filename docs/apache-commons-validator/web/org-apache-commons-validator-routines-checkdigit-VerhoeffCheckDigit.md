Package org.apache.commons.validator.routines.checkdigit

# Class VerhoeffCheckDigit

java.lang.Object
org.apache.commons.validator.routines.checkdigit.VerhoeffCheckDigit

All Implemented Interfaces:
`Serializable`, `CheckDigit`

---

public final class VerhoeffCheckDigit
extends Object
implements Serializable
**Verhoeff** (Dihedral) Check Digit calculation/validation.
 

 Check digit calculation for numeric codes using a
 Dihedral Group
 of order 10.
 

 See Wikipedia
  - Verhoeff algorithm for more details.

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
`VERHOEFF_CHECK_DIGIT`

Singleton Verhoeff Check Digit instance

- 

## Constructor Summary

Constructors

Constructor
Description
`VerhoeffCheckDigit()`

Constructs a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`calculate(String code)`

Calculate a Verhoeff *Check Digit* for a code.

`boolean`
`isValid(String code)`

Validate the Verhoeff *Check Digit* for a code.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### VERHOEFF_CHECK_DIGIT

public static final CheckDigit VERHOEFF_CHECK_DIGIT
Singleton Verhoeff Check Digit instance

- 

## Constructor Details

  - 

### VerhoeffCheckDigit

public VerhoeffCheckDigit()
Constructs a new instance.

- 

## Method Details

  - 

### calculate

public String calculate(String code)
                 throws CheckDigitException
Calculate a Verhoeff *Check Digit* for a code.

Specified by:
`calculate` in interface `CheckDigit`
Parameters:
`code` - The code to calculate the Check Digit for
Returns:
The calculated Check Digit
Throws:
`CheckDigitException` - if an error occurs calculating
 the check digit for the specified code

  - 

### isValid

public boolean isValid(String code)
Validate the Verhoeff *Check Digit* for a code.

Specified by:
`isValid` in interface `CheckDigit`
Parameters:
`code` - The code to validate
Returns:
`true` if the check digit is valid,
 otherwise `false`