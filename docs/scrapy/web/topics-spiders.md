# Spiders

Spiders are classes which define how a certain site (or a group of sites) will be
scraped, including how to perform the crawl (i.e. follow links) and how to
extract structured data from their pages (i.e. scraping items). In other words,
Spiders are the place where you define the custom behaviour for crawling and
parsing pages for a particular site (or, in some cases, a group of sites).

For spiders, the scraping cycle goes through something like this:

- 

You start by generating the initial requests to crawl the first URLs, and
specify a callback function to be called with the response downloaded from
those requests.

The first requests to perform are obtained by iterating the
`start()` method, which by default yields a
`Request` object for each URL in the
`start_urls` spider attribute, with the
`parse` method set as `callback`
function to handle each `Response`.

- 

In the callback function, you parse the response (web page) and return
item objects,
`Request` objects, or an iterable of these objects.
Those Requests will also contain a callback (maybe
the same) and will then be downloaded by Scrapy and then their
response handled by the specified callback.

- 

In callback functions, you parse the page contents, typically using
Selectors (but you can also use BeautifulSoup, lxml or whatever
mechanism you prefer) and generate items with the parsed data.

- 

Finally, the items returned from the spider will be typically persisted to a
database (in some Item Pipeline) or written to
a file using Feed exports.

Even though this cycle applies (more or less) to any kind of spider, there are
different kinds of default spiders bundled into Scrapy for different purposes.
We will talk about those types here.

## scrapy.Spider

*class *scrapy.spiders.Spider

*class *scrapy.Spider(**args: Any*, ***kwargs: Any*)

Base class that any spider must subclass.

It provides a default `start()` implementation that sends
requests based on the `start_urls` class attribute and calls the
`parse()` method for each response.

name

A string which defines the name for this spider. The spider name is how
the spider is located (and instantiated) by Scrapy, so it must be
unique. However, nothing prevents you from instantiating more than one
instance of the same spider. This is the most important spider attribute
and it’s required.

If the spider scrapes a single domain, a common practice is to name the
spider after the domain, with or without the TLD [https://en.wikipedia.org/wiki/Top-level_domain]. So, for example, a
spider that crawls `mywebsite.com` would often be called
`mywebsite`.

allowed_domains

An optional list of strings containing domains that this spider is
allowed to crawl. Requests for URLs not belonging to the domain names
specified in this list (or their subdomains) won’t be followed if
`OffsiteMiddleware` is
enabled.

Let’s say your target url is `https://www.example.com/1.html`,
then add `'example.com'` to the list.

start_urls*: list [https://docs.python.org/3/library/stdtypes.html#list][str [https://docs.python.org/3/library/stdtypes.html#str]]*

Start URLs. See `start()`.

custom_settings

A dictionary of settings that will be overridden from the project wide
configuration when running this spider. It must be defined as a class
attribute since the settings are updated before instantiation.

For a list of available built-in settings see:
Built-in settings reference.

crawler

This attribute is set by the `from_crawler()` class method after
initializing the class, and links to the
`Crawler` object to which this spider instance is
bound.

Crawlers encapsulate a lot of components in the project for their single
entry access (such as extensions, middlewares, signals managers, etc).
See Crawler API to know more about them.

settings

Configuration for running this spider. This is a
`Settings` instance, see the
Settings topic for a detailed introduction on this subject.

logger

Python logger created with the Spider’s `name`. You can use it to
send log messages through it as described on
Logging from Spiders.

state

A dict you can use to persist some spider state between batches.
See Keeping persistent state between batches to know more about it.

from_crawler(*crawler*, **args*, ***kwargs*)

This is the class method used by Scrapy to create your spiders.

You probably won’t need to override this directly because the default
implementation acts as a proxy to the `__init__()` method, calling
it with the given arguments `args` and named arguments `kwargs`.

Nonetheless, this method sets the `crawler` and `settings`
attributes in the new instance so they can be accessed later inside the
spider’s code.

Changed in version 2.11: The settings in `crawler.settings` can now be modified in this
method, which is handy if you want to modify them based on
arguments. As a consequence, these settings aren’t the final values
as they can be modified later by e.g. add-ons. For the same reason, most of the
`Crawler` attributes aren’t initialized at
this point.

The final settings and the initialized
`Crawler` attributes are available in the
`start()` method, handlers of the
`engine_started` signal and later.