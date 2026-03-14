Package org.apache.commons.validator

# Class CreditCardValidator

java.lang.Object
org.apache.commons.validator.CreditCardValidator

---

@Deprecated
public class CreditCardValidator
extends Object
Deprecated.
Use the new CreditCardValidator in the routines package. This class
 will be removed in a future release.

Perform credit card validations.

 

 By default, all supported card types are allowed.  You can specify which
 cards should pass validation by configuring the validation options. For
 example,
 

 

```

 CreditCardValidator ccv = new CreditCardValidator(CreditCardValidator.AMEX + CreditCardValidator.VISA);
 
```

 

 configures the validator to only pass American Express and Visa cards.
 If a card type is not directly supported by this class, you can implement
 the CreditCardType interface and pass an instance into the
 `addAllowedCardType` method.
 

 

 For a similar implementation in Perl, reference Sean M. Burke's
 script.
 More information is also available
 here.
 

Since:
1.1

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static interface `
`CreditCardValidator.CreditCardType`

Deprecated.
CreditCardType implementations define how validation is performed
 for one type/brand of credit card.

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final int`
`AMEX`

Deprecated.
Option specifying that American Express cards are allowed.

`static final int`
`DISCOVER`

Deprecated.
Option specifying that Discover cards are allowed.

`static final int`
`MASTERCARD`

Deprecated.
Option specifying that Mastercard cards are allowed.

`static final int`
`NONE`

Deprecated.
Option specifying that no cards are allowed.

`static final int`
`VISA`

Deprecated.
Option specifying that Visa cards are allowed.

- 

## Constructor Summary

Constructors

Constructor
Description
`CreditCardValidator()`

Deprecated.
Create a new CreditCardValidator with default options.

`CreditCardValidator(int options)`

Deprecated.
Creates a new CreditCardValidator with the specified options.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`addAllowedCardType(CreditCardValidator.CreditCardType type)`

Deprecated.
Adds an allowed CreditCardType that participates in the card
 validation algorithm.

`boolean`
`isValid(String card)`

Deprecated.
Checks if the field is a valid credit card number.

`protected boolean`
`luhnCheck(String cardNumber)`

Deprecated.
Checks for a valid credit card number.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### NONE

public static final int NONE
Deprecated.
Option specifying that no cards are allowed.  This is useful if
 you want only custom card types to validate so you turn off the
 default cards with this option.
 

```

 
 CreditCardValidator v = new CreditCardValidator(CreditCardValidator.NONE);
 v.addAllowedCardType(customType);
 v.isValid(aCardNumber);
 
 
```

Since:
1.1.2
See Also:

    - Constant Field Values

  - 

### AMEX

public static final int AMEX
Deprecated.
Option specifying that American Express cards are allowed.

See Also:

    - Constant Field Values

  - 

### VISA

public static final int VISA
Deprecated.
Option specifying that Visa cards are allowed.

See Also:

    - Constant Field Values

  - 

### MASTERCARD

public static final int MASTERCARD
Deprecated.
Option specifying that Mastercard cards are allowed.

See Also:

    - Constant Field Values

  - 

### DISCOVER

public static final int DISCOVER
Deprecated.
Option specifying that Discover cards are allowed.

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### CreditCardValidator

public CreditCardValidator()
Deprecated.
Create a new CreditCardValidator with default options.

  - 

### CreditCardValidator

public CreditCardValidator(int options)
Deprecated.
Creates a new CreditCardValidator with the specified options.

Parameters:
`options` - Pass in
 CreditCardValidator.VISA + CreditCardValidator.AMEX to specify that
 those are the only valid card types.

- 

## Method Details

  - 

### addAllowedCardType

public void addAllowedCardType(CreditCardValidator.CreditCardType type)
Deprecated.
Adds an allowed CreditCardType that participates in the card
 validation algorithm.

Parameters:
`type` - The type that is now allowed to pass validation.
Since:
1.1.2

  - 

### isValid

public boolean isValid(String card)
Deprecated.
Checks if the field is a valid credit card number.

Parameters:
`card` - The card number to validate.
Returns:
Whether the card number is valid.

  - 

### luhnCheck

protected boolean luhnCheck(String cardNumber)
Deprecated.
Checks for a valid credit card number.

Parameters:
`cardNumber` - Credit Card Number.
Returns:
Whether the card number passes the luhnCheck.