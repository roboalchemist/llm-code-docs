# Interface AssertableApplicationContext

All Superinterfaces:
`org.springframework.context.ApplicationContext, ApplicationContextAssertProvider<org.springframework.context.ConfigurableApplicationContext>, org.springframework.context.ApplicationEventPublisher, org.assertj.core.api.AssertProvider<ApplicationContextAssert<org.springframework.context.ConfigurableApplicationContext>>, AutoCloseable, org.springframework.beans.factory.BeanFactory, Closeable, org.springframework.context.ConfigurableApplicationContext, org.springframework.core.env.EnvironmentCapable, org.springframework.beans.factory.HierarchicalBeanFactory, org.springframework.context.Lifecycle, org.springframework.beans.factory.ListableBeanFactory, org.springframework.context.MessageSource, org.springframework.core.io.ResourceLoader, org.springframework.core.io.support.ResourcePatternResolver`

---

public interface AssertableApplicationContext
extends ApplicationContextAssertProvider<org.springframework.context.ConfigurableApplicationContext>, org.springframework.context.ConfigurableApplicationContext
An `ApplicationContext` that additionally supports AssertJ style assertions. Can
be used to decorate an existing application context or an application context that
failed to start.

See `ApplicationContextAssertProvider` for more details.

Since:
2.0.0
See Also:

- `ApplicationContextRunner`

- `ApplicationContext`

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
`static AssertableApplicationContext`
`get(Supplier<? extends org.springframework.context.ConfigurableApplicationContext> contextSupplier)`

Factory method to create a new `AssertableApplicationContext` instance.

`static AssertableApplicationContext`
`get(Supplier<? extends org.springframework.context.ConfigurableApplicationContext> contextSupplier,
 Class<?>... additionalContextInterfaces)`

Factory method to create a new `AssertableApplicationContext` instance.

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

static AssertableApplicationContext get(Supplier<? extends org.springframework.context.ConfigurableApplicationContext> contextSupplier)
Factory method to create a new `AssertableApplicationContext` instance.

Parameters:
`contextSupplier` - a supplier that will either return a fully configured
`ConfigurableApplicationContext` or throw an exception if the context fails
to start.
Returns:
an `AssertableApplicationContext` instance

  - 

### get

static AssertableApplicationContext get(Supplier<? extends org.springframework.context.ConfigurableApplicationContext> contextSupplier,
 Class<?>... additionalContextInterfaces)
Factory method to create a new `AssertableApplicationContext` instance.

Parameters:
`contextSupplier` - a supplier that will either return a fully configured
`ConfigurableApplicationContext` or throw an exception if the context fails
to start.
`additionalContextInterfaces` - and additional context interfaces to add to the
proxy
Returns:
an `AssertableApplicationContext` instance
Since:
3.4.0