# Source: https://screenshotone.com/docs/errors/signature-is-required/

# Signature Required

It is an API error returned when the signature parameter is missing in the request.

```json
{
    "is_successful": false,
    "error_code": "signature_is_required",
    "error_message": "The `signature` parameter is required. Because signing requests is required in the access page—https://dash.screenshotone.com/access. Make sure you use the correct signing algorithm—https://screenshotone.com/docs/signed-requests/.",
    "documentation_url": "https://screenshotone.com/docs/errors/signature-is-required/"
}
```

## Reasons and how to fix

### Missing Signature Parameter

The most common reason for the "signature_is_required" error is that the `signature` parameter is not included in the request. This parameter is mandatory for authenticating and authorizing the API request if on the [access dashboard page](https://dash.screenshotone.com/access) forcing signing requests is activated.

To fix this, ensure that you include the `signature` parameter in your API request.

### Programmatic Issues

If you are dynamically generating requests (e.g., through a script or application), there might be a bug causing the `signature` to be omitted.

To fix this, debug your script or application to ensure the `signature` is being properly set and included in every API request.

### Request Validation

To ensure your request is valid, double-check all parameters and the generated signature before sending the request to the API.

## Reach out to support

If you continue to face issues or need further assistance, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.