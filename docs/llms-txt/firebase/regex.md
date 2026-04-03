# Source: https://firebase.google.com/docs/reference/security/database/regex.md.txt

Regular expression literals can be used to validate client supplied strings. Use`string.matches(/pattern/)`to test if a string adheres to a regular expression pattern. The regular expression syntax is not identical to common regular expressions syntax, in particular:

- `*``+``.``(``)``[``]``{``}``\`work as normal.
- `^`and`$`anchors only work if we're using them to match the first or last character in the pattern.
- only the`i`(ignore case) modifier flag is supported

## Literals

A regular expression literal is introduced into a security expression using the`/pattern/`notation. To test whether a string adheres to a regular expression pattern, use the matches member function of string. The following matches rule checks whether the new data starts with the string foo.  

    ".validate": "newData.val().matches(/^foo/)"

## Supported Features

Firebase supports only a subset of typical regular expression features. However, the regular expression syntax should feel familiar.

These are the supported symbols:

|        Character         |                                                                 Meaning                                                                  |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `\s``\w``\d``\S``\W``\D` | predefined character sets for matching whitespace, a word character, or a digit, and their negations (respectively)                      |
| `\`                      | escape, the character following is interpreted literally. If you want to match on "" itself, escape it too`/\/`                          |
| `^`                      | anchor to the beginning of the string. This can only be used as the first letter of the pattern. `/a/`matches "ba", while`/^a/`does not. |
| `$`                      | anchor to the end of the string. This can only be used as the last letter of the pattern. `/a/`matches "ab", while`/a$/`does not.        |
| `*`                      | matches zero or many of the preceding pattern. `/^a*$/`matches "" and "aaa", but not "b"                                                 |
| `+`                      | matches one or more of the preceding pattern. `/^a+$/`matches "a" and "aaa", but not ""                                                  |
| `?`                      | matches zero or one of the preceding pattern. `/^a?$/`matches "" and "a", but not "aa"                                                   |
| `.`                      | matches any character `/......../`matches "Firebase"                                                                                     |
| `(pattern)`              | parenthesis groups a pattern into a single unit `/(ab)*/`matches "abab"                                                                  |
| `a|b`                    | matches either a or b `/a|bc/`matches "ac" or "bc"                                                                                       |
| `[akz]`                  | a character set, matches any of the included characters. `/[ABCDEF]/`matches only capitalized letters from A to F.                       |
| `[a-z]`                  | a character interval, matches all characters inclusively in the specified range. `/[0-9A-F]+/`matches hexadecimal strings                |
| `[^0-9]`                 | A leading`^`negates the character set, matching anything other than the specified character set.                                         |

<br />

An`i`trailing the regular expression literal construction (e.g.`/yes/i`) indicates the matching will be case insensitive. Other regular expression modifiers are not supported at this time.

Regular expression matching in theFirebase Realtime DatabaseSecurity Rulesis neither greedy nor non-greedy, since it only allows you to detect a match and not to capture portions of the string.

## Usage

Require a string to be a date formatted as YYYY-MM-DD between 1900-2099:  

    ".validate": "newData.isString() && newData.val().matches(/^(19|20)[0-9][0-9][-\\/. ](0[1-9]|1[012])[-\\/. ](0[1-9]|[12][0-9]|3[01])$/)"

Require string to be an email address:  

    ".validate": "newData.isString() && newData.val().matches(/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,4}$/i)"

| **Note:** **THIS WILL REJECT SOME VALID EMAILS** . Validating email address in regular expressions is difficult in general. See[this site](http://www.regular-expressions.info/email.html)for more depth on the subject.

Require string to be a basic URL:  

    ".validate": "newData.isString() && newData.val().matches(/^(ht|f)tp(s?):\\/\\/[0-9a-zA-Z]([-.\\w]*[0-9a-zA-Z])*((0-9)*)*(\\/?)([a-zA-Z0-9\\-\\.\\?\\,\\'\\/\\\\+&=%\\$#_]*)?$/)"