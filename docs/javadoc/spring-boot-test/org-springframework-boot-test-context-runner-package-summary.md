# Package org.springframework.boot.test.context.runner

---

@NullMarked
package org.springframework.boot.test.context.runner

Test utilities to run application contexts for testing.

- 

Related Packages

Package
Description
org.springframework.boot.test.context

Support for mapping annotation attribute values in the Spring `Environment`.

org.springframework.boot.test.context.assertj

AssertJ support for ApplicationContexts.

- 

Class
Description
AbstractApplicationContextRunner<SELF extends AbstractApplicationContextRunner<SELF,C,A>, C extends org.springframework.context.ConfigurableApplicationContext, A extends ApplicationContextAssertProvider<C>>

Utility design to run an `ApplicationContext` and provide AssertJ style
assertions.

AbstractApplicationContextRunner.BeanRegistration<T>

A Bean registration to be applied when the context loaded.

AbstractApplicationContextRunner.RunnerConfiguration<C extends org.springframework.context.ConfigurableApplicationContext>
 
ApplicationContextRunner

An `ApplicationContext runner` for a standard,
non-web environment `ConfigurableApplicationContext`.

ContextConsumer<C extends org.springframework.context.ApplicationContext>

Callback interface used to process an `ApplicationContext` with the ability to
throw a (checked) exception.

ReactiveWebApplicationContextRunner

An `ApplicationContext runner` for a
`ConfigurableReactiveWebApplicationContext`.

WebApplicationContextRunner

An `ApplicationContext runner` for a Servlet
based `ConfigurableWebApplicationContext`.