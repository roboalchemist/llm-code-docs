Package org.apache.commons.validator.routines

# Class UrlValidator

java.lang.Object
org.apache.commons.validator.routines.UrlValidator

All Implemented Interfaces:
`Serializable`

---

public class UrlValidator
extends Object
implements Serializable

**URL Validation** routines.
 Behavior of validation is modified by passing in options:
 

 
- ALLOW_2_SLASHES - [FALSE]  Allows double '/' characters in the path
 component.
 
- NO_FRAGMENT- [FALSE]  By default fragments are allowed, if this option is
 included then fragments are flagged as illegal.
 
- ALLOW_ALL_SCHEMES - [FALSE] By default only http, https, and ftp are
 considered valid schemes.  Enabling this option will let any scheme pass validation.
 

 

Originally based in on php script by Debbie Dyer, validation.php v1.2b, Date: 03/07/02,
 https://javascript.internet.com. However, this validation now bears little resemblance
 to the php original.
 

```

   Example of usage:
   Construct a UrlValidator with valid schemes of "http", and "https".

    String[] schemes = {"http","https"}.
    UrlValidator urlValidator = new UrlValidator(schemes);
    if (urlValidator.isValid("ftp://foo.bar.com/")) {
       System.out.println("URL is valid");
    } else {
       System.out.println("URL is invalid");
    }

    prints "URL is invalid"
   If instead the default constructor is used.

    UrlValidator urlValidator = new UrlValidator();
    if (urlValidator.isValid("ftp://foo.bar.com/")) {
       System.out.println("URL is valid");
    } else {
       System.out.println("URL is invalid");
    }

   prints out "URL is valid"
  
```

Since:
1.4
See Also:

- 
  Uniform Resource Identifiers (URI): Generic Syntax
 

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final long`
`ALLOW_2_SLASHES`

Allow two slashes in the path component of the URL.

`static final long`
`ALLOW_ALL_SCHEMES`

Allows all validly formatted schemes to pass validation instead of
 supplying a set of valid schemes.

`static final long`
`ALLOW_LOCAL_URLS`

Allow local URLs, such as https://localhost/ or https://machine/ .

`static final long`
`NO_FRAGMENTS`

Enabling this options disallows any URL fragments.

- 

## Constructor Summary

Constructors

Constructor
Description
`UrlValidator()`

Constructs a new instance with default properties.

`UrlValidator(long options)`

Constructs a new instance with the given validation options.

`UrlValidator(String[] schemes)`

Behavior of validation is modified by passing in several strings options:

`UrlValidator(String[] schemes,
 long options)`

Behavior of validation is modified by passing in options:

`UrlValidator(String[] schemes,
 RegexValidator authorityValidator,
 long options)`

Customizable constructor.

`UrlValidator(String[] schemes,
 RegexValidator authorityValidator,
 long options,
 DomainValidator domainValidator)`

Customizable constructor.

`UrlValidator(RegexValidator authorityValidator,
 long options)`

Constructs a new instance with the given validation options.

- 

## Method Summary

Modifier and Type
Method
Description
`protected int`
`countToken(String token,
 String target)`

Returns the number of times the token appears in the target.

`static UrlValidator`
`getInstance()`

Returns the singleton instance of this class with default schemes and options.

`boolean`
`isValid(String value)`

Checks if a field has a valid URL address.

`protected boolean`
`isValidAuthority(String authority)`

Returns true if the authority is properly formatted.

`protected boolean`
`isValidFragment(String fragment)`

Returns true if the given fragment is null or fragments are allowed.

`protected boolean`
`isValidPath(String path)`

Returns true if the path is valid.

`protected boolean`
`isValidQuery(String query)`

Returns true if the query is null, or it's a properly formatted query string.

`protected boolean`
`isValidScheme(String scheme)`

Validate scheme.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### ALLOW_ALL_SCHEMES

public static final long ALLOW_ALL_SCHEMES
Allows all validly formatted schemes to pass validation instead of
 supplying a set of valid schemes.

See Also:

    - Constant Field Values

  - 

### ALLOW_2_SLASHES

public static final long ALLOW_2_SLASHES
Allow two slashes in the path component of the URL.

See Also:

    - Constant Field Values

  - 

### NO_FRAGMENTS

public static final long NO_FRAGMENTS
Enabling this options disallows any URL fragments.

See Also:

    - Constant Field Values

  - 

### ALLOW_LOCAL_URLS

public static final long ALLOW_LOCAL_URLS
Allow local URLs, such as https://localhost/ or https://machine/ .
 This enables a broad-brush check, for complex local machine name
  validation requirements you should create your validator with
  a `RegexValidator` instead (`UrlValidator(RegexValidator, long)`)

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### UrlValidator

public UrlValidator()
Constructs a new instance with default properties.

  - 

### UrlValidator

public UrlValidator(long options)
Constructs a new instance with the given validation options.

Parameters:
`options` - The options should be set using the public constants declared in
 this class.  To set multiple options you simply add them together.  For example,
 ALLOW_2_SLASHES + NO_FRAGMENTS enables both of those options.

  - 

### UrlValidator

public UrlValidator(RegexValidator authorityValidator,
 long options)
Constructs a new instance with the given validation options.

Parameters:
`authorityValidator` - Regular expression validator used to validate the authority part
 This allows the user to override the standard set of domains.
`options` - Validation options. Set using the public constants of this class.
 To set multiple options, simply add them together:
 

`ALLOW_2_SLASHES + NO_FRAGMENTS`
 enables both of those options.

  - 

### UrlValidator

public UrlValidator(String[] schemes)
Behavior of validation is modified by passing in several strings options:

Parameters:
`schemes` - Pass in one or more URL schemes to consider valid, passing in
        a null will default to "http,https,ftp" being valid.
        If a non-null schemes is specified then all valid schemes must
        be specified. Setting the ALLOW_ALL_SCHEMES option will
        ignore the contents of schemes.

  - 

### UrlValidator

public UrlValidator(String[] schemes,
 long options)
Behavior of validation is modified by passing in options:

Parameters:
`schemes` - The set of valid schemes. Ignored if the ALLOW_ALL_SCHEMES option is set.
`options` - The options should be set using the public constants declared in
 this class.  To set multiple options you simply add them together.  For example,
 ALLOW_2_SLASHES + NO_FRAGMENTS enables both of those options.

  - 

### UrlValidator

public UrlValidator(String[] schemes,
 RegexValidator authorityValidator,
 long options)
Customizable constructor. Validation behavior is modified by passing in options.

Parameters:
`schemes` - the set of valid schemes. Ignored if the ALLOW_ALL_SCHEMES option is set.
`authorityValidator` - Regular expression validator used to validate the authority part
`options` - Validation options. Set using the public constants of this class.
 To set multiple options, simply add them together:
 

`ALLOW_2_SLASHES + NO_FRAGMENTS`
 enables both of those options.

  - 

### UrlValidator

public UrlValidator(String[] schemes,
 RegexValidator authorityValidator,
 long options,
 DomainValidator domainValidator)
Customizable constructor. Validation behavior is modified by passing in options.

Parameters:
`schemes` - the set of valid schemes. Ignored if the ALLOW_ALL_SCHEMES option is set.
`authorityValidator` - Regular expression validator used to validate the authority part
`options` - Validation options. Set using the public constants of this class.
 To set multiple options, simply add them together:
 

`ALLOW_2_SLASHES + NO_FRAGMENTS`
 enables both of those options.
`domainValidator` - the DomainValidator to use; must agree with ALLOW_LOCAL_URLS setting
Since:
1.7

- 

## Method Details

  - 

### getInstance

public static UrlValidator getInstance()
Returns the singleton instance of this class with default schemes and options.

Returns:
singleton instance with default schemes and options

  - 

### countToken

protected int countToken(String token,
 String target)
Returns the number of times the token appears in the target.

Parameters:
`token` - Token value to be counted.
`target` - Target value to count tokens in.
Returns:
the number of tokens.

  - 

### isValid

public boolean isValid(String value)

Checks if a field has a valid URL address.

 Note that the method calls #isValidAuthority()
 which checks that the domain is valid.

Parameters:
`value` - The value validation is being performed on.  A `null`
 value is considered invalid.
Returns:
true if the URL is valid.

  - 

### isValidAuthority

protected boolean isValidAuthority(String authority)
Returns true if the authority is properly formatted.  An authority is the combination
 of hostname and port.  A `null` authority value is considered invalid.
 Note: this implementation validates the domain unless a RegexValidator was provided.
 If a RegexValidator was supplied, and it matches, then the authority is regarded
 as valid with no further checks, otherwise the method checks against the
 AUTHORITY_PATTERN and the DomainValidator (ALLOW_LOCAL_URLS)

Parameters:
`authority` - Authority value to validate, allows IDN
Returns:
true if authority (hostname and port) is valid.

  - 

### isValidFragment

protected boolean isValidFragment(String fragment)
Returns true if the given fragment is null or fragments are allowed.

Parameters:
`fragment` - Fragment value to validate.
Returns:
true if fragment is valid.

  - 

### isValidPath

protected boolean isValidPath(String path)
Returns true if the path is valid.  A `null` value is considered invalid.

Parameters:
`path` - Path value to validate.
Returns:
true if path is valid.

  - 

### isValidQuery

protected boolean isValidQuery(String query)
Returns true if the query is null, or it's a properly formatted query string.

Parameters:
`query` - Query value to validate.
Returns:
true if query is valid.

  - 

### isValidScheme

protected boolean isValidScheme(String scheme)
Validate scheme. If schemes[] was initialized to a non-null,
 then only those schemes are allowed.
 Otherwise, the default schemes are "http", "https", "ftp".
 Matching is case-blind.

Parameters:
`scheme` - The scheme to validate.  A `null` value is considered
 invalid.
Returns:
true if valid.