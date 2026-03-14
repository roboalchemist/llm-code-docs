Package org.apache.commons.validator.routines.checkdigit

# Class SedolCheckDigit

java.lang.Object
org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit
org.apache.commons.validator.routines.checkdigit.SedolCheckDigit

All Implemented Interfaces:
`Serializable`, `CheckDigit`

---

public final class SedolCheckDigit
extends ModulusCheckDigit
Modulus 10 **SEDOL** (UK Securities) Check Digit calculation/validation.

 

 SEDOL Numbers are 7 character alphanumeric codes used
 to identify UK Securities (SEDOL stands for Stock Exchange Daily Official List).
 
 

 Check digit calculation is based on *modulus 10* with digits being weighted
 based on their position, from left to right, as follows:
 
 

```

      position:  1  2  3  4  5  6  7
     weighting:  1  3  1  7  3  9  1
 
```

 

 See Wikipedia - SEDOL
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
`SEDOL_CHECK_DIGIT`

Singleton SEDOL check digit instance

- 

## Constructor Summary

Constructors

Constructor
Description
`SedolCheckDigit()`

Constructs a modulus 10 Check Digit routine for ISBN-10.

- 

## Method Summary

Modifier and Type
Method
Description
`protected int`
`calculateModulus(String code,
 boolean includesCheckDigit)`

Calculate the modulus for an SEDOL code.

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

`calculate, getModulus, isValid, sumDigits, toCheckDigit`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### SEDOL_CHECK_DIGIT

public static final CheckDigit SEDOL_CHECK_DIGIT
Singleton SEDOL check digit instance

- 

## Constructor Details

  - 

### SedolCheckDigit

public SedolCheckDigit()
Constructs a modulus 10 Check Digit routine for ISBN-10.

- 

## Method Details

  - 

### calculateModulus

protected int calculateModulus(String code,
 boolean includesCheckDigit)
                        throws CheckDigitException
Calculate the modulus for an SEDOL code.

Overrides:
`calculateModulus` in class `ModulusCheckDigit`
Parameters:
`code` - The code to calculate the modulus for.
`includesCheckDigit` - Whether the code includes the Check Digit or not.
Returns:
The modulus value
Throws:
`CheckDigitException` - if an error occurs calculating the modulus
 for the specified code

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
`CheckDigitException` - if character is not alphanumeric

  - 

### weightedValue

protected int weightedValue(int charValue,
 int leftPos,
 int rightPos)
Calculates the *weighted* value of a character in the
 code at a specified position.

Specified by:
`weightedValue` in class `ModulusCheckDigit`
Parameters:
`charValue` - The numeric value of the character.
`leftPos` - The position of the character in the code, counting from left to right
`rightPos` - The position of the character in the code, counting from right to left
Returns:
The weighted value of the character.