# Common Practices

This section documents common practices when using Scrapy. These are things
that cover many topics and don’t often fall into any other specific section.

## Run Scrapy from a script

You can use the API to run Scrapy from a script, instead of
the typical way of running Scrapy via `scrapy crawl`.

Remember that Scrapy is built on top of the Twisted
asynchronous networking library, so you need to run it inside the Twisted reactor.

The first utility you can use to run your spiders is
`scrapy.crawler.AsyncCrawlerProcess` or
`scrapy.crawler.CrawlerProcess`. These classes will start a Twisted
reactor for you, configuring the logging and setting shutdown handlers. These
classes are the ones used by all Scrapy commands. They have similar
functionality, differing in their asynchronous API style:
`AsyncCrawlerProcess` returns coroutines from its
asynchronous methods while `CrawlerProcess` returns
`Deferred` [https://docs.twisted.org/en/stable/api/twisted.internet.defer.Deferred.html] objects.

Here’s an example showing how to run a single spider with it.

```
import scrapy
from scrapy.crawler import AsyncCrawlerProcess

class MySpider(scrapy.Spider):
    # Your spider definition
    ...

process = AsyncCrawlerProcess(
    settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
    }
)

process.crawl(MySpider)
process.start()  # the script will block here until the crawling is finished

```