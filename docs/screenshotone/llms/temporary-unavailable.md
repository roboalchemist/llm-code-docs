# Source: https://screenshotone.com/docs/errors/temporary-unavailable/

# Temporary Unavailable

It is an API error returned when the API is temporarily unavailable due to an error or overload.

```json
{
    "is_successful": false,
    "error_code": "temporary_unavailable",
    "error_message": "The API is temporarily unavailable due to an error or overload. Please wait a bit and then safely retry your request.",
    "documentation_url": "https://screenshotone.com/docs/errors/temporary-unavailable/"
}
```

## Reasons and how to fix

### API Overload

One common reason for the "temporary_unavailable" error is that the API is overloaded with requests, causing temporary unavailability.

To fix this, you can:

1. **Wait and retry**: Wait for a short period and then retry your request. The API should become available once the load decreases.
2. **Rate limiting**: Implement rate limiting on your end to avoid overwhelming the API with too many requests in a short period.

### Temporary Errors

Temporary errors or issues within the API infrastructure can also cause this error.

To fix this, consider:

1. **Retry the request**: Since the issue is temporary, retrying the request after a brief wait is often effective.
2. **Monitor status page**: Check [the API status page](https://status.screenshotone.com/) to see if there are any ongoing issues.

### Scheduled Maintenance

The API might be undergoing scheduled maintenance, leading to temporary unavailability.

### Network Issues

Network issues between your system and the API server can also result in this error.

To fix this, ensure your network connection is stable and retry the request.

## Implementing Retry Logic

Implementing retry logic in your application can help handle temporary unavailability gracefully. Use exponential backoff strategy for retries to avoid overwhelming the API further.

## Reach out to support

If you continue to face issues or need further assistance, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.