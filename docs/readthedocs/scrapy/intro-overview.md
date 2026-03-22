# Scrapy at a glance

Scrapy (/ˈskreɪpaɪ/) is an application framework for crawling web sites and extracting
structured data which can be used for a wide range of useful applications, like
data mining, information processing or historical archival.

Even though Scrapy was originally designed for web scraping [https://en.wikipedia.org/wiki/Web_scraping], it can also be
used to extract data using APIs (such as Amazon Associates Web Services [https://affiliate-program.amazon.com/welcome/ecs]) or
as a general purpose web crawler.

## Walk-through of an example spider

In order to show you what Scrapy brings to the table, we’ll walk you through an
example of a Scrapy Spider using the simplest way to run a spider.

Here’s the code for a spider that scrapes famous quotes from website
https://quotes.toscrape.com, following the pagination:

```
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/tag/humor/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

```