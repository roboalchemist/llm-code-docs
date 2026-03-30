Package com.beust.jcommander

## Class JCommander






- java.lang.Object

- 



  - com.beust.jcommander.JCommander









- 

---


```
public class JCommander
extends java.lang.Object
```

The main class for JCommander. It's responsible for parsing the object that contains
 all the annotated fields, parse the command line and assign the fields with the correct
 values and a few other helper methods, such as usage().

 The object(s) you pass in the constructor are expected to have one or more
 \@Parameter annotations on them. You can pass either a single object, an array of objects
 or an instance of Iterable. In the case of an array or Iterable, JCommander will collect
 the \@Parameter annotations from all the objects passed in parameter.








- 





  - 



### Nested Class Summary


Nested Classes 

Modifier and Type
Class
Description


`static class `
`JCommander.Builder`
 


`static class `
`JCommander.ProgramName`

Encapsulation of either a main application or an individual command.












  - 



### Field Summary


Fields 

Modifier and Type
Field
Description


`static java.lang.String`
`DEBUG_PROPERTY`
 


`protected IParameterizedParser`
`parameterizedParser`
 











  - 



### Constructor Summary


Constructors 

Constructor
Description


`JCommander()`

Creates a new un-configured JCommander object.



`JCommander​(java.lang.Object object)`
 


`JCommander​(java.lang.Object object,
          java.lang.String... args)`

Deprecated.
Construct a JCommander instance first and then call parse() on it.




`JCommander​(java.lang.Object object,
          java.util.ResourceBundle bundle)`
 


`JCommander​(java.lang.Object object,
          java.util.ResourceBundle bundle,
          java.lang.String... args)`
 











  - 



### Method Summary


All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`void`
`addCommand​(java.lang.Object object)`
 


`void`
`addCommand​(java.lang.String name,
          java.lang.Object object)`

Add a command object.



`void`
`addCommand​(java.lang.String name,
          java.lang.Object object,
          java.lang.String... aliases)`

Add a command object and its aliases.



`void`
`addConverterFactory​(IStringConverterFactory converterFactory)`

Adds a factory to lookup string converters.



`void`
`addConverterInstanceFactory​(IStringConverterInstanceFactory converterInstanceFactory)`

Adds a factory to lookup string converters.



`void`
`addObject​(java.lang.Object object)`

Adds the provided arg object to the set of objects that this commander
 will parse arguments into.



`java.lang.Object`
`convertValue​(Parameterized parameterized,
            java.lang.Class type,
            java.lang.String optionName,
            java.lang.String value)`
 


`void`
`createDescriptions()`

Create the ParameterDescriptions for all the \@Parameter found.



`JCommander`
`findCommandByAlias​(java.lang.String commandOrAlias)`
 


`java.util.ResourceBundle`
`getBundle()`
 


`int`
`getColumnSize()`
 


`java.util.Map<java.lang.String,​JCommander>`
`getCommands()`
 


`Console`
`getConsole()`
 


`java.util.Map<com.beust.jcommander.FuzzyMap.IKey,​ParameterDescription>`
`getDescriptions()`
 


`java.util.Map<Parameterized,​ParameterDescription>`
`getFields()`
 


`com.beust.jcommander.JCommander.MainParameter`
`getMainParameter()`
 


`java.lang.String`
`getMainParameterDescription()`
 


`ParameterDescription`
`getMainParameterValue()`
 


`java.util.List<java.lang.Object>`
`getObjects()`
 


`com.beust.jcommander.JCommander.Options`
`getOptions()`
 


`java.util.Comparator<? super ParameterDescription>`
`getParameterDescriptionComparator()`
 


`java.util.List<ParameterDescription>`
`getParameters()`
 


`java.lang.String`
`getParsedAlias()`

The name of the command or the alias in the form it was
 passed to the command line.



`java.lang.String`
`getParsedCommand()`
 


`java.lang.String`
`getProgramDisplayName()`

Get the program display name (used only in the usage).



`java.lang.String`
`getProgramName()`

Get the program name (used only in the usage).



`java.util.Map<JCommander.ProgramName,​JCommander>`
`getRawCommands()`
 


`java.util.List<java.lang.String>`
`getUnknownOptions()`
 


`IUsageFormatter`
`getUsageFormatter()`

Returns the usage formatter.



`boolean`
`isParameterOverwritingAllowed()`
 


`static JCommander.Builder`
`newBuilder()`
 


`void`
`parse​(java.lang.String... args)`

Parse and validate the command line parameters.



`void`
`parseWithoutValidation​(java.lang.String... args)`

Parse the command line parameters without validating them.



`void`
`setAcceptUnknownOptions​(boolean b)`
 


`void`
`setAllowAbbreviatedOptions​(boolean b)`
 


`void`
`setAllowParameterOverwriting​(boolean b)`
 


`void`
`setAtFileCharset​(java.nio.charset.Charset charset)`

Sets the charset used to expand `@files`.



`void`
`setCaseSensitiveOptions​(boolean b)`
 


`void`
`setColumnSize​(int columnSize)`
 


`void`
`setConsole​(Console console)`
 


`void`
`setDefaultProvider​(IDefaultProvider defaultProvider)`

Define the default provider for this instance.



`void`
`setDescriptionsBundle​(java.util.ResourceBundle bundle)`

Sets the `ResourceBundle` to use for looking up descriptions.



`void`
`setExpandAtSign​(boolean expandAtSign)`

Disables expanding `@file`.



`void`
`setParameterDescriptionComparator​(java.util.Comparator<? super ParameterDescription> c)`
 


`void`
`setParameterizedParser​(IParameterizedParser parameterizedParser)`
 


`void`
`setProgramName​(java.lang.String name)`

Set the program name (used only in the usage).



`void`
`setProgramName​(java.lang.String name,
              java.lang.String... aliases)`

Set the program name



`void`
`setUsageFormatter​(IUsageFormatter usageFormatter)`

Sets the usage formatter.



`void`
`setVerbose​(int verbose)`
 


`void`
`usage()`

Prints the usage on `getConsole()` using the underlying `usageFormatter`.






    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Field Detail







    - 

#### DEBUG_PROPERTY


```
public static final java.lang.String DEBUG_PROPERTY
```


See Also:
Constant Field Values










    - 

#### parameterizedParser


```
protected IParameterizedParser parameterizedParser
```













  - 



### Constructor Detail







    - 

#### JCommander


```
public JCommander()
```

Creates a new un-configured JCommander object.









    - 

#### JCommander


```
public JCommander​(java.lang.Object object)
```


Parameters:
`object` - The arg object expected to contain `Parameter` annotations.










    - 

#### JCommander


```
public JCommander​(java.lang.Object object,
                  java.util.ResourceBundle bundle)
```


Parameters:
`object` - The arg object expected to contain `Parameter` annotations.
`bundle` - The bundle to use for the descriptions. Can be null.










    - 

#### JCommander


```
public JCommander​(java.lang.Object object,
                  java.util.ResourceBundle bundle,
                  java.lang.String... args)
```


Parameters:
`object` - The arg object expected to contain `Parameter` annotations.
`bundle` - The bundle to use for the descriptions. Can be null.
`args` - The arguments to parse (optional).










    - 

#### JCommander


```
@Deprecated
public JCommander​(java.lang.Object object,
                  java.lang.String... args)
```

Deprecated.
Construct a JCommander instance first and then call parse() on it.


Parameters:
`object` - The arg object expected to contain `Parameter` annotations.
`args` - The arguments to parse (optional).













  - 



### Method Detail







    - 

#### setParameterizedParser


```
public void setParameterizedParser​(IParameterizedParser parameterizedParser)
```










    - 

#### setExpandAtSign


```
public void setExpandAtSign​(boolean expandAtSign)
```

Disables expanding `@file`.

 JCommander supports the `@file` syntax, which allows you to put all your options
 into a file and pass this file as parameter @param expandAtSign whether to expand `@file`.









    - 

#### setConsole


```
public void setConsole​(Console console)
```










    - 

#### getConsole


```
public Console getConsole()
```


Returns:
a wrapper for a `PrintStream`, typically `System.out`.










    - 

#### addObject


```
public final void addObject​(java.lang.Object object)
```

Adds the provided arg object to the set of objects that this commander
 will parse arguments into.

Parameters:
`object` - The arg object expected to contain `Parameter`
 annotations. If `object` is an array or is `Iterable`,
 the child objects will be added instead.










    - 

#### setDescriptionsBundle


```
public final void setDescriptionsBundle​(java.util.ResourceBundle bundle)
```

Sets the `ResourceBundle` to use for looking up descriptions.
 Set this to `null` to use description text directly.









    - 

#### parse


```
public void parse​(java.lang.String... args)
```

Parse and validate the command line parameters.









    - 

#### parseWithoutValidation


```
public void parseWithoutValidation​(java.lang.String... args)
```

Parse the command line parameters without validating them.









    - 

#### createDescriptions


```
public void createDescriptions()
```

Create the ParameterDescriptions for all the \@Parameter found.









    - 

#### getMainParameterDescription


```
public java.lang.String getMainParameterDescription()
```










    - 

#### setProgramName


```
public void setProgramName​(java.lang.String name)
```

Set the program name (used only in the usage).









    - 

#### getProgramName


```
public java.lang.String getProgramName()
```

Get the program name (used only in the usage).









    - 

#### getProgramDisplayName


```
public java.lang.String getProgramDisplayName()
```

Get the program display name (used only in the usage).









    - 

#### setProgramName


```
public void setProgramName​(java.lang.String name,
                           java.lang.String... aliases)
```

Set the program name

Parameters:
`name` - program name
`aliases` - aliases to the program name










    - 

#### usage


```
public void usage()
```

Prints the usage on `getConsole()` using the underlying `usageFormatter`.









    - 

#### setUsageFormatter


```
public void setUsageFormatter​(IUsageFormatter usageFormatter)
```

Sets the usage formatter.

Parameters:
`usageFormatter` - the usage formatter
Throws:
`java.lang.IllegalArgumentException` - if the argument is null










    - 

#### getUsageFormatter


```
public IUsageFormatter getUsageFormatter()
```

Returns the usage formatter.

Returns:
the usage formatter










    - 

#### getOptions


```
public com.beust.jcommander.JCommander.Options getOptions()
```










    - 

#### getDescriptions


```
public java.util.Map<com.beust.jcommander.FuzzyMap.IKey,​ParameterDescription> getDescriptions()
```










    - 

#### getMainParameter


```
public com.beust.jcommander.JCommander.MainParameter getMainParameter()
```










    - 

#### newBuilder


```
public static JCommander.Builder newBuilder()
```










    - 

#### getFields


```
public java.util.Map<Parameterized,​ParameterDescription> getFields()
```










    - 

#### getParameterDescriptionComparator


```
public java.util.Comparator<? super ParameterDescription> getParameterDescriptionComparator()
```










    - 

#### setParameterDescriptionComparator


```
public void setParameterDescriptionComparator​(java.util.Comparator<? super ParameterDescription> c)
```










    - 

#### setColumnSize


```
public void setColumnSize​(int columnSize)
```










    - 

#### getColumnSize


```
public int getColumnSize()
```










    - 

#### getBundle


```
public java.util.ResourceBundle getBundle()
```










    - 

#### getParameters


```
public java.util.List<ParameterDescription> getParameters()
```


Returns:
a Collection of all the \@Parameter annotations found on the
 target class. This can be used to display the usage() in a different
 format (e.g. HTML).










    - 

#### getMainParameterValue


```
public ParameterDescription getMainParameterValue()
```


Returns:
the main parameter description or null if none is defined.










    - 

#### setDefaultProvider


```
public void setDefaultProvider​(IDefaultProvider defaultProvider)
```

Define the default provider for this instance.









    - 

#### addConverterFactory


```
public void addConverterFactory​(IStringConverterFactory converterFactory)
```

Adds a factory to lookup string converters. The added factory is used prior to previously added factories.

Parameters:
`converterFactory` - the factory determining string converters










    - 

#### addConverterInstanceFactory


```
public void addConverterInstanceFactory​(IStringConverterInstanceFactory converterInstanceFactory)
```

Adds a factory to lookup string converters. The added factory is used prior to previously added factories.

Parameters:
`converterInstanceFactory` - the factory generating string converter instances










    - 

#### convertValue


```
public java.lang.Object convertValue​(Parameterized parameterized,
                                     java.lang.Class type,
                                     java.lang.String optionName,
                                     java.lang.String value)
```


Parameters:
`type` - The type of the actual parameter
`optionName` - 
`value` - The value to convert










    - 

#### addCommand


```
public void addCommand​(java.lang.String name,
                       java.lang.Object object)
```

Add a command object.









    - 

#### addCommand


```
public void addCommand​(java.lang.Object object)
```










    - 

#### addCommand


```
public void addCommand​(java.lang.String name,
                       java.lang.Object object,
                       java.lang.String... aliases)
```

Add a command object and its aliases.









    - 

#### getCommands


```
public java.util.Map<java.lang.String,​JCommander> getCommands()
```










    - 

#### getRawCommands


```
public java.util.Map<JCommander.ProgramName,​JCommander> getRawCommands()
```










    - 

#### getParsedCommand


```
public java.lang.String getParsedCommand()
```










    - 

#### getParsedAlias


```
public java.lang.String getParsedAlias()
```

The name of the command or the alias in the form it was
 passed to the command line. `null` if no
 command or alias was specified.

Returns:
Name of command or alias passed to command line. If none passed: `null`.










    - 

#### getObjects


```
public java.util.List<java.lang.Object> getObjects()
```


Returns:
the objects that JCommander will fill with the result of
 parsing the command line.










    - 

#### findCommandByAlias


```
public JCommander findCommandByAlias​(java.lang.String commandOrAlias)
```










    - 

#### setVerbose


```
public void setVerbose​(int verbose)
```










    - 

#### setCaseSensitiveOptions


```
public void setCaseSensitiveOptions​(boolean b)
```










    - 

#### setAllowAbbreviatedOptions


```
public void setAllowAbbreviatedOptions​(boolean b)
```










    - 

#### setAcceptUnknownOptions


```
public void setAcceptUnknownOptions​(boolean b)
```










    - 

#### getUnknownOptions


```
public java.util.List<java.lang.String> getUnknownOptions()
```










    - 

#### setAllowParameterOverwriting


```
public void setAllowParameterOverwriting​(boolean b)
```










    - 

#### isParameterOverwritingAllowed


```
public boolean isParameterOverwritingAllowed()
```










    - 

#### setAtFileCharset


```
public void setAtFileCharset​(java.nio.charset.Charset charset)
```

Sets the charset used to expand `@files`.

Parameters:
`charset` - the charset