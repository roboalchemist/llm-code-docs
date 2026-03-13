Package com.beust.jcommander

## Annotation Type Parameter







- 

---


```
@Retention(RUNTIME)
@Target({FIELD,METHOD})
public @interface Parameter
```









- 





  - 



### Field Summary


Fields 

Modifier and Type
Fields
Description


`static int`
`DEFAULT_ARITY`

How many parameter values this parameter will consume.












  - 



### Optional Element Summary


Optional Elements 

Modifier and Type
Optional Element
Description


`int`
`arity`
 


`java.lang.Class<? extends IStringConverter<?>>`
`converter`

The string converter to use for this field.



`java.lang.String`
`description`

A description of this option.



`java.lang.String`
`descriptionKey`

The key used to find the string in the message bundle.



`boolean`
`echoInput`

If true, console will not echo typed input
 Used in conjunction with password = true



`boolean`
`forceNonOverwritable`

If true, this parameter can be overwritten through a file or another appearance of the parameter



`boolean`
`help`

If true, this parameter is for help.



`boolean`
`hidden`

If true, this parameter won't appear in the usage().



`java.lang.Class<? extends IStringConverter<?>>`
`listConverter`

The list string converter to use for this field.



`java.lang.String[]`
`names`

An array of allowed command line parameters (e.g.



`int`
`order`

If specified, this number will be used to order the description of this parameter when usage() is invoked.



`boolean`
`password`

If true, this parameter is a password and it will be prompted on the console
 (if available).



`boolean`
`required`

Whether this option is required.



`java.lang.Class<? extends IParameterSplitter>`
`splitter`

What splitter to use (applicable only on fields of type List).



`java.lang.Class<? extends IValueValidator>[]`
`validateValueWith`

Validate the value for this parameter.



`java.lang.Class<? extends IParameterValidator>[]`
`validateWith`

Validate the parameter found on the command line.



`boolean`
`variableArity`
 














- 





  - 



### Field Detail







    - 

#### DEFAULT_ARITY


```
static final int DEFAULT_ARITY
```

How many parameter values this parameter will consume. For example,
 an arity of 2 will allow "-pair value1 value2".












  - 



### Element Detail







    - 

#### names


```
java.lang.String[] names
```

An array of allowed command line parameters (e.g. "-d", "--outputdir", etc...).
 If this attribute is omitted, the field it's annotating will receive all the
 unparsed options. There can only be at most one such annotation.

Default:
{}












  - 





    - 

#### description


```
java.lang.String description
```

A description of this option.

Default:
""












  - 





    - 

#### required


```
boolean required
```

Whether this option is required.

Default:
false












  - 





    - 

#### descriptionKey


```
java.lang.String descriptionKey
```

The key used to find the string in the message bundle.

Default:
""












  - 





    - 

#### arity


```
int arity
```


Default:
-1












  - 





    - 

#### password


```
boolean password
```

If true, this parameter is a password and it will be prompted on the console
 (if available).

Default:
false












  - 





    - 

#### converter


```
java.lang.Class<? extends IStringConverter<?>> converter
```

The string converter to use for this field. If the field is of type List
 and not listConverter attribute was specified, JCommander will split
 the input in individual values and convert each of them separately.

Default:
com.beust.jcommander.converters.NoConverter.class












  - 





    - 

#### listConverter


```
java.lang.Class<? extends IStringConverter<?>> listConverter
```

The list string converter to use for this field. If it's specified, the
 field has to be of type List and the converter needs to return
 a List that's compatible with that type.

Default:
com.beust.jcommander.converters.NoConverter.class












  - 





    - 

#### hidden


```
boolean hidden
```

If true, this parameter won't appear in the usage().

Default:
false












  - 





    - 

#### validateWith


```
java.lang.Class<? extends IParameterValidator>[] validateWith
```

Validate the parameter found on the command line.

Default:
{com.beust.jcommander.validators.NoValidator.class}












  - 





    - 

#### validateValueWith


```
java.lang.Class<? extends IValueValidator>[] validateValueWith
```

Validate the value for this parameter.

Default:
{com.beust.jcommander.validators.NoValueValidator.class}












  - 





    - 

#### variableArity


```
boolean variableArity
```


Returns:
true if this parameter has a variable arity. See @{IVariableArity}


Default:
false












  - 





    - 

#### splitter


```
java.lang.Class<? extends IParameterSplitter> splitter
```

What splitter to use (applicable only on fields of type List). By default,
 a comma separated splitter will be used.

Default:
com.beust.jcommander.converters.CommaParameterSplitter.class












  - 





    - 

#### echoInput


```
boolean echoInput
```

If true, console will not echo typed input
 Used in conjunction with password = true

Default:
false












  - 





    - 

#### help


```
boolean help
```

If true, this parameter is for help. If such a parameter is specified,
 required parameters are no longer checked for their presence.

Default:
false












  - 





    - 

#### forceNonOverwritable


```
boolean forceNonOverwritable
```

If true, this parameter can be overwritten through a file or another appearance of the parameter

Returns:
nc


Default:
false












  - 





    - 

#### order


```
int order
```

If specified, this number will be used to order the description of this parameter when usage() is invoked.

Returns:


Default:
-1