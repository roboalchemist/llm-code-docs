# Extensions

Extensions are components that allow inserting your
own custom functionality into Scrapy.

Unlike other components, extensions do not have a specific role in Scrapy. They
are “wildcard” components that can be used for anything that does not fit the
role of any other type of component.

## Loading and activating extensions

Extensions are loaded at startup by creating a single instance of the extension
class per spider being run.

To enable an extension, add it to the `EXTENSIONS` setting. For
example:

```
EXTENSIONS = {
    "scrapy.extensions.corestats.CoreStats": 500,
    "scrapy.extensions.telnet.TelnetConsole": 500,
}

```