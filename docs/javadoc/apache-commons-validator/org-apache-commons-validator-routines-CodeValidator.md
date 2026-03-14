Package org.apache.commons.validator.routines

# Class CodeValidator

java.lang.Object
org.apache.commons.validator.routines.CodeValidator

All Implemented Interfaces:
`Serializable`

---

public final class CodeValidator
extends Object
implements Serializable
Generic **Code Validation** providing format, minimum/maximum
 length and `CheckDigit` validations.
 

 Performs the following validations on a code:
 

   
- if the code is null, return null/false as appropriate
   
- trim the input. If the resulting code is empty, return null/false as appropriate
   
- Check the *format* of the code using a *regular expression.* (if specified)
   
- Check the *minimum* and *maximum* length  (if specified) of the *parsed* code
      (that is, parsed by the *regular expression*).
   
- Performs `CheckDigit` validation on the parsed code (if specified).
   
- The `validate(String)` method returns the trimmed, parsed input (or null if validation failed)
 

 

 **Note**
 The `isValid(String)` method will return true if the input passes validation.
 Since this includes trimming as well as potentially dropping parts of the input,
 it is possible for a String to pass validation
 but fail the checkdigit test if passed directly to it (the check digit routines generally don't trim input
 nor do they generally check the format/length).
 To be sure that you are passing valid input to a method use `validate(String)` as follows:
 

```

 Object valid = validator.validate(input);
 if (valid != null) {
    some_method(valid.toString());
 }
 
```

 

 Configure the validator with the appropriate regular expression, minimum/maximum length
 and `CheckDigit` validator and then call one of the two validation
 methods provided:
    

       
- `boolean isValid(code)`
       
- `String validate(code)`
    

 

 Codes often include *format* characters - such as hyphens - to make them
 more easily human-readable. These can be removed prior to length and check digit
 validation by specifying them as a *non-capturing* group in the regular
 expression (that is, use the `(?:   )` notation).
 

 Or just avoid using parentheses except for the parts you want to capture

Since:
1.4
See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`CodeValidator(String regex,
 int minLength,
 int maxLength,
 CheckDigit checkdigit)`

Constructs a code validator with a specified regular
 expression, minimum/maximum length and `CheckDigit` validation.

`CodeValidator(String regex,
 int length,
 CheckDigit checkdigit)`

Constructs a code validator with a specified regular
 expression, length and `CheckDigit`.

`CodeValidator(String regex,
 CheckDigit checkdigit)`

Constructs a code validator with a specified regular
 expression and `CheckDigit`.

`CodeValidator(RegexValidator regexValidator,
 int minLength,
 int maxLength,
 CheckDigit checkdigit)`

Constructs a code validator with a specified regular expression
 validator, minimum/maximum length and `CheckDigit` validation.

`CodeValidator(RegexValidator regexValidator,
 int length,
 CheckDigit checkdigit)`

Constructs a code validator with a specified regular expression,
 validator, length and `CheckDigit` validation.

`CodeValidator(RegexValidator regexValidator,
 CheckDigit checkdigit)`

Constructs a code validator with a specified regular expression,
 validator and `CheckDigit` validation.

- 

## Method Summary

Modifier and Type
Method
Description
`CheckDigit`
`getCheckDigit()`

Gets the check digit validation routine.

`int`
`getMaxLength()`

Gets the maximum length of the code.

`int`
`getMinLength()`

Gets the minimum length of the code.

`RegexValidator`
`getRegexValidator()`

Gets the *regular expression* validator.

`boolean`
`isValid(String input)`

Validate the code returning either `true`
 or `false`.

`Object`
`validate(String input)`

Validate the code returning either the valid code or
 `null` if invalid.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### CodeValidator

public CodeValidator(RegexValidator regexValidator,
 CheckDigit checkdigit)
Constructs a code validator with a specified regular expression,
 validator and `CheckDigit` validation.

Parameters:
`regexValidator` - The format regular expression validator
`checkdigit` - The check digit validation routine.

  - 

### CodeValidator

public CodeValidator(RegexValidator regexValidator,
 int length,
 CheckDigit checkdigit)
Constructs a code validator with a specified regular expression,
 validator, length and `CheckDigit` validation.

Parameters:
`regexValidator` - The format regular expression validator
`length` - The length of the code
  (sets the minimum/maximum to the same value)
`checkdigit` - The check digit validation routine

  - 

### CodeValidator

public CodeValidator(RegexValidator regexValidator,
 int minLength,
 int maxLength,
 CheckDigit checkdigit)
Constructs a code validator with a specified regular expression
 validator, minimum/maximum length and `CheckDigit` validation.

Parameters:
`regexValidator` - The format regular expression validator
`minLength` - The minimum length of the code
`maxLength` - The maximum length of the code
`checkdigit` - The check digit validation routine

  - 

### CodeValidator

public CodeValidator(String regex,
 CheckDigit checkdigit)
Constructs a code validator with a specified regular
 expression and `CheckDigit`.
 The RegexValidator validator is created to be case-sensitive

Parameters:
`regex` - The format regular expression
`checkdigit` - The check digit validation routine

  - 

### CodeValidator

public CodeValidator(String regex,
 int length,
 CheckDigit checkdigit)
Constructs a code validator with a specified regular
 expression, length and `CheckDigit`.
 The RegexValidator validator is created to be case-sensitive

Parameters:
`regex` - The format regular expression.
`length` - The length of the code
  (sets the minimum/maximum to the same)
`checkdigit` - The check digit validation routine

  - 

### CodeValidator

public CodeValidator(String regex,
 int minLength,
 int maxLength,
 CheckDigit checkdigit)
Constructs a code validator with a specified regular
 expression, minimum/maximum length and `CheckDigit` validation.
 The RegexValidator validator is created to be case-sensitive

Parameters:
`regex` - The regular expression
`minLength` - The minimum length of the code
`maxLength` - The maximum length of the code
`checkdigit` - The check digit validation routine

- 

## Method Details

  - 

### getCheckDigit

public CheckDigit getCheckDigit()
Gets the check digit validation routine.
 

 **N.B.** Optional, if not set no Check Digit
 validation will be performed on the code.

Returns:
The check digit validation routine

  - 

### getMaxLength

public int getMaxLength()
Gets the maximum length of the code.
 

 **N.B.** Optional, if less than zero the
 maximum length will not be checked.

Returns:
The maximum length of the code or
 `-1` if the code has no maximum length

  - 

### getMinLength

public int getMinLength()
Gets the minimum length of the code.
 

 **N.B.** Optional, if less than zero the
 minimum length will not be checked.

Returns:
The minimum length of the code or
 `-1` if the code has no minimum length

  - 

### getRegexValidator

public RegexValidator getRegexValidator()
Gets the *regular expression* validator.
 

 **N.B.** Optional, if not set no regular
 expression validation will be performed on the code.

Returns:
The regular expression validator

  - 

### isValid

public boolean isValid(String input)
Validate the code returning either `true`
 or `false`.
 

 This calls `validate(String)` and returns false
 if the return value is null, true otherwise.
 

 Note that `validate(String)` trims the input
 and if there is a `RegexValidator` it may also
 change the input as part of the validation.

Parameters:
`input` - The code to validate
Returns:
`true` if valid, otherwise
 `false`

  - 

### validate

public Object validate(String input)
Validate the code returning either the valid code or
 `null` if invalid.
 

 Note that this method trims the input
 and if there is a `RegexValidator` it may also
 change the input as part of the validation.

Parameters:
`input` - The code to validate
Returns:
The code if valid, otherwise `null`
 if invalid