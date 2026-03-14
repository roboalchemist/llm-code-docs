Package org.apache.commons.validator.routines

# Class ISBNValidator

java.lang.Object
org.apache.commons.validator.routines.ISBNValidator

All Implemented Interfaces:
`Serializable`

---

public class ISBNValidator
extends Object
implements Serializable
**ISBN-10** and **ISBN-13** Code Validation.
 

 This validator validates the code is either a valid ISBN-10
 (using a `CodeValidator` with the `ISBN10CheckDigit`)
 or a valid ISBN-13 code (using a `CodeValidator` with
 the `EAN13CheckDigit` routine).
 

 The `validate()` methods return the ISBN code with formatting
 characters removed if valid or `null` if invalid.
 

 This validator also provides the facility to convert ISBN-10 codes to
 ISBN-13 if the `convert` property is `true`.
 

 From 1st January 2007 the book industry will start to use a new 13 digit
 ISBN number (rather than this 10 digit ISBN number). ISBN-13 codes are
 EAN
 codes, for more information see:

 

   
- Wikipedia - International
       Standard Book Number (ISBN).
   
- EAN - see
       Wikipedia -
       European Article Number.
   
- ISBN-13
       Transition details.
 

 

ISBN-13s are either prefixed with 978 or 979. 978 prefixes are only assigned
 to the ISBN agency. 979 prefixes may be assigned to ISBNs or ISMNs
 (International
 Standard Music Numbers).
 

     
- 979-0 are assigned to the ISMN agency
     
- 979-10, 979-11, 979-12 are assigned to the ISBN agency
 

 All other 979 prefixed EAN-13 numbers have not yet been assigned to an agency. The
 validator validates all 13-digit codes with 978 or 979 prefixes.

Since:
1.4
See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`ISBNValidator()`

Constructs an ISBN validator which converts ISBN-10 codes
 to ISBN-13.

`ISBNValidator(boolean convert)`

Constructs an ISBN validator indicating whether
 ISBN-10 codes should be converted to ISBN-13.

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`convertToISBN13(String isbn10)`

Convert an ISBN-10 code to an ISBN-13 code.

`static ISBNValidator`
`getInstance()`

Gets the singleton instance of the ISBN validator which
 converts ISBN-10 codes to ISBN-13.

`static ISBNValidator`
`getInstance(boolean convert)`

Gets the singleton instance of the ISBN validator specifying
 whether ISBN-10 codes should be converted to ISBN-13.

`boolean`
`isValid(String code)`

Check the code is either a valid ISBN-10 or ISBN-13 code.

`boolean`
`isValidISBN10(String code)`

Check the code is a valid ISBN-10 code.

`boolean`
`isValidISBN13(String code)`

Check the code is a valid ISBN-13 code.

`String`
`validate(String code)`

Check the code is either a valid ISBN-10 or ISBN-13 code.

`String`
`validateISBN10(String code)`

Check the code is a valid ISBN-10 code.

`String`
`validateISBN13(String code)`

Check the code is a valid ISBN-13 code.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### ISBNValidator

public ISBNValidator()
Constructs an ISBN validator which converts ISBN-10 codes
 to ISBN-13.

  - 

### ISBNValidator

public ISBNValidator(boolean convert)
Constructs an ISBN validator indicating whether
 ISBN-10 codes should be converted to ISBN-13.

Parameters:
`convert` - `true` if valid ISBN-10 codes
 should be converted to ISBN-13 codes or `false`
 if valid ISBN-10 codes should be returned unchanged.

- 

## Method Details

  - 

### getInstance

public static ISBNValidator getInstance()
Gets the singleton instance of the ISBN validator which
 converts ISBN-10 codes to ISBN-13.

Returns:
A singleton instance of the ISBN validator.

  - 

### getInstance

public static ISBNValidator getInstance(boolean convert)
Gets the singleton instance of the ISBN validator specifying
 whether ISBN-10 codes should be converted to ISBN-13.

Parameters:
`convert` - `true` if valid ISBN-10 codes
 should be converted to ISBN-13 codes or `false`
 if valid ISBN-10 codes should be returned unchanged.
Returns:
A singleton instance of the ISBN validator.

  - 

### convertToISBN13

public String convertToISBN13(String isbn10)
Convert an ISBN-10 code to an ISBN-13 code.
 

 This method requires a valid ISBN-10 with NO formatting
 characters.

Parameters:
`isbn10` - The ISBN-10 code to convert
Returns:
A converted ISBN-13 code or `null`
 if the ISBN-10 code is not valid

  - 

### isValid

public boolean isValid(String code)
Check the code is either a valid ISBN-10 or ISBN-13 code.

Parameters:
`code` - The code to validate.
Returns:
`true` if a valid ISBN-10 or
 ISBN-13 code, otherwise `false`.

  - 

### isValidISBN10

public boolean isValidISBN10(String code)
Check the code is a valid ISBN-10 code.

Parameters:
`code` - The code to validate.
Returns:
`true` if a valid ISBN-10
 code, otherwise `false`.

  - 

### isValidISBN13

public boolean isValidISBN13(String code)
Check the code is a valid ISBN-13 code.

Parameters:
`code` - The code to validate.
Returns:
`true` if a valid ISBN-13
 code, otherwise `false`.

  - 

### validate

public String validate(String code)
Check the code is either a valid ISBN-10 or ISBN-13 code.
 

 If valid, this method returns the ISBN code with
 formatting characters removed (such as space or hyphen).
 

 Converts an ISBN-10 codes to ISBN-13 if
 `convertToISBN13` is `true`.

Parameters:
`code` - The code to validate.
Returns:
A valid ISBN code if valid, otherwise `null`.

  - 

### validateISBN10

public String validateISBN10(String code)
Check the code is a valid ISBN-10 code.
 

 If valid, this method returns the ISBN-10 code with
 formatting characters removed (such as space or hyphen).

Parameters:
`code` - The code to validate.
Returns:
A valid ISBN-10 code if valid,
 otherwise `null`.

  - 

### validateISBN13

public String validateISBN13(String code)
Check the code is a valid ISBN-13 code.
 

 If valid, this method returns the ISBN-13 code with
 formatting characters removed (such as space or hyphen).

Parameters:
`code` - The code to validate.
Returns:
A valid ISBN-13 code if valid,
 otherwise `null`.