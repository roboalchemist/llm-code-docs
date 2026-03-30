# Source: https://screenshotone.com/docs/bulk-screenshots/

# Bulk Screenshots

import Alert from "@/components/Alert.astro";

:::tip
Our bulk screenshots API endpoint is a simple wrapper endpoint around the regular screenshot API endpoints like (`/take`, `/animate`, and similar). But since it is a simple wrapper, you might find it much better to implement your own bulk screenshot solution. Check out our guide on [how to take screenshots of multiple URLs](/docs/guides/bulk-screenshots/) with ScreenshotOne API.
:::

## Request

You can use a bulk screenshot-taking feature to take many screenshots in one request.
Send a simple POST HTTP request to `/bulk` path with the list of URLs (HTML or Markdown):

```
POST https://api.screenshotone.com/bulk 

{
    "access_key": "<your access key>"
    "execute": false,
    "optimize": false,
    "options": {"url": "https://example.com", "viewport_width": 1280, "viewport_height": 1024, "block_ads": true}, 
    "requests": [
        {"viewport_width": 360, "viewport_height": 640}, // a screenshot of example.com with a different viewport
        {"url": "https://example.com"},
        {"url": "https://finance.yahoo.com", "block_cookie_banners": true},
        {"html": "<h1>Hello, world!</h1>", "block_ads": false}, 
        {"markdown": "**Yes!**"}
    ]
}
```

The options property contains default options that will be applied to every request. And for every request, you can specify options to override the default values. You can specify all [the regular options you use to take a single screenshot](/docs/options).

You can specify the access key as a query parameter `access_key=<your access key>`, an HTTP header `X-Access-Key: <your access key>`, or in the request's body.

## Response

The response contains an array of screenshot URLs you can use to download the screenshots:

```json
{
    "responses": [
        {"url": "https://api.screenshotone.com/take?url=http://example.com&viewport_width=1280&viewport_height=1024&block_ads=true"},
        {"url": "https://api.screenshotone.com/take?url=https://finance.yahoo.com&viewport_width=1280&viewport_height=1024&block_ads=true&block_cookie_banners=true"},
        {"url": "https://api.screenshotone.com/take?html=<h1>Hello, world!</h1>&viewport_width=1280&viewport_height=1024&block_ads=false&block_cookie_banners=true"}
    ]
}
```

But if you requested to [execute requests](#execute-requests), the result will also contain a summary execution response for each request: 

```
[
    {
        "url": "https://api.screenshotone.com/take?url=http://example.com&viewport_width=1280&viewport_height=1024&block_ads=true",
        "response": {
            "is_successful": true,
            "status": 200,
            "statusText": "OK"
        }
    },
    {
        "url": "https://api.screenshotone.com/take?url=https://finance.yahoo.com&viewport_width=1280&viewport_height=1024&block_ads=true&block_cookie_banners=true",
        "response": {
            "is_successful": true,
            "status": 200,
            "statusText": "OK"
        }
    },
    {
        "url": "https://api.screenshotone.com/take?html=<h1>Hello, world!</h1>&viewport_width=1280&viewport_height=1024&block_ads=false&block_cookie_banners=true",
        "response": {
            "is_successful": true,
            "status": 200,
            "statusText": "OK"
        }
    },
    {
        "url": "https://api.screenshotone.com/take?markdown=**Yes!**&viewport_width=1280&viewport_height=1024&block_ads=false&block_cookie_banners=true",
        "response": {
            "is_successful": true,
            "status": 200,
            "statusText": "OK"
        }
    }
]
```

As you noticed, images are not returned, but in case of an error, the `is_successful` property will be `false`, and you can expect the `body` property to explore the error:

```
[
    {
        "url": "https://api.screenshotone.com/take?url=http://example.com&viewport_width=1280&viewport_height=1024&block_ads=true",
        "response": {
            "is_successful": false,
            "status": 400,
            "statusText": "Bad request", 
            body: {
                "error_code": "concurrency_limit_reached"
                "error_message": "Concurrency limit is reached"
            }
        }
    }
]
```

## Execute requests 

Bulk screenshots are implemented in a lazy loading way. It means that the screenshot is literally taken when you tried to download it, not when you sent a bulk request. If you want to execute each request before you get a response, set the parameter `execute` to `true`:
```
POST https://api.screenshotone.com/bulk 

{
    "access_key": "<your access key>"
    "execute": true,
    // ... 
}
```

But make sure to wait enough time until all the screenshots are done.

## Optimizations

To take bulk screenshots faster, you can use the optimization feature if you want to take bulk screenshots for the same URLs (HTML or Markdown) but with a different set of parameters: 

```
POST https://api.screenshotone.com/bulk 

{
    "access_key": "<your access key>"
    "execute": true,
    "optimize": true,
    "options": {"url": "https://example.com", "viewport_width": 1280, "viewport_height": 1024}, 
    "requests": [
        {"viewport_width": 360, "viewport_height": 640}, // a screenshot of example.com with a different viewport
        {"viewport_width": 736, "viewport_height": 414}
    ]
}
```

<Alert>
The feature only works when `execute` is set to `true`.
</Alert>

The optimization is not guaranteed since many sites can reload and take the same time to render in case the viewport is changed. And some options, like blocking and not blocking ads, do require a page reload, which takes the same time as not using optimization at all. 

The best approach is to test if it works for your use case.

## Use cases 

### Upload bulk screenshots to S3-compatible storage

In the example, I want to take screenshots for one site but for different devices and upload them to [S3-compatible storage](https://screenshotone.com/docs/options/#storing): 

```
POST https://api.screenshotone.com/bulk 

{
    "access_key": "<your access key>"
    "execute": true,
    "options": {"url": "https://example.com", "store": true, "response_type": "empty"}, 
    "requests": [
        {"viewport_device": "pixel_4a_5g_landscape", "storage_path": "pixel_4a_5g_landscape"},        
        {"viewport_device": "iphone_13_pro", "storage_path": "iphone_13_pro"},        
        {"viewport_device": "iphone_13", "storage_path": "iphone_13"}        
    ]
}
```

In this example, I upload screenshots taken from different devices and save the files with the names of the devices. 

## Limitations

Currently, only up to 20 requests are supported in the one bulk request.