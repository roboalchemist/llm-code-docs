# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/amazon-simple-storage-service.md

# Amazon Simple Storage Service (S3)

<!-- -->

## AWS::S3::Bucket[â](#awss3bucket "Direct link to AWS::S3::Bucket")

The following example demonstrates how to ingest your AWS S3 buckets to Port.

#### S3 Bucket supported actions[â](#s3-bucket-supported-actions "Direct link to S3 Bucket supported actions")

The table below summarizes the available actions for ingesting Amazon S3 Bucket resources in Port:

| Action                                                                                                                  | Description                                                   | Type     | Required AWS Permission         |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------- | ------------------------------- |
| [ListBucketsAction](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)                               | Discover all S3 buckets across your AWS account.              | Default  | `s3:ListAllMyBuckets`           |
| [GetBucketTaggingAction](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html)                     | Bring in bucket tags for catalog filtering and grouping.      | Default  | `s3:GetBucketTagging`           |
| [GetBucketLocationAction](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html)                   | Retrieve the bucket's region.                                 | Optional | `s3:GetBucketLocation`          |
| [GetBucketEncryptionAction](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html)               | Retrieve server-side encryption configuration for the bucket. | Optional | `s3:GetBucketEncryption`        |
| [GetBucketPublicAccessBlockAction](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)       | Retrieve public access block configuration.                   | Optional | `s3:GetBucketPublicAccessBlock` |
| [GetBucketOwnershipControlsAction](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketOwnershipControls.html) | Retrieve bucket ownership controls.                           | Optional | `s3:GetBucketOwnershipControls` |

Optional Properties Note

Properties of optional actions will not appear in the response unless you explicitly include the action that provides them in your configuration.

You can use the following Port blueprint definitions and integration configuration:

**S3 Bucket blueprint (click to expand)**

Create in Port

```
{
  "identifier": "s3Bucket",
  "description": "This blueprint represents an AWS S3 bucket in our software catalog",
  "title": "S3 bucket",
  "icon": "AWS",
  "schema": {
    "properties": {
      "arn": {
        "type": "string",
        "title": "ARN"
      },
      "creationDate": {
        "type": "string",
        "format": "date-time",
        "title": "Creation date"
      },
      "tags": {
        "type": "array",
        "title": "Tags",
        "items": {
          "type": "object",
          "properties": {
            "Key": {
              "type": "string"
            },
            "Value": {
              "type": "string"
            }
          }
        }
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

**S3 Bucket mapping configuration (click to expand)**

```
resources:
  - kind: AWS::S3::Bucket
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Properties.Arn
          title: .Properties.BucketName
          blueprint: '"s3Bucket"'
          properties:
            arn: .Properties.Arn
            creationDate: .Properties.CreationDate
            tags: .Properties.Tags
          relations:
            account: .__ExtraContext.AccountId
```

For more details about S3 bucket properties, refer to the [AWS S3 API documentation](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html).
