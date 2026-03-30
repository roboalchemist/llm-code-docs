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

- Field | 

- Required | 

- Optional





- Detail: 

- Field | 

- Element









picocli

## Annotation Type CommandLine.Command







- 

---




```
@Retention(value=RUNTIME)
 @Target(value={TYPE,LOCAL_VARIABLE,FIELD,PACKAGE,METHOD})
public static @interface CommandLine.Command
```


Annotate your class with `@Command` when you want more control over the format of the generated help
 message. From 3.6, methods can also be annotated with `@Command`, where the method parameters define the
 command options and positional parameters.
 

```

 @Command(name              = "Encrypt", mixinStandardHelpOptions = true,
        description         = "Encrypt FILE(s), or standard input, to standard output or to the output file.",
        version             = "Encrypt version 1.0",
        footer              = "Copyright (c) 2017",
        exitCodeListHeading = "Exit Codes:%n",
        exitCodeList        = { " 0:Successful program execution.",
                                "64:Invalid input: an unknown option or invalid parameter was specified.",
                                "70:Execution exception: an exception occurred while executing the business logic."}
        )
 public class Encrypt {
     @Parameters(paramLabel = "FILE", description = "Any number of input files")
     private List<File> files = new ArrayList<File>();

     @Option(names = { "-o", "--out" }, description = "Output file (default: print to console)")
     private File outputFile;

     @Option(names = { "-v", "--verbose"}, description = "Verbose mode. Helpful for troubleshooting. Multiple -v options increase the verbosity.")
     private boolean[] verbose;
 }
```

 


 The structure of a help message looks like this:
 

   
  - [header]
   
  - [synopsis]: `Usage: <commandName> [OPTIONS] [FILE...]`
   
  - [description]
   
  - [parameter list]: `[FILE...]   Any number of input files`
   
  - [option list]: `-h, --help   prints this help message and exits`
   
  - [exit code list]
   
  - [footer]
 









- 




  - 



### Optional Element Summary


Optional Elements 

Modifier and Type
Optional Element and Description


`boolean`
`abbreviateSynopsis`
Specify `true` to generate an abbreviated synopsis like `"<main> [OPTIONS] [PARAMETERS...] [COMMAND]"`.



`boolean`
`addMethodSubcommands`
Specify whether methods annotated with `@Command` should be registered as subcommands of their
 enclosing `@Command` class.



`String[]`
`aliases`
Alternative command names by which this subcommand is recognized on the command line.



`String`
`commandListHeading`
Set the heading preceding the subcommands list.



`String[]`
`customSynopsis`
Specify one or more custom synopsis lines to display instead of an auto-generated synopsis.



`Class<? extends CommandLine.IDefaultValueProvider>`
`defaultValueProvider`
Class that can provide default values dynamically at runtime.



`String[]`
`description`
Optional text to display between the synopsis line(s) and the list of options.



`String`
`descriptionHeading`
Set the heading preceding the description section.



`String[]`
`exitCodeList`
Set the values to be displayed in the exit codes section as a list of `"key:value"` pairs:
  keys are exit codes, values are descriptions.



`String`
`exitCodeListHeading`
Set the heading preceding the exit codes section, may contain `"%n"` line separators.



`int`
`exitCodeOnExecutionException`
Exit code signifying that an exception occurred when invoking the Runnable, Callable or Method user object of a command.



`int`
`exitCodeOnInvalidInput`
Exit code for command line usage error.



`int`
`exitCodeOnSuccess`
Exit code for successful termination.



`int`
`exitCodeOnUsageHelp`
Exit code for successful termination after printing usage help on user request.



`int`
`exitCodeOnVersionHelp`
Exit code for successful termination after printing version help on user request.



`String[]`
`footer`
Optional text to display after the list of options.



`String`
`footerHeading`
Set the heading preceding the footer section.



`String[]`
`header`
Optional summary description of the command, shown before the synopsis.



`String`
`headerHeading`
Set the heading preceding the header section.



`boolean`
`helpCommand`
Set this attribute to `true` if this subcommand is a help command, and required options and positional
 parameters of the parent command should not be validated.



`boolean`
`hidden`
Set `hidden=true` if this command should not be included in the list of commands in the usage help of the parent command.



`boolean`
`mixinStandardHelpOptions`
Adds the standard `-h` and `--help` usageHelp options and `-V`
 and `--version` versionHelp options to the options of this command.



`Class<? extends CommandLine.IModelTransformer>`
`modelTransformer`
Returns the model transformer for this command.



`String`
`name`
Program name to show in the synopsis.



`String`
`optionListHeading`
Set the heading preceding the options list.



`String`
`parameterListHeading`
Set the heading preceding the parameters list.



`Class<? extends CommandLine.IParameterPreprocessor>`
`preprocessor`
Returns the preprocessor for this command.



`char`
`requiredOptionMarker`
Prefix required options with this character in the options list.



`String`
`resourceBundle`
Set the base name of the ResourceBundle to find option and positional parameters descriptions, as well as
 usage help message sections and section headings.



`CommandLine.ScopeType`
`scope`
Returns whether subcommands inherit their attributes from this parent command.



`String`
`separator`
String that separates options from option parameters.



`boolean`
`showAtFileInUsageHelp`
Specify `true` to show a `[@<filename>...]` entry
 in the synopsis and parameter list of the usage help message.



`boolean`
`showDefaultValues`
Specify `true` to show default values in the description column of the options list (except for
 boolean options).



`boolean`
`showEndOfOptionsDelimiterInUsageHelp`
Specify `true` to show a `[--]` "End of options" entry
 in the synopsis and option list of the usage help message.



`boolean`
`sortOptions`
Specify `false` to show Options in declaration order in the option list of the usage help message (or to sort options by their order index if set).



`boolean`
`sortSynopsis`
Specify `false` to show options in declaration order in the synopsis of the usage help message (or to sort options by their order index if set).



`Class<?>[]`
`subcommands`
A list of classes to instantiate and register as subcommands.



`boolean`
`subcommandsRepeatable`
Returns whether the subcommands of this command are repeatable, that is, whether such subcommands can
 occur multiple times and may be followed by sibling commands instead of only by child commands of the subcommand.



`String`
`synopsisHeading`
Set the heading preceding the synopsis text.



`String`
`synopsisSubcommandLabel`
Specify the String to show in the synopsis for the subcommands of this command.



`boolean`
`usageHelpAutoWidth`
If `true`, picocli will attempt to detect the terminal width and adjust the usage help message accordingly.



`int`
`usageHelpWidth`
Set the `usage help message width`.



`String[]`
`version`
Version information for this command, to print to the console when the user specifies an
 option to request version help.



`Class<? extends CommandLine.IVersionProvider>`
`versionProvider`
Class that can provide version information dynamically at runtime.














- 




  - 



### Element Detail







    - 

#### name


```
public abstract String name
```

Program name to show in the synopsis. If omitted, `"<main class>"` is used.
 For declaratively added subcommands, this attribute is also used
 by the parser to recognize subcommands in the command line arguments.

Returns:
the program name to show in the synopsis
See Also:
`CommandLine.Model.CommandSpec.name()`, 
`CommandLine.Help.commandName()`


Default:
"<main class>"










  - 





    - 

#### aliases


```
public abstract String[] aliases
```

Alternative command names by which this subcommand is recognized on the command line.

Returns:
one or more alternative command names
Since:
3.1


Default:
{}










  - 





    - 

#### subcommands


```
public abstract Class<?>[] subcommands
```

A list of classes to instantiate and register as subcommands. When registering subcommands declaratively
 like this, you don't need to call the `CommandLine.addSubcommand(String, Object)` method. For example, this:
 

```

 @Command(subcommands = {
         GitStatus.class,
         GitCommit.class,
         GitBranch.class })
 public class Git { ... }

 CommandLine commandLine = new CommandLine(new Git());
 
```
 is equivalent to this:
 

```

 // alternative: programmatically add subcommands.
 // NOTE: in this case there should be no `subcommands` attribute on the @Command annotation.
 @Command public class Git { ... }

 CommandLine commandLine = new CommandLine(new Git())
         .addSubcommand("status",   new GitStatus())
         .addSubcommand("commit",   new GitCommit())
         .addSubcommand("branch",   new GitBranch());
 
```

 Applications may be interested in the following built-in commands in picocli
 that can be used as subcommands:
 

   
      - `CommandLine.HelpCommand` - a `help` subcommand that prints help on the following or preceding command
   
      - `AutoComplete.GenerateCompletion` - a `generate-completion` subcommand that prints a Bash/ZSH completion script for its parent command, so that clients can install autocompletion in one line by running `source <(parent-command generate-completion)` in the shell
 


Returns:
the declaratively registered subcommands of this command, or an empty array if none
Since:
0.9.8
See Also:
`CommandLine.addSubcommand(String, Object)`, 
`CommandLine.HelpCommand`


Default:
{}










  - 





    - 

#### subcommandsRepeatable


```
public abstract boolean subcommandsRepeatable
```

Returns whether the subcommands of this command are repeatable, that is, whether such subcommands can
 occur multiple times and may be followed by sibling commands instead of only by child commands of the subcommand.

Since:
4.2


Default:
false










  - 





    - 

#### addMethodSubcommands


```
public abstract boolean addMethodSubcommands
```

Specify whether methods annotated with `@Command` should be registered as subcommands of their
 enclosing `@Command` class.
 The default is `true`. For example:
 

```

 @Command
 public class Git {
     @Command
     void status() { ... }
 }

 CommandLine git = new CommandLine(new Git());
 
```
 is equivalent to this:
 

```

 // don't add command methods as subcommands automatically
 @Command(addMethodSubcommands = false)
 public class Git {
     @Command
     void status() { ... }
 }

 // add command methods as subcommands programmatically
 CommandLine git = new CommandLine(new Git());
 CommandLine status = new CommandLine(CommandLine.getCommandMethods(Git.class, "status").get(0));
 git.addSubcommand("status", status);
 
```


Returns:
whether methods annotated with `@Command` should be registered as subcommands
Since:
3.6.0
See Also:
`CommandLine.addSubcommand(String, Object)`, 
`CommandLine.getCommandMethods(Class, String)`, 
`CommandLine.Model.CommandSpec.addMethodSubcommands()`


Default:
true










  - 





    - 

#### separator


```
public abstract String separator
```

String that separates options from option parameters. Default is `"="`. Spaces are also accepted.

Returns:
the string that separates options from option parameters, used both when parsing and when generating usage help
See Also:
`CommandLine.setSeparator(String)`


Default:
"="










  - 





    - 

#### version


```
public abstract String[] version
```

Version information for this command, to print to the console when the user specifies an
 option to request version help. Each element of the array is rendered on a separate line.
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.
 

This is not part of the usage help message.

Returns:
a string or an array of strings with version information about this command (each string in the array is displayed on a separate line).
Since:
0.9.8
See Also:
`CommandLine.printVersionHelp(PrintStream)`


Default:
{}










  - 





    - 

#### versionProvider


```
public abstract Class<? extends CommandLine.IVersionProvider> versionProvider
```

Class that can provide version information dynamically at runtime. An implementation may return version
 information obtained from the JAR manifest, a properties file or some other source.

Returns:
a Class that can provide version information dynamically at runtime
Since:
2.2


Default:
picocli.CommandLine.NoVersionProvider.class










  - 





    - 

#### mixinStandardHelpOptions


```
public abstract boolean mixinStandardHelpOptions
```

Adds the standard `-h` and `--help` usageHelp options and `-V`
 and `--version` versionHelp options to the options of this command.
 


 Note that if no `version()` or `versionProvider()` is specified, the `--version` option will not print anything.
 


 For internationalization: the help option has `descriptionKey = "mixinStandardHelpOptions.help"`,
 and the version option has `descriptionKey = "mixinStandardHelpOptions.version"`.
 

Returns:
whether the auto-help mixin should be added to this command
Since:
3.0


Default:
false










  - 





    - 

#### helpCommand


```
public abstract boolean helpCommand
```

Set this attribute to `true` if this subcommand is a help command, and required options and positional
 parameters of the parent command should not be validated. If a subcommand marked as `helpCommand` is
 specified on the command line, picocli will not validate the parent arguments (so no "missing required
 option" errors) and the `CommandLine.printHelpIfRequested(List, PrintStream, PrintStream, Help.Ansi)` method will return `true`.

Returns:
`true` if this subcommand is a help command and picocli should not check for missing required
      options and positional parameters on the parent command
Since:
3.0


Default:
false










  - 





    - 

#### headerHeading


```
public abstract String headerHeading
```

Set the heading preceding the header section.
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.

Returns:
the heading preceding the header section
See Also:
`CommandLine.Model.UsageMessageSpec.headerHeading()`, 
`CommandLine.Help.headerHeading(Object...)`


Default:
""










  - 





    - 

#### header


```
public abstract String[] header
```

Optional summary description of the command, shown before the synopsis. Each element of the array is rendered on a separate line.
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.

Returns:
summary description of the command
See Also:
`CommandLine.Model.UsageMessageSpec.header()`, 
`CommandLine.Help.header(Object...)`


Default:
{}










  - 





    - 

#### synopsisHeading


```
public abstract String synopsisHeading
```

Set the heading preceding the synopsis text. The default heading is `"Usage: "` (without a line break between the heading and the synopsis text).
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.

Returns:
the heading preceding the synopsis text
See Also:
`CommandLine.Help.synopsisHeading(Object...)`


Default:
"Usage: "










  - 





    - 

#### abbreviateSynopsis


```
public abstract boolean abbreviateSynopsis
```

Specify `true` to generate an abbreviated synopsis like `"<main> [OPTIONS] [PARAMETERS...] [COMMAND]"`.
 By default, a detailed synopsis with individual option names and parameters is generated.

Returns:
whether the synopsis should be abbreviated
See Also:
`CommandLine.Help.abbreviatedSynopsis()`, 
`CommandLine.Help.detailedSynopsis(int, Comparator, boolean)`


Default:
false










  - 





    - 

#### customSynopsis


```
public abstract String[] customSynopsis
```

Specify one or more custom synopsis lines to display instead of an auto-generated synopsis. Each element of the array is rendered on a separate line.
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.

Returns:
custom synopsis text to replace the auto-generated synopsis
See Also:
`CommandLine.Help.customSynopsis(Object...)`


Default:
{}










  - 





    - 

#### synopsisSubcommandLabel


```
public abstract String synopsisSubcommandLabel
```

Specify the String to show in the synopsis for the subcommands of this command. The default is
 `"[COMMAND]"`. Ignored if this command has no subcommands.

Since:
4.0


Default:
"[COMMAND]"










  - 





    - 

#### descriptionHeading


```
public abstract String descriptionHeading
```

Set the heading preceding the description section.
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.

Returns:
the heading preceding the description section
See Also:
`CommandLine.Help.descriptionHeading(Object...)`


Default:
""










  - 





    - 

#### description


```
public abstract String[] description
```

Optional text to display between the synopsis line(s) and the list of options. Each element of the array is rendered on a separate line.
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.

Returns:
description of this command
See Also:
`CommandLine.Help.description(Object...)`


Default:
{}










  - 





    - 

#### parameterListHeading


```
public abstract String parameterListHeading
```

Set the heading preceding the parameters list.
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.

Returns:
the heading preceding the parameters list
See Also:
`CommandLine.Help.parameterListHeading(Object...)`


Default:
""










  - 





    - 

#### optionListHeading


```
public abstract String optionListHeading
```

Set the heading preceding the options list.
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.

Returns:
the heading preceding the options list
See Also:
`CommandLine.Help.optionListHeading(Object...)`


Default:
""










  - 





    - 

#### sortOptions


```
public abstract boolean sortOptions
```

Specify `false` to show Options in declaration order in the option list of the usage help message (or to sort options by their order index if set).
 Note that picocli cannot reliably detect declaration order in commands that have both `@Option`-annotated methods and `@Option`-annotated fields.
 The default (`true`) is to sort alphabetically.

Returns:
whether options should be shown in alphabetic order.


Default:
true










  - 





    - 

#### sortSynopsis


```
public abstract boolean sortSynopsis
```

Specify `false` to show options in declaration order in the synopsis of the usage help message (or to sort options by their order index if set).
 Note that picocli cannot reliably detect declaration order in commands that have both `@Option`-annotated methods and `@Option`-annotated fields.
 The default (`true`) is to sort alphabetically.

Returns:
whether options in the synopsis should be shown in alphabetic order.
Since:
4.7.7


Default:
true










  - 





    - 

#### requiredOptionMarker


```
public abstract char requiredOptionMarker
```

Prefix required options with this character in the options list. The default is no marker: the synopsis
 indicates which options and parameters are required.

Returns:
the character to show in the options list to mark required options


Default:
32










  - 





    - 

#### defaultValueProvider


```
public abstract Class<? extends CommandLine.IDefaultValueProvider> defaultValueProvider
```

Class that can provide default values dynamically at runtime. An implementation may return default
 value obtained from a configuration file like a properties file or some other source.
 


 Applications may be interested in the `CommandLine.PropertiesDefaultProvider` built-in default provider
 that allows end users to maintain their own default values for options and positional parameters,
 which may override the defaults that are hard-coded in the application.
 

Returns:
a Class that can provide default values dynamically at runtime
Since:
3.6


Default:
picocli.CommandLine.NoDefaultProvider.class










  - 





    - 

#### showDefaultValues


```
public abstract boolean showDefaultValues
```

Specify `true` to show default values in the description column of the options list (except for
 boolean options). False by default.
 

Note that picocli 3.2 allows embedding default values anywhere in the
 option or positional parameter description that ignores this setting.

Returns:
whether the default values for options and parameters should be shown in the description column


Default:
false










  - 





    - 

#### showAtFileInUsageHelp


```
public abstract boolean showAtFileInUsageHelp
```

Specify `true` to show a `[@<filename>...]` entry
 in the synopsis and parameter list of the usage help message.
 (The entry is not shown if expanding parameter files is disabled.)

Since:
4.2


Default:
false










  - 





    - 

#### showEndOfOptionsDelimiterInUsageHelp


```
public abstract boolean showEndOfOptionsDelimiterInUsageHelp
```

Specify `true` to show a `[--]` "End of options" entry
 in the synopsis and option list of the usage help message.

Since:
4.3


Default:
false










  - 





    - 

#### commandListHeading


```
public abstract String commandListHeading
```

Set the heading preceding the subcommands list. The default heading is `"Commands:%n"` (with a line break at the end).
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.

Returns:
the heading preceding the subcommands list
See Also:
`CommandLine.Help.commandListHeading(Object...)`


Default:
"Commands:%n"










  - 





    - 

#### footerHeading


```
public abstract String footerHeading
```

Set the heading preceding the footer section.
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.

Returns:
the heading preceding the footer section
See Also:
`CommandLine.Help.footerHeading(Object...)`


Default:
""










  - 





    - 

#### footer


```
public abstract String[] footer
```

Optional text to display after the list of options. Each element of the array is rendered on a separate line.
 

May contain embedded format specifiers like `%n` line separators. Literal percent `'%'` characters must be escaped with another `%`.

Returns:
text to display after the list of options
See Also:
`CommandLine.Help.footer(Object...)`


Default:
{}










  - 





    - 

#### hidden


```
public abstract boolean hidden
```

Set `hidden=true` if this command should not be included in the list of commands in the usage help of the parent command.

Returns:
whether this command should be excluded from the usage message
Since:
3.0


Default:
false










  - 





    - 

#### resourceBundle


```
public abstract String resourceBundle
```

Set the base name of the ResourceBundle to find option and positional parameters descriptions, as well as
 usage help message sections and section headings. 

See `CommandLine.Model.Messages` for more details and an example.

Returns:
the base name of the ResourceBundle for usage help strings
Since:
3.6
See Also:
`CommandLine.Model.ArgSpec.messages()`, 
`CommandLine.Model.UsageMessageSpec.messages()`, 
`CommandLine.Model.CommandSpec.resourceBundle()`, 
`CommandLine.setResourceBundle(ResourceBundle)`


Default:
""










  - 





    - 

#### usageHelpWidth


```
public abstract int usageHelpWidth
```

Set the `usage help message width`. The default is 80.

Since:
3.7
See Also:
`CommandLine.Model.UsageMessageSpec.width()`


Default:
80










  - 





    - 

#### usageHelpAutoWidth


```
public abstract boolean usageHelpAutoWidth
```

If `true`, picocli will attempt to detect the terminal width and adjust the usage help message accordingly.
 End users may enable this by setting system property `"picocli.usage.width"` to `AUTO`,
 and may disable this by setting this system property to a numeric value.
 This feature requires Java 7 or greater. The default is `false`

Since:
4.0
See Also:
`CommandLine.Model.UsageMessageSpec.autoWidth()`


Default:
false










  - 





    - 

#### exitCodeOnSuccess


```
public abstract int exitCodeOnSuccess
```

Exit code for successful termination. 0 by default.

Since:
4.0
See Also:
`CommandLine.execute(String...)`


Default:
0










  - 





    - 

#### exitCodeOnUsageHelp


```
public abstract int exitCodeOnUsageHelp
```

Exit code for successful termination after printing usage help on user request. 0 by default.

Since:
4.0
See Also:
`CommandLine.execute(String...)`


Default:
0










  - 





    - 

#### exitCodeOnVersionHelp


```
public abstract int exitCodeOnVersionHelp
```

Exit code for successful termination after printing version help on user request. 0 by default.

Since:
4.0
See Also:
`CommandLine.execute(String...)`


Default:
0










  - 





    - 

#### exitCodeOnInvalidInput


```
public abstract int exitCodeOnInvalidInput
```

Exit code for command line usage error. 2 by default.

Since:
4.0
See Also:
`CommandLine.execute(String...)`


Default:
2










  - 





    - 

#### exitCodeOnExecutionException


```
public abstract int exitCodeOnExecutionException
```

Exit code signifying that an exception occurred when invoking the Runnable, Callable or Method user object of a command.
 1 by default.

Since:
4.0
See Also:
`CommandLine.execute(String...)`


Default:
1










  - 





    - 

#### exitCodeListHeading


```
public abstract String exitCodeListHeading
```

Set the heading preceding the exit codes section, may contain `"%n"` line separators. `""` (empty string) by default.

Since:
4.0
See Also:
`CommandLine.Help.exitCodeListHeading(Object...)`


Default:
""










  - 





    - 

#### exitCodeList


```
public abstract String[] exitCodeList
```

Set the values to be displayed in the exit codes section as a list of `"key:value"` pairs:
  keys are exit codes, values are descriptions. Descriptions may contain `"%n"` line separators.
 

For example:
 

```

 @Command(exitCodeListHeading = "Exit Codes:%n",
          exitCodeList = { " 0:Successful program execution.",
                           "64:Invalid input: an unknown option or invalid parameter was specified.",
                           "70:Execution exception: an exception occurred while executing the business logic."})
 
```


Since:
4.0


Default:
{}










  - 





    - 

#### scope


```
public abstract CommandLine.ScopeType scope
```

Returns whether subcommands inherit their attributes from this parent command.

Since:
4.6


Default:
picocli.CommandLine.ScopeType.LOCAL










  - 





    - 

#### modelTransformer


```
public abstract Class<? extends CommandLine.IModelTransformer> modelTransformer
```

Returns the model transformer for this command.

Since:
4.6


Default:
picocli.CommandLine.NoOpModelTransformer.class










  - 





    - 

#### preprocessor


```
public abstract Class<? extends CommandLine.IParameterPreprocessor> preprocessor
```

Returns the preprocessor for this command.

Since:
4.6
See Also:
`CommandLine.IParameterPreprocessor`


Default:
picocli.CommandLine.NoOpParameterPreprocessor.class

















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

- Field | 

- Required | 

- Optional





- Detail: 

- Field | 

- Element