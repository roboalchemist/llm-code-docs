Package com.beust.jcommander

## Annotation Type DynamicParameter







- 

---


```
@Retention(RUNTIME)
@Target(FIELD)
public @interface DynamicParameter
```









- 





  - 



### Optional Element Summary


Optional Elements 

Modifier and Type
Optional Element
Description


`java.lang.String`
`assignment`

The character(s) used to assign the values.



`java.lang.String`
`description`

A description of this option.



`java.lang.String`
`descriptionKey`

The key used to find the string in the message bundle.



`boolean`
`hidden`

If true, this parameter won't appear in the usage().



`java.lang.String[]`
`names`

An array of allowed command line parameters (e.g.



`int`
`order`

If specified, this number will be used to order the description of this parameter when usage() is invoked.



`boolean`
`required`

Whether this option is required.



`java.lang.Class<? extends IValueValidator>[]`
`validateValueWith`
 


`java.lang.Class<? extends IParameterValidator>[]`
`validateWith`

The validation classes to use.















- 





  - 



### Element Detail







    - 

#### names


```
java.lang.String[] names
```

An array of allowed command line parameters (e.g. "-D", "--define", etc...).

Default:
{}












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

#### description


```
java.lang.String description
```

A description of this option.

Default:
""












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

The validation classes to use.

Default:
{com.beust.jcommander.validators.NoValidator.class}












  - 





    - 

#### assignment


```
java.lang.String assignment
```

The character(s) used to assign the values.

Default:
"="












  - 





    - 

#### validateValueWith


```
java.lang.Class<? extends IValueValidator>[] validateValueWith
```


Default:
{com.beust.jcommander.validators.NoValueValidator.class}












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