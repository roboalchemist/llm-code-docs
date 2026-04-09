# Coroutines

Scrapy supports the coroutine syntax [https://docs.python.org/3/reference/compound_stmts.html#async]
(i.e. `async def`).

## Supported callables

The following callables may be defined as coroutines using `async def`, and
hence use coroutine syntax (e.g. `await`, `async for`, `async with`):

- 

The `start()` spider method, which *must* be
defined as an asynchronous generator [https://docs.python.org/3/glossary.html#term-asynchronous-generator].

Added in version 2.13.