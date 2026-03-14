Package com.beust.jcommander

## Class WrappedParameter






- java.lang.Object

- 



  - com.beust.jcommander.WrappedParameter









- 

---


```
public class WrappedParameter
extends java.lang.Object
```

Encapsulates the operations common to @Parameter and @DynamicParameter








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`WrappedParameter​(DynamicParameter p)`
 


`WrappedParameter​(Parameter p)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`void`
`addValue​(Parameterized parameterized,
        java.lang.Object object,
        java.lang.Object value)`
 


`void`
`addValue​(Parameterized parameterized,
        java.lang.Object object,
        java.lang.Object value,
        java.lang.reflect.Field field)`
 


`int`
`arity()`
 


`boolean`
`echoInput()`
 


`java.lang.String`
`getAssignment()`
 


`DynamicParameter`
`getDynamicParameter()`
 


`Parameter`
`getParameter()`
 


`boolean`
`hidden()`
 


`boolean`
`isHelp()`
 


`boolean`
`isNonOverwritableForced()`
 


`java.lang.String[]`
`names()`
 


`int`
`order()`
 


`boolean`
`password()`
 


`boolean`
`required()`
 


`java.lang.Class<? extends IValueValidator>[]`
`validateValueWith()`
 


`java.lang.Class<? extends IParameterValidator>[]`
`validateWith()`
 


`boolean`
`variableArity()`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### WrappedParameter


```
public WrappedParameter​(Parameter p)
```










    - 

#### WrappedParameter


```
public WrappedParameter​(DynamicParameter p)
```













  - 



### Method Detail







    - 

#### getParameter


```
public Parameter getParameter()
```










    - 

#### getDynamicParameter


```
public DynamicParameter getDynamicParameter()
```










    - 

#### arity


```
public int arity()
```










    - 

#### hidden


```
public boolean hidden()
```










    - 

#### required


```
public boolean required()
```










    - 

#### password


```
public boolean password()
```










    - 

#### names


```
public java.lang.String[] names()
```










    - 

#### variableArity


```
public boolean variableArity()
```










    - 

#### order


```
public int order()
```










    - 

#### validateWith


```
public java.lang.Class<? extends IParameterValidator>[] validateWith()
```










    - 

#### validateValueWith


```
public java.lang.Class<? extends IValueValidator>[] validateValueWith()
```










    - 

#### echoInput


```
public boolean echoInput()
```










    - 

#### addValue


```
public void addValue​(Parameterized parameterized,
                     java.lang.Object object,
                     java.lang.Object value)
```










    - 

#### addValue


```
public void addValue​(Parameterized parameterized,
                     java.lang.Object object,
                     java.lang.Object value,
                     java.lang.reflect.Field field)
              throws java.lang.IllegalAccessException
```


Throws:
`java.lang.IllegalAccessException`










    - 

#### getAssignment


```
public java.lang.String getAssignment()
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