# Source: https://screenshotone.com/docs/errors/invalid-cookie-parameter/

# Invalid Cookie Parameter

It is an API error returned when the `cookies` parameter is invalid.

```json
{
    "is_successful": false,
    "error_message": "The `cookies` parameters you provided are invalid. Please, consider providing different values and adhere to the format specified in the ScreenshotOne documentation.",
    "error_code": "invalid_cookie_parameter",
    "documentation_url": "https://screenshotone.com/docs/errors/invalid-cookie-parameter/"
}
```

## Reasons and how to fix

### The format of the parameter is invalid

Make sure you adhere to the format specified in the [ScreenshotOne options documentation](https://screenshotone.com/docs/options/#cookies):

```
cookies=name1=val1; Domain=example.com; Secure; HttpOnly
```

It is not for demonstration purposes, but the string must be URL-encoded. 

If you need to specify multiple cookies, you can do it like this:

```
cookies=name1=val1; Domain=example.com; Secure; HttpOnly&cookies=name2=val2; Domain=example.com; Secure; HttpOnly
```

## Reach out to support

If you continue to face issues, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.