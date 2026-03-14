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

- Field | 

- Constr | 

- Method





- Detail: 

- Field | 

- Constr | 

- Method









picocli

## Class CommandLine.Help.ColorScheme






- java.lang.Object

- 



  - picocli.CommandLine.Help.ColorScheme









- 

Enclosing class:
CommandLine.Help


---




```
public static class CommandLine.Help.ColorScheme
extends Object
```

All usage help message are generated with a color scheme that assigns certain styles and colors to common
 parts of a usage message: the command name, options, positional parameters and option parameters.
 Users may customize these styles by creating Help with a custom color scheme.
 

Note that these options and styles may not be rendered if ANSI escape codes are not
 enabled.
 

From 4.0, instances of this class are immutable.

See Also:
`CommandLine.Help.ColorScheme.Builder`, 
`CommandLine.Help.defaultColorScheme(Ansi)`









- 




  - 



### Nested Class Summary


Nested Classes 

Modifier and Type
Class and Description


`static class `
`CommandLine.Help.ColorScheme.Builder`
Builder class to create `ColorScheme` instances.










  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description


`CommandLine.Help.Ansi`
`ansi()`
Returns the `Ansi` setting of this color scheme.



`CommandLine.Help.Ansi.Text`
`apply(String plainText,
     List<CommandLine.Help.Ansi.IStyle> styles)`
Returns a new Text object where all the specified styles are applied to the full length of the
 specified plain text.



`List<CommandLine.Help.Ansi.IStyle>`
`commandStyles()`
Returns the registered styles for commands in this color scheme.



`CommandLine.Help.Ansi.Text`
`commandText(String command)`
Returns a Text with all command styles applied to the specified command string.



`Map<String,CommandLine.Help.Ansi.IStyle>`
`customMarkupMap()`
Returns the custom mapping from markup names (the names of the `CommandLine.Help.Ansi.Style` enum constants, like bold, italic, fg_blue, bg_green, etc) to `CommandLine.Help.Ansi.IStyle` objects in this color scheme.



`boolean`
`equals(Object obj)` 


`List<CommandLine.Help.Ansi.IStyle>`
`errorStyles()`
Returns the registered styles for errors in this color scheme.



`CommandLine.Help.Ansi.Text`
`errorText(String error)`
Returns a Text with all error styles applied to the specified error string.



`int`
`hashCode()` 


`List<CommandLine.Help.Ansi.IStyle>`
`optionParamStyles()`
Returns the registered styles for option parameters in this color scheme.



`CommandLine.Help.Ansi.Text`
`optionParamText(String optionParam)`
Returns a Text with all optionParam styles applied to the specified optionParam string.



`List<CommandLine.Help.Ansi.IStyle>`
`optionStyles()`
Returns the registered styles for options in this color scheme.



`CommandLine.Help.Ansi.Text`
`optionText(String option)`
Returns a Text with all option styles applied to the specified option string.



`List<CommandLine.Help.Ansi.IStyle>`
`parameterStyles()`
Returns the registered styles for positional parameters in this color scheme.



`CommandLine.Help.Ansi.Text`
`parameterText(String parameter)`
Returns a Text with all parameter styles applied to the specified parameter string.



`CommandLine.Help.Ansi.IStyle[]`
`parse(String commaSeparatedCodes)`
Converts the specified markup styles to an array of `CommandLine.Help.Ansi.IStyle` objects.



`CommandLine.Help.Ansi.IStyle`
`resetStyle()`
Returns the style that "resets" the style state to neutral.



`String`
`richStackTraceString(Throwable t)`
Returns a String with the `error styles` applied to the stack trace lines showing the
 throwable class name and error message (including "Caused by:..." lines), and the `stack trace styles`
 applied to the remaining stack trace of lines the specified Throwable.



`List<CommandLine.Help.Ansi.IStyle>`
`stackTraceStyles()`
Returns the registered styles for stack traces in this color scheme.



`CommandLine.Help.Ansi.Text`
`stackTraceText(String stackTrace)`
Returns a Text with all stackTrace styles applied to all lines in the specified stackTrace string.



`CommandLine.Help.Ansi.Text`
`stackTraceText(Throwable t)`
Returns a Text with all stackTrace styles applied to all lines in the stack trace of the specified Throwable.



`String`
`string(String stringWithMarkup)`
Returns a String where any markup like
 `@|bg(red),white,underline some text|@` is converted to the styles defined in this ColorScheme
 (if its Ansi mode is ON), or to the plain text without the markup (if this ColorScheme's Ansi mode is OFF).



`CommandLine.Help.Ansi.Text`
`text(String stringWithMarkup)`
Returns a new Text object for this ColorScheme, encapsulating the specified string
 which may contain markup like `@|bg(red),white,underline some text|@`.



`String`
`toString()` 





    - 



### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`













- 




  - 



### Method Detail







    - 

#### commandText


```
public CommandLine.Help.Ansi.Text commandText(String command)
```

Returns a Text with all command styles applied to the specified command string.

Parameters:
`command` - the command string to apply the registered command styles to
Returns:
a Text with all command styles applied to the specified command string










    - 

#### optionText


```
public CommandLine.Help.Ansi.Text optionText(String option)
```

Returns a Text with all option styles applied to the specified option string.

Parameters:
`option` - the option string to apply the registered option styles to
Returns:
a Text with all option styles applied to the specified option string










    - 

#### parameterText


```
public CommandLine.Help.Ansi.Text parameterText(String parameter)
```

Returns a Text with all parameter styles applied to the specified parameter string.

Parameters:
`parameter` - the parameter string to apply the registered parameter styles to
Returns:
a Text with all parameter styles applied to the specified parameter string










    - 

#### optionParamText


```
public CommandLine.Help.Ansi.Text optionParamText(String optionParam)
```

Returns a Text with all optionParam styles applied to the specified optionParam string.

Parameters:
`optionParam` - the option parameter string to apply the registered option parameter styles to
Returns:
a Text with all option parameter styles applied to the specified option parameter string










    - 

#### errorText


```
public CommandLine.Help.Ansi.Text errorText(String error)
```

Returns a Text with all error styles applied to the specified error string.

Parameters:
`error` - the error string to apply the registered error styles to
Returns:
a Text with all error styles applied to the specified error string
Since:
4.3










    - 

#### stackTraceText


```
public CommandLine.Help.Ansi.Text stackTraceText(String stackTrace)
```

Returns a Text with all stackTrace styles applied to all lines in the specified stackTrace string.

Parameters:
`stackTrace` - the stack trace string to apply the registered stack trace styles to
Returns:
a Text with all stack trace styles applied to the specified stack trace string
Since:
4.3










    - 

#### stackTraceText


```
public CommandLine.Help.Ansi.Text stackTraceText(Throwable t)
```

Returns a Text with all stackTrace styles applied to all lines in the stack trace of the specified Throwable.

Parameters:
`t` - the Throwable whose stack trace string to apply the registered stack trace styles to
Returns:
a Text with all stack trace styles applied to the stack trace of the specified Throwable
Since:
4.5










    - 

#### richStackTraceString


```
public String richStackTraceString(Throwable t)
```

Returns a String with the `error styles` applied to the stack trace lines showing the
 throwable class name and error message (including "Caused by:..." lines), and the `stack trace styles`
 applied to the remaining stack trace of lines the specified Throwable.

Parameters:
`t` - the Throwable whose stack trace string to apply the error and stack trace styles to
Returns:
a String with error and stack trace styles applied to the stack trace of the specified Throwable
Since:
4.5










    - 

#### ansi


```
public CommandLine.Help.Ansi ansi()
```

Returns the `Ansi` setting of this color scheme.









    - 

#### commandStyles


```
public List<CommandLine.Help.Ansi.IStyle> commandStyles()
```

Returns the registered styles for commands in this color scheme.

Since:
4.0










    - 

#### optionStyles


```
public List<CommandLine.Help.Ansi.IStyle> optionStyles()
```

Returns the registered styles for options in this color scheme.

Since:
4.0










    - 

#### parameterStyles


```
public List<CommandLine.Help.Ansi.IStyle> parameterStyles()
```

Returns the registered styles for positional parameters in this color scheme.

Since:
4.0










    - 

#### optionParamStyles


```
public List<CommandLine.Help.Ansi.IStyle> optionParamStyles()
```

Returns the registered styles for option parameters in this color scheme.

Since:
4.0










    - 

#### errorStyles


```
public List<CommandLine.Help.Ansi.IStyle> errorStyles()
```

Returns the registered styles for errors in this color scheme.

Since:
4.3










    - 

#### stackTraceStyles


```
public List<CommandLine.Help.Ansi.IStyle> stackTraceStyles()
```

Returns the registered styles for stack traces in this color scheme.

Since:
4.3










    - 

#### customMarkupMap


```
public Map<String,CommandLine.Help.Ansi.IStyle> customMarkupMap()
```

Returns the custom mapping from markup names (the names of the `CommandLine.Help.Ansi.Style` enum constants, like bold, italic, fg_blue, bg_green, etc) to `CommandLine.Help.Ansi.IStyle` objects in this color scheme.
 By default this returns an empty map, unless a custom map was configured.

Since:
4.2










    - 

#### parse


```
public CommandLine.Help.Ansi.IStyle[] parse(String commaSeparatedCodes)
```

Converts the specified markup styles to an array of `CommandLine.Help.Ansi.IStyle` objects.
 If no custom markup mapping is specified, this method delegates to `CommandLine.Help.Ansi.Style.parse(String)`,
 otherwise it returns the styles found in the custom mapping for the specified markup styles.

Parameters:
`commaSeparatedCodes` - a string with a comma-separated list of markup styles (for example, `"bold,underline,bg_red"`
Since:
4.2










    - 

#### resetStyle


```
public CommandLine.Help.Ansi.IStyle resetStyle()
```

Returns the style that "resets" the style state to neutral.

Returns:
`CommandLine.Help.Ansi.Style.reset` if no customMarkupMap() is defined, otherwise either the style registered with the "reset" name or an empty `IStyle` if no such style is registered.
Since:
4.2










    - 

#### equals


```
public boolean equals(Object obj)
```


Overrides:
`equals` in class `Object`










    - 

#### hashCode


```
public int hashCode()
```


Overrides:
`hashCode` in class `Object`










    - 

#### toString


```
public String toString()
```


Overrides:
`toString` in class `Object`










    - 

#### apply


```
public CommandLine.Help.Ansi.Text apply(String plainText,
                                        List<CommandLine.Help.Ansi.IStyle> styles)
```

Returns a new Text object where all the specified styles are applied to the full length of the
 specified plain text.

Parameters:
`plainText` - the string to apply all styles to. Must not contain markup!
`styles` - the styles to apply to the full plain text
Returns:
a new Text object
Since:
4.2










    - 

#### text


```
public CommandLine.Help.Ansi.Text text(String stringWithMarkup)
```

Returns a new Text object for this ColorScheme, encapsulating the specified string
 which may contain markup like `@|bg(red),white,underline some text|@`.
 


 Calling `toString()` on the returned Text will convert
 the markup to the styles defined in this ColorScheme
 (if its Ansi mode is ON), or to the plain text without the markup (if this ColorScheme's Ansi mode is OFF).
 


 Equivalent to `this.ansi().new Text(stringWithMarkup, this)`.

Since:
4.2
See Also:
`CommandLine.Help.Ansi.text(String)`










    - 

#### string


```
public String string(String stringWithMarkup)
```

Returns a String where any markup like
 `@|bg(red),white,underline some text|@` is converted to the styles defined in this ColorScheme
 (if its Ansi mode is ON), or to the plain text without the markup (if this ColorScheme's Ansi mode is OFF).
 


 Equivalent to `this.ansi().new Text(stringWithMarkup, this).toString()`.

Since:
4.2
See Also:
`CommandLine.Help.Ansi.string(String)`

















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

- Field | 

- Constr | 

- Method





- Detail: 

- Field | 

- Constr | 

- Method