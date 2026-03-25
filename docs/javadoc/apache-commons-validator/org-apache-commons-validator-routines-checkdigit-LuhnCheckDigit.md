Package org.apache.commons.validator.routines.checkdigit

# Class LuhnCheckDigit

java.lang.Object
org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit
org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit

All Implemented Interfaces:
`Serializable`, `CheckDigit`

---

public final class LuhnCheckDigit
extends ModulusCheckDigit
Modulus 10 **Luhn** Check Digit calculation/validation.

 Luhn check digits are used, for example, by:
 

    
- Credit Card Numbers
    
- IMEI Numbers - International
        Mobile Equipment Identity Numbers
 

 Check digit calculation is based on *modulus 10* with digits in
 an *odd* position (from right to left) being weighted 1 and *even*
 position digits being weighted 2 (weighted values greater than 9 have 9 subtracted).

 

 See Wikipedia
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
`LUHN_CHECK_DIGIT`

Singleton Luhn Check Digit instance

- 

## Constructor Summary

Constructors

Constructor
Description
`LuhnCheckDigit()`

Constructs a modulus 10 Luhn Check Digit routine.

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

### LUHN_CHECK_DIGIT

public static final CheckDigit LUHN_CHECK_DIGIT
Singleton Luhn Check Digit instance

- 

## Constructor Details

  - 

### LuhnCheckDigit

public LuhnCheckDigit()
Constructs a modulus 10 Luhn Check Digit routine.

- 

## Method Details

  - 

### weightedValue

protected int weightedValue(int charValue,
 int leftPos,
 int rightPos)

Calculates the *weighted* value of a character in the
 code at a specified position.

 

For Luhn (from right to left) **odd** digits are weighted
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