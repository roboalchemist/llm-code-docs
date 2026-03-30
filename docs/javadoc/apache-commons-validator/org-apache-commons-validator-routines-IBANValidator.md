Package org.apache.commons.validator.routines

# Class IBANValidator

java.lang.Object
org.apache.commons.validator.routines.IBANValidator

---

public class IBANValidator
extends Object
IBAN Validator.
 

 Checks an IBAN for:
 

 
- country code prefix
 
- IBAN length
 
- pattern (digits and/or uppercase letters)
 
- IBAN Checkdigits (using `IBANCheckDigit`)
 

 The class does not perform checks on the embedded BBAN (Basic Bank Account Number).
 Each country has its own rules for these.
 

 The validator includes a default set of formats derived from the IBAN registry at
 https://www.swift.com/standards/data-standards/iban.
 
 

 This can get out of date, but the set can be adjusted by creating a validator and using the
 `setValidator(String, int, String)` or
 `setValidator(Validator)`
 method to add (or remove) an entry.
 
 

 For example:
 
 

```

 IBANValidator ibv = new IBANValidator();
 ibv.setValidator("XX", 12, "XX\\d{10}")
 
```

 

 The singleton default instance cannot be modified in this way.
 

Since:
1.5.0

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class `
`IBANValidator.Validator`

The validation class

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final IBANValidator`
`DEFAULT_IBAN_VALIDATOR`

The singleton instance which uses the default formats

- 

## Constructor Summary

Constructors

Constructor
Description
`IBANValidator()`

Create a default IBAN validator.

`IBANValidator(IBANValidator.Validator[] validators)`

Create an IBAN validator from the specified map of IBAN formats.

- 

## Method Summary

Modifier and Type
Method
Description
`IBANValidator.Validator[]`
`getDefaultValidators()`

Gets a copy of the default Validators.

`static IBANValidator`
`getInstance()`

Gets the singleton instance of the IBAN validator using the default formats

`IBANValidator.Validator`
`getValidator(String code)`

Gets the Validator for a given IBAN

`boolean`
`hasValidator(String code)`

Does the class have the required validator?

`boolean`
`isValid(String code)`

Validate an IBAN Code

`IBANValidator.Validator`
`setValidator(String countryCode,
 int length,
 String format)`

Installs a validator.

`IBANValidator.Validator`
`setValidator(IBANValidator.Validator validator)`

Installs a validator.

`IBANValidatorStatus`
`validate(String code)`

Validate an IBAN Code

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### DEFAULT_IBAN_VALIDATOR

public static final IBANValidator DEFAULT_IBAN_VALIDATOR
The singleton instance which uses the default formats

- 

## Constructor Details

  - 

### IBANValidator

public IBANValidator()
Create a default IBAN validator.

  - 

### IBANValidator

public IBANValidator(IBANValidator.Validator[] validators)
Create an IBAN validator from the specified map of IBAN formats.

Parameters:
`validators` - map of IBAN formats

- 

## Method Details

  - 

### getInstance

public static IBANValidator getInstance()
Gets the singleton instance of the IBAN validator using the default formats

Returns:
A singleton instance of the IBAN validator

  - 

### getDefaultValidators

public IBANValidator.Validator[] getDefaultValidators()
Gets a copy of the default Validators.

Returns:
a copy of the default Validator array

  - 

### getValidator

public IBANValidator.Validator getValidator(String code)
Gets the Validator for a given IBAN

Parameters:
`code` - a string starting with the ISO country code (for example, an IBAN)
Returns:
the validator or `null` if there is not one registered.

  - 

### hasValidator

public boolean hasValidator(String code)
Does the class have the required validator?

Parameters:
`code` - the code to check
Returns:
true if there is a validator

  - 

### isValid

public boolean isValid(String code)
Validate an IBAN Code

Parameters:
`code` - The value validation is being performed on
Returns:
`true` if the value is valid

  - 

### setValidator

public IBANValidator.Validator setValidator(String countryCode,
 int length,
 String format)
Installs a validator.
 Will replace any existing entry which has the same countryCode.

Parameters:
`countryCode` - the country code
`length` - the length of the IBAN. Must be ≥ 8 and ≤ 32.
 If the length is < 0, the validator is removed, and the format is not used.
`format` - the format of the IBAN (as a regular expression)
Returns:
the previous Validator, or `null` if there was none
Throws:
`IllegalArgumentException` - if there is a problem
`IllegalStateException` - if an attempt is made to modify the singleton validator

  - 

### setValidator

public IBANValidator.Validator setValidator(IBANValidator.Validator validator)
Installs a validator.
 Will replace any existing entry which has the same countryCode

Parameters:
`validator` - the instance to install.
Returns:
the previous Validator, or `null` if there was none
Throws:
`IllegalStateException` - if an attempt is made to modify the singleton validator

  - 

### validate

public IBANValidatorStatus validate(String code)
Validate an IBAN Code

Parameters:
`code` - The value validation is being performed on
Returns:
`IBANValidatorStatus` for validation
Since:
1.10.0