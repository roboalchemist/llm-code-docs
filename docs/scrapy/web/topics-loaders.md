# Item Loaders

Item Loaders provide a convenient mechanism for populating scraped items. Even though items can be populated directly, Item Loaders provide a
much more convenient API for populating them from a scraping process, by automating
some common tasks like parsing the raw extracted data before assigning it.

In other words, items provide the *container* of
scraped data, while Item Loaders provide the mechanism for *populating* that
container.

Item Loaders are designed to provide a flexible, efficient and easy mechanism
for extending and overriding different field parsing rules, either by spider,
or by source format (HTML, XML, etc) without becoming a nightmare to maintain.

Note

Item Loaders are an extension of the itemloaders [https://itemloaders.readthedocs.io/en/latest/] library that make it
easier to work with Scrapy by adding support for
responses.