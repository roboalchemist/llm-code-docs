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

## Class CommandLine.ExitCode






- java.lang.Object

- 



  - picocli.CommandLine.ExitCode









- 

Enclosing class:
CommandLine


---




```
public static final class CommandLine.ExitCode
extends Object
```

Defines some exit codes used by picocli as default return values from the `execute`
 and `executeHelpRequest` methods.
 

Commands can override these defaults with annotations (e.g. `@Command(exitCodeOnInvalidInput = 64, exitCodeOnExecutionException = 70)`
 or programmatically (e.g. `CommandLine.Model.CommandSpec.exitCodeOnInvalidInput(int)`).
 

Additionally, there are several mechanisms for commands to return custom exit codes.
 See the javadoc of the `execute` method for details.
 
### Standard Exit Codes

 

There are a few conventions, but there is no
 standard. The specific set of codes returned is unique to the program that sets it.
 Typically an exit code of zero indicates success, any non-zero exit code indicates failure. For reference, here are a few conventions:
 

   
  - Wikipedia page on Exit Status
   
  - Bash exit codes
   
  - FreeBSD exit codes
   
  - Windows exit codes
 

 
### Valid Ranges

 

Note that *nix shells may restrict exit codes to the 0-255 range, DOS seems to allow larger numbers.
 See this StackOverflow question.

Since:
4.0









- 




  - 



### Field Summary


Fields 

Modifier and Type
Field and Description


`static int`
`OK`
Return value from the `execute` and
 `executeHelpRequest` methods signifying successful termination.



`static int`
`SOFTWARE`
Return value from the `execute` method signifying internal software error: an exception occurred when invoking the Runnable, Callable or Method user object of a command.



`static int`
`USAGE`
Return value from the `execute` method signifying command line usage error: user input for the command was incorrect, e.g., the wrong number of arguments, a bad flag, a bad syntax in a parameter, or whatever.










  - 



### Method Summary




    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`













- 




  - 



### Field Detail







    - 

#### OK


```
public static final int OK
```

Return value from the `execute` and
 `executeHelpRequest` methods signifying successful termination.
 

The value of this constant is 0.

See Also:
Constant Field Values










    - 

#### SOFTWARE


```
public static final int SOFTWARE
```

Return value from the `execute` method signifying internal software error: an exception occurred when invoking the Runnable, Callable or Method user object of a command. 

The value of this constant is 1.

See Also:
Constant Field Values










    - 

#### USAGE


```
public static final int USAGE
```

Return value from the `execute` method signifying command line usage error: user input for the command was incorrect, e.g., the wrong number of arguments, a bad flag, a bad syntax in a parameter, or whatever. 

The value of this constant is 2.

See Also:
Constant Field Values

















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