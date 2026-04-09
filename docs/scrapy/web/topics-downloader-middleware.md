# Downloader Middleware

The downloader middleware is a framework of hooks into Scrapy’s
request/response processing.  It’s a light, low-level system for globally
altering Scrapy’s requests and responses.

## Activating a downloader middleware

To activate a downloader middleware component, add it to the
`DOWNLOADER_MIDDLEWARES` setting, which is a dict whose keys are the
middleware class paths and their values are the middleware orders.

Here’s an example:

```
DOWNLOADER_MIDDLEWARES = {
    "myproject.middlewares.CustomDownloaderMiddleware": 543,
}

```