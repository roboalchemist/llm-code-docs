# Debugging memory leaks

In Scrapy, objects such as requests, responses and items have a finite
lifetime: they are created, used for a while, and finally destroyed.

From all those objects, the Request is probably the one with the longest
lifetime, as it stays waiting in the Scheduler queue until it’s time to process
it. For more info see Architecture overview.

As these Scrapy objects have a (rather long) lifetime, there is always the risk
of accumulating them in memory without releasing them properly and thus causing
what is known as a “memory leak”.

To help debugging memory leaks, Scrapy provides a built-in mechanism for
tracking objects references called trackref,
and you can also use a third-party library called muppy for more advanced memory debugging (see below for more
info). Both mechanisms must be used from the Telnet Console.

## Common causes of memory leaks

It happens quite often (sometimes by accident, sometimes on purpose) that the
Scrapy developer passes objects referenced in Requests (for example, using the
`cb_kwargs` or `meta`
attributes or the request callback function) and that effectively bounds the
lifetime of those referenced objects to the lifetime of the Request. This is,
by far, the most common cause of memory leaks in Scrapy projects, and a quite
difficult one to debug for newcomers.

In big projects, the spiders are typically written by different people and some
of those spiders could be “leaking” and thus affecting the rest of the other
(well-written) spiders when they get to run concurrently, which, in turn,
affects the whole crawling process.

The leak could also come from a custom middleware, pipeline or extension that
you have written, if you are not releasing the (previously allocated) resources
properly. For example, allocating resources on `spider_opened`
but not releasing them on `spider_closed` may cause problems if
you’re running multiple spiders per process.

### Too Many Requests?

By default Scrapy keeps the request queue in memory; it includes
`Request` objects and all objects
referenced in Request attributes (e.g. in `cb_kwargs`
and `meta`).
While not necessarily a leak, this can take a lot of memory. Enabling
persistent job queue could help keeping memory usage
in control.

## Debugging memory leaks with `trackref`

`trackref` is a module provided by Scrapy to debug the most common cases of
memory leaks. It basically tracks the references to all live Request,
Response, Item, Spider and Selector objects.

You can enter the telnet console and inspect how many objects (of the classes
mentioned above) are currently alive using the `prefs()` function which is an
alias to the `print_live_refs()` function:

```
telnet localhost 6023

.. code-block:: pycon

    >>> prefs()
    Live References

    ExampleSpider                       1   oldest: 15s ago
    HtmlResponse                       10   oldest: 1s ago
    Selector                            2   oldest: 0s ago
    FormRequest                       878   oldest: 7s ago

```