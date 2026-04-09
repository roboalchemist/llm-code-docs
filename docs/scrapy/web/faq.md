# Frequently Asked Questions

## How does Scrapy compare to BeautifulSoup or lxml?

BeautifulSoup [https://www.crummy.com/software/BeautifulSoup/] and lxml [https://lxml.de/] are libraries for parsing HTML and XML. Scrapy is
an application framework for writing web spiders that crawl web sites and
extract data from them.

Scrapy provides a built-in mechanism for extracting data (called
selectors) but you can easily use BeautifulSoup [https://www.crummy.com/software/BeautifulSoup/]
(or lxml [https://lxml.de/]) instead, if you feel more comfortable working with them. After
all, they’re just parsing libraries which can be imported and used from any
Python code.

In other words, comparing BeautifulSoup [https://www.crummy.com/software/BeautifulSoup/] (or lxml [https://lxml.de/]) to Scrapy is like
comparing jinja2 [https://palletsprojects.com/projects/jinja/] to Django [https://www.djangoproject.com/].

## Can I use Scrapy with BeautifulSoup?

Yes, you can.
As mentioned above, BeautifulSoup [https://www.crummy.com/software/BeautifulSoup/] can be used
for parsing HTML responses in Scrapy callbacks.
You just have to feed the response’s body into a `BeautifulSoup` object
and extract whatever data you need from it.

Here’s an example spider using BeautifulSoup API, with `lxml` as the HTML parser:

```
from bs4 import BeautifulSoup
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = ("http://www.example.com/",)

    def parse(self, response):
        # use lxml to get decent HTML parsing speed
        soup = BeautifulSoup(response.text, "lxml")
        yield {"url": response.url, "title": soup.h1.string}

```