# Interface ApplicationContextAssertProvider<C extends org.springframework.context.ApplicationContext>

Type Parameters:
`C` - the application context type

All Superinterfaces:
`org.springframework.context.ApplicationContext, org.springframework.context.ApplicationEventPublisher, org.assertj.core.api.AssertProvider<ApplicationContextAssert<C>>, AutoCloseable, org.springframework.beans.factory.BeanFactory, Closeable, org.springframework.core.env.EnvironmentCapable, org.springframework.beans.factory.HierarchicalBeanFactory, org.springframework.beans.factory.ListableBeanFactory, org.springframework.context.MessageSource, org.springframework.core.io.ResourceLoader, org.springframework.core.io.support.ResourcePatternResolver`

All Known Subinterfaces:
`AssertableApplicationContext, AssertableReactiveWebApplicationContext, AssertableWebApplicationContext`

---

public interface ApplicationContextAssertProvider<C extends org.springframework.context.ApplicationContext>
extends org.springframework.context.ApplicationContext, org.assertj.core.api.AssertProvider<ApplicationContextAssert<C>>, Closeable
An `ApplicationContext` that additionally supports AssertJ style assertions. Can
be used to decorate an existing application context or an application context that
failed to start.

Assertions can be applied using the standard AssertJ `assertThat(...)` style (see
`ApplicationContextAssert` for a complete list). For example: 

```

assertThat(applicationContext).hasSingleBean(MyBean.class);

```

If the original `ApplicationContext` is needed for any reason the
`getSourceApplicationContext()` method can be used.

Any `ApplicationContext` method called on a context that has failed to start will
throw an `IllegalStateException`.

Since:
2.0.0
See Also:

- `AssertableApplicationContext`

- `AssertableWebApplicationContext`

- `AssertableReactiveWebApplicationContext`

- `ApplicationContextAssert`

- 

## Field Summary

### Fields inherited from interface org.springframework.beans.factory.BeanFactory

`FACTORY_BEAN_PREFIX, FACTORY_BEAN_PREFIX_CHAR`

### Fields inherited from interface org.springframework.core.io.ResourceLoader

`CLASSPATH_URL_PREFIX`

### Fields inherited from interface org.springframework.core.io.support.ResourcePatternResolver

`CLASSPATH_ALL_URL_PREFIX`

- 

## Method Summary

Modifier and Type
Method
Description
`ApplicationContextAssert<C>`
`assertThat()`

Deprecated.
to prevent accidental use.

`void`
`close()`
 
`static <T extends ApplicationContextAssertProvider<C>, C extends org.springframework.context.ApplicationContext>
T`
`get(Class<T> type,
 Class<? extends C> contextType,
 Supplier<? extends C> contextSupplier)`

Factory method to create a new `ApplicationContextAssertProvider` instance.

`static <T extends ApplicationContextAssertProvider<C>, C extends org.springframework.context.ApplicationContext>
T`
`get(Class<T> type,
 Class<? extends C> contextType,
 Supplier<? extends C> contextSupplier,
 Class<?>... additionalContextInterfaces)`

Factory method to create a new `ApplicationContextAssertProvider` instance.

`C`
`getSourceApplicationContext()`

Return the original source `ApplicationContext`.

`<T extends C>
T`
`getSourceApplicationContext(Class<T> requiredType)`

Return the original source `ApplicationContext`, casting it to the requested
type.

`@Nullable Throwable`
`getStartupFailure()`

Return the failure that caused application context to fail or `null` if the
context started without issue.

### Methods inherited from interface org.springframework.context.ApplicationContext

`getApplicationName, getAutowireCapableBeanFactory, getDisplayName, getId, getParent, getStartupDate`

### Methods inherited from interface org.springframework.context.ApplicationEventPublisher

`publishEvent, publishEvent`

### Methods inherited from interface org.springframework.beans.factory.BeanFactory

`containsBean, getAliases, getBean, getBean, getBean, getBean, getBean, getBeanProvider, getBeanProvider, getBeanProvider, getType, getType, isPrototype, isSingleton, isTypeMatch, isTypeMatch`

### Methods inherited from interface org.springframework.core.env.EnvironmentCapable

`getEnvironment`

### Methods inherited from interface org.springframework.beans.factory.HierarchicalBeanFactory

`containsLocalBean, getParentBeanFactory`

### Methods inherited from interface org.springframework.beans.factory.ListableBeanFactory

`containsBeanDefinition, findAllAnnotationsOnBean, findAnnotationOnBean, findAnnotationOnBean, getBeanDefinitionCount, getBeanDefinitionNames, getBeanNamesForAnnotation, getBeanNamesForType, getBeanNamesForType, getBeanNamesForType, getBeanNamesForType, getBeanProvider, getBeanProvider, getBeansOfType, getBeansOfType, getBeansWithAnnotation`

### Methods inherited from interface org.springframework.context.MessageSource

`getMessage, getMessage, getMessage`

### Methods inherited from interface org.springframework.core.io.ResourceLoader

`getClassLoader, getResource`

### Methods inherited from interface org.springframework.core.io.support.ResourcePatternResolver

`getResources`

- 

## Method Details

  - 

### assertThat

@Deprecated(since="2.0.0",
            forRemoval=false)
ApplicationContextAssert<C> assertThat()
Deprecated.
to prevent accidental use. Prefer standard AssertJ
`assertThat(context)...` calls instead.

Return an assert for AspectJ.

Specified by:
`assertThat` in interface `org.assertj.core.api.AssertProvider<C extends org.springframework.context.ApplicationContext>`
Returns:
an AspectJ assert

  - 

### getSourceApplicationContext

C getSourceApplicationContext()
Return the original source `ApplicationContext`.

Returns:
the source application context
Throws:
`IllegalStateException` - if the source context failed to start

  - 

### getSourceApplicationContext

<T extends C> T getSourceApplicationContext(Class<T> requiredType)
Return the original source `ApplicationContext`, casting it to the requested
type.

Type Parameters:
`T` - the context type
Parameters:
`requiredType` - the required context type
Returns:
the source application context
Throws:
`IllegalStateException` - if the source context failed to start

  - 

### getStartupFailure

@Nullable Throwable getStartupFailure()
Return the failure that caused application context to fail or `null` if the
context started without issue.

Returns:
the startup failure or `null`

  - 

### close

void close()

Specified by:
`close` in interface `AutoCloseable`
Specified by:
`close` in interface `Closeable`

  - 

### get

static <T extends ApplicationContextAssertProvider<C>, C extends org.springframework.context.ApplicationContext>
T get(Class<T> type,
 Class<? extends C> contextType,
 Supplier<? extends C> contextSupplier)
Factory method to create a new `ApplicationContextAssertProvider` instance.

Type Parameters:
`T` - the assert provider type
`C` - the context type
Parameters:
`type` - the type of `ApplicationContextAssertProvider` required (must be
an interface)
`contextType` - the type of `ApplicationContext` being managed (must be an
interface)
`contextSupplier` - a supplier that will either return a fully configured
`ApplicationContext` or throw an exception if the context fails to start.
Returns:
a `ApplicationContextAssertProvider` instance

  - 

### get

static <T extends ApplicationContextAssertProvider<C>, C extends org.springframework.context.ApplicationContext>
T get(Class<T> type,
 Class<? extends C> contextType,
 Supplier<? extends C> contextSupplier,
 Class<?>... additionalContextInterfaces)
Factory method to create a new `ApplicationContextAssertProvider` instance.

Type Parameters:
`T` - the assert provider type
`C` - the context type
Parameters:
`type` - the type of `ApplicationContextAssertProvider` required (must be
an interface)
`contextType` - the type of `ApplicationContext` being managed (must be an
interface)
`contextSupplier` - a supplier that will either return a fully configured
`ApplicationContext` or throw an exception if the context fails to start.
`additionalContextInterfaces` - and additional context interfaces to add to the
proxy
Returns:
a `ApplicationContextAssertProvider` instance
Since:
3.4.0