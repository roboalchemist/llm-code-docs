JavaScript is disabled on your browser.





Skip navigation links






- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help







- Prev Class

- Next Class





- Frames

- No Frames





- All Classes









- Summary: 

- Nested | 

- Enum Constants | 

- Field | 

- Method





- Detail: 

- Enum Constants | 

- Field | 

- Method









picocli

## Enum CommandLine.Help.Ansi






- java.lang.Object

- 



  - java.lang.Enum<CommandLine.Help.Ansi>

  - 



    - picocli.CommandLine.Help.Ansi












- 

All Implemented Interfaces:
Serializable, Comparable<CommandLine.Help.Ansi>


Enclosing class:
CommandLine.Help


---




```
public static enum CommandLine.Help.Ansi
extends Enum<CommandLine.Help.Ansi>
```

Provides methods and inner classes to support using ANSI escape codes in usage help messages.








- 




  - 



### Nested Class Summary


Nested Classes 

Modifier and Type
Class and Description


`static interface `
`CommandLine.Help.Ansi.IStyle`
Defines the interface for an ANSI escape sequence.



`static class `
`CommandLine.Help.Ansi.Style`
A set of pre-defined ANSI escape code styles and colors, and a set of convenience methods for parsing
 text with embedded markup style names, as well as convenience methods for converting
 styles to strings with embedded escape codes.



`class `
`CommandLine.Help.Ansi.Text`
Encapsulates rich text with styles and colors.










  - 



### Enum Constant Summary


Enum Constants 

Enum Constant and Description


`AUTO`
Only emit ANSI escape codes if the platform supports it and system property `"picocli.ansi"`
 is not set to any value other than `"true"` (case insensitive).



`OFF`
Forced OFF: never emit ANSI escape code regardless of the platform.



`ON`
Forced ON: always emit ANSI escape code regardless of the platform.










  - 



### Method Summary


All Methods Static Methods Instance Methods Concrete Methods Deprecated Methods 

Modifier and Type
Method and Description


`CommandLine.Help.Ansi.Text`
`apply(String plainText,
     List<CommandLine.Help.Ansi.IStyle> styles)`
Deprecated. 
use `CommandLine.Help.ColorScheme.apply(String, List)` instead




`boolean`
`enabled()`
Returns `true` if ANSI escape codes should be emitted, `false` otherwise.



`String`
`string(String stringWithMarkup)`
Returns a String where any markup like
 `@|bg(red),white,underline some text|@` is converted to ANSI escape codes
 if this Ansi is ON, or suppressed if this Ansi is OFF.



`CommandLine.Help.Ansi.Text`
`text(String stringWithMarkup)`
Returns a new Text object for this Ansi mode, encapsulating the specified string
 which may contain markup like `@|bg(red),white,underline some text|@`.



`static CommandLine.Help.Ansi`
`valueOf(boolean enabled)`
Returns Ansi.ON if the specified `enabled` flag is true, Ansi.OFF otherwise.



`static CommandLine.Help.Ansi`
`valueOf(String name)`
Returns the enum constant of this type with the specified name.



`static CommandLine.Help.Ansi[]`
`values()`
Returns an array containing the constants of this enum type, in
the order they are declared.






    - 



### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`





    - 



### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`













- 




  - 



### Enum Constant Detail







    - 

#### AUTO


```
public static final CommandLine.Help.Ansi AUTO
```

Only emit ANSI escape codes if the platform supports it and system property `"picocli.ansi"`
 is not set to any value other than `"true"` (case insensitive).









    - 

#### ON


```
public static final CommandLine.Help.Ansi ON
```

Forced ON: always emit ANSI escape code regardless of the platform.









    - 

#### OFF


```
public static final CommandLine.Help.Ansi OFF
```

Forced OFF: never emit ANSI escape code regardless of the platform.










  - 



### Method Detail







    - 

#### values


```
public static CommandLine.Help.Ansi[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared.  This method may be used to iterate
over the constants as follows:

```

for (CommandLine.Help.Ansi c : CommandLine.Help.Ansi.values())
    System.out.println(c);

```


Returns:
an array containing the constants of this enum type, in the order they are declared










    - 

#### valueOf


```
public static CommandLine.Help.Ansi valueOf(String name)
```

Returns the enum constant of this type with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this type.  (Extraneous whitespace characters are 
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`IllegalArgumentException` - if this enum type has no constant with the specified name
`NullPointerException` - if the argument is null










    - 

#### enabled


```
public boolean enabled()
```

Returns `true` if ANSI escape codes should be emitted, `false` otherwise.

Returns:
ON: `true`, OFF: `false`, AUTO: if system property `"picocli.ansi"` has value
      `"tty"` (case-insensitive), then return `true` if either `System.console() != null`
      or picocli guesses the application is running in a pseudo-terminal pty on a Linux emulator in Windows.
      If system property `"picocli.ansi"` has value `"true"` (case-sensitive) then return `true`.
      Otherwise use picocli's Heuristics for Enabling ANSI
      to determine whether the platform supports ANSI escape codes.










    - 

#### text


```
public CommandLine.Help.Ansi.Text text(String stringWithMarkup)
```

Returns a new Text object for this Ansi mode, encapsulating the specified string
 which may contain markup like `@|bg(red),white,underline some text|@`.
 


 Calling `toString()` on the returned Text will either include ANSI escape codes
 (if this Ansi mode is ON), or suppress ANSI escape codes (if this Ansi mode is OFF).
 


 Equivalent to `this.new Text(stringWithMarkup)`.

Since:
3.4
See Also:
`CommandLine.Help.ColorScheme.text(String)`










    - 

#### string


```
public String string(String stringWithMarkup)
```

Returns a String where any markup like
 `@|bg(red),white,underline some text|@` is converted to ANSI escape codes
 if this Ansi is ON, or suppressed if this Ansi is OFF.
 


 Equivalent to `this.new Text(stringWithMarkup).toString()`.

Since:
3.4
See Also:
`CommandLine.Help.ColorScheme.string(String)`










    - 

#### valueOf


```
public static CommandLine.Help.Ansi valueOf(boolean enabled)
```

Returns Ansi.ON if the specified `enabled` flag is true, Ansi.OFF otherwise.

Since:
3.4










    - 

#### apply


```
@Deprecated
public CommandLine.Help.Ansi.Text apply(String plainText,
                                                     List<CommandLine.Help.Ansi.IStyle> styles)
```

Deprecated. use `CommandLine.Help.ColorScheme.apply(String, List)` instead
















Skip navigation links






- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help







- Prev Class

- Next Class





- Frames

- No Frames





- All Classes









- Summary: 

- Nested | 

- Enum Constants | 

- Field | 

- Method





- Detail: 

- Enum Constants | 

- Field | 

- Method