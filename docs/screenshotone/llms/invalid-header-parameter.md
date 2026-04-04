# Source: https://screenshotone.com/docs/errors/invalid-header-parameter/

# Invalid Header Parameter

It is an API error returned when the `headers` parameter is invalid.

```json
{
    "is_successful": false,
    "error_message": "The `headers` parameters you provided are invalid. Please, consider providing different values and adhere to the format specified in the ScreenshotOne documentation.",
    "error_code": "invalid_header_parameter",
    "documentation_url": "https://screenshotone.com/docs/errors/invalid-header-parameter/"
}
```

## Reasons and how to fix

### The format of the parameter is invalid

Make sure you adhere to the format specified in the [ScreenshotOne options documentation](https://screenshotone.com/docs/options/#headers). If you sent a GET request, your headers must be in the query string as:

```
headers=name1:val1&headers=name2:val2
```

If you sent a POST request, your headers must be in the request body as:

```json
{
    // ...
    "headers": ["name1:val1", "name2:val2"]
    // ...
}
```

## Reach out to support

If you continue to face issues, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.