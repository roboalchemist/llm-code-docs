Package com.beust.jcommander

## Class JCommander.Builder






- java.lang.Object

- 



  - com.beust.jcommander.JCommander.Builder









- 

Enclosing class:
JCommander


---


```
public static class JCommander.Builder
extends java.lang.Object
```









- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`Builder()`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`JCommander.Builder`
`acceptUnknownOptions​(boolean b)`
 


`JCommander.Builder`
`addCommand​(java.lang.Object command)`
 


`JCommander.Builder`
`addCommand​(java.lang.String name,
          java.lang.Object command,
          java.lang.String... aliases)`
 


`JCommander.Builder`
`addConverterFactory​(IStringConverterFactory factory)`

Adds a factory to lookup string converters.



`JCommander.Builder`
`addConverterInstanceFactory​(IStringConverterInstanceFactory factory)`
 


`JCommander.Builder`
`addObject​(java.lang.Object o)`

Adds the provided arg object to the set of objects that this commander
 will parse arguments into.



`JCommander.Builder`
`allowAbbreviatedOptions​(boolean b)`
 


`JCommander.Builder`
`allowParameterOverwriting​(boolean b)`
 


`JCommander.Builder`
`args​(java.lang.String[] args)`
 


`JCommander.Builder`
`atFileCharset​(java.nio.charset.Charset charset)`
 


`JCommander`
`build()`
 


`JCommander.Builder`
`columnSize​(int columnSize)`
 


`JCommander.Builder`
`console​(Console console)`
 


`JCommander.Builder`
`defaultProvider​(IDefaultProvider provider)`

Define the default provider for this instance.



`JCommander.Builder`
`expandAtSign​(java.lang.Boolean expand)`

Disables expanding `@file`.



`JCommander.Builder`
`programName​(java.lang.String name)`

Set the program name (used only in the usage).



`JCommander.Builder`
`resourceBundle​(java.util.ResourceBundle bundle)`

Sets the `ResourceBundle` to use for looking up descriptions.



`JCommander.Builder`
`usageFormatter​(IUsageFormatter usageFormatter)`
 


`JCommander.Builder`
`verbose​(int verbose)`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### Builder


```
public Builder()
```













  - 



### Method Detail







    - 

#### addObject


```
public JCommander.Builder addObject​(java.lang.Object o)
```

Adds the provided arg object to the set of objects that this commander
 will parse arguments into.

Parameters:
`o` - The arg object expected to contain `Parameter`
 annotations. If `object` is an array or is `Iterable`,
 the child objects will be added instead.










    - 

#### resourceBundle


```
public JCommander.Builder resourceBundle​(java.util.ResourceBundle bundle)
```

Sets the `ResourceBundle` to use for looking up descriptions.
 Set this to `null` to use description text directly.









    - 

#### args


```
public JCommander.Builder args​(java.lang.String[] args)
```










    - 

#### console


```
public JCommander.Builder console​(Console console)
```










    - 

#### expandAtSign


```
public JCommander.Builder expandAtSign​(java.lang.Boolean expand)
```

Disables expanding `@file`.

 JCommander supports the `@file` syntax, which allows you to put all your options
 into a file and pass this file as parameter @param expandAtSign whether to expand `@file`.









    - 

#### programName


```
public JCommander.Builder programName​(java.lang.String name)
```

Set the program name (used only in the usage).









    - 

#### columnSize


```
public JCommander.Builder columnSize​(int columnSize)
```










    - 

#### defaultProvider


```
public JCommander.Builder defaultProvider​(IDefaultProvider provider)
```

Define the default provider for this instance.









    - 

#### addConverterFactory


```
public JCommander.Builder addConverterFactory​(IStringConverterFactory factory)
```

Adds a factory to lookup string converters. The added factory is used prior to previously added factories.

Parameters:
`factory` - the factory determining string converters










    - 

#### verbose


```
public JCommander.Builder verbose​(int verbose)
```










    - 

#### allowAbbreviatedOptions


```
public JCommander.Builder allowAbbreviatedOptions​(boolean b)
```










    - 

#### acceptUnknownOptions


```
public JCommander.Builder acceptUnknownOptions​(boolean b)
```










    - 

#### allowParameterOverwriting


```
public JCommander.Builder allowParameterOverwriting​(boolean b)
```










    - 

#### atFileCharset


```
public JCommander.Builder atFileCharset​(java.nio.charset.Charset charset)
```










    - 

#### addConverterInstanceFactory


```
public JCommander.Builder addConverterInstanceFactory​(IStringConverterInstanceFactory factory)
```










    - 

#### addCommand


```
public JCommander.Builder addCommand​(java.lang.Object command)
```










    - 

#### addCommand


```
public JCommander.Builder addCommand​(java.lang.String name,
                                     java.lang.Object command,
                                     java.lang.String... aliases)
```










    - 

#### usageFormatter


```
public JCommander.Builder usageFormatter​(IUsageFormatter usageFormatter)
```










    - 

#### build


```
public JCommander build()
```