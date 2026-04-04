# Source: https://screenshotone.com/docs/getting-started/

# Getting Started

You can use the API to generate invoices in PDF format for any given URL or HTML. Or make hundreds of screenshots of your site with different options to check that the site looks as expected.

Whatever use case you have, I get you covered. If there is a feature missing, please, contact me, and I will try to help you as fast as possible.

## First Touch

ScreenshotOne API is straightforward to use. There is an example of an actual request to an API:

```
GET https://api.screenshotone.com/take?url=https://apple.com&access_key=<access key>
```

The result is:
![A screenshot of the Apple site](apple-screenshot.png)

[Sign up](https://dash.screenshotone.com/sign-up) to get the access key and start taking screenshots.

## Requests

ScreenshotOne API supports both GET and POST HTTP requests.

All requests are sent over HTTPS. HTTPS is a non-negotiable requirement to protect your privacy.

To take a screenshot of the site with GET HTTP request, send a request to:

```
https://api.screenshotone.com/take?[options]
```

Takes and returns a screenshot of the given site with specified [options](/docs/options).

If you send a POST HTTP request to take a screenshot, you should specify options as JSON in the body of the request:

```
POST https://api.screenshotone.com/take
Content-Type: application/json
{
    ...[options]
}
```

### Access key

You can specify the access key as part of `GET` parameters, `POST` `JSON` body, or as a header `X-Access-Key`.

## Responses

The response format depends on the given options. You might request API to return an image of PNG type or raw HTML instead of rendering it.

API returns the `Content-Type` header set according to the relevant MIME type for the requested format in options.

Since API returns binary in the data, you can safely put the request URL to ScreenshotOne API directly into the <img> and <meta> tags:

```
<img
  src="https://api.screenshotone.com/take?url=apple.com&access_key=<your access key>"
  alt="A screenshot of apple.com"
/>
```

## Errors

The request might return an error due to an internal error, invalid options or when the limit is reached. ScreenshotOne API follows the HTTP status code semantic and returns JSON in case of an error:

```
GET https://api.screenshotone.com/?[options]

Content-Type: application/json
{
    "error": {
        "code": "an_error_code",
        "message": "An error message"
    }
}
```

The API will always return [a human-readable error message, error code, and suitable HTTP status code](/docs/errors).