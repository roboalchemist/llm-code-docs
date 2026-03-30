# Source: https://screenshotone.com/docs/errors/host-returned-error/

# Host Returned Error

It is an API error returned when the host server does not respond with a successful status code within the range of 200-299.

```json
{
    "is_successful": false,
    "error_code": "host_returned_error",
    "error_message": "If the host doesn't respond successfully within the range of 200-299 status codes, the API won't take a screenshot. You can force the API to take a screenshot of the error page by specifying `ignore_host_errors`=true. You can get the returned status code from the site by reading the `returned_status_code` field.",
    "documentation_url": "https://screenshotone.com/docs/errors/host-returned-error/"
}
```

## Reasons and how to fix

### Host Returned Non-Success Status Code

The most common reason for the "host_returned_error" error is that the host server returned a status code outside the 200-299 range, indicating an unsuccessful response.

To fix this, you can:

1. **Check host server status**: Ensure the host server is operational and capable of returning a successful status code.
2. **Review site response**: Investigate the response from the host server to understand why it is not returning a successful status code.

### Forcing Screenshot of Error Pages

If you want the API to take a screenshot of the error page even when the host returns an error, you can use the `ignore_host_errors` option.

To fix this, set `ignore_host_errors` to `true` in your API request:

```json
{
    "ignore_host_errors": true
}
```

## Retrieving the Returned Status Code

You can get the status code returned by the host server by reading the `returned_status_code` field in the response. This will help in diagnosing and understanding the nature of the error.

## Reach out to support

If you continue to face issues or need further assistance, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.