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

## Class CommandLine.Model.ArgGroupSpec






- java.lang.Object

- 



  - picocli.CommandLine.Model.ArgGroupSpec









- 

All Implemented Interfaces:
CommandLine.Model.IOrdered


Enclosing class:
CommandLine.Model


---




```
public static class CommandLine.Model.ArgGroupSpec
extends Object
implements CommandLine.Model.IOrdered
```

The `ArgGroupSpec` class models a `group` of arguments (options, positional parameters or a mixture of the two).

Since:
4.0
See Also:
`CommandLine.ArgGroup`









- 




  - 



### Nested Class Summary


Nested Classes 

Modifier and Type
Class and Description


`static class `
`CommandLine.Model.ArgGroupSpec.Builder`
Builder responsible for creating valid `ArgGroupSpec` objects.










  - 



### Method Summary


All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description


`List<CommandLine.Model.OptionSpec>`
`allOptionsNested()`
Returns all options configured for this group and all subgroups.



`List<CommandLine.Model.PositionalParamSpec>`
`allPositionalParametersNested()`
Returns all positional parameters configured for this group and all subgroups.



`Set<CommandLine.Model.ArgSpec>`
`args()`
Returns the options and positional parameters in this group; may be empty but not `null`.



`static CommandLine.Model.ArgGroupSpec.Builder`
`builder()`
Returns a new `CommandLine.Model.ArgGroupSpec.Builder`.



`static CommandLine.Model.ArgGroupSpec.Builder`
`builder(CommandLine.Model.IAnnotatedElement annotatedElement)`
Returns a new `CommandLine.Model.ArgGroupSpec.Builder` associated with the specified annotated element.



`CommandLine.Help.IParamLabelRenderer`
`createLabelRenderer(CommandLine.Model.CommandSpec commandSpec)` 


`boolean`
`equals(Object obj)` 


`boolean`
`exclusive()`
Returns whether this is a mutually exclusive group; `true` by default.



`CommandLine.Model.IGetter`
`getter()`
Returns the `CommandLine.Model.IGetter` that is responsible for supplying the value of the annotated program element associated with this group.



`int`
`hashCode()` 


`String`
`heading()`
Returns the heading of this group (may be `null`), used when generating the usage documentation.



`String`
`headingKey()`
Returns the heading key of this group (may be `null`), used to get the heading from a resource bundle.



`boolean`
`isSubgroupOf(CommandLine.Model.ArgGroupSpec group)`
Returns `true` if this group is a subgroup (or a nested sub-subgroup, to any level of depth)
 of the specified group, `false` otherwise.



`CommandLine.Model.Messages`
`messages()`
Returns the Messages for this argument group specification, or `null`.



`CommandLine.Model.ArgGroupSpec`
`messages(CommandLine.Model.Messages msgs)`
Sets the Messages for this ArgGroupSpec, and returns this ArgGroupSpec.



`CommandLine.Range`
`multiplicity()`
Returns the multiplicity of this group: how many occurrences it may have on the command line; `"0..1"` (optional) by default.



`List<CommandLine.Model.OptionSpec>`
`options()`
Returns the list of options configured for this group.



`int`
`order()`
Returns the position in the options list in the usage help message at which this group should be shown.



`CommandLine.Model.ArgGroupSpec`
`parentGroup()`
Returns the parent group that this group is part of, or `null` if this group is not part of a composite.



`List<CommandLine.Model.PositionalParamSpec>`
`positionalParameters()`
Returns the list of positional parameters configured for this group.



`Set<CommandLine.Model.ArgSpec>`
`requiredArgs()`
Returns the required options and positional parameters in this group; may be empty but not `null`.



`CommandLine.Model.IScope`
`scope()`
Returns the `CommandLine.Model.IScope` that determines where the setter sets the value (or the getter gets the value) of the annotated program element associated with this group.



`CommandLine.Model.ISetter`
`setter()`
Returns the `CommandLine.Model.ISetter` that is responsible for modifying the value of the annotated program element associated with this group.



`List<CommandLine.Model.IAnnotatedElement>`
`specElements()`
Returns the list of program elements annotated with `{@literal @}Spec` configured for this group.



`List<CommandLine.Model.ArgGroupSpec>`
`subgroups()`
Return the subgroups that this group is composed of; may be empty but not `null`.



`String`
`synopsis()`
Returns the synopsis of this group.



`CommandLine.Help.Ansi.Text`
`synopsisText(CommandLine.Help.ColorScheme colorScheme,
            Set<CommandLine.Model.ArgSpec> outparam_groupArgs)`
Returns the synopsis of this group.



`String`
`toString()` 


`CommandLine.Model.ITypeInfo`
`typeInfo()`
Returns the type info for the annotated program element associated with this group.



`boolean`
`validate()`
Returns whether picocli should validate the rules of this group:
 for a mutually exclusive group this means that no more than one arguments in the group is specified on the command line;
 for a co-occurring group this means that all arguments in the group are specified on the command line.






    - 



### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`













- 




  - 



### Method Detail







    - 

#### builder


```
public static CommandLine.Model.ArgGroupSpec.Builder builder()
```

Returns a new `CommandLine.Model.ArgGroupSpec.Builder`.

Returns:
a new ArgGroupSpec.Builder instance










    - 

#### builder


```
public static CommandLine.Model.ArgGroupSpec.Builder builder(CommandLine.Model.IAnnotatedElement annotatedElement)
```

Returns a new `CommandLine.Model.ArgGroupSpec.Builder` associated with the specified annotated element.

Parameters:
`annotatedElement` - the annotated element containing `@Option` and `@Parameters`
Returns:
a new ArgGroupSpec.Builder instance










    - 

#### exclusive


```
public boolean exclusive()
```

Returns whether this is a mutually exclusive group; `true` by default.
 If `false`, this is a co-occurring group. Ignored if `validate()` is `false`.

See Also:
`CommandLine.ArgGroup.exclusive()`










    - 

#### multiplicity


```
public CommandLine.Range multiplicity()
```

Returns the multiplicity of this group: how many occurrences it may have on the command line; `"0..1"` (optional) by default.
 A group can be made required by specifying a multiplicity of `"1"`. For a group of mutually exclusive arguments,
 being required means that one of the arguments in the group must appear on the command line, or a MissingParameterException is thrown.
 For a group of co-occurring arguments, being required means that all arguments in the group must appear on the command line.
 Ignored if `validate()` is `false`.

See Also:
`CommandLine.ArgGroup.multiplicity()`










    - 

#### validate


```
public boolean validate()
```

Returns whether picocli should validate the rules of this group:
 for a mutually exclusive group this means that no more than one arguments in the group is specified on the command line;
 for a co-occurring group this means that all arguments in the group are specified on the command line.
 `true` by default.

See Also:
`CommandLine.ArgGroup.validate()`










    - 

#### order


```
public int order()
```

Returns the position in the options list in the usage help message at which this group should be shown.
 Groups with a lower number are shown before groups with a higher number.
 This attribute is only honored for groups that have a `heading` (or a `headingKey` with a non-`null` resource bundle value).

Specified by:
`order` in interface `CommandLine.Model.IOrdered`










    - 

#### heading


```
public String heading()
```

Returns the heading of this group (may be `null`), used when generating the usage documentation.

See Also:
`CommandLine.ArgGroup.heading()`










    - 

#### headingKey


```
public String headingKey()
```

Returns the heading key of this group (may be `null`), used to get the heading from a resource bundle.

See Also:
`CommandLine.ArgGroup.headingKey()`










    - 

#### parentGroup


```
public CommandLine.Model.ArgGroupSpec parentGroup()
```

Returns the parent group that this group is part of, or `null` if this group is not part of a composite.









    - 

#### subgroups


```
public List<CommandLine.Model.ArgGroupSpec> subgroups()
```

Return the subgroups that this group is composed of; may be empty but not `null`.

Returns:
immutable list of subgroups that this group is composed of.










    - 

#### specElements


```
public List<CommandLine.Model.IAnnotatedElement> specElements()
```

Returns the list of program elements annotated with `{@literal @}Spec` configured for this group.

Since:
4.6










    - 

#### isSubgroupOf


```
public boolean isSubgroupOf(CommandLine.Model.ArgGroupSpec group)
```

Returns `true` if this group is a subgroup (or a nested sub-subgroup, to any level of depth)
 of the specified group, `false` otherwise.

Parameters:
`group` - the group to check if it contains this group
Returns:
`true` if this group is a subgroup or a nested sub-subgroup of the specified group










    - 

#### typeInfo


```
public CommandLine.Model.ITypeInfo typeInfo()
```

Returns the type info for the annotated program element associated with this group.

Returns:
type information that does not require `Class` objects and be constructed both at runtime and compile time










    - 

#### getter


```
public CommandLine.Model.IGetter getter()
```

Returns the `CommandLine.Model.IGetter` that is responsible for supplying the value of the annotated program element associated with this group.









    - 

#### setter


```
public CommandLine.Model.ISetter setter()
```

Returns the `CommandLine.Model.ISetter` that is responsible for modifying the value of the annotated program element associated with this group.









    - 

#### scope


```
public CommandLine.Model.IScope scope()
```

Returns the `CommandLine.Model.IScope` that determines where the setter sets the value (or the getter gets the value) of the annotated program element associated with this group.









    - 

#### args


```
public Set<CommandLine.Model.ArgSpec> args()
```

Returns the options and positional parameters in this group; may be empty but not `null`.









    - 

#### requiredArgs


```
public Set<CommandLine.Model.ArgSpec> requiredArgs()
```

Returns the required options and positional parameters in this group; may be empty but not `null`.









    - 

#### positionalParameters


```
public List<CommandLine.Model.PositionalParamSpec> positionalParameters()
```

Returns the list of positional parameters configured for this group.

Returns:
an immutable list of positional parameters in this group.










    - 

#### options


```
public List<CommandLine.Model.OptionSpec> options()
```

Returns the list of options configured for this group.

Returns:
an immutable list of options in this group.










    - 

#### allOptionsNested


```
public List<CommandLine.Model.OptionSpec> allOptionsNested()
```

Returns all options configured for this group and all subgroups.

Returns:
an immutable list of all options in this group and its subgroups.
Since:
4.4










    - 

#### allPositionalParametersNested


```
public List<CommandLine.Model.PositionalParamSpec> allPositionalParametersNested()
```

Returns all positional parameters configured for this group and all subgroups.

Returns:
an immutable list of all positional parameters in this group and its subgroups.
Since:
4.4










    - 

#### synopsis


```
public String synopsis()
```

Returns the synopsis of this group.









    - 

#### synopsisText


```
public CommandLine.Help.Ansi.Text synopsisText(CommandLine.Help.ColorScheme colorScheme,
                                               Set<CommandLine.Model.ArgSpec> outparam_groupArgs)
```

Returns the synopsis of this group.

Parameters:
`colorScheme` - the color scheme to use for options and positional parameters in this group and subgroups
`outparam_groupArgs` - all options and positional parameters in the groups this method generates a synopsis for;
                           these options and positional parameters should be excluded from appearing elsewhere in the synopsis
Returns:
the synopsis Text










    - 

#### createLabelRenderer


```
public CommandLine.Help.IParamLabelRenderer createLabelRenderer(CommandLine.Model.CommandSpec commandSpec)
```










    - 

#### messages


```
public CommandLine.Model.Messages messages()
```

Returns the Messages for this argument group specification, or `null`.









    - 

#### messages


```
public CommandLine.Model.ArgGroupSpec messages(CommandLine.Model.Messages msgs)
```

Sets the Messages for this ArgGroupSpec, and returns this ArgGroupSpec.

Parameters:
`msgs` - the new Messages value, may be `null`
See Also:
`CommandLine.Command.resourceBundle()`, 
`headingKey()`










    - 

#### equals


```
public boolean equals(Object obj)
```


Overrides:
`equals` in class `Object`










    - 

#### hashCode


```
public int hashCode()
```


Overrides:
`hashCode` in class `Object`










    - 

#### toString


```
public String toString()
```


Overrides:
`toString` in class `Object`

















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