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

## Interface CommandLine.INegatableOptionTransformer







- 

All Known Implementing Classes:
CommandLine.RegexTransformer


Enclosing class:
CommandLine


---




```
public static interface CommandLine.INegatableOptionTransformer
```

Determines the option name transformation of negatable boolean options.
 Making an option negatable has two aspects:
 

   
  - the negative form recognized by the parser while parsing the command line
   
  - the documentation string showing both the positive and the negative form in the usage help message
 


 Additionally, this transformer controls which names of a negatable option are actually negatable:
 for example, by default short options like `-v` do not have a negative form, even if the same option's
 long form, `--verbose`, may have a negative form, `--no-verbose`.
 

Since:
4.0
See Also:
`CommandLine.RegexTransformer`









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`String`
`makeNegative(String optionName,
            CommandLine.Model.CommandSpec cmd)`
Returns the negative form of the specified option name for the parser to recognize when parsing command line arguments.



`String`
`makeSynopsis(String optionName,
            CommandLine.Model.CommandSpec cmd)`
Returns the documentation string to show in the synopsis and usage help message for the specified option.














- 




  - 



### Method Detail







    - 

#### makeNegative


```
String makeNegative(String optionName,
                    CommandLine.Model.CommandSpec cmd)
```

Returns the negative form of the specified option name for the parser to recognize when parsing command line arguments.

Parameters:
`optionName` - the option name to create a negative form for, for example `--force`
`cmd` - the command that the option is part of
Returns:
the negative form of the specified option name, for example `--no-force`










    - 

#### makeSynopsis


```
String makeSynopsis(String optionName,
                    CommandLine.Model.CommandSpec cmd)
```

Returns the documentation string to show in the synopsis and usage help message for the specified option.
 The returned value should be concise and clearly suggest that both the positive and the negative form are valid option names

Parameters:
`optionName` - the option name to create a documentation string for, for example `--force`, or `-XX:+<option>`
`cmd` - the command that the option is part of
Returns:
the documentation string for the negatable option, for example `--[no-]force`, or `-XX:(+|-)<option>`

















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