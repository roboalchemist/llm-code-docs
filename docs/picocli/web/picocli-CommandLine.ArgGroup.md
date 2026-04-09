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

## Annotation Type CommandLine.ArgGroup







- 

---




```
@Retention(value=RUNTIME)
 @Target(value={FIELD,METHOD,PARAMETER})
public static @interface CommandLine.ArgGroup
```

A `Command` may define one or more `ArgGroups`: a group of options, positional parameters or a mixture of the two.
 Groups can be used to:
 

     
  - define **mutually exclusive** arguments. By default, options and positional parameters
     in a group are mutually exclusive. This can be controlled with the `exclusive` attribute.
     Picocli will throw a `CommandLine.MutuallyExclusiveArgsException` if the command line contains multiple arguments that are mutually exclusive.
     
  - define a set of arguments that **must co-occur**. Set `exclusive = false`
     to define a group of options and positional parameters that must always be specified together.
     Picocli will throw a `MissingParameterException` if not all the options and positional parameters in a co-occurring group are specified together.
     
  - create an **option section** in the usage help message.
     To be shown in the usage help message, a group needs to have a `heading` (which may come from a resource bundle).
     Groups without a heading are only used for validation.
     Set `validate = false` for groups whose purpose is only to customize the usage help message.
     
  - define **composite repeating argument groups**. Groups may contain other groups to create composite groups.
 

 

Groups may be optional (`multiplicity = "0..1"`), required (`multiplicity = "1"`), or repeating groups (`multiplicity = "0..*"` or `multiplicity = "1..*"`).
 For a group of mutually exclusive arguments, making the group required means that one of the arguments in the group must appear on the command line, or a `MissingParameterException` is thrown.
 For a group of co-occurring arguments, all arguments in the group must appear on the command line.
 
 

Groups can be composed for validation purposes:
 

 
  - When the parent group is mutually exclusive, only one of the subgroups may be present.
 
  - When the parent group is a co-occurring group, all subgroups must be present.
 
  - When the parent group is required, at least one subgroup must be present.
 

 


 Below is an example of an `ArgGroup` defining a set of dependent options that must occur together.
 All options are required *within the group*, while the group itself is optional:
 

```

 public class DependentOptions {
     @ArgGroup(exclusive = false, multiplicity = "0..1")
     Dependent group;

     static class Dependent {
         @Option(names = "-a", required = true) int a;
         @Option(names = "-b", required = true) int b;
         @Option(names = "-c", required = true) int c;
     }
 }
```


Since:
4.0
See Also:
`CommandLine.Model.ArgGroupSpec`









- 




  - 



### Optional Element Summary


Optional Elements 

Modifier and Type
Optional Element and Description


`boolean`
`exclusive`
Determines whether this is a mutually exclusive group; `true` by default.



`String`
`heading`
The heading of this group, used when generating the usage documentation.



`String`
`headingKey`
ResourceBundle key for this group's usage help message section heading.



`String`
`multiplicity`
Determines how often this group can be specified on the command line; `"0..1"` (optional) by default.



`int`
`order`
Determines the position in the options list in the usage help message at which this group should be shown.



`boolean`
`validate`
Determines whether picocli should validate the rules of this group (`true` by default).














- 




  - 



### Element Detail







    - 

#### heading


```
public abstract String heading
```

The heading of this group, used when generating the usage documentation.
 When neither a `heading` nor a `headingKey` are specified,
 this group is used for validation only and does not change the usage help message.

Default:
"__no_heading__"










  - 





    - 

#### headingKey


```
public abstract String headingKey
```

ResourceBundle key for this group's usage help message section heading.
 When neither a `heading` nor a `headingKey` are specified,
 this group is used for validation only and does not change the usage help message.

Default:
"__no_heading_key__"










  - 





    - 

#### exclusive


```
public abstract boolean exclusive
```

Determines whether this is a mutually exclusive group; `true` by default.
 If `false`, this is a co-occurring group. Ignored if `validate()` is `false`.

Default:
true










  - 





    - 

#### multiplicity


```
public abstract String multiplicity
```

Determines how often this group can be specified on the command line; `"0..1"` (optional) by default.
 For a group of mutually exclusive arguments, making the group required `multiplicity = "1"` means that
 one of the arguments in the group must appear on the command line, or a MissingParameterException is thrown.
 For a group of co-occurring arguments, making the group required means that all arguments in the group must appear on the command line.
 Ignored if `validate()` is `false`.

Default:
"0..1"










  - 





    - 

#### validate


```
public abstract boolean validate
```

Determines whether picocli should validate the rules of this group (`true` by default).
 For a mutually exclusive group validation means verifying that no more than one elements of the group is specified on the command line;
 for a co-occurring group validation means verifying that all elements of the group are specified on the command line.
 Set `validate = false` for groups whose purpose is only to customize the usage help message.

See Also:
`multiplicity()`, 
`heading()`


Default:
true










  - 





    - 

#### order


```
public abstract int order
```

Determines the position in the options list in the usage help message at which this group should be shown.
 Groups with a lower number are shown before groups with a higher number.
 This attribute is only honored for groups that have a `heading` (or a `headingKey` with a non-`null` resource bundle value).

Default:
-1

















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