# Broad Crawls

Scrapy defaults are optimized for crawling specific sites. These sites are
often handled by a single Scrapy spider, although this is not necessary or
required (for example, there are generic spiders that handle any given site
thrown at them).

In addition to this “focused crawl”, there is another common type of crawling
which covers a large (potentially unlimited) number of domains, and is only
limited by time or other arbitrary constraint, rather than stopping when the
domain was crawled to completion or when there are no more requests to perform.
These are called “broad crawls” and is the typical crawlers employed by search
engines.

These are some common properties often found in broad crawls:

- 

they crawl many domains (often, unbounded) instead of a specific set of sites

- 

they don’t necessarily crawl domains to completion, because it would be
impractical (or impossible) to do so, and instead limit the crawl by time or
number of pages crawled

- 

they are simpler in logic (as opposed to very complex spiders with many
extraction rules) because data is often post-processed in a separate stage

- 

they crawl many domains concurrently, which allows them to achieve faster
crawl speeds by not being limited by any particular site constraint (each site
is crawled slowly to respect politeness, but many sites are crawled in
parallel)

As said above, Scrapy default settings are optimized for focused crawls, not
broad crawls. However, due to its asynchronous architecture, Scrapy is very
well suited for performing fast broad crawls. This page summarizes some things
you need to keep in mind when using Scrapy for doing broad crawls, along with
concrete suggestions of Scrapy settings to tune in order to achieve an
efficient broad crawl.

## Increase concurrency

Concurrency is the number of requests that are processed in parallel. There is
a global limit (`CONCURRENT_REQUESTS`) and an additional limit that
can be set per domain (`CONCURRENT_REQUESTS_PER_DOMAIN`).

The default global concurrency limit in Scrapy is not suitable for crawling
many different domains in parallel, so you will want to increase it. How much
to increase it will depend on how much CPU and memory your crawler will have
available.

A good starting point is `100`:

```
CONCURRENT_REQUESTS = 100

```