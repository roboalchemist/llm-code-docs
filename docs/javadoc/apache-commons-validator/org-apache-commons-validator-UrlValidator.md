Package org.apache.commons.validator

# Class UrlValidator

java.lang.Object
org.apache.commons.validator.UrlValidator

All Implemented Interfaces:
`Serializable`

---

@Deprecated
public class UrlValidator
extends Object
implements Serializable
Deprecated.
Use the new UrlValidator in the routines package. This class
 will be removed in a future release.

Validates URLs.
 Behaviour of validation is modified by passing in options:
 

 
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
1.1
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
`static final int`
`ALLOW_2_SLASHES`

Deprecated.
Allow two slashes in the path component of the URL.

`static final int`
`ALLOW_ALL_SCHEMES`

Deprecated.
Allows all validly formatted schemes to pass validation instead of
 supplying a set of valid schemes.

`protected String[]`
`defaultSchemes`

Deprecated.
If no schemes are provided, default to this set.

`static final int`
`NO_FRAGMENTS`

Deprecated.
Enabling this options disallows any URL fragments.

- 

## Constructor Summary

Constructors

Constructor
Description
`UrlValidator()`

Deprecated.
Create a UrlValidator with default properties.

`UrlValidator(int options)`

Deprecated.
Initialize a UrlValidator with the given validation options.

`UrlValidator(String[] schemes)`

Deprecated.
Behavior of validation is modified by passing in several strings options:

`UrlValidator(String[] schemes,
 int options)`

Deprecated.
Behaviour of validation is modified by passing in options:

- 

## Method Summary

Modifier and Type
Method
Description
`protected int`
`countToken(String token,
 String target)`

Deprecated.
Returns the number of times the token appears in the target.

`boolean`
`isValid(String value)`

Deprecated.
Checks if a field has a valid URL address.

`protected boolean`
`isValidAuthority(String authority)`

Deprecated.
Returns true if the authority is properly formatted.

`protected boolean`
`isValidFragment(String fragment)`

Deprecated.
Returns true if the given fragment is null or fragments are allowed.

`protected boolean`
`isValidPath(String path)`

Deprecated.
Returns true if the path is valid.

`protected boolean`
`isValidQuery(String query)`

Deprecated.
Returns true if the query is null, or it's a properly formatted query string.

`protected boolean`
`isValidScheme(String scheme)`

Deprecated.
Validate scheme.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### ALLOW_ALL_SCHEMES

public static final int ALLOW_ALL_SCHEMES
Deprecated.
Allows all validly formatted schemes to pass validation instead of
 supplying a set of valid schemes.

See Also:

    - Constant Field Values

  - 

### ALLOW_2_SLASHES

public static final int ALLOW_2_SLASHES
Deprecated.
Allow two slashes in the path component of the URL.

See Also:

    - Constant Field Values

  - 

### NO_FRAGMENTS

public static final int NO_FRAGMENTS
Deprecated.
Enabling this options disallows any URL fragments.

See Also:

    - Constant Field Values

  - 

### defaultSchemes

protected String[] defaultSchemes
Deprecated.
If no schemes are provided, default to this set.

- 

## Constructor Details

  - 

### UrlValidator

public UrlValidator()
Deprecated.
Create a UrlValidator with default properties.

  - 

### UrlValidator

public UrlValidator(int options)
Deprecated.
Initialize a UrlValidator with the given validation options.

Parameters:
`options` - The options should be set using the public constants declared in
 this class.  To set multiple options you simply add them together.  For example,
 ALLOW_2_SLASHES + NO_FRAGMENTS enables both of those options.

  - 

### UrlValidator

public UrlValidator(String[] schemes)
Deprecated.
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
 int options)
Deprecated.
Behaviour of validation is modified by passing in options:

Parameters:
`schemes` - The set of valid schemes.
`options` - The options should be set using the public constants declared in
 this class.  To set multiple options you simply add them together.  For example,
 ALLOW_2_SLASHES + NO_FRAGMENTS enables both of those options.

- 

## Method Details

  - 

### countToken

protected int countToken(String token,
 String target)
Deprecated.
Returns the number of times the token appears in the target.

Parameters:
`token` - Token value to be counted.
`target` - Target value to count tokens in.
Returns:
the number of tokens.

  - 

### isValid

public boolean isValid(String value)
Deprecated.

Checks if a field has a valid URL address.

Parameters:
`value` - The value validation is being performed on.  A `null`
 value is considered invalid.
Returns:
true if the URL is valid.

  - 

### isValidAuthority

protected boolean isValidAuthority(String authority)
Deprecated.
Returns true if the authority is properly formatted.  An authority is the combination
 of hostname and port.  A `null` authority value is considered invalid.

Parameters:
`authority` - Authority value to validate.
Returns:
true if authority (hostname and port) is valid.

  - 

### isValidFragment

protected boolean isValidFragment(String fragment)
Deprecated.
Returns true if the given fragment is null or fragments are allowed.

Parameters:
`fragment` - Fragment value to validate.
Returns:
true if fragment is valid.

  - 

### isValidPath

protected boolean isValidPath(String path)
Deprecated.
Returns true if the path is valid.  A `null` value is considered invalid.

Parameters:
`path` - Path value to validate.
Returns:
true if path is valid.

  - 

### isValidQuery

protected boolean isValidQuery(String query)
Deprecated.
Returns true if the query is null, or it's a properly formatted query string.

Parameters:
`query` - Query value to validate.
Returns:
true if query is valid.

  - 

### isValidScheme

protected boolean isValidScheme(String scheme)
Deprecated.
Validate scheme. If schemes[] was initialized to a non-null,
 then only those schemes are allowed.  Note this is slightly different
 than for the constructor.

Parameters:
`scheme` - The scheme to validate.  A `null` value is considered
 invalid.
Returns:
true if valid.