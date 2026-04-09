Package com.beust.jcommander.defaultprovider

## Class PropertyFileDefaultProvider






- java.lang.Object

- 



  - com.beust.jcommander.defaultprovider.PropertyFileDefaultProvider









- 

All Implemented Interfaces:
`IDefaultProvider`


---


```
public class PropertyFileDefaultProvider
extends java.lang.Object
implements IDefaultProvider
```

A default provider that reads its default values from a property file.








- 





  - 



### Field Summary


Fields 

Modifier and Type
Field
Description


`static java.lang.String`
`DEFAULT_FILE_NAME`
 











  - 



### Constructor Summary


Constructors 

Constructor
Description


`PropertyFileDefaultProvider()`
 


`PropertyFileDefaultProvider​(java.lang.String fileName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.lang.String`
`getDefaultValueFor​(java.lang.String optionName)`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Field Detail







    - 

#### DEFAULT_FILE_NAME


```
public static final java.lang.String DEFAULT_FILE_NAME
```


See Also:
Constant Field Values













  - 



### Constructor Detail







    - 

#### PropertyFileDefaultProvider


```
public PropertyFileDefaultProvider()
```










    - 

#### PropertyFileDefaultProvider


```
public PropertyFileDefaultProvider​(java.lang.String fileName)
```













  - 



### Method Detail







    - 

#### getDefaultValueFor


```
public java.lang.String getDefaultValueFor​(java.lang.String optionName)
```


Specified by:
`getDefaultValueFor` in interface `IDefaultProvider`
Parameters:
`optionName` - The name of the option as specified in the names() attribute
 of the @Parameter option (e.g. "-file").
Returns:
the default value for this option.