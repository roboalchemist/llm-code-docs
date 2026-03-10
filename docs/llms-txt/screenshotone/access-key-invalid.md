# Source: https://screenshotone.com/docs/errors/access-key-invalid/

# Access Key Invalid

It is an API error returned when the provided access key is invalid or incorrect.

```json
{
    "is_successful": false,
    "error_code": "access_key_invalid",
    "error_message": "The `access_key` parameter is set, but it is not correct. Please, check out the access dashboard page to get the access key—https://dash.screenshotone.com/access.",
    "documentation_url": "https://screenshotone.com/docs/errors/access-key-invalid/"
}
```

## Reasons and how to fix

### Incorrect Access Key

One common reason for the "access_key_invalid" error is using an incorrect access key. This can happen if the key is copied incorrectly or if an old key is being used.

To fix this, ensure you are using the correct access key by visiting the [access dashboard page](https://dash.screenshotone.com/access) and copying the key directly from there.

### Typographical Errors

Typos in the access key parameter can also lead to this error. This includes extra spaces, missing characters, or incorrect case sensitivity.

To fix this, carefully check and re-enter the access key, ensuring there are no typographical errors. Copy-pasting the key directly from the dashboard is recommended.

### Misconfigured Environment

In some cases, the environment where the API request is being made might be misconfigured, leading to the wrong access key being used.

To fix this, review your environment configuration settings to ensure the correct access key is being used in the appropriate environment (e.g., development, staging, production).

## Reach out to support

If you continue to face issues, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.