# Class SpringBootTestContextBootstrapper

java.lang.Object
org.springframework.test.context.support.AbstractTestContextBootstrapper
org.springframework.test.context.support.DefaultTestContextBootstrapper
org.springframework.boot.test.context.SpringBootTestContextBootstrapper

All Implemented Interfaces:
`org.springframework.test.context.TestContextBootstrapper`

---

public class SpringBootTestContextBootstrapper
extends org.springframework.test.context.support.DefaultTestContextBootstrapper
`TestContextBootstrapper` for Spring Boot. Provides support for
`@SpringBootTest` and may also be used directly or subclassed.
Provides the following features over and above `DefaultTestContextBootstrapper`:

- Uses `SpringBootContextLoader` as the
`default context loader`.

- Automatically searches for a
`@SpringBootConfiguration` when required.

- Allows custom `Environment` `getProperties(Class)` to be defined.

- Provides support for different `webEnvironment` modes.

Since:
1.4.0
See Also:

- `SpringBootTest`

- `TestConfiguration`

- 

## Constructor Summary

Constructors

Constructor
Description
`SpringBootTestContextBootstrapper()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`org.springframework.test.context.TestContext`
`buildTestContext()`
 
`protected final org.springframework.test.context.MergedContextConfiguration`
`createModifiedConfig(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 Class<?>[] classes)`

Create a new `MergedContextConfiguration` with different classes.

`protected final org.springframework.test.context.MergedContextConfiguration`
`createModifiedConfig(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 Class<?>[] classes,
 String[] propertySourceProperties)`

Create a new `MergedContextConfiguration` with different classes and
properties.

`protected String`
`determineResourceBasePath(org.springframework.test.context.MergedContextConfiguration configuration)`

Determines the resource base path for web applications using the value of
`@WebAppConfiguration`, if any, on the test class of the
given `configuration`.

`protected @Nullable SpringBootTest`
`getAnnotation(Class<?> testClass)`
 
`protected Class<?> @Nullable []`
`getClasses(Class<?> testClass)`
 
`protected Class<? extends org.springframework.test.context.ContextLoader>`
`getDefaultContextLoaderClass(Class<?> testClass)`
 
`protected @Nullable String`
`getDifferentiatorPropertySourceProperty()`

Return a "differentiator" property to ensure that there is something to
differentiate regular tests and bootstrapped tests.

`protected Class<?>[]`
`getOrFindConfigurationClasses(org.springframework.test.context.MergedContextConfiguration mergedConfig)`
 
`protected String @Nullable []`
`getProperties(Class<?> testClass)`
 
`protected @Nullable SpringBootTest.WebEnvironment`
`getWebEnvironment(Class<?> testClass)`

Return the `SpringBootTest.WebEnvironment` type for this test or null if undefined.

`protected org.springframework.test.context.MergedContextConfiguration`
`processMergedContextConfiguration(org.springframework.test.context.MergedContextConfiguration mergedConfig)`
 
`protected void`
`processPropertySourceProperties(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 List<String> propertySourceProperties)`

Post process the property source properties, adding or removing elements as
required.

`protected org.springframework.test.context.ContextLoader`
`resolveContextLoader(Class<?> testClass,
 List<org.springframework.test.context.ContextConfigurationAttributes> configAttributesList)`
 
`protected void`
`verifyConfiguration(Class<?> testClass)`
 

### Methods inherited from class org.springframework.test.context.support.AbstractTestContextBootstrapper

`buildMergedContextConfiguration, getBootstrapContext, getCacheAwareContextLoaderDelegate, getContextCustomizerFactories, getDefaultTestExecutionListeners, getTestExecutionListeners, resolveExplicitContextLoaderClass, setBootstrapContext`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### SpringBootTestContextBootstrapper

public SpringBootTestContextBootstrapper()

- 

## Method Details

  - 

### buildTestContext

public org.springframework.test.context.TestContext buildTestContext()

Specified by:
`buildTestContext` in interface `org.springframework.test.context.TestContextBootstrapper`
Overrides:
`buildTestContext` in class `org.springframework.test.context.support.AbstractTestContextBootstrapper`

  - 

### resolveContextLoader

protected org.springframework.test.context.ContextLoader resolveContextLoader(Class<?> testClass,
 List<org.springframework.test.context.ContextConfigurationAttributes> configAttributesList)

Overrides:
`resolveContextLoader` in class `org.springframework.test.context.support.AbstractTestContextBootstrapper`

  - 

### getDefaultContextLoaderClass

protected Class<? extends org.springframework.test.context.ContextLoader> getDefaultContextLoaderClass(Class<?> testClass)

Overrides:
`getDefaultContextLoaderClass` in class `org.springframework.test.context.support.DefaultTestContextBootstrapper`

  - 

### processMergedContextConfiguration

protected org.springframework.test.context.MergedContextConfiguration processMergedContextConfiguration(org.springframework.test.context.MergedContextConfiguration mergedConfig)

Overrides:
`processMergedContextConfiguration` in class `org.springframework.test.context.support.AbstractTestContextBootstrapper`

  - 

### determineResourceBasePath

protected String determineResourceBasePath(org.springframework.test.context.MergedContextConfiguration configuration)
Determines the resource base path for web applications using the value of
`@WebAppConfiguration`, if any, on the test class of the
given `configuration`. Defaults to `src/main/webapp` in its absence.

Parameters:
`configuration` - the configuration to examine
Returns:
the resource base path
Since:
2.1.6

  - 

### getOrFindConfigurationClasses

protected Class<?>[] getOrFindConfigurationClasses(org.springframework.test.context.MergedContextConfiguration mergedConfig)

  - 

### getDifferentiatorPropertySourceProperty

protected @Nullable String getDifferentiatorPropertySourceProperty()
Return a "differentiator" property to ensure that there is something to
differentiate regular tests and bootstrapped tests. Without this property a cached
context could be returned that wasn't created by this bootstrapper. By default uses
the bootstrapper class as a property.

Returns:
the differentiator or `null`

  - 

### processPropertySourceProperties

protected void processPropertySourceProperties(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 List<String> propertySourceProperties)
Post process the property source properties, adding or removing elements as
required.

Parameters:
`mergedConfig` - the merged context configuration
`propertySourceProperties` - the property source properties to process

  - 

### getWebEnvironment

protected @Nullable SpringBootTest.WebEnvironment getWebEnvironment(Class<?> testClass)
Return the `SpringBootTest.WebEnvironment` type for this test or null if undefined.

Parameters:
`testClass` - the source test class
Returns:
the `SpringBootTest.WebEnvironment` or `null`

  - 

### getClasses

protected Class<?> @Nullable [] getClasses(Class<?> testClass)

  - 

### getProperties

protected String @Nullable [] getProperties(Class<?> testClass)

  - 

### getAnnotation

protected @Nullable SpringBootTest getAnnotation(Class<?> testClass)

  - 

### verifyConfiguration

protected void verifyConfiguration(Class<?> testClass)

  - 

### createModifiedConfig

protected final org.springframework.test.context.MergedContextConfiguration createModifiedConfig(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 Class<?>[] classes)
Create a new `MergedContextConfiguration` with different classes.

Parameters:
`mergedConfig` - the source config
`classes` - the replacement classes
Returns:
a new `MergedContextConfiguration`

  - 

### createModifiedConfig

protected final org.springframework.test.context.MergedContextConfiguration createModifiedConfig(org.springframework.test.context.MergedContextConfiguration mergedConfig,
 Class<?>[] classes,
 String[] propertySourceProperties)
Create a new `MergedContextConfiguration` with different classes and
properties.

Parameters:
`mergedConfig` - the source config
`classes` - the replacement classes
`propertySourceProperties` - the replacement properties
Returns:
a new `MergedContextConfiguration`