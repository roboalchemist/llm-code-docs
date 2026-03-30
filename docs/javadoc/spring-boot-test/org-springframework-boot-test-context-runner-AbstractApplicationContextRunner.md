# Class AbstractApplicationContextRunner<SELF extends AbstractApplicationContextRunner<SELF,C,A>, C extends org.springframework.context.ConfigurableApplicationContext, A extends ApplicationContextAssertProvider<C>>

java.lang.Object
org.springframework.boot.test.context.runner.AbstractApplicationContextRunner<SELF,C,A>

Type Parameters:
`SELF` - the "self" type for this runner
`C` - the context type
`A` - the application context assertion provider

Direct Known Subclasses:
`ApplicationContextRunner, ReactiveWebApplicationContextRunner, WebApplicationContextRunner`

---

public abstract class AbstractApplicationContextRunner<SELF extends AbstractApplicationContextRunner<SELF,C,A>, C extends org.springframework.context.ConfigurableApplicationContext, A extends ApplicationContextAssertProvider<C>>
extends Object
Utility design to run an `ApplicationContext` and provide AssertJ style
assertions. The test is best used as a field of a test class, describing the shared
configuration required for the test:

```

public class MyContextTests {
    private final ApplicationContextRunner contextRunner = new ApplicationContextRunner()
            .withPropertyValues("spring.foo=bar")
            .withUserConfiguration(MyConfiguration.class);
}
```

The initialization above makes sure to register `MyConfiguration` for all tests
and set the `spring.foo` property to `bar` unless specified otherwise.

Based on the configuration above, a specific test can simulate what will happen when
the context runs, perhaps with overridden property values:

```

@Test
public someTest() {
    this.contextRunner.withPropertyValues("spring.foo=biz").run((context) -> {
        assertThat(context).containsSingleBean(MyBean.class);
        // other assertions
    });
}
```

The test above has changed the `spring.foo` property to `biz` and is
asserting that the context contains a single `MyBean` bean. The
`run` method takes a `ContextConsumer` that can apply
assertions to the context. Upon completion, the context is automatically closed.

If the application context fails to start the `#run(ContextConsumer)` method is
called with a "failed" application context. Calls to the context will throw an
`IllegalStateException` and assertions that expect a running context will fail.
The `getFailure()` assertion can be used if
further checks are required on the cause of the failure: 

```

@Test
public someTest() {
    this.context.withPropertyValues("spring.foo=fails").run((loaded) -> {
        assertThat(loaded).getFailure().hasCauseInstanceOf(BadPropertyException.class);
        // other assertions
    });
}
```

Since:
2.0.0
See Also:

- `ApplicationContextRunner`

- `WebApplicationContextRunner`

- `ReactiveWebApplicationContextRunner`

- `ApplicationContextAssert`

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`protected static final class `
`AbstractApplicationContextRunner.BeanRegistration<T>`

A Bean registration to be applied when the context loaded.

`protected static final class `
`AbstractApplicationContextRunner.RunnerConfiguration<C extends org.springframework.context.ConfigurableApplicationContext>`
 

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`AbstractApplicationContextRunner(Function<AbstractApplicationContextRunner.RunnerConfiguration<C>, SELF> instanceFactory,
 Supplier<C> contextFactory,
 Class<?>... additionalContextInterfaces)`

Create a new `AbstractApplicationContextRunner` instance.

`protected `
`AbstractApplicationContextRunner(AbstractApplicationContextRunner.RunnerConfiguration<C> configuration,
 Function<AbstractApplicationContextRunner.RunnerConfiguration<C>, SELF> instanceFactory)`

Create a new `AbstractApplicationContextRunner` instance.

- 

## Method Summary

Modifier and Type
Method
Description
`SELF`
`prepare(ContextConsumer<? super A> consumer)`

Prepare a new `ApplicationContext` based on the current state of this loader.

`SELF`
`run(ContextConsumer<? super A> consumer)`

Create and refresh a new `ApplicationContext` based on the current state of
this loader.

`SELF`
`with(Function<SELF,SELF> customizer)`

Apply customization to this runner.

`SELF`
`withAllowBeanDefinitionOverriding(boolean allowBeanDefinitionOverriding)`

Specify if bean definition overriding, by registering a definition with the same
name as an existing definition, should be allowed.

`SELF`
`withAllowCircularReferences(boolean allowCircularReferences)`

Specify if circular references between beans should be allowed.

`<T> SELF`
`withBean(@Nullable String name,
 Class<T> type,
 Object... constructorArgs)`

Register the specified user bean with the `ApplicationContext`.

`<T> SELF`
`withBean(@Nullable String name,
 Class<T> type,
 Supplier<T> supplier,
 org.springframework.beans.factory.config.BeanDefinitionCustomizer... customizers)`

Register the specified user bean with the `ApplicationContext`.

`<T> SELF`
`withBean(Class<T> type,
 Object... constructorArgs)`

Register the specified user bean with the `ApplicationContext`.

`<T> SELF`
`withBean(Class<T> type,
 Supplier<T> supplier,
 org.springframework.beans.factory.config.BeanDefinitionCustomizer... customizers)`

Register the specified user bean with the `ApplicationContext`.

`SELF`
`withClassLoader(@Nullable ClassLoader classLoader)`

Customize the `ClassLoader` that the `ApplicationContext` should use
for resource loading and bean class loading.

`SELF`
`withConfiguration(org.springframework.boot.context.annotation.Configurations configurations)`

Register the specified configuration classes with the `ApplicationContext`.

`SELF`
`withInitializer(org.springframework.context.ApplicationContextInitializer<? super C> initializer)`

Add an `ApplicationContextInitializer` to be called when the context is
created.

`SELF`
`withParent(org.springframework.context.ApplicationContext parent)`

Configure the `parent` of the `ApplicationContext`.

`SELF`
`withPropertyValues(String... pairs)`

Add the specified `Environment` property pairs.

`SELF`
`withSystemProperties(String... pairs)`

Add the specified `System` property pairs.

`SELF`
`withUserConfiguration(Class<?>... configurationClasses)`

Register the specified user configuration classes with the
`ApplicationContext`.

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### AbstractApplicationContextRunner

protected AbstractApplicationContextRunner(Function<AbstractApplicationContextRunner.RunnerConfiguration<C>, SELF> instanceFactory,
 Supplier<C> contextFactory,
 Class<?>... additionalContextInterfaces)
Create a new `AbstractApplicationContextRunner` instance.

Parameters:
`instanceFactory` - the factory used to create new instance of the runner
`contextFactory` - the factory used to create the actual context
`additionalContextInterfaces` - any additional application context interfaces to
be added to the application context proxy
Since:
3.4.0

  - 

### AbstractApplicationContextRunner

protected AbstractApplicationContextRunner(AbstractApplicationContextRunner.RunnerConfiguration<C> configuration,
 Function<AbstractApplicationContextRunner.RunnerConfiguration<C>, SELF> instanceFactory)
Create a new `AbstractApplicationContextRunner` instance.

Parameters:
`configuration` - the configuration for the runner to use
`instanceFactory` - the factory used to create new instance of the runner
Since:
2.6.0

- 

## Method Details

  - 

### withAllowBeanDefinitionOverriding

public SELF withAllowBeanDefinitionOverriding(boolean allowBeanDefinitionOverriding)
Specify if bean definition overriding, by registering a definition with the same
name as an existing definition, should be allowed.

Parameters:
`allowBeanDefinitionOverriding` - if bean overriding is allowed
Returns:
a new instance with the updated bean definition overriding policy
Since:
2.3.0
See Also:

    - `DefaultListableBeanFactory.setAllowBeanDefinitionOverriding(boolean)`

  - 

### withAllowCircularReferences

public SELF withAllowCircularReferences(boolean allowCircularReferences)
Specify if circular references between beans should be allowed.

Parameters:
`allowCircularReferences` - if circular references between beans are allowed
Returns:
a new instance with the updated circular references policy
Since:
2.6.0
See Also:

    - `AbstractAutowireCapableBeanFactory.setAllowCircularReferences(boolean)`

  - 

### withInitializer

public SELF withInitializer(org.springframework.context.ApplicationContextInitializer<? super C> initializer)
Add an `ApplicationContextInitializer` to be called when the context is
created.

Parameters:
`initializer` - the initializer to add
Returns:
a new instance with the updated initializers

  - 

### withPropertyValues

public SELF withPropertyValues(String... pairs)
Add the specified `Environment` property pairs. Key-value pairs can be
specified with colon (":") or equals ("=") separators. Override matching keys that
might have been specified previously.

Parameters:
`pairs` - the key-value pairs for properties that need to be added to the
environment
Returns:
a new instance with the updated property values
See Also:

    - `TestPropertyValues`

    - `withSystemProperties(String...)`

  - 

### withSystemProperties

public SELF withSystemProperties(String... pairs)
Add the specified `System` property pairs. Key-value pairs can be specified
with colon (":") or equals ("=") separators. System properties are added before the
context is `run` and restored when the context is
closed.

Parameters:
`pairs` - the key-value pairs for properties that need to be added to the system
Returns:
a new instance with the updated system properties
See Also:

    - `TestPropertyValues`

    - `withSystemProperties(String...)`

  - 

### withClassLoader

public SELF withClassLoader(@Nullable ClassLoader classLoader)
Customize the `ClassLoader` that the `ApplicationContext` should use
for resource loading and bean class loading.

Parameters:
`classLoader` - the classloader to use (or `null` to use the default)
Returns:
a new instance with the updated class loader
See Also:

    - `FilteredClassLoader`

  - 

### withParent

public SELF withParent(org.springframework.context.ApplicationContext parent)
Configure the `parent` of the `ApplicationContext`.

Parameters:
`parent` - the parent
Returns:
a new instance with the updated parent

  - 

### withBean

public <T> SELF withBean(Class<T> type,
 Object... constructorArgs)
Register the specified user bean with the `ApplicationContext`. The bean name
is generated from the configured `BeanNameGenerator` on the underlying
context.

Such beans are registered after regular user configurations in the order of registration.

Type Parameters:
`T` - the type of the bean
Parameters:
`type` - the type of the bean
`constructorArgs` - custom argument values to be fed into Spring's constructor
resolution algorithm, resolving either all arguments or just specific ones, with
the rest to be resolved through regular autowiring (may be `null` or empty)
Returns:
a new instance with the updated bean

  - 

### withBean

public <T> SELF withBean(@Nullable String name,
 Class<T> type,
 Object... constructorArgs)
Register the specified user bean with the `ApplicationContext`.

Such beans are registered after regular user configurations in the order of registration.

Type Parameters:
`T` - the type of the bean
Parameters:
`name` - the bean name or `null` to use a generated name
`type` - the type of the bean
`constructorArgs` - custom argument values to be fed into Spring's constructor
resolution algorithm, resolving either all arguments or just specific ones, with
the rest to be resolved through regular autowiring (may be `null` or empty)
Returns:
a new instance with the updated bean

  - 

### withBean

public <T> SELF withBean(Class<T> type,
 Supplier<T> supplier,
 org.springframework.beans.factory.config.BeanDefinitionCustomizer... customizers)
Register the specified user bean with the `ApplicationContext`. The bean name
is generated from the configured `BeanNameGenerator` on the underlying
context.

Such beans are registered after regular user configurations in the order of registration.

Type Parameters:
`T` - the type of the bean
Parameters:
`type` - the type of the bean
`supplier` - a supplier for the bean
`customizers` - one or more callbacks for customizing the factory's
`BeanDefinition`, e.g. setting a lazy-init or primary flag
Returns:
a new instance with the updated bean

  - 

### withBean

public <T> SELF withBean(@Nullable String name,
 Class<T> type,
 Supplier<T> supplier,
 org.springframework.beans.factory.config.BeanDefinitionCustomizer... customizers)
Register the specified user bean with the `ApplicationContext`. The bean name
is generated from the configured `BeanNameGenerator` on the underlying
context.

Such beans are registered after regular user configurations in the order of registration.

Type Parameters:
`T` - the type of the bean
Parameters:
`name` - the bean name or `null` to use a generated name
`type` - the type of the bean
`supplier` - a supplier for the bean
`customizers` - one or more callbacks for customizing the factory's
`BeanDefinition`, e.g. setting a lazy-init or primary flag
Returns:
a new instance with the updated bean

  - 

### withUserConfiguration

public SELF withUserConfiguration(Class<?>... configurationClasses)
Register the specified user configuration classes with the
`ApplicationContext`.

Parameters:
`configurationClasses` - the user configuration classes to add
Returns:
a new instance with the updated configuration

  - 

### withConfiguration

public SELF withConfiguration(org.springframework.boot.context.annotation.Configurations configurations)
Register the specified configuration classes with the `ApplicationContext`.

Parameters:
`configurations` - the configurations to add
Returns:
a new instance with the updated configuration

  - 

### with

public SELF with(Function<SELF,SELF> customizer)
Apply customization to this runner.

Parameters:
`customizer` - the customizer to call
Returns:
a new instance with the customizations applied

  - 

### run

public SELF run(ContextConsumer<? super A> consumer)
Create and refresh a new `ApplicationContext` based on the current state of
this loader. The context is consumed by the specified `consumer` and closed
upon completion.

Parameters:
`consumer` - the consumer of the created `ApplicationContext`
Returns:
this instance

  - 

### prepare

public SELF prepare(ContextConsumer<? super A> consumer)
Prepare a new `ApplicationContext` based on the current state of this loader.
The context is consumed by the specified `consumer` and closed upon
completion. Unlike `run(ContextConsumer)`, this method does not refresh the
consumed context.

Parameters:
`consumer` - the consumer of the created `ApplicationContext`
Returns:
this instance
Since:
3.0.0