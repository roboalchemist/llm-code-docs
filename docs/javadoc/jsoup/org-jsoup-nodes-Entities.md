Package org.jsoup.nodes

# Class Entities

java.lang.Object
org.jsoup.nodes.Entities

---

public class Entities
extends Object
HTML entities, and escape routines. Source: W3C
 HTML named character references.

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static enum `
`Entities.EscapeMode`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static int`
`codepointsForName(String name,
 int[] codepoints)`
 
`static String`
`escape(String data)`

HTML escape an input string, using the default settings (UTF-8, base entities).

`static String`
`escape(String data,
 Document.OutputSettings out)`

HTML escape an input string.

`static String`
`findPrefix(String input)`

Finds the longest base named entity that is a prefix of the input.

`static String`
`getByName(String name)`

Get the character(s) represented by the named entity

`static boolean`
`isBaseNamedEntity(String name)`

Check if the input is a known named entity in the base entity set.

`static boolean`
`isNamedEntity(String name)`

Check if the input is a known named entity

`static String`
`unescape(String string)`

Un-escape an HTML escaped string.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### isNamedEntity

public static boolean isNamedEntity(String name)
Check if the input is a known named entity

Parameters:
`name` - the possible entity name (e.g. "lt" or "amp")
Returns:
true if a known named entity

  - 

### isBaseNamedEntity

public static boolean isBaseNamedEntity(String name)
Check if the input is a known named entity in the base entity set.

Parameters:
`name` - the possible entity name (e.g. "lt" or "amp")
Returns:
true if a known named entity in the base set
See Also:

    - `isNamedEntity(String)`

  - 

### getByName

public static String getByName(String name)
Get the character(s) represented by the named entity

Parameters:
`name` - entity (e.g. "lt" or "amp")
Returns:
the string value of the character(s) represented by this entity, or "" if not defined

  - 

### codepointsForName

public static int codepointsForName(String name,
 int[] codepoints)

  - 

### findPrefix

public static String findPrefix(String input)
Finds the longest base named entity that is a prefix of the input. That is, input "notit" would return "not".

Returns:
longest entity name that is a prefix of the input, or "" if no entity matches

  - 

### escape

public static String escape(String data,
 Document.OutputSettings out)
HTML escape an input string. That is, `<` is returned as `<`. The escaped string is suitable for use
     both in attributes and in text data.

Parameters:
`data` - the un-escaped string to escape
`out` - the output settings to use. This configures the character set escaped against (that is, if a
     character is supported in the output character set, it doesn't have to be escaped), and also HTML or XML
     settings.
Returns:
the escaped string

  - 

### escape

public static String escape(String data)
HTML escape an input string, using the default settings (UTF-8, base entities). That is, `<` is
     returned as `<`. The escaped string is suitable for use both in attributes and in text data.

Parameters:
`data` - the un-escaped string to escape
Returns:
the escaped string
See Also:

    - `escape(String, OutputSettings)`

  - 

### unescape

public static String unescape(String string)
Un-escape an HTML escaped string. That is, `<` is returned as `<`.

Parameters:
`string` - the HTML string to un-escape
Returns:
the unescaped string