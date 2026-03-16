# Class SpringBootTestAotProcessor

java.lang.Object
org.springframework.context.aot.AbstractAotProcessor<Void>
org.springframework.test.context.aot.TestAotProcessor
org.springframework.boot.test.context.SpringBootTestAotProcessor

---

public class SpringBootTestAotProcessor
extends org.springframework.test.context.aot.TestAotProcessor
Entry point for AOT processing of a Spring Boot application's tests.

**For internal use only.**

Since:
3.0.0

- 

## Nested Class Summary

### Nested classes/interfaces inherited from class org.springframework.context.aot.AbstractAotProcessor

`org.springframework.context.aot.AbstractAotProcessor.Settings`

- 

## Field Summary

### Fields inherited from class org.springframework.context.aot.AbstractAotProcessor

`AOT_PROCESSING`

- 

## Constructor Summary

Constructors

Constructor
Description
`SpringBootTestAotProcessor(Set<Path> classpathRoots,
 org.springframework.context.aot.AbstractAotProcessor.Settings settings)`

Create a new processor for the specified test classpath roots and general settings.

- 

## Method Summary

Modifier and Type
Method
Description
`static void`
`main(String[] args)`
 

### Methods inherited from class org.springframework.test.context.aot.TestAotProcessor

`doProcess, getClasspathRoots, performAotProcessing, scanClasspathRoots`

### Methods inherited from class org.springframework.context.aot.AbstractAotProcessor

`createFileSystemGeneratedFiles, deleteExistingOutput, getSettings, process, writeHints`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### SpringBootTestAotProcessor

public SpringBootTestAotProcessor(Set<Path> classpathRoots,
 org.springframework.context.aot.AbstractAotProcessor.Settings settings)
Create a new processor for the specified test classpath roots and general settings.

Parameters:
`classpathRoots` - the classpath roots to scan for test classes
`settings` - the general AOT processor settings

- 

## Method Details

  - 

### main

public static void main(String[] args)