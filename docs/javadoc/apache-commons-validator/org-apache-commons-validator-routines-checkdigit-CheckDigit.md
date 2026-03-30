Package org.apache.commons.validator.routines.checkdigit

# Interface CheckDigit

All Known Implementing Classes:
`ABANumberCheckDigit`, `CASNumberCheckDigit`, `CUSIPCheckDigit`, `EAN13CheckDigit`, `ECNumberCheckDigit`, `IBANCheckDigit`, `ISBN10CheckDigit`, `ISBNCheckDigit`, `ISINCheckDigit`, `ISSNCheckDigit`, `LuhnCheckDigit`, `ModulusCheckDigit`, `ModulusTenCheckDigit`, `SedolCheckDigit`, `VerhoeffCheckDigit`

---

public interface CheckDigit
**Check Digit** calculation and validation.
 

 The logic for validating check digits has previously been
 embedded within the logic for specific code validation, which
 includes other validations such as verifying the format
 or length of a code. `CheckDigit` provides for separating out
 the check digit calculation logic enabling it to be more easily
 tested and reused.
 
 

 Although Commons Validator is primarily concerned with validation,
 `CheckDigit` also defines behavior for calculating/generating check
 digits, since it makes sense that users will want to (re-)use the
 same logic for both. The `ISBNValidator`
 makes specific use of this feature by providing the facility to validate ISBN-10 codes
 and then convert them to the new ISBN-13 standard.
 
 

 CheckDigit is used by the new generic `CodeValidator` implementation.
 

 
## Implementations

 See the
 Package Summary for a full
 list of implementations provided within Commons Validator.

Since:
1.4
See Also:

- `CodeValidator`

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`calculate(String code)`

Calculates the *Check Digit* for a code.

`boolean`
`isValid(String code)`

Validates the check digit for the code.

- 

## Method Details

  - 

### calculate

String calculate(String code)
          throws CheckDigitException
Calculates the *Check Digit* for a code.

Parameters:
`code` - The code to calculate the Check Digit for.
 The string must not include the check digit
Returns:
The calculated Check Digit
Throws:
`CheckDigitException` - if an error occurs.

  - 

### isValid

boolean isValid(String code)
Validates the check digit for the code.

Parameters:
`code` - The code to validate, the string must include the check digit.
Returns:
`true` if the check digit is valid, otherwise
 `false`.