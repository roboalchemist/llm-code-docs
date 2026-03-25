Package com.beust.jcommander

## Class Parameterized






- java.lang.Object

- 



  - com.beust.jcommander.Parameterized









- 

---


```
public class Parameterized
extends java.lang.Object
```

Encapsulate a field or a method annotated with @Parameter or @DynamicParameter








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`Parameterized​(WrappedParameter wp,
             ParametersDelegate pd,
             java.lang.reflect.Field field,
             java.lang.reflect.Method method)`
 











  - 



### Method Summary


All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`boolean`
`equals​(java.lang.Object obj)`
 


`java.lang.reflect.Type`
`findFieldGenericType()`
 


`java.lang.Object`
`get​(java.lang.Object object)`
 


`ParametersDelegate`
`getDelegateAnnotation()`
 


`java.lang.reflect.Type`
`getGenericType()`
 


`java.lang.String`
`getName()`
 


`Parameter`
`getParameter()`
 


`java.lang.Class<?>`
`getType()`
 


`WrappedParameter`
`getWrappedParameter()`
 


`int`
`hashCode()`
 


`boolean`
`isDynamicParameter()`
 


`boolean`
`isDynamicParameter​(java.lang.reflect.Field field)`
 


`static java.util.List<Parameterized>`
`parseArg​(java.lang.Object arg)`
 


`void`
`set​(java.lang.Object object,
   java.lang.Object value)`
 





    - 



### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### Parameterized


```
public Parameterized​(WrappedParameter wp,
                     ParametersDelegate pd,
                     java.lang.reflect.Field field,
                     java.lang.reflect.Method method)
```













  - 



### Method Detail







    - 

#### parseArg


```
public static java.util.List<Parameterized> parseArg​(java.lang.Object arg)
```










    - 

#### getWrappedParameter


```
public WrappedParameter getWrappedParameter()
```










    - 

#### getType


```
public java.lang.Class<?> getType()
```










    - 

#### getName


```
public java.lang.String getName()
```










    - 

#### get


```
public java.lang.Object get​(java.lang.Object object)
```










    - 

#### hashCode


```
public int hashCode()
```


Overrides:
`hashCode` in class `java.lang.Object`










    - 

#### equals


```
public boolean equals​(java.lang.Object obj)
```


Overrides:
`equals` in class `java.lang.Object`










    - 

#### isDynamicParameter


```
public boolean isDynamicParameter​(java.lang.reflect.Field field)
```










    - 

#### set


```
public void set​(java.lang.Object object,
                java.lang.Object value)
```










    - 

#### getDelegateAnnotation


```
public ParametersDelegate getDelegateAnnotation()
```










    - 

#### getGenericType


```
public java.lang.reflect.Type getGenericType()
```










    - 

#### getParameter


```
public Parameter getParameter()
```










    - 

#### findFieldGenericType


```
public java.lang.reflect.Type findFieldGenericType()
```


Returns:
the generic type of the collection for this field, or null if not applicable.










    - 

#### isDynamicParameter


```
public boolean isDynamicParameter()
```