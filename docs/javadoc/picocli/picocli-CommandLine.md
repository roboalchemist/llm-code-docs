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

## Class CommandLine






- java.lang.Object

- 



  - picocli.CommandLine









- 

---




```
public class CommandLine
extends Object
```



 CommandLine interpreter that uses reflection to initialize an annotated user object with values obtained from the
 command line arguments.
 


 The full user manual is hosted at https://picocli.info.
 
## Example

 


 An example that implements `Callable` and uses the `CommandLine.execute` convenience API to run in a single line of code:
 
 

```

 @Command(name = "checksum", mixinStandardHelpOptions = true, version = "checksum 4.0",
          description = "Prints the checksum (SHA-1 by default) of a file to STDOUT.")
 class CheckSum implements Callable<Integer> {

     @Parameters(index = "0", description = "The file whose checksum to calculate.")
     private File file;

     @Option(names = {"-a", "--algorithm"}, description = "MD5, SHA-1, SHA-256, ...")
     private String algorithm = "SHA-1";

     @Override
     public Integer call() throws Exception { // your business logic goes here...
         byte[] fileContents = Files.readAllBytes(file.toPath());
         byte[] digest = MessageDigest.getInstance(algorithm).digest(fileContents);
         System.out.printf("%0" + (digest.length*2) + "x%n", new BigInteger(1,digest));
         return 0;
     }

     // CheckSum implements Callable, so parsing, error handling and handling user
     // requests for usage help or version help can be done with one line of code.
     public static void main(String[] args) {
         int exitCode = new CommandLine(new CheckSum()).execute(args);
         System.exit(exitCode);
     }
 }
 
```

 

Another example where the application calls `parseArgs` and takes responsibility
 for error handling and checking whether the user requested help:
 

```
import static picocli.CommandLine.*;

 @Command(mixinStandardHelpOptions = true, version = "v3.0.0",
         header = "Encrypt FILE(s), or standard input, to standard output or to the output file.")
 public class Encrypt {

     @Parameters(description = "Any number of input files")
     private List<File> files = new ArrayList<File>();

     @Option(names = { "-o", "--out" }, description = "Output file (default: print to console)")
     private File outputFile;

     @Option(names = { "-v", "--verbose"}, description = "Verbose mode. Helpful for troubleshooting. Multiple -v options increase the verbosity.")
     private boolean[] verbose;
 }
 
```

 


 Use `CommandLine` to initialize a user object as follows:
 

```

 public static void main(String... args) {
     Encrypt encrypt = new Encrypt();
     try {
         ParseResult parseResult = new CommandLine(encrypt).parseArgs(args);
         if (!CommandLine.printHelpIfRequested(parseResult)) {
             runProgram(encrypt);
         }
     } catch (ParameterException ex) { // command line arguments could not be parsed
         System.err.println(ex.getMessage());
         ex.getCommandLine().usage(System.err);
     }
 }
 
```


 Invoke the above program with some command line arguments. The below are all equivalent:
 
 

```

 --verbose --out=outfile in1 in2
 --verbose --out outfile in1 in2
 -v --out=outfile in1 in2
 -v -o outfile in1 in2
 -v -o=outfile in1 in2
 -vo outfile in1 in2
 -vo=outfile in1 in2
 -v -ooutfile in1 in2
 -vooutfile in1 in2
 
```

 
## Classes and Interfaces for Defining a CommandSpec Model

 


 
 
 
## Classes Related to Parsing Command Line Arguments

 


 
 








- 




  - 



### Nested Class Summary


Nested Classes 

Modifier and Type
Class and Description


`static class `
`CommandLine.AbstractHandler<R,T extends CommandLine.AbstractHandler<R,T>>`
Deprecated. 
see `execute(String...)`




`static class `
`CommandLine.AbstractParseResultHandler<R>`
Deprecated. 
see `execute(String...)`, `getExecutionStrategy()`, `getParameterExceptionHandler()`, `getExecutionExceptionHandler()`




`static interface `
`CommandLine.ArgGroup`
A `Command` may define one or more `ArgGroups`: a group of options, positional parameters or a mixture of the two.



`static interface `
`CommandLine.Command`
Annotate your class with `@Command` when you want more control over the format of the generated help
 message.



`static class `
`CommandLine.DefaultExceptionHandler<R>`
Deprecated. 
see `execute(String...)`, `getParameterExceptionHandler()` and `getExecutionExceptionHandler()`




`static class `
`CommandLine.DuplicateNameException`
Exception indicating that multiple named elements have incorrectly used the same name.



`static class `
`CommandLine.DuplicateOptionAnnotationsException`
Exception indicating that multiple fields have been annotated with the same Option name.



`static class `
`CommandLine.ExecutionException`
Exception indicating a problem while invoking a command or subcommand.



`static class `
`CommandLine.ExitCode`
Defines some exit codes used by picocli as default return values from the `execute`
 and `executeHelpRequest` methods.



`static class `
`CommandLine.Help`
A collection of methods and inner classes that provide fine-grained control over the contents and layout of
 the usage help message to display to end users when help is requested or invalid input values were specified.



`static class `
`CommandLine.HelpCommand`
Help command that can be installed as a subcommand on all application commands.



`static interface `
`CommandLine.IDefaultValueProvider`
Provides default value for a command.



`static interface `
`CommandLine.IExceptionHandler`
Deprecated. 
see `execute(String...)`, `CommandLine.IParameterExceptionHandler` and `CommandLine.IExecutionExceptionHandler`




`static interface `
`CommandLine.IExceptionHandler2<R>`
Deprecated. 
see `execute(String...)`, `CommandLine.IParameterExceptionHandler` and `CommandLine.IExecutionExceptionHandler`




`static interface `
`CommandLine.IExecutionExceptionHandler`
Classes implementing this interface know how to handle Exceptions that occurred while executing the `Runnable`, `Callable` or `Method` user object of the command.



`static interface `
`CommandLine.IExecutionStrategy`
Implementations are responsible for "executing" the user input and returning an exit code.



`static interface `
`CommandLine.IExitCodeExceptionMapper`
Interface that provides the appropriate exit code that will be returned from the `execute`
 method for an exception that occurred during parsing or while invoking the command's Runnable, Callable, or Method.



`static interface `
`CommandLine.IExitCodeGenerator`
`@Command`-annotated classes can implement this interface to specify an exit code that will be returned
 from the `execute` method when the command is successfully invoked.



`static interface `
`CommandLine.IFactory`
Factory for instantiating classes that are registered declaratively with annotation attributes, like
 `CommandLine.Command.subcommands()`, `CommandLine.Option.converter()`, `CommandLine.Parameters.converter()` and `CommandLine.Command.versionProvider()`.



`static interface `
`CommandLine.IHelpCommandInitializable`
Deprecated. 
use `CommandLine.IHelpCommandInitializable2` instead




`static interface `
`CommandLine.IHelpCommandInitializable2`
Help commands that provide usage help for other commands can implement this interface to be initialized with the information they need.



`static interface `
`CommandLine.IHelpFactory`
Creates the `CommandLine.Help` instance used to render the usage help message.



`static interface `
`CommandLine.IHelpSectionRenderer`
Renders a section of the usage help message.



`static interface `
`CommandLine.IModelTransformer`
Provides a way to modify how the command model is built.



`static interface `
`CommandLine.INegatableOptionTransformer`
Determines the option name transformation of negatable boolean options.



`static class `
`CommandLine.InitializationException`
Exception indicating a problem during `CommandLine` initialization.



`static interface `
`CommandLine.IParameterConsumer`
Options or positional parameters can be assigned a `IParameterConsumer` that implements
 custom logic to process the parameters for this option or this position.



`static interface `
`CommandLine.IParameterExceptionHandler`
Classes implementing this interface know how to handle `ParameterExceptions` (usually from invalid user input).



`static interface `
`CommandLine.IParameterPreprocessor`
Options, positional parameters and commands can be assigned a `IParameterPreprocessor` that
 implements custom logic to preprocess the parameters for this option, position or command.



`static interface `
`CommandLine.IParseResultHandler`
Deprecated. 
Use `CommandLine.IExecutionStrategy` instead.




`static interface `
`CommandLine.IParseResultHandler2<R>`
Deprecated. 
use `CommandLine.IExecutionStrategy` instead, see `execute(String...)`




`static interface `
`CommandLine.ITypeConverter<K>`

 When parsing command line arguments and initializing
 fields annotated with `@Option` or `@Parameters`,
 String values can be converted to any type for which a `ITypeConverter` is registered.



`static interface `
`CommandLine.IVersionProvider`
Provides version information for a command.



`static class `
`CommandLine.MaxValuesExceededException`
Exception indicating that more values were specified for an option or parameter than its `arity` allows.



`static class `
`CommandLine.MissingParameterException`
Exception indicating that a required parameter was not specified.



`static class `
`CommandLine.MissingTypeConverterException`
Exception indicating that an annotated field had a type for which no `CommandLine.ITypeConverter` was
 registered.



`static interface `
`CommandLine.Mixin`

 Fields annotated with `@Mixin` are "expanded" into the current command: `@Option` and
 `@Parameters` in the mixin class are added to the options and positional parameters of this command.



`static class `
`CommandLine.Model`
This class provides a namespace for classes and interfaces that model concepts and attributes of command line interfaces in picocli.



`static class `
`CommandLine.MutuallyExclusiveArgsException`
Exception indicating that the user input included multiple arguments from a mutually exclusive group.



`static interface `
`CommandLine.Option`

 Annotate fields in your class with `@Option` and picocli will initialize these fields when matching
 arguments are specified on the command line.



`static class `
`CommandLine.OverwrittenOptionException`
Exception indicating that an option for a single-value option field has been specified multiple times on the command line.



`static class `
`CommandLine.ParameterException`
Exception indicating something went wrong while parsing command line options.



`static class `
`CommandLine.ParameterIndexGapException`
Exception indicating that there was a gap in the indices of the fields annotated with `CommandLine.Parameters`.



`static interface `
`CommandLine.Parameters`

 Fields annotated with `@Parameters` will be initialized with positional parameters.



`static interface `
`CommandLine.ParentCommand`

 Fields annotated with `@ParentCommand` will be initialized with the parent command of the current subcommand.



`static class `
`CommandLine.ParseResult`
Encapsulates the result of parsing an array of command line arguments.



`static class `
`CommandLine.PicocliException`
Base class of all exceptions thrown by `picocli.CommandLine`.



`static class `
`CommandLine.PropertiesDefaultProvider`
`IDefaultValueProvider` implementation that loads default values for command line
 options and positional parameters from a properties file or `Properties` object.



`static class `
`CommandLine.Range`
Describes the number of parameters required and accepted by an option or a positional parameter.



`static class `
`CommandLine.RegexTransformer`
A regular expression-based option name transformation for negatable options.



`static class `
`CommandLine.RunAll`
Command line execution strategy that prints help if requested, and otherwise executes the top-level command and
 all subcommands as `Runnable`, `Callable` or `Method`.



`static class `
`CommandLine.RunFirst`
Command line execution strategy that prints help if requested, and otherwise executes the top-level
 `Runnable` or `Callable` command.



`static class `
`CommandLine.RunLast`
Command line execution strategy that prints help if requested, and otherwise executes the most specific
 `Runnable` or `Callable` subcommand.



`static class `
`CommandLine.ScopeType`
Specifies the scope of the element.



`static interface `
`CommandLine.Spec`
Fields annotated with `@Spec` will be initialized with the `CommandSpec` for the command the field is part of.



`static class `
`CommandLine.TraceLevel`
Enumerates over the trace level values for filtering which internal debug statements should be printed.



`static class `
`CommandLine.Tracer`
Utility class for printing internal debug statements.



`static class `
`CommandLine.TypeConversionException`
Exception thrown by `CommandLine.ITypeConverter` implementations to indicate a String could not be converted.



`static interface `
`CommandLine.Unmatched`
Fields annotated with `@Unmatched` will be initialized with the list of unmatched command line arguments, if any.



`static class `
`CommandLine.UnmatchedArgumentException`
Exception indicating that a command line argument could not be mapped to any of the fields annotated with
 `CommandLine.Option` or `CommandLine.Parameters`.



`static class `
`CommandLine.UseDefaultConverter`
Converter that can be used to signal to picocli that it should use the default converter.










  - 



### Field Summary


Fields 

Modifier and Type
Field and Description


`static String`
`VERSION`
This is picocli version "4.7.7".










  - 



### Constructor Summary


Constructors 

Constructor and Description


`CommandLine(Object command)`
Constructs a new `CommandLine` interpreter with the specified object (which may be an annotated user object or a `CommandSpec`) and a default factory.



`CommandLine(Object command,
           CommandLine.IFactory factory)`
Constructs a new `CommandLine` interpreter with the specified object (which may be an annotated user object or a `CommandSpec`) and object factory.










  - 



### Method Summary


All Methods Static Methods Instance Methods Concrete Methods Deprecated Methods 

Modifier and Type
Method and Description


`CommandLine`
`addMixin(String name,
        Object mixin)`
Adds the options and positional parameters in the specified mixin to this command.



`CommandLine`
`addSubcommand(Object command)`
Registers a subcommand with the name obtained from the `@Command(name = "...")` annotation attribute of the specified command.



`CommandLine`
`addSubcommand(String name,
             Object command)`
Registers a subcommand with the specified name.



`CommandLine`
`addSubcommand(String name,
             Object command,
             String... aliases)`
Registers a subcommand with the specified name and all specified aliases.



`static <C extends Callable<T>,T>
T`
`call(Class<C> callableClass,
    CommandLine.IFactory factory,
    PrintStream out,
    CommandLine.Help.Ansi ansi,
    String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`static <C extends Callable<T>,T>
T`
`call(Class<C> callableClass,
    CommandLine.IFactory factory,
    PrintStream out,
    PrintStream err,
    CommandLine.Help.Ansi ansi,
    String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`static <C extends Callable<T>,T>
T`
`call(Class<C> callableClass,
    CommandLine.IFactory factory,
    PrintStream out,
    String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`static <C extends Callable<T>,T>
T`
`call(Class<C> callableClass,
    CommandLine.IFactory factory,
    String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`static <C extends Callable<T>,T>
T`
`call(C callable,
    PrintStream out,
    CommandLine.Help.Ansi ansi,
    String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`static <C extends Callable<T>,T>
T`
`call(C callable,
    PrintStream out,
    PrintStream err,
    CommandLine.Help.Ansi ansi,
    String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`static <C extends Callable<T>,T>
T`
`call(C callable,
    PrintStream out,
    String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`static <C extends Callable<T>,T>
T`
`call(C callable,
    String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`void`
`clearExecutionResults()`
Clears the execution result of a previous invocation from this `CommandLine` and all subcommands.



`static CommandLine.DefaultExceptionHandler<List<Object>>`
`defaultExceptionHandler()`
Convenience method that returns `new DefaultExceptionHandler<List<Object>>()`.



`static CommandLine.IFactory`
`defaultFactory()`
Returns the default `CommandLine.IFactory` implementation used if no factory was specified in the `CommandLine constructor`.



`int`
`execute(String... args)`
Convenience method to allow command line application authors to avoid some boilerplate code in their application.



`static Integer`
`executeHelpRequest(CommandLine.ParseResult parseResult)`
Helper method that may be useful when processing the `ParseResult` that results from successfully
 parsing command line arguments.



`Character`
`getAtFileCommentChar()`
Returns the character that starts a single-line comment or `null` if all content of argument files should
 be interpreted as arguments (without comments).



`CommandLine.Help.ColorScheme`
`getColorScheme()`
Returns the color scheme to use when printing help.



`<T> T`
`getCommand()`
Returns the annotated user object that this `CommandLine` instance was constructed with.



`static List<Method>`
`getCommandMethods(Class<?> cls,
                 String methodName)`
Helper to get methods of a class annotated with `@Command` via reflection, optionally filtered by method name (not `@Command.name`).



`String`
`getCommandName()`
Returns the command name (also called program name) displayed in the usage help synopsis.



`CommandLine.Model.CommandSpec`
`getCommandSpec()`
Returns the `CommandSpec` model that this `CommandLine` was constructed with.



`CommandLine.IDefaultValueProvider`
`getDefaultValueProvider()`
Returns the default value provider for the command, or `null` if none has been set.



`String`
`getEndOfOptionsDelimiter()`
Returns the end-of-options delimiter that signals that the remaining command line arguments should be treated as positional parameters.



`PrintWriter`
`getErr()`
Returns the writer to use when printing diagnostic (error) messages during command execution.



`CommandLine.IExecutionExceptionHandler`
`getExecutionExceptionHandler()`
Returns the handler for dealing with exceptions that occurred in the `Callable`, `Runnable` or `Method`
 user object of a command when the command was executed.



`<T> T`
`getExecutionResult()`
Returns the result of calling the user object `Callable` or invoking the user object `Method`
 after parsing the user input, or `null` if this command has not been executed
 or if this `CommandLine` is for a subcommand that was not specified by the end user on the command line.



`CommandLine.IExecutionStrategy`
`getExecutionStrategy()`
Returns the execution strategy used by the `execute` method to invoke
 the business logic on the user objects of this command and/or the user-specified subcommand(s).



`CommandLine.IExitCodeExceptionMapper`
`getExitCodeExceptionMapper()`
Returns the mapper that was set by the application to map from exceptions to exit codes, for use by the `execute` method.



`CommandLine.IFactory`
`getFactory()`
Returns the factory that this `CommandLine` was constructed with.



`CommandLine.Help`
`getHelp()`
Returns a new `Help` object created by the `IHelpFactory` with the `CommandSpec` and `ColorScheme` of this command.



`CommandLine.IHelpFactory`
`getHelpFactory()`
Returns the `IHelpFactory` that is used to construct the usage help message.



`List<String>`
`getHelpSectionKeys()`
Returns the section keys in the order that the usage help message should render the sections.



`Map<String,CommandLine.IHelpSectionRenderer>`
`getHelpSectionMap()`
Returns the map of section keys and renderers used to construct the usage help message.



`Map<String,Object>`
`getMixins()`
Returns a map of user objects whose options and positional parameters were added to ("mixed in" with) this command.



`CommandLine.INegatableOptionTransformer`
`getNegatableOptionTransformer()`
Returns the `INegatableOptionTransformer` used to create the negative form of negatable options.



`PrintWriter`
`getOut()`
Returns the writer used when printing user-requested usage help or version help during command execution.



`CommandLine.IParameterExceptionHandler`
`getParameterExceptionHandler()`
Returns the handler for dealing with invalid user input when the command is executed.



`CommandLine`
`getParent()`
Returns the command that this is a subcommand of, or `null` if this is a top-level command.



`CommandLine.ParseResult`
`getParseResult()` 


`ResourceBundle`
`getResourceBundle()`
Returns the ResourceBundle of this command or `null` if no resource bundle is set.



`String`
`getSeparator()`
Returns the String that separates option names from option values when parsing command line options.



`Map<String,CommandLine>`
`getSubcommands()`
Returns a map with the subcommands registered on this instance.



`List<String>`
`getUnmatchedArguments()`
Returns the list of unmatched command line arguments, if any.



`int`
`getUsageHelpLongOptionsMaxWidth()`
Returns the maximum usage help long options column max width to the specified value.



`int`
`getUsageHelpWidth()`
Returns the maximum width of the usage help message.



`String`
`getUsageMessage()`
Similar to `usage(PrintStream)`, but returns the usage help message as a String instead of printing it to the `PrintStream`.



`String`
`getUsageMessage(CommandLine.Help.Ansi ansi)`
Similar to `usage(PrintStream, Help.Ansi)`, but returns the usage help message as a String instead of printing it to the `PrintStream`.



`String`
`getUsageMessage(CommandLine.Help.ColorScheme colorScheme)`
Similar to `usage(PrintStream, Help.ColorScheme)`, but returns the usage help message as a String instead of printing it to the `PrintStream`.



`static Object`
`invoke(String methodName,
      Class<?> cls,
      PrintStream out,
      CommandLine.Help.Ansi ansi,
      String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`static Object`
`invoke(String methodName,
      Class<?> cls,
      PrintStream out,
      PrintStream err,
      CommandLine.Help.Ansi ansi,
      String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`static Object`
`invoke(String methodName,
      Class<?> cls,
      PrintStream out,
      String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`static Object`
`invoke(String methodName,
      Class<?> cls,
      String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`boolean`
`isAbbreviatedOptionsAllowed()`
Returns whether abbreviation of option names should be allowed when matching options.



`boolean`
`isAbbreviatedSubcommandsAllowed()`
Returns whether abbreviation of subcommands should be allowed when matching subcommands.



`boolean`
`isAdjustLineBreaksForWideCJKCharacters()`
Returns whether line breaks should take wide Chinese, Japanese and Korean characters into account for line-breaking purposes.



`boolean`
`isAllowOptionsAsOptionParameters()`
Returns whether options can have parameter values that match the name of an option in this command,
 or whether such values should be rejected with a missing parameter exception.



`boolean`
`isAllowSubcommandsAsOptionParameters()`
Returns whether options can have parameter values that match subcommand names or aliases,
 or whether such values should be rejected with a missing parameter exception.



`boolean`
`isCaseInsensitiveEnumValuesAllowed()`
Returns whether the parser should ignore case when converting arguments to `enum` values.



`boolean`
`isExpandAtFiles()`
Returns whether arguments starting with `'@'` should be treated as the path to an argument file and its
 contents should be expanded into separate arguments for each line in the specified file.



`boolean`
`isInterpolateVariables()`
Returns whether variables should be interpolated in String values.



`boolean`
`isOptionsCaseInsensitive()`
Returns whether upper case and lower case should be ignored when matching option names.



`boolean`
`isOverwrittenOptionsAllowed()`
Returns whether options for single-value fields can be specified multiple times on the command line.



`boolean`
`isPosixClusteredShortOptionsAllowed()`
Returns whether the parser accepts clustered short options.



`boolean`
`isSplitQuotedStrings()`
Deprecated. 
Most applications should not change the default. The rare application that *does* need to split parameter values
 without respecting quotes should use `CommandLine.Model.ParserSpec.splitQuotedStrings(boolean)`.




`boolean`
`isStopAtPositional()`
Returns whether the parser interprets the first positional parameter as "end of options" so the remaining
 arguments are all treated as positional parameters.



`boolean`
`isStopAtUnmatched()`
Returns whether the parser should stop interpreting options and positional parameters as soon as it encounters an
 unmatched option.



`boolean`
`isSubcommandsCaseInsensitive()`
Returns whether upper case and lower case should be ignored when matching subcommands.



`boolean`
`isToggleBooleanFlags()`
Returns whether the value of boolean flag options should be "toggled" when the option is matched.



`boolean`
`isTrimQuotes()`
Returns whether the parser should trim quotes from command line arguments.



`boolean`
`isUnmatchedArgumentsAllowed()`
Returns whether the end user may specify arguments on the command line that are not matched to any option or parameter fields.



`boolean`
`isUnmatchedOptionsAllowedAsOptionParameters()`
Returns whether options can have parameter values that resemble an option, or whether such values should be rejected as unknown options.



`boolean`
`isUnmatchedOptionsArePositionalParams()`
Returns whether arguments on the command line that resemble an option should be treated as positional parameters.



`boolean`
`isUsageHelpAutoWidth()`
Returns whether picocli should attempt to detect the terminal size and adjust the usage help message width
 to take the full terminal width.



`boolean`
`isUsageHelpRequested()`
Returns `true` if an option annotated with `CommandLine.Option.usageHelp()` was specified on the command line.



`boolean`
`isUseSimplifiedAtFiles()`
Returns whether to use a simplified argument file format that is compatible with JCommander.



`boolean`
`isVersionHelpRequested()`
Returns `true` if an option annotated with `CommandLine.Option.versionHelp()` was specified on the command line.



`List<CommandLine>`
`parse(String... args)`
Deprecated. 
use `parseArgs(String...)` instead




`CommandLine.ParseResult`
`parseArgs(String... args)`
Expands any @-files in the specified command line arguments, then
 parses the arguments and returns a `ParseResult` with the options, positional
 parameters, and subcommands (if any) that were recognized and initialized during the parsing process.



`<R> R`
`parseWithHandler(CommandLine.IParseResultHandler2<R> handler,
                String[] args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`List<Object>`
`parseWithHandler(CommandLine.IParseResultHandler handler,
                PrintStream out,
                String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`<R> R`
`parseWithHandlers(CommandLine.IParseResultHandler2<R> handler,
                 CommandLine.IExceptionHandler2<R> exceptionHandler,
                 String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`List<Object>`
`parseWithHandlers(CommandLine.IParseResultHandler handler,
                 PrintStream out,
                 CommandLine.Help.Ansi ansi,
                 CommandLine.IExceptionHandler exceptionHandler,
                 String... args)`
Deprecated. 
use `execute(String...)` and `getExecutionResult()` instead




`static <T> T`
`populateCommand(T command,
               String... args)`

 Convenience method that initializes the specified annotated object from the specified command line arguments.



`static <T> T`
`populateSpec(Class<T> spec,
            String... args)`

 Convenience method that derives the command specification from the specified interface class, and returns an
 instance of the specified interface.



`static boolean`
`printHelpIfRequested(CommandLine.ParseResult parseResult)`
Delegates to `executeHelpRequest(ParseResult)`.



`static boolean`
`printHelpIfRequested(List<CommandLine> parsedCommands,
                    PrintStream out,
                    CommandLine.Help.Ansi ansi)`
Deprecated. 
use `printHelpIfRequested(ParseResult)` instead




`static boolean`
`printHelpIfRequested(List<CommandLine> parsedCommands,
                    PrintStream out,
                    PrintStream err,
                    CommandLine.Help.Ansi ansi)`
Deprecated. 
use `executeHelpRequest(ParseResult)` instead




`static boolean`
`printHelpIfRequested(List<CommandLine> parsedCommands,
                    PrintStream out,
                    PrintStream err,
                    CommandLine.Help.ColorScheme colorScheme)`
Deprecated. 
use `executeHelpRequest(ParseResult)` instead




`void`
`printVersionHelp(PrintStream out)`
Delegates to `printVersionHelp(PrintStream, Help.Ansi)` with the ANSI setting of the configured color scheme.



`void`
`printVersionHelp(PrintStream out,
                CommandLine.Help.Ansi ansi)`
Prints version information from the `CommandLine.Command.version()` annotation to the specified `PrintStream`.



`void`
`printVersionHelp(PrintStream out,
                CommandLine.Help.Ansi ansi,
                Object... params)`
Prints version information from the `CommandLine.Command.version()` annotation to the specified `PrintStream`.



`void`
`printVersionHelp(PrintWriter out)`
Delegates to `printVersionHelp(PrintWriter, Help.Ansi, Object...)` with the ANSI setting of the configured color scheme.



`void`
`printVersionHelp(PrintWriter out,
                CommandLine.Help.Ansi ansi,
                Object... params)`
Prints version information from the `CommandLine.Command.version()` annotation to the specified `PrintWriter`.



`<K> CommandLine`
`registerConverter(Class<K> cls,
                 CommandLine.ITypeConverter<K> converter)`
Registers the specified type converter for the specified class.



`static <R extends Runnable>
void`
`run(Class<R> runnableClass,
   CommandLine.IFactory factory,
   PrintStream out,
   CommandLine.Help.Ansi ansi,
   String... args)`
Deprecated. 
use `execute(String...)` instead




`static <R extends Runnable>
void`
`run(Class<R> runnableClass,
   CommandLine.IFactory factory,
   PrintStream out,
   PrintStream err,
   CommandLine.Help.Ansi ansi,
   String... args)`
Deprecated. 
use `execute(String...)` instead




`static <R extends Runnable>
void`
`run(Class<R> runnableClass,
   CommandLine.IFactory factory,
   PrintStream out,
   String... args)`
Deprecated. 
use `execute(String...)` instead




`static <R extends Runnable>
void`
`run(Class<R> runnableClass,
   CommandLine.IFactory factory,
   String... args)`
Deprecated. 
use `execute(String...)` instead




`static <R extends Runnable>
void`
`run(R runnable,
   PrintStream out,
   CommandLine.Help.Ansi ansi,
   String... args)`
Deprecated. 
use `execute(String...)` instead




`static <R extends Runnable>
void`
`run(R runnable,
   PrintStream out,
   PrintStream err,
   CommandLine.Help.Ansi ansi,
   String... args)`
Deprecated. 
use `execute(String...)` instead




`static <R extends Runnable>
void`
`run(R runnable,
   PrintStream out,
   String... args)`
Deprecated. 
use `execute(String...)` instead




`static <R extends Runnable>
void`
`run(R runnable,
   String... args)`
Deprecated. 
use `execute(String...)` instead




`CommandLine`
`setAbbreviatedOptionsAllowed(boolean newValue)`
Sets whether abbreviated option names should be matched.



`CommandLine`
`setAbbreviatedSubcommandsAllowed(boolean newValue)`
Sets whether abbreviated subcommands should be matched.



`CommandLine`
`setAdjustLineBreaksForWideCJKCharacters(boolean adjustForWideChars)`
Sets whether line breaks should take wide Chinese, Japanese and Korean characters into account, and returns this UsageMessageSpec.



`CommandLine`
`setAllowOptionsAsOptionParameters(boolean newValue)`
Sets whether options can have parameter values that match the name of an option in this command, or whether such values should be rejected with a missing parameter exception.



`CommandLine`
`setAllowSubcommandsAsOptionParameters(boolean newValue)`
Sets whether options can have parameter values that match subcommand names or aliases, or whether such values should be rejected with a missing parameter exception.



`CommandLine`
`setAtFileCommentChar(Character atFileCommentChar)`
Sets the character that starts a single-line comment or `null` if all content of argument files should
 be interpreted as arguments (without comments).



`CommandLine`
`setCaseInsensitiveEnumValuesAllowed(boolean newValue)`
Sets whether the parser should ignore case when converting arguments to `enum` values.



`CommandLine`
`setColorScheme(CommandLine.Help.ColorScheme colorScheme)`
Sets the color scheme to use when printing help.



`CommandLine`
`setCommandName(String commandName)`
Sets the command name (also called program name) displayed in the usage help synopsis to the specified value.



`CommandLine`
`setDefaultValueProvider(CommandLine.IDefaultValueProvider newValue)`
Sets a default value provider for the command and sub-commands



`CommandLine`
`setEndOfOptionsDelimiter(String delimiter)`
Sets the end-of-options delimiter that signals that the remaining command line arguments should be treated as positional parameters.



`CommandLine`
`setErr(PrintWriter err)`
Sets the writer to use when printing diagnostic (error) messages during command execution.



`CommandLine`
`setExecutionExceptionHandler(CommandLine.IExecutionExceptionHandler executionExceptionHandler)`
Sets a custom handler for dealing with exceptions that occurred in the `Callable`, `Runnable` or `Method`
 user object of a command when the command was executed via the execute method.



`void`
`setExecutionResult(Object result)`
Sets the result of calling the business logic on the command's user object.



`CommandLine`
`setExecutionStrategy(CommandLine.IExecutionStrategy executionStrategy)`
Sets the execution strategy that the `execute` method should use to invoke
 the business logic on the user objects of this command and/or the user-specified subcommand(s).



`CommandLine`
`setExitCodeExceptionMapper(CommandLine.IExitCodeExceptionMapper exitCodeExceptionMapper)`
Sets the mapper used by the `execute` method to map exceptions to exit codes.



`CommandLine`
`setExpandAtFiles(boolean expandAtFiles)`
Sets whether arguments starting with `'@'` should be treated as the path to an argument file and its
 contents should be expanded into separate arguments for each line in the specified file.



`CommandLine`
`setHelpFactory(CommandLine.IHelpFactory helpFactory)`
Sets a new `IHelpFactory` to customize the usage help message.



`CommandLine`
`setHelpSectionKeys(List<String> keys)`
Sets the section keys in the order that the usage help message should render the sections.



`CommandLine`
`setHelpSectionMap(Map<String,CommandLine.IHelpSectionRenderer> map)`
Sets the map of section keys and renderers used to construct the usage help message.



`CommandLine`
`setInterpolateVariables(boolean interpolate)`
Sets whether variables should be interpolated in String values.



`CommandLine`
`setNegatableOptionTransformer(CommandLine.INegatableOptionTransformer transformer)`
Sets the `INegatableOptionTransformer` used to create the negative form of negatable options.



`CommandLine`
`setOptionsCaseInsensitive(boolean newValue)`
Sets whether upper case and lower case should be ignored when matching option names.



`CommandLine`
`setOut(PrintWriter out)`
Sets the writer to use when printing user-requested usage help or version help during command execution.



`CommandLine`
`setOverwrittenOptionsAllowed(boolean newValue)`
Sets whether options for single-value fields can be specified multiple times on the command line without a `CommandLine.OverwrittenOptionException` being thrown.



`CommandLine`
`setParameterExceptionHandler(CommandLine.IParameterExceptionHandler parameterExceptionHandler)`
Sets the handler for dealing with invalid user input when the command is executed.



`CommandLine`
`setPosixClusteredShortOptionsAllowed(boolean newValue)`
Sets whether short options like `-x -v -f SomeFile` can be clustered together like `-xvfSomeFile`.



`CommandLine`
`setResourceBundle(ResourceBundle bundle)`
Sets the ResourceBundle containing usage help message strings.



`CommandLine`
`setSeparator(String separator)`
Sets the String the parser uses to separate option names from option values to the specified value.



`CommandLine`
`setSplitQuotedStrings(boolean newValue)`
Deprecated. 
Most applications should not change the default. The rare application that *does* need to split parameter values
 without respecting quotes should use `CommandLine.Model.ParserSpec.splitQuotedStrings(boolean)`.




`CommandLine`
`setStopAtPositional(boolean newValue)`
Sets whether the parser interprets the first positional parameter as "end of options" so the remaining
 arguments are all treated as positional parameters.



`CommandLine`
`setStopAtUnmatched(boolean newValue)`
Sets whether the parser should stop interpreting options and positional parameters as soon as it encounters an
 unmatched option.



`CommandLine`
`setSubcommandsCaseInsensitive(boolean newValue)`
Sets whether upper case and lower case should be ignored when matching subcommands.



`CommandLine`
`setToggleBooleanFlags(boolean newValue)`
Sets whether the value of boolean flag options should be "toggled" when the option is matched.



`CommandLine`
`setTrimQuotes(boolean newValue)`
Sets whether the parser should trim quotes from command line arguments before processing them.



`CommandLine`
`setUnmatchedArgumentsAllowed(boolean newValue)`
Sets whether the end user may specify unmatched arguments on the command line without a `CommandLine.UnmatchedArgumentException` being thrown.



`CommandLine`
`setUnmatchedOptionsAllowedAsOptionParameters(boolean newValue)`
Sets whether options can have parameter values that resemble an option, or whether such values should be rejected as unknown options.



`CommandLine`
`setUnmatchedOptionsArePositionalParams(boolean newValue)`
Sets whether arguments on the command line that resemble an option should be treated as positional parameters.



`CommandLine`
`setUsageHelpAutoWidth(boolean detectTerminalSize)`
Sets whether picocli should attempt to detect the terminal size and adjust the usage help message width
 to take the full terminal width.



`CommandLine`
`setUsageHelpLongOptionsMaxWidth(int columnWidth)`
Returns the maximum usage help long options column max width to the specified value.



`CommandLine`
`setUsageHelpWidth(int width)`
Sets the maximum width of the usage help message.



`CommandLine`
`setUseSimplifiedAtFiles(boolean simplifiedAtFiles)`
Sets whether to use a simplified argument file format that is compatible with JCommander.



`static CommandLine.Tracer`
`tracer()`
Returns the `Tracer` used internally for printing internal debug statements.



`static void`
`usage(Object command,
     PrintStream out)`
Equivalent to `new CommandLine(command).usage(out)`.



`static void`
`usage(Object command,
     PrintStream out,
     CommandLine.Help.Ansi ansi)`
Equivalent to `new CommandLine(command).usage(out, ansi)`.



`static void`
`usage(Object command,
     PrintStream out,
     CommandLine.Help.ColorScheme colorScheme)`
Equivalent to `new CommandLine(command).usage(out, colorScheme)`.



`void`
`usage(PrintStream out)`
Delegates to `usage(PrintStream, Help.ColorScheme)` with the configured color scheme.



`void`
`usage(PrintStream out,
     CommandLine.Help.Ansi ansi)`
Delegates to `usage(PrintStream, Help.ColorScheme)` with the default color scheme.



`void`
`usage(PrintStream out,
     CommandLine.Help.ColorScheme colorScheme)`
Prints a usage help message for the annotated command class to the specified `PrintStream`.



`void`
`usage(PrintWriter writer)`
Delegates to `usage(PrintWriter, Help.ColorScheme)` with the configured color scheme.



`void`
`usage(PrintWriter writer,
     CommandLine.Help.Ansi ansi)`
Similar to `usage(PrintStream, Help.Ansi)` but with the specified `PrintWriter` instead of a `PrintStream`.



`void`
`usage(PrintWriter writer,
     CommandLine.Help.ColorScheme colorScheme)`
Similar to `usage(PrintStream, Help.ColorScheme)`, but with the specified `PrintWriter` instead of a `PrintStream`.






    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`













- 




  - 



### Field Detail







    - 

#### VERSION


```
public static final String VERSION
```

This is picocli version "4.7.7".

See Also:
Constant Field Values











  - 



### Constructor Detail







    - 

#### CommandLine


```
public CommandLine(Object command)
```

Constructs a new `CommandLine` interpreter with the specified object (which may be an annotated user object or a `CommandSpec`) and a default factory.
 

The specified object may be a `CommandSpec` object, or it may be a `@Command`-annotated
 user object with `@Option` and `@Parameters`-annotated fields and methods, in which case picocli automatically
 constructs a `CommandSpec` from this user object.
 

 If the specified command object is an interface `Class` with `@Option` and `@Parameters`-annotated methods,
 picocli creates a `Proxy` whose methods return the matched command line values.
 If the specified command object is a concrete `Class`, picocli delegates to the default factory to get an instance.
 


 If the specified object implements `Runnable` or `Callable`, or if it is a `Method` object,
 the command can be run as an application in a single line of code by using the
 `execute` method to omit some boilerplate code for handling help requests and invalid input.
 See `getCommandMethods` for a convenient way to obtain a command `Method`.
 


 When the `parseArgs(String...)` method is called, the `CommandSpec` object will be
 initialized based on command line arguments. If the commandSpec is created from an annotated user object, this
 user object will be initialized based on the command line arguments.
 

Parameters:
`command` - an annotated user object or a `CommandSpec` object to initialize from the command line arguments
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation










    - 

#### CommandLine


```
public CommandLine(Object command,
                   CommandLine.IFactory factory)
```

Constructs a new `CommandLine` interpreter with the specified object (which may be an annotated user object or a `CommandSpec`) and object factory.
 

The specified object may be a `CommandSpec` object, or it may be a `@Command`-annotated
 user object with `@Option` and `@Parameters`-annotated fields and methods, in which case picocli automatically
 constructs a `CommandSpec` from this user object.
 

 If the specified command object is an interface `Class` with `@Option` and `@Parameters`-annotated methods,
 picocli creates a `Proxy` whose methods return the matched command line values.
 If the specified command object is a concrete `Class`, picocli delegates to the factory to get an instance.
 


 If the specified object implements `Runnable` or `Callable`, or if it is a `Method` object,
 the command can be run as an application in a single line of code by using the
 `execute` method to omit some boilerplate code for handling help requests and invalid input.
 See `getCommandMethods` for a convenient way to obtain a command `Method`.
 


 When the `parseArgs(String...)` method is called, the `CommandSpec` object will be
 initialized based on command line arguments. If the commandSpec is created from an annotated user object, this
 user object will be initialized based on the command line arguments.
 

Parameters:
`command` - an annotated user object or a `CommandSpec` object to initialize from the command line arguments
`factory` - the factory used to create instances of subcommands, converters, etc., that are registered declaratively with annotation attributes
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
Since:
2.2











  - 



### Method Detail







    - 

#### getCommandSpec


```
public CommandLine.Model.CommandSpec getCommandSpec()
```

Returns the `CommandSpec` model that this `CommandLine` was constructed with.

Returns:
the `CommandSpec` model
Since:
3.0










    - 

#### addMixin


```
public CommandLine addMixin(String name,
                            Object mixin)
```

Adds the options and positional parameters in the specified mixin to this command.
 

The specified object may be a `CommandSpec` object, or it may be a user object with
 `@Option` and `@Parameters`-annotated fields, in which case picocli automatically
 constructs a `CommandSpec` from this user object.
 

Parameters:
`name` - the name by which the mixin object may later be retrieved
`mixin` - an annotated user object or a `CommandSpec` object whose options and positional parameters to add to this command
Returns:
this CommandLine object, to allow method chaining
Since:
3.0










    - 

#### getMixins


```
public Map<String,Object> getMixins()
```

Returns a map of user objects whose options and positional parameters were added to ("mixed in" with) this command.

Returns:
a new Map containing the user objects mixed in with this command. If `CommandSpec` objects without
          user objects were programmatically added, use the `underlying model` directly.
Since:
3.0










    - 

#### addSubcommand


```
public CommandLine addSubcommand(Object command)
```

Registers a subcommand with the name obtained from the `@Command(name = "...")` annotation attribute of the specified command.

Parameters:
`command` - the object to initialize with command line arguments following the subcommand name.
                This may be a `Class` that has a `@Command` annotation, or an instance of such a
                class, or a `CommandSpec` or `CommandLine` instance with its own (nested) subcommands.
Returns:
this CommandLine object, to allow method chaining
Throws:
`CommandLine.InitializationException` - if no name could be found for the specified subcommand,
          or if another subcommand was already registered under the same name, or if one of the aliases
          of the specified subcommand was already used by another subcommand.
Since:
4.0
See Also:
`addSubcommand(String, Object)`










    - 

#### addSubcommand


```
public CommandLine addSubcommand(String name,
                                 Object command)
```

Registers a subcommand with the specified name. For example:
 

```

 CommandLine commandLine = new CommandLine(new Git())
         .addSubcommand("status",   new GitStatus())
         .addSubcommand("commit",   new GitCommit();
         .addSubcommand("add",      new GitAdd())
         .addSubcommand("branch",   new GitBranch())
         .addSubcommand("checkout", new GitCheckout())
         //...
         ;
 
```


 

The specified object can be an annotated object or a
 `CommandLine` instance with its own nested subcommands. For example:
 

```

 CommandLine commandLine = new CommandLine(new MainCommand())
         .addSubcommand("cmd1",                 new ChildCommand1()) // subcommand
         .addSubcommand("cmd2",                 new ChildCommand2())
         .addSubcommand("cmd3", new CommandLine(new ChildCommand3()) // subcommand with nested sub-subcommands
                 .addSubcommand("cmd3sub1",                 new GrandChild3Command1())
                 .addSubcommand("cmd3sub2",                 new GrandChild3Command2())
                 .addSubcommand("cmd3sub3", new CommandLine(new GrandChild3Command3()) // deeper nesting
                         .addSubcommand("cmd3sub3sub1", new GreatGrandChild3Command3_1())
                         .addSubcommand("cmd3sub3sub2", new GreatGrandChild3Command3_2())
                 )
         );
 
```

 

The default type converters are available on all subcommands and nested sub-subcommands, but custom type
 converters are registered only with the subcommand hierarchy as it existed when the custom type was registered.
 To ensure a custom type converter is available to all subcommands, register the type converter last, after
 adding subcommands.
 

See also the `CommandLine.Command.subcommands()` annotation to register subcommands declaratively.

Parameters:
`name` - the string to recognize on the command line as a subcommand.
             If `null`, the name of the specified subcommand is used;
             if this is also `null`, the first alias is used.
`command` - the object to initialize with command line arguments following the subcommand name.
                This may be a `Class` that has a `@Command` annotation, or an instance of such a
                class, or a `CommandSpec` or `CommandLine` instance with its own (nested) subcommands.
Returns:
this CommandLine object, to allow method chaining
Throws:
`CommandLine.InitializationException` - if the specified name is `null`, and no alternative name could be found,
          or if another subcommand was already registered under the same name, or if one of the aliases
          of the specified subcommand was already used by another subcommand.
Since:
0.9.7
See Also:
`registerConverter(Class, ITypeConverter)`, 
`CommandLine.Command.subcommands()`










    - 

#### addSubcommand


```
public CommandLine addSubcommand(String name,
                                 Object command,
                                 String... aliases)
```

Registers a subcommand with the specified name and all specified aliases. See also `addSubcommand(String, Object)`.

Parameters:
`name` - the string to recognize on the command line as a subcommand.
             If `null`, the name of the specified subcommand is used;
             if this is also `null`, the first alias is used.
`command` - the object to initialize with command line arguments following the subcommand name.
                This may be a `Class` that has a `@Command` annotation, or an instance of such a
                class, or a `CommandSpec` or `CommandLine` instance with its own (nested) subcommands.
`aliases` - zero or more alias names that are also recognized on the command line as this subcommand
Returns:
this CommandLine object, to allow method chaining
Throws:
`CommandLine.InitializationException` - if the specified name is `null`, and no alternative name could be found,
          or if another subcommand was already registered under the same name, or if one of the aliases
          of the specified subcommand was already used by another subcommand.
Since:
3.1
See Also:
`addSubcommand(String, Object)`










    - 

#### getSubcommands


```
public Map<String,CommandLine> getSubcommands()
```

Returns a map with the subcommands registered on this instance.

Returns:
a map with the registered subcommands
Since:
0.9.7










    - 

#### getParent


```
public CommandLine getParent()
```

Returns the command that this is a subcommand of, or `null` if this is a top-level command.

Returns:
the command that this is a subcommand of, or `null` if this is a top-level command
Since:
0.9.8
See Also:
`addSubcommand(String, Object)`, 
`CommandLine.Command.subcommands()`










    - 

#### getCommand


```
public <T> T getCommand()
```

Returns the annotated user object that this `CommandLine` instance was constructed with.

Type Parameters:
`T` - the type of the variable that the return value is being assigned to
Returns:
the annotated object that this `CommandLine` instance was constructed with
Since:
0.9.7










    - 

#### getFactory


```
public CommandLine.IFactory getFactory()
```

Returns the factory that this `CommandLine` was constructed with.

Returns:
the factory that this `CommandLine` was constructed with, never `null`
Since:
4.6










    - 

#### isUsageHelpRequested


```
public boolean isUsageHelpRequested()
```

Returns `true` if an option annotated with `CommandLine.Option.usageHelp()` was specified on the command line.

Returns:
whether the parser encountered an option annotated with `CommandLine.Option.usageHelp()`.
Since:
0.9.8










    - 

#### isVersionHelpRequested


```
public boolean isVersionHelpRequested()
```

Returns `true` if an option annotated with `CommandLine.Option.versionHelp()` was specified on the command line.

Returns:
whether the parser encountered an option annotated with `CommandLine.Option.versionHelp()`.
Since:
0.9.8










    - 

#### getHelp


```
public CommandLine.Help getHelp()
```

Returns a new `Help` object created by the `IHelpFactory` with the `CommandSpec` and `ColorScheme` of this command.

Since:
4.1
See Also:
`Help#Help(CommandSpec, Help.ColorScheme)`, 
`getHelpFactory()`, 
`getCommandSpec()`, 
`getColorScheme()`










    - 

#### getHelpFactory


```
public CommandLine.IHelpFactory getHelpFactory()
```

Returns the `IHelpFactory` that is used to construct the usage help message.

Since:
3.9
See Also:
`setHelpFactory(IHelpFactory)`










    - 

#### setHelpFactory


```
public CommandLine setHelpFactory(CommandLine.IHelpFactory helpFactory)
```

Sets a new `IHelpFactory` to customize the usage help message.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`helpFactory` - the new help factory. Must be non-`null`.
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.9










    - 

#### getHelpSectionKeys


```
public List<String> getHelpSectionKeys()
```

Returns the section keys in the order that the usage help message should render the sections.
 This ordering may be modified with `setSectionKeys`. The default keys are (in order):
 

   
      - `SECTION_KEY_HEADER_HEADING`
   
      - `SECTION_KEY_HEADER`
   
      - `SECTION_KEY_SYNOPSIS_HEADING`
   
      - `SECTION_KEY_SYNOPSIS`
   
      - `SECTION_KEY_DESCRIPTION_HEADING`
   
      - `SECTION_KEY_DESCRIPTION`
   
      - `SECTION_KEY_PARAMETER_LIST_HEADING`
   
      - `SECTION_KEY_AT_FILE_PARAMETER`
   
      - `SECTION_KEY_PARAMETER_LIST`
   
      - `SECTION_KEY_OPTION_LIST_HEADING`
   
      - `SECTION_KEY_OPTION_LIST`
   
      - `SECTION_KEY_COMMAND_LIST_HEADING`
   
      - `SECTION_KEY_COMMAND_LIST`
   
      - `SECTION_KEY_EXIT_CODE_LIST_HEADING`
   
      - `SECTION_KEY_EXIT_CODE_LIST`
   
      - `SECTION_KEY_FOOTER_HEADING`
   
      - `SECTION_KEY_FOOTER`
 


Since:
3.9










    - 

#### setHelpSectionKeys


```
public CommandLine setHelpSectionKeys(List<String> keys)
```

Sets the section keys in the order that the usage help message should render the sections.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.
 

Use `CommandLine.Model.UsageMessageSpec.sectionKeys(List)` to customize a command without affecting its subcommands.

Since:
3.9
See Also:
`getHelpSectionKeys()`










    - 

#### getHelpSectionMap


```
public Map<String,CommandLine.IHelpSectionRenderer> getHelpSectionMap()
```

Returns the map of section keys and renderers used to construct the usage help message.
 The usage help message can be customized by adding, replacing and removing section renderers from this map.
 Sections can be reordered with `setSectionKeys`.
 Sections that are either not in this map or not in the list returned by `getSectionKeys` are omitted.
 


 NOTE: By modifying the returned `Map`, only the usage help message *of this command* is affected.
 Use `setHelpSectionMap(Map)` to customize the usage help message for this command *and all subcommands*.
 

Since:
3.9










    - 

#### setHelpSectionMap


```
public CommandLine setHelpSectionMap(Map<String,CommandLine.IHelpSectionRenderer> map)
```

Sets the map of section keys and renderers used to construct the usage help message.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.
 

Use `CommandLine.Model.UsageMessageSpec.sectionMap(Map)` to customize a command without affecting its subcommands.

Since:
3.9
See Also:
`getHelpSectionMap()`










    - 

#### isAdjustLineBreaksForWideCJKCharacters


```
public boolean isAdjustLineBreaksForWideCJKCharacters()
```

Returns whether line breaks should take wide Chinese, Japanese and Korean characters into account for line-breaking purposes. The default is `true`.

Returns:
true if wide Chinese, Japanese and Korean characters are counted as double the size of other characters for line-breaking purposes
Since:
4.0










    - 

#### setAdjustLineBreaksForWideCJKCharacters


```
public CommandLine setAdjustLineBreaksForWideCJKCharacters(boolean adjustForWideChars)
```

Sets whether line breaks should take wide Chinese, Japanese and Korean characters into account, and returns this UsageMessageSpec. The default is `true`.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`adjustForWideChars` - if true, wide Chinese, Japanese and Korean characters are counted as double the size of other characters for line-breaking purposes
Since:
4.0










    - 

#### isToggleBooleanFlags


```
public boolean isToggleBooleanFlags()
```

Returns whether the value of boolean flag options should be "toggled" when the option is matched.
 From 4.0, this is `false` by default, and when a flag option is specified on the command line picocli
 will set its value to the opposite of its default value.
 If this method returns `true`, flags are toggled, so if the value is `true` it is
 set to `false`, and when the value is `false` it is set to `true`.
 When toggling is enabled, specifying a flag option twice on the command line will have no effect because they cancel each other out.

Returns:
`true` the value of boolean flag options should be "toggled" when the option is matched, `false` otherwise
Since:
3.0










    - 

#### setToggleBooleanFlags


```
public CommandLine setToggleBooleanFlags(boolean newValue)
```

Sets whether the value of boolean flag options should be "toggled" when the option is matched. The default is `false`,
 and when a flag option is specified on the command line picocli will set its value to the opposite of its default value.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.0










    - 

#### isInterpolateVariables


```
public boolean isInterpolateVariables()
```

Returns whether variables should be interpolated in String values. The default is `true`.

Since:
4.0










    - 

#### setInterpolateVariables


```
public CommandLine setInterpolateVariables(boolean interpolate)
```

Sets whether variables should be interpolated in String values. The default is `true`.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Since:
4.0










    - 

#### isOverwrittenOptionsAllowed


```
public boolean isOverwrittenOptionsAllowed()
```

Returns whether options for single-value fields can be specified multiple times on the command line.
 The default is `false` and a `CommandLine.OverwrittenOptionException` is thrown if this happens.
 When `true`, the last specified value is retained.

Returns:
`true` if options for single-value fields can be specified multiple times on the command line, `false` otherwise
Since:
0.9.7










    - 

#### setOverwrittenOptionsAllowed


```
public CommandLine setOverwrittenOptionsAllowed(boolean newValue)
```

Sets whether options for single-value fields can be specified multiple times on the command line without a `CommandLine.OverwrittenOptionException` being thrown.
 The default is `false`.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting
Returns:
this `CommandLine` object, to allow method chaining
Since:
0.9.7










    - 

#### isPosixClusteredShortOptionsAllowed


```
public boolean isPosixClusteredShortOptionsAllowed()
```

Returns whether the parser accepts clustered short options. The default is `true`.

Returns:
`true` if short options like `-x -v -f SomeFile` can be clustered together like `-xvfSomeFile`, `false` otherwise
Since:
3.0










    - 

#### setPosixClusteredShortOptionsAllowed


```
public CommandLine setPosixClusteredShortOptionsAllowed(boolean newValue)
```

Sets whether short options like `-x -v -f SomeFile` can be clustered together like `-xvfSomeFile`. The default is `true`.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.0










    - 

#### isCaseInsensitiveEnumValuesAllowed


```
public boolean isCaseInsensitiveEnumValuesAllowed()
```

Returns whether the parser should ignore case when converting arguments to `enum` values. The default is `false`.

Returns:
`true` if enum values can be specified that don't match the `toString()` value of the enum constant, `false` otherwise;
 e.g., for an option of type java.time.DayOfWeek,
 values `MonDaY`, `monday` and `MONDAY` are all recognized if `true`.
Since:
3.4










    - 

#### setCaseInsensitiveEnumValuesAllowed


```
public CommandLine setCaseInsensitiveEnumValuesAllowed(boolean newValue)
```

Sets whether the parser should ignore case when converting arguments to `enum` values. The default is `false`.
 When set to true, for example, for an option of type java.time.DayOfWeek,
 values `MonDaY`, `monday` and `MONDAY` are all recognized if `true`.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.4










    - 

#### isTrimQuotes


```
public boolean isTrimQuotes()
```

Returns whether the parser should trim quotes from command line arguments. The default is
 read from the system property "picocli.trimQuotes" and will be `true` if the property is present and empty,
 or if its value is "true".
 

If this property is set to `true`, the parser will remove quotes from the command line arguments, as follows:
 

   
      - if the command line argument contains just the leading and trailing quote, these quotes are removed
   
      - if the command line argument contains more quotes than just the leading and trailing quote, the parser first
   tries to process the parameter with the quotes intact. For example, the `split` regular expression inside
   a quoted region should be ignored, so arguments like `"a,b","x,y"` are handled correctly.
   For arguments with nested quotes, quotes are removed later in the processing pipeline, after `split` operations are applied.
 


Returns:
`true` if the parser should trim quotes from command line arguments before processing them, `false` otherwise;
Since:
3.7
See Also:
`CommandLine.Model.ParserSpec.trimQuotes()`










    - 

#### setTrimQuotes


```
public CommandLine setTrimQuotes(boolean newValue)
```

Sets whether the parser should trim quotes from command line arguments before processing them. The default is
 read from the system property "picocli.trimQuotes" and will be `true` if the property is set and empty, or
 if its value is "true".
 

If this property is set to `true`, the parser will remove quotes from the command line arguments, as follows:
 

   
      - if the command line argument contains just the leading and trailing quote, these quotes are removed
   
      - if the command line argument contains more quotes than just the leading and trailing quote, the parser first
   tries to process the parameter with the quotes intact. For example, the `split` regular expression inside
   a quoted region should be ignored, so arguments like `"a,b","x,y"` are handled correctly.
   For arguments with nested quotes, quotes are removed later in the processing pipeline, after `split` operations are applied.
 

 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.
 

Calling this method will cause the "picocli.trimQuotes" property to have no effect.

Parameters:
`newValue` - the new setting
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.7
See Also:
`CommandLine.Model.ParserSpec.trimQuotes(boolean)`










    - 

#### isSplitQuotedStrings


```
@Deprecated
public boolean isSplitQuotedStrings()
```

Deprecated. Most applications should not change the default. The rare application that *does* need to split parameter values
 without respecting quotes should use `CommandLine.Model.ParserSpec.splitQuotedStrings(boolean)`.
Returns whether the parser is allowed to split quoted Strings or not. The default is `false`,
 so quotes are respected: quoted strings are treated as a single value that should not be broken up.
 


 For example, take a single command line parameter `"a,b","x,y"`. With a comma split regex, the default of `splitQuotedStrings = false`
 means that this value will be split into two strings: `"a,b"` and `"x,y"`. This is usually what you want.
 


 If `splitQuotedStrings` is set to `true`, quotes are not respected, and the value is split up into four parts:
 the first is `"a`, the second is `b"`, the third is `"x`, and the last part is `y"`. This is generally not what you want.
 

Returns:
`true` if the parser is allowed to split quoted Strings, `false` otherwise;
Since:
3.7
See Also:
`CommandLine.Model.ArgSpec.splitRegex()`, 
`CommandLine.Model.ParserSpec.splitQuotedStrings()`










    - 

#### setSplitQuotedStrings


```
@Deprecated
public CommandLine setSplitQuotedStrings(boolean newValue)
```

Deprecated. Most applications should not change the default. The rare application that *does* need to split parameter values
 without respecting quotes should use `CommandLine.Model.ParserSpec.splitQuotedStrings(boolean)`.
Sets whether the parser is allowed to split quoted Strings. The default is `false`,
 so quotes are respected: quoted strings are treated as a single value that should not be broken up.
 


 For example, take a single command line parameter `"a,b","x,y"`. With a comma split regex, the default of `splitQuotedStrings = false`
 means that this value will be split into two strings: `"a,b"` and `"x,y"`. This is usually what you want.
 


 However, if `splitQuotedStrings` is set to `true`, quotes are not respected, and the value is split up into four parts:
 the first is `"a`, the second is `b"`, the third is `"x`, and the last part is `y"`. This is generally not what you want.
 
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.7
See Also:
`CommandLine.Model.ArgSpec.splitRegex()`, 
`CommandLine.Model.ParserSpec.splitQuotedStrings(boolean)`










    - 

#### getEndOfOptionsDelimiter


```
public String getEndOfOptionsDelimiter()
```

Returns the end-of-options delimiter that signals that the remaining command line arguments should be treated as positional parameters.

Returns:
the end-of-options delimiter. The default is `"--"`.
Since:
3.5










    - 

#### setEndOfOptionsDelimiter


```
public CommandLine setEndOfOptionsDelimiter(String delimiter)
```

Sets the end-of-options delimiter that signals that the remaining command line arguments should be treated as positional parameters.

Parameters:
`delimiter` - the end-of-options delimiter; must not be `null`. The default is `"--"`.
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.5










    - 

#### isSubcommandsCaseInsensitive


```
public boolean isSubcommandsCaseInsensitive()
```

Returns whether upper case and lower case should be ignored when matching subcommands. The default is `false`.

Returns:
`true` if subcommands can be matched when they differ only in case from the `getCommandName()` value of a registered one, `false` otherwise.
       For example, if true, for a subcommand with name `help`, inputs like `help`, `HeLp` and `HELP` are all recognized.
Since:
4.3










    - 

#### setSubcommandsCaseInsensitive


```
public CommandLine setSubcommandsCaseInsensitive(boolean newValue)
```

Sets whether upper case and lower case should be ignored when matching subcommands. The default is `false`.
 For example, when set to `true`, for a subcommand with name `help`, inputs like `help`, `HeLp` and `HELP` are all recognized.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting
Returns:
this `CommandLine` object, to allow method chaining
Since:
4.3










    - 

#### isOptionsCaseInsensitive


```
public boolean isOptionsCaseInsensitive()
```

Returns whether upper case and lower case should be ignored when matching option names. The default is `false`.

Returns:
`true` if options can be matched when they differ only in case from the `names()` value of a registered one, `false` otherwise;
       For example, if true, for an option with name `-h`, inputs like `-h`, `-H` are both recognized.
Since:
4.3










    - 

#### setOptionsCaseInsensitive


```
public CommandLine setOptionsCaseInsensitive(boolean newValue)
```

Sets whether upper case and lower case should be ignored when matching option names. The default is `false`.
 For example, when set to `true`, for an option with name `-h`, inputs like `-h`, `-H` are both recognized.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.
 Note that changing case sensitivity will also change the case sensitivity of negatable options:
 any custom `CommandLine.INegatableOptionTransformer` that was previously installed will be replaced by the case-insensitive
 version of the default transformer. To ensure your custom transformer is used, install it last, after changing case sensitivity.

Parameters:
`newValue` - the new setting
Returns:
this `CommandLine` object, to allow method chaining
Since:
4.3










    - 

#### isAbbreviatedSubcommandsAllowed


```
public boolean isAbbreviatedSubcommandsAllowed()
```

Returns whether abbreviation of subcommands should be allowed when matching subcommands. The default is `false`.

Returns:
`true` if subcommands can be matched when they are abbreviations of the `getCommandName()` value of a registered one, `false` otherwise.
       For example, if true, for a subcommand with name `helpCommand`, inputs like `h`, `h-c` and `hC` are all recognized.
Since:
4.4










    - 

#### setAbbreviatedSubcommandsAllowed


```
public CommandLine setAbbreviatedSubcommandsAllowed(boolean newValue)
```

Sets whether abbreviated subcommands should be matched. The default is `false`.
 For example, when set to `true`, for a subcommand `helpCommand`, inputs like `h`, `h-c` and `hC` are all recognized.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting
Returns:
this `CommandLine` object, to allow method chaining
Since:
4.4










    - 

#### isAbbreviatedOptionsAllowed


```
public boolean isAbbreviatedOptionsAllowed()
```

Returns whether abbreviation of option names should be allowed when matching options. The default is `false`.

Returns:
`true` if options can be matched when they are abbreviations of the `names()` value of a registered one, `false` otherwise.
       For example, if true, for a subcommand with name `--helpMe`, inputs like `--h`, `--h-m` and `--hM` are all recognized.
Since:
4.4










    - 

#### setAbbreviatedOptionsAllowed


```
public CommandLine setAbbreviatedOptionsAllowed(boolean newValue)
```

Sets whether abbreviated option names should be matched. The default is `false`.
 For example, when set to `true`, for an option with name `--helpMe`, inputs like `--h`, `--h-m` and `--hM` are all recognized.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting
Returns:
this `CommandLine` object, to allow method chaining
Since:
4.4










    - 

#### getDefaultValueProvider


```
public CommandLine.IDefaultValueProvider getDefaultValueProvider()
```

Returns the default value provider for the command, or `null` if none has been set.

Returns:
the default value provider for this command, or `null`
Since:
3.6
See Also:
`CommandLine.Command.defaultValueProvider()`, 
`CommandLine.Model.CommandSpec.defaultValueProvider()`, 
`CommandLine.Model.ArgSpec.defaultValueString()`










    - 

#### setDefaultValueProvider


```
public CommandLine setDefaultValueProvider(CommandLine.IDefaultValueProvider newValue)
```

Sets a default value provider for the command and sub-commands
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 sub-commands and nested sub-subcommands *at the moment this method is called*. Sub-commands added
 later will have the default setting. To ensure a setting is applied to all
 sub-commands, call the setter last, after adding sub-commands.

Parameters:
`newValue` - the default value provider to use
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.6










    - 

#### isStopAtPositional


```
public boolean isStopAtPositional()
```

Returns whether the parser interprets the first positional parameter as "end of options" so the remaining
 arguments are all treated as positional parameters. The default is `false`.

Returns:
`true` if all values following the first positional parameter should be treated as positional parameters, `false` otherwise
Since:
2.3










    - 

#### setStopAtPositional


```
public CommandLine setStopAtPositional(boolean newValue)
```

Sets whether the parser interprets the first positional parameter as "end of options" so the remaining
 arguments are all treated as positional parameters. The default is `false`.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - `true` if all values following the first positional parameter should be treated as positional parameters, `false` otherwise
Returns:
this `CommandLine` object, to allow method chaining
Since:
2.3










    - 

#### isStopAtUnmatched


```
public boolean isStopAtUnmatched()
```

Returns whether the parser should stop interpreting options and positional parameters as soon as it encounters an
 unmatched option. Unmatched options are arguments that look like an option but are not one of the known options, or
 positional arguments for which there is no available slots (the command has no positional parameters or their size is limited).
 The default is `false`.
 

Setting this flag to `true` automatically sets the unmatchedArgumentsAllowed flag to `true` also.

Returns:
`true` when an unmatched option should result in the remaining command line arguments to be added to the
      unmatchedArguments list
Since:
2.3










    - 

#### setStopAtUnmatched


```
public CommandLine setStopAtUnmatched(boolean newValue)
```

Sets whether the parser should stop interpreting options and positional parameters as soon as it encounters an
 unmatched option. Unmatched options are arguments that look like an option but are not one of the known options, or
 positional arguments for which there is no available slots (the command has no positional parameters or their size is limited).
 The default is `false`.
 

Setting this flag to `true` automatically sets the unmatchedArgumentsAllowed flag to `true` also.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - `true` when an unmatched option should result in the remaining command line arguments to be added to the
      unmatchedArguments list
Returns:
this `CommandLine` object, to allow method chaining
Since:
2.3










    - 

#### isAllowSubcommandsAsOptionParameters


```
public boolean isAllowSubcommandsAsOptionParameters()
```

Returns whether options can have parameter values that match subcommand names or aliases,
 or whether such values should be rejected with a missing parameter exception.
 The default is `false`, so by default input like `-x=subcommand` is rejected if `-x` is an option that takes a String parameter, and `subcommand` is a subcommand of this command.

Returns:
`true` when options can have parameter values that match subcommand names or aliases, `false` when such values should be rejected with a missing parameter exception
Since:
4.7.7
See Also:
`CommandLine.Model.ParserSpec.allowSubcommandsAsOptionParameters()`










    - 

#### setAllowSubcommandsAsOptionParameters


```
public CommandLine setAllowSubcommandsAsOptionParameters(boolean newValue)
```

Sets whether options can have parameter values that match subcommand names or aliases, or whether such values should be rejected with a missing parameter exception.
 The default is `false`, so by default
 input like `-x=subcommand` is rejected if `-x` is an option that takes a String parameter, and `subcommand` is a subcommand of this command.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting. When `true`, options can have parameter values that match subcommand names or aliases, when `false`, such values are rejected with a missing parameter exception
Returns:
this `CommandLine` object, to allow method chaining
Since:
4.7.7
See Also:
`CommandLine.Model.ParserSpec.allowSubcommandsAsOptionParameters(boolean)`










    - 

#### isAllowOptionsAsOptionParameters


```
public boolean isAllowOptionsAsOptionParameters()
```

Returns whether options can have parameter values that match the name of an option in this command,
 or whether such values should be rejected with a missing parameter exception.
 The default is `false`, so by default input like `-x=--some-option` is rejected if `-x` is an option that takes a String parameter, and `--some-option` is an option of this command.
 

This method only considers actual options of this command, as opposed to `isUnmatchedOptionsAllowedAsOptionParameters()`, which considers values that *resemble* options.

Returns:
`true` when options can have parameter values that match the name of an option in this command, `false` when such values should be rejected with a missing parameter exception
Since:
4.7.7
See Also:
`isUnmatchedOptionsAllowedAsOptionParameters()`, 
`CommandLine.Model.ParserSpec.allowOptionsAsOptionParameters()`










    - 

#### setAllowOptionsAsOptionParameters


```
public CommandLine setAllowOptionsAsOptionParameters(boolean newValue)
```

Sets whether options can have parameter values that match the name of an option in this command, or whether such values should be rejected with a missing parameter exception.
 The default is `false`, so by default
 input like `-x=--some-option` is rejected if `-x` is an option that takes a String parameter, and `--some-option` is an option of this command.
 

This method only considers actual options of this command, as opposed to `setUnmatchedOptionsAllowedAsOptionParameters(boolean)`, which considers values that *resemble* options.
 

Use with caution! When set to `true`, any option in the command will consume the maximum number of arguments possible for its arity.
 This means that an option with `arity = "*"` will consume *all* command line arguments following that option.
 If this is not what you want, consider custom parameter processing.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting. When `true`, options can have parameter values that match the name of an option in this command, when `false`, such values are rejected with a missing parameter exception
Returns:
this `CommandLine` object, to allow method chaining
Since:
4.7.7
See Also:
`setUnmatchedOptionsAllowedAsOptionParameters(boolean)`, 
`CommandLine.Model.ParserSpec.allowOptionsAsOptionParameters(boolean)`










    - 

#### isUnmatchedOptionsAllowedAsOptionParameters


```
public boolean isUnmatchedOptionsAllowedAsOptionParameters()
```

Returns whether options can have parameter values that resemble an option, or whether such values should be rejected as unknown options.
 The default is `true`, so by default input like `-x=-unknown` is accepted if `-x` is an option that takes a String parameter.
 

This method only considers values that *resemble* options, as opposed to `isAllowOptionsAsOptionParameters()`, which considers actual options of this command.

Returns:
`true` when options can have parameter values that resemble an option, `false` when such values should be rejected as unknown options
Since:
4.4
See Also:
`isAllowOptionsAsOptionParameters()`, 
`CommandLine.Model.ParserSpec.unmatchedOptionsAllowedAsOptionParameters()`










    - 

#### setUnmatchedOptionsAllowedAsOptionParameters


```
public CommandLine setUnmatchedOptionsAllowedAsOptionParameters(boolean newValue)
```

Sets whether options can have parameter values that resemble an option, or whether such values should be rejected as unknown options.
 The default is `true`, so by default
 input like `-x=-unknown` is accepted if `-x` is an option that takes a String parameter.
 

This method only considers values that *resemble* options, as opposed to `setAllowOptionsAsOptionParameters(boolean)`, which considers actual options of this command.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting. When `true`, options can have parameter values that resemble an option, when `false`, such values are rejected as unknown options
Returns:
this `CommandLine` object, to allow method chaining
Since:
4.4
See Also:
`setAllowOptionsAsOptionParameters(boolean)`, 
`CommandLine.Model.ParserSpec.unmatchedOptionsAllowedAsOptionParameters(boolean)`










    - 

#### isUnmatchedOptionsArePositionalParams


```
public boolean isUnmatchedOptionsArePositionalParams()
```

Returns whether arguments on the command line that resemble an option should be treated as positional parameters.
 The default is `false` and the parser behaviour depends on `isUnmatchedArgumentsAllowed()`.

Returns:
`true` arguments on the command line that resemble an option should be treated as positional parameters, `false` otherwise
Since:
3.0
See Also:
`getUnmatchedArguments()`










    - 

#### setUnmatchedOptionsArePositionalParams


```
public CommandLine setUnmatchedOptionsArePositionalParams(boolean newValue)
```

Sets whether arguments on the command line that resemble an option should be treated as positional parameters.
 The default is `false`.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting. When `true`, arguments on the command line that resemble an option should be treated as positional parameters.
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.0
See Also:
`getUnmatchedArguments()`, 
`isUnmatchedArgumentsAllowed()`










    - 

#### isUnmatchedArgumentsAllowed


```
public boolean isUnmatchedArgumentsAllowed()
```

Returns whether the end user may specify arguments on the command line that are not matched to any option or parameter fields.
 The default is `false` and a `CommandLine.UnmatchedArgumentException` is thrown if this happens.
 When `true`, the last unmatched arguments are available via the `getUnmatchedArguments()` method.

Returns:
`true` if the end use may specify unmatched arguments on the command line, `false` otherwise
Since:
0.9.7
See Also:
`getUnmatchedArguments()`










    - 

#### setUnmatchedArgumentsAllowed


```
public CommandLine setUnmatchedArgumentsAllowed(boolean newValue)
```

Sets whether the end user may specify unmatched arguments on the command line without a `CommandLine.UnmatchedArgumentException` being thrown.
 The default is `false`.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`newValue` - the new setting. When `true`, the last unmatched arguments are available via the `getUnmatchedArguments()` method.
Returns:
this `CommandLine` object, to allow method chaining
Since:
0.9.7
See Also:
`getUnmatchedArguments()`










    - 

#### getUnmatchedArguments


```
public List<String> getUnmatchedArguments()
```

Returns the list of unmatched command line arguments, if any.

Returns:
the list of unmatched command line arguments or an empty list
Since:
0.9.7
See Also:
`isUnmatchedArgumentsAllowed()`










    - 

#### getColorScheme


```
public CommandLine.Help.ColorScheme getColorScheme()
```

Returns the color scheme to use when printing help.
 The default value is the default color scheme with `Ansi.AUTO`.

Since:
4.0
See Also:
`execute(String...)`, 
`usage(PrintStream)`, 
`usage(PrintWriter)`, 
`getUsageMessage()`, 
`CommandLine.Help.defaultColorScheme(CommandLine.Help.Ansi)`










    - 

#### setColorScheme


```
public CommandLine setColorScheme(CommandLine.Help.ColorScheme colorScheme)
```

Sets the color scheme to use when printing help.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`colorScheme` - the new color scheme
Since:
4.0
See Also:
`execute(String...)`, 
`usage(PrintStream)`, 
`usage(PrintWriter)`, 
`getUsageMessage()`










    - 

#### getOut


```
public PrintWriter getOut()
```

Returns the writer used when printing user-requested usage help or version help during command execution.
 Defaults to a PrintWriter wrapper around `System.out` unless `setOut(PrintWriter)` was called with a different writer.
 

This method is used by `execute(String...)`. Custom `IExecutionStrategy` implementations should also use this writer.
 


 By convention, when the user requests
 help with a `--help` or similar option, the usage help message is printed to the standard output stream so that it can be easily searched and paged.

Since:
4.0










    - 

#### setOut


```
public CommandLine setOut(PrintWriter out)
```

Sets the writer to use when printing user-requested usage help or version help during command execution.
 

This method is used by `execute(String...)`. Custom `IExecutionStrategy` implementations should also use this writer.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`out` - the new PrintWriter to use
Returns:
this CommandLine for method chaining
Since:
4.0










    - 

#### getErr


```
public PrintWriter getErr()
```

Returns the writer to use when printing diagnostic (error) messages during command execution.
 Defaults to a PrintWriter wrapper around `System.err`, unless `setErr(PrintWriter)` was called with a different writer.
 

This method is used by `execute(String...)`.
 `IParameterExceptionHandler` and `IExecutionExceptionHandler` implementations
 should use this writer to print error messages (which may include a usage help message) when an unexpected error occurs.

Since:
4.0










    - 

#### setErr


```
public CommandLine setErr(PrintWriter err)
```

Sets the writer to use when printing diagnostic (error) messages during command execution.
 

This method is used by `execute(String...)`.
 `IParameterExceptionHandler` and `IExecutionExceptionHandler` implementations
 should use this writer to print error messages (which may include a usage help message) when an unexpected error occurs.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`err` - the new PrintWriter to use
Returns:
this CommandLine for method chaining
Since:
4.0










    - 

#### getExitCodeExceptionMapper


```
public CommandLine.IExitCodeExceptionMapper getExitCodeExceptionMapper()
```

Returns the mapper that was set by the application to map from exceptions to exit codes, for use by the `execute` method.

Returns:
the mapper that was set, or `null` if none was set
Since:
4.0










    - 

#### setExitCodeExceptionMapper


```
public CommandLine setExitCodeExceptionMapper(CommandLine.IExitCodeExceptionMapper exitCodeExceptionMapper)
```

Sets the mapper used by the `execute` method to map exceptions to exit codes.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`exitCodeExceptionMapper` - the new value
Returns:
this CommandLine for method chaining
Since:
4.0










    - 

#### getExecutionStrategy


```
public CommandLine.IExecutionStrategy getExecutionStrategy()
```

Returns the execution strategy used by the `execute` method to invoke
 the business logic on the user objects of this command and/or the user-specified subcommand(s).
 The default value is `RunLast`.

Returns:
the execution strategy to run the user-specified command
Since:
4.0










    - 

#### setExecutionStrategy


```
public CommandLine setExecutionStrategy(CommandLine.IExecutionStrategy executionStrategy)
```

Sets the execution strategy that the `execute` method should use to invoke
 the business logic on the user objects of this command and/or the user-specified subcommand(s).
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`executionStrategy` - the new execution strategy to run the user-specified command
Returns:
this CommandLine for method chaining
Since:
4.0










    - 

#### getParameterExceptionHandler


```
public CommandLine.IParameterExceptionHandler getParameterExceptionHandler()
```

Returns the handler for dealing with invalid user input when the command is executed.
 

The default implementation prints an error message describing the problem, followed by either suggested alternatives
 for mistyped options, or the full usage help message of the problematic command;
 it then delegates to the exit code exception mapper for an exit code, with
 `exitCodeOnInvalidInput` as the default exit code.
 


 Alternatively, you can install a "short error message handler" like this:
 
 

```

 static class ShortErrorMessageHandler implements IParameterExceptionHandler {
     public int handleParseException(ParameterException ex, String[] args) {
         CommandLine cmd = ex.getCommandLine();
         PrintWriter writer = cmd.getErr();

         writer.println(ex.getMessage());
         UnmatchedArgumentException.printSuggestions(ex, writer);
         writer.print(cmd.getHelp().fullSynopsis());

         CommandSpec spec = cmd.getCommandSpec();
         writer.printf("Try '%s --help' for more information.%n", spec.qualifiedName());

         return cmd.getExitCodeExceptionMapper() != null
                     ? cmd.getExitCodeExceptionMapper().getExitCode(ex)
                     : spec.exitCodeOnInvalidInput();
     }
 }
 
```

 

Install this error handler like this:
 

```

 new CommandLine(new MyApp())
     .setParameterExceptionHandler(new ShortErrorMessageHandler())
     .execute(args);
 
```


Returns:
the handler for dealing with invalid user input
Since:
4.0










    - 

#### setParameterExceptionHandler


```
public CommandLine setParameterExceptionHandler(CommandLine.IParameterExceptionHandler parameterExceptionHandler)
```

Sets the handler for dealing with invalid user input when the command is executed.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`parameterExceptionHandler` - the new handler for dealing with invalid user input
Returns:
this CommandLine for method chaining
Since:
4.0
See Also:
`an example short exception handler`










    - 

#### getExecutionExceptionHandler


```
public CommandLine.IExecutionExceptionHandler getExecutionExceptionHandler()
```

Returns the handler for dealing with exceptions that occurred in the `Callable`, `Runnable` or `Method`
 user object of a command when the command was executed.
 

The default implementation rethrows the specified exception.

Returns:
the handler for dealing with exceptions that occurred in the business logic when the `execute` method was invoked.
Since:
4.0










    - 

#### setExecutionExceptionHandler


```
public CommandLine setExecutionExceptionHandler(CommandLine.IExecutionExceptionHandler executionExceptionHandler)
```

Sets a custom handler for dealing with exceptions that occurred in the `Callable`, `Runnable` or `Method`
 user object of a command when the command was executed via the execute method.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`executionExceptionHandler` - the handler for dealing with exceptions that occurred in the business logic when the `execute` method was invoked.
Returns:
this CommandLine for method chaining
Since:
4.0












    - 

#### populateCommand


```
public static <T> T populateCommand(T command,
                                    String... args)
```



 Convenience method that initializes the specified annotated object from the specified command line arguments.
 


 This is equivalent to
 

```

 new CommandLine(command).parseArgs(args);
 return command;
 
```

 

All this method does is parse the arguments and populate the annotated fields and methods.
 The caller is responsible for catching any exceptions, handling requests for usage help
 or version information, and invoking the business logic.
 Applications may be interested in using the `execute(String...)` method instead.

Type Parameters:
`T` - the type of the annotated object
Parameters:
`command` - the object to initialize. This object contains fields annotated with
          `@Option` or `@Parameters`.
`args` - the command line arguments to parse
Returns:
the specified annotated object
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ParameterException` - if the specified command line arguments are invalid
Since:
0.9.7
See Also:
`execute(String...)`










    - 

#### populateSpec


```
public static <T> T populateSpec(Class<T> spec,
                                 String... args)
```



 Convenience method that derives the command specification from the specified interface class, and returns an
 instance of the specified interface. The interface is expected to have annotated getter methods. Picocli will
 instantiate the interface and the getter methods will return the option and positional parameter values matched on the command line.
 


 This is equivalent to
 

```

 CommandLine cli = new CommandLine(spec);
 cli.parse(args);
 return cli.getCommand();
 
```

 

All this method does is parse the arguments and return an instance whose annotated methods return the specified values.
 The caller is responsible for catching any exceptions, handling requests for usage help
 or version information, and invoking the business logic.
 Applications may be interested in using the `execute(String...)` method instead.

Type Parameters:
`T` - the type of the annotated object
Parameters:
`spec` - the interface that defines the command specification. This object contains getter methods annotated with
          `@Option` or `@Parameters`.
`args` - the command line arguments to parse
Returns:
an instance of the specified annotated interface
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ParameterException` - if the specified command line arguments are invalid
Since:
3.1
See Also:
`execute(String...)`










    - 

#### parse


```
@Deprecated
public List<CommandLine> parse(String... args)
```

Deprecated. use `parseArgs(String...)` instead
Expands any @-files in the specified command line arguments, then
 parses the arguments and returns a list of `CommandLine` objects representing the
 top-level command and any subcommands (if any) that were recognized and initialized during the parsing process.
 


 If parsing succeeds, the first element in the returned list is always `this CommandLine` object. The
 returned list may contain more elements if subcommands were registered
 and these subcommands were initialized by matching command line arguments. If parsing fails, a
 `CommandLine.ParameterException` is thrown.
 
 

All this method does is parse the arguments and populate the annotated fields and methods.
 The caller is responsible for catching any exceptions, handling requests for usage help
 or version information, and invoking the business logic.
 Applications may be interested in using the `execute(String...)` method instead.

Parameters:
`args` - the command line arguments to parse
Returns:
a list with the top-level command and any subcommands initialized by this method
Throws:
`CommandLine.ParameterException` - if the specified command line arguments are invalid; use
      `CommandLine.ParameterException.getCommandLine()` to get the command or subcommand whose user input was invalid










    - 

#### parseArgs


```
public CommandLine.ParseResult parseArgs(String... args)
```

Expands any @-files in the specified command line arguments, then
 parses the arguments and returns a `ParseResult` with the options, positional
 parameters, and subcommands (if any) that were recognized and initialized during the parsing process.
 

If parsing fails, a `CommandLine.ParameterException` is thrown.
 

All this method does is parse the arguments and populate the annotated fields and methods.
 The caller is responsible for catching any exceptions, handling requests for usage help
 or version information, and invoking the business logic.
 Applications may be interested in using the `execute(String...)` method instead.

Parameters:
`args` - the command line arguments to parse
Returns:
a list with the top-level command and any subcommands initialized by this method
Throws:
`CommandLine.ParameterException` - if the specified command line arguments are invalid; use
      `CommandLine.ParameterException.getCommandLine()` to get the command or subcommand whose user input was invalid
See Also:
`execute(String...)`










    - 

#### getParseResult


```
public CommandLine.ParseResult getParseResult()
```










    - 

#### getExecutionResult


```
public <T> T getExecutionResult()
```

Returns the result of calling the user object `Callable` or invoking the user object `Method`
 after parsing the user input, or `null` if this command has not been executed
 or if this `CommandLine` is for a subcommand that was not specified by the end user on the command line.
 

**Implementation note:**
 

It is the responsibility of the `IExecutionStrategy` to set this value.

Type Parameters:
`T` - type of the result value
Returns:
the result of the user object `Callable` or `Method` (may be `null`), or `null` if this (sub)command was not executed
Since:
4.0










    - 

#### setExecutionResult


```
public void setExecutionResult(Object result)
```

Sets the result of calling the business logic on the command's user object.

Parameters:
`result` - the business logic result, may be `null`
Since:
4.0
See Also:
`execute(String...)`, 
`CommandLine.IExecutionStrategy`










    - 

#### clearExecutionResults


```
public void clearExecutionResults()
```

Clears the execution result of a previous invocation from this `CommandLine` and all subcommands.

Since:
4.0










    - 

#### defaultExceptionHandler


```
public static CommandLine.DefaultExceptionHandler<List<Object>> defaultExceptionHandler()
```

Convenience method that returns `new DefaultExceptionHandler<List<Object>>()`.









    - 

#### printHelpIfRequested


```
@Deprecated
public static boolean printHelpIfRequested(List<CommandLine> parsedCommands,
                                                        PrintStream out,
                                                        CommandLine.Help.Ansi ansi)
```

Deprecated. use `printHelpIfRequested(ParseResult)` instead

Since:
2.0










    - 

#### printHelpIfRequested


```
public static boolean printHelpIfRequested(CommandLine.ParseResult parseResult)
```

Delegates to `executeHelpRequest(ParseResult)`.

Parameters:
`parseResult` - contains the `CommandLine` objects found during parsing; check these to see if help was requested
Returns:
`true` if help was printed, `false` otherwise
Since:
3.0










    - 

#### printHelpIfRequested


```
@Deprecated
public static boolean printHelpIfRequested(List<CommandLine> parsedCommands,
                                                        PrintStream out,
                                                        PrintStream err,
                                                        CommandLine.Help.Ansi ansi)
```

Deprecated. use `executeHelpRequest(ParseResult)` instead
Delegates to the implementation of `executeHelpRequest(ParseResult)`.

Parameters:
`parsedCommands` - the list of `CommandLine` objects to check if help was requested
`out` - the `PrintStream` to print help to if requested
`err` - the error string to print diagnostic messages to, in addition to the output from the exception handler
`ansi` - for printing help messages using ANSI styles and colors
Returns:
`true` if help was printed, `false` otherwise
Since:
3.0










    - 

#### printHelpIfRequested


```
@Deprecated
public static boolean printHelpIfRequested(List<CommandLine> parsedCommands,
                                                        PrintStream out,
                                                        PrintStream err,
                                                        CommandLine.Help.ColorScheme colorScheme)
```

Deprecated. use `executeHelpRequest(ParseResult)` instead
Delegates to the implementation of `executeHelpRequest(ParseResult)`.

Parameters:
`parsedCommands` - the list of `CommandLine` objects to check if help was requested
`out` - the `PrintStream` to print help to if requested
`err` - the error string to print diagnostic messages to, in addition to the output from the exception handler
`colorScheme` - for printing help messages using ANSI styles and colors
Returns:
`true` if help was printed, `false` otherwise
Since:
3.6










    - 

#### executeHelpRequest


```
public static Integer executeHelpRequest(CommandLine.ParseResult parseResult)
```

Helper method that may be useful when processing the `ParseResult` that results from successfully
 parsing command line arguments. This method prints out
 usage help to the configured output writer
 if requested or version help
 to the configured output writer if requested
 and returns `CommandLine.Model.CommandSpec.exitCodeOnUsageHelp()` or `CommandLine.Model.CommandSpec.exitCodeOnVersionHelp()`, respectively.
 If the command is a `CommandLine.Command.helpCommand()` and `runnable` or `callable`,
 that command is executed and this method returns `CommandLine.Model.CommandSpec.exitCodeOnUsageHelp()`.
 Otherwise, if none of the specified `CommandLine` objects have help requested,
 this method returns `null`.


 Note that this method *only* looks at the `usageHelp` and
 `versionHelp` attributes. The `help` attribute is ignored.
 

**Implementation note:**


 When an error occurs while processing the help request, it is recommended custom Help commands throw a
 `CommandLine.ParameterException` with a reference to the parent command. This will print the error message and the
 usage for the parent command, and will use the exit code of the exception handler if one was set.
 

Parameters:
`parseResult` - contains the `CommandLine` objects found during parsing; check these to see if help was requested
Returns:
`CommandLine.Model.CommandSpec.exitCodeOnUsageHelp()` if usage help was requested,
      `CommandLine.Model.CommandSpec.exitCodeOnVersionHelp()` if version help was requested, and `null` otherwise
Since:
4.0
See Also:
`CommandLine.IHelpCommandInitializable2`










    - 

#### execute


```
public int execute(String... args)
```

Convenience method to allow command line application authors to avoid some boilerplate code in their application.
 To use this method, the annotated object that this `CommandLine` is constructed with needs to
 either implement `Runnable`, `Callable`, or be a `Method` object.
 See `getCommandMethods` for a convenient way to obtain a command `Method`.
 

This method replaces the `run`, `call`
 and `invoke` convenience methods that were available with previous versions of picocli.
 


 **Exit Code**
 


 This method returns an exit code that applications can use to call `System.exit`.
 (The return value of the `Callable` or `Method` can still be obtained via `getExecutionResult`.)
 If the user object `Callable` or `Method` returns an `int` or `Integer`,
 this will be used as the exit code. Additionally, if the user object implements `IExitCodeGenerator`,
 an exit code is obtained by calling its `getExitCode()` method (after invoking the user object).
 


 In the case of multiple exit codes the highest value will be used (or if all values are negative, the lowest value will be used).
 


 **Exception Handling**
 


 This method never throws an exception.
 


 If the user specified invalid input, the parameter exception handler is invoked.
 By default this prints an error message and the usage help message, and returns an exit code.
 


 If an exception occurred while the user object `Runnable`, `Callable`, or `Method`
 was invoked, this exception is caught and passed to the execution exception handler.
 The default `IExecutionExceptionHandler` will rethrow this Exception.
 


 Any exception thrown from the `IParameterExceptionHandler` or `IExecutionExceptionHandler` is caught,
 it stacktrace is printed and is mapped to an exit code, using the following logic:
 


 If an `IExitCodeExceptionMapper` is configured,
 this mapper is used to determine the exit code based on the exception.
 


 If an `IExitCodeExceptionMapper` is not set, by default this method will return the `@Command` annotation's
 `exitCodeOnInvalidInput` or `exitCodeOnExecutionException` value, respectively.
 

**Example Usage:**
 

```

 @Command
 class MyCommand implements Callable<Integer> {
     public Integer call() { return 123; }
 }
 CommandLine cmd = new CommandLine(new MyCommand());
 int exitCode = cmd.execute(args);
 assert exitCode == 123;
 System.exit(exitCode);
 
```

 

Since `execute` is an instance method, not a static method, applications can do configuration before invoking the command. For example:
 

```

 CommandLine cmd = new CommandLine(new MyCallable())
         .setCaseInsensitiveEnumValuesAllowed(true) // configure a non-default parser option
         .setOut(myOutWriter()) // configure an alternative to System.out
         .setErr(myErrWriter()) // configure an alternative to System.err
         .setColorScheme(myColorScheme()); // configure a custom color scheme
 int exitCode = cmd.execute(args);
 System.exit(exitCode);
 
```

 


 If the specified command has subcommands, the last subcommand specified on the
 command line is executed. This can be configured by setting the execution strategy.
 Built-in alternatives are executing the first subcommand, or executing all specified subcommands.
 

Parameters:
`args` - the command line arguments to parse
Returns:
the exit code
Since:
4.0
See Also:
`CommandLine.ExitCode`, 
`CommandLine.IExitCodeGenerator`, 
`getExecutionResult()`, 
`getExecutionStrategy()`, 
`getParameterExceptionHandler()`, 
`getExecutionExceptionHandler()`, 
`getExitCodeExceptionMapper()`










    - 

#### parseWithHandler


```
@Deprecated
public List<Object> parseWithHandler(CommandLine.IParseResultHandler handler,
                                                  PrintStream out,
                                                  String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead

Since:
2.0










    - 

#### parseWithHandler


```
@Deprecated
public <R> R parseWithHandler(CommandLine.IParseResultHandler2<R> handler,
                                           String[] args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Returns the result of calling `parseWithHandlers(IParseResultHandler2,  IExceptionHandler2, String...)` with
 a new `CommandLine.DefaultExceptionHandler` in addition to the specified parse result handler and the specified command line arguments.
 


 This is a convenience method intended to offer the same ease of use as the `run`
 and `call` methods, but with more flexibility and better
 support for nested subcommands.
 
 

Calling this method roughly expands to:
 

```

 try {
     ParseResult parseResult = parseArgs(args);
     return handler.handleParseResult(parseResult);
 } catch (ParameterException ex) {
     return new DefaultExceptionHandler<R>().handleParseException(ex, args);
 }
 
```

 


 Picocli provides some default handlers that allow you to accomplish some common tasks with very little code.
 The following handlers are available:
 

   
      - `CommandLine.RunLast` handler prints help if requested, and otherwise gets the last specified command or subcommand
 and tries to execute it as a `Runnable` or `Callable`.
   
      - `CommandLine.RunFirst` handler prints help if requested, and otherwise executes the top-level command as a `Runnable` or `Callable`.
   
      - `CommandLine.RunAll` handler prints help if requested, and otherwise executes all recognized commands and subcommands as `Runnable` or `Callable` tasks.
   
      - `CommandLine.DefaultExceptionHandler` prints the error message followed by usage help
 


Type Parameters:
`R` - the return type of this handler
Parameters:
`handler` - the function that will handle the result of successfully parsing the command line arguments
`args` - the command line arguments
Returns:
an object resulting from handling the parse result or the exception that occurred while parsing the input
Throws:
`CommandLine.ExecutionException` - if the command line arguments were parsed successfully but a problem occurred while processing the
      parse results; use `CommandLine.ExecutionException.getCommandLine()` to get the command or subcommand where processing failed
Since:
3.0
See Also:
`CommandLine.RunLast`, 
`CommandLine.RunAll`










    - 

#### parseWithHandlers


```
@Deprecated
public List<Object> parseWithHandlers(CommandLine.IParseResultHandler handler,
                                                   PrintStream out,
                                                   CommandLine.Help.Ansi ansi,
                                                   CommandLine.IExceptionHandler exceptionHandler,
                                                   String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead

Since:
2.0










    - 

#### parseWithHandlers


```
@Deprecated
public <R> R parseWithHandlers(CommandLine.IParseResultHandler2<R> handler,
                                            CommandLine.IExceptionHandler2<R> exceptionHandler,
                                            String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Tries to parse the specified command line arguments, and if successful, delegates
 the processing of the resulting `ParseResult` object to the specified handler.
 If the command line arguments were invalid, the `ParameterException` thrown from the `parse` method
 is caught and passed to the specified `CommandLine.IExceptionHandler2`.
 


 This is a convenience method intended to offer the same ease of use as the `run`
 and `call` methods, but with more flexibility and better
 support for nested subcommands.
 
 

Calling this method roughly expands to:
 

```

 ParseResult parseResult = null;
 try {
     parseResult = parseArgs(args);
     return handler.handleParseResult(parseResult);
 } catch (ParameterException ex) {
     return exceptionHandler.handleParseException(ex, (String[]) args);
 } catch (ExecutionException ex) {
     return exceptionHandler.handleExecutionException(ex, parseResult);
 }
 
```

 


 Picocli provides some default handlers that allow you to accomplish some common tasks with very little code.
 The following handlers are available:
 

   
      - `CommandLine.RunLast` handler prints help if requested, and otherwise gets the last specified command or subcommand
 and tries to execute it as a `Runnable` or `Callable`.
   
      - `CommandLine.RunFirst` handler prints help if requested, and otherwise executes the top-level command as a `Runnable` or `Callable`.
   
      - `CommandLine.RunAll` handler prints help if requested, and otherwise executes all recognized commands and subcommands as `Runnable` or `Callable` tasks.
   
      - `CommandLine.DefaultExceptionHandler` prints the error message followed by usage help
 


Type Parameters:
`R` - the return type of the result handler and exception handler
Parameters:
`handler` - the function that will handle the result of successfully parsing the command line arguments
`exceptionHandler` - the function that can handle the `ParameterException` thrown when the command line arguments are invalid
`args` - the command line arguments
Returns:
an object resulting from handling the parse result or the exception that occurred while parsing the input
Throws:
`CommandLine.ExecutionException` - if the command line arguments were parsed successfully but a problem occurred while processing the parse
      result `ParseResult` object; use `CommandLine.ExecutionException.getCommandLine()` to get the command or subcommand where processing failed
Since:
3.0
See Also:
`CommandLine.RunLast`, 
`CommandLine.RunAll`, 
`CommandLine.DefaultExceptionHandler`










    - 

#### usage


```
public static void usage(Object command,
                         PrintStream out)
```

Equivalent to `new CommandLine(command).usage(out)`. See `usage(PrintStream)` for details.

Parameters:
`command` - the object annotated with `CommandLine.Command`, `CommandLine.Option` and `CommandLine.Parameters`
`out` - the print stream to print the help message to
Throws:
`IllegalArgumentException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation










    - 

#### usage


```
public static void usage(Object command,
                         PrintStream out,
                         CommandLine.Help.Ansi ansi)
```

Equivalent to `new CommandLine(command).usage(out, ansi)`.
 See `usage(PrintStream, Help.Ansi)` for details.

Parameters:
`command` - the object annotated with `CommandLine.Command`, `CommandLine.Option` and `CommandLine.Parameters`
`out` - the print stream to print the help message to
`ansi` - whether the usage message should contain ANSI escape codes or not
Throws:
`IllegalArgumentException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation










    - 

#### usage


```
public static void usage(Object command,
                         PrintStream out,
                         CommandLine.Help.ColorScheme colorScheme)
```

Equivalent to `new CommandLine(command).usage(out, colorScheme)`.
 See `usage(PrintStream, Help.ColorScheme)` for details.

Parameters:
`command` - the object annotated with `CommandLine.Command`, `CommandLine.Option` and `CommandLine.Parameters`
`out` - the print stream to print the help message to
`colorScheme` - the `ColorScheme` defining the styles for options, parameters and commands when ANSI is enabled
Throws:
`IllegalArgumentException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation










    - 

#### usage


```
public void usage(PrintStream out)
```

Delegates to `usage(PrintStream, Help.ColorScheme)` with the configured color scheme.

Parameters:
`out` - the printStream to print to
See Also:
`usage(PrintStream, Help.ColorScheme)`










    - 

#### usage


```
public void usage(PrintWriter writer)
```

Delegates to `usage(PrintWriter, Help.ColorScheme)` with the configured color scheme.

Parameters:
`writer` - the PrintWriter to print to
Since:
3.0
See Also:
`usage(PrintWriter, Help.ColorScheme)`










    - 

#### usage


```
public void usage(PrintStream out,
                  CommandLine.Help.Ansi ansi)
```

Delegates to `usage(PrintStream, Help.ColorScheme)` with the default color scheme.

Parameters:
`out` - the printStream to print to
`ansi` - whether the usage message should include ANSI escape codes or not
See Also:
`usage(PrintStream, Help.ColorScheme)`










    - 

#### usage


```
public void usage(PrintWriter writer,
                  CommandLine.Help.Ansi ansi)
```

Similar to `usage(PrintStream, Help.Ansi)` but with the specified `PrintWriter` instead of a `PrintStream`.

Since:
3.0










    - 

#### usage


```
public void usage(PrintStream out,
                  CommandLine.Help.ColorScheme colorScheme)
```

Prints a usage help message for the annotated command class to the specified `PrintStream`.
 Delegates construction of the usage help message to the `CommandLine.Help` inner class and is equivalent to:
 

```

 Help.ColorScheme colorScheme = Help.defaultColorScheme(Help.Ansi.AUTO);
 Help help = getHelpFactory().create(getCommandSpec(), colorScheme)
 StringBuilder sb = new StringBuilder();
 for (String key : getHelpSectionKeys()) {
     IHelpSectionRenderer renderer = getHelpSectionMap().get(key);
     if (renderer != null) { sb.append(renderer.render(help)); }
 }
 out.print(sb);
 
```

 

Annotate your class with `CommandLine.Command` to control many aspects of the usage help message, including
 the program name, text of section headings and section contents, and some aspects of the auto-generated sections
 of the usage help message.
 

To customize the auto-generated sections of the usage help message, like how option details are displayed,
 instantiate a `CommandLine.Help` object and use a `CommandLine.Help.TextTable` with more of fewer columns, a custom
 layout, and/or a custom option renderer
 for ultimate control over which aspects of an Option or Field are displayed where.

Parameters:
`out` - the `PrintStream` to print the usage help message to
`colorScheme` - the `ColorScheme` defining the styles for options, parameters and commands when ANSI is enabled
See Also:
`CommandLine.Model.UsageMessageSpec`










    - 

#### usage


```
public void usage(PrintWriter writer,
                  CommandLine.Help.ColorScheme colorScheme)
```

Similar to `usage(PrintStream, Help.ColorScheme)`, but with the specified `PrintWriter` instead of a `PrintStream`.

Since:
3.0










    - 

#### getUsageMessage


```
public String getUsageMessage()
```

Similar to `usage(PrintStream)`, but returns the usage help message as a String instead of printing it to the `PrintStream`.

Since:
3.2










    - 

#### getUsageMessage


```
public String getUsageMessage(CommandLine.Help.Ansi ansi)
```

Similar to `usage(PrintStream, Help.Ansi)`, but returns the usage help message as a String instead of printing it to the `PrintStream`.

Since:
3.2










    - 

#### getUsageMessage


```
public String getUsageMessage(CommandLine.Help.ColorScheme colorScheme)
```

Similar to `usage(PrintStream, Help.ColorScheme)`, but returns the usage help message as a String instead of printing it to the `PrintStream`.

Since:
3.2










    - 

#### printVersionHelp


```
public void printVersionHelp(PrintStream out)
```

Delegates to `printVersionHelp(PrintStream, Help.Ansi)` with the ANSI setting of the configured color scheme.

Parameters:
`out` - the printStream to print to
Since:
0.9.8
See Also:
`printVersionHelp(PrintStream, Help.Ansi)`










    - 

#### printVersionHelp


```
public void printVersionHelp(PrintStream out,
                             CommandLine.Help.Ansi ansi)
```

Prints version information from the `CommandLine.Command.version()` annotation to the specified `PrintStream`.
 Each element of the array of version strings is printed on a separate line. Version strings may contain
 markup for colors and style.

Parameters:
`out` - the printStream to print to
`ansi` - whether the usage message should include ANSI escape codes or not
Since:
0.9.8
See Also:
`CommandLine.Command.version()`, 
`CommandLine.Option.versionHelp()`, 
`isVersionHelpRequested()`










    - 

#### printVersionHelp


```
public void printVersionHelp(PrintStream out,
                             CommandLine.Help.Ansi ansi,
                             Object... params)
```

Prints version information from the `CommandLine.Command.version()` annotation to the specified `PrintStream`.
 Each element of the array of version strings is formatted with the
 specified parameters, and printed on a separate line. Both version strings and parameters may contain
 markup for colors and style.

Parameters:
`out` - the printStream to print to
`ansi` - whether the usage message should include ANSI escape codes or not
`params` - Arguments referenced by the format specifiers in the version strings
Since:
1.0.0
See Also:
`CommandLine.Command.version()`, 
`CommandLine.Option.versionHelp()`, 
`isVersionHelpRequested()`










    - 

#### printVersionHelp


```
public void printVersionHelp(PrintWriter out)
```

Delegates to `printVersionHelp(PrintWriter, Help.Ansi, Object...)` with the ANSI setting of the configured color scheme.

Parameters:
`out` - the PrintWriter to print to
Since:
4.0










    - 

#### printVersionHelp


```
public void printVersionHelp(PrintWriter out,
                             CommandLine.Help.Ansi ansi,
                             Object... params)
```

Prints version information from the `CommandLine.Command.version()` annotation to the specified `PrintWriter`.
 Each element of the array of version strings is formatted with the
 specified parameters, and printed on a separate line. Both version strings and parameters may contain
 markup for colors and style.

Parameters:
`out` - the PrintWriter to print to
`ansi` - whether the usage message should include ANSI escape codes or not
`params` - Arguments referenced by the format specifiers in the version strings
Since:
4.0
See Also:
`CommandLine.Command.version()`, 
`CommandLine.Option.versionHelp()`, 
`isVersionHelpRequested()`












    - 

#### call


```
@Deprecated
public static <C extends Callable<T>,T> T call(C callable,
                                                            String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Equivalent to `new CommandLine(callable).execute(args)`, except for the return value.

Type Parameters:
`C` - the annotated object must implement Callable
`T` - the return type of the most specific command (must implement `Callable`)
Parameters:
`callable` - the command to call when parsing succeeds.
`args` - the command line arguments to parse
Returns:
`null` if an error occurred while parsing the command line options, or if help was requested and printed. Otherwise returns the result of calling the Callable
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Callable throws an exception
Since:
3.0
See Also:
`execute(String...)`












    - 

#### call


```
@Deprecated
public static <C extends Callable<T>,T> T call(C callable,
                                                            PrintStream out,
                                                            String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Delegates to `call(Callable, PrintStream, PrintStream, Help.Ansi, String...)` with `System.err` for
 diagnostic error messages and `CommandLine.Help.Ansi.AUTO`.

Type Parameters:
`C` - the annotated object must implement Callable
`T` - the return type of the most specific command (must implement `Callable`)
Parameters:
`callable` - the command to call when parsing succeeds.
`out` - the printStream to print the usage help message to when the user requested help
`args` - the command line arguments to parse
Returns:
`null` if an error occurred while parsing the command line options, or if help was requested and printed. Otherwise returns the result of calling the Callable
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Callable throws an exception
See Also:
`CommandLine.RunLast`












    - 

#### call


```
@Deprecated
public static <C extends Callable<T>,T> T call(C callable,
                                                            PrintStream out,
                                                            CommandLine.Help.Ansi ansi,
                                                            String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Delegates to `call(Callable, PrintStream, PrintStream, Help.Ansi, String...)` with `System.err` for diagnostic error messages.

Type Parameters:
`C` - the annotated object must implement Callable
`T` - the return type of the most specific command (must implement `Callable`)
Parameters:
`callable` - the command to call when parsing succeeds.
`out` - the printStream to print the usage help message to when the user requested help
`ansi` - the ANSI style to use
`args` - the command line arguments to parse
Returns:
`null` if an error occurred while parsing the command line options, or if help was requested and printed. Otherwise returns the result of calling the Callable
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Callable throws an exception
See Also:
`CommandLine.RunLast`












    - 

#### call


```
@Deprecated
public static <C extends Callable<T>,T> T call(C callable,
                                                            PrintStream out,
                                                            PrintStream err,
                                                            CommandLine.Help.Ansi ansi,
                                                            String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Convenience method to allow command line application authors to avoid some boilerplate code in their application.
 The annotated object needs to implement `Callable`.
 

Consider using the `execute(String...)` method instead:
 

```

 CommandLine cmd = new CommandLine(callable)
         .setOut(myOutWriter()) // System.out by default
         .setErr(myErrWriter()) // System.err by default
         .setColorScheme(myColorScheme()); // default color scheme, Ansi.AUTO by default
 int exitCode = cmd.execute(args);
 //System.exit(exitCode);
 
```

 


 If the specified Callable command has subcommands, the last subcommand specified on the
 command line is executed.
 

Type Parameters:
`C` - the annotated object must implement Callable
`T` - the return type of the specified `Callable`
Parameters:
`callable` - the command to call when parsing succeeds.
`out` - the printStream to print the usage help message to when the user requested help
`err` - the printStream to print diagnostic messages to
`ansi` - including whether the usage message should include ANSI escape codes or not
`args` - the command line arguments to parse
Returns:
`null` if an error occurred while parsing the command line options, or if help was requested and printed. Otherwise returns the result of calling the Callable
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Callable throws an exception
Since:
3.0










    - 

#### call


```
@Deprecated
public static <C extends Callable<T>,T> T call(Class<C> callableClass,
                                                            CommandLine.IFactory factory,
                                                            String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Equivalent to `new CommandLine(callableClass, factory).execute(args)`, except for the return value.

Type Parameters:
`C` - the annotated class must implement Callable
`T` - the return type of the most specific command (must implement `Callable`)
Parameters:
`callableClass` - class of the command to call when parsing succeeds.
`factory` - the factory responsible for instantiating the specified callable class and potentially inject other components
`args` - the command line arguments to parse
Returns:
`null` if an error occurred while parsing the command line options, or if help was requested and printed. Otherwise returns the result of calling the Callable
Throws:
`CommandLine.InitializationException` - if the specified class cannot be instantiated by the factory, or does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Callable throws an exception
Since:
3.2
See Also:
`execute(String...)`










    - 

#### call


```
@Deprecated
public static <C extends Callable<T>,T> T call(Class<C> callableClass,
                                                            CommandLine.IFactory factory,
                                                            PrintStream out,
                                                            String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Delegates to `call(Class, IFactory, PrintStream, PrintStream, Help.Ansi, String...)` with
 `System.err` for diagnostic error messages, and `CommandLine.Help.Ansi.AUTO`.

Type Parameters:
`C` - the annotated class must implement Callable
`T` - the return type of the most specific command (must implement `Callable`)
Parameters:
`callableClass` - class of the command to call when parsing succeeds.
`factory` - the factory responsible for instantiating the specified callable class and potentially injecting other components
`out` - the printStream to print the usage help message to when the user requested help
`args` - the command line arguments to parse
Returns:
`null` if an error occurred while parsing the command line options, or if help was requested and printed. Otherwise returns the result of calling the Callable
Throws:
`CommandLine.InitializationException` - if the specified class cannot be instantiated by the factory, or does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Callable throws an exception
Since:
3.2










    - 

#### call


```
@Deprecated
public static <C extends Callable<T>,T> T call(Class<C> callableClass,
                                                            CommandLine.IFactory factory,
                                                            PrintStream out,
                                                            CommandLine.Help.Ansi ansi,
                                                            String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Delegates to `call(Class, IFactory, PrintStream, PrintStream, Help.Ansi, String...)` with
 `System.err` for diagnostic error messages.

Type Parameters:
`C` - the annotated class must implement Callable
`T` - the return type of the most specific command (must implement `Callable`)
Parameters:
`callableClass` - class of the command to call when parsing succeeds.
`factory` - the factory responsible for instantiating the specified callable class and potentially injecting other components
`out` - the printStream to print the usage help message to when the user requested help
`ansi` - the ANSI style to use
`args` - the command line arguments to parse
Returns:
`null` if an error occurred while parsing the command line options, or if help was requested and printed. Otherwise returns the result of calling the Callable
Throws:
`CommandLine.InitializationException` - if the specified class cannot be instantiated by the factory, or does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Callable throws an exception
Since:
3.2










    - 

#### call


```
@Deprecated
public static <C extends Callable<T>,T> T call(Class<C> callableClass,
                                                            CommandLine.IFactory factory,
                                                            PrintStream out,
                                                            PrintStream err,
                                                            CommandLine.Help.Ansi ansi,
                                                            String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Convenience method to allow command line application authors to avoid some boilerplate code in their application.
 The specified factory will create an instance of the specified `callableClass`;
 use this method instead of `call(Callable, ...)`
 if you want to use a factory that performs Dependency Injection.
 The annotated class needs to implement `Callable`.
 

Consider using the `execute(String...)` method instead:
 

```

 CommandLine cmd = new CommandLine(callableClass, factory)
         .setOut(myOutWriter()) // System.out by default
         .setErr(myErrWriter()) // System.err by default
         .setColorScheme(myColorScheme()); // default color scheme, Ansi.AUTO by default
 int exitCode = cmd.execute(args);
 //System.exit(exitCode);
 
```

 


 If the specified Callable command has subcommands, the last subcommand specified on the
 command line is executed.
 

Type Parameters:
`C` - the annotated class must implement Callable
`T` - the return type of the most specific command (must implement `Callable`)
Parameters:
`callableClass` - class of the command to call when parsing succeeds.
`factory` - the factory responsible for instantiating the specified callable class and potentially injecting other components
`out` - the printStream to print the usage help message to when the user requested help
`err` - the printStream to print diagnostic messages to
`ansi` - the ANSI style to use
`args` - the command line arguments to parse
Returns:
`null` if an error occurred while parsing the command line options, or if help was requested and printed. Otherwise returns the result of calling the Callable
Throws:
`CommandLine.InitializationException` - if the specified class cannot be instantiated by the factory, or does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Callable throws an exception
Since:
3.2












    - 

#### run


```
@Deprecated
public static <R extends Runnable> void run(R runnable,
                                                         String... args)
```

Deprecated. use `execute(String...)` instead
Equivalent to `new CommandLine(runnable).execute(args)`.

Type Parameters:
`R` - the annotated object must implement Runnable
Parameters:
`runnable` - the command to run when parsing succeeds.
`args` - the command line arguments to parse
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Runnable throws an exception
Since:
3.0
See Also:
`execute(String...)`












    - 

#### run


```
@Deprecated
public static <R extends Runnable> void run(R runnable,
                                                         PrintStream out,
                                                         String... args)
```

Deprecated. use `execute(String...)` instead
Delegates to `run(Runnable, PrintStream, PrintStream, Help.Ansi, String...)` with `System.err` for diagnostic error messages and `CommandLine.Help.Ansi.AUTO`.

Type Parameters:
`R` - the annotated object must implement Runnable
Parameters:
`runnable` - the command to run when parsing succeeds.
`out` - the printStream to print the usage help message to when the user requested help
`args` - the command line arguments to parse
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Runnable throws an exception
See Also:
`CommandLine.RunLast`












    - 

#### run


```
@Deprecated
public static <R extends Runnable> void run(R runnable,
                                                         PrintStream out,
                                                         CommandLine.Help.Ansi ansi,
                                                         String... args)
```

Deprecated. use `execute(String...)` instead
Delegates to `run(Runnable, PrintStream, PrintStream, Help.Ansi, String...)` with `System.err` for diagnostic error messages.

Type Parameters:
`R` - the annotated object must implement Runnable
Parameters:
`runnable` - the command to run when parsing succeeds.
`out` - the printStream to print the usage help message to when the user requested help
`ansi` - whether the usage message should include ANSI escape codes or not
`args` - the command line arguments to parse
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Runnable throws an exception
See Also:
`CommandLine.RunLast`












    - 

#### run


```
@Deprecated
public static <R extends Runnable> void run(R runnable,
                                                         PrintStream out,
                                                         PrintStream err,
                                                         CommandLine.Help.Ansi ansi,
                                                         String... args)
```

Deprecated. use `execute(String...)` instead
Convenience method to allow command line application authors to avoid some boilerplate code in their application.
 The annotated object needs to implement `Runnable`.
 

Consider using the `execute(String...)` method instead:
 

```

 CommandLine cmd = new CommandLine(runnable)
         .setOut(myOutWriter()) // System.out by default
         .setErr(myErrWriter()) // System.err by default
         .setColorScheme(myColorScheme()); // default color scheme, Ansi.AUTO by default
 int exitCode = cmd.execute(args);
 //System.exit(exitCode);
 
```

 


 If the specified Runnable command has subcommands, the last subcommand specified on the
 command line is executed.
 


 From picocli v2.0, this method prints usage help or version help if requested,
 and any exceptions thrown by the `Runnable` are caught and rethrown wrapped in an `ExecutionException`.
 

Type Parameters:
`R` - the annotated object must implement Runnable
Parameters:
`runnable` - the command to run when parsing succeeds.
`out` - the printStream to print the usage help message to when the user requested help
`err` - the printStream to print diagnostic messages to
`ansi` - whether the usage message should include ANSI escape codes or not
`args` - the command line arguments to parse
Throws:
`CommandLine.InitializationException` - if the specified command object does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Runnable throws an exception
Since:
3.0










    - 

#### run


```
@Deprecated
public static <R extends Runnable> void run(Class<R> runnableClass,
                                                         CommandLine.IFactory factory,
                                                         String... args)
```

Deprecated. use `execute(String...)` instead
Equivalent to `new CommandLine(runnableClass, factory).execute(args)`.

Type Parameters:
`R` - the annotated class must implement Runnable
Parameters:
`runnableClass` - class of the command to run when parsing succeeds.
`factory` - the factory responsible for instantiating the specified Runnable class and potentially injecting other components
`args` - the command line arguments to parse
Throws:
`CommandLine.InitializationException` - if the specified class cannot be instantiated by the factory, or does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Runnable throws an exception
Since:
3.2
See Also:
`execute(String...)`










    - 

#### run


```
@Deprecated
public static <R extends Runnable> void run(Class<R> runnableClass,
                                                         CommandLine.IFactory factory,
                                                         PrintStream out,
                                                         String... args)
```

Deprecated. use `execute(String...)` instead
Delegates to `run(Class, IFactory, PrintStream, PrintStream, Help.Ansi, String...)` with
 `System.err` for diagnostic error messages, and `CommandLine.Help.Ansi.AUTO`.

Type Parameters:
`R` - the annotated class must implement Runnable
Parameters:
`runnableClass` - class of the command to run when parsing succeeds.
`factory` - the factory responsible for instantiating the specified Runnable class and potentially injecting other components
`out` - the printStream to print the usage help message to when the user requested help
`args` - the command line arguments to parse
Throws:
`CommandLine.InitializationException` - if the specified class cannot be instantiated by the factory, or does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Runnable throws an exception
Since:
3.2
See Also:
`run(Class, IFactory, PrintStream, PrintStream, Help.Ansi, String...)`, 
`parseWithHandlers(IParseResultHandler2, IExceptionHandler2, String...)`, 
`CommandLine.RunLast`










    - 

#### run


```
@Deprecated
public static <R extends Runnable> void run(Class<R> runnableClass,
                                                         CommandLine.IFactory factory,
                                                         PrintStream out,
                                                         CommandLine.Help.Ansi ansi,
                                                         String... args)
```

Deprecated. use `execute(String...)` instead
Delegates to `run(Class, IFactory, PrintStream, PrintStream, Help.Ansi, String...)` with
 `System.err` for diagnostic error messages.

Type Parameters:
`R` - the annotated class must implement Runnable
Parameters:
`runnableClass` - class of the command to run when parsing succeeds.
`factory` - the factory responsible for instantiating the specified Runnable class and potentially injecting other components
`out` - the printStream to print the usage help message to when the user requested help
`ansi` - whether the usage message should include ANSI escape codes or not
`args` - the command line arguments to parse
Throws:
`CommandLine.InitializationException` - if the specified class cannot be instantiated by the factory, or does not have a `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation
`CommandLine.ExecutionException` - if the Runnable throws an exception
Since:
3.2
See Also:
`run(Class, IFactory, PrintStream, PrintStream, Help.Ansi, String...)`, 
`parseWithHandlers(IParseResultHandler2, IExceptionHandler2, String...)`, 
`CommandLine.RunLast`










    - 

#### run


```
@Deprecated
public static <R extends Runnable> void run(Class<R> runnableClass,
                                                         CommandLine.IFactory factory,
                                                         PrintStream out,
                                                         PrintStream err,
                                                         CommandLine.Help.Ansi ansi,
                                                         String... args)
```

Deprecated. use `execute(String...)` instead
Convenience method to allow command line application authors to avoid some boilerplate code in their application.
 The specified factory will create an instance of the specified `runnableClass`;
 use this method instead of `run(Runnable, ...)`
 if you want to use a factory that performs Dependency Injection.
 The annotated class needs to implement `Runnable`.
 

Consider using the `execute(String...)` method instead:
 

```

 CommandLine cmd = new CommandLine(runnableClass, factory)
         .setOut(myOutWriter()) // System.out by default
         .setErr(myErrWriter()) // System.err by default
         .setColorScheme(myColorScheme()); // default color scheme, Ansi.AUTO by default
 int exitCode = cmd.execute(args);
 //System.exit(exitCode);
 
```

 


 If the specified Runnable command has subcommands, the last subcommand specified on the
 command line is executed.
 


 This method prints usage help or version help if requested,
 and any exceptions thrown by the `Runnable` are caught and rethrown wrapped in an `ExecutionException`.
 

Type Parameters:
`R` - the annotated class must implement Runnable
Parameters:
`runnableClass` - class of the command to run when parsing succeeds.
`factory` - the factory responsible for instantiating the specified Runnable class and potentially injecting other components
`out` - the printStream to print the usage help message to when the user requested help
`err` - the printStream to print diagnostic messages to
`ansi` - whether the usage message should include ANSI escape codes or not
`args` - the command line arguments to parse
Since:
3.2










    - 

#### invoke


```
@Deprecated
public static Object invoke(String methodName,
                                         Class<?> cls,
                                         String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Delegates to `invoke(String, Class, PrintStream, PrintStream, Help.Ansi, String...)` with `System.out` for
 requested usage help messages, `System.err` for diagnostic error messages, and `CommandLine.Help.Ansi.AUTO`.

Parameters:
`methodName` - the `@Command`-annotated method to build a `CommandLine.Model.CommandSpec` model from,
                   and run when parsing succeeds.
`cls` - the class where the `@Command`-annotated method is declared, or a subclass
`args` - the command line arguments to parse
Throws:
`CommandLine.InitializationException` - if the specified method does not have a `CommandLine.Command` annotation,
      or if the specified class contains multiple `@Command`-annotated methods with the specified name
`CommandLine.ExecutionException` - if the Runnable throws an exception
Since:
3.6
See Also:
`invoke(String, Class, PrintStream, PrintStream, Help.Ansi, String...)`, 
`parseWithHandlers(IParseResultHandler2, IExceptionHandler2, String...)`










    - 

#### invoke


```
@Deprecated
public static Object invoke(String methodName,
                                         Class<?> cls,
                                         PrintStream out,
                                         String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Delegates to `invoke(String, Class, PrintStream, PrintStream, Help.Ansi, String...)` with the specified stream for
 requested usage help messages, `System.err` for diagnostic error messages, and `CommandLine.Help.Ansi.AUTO`.

Parameters:
`methodName` - the `@Command`-annotated method to build a `CommandLine.Model.CommandSpec` model from,
                   and run when parsing succeeds.
`cls` - the class where the `@Command`-annotated method is declared, or a subclass
`out` - the printstream to print requested help message to
`args` - the command line arguments to parse
Throws:
`CommandLine.InitializationException` - if the specified method does not have a `CommandLine.Command` annotation,
      or if the specified class contains multiple `@Command`-annotated methods with the specified name
`CommandLine.ExecutionException` - if the Runnable throws an exception
Since:
3.6
See Also:
`invoke(String, Class, PrintStream, PrintStream, Help.Ansi, String...)`, 
`parseWithHandlers(IParseResultHandler2, IExceptionHandler2, String...)`










    - 

#### invoke


```
@Deprecated
public static Object invoke(String methodName,
                                         Class<?> cls,
                                         PrintStream out,
                                         CommandLine.Help.Ansi ansi,
                                         String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Delegates to `invoke(String, Class, PrintStream, PrintStream, Help.Ansi, String...)` with the specified stream for
 requested usage help messages, `System.err` for diagnostic error messages, and the specified Ansi mode.

Parameters:
`methodName` - the `@Command`-annotated method to build a `CommandLine.Model.CommandSpec` model from,
                   and run when parsing succeeds.
`cls` - the class where the `@Command`-annotated method is declared, or a subclass
`out` - the printstream to print requested help message to
`ansi` - whether the usage message should include ANSI escape codes or not
`args` - the command line arguments to parse
Throws:
`CommandLine.InitializationException` - if the specified method does not have a `CommandLine.Command` annotation,
      or if the specified class contains multiple `@Command`-annotated methods with the specified name
`CommandLine.ExecutionException` - if the Runnable throws an exception
Since:
3.6
See Also:
`invoke(String, Class, PrintStream, PrintStream, Help.Ansi, String...)`, 
`parseWithHandlers(IParseResultHandler2, IExceptionHandler2, String...)`










    - 

#### invoke


```
@Deprecated
public static Object invoke(String methodName,
                                         Class<?> cls,
                                         PrintStream out,
                                         PrintStream err,
                                         CommandLine.Help.Ansi ansi,
                                         String... args)
```

Deprecated. use `execute(String...)` and `getExecutionResult()` instead
Convenience method to allow command line application authors to avoid some boilerplate code in their application.
 Constructs a `CommandLine.Model.CommandSpec` model from the `@Option` and `@Parameters`-annotated method parameters
 of the `@Command`-annotated method, parses the specified command line arguments and invokes the specified method.
 

Consider using the `execute(String...)` method instead:
 

```

 Method commandMethod = getCommandMethods(cls, methodName).get(0);
 CommandLine cmd = new CommandLine(commandMethod)
         .setOut(myOutWriter()) // System.out by default
         .setErr(myErrWriter()) // System.err by default
         .setColorScheme(myColorScheme()); // default color scheme, Ansi.AUTO by default
 int exitCode = cmd.execute(args);
 //System.exit(exitCode);
 
```


Parameters:
`methodName` - the `@Command`-annotated method to build a `CommandLine.Model.CommandSpec` model from,
                   and run when parsing succeeds.
`cls` - the class where the `@Command`-annotated method is declared, or a subclass
`out` - the printStream to print the usage help message to when the user requested help
`err` - the printStream to print diagnostic messages to
`ansi` - whether the usage message should include ANSI escape codes or not
`args` - the command line arguments to parse
Throws:
`CommandLine.InitializationException` - if the specified method does not have a `CommandLine.Command` annotation,
      or if the specified class contains multiple `@Command`-annotated methods with the specified name
`CommandLine.ExecutionException` - if the method throws an exception
Since:
3.6










    - 

#### getCommandMethods


```
public static List<Method> getCommandMethods(Class<?> cls,
                                             String methodName)
```

Helper to get methods of a class annotated with `@Command` via reflection, optionally filtered by method name (not `@Command.name`).
 Methods have to be either public (inherited) members or be declared by `cls`, that is "inherited" static or protected methods will not be picked up.

Parameters:
`cls` - the class to search for methods annotated with `@Command`
`methodName` - if not `null`, return only methods whose method name (not `@Command.name`) equals this string. Ignored if `null`.
Returns:
the matching command methods, or an empty list
Since:
3.6.0
See Also:
`invoke(String, Class, String...)`










    - 

#### registerConverter


```
public <K> CommandLine registerConverter(Class<K> cls,
                                         CommandLine.ITypeConverter<K> converter)
```

Registers the specified type converter for the specified class. When initializing fields annotated with
 `CommandLine.Option`, the field's type is used as a lookup key to find the associated type converter, and this
 type converter converts the original command line argument string value to the correct type.
 


 Java 8 lambdas make it easy to register custom type converters:
 
 

```

 commandLine.registerConverter(java.nio.file.Path.class, s -> java.nio.file.Paths.get(s));
 commandLine.registerConverter(java.time.Duration.class, s -> java.time.Duration.parse(s));
```

 


 Built-in type converters are pre-registered for the following java 1.5 types:
 
 

   
      - all primitive types
   
      - all primitive wrapper types: Boolean, Byte, Character, Double, Float, Integer, Long, Short
   
      - any enum
   
      - java.io.File
   
      - java.math.BigDecimal
   
      - java.math.BigInteger
   
      - java.net.InetAddress
   
      - java.net.URI
   
      - java.net.URL
   
      - java.nio.charset.Charset
   
      - java.sql.Time
   
      - java.util.Date
   
      - java.util.UUID
   
      - java.util.regex.Pattern
   
      - StringBuilder
   
      - CharSequence
   
      - String
 

 

The specified converter will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment the converter is registered*. Subcommands added
 later will not have this converter added automatically. To ensure a custom type converter is available to all
 subcommands, register the type converter last, after adding subcommands.

Type Parameters:
`K` - the target type
Parameters:
`cls` - the target class to convert parameter string values to
`converter` - the class capable of converting string values to the specified target type
Returns:
this CommandLine object, to allow method chaining
See Also:
`addSubcommand(String, Object)`










    - 

#### getSeparator


```
public String getSeparator()
```

Returns the String that separates option names from option values when parsing command line options.

Returns:
the String the parser uses to separate option names from option values
See Also:
`CommandLine.Model.ParserSpec.separator()`










    - 

#### setSeparator


```
public CommandLine setSeparator(String separator)
```

Sets the String the parser uses to separate option names from option values to the specified value.
 The separator may also be set declaratively with the `CommandLine.Command.separator()` annotation attribute.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`separator` - the String that separates option names from option values
Returns:
this `CommandLine` object, to allow method chaining
See Also:
`CommandLine.Model.ParserSpec.separator(String)`










    - 

#### getResourceBundle


```
public ResourceBundle getResourceBundle()
```

Returns the ResourceBundle of this command or `null` if no resource bundle is set.

Since:
3.6
See Also:
`CommandLine.Command.resourceBundle()`, 
`CommandLine.Model.CommandSpec.resourceBundle()`










    - 

#### setResourceBundle


```
public CommandLine setResourceBundle(ResourceBundle bundle)
```

Sets the ResourceBundle containing usage help message strings.
 

The specified bundle will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will not be impacted. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`bundle` - the ResourceBundle containing usage help message strings
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.6
See Also:
`CommandLine.Command.resourceBundle()`, 
`CommandLine.Model.CommandSpec.resourceBundle(ResourceBundle)`










    - 

#### getUsageHelpWidth


```
public int getUsageHelpWidth()
```

Returns the maximum width of the usage help message. The default is 80.

See Also:
`CommandLine.Model.UsageMessageSpec.width()`










    - 

#### setUsageHelpWidth


```
public CommandLine setUsageHelpWidth(int width)
```

Sets the maximum width of the usage help message. Longer lines are wrapped.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`width` - the maximum width of the usage help message
Returns:
this `CommandLine` object, to allow method chaining
See Also:
`CommandLine.Model.UsageMessageSpec.width(int)`










    - 

#### getUsageHelpLongOptionsMaxWidth


```
public int getUsageHelpLongOptionsMaxWidth()
```

Returns the maximum usage help long options column max width to the specified value.
 This value controls the maximum width of the long options column: any positional parameter
 labels or long options that are longer than the specified value will overflow into
 the description column, and cause the description to be displayed on the next line.

Since:
4.2
See Also:
`CommandLine.Model.UsageMessageSpec.longOptionsMaxWidth()`










    - 

#### setUsageHelpLongOptionsMaxWidth


```
public CommandLine setUsageHelpLongOptionsMaxWidth(int columnWidth)
```

Returns the maximum usage help long options column max width to the specified value.
 This value controls the maximum width of the long options column: any positional parameter
 labels or long options that are longer than the specified value will overflow into
 the description column, and cause the description to be displayed on the next line.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`columnWidth` - the new maximum usage help long options column max width. Must be 20 or greater.
Returns:
this `CommandLine` object, to allow method chaining
Since:
4.2
See Also:
`CommandLine.Model.UsageMessageSpec.longOptionsMaxWidth(int)`










    - 

#### isUsageHelpAutoWidth


```
public boolean isUsageHelpAutoWidth()
```

Returns whether picocli should attempt to detect the terminal size and adjust the usage help message width
 to take the full terminal width. End users may enable this by setting system property `"picocli.usage.width"` to `AUTO`,
 and may disable this by setting this system property to a numeric value.
 This feature requires Java 7 or greater. The default is `false`.

Since:
4.0
See Also:
`CommandLine.Model.UsageMessageSpec.autoWidth()`










    - 

#### setUsageHelpAutoWidth


```
public CommandLine setUsageHelpAutoWidth(boolean detectTerminalSize)
```

Sets whether picocli should attempt to detect the terminal size and adjust the usage help message width
 to take the full terminal width. The default is `false`.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.

Parameters:
`detectTerminalSize` - whether picocli should attempt to detect the terminal size
Returns:
this `CommandLine` object, to allow method chaining
Since:
4.0
See Also:
`CommandLine.Model.UsageMessageSpec.autoWidth(boolean)`










    - 

#### getCommandName


```
public String getCommandName()
```

Returns the command name (also called program name) displayed in the usage help synopsis.

Returns:
the command name (also called program name) displayed in the usage
Since:
2.0
See Also:
`CommandLine.Model.CommandSpec.name()`










    - 

#### setCommandName


```
public CommandLine setCommandName(String commandName)
```

Sets the command name (also called program name) displayed in the usage help synopsis to the specified value.
 Note that this method only modifies the usage help message, it does not impact parsing behaviour.
 The command name may also be set declaratively with the `CommandLine.Command.name()` annotation attribute.

Parameters:
`commandName` - command name (also called program name) displayed in the usage help synopsis
Returns:
this `CommandLine` object, to allow method chaining
Since:
2.0
See Also:
`CommandLine.Model.CommandSpec.name(String)`










    - 

#### isExpandAtFiles


```
public boolean isExpandAtFiles()
```

Returns whether arguments starting with `'@'` should be treated as the path to an argument file and its
 contents should be expanded into separate arguments for each line in the specified file.
 This property is `true` by default.

Returns:
whether "argument files" or `@files` should be expanded into their content
Since:
2.1
See Also:
`CommandLine.Model.ParserSpec.expandAtFiles()`










    - 

#### setExpandAtFiles


```
public CommandLine setExpandAtFiles(boolean expandAtFiles)
```

Sets whether arguments starting with `'@'` should be treated as the path to an argument file and its
 contents should be expanded into separate arguments for each line in the specified file. (`true` by default.)

Parameters:
`expandAtFiles` - whether "argument files" or `@files` should be expanded into their content
Returns:
this `CommandLine` object, to allow method chaining
Since:
2.1
See Also:
`CommandLine.Model.ParserSpec.expandAtFiles(boolean)`










    - 

#### getAtFileCommentChar


```
public Character getAtFileCommentChar()
```

Returns the character that starts a single-line comment or `null` if all content of argument files should
 be interpreted as arguments (without comments).
 If specified, all characters from the comment character to the end of the line are ignored.

Returns:
the character that starts a single-line comment or `null`. The default is `'#'`.
Since:
3.5
See Also:
`CommandLine.Model.ParserSpec.atFileCommentChar()`










    - 

#### setAtFileCommentChar


```
public CommandLine setAtFileCommentChar(Character atFileCommentChar)
```

Sets the character that starts a single-line comment or `null` if all content of argument files should
 be interpreted as arguments (without comments).
 If specified, all characters from the comment character to the end of the line are ignored.

Parameters:
`atFileCommentChar` - the character that starts a single-line comment or `null`. The default is `'#'`.
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.5
See Also:
`CommandLine.Model.ParserSpec.atFileCommentChar(Character)`










    - 

#### isUseSimplifiedAtFiles


```
public boolean isUseSimplifiedAtFiles()
```

Returns whether to use a simplified argument file format that is compatible with JCommander.
 In this format, every line (except empty lines and comment lines)
 is interpreted as a single argument. Arguments containing whitespace do not need to be quoted.
 When system property `"picocli.useSimplifiedAtFiles"` is defined, the system property value overrides the programmatically set value.

Returns:
whether to use a simplified argument file format. The default is `false`.
Since:
3.9
See Also:
`CommandLine.Model.ParserSpec.useSimplifiedAtFiles()`










    - 

#### setUseSimplifiedAtFiles


```
public CommandLine setUseSimplifiedAtFiles(boolean simplifiedAtFiles)
```

Sets whether to use a simplified argument file format that is compatible with JCommander.
 In this format, every line (except empty lines and comment lines)
 is interpreted as a single argument. Arguments containing whitespace do not need to be quoted.
 When system property `"picocli.useSimplifiedAtFiles"` is defined, the system property value overrides the programmatically set value.

Parameters:
`simplifiedAtFiles` - whether to use a simplified argument file format. The default is `false`.
Returns:
this `CommandLine` object, to allow method chaining
Since:
3.9
See Also:
`CommandLine.Model.ParserSpec.useSimplifiedAtFiles(boolean)`










    - 

#### getNegatableOptionTransformer


```
public CommandLine.INegatableOptionTransformer getNegatableOptionTransformer()
```

Returns the `INegatableOptionTransformer` used to create the negative form of negatable options.
 By default this returns the result of `CommandLine.RegexTransformer.createDefault()`.

Returns:
the `INegatableOptionTransformer` used to create negative option names.
Since:
4.0
See Also:
`CommandLine.Option.negatable()`, 
`CommandLine.Model.CommandSpec.negatableOptionTransformer()`










    - 

#### setNegatableOptionTransformer


```
public CommandLine setNegatableOptionTransformer(CommandLine.INegatableOptionTransformer transformer)
```

Sets the `INegatableOptionTransformer` used to create the negative form of negatable options.
 

The specified setting will be registered with this `CommandLine` and the full hierarchy of its
 subcommands and nested sub-subcommands *at the moment this method is called*. Subcommands added
 later will have the default setting. To ensure a setting is applied to all
 subcommands, call the setter last, after adding subcommands.
 Note that `setOptionsCaseInsensitive(boolean)` will also change the case sensitivity of negatable options:
 any custom `CommandLine.INegatableOptionTransformer` that was previously installed will be replaced by the case-insensitive
 version of the default transformer. To ensure your custom transformer is used, install it last, after changing case sensitivity.

Parameters:
`transformer` - the `INegatableOptionTransformer` used to create negative option names.
Returns:
this `CommandLine` object, to allow method chaining
Since:
4.0
See Also:
`CommandLine.Option.negatable()`, 
`CommandLine.Model.CommandSpec.negatableOptionTransformer(CommandLine.INegatableOptionTransformer)`










    - 

#### defaultFactory


```
public static CommandLine.IFactory defaultFactory()
```

Returns the default `CommandLine.IFactory` implementation used if no factory was specified in the `CommandLine constructor`.
 

This implementation has special logic for instantiating `Collections`
 and `Maps`, and otherwise tries to create an instance by invoking the default constructor of the specified class.
 

Special logic for instantiating Collections and Maps:
 

```

 // if class is an interface that extends java.util.Collection, return a new instance of:
 1. List       -> ArrayList
 2. SortedSet  -> TreeSet
 3. Set        -> LinkedHashSet
 4. Queue      -> LinkedList
 5. Collection -> ArrayList

 // if extending or implementing java.util.Map:
 1. try invoking the default constructor; return this on success.
 2. if this fails, return a LinkedHashMap
 
```


Since:
4.0










    - 

#### tracer


```
public static CommandLine.Tracer tracer()
```

Returns the `Tracer` used internally for printing internal debug statements.

Returns:
the `Tracer` used internally for printing internal debug statements
Since:
4.7.7

















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