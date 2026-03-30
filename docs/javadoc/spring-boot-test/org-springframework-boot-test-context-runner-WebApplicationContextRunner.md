# Class WebApplicationContextRunner

java.lang.Object
org.springframework.boot.test.context.runner.AbstractApplicationContextRunner<WebApplicationContextRunner, org.springframework.web.context.ConfigurableWebApplicationContext, AssertableWebApplicationContext>
org.springframework.boot.test.context.runner.WebApplicationContextRunner

---

public final class WebApplicationContextRunner
extends AbstractApplicationContextRunner<WebApplicationContextRunner, org.springframework.web.context.ConfigurableWebApplicationContext, AssertableWebApplicationContext>
An `ApplicationContext runner` for a Servlet
based `ConfigurableWebApplicationContext`.

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
`WebApplicationContextRunner()`

Create a new `WebApplicationContextRunner` instance using an
`AnnotationConfigServletWebApplicationContext` with a
`MockServletContext` as the underlying source.

`WebApplicationContextRunner(Supplier<org.springframework.web.context.ConfigurableWebApplicationContext> contextFactory)`

Create a new `WebApplicationContextRunner` instance using the specified
`contextFactory` as the underlying source.

`WebApplicationContextRunner(Supplier<org.springframework.web.context.ConfigurableWebApplicationContext> contextFactory,
 Class<?>... additionalContextInterfaces)`

Create a new `WebApplicationContextRunner` instance using the specified
`contextFactory` as the underlying source.

- 

## Method Summary

Modifier and Type
Method
Description
`static @Nullable Supplier<org.springframework.web.context.ConfigurableWebApplicationContext>`
`withMockServletContext(@Nullable Supplier<org.springframework.web.context.ConfigurableWebApplicationContext> contextFactory)`

Decorate the specified `contextFactory` to set a `MockServletContext`
on each newly created `WebApplicationContext`.

### Methods inherited from class AbstractApplicationContextRunner

`prepare, run, with, withAllowBeanDefinitionOverriding, withAllowCircularReferences, withBean, withBean, withBean, withBean, withClassLoader, withConfiguration, withInitializer, withParent, withPropertyValues, withSystemProperties, withUserConfiguration`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### WebApplicationContextRunner

public WebApplicationContextRunner()
Create a new `WebApplicationContextRunner` instance using an
`AnnotationConfigServletWebApplicationContext` with a
`MockServletContext` as the underlying source.

See Also:

    - `withMockServletContext(Supplier)`

  - 

### WebApplicationContextRunner

public WebApplicationContextRunner(Supplier<org.springframework.web.context.ConfigurableWebApplicationContext> contextFactory)
Create a new `WebApplicationContextRunner` instance using the specified
`contextFactory` as the underlying source.

Parameters:
`contextFactory` - a supplier that returns a new instance on each call be added
to the application context proxy

  - 

### WebApplicationContextRunner

public WebApplicationContextRunner(Supplier<org.springframework.web.context.ConfigurableWebApplicationContext> contextFactory,
 Class<?>... additionalContextInterfaces)
Create a new `WebApplicationContextRunner` instance using the specified
`contextFactory` as the underlying source.

Parameters:
`contextFactory` - a supplier that returns a new instance on each call
`additionalContextInterfaces` - any additional application context interfaces to
be added to the application context proxy
Since:
3.4.0

- 

## Method Details

  - 

### withMockServletContext

@Contract("!null -> !null")
public static @Nullable Supplier<org.springframework.web.context.ConfigurableWebApplicationContext> withMockServletContext(@Nullable Supplier<org.springframework.web.context.ConfigurableWebApplicationContext> contextFactory)
Decorate the specified `contextFactory` to set a `MockServletContext`
on each newly created `WebApplicationContext`.

Parameters:
`contextFactory` - the context factory to decorate
Returns:
an updated supplier that will set the `MockServletContext`