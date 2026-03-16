# Interface AssertableReactiveWebApplicationContext

All Superinterfaces:
`org.springframework.context.ApplicationContext, ApplicationContextAssertProvider<org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext>, org.springframework.context.ApplicationEventPublisher, org.assertj.core.api.AssertProvider<ApplicationContextAssert<org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext>>, AutoCloseable, org.springframework.beans.factory.BeanFactory, Closeable, org.springframework.context.ConfigurableApplicationContext, org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext, org.springframework.core.env.EnvironmentCapable, org.springframework.beans.factory.HierarchicalBeanFactory, org.springframework.context.Lifecycle, org.springframework.beans.factory.ListableBeanFactory, org.springframework.context.MessageSource, org.springframework.boot.web.context.reactive.ReactiveWebApplicationContext, org.springframework.core.io.ResourceLoader, org.springframework.core.io.support.ResourcePatternResolver`

---

public interface AssertableReactiveWebApplicationContext
extends ApplicationContextAssertProvider<org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext>, org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext
A `ReactiveWebApplicationContext` that additionally supports AssertJ style
assertions. Can be used to decorate an existing reactive web application context or an
application context that failed to start.

See `ApplicationContextAssertProvider` for more details.

Since:
2.0.0
See Also:

- `ReactiveWebApplicationContext`

- `ReactiveWebApplicationContext`

- 

## Field Summary

### Fields inherited from interface org.springframework.beans.factory.BeanFactory

`FACTORY_BEAN_PREFIX, FACTORY_BEAN_PREFIX_CHAR`

### Fields inherited from interface org.springframework.context.ConfigurableApplicationContext

`APPLICATION_STARTUP_BEAN_NAME, BOOTSTRAP_EXECUTOR_BEAN_NAME, CONFIG_LOCATION_DELIMITERS, CONVERSION_SERVICE_BEAN_NAME, ENVIRONMENT_BEAN_NAME, LOAD_TIME_WEAVER_BEAN_NAME, SHUTDOWN_HOOK_THREAD_NAME, SYSTEM_ENVIRONMENT_BEAN_NAME, SYSTEM_PROPERTIES_BEAN_NAME`

### Fields inherited from interface org.springframework.core.io.ResourceLoader

`CLASSPATH_URL_PREFIX`

### Fields inherited from interface org.springframework.core.io.support.ResourcePatternResolver

`CLASSPATH_ALL_URL_PREFIX`

- 

## Method Summary

Static Methods

Modifier and Type
Method
Description
`static AssertableReactiveWebApplicationContext`
`get(Supplier<? extends org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext> contextSupplier)`

Factory method to create a new `AssertableReactiveWebApplicationContext`
instance.

`static AssertableReactiveWebApplicationContext`
`get(Supplier<? extends org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext> contextSupplier,
 Class<?>... additionalContextInterfaces)`

Factory method to create a new `AssertableReactiveWebApplicationContext`
instance.

### Methods inherited from interface org.springframework.context.ApplicationContext

`getApplicationName, getAutowireCapableBeanFactory, getDisplayName, getId, getParent, getStartupDate`

### Methods inherited from interface ApplicationContextAssertProvider

`assertThat, close, getSourceApplicationContext, getSourceApplicationContext, getStartupFailure`

### Methods inherited from interface org.springframework.context.ApplicationEventPublisher

`publishEvent, publishEvent`

### Methods inherited from interface org.springframework.beans.factory.BeanFactory

`containsBean, getAliases, getBean, getBean, getBean, getBean, getBean, getBeanProvider, getBeanProvider, getBeanProvider, getType, getType, isPrototype, isSingleton, isTypeMatch, isTypeMatch`

### Methods inherited from interface org.springframework.context.ConfigurableApplicationContext

`addApplicationListener, addBeanFactoryPostProcessor, addProtocolResolver, close, getApplicationStartup, getBeanFactory, getEnvironment, isActive, isClosed, pause, refresh, registerShutdownHook, removeApplicationListener, restart, setApplicationStartup, setClassLoader, setEnvironment, setId, setParent`

### Methods inherited from interface org.springframework.beans.factory.HierarchicalBeanFactory

`containsLocalBean, getParentBeanFactory`

### Methods inherited from interface org.springframework.context.Lifecycle

`isRunning, start, stop`

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

### get

static AssertableReactiveWebApplicationContext get(Supplier<? extends org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext> contextSupplier)
Factory method to create a new `AssertableReactiveWebApplicationContext`
instance.

Parameters:
`contextSupplier` - a supplier that will either return a fully configured
`ConfigurableReactiveWebApplicationContext` or throw an exception if the
context fails to start.
Returns:
a `AssertableReactiveWebApplicationContext` instance

  - 

### get

static AssertableReactiveWebApplicationContext get(Supplier<? extends org.springframework.boot.web.context.reactive.ConfigurableReactiveWebApplicationContext> contextSupplier,
 Class<?>... additionalContextInterfaces)
Factory method to create a new `AssertableReactiveWebApplicationContext`
instance.

Parameters:
`contextSupplier` - a supplier that will either return a fully configured
`ConfigurableReactiveWebApplicationContext` or throw an exception if the
context fails to start.
`additionalContextInterfaces` - and additional context interfaces to add to the
proxy
Returns:
a `AssertableReactiveWebApplicationContext` instance
Since:
3.4.0