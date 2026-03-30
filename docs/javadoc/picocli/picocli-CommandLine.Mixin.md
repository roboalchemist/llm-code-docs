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

- Field | 

- Required | 

- Optional





- Detail: 

- Field | 

- Element









picocli

## Annotation Type CommandLine.Mixin







- 

---




```
@Retention(value=RUNTIME)
 @Target(value={FIELD,PARAMETER})
public static @interface CommandLine.Mixin
```



 Fields annotated with `@Mixin` are "expanded" into the current command: `@Option` and
 `@Parameters` in the mixin class are added to the options and positional parameters of this command.
 A `CommandLine.DuplicateOptionAnnotationsException` is thrown if any of the options in the mixin has the same name as
 an option in this command.
 


 The `Mixin` annotation provides a way to reuse common options and parameters without subclassing. For example:
 

```

 @Command(name="HelloWorld")
 class HelloWorld implements Runnable {

     // adds the --help and --version options to this command
     @Mixin
     private HelpOptions options = new HelpOptions();

     @Option(names = {"-u", "--userName"}, required = true, description = "The user name")
     String userName;

     public void run() { System.out.println("Hello, " + userName); }
 }

 // Common reusable help options.
 class HelpOptions {

     @Option(names = { "-h", "--help"}, usageHelp = true, description = "Display this help and exit")
     private boolean help;

     @Option(names = { "-V", "--version"}, versionHelp = true, description = "Display version info and exit")
     private boolean versionHelp;
 }
 
```


Since:
3.0









- 




  - 



### Optional Element Summary


Optional Elements 

Modifier and Type
Optional Element and Description


`String`
`name`
Optionally specify a name that the mixin object can be retrieved with from the `CommandSpec`.














- 




  - 



### Element Detail







    - 

#### name


```
public abstract String name
```

Optionally specify a name that the mixin object can be retrieved with from the `CommandSpec`.
 If not specified the name of the annotated field is used.

Returns:
a String to register the mixin object with, or an empty String if the name of the annotated field should be used


Default:
""

















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

- Field | 

- Required | 

- Optional





- Detail: 

- Field | 

- Element