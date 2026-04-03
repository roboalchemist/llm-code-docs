# Source: https://firebase.google.com/docs/reference/rules/rules.String.md.txt

# Interface: String

# [rules](https://firebase.google.com/docs/reference/rules/rules).String

interface static

Primitive type representing a string value.

Strings can be lexicographically
compared using the `==`, `!=`, `>`,
`<`, `>=` and `<=` operators.

Strings can be concatenated using the `+` operator:  

```scilab
// Concatenate a username and an email domain
'username' + '@domain.com'
```

Sub-strings can be accessed using the index operator `[]`.
They can also be accessed using the range operator `[i:j]`. Note
that parameter `j`, the upper bound in the range operator, is
not inclusive.  

```scilab
// Check if the first character of a string is 'a'
mystring[0] == 'a'

// Check if the string starts with 'abc'
mystring[0:3] == 'abc'
```

Boolean, integer, float, and null values can be converted into strings
using the `string()` function:  

```text
string(true) == "true"
string(1) == "1"
string(2.0) == "2.0"
string(null) == "null"
```

## Methods

### lower

lower() returns [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)

Returns a lowercase version of the input string.

Returns

:   `non-null `[rules.String](https://firebase.google.com/docs/reference/rules/rules.String) the lowercase string.

#### Example

    'ABC'.lower() == 'abc'
    'ABC123'.lower() == 'abc123'

### matches

matches(re) returns [rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean)

Performs a regular expression match on the whole string.

|                                                                                            #### Parameter                                                                                            ||
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| re | [rules.String](https://firebase.google.com/docs/reference/rules/rules.String) A regular expression using [Google RE2 syntax](https://github.com/google/re2/wiki/Syntax). Value must not be null. |

Returns

:   `non-null `[rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean) true if the whole string matches, false otherwise.

#### Example

    'user@domain.com'.matches('.*@domain[.]com') == true
    'banana'.matches('.*@domain[.]com') == false

### replace

replace(re, sub) returns [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)

Replaces all occurrences of substrings matching a regular expression with a
user-supplied string.

|                                                                                            #### Parameter                                                                                             ||
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| re  | [rules.String](https://firebase.google.com/docs/reference/rules/rules.String) A regular expression using [Google RE2 syntax](https://github.com/google/re2/wiki/Syntax). Value must not be null. |
| sub | [rules.String](https://firebase.google.com/docs/reference/rules/rules.String) A string to substitute. Value must not be null.                                                                    |

Returns

:   `non-null `[rules.String](https://firebase.google.com/docs/reference/rules/rules.String) A string representing the result of the replacement
    operation. If no substrings matched the regular expression, the unmodified
    original string is returned.

#### Example

    'banana'.replace("a", "o") == 'bonono'
    'banana'.replace("ana", "ee") == 'beena'
    'foo@test.com'.replace(".", "-") == '---------------' // '.' regex match all

### size

size() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Returns the number of characters in the string.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) the number of characters.

#### Example

    'a'.size() == 1
    'abc'.size() == 3

### split

split(re) returns [rules.List](https://firebase.google.com/docs/reference/rules/rules.List)

Splits a string according to a regular expression.

|                                                                                            #### Parameter                                                                                            ||
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| re | [rules.String](https://firebase.google.com/docs/reference/rules/rules.String) A regular expression using [Google RE2 syntax](https://github.com/google/re2/wiki/Syntax). Value must not be null. |

Returns

:   `non-null `[rules.List](https://firebase.google.com/docs/reference/rules/rules.List) a list of strings.

#### Example

    'a/b/c'.split('/') == ['a', 'b', 'c']

### toUtf8

toUtf8() returns [rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes)

Returns the UTF-8 byte encoding of a string.

Returns

:   `non-null `[rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes) a Bytes sequence containing the UTF-8 encoded
    representation of the string.

#### Example

    '**'.toUtf8() == b'\x2A\x2A'
    'â¬'.toUtf8() == b'\xE2\x82\xAC'

### trim

trim() returns [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)

Returns a version of the string with leading and trailing spaces removed.

Returns

:   `non-null `[rules.String](https://firebase.google.com/docs/reference/rules/rules.String) the trimmed string.

#### Example

    ' a '.trim() == 'a'
    'b'.trim() == 'b'

### upper

upper() returns [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)

Returns an uppercase version of the input string.

Returns

:   `non-null `[rules.String](https://firebase.google.com/docs/reference/rules/rules.String) the uppercase string.

#### Example

    'abc'.upper() == 'ABC'
    'abc123'.upper() == 'ABC123'