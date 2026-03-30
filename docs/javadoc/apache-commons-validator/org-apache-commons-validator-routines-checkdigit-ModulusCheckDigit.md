Package org.apache.commons.validator.routines.checkdigit

# Class ModulusCheckDigit

java.lang.Object
org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit

All Implemented Interfaces:
`Serializable`, `CheckDigit`

Direct Known Subclasses:
`ABANumberCheckDigit`, `CASNumberCheckDigit`, `CUSIPCheckDigit`, `EAN13CheckDigit`, `ECNumberCheckDigit`, `ISBN10CheckDigit`, `ISINCheckDigit`, `ISSNCheckDigit`, `LuhnCheckDigit`, `ModulusTenCheckDigit`, `SedolCheckDigit`

---

public abstract class ModulusCheckDigit
extends Object
implements Serializable
Abstract **Modulus** Check digit calculation/validation.
 

 Provides a *base* class for building *modulus* Check Digit routines.
 
 

 This implementation only handles *single-digit numeric* codes, such as **EAN-13**. For *alphanumeric* codes such as **EAN-128** you will need
 to implement/override the `toInt()` and `toChar()` methods.
 

Since:
1.4
See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`ModulusCheckDigit(int modulus)`

Constructs a `CheckDigit` routine for a specified modulus.

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`calculate(String code)`

Calculate a modulus *Check Digit* for a code which does not yet have one.

`protected int`
`calculateModulus(String code,
 boolean includesCheckDigit)`

Calculate the modulus for a code.

`int`
`getModulus()`

Gets the modulus value this check digit routine is based on.

`boolean`
`isValid(String code)`

Validate a modulus check digit for a code.

`static int`
`sumDigits(int number)`

Add together the individual digits in a number.

`protected String`
`toCheckDigit(int charValue)`

Convert an integer value to a check digit.

`protected int`
`toInt(char character,
 int leftPos,
 int rightPos)`

Convert a character at a specified position to an integer value.

`protected abstract int`
`weightedValue(int charValue,
 int leftPos,
 int rightPos)`

Calculates the *weighted* value of a character in the
 code at a specified position.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### ModulusCheckDigit

public ModulusCheckDigit(int modulus)
Constructs a `CheckDigit` routine for a specified modulus.

Parameters:
`modulus` - The modulus value to use for the check digit calculation

- 

## Method Details

  - 

### sumDigits

public static int sumDigits(int number)
Add together the individual digits in a number.

Parameters:
`number` - The number whose digits are to be added
Returns:
The sum of the digits

  - 

### calculate

public String calculate(String code)
                 throws CheckDigitException
Calculate a modulus *Check Digit* for a code which does not yet have one.

Specified by:
`calculate` in interface `CheckDigit`
Parameters:
`code` - The code for which to calculate the Check Digit;
 the check digit should not be included
Returns:
The calculated Check Digit
Throws:
`CheckDigitException` - if an error occurs calculating the check digit

  - 

### calculateModulus

protected int calculateModulus(String code,
 boolean includesCheckDigit)
                        throws CheckDigitException
Calculate the modulus for a code.

Parameters:
`code` - The code to calculate the modulus for.
`includesCheckDigit` - Whether the code includes the Check Digit or not.
Returns:
The modulus value
Throws:
`CheckDigitException` - if an error occurs calculating the modulus
 for the specified code

  - 

### getModulus

public int getModulus()
Gets the modulus value this check digit routine is based on.

Returns:
The modulus value this check digit routine is based on

  - 

### isValid

public boolean isValid(String code)
Validate a modulus check digit for a code.

Specified by:
`isValid` in interface `CheckDigit`
Parameters:
`code` - The code to validate
Returns:
`true` if the check digit is valid, otherwise
 `false`

  - 

### toCheckDigit

protected String toCheckDigit(int charValue)
                       throws CheckDigitException
Convert an integer value to a check digit.
 

 **Note:** this implementation only handles single-digit numeric values
 For non-numeric characters, override this method to provide
 integer-->character conversion.

Parameters:
`charValue` - The integer value of the character
Returns:
The converted character
Throws:
`CheckDigitException` - if integer character value
 doesn't represent a numeric character

  - 

### toInt

protected int toInt(char character,
 int leftPos,
 int rightPos)
             throws CheckDigitException
Convert a character at a specified position to an integer value.
 

 **Note:** this implementation only handlers numeric values
 For non-numeric characters, override this method to provide
 character-->integer conversion.

Parameters:
`character` - The character to convert
`leftPos` - The position of the character in the code, counting from left to right (for identifiying the position in the string)
`rightPos` - The position of the character in the code, counting from right to left (not used here)
Returns:
The integer value of the character
Throws:
`CheckDigitException` - if character is non-numeric

  - 

### weightedValue

protected abstract int weightedValue(int charValue,
 int leftPos,
 int rightPos)
                              throws CheckDigitException
Calculates the *weighted* value of a character in the
 code at a specified position.
 

 Some modulus routines weight the value of a character
 depending on its position in the code (for example, ISBN-10), while
 others use different weighting factors for odd/even positions
 (for example, EAN or Luhn). Implement the appropriate mechanism
 required by overriding this method.

Parameters:
`charValue` - The numeric value of the character
`leftPos` - The position of the character in the code, counting from left to right
`rightPos` - The position of the character in the code, counting from right to left
Returns:
The weighted value of the character
Throws:
`CheckDigitException` - if an error occurs calculating
 the weighted value