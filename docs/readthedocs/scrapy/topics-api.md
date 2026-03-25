# Core API

This section documents the Scrapy core API, and it’s intended for developers of
extensions and middlewares.

## Crawler API

The main entry point to the Scrapy API is the `Crawler`
object, which components can get for
initialization. It provides access to all Scrapy core
components, and it is the only way for components to access them and hook their
functionality into Scrapy.

The Extension Manager is responsible for loading and keeping track of installed
extensions and it’s configured through the `EXTENSIONS` setting which
contains a dictionary of all available extensions and their order similar to
how you configure the downloader middlewares.

*class *scrapy.crawler.Crawler(*spidercls: type [https://docs.python.org/3/library/functions.html#type][Spider]*, *settings: dict [https://docs.python.org/3/library/stdtypes.html#dict][str [https://docs.python.org/3/library/stdtypes.html#str], Any [https://docs.python.org/3/library/typing.html#typing.Any]] | Settings | None [https://docs.python.org/3/library/constants.html#None] = None*, *init_reactor: bool [https://docs.python.org/3/library/functions.html#bool] = False*)

The Crawler object must be instantiated with a
`scrapy.Spider` subclass and a
`scrapy.settings.Settings` object.

request_fingerprinter

The request fingerprint builder of this crawler.

This is used from extensions and middlewares to build short, unique
identifiers for requests. See Request fingerprints.

settings

The settings manager of this crawler.

This is used by extensions & middlewares to access the Scrapy settings
of this crawler.

For an introduction on Scrapy settings see Settings.

For the API see `Settings` class.

signals

The signals manager of this crawler.

This is used by extensions & middlewares to hook themselves into Scrapy
functionality.

For an introduction on signals see Signals.

For the API see `SignalManager` class.

stats

The stats collector of this crawler.

This is used from extensions & middlewares to record stats of their
behaviour, or access stats collected by other extensions.

For an introduction on stats collection see Stats Collection.

For the API see `StatsCollector` class.

extensions

The extension manager that keeps track of enabled extensions.

Most extensions won’t need to access this attribute.

For an introduction on extensions and a list of available extensions on
Scrapy see Extensions.

engine

The execution engine, which coordinates the core crawling logic
between the scheduler, downloader and spiders.

Some extension may want to access the Scrapy engine, to inspect  or
modify the downloader and scheduler behaviour, although this is an
advanced use and this API is not yet stable.

spider

Spider currently being crawled. This is an instance of the spider class
provided while constructing the crawler, and it is created after the
arguments given in the `crawl()` method.

*async *crawl_async(**args: Any [https://docs.python.org/3/library/typing.html#typing.Any]*, ***kwargs: Any [https://docs.python.org/3/library/typing.html#typing.Any]*) → None [https://docs.python.org/3/library/constants.html#None]

Start the crawler by instantiating its spider class with the given
*args* and *kwargs* arguments, while setting the execution engine in
motion. Should be called only once.

Added in version 2.14.