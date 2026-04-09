Package org.jbake.parser

# Class Engines

java.lang.Object
org.jbake.parser.Engines

---

public class Engines
extends Object

A singleton class giving access to markup engines. Markup engines are loaded based on classpath.
 New engines may be registered either at runtime (not recommanded) or by putting a descriptor file
 on classpath (recommanded).

 

The descriptor file must be found in *META-INF* directory and named
 *org.jbake.parser.MarkupEngines.properties*. The format of the file is easy:
 `
 org.jbake.parser.RawMarkupEngine=html

 org.jbake.parser.AsciidoctorEngine=ad,adoc,asciidoc

 org.jbake.parser.MarkdownEngine=md

 `
 

where the key is the class of the engine (must extend `MarkupEngine` and have a no-arg
 constructor and the value is a comma-separated list of file extensions that this engine is capable of proceeding.

 

Markup engines are singletons, so are typically used to initialize the underlying renderning engines. They
 **must not** store specific information of a currently processed file (use `the parser context`
 for that).

 This class loads the engines only if they are found on classpath. If not, the engine is not registered. This allows
 JBake to support multiple rendering engines without the explicit need to have them on classpath. This is a better
 fit for embedding.

- 

## Method Summary

Modifier and Type
Method
Description
`static ParserEngine`
`get(String fileExtension)`
 
`static Set<String>`
`getRecognizedExtensions()`
 
`static void`
`register(String fileExtension,
 ParserEngine engine)`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### get

public static ParserEngine get(String fileExtension)

  - 

### register

public static void register(String fileExtension,
 ParserEngine engine)

  - 

### getRecognizedExtensions

public static Set<String> getRecognizedExtensions()