Package com.beust.jcommander

## Class FuzzyMap






- java.lang.Object

- 



  - com.beust.jcommander.FuzzyMap









- 

---


```
public class FuzzyMap
extends java.lang.Object
```

Helper class to perform fuzzy key look ups: looking up case insensitive or
 abbreviated keys.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`FuzzyMap()`
 











  - 



### Method Summary


All Methods Static Methods Concrete Methods 

Modifier and Type
Method
Description


`static <V> V`
`findInMap​(java.util.Map<? extends com.beust.jcommander.FuzzyMap.IKey,​V> map,
         com.beust.jcommander.FuzzyMap.IKey name,
         boolean caseSensitive,
         boolean allowAbbreviations)`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### FuzzyMap


```
public FuzzyMap()
```













  - 



### Method Detail







    - 

#### findInMap


```
public static <V> V findInMap​(java.util.Map<? extends com.beust.jcommander.FuzzyMap.IKey,​V> map,
                              com.beust.jcommander.FuzzyMap.IKey name,
                              boolean caseSensitive,
                              boolean allowAbbreviations)
```