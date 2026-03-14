Package org.apache.commons.validator

# Interface CreditCardValidator.CreditCardType

Enclosing class:
`CreditCardValidator`

---

public static interface CreditCardValidator.CreditCardType
CreditCardType implementations define how validation is performed
 for one type/brand of credit card.

Since:
1.1.2

- 

## Method Summary

Modifier and Type
Method
Description
`boolean`
`matches(String card)`

Returns true if the card number matches this type of credit
 card.

- 

## Method Details

  - 

### matches

boolean matches(String card)
Returns true if the card number matches this type of credit
 card.  Note that this method is **not** responsible
 for analyzing the general form of the card number because
 `CreditCardValidator` performs those checks before
 calling this method.  It is generally only required to valid the
 length and prefix of the number to determine if it's the correct
 type.

Parameters:
`card` - The card number, never null.
Returns:
true if the number matches.