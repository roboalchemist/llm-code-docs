Package org.jsoup.helper

# Class Regex

java.lang.Object
org.jsoup.helper.Regex

---

public class Regex
extends Object
A regular expression abstraction. Allows jsoup to optionally use the re2j regular expression engine (linear time)
 instead of the JDK's backtracking regex implementation.

 

If the `com.google.re2j` library is found on the classpath, by default it will be used. You can override this
 by setting `-Djsoup.useRe2j=false` to explicitly disable, and use the JDK regex engine.

 

(Currently this a simplified implementation for jsoup's specific use; can extend as required.)

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static interface `
`Regex.Matcher`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static Regex`
`compile(String regex)`

Compile a regex, using re2j if enabled and available; otherwise JDK regex.

`static Regex`
`fromPattern(Pattern pattern)`

Wraps an existing JDK Pattern (for API compat); doesn't switch

`Regex.Matcher`
`matcher(CharSequence input)`
 
`String`
`toString()`
 
`static boolean`
`usingRe2j()`

Checks if re2j is available (on classpath) and enabled (via system property).

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Method Details

  - 

### compile

public static Regex compile(String regex)
Compile a regex, using re2j if enabled and available; otherwise JDK regex.

Parameters:
`regex` - the regex to compile
Returns:
the compiled regex
Throws:
`ValidationException` - if the regex is invalid

  - 

### fromPattern

public static Regex fromPattern(Pattern pattern)
Wraps an existing JDK Pattern (for API compat); doesn't switch

  - 

### usingRe2j

public static boolean usingRe2j()
Checks if re2j is available (on classpath) and enabled (via system property).

Returns:
true if re2j is available and enabled

  - 

### matcher

public Regex.Matcher matcher(CharSequence input)

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`