Package com.beust.jcommander

## Class ParameterDescription






- java.lang.Object

- 



  - com.beust.jcommander.ParameterDescription









- 

---


```
public class ParameterDescription
extends java.lang.Object
```









- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`ParameterDescription​(java.lang.Object object,
                    DynamicParameter annotation,
                    Parameterized parameterized,
                    java.util.ResourceBundle bundle,
                    JCommander jc)`
 


`ParameterDescription​(java.lang.Object object,
                    Parameter annotation,
                    Parameterized parameterized,
                    java.util.ResourceBundle bundle,
                    JCommander jc)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`void`
`addValue​(java.lang.String value)`
 


`void`
`addValue​(java.lang.String value,
        boolean isDefault)`

Add the specified value to the field.



`java.lang.Object`
`getDefault()`
 


`java.lang.String`
`getDescription()`
 


`java.lang.String`
`getLongestName()`
 


`java.lang.String`
`getNames()`
 


`java.lang.Object`
`getObject()`
 


`WrappedParameter`
`getParameter()`
 


`Parameter`
`getParameterAnnotation()`
 


`Parameterized`
`getParameterized()`
 


`boolean`
`isAssigned()`
 


`boolean`
`isDynamicParameter()`
 


`boolean`
`isHelp()`
 


`boolean`
`isNonOverwritableForced()`
 


`void`
`setAssigned​(boolean b)`
 


`java.lang.String`
`toString()`
 


`void`
`validateParameter​(java.lang.Class<? extends IParameterValidator> validator,
                 java.lang.String name,
                 java.lang.String value)`
 


`void`
`validateValueParameter​(java.lang.Class<? extends IValueValidator> validator,
                      java.lang.String name,
                      java.lang.Object value)`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### ParameterDescription


```
public ParameterDescription​(java.lang.Object object,
                            DynamicParameter annotation,
                            Parameterized parameterized,
                            java.util.ResourceBundle bundle,
                            JCommander jc)
```










    - 

#### ParameterDescription


```
public ParameterDescription​(java.lang.Object object,
                            Parameter annotation,
                            Parameterized parameterized,
                            java.util.ResourceBundle bundle,
                            JCommander jc)
```













  - 



### Method Detail







    - 

#### getLongestName


```
public java.lang.String getLongestName()
```










    - 

#### getDefault


```
public java.lang.Object getDefault()
```










    - 

#### getDescription


```
public java.lang.String getDescription()
```










    - 

#### getObject


```
public java.lang.Object getObject()
```










    - 

#### getNames


```
public java.lang.String getNames()
```










    - 

#### getParameter


```
public WrappedParameter getParameter()
```










    - 

#### getParameterized


```
public Parameterized getParameterized()
```










    - 

#### addValue


```
public void addValue​(java.lang.String value)
```










    - 

#### isAssigned


```
public boolean isAssigned()
```


Returns:
true if this parameter received a value during the parsing phase.










    - 

#### setAssigned


```
public void setAssigned​(boolean b)
```










    - 

#### addValue


```
public void addValue​(java.lang.String value,
                     boolean isDefault)
```

Add the specified value to the field. First, validate the value if a
 validator was specified. Then look up any field converter, then any type
 converter, and if we can't find any, throw an exception.









    - 

#### getParameterAnnotation


```
public Parameter getParameterAnnotation()
```










    - 

#### validateValueParameter


```
public void validateValueParameter​(java.lang.Class<? extends IValueValidator> validator,
                                   java.lang.String name,
                                   java.lang.Object value)
```










    - 

#### validateParameter


```
public void validateParameter​(java.lang.Class<? extends IParameterValidator> validator,
                              java.lang.String name,
                              java.lang.String value)
```










    - 

#### toString


```
public java.lang.String toString()
```


Overrides:
`toString` in class `java.lang.Object`










    - 

#### isDynamicParameter


```
public boolean isDynamicParameter()
```










    - 

#### isHelp


```
public boolean isHelp()
```










    - 

#### isNonOverwritableForced


```
public boolean isNonOverwritableForced()
```