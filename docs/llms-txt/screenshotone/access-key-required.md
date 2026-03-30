# Source: https://screenshotone.com/docs/errors/access-key-required/

# Access Key Required

It is an API error returned when the access key parameter is missing in the request.

```json
{
    "is_successful": false,
    "error_code": "access_key_required",
    "error_message": "The `access_key` parameter is required. Please, check out the access dashboard page to get the access key—https://dash.screenshotone.com/access.",
    "documentation_url": "https://screenshotone.com/docs/errors/access-key-required/"
}
```

## Reasons and how to fix

### Missing Access Key Parameter

The most common reason for the "access_key_required" error is that the `access_key` parameter is not included in the request. This is mandatory for authenticating and authorizing the API request.

To fix this, ensure that you include the `access_key` parameter in your API request. You can obtain your access key from the [access dashboard page](https://dash.screenshotone.com/access).

### Misconfigured Request

Sometimes, a request might be misconfigured, leading to the `access_key` parameter being omitted.

To fix this, review the configuration of your API client or the code that constructs the request to ensure that the `access_key` parameter is always included.

### Typographical Errors

A typo or incorrect parameter name might lead to the `access_key` not being recognized by the API.

To fix this, double-check the parameter name in your request to ensure it is spelled correctly as `access_key`.

### Programmatic Issues

If you are dynamically generating requests (e.g., through a script or application), there might be a bug causing the `access_key` to be omitted.

To fix this, debug your script or application to ensure the `access_key` is being properly set and included in every API request.

## Reach out to support

If you continue to face issues, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.