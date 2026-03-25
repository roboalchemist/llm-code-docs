# Package org.apache.commons.validator.routines

---

package org.apache.commons.validator.routines

This package contains *independent* validation routines.
 
## Table of Contents

 

 
- 1. Overview
 
- 2. Date and Time Validators
 

 
  - 2.1 Overview
 
  - 2.2 Validating a Date Value
 
  - 2.3 Formatting
 
  - 2.4 Time Zones
 
  - 2.5 Comparing Dates and Times
 

 
 
- 3. Numeric Validators
 

 
  - 3.1 Overview
 
  - 3.2 Validating a Numeric Value
 
  - 3.3 Formatting
 
  - 3.4 Comparing Numbers
 
  - 3.5 Currency Validation
 
  - 3.6 Percent Validation
 

 
 
- 4. Other Validators
 

 
  - 4.1 Overview
 
  - 4.2 Regular Expression validation
 
  - 4.3 Check Digit Validation/Calculation
 
  - 4.4 General Code Validation
 
  - 4.5 IBAN Validation
 
  - 4.6 ISBN Validation
 
  - 4.7 IP Address Validation
 
  - 4.8 Email Address Validation
 
  - 4.9 URL Validation
 
  - 4.10 Domain Name Validation
 

 
 

 
 
## 1. Overview

 

 Commons Validator serves two purposes:
 
 

 
- To provide standard, independent validation routines/functions.
 
- To provide a *mini* framework for Validation.
 

 

 This package has been created, since version 1.3.0, in an attempt to clearly
 separate these two concerns and is the location for the standard, independent
 validation routines/functions in *Commons Validator*.
 
 

 The contents of this package have no dependencies on the framework aspect of
 Commons Validator and can be used on their own.
 
 
 
## 2. Date and Time Validators

 
 
## 2.1 Overview

 

 The date and time validators either validate according to a specified *format*
 or use a standard *format* for a specified `Locale`.
 
 

 
- Date Validator - validates dates
 converting to a `java.util.Date` type.
 
- Calendar Validator - validates dates
 converting to a `java.util.Calendar` type.
 
- Time Validator - validates times
 converting to a `java.util.Calendar` type.
 

 
 
## 2.2 Validating a Date Value

 

 You can either use one of the `isValid()` methods to just determine
 if a date is valid, or use one of the `validate()` methods to
 validate a date and convert it to a `java.util.Date`...
 
 

```

 // Get the Date validator
 DateValidator validator = DateValidator.getInstance();
 // Validate/Convert the date
 Date fooDate = validator.validate(fooString, "dd/MM/yyyy");
 if (fooDate == null) {
 // error...not a valid date
 return;
 }
 
```

 

The following methods are provided to validate a date/time (return a boolean result):
 
 

 
- `isValid(<em>value</em>)`
 
- `isValid(<em>value</em>, <em>pattern</em>)`
 
- `isValid(<em>value</em>, Locale)`
 
- `isValid(<em>value</em>, <em>pattern</em>, Locale)`
 

 

The following methods are provided to validate a date/time and convert it to either a
 `java.util.Date` or `java.util.Calendar`:
 
 

 
- `validate(<em>value</em>)`
 
- `validate(<em>value</em>, <em>pattern</em>)`
 
- `validate(<em>value</em>, Locale)`
 
- `validate(<em>value</em>, <em>pattern</em>, Locale)`
 

 
 
## 2.3 Formatting

 

 Formatting and validating are two sides of the same coin. Typically
 *input* values which are converted from Strings according to a
 specified *format* also have to be rendered for *output* in
 the same format. These validators provide the mechanism for formatting from
 date/time objects to Strings. The following methods are provided to format
 date/time values as Strings:
 
 

 
- `format(<em>date/calendar</em>)`
 
- `format(<em>date/calendar</em>, <em>pattern</em>)`
 
- `format(<em>date/calendar</em>, Locale)`
 
- `format(<em>date/calendar</em>, <em>pattern</em>, Locale)`
 

 
 
## 2.4 Time Zones

 

 If the date being parsed relates to a different time zone than the
 system default, you can specify the `TimeZone` to use when
 validating/converting:
 
 

```

 // Get the GMT time zone
 TimeZone GMT = TimeZone.getInstance("GMT");
 // Validate/Convert the date using GMT
 Date fooDate = validator.validate(fooString, "dd/MM/yyyy", GMT);
 
```

 

The following Time Zone *flavors* of the Validation/Conversion methods
 are provided:
 

 
- `validate(<em>value</em>, TimeZone)`
 
- `validate(<em>value</em>, <em>pattern</em>, TimeZone)`
 
- `validate(<em>value</em>, Locale, TimeZone)`
 
- `validate(<em>value</em>, <em>pattern</em>, Locale, TimeZone)`
 

 
 
## 2.5 Comparing Dates and Times

 

 As well as validating that a value is a valid date or time, these validators
 also provide *date comparison* functions. The `DateValidator`
 and `CalendarValidator` provide functions for comparing years,
 quarters, months, weeks and dates and the `TimeValidator` provides
 functions for comparing hours, minutes, seconds and milliseconds.
 For example, to check that a date is in the current month, you could use
 the `compareMonths()` method, which compares the year and month
 components of a date:
 
 

```

 // Check if the date is in the current month
 int compare = validator.compareMonths(fooDate, new Date(), null);
 if (compare == 0) {
 // do current month processing
 return;
 }
 // Check if the date is in the previous quarter
 compare = validator.compareQuarters(fooDate, new Date(), null);
 if (compare < 0) {
 // do previous quarter processing
 return;
 }
 // Check if the date is in the next year
 compare = validator.compareYears(fooDate, new Date(), null);
 if (compare > 0) {
 // do next year processing
 return;
 }
 
```

 
 
## 3 Numeric Validators

 
 
## 3.1 Overview

 

 The numeric validators either validate according to a specified *format*
 or use a standard *format* for a specified `Locale` or use
 a *custom* format for a specified `Locale`.
 
 

 
- Byte Validator - validates numbers
 converting to a `java.lang.Byte` type.
 
- Short Validator - validates numbers
 converting to a `java.lang.Short` type.
 
- Integer Validator - validates numbers
 converting to a `java.lang.Integer` type.
 
- Long Validator - validates numbers
 converting to a `java.lang.Long` type.
 
- Float Validator - validates numbers
 converting to a `java.lang.Float` type.
 
- Double Validator - validates numbers
 converting to a `java.lang.Double` type.
 
- BigInteger Validator - validates numbers
 converting to a `java.math.BigInteger` type.
 
- BigDecimal Validator - validates numbers
 converting to a `java.math.BigDecimal` type.
 

 
 
## 3.2 Validating a Numeric Value

 

 You can either use one of the `isValid()` methods to just determine
 if a number is valid, or use one of the `validate()` methods to
 validate a number and convert it to an appropriate type.
 
 

 The following example validates an integer against a custom pattern
 for the *German* locale. Please note the format is specified using
 the standard symbols for `DecimalFormat` so although
 the decimal separator is indicated as a period (".") in the format, the
 validator will check using the German decimal separator - which is a comma (",").
 
 

```

 // Get the Integer validator
 IntegerValidator validator = IntegerValidator.getInstance();
 // Validate/Convert the number
 Integer fooInteger = validator.validate(fooString, "#,##0.00", Locale.GERMAN);
 if (fooInteger == null) {
 // error...not a valid Integer
 return;
 }
 
```

 

The following methods are provided to validate a number (return a boolean result):
 

 
- `isValid(<em>value</em>)`
 
- `isValid(<em>value</em>, <em>pattern</em>)`
 
- `isValid(<em>value</em>, Locale)`
 
- `isValid(<em>value</em>, <em>pattern</em>, Locale)`
 

 

The following methods are provided to validate a number and convert it one of
 the `java.lang.Number` implementations:
 

 
- `validate(<em>value</em>)`
 
- `validate(<em>value</em>, <em>pattern</em>)`
 
- `validate(<em>value</em>, Locale)`
 
- `validate(<em>value</em>, <em>pattern</em>, Locale)`
 

 
 
## 3.3 Formatting

 

 Formatting and validating are two sides of the same coin. Typically
 *input* values which are converted from Strings according to a
 specified *format* also have to be rendered for *output* in
 the same format. These validators provide the mechanism for formatting from
 numeric objects to Strings. The following methods are provided to format
 numeric values as Strings:
 
 

 
- `format(<em>number</em>)`
 
- `format(<em>number</em>, <em>pattern</em>)`
 
- `format(<em>number</em>, Locale)`
 
- `format(<em>number</em>, <em>pattern</em>, Locale)`
 

 
 
## 3.4 Comparing Numbers

 

 As well as validating that a value is a valid number, these validators
 also provide functions for validating the *minimum*, *maximum*
 and *range* of a value.
 
 

```

 // Check the number is between 25 and 75
 if (validator.isInRange(fooInteger, 25, 75) {
 // valid...in the specified range
 return;
 }
 
```

 
 
## 3.5 Currency Validation

 

 A default Currency Validator
 implementation is provided, although all the *numeric* validators
 support currency validation. The default implementation converts
 currency amounts to a `java.math.BigDecimal` and additionally
 it provides *lenient* currency symbol validation. That is, currency
 amounts are valid with *or* without the currency symbol.
 
 

```

 BigDecimalValidator validator = CurrencyValidator.getInstance();
 BigDecimal fooAmount = validator.validate("$12,500.00", Locale.US);
 if (fooAmount == null) {
 // error...not a valid currency amount
 return;
 }
 // Check the amount is a minimum of $1,000
 if (validator.minValue(fooAmount, 1000) {
 // valid...in the specified range
 return;
 }
 
```

 

 If, for example, you want to use the Integer
 Validator to validate a currency, then you can simply create a
 new instance with the appropriate *format style*. Note that
 the other validators do not support the *lenient* currency symbol
 validation.
 
 

```

 IntegerValidator validator =
 new IntegerValidator(true, IntegerValidator.CURRENCY_FORMAT);
 String pattern = "#,###" + 'Â¤' + 'Â¤';  // Use international symbol
 Integer fooAmount = validator.validate("10.100EUR", pattern, Locale.GERMAN);
 if (fooAmount == null) {
 // error...not a valid currency amount
 return;
 }
 
```

 
 
## 3.6 Percent Validation

 

 A default Percent Validator
 implementation is provided, although the *Float*,
 *Double* and *BigDecimal* validators also support
 percent validation. The default implementation converts
 percent amounts to a `java.math.BigDecimal` and additionally
 it provides *lenient* percent symbol validation. That is, percent
 amounts are valid with *or* without the percent symbol.
 
 

```

 BigDecimalValidator validator = PercentValidator.getInstance();
 BigDecimal fooPercent = validator.validate("20%", Locale.US);
 if (fooPercent == null) {
 // error...not a valid percent
 return;
 }
 // Check the percent is between 10% and 90%
 if (validator.isInRange(fooPercent, 0.1, 0.9) {
 // valid...in the specified range
 return;
 }
 
```

 

 If, for example, you want to use the Float
 Validator to validate a percent, then you can simply create a
 new instance with the appropriate *format style*. Note that
 the other validators do not support the *lenient* percent symbol
 validation.
 
 

```

 FloatValidator validator =
 new FloatValidator(true, FloatValidator.PERCENT_FORMAT);
 Float fooPercent = validator.validate("20%", "###%");
 if (fooPercent == null) {
 // error...not a valid percent
 return;
 }
 
```

 

 **Note**: in theory the other numeric validators besides
 *Float*, *Double* and *BigDecimal* (that is, *Byte*,
 *Short*, *Integer*, *Long* and *BigInteger*)
 also support percent validation. However, since they don't allow fractions
 they will only work with percentages greater than 100%.
 
 
 
## 4. Other Validators

 
 
## 4.1 Overview

 

 This section lists other available validators.
 
 

 
- Regular Expressions - validates
 using Java 1.4+ regular expression support
 
- Check Digit - validates/calculates
 check digits (for example, EAN/UPC, credit card, ISBN).
 
- Code Validation - provides generic
 code validation - format, minimum/maximum length and check digit.
 
- IBAN Validation - provides International Bank Account Number validation.
 
- ISBN Validation - provides ISBN-10
 and ISBN-13 validation.
 
- IP Address Validation - provides IPv4 address
 validation.
 
- Email Address Validation - provides email
 address validation according to RFC 822 standards.
 
- URL Validation - provides URL validation on
 scheme, domain, and authority.
 
- Domain Name Validation - provides domain
 name and IANA TLD validation.
 

 
 
## 4.2 Regular Expression Validation

 

 Regular expression validation can be done either by using the *static*
 methods provided by RegexValidator or
 by creating a new instance, which caches and re-uses compiled Patterns.
 
 

 
- **Method Flavours** - three *flavors* of validation methods are provided:
 
- 
 

 
  - `isValid()` methods return true/false to indicate
 whether validation was successful.
 
  - `validate()` methods return a `String`
 value of the matched *groups* aggregated together or
 `null` if invalid.
 
  - `match()` methods return a `String` array
 of the matched *groups* or `null` if invalid.
 

 
 
- **Case Sensitivity** - matching can be done in either a
 *case-sensitive* or *case-insensitive* way.
 
- **Multiple Expressions** - instances of the
 RegexValidator
 can be created to either match against a single regular expression
 or set (String array) of regular expressions.
 

 

 Below is an example of using one of the static methods to validate,
 matching in a *case insensitive* manner and returning a String
 of the matched groups (which doesn't include the hyphen).
 
 

```

 // set up the parameters
 boolean caseSensitive   = false;
 String regex            = "^([A-Z]*)(?:\\-)([A-Z]*)$";
 // validate - result should be a String of value "abcdef"
 String result = RegexValidator.validate("abc-def", regex, caseSensitive);
 
```

 

The following static methods are provided for regular expression validation:
 
 

 
- `isValid(<em>value</em>, <em>regex</em>)`
 
- `isValid(<em>value</em>, <em>regex</em>, <em>caseSensitive</em>)`
 
- `validate(<em>value</em>, <em>regex</em>)`
 
- `validate(<em>value</em>, <em>regex</em>, <em>caseSensitive</em>)`
 
- `match(<em>value</em>, <em>regex</em>)`
 
- `match(<em>value</em>, <em>regex</em>, <em>caseSensitive</em>)`
 

 

 Below is an example of creating an instance of
 RegexValidator matching in a *case insensitive*
 manner against a set of regular expressions:
 
 

```

 // set up the parameters
 boolean caseSensitive = false;
 String regex1   = "^([A-Z]*)(?:\\-)([A-Z]*)*$"
 String regex2   = "^([A-Z]*)$";
 String[] regexs = new String[] {regex1, regex1};
 // Create the validator
 RegexValidator validator = new RegexValidator(regexs, caseSensitive);
 // Validate true/false
 boolean valid = validator.isValid("abc-def");
 // Validate and return a String
 String result = validator.validate("abc-def");
 // Validate and return a String[]
 String[] groups = validator.match("abc-def");
 
```

 

See the
 RegexValidator Javadoc for a full list
 of the available constructors.
 
 
 
## 4.3 Check Digit validation/calculation

 

 CheckDigit defines a new
 type for the calculation and validation of check digits with the
 following methods:
 
 

 
- `isValid(<em>code</em>)` - validates the check digit of a code,
 returning `true` or `false`.
 
- `calculate(<em>code</em>)` - calculates the check digit for a code
 returning the check digit character.
 

 

 The following implementations are provided:
 
 

 
- ABANumberCheckDigit
 for **ABA Number** (or **Routing Transit Number** (RTN)) check digit calculation.
 
- CUSIPCheckDigit
 for **CUSIP** (North American Securities) check digit calculation.
 
- EAN13CheckDigit
 for **EAN-13**, **UPC**, **ISBN-13** check digit calculation.
 
- IBANCheckDigit
 for **IBAN** check digit calculation.
 
- ISBNCheckDigit
 for **ISBN-10** and **ISBN-13** check digit calculation.
 
- ISBN10CheckDigit
 for **ISBN-10** check digit calculation.
 
- ISINCheckDigit
 for **ISIN** International Securities Identifying Number check digit calculation.
 
- LuhnCheckDigit
 for **Luhn** check digit calculation - used by **credit cards**.
 
- ModulusCheckDigit
 - **abstract** class for custom **modulus** check digit
 implementations.
 
- SedolCheckDigit
 for **SEDOL** (UK Securities) check digit calculation.
 
- VerhoeffCheckDigit
 for **Verhoeff** (Dihedral) check digit calculation.
 

 

 The following examples show validating the check digit of a code:
 
 

```

 // Luhn check digit validation
 boolean valid = LuhnCheckDigit.INSTANCE.isValid(code);
 // EAN / UPC / ISBN-13 check digit validation
 boolean valid = EAN13CheckDigit.INSTANCE.isValid(code);
 // ISBN-10 check digit validation
 boolean valid = ISBNCheckDigit.ISBN10.isValid(code);
 boolean valid = ISBN10CheckDigit.INSTANCE.isValid(code);
 // ISBN-13 check digit validation
 boolean valid = ISBNCheckDigit.ISBN13.isValid(code);
 // ISBN-10 or ISBN-13 check digit validation
 boolean valid = ISBNCheckDigit.ISBN.isValid(code);
 
```

 

 The following examples show calculating the check digit of a code:
 
 

```

 // Luhn check digit validation
 char checkdigit = LuhnCheckDigit.INSTANCE.calculate(code);
 // EAN / UPC / ISBN-13 check digit validation
 char checkdigit = EAN13CheckDigit.INSTANCE.calculate(code);
 // ISBN-10 check digit validation
 char checkdigit = ISBNCheckDigit.ISBN10.isValid(code);
 char checkdigit = ISBN10CheckDigit.INSTANCE.calculate(code);
 // ISBN-13 check digit validation
 char checkdigit = ISBNCheckDigit.ISBN13.calculate(code);
 // ISBN-10 or ISBN-13 check digit validation
 char checkdigit = ISBNCheckDigit.ISBN.calculate(code);
 
```

 
 
## 4.4 General Code validation

 

 CodeValidator provides a generic
 implementation for validating codes. It performs the following
 validations on a code:
 
 

 
- **Format** - the format of the code is validated using
 a *regular expression* (see  RegexValidator).
 
- **Length** - the minimum/maximum length of the code is
 checked - after being parsed by the regular expression - with which
 *format* characters can be removed with the use of
 *non-capturing* groups.
 
- **Check Digit** - a CheckDigit
 routine checks that code's check digit is valid.
 

 

 For example to create a validator to validate EAN-13 codes (numeric,
 with a length of 13):
 
 

```

 // Create an EAN-13 code validator
 CodeValidator validator = new CodeValidator("^[0-9]*$", 13, EAN13CheckDigit.INSTANCE);
 // Validate an EAN-13 code
 if (!validator.isValid(code)) {
 ... // invalid
 }
 
```

 
 
## 4.5 IBAN validation

 

 IBANValidator provides validation of
 International Bank Account Number.
 
 

 The validator includes a default set of formats derived from the IBAN registry at
 https://www.swift.com/standards/data-standards/iban.
 
 

 For example:
 
 

```

 // Get an IBANValidator
 IBANValidator validator = IBANValidator.getInstance();
 // Validate an IBAN
 if (!validator.isValid(candidateIBAN)) {
 ... // invalid
 }
 
```

 
 
## 4.6 ISBN validation

 

 ISBNValidator provides ISBN-10
 and ISBN-13 validation and can *optionally* convert
 ISBN-10 codes to ISBN-13.
 
 

 
- **ISBN-10** - validates using a
 CodeValidator with the
 ISBN10CheckDigit
 routine.
 
- 
 

 
  - `isValidISBN10(<em>value</em>)` - returns a boolean
 
  - `validateISBN10(<em>value</em>)` - returns a reformatted ISBN-10 code
 

 
 
- **ISBN-13** - validates using a
 CodeValidator with the
 EAN13CheckDigit
 routine.
 
- 
 

 
  - `isValidISBN13(<em>value</em>)` - returns a boolean
 
  - `validateISBN13(<em>value</em>)` - returns a reformatted ISBN-13 code
 

 
 
- **ISBN-10** and **ISBN-13** - validates codes are either
 valid ISBN-10 or valid ISBN-13 - optionally can convert ISBN-10 codes to ISBN-13.
 
- 
 

 
  - `isValid(<em>value</em>)` - returns a boolean
 
  - `validate(<em>value</em>)` - returns a reformatted ISBN code
 (converts ISBN-10 to ISBN-13 if the *convert* option is `true`).
 

 
 

 

 For example to validate
 
 

```

 // Validate an ISBN-10 or ISBN-13 code
 if (!ISBNValidator.getInstance().isValid(code)) {
 ... // invalid
 }
 // Validate an ISBN-10 or ISBN-13 code (converting to ISBN-13)
 String code = ISBNValidator.getInstance().validate(code);
 // Validate an ISBN-10 or ISBN-13 code (not converting)
 String code = ISBNValidator.getInstance(false).validate(code);
 
```

 
 
## 4.7 IP Address Validation

 

 InetAddressValidator provides
 IPv4 address validation.
 
 

 For example:
 
 

```

 // Get an InetAddressValidator
 InetAddressValidator validator = InetAddressValidator.getInstance();
 // Validate an IPv4 address
 if (!validator.isValid(candidateInetAddress)) {
 ... // invalid
 }
 
```

 
 
## 4.8 Email Address Validation

 

 EmailValidator provides email address
 validation according to RFC 822 standards.
 
 

 For example:
 
 

```

 // Get an EmailValidator
 EmailValidator validator = EmailValidator.getInstance();
 // Validate an email address
 boolean isAddressValid = validator.isValid("[email protected]");
 // Validate a variable containing an email address
 if (!validator.isValid(addressFromUserForm)) {
 webController.sendRedirect(ERROR_REDIRECT, "Email address isn't valid");
 // etc.
 }
 
```

 
 
## 4.9 URL Validation

 

 UrlValidator provides URL validation by
 checking the scheme, authority, path, query, and fragment in turn. Clients
 may specify valid schemes to be used in validating in addition to or instead of
 the default values (HTTP, HTTPS, FTP). The UrlValidator also supports options
 that change the parsing rules; for example, the ALLOW_2_SLASHES option instructs
 the Validator to allow consecutive slash characters in the path component, which
 is considered an error by default.
 For more information on the available options, see the UrlValidator documentation.
 
 

 For example:
 
 

```

 // Get an UrlValidator
 UrlValidator defaultValidator = new UrlValidator(); // default schemes
 if (defaultValidator.isValid("http://www.apache.org")) {
 ... // valid
 }
 if (!defaultValidator.isValid("http//www.oops.com")) {
 ... // invalid
 }
 // Get an UrlValidator with custom schemes
 String[] customSchemes = { "sftp", "scp", "https" };
 UrlValidator customValidator = new UrlValidator(customSchemes);
 if (!customValidator.isValid("http://www.apache.org")) {
 ... // invalid due to insecure protocol
 }
 // Get an UrlValidator that allows double slashes in the path
 UrlValidator doubleSlashValidator = new UrlValidator(UrlValidator.ALLOW_2_SLASHES);
 if (doubleSlashValidator.isValid("http://www.apache.org//projects")) {
 ... // valid only in this Validator instance
 }
 
```

 
 
## 4.10 Domain Name Validation

 

 DomainValidator provides validation of Internet
 domain names as specified by RFC1034/RFC1123 and according to the IANA-recognized
 list of top-level domains (TLDs). Clients may validate an entire domain name, a
 TLD of any category, or a TLD within a specific category.
 
 

 For example:
 
 

```

 // Get a DomainValidator
 DomainValidator validator = DomainValidator.getInstance();
 // Validate a domain name
 if (validator.isValid("www.apache.org")) {
 ... // valid
 }
 if (!validator.isValid("www.apache.wrong")) {
 ... // invalid
 }
 // Validate a TLD
 if (validator.isValidTld(".com")) {
 ... // valid
 }
 if (validator.isValidTld("org")) {
 ... // valid, the leading dot is optional
 }
 if (validator.isValidTld(".us")) {
 ... // valid, country code TLDs are also accepted
 }
 // Validate TLDs in categories
 if (validator.isValidGenericTld(".name")) {
 ... // valid
 }
 if (!validator.isValidGenericTld(".uk")) {
 ... // invalid, .uk is a country code TLD
 }
 if (!validator.isValidCountryCodeTld(".info")) {
 ... // invalid, .info is a generic TLD
 }
 
```

- 

Related Packages

Package
Description
org.apache.commons.validator

The Validator package provides validation for JavaBeans based on an xml file.

org.apache.commons.validator.routines.checkdigit

This package contains *Check Digit* validation/calculation routines.

org.apache.commons.validator.util

This package contains utility classes used by Commons Validator.

- 

Class
Description
AbstractCalendarValidator

Abstract class for Date/Time/Calendar validation.

AbstractFormatValidator

Abstract class for *Format* based Validation.

AbstractNumberValidator

Abstract class for Number Validation.

BigDecimalValidator

**BigDecimal Validation** and Conversion routines (`java.math.BigDecimal`).

BigIntegerValidator

**BigInteger Validation** and Conversion routines (`java.math.BigInteger`).

ByteValidator

**Byte Validation** and Conversion routines (`Byte`).

CalendarValidator

**Calendar Validation** and Conversion routines (`java.util.Calendar`).

CodeValidator

Generic **Code Validation** providing format, minimum/maximum
 length and `CheckDigit` validations.

CreditCardValidator

Perform credit card validations.

CreditCardValidator.CreditCardRange

Class that represents a credit card range.

CurrencyValidator

**Currency Validation** and Conversion routines (`java.math.BigDecimal`).

DateValidator

**Date Validation** and Conversion routines (`java.util.Date`).

DomainValidator

**Domain name** validation routines.

DomainValidator.ArrayType

Enum used by `DomainValidator.updateTLDOverride(ArrayType, String[])`
 to determine which override array to update / fetch

DomainValidator.Item

Specifies overrides when creating a new class.

DoubleValidator

**Double Validation** and Conversion routines (`Double`).

EmailValidator

Perform email validations.

FloatValidator

**Float Validation** and Conversion routines (`Float`).

IBANValidator

IBAN Validator.

IBANValidator.Validator

The validation class

IBANValidatorStatus

Statuses of IBAN validation.

InetAddressValidator

**InetAddress** validation and conversion routines (`java.net.InetAddress`).

IntegerValidator

**Integer Validation** and Conversion routines ({`Integer`).

ISBNValidator

**ISBN-10** and **ISBN-13** Code Validation.

ISINValidator

**ISIN** (International Securities Identifying Number) validation.

ISSNValidator

International Standard Serial Number (ISSN)
 is an eight-digit serial number used to
 uniquely identify a serial publication.

LongValidator

**Long Validation** and Conversion routines (`Long`).

PercentValidator

**Percentage Validation** and Conversion routines (`java.math.BigDecimal`).

RegexValidator

**Regular Expression** validation (using the JRE's regular expression support).

ShortValidator

**Short Validation** and Conversion routines (`Short`).

TimeValidator

**Time Validation** and Conversion routines (`java.util.Calendar`).

UrlValidator

**URL Validation** routines.