Package org.apache.commons.validator.routines.checkdigit

# Class ISINCheckDigit

java.lang.Object
org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit
org.apache.commons.validator.routines.checkdigit.ISINCheckDigit

All Implemented Interfaces:
`Serializable`, `CheckDigit`

---

public final class ISINCheckDigit
extends ModulusCheckDigit
Modulus 10 **ISIN** (International Securities Identifying Number) Check Digit calculation/validation.

 

 ISIN Numbers are 12 character alphanumeric codes used
 to identify Securities.
 

 

 Check digit calculation uses the *Modulus 10 Double Add Double* technique
 with every second digit being weighted by 2. Alphabetic characters are
 converted to numbers by their position in the alphabet starting with A being 10.
 Weighted numbers greater than ten are treated as two separate numbers.
 

 

 See Wikipedia - ISIN
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
`ISIN_CHECK_DIGIT`

Singleton ISIN Check Digit instance

- 

## Constructor Summary

Constructors

Constructor
Description
`ISINCheckDigit()`

Constructs an ISIN Identifier Check Digit routine.

- 

## Method Summary

Modifier and Type
Method
Description
`protected int`
`calculateModulus(String code,
 boolean includesCheckDigit)`

Calculate the modulus for an ISIN code.

`protected int`
`weightedValue(int charValue,
 int leftPos,
 int rightPos)`

Calculates the *weighted* value of a character in the
 code at a specified position.

### Methods inherited from class org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit

`calculate, getModulus, isValid, sumDigits, toCheckDigit, toInt`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### ISIN_CHECK_DIGIT

public static final CheckDigit ISIN_CHECK_DIGIT
Singleton ISIN Check Digit instance

- 

## Constructor Details

  - 

### ISINCheckDigit

public ISINCheckDigit()
Constructs an ISIN Identifier Check Digit routine.

- 

## Method Details

  - 

### calculateModulus

protected int calculateModulus(String code,
 boolean includesCheckDigit)
                        throws CheckDigitException
Calculate the modulus for an ISIN code.

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

### weightedValue

protected int weightedValue(int charValue,
 int leftPos,
 int rightPos)

Calculates the *weighted* value of a character in the
 code at a specified position.

 

For ISIN (from right to left) **odd** digits are weighted
 with a factor of **one** and **even** digits with a factor
 of **two**. Weighted values are reduced to their digital root

Specified by:
`weightedValue` in class `ModulusCheckDigit`
Parameters:
`charValue` - The numeric value of the character.
`leftPos` - The position of the character in the code, counting from left to right
`rightPos` - The position of the character in the code, counting from right to left
Returns:
The weighted value of the character.