# Source: https://screenshotone.com/docs/errors/storage-access-denied/

# Storage Access Denied

It is an API error returned when the API can't upload a screenshot your S3 storage because the access is denined:

```json
{
    "is_successful": false,
    "error_message": "Failed to upload the screenshot to the storage since access was denied. Check the API keys you specify when using the storage integration.",
    "error_code": "storage_access_denied",
    "documentation_url": "https://screenshotone.com/docs/errors/storage-access-denied/"
}
```

## Reasons and how to fix

Let's quickly consider possible reasons and possible solutions.

### Perform configuration testing

In [the dashboard](https://dash.screenshotone.com/integrations/s3), you can test configuration and get the detailed error description:

![Configuration Testing](configuration_testing.jpg)

### Check credentials and URL

Make sure and double check that all your credentials and the storage URL is correct.

## Reach out to support

If nothing helps you, please, reach out to `support@screenshotone.com` and we will try to help you as fast as possible.