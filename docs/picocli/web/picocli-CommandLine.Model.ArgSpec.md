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

## Class CommandLine.Model.ArgSpec






- java.lang.Object

- 



  - picocli.CommandLine.Model.ArgSpec









- 

Direct Known Subclasses:
CommandLine.Model.OptionSpec, CommandLine.Model.PositionalParamSpec


Enclosing class:
CommandLine.Model


---




```
public abstract static class CommandLine.Model.ArgSpec
extends Object
```

Models the shared attributes of `CommandLine.Model.OptionSpec` and `CommandLine.Model.PositionalParamSpec`.

Since:
3.0









- 




  - 



### Field Summary


Fields 

Modifier and Type
Field and Description


`protected CommandLine.Model.IAnnotatedElement`
`annotatedElement` 


`protected String`
`toString` 


`protected CommandLine.Model.ITypeInfo`
`typeInfo` 


`protected boolean`
`valueIsDefaultValue` 









  - 



### Method Summary


All Methods Instance Methods Abstract Methods Concrete Methods Deprecated Methods 

Modifier and Type
Method and Description


`CommandLine.Range`
`arity()`
Returns how many arguments this option or positional parameter requires.



`Class<?>[]`
`auxiliaryTypes()`
Returns auxiliary type information used when the `type()` is a generic type like
 `Collection`, `Map` or `Optional`; returns the concrete type when `type()`
 is an abstract class, otherwise, returns the same as `type()`.



`CommandLine.Model.CommandSpec`
`command()`
Returns the command this option or positional parameter belongs to.



`Iterable<String>`
`completionCandidates()`
Returns the explicitly set completion candidates for this option or positional parameter, valid enum
 constant names, or `null` if this option or positional parameter does not have any completion
 candidates and its type is not an enum.



`CommandLine.ITypeConverter<?>[]`
`converters()`
Returns one or more `type converters` to use to convert the command line
 argument into a strongly typed value (or key-value pair for map fields).



`String`
`defaultValue()`
Returns the default value to assign if this option or positional parameter was not specified on the command line, before splitting and type conversion.



`String`
`defaultValueString()`
Returns the default value String for the purpose of displaying it in the description, without interpolating variables.



`String`
`defaultValueString(boolean interpolateVariables)`
Returns the default value String displayed in the description; interpolating variables if specified.



`String[]`
`description()`
Returns the description of this option or positional parameter, after all variables have been rendered,
 including the `${DEFAULT-VALUE}` and `${COMPLETION-CANDIDATES}` variables.



`String`
`descriptionKey()`
Returns the description key of this arg spec, used to get the description from a resource bundle.



`boolean`
`echo()`
Returns whether the user input is echoed to the console or not for an interactive option or positional parameter when asking for user input.



`protected boolean`
`equalsImpl(CommandLine.Model.ArgSpec other)` 


`protected abstract Collection<String>`
`getAdditionalDescriptionKeys()`
Subclasses should override to return a collection of additional description keys that may be used to find
 description text for this option or positional parameter in the resource bundle.



`CommandLine.Model.IGetter`
`getter()`
Returns the `CommandLine.Model.IGetter` that is responsible for supplying the value of this argument.



`<T> T`
`getValue()`
Returns the current value of this argument.



`CommandLine.Model.ArgGroupSpec`
`group()`
Returns the groups this option or positional parameter belongs to, or `null` if this option is not part of a group.



`protected int`
`hashCodeImpl()` 


`boolean`
`hasInitialValue()`
Determines whether the option or positional parameter will be reset to the `initialValue()`
 before parsing new input.



`boolean`
`hidden()`
Returns whether this option should be excluded from the usage message.



`boolean`
`hideParamSyntax()`
Returns whether usage syntax decorations around the paramLabel should be suppressed.



`boolean`
`inherited()`
Returns whether this option is inherited from a parent command.



`Object`
`initialValue()`
Returns the initial value of this option or positional parameter: the value that, if `hasInitialValue()` is true,
 the option will be reset to before parsing (regardless of whether a default value exists),
 to clear values that would otherwise remain from parsing previous input.



`boolean`
`interactive()`
Returns whether this option will prompt the user to enter a value on the command line.



`protected boolean`
`internalShowDefaultValue(boolean usageHelpShowDefaults)`
Returns whether the default for this option or positional parameter should be shown, potentially overriding the specified global setting.



`boolean`
`isMultiValue()`
Returns `true` if this argument's `type()` is an array, a `Collection` or a `Map`, `false` otherwise.



`abstract boolean`
`isOption()`
Returns `true` if this argument is a named option, `false` otherwise.



`abstract boolean`
`isPositional()`
Returns `true` if this argument is a positional parameter, `false` otherwise.



`boolean`
`isValueGettable()`
Check whether the `getValue()` method is able to get an actual value from the current `getter()`.



`String`
`mapFallbackValue()`
Returns the fallback value for this Map option or positional parameter: the value that is put into the Map when only the
 key is specified for the option or positional parameter, like `-Dkey` instead of `-Dkey=value`.



`CommandLine.Model.Messages`
`messages()`
Returns the Messages for this arg specification, or `null`.



`CommandLine.Model.ArgSpec`
`messages(CommandLine.Model.Messages msgs)`
Sets the Messages for this ArgSpec, and returns this ArgSpec.



`boolean`
`originallyRequired()`
Returns the original value of the option's required attribute, regardless of whether the option is used in an exclusive group or not.



`List<String>`
`originalStringValues()`
Returns the original command line arguments matched by this option or positional parameter spec.



`CommandLine.IParameterConsumer`
`parameterConsumer()`
Returns a custom `IParameterConsumer` to temporarily suspend picocli's parsing logic
 and process one or more command line arguments in a custom manner, or `null`.



`String`
`paramLabel()`
Returns the name of the option or positional parameter used in the usage help message.



`CommandLine.IParameterPreprocessor`
`preprocessor()`
Returns a custom `IParameterPreprocessor` to either replace or complement picocli's parsing logic
 for the parameter(s) of this option or position.



`String`
`prompt()`
Returns the text displayed to the end user for an interactive option or positional parameter when asking for user input.



`String[]`
`renderedDescription()`
Deprecated. 
Use `description()` instead




`boolean`
`required()`
Returns whether this is a required option or positional parameter without a default value.



`protected void`
`resetOriginalStringValues()`
Sets the `originalStringValues` to a new list instance.



`protected void`
`resetStringValues()`
Sets the `stringValues` to a new list instance.



`CommandLine.Model.ArgSpec`
`root()`
Returns the root option or positional parameter (on the parent command), if this option or positional parameter was inherited;
 or `null` if it was not.



`CommandLine.Model.IScope`
`scope()`
Returns the binding `CommandLine.Model.IScope` that determines on which object to set the value (or from which object to get the value) of this argument.



`CommandLine.ScopeType`
`scopeType()`
Returns the scope of this argument; is it local, or inherited (it applies to this command as well as all sub- and sub-subcommands).



`CommandLine.Model.ISetter`
`setter()`
Returns the `CommandLine.Model.ISetter` that is responsible for modifying the value of this argument.



`<T> T`
`setValue(T newValue)`
Sets the value of this argument to the specified value and returns the previous value.



`<T> T`
`setValue(T newValue,
        CommandLine commandLine)`
Deprecated. 
use `setValue(Object)` instead. This was a design mistake.




`CommandLine.Help.Visibility`
`showDefaultValue()`
Returns whether this option or positional parameter's default value should be shown in the usage help.



`String`
`splitRegex()`
Returns a regular expression to split option parameter values or `""` if the value should not be split.



`String`
`splitRegexSynopsisLabel()`
Returns a regular expression to split option parameter for usage information.



`List<String>`
`stringValues()`
Returns the untyped command line arguments matched by this option or positional parameter spec.



`String`
`toString()`
Returns a string respresentation of this option or positional parameter.



`Class<?>`
`type()`
Returns the type to convert the option or positional parameter to before setting the value.



`List<Object>`
`typedValues()`
Returns the typed command line arguments matched by this option or positional parameter spec.



`CommandLine.Model.ITypeInfo`
`typeInfo()`
Returns the `ITypeInfo` that can be used both at compile time (by annotation processors) and at runtime.



`Object`
`userObject()`
Returns the user object associated with this option or positional parameters.






    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`













- 




  - 



### Field Detail







    - 

#### typeInfo


```
protected final CommandLine.Model.ITypeInfo typeInfo
```










    - 

#### valueIsDefaultValue


```
protected boolean valueIsDefaultValue
```










    - 

#### annotatedElement


```
protected final CommandLine.Model.IAnnotatedElement annotatedElement
```










    - 

#### toString


```
protected String toString
```











  - 



### Method Detail







    - 

#### originallyRequired


```
public boolean originallyRequired()
```

Returns the original value of the option's required attribute, regardless of whether the option is used in an exclusive group or not.

Since:
4.7.7
See Also:
`CommandLine.Option.required()`










    - 

#### required


```
public boolean required()
```

Returns whether this is a required option or positional parameter without a default value.
 If this argument is part of a group, this method returns whether this argument is required *within the group* (so it is not necessarily a required argument for the command).

See Also:
`CommandLine.Option.required()`










    - 

#### interactive


```
public boolean interactive()
```

Returns whether this option will prompt the user to enter a value on the command line.

See Also:
`CommandLine.Parameters.interactive()`, 
`CommandLine.Option.interactive()`










    - 

#### echo


```
public boolean echo()
```

Returns whether the user input is echoed to the console or not for an interactive option or positional parameter when asking for user input.

Since:
4.6
See Also:
`CommandLine.Option.echo()`, 
`CommandLine.Parameters.echo()`










    - 

#### prompt


```
public String prompt()
```

Returns the text displayed to the end user for an interactive option or positional parameter when asking for user input.

Since:
4.6
See Also:
`CommandLine.Option.prompt()`, 
`CommandLine.Parameters.prompt()`










    - 

#### description


```
public String[] description()
```

Returns the description of this option or positional parameter, after all variables have been rendered,
 including the `${DEFAULT-VALUE}` and `${COMPLETION-CANDIDATES}` variables.
 Use `CommandLine.Model.CommandSpec.interpolateVariables(Boolean)` to switch off variable expansion if needed.
 


 If a resource bundle has been set, this method will first try to find a value in the resource bundle:
 If the resource bundle has no entry for the `fully qualified commandName + "." + descriptionKey` or for the unqualified `descriptionKey`,
 an attempt is made to find the option or positional parameter description using any of the
 additional description keys, first with the `fully qualified commandName + "."` prefix, then without.
 

See Also:
`CommandLine.Model.CommandSpec.qualifiedName(String)`, 
`getAdditionalDescriptionKeys()`, 
`CommandLine.Parameters.description()`, 
`CommandLine.Option.description()`










    - 

#### getAdditionalDescriptionKeys


```
protected abstract Collection<String> getAdditionalDescriptionKeys()
```

Subclasses should override to return a collection of additional description keys that may be used to find
 description text for this option or positional parameter in the resource bundle.

Since:
4.0
See Also:
`CommandLine.Model.OptionSpec.getAdditionalDescriptionKeys()`, 
`CommandLine.Model.PositionalParamSpec.getAdditionalDescriptionKeys()`










    - 

#### descriptionKey


```
public String descriptionKey()
```

Returns the description key of this arg spec, used to get the description from a resource bundle.

Since:
3.6
See Also:
`CommandLine.Option.descriptionKey()`, 
`CommandLine.Parameters.descriptionKey()`










    - 

#### renderedDescription


```
@Deprecated
public String[] renderedDescription()
```

Deprecated. Use `description()` instead









    - 

#### arity


```
public CommandLine.Range arity()
```

Returns how many arguments this option or positional parameter requires.

See Also:
`CommandLine.Option.arity()`










    - 

#### paramLabel


```
public String paramLabel()
```

Returns the name of the option or positional parameter used in the usage help message.

See Also:
`CommandLine.Option.paramLabel()`, 
`CommandLine.Parameters.paramLabel()`










    - 

#### hideParamSyntax


```
public boolean hideParamSyntax()
```

Returns whether usage syntax decorations around the paramLabel should be suppressed.
 The default is `false`: by default, the paramLabel is surrounded with `'['` and `']'` characters
 if the value is optional and followed by ellipses ("...") when multiple values can be specified.

Since:
3.6.0










    - 

#### auxiliaryTypes


```
public Class<?>[] auxiliaryTypes()
```

Returns auxiliary type information used when the `type()` is a generic type like
 `Collection`, `Map` or `Optional`; returns the concrete type when `type()`
 is an abstract class, otherwise, returns the same as `type()`.

See Also:
`CommandLine.Option.type()`










    - 

#### converters


```
public CommandLine.ITypeConverter<?>[] converters()
```

Returns one or more `type converters` to use to convert the command line
 argument into a strongly typed value (or key-value pair for map fields). This is useful when a particular
 option or positional parameter should use a custom conversion that is different from the normal conversion for the arg spec's type.

See Also:
`CommandLine.Option.converter()`










    - 

#### splitRegex


```
public String splitRegex()
```

Returns a regular expression to split option parameter values or `""` if the value should not be split.

See Also:
`CommandLine.Option.split()`










    - 

#### splitRegexSynopsisLabel


```
public String splitRegexSynopsisLabel()
```

Returns a regular expression to split option parameter for usage information.

Since:
4.3
See Also:
`CommandLine.Option.splitSynopsisLabel()`










    - 

#### hidden


```
public boolean hidden()
```

Returns whether this option should be excluded from the usage message.

See Also:
`CommandLine.Option.hidden()`










    - 

#### inherited


```
public boolean inherited()
```

Returns whether this option is inherited from a parent command.

Since:
4.3.0
See Also:
`CommandLine.Option.scope()`










    - 

#### root


```
public CommandLine.Model.ArgSpec root()
```

Returns the root option or positional parameter (on the parent command), if this option or positional parameter was inherited;
 or `null` if it was not.

Since:
4.6.0
See Also:
`CommandLine.Option.scope()`










    - 

#### type


```
public Class<?> type()
```

Returns the type to convert the option or positional parameter to before setting the value.
 This may be a container type like `List`, `Map`, or `Optional`,
 in which case the type or types of the elements are returned by `auxiliaryTypes()`.









    - 

#### typeInfo


```
public CommandLine.Model.ITypeInfo typeInfo()
```

Returns the `ITypeInfo` that can be used both at compile time (by annotation processors) and at runtime.

Since:
4.0










    - 

#### userObject


```
public Object userObject()
```

Returns the user object associated with this option or positional parameters.

Returns:
may return the annotated program element, or some other useful object
Since:
4.0










    - 

#### mapFallbackValue


```
public String mapFallbackValue()
```

Returns the fallback value for this Map option or positional parameter: the value that is put into the Map when only the
 key is specified for the option or positional parameter, like `-Dkey` instead of `-Dkey=value`.
 

If no `mapFallbackValue` is set, key-only Map parameters like `-Dkey`
 are considered invalid user input and cause a `CommandLine.ParameterException` to be thrown.
 

By default, this method returns a special "__unspecified__" value indicating that no `mapFallbackValue` was set.

Since:
4.6
See Also:
`CommandLine.Option.mapFallbackValue()`, 
`CommandLine.Parameters.mapFallbackValue()`










    - 

#### defaultValue


```
public String defaultValue()
```

Returns the default value to assign if this option or positional parameter was not specified on the command line, before splitting and type conversion.
 This method returns the programmatically set value; this may differ from the default value that is actually used:
 if this ArgSpec is part of a CommandSpec with a `CommandLine.IDefaultValueProvider`, picocli will first try to obtain
 the default value from the default value provider, and this method is only called if the default provider is
 `null` or returned a `null` value.

Returns:
the programmatically set default value of this option/positional parameter,
      returning `null` means this option or positional parameter does not have a default
See Also:
`CommandLine.Model.CommandSpec.defaultValueProvider()`, 
`CommandLine.Model.OptionSpec.fallbackValue()`










    - 

#### initialValue


```
public Object initialValue()
```

Returns the initial value of this option or positional parameter: the value that, if `hasInitialValue()` is true,
 the option will be reset to before parsing (regardless of whether a default value exists),
 to clear values that would otherwise remain from parsing previous input.









    - 

#### hasInitialValue


```
public boolean hasInitialValue()
```

Determines whether the option or positional parameter will be reset to the `initialValue()`
 before parsing new input.









    - 

#### showDefaultValue


```
public CommandLine.Help.Visibility showDefaultValue()
```

Returns whether this option or positional parameter's default value should be shown in the usage help.









    - 

#### defaultValueString


```
public String defaultValueString()
```

Returns the default value String for the purpose of displaying it in the description, without interpolating variables.

See Also:
`defaultValueString(boolean)`










    - 

#### defaultValueString


```
public String defaultValueString(boolean interpolateVariables)
```

Returns the default value String displayed in the description; interpolating variables if specified. If this ArgSpec is part of a
 CommandSpec with a `CommandLine.IDefaultValueProvider`, this method will first try to obtain
 the default value from the default value provider; if the provider is `null` or if it
 returns a `null` value, then next any value set to `defaultValue()`
 is returned, and if this is also `null`, finally the initial value is returned.

Parameters:
`interpolateVariables` - whether to interpolate variables in the `defaultValue` attribute of this ArgSpec
Since:
4.0
See Also:
`CommandLine.Model.CommandSpec.defaultValueProvider()`, 
`defaultValue()`










    - 

#### completionCandidates


```
public Iterable<String> completionCandidates()
```

Returns the explicitly set completion candidates for this option or positional parameter, valid enum
 constant names, or `null` if this option or positional parameter does not have any completion
 candidates and its type is not an enum.

Returns:
the completion candidates for this option or positional parameter, valid enum constant names,
 or `null`
Since:
3.2










    - 

#### parameterConsumer


```
public CommandLine.IParameterConsumer parameterConsumer()
```

Returns a custom `IParameterConsumer` to temporarily suspend picocli's parsing logic
 and process one or more command line arguments in a custom manner, or `null`.
 An example of when this may be useful is when passing arguments through to another program.

Since:
4.0










    - 

#### preprocessor


```
public CommandLine.IParameterPreprocessor preprocessor()
```

Returns a custom `IParameterPreprocessor` to either replace or complement picocli's parsing logic
 for the parameter(s) of this option or position.

Since:
4.6










    - 

#### getter


```
public CommandLine.Model.IGetter getter()
```

Returns the `CommandLine.Model.IGetter` that is responsible for supplying the value of this argument.









    - 

#### setter


```
public CommandLine.Model.ISetter setter()
```

Returns the `CommandLine.Model.ISetter` that is responsible for modifying the value of this argument.









    - 

#### scope


```
public CommandLine.Model.IScope scope()
```

Returns the binding `CommandLine.Model.IScope` that determines on which object to set the value (or from which object to get the value) of this argument.









    - 

#### scopeType


```
public CommandLine.ScopeType scopeType()
```

Returns the scope of this argument; is it local, or inherited (it applies to this command as well as all sub- and sub-subcommands).

Returns:
whether this argument applies to all descendent subcommands of the command where it is defined
Since:
4.3










    - 

#### isValueGettable


```
public boolean isValueGettable()
```

Check whether the `getValue()` method is able to get an actual value from the current `getter()`.

Since:
4.7










    - 

#### getValue


```
public <T> T getValue()
               throws CommandLine.PicocliException
```

Returns the current value of this argument. Delegates to the current `getter()`.

Throws:
`CommandLine.PicocliException`












    - 

#### setValue


```
public <T> T setValue(T newValue)
               throws CommandLine.PicocliException
```

Sets the value of this argument to the specified value and returns the previous value. Delegates to the current `setter()`.

Throws:
`CommandLine.PicocliException`












    - 

#### setValue


```
@Deprecated
public <T> T setValue(T newValue,
                                   CommandLine commandLine)
                            throws CommandLine.PicocliException
```

Deprecated. use `setValue(Object)` instead. This was a design mistake.
Sets the value of this argument to the specified value and returns the previous value. Delegates to the current `setter()`.

Throws:
`CommandLine.PicocliException`
Since:
3.5










    - 

#### isMultiValue


```
public boolean isMultiValue()
```

Returns `true` if this argument's `type()` is an array, a `Collection` or a `Map`, `false` otherwise.









    - 

#### isOption


```
public abstract boolean isOption()
```

Returns `true` if this argument is a named option, `false` otherwise.









    - 

#### isPositional


```
public abstract boolean isPositional()
```

Returns `true` if this argument is a positional parameter, `false` otherwise.









    - 

#### group


```
public CommandLine.Model.ArgGroupSpec group()
```

Returns the groups this option or positional parameter belongs to, or `null` if this option is not part of a group.

Since:
4.0










    - 

#### command


```
public CommandLine.Model.CommandSpec command()
```

Returns the command this option or positional parameter belongs to.
 

Beware that it is possible to programmatically add an option or positional parameter to more than one command model.
 (This will not happen in models that are auto-generated from annotations). In that case this method will only return
 the one it was added to last.
 

If the option or positional parameter has not yet been attached to a command, `null` will be returned.

Since:
4.1










    - 

#### stringValues


```
public List<String> stringValues()
```

Returns the untyped command line arguments matched by this option or positional parameter spec.

Returns:
the matched arguments after splitting, but before type conversion.
      For map properties, `"key=value"` values are split into the key and the value part.










    - 

#### typedValues


```
public List<Object> typedValues()
```

Returns the typed command line arguments matched by this option or positional parameter spec.

Returns:
the matched arguments after splitting and type conversion.
      For map properties, `"key=value"` values are split into the key and the value part.










    - 

#### resetStringValues


```
protected void resetStringValues()
```

Sets the `stringValues` to a new list instance.









    - 

#### originalStringValues


```
public List<String> originalStringValues()
```

Returns the original command line arguments matched by this option or positional parameter spec.

Returns:
the matched arguments as found on the command line: empty Strings for options without value, the
      values have not been split, and for map properties values may look like `"key=value"`










    - 

#### resetOriginalStringValues


```
protected void resetOriginalStringValues()
```

Sets the `originalStringValues` to a new list instance.









    - 

#### internalShowDefaultValue


```
protected boolean internalShowDefaultValue(boolean usageHelpShowDefaults)
```

Returns whether the default for this option or positional parameter should be shown, potentially overriding the specified global setting.

Parameters:
`usageHelpShowDefaults` - whether the command's UsageMessageSpec is configured to show default values.










    - 

#### messages


```
public CommandLine.Model.Messages messages()
```

Returns the Messages for this arg specification, or `null`.

Since:
3.6










    - 

#### messages


```
public CommandLine.Model.ArgSpec messages(CommandLine.Model.Messages msgs)
```

Sets the Messages for this ArgSpec, and returns this ArgSpec.

Parameters:
`msgs` - the new Messages value, may be `null`
Since:
3.6
See Also:
`CommandLine.Command.resourceBundle()`, 
`description()`, 
`description()`










    - 

#### toString


```
public String toString()
```

Returns a string respresentation of this option or positional parameter.

Overrides:
`toString` in class `Object`










    - 

#### equalsImpl


```
protected boolean equalsImpl(CommandLine.Model.ArgSpec other)
```










    - 

#### hashCodeImpl


```
protected int hashCodeImpl()
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