# Class SpringBootContextLoader

java.lang.Object
org.springframework.test.context.support.AbstractContextLoader
org.springframework.boot.test.context.SpringBootContextLoader

All Implemented Interfaces:
`org.springframework.test.context.aot.AotContextLoader, org.springframework.test.context.ContextLoader, org.springframework.test.context.SmartContextLoader`

---

public class SpringBootContextLoader
extends org.springframework.test.context.support.AbstractContextLoader
implements org.springframework.test.context.aot.AotContextLoader
A `ContextLoader` that can be used to test Spring Boot applications (those that
normally startup using `SpringApplication`). Although this loader can be used
directly, most test will instead want to use it with
`@SpringBootTest`.

The loader supports both standard `MergedContextConfiguration` as well as
`WebMergedContextConfiguration`. If `WebMergedContextConfiguration` is used
the context will either use a mock servlet environment, or start the full embedded web
server.

If `@ActiveProfiles` are provided in the test class they will be used to create
the application context.

Since:
1.4.0
See Also:

- `SpringBootTest`

- 

## Constructor Summary

Constructors

Constructor
Description
`SpringBootContextLoader()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`protected Class<?>[]`
`detectDefaultConfigurationClasses(Class<?> declaringClass)`

Detect the default configuration classes for the supplied test class.

`protected org.springframework.boot.ApplicationContextFactory`
`getApplicationContextFactory(org.springframework.test.context.MergedContextConfiguration mergedConfig)`

Return the `ApplicationContextFactory` that should be used for the test.

`protected @Nullable org.springframework.core.env.ConfigurableEnvironment`
`getEnvironment()`

Returns the `ConfigurableEnvironment` instance that should be applied to
`SpringApplication` or `null` to use the default.

`protected List<org.springframework.context.ApplicationContextInitializer<?>>`
`getInitializers(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 org.springframework.boot.SpringApplication application)`

Return the `initializers` that will be applied
to the context.

`protected String[]`
`getInlinedProperties(org.springframework.test.context.MergedContextConfiguration mergedConfig)`
 
`protected String`
`getResourceSuffix()`
 
`protected String[]`
`getResourceSuffixes()`
 
`protected org.springframework.boot.SpringApplication`
`getSpringApplication()`

Builds new `SpringApplication` instance.

`org.springframework.context.ApplicationContext`
`loadContext(org.springframework.test.context.MergedContextConfiguration mergedConfig)`
 
`org.springframework.context.ApplicationContext`
`loadContextForAotProcessing(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 org.springframework.aot.hint.RuntimeHints runtimeHints)`
 
`org.springframework.context.ApplicationContext`
`loadContextForAotRuntime(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 org.springframework.context.ApplicationContextInitializer<org.springframework.context.ConfigurableApplicationContext> initializer)`
 
`void`
`processContextConfiguration(org.springframework.test.context.ContextConfigurationAttributes configAttributes)`
 

### Methods inherited from class org.springframework.test.context.support.AbstractContextLoader

`customizeContext, generateDefaultLocations, isGenerateDefaultLocations, modifyLocations, prepareContext, processLocations`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.springframework.test.context.aot.AotContextLoader

`loadContextForAotProcessing`

### Methods inherited from interface org.springframework.test.context.SmartContextLoader

`loadContext, processLocations`

- 

## Constructor Details

  - 

### SpringBootContextLoader

public SpringBootContextLoader()

- 

## Method Details

  - 

### loadContext

public org.springframework.context.ApplicationContext loadContext(org.springframework.test.context.MergedContextConfiguration mergedConfig)
                                                           throws Exception

Specified by:
`loadContext` in interface `org.springframework.test.context.SmartContextLoader`
Throws:
`Exception`

  - 

### loadContextForAotProcessing

public org.springframework.context.ApplicationContext loadContextForAotProcessing(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 org.springframework.aot.hint.RuntimeHints runtimeHints)
                                                                           throws Exception

Specified by:
`loadContextForAotProcessing` in interface `org.springframework.test.context.aot.AotContextLoader`
Throws:
`Exception`

  - 

### loadContextForAotRuntime

public org.springframework.context.ApplicationContext loadContextForAotRuntime(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 org.springframework.context.ApplicationContextInitializer<org.springframework.context.ConfigurableApplicationContext> initializer)
                                                                        throws Exception

Specified by:
`loadContextForAotRuntime` in interface `org.springframework.test.context.aot.AotContextLoader`
Throws:
`Exception`

  - 

### getApplicationContextFactory

protected org.springframework.boot.ApplicationContextFactory getApplicationContextFactory(org.springframework.test.context.MergedContextConfiguration mergedConfig)
Return the `ApplicationContextFactory` that should be used for the test. By
default this method will return a factory that will create an appropriate
`ApplicationContext` for the `WebApplicationType`.

Parameters:
`mergedConfig` - the merged context configuration
Returns:
the application context factory to use
Since:
3.2.0

  - 

### getSpringApplication

protected org.springframework.boot.SpringApplication getSpringApplication()
Builds new `SpringApplication` instance. This method
is only called when a `main` method isn't being used to create the
`SpringApplication`.

Returns:
a `SpringApplication` instance

  - 

### getEnvironment

protected @Nullable org.springframework.core.env.ConfigurableEnvironment getEnvironment()
Returns the `ConfigurableEnvironment` instance that should be applied to
`SpringApplication` or `null` to use the default. You can override this
method if you need a custom environment.

Returns:
a `ConfigurableEnvironment` instance

  - 

### getInlinedProperties

protected String[] getInlinedProperties(org.springframework.test.context.MergedContextConfiguration mergedConfig)

  - 

### getInitializers

protected List<org.springframework.context.ApplicationContextInitializer<?>> getInitializers(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 org.springframework.boot.SpringApplication application)
Return the `initializers` that will be applied
to the context. By default this method will adapt `context
customizers`, add `application
initializers` and add
`initializers
specified on the test`.

Parameters:
`mergedConfig` - the source context configuration
`application` - the application instance
Returns:
the initializers to apply
Since:
2.0.0

  - 

### processContextConfiguration

public void processContextConfiguration(org.springframework.test.context.ContextConfigurationAttributes configAttributes)

Specified by:
`processContextConfiguration` in interface `org.springframework.test.context.SmartContextLoader`
Overrides:
`processContextConfiguration` in class `org.springframework.test.context.support.AbstractContextLoader`

  - 

### detectDefaultConfigurationClasses

protected Class<?>[] detectDefaultConfigurationClasses(Class<?> declaringClass)
Detect the default configuration classes for the supplied test class. By default
simply delegates to
`AnnotationConfigContextLoaderUtils.detectDefaultConfigurationClasses(Class)`.

Parameters:
`declaringClass` - the test class that declared `@ContextConfiguration`
Returns:
an array of default configuration classes, potentially empty but never
`null`
See Also:

    - `AnnotationConfigContextLoaderUtils`

  - 

### getResourceSuffixes

protected String[] getResourceSuffixes()

Overrides:
`getResourceSuffixes` in class `org.springframework.test.context.support.AbstractContextLoader`

  - 

### getResourceSuffix

protected String getResourceSuffix()

Specified by:
`getResourceSuffix` in class `org.springframework.test.context.support.AbstractContextLoader`