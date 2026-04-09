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

## Class CommandLine.Model






- java.lang.Object

- 



  - picocli.CommandLine.Model









- 

Enclosing class:
CommandLine


---




```
public static final class CommandLine.Model
extends Object
```

This class provides a namespace for classes and interfaces that model concepts and attributes of command line interfaces in picocli.

Since:
3.0









- 




  - 



### Nested Class Summary


Nested Classes 

Modifier and Type
Class and Description


`static class `
`CommandLine.Model.ArgGroupSpec`
The `ArgGroupSpec` class models a `group` of arguments (options, positional parameters or a mixture of the two).



`static class `
`CommandLine.Model.ArgSpec`
Models the shared attributes of `CommandLine.Model.OptionSpec` and `CommandLine.Model.PositionalParamSpec`.



`static class `
`CommandLine.Model.CommandSpec`
The `CommandSpec` class models a command specification, including the options, positional parameters and subcommands
 supported by the command, as well as attributes for the version help message and the usage help message of the command.



`static interface `
`CommandLine.Model.IAnnotatedElement`
Internal interface to allow annotation processors to construct a command model at compile time.



`static interface `
`CommandLine.Model.IExtensible`
Interface to allow extending the capabilities of other interface without Java 8 default methods.



`static interface `
`CommandLine.Model.IGetter`
Customizable getter for obtaining the current value of an option or positional parameter.



`static interface `
`CommandLine.Model.IOrdered`
Interface for sorting `options` and `groups` together.



`static interface `
`CommandLine.Model.IScope`
The scope of a getter/setter binding is the context where the current value should be gotten from or set to.



`static interface `
`CommandLine.Model.IScoped`
This interface provides access to an `CommandLine.Model.IScope` instance.



`static interface `
`CommandLine.Model.ISetter`
Customizable setter for modifying the value of an option or positional parameter.



`static interface `
`CommandLine.Model.ITypeInfo`
Encapculates type information for an option or parameter to make this information available both at runtime
 and at compile time (when `Class` values are not available).



`static class `
`CommandLine.Model.Messages`
Utility class for getting resource bundle strings.



`static class `
`CommandLine.Model.MethodParam`
Command method parameter, similar to java.lang.reflect.Parameter (not available before Java 8).



`static class `
`CommandLine.Model.OptionSpec`
The `OptionSpec` class models aspects of a *named option* of a command, including whether
 it is required or optional, the option parameters supported (or required) by the option,
 and attributes for the usage help message describing the option.



`static class `
`CommandLine.Model.ParserSpec`
Models parser configuration specification.



`static class `
`CommandLine.Model.PositionalParamSpec`
The `PositionalParamSpec` class models aspects of a *positional parameter* of a command, including whether
 it is required or optional, and attributes for the usage help message describing the positional parameter.



`static class `
`CommandLine.Model.UnmatchedArgsBinding`
This class allows applications to specify a custom binding that will be invoked for unmatched arguments.



`static class `
`CommandLine.Model.UsageMessageSpec`
Models the usage help message specification and can be used to customize the usage help message.










  - 



### Method Summary




    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`















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