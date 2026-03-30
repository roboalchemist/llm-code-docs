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

## Class AutoComplete






- java.lang.Object

- 



  - picocli.AutoComplete









- 

---




```
public class AutoComplete
extends Object
```

Stand-alone tool that generates bash auto-complete scripts for picocli-based command line applications.








- 




  - 



### Nested Class Summary


Nested Classes 

Modifier and Type
Class and Description


`static class `
`AutoComplete.GenerateCompletion`
Command that generates a Bash/ZSH completion script for its top-level command.










  - 



### Field Summary


Fields 

Modifier and Type
Field and Description


`static int`
`EXIT_CODE_COMMAND_SCRIPT_EXISTS`
Exit code of this application when the specified command script exists (2).



`static int`
`EXIT_CODE_COMPLETION_SCRIPT_EXISTS`
Exit code of this application when the specified completion script exists (3).



`static int`
`EXIT_CODE_EXECUTION_ERROR`
Exit code of this application when an exception was encountered during operation (4).



`static int`
`EXIT_CODE_INVALID_INPUT`
Exit code of this application when the specified command line arguments are invalid (1).



`static int`
`EXIT_CODE_SUCCESS`
Normal exit code of this application (0).










  - 



### Method Summary


All Methods Static Methods Concrete Methods 

Modifier and Type
Method and Description


`static String`
`bash(String scriptName,
    CommandLine commandLine)`
Generates and returns the source code for an autocompletion bash script for the specified picocli-based application.



`static void`
`bash(String scriptName,
    File out,
    File command,
    CommandLine commandLine)`
Generates source code for an autocompletion bash script for the specified picocli-based application,
 and writes this script to the specified `out` file, and optionally writes an invocation script
 to the specified `command` file.



`static int`
`complete(CommandLine.Model.CommandSpec spec,
        String[] args,
        int argIndex,
        int positionInArg,
        int cursor,
        List<CharSequence> candidates)` 


`static void`
`main(String... args)`
Generates a bash completion script for the specified command class.






    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`













- 




  - 



### Field Detail







    - 

#### EXIT_CODE_SUCCESS


```
public static final int EXIT_CODE_SUCCESS
```

Normal exit code of this application (0).

See Also:
Constant Field Values










    - 

#### EXIT_CODE_INVALID_INPUT


```
public static final int EXIT_CODE_INVALID_INPUT
```

Exit code of this application when the specified command line arguments are invalid (1).

See Also:
Constant Field Values










    - 

#### EXIT_CODE_COMMAND_SCRIPT_EXISTS


```
public static final int EXIT_CODE_COMMAND_SCRIPT_EXISTS
```

Exit code of this application when the specified command script exists (2).

See Also:
Constant Field Values










    - 

#### EXIT_CODE_COMPLETION_SCRIPT_EXISTS


```
public static final int EXIT_CODE_COMPLETION_SCRIPT_EXISTS
```

Exit code of this application when the specified completion script exists (3).

See Also:
Constant Field Values










    - 

#### EXIT_CODE_EXECUTION_ERROR


```
public static final int EXIT_CODE_EXECUTION_ERROR
```

Exit code of this application when an exception was encountered during operation (4).

See Also:
Constant Field Values











  - 



### Method Detail







    - 

#### main


```
public static void main(String... args)
```

Generates a bash completion script for the specified command class.

Parameters:
`args` - command line options. Specify at least the `commandLineFQCN` mandatory parameter, which is
      the fully qualified class name of the annotated `@Command` class to generate a completion script for.
      Other parameters are optional. Specify `-h` to see details on the available options.










    - 

#### bash


```
public static void bash(String scriptName,
                        File out,
                        File command,
                        CommandLine commandLine)
                 throws IOException
```

Generates source code for an autocompletion bash script for the specified picocli-based application,
 and writes this script to the specified `out` file, and optionally writes an invocation script
 to the specified `command` file.

Parameters:
`scriptName` - the name of the command to generate a bash autocompletion script for
`commandLine` - the `CommandLine` instance for the command line application
`out` - the file to write the autocompletion bash script source code to
`command` - the file to write a helper script to that invokes the command, or `null` if no helper script file should be written
Throws:
`IOException` - if a problem occurred writing to the specified files










    - 

#### bash


```
public static String bash(String scriptName,
                          CommandLine commandLine)
```

Generates and returns the source code for an autocompletion bash script for the specified picocli-based application.

Parameters:
`scriptName` - the name of the command to generate a bash autocompletion script for
`commandLine` - the `CommandLine` instance for the command line application
Returns:
source code for an autocompletion bash script










    - 

#### complete


```
public static int complete(CommandLine.Model.CommandSpec spec,
                           String[] args,
                           int argIndex,
                           int positionInArg,
                           int cursor,
                           List<CharSequence> candidates)
```

















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