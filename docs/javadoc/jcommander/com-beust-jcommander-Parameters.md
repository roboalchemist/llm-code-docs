Package com.beust.jcommander

## Annotation Type Parameters







- 

---


```
@Retention(RUNTIME)
@Target(TYPE)
@Inherited
public @interface Parameters
```

An annotation used to specify settings for parameter parsing.








- 





  - 



### Optional Element Summary


Optional Elements 

Modifier and Type
Optional Element
Description


`java.lang.String`
`commandDescription`

If the annotated class was added to `JCommander` as a command with
 `JCommander.addCommand(java.lang.String, java.lang.Object)`, then this string will be displayed in the
 description when `JCommander.usage()` is invoked.



`java.lang.String`
`commandDescriptionKey`
 


`java.lang.String[]`
`commandNames`

An array of allowed command names.



`boolean`
`hidden`

If true, this command won't appear in the usage().



`java.lang.String`
`resourceBundle`

The name of the resource bundle to use for this class.



`java.lang.String`
`separators`

The character(s) that separate options.















- 





  - 



### Element Detail







    - 

#### resourceBundle


```
java.lang.String resourceBundle
```

The name of the resource bundle to use for this class.

Default:
""












  - 





    - 

#### separators


```
java.lang.String separators
```

The character(s) that separate options.

Default:
" "












  - 





    - 

#### commandDescription


```
java.lang.String commandDescription
```

If the annotated class was added to `JCommander` as a command with
 `JCommander.addCommand(java.lang.String, java.lang.Object)`, then this string will be displayed in the
 description when `JCommander.usage()` is invoked.

Default:
""












  - 





    - 

#### commandDescriptionKey


```
java.lang.String commandDescriptionKey
```


Returns:
the key used to find the command description in the resource bundle.


Default:
""












  - 





    - 

#### commandNames


```
java.lang.String[] commandNames
```

An array of allowed command names.

Default:
{}












  - 





    - 

#### hidden


```
boolean hidden
```

If true, this command won't appear in the usage().

Default:
false