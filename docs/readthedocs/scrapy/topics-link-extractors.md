# Link Extractors

A link extractor is an object that extracts links from responses.

The `__init__` method of
`LxmlLinkExtractor` takes settings that
determine which links may be extracted. `LxmlLinkExtractor.extract_links` returns a
list of matching `Link` objects from a
`Response` object.

Link extractors are used in `CrawlSpider` spiders
through a set of `Rule` objects.

You can also use link extractors in regular spiders. For example, you can instantiate
`LinkExtractor` into a class
variable in your spider, and use it from your spider callbacks:

```
def parse(self, response):
    for link in self.link_extractor.extract_links(response):
        yield Request(link.url, callback=self.parse)

```