# Source: https://mikro-orm.io/api/core/function/Transactional.md

# Transactional<!-- -->

### Callable

* ****Transactional**\<T>(options): MethodDecorator

***

* This decorator wraps the method with `em.transactional()`, so you can provide `TransactionOptions` just like with `em.transactional()`. The difference is that you can specify the context in which the transaction begins by providing `context` option, and if omitted, the transaction will begin in the current context implicitly. It works on async functions and can be nested with `em.transactional()`.

  ***

  #### Parameters

  * ##### options: TransactionalOptions\<T> = <!-- -->{}

  #### Returns MethodDecorator
