# Add-ons

Scrapy’s add-on system is a framework which unifies managing and configuring
components that extend Scrapy’s core functionality, such as middlewares,
extensions, or pipelines. It provides users with a plug-and-play experience in
Scrapy extension management, and grants extensive configuration control to
developers.

## Activating and configuring add-ons

During `Crawler` initialization, the list of enabled
add-ons is read from your `ADDONS` setting.

The `ADDONS` setting is a dict in which every key is an add-on class or its
import path and the value is its priority.

This is an example where two add-ons are enabled in a project’s
`settings.py`:

```
ADDONS = {
    'path.to.someaddon': 0,
    SomeAddonClass: 1,
}

```