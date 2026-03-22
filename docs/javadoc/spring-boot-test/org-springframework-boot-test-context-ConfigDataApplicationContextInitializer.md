# Class ConfigDataApplicationContextInitializer

java.lang.Object
org.springframework.boot.test.context.ConfigDataApplicationContextInitializer

All Implemented Interfaces:
`org.springframework.context.ApplicationContextInitializer<org.springframework.context.ConfigurableApplicationContext>`

---

public class ConfigDataApplicationContextInitializer
extends Object
implements org.springframework.context.ApplicationContextInitializer<org.springframework.context.ConfigurableApplicationContext>
`ApplicationContextInitializer` that can be used with the
`ContextConfiguration.initializers()` to trigger loading of `ConfigData`
such as application.properties.

Since:
2.4.0
See Also:

- `ConfigDataEnvironmentPostProcessor`

- 

## Constructor Summary

Constructors

Constructor
Description
`ConfigDataApplicationContextInitializer()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`initialize(org.springframework.context.ConfigurableApplicationContext applicationContext)`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### ConfigDataApplicationContextInitializer

public ConfigDataApplicationContextInitializer()

- 

## Method Details

  - 

### initialize

public void initialize(org.springframework.context.ConfigurableApplicationContext applicationContext)

Specified by:
`initialize` in interface `org.springframework.context.ApplicationContextInitializer<org.springframework.context.ConfigurableApplicationContext>`