Package com.beust.jcommander

## Interface IUsageFormatter







- 

All Known Implementing Classes:
`DefaultUsageFormatter`, `UnixStyleUsageFormatter`


---


```
public interface IUsageFormatter
```

A formatter for help messages.








- 





  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description


`java.lang.String`
`getCommandDescription​(java.lang.String commandName)`
 


`void`
`usage​(java.lang.String commandName)`

Display the usage for this command.



`void`
`usage​(java.lang.StringBuilder out)`

Store the help in the passed string builder.



`void`
`usage​(java.lang.StringBuilder out,
     java.lang.String indent)`

Stores the help in the passed string builder, with the argument indentation.



`void`
`usage​(java.lang.String commandName,
     java.lang.StringBuilder out)`

Store the help for the command in the passed string builder.



`void`
`usage​(java.lang.String commandName,
     java.lang.StringBuilder out,
     java.lang.String indent)`

Store the help for the command in the passed string builder, indenting every line with "indent".















- 





  - 



### Method Detail







    - 

#### usage


```
void usage​(java.lang.String commandName)
```

Display the usage for this command.









    - 

#### usage


```
void usage​(java.lang.String commandName,
           java.lang.StringBuilder out)
```

Store the help for the command in the passed string builder.









    - 

#### usage


```
void usage​(java.lang.StringBuilder out)
```

Store the help in the passed string builder.









    - 

#### usage


```
void usage​(java.lang.String commandName,
           java.lang.StringBuilder out,
           java.lang.String indent)
```

Store the help for the command in the passed string builder, indenting every line with "indent".









    - 

#### usage


```
void usage​(java.lang.StringBuilder out,
           java.lang.String indent)
```

Stores the help in the passed string builder, with the argument indentation.









    - 

#### getCommandDescription


```
java.lang.String getCommandDescription​(java.lang.String commandName)
```


Returns:
the description of the argument command