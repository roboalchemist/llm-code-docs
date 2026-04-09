# Class AbstractApplicationContextRunner.BeanRegistration<T>

java.lang.Object
org.springframework.boot.test.context.runner.AbstractApplicationContextRunner.BeanRegistration<T>

Type Parameters:
`T` - the bean type

Enclosing class:
`AbstractApplicationContextRunner<SELF extends AbstractApplicationContextRunner<SELF,C,A>, C extends org.springframework.context.ConfigurableApplicationContext, A extends ApplicationContextAssertProvider<C>>`

---

protected static final class AbstractApplicationContextRunner.BeanRegistration<T>
extends Object
A Bean registration to be applied when the context loaded.

Since:
2.0.0

- 

## Constructor Summary

Constructors

Constructor
Description
`BeanRegistration(@Nullable String name,
 Class<T> type,
 Object... constructorArgs)`
 
`BeanRegistration(@Nullable String name,
 Class<T> type,
 Supplier<T> supplier,
 org.springframework.beans.factory.config.BeanDefinitionCustomizer... customizers)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`apply(org.springframework.context.ConfigurableApplicationContext context)`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### BeanRegistration

public BeanRegistration(@Nullable String name,
 Class<T> type,
 Object... constructorArgs)

  - 

### BeanRegistration

public BeanRegistration(@Nullable String name,
 Class<T> type,
 Supplier<T> supplier,
 org.springframework.beans.factory.config.BeanDefinitionCustomizer... customizers)

- 

## Method Details

  - 

### apply

public void apply(org.springframework.context.ConfigurableApplicationContext context)