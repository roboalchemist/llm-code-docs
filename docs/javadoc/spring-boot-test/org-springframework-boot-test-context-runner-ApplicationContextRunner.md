# Class ApplicationContextRunner

java.lang.Object
org.springframework.boot.test.context.runner.AbstractApplicationContextRunner<ApplicationContextRunner, org.springframework.context.ConfigurableApplicationContext, AssertableApplicationContext>
org.springframework.boot.test.context.runner.ApplicationContextRunner

---

public class ApplicationContextRunner
extends AbstractApplicationContextRunner<ApplicationContextRunner, org.springframework.context.ConfigurableApplicationContext, AssertableApplicationContext>
An `ApplicationContext runner` for a standard,
non-web environment `ConfigurableApplicationContext`.

See `AbstractApplicationContextRunner` for details.

Since:
2.0.0

- 

## Nested Class Summary

### Nested classes/interfaces inherited from class AbstractApplicationContextRunner

`AbstractApplicationContextRunner.BeanRegistration<T>, AbstractApplicationContextRunner.RunnerConfiguration<C>`

- 

## Constructor Summary

Constructors

Constructor
Description
`ApplicationContextRunner()`

Create a new `ApplicationContextRunner` instance using an
`AnnotationConfigApplicationContext` as the underlying source.

`ApplicationContextRunner(Supplier<org.springframework.context.ConfigurableApplicationContext> contextFactory)`

Create a new `ApplicationContextRunner` instance using the specified
`contextFactory` as the underlying source.

`ApplicationContextRunner(Supplier<org.springframework.context.ConfigurableApplicationContext> contextFactory,
 Class<?>... additionalContextInterfaces)`

Create a new `ApplicationContextRunner` instance using the specified
`contextFactory` as the underlying source.

- 

## Method Summary

### Methods inherited from class AbstractApplicationContextRunner

`prepare, run, with, withAllowBeanDefinitionOverriding, withAllowCircularReferences, withBean, withBean, withBean, withBean, withClassLoader, withConfiguration, withInitializer, withParent, withPropertyValues, withSystemProperties, withUserConfiguration`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### ApplicationContextRunner

public ApplicationContextRunner()
Create a new `ApplicationContextRunner` instance using an
`AnnotationConfigApplicationContext` as the underlying source.

  - 

### ApplicationContextRunner

public ApplicationContextRunner(Supplier<org.springframework.context.ConfigurableApplicationContext> contextFactory)
Create a new `ApplicationContextRunner` instance using the specified
`contextFactory` as the underlying source.

Parameters:
`contextFactory` - a supplier that returns a new instance on each call be added
to the application context proxy

  - 

### ApplicationContextRunner

public ApplicationContextRunner(Supplier<org.springframework.context.ConfigurableApplicationContext> contextFactory,
 Class<?>... additionalContextInterfaces)
Create a new `ApplicationContextRunner` instance using the specified
`contextFactory` as the underlying source.

Parameters:
`contextFactory` - a supplier that returns a new instance on each call
`additionalContextInterfaces` - any additional application context interfaces to
be added to the application context proxy
Since:
3.4.0