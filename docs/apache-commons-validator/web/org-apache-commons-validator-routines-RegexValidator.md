Package org.apache.commons.validator.routines

# Class RegexValidator

java.lang.Object
org.apache.commons.validator.routines.RegexValidator

All Implemented Interfaces:
`Serializable`

---

public class RegexValidator
extends Object
implements Serializable
**Regular Expression** validation (using the JRE's regular expression support).
 

 Constructs the validator either for a single regular expression or a set (array) of regular expressions. By default, validation is *case sensitive* but
 constructors are provided to allow *case in-sensitive* validation. For example to create a validator which does *case in-sensitive* validation
 for a set of regular expressions:
 

 

```

 
 String[] regexs = new String[] {...};
 RegexValidator validator = new RegexValidator(regexs, false);
 
 
```

 

 
- Validate `true` or `false`:
 
- 
 

 
  - `boolean valid = validator.isValid(value);`
 

 
 
- Validate returning an aggregated String of the matched groups:
 
- 
 

 
  - `String result = validator.validate(value);`
 

 
 
- Validate returning the matched groups:
 
- 
 

 
  - `String[] result = validator.match(value);`
 

 
 

 **Note that patterns are matched against the entire input.**

 

 Cached instances pre-compile and re-use `Pattern`(s) - which according to the `Pattern` API are safe to use in a multi-threaded environment.
 

Since:
1.4
See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`RegexValidator(String regex)`

Constructs a new *case sensitive* instance for a single regular expression.

`RegexValidator(String... regexs)`

Constructs a new *case sensitive* instance that matches any one in the array of regular expressions.

`RegexValidator(String[] regexs,
 boolean caseSensitive)`

Constructs a new instance that matches any one of the set of regular expressions with the specified case sensitivity.

`RegexValidator(String regex,
 boolean caseSensitive)`

Constructs a new instance for a single regular expression with the specified case sensitivity.

- 

## Method Summary

Modifier and Type
Method
Description
`Pattern[]`
`getPatterns()`

Gets a copy of the Patterns.

`boolean`
`isValid(String value)`

Validates a value against the set of regular expressions.

`String[]`
`match(String value)`

Validates a value against the set of regular expressions returning the array of matched groups.

`String`
`toString()`

Provides a String representation of this validator.

`String`
`validate(String value)`

Validates a value against the set of regular expressions returning a String value of the aggregated groups.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### RegexValidator

public RegexValidator(String regex)
Constructs a new *case sensitive* instance for a single regular expression.

Parameters:
`regex` - The regular expression this validator will validate against

  - 

### RegexValidator

public RegexValidator(String... regexs)
Constructs a new *case sensitive* instance that matches any one in the array of regular expressions.

Parameters:
`regexs` - The set of regular expressions this validator will validate against

  - 

### RegexValidator

public RegexValidator(String regex,
 boolean caseSensitive)
Constructs a new instance for a single regular expression with the specified case sensitivity.

Parameters:
`regex` - The regular expression this validator will validate against
`caseSensitive` - when `true` matching is *case sensitive*, otherwise matching is *case in-sensitive*

  - 

### RegexValidator

public RegexValidator(String[] regexs,
 boolean caseSensitive)
Constructs a new instance that matches any one of the set of regular expressions with the specified case sensitivity.

Parameters:
`regexs` - The set of regular expressions this validator will validate against
`caseSensitive` - when `true` matching is *case sensitive*, otherwise matching is *case in-sensitive*

- 

## Method Details

  - 

### getPatterns

public Pattern[] getPatterns()
Gets a copy of the Patterns.

Returns:
a copy of the Patterns.
Since:
1.8

  - 

### isValid

public boolean isValid(String value)
Validates a value against the set of regular expressions.

Parameters:
`value` - The value to validate.
Returns:
`true` if the value is valid otherwise `false`.

  - 

### match

public String[] match(String value)
Validates a value against the set of regular expressions returning the array of matched groups.

Parameters:
`value` - The value to validate.
Returns:
String array of the *groups* matched if valid or `null` if invalid

  - 

### toString

public String toString()
Provides a String representation of this validator.

Overrides:
`toString` in class `Object`
Returns:
A String representation of this validator.

  - 

### validate

public String validate(String value)
Validates a value against the set of regular expressions returning a String value of the aggregated groups.

Parameters:
`value` - The value to validate.
Returns:
Aggregated String value comprised of the *groups* matched if valid or `null` if invalid