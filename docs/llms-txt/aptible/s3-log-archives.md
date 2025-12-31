# Source: https://www.aptible.com/docs/core-concepts/observability/logs/s3-log-archives.md

# Log Archiving to S3

<Info> S3 Log Archiving is currently in limited beta release and is only available on the [Enterprise plan](https://www.aptible.com/pricing). Please note that this feature is subject to limited availability while in the beta release stage. </Info>

Once you have configured [Log Drains](/core-concepts/observability/logs/log-drains/overview) for daily access to your logs (e.g., for searching and alerting purposes), you should also configure backup log delivery to Amazon S3. Having this backup method will help ensure that, in the event, your primary logging provider experiences delivery or availability issues, your ability to retain logs for compliance purposes will not be impacted.

Aptible provides this disaster-recovery option by uploading archives of your container logs to an S3 bucket owned by you, where you can define any retention policies as needed.

# Setup

## Prerequisites

To begin sending log archives to an S3 bucket, you must have your own AWS account and an S3 bucket configured for this purpose.

This must be the sole purpose of your S3 bucket (that is, do not add other content to this bucket), your S3 bucket **must** have versioning enabled, and your S3 bucket **must** be in the same region as your Stack. To enable [S3 bucket versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) via the AWS Console, visit the Properties tab of your S3 bucket, click Edit under Bucket Versioning, choose Enable, and then Save Changes.

## Process

Once you have created a bucket and enabled versioning, apply the following policy to the bucket in order to allow Aptible to replicate objects to it.

<Warning> You need to replace `YOUR_BUCKET_NAME` in both "Resource" sections with the name of your bucket. </Warning>

```json  theme={null}
{
  "Version": "2012-10-17",
  "Id": "Aptible log sync",
  "Statement": [
    {
      "Sid": "dest_objects",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::916150859591:role/s3-stack-log-replication"
      },
      "Action": [
        "s3:ReplicateObject",
        "s3:ReplicateDelete",
        "s3:ObjectOwnerOverrideToBucketOwner"
      ],
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
    },
    {
      "Sid": "dest_bucket",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::916150859591:role/s3-stack-log-replication"
      },
      "Action": [
        "s3:List*",
        "s3:GetBucketVersioning",
        "s3:PutBucketVersioning"
      ],
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME"
    }
  ]
}
```

Contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) to request access to this limited beta. We will need to know:

* Your AWS Account ID.
* The name of your S3 bucket to use for archiving.

# Delivery

To ensure you only need to read or process each file once, we do not upload any files which are actively being written to. This means we will only upload a log archive file when either of two conditions is met:

* After the container has exited, the log file will be eligible for upload.
* If the container log exceeds 500 MB, we will rotate the log, and the rotated file will be eligible for upload.

Aptible will upload log files at the bottom of every hour (1:30, 2:30, etc.).

If you have long-running containers that generate a low volume of logs, you may need to restart the App or Database periodically to flush the log archives to S3. As such, this feature is only intended to be used as a disaster archive for compliance purposes, not for the troubleshooting of running services, data processing pipelines, or any usage that mandates near-realtime access.

# Retrieval

You should not need access the log files from your S3 bucket directly, as Aptible has provided a command in our [CLI](/reference/aptible-cli/cli-commands/overview) that provides you the ability to search, download and decrypt your container logs: [`aptible logs_from_archive`](/reference/aptible-cli/cli-commands/cli-logs-from-archive).

This utility has no reliance on Aptible's services, and since the S3 bucket is under your ownership, you may use it to access your Log Archive even if you are no longer a customer of Aptible.

# File Format

## Encryption

Files stored in your S3 bucket are encrypted with an AES-GCM 256-bit key, protecting your data in transit and at rest in your S3 bucket. Decryption is handled automatically upon retrieval via the Aptible CLI.

## Compression

The files are stored and downloaded in gzip format to minimize storage and transfer costs.

## JSON Format

Once uncompressed, the logs will be in the [JSON format as emitted by Docker](https://docs.docker.com/config/containers/logging/json-file/). For example:

```json  theme={null}
{"log":"Log line is here\n","stream":"stdout","time":"2022-01-01T12:23:45.5678Z"}
{"log":"An error may be here\n","stream":"stderr","time":"2022-01-01T12:23:45.5678Z"}
```
