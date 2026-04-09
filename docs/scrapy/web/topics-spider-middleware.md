# Spider Middleware

The spider middleware is a framework of hooks into Scrapy’s spider processing
mechanism where you can plug custom functionality to process the responses that
are sent to Spiders for processing and to process the requests
and items that are generated from spiders.

## Activating a spider middleware

To activate a spider middleware component, add it to the
`SPIDER_MIDDLEWARES` setting, which is a dict whose keys are the
middleware class path and their values are the middleware orders.

Here’s an example:

```
SPIDER_MIDDLEWARES = {
    "myproject.middlewares.CustomSpiderMiddleware": 543,
}

```