# Interface AssertableWebApplicationContext

All Superinterfaces:
`org.springframework.context.ApplicationContext, ApplicationContextAssertProvider<org.springframework.web.context.ConfigurableWebApplicationContext>, org.springframework.context.ApplicationEventPublisher, org.assertj.core.api.AssertProvider<ApplicationContextAssert<org.springframework.web.context.ConfigurableWebApplicationContext>>, AutoCloseable, org.springframework.beans.factory.BeanFactory, Closeable, org.springframework.context.ConfigurableApplicationContext, org.springframework.web.context.ConfigurableWebApplicationContext, org.springframework.core.env.EnvironmentCapable, org.springframework.beans.factory.HierarchicalBeanFactory, org.springframework.context.Lifecycle, org.springframework.beans.factory.ListableBeanFactory, org.springframework.context.MessageSource, org.springframework.core.io.ResourceLoader, org.springframework.core.io.support.ResourcePatternResolver, org.springframework.web.context.WebApplicationContext`

---

public interface AssertableWebApplicationContext
extends ApplicationContextAssertProvider<org.springframework.web.context.ConfigurableWebApplicationContext>, org.springframework.web.context.ConfigurableWebApplicationContext
A `WebApplicationContext` that additionally supports AssertJ style assertions.
Can be used to decorate an existing servlet web application context or an application
context that failed to start.

See `ApplicationContextAssertProvider` for more details.

Since:
2.0.0
See Also:

- `WebApplicationContextRunner`

- `WebApplicationContext`

- 

## Field Summary

### Fields inherited from interface org.springframework.beans.factory.BeanFactory

`FACTORY_BEAN_PREFIX, FACTORY_BEAN_PREFIX_CHAR`

### Fields inherited from interface org.springframework.context.ConfigurableApplicationContext

`APPLICATION_STARTUP_BEAN_NAME, BOOTSTRAP_EXECUTOR_BEAN_NAME, CONFIG_LOCATION_DELIMITERS, CONVERSION_SERVICE_BEAN_NAME, ENVIRONMENT_BEAN_NAME, LOAD_TIME_WEAVER_BEAN_NAME, SHUTDOWN_HOOK_THREAD_NAME, SYSTEM_ENVIRONMENT_BEAN_NAME, SYSTEM_PROPERTIES_BEAN_NAME`

### Fields inherited from interface org.springframework.web.context.ConfigurableWebApplicationContext

`APPLICATION_CONTEXT_ID_PREFIX, SERVLET_CONFIG_BEAN_NAME`

### Fields inherited from interface org.springframework.core.io.ResourceLoader

`CLASSPATH_URL_PREFIX`

### Fields inherited from interface org.springframework.core.io.support.ResourcePatternResolver

`CLASSPATH_ALL_URL_PREFIX`

### Fields inherited from interface org.springframework.web.context.WebApplicationContext

`CONTEXT_ATTRIBUTES_BEAN_NAME, CONTEXT_PARAMETERS_BEAN_NAME, ROOT_WEB_APPLICATION_CONTEXT_ATTRIBUTE, SCOPE_APPLICATION, SCOPE_REQUEST, SCOPE_SESSION, SERVLET_CONTEXT_BEAN_NAME`

- 

## Method Summary

Static Methods

Modifier and Type
Method
Description
`static AssertableWebApplicationContext`
`get(Supplier<? extends org.springframework.web.context.ConfigurableWebApplicationContext> contextSupplier)`

Factory method to create a new `AssertableWebApplicationContext` instance.

`static AssertableWebApplicationContext`
`get(Supplier<? extends org.springframework.web.context.ConfigurableWebApplicationContext> contextSupplier,
 Class<?>... additionalContextInterfaces)`

Factory method to create a new `AssertableWebApplicationContext` instance.

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

### Methods inherited from interface org.springframework.web.context.ConfigurableWebApplicationContext

`getConfigLocations, getNamespace, getServletConfig, setConfigLocation, setConfigLocations, setNamespace, setServletConfig, setServletContext`

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

### Methods inherited from interface org.springframework.web.context.WebApplicationContext

`getServletContext`

- 

## Method Details

  - 

### get

static AssertableWebApplicationContext get(Supplier<? extends org.springframework.web.context.ConfigurableWebApplicationContext> contextSupplier)
Factory method to create a new `AssertableWebApplicationContext` instance.

Parameters:
`contextSupplier` - a supplier that will either return a fully configured
`ConfigurableWebApplicationContext` or throw an exception if the context
fails to start.
Returns:
a `AssertableWebApplicationContext` instance

  - 

### get

static AssertableWebApplicationContext get(Supplier<? extends org.springframework.web.context.ConfigurableWebApplicationContext> contextSupplier,
 Class<?>... additionalContextInterfaces)
Factory method to create a new `AssertableWebApplicationContext` instance.

Parameters:
`contextSupplier` - a supplier that will either return a fully configured
`ConfigurableWebApplicationContext` or throw an exception if the context
fails to start.
`additionalContextInterfaces` - and additional context interfaces to add to the
proxy
Returns:
a `AssertableWebApplicationContext` instance
Since:
3.4.0