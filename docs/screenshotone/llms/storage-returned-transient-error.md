# Source: https://screenshotone.com/docs/errors/storage-returned-transient-error/

# Storage Returned Transient Error

It is an API error returned when the storage server returns a transient error and retries have been exhausted.

```json
{
    "is_successful": false,
    "error_code": "storage_returned_transient_error",
    "error_message": "The storage returned an HTTP status code between 500 and 599 and we exhausted retries. You can likely retry the request again.",
    "documentation_url": "https://screenshotone.com/docs/errors/storage-returned-transient-error/"
}
```

## Reasons and how to fix

### Transient Storage Server Error

The most common reason for the "storage_returned_transient_error" is that the S3 storage returned an HTTP status code between 500 and 599, indicating a transient error.

To fix this, you can:

1. **Retry the request**: Since the error is transient, retrying the request after a short wait is often effective.
2. **Check storage service status**: Verify the status of the storage service you are using to see if there are any ongoing issues or maintenance that might be causing the error.

### Exhausted Retries

The API has attempted to retry the request multiple times but has exhausted its retry limit.

To fix this, consider implementing additional retries on your end, with exponential backoff to avoid overwhelming the storage server.

### Temporary Network Issues

Temporary network issues can also cause transient errors from the storage server.

To fix this, ensure that your network connection is stable and retry the request.

## Reach out to support

If you continue to face issues or need further assistance, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.