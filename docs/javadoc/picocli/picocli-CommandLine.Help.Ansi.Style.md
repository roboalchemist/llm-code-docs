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

## Enum CommandLine.Help.Ansi.Style






- java.lang.Object

- 



  - java.lang.Enum<CommandLine.Help.Ansi.Style>

  - 



    - picocli.CommandLine.Help.Ansi.Style












- 

All Implemented Interfaces:
Serializable, Comparable<CommandLine.Help.Ansi.Style>, CommandLine.Help.Ansi.IStyle


Enclosing class:
CommandLine.Help.Ansi


---




```
public static enum CommandLine.Help.Ansi.Style
extends Enum<CommandLine.Help.Ansi.Style>
implements CommandLine.Help.Ansi.IStyle
```

A set of pre-defined ANSI escape code styles and colors, and a set of convenience methods for parsing
 text with embedded markup style names, as well as convenience methods for converting
 styles to strings with embedded escape codes.








- 




  - 



### Enum Constant Summary


Enum Constants 

Enum Constant and Description


`bg_black` 


`bg_blue` 


`bg_cyan` 


`bg_green` 


`bg_magenta` 


`bg_red` 


`bg_white` 


`bg_yellow` 


`blink` 


`bold` 


`faint` 


`fg_black` 


`fg_blue` 


`fg_cyan` 


`fg_green` 


`fg_magenta` 


`fg_red` 


`fg_white` 


`fg_yellow` 


`italic` 


`reset` 


`reverse` 


`underline` 









  - 



### Field Summary




    - 



### Fields inherited from interface picocli.CommandLine.Help.Ansi.IStyle

`CSI`









  - 



### Method Summary


All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description


`static CommandLine.Help.Ansi.IStyle`
`bg(String str)`
Parses the specified style markup and returns the associated style.



`static CommandLine.Help.Ansi.IStyle`
`fg(String str)`
Parses the specified style markup and returns the associated style.



`String`
`off()`
Returns the ANSI escape code for turning this style off.



`static String`
`off(CommandLine.Help.Ansi.IStyle... styles)`
Returns the concatenated ANSI escape codes for turning all specified styles off.



`String`
`on()`
Returns the ANSI escape code for turning this style on.



`static String`
`on(CommandLine.Help.Ansi.IStyle... styles)`
Returns the concatenated ANSI escape codes for turning all specified styles on.



`static CommandLine.Help.Ansi.IStyle[]`
`parse(String commaSeparatedCodes)`
Parses the specified comma-separated sequence of style descriptors and returns the associated
  styles.



`static CommandLine.Help.Ansi.Style`
`valueOf(String name)`
Returns the enum constant of this type with the specified name.



`static CommandLine.Help.Ansi.Style[]`
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

#### reset


```
public static final CommandLine.Help.Ansi.Style reset
```










    - 

#### bold


```
public static final CommandLine.Help.Ansi.Style bold
```










    - 

#### faint


```
public static final CommandLine.Help.Ansi.Style faint
```










    - 

#### italic


```
public static final CommandLine.Help.Ansi.Style italic
```










    - 

#### underline


```
public static final CommandLine.Help.Ansi.Style underline
```










    - 

#### blink


```
public static final CommandLine.Help.Ansi.Style blink
```










    - 

#### reverse


```
public static final CommandLine.Help.Ansi.Style reverse
```










    - 

#### fg_black


```
public static final CommandLine.Help.Ansi.Style fg_black
```










    - 

#### fg_red


```
public static final CommandLine.Help.Ansi.Style fg_red
```










    - 

#### fg_green


```
public static final CommandLine.Help.Ansi.Style fg_green
```










    - 

#### fg_yellow


```
public static final CommandLine.Help.Ansi.Style fg_yellow
```










    - 

#### fg_blue


```
public static final CommandLine.Help.Ansi.Style fg_blue
```










    - 

#### fg_magenta


```
public static final CommandLine.Help.Ansi.Style fg_magenta
```










    - 

#### fg_cyan


```
public static final CommandLine.Help.Ansi.Style fg_cyan
```










    - 

#### fg_white


```
public static final CommandLine.Help.Ansi.Style fg_white
```










    - 

#### bg_black


```
public static final CommandLine.Help.Ansi.Style bg_black
```










    - 

#### bg_red


```
public static final CommandLine.Help.Ansi.Style bg_red
```










    - 

#### bg_green


```
public static final CommandLine.Help.Ansi.Style bg_green
```










    - 

#### bg_yellow


```
public static final CommandLine.Help.Ansi.Style bg_yellow
```










    - 

#### bg_blue


```
public static final CommandLine.Help.Ansi.Style bg_blue
```










    - 

#### bg_magenta


```
public static final CommandLine.Help.Ansi.Style bg_magenta
```










    - 

#### bg_cyan


```
public static final CommandLine.Help.Ansi.Style bg_cyan
```










    - 

#### bg_white


```
public static final CommandLine.Help.Ansi.Style bg_white
```











  - 



### Method Detail







    - 

#### values


```
public static CommandLine.Help.Ansi.Style[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared.  This method may be used to iterate
over the constants as follows:

```

for (CommandLine.Help.Ansi.Style c : CommandLine.Help.Ansi.Style.values())
    System.out.println(c);

```


Returns:
an array containing the constants of this enum type, in the order they are declared










    - 

#### valueOf


```
public static CommandLine.Help.Ansi.Style valueOf(String name)
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

#### on


```
public String on()
```

Description copied from interface: `CommandLine.Help.Ansi.IStyle`
Returns the ANSI escape code for turning this style on.

Specified by:
`on` in interface `CommandLine.Help.Ansi.IStyle`
Returns:
the ANSI escape code for turning this style on










    - 

#### off


```
public String off()
```

Description copied from interface: `CommandLine.Help.Ansi.IStyle`
Returns the ANSI escape code for turning this style off.

Specified by:
`off` in interface `CommandLine.Help.Ansi.IStyle`
Returns:
the ANSI escape code for turning this style off










    - 

#### on


```
public static String on(CommandLine.Help.Ansi.IStyle... styles)
```

Returns the concatenated ANSI escape codes for turning all specified styles on.

Parameters:
`styles` - the styles to generate ANSI escape codes for
Returns:
the concatenated ANSI escape codes for turning all specified styles on










    - 

#### off


```
public static String off(CommandLine.Help.Ansi.IStyle... styles)
```

Returns the concatenated ANSI escape codes for turning all specified styles off.

Parameters:
`styles` - the styles to generate ANSI escape codes for
Returns:
the concatenated ANSI escape codes for turning all specified styles off










    - 

#### fg


```
public static CommandLine.Help.Ansi.IStyle fg(String str)
```

Parses the specified style markup and returns the associated style.
  The markup may be one of the Style enum value names, or it may be one of the Style enum value
  names when `"fg_"` is prepended, or it may be one of the indexed colors in the 256 color palette.

Parameters:
`str` - the case-insensitive style markup to convert, e.g. `"blue"` or `"fg_blue"`,
          or `"46"` (indexed color) or `"0;5;0"` (RGB components of an indexed color)
Returns:
the IStyle for the specified converter










    - 

#### bg


```
public static CommandLine.Help.Ansi.IStyle bg(String str)
```

Parses the specified style markup and returns the associated style.
  The markup may be one of the Style enum value names, or it may be one of the Style enum value
  names when `"bg_"` is prepended, or it may be one of the indexed colors in the 256 color palette.

Parameters:
`str` - the case-insensitive style markup to convert, e.g. `"blue"` or `"bg_blue"`,
          or `"46"` (indexed color) or `"0;5;0"` (RGB components of an indexed color)
Returns:
the IStyle for the specified converter










    - 

#### parse


```
public static CommandLine.Help.Ansi.IStyle[] parse(String commaSeparatedCodes)
```

Parses the specified comma-separated sequence of style descriptors and returns the associated
  styles. For each markup, strings starting with `"bg("` are delegated to
  `bg(String)`, others are delegated to `fg(String)`.

Parameters:
`commaSeparatedCodes` - one or more descriptors, e.g. `"bg(blue),underline,red"`
Returns:
an array with all styles for the specified descriptors

















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