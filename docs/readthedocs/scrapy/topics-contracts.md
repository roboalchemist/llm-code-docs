# Spiders Contracts

Testing spiders can get particularly annoying and while nothing prevents you
from writing unit tests the task gets cumbersome quickly. Scrapy offers an
integrated way of testing your spiders by the means of contracts.

This allows you to test each callback of your spider by hardcoding a sample url
and check various constraints for how the callback processes the response. Each
contract is prefixed with an `@` and included in the docstring. See the
following example:

```
def parse(self, response):
    """
    This function parses a sample response. Some contracts are mingled
    with this docstring.

    @url http://www.example.com/s?field-keywords=selfish+gene
    @returns items 1 16
    @returns requests 0 0
    @scrapes Title Author Year Price
    """

```