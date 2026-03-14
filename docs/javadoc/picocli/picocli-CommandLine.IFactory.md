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

## Interface CommandLine.IFactory







- 

Enclosing class:
CommandLine


---




```
public static interface CommandLine.IFactory
```

Factory for instantiating classes that are registered declaratively with annotation attributes, like
 `CommandLine.Command.subcommands()`, `CommandLine.Option.converter()`, `CommandLine.Parameters.converter()` and `CommandLine.Command.versionProvider()`.
 The factory is also used to instantiate the `Collection` or `Map` implementation class for multi-value
 options and positional parameters with an abstract type, like `List<String>`.
 

You may provide a custom implementation of this interface.
 For example, a custom factory implementation could delegate to a dependency injection container that provides the requested instance.
 

***Custom factory implementations should always fall back to the default factory if instantiation failed.*** For example:
 
 

```

 class MyFactory implements IFactory {
     private final ApplicationContext applicationContext = getAppContext();

     public <T> T create(Class<T> cls) throws Exception {
         try {
             applicationContext.getBean(cls);
         } catch (Exception ex) {
             CommandLine.defaultFactory().create(cls);
         }
     }
 }
 
```

 

Tip: custom factory implementations that have resources that need to be closed when done should consider
 implementing `java.lang.AutoCloseable` or `java.io.Closeable`. This allows applications to use
 the following idiom for configuring picocli before running their application:
 

```

 public static void main(String[] args) {
     int exitCode = 0;
     try (MyFactory factory = createMyFactory()) {
         exitCode = new CommandLine(MyClass.class, factory)
                 .setXxx(x) // configure the picocli parser...
                 .execute(args);
     }
     System.exit(exitCode);
 }
 
```


Since:
2.2
See Also:
`CommandLine.CommandLine(Object, IFactory)`, 
`CommandLine.call(Class, IFactory, PrintStream, PrintStream, Help.Ansi, String...)`, 
`CommandLine.run(Class, IFactory, PrintStream, PrintStream, Help.Ansi, String...)`, 
`CommandLine.defaultFactory()`









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`<K> K`
`create(Class<K> cls)`
Returns an instance of the specified class.














- 




  - 



### Method Detail







    - 

#### create


```
<K> K create(Class<K> cls)
      throws Exception
```

Returns an instance of the specified class.

Type Parameters:
`K` - the type of the object to return
Parameters:
`cls` - the class of the object to return
Returns:
the instance
Throws:
`Exception` - an exception detailing what went wrong when creating or obtaining the instance

















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