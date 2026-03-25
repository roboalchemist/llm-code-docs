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

## Interface CommandLine.IParameterConsumer







- 

Enclosing class:
CommandLine


---




```
public static interface CommandLine.IParameterConsumer
```

Options or positional parameters can be assigned a `IParameterConsumer` that implements
 custom logic to process the parameters for this option or this position.
 When an option or positional parameter with a custom `IParameterConsumer` is matched on the
 command line, picocli's internal parser is temporarily suspended, and this object becomes
 responsible for consuming and processing as many command line arguments as needed.
 

This may be useful when passing through parameters to another command.
 

Example usage:
 

```

 @Command(name = "find")
 class Find {
     @Option(names = "-exec", parameterConsumer = Find.ExecParameterConsumer.class)
     List<String> list = new ArrayList<String>();

     static class ExecParameterConsumer implements IParameterConsumer {
         public void consumeParameters(Stack<String> args, ArgSpec argSpec, CommandSpec commandSpec) {
             List<String> list = argSpec.getValue();
             while (!args.isEmpty()) {
                 String arg = args.pop();
                 list.add(arg);

                 // `find -exec` semantics: stop processing after a ';' or '+' argument
                 if (";".equals(arg) || "+".equals(arg)) {
                     break;
                 }
             }
         }
     }
 }
```

 

If this interface does not meet your requirements, you may have a look at the more powerful
 and flexible `CommandLine.IParameterPreprocessor` interface introduced with picocli 4.6.

Since:
4.0
See Also:
`CommandLine.Option.parameterConsumer()`, 
`CommandLine.Parameters.parameterConsumer()`









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`void`
`consumeParameters(Stack<String> args,
                 CommandLine.Model.ArgSpec argSpec,
                 CommandLine.Model.CommandSpec commandSpec)`
Consumes as many of the specified command line arguments as needed by popping them off
 the specified Stack.














- 




  - 



### Method Detail







    - 

#### consumeParameters


```
void consumeParameters(Stack<String> args,
                       CommandLine.Model.ArgSpec argSpec,
                       CommandLine.Model.CommandSpec commandSpec)
```

Consumes as many of the specified command line arguments as needed by popping them off
 the specified Stack. Implementors are free to ignore the arity
 of the option or positional parameter, they are free to consume arguments that would
 normally be matched as other options of the command, and they are free to consume
 arguments that would normally be matched as an end-of-options delimiter.
 

Implementors are responsible for saving the consumed values;
 if the user object of the option or positional parameter is a Collection
 or a Map, a common approach would be to obtain the current instance via the
 `CommandLine.Model.ArgSpec.getValue()`, and add to this instance. If the user object is an
 array, the implementation would need to create a new array that contains the
 old values as well as the newly consumed values, and store this array in the
 user object via the `CommandLine.Model.ArgSpec.setValue(Object)`.
 


 If the user input is invalid, implementations should throw a `CommandLine.ParameterException`
 with a message to display to the user.
 


 When this method returns, the picocli parser will process the remaining arguments on the Stack.
 

Parameters:
`args` - the command line arguments
`argSpec` - the option or positional parameter for which to consume command line arguments
`commandSpec` - the command that the option or positional parameter belongs to
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