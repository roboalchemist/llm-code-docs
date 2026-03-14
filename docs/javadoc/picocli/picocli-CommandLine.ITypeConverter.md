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

## Interface CommandLine.ITypeConverter<K>







- 

Type Parameters:
`K` - the type of the object that is the result of the conversion


All Known Implementing Classes:
CommandLine.UseDefaultConverter


Enclosing class:
CommandLine


---




```
public static interface CommandLine.ITypeConverter<K>
```



 When parsing command line arguments and initializing
 fields annotated with `@Option` or `@Parameters`,
 String values can be converted to any type for which a `ITypeConverter` is registered.
 


 This interface defines the contract for classes that know how to convert a String into some domain object.
 Custom converters can be registered with the `CommandLine.registerConverter(Class, ITypeConverter)` method.
 


 Java 8 lambdas make it easy to register custom type converters:
 
 

```

 commandLine.registerConverter(java.nio.file.Path.class, s -> java.nio.file.Paths.get(s));
 commandLine.registerConverter(java.time.Duration.class, s -> java.time.Duration.parse(s));
```

 


 Built-in type converters are pre-registered for the following java 1.5 types:
 
 

   
  - all primitive types
   
  - all primitive wrapper types: Boolean, Byte, Character, Double, Float, Integer, Long, Short
   
  - any enum
   
  - java.io.File
   
  - java.math.BigDecimal
   
  - java.math.BigInteger
   
  - java.net.InetAddress
   
  - java.net.URI
   
  - java.net.URL
   
  - java.nio.charset.Charset
   
  - java.sql.Time
   
  - java.util.Date
   
  - java.util.UUID
   
  - java.util.regex.Pattern
   
  - StringBuilder
   
  - CharSequence
   
  - String
 









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`K`
`convert(String value)`
Converts the specified command line argument value to some domain object.














- 




  - 



### Method Detail







    - 

#### convert


```
K convert(String value)
   throws Exception
```

Converts the specified command line argument value to some domain object.

Parameters:
`value` - the command line argument String value
Returns:
the resulting domain object
Throws:
`Exception` - an exception detailing what went wrong during the conversion.
          Any exception thrown from this method will be caught and shown to the end user.
          An example error message shown to the end user could look something like this:
          `Invalid value for option '--some-option': cannot convert 'xxxinvalidinput' to SomeType (java.lang.IllegalArgumentException: Invalid format: must be 'x:y:z' but was 'xxxinvalidinput')`
`CommandLine.TypeConversionException` - throw this exception to have more control over the error
          message that is shown to the end user when type conversion fails.
          An example message shown to the user could look like this:
          `Invalid value for option '--some-option': Invalid format: must be 'x:y:z' but was 'xxxinvalidinput'`

















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