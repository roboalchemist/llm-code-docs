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

## Class CommandLine.Model.ArgGroupSpec.Builder






- java.lang.Object

- 



  - picocli.CommandLine.Model.ArgGroupSpec.Builder









- 

Enclosing class:
CommandLine.Model.ArgGroupSpec


---




```
public static class CommandLine.Model.ArgGroupSpec.Builder
extends Object
```

Builder responsible for creating valid `ArgGroupSpec` objects.

Since:
4.0









- 




  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description


`CommandLine.Model.ArgGroupSpec.Builder`
`addArg(CommandLine.Model.ArgSpec arg)`
Adds the specified argument to the list of options and positional parameters that depend on this group.



`CommandLine.Model.ArgGroupSpec.Builder`
`addSpecElement(CommandLine.Model.IAnnotatedElement element)`
Adds the specified `{@literal @}Spec` annotated program element to the list of spec elements for this group.



`CommandLine.Model.ArgGroupSpec.Builder`
`addSubgroup(CommandLine.Model.ArgGroupSpec group)`
Adds the specified group to the list of subgroups that this group is composed of.



`List<CommandLine.Model.ArgSpec>`
`args()`
Returns the list of options and positional parameters that depend on this group.



`CommandLine.Model.ArgGroupSpec`
`build()`
Returns a valid `ArgGroupSpec` instance.



`boolean`
`exclusive()`
Returns whether this is a mutually exclusive group; `true` by default.



`CommandLine.Model.ArgGroupSpec.Builder`
`exclusive(boolean newValue)`
Sets whether this is a mutually exclusive group; `true` by default.



`CommandLine.Model.IGetter`
`getter()`
Returns the `CommandLine.Model.IGetter` that is responsible for supplying the value of the annotated program element associated with this group.



`CommandLine.Model.ArgGroupSpec.Builder`
`getter(CommandLine.Model.IGetter getter)`
Sets the `CommandLine.Model.IGetter` that is responsible for getting the value of the annotated program element associated with this group, and returns this builder.



`String`
`heading()`
Returns the heading of this group, used when generating the usage documentation.



`CommandLine.Model.ArgGroupSpec.Builder`
`heading(String newValue)`
Sets the heading of this group (may be `null`), used when generating the usage documentation.



`String`
`headingKey()`
Returns the heading key of this group, used to get the heading from a resource bundle.



`CommandLine.Model.ArgGroupSpec.Builder`
`headingKey(String newValue)`
Sets the heading key of this group, used to get the heading from a resource bundle.



`CommandLine.Range`
`multiplicity()`
Returns the multiplicity of this group: how many occurrences it may have on the command line; `"0..1"` (optional) by default.



`CommandLine.Model.ArgGroupSpec.Builder`
`multiplicity(CommandLine.Range newValue)`
Sets the multiplicity of this group: how many occurrences it may have on the command line; `"0..1"` (optional) by default.



`CommandLine.Model.ArgGroupSpec.Builder`
`multiplicity(String newValue)`
Sets the multiplicity of this group: how many occurrences it may have on the command line; `"0..1"` (optional) by default.



`int`
`order()`
Returns the position in the options list in the usage help message at which this group should be shown.



`CommandLine.Model.ArgGroupSpec.Builder`
`order(int order)`
Sets the position in the options list in the usage help message at which this group should be shown, and returns this builder.



`CommandLine.Model.IScope`
`scope()`
Returns the `CommandLine.Model.IScope` that determines where the setter sets the value (or the getter gets the value) of the annotated program element associated with this group.



`CommandLine.Model.ArgGroupSpec.Builder`
`scope(CommandLine.Model.IScope scope)`
Sets the `CommandLine.Model.IScope` that targets where the setter sets the value of the annotated program element associated with this group, and returns this builder.



`CommandLine.Model.ISetter`
`setter()`
Returns the `CommandLine.Model.ISetter` that is responsible for modifying the value of the annotated program element associated with this group.



`CommandLine.Model.ArgGroupSpec.Builder`
`setter(CommandLine.Model.ISetter setter)`
Sets the `CommandLine.Model.ISetter` that is responsible for modifying the value of the annotated program element associated with this group, and returns this builder.



`List<CommandLine.Model.IAnnotatedElement>`
`specElements()`
Returns the list of program elements annotated with `{@literal @}Spec` configured for this group.



`List<CommandLine.Model.ArgGroupSpec>`
`subgroups()`
Returns the list of subgroups that this group is composed of.



`CommandLine.Model.ITypeInfo`
`typeInfo()`
Returns the type info for the annotated program element associated with this group.



`CommandLine.Model.ArgGroupSpec.Builder`
`typeInfo(CommandLine.Model.ITypeInfo newValue)`
Sets the type info for the annotated program element associated with this group, and returns this builder.



`CommandLine.Model.ArgGroupSpec.Builder`
`updateArgGroupAttributes(CommandLine.ArgGroup group)`
Updates this builder from the specified annotation values.



`boolean`
`validate()`
Returns whether picocli should validate the rules of this group:
 for a mutually exclusive group this means that no more than one arguments in the group is specified on the command line;
 for a co-occurring group this means that all arguments in the group are specified on the command line.



`CommandLine.Model.ArgGroupSpec.Builder`
`validate(boolean newValue)`
Sets whether picocli should validate the rules of this group:
 for a mutually exclusive group this means that no more than one arguments in the group is specified on the command line;
 for a co-occurring group this means that all arguments in the group are specified on the command line.






    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`













- 




  - 



### Method Detail







    - 

#### updateArgGroupAttributes


```
public CommandLine.Model.ArgGroupSpec.Builder updateArgGroupAttributes(CommandLine.ArgGroup group)
```

Updates this builder from the specified annotation values.

Parameters:
`group` - annotation values
Returns:
this builder for method chaining










    - 

#### build


```
public CommandLine.Model.ArgGroupSpec build()
```

Returns a valid `ArgGroupSpec` instance.









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

#### exclusive


```
public CommandLine.Model.ArgGroupSpec.Builder exclusive(boolean newValue)
```

Sets whether this is a mutually exclusive group; `true` by default.
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

#### multiplicity


```
public CommandLine.Model.ArgGroupSpec.Builder multiplicity(String newValue)
```

Sets the multiplicity of this group: how many occurrences it may have on the command line; `"0..1"` (optional) by default.
 A group can be made required by specifying a multiplicity of `"1"`. For a group of mutually exclusive arguments,
 being required means that one of the arguments in the group must appear on the command line, or a MissingParameterException is thrown.
 For a group of co-occurring arguments, being required means that all arguments in the group must appear on the command line.
 Ignored if `validate()` is `false`.

See Also:
`CommandLine.ArgGroup.multiplicity()`










    - 

#### multiplicity


```
public CommandLine.Model.ArgGroupSpec.Builder multiplicity(CommandLine.Range newValue)
```

Sets the multiplicity of this group: how many occurrences it may have on the command line; `"0..1"` (optional) by default.
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

#### validate


```
public CommandLine.Model.ArgGroupSpec.Builder validate(boolean newValue)
```

Sets whether picocli should validate the rules of this group:
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









    - 

#### order


```
public CommandLine.Model.ArgGroupSpec.Builder order(int order)
```

Sets the position in the options list in the usage help message at which this group should be shown, and returns this builder.









    - 

#### heading


```
public String heading()
```

Returns the heading of this group, used when generating the usage documentation.

See Also:
`CommandLine.ArgGroup.heading()`










    - 

#### heading


```
public CommandLine.Model.ArgGroupSpec.Builder heading(String newValue)
```

Sets the heading of this group (may be `null`), used when generating the usage documentation.

See Also:
`CommandLine.ArgGroup.heading()`










    - 

#### headingKey


```
public String headingKey()
```

Returns the heading key of this group, used to get the heading from a resource bundle.

See Also:
`CommandLine.ArgGroup.headingKey()`










    - 

#### headingKey


```
public CommandLine.Model.ArgGroupSpec.Builder headingKey(String newValue)
```

Sets the heading key of this group, used to get the heading from a resource bundle.

See Also:
`CommandLine.ArgGroup.headingKey()`










    - 

#### typeInfo


```
public CommandLine.Model.ITypeInfo typeInfo()
```

Returns the type info for the annotated program element associated with this group.

Returns:
type information that does not require `Class` objects and be constructed both at runtime and compile time










    - 

#### typeInfo


```
public CommandLine.Model.ArgGroupSpec.Builder typeInfo(CommandLine.Model.ITypeInfo newValue)
```

Sets the type info for the annotated program element associated with this group, and returns this builder.

Parameters:
`newValue` - type information that does not require `Class` objects and be constructed both at runtime and compile time










    - 

#### getter


```
public CommandLine.Model.IGetter getter()
```

Returns the `CommandLine.Model.IGetter` that is responsible for supplying the value of the annotated program element associated with this group.









    - 

#### getter


```
public CommandLine.Model.ArgGroupSpec.Builder getter(CommandLine.Model.IGetter getter)
```

Sets the `CommandLine.Model.IGetter` that is responsible for getting the value of the annotated program element associated with this group, and returns this builder.









    - 

#### setter


```
public CommandLine.Model.ISetter setter()
```

Returns the `CommandLine.Model.ISetter` that is responsible for modifying the value of the annotated program element associated with this group.









    - 

#### setter


```
public CommandLine.Model.ArgGroupSpec.Builder setter(CommandLine.Model.ISetter setter)
```

Sets the `CommandLine.Model.ISetter` that is responsible for modifying the value of the annotated program element associated with this group, and returns this builder.









    - 

#### scope


```
public CommandLine.Model.IScope scope()
```

Returns the `CommandLine.Model.IScope` that determines where the setter sets the value (or the getter gets the value) of the annotated program element associated with this group.









    - 

#### scope


```
public CommandLine.Model.ArgGroupSpec.Builder scope(CommandLine.Model.IScope scope)
```

Sets the `CommandLine.Model.IScope` that targets where the setter sets the value of the annotated program element associated with this group, and returns this builder.









    - 

#### addArg


```
public CommandLine.Model.ArgGroupSpec.Builder addArg(CommandLine.Model.ArgSpec arg)
```

Adds the specified argument to the list of options and positional parameters that depend on this group.









    - 

#### args


```
public List<CommandLine.Model.ArgSpec> args()
```

Returns the list of options and positional parameters that depend on this group.









    - 

#### addSubgroup


```
public CommandLine.Model.ArgGroupSpec.Builder addSubgroup(CommandLine.Model.ArgGroupSpec group)
```

Adds the specified group to the list of subgroups that this group is composed of.









    - 

#### subgroups


```
public List<CommandLine.Model.ArgGroupSpec> subgroups()
```

Returns the list of subgroups that this group is composed of.









    - 

#### addSpecElement


```
public CommandLine.Model.ArgGroupSpec.Builder addSpecElement(CommandLine.Model.IAnnotatedElement element)
```

Adds the specified `{@literal @}Spec` annotated program element to the list of spec elements for this group.

Since:
4.6










    - 

#### specElements


```
public List<CommandLine.Model.IAnnotatedElement> specElements()
```

Returns the list of program elements annotated with `{@literal @}Spec` configured for this group.

Since:
4.6

















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