# Exceptions

## Built-in Exceptions reference

Here’s a list of all exceptions included in Scrapy and their usage.

### CloseSpider

*exception *scrapy.exceptions.CloseSpider(*reason='cancelled'*)

This exception can be raised from a spider callback to request the spider to be
closed/stopped. Supported arguments:

Parameters:

**reason** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – the reason for closing

For example:

```
def parse_page(self, response):
    if "Bandwidth exceeded" in response.body:
        raise CloseSpider("bandwidth_exceeded")

```