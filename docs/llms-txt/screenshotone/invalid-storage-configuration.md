# Source: https://screenshotone.com/docs/errors/invalid-storage-configuration/

# Invalid Storage Configuration

It is an API error returned when the storage configuration for S3 is invalid.

```json
{
    "is_successful": false,
    "error_code": "invalid_storage_configuration",
    "error_message": "If you haven't created the bucket in the `us-east-1` AWS region, please, specify your bucket region through an endpoint in a format like https://s3.<your-region>.amazonaws.com.",
    "documentation_url": "https://screenshotone.com/docs/errors/invalid-storage-configuration/"
}
```

## Reasons and how to fix

### Incorrect AWS S3 Bucket Region

One common reason for the "invalid_storage_configuration" error is that the S3 bucket is not created in the `us-east-1` region and the bucket region is not specified correctly.

To fix this, you can:

1. **Specify the bucket Region**: Ensure you specify your bucket region in the endpoint format like `https://s3.<your-region>.amazonaws.com`. Replace `<your-region>` with the actual AWS region where your bucket is located.

### Missing or misconfigured Bucket

If the S3 bucket does not exist or is misconfigured, this can lead to the "invalid_storage_configuration" error.

To fix this, consider:

1. **Verify bucket existence**: Check that the S3 bucket exists in your AWS account and is accessible.
2. **Correct bucket configuration**: Ensure the bucket is configured correctly, including permissions and policies.

### Incorrect Endpoint URL

The endpoint URL might be incorrectly formatted, causing the API to fail in accessing the specified S3 bucket.

To fix this, ensure the endpoint URL is correctly formatted as `https://s3.<your-region>.amazonaws.com`, with the correct region specified.

### AWS IAM Permissions

Inadequate permissions set in the AWS IAM policies might prevent the API from accessing the S3 bucket, leading to this error.

To fix this, ensure that the IAM roles and policies associated with your bucket have the necessary permissions to allow access from the API.

## Reach out to support

If you continue to face issues or need further assistance, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.