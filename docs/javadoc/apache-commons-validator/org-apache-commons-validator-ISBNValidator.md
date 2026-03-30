Package org.apache.commons.validator

# Class ISBNValidator

java.lang.Object
org.apache.commons.validator.ISBNValidator

---

@Deprecated
public class ISBNValidator
extends Object
Deprecated.
Use the new ISBNValidator in the routines package

A class for validating 10 digit ISBN codes.
 Based on this
 
 algorithm

 **NOTE:** This has been replaced by the new
  `ISBNValidator`.

Since:
1.2.0

- 

## Constructor Summary

Constructors

Constructor
Description
`ISBNValidator()`

Deprecated.
Constructs a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`boolean`
`isValid(String isbn)`

Deprecated.
If the ISBN is formatted with space or dash separators its format is
 validated.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### ISBNValidator

public ISBNValidator()
Deprecated.
Constructs a new instance.

- 

## Method Details

  - 

### isValid

public boolean isValid(String isbn)
Deprecated.
If the ISBN is formatted with space or dash separators its format is
 validated.  Then the digits in the number are weighted, summed, and
 divided by 11 according to the ISBN algorithm.  If the result is zero,
 the ISBN is valid.  This method accepts formatted or raw ISBN codes.

Parameters:
`isbn` - Candidate ISBN number to be validated. `null` is
 considered invalid.
Returns:
true if the string is a valid ISBN code.