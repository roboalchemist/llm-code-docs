# Source: https://screenshotone.com/docs/errors/matched-failed-request/

# Matched Failed Request

This API error is returned when a request matched by the specified pattern in the `fail_if_request_failed` option has been failed:

```json
{
    "is_successful": false,
    "error_code": "matched_failed_request",
    "error_message": "A request matched by the specified pattern by the `fail_if_request_failed` option has been failed. If it seems to be a mistake or not what you expected, please, reach out to `support@screenshotone.com` as quickly as possible, and we will assist and try to resolve your problem.",
    "documentation_url": "https://screenshotone.com/docs/errors/matched-failed-request/"
}
```

## Reasons and how to fix

The reason you get this error message is because you specified the [fail_if_request_failed](/docs/options/#fail_if_request_failed) option.

If you want to disable this behavior, you simply need to remove the parameter from your request. If you have a request like:

```
https://api.screenshotone.com/take?access_key=<your access key>&url=https://example.com&fail_if_request_failed=**example.com**
```

Make it like this:

```
https://api.screenshotone.com/take?access_key=<your access key>&url=https://example.com
```

In case, if the error persists, please immediately reach out to `support@screenshotone.com`, and we will try to fix that as soon as possible.

## Reach out to support

Also, if you encounter any issues or bugs, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.