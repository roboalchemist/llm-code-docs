# Source: https://screenshotone.com/docs/async-and-webhooks/

# Async and Webhooks

import Alert from "@/components/Alert.astro";

ScreenshotOne supports asynchronous screenshot rendering and webhooks. The document describes both of them in one
place since usually they are used together.

The main current supported use case is to render screenshots asynchronously, [upload them to S3](/docs/upload-to-s3/) and return the file location to the specified webhook. That's what customers asked to implement first.

## Async

You can literally execute any request asynchronously by setting the `async` option to `true.` But not every request makes sense to execute asynchronously.

Once you set `async=true,` the API checks your access key and limits and returns the response immediately but continues to execute the request.

One of the top use cases for which it was requested is uploading files to S3 asynchronously without waiting for screenshots to be rendered.

An example of such a request could be:

```
https://api.screenshotone.com/take?access_key=0MpjJxw8Vk7ZAw&url=https://example.com&store=true&storage_path=example.com&response_type=json&async=true
```

You request rendering but don't wait for the response. What if you want to get the result of uploading? You can do it by using webhooks.

## Webhooks

Using webhooks with ScreenshotOne allows you to deliver the results of the request execution to your URL as a POST body.

<Alert>
    Currently, caching is not supported for webhooks since it doesn't make much
    sense. If you need its support for other use cases, please, send a chat
    message or email to `support@screenshotone.com`.
</Alert>

You can use webhooks with both synchronous and asynchronous requests. But usually, it is used in combination with asynchronous requests.

An example of an asynchronous request that uploads rendered screenshot to S3 and sends a webhook might look like this:

```
https://api.screenshotone.com/take?access_key=<your api key>
  &url=https://example.com
  &store=true
  &storage_path=example.com
  &response_type=json
  &async=true  
  &webhook_url=<your webhook URL>
  &storage_return_location=true
```

Not that, to get the location, you must specify the `storage_return_location` parameter as `true`.

An example of the webhook request body you will receive:

```
{
  "screenshot_url": "...",
  // ...
  "store": {
    // ...
    "location": "..."
  },
}
```

You also receive the `X-ScreenshotOne-Signature` (`x-screenshotone-signature`) header that you should use to validate the webhook request body and make sure that ScreenshotOne sent the request.

If you do not upload the screenshot to any S3-compatible storage, you will receive [the `screenshot_url`](/docs/screenshot-url/) in the response body if you set `response_type=json`: 

```json
{
  // ...
  "screenshot_url": "..."
}
```

If you don't specify the `response_type` parameter as `json`, you will receive the screenshot in the binary format in the response body.

```
<binary data>
```

### Verifying Signature

To ensure that ScreenshotOne sent the request, you should get the signature from the `X-ScreenshotOne-Signature` header and verify it with your secret key from [the access page](https://dash.screenshotone.com/access) by applying the HMAC SHA-256 algorithm.

<Alert>
    Never share your secret key with any party. In case it is leaked, you can
    quickly regenerate it on [the access
    page](https://dash.screenshotone.com/access).
</Alert>

A pseudo-code on TypeScript (Node.js) of how you can do it:

```javascript
import * as crypto from "crypto";

const receivedSignature = request.headers.get("x-screenshotone-signature");
const requestBody = await request.rawText();

const calculatedSignature = crypto
    .createHmac("sha256", yourSecretKey)
    .update(requestBody, "utf-8")
    .digest("hex");

if (calculatedSignature !== receivedSignature) {
    // the signature is not valid
    // you should not process this request and reject it immediately
    throw new Error("...");
}

// it is safe to process the request
// you can do something with the webhook request body
```

### Disable Signing

Singing webhook request body takes time. If you are sure that your webhooks are unique and secret, you might want to disable signing to improve performance by using `webhook_sign=false`.

### Debugging and support headers

There are a few headers that are not part of the body and are not participating in the signing. They must not be used for any logic; it is just for debugging and support purposes:

-   `x-screenshotone-rendering-seconds`—screenshot rendering time in seconds with fractions, e.g. `2.56`;
-   `x-screenshotone-size-bytes`—screenshot size if available (not streaming), e.g. `30033`;
-   `x-screenshotone-trace-id`—unique request trace id when reaching out to the ScreenshotOne support;
-   `x-screenshotone-reference`—screenshot or video id (if available) that can be seen in the history or used when reaching out to the ScreenshotOne support.

### External identifier

You can set `external_identifier` parameter to any alphanumeric value. It will be included in the webhook request headers:

- `x-screenshotone-external-identifier`—external identifier. It is helpful for error tracking and successful request tracking.

### Webhook errors

We currently don't support a separate endpoint to send webhook errors. But you can still get them in the webhook request body or headers.

By default, errors are not sent to the webhook URL, at all. But if you want to get them, you can set `webhook_errors=true` parameter.

And you will get error details in the webhook request body if the JSON response type is used: 

```javascript
{
    // ...  
    "error_code": "...",
    "error_message": "...",
    "documentation_url": "..."
}
```

Or always in the headers: 

- `x-screenshotone-error-code`—error code;
- `x-screenshotone-error-message`—error message;
- `x-screenshotone-documentation-url`—documentation URL about the error.

Check out all possible error codes in the [API error reference](/docs/errors/).

### Testing webhook errors

You can test it with an URL like this `https://example.com/404`. It will trigger an error.

In general, it is enough to check for the error code presence or absence of the screenshot URL/binary data to determine if the request was successful or not.

In the worst case scenario, you might assume if you haven't been notified about any errors or successful requests, likely the request has been failed.

## Summary

That's it. In case you have any questions or problems, feel free to write to `support@screenshotone.com`.