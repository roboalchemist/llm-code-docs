# Item Exporters

Once you have scraped your items, you often want to persist or export those
items, to use the data in some other application. That is, after all, the whole
purpose of the scraping process.

For this purpose Scrapy provides a collection of Item Exporters for different
output formats, such as XML, CSV or JSON.

## Using Item Exporters

If you are in a hurry, and just want to use an Item Exporter to output scraped
data see the Feed exports. Otherwise, if you want to know how
Item Exporters work or need more custom functionality (not covered by the
default exports), continue reading below.

In order to use an Item Exporter, you  must instantiate it with its required
args. Each Item Exporter requires different arguments, so check each exporter
documentation to be sure, in Built-in Item Exporters reference. After you have
instantiated your exporter, you have to:

1. call the method `start_exporting()` in order to
signal the beginning of the exporting process

2. call the `export_item()` method for each item you want
to export

3. and finally call the `finish_exporting()` to signal
the end of the exporting process

Here you can see an Item Pipeline which uses multiple
Item Exporters to group scraped items to different files according to the
value of one of their fields:

```
from itemadapter import ItemAdapter
from scrapy.exporters import XmlItemExporter

class PerYearXmlExportPipeline:
    """Distribute items across multiple XML files according to their 'year' field"""

    def open_spider(self, spider):
        self.year_to_exporter = {}

    def close_spider(self, spider):
        for exporter, xml_file in self.year_to_exporter.values():
            exporter.finish_exporting()
            xml_file.close()

    def _exporter_for_item(self, item):
        adapter = ItemAdapter(item)
        year = adapter["year"]
        if year not in self.year_to_exporter:
            xml_file = open(f"{year}.xml", "wb")
            exporter = XmlItemExporter(xml_file)
            exporter.start_exporting()
            self.year_to_exporter[year] = (exporter, xml_file)
        return self.year_to_exporter[year][0]

    def process_item(self, item):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item

```