JavaScript is disabled on your browser.





Skip navigation links






- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help







- Prev Class

- Next Class





- Frames

- No Frames





- All Classes









- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method





- Detail: 

- Field | 

- Constr | 

- Method









picocli

## Class AutoComplete.GenerateCompletion






- java.lang.Object

- 



  - picocli.AutoComplete.GenerateCompletion









- 

All Implemented Interfaces:
Runnable


Enclosing class:
AutoComplete


---




```
public static class AutoComplete.GenerateCompletion
extends Object
implements Runnable
```

Command that generates a Bash/ZSH completion script for its top-level command.
 


 This class can be used as a subcommand for the top-level command in your application.
 Users can then install completion for the top-level command by running the following command:
 

```

 source <(top-level-command [sub-command] generate-completion)
 
```


Since:
4.1









- 




  - 



### Constructor Summary


Constructors 

Constructor and Description


`GenerateCompletion()` 









  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description


`void`
`run()` 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`













- 




  - 



### Constructor Detail







    - 

#### GenerateCompletion


```
public GenerateCompletion()
```











  - 



### Method Detail







    - 

#### run


```
public void run()
```


Specified by:
`run` in interface `Runnable`

















Skip navigation links






- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help







- Prev Class

- Next Class





- Frames

- No Frames





- All Classes









- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method





- Detail: 

- Field | 

- Constr | 

- Method