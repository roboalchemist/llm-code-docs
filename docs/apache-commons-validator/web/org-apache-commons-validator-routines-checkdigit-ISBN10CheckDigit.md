Package org.apache.commons.validator.routines.checkdigit

# Class ISBN10CheckDigit

java.lang.Object
org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit
org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit

All Implemented Interfaces:
`Serializable`, `CheckDigit`

---

public final class ISBN10CheckDigit
extends ModulusCheckDigit
Modulus 11 **ISBN-10** Check Digit calculation/validation.
 

 ISBN-10 Numbers are a numeric code except for the last (check) digit
 which can have a value of "X".
 

 Check digit calculation is based on *modulus 11* with digits being weighted
 based by their position, from right to left  with the first digit being weighted
 1, the second 2 and so on. If the check digit is calculated as "10" it is converted
 to "X".
 

 **N.B.** From 1st January 2007 the book industry will start to use a new 13 digit
 ISBN number (rather than this 10 digit ISBN number) which uses the EAN-13 / UPC
 (see `EAN13CheckDigit`) standard.
 

 For further information see:
 

   
- Wikipedia - International
       Standard Book Number (ISBN).
   
- ISBN-13
       Transition details.
 

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
`ISBN10_CHECK_DIGIT`

Singleton ISBN-10 Check Digit instance

- 

## Constructor Summary

Constructors

Constructor
Description
`ISBN10CheckDigit()`

Constructs a modulus 11 Check Digit routine for ISBN-10.

- 

## Method Summary

Modifier and Type
Method
Description
`protected String`
`toCheckDigit(int charValue)`

Convert an integer value to a character at a specified position.

`protected int`
`toInt(char character,
 int leftPos,
 int rightPos)`

Convert a character at a specified position to an
 integer value.

`protected int`
`weightedValue(int charValue,
 int leftPos,
 int rightPos)`

Calculates the *weighted* value of a character in the
 code at a specified position.

### Methods inherited from class org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit

`calculate, calculateModulus, getModulus, isValid, sumDigits`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### ISBN10_CHECK_DIGIT

public static final CheckDigit ISBN10_CHECK_DIGIT
Singleton ISBN-10 Check Digit instance

- 

## Constructor Details

  - 

### ISBN10CheckDigit

public ISBN10CheckDigit()
Constructs a modulus 11 Check Digit routine for ISBN-10.

- 

## Method Details

  - 

### toCheckDigit

protected String toCheckDigit(int charValue)
                       throws CheckDigitException

Convert an integer value to a character at a specified position.

 

Value '10' for position 1 (check digit) converted to 'X'.

Overrides:
`toCheckDigit` in class `ModulusCheckDigit`
Parameters:
`charValue` - The integer value of the character.
Returns:
The converted character.
Throws:
`CheckDigitException` - if an error occurs.

  - 

### toInt

protected int toInt(char character,
 int leftPos,
 int rightPos)
             throws CheckDigitException

Convert a character at a specified position to an
 integer value.

 

Character 'X' check digit converted to 10.

Overrides:
`toInt` in class `ModulusCheckDigit`
Parameters:
`character` - The character to convert.
`leftPos` - The position of the character in the code, counting from left to right
`rightPos` - The position of the character in the code, counting from right to left
Returns:
The integer value of the character.
Throws:
`CheckDigitException` - if an error occurs.

  - 

### weightedValue

protected int weightedValue(int charValue,
 int leftPos,
 int rightPos)
Calculates the *weighted* value of a character in the
 code at a specified position.

 

For ISBN-10 (from right to left) digits are weighted
 by their position.

Specified by:
`weightedValue` in class `ModulusCheckDigit`
Parameters:
`charValue` - The numeric value of the character.
`leftPos` - The position of the character in the code, counting from left to right
`rightPos` - The position of the character in the code, counting from right to left
Returns:
The weighted value of the character.