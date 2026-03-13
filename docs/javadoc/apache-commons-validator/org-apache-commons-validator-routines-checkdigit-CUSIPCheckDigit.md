Package org.apache.commons.validator.routines.checkdigit

# Class CUSIPCheckDigit

java.lang.Object
org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit
org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit

All Implemented Interfaces:
`Serializable`, `CheckDigit`

---

public final class CUSIPCheckDigit
extends ModulusCheckDigit
Modulus 10 **CUSIP** (North American Securities) Check Digit calculation/validation.

 

 CUSIP Numbers are 9 character alphanumeric codes used
 to identify North American Securities.
 

 

 Check digit calculation uses the *Modulus 10 Double Add Double* technique
 with every second digit being weighted by 2. Alphabetic characters are
 converted to numbers by their position in the alphabet starting with A being 10.
 Weighted numbers greater than ten are treated as two separate numbers.
 

 

 See Wikipedia - CUSIP
 for more details.
 

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
`CUSIP_CHECK_DIGIT`

Singleton CUSIP Check Digit instance

- 

## Constructor Summary

Constructors

Constructor
Description
`CUSIPCheckDigit()`

Constructs a CUSIP Identifier Check Digit routine.

- 

## Method Summary

Modifier and Type
Method
Description
`protected int`
`toInt(char character,
 int leftPos,
 int rightPos)`

Convert a character at a specified position to an integer value.

`protected int`
`weightedValue(int charValue,
 int leftPos,
 int rightPos)`

Calculates the *weighted* value of a character in the
 code at a specified position.

### Methods inherited from class org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit

`calculate, calculateModulus, getModulus, isValid, sumDigits, toCheckDigit`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### CUSIP_CHECK_DIGIT

public static final CheckDigit CUSIP_CHECK_DIGIT
Singleton CUSIP Check Digit instance

- 

## Constructor Details

  - 

### CUSIPCheckDigit

public CUSIPCheckDigit()
Constructs a CUSIP Identifier Check Digit routine.

- 

## Method Details

  - 

### toInt

protected int toInt(char character,
 int leftPos,
 int rightPos)
             throws CheckDigitException
Convert a character at a specified position to an integer value.

Overrides:
`toInt` in class `ModulusCheckDigit`
Parameters:
`character` - The character to convert
`leftPos` - The position of the character in the code, counting from left to right
`rightPos` - The position of the character in the code, counting from right to left
Returns:
The integer value of the character
Throws:
`CheckDigitException` - if the character is not alphanumeric

  - 

### weightedValue

protected int weightedValue(int charValue,
 int leftPos,
 int rightPos)

Calculates the *weighted* value of a character in the
 code at a specified position.

 

For CUSIP (from right to left) **odd** digits are weighted
 with a factor of **one** and **even** digits with a factor
 of **two**. Weighted values > 9, have 9 subtracted

Specified by:
`weightedValue` in class `ModulusCheckDigit`
Parameters:
`charValue` - The numeric value of the character.
`leftPos` - The position of the character in the code, counting from left to right
`rightPos` - The position of the character in the code, counting from right to left
Returns:
The weighted value of the character.