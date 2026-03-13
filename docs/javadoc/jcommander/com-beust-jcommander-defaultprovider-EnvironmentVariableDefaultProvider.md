Package com.beust.jcommander.defaultprovider

## Class EnvironmentVariableDefaultProvider






- java.lang.Object

- 



  - com.beust.jcommander.defaultprovider.EnvironmentVariableDefaultProvider









- 

All Implemented Interfaces:
`IDefaultProvider`


---


```
public final class EnvironmentVariableDefaultProvider
extends java.lang.Object
implements IDefaultProvider
```

A default provider that reads its default values from an environment
 variable.
 
 A prefix pattern can be provided to indicate how options are identified.
 The default pattern `-/` mandates that options MUST start with either a dash or a slash.
 Options can have values separated by whitespace.
 Values can contain whitespace as long as they are single-quoted or double-quoted.
 Otherwhise whitespace identifies the end of a value.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`EnvironmentVariableDefaultProvider()`

Creates a default provider reading the environment variable `JCOMMANDER_OPTS` using the prefixes pattern `-/`.



`EnvironmentVariableDefaultProvider​(java.lang.String environmentVariableName,
                                  java.lang.String optionPrefixes)`

Creates a default provider reading the specified environment variable using the specified prefixes pattern.












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



### Constructor Detail







    - 

#### EnvironmentVariableDefaultProvider


```
public EnvironmentVariableDefaultProvider()
```

Creates a default provider reading the environment variable `JCOMMANDER_OPTS` using the prefixes pattern `-/`.









    - 

#### EnvironmentVariableDefaultProvider


```
public EnvironmentVariableDefaultProvider​(java.lang.String environmentVariableName,
                                          java.lang.String optionPrefixes)
```

Creates a default provider reading the specified environment variable using the specified prefixes pattern.

Parameters:
`environmentVariableName` - The name of the environment variable to read (e. g. `"JCOMMANDER_OPTS"`). Must not be `null`.
`optionPrefixes` - A set of characters used to indicate the start of an option (e. g. `"-/"` if option names may start with either dash or slash). Must not be `null`.













  - 



### Method Detail







    - 

#### getDefaultValueFor


```
public final java.lang.String getDefaultValueFor​(java.lang.String optionName)
```


Specified by:
`getDefaultValueFor` in interface `IDefaultProvider`
Parameters:
`optionName` - The name of the option as specified in the names() attribute
 of the @Parameter option (e.g. "-file").
Returns:
the default value for this option.