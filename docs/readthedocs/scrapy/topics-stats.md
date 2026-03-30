# Stats Collection

Scrapy provides a convenient facility for collecting stats in the form of
key/values, where values are often counters. The facility is called the Stats
Collector, and can be accessed through the `stats`
attribute of the Crawler API, as illustrated by the examples in
the Common Stats Collector uses section below.

However, the Stats Collector is always available, so you can always import it
in your module and use its API (to increment or set new stat keys), regardless
of whether the stats collection is enabled or not. If it’s disabled, the API
will still work but it won’t collect anything. This is aimed at simplifying the
stats collector usage: you should spend no more than one line of code for
collecting stats in your spider, Scrapy extension, or whatever code you’re
using the Stats Collector from.

Another feature of the Stats Collector is that it’s very efficient (when
enabled) and extremely efficient (almost unnoticeable) when disabled.

The Stats Collector keeps a stats table per open spider which is automatically
opened when the spider is opened, and closed when the spider is closed.

## Common Stats Collector uses

Access the stats collector through the `stats`
attribute. Here is an example of an extension that access stats:

```
class ExtensionThatAccessStats:
    def __init__(self, stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

```