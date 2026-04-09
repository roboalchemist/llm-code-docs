# Items

The main goal in scraping is to extract structured data from unstructured
sources, typically, web pages. Spiders may return the
extracted data as items, Python objects that define key-value pairs.

Scrapy supports multiple types of items. When you create an
item, you may use whichever type of item you want. When you write code that
receives an item, your code should work for any item type.

## Item Types

Scrapy supports the following types of items, via the itemadapter [https://github.com/scrapy/itemadapter] library:
dictionaries, Item objects,
dataclass objects, and attrs objects.

### Dictionaries

As an item type, `dict` [https://docs.python.org/3/library/stdtypes.html#dict] is convenient and familiar.

### Item objects

`Item` provides a `dict` [https://docs.python.org/3/library/stdtypes.html#dict]-like API plus additional features that
make it the most feature-complete item type:

*class *scrapy.Item(**args: Any*, ***kwargs: Any*)

Base class for scraped items.

In Scrapy, an object is considered an `item` if it’s supported by the
itemadapter [https://github.com/scrapy/itemadapter] library. For example, when the output of a spider callback
is evaluated, only such objects are passed to item pipelines. `Item` is one of the classes supported by
itemadapter [https://github.com/scrapy/itemadapter] by default.

Items must declare `Field` attributes, which are processed and stored
in the `fields` attribute. This restricts the set of allowed field names
and prevents typos, raising `KeyError` when referring to undefined fields.
Additionally, fields can be used to define metadata and control the way
data is processed internally. Please refer to the documentation
about fields for additional information.

Unlike instances of `dict` [https://docs.python.org/3/library/stdtypes.html#dict], instances of `Item` may be
tracked to debug memory leaks.

copy() → Self

deepcopy() → Self

Return a `deepcopy()` [https://docs.python.org/3/library/copy.html#copy.deepcopy] of this item.

fields*: dict [https://docs.python.org/3/library/stdtypes.html#dict][str [https://docs.python.org/3/library/stdtypes.html#str], Field]** = {}*

A dictionary containing *all declared fields* for this Item, not only
those populated. The keys are the field names and the values are the
`Field` objects used in the Item declaration.

`Item` objects replicate the standard `dict` [https://docs.python.org/3/library/stdtypes.html#dict] API, including
its `__init__` method.

`Item` allows the defining of field names, so that:

- 

`KeyError` [https://docs.python.org/3/library/exceptions.html#KeyError] is raised when using undefined field names (i.e.
prevents typos going unnoticed)

- 

Item exporters can export all fields by
default even if the first scraped object does not have values for all
of them

`Item` also allows the defining of field metadata, which can be used to
customize serialization.

`trackref` tracks `Item` objects to help find memory leaks
(see Debugging memory leaks with trackref).

Example:

```
from scrapy.item import Item, Field

class CustomItem(Item):
    one_field = Field()
    another_field = Field()

```