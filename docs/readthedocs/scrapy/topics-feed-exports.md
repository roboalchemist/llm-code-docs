# Feed exports

One of the most frequently required features when implementing scrapers is
being able to store the scraped data properly and, quite often, that means
generating an “export file” with the scraped data (commonly called “export
feed”) to be consumed by other systems.

Scrapy provides this functionality out of the box with the Feed Exports, which
allows you to generate feeds with the scraped items, using multiple
serialization formats and storage backends.

This page provides detailed documentation for all feed export features. If you
are looking for a step-by-step guide, check out Zyte’s export guides [https://docs.zyte.com/web-scraping/guides/export/index.html#exporting-scraped-data].

## Serialization formats

For serializing the scraped data, the feed exports use the Item exporters. These formats are supported out of the box:

- 

JSON

- 

JSON lines

- 

CSV

- 

XML

But you can also extend the supported format through the
`FEED_EXPORTERS` setting.

### JSON

- 

Value for the `format` key in the `FEEDS` setting: `json`

- 

Exporter used: `JsonItemExporter`

- 

See this warning if you’re using JSON with
large feeds.

### JSON lines

- 

Value for the `format` key in the `FEEDS` setting: `jsonlines`

- 

Exporter used: `JsonLinesItemExporter`

### CSV

- 

Value for the `format` key in the `FEEDS` setting: `csv`

- 

Exporter used: `CsvItemExporter`

- 

To specify columns to export, their order and their column names, use
`FEED_EXPORT_FIELDS`. Other feed exporters can also use this
option, but it is important for CSV because unlike many other export
formats CSV uses a fixed header.

### XML

- 

Value for the `format` key in the `FEEDS` setting: `xml`

- 

Exporter used: `XmlItemExporter`

### Pickle

- 

Value for the `format` key in the `FEEDS` setting: `pickle`

- 

Exporter used: `PickleItemExporter`

### Marshal

- 

Value for the `format` key in the `FEEDS` setting: `marshal`

- 

Exporter used: `MarshalItemExporter`

## Storages

When using the feed exports you define where to store the feed using one or multiple URIs [https://en.wikipedia.org/wiki/Uniform_Resource_Identifier]
(through the `FEEDS` setting). The feed exports supports multiple
storage backend types which are defined by the URI scheme.

The storages backends supported out of the box are:

- 

Local filesystem

- 

FTP

- 

S3 (requires boto3 [https://github.com/boto/boto3])

- 

Google Cloud Storage (GCS) (requires google-cloud-storage [https://cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python])

- 

Standard output

Some storage backends may be unavailable if the required external libraries are
not available. For example, the S3 backend is only available if the boto3 [https://github.com/boto/boto3]
library is installed.

## Storage URI parameters

The storage URI can also contain parameters that get replaced when the feed is
being created. These parameters are:

- 

`%(time)s` - gets replaced by a timestamp when the feed is being created

- 

`%(name)s` - gets replaced by the spider name

Any other named parameter gets replaced by the spider attribute of the same
name. For example, `%(site_id)s` would get replaced by the `spider.site_id`
attribute the moment the feed is being created.

Here are some examples to illustrate:

- 

Store in FTP using one directory per spider:

  - 

`ftp://user:password@ftp.example.com/scraping/feeds/%(name)s/%(time)s.json`

- 

Store in S3 using one directory per spider:

  - 

`s3://mybucket/scraping/feeds/%(name)s/%(time)s.json`

Note

Spider arguments become spider attributes, hence
they can also be used as storage URI parameters.