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

## Interface CommandLine.IParameterPreprocessor







- 

Enclosing class:
CommandLine


---




```
public static interface CommandLine.IParameterPreprocessor
```

Options, positional parameters and commands can be assigned a `IParameterPreprocessor` that
 implements custom logic to preprocess the parameters for this option, position or command.
 When an option, positional parameter or command with a custom `IParameterPreprocessor` is matched
 on the command line, picocli's internal parser is temporarily suspended, and this custom logic is invoked.
 


 This custom logic may completely replace picocli's internal parsing for this option, positional parameter
 or command, or it may do some preprocessing before picocli's internal parsing is resumed for this option,
 positional parameter or command.
 


 The "preprocessing" can include modifying the stack of command line parameters, or modifying the model.
 
 

This may be useful when disambiguating input for commands that have both a positional parameter and an
 option with an optional parameter.
 

Example usage:
 

```

 @Command(name = "edit")
 class Edit {
     @Parameters(index = "0", description = "The file to edit.")
     File file;

     enum Editor { defaultEditor, eclipse, idea, netbeans }

     @Option(names = "--open", arity = "0..1", preprocessor = Edit.MyPreprocessor.class,
         description = {
             "Optionally specify the editor to use; if omitted the default editor is used. ",
             "Example: edit --open=idea FILE opens IntelliJ IDEA (notice the '=' separator)",
             "         edit --open FILE opens the specified file in the default editor"
         })
     Editor editor = Editor.defaultEditor;

     static class MyPreprocessor implements IParameterPreprocessor {
         public boolean preprocess(Stack<String> args, CommandSpec commandSpec, ArgSpec argSpec, Map<String, Object> info) {
             // we need to decide whether the next arg is the file to edit or the name of the editor to use...
             if (" ".equals(info.get("separator"))) { // parameter was not attached to option
                 args.push(Editor.defaultEditor.name()); // act as if the user specified --open=defaultEditor
             }
             return false; // picocli's internal parsing is resumed for this option
         }
     }
 }
```


Since:
4.6
See Also:
`CommandLine.Option.preprocessor()`, 
`CommandLine.Parameters.preprocessor()`









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`boolean`
`preprocess(Stack<String> args,
          CommandLine.Model.CommandSpec commandSpec,
          CommandLine.Model.ArgSpec argSpec,
          Map<String,Object> info)`
Called when either the command, option or positional parameter that has this preprocessor configured was
 recognized by the picocli parser.














- 




  - 



### Method Detail







    - 

#### preprocess


```
boolean preprocess(Stack<String> args,
                   CommandLine.Model.CommandSpec commandSpec,
                   CommandLine.Model.ArgSpec argSpec,
                   Map<String,Object> info)
```

Called when either the command, option or positional parameter that has this preprocessor configured was
 recognized by the picocli parser.
 

Implementors are free to modify one or more of the specified command line arguments before they are
 processed by the picocli parser (or by the option's `parameter consumer`, if one is specified).
 


 Implementors may optionally *consume* one or more of the specified command line arguments:
 a return value of `true` signals that the preprocessor consumed the parameter:
 picocli should skip further processing of this option or positional parameter,
 and the preprocessor implementation takes responsibility for assigning the
 option or positional parameter a value. A return value of `false` means that picocli should
 process the stack as usual for this option or positional parameter, and picocli is responsible for
 assigning this option or positional parameter a value.
 


 For a command, returning `true` signals that the preprocessor takes responsibility for parsing all
 options and positional parameters for this command, and takes responsibility for validating constraints like
 whether all required options and positional parameters were specified.
 A return value of `false` means that picocli should
 process the stack as usual for this command, and picocli is responsible for validation.
 Command preprocessors can signal back to the picocli parser when they detect that the user requested version
 information or usage help by putting a value of `true` in the specified
 `info` map for keys `versionHelpRequested` or `usageHelpRequested`, respectively.
 


 If the user input is invalid, implementations should throw a `CommandLine.ParameterException`
 with a message to display to the user.
 

Parameters:
`args` - the remaining command line arguments that follow the matched argument
           (the matched argument is not on the stack anymore)
`commandSpec` - the command or subcommand that was matched (if the specified `argSpec` is
            `null`), or the command that the matched option or positional parameter belongs to
`argSpec` - the option or positional parameter for which to pre-process command line arguments
             (may be `null` when this method is called for a subcommand that was matched)
`info` - a map containing additional information on the current parser state,
                including whether the option parameter was attached to the option name with
                a `=` separator, whether quotes have already been stripped off the option, etc.
             Implementations may modify this map to communicate back to the picocli parser.
             Supported values:
             
               Supported values in the info Map
               
                 keyvalid valuestype
               
               
                 separator'' (empty string): attached without separator, ' ' (space): not attached, (any other string): option name was attached to option param with specified separator
                 java.lang.String
               
               
                 negated
                 `true`: the option or positional parameter is a negated option/parameter, `false`: the option or positional parameter is not a negated option/parameter
                 java.lang.Boolean
               
               
                 unquoted
                 `true`: quotes surrounding the value have already been stripped off, `false`: quotes surrounding the value have not yet been stripped off
                 java.lang.Boolean
               
               
                 versionHelpRequested
                 `true`: version help was requested, `false`: version help was not requested
                 java.lang.Boolean
               
               
                 usageHelpRequested
                 `true`: usage help was requested, `false`: usage help was not requested
                 java.lang.Boolean
               
             
Returns:
true if the preprocessor consumed the parameter
          and picocli should skip further processing of the stack for this option or positional parameter;
          false if picocli should continue processing the stack for this option or positional parameter
Throws:
`CommandLine.ParameterException` - if the user input is invalid

















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