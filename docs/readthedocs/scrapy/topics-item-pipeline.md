# Item Pipeline

After an item has been scraped by a spider, it is sent to the Item Pipeline
which processes it through several components that are executed sequentially.

Each item pipeline component (sometimes referred as just “Item Pipeline”) is a
Python class that implements a simple method. They receive an item and perform
an action over it, also deciding if the item should continue through the
pipeline or be dropped and no longer processed.

Typical uses of item pipelines are:

- 

cleansing HTML data

- 

validating scraped data (checking that the items contain certain fields)

- 

checking for duplicates (and dropping them)

- 

storing the scraped item in a database

## Writing your own item pipeline

Each item pipeline is a component that must
implement the following method:

process_item(*self*, *item*)

This method is called for every item pipeline component.

item is an item object, see
Supporting All Item Types.

`process_item()` must either return an item object
or raise a `DropItem` exception.

Dropped items are no longer processed by further pipeline components.

Parameters:

**item** (item object) – the scraped item

Additionally, they may also implement the following methods:

open_spider(*self*)

This method is called when the spider is opened.

close_spider(*self*)

This method is called when the spider is closed.

Any of these methods may be defined as a coroutine function (`async def`).

## Item pipeline example

### Price validation and dropping items with no prices

Let’s take a look at the following hypothetical pipeline that adjusts the
`price` attribute for those items that do not include VAT
(`price_excludes_vat` attribute), and drops those items which don’t
contain a price:

```
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class PricePipeline:
    vat_factor = 1.15

    def process_item(self, item):
        adapter = ItemAdapter(item)
        if adapter.get("price"):
            if adapter.get("price_excludes_vat"):
                adapter["price"] = adapter["price"] * self.vat_factor
            return item
        else:
            raise DropItem("Missing price")

```