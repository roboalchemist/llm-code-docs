# Source: https://docs.axonius.com/docs/qualys-s3.md

# Qualys S3 Integrated

Qualys S3 Integrated fetches data from AWS S3 Buckets that are configured to receive data from Qualys scans.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Access Key ID** - Provide your Access Key ID. For detailed instructions, refer to [this page](/docs/connecting-aws-adapter-using-iam-user). Note that in step 3 (copying the JSON containing the roles required for creating the policy), only the S3 roles are relevant.
2. **Region** - Provide your specified S3 bucket region.
3. **Bucket Name** - Provide your bucket name.
4. **Secret Access Key** - The credentials used to access the S3 object.
5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![qualys s3 integrated connection parameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-O0PJL7TR.png)

## APIs

Axonius uses the [Qualys Integration with AWS S3 Bucket API guide](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://cdn2.qualys.com/docs/qualys-aws-s3-integration-user-guide.pdf).

## Supported From Version

Supported from Axonius version 6.1