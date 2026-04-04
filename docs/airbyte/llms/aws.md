# Source: https://docs.airbyte.com/platform/deploying-airbyte/infrastructure/aws.md

# Source: https://docs.airbyte.com/platform/2.0/deploying-airbyte/infrastructure/aws.md

# Source: https://docs.airbyte.com/platform/1.8/deploying-airbyte/infrastructure/aws.md

# Source: https://docs.airbyte.com/platform/1.7/deploying-airbyte/infrastructure/aws.md

# Source: https://docs.airbyte.com/platform/1.6/deploying-airbyte/infrastructure/aws.md

# Amazon Web Services (AWS)

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Airbyte supports Amazon Web Services as a Cloud Provider. There are several ways that you can deploy Airbyte using AWS.

You can use the AWS managed Kubernetes solution EKS, using `abctl` on an EC2 instance, or on a Kubernetes distribution that has been deployed on EC2 instances.

## Policies[​](#policies "Direct link to Policies")

You will need to create an AWS Role and associate that Role with either an AWS User when using Access Credentials, or an Instance Profile or Kubernetes Service Account when using IAM Roles for Service Accounts. That Role will need the following policies depending on in for integrate with S3 and AWS Secret Manager respectively.

### AWS S3 Policy[​](#aws-s3-policy "Direct link to AWS S3 Policy")

The [following policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html#iam-policy-ex0), allow the cluster to communicate with S3 storage

```
{
  "Version": "2012-10-17",
  "Statement":
    [
      { "Effect": "Allow", "Action": "s3:ListAllMyBuckets", "Resource": "*" },
      {
        "Effect": "Allow",
        "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
        "Resource": "arn:aws:s3:::YOUR-S3-BUCKET-NAME",
      },
      {
        "Effect": "Allow",
        "Action":
          [
            "s3:PutObject",
            "s3:PutObjectAcl",
            "s3:GetObject",
            "s3:GetObjectAcl",
            "s3:DeleteObject",
          ],
        "Resource": "arn:aws:s3:::YOUR-S3-BUCKET-NAME/*",
      },
    ],
}
```

### AWS Secret Manager Policy[​](#aws-secret-manager-policy "Direct link to AWS Secret Manager Policy")

The [following policies](https://docs.aws.amazon.com/mediaconnect/latest/ug/iam-policy-examples-asm-secrets.html), allow the cluster to communicate with AWS Secret Manager

```
{
  "Version": "2012-10-17",
  "Statement":
    [
      {
        "Effect": "Allow",
        "Action":
          [
            "secretsmanager:GetSecretValue",
            "secretsmanager:CreateSecret",
            "secretsmanager:ListSecrets",
            "secretsmanager:DescribeSecret",
            "secretsmanager:TagResource",
            "secretsmanager:UpdateSecret",
          ],
        "Resource": ["*"],
        "Condition":
          {
            "ForAllValues:StringEquals":
              { "secretsmanager:ResourceTag/AirbyteManaged": "true" },
          },
      },
    ],
}
```
