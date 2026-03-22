# asyncio

Scrapy has partial support for `asyncio` [https://docs.python.org/3/library/asyncio.html#module-asyncio]. After you install the
asyncio reactor, you may use `asyncio` [https://docs.python.org/3/library/asyncio.html#module-asyncio] and
`asyncio` [https://docs.python.org/3/library/asyncio.html#module-asyncio]-powered libraries in any coroutine.

## Installing the asyncio reactor

To enable `asyncio` [https://docs.python.org/3/library/asyncio.html#module-asyncio] support, your `TWISTED_REACTOR` setting needs
to be set to `'twisted.internet.asyncioreactor.AsyncioSelectorReactor'`,
which is the default value.

If you are using `AsyncCrawlerRunner` or
`CrawlerRunner`, you also need to
install the `AsyncioSelectorReactor` [https://docs.twisted.org/en/stable/api/twisted.internet.asyncioreactor.AsyncioSelectorReactor.html]
reactor manually. You can do that using
`install_reactor()`:

```
install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")

```