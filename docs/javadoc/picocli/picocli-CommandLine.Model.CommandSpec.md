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

## Class CommandLine.Model.CommandSpec






- java.lang.Object

- 



  - picocli.CommandLine.Model.CommandSpec









- 

Enclosing class:
CommandLine.Model


---




```
public static class CommandLine.Model.CommandSpec
extends Object
```

The `CommandSpec` class models a command specification, including the options, positional parameters and subcommands
 supported by the command, as well as attributes for the version help message and the usage help message of the command.
 


 Picocli views a command line application as a hierarchy of commands: there is a top-level command (usually the Java
 class with the `main` method) with optionally a set of command line options, positional parameters and subcommands.
 Subcommands themselves can have options, positional parameters and nested sub-subcommands to any level of depth.
 


 The object model has a corresponding hierarchy of `CommandSpec` objects, each with a set of `CommandLine.Model.OptionSpec`,
 `CommandLine.Model.PositionalParamSpec` and subcommands associated with it.
 This object model is used by the picocli command line interpreter and help message generator.
 

Picocli can construct a `CommandSpec` automatically from classes with `@Command`, `@Option` and
 `@Parameters` annotations. Alternatively a `CommandSpec` can be constructed programmatically.
 

Since:
3.0









- 




  - 



### Field Summary


Fields 

Modifier and Type
Field and Description


`static String`
`DEFAULT_COMMAND_NAME`
Constant String holding the default program name: `"<main class>" `.










  - 



### Method Summary


All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description


`CommandLine.Model.CommandSpec`
`add(CommandLine.Model.ArgSpec arg)`
Adds the specified option spec or positional parameter spec to the list of configured arguments to expect.



`CommandLine.Model.CommandSpec`
`addArgGroup(CommandLine.Model.ArgGroupSpec group)`
Adds the specified argument group to the groups in this command.



`CommandLine.Model.CommandSpec`
`addMethodSubcommands()`
Reflects on the class of the user object and registers any command methods
 (class methods annotated with `@Command`) as subcommands.



`CommandLine.Model.CommandSpec`
`addMethodSubcommands(CommandLine.IFactory factory)`
Reflects on the class of the user object and registers any command methods
 (class methods annotated with `@Command`) as subcommands.



`CommandLine.Model.CommandSpec`
`addMixin(String name,
        CommandLine.Model.CommandSpec mixin)`
Adds the specified mixin `CommandSpec` object to the map of mixins for this command.



`CommandLine.Model.CommandSpec`
`addMixin(String name,
        CommandLine.Model.CommandSpec mixin,
        CommandLine.Model.IAnnotatedElement annotatedElement)`
Adds the specified mixin `CommandSpec` object to the map of mixins for this command.



`CommandLine.Model.CommandSpec`
`addOption(CommandLine.Model.OptionSpec option)`
Adds the specified option spec to the list of configured arguments to expect.



`CommandLine.Model.CommandSpec`
`addParentCommandElement(CommandLine.Model.IAnnotatedElement spec)`
Adds the specified `{@literal @}ParentCommand`-annotated program element to the list of elements for this command.



`CommandLine.Model.CommandSpec`
`addPositional(CommandLine.Model.PositionalParamSpec positional)`
Adds the specified positional parameter spec to the list of configured arguments to expect.



`CommandLine.Model.CommandSpec`
`addSpecElement(CommandLine.Model.IAnnotatedElement spec)`
Adds the specified `{@literal @}Spec`-annotated program element to the list of elements for this command.



`CommandLine.Model.CommandSpec`
`addSubcommand(String name,
             CommandLine.Model.CommandSpec subcommand)`
Adds the specified subcommand with the specified name.



`CommandLine.Model.CommandSpec`
`addSubcommand(String name,
             CommandLine subCommandLine)`
Adds the specified subcommand with the specified name.



`CommandLine.Model.CommandSpec`
`addUnmatchedArgsBinding(CommandLine.Model.UnmatchedArgsBinding spec)`
Adds the specified `UnmatchedArgsBinding` to the list of model objects to capture unmatched arguments for this command.



`String[]`
`aliases()`
Returns the alias command names of this subcommand.



`CommandLine.Model.CommandSpec`
`aliases(String... aliases)`
Sets the alternative names by which this subcommand is recognized on the command line.



`List<CommandLine.Model.ArgGroupSpec>`
`argGroups()`
Returns the argument groups in this command.



`List<CommandLine.Model.ArgSpec>`
`args()`
Returns the list of all options and positional parameters configured for this command.



`CommandLine`
`commandLine()`
Returns the CommandLine constructed with this `CommandSpec` model.



`protected CommandLine.Model.CommandSpec`
`commandLine(CommandLine commandLine)`
Sets the CommandLine constructed with this `CommandSpec` model.



`static CommandLine.Model.CommandSpec`
`create()`
Creates and returns a new `CommandSpec` without any associated user object.



`CommandLine.IDefaultValueProvider`
`defaultValueProvider()`
Returns the default value provider for this command.



`CommandLine.Model.CommandSpec`
`defaultValueProvider(CommandLine.IDefaultValueProvider defaultValueProvider)`
Sets default value provider for this command.



`int`
`exitCodeOnExecutionException()`
Returns exit code signifying that an exception occurred when invoking the Runnable, Callable or Method user object of a command.



`CommandLine.Model.CommandSpec`
`exitCodeOnExecutionException(int newValue)`
Sets exit code signifying that an exception occurred when invoking the Runnable, Callable or Method user object of a command.



`int`
`exitCodeOnInvalidInput()`
Returns exit code for command line usage error.



`CommandLine.Model.CommandSpec`
`exitCodeOnInvalidInput(int newValue)`
Sets exit code for command line usage error.



`int`
`exitCodeOnSuccess()`
Returns exit code for successful termination.



`CommandLine.Model.CommandSpec`
`exitCodeOnSuccess(int newValue)`
Sets exit code for successful termination.



`int`
`exitCodeOnUsageHelp()`
Returns exit code for successful termination after printing usage help on user request.



`CommandLine.Model.CommandSpec`
`exitCodeOnUsageHelp(int newValue)`
Sets exit code for successful termination after printing usage help on user request.



`int`
`exitCodeOnVersionHelp()`
Returns exit code for successful termination after printing version help on user request.



`CommandLine.Model.CommandSpec`
`exitCodeOnVersionHelp(int newValue)`
Sets exit code for successful termination after printing version help on user request.



`CommandLine.Model.OptionSpec`
`findOption(char shortName)`
Returns the option with the specified short name, or `null` if no option with that name is defined for this command.



`CommandLine.Model.OptionSpec`
`findOption(String name)`
Returns the option with the specified name, or `null` if no option with that name is defined for this command.



`static CommandLine.Model.CommandSpec`
`forAnnotatedObject(Object userObject)`
Creates and returns a new `CommandSpec` initialized from the specified associated user object.



`static CommandLine.Model.CommandSpec`
`forAnnotatedObject(Object userObject,
                  CommandLine.IFactory factory)`
Creates and returns a new `CommandSpec` initialized from the specified associated user object.



`static CommandLine.Model.CommandSpec`
`forAnnotatedObjectLenient(Object userObject)`
Creates and returns a new `CommandSpec` initialized from the specified associated user object.



`static CommandLine.Model.CommandSpec`
`forAnnotatedObjectLenient(Object userObject,
                         CommandLine.IFactory factory)`
Creates and returns a new `CommandSpec` initialized from the specified associated user object.



`boolean`
`helpCommand()`
Returns whether this subcommand is a help command, and required options and positional
 parameters of the parent command should not be validated.



`CommandLine.Model.CommandSpec`
`helpCommand(boolean newValue)`
Sets whether this is a help command and required parameter checking should be suspended.



`boolean`
`inherited()`
Returns whether this command is inherited from a parent command.



`boolean`
`interpolateVariables()`
Returns whether variables should be interpolated in String values.



`CommandLine.Model.CommandSpec`
`interpolateVariables(Boolean interpolate)`
Sets whether variables should be interpolated in String values.



`boolean`
`isAddMethodSubcommands()`
Returns whether method commands should be added as subcommands.



`Map<String,CommandLine.Model.IAnnotatedElement>`
`mixinAnnotatedElements()`
Returns a map of the mixin names to mixin `IAnnotatedElement` objects for this command.



`Map<String,CommandLine.Model.CommandSpec>`
`mixins()`
Returns a map of the mixin names to mixin `CommandSpec` objects configured for this command.



`boolean`
`mixinStandardHelpOptions()`
Returns `true` if the standard help options have been mixed in with this command, `false` otherwise.



`CommandLine.Model.CommandSpec`
`mixinStandardHelpOptions(boolean newValue)`
Sets whether the standard help options should be mixed in with this command.



`CommandLine.IModelTransformer`
`modelTransformer()`
Returns the model transformer for this CommandSpec instance.



`CommandLine.Model.CommandSpec`
`modelTransformer(CommandLine.IModelTransformer modelTransformer)`
Sets the model transformer for this CommandSpec instance.



`String`
`name()`
Returns name of this command.



`CommandLine.Model.CommandSpec`
`name(String name)`
Sets the String to use as the program name in the synopsis line of the help message.



`Set<String>`
`names()`
Returns all names of this command, including `name()` and `aliases()`.



`CommandLine.INegatableOptionTransformer`
`negatableOptionTransformer()`
Returns the `INegatableOptionTransformer` used to create the negative form of negatable options.



`CommandLine.Model.CommandSpec`
`negatableOptionTransformer(CommandLine.INegatableOptionTransformer newValue)`
Sets the `INegatableOptionTransformer` used to create the negative form of negatable options.



`Map<String,CommandLine.Model.OptionSpec>`
`negatedOptionsMap()`
Returns a map of the negated option names to option spec objects configured for this command.



`List<CommandLine.Model.OptionSpec>`
`options()`
Returns the list of options configured for this command.



`boolean`
`optionsCaseInsensitive()`
Returns whether the options are case-insensitive.



`CommandLine.Model.CommandSpec`
`optionsCaseInsensitive(boolean caseInsensitiveOptions)`
Sets the case-insensitivity of options.



`Map<String,CommandLine.Model.OptionSpec>`
`optionsMap()`
Returns a map of the option names to option spec objects configured for this command.



`CommandLine.Model.CommandSpec`
`parent()`
Returns the parent command of this subcommand, or `null` if this is a top-level command.



`CommandLine.Model.CommandSpec`
`parent(CommandLine.Model.CommandSpec parent)`
Sets the parent command of this subcommand.



`List<CommandLine.Model.IAnnotatedElement>`
`parentCommandElements()`
Returns the list of program elements annotated with `{@literal @}ParentCommand` configured for this command.



`CommandLine.Model.ParserSpec`
`parser()`
Returns the parser specification for this command.



`CommandLine.Model.CommandSpec`
`parser(CommandLine.Model.ParserSpec settings)`
Initializes the parser specification for this command from the specified settings and returns this commandSpec.



`List<CommandLine.Model.PositionalParamSpec>`
`positionalParameters()`
Returns the list of positional parameters configured for this command.



`Map<Character,CommandLine.Model.OptionSpec>`
`posixOptionsMap()`
Returns a map of the short (single character) option names to option spec objects configured for this command.



`CommandLine.IParameterPreprocessor`
`preprocessor()`
Returns the preprocessor for this CommandSpec instance.



`CommandLine.Model.CommandSpec`
`preprocessor(CommandLine.IParameterPreprocessor preprocessor)`
Sets the preprocessor for this CommandSpec instance.



`String`
`qualifiedName()`
Returns the String to use as the program name in the synopsis line of the help message:
 this command's `name`, preceded by the qualified name of the parent command, if any, separated by a space.



`String`
`qualifiedName(String separator)`
Returns this command's fully qualified name, which is its `name`, preceded by the qualified name of the parent command, if this command has a parent command.



`CommandLine.Model.CommandSpec`
`remove(CommandLine.Model.ArgSpec arg)`
(INCUBATING) Removes the specified option spec or positional parameter spec from the list of configured arguments to expect.



`CommandLine`
`removeSubcommand(String name)`
Removes the subcommand with the specified name or alias from this CommandSpec and
 returns the `CommandLine` instance that was associated with the specified name,
 or `null` of the specified name was not associated with a subcommand.



`List<CommandLine.Model.ArgSpec>`
`requiredArgs()`
Returns the list of required options and positional parameters configured for this command.



`ResourceBundle`
`resourceBundle()`
Returns the resource bundle for this command.



`CommandLine.Model.CommandSpec`
`resourceBundle(ResourceBundle bundle)`
Initializes the resource bundle for this command: sets the `UsageMessageSpec.messages` to
 a `Messages` object created from this command spec and the specified bundle, and then sets the
 `ArgSpec.messages` of all options and positional parameters in this command
 to the same `Messages` instance.



`String`
`resourceBundleBaseName()`
Returns the resource bundle base name for this command.



`CommandLine.Model.CommandSpec`
`resourceBundleBaseName(String resourceBundleBaseName)`
Initializes the resource bundle for this command: sets the `UsageMessageSpec.messages` to
 a `Messages` object created from this command spec and the specified bundle, and then sets the
 `ArgSpec.messages` of all options and positional parameters in this command
 to the same `Messages` instance.



`CommandLine.Model.CommandSpec`
`root()`
Returns the root command: the top-level command of the hierarchy, never `null`.



`CommandLine.ScopeType`
`scopeType()`
Returns the scope of this argument; is it local, or inherited (it applies to this command as well as all sub- and sub-subcommands).



`CommandLine.Model.CommandSpec`
`scopeType(CommandLine.ScopeType scopeType)`
Sets the scope of where this argument applies: only this command, or also all sub (and sub-sub) commands, and returns this builder.



`CommandLine.Model.CommandSpec`
`setAddMethodSubcommands(Boolean addMethodSubcommands)`
Sets whether method commands should be added as subcommands.



`List<CommandLine.Model.IAnnotatedElement>`
`specElements()`
Returns the list of program elements annotated with `{@literal @}Spec` configured for this command.



`Map<String,CommandLine>`
`subcommands()`
Returns a read-only view of the subcommand map.



`boolean`
`subcommandsCaseInsensitive()`
Returns whether the subcommands are case-insensitive.



`CommandLine.Model.CommandSpec`
`subcommandsCaseInsensitive(boolean caseInsensitiveSubcommands)`
Sets the case-insensitivity of subcommands.



`boolean`
`subcommandsRepeatable()`
Returns whether the subcommands of this command are repeatable, that is, whether such subcommands can
 occur multiple times and may be followed by sibling commands instead of just child commands.



`CommandLine.Model.CommandSpec`
`subcommandsRepeatable(boolean subcommandsRepeatable)`
Sets whether the subcommands of this command are repeatable, that is, whether such subcommands can
 occur multiple times and may be followed by sibling commands instead of just child commands.



`String`
`toString()`
Returns a string representation of this command, used in error messages and trace messages.



`List<CommandLine.Model.UnmatchedArgsBinding>`
`unmatchedArgsBindings()`
Returns the list of `UnmatchedArgumentsBindings` configured for this command;
 each `UnmatchedArgsBinding` captures the arguments that could not be matched to any options or positional parameters.



`void`
`updateCommandAttributes(CommandLine.Command cmd,
                       CommandLine.IFactory factory)`
Updates the following attributes from the specified `@Command` annotation:
 aliases, `parser separator`, command name, version, help command,
 version provider, default provider and `usage message spec`.



`CommandLine.Model.UsageMessageSpec`
`usageMessage()`
Returns the usage help message specification for this command.



`CommandLine.Model.CommandSpec`
`usageMessage(CommandLine.Model.UsageMessageSpec settings)`
Initializes the usageMessage specification for this command from the specified settings and returns this commandSpec.



`Object`
`userObject()`
Returns the user object associated with this command.



`String[]`
`version()`
Returns version information for this command, to print to the console when the user specifies an
 option to request version help.



`CommandLine.Model.CommandSpec`
`version(String... version)`
Sets version information literals for this command, to print to the console when the user specifies an
 option to request version help.



`CommandLine.IVersionProvider`
`versionProvider()`
Returns the version provider for this command, to generate the `version()` strings.



`CommandLine.Model.CommandSpec`
`versionProvider(CommandLine.IVersionProvider versionProvider)`
Sets version provider for this command, to generate the `version()` strings.



`CommandLine.Model.CommandSpec`
`withToString(String newValue)`
Sets the string representation of this command, used in error messages and trace messages.



`static CommandLine.Model.CommandSpec`
`wrapWithoutInspection(Object userObject)`
Creates and returns a new `CommandSpec` with the specified associated user object.



`static CommandLine.Model.CommandSpec`
`wrapWithoutInspection(Object userObject,
                     CommandLine.IFactory factory)`
Creates and returns a new `CommandSpec` with the specified associated user object.






    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`













- 




  - 



### Field Detail







    - 

#### DEFAULT_COMMAND_NAME


```
public static final String DEFAULT_COMMAND_NAME
```

Constant String holding the default program name: `"<main class>" `.

Since:
4.0
See Also:
Constant Field Values











  - 



### Method Detail







    - 

#### create


```
public static CommandLine.Model.CommandSpec create()
```

Creates and returns a new `CommandSpec` without any associated user object.









    - 

#### wrapWithoutInspection


```
public static CommandLine.Model.CommandSpec wrapWithoutInspection(Object userObject)
```

Creates and returns a new `CommandSpec` with the specified associated user object.
 The specified user object is *not* inspected for annotations.

Parameters:
`userObject` - the associated user object. May be any object, may be `null`.










    - 

#### wrapWithoutInspection


```
public static CommandLine.Model.CommandSpec wrapWithoutInspection(Object userObject,
                                                                  CommandLine.IFactory factory)
```

Creates and returns a new `CommandSpec` with the specified associated user object.
 The specified user object is *not* inspected for annotations.

Parameters:
`userObject` - the associated user object. May be any object, may be `null`.
`factory` - the factory used to create instances of subcommands, converters, etc., that are registered declaratively with annotation attributes
Since:
4.2










    - 

#### forAnnotatedObject


```
public static CommandLine.Model.CommandSpec forAnnotatedObject(Object userObject)
```

Creates and returns a new `CommandSpec` initialized from the specified associated user object. The specified
 user object must have at least one `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation.

Parameters:
`userObject` - the user object annotated with `CommandLine.Command`, `CommandLine.Option` and/or `CommandLine.Parameters` annotations.
Throws:
`CommandLine.InitializationException` - if the specified object has no picocli annotations or has invalid annotations










    - 

#### forAnnotatedObject


```
public static CommandLine.Model.CommandSpec forAnnotatedObject(Object userObject,
                                                               CommandLine.IFactory factory)
```

Creates and returns a new `CommandSpec` initialized from the specified associated user object. The specified
 user object must have at least one `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotation.

Parameters:
`userObject` - the user object annotated with `CommandLine.Command`, `CommandLine.Option` and/or `CommandLine.Parameters` annotations.
`factory` - the factory used to create instances of subcommands, converters, etc., that are registered declaratively with annotation attributes
Throws:
`CommandLine.InitializationException` - if the specified object has no picocli annotations or has invalid annotations










    - 

#### forAnnotatedObjectLenient


```
public static CommandLine.Model.CommandSpec forAnnotatedObjectLenient(Object userObject)
```

Creates and returns a new `CommandSpec` initialized from the specified associated user object. If the specified
 user object has no `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotations, an empty `CommandSpec` is returned.

Parameters:
`userObject` - the user object annotated with `CommandLine.Command`, `CommandLine.Option` and/or `CommandLine.Parameters` annotations.
Throws:
`CommandLine.InitializationException` - if the specified object has invalid annotations










    - 

#### forAnnotatedObjectLenient


```
public static CommandLine.Model.CommandSpec forAnnotatedObjectLenient(Object userObject,
                                                                      CommandLine.IFactory factory)
```

Creates and returns a new `CommandSpec` initialized from the specified associated user object. If the specified
 user object has no `CommandLine.Command`, `CommandLine.Option` or `CommandLine.Parameters` annotations, an empty `CommandSpec` is returned.

Parameters:
`userObject` - the user object annotated with `CommandLine.Command`, `CommandLine.Option` and/or `CommandLine.Parameters` annotations.
`factory` - the factory used to create instances of subcommands, converters, etc., that are registered declaratively with annotation attributes
Throws:
`CommandLine.InitializationException` - if the specified object has invalid annotations










    - 

#### userObject


```
public Object userObject()
```

Returns the user object associated with this command.

See Also:
`CommandLine.getCommand()`










    - 

#### commandLine


```
public CommandLine commandLine()
```

Returns the CommandLine constructed with this `CommandSpec` model.









    - 

#### commandLine


```
protected CommandLine.Model.CommandSpec commandLine(CommandLine commandLine)
```

Sets the CommandLine constructed with this `CommandSpec` model.









    - 

#### parser


```
public CommandLine.Model.ParserSpec parser()
```

Returns the parser specification for this command.









    - 

#### parser


```
public CommandLine.Model.CommandSpec parser(CommandLine.Model.ParserSpec settings)
```

Initializes the parser specification for this command from the specified settings and returns this commandSpec.









    - 

#### usageMessage


```
public CommandLine.Model.UsageMessageSpec usageMessage()
```

Returns the usage help message specification for this command.









    - 

#### usageMessage


```
public CommandLine.Model.CommandSpec usageMessage(CommandLine.Model.UsageMessageSpec settings)
```

Initializes the usageMessage specification for this command from the specified settings and returns this commandSpec.









    - 

#### subcommandsCaseInsensitive


```
public boolean subcommandsCaseInsensitive()
```

Returns whether the subcommands are case-insensitive.

Since:
4.3










    - 

#### subcommandsCaseInsensitive


```
public CommandLine.Model.CommandSpec subcommandsCaseInsensitive(boolean caseInsensitiveSubcommands)
```

Sets the case-insensitivity of subcommands.

Since:
4.3










    - 

#### optionsCaseInsensitive


```
public boolean optionsCaseInsensitive()
```

Returns whether the options are case-insensitive.

Since:
4.3










    - 

#### optionsCaseInsensitive


```
public CommandLine.Model.CommandSpec optionsCaseInsensitive(boolean caseInsensitiveOptions)
```

Sets the case-insensitivity of options.
 Note that changing case sensitivity will also change the case sensitivity of negatable options:
 any custom `CommandLine.INegatableOptionTransformer` that was previously installed will be replaced by the case-insensitive
 version of the default transformer. To ensure your custom transformer is used, install it last, after changing case sensitivity.

Since:
4.3










    - 

#### resourceBundleBaseName


```
public String resourceBundleBaseName()
```

Returns the resource bundle base name for this command.

Returns:
the resource bundle base name from the CommandLine.Model.UsageMessageSpec.messages()
Since:
4.0










    - 

#### resourceBundleBaseName


```
public CommandLine.Model.CommandSpec resourceBundleBaseName(String resourceBundleBaseName)
```

Initializes the resource bundle for this command: sets the `UsageMessageSpec.messages` to
 a `Messages` object created from this command spec and the specified bundle, and then sets the
 `ArgSpec.messages` of all options and positional parameters in this command
 to the same `Messages` instance. Subcommands are not modified.
 

This method is preferable to `resourceBundle(ResourceBundle)` for pre-Java 8

Parameters:
`resourceBundleBaseName` - the base name of the ResourceBundle to set, may be `null`
Returns:
this commandSpec
Since:
4.0
See Also:
`addSubcommand(String, CommandLine)`










    - 

#### resourceBundle


```
public ResourceBundle resourceBundle()
```

Returns the resource bundle for this command.

Returns:
the resource bundle from the CommandLine.Model.UsageMessageSpec.messages()
Since:
3.6










    - 

#### resourceBundle


```
public CommandLine.Model.CommandSpec resourceBundle(ResourceBundle bundle)
```

Initializes the resource bundle for this command: sets the `UsageMessageSpec.messages` to
 a `Messages` object created from this command spec and the specified bundle, and then sets the
 `ArgSpec.messages` of all options and positional parameters in this command
 to the same `Messages` instance. Subcommands are not modified.

Parameters:
`bundle` - the ResourceBundle to set, may be `null`
Returns:
this commandSpec
Since:
3.6
See Also:
`addSubcommand(String, CommandLine)`










    - 

#### subcommands


```
public Map<String,CommandLine> subcommands()
```

Returns a read-only view of the subcommand map.









    - 

#### addSubcommand


```
public CommandLine.Model.CommandSpec addSubcommand(String name,
                                                   CommandLine.Model.CommandSpec subcommand)
```

Adds the specified subcommand with the specified name.
 If the specified subcommand does not have a ResourceBundle set, it is initialized to the ResourceBundle of this command spec.

Parameters:
`name` - subcommand name - the preferred subcommand name to register the subcommand under.
             If `null`, the name of the specified subcommand is used;
             if this is also `null`, the first alias is used.
             When this String is encountered in the command line arguments, the subcommand is invoked.
`subcommand` - describes the subcommand to envoke when the name is encountered on the command line
Returns:
this `CommandSpec` object for method chaining
Throws:
`CommandLine.InitializationException` - if the specified name is `null`, and no alternative name could be found,
          or if another subcommand was already registered under the same name, or if one of the aliases
          of the specified subcommand was already used by another subcommand.










    - 

#### addSubcommand


```
public CommandLine.Model.CommandSpec addSubcommand(String name,
                                                   CommandLine subCommandLine)
```

Adds the specified subcommand with the specified name.
 If the specified subcommand does not have a ResourceBundle set, it is initialized to the ResourceBundle of this command spec.

Parameters:
`name` - subcommand name - the preferred subcommand name to register the subcommand under.
             If `null`, the name of the specified subcommand is used;
             if this is also `null`, the first alias is used.
             When this String is encountered in the command line arguments, the subcommand is invoked.
`subCommandLine` - the subcommand to envoke when the name is encountered on the command line
Returns:
this `CommandSpec` object for method chaining
Throws:
`CommandLine.InitializationException` - if the specified name is `null`, and no alternative name could be found,
          or if another subcommand was already registered under the same name, or if one of the aliases
          of the specified subcommand was already used by another subcommand.










    - 

#### removeSubcommand


```
public CommandLine removeSubcommand(String name)
```

Removes the subcommand with the specified name or alias from this CommandSpec and
 returns the `CommandLine` instance that was associated with the specified name,
 or `null` of the specified name was not associated with a subcommand.

Parameters:
`name` - name or alias of the subcommand to remove; may be
      `abbreviated` or `case-insensitive`
Returns:
the removed `CommandLine` instance or `null`
Since:
4.6










    - 

#### isAddMethodSubcommands


```
public boolean isAddMethodSubcommands()
```

Returns whether method commands should be added as subcommands. True by default. Used by the annotation processor.

Since:
4.0










    - 

#### setAddMethodSubcommands


```
public CommandLine.Model.CommandSpec setAddMethodSubcommands(Boolean addMethodSubcommands)
```

Sets whether method commands should be added as subcommands. True by default. Used by the annotation processor.

Since:
4.0










    - 

#### interpolateVariables


```
public boolean interpolateVariables()
```

Returns whether variables should be interpolated in String values. True by default.

Since:
4.0










    - 

#### interpolateVariables


```
public CommandLine.Model.CommandSpec interpolateVariables(Boolean interpolate)
```

Sets whether variables should be interpolated in String values. True by default.

Since:
4.0










    - 

#### addMethodSubcommands


```
public CommandLine.Model.CommandSpec addMethodSubcommands()
```

Reflects on the class of the user object and registers any command methods
 (class methods annotated with `@Command`) as subcommands.

Returns:
this `CommandLine.Model.CommandSpec` object for method chaining
Since:
3.6.0
See Also:
`addMethodSubcommands(CommandLine.IFactory)`, 
`addSubcommand(String, CommandLine)`










    - 

#### addMethodSubcommands


```
public CommandLine.Model.CommandSpec addMethodSubcommands(CommandLine.IFactory factory)
```

Reflects on the class of the user object and registers any command methods
 (class methods annotated with `@Command`) as subcommands.

Parameters:
`factory` - the factory used to create instances of subcommands, converters, etc., that are registered declaratively with annotation attributes
Returns:
this `CommandLine.Model.CommandSpec` object for method chaining
Since:
3.7.0
See Also:
`addSubcommand(String, CommandLine)`










    - 

#### parent


```
public CommandLine.Model.CommandSpec parent()
```

Returns the parent command of this subcommand, or `null` if this is a top-level command.









    - 

#### root


```
public CommandLine.Model.CommandSpec root()
```

Returns the root command: the top-level command of the hierarchy, never `null`.

Since:
4.3










    - 

#### parent


```
public CommandLine.Model.CommandSpec parent(CommandLine.Model.CommandSpec parent)
```

Sets the parent command of this subcommand.

Returns:
this CommandSpec for method chaining










    - 

#### add


```
public CommandLine.Model.CommandSpec add(CommandLine.Model.ArgSpec arg)
```

Adds the specified option spec or positional parameter spec to the list of configured arguments to expect.

Parameters:
`arg` - the option spec or positional parameter spec to add
Returns:
this CommandSpec for method chaining










    - 

#### addOption


```
public CommandLine.Model.CommandSpec addOption(CommandLine.Model.OptionSpec option)
```

Adds the specified option spec to the list of configured arguments to expect.
 The option's CommandLine.Model.ArgSpec.description() may now return Strings from this
 CommandSpec's messages.
 The option parameter's CommandLine.Model.ArgSpec.defaultValueString() may
 now return Strings from this CommandSpec's `defaultValueProvider()` IDefaultValueProvider}.

Parameters:
`option` - the option spec to add
Returns:
this CommandSpec for method chaining
Throws:
`CommandLine.DuplicateOptionAnnotationsException` - if any of the names of the specified option is the same as the name of another option










    - 

#### addPositional


```
public CommandLine.Model.CommandSpec addPositional(CommandLine.Model.PositionalParamSpec positional)
```

Adds the specified positional parameter spec to the list of configured arguments to expect.
 The positional parameter's CommandLine.Model.ArgSpec.description() may
 now return Strings from this CommandSpec's messages.
 The positional parameter's CommandLine.Model.ArgSpec.defaultValueString() may
 now return Strings from this CommandSpec's `defaultValueProvider()` IDefaultValueProvider}.

Parameters:
`positional` - the positional parameter spec to add
Returns:
this CommandSpec for method chaining










    - 

#### remove


```
public CommandLine.Model.CommandSpec remove(CommandLine.Model.ArgSpec arg)
```

(INCUBATING) Removes the specified option spec or positional parameter spec from the list of configured arguments to expect.

Parameters:
`arg` - the option spec or positional parameter spec to remove
Returns:
this CommandSpec for method chaining
Throws:
`UnsupportedOperationException` - if the specified ArgSpec is part of a `CommandLine.Model.ArgGroupSpec`
`NoSuchElementException` - if the specified ArgSpec is not part of this `CommandSpec`
Since:
4.0










    - 

#### addArgGroup


```
public CommandLine.Model.CommandSpec addArgGroup(CommandLine.Model.ArgGroupSpec group)
```

Adds the specified argument group to the groups in this command.

Parameters:
`group` - the group spec to add
Returns:
this CommandSpec for method chaining
Throws:
`CommandLine.InitializationException` - if the specified group or one of its ancestors has already been added
Since:
4.0










    - 

#### addMixin


```
public CommandLine.Model.CommandSpec addMixin(String name,
                                              CommandLine.Model.CommandSpec mixin,
                                              CommandLine.Model.IAnnotatedElement annotatedElement)
```

Adds the specified mixin `CommandSpec` object to the map of mixins for this command.

Parameters:
`name` - the name that can be used to later retrieve the mixin
`mixin` - the mixin whose options and positional parameters and other attributes to add to this command
`annotatedElement` - the `@Mixin`-annotated program element
Returns:
this CommandSpec for method chaining
Since:
4.1
See Also:
`mixinAnnotatedElements()`










    - 

#### addMixin


```
public CommandLine.Model.CommandSpec addMixin(String name,
                                              CommandLine.Model.CommandSpec mixin)
```

Adds the specified mixin `CommandSpec` object to the map of mixins for this command.

Parameters:
`name` - the name that can be used to later retrieve the mixin
`mixin` - the mixin whose options and positional parameters and other attributes to add to this command
Returns:
this CommandSpec for method chaining










    - 

#### addUnmatchedArgsBinding


```
public CommandLine.Model.CommandSpec addUnmatchedArgsBinding(CommandLine.Model.UnmatchedArgsBinding spec)
```

Adds the specified `UnmatchedArgsBinding` to the list of model objects to capture unmatched arguments for this command.

Parameters:
`spec` - the unmatched arguments binding to capture unmatched arguments
Returns:
this CommandSpec for method chaining










    - 

#### addSpecElement


```
public CommandLine.Model.CommandSpec addSpecElement(CommandLine.Model.IAnnotatedElement spec)
```

Adds the specified `{@literal @}Spec`-annotated program element to the list of elements for this command.

Returns:
this CommandSpec for method chaining
Since:
4.0










    - 

#### addParentCommandElement


```
public CommandLine.Model.CommandSpec addParentCommandElement(CommandLine.Model.IAnnotatedElement spec)
```

Adds the specified `{@literal @}ParentCommand`-annotated program element to the list of elements for this command.

Returns:
this CommandSpec for method chaining
Since:
4.0










    - 

#### mixins


```
public Map<String,CommandLine.Model.CommandSpec> mixins()
```

Returns a map of the mixin names to mixin `CommandSpec` objects configured for this command.

Returns:
an immutable map of mixins added to this command.










    - 

#### mixinAnnotatedElements


```
public Map<String,CommandLine.Model.IAnnotatedElement> mixinAnnotatedElements()
```

Returns a map of the mixin names to mixin `IAnnotatedElement` objects for this command.

Returns:
an immutable map of `@Mixin`-annotated elements added to this command.
Since:
4.1
See Also:
`addMixin(String, CommandLine.Model.CommandSpec, CommandLine.Model.IAnnotatedElement)`










    - 

#### options


```
public List<CommandLine.Model.OptionSpec> options()
```

Returns the list of options configured for this command.

Returns:
an immutable list of options that this command recognizes.










    - 

#### positionalParameters


```
public List<CommandLine.Model.PositionalParamSpec> positionalParameters()
```

Returns the list of positional parameters configured for this command.

Returns:
an immutable list of positional parameters that this command recognizes.










    - 

#### argGroups


```
public List<CommandLine.Model.ArgGroupSpec> argGroups()
```

Returns the argument groups in this command.

Returns:
an immutable list of groups of options and positional parameters in this command
Since:
4.0










    - 

#### optionsMap


```
public Map<String,CommandLine.Model.OptionSpec> optionsMap()
```

Returns a map of the option names to option spec objects configured for this command.

Returns:
an immutable map of options that this command recognizes.










    - 

#### negatedOptionsMap


```
public Map<String,CommandLine.Model.OptionSpec> negatedOptionsMap()
```

Returns a map of the negated option names to option spec objects configured for this command.

Returns:
an immutable map of negatable options that this command recognizes.
Since:
4.0










    - 

#### posixOptionsMap


```
public Map<Character,CommandLine.Model.OptionSpec> posixOptionsMap()
```

Returns a map of the short (single character) option names to option spec objects configured for this command.

Returns:
an immutable map of options that this command recognizes.










    - 

#### requiredArgs


```
public List<CommandLine.Model.ArgSpec> requiredArgs()
```

Returns the list of required options and positional parameters configured for this command.
 This does not include options and positional parameters that are part of a group.

Returns:
an immutable list of the required options and positional parameters for this command.










    - 

#### unmatchedArgsBindings


```
public List<CommandLine.Model.UnmatchedArgsBinding> unmatchedArgsBindings()
```

Returns the list of `UnmatchedArgumentsBindings` configured for this command;
 each `UnmatchedArgsBinding` captures the arguments that could not be matched to any options or positional parameters.









    - 

#### specElements


```
public List<CommandLine.Model.IAnnotatedElement> specElements()
```

Returns the list of program elements annotated with `{@literal @}Spec` configured for this command.

Since:
4.0










    - 

#### parentCommandElements


```
public List<CommandLine.Model.IAnnotatedElement> parentCommandElements()
```

Returns the list of program elements annotated with `{@literal @}ParentCommand` configured for this command.

Since:
4.0










    - 

#### name


```
public String name()
```

Returns name of this command. Used in the synopsis line of the help message.
 `DEFAULT_COMMAND_NAME` by default, initialized from `CommandLine.Command.name()` if defined.

See Also:
`qualifiedName()`










    - 

#### aliases


```
public String[] aliases()
```

Returns the alias command names of this subcommand.

Since:
3.1










    - 

#### names


```
public Set<String> names()
```

Returns all names of this command, including `name()` and `aliases()`.

Since:
3.9










    - 

#### args


```
public List<CommandLine.Model.ArgSpec> args()
```

Returns the list of all options and positional parameters configured for this command.

Returns:
an immutable list of all options and positional parameters for this command.










    - 

#### qualifiedName


```
public String qualifiedName()
```

Returns the String to use as the program name in the synopsis line of the help message:
 this command's `name`, preceded by the qualified name of the parent command, if any, separated by a space.

Returns:
`DEFAULT_COMMAND_NAME` by default, initialized from `CommandLine.Command.name()` and the parent command if defined.
Since:
3.0.1










    - 

#### qualifiedName


```
public String qualifiedName(String separator)
```

Returns this command's fully qualified name, which is its `name`, preceded by the qualified name of the parent command, if this command has a parent command.

Parameters:
`separator` - the string to put between the names of the commands in the hierarchy
Returns:
`DEFAULT_COMMAND_NAME` by default, initialized from `CommandLine.Command.name()` and the parent command if any.
Since:
3.6










    - 

#### version


```
public String[] version()
```

Returns version information for this command, to print to the console when the user specifies an
 option to request version help. This is not part of the usage help message.

Returns:
the version strings generated by the `version provider` if one is set, otherwise the version literals










    - 

#### versionProvider


```
public CommandLine.IVersionProvider versionProvider()
```

Returns the version provider for this command, to generate the `version()` strings.

Returns:
the version provider or `null` if the version strings should be returned from the version literals.










    - 

#### helpCommand


```
public boolean helpCommand()
```

Returns whether this subcommand is a help command, and required options and positional
 parameters of the parent command should not be validated.

Returns:
`true` if this subcommand is a help command and picocli should not check for missing required
      options and positional parameters on the parent command
See Also:
`CommandLine.Command.helpCommand()`










    - 

#### exitCodeOnSuccess


```
public int exitCodeOnSuccess()
```

Returns exit code for successful termination. 0 by default, may be set programmatically or via the `exitCodeOnSuccess` annotation.

Since:
4.0
See Also:
`CommandLine.execute(String...)`










    - 

#### exitCodeOnUsageHelp


```
public int exitCodeOnUsageHelp()
```

Returns exit code for successful termination after printing usage help on user request. 0 by default, may be set programmatically or via the `exitCodeOnVersionHelp` annotation.

Since:
4.0
See Also:
`CommandLine.execute(String...)`










    - 

#### exitCodeOnVersionHelp


```
public int exitCodeOnVersionHelp()
```

Returns exit code for successful termination after printing version help on user request. 0 by default, may be set programmatically or via the `exitCodeOnUsageHelp` annotation.

Since:
4.0
See Also:
`CommandLine.execute(String...)`










    - 

#### exitCodeOnInvalidInput


```
public int exitCodeOnInvalidInput()
```

Returns exit code for command line usage error. 2 by default, may be set programmatically or via the `exitCodeOnInvalidInput` annotation.

Since:
4.0
See Also:
`CommandLine.execute(String...)`










    - 

#### exitCodeOnExecutionException


```
public int exitCodeOnExecutionException()
```

Returns exit code signifying that an exception occurred when invoking the Runnable, Callable or Method user object of a command.
 1 by default, may be set programmatically or via the `exitCodeOnExecutionException` annotation.

Since:
4.0
See Also:
`CommandLine.execute(String...)`










    - 

#### negatableOptionTransformer


```
public CommandLine.INegatableOptionTransformer negatableOptionTransformer()
```

Returns the `INegatableOptionTransformer` used to create the negative form of negatable options.

Since:
4.0
See Also:
`CommandLine.Option.negatable()`










    - 

#### mixinStandardHelpOptions


```
public boolean mixinStandardHelpOptions()
```

Returns `true` if the standard help options have been mixed in with this command, `false` otherwise.









    - 

#### subcommandsRepeatable


```
public boolean subcommandsRepeatable()
```

Returns whether the subcommands of this command are repeatable, that is, whether such subcommands can
 occur multiple times and may be followed by sibling commands instead of just child commands.

Since:
4.2
See Also:
`CommandLine.Command.subcommandsRepeatable()`










    - 

#### toString


```
public String toString()
```

Returns a string representation of this command, used in error messages and trace messages.

Overrides:
`toString` in class `Object`










    - 

#### name


```
public CommandLine.Model.CommandSpec name(String name)
```

Sets the String to use as the program name in the synopsis line of the help message.

Returns:
this CommandSpec for method chaining










    - 

#### aliases


```
public CommandLine.Model.CommandSpec aliases(String... aliases)
```

Sets the alternative names by which this subcommand is recognized on the command line.

Returns:
this CommandSpec for method chaining
Since:
3.1










    - 

#### defaultValueProvider


```
public CommandLine.IDefaultValueProvider defaultValueProvider()
```

Returns the default value provider for this command.

Returns:
the default value provider or `null`
Since:
3.6










    - 

#### defaultValueProvider


```
public CommandLine.Model.CommandSpec defaultValueProvider(CommandLine.IDefaultValueProvider defaultValueProvider)
```

Sets default value provider for this command.

Parameters:
`defaultValueProvider` - the default value provider to use, or `null`.
Returns:
this CommandSpec for method chaining
Since:
3.6










    - 

#### version


```
public CommandLine.Model.CommandSpec version(String... version)
```

Sets version information literals for this command, to print to the console when the user specifies an
 option to request version help. Only used if no `versionProvider` is set.

Returns:
this CommandSpec for method chaining










    - 

#### versionProvider


```
public CommandLine.Model.CommandSpec versionProvider(CommandLine.IVersionProvider versionProvider)
```

Sets version provider for this command, to generate the `version()` strings.

Parameters:
`versionProvider` - the version provider to use to generate the version strings, or `null` if the version literals should be used.
Returns:
this CommandSpec for method chaining










    - 

#### helpCommand


```
public CommandLine.Model.CommandSpec helpCommand(boolean newValue)
```

Sets whether this is a help command and required parameter checking should be suspended.

Returns:
this CommandSpec for method chaining
See Also:
`CommandLine.Command.helpCommand()`










    - 

#### exitCodeOnSuccess


```
public CommandLine.Model.CommandSpec exitCodeOnSuccess(int newValue)
```

Sets exit code for successful termination. 0 by default.

Since:
4.0
See Also:
`CommandLine.execute(String...)`










    - 

#### exitCodeOnUsageHelp


```
public CommandLine.Model.CommandSpec exitCodeOnUsageHelp(int newValue)
```

Sets exit code for successful termination after printing usage help on user request. 0 by default.

Since:
4.0
See Also:
`CommandLine.execute(String...)`










    - 

#### exitCodeOnVersionHelp


```
public CommandLine.Model.CommandSpec exitCodeOnVersionHelp(int newValue)
```

Sets exit code for successful termination after printing version help on user request. 0 by default.

Since:
4.0
See Also:
`CommandLine.execute(String...)`










    - 

#### exitCodeOnInvalidInput


```
public CommandLine.Model.CommandSpec exitCodeOnInvalidInput(int newValue)
```

Sets exit code for command line usage error. 2 by default.

Since:
4.0
See Also:
`CommandLine.execute(String...)`










    - 

#### exitCodeOnExecutionException


```
public CommandLine.Model.CommandSpec exitCodeOnExecutionException(int newValue)
```

Sets exit code signifying that an exception occurred when invoking the Runnable, Callable or Method user object of a command.
 1 by default.

Since:
4.0
See Also:
`CommandLine.execute(String...)`










    - 

#### inherited


```
public boolean inherited()
```

Returns whether this command is inherited from a parent command.

Since:
4.6
See Also:
`CommandLine.Command.scope()`










    - 

#### scopeType


```
public CommandLine.ScopeType scopeType()
```

Returns the scope of this argument; is it local, or inherited (it applies to this command as well as all sub- and sub-subcommands).

Returns:
whether this argument applies to all descendent subcommands of the command where it is defined
Since:
4.6










    - 

#### scopeType


```
public CommandLine.Model.CommandSpec scopeType(CommandLine.ScopeType scopeType)
```

Sets the scope of where this argument applies: only this command, or also all sub (and sub-sub) commands, and returns this builder.

Since:
4.6










    - 

#### modelTransformer


```
public CommandLine.IModelTransformer modelTransformer()
```

Returns the model transformer for this CommandSpec instance.

Since:
4.6










    - 

#### modelTransformer


```
public CommandLine.Model.CommandSpec modelTransformer(CommandLine.IModelTransformer modelTransformer)
```

Sets the model transformer for this CommandSpec instance.

Since:
4.6










    - 

#### preprocessor


```
public CommandLine.IParameterPreprocessor preprocessor()
```

Returns the preprocessor for this CommandSpec instance.

Since:
4.6










    - 

#### preprocessor


```
public CommandLine.Model.CommandSpec preprocessor(CommandLine.IParameterPreprocessor preprocessor)
```

Sets the preprocessor for this CommandSpec instance.

Since:
4.6










    - 

#### negatableOptionTransformer


```
public CommandLine.Model.CommandSpec negatableOptionTransformer(CommandLine.INegatableOptionTransformer newValue)
```

Sets the `INegatableOptionTransformer` used to create the negative form of negatable options.
 Note that `optionsCaseInsensitive()` will also change the case sensitivity of negatable options:
 any custom `CommandLine.INegatableOptionTransformer` that was previously installed will be replaced by the case-insensitive
 version of the default transformer. To ensure your custom transformer is used, install it last, after changing case sensitivity.

Since:
4.0
See Also:
`CommandLine.Option.negatable()`










    - 

#### mixinStandardHelpOptions


```
public CommandLine.Model.CommandSpec mixinStandardHelpOptions(boolean newValue)
```

Sets whether the standard help options should be mixed in with this command.

Returns:
this CommandSpec for method chaining
See Also:
`CommandLine.Command.mixinStandardHelpOptions()`










    - 

#### subcommandsRepeatable


```
public CommandLine.Model.CommandSpec subcommandsRepeatable(boolean subcommandsRepeatable)
```

Sets whether the subcommands of this command are repeatable, that is, whether such subcommands can
 occur multiple times and may be followed by sibling commands instead of just child commands.

Since:
4.2
See Also:
`CommandLine.Command.subcommandsRepeatable()`










    - 

#### withToString


```
public CommandLine.Model.CommandSpec withToString(String newValue)
```

Sets the string representation of this command, used in error messages and trace messages.

Parameters:
`newValue` - the string representation
Returns:
this CommandSpec for method chaining










    - 

#### updateCommandAttributes


```
public void updateCommandAttributes(CommandLine.Command cmd,
                                    CommandLine.IFactory factory)
```

Updates the following attributes from the specified `@Command` annotation:
 aliases, `parser separator`, command name, version, help command,
 version provider, default provider and `usage message spec`.

Parameters:
`cmd` - the `@Command` annotation to get attribute values from
`factory` - factory used to instantiate classes
Since:
3.7










    - 

#### findOption


```
public CommandLine.Model.OptionSpec findOption(char shortName)
```

Returns the option with the specified short name, or `null` if no option with that name is defined for this command.









    - 

#### findOption


```
public CommandLine.Model.OptionSpec findOption(String name)
```

Returns the option with the specified name, or `null` if no option with that name is defined for this command.

Parameters:
`name` - used to search the options. May include option name prefix characters or not.

















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