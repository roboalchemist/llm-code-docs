Package org.apache.commons.validator.routines.checkdigit

# Class EAN13CheckDigit

java.lang.Object
org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit
org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit

All Implemented Interfaces:
`Serializable`, `CheckDigit`

---

public final class EAN13CheckDigit
extends ModulusCheckDigit
Modulus 10 **EAN-13** / **UPC** / **ISBN-13** Check Digit
 calculation/validation.
 

 Check digit calculation is based on *modulus 10* with digits in
 an *odd* position (from right to left) being weighted 1 and *even*
 position digits being weighted 3.
 

 For further information see:
 

   
- EAN-13 - see
       Wikipedia -
       European Article Number.
   
- UPC - see
       Wikipedia -
       Universal Product Code.
   
- ISBN-13 - see
       Wikipedia - International
       Standard Book Number (ISBN).
 

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
`EAN13_CHECK_DIGIT`

Singleton EAN-13 Check Digit instance

- 

## Constructor Summary

Constructors

Constructor
Description
`EAN13CheckDigit()`

Constructs a modulus 10 Check Digit routine for EAN/UPC.

- 

## Method Summary

Modifier and Type
Method
Description
`protected int`
`weightedValue(int charValue,
 int leftPos,
 int rightPos)`

Calculates the *weighted* value of a character in the
 code at a specified position.

### Methods inherited from class org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit

`calculate, calculateModulus, getModulus, isValid, sumDigits, toCheckDigit, toInt`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### EAN13_CHECK_DIGIT

public static final CheckDigit EAN13_CHECK_DIGIT
Singleton EAN-13 Check Digit instance

- 

## Constructor Details

  - 

### EAN13CheckDigit

public EAN13CheckDigit()
Constructs a modulus 10 Check Digit routine for EAN/UPC.

- 

## Method Details

  - 

### weightedValue

protected int weightedValue(int charValue,
 int leftPos,
 int rightPos)

Calculates the *weighted* value of a character in the
 code at a specified position.

 

For EAN-13 (from right to left) **odd** digits are weighted
 with a factor of **one** and **even** digits with a factor
 of **three**.

Specified by:
`weightedValue` in class `ModulusCheckDigit`
Parameters:
`charValue` - The numeric value of the character.
`leftPos` - The position of the character in the code, counting from left to right
`rightPos` - The position of the character in the code, counting from right to left
Returns:
The weighted value of the character.