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

## Class CommandLine.HelpCommand






- java.lang.Object

- 



  - picocli.CommandLine.HelpCommand









- 

All Implemented Interfaces:
Runnable, Callable<Integer>, CommandLine.IHelpCommandInitializable, CommandLine.IHelpCommandInitializable2


Enclosing class:
CommandLine


---




```
public static final class CommandLine.HelpCommand
extends Object
implements CommandLine.IHelpCommandInitializable, CommandLine.IHelpCommandInitializable2, Runnable, Callable<Integer>
```

Help command that can be installed as a subcommand on all application commands. When invoked with a subcommand
 argument, it prints usage help for the specified subcommand. For example:

```


 // print help for subcommand
 command help subcommand
 
```


 When invoked without additional parameters, it prints usage help for the parent command. For example:
 

```


 // print help for command
 command help
 
```

 For internationalization: this command has a `--help` option with `descriptionKey = "helpCommand.help"`,
 and a `COMMAND` positional parameter with `descriptionKey = "helpCommand.command"`.

Since:
3.0









- 




  - 



### Constructor Summary


Constructors 

Constructor and Description


`HelpCommand()` 









  - 



### Method Summary


All Methods Instance Methods Concrete Methods Deprecated Methods 

Modifier and Type
Method and Description


`Integer`
`call()` 


`void`
`init(CommandLine helpCommandLine,
    CommandLine.Help.Ansi ansi,
    PrintStream out,
    PrintStream err)`
Deprecated. 



`void`
`init(CommandLine helpCommandLine,
    CommandLine.Help.ColorScheme colorScheme,
    PrintWriter out,
    PrintWriter err)`
Initializes this object with the information needed to implement a help command that provides usage help for other commands.



`void`
`run()`
Invokes `usage` for the specified command, or for the parent command.






    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`













- 




  - 



### Constructor Detail







    - 

#### HelpCommand


```
public HelpCommand()
```











  - 



### Method Detail







    - 

#### run


```
public void run()
```

Invokes `usage` for the specified command, or for the parent command.

Specified by:
`run` in interface `Runnable`










    - 

#### call


```
public Integer call()
```


Specified by:
`call` in interface `Callable<Integer>`










    - 

#### init


```
@Deprecated
public void init(CommandLine helpCommandLine,
                              CommandLine.Help.Ansi ansi,
                              PrintStream out,
                              PrintStream err)
```

Deprecated. 
Initializes this object with the information needed to implement a help command that provides usage help for other commands.

Specified by:
`init` in interface `CommandLine.IHelpCommandInitializable`
Parameters:
`helpCommandLine` - the `CommandLine` object associated with this help command. Implementors can use
                        this to walk the command hierarchy and get access to the help command's parent and sibling commands.
`ansi` - whether to use Ansi colors or not
`out` - the stream to print the usage help message to
`err` - the error stream to print any diagnostic messages to, in addition to the output from the exception handler










    - 

#### init


```
public void init(CommandLine helpCommandLine,
                 CommandLine.Help.ColorScheme colorScheme,
                 PrintWriter out,
                 PrintWriter err)
```

Initializes this object with the information needed to implement a help command that provides usage help for other commands.

Specified by:
`init` in interface `CommandLine.IHelpCommandInitializable2`
Parameters:
`helpCommandLine` - the `CommandLine` object associated with this help command. Implementors can use
                        this to walk the command hierarchy and get access to the help command's parent and sibling commands.
`colorScheme` - the color scheme to use when printing help, including whether to use Ansi colors or not
`out` - the output writer to print the usage help message to
`err` - the error writer to print any diagnostic messages to, in addition to the output from the exception handler

















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