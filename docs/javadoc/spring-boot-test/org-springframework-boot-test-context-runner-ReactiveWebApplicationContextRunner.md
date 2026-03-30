# Class ReactiveWebApplicationContextRunner

java.lang.Object
org.springframework.boot.test.context.runner.AbstractApplicationContextRunner<ReactiveWebApplicationContextRunner, org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext, AssertableReactiveWebApplicationContext>
org.springframework.boot.test.context.runner.ReactiveWebApplicationContextRunner

---

public final class ReactiveWebApplicationContextRunner
extends AbstractApplicationContextRunner<ReactiveWebApplicationContextRunner, org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext, AssertableReactiveWebApplicationContext>
An `ApplicationContext runner` for a
`ConfigurableReactiveWebApplicationContext`.

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
`ReactiveWebApplicationContextRunner()`

Create a new `ReactiveWebApplicationContextRunner` instance using a
`AnnotationConfigReactiveWebApplicationContext` as the underlying source.

`ReactiveWebApplicationContextRunner(Supplier<org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext> contextFactory)`

Create a new `ApplicationContextRunner` instance using the specified
`contextFactory` as the underlying source.

`ReactiveWebApplicationContextRunner(Supplier<org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext> contextFactory,
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

### ReactiveWebApplicationContextRunner

public ReactiveWebApplicationContextRunner()
Create a new `ReactiveWebApplicationContextRunner` instance using a
`AnnotationConfigReactiveWebApplicationContext` as the underlying source.

  - 

### ReactiveWebApplicationContextRunner

public ReactiveWebApplicationContextRunner(Supplier<org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext> contextFactory)
Create a new `ApplicationContextRunner` instance using the specified
`contextFactory` as the underlying source.

Parameters:
`contextFactory` - a supplier that returns a new instance on each call be added
to the application context proxy
Since:
3.4.0

  - 

### ReactiveWebApplicationContextRunner

public ReactiveWebApplicationContextRunner(Supplier<org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext> contextFactory,
 Class<?>... additionalContextInterfaces)
Create a new `ApplicationContextRunner` instance using the specified
`contextFactory` as the underlying source.

Parameters:
`contextFactory` - a supplier that returns a new instance on each call
`additionalContextInterfaces` - any additional application context interfaces to
be added to the application context proxy
Since:
3.4.0