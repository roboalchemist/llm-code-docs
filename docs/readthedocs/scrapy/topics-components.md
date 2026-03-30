# Components

A Scrapy component is any class whose objects are built using
`build_from_crawler()`.

That includes the classes that you may assign to the following settings:

- 

`ADDONS`

- 

`DNS_RESOLVER`

- 

`DOWNLOAD_HANDLERS`

- 

`DOWNLOADER_CLIENTCONTEXTFACTORY`

- 

`DOWNLOADER_MIDDLEWARES`

- 

`DUPEFILTER_CLASS`

- 

`EXTENSIONS`

- 

`FEED_EXPORTERS`

- 

`FEED_STORAGES`

- 

`ITEM_PIPELINES`

- 

`SCHEDULER`

- 

`SCHEDULER_DISK_QUEUE`

- 

`SCHEDULER_MEMORY_QUEUE`

- 

`SCHEDULER_PRIORITY_QUEUE`

- 

`SCHEDULER_START_DISK_QUEUE`

- 

`SCHEDULER_START_MEMORY_QUEUE`

- 

`SPIDER_MIDDLEWARES`

Third-party Scrapy components may also let you define additional Scrapy
components, usually configurable through settings, to
modify their behavior.

## Initializing from the crawler

Any Scrapy component may optionally define the following class method:

*classmethod *from_crawler(*cls*, *crawler: scrapy.crawler.Crawler*, **args*, ***kwargs*)

Return an instance of the component based on *crawler*.

*args* and *kwargs* are component-specific arguments that some components
receive. However, most components do not get any arguments, and instead
use settings.

If a component class defines this method, this class method is called to
create any instance of the component.

The *crawler* object provides access to all Scrapy core components like
settings and signals,
allowing the component to access them and hook its functionality into
Scrapy.

## Settings

Components can be configured through settings.

Components can read any setting from the
`settings` attribute of the
`Crawler` object they can get for initialization. That includes both built-in and custom settings.

For example:

```
class MyExtension:
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings.getbool("LOG_ENABLED"))

    def __init__(self, log_is_enabled=False):
        if log_is_enabled:
            print("log is enabled!")

```