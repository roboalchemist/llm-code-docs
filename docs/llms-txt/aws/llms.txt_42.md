# Source: https://docs.aws.amazon.com/AmazonS3/latest/userguide/llms.txt

# Amazon Simple Storage Service User Guide

> Learn how to use Amazon Simple Storage Service (Amazon S3) to store and retrieve any amount of data from anywhere. This guide explains Amazon S3 concepts, such as buckets, objects, and related configurations, and includes code examples for common operations.

- [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [Amazon S3 Object Lambda availability change](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazons3-ol-change.html)
- [Tagging S3 resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html)
- [Quotas](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Quotas.html)
- [Reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Reference.html)
- [Document history](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WhatsNew.html)

## [Getting started](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)

- [Using Amazon S3 with the AWS CLI](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GettingStartedS3CLI.html): Learn how to use the AWS CLI to create general purpose buckets, upload objects, download objects, and manage your Amazon S3 resources.


## [Working with general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html)

- [General purpose buckets overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html): Store all of your files, known as objects, within a uniquely named Amazon S3 general purpose bucket.
- [Common bucket patterns](https://docs.aws.amazon.com/AmazonS3/latest/userguide/common-bucket-patterns.html): Learn more about common general purpose bucket patterns for building applications on Amazon S3, including the multi-tenant bucket pattern and the bucket-per-use pattern.
- [Naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html): Learn about the rules for naming Amazon S3 general purpose buckets.
- [Quotas, restrictions, and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html): Restrictions for using general purpose buckets in Amazon S3, including the number of buckets per account and bucket naming guidelines.

### [Accessing a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html)

Learn about the various ways to access general purpose buckets in Amazon S3.

- [Virtual hosting of general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html): Use virtual hosting to serve multiple websites from a single web server.
- [Creating a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html): Learn how to create an Amazon S3 general purpose bucket, configure essential settings, and understand key concepts like S3 Object Ownership, S3 Block Public Access settings, and default encryption.
- [Viewing bucket properties](https://docs.aws.amazon.com/AmazonS3/latest/userguide/view-bucket-properties.html): View Amazon S3 general purpose bucket properties like versioning, tags, encryption, logging, notifications, object locking, static website hosting, and more.
- [Listing buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/list-buckets.html): List your Amazon S3 general purpose buckets.
- [Emptying a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/empty-bucket.html): Delete the contents of an Amazon S3 general purpose bucket using the console, AWS CLI, or APIs, or by using a lifecycle configuration.
- [Deleting a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html): Learn how to delete an Amazon S3 general purpose bucket by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), or AWS SDKs.

### [Mountpoint for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mountpoint.html)

Learn how to install and use Mountpoint for Amazon S3 to mount Amazon S3 buckets on your local file system.

- [Installing Mountpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mountpoint-installation.html): Learn how to install Mountpoint for Amazon S3 so that you can manage S3 general purpose bucket objects on your local file system.
- [Configuring and using Mountpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mountpoint-usage.html): Learn how to configure and use Mountpoint for Amazon S3 so that you can manage S3 general purpose bucket objects on your local file system.
- [Troubleshooting Mountpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mountpoint-troubleshooting.html): Learn how to access logs and other assistance for troubleshooting Mountpoint for Amazon S3.

### [Storage Browser for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-browser.html)

Learn how to install and use Storage Browser for S3 to access S3 data according to your use case.

- [Using Storage Browser for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-storagebrowser.html): In Storage Browser for S3, a location is an S3 general purpose bucket or prefix, that you grant end users access to using S3 Access Grants, IAM policies, or your own managed authorization service.
- [Installing Storage Browser for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/installing-storagebrowser.html): The fastest way to get started with Storage Browser is to clone one of the sample projects on GitHub.
- [Setting up Storage Browser for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setup-storagebrowser.html): To connect end users with Amazon S3 locations, you must first set up an authentication and authorization method.
- [Configuring Storage Browser for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3config-storagebrowser.html): To allow Storage Browser for S3 access to S3 buckets, the Storage Browser component makes the REST API calls to Amazon S3.
- [Troubleshooting Storage Browser for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshooting-storagebrowser.html): If youâre experiencing issues with Storage Browser for S3, make sure to review the following troubleshooting tips:

### [Configuring Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html)

Get faster data transfers to and from Amazon S3 with Amazon S3 Transfer Acceleration.

- [Getting started](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-getting-started.html): How to get started using Amazon S3 Transfer Acceleration.
- [Enabling Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-examples.html): Enable Amazon S3 Transfer Acceleration on a bucket and use the acceleration endpoint for the enabled general purpose bucket.
- [Speed Comparison tool](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-speed-comparison.html): Describes Amazon S3 Transfer Acceleration Speed Comparison tool.

### [Using Requester Pays](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html)

Configure a general purpose bucket to be a Requester Pays bucket so that the requester pays the cost of the request and data download instead of the bucket owner.

- [Configuring Requester Pays](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysExamples.html): Configure a Requester Pays bucket in Amazon S3 using the console or REST API.
- [Retrieving the requestPayment configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketPayerValues.html): You can determine the Payer value that is set on a bucket by requesting the resource requestPayment.
- [Downloading objects from Requester Pays buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ObjectsinRequesterPaysBuckets.html): Set up a confirmation notice so that requesters acknowledge that they will be charged for downloading data from the Requester Pays buckets.


## [Working with objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-downloading-objects.html)

- [Objects overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html): Describes the fundamental elements of an Amazon S3 object and how to use the object.
- [Naming objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html): Learn how to use object keys to name Amazon S3 objects.

### [Working with metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingMetadata.html)

Find and change select Amazon S3 object metadata.

- [Editing object metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-object-metadata.html): How to edit metadata for an Amazon S3 object or object.

### [Discovering your data with S3 Metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html)

Use Amazon S3 Metadata to accelerate data discovery by easily surfacing, storing, and querying the metadata for your S3 objects.

- [Limitations and restrictions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-restrictions.html): Learn about the restrictions and limitations for creating Amazon S3 metadata tables.
- [Journal tables schema](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-schema.html): Learn about the schema for Amazon S3 Metadata fully managed Apache Iceberg journal tables.
- [Live inventory tables schema](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-inventory-schema.html): Learn about the schema for Amazon S3 Metadata fully managed Apache Iceberg inventory tables.

### [Configuring metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-configuring.html)

Learn how to configure Amazon S3 metadata tables for your general purpose buckets.

- [Permissions for metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-permissions.html): Learn about the permissions required to create and work with Amazon S3 metadata tables.
- [Creating metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-create-configuration.html): Learn how to create a metadata table configuration for an Amazon S3 general purpose bucket.
- [Controlling access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-access-control.html): Control access to your Amazon S3 metadata tables by using table bucket and table policies.
- [Expiring journal table records](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-expire-journal-table-records.html): Learn how to expire journal table records in an Amazon S3 Metadata journal table.
- [Enabling or disabling live inventory tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-enable-disable-inventory-tables.html): Learn how to enable or disable live inventory tables in an Amazon S3 Metadata metadata table configuration.
- [Viewing metadata table configurations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-view-configuration.html): Learn how to view your Amazon S3 Metadata table configuration for a general purpose bucket.
- [Deleting metadata table configurations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-delete-configuration.html): Learn how to remove an Amazon S3 metadata table configuration from a general purpose bucket
- [Deleting metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-delete-table.html): Learn how to delete an Amazon S3 metadata table from a table bucket.

### [Querying metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-querying.html)

Learn how to analyze your Amazon S3 Metadata tables with any query engine that supports the Apache Iceberg format.

- [Permissions for querying metadata tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-bucket-query-permissions.html): Learn about the required permissions to query S3 Metadata tables.
- [Querying metadata tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-bucket-integration.html): Learn how you can query your S3 Metadata tables by using AWS analytics services such as Amazon Athena, Amazon Redshift, and Amazon EMR.
- [Querying metadata tables with open-source query engines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-bucket-integration-open-source.html): Learn how you can query your S3 Metadata tables by using open-source query engines, such as Apache Spark.
- [Optimizing query performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-optimizing-query-performance.html): Learn how to optimize your S3 Metadata table queries for performance and cost.

### [Example metadata table queries](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-example-queries.html)

See a list of example SQL queries to help you understand the kind of data you can get from your S3 Metadata tables.

- [Joining custom metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-join-custom-metadata.html): Learn how to join S3 Metadata tables with your self-managed metadata tables.
- [Visualizing metadata table data with Quick](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-quicksight-dashboards.html): Learn how you can get insights about your S3 metadata tables, such as understanding what storage classes your objects use.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-troubleshooting.html): Learn how to troubleshoot common issues with Amazon S3 Metadata.

### [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html)

Upload files or folders to an Amazon S3 bucket.

### [Using multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

Upload a single object as a set of parts independently using the multipart upload API.

- [Configuring a lifecycle configuration to delete incomplete multipart uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.html): Configure a lifecycle rule to abort incomplete multipart uploads by using the AWS Command Line Interface or AWS Management Console.
- [Uploading an object using multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-upload-object.html): Use multipart upload to upload a single object to Amazon S3.
- [Uploading a directory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HLuploadDirDotNet.html): Upload a directory to Amazon S3 using the high-level .NET TransferUtility class.
- [Listing multipart uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/list-mpu.html): List in progress multipart uploads.
- [Tracking a multipart upload with the AWS SDKs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/track-mpu.html): Monitor in progress multipart uploads.
- [Aborting a multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/abort-mpu.html): Stop in progress multipart uploads.
- [Copying an object using multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CopyingObjectsMPUapi.html): Copy objects greater than 5 GB by breaking it into parts to upload using the Amazon S3 multipart upload API.
- [Upload an object through multipart upload and verify its data integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorial-s3-mpu-additional-checksums.html): Walk through an example of how to do multipart upload in Amazon S3 and verify the data integrity of the uploaded files.
- [Multipart upload limits](https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html): Lists the core specifications including size restrictions of a multipart upload.

### [Making conditional requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html)

conditional requests are included in header fields and test a precondition before doing some S3 operation.

- [How to retrieve or copy objects based on metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-reads.html): conditional requests are included in header fields and test a precondition before doing some S3 operation.

### [How to prevent object overwrites](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes.html)

conditional requests are included in header fields and test a precondition before doing some S3 operations.

- [Enforce conditional writes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes-enforce.html): conditional requests are included in header fields and test a precondition before doing some S3 operations.

### [How to perform conditional deletes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-deletes.html)

conditional deletes are included in header fields and test a precondition before doing some S3 operations.

- [Enforce conditional deletes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-delete-enforce.html): conditional deletes are included in header fields and test a precondition before doing some S3 operations.
- [Copying, moving, and renaming objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/copy-object.html): Learn how to copy, move, or rename an object that's already stored in Amazon S3.
- [Downloading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html): Learn how to download objects from an Amazon S3 bucket.

### [Checking object integrity in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html)

Verify the integrity of objects uploaded and downloaded to Amazon S3.

- [Checking object integrity for data uploads in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity-upload.html): Verify the integrity of objects uploaded and downloaded to Amazon S3.
- [Checking object integrity for data at rest in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity-at-rest.html): Verify the integrity of objects uploaded and downloaded to Amazon S3, at rest.

### [Deleting objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html)

Delete one or more objects directly from Amazon S3 whether or not the bucket has versioning enabled.

- [Deleting a single object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-objects.html): Delete a single object directly from Amazon S3.
- [Deleting multiple objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-multiple-objects.html): Delete a multiple objects directly from Amazon S3.

### [Organizing and listing objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/organizing-objects.html)

Use prefixes and folders to organize objects and group similar objects together in a bucket.

- [Using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html): Use prefixes in Amazon S3 to organize object keys hierarchically.
- [Listing objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ListingKeysUsingAPIs.html): Use the Amazon S3 list operation to select and browse object keys hierarchically.
- [Using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html): Use the Amazon S3 console to create folders that you can use to group your objects.
- [Viewing object properties](https://docs.aws.amazon.com/AmazonS3/latest/userguide/view-object-properties.html): View and configure Amazon S3 object properties using the console, including storage class, encryption settings, tags, and metadata.

### [Categorizing objects with tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html)

Lists the restrictions of objects tags, includes examples of tagging objects, and the API operations for tagging objects

- [Controlling access with tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging-and-policies.html): Explains how to use permissions policies to manage object tagging related permissions.
- [Managing object tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging-managing.html): How to label Amazon S3 objects with tags in the console and SDK.

### [Using presigned URLs to download and upload objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html)

Use a presigned URL to share or upload objects in Amazon S3 without requiring AWS security credentials or permissions.

- [Sharing objects with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html): Describes how to set up your objects so that you can share them with others by creating a presigned URL to download the objects.
- [Uploading objects with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html): Upload objects by using presigned URLs when someone with permission has provided you with the URL resources.

### [Transforming objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html)

Extend the functionality of standard Amazon S3 access points by using Object Lambda Access Points to perform data transformations on objects that are accessed through access points.

### [Creating Object Lambda Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-create.html)

Create Object Lambda Access Points to extend the functionality of standard Amazon S3 access points and perform data transformations on objects that are accessed through access points.

- [Automate S3 Object Lambda setup with AWS CloudFormation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-using-cfn-template.html): Use CloudFormation templates to quickly set up Object Lambda Access Points.
- [Using Amazon S3 Object Lambda Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-use.html): Use Amazon S3 Object Lambda Access Points to extend the functionality of standard Amazon S3 access points and perform data transformations on objects that are accessed through access points.

### [Security considerations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-security.html)

Learn about the various security considerations for Amazon S3 Object Lambda Access Points.

- [Configuring IAM policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-policies.html): Configure AWS Identity and Access Management (IAM) resource policies so that you can control the use of Object Lambda Access Points in Amazon S3.

### [Writing Lambda functions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-writing-lambda.html)

Write and debug AWS Lambda functions to extend the functionality of standard Amazon S3 access points that support S3 Object Lambda Access Points.

- [Event context format and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-event-context.html): Example request data fields sent by Object Lambda Access Points.
- [Working with Range and partNumber headers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/range-get-olap.html): Use only a byte Range or partNumber with Object Lambda Access Points.
- [Using AWS built functions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-examples.html): Use AWS built functions to create an AWS Lambda function to use with Amazon S3 Object Lambda Access Points.
- [Best practices and guidelines for S3 Object Lambda](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-best-practices.html): When using S3 Object Lambda, follow these best practices and guidelines to optimize operations and performance.

### [S3 Object Lambda tutorials](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-tutorials.html)

Provide tutorials of S3 Object Lambda

- [Transforming data with S3 Object Lambda](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorial-s3-object-lambda-uppercase.html): Walk through an example of how to transform data in Amazon S3 using S3 Object Lambda to suit the needs of the requesting client or application.
- [Detecting and redacting PII data](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorial-s3-object-lambda-redact-pii.html): Walk through an example of how to use S3 Object Lambda with an AWS Lambda function supported by Amazon Comprehend in the AWS Serverless Application Repository to detect, redact, and protect sensitive personally identifiable information (PII) data.
- [Troubleshooting S3 Object Lambda](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-debugging-lambda.html): Troubleshoot S3 Object Lambda errors.

### [Performing object operations in bulk](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html)

Perform large-scale batch operations on Amazon S3 objects using S3 Batch Operations.

- [Granting permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-iam-role-policies.html): Grant the permissions that are required for creating and performing S3 Batch Operations jobs.
- [Creating a job](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-create-job.html): Create a job to perform large-scale batch operations on Amazon S3 objects by using S3 Batch Operations.

### [Supported operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-operations.html)

Learn which operations are supported by S3 Batch Operations.

### [Copy objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-copy-object.html)

Learn how to use Amazon S3 Batch Operations to copy objects.

### [Examples that use Batch Operations to copy objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-examples-copy.html)

Examples using Amazon S3 Batch Operations to create a Copy (CopyObject) job to copy Amazon S3 objects in bulk.

- [Using an inventory report to copy objects across AWS accounts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/specify-batchjob-manifest-xaccount-inventory.html): Use Amazon S3 Inventory to create an inventory report and use the report to create a list of objects to copy with S3 Batch Operations.
- [Using a CSV manifest to copy objects across AWS accounts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/specify-batchjob-manifest-xaccount-csv.html): Learn how to use a CSV manifest that's stored in the source account to copy objects across AWS accounts with S3 Batch Operations.
- [Using Batch Operations to encrypt objects with S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-copy-example-bucket-key.html): Use the S3 Batch Operations Copy operation to apply S3 Bucket Keys to objects in a bucket in Amazon S3.
- [Compute checksums](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-compute-checksums.html): Using S3 Batch Operations Compute checksum to calculate checksum values.
- [Delete all object tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-delete-object-tagging.html): Learn how to use S3 Batch Operations to delete object tags in Amazon S3.
- [Invoke AWS Lambda function](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-invoke-lambda.html): Using S3 Batch Operations to invoke a Lambda function.
- [Replace all object tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-put-object-tagging.html): Learn how to use Amazon S3 Batch Operations to replace object tags.
- [Replace access control list (ACL)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-put-object-acl.html): Using S3 Batch Operations to set object access control lists (ACLs) in Amazon S3.
- [Restore objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-initiate-restore-object.html): Use Amazon S3 Batch Operations to restore archived objects in Amazon S3.

### [Update object encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-update-encryption.html)

Learn how to use Amazon S3 Batch Operations to update object encryption.

- [Creating a Batch Operations job to update object encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-update.html): Create an Amazon S3 Batch Operations job to update object encryption.
- [Object Lock retention](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-retention-date.html): Using S3 Batch Operations for retention dates.
- [Object Lock legal hold](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-legal-hold.html): Use S3 Batch Operations to place or remove a legal hold on many Amazon S3 objects at the same time.

### [Managing jobs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-managing-jobs.html)

Learn how to manage Amazon S3 Batch Operations jobs.

- [Listing jobs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-list-jobs.html): Retrieve a list of S3 Batch Operations jobs.
- [Viewing job details](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-details.html): View details of your S3 Batch Operations jobs.
- [Assigning job priority](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-priority.html): Assign a numeric priority to your S3 Batch Operations jobs.

### [Tracking job status and completion reports](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-status.html)

Track S3 Batch Operations job status and reports.

- [Examples of tracking using Amazon EventBridge](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-examples-event-bridge-cloud-trail.html): Manage and view S3 Batch Operations events using Amazon EventBridge.
- [Examples of completion reports](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-examples-reports.html): Contains examples of S3 Batch Operations completion reports for jobs that have completed, failed, or been canceled.

### [Using tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags.html)

Controlling access and labeling using tags for S3 Batch Operations jobs.

- [Creating a job](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-tags-create.html): Create an Amazon S3 Batch Operations job with job tags used for labeling.
- [Deleting tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-job-tags.html): Delete the tags from an Amazon S3 Batch Operations job.
- [Putting job tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/put-job-tags.html): Add job tags to an existing Amazon S3 Batch Operations job.
- [Getting job tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/get-job-tags.html): Retrieve the tags of an Amazon S3 Batch Operations job.
- [Controlling permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags-examples.html): Examples of using job tags in policies to control access to your S3 Batch Operations jobs.

### [Managing Object Lock with Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/managing-object-lock-batchops.html)

Manage Amazon S3 Object Lock with Batch Operations.

- [Enabling Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-object-lock.html): Enable Amazon S3 Object Lock by using S3 Batch Operations.
- [Setting retention](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-object-lock-retention.html): Set Amazon Object Lock retention by using Batch Operations.
- [Setting retention compliance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-compliance-mode.html): Use Amazon S3 Batch Operations to set S3 Object Lock retention compliance mode.
- [Setting retention governance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-governance-mode.html): Use Amazon S3 Batch Operations to apply S3 Object Lock retention governance mode.
- [Turning off legal hold](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-legal-hold-off.html): Use Amazon S3 Batch Operations to turn off S3 Object Lock legal holds.
- [Tutorial: Batch-transcoding videos](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorial-s3-batchops-lambda-mediaconvert-video.html): Walk through an example of how to configure S3 Batch Operations to invoke an AWS Lambda function for batch-transcoding of videos stored in Amazon S3 through AWS Elemental MediaConvert.
- [Troubleshooting S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshooting-batch-operations.html): This section provides troubleshooting guidance for common issues with Amazon S3 Batch Operations.

### [Querying data in place](https://docs.aws.amazon.com/AmazonS3/latest/userguide/selecting-content-from-objects.html)

Run a specified SQL expression against an object in Amazon S3, and return query results in response.

- [S3 Select examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-select.html)

### [SQL Reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference.html)

SQL reference for Amazon S3 Select

- [SELECT command](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-select.html): Overview of the SELECT SQL command supported by Amazon S3 Select.
- [Data types](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-data-types.html): Overview of the data types supported by Amazon S3 Select.
- [Operators](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-operators.html): Overview of the operators supported by Amazon S3 Select.
- [Reserved keywords](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-keyword-list.html)

### [SQL functions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-sql-functions.html)

Overview of the SQL functions supported by Amazon S3 Select.

- [Aggregate functions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-aggregate.html)
- [Conditional functions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-conditional.html)
- [Conversion functions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-conversion.html)
- [Date functions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-date.html)
- [String functions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-string.html)


## [Working with directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html)

### [Use cases for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-use-cases.html)

Directory buckets support bucket creation in the following bucket location types: Availability Zone or Local Zone.

### [High performance workloads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-high-performance.html)

Amazon S3 Express One Zone, a high-performance, single-zone Amazon S3 storage class that is purpose-built to deliver consistent, single-digit millisecond data access for your most latency-sensitive applications.

### [Tutorial: Getting started with S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-getting-started.html)

Learn how to get started working with the Amazon S3 Express One Zone storage class and directory buckets.

- [Configure a VPC endpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-tutorial-endpoints.html): Configure a gateway VPC endpoint to access S3 Express One Zone directory buckets and objects without traversing a NAT Gateway, improving network efficiency and reducing costs.
- [Create a directory bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-tutorial-create-directory-bucket.html): Learn how to create a directory bucket in Amazon S3 using the AWS Management Console.
- [Importing data into a directory bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-tutorial-Import.html): Learn how to import objects from a general purpose bucket into an S3 Express One Zone directory bucket using the Import action in the S3 console.
- [Upload objects to a directory bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-tutorial-Upload.html): Learn how to manually upload objects to an S3 Express One Zone directory bucket using the AWS Management Console, including steps for selecting regions, choosing checksums, and adding metadata.
- [Empty a directory bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-tutoiral-Empty.html): Learn how to empty an S3 Express One Zone directory bucket using the Amazon S3 console.
- [Deleting a directory bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-tutoiral-Delete.html): Learn how to delete an S3 Express One Zone directory bucket using the AWS Management Console after emptying the bucket and stopping multipart uploads.
- [S3 Express One Zone Availability Zones and Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Endpoints.html): Learn about the Amazon S3 Express One Zone storage class Regions and Availability Zones.
- [Networking for directory buckets in an Availability Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-az-networking.html): Using Regional and Zonal API endpoints to access objects in directory buckets in an Availability Zone.
- [Creating directory buckets in an Availability Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-create.html): Learn how to create a directory bucket so that you can store objects in the Amazon S3 Express One Zone storage class.
- [Regional and Zonal endpoints for directory buckets in an Availability Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html): A list of Regional and Zonal endpoints for directory buckets in an Availability Zone.

### [Optimizing S3 Express One Zone performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-performance.html)

optimizing performance for S3 Express One Zone

- [Optimizing S3 Express One Zone performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-optimizing-performance-design-patterns.html): Learn about best practices and design patterns to optimize performance for the Amazon S3 Express One Zone storage class.

### [Data residency workloads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-data-residency.html)

S3 in AWS Local Zone supports storing data in a specific data perimeter to meet data residency and isolation requirements.

- [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html): The topic explains concepts for directory buckets in Local Zones, detailing connectivity, key terms, and endpoint routing for directory buckets.
- [Enable accounts for Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/opt-in-directory-bucket-lz.html): The topic describes how to enable accounts for Local Zones so you can create or access directory buckets in Local Zones.
- [Private connectivity from your VPC](https://docs.aws.amazon.com/AmazonS3/latest/userguide/connectivity-lz-directory-buckets.html): The topic describes configuring gateway VPC endpoints between your VPC and S3 in Local Zones.
- [Creating a directory bucket in a Local Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-directory-bucket-LZ.html): The topic describes how to create a directory bucket in a Local Zone.
- [Authenticating and authorizing for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/iam-directory-bucket-LZ.html): This topic describes how to authenticate and authorize for directory bucket in a Local Zone.
- [Differences for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-differences.html): Notable differences for directory buckets
- [Networking for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-networking.html): Using Regional and Zonal API endpoints to access objects in directory buckets.
- [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html): Use the directory bucket naming rules when you create a directory bucket in Amazon S3.
- [Viewing properties](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-view.html): Learn how to view the properties for an Amazon S3 directory bucket.
- [Managing bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-bucket-policy.html): Learn how to work with bucket policies for Amazon S3 directory buckets by using the Amazon S3 console and the AWS SDKs.
- [Emptying a directory bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-empty.html): Learn how to empty an Amazon S3 directory bucket.
- [Deleting a directory bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-delete.html): Learn how to delete an Amazon S3 directory bucket.
- [Listing directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-ListExamples.html): Use AWS SDK and CLI examples to list Amazon S3 directory buckets.
- [Determining whether you can access a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-HeadExamples.html): See AWS SDK examples of using the HeadBucket API operation with Amazon S3 directory buckets.

### [Working with objects in a directory bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects.html)

Learn how to upload, copy, delete, and manage objects in an Amazon S3 directory bucket.

- [Importing objects into a directory bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job.html): Learn how to import objects from an Amazon S3 general purpose bucket into an Amazon S3 directory bucket.

### [Working with S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-lifecycle.html)

Create a lifecycle configuration for objects in directory buckets.

- [Creating and managing a Lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-create-lc.html): You can create a lifecycle configuration for directory buckets by using the AWS Command Line Interface (AWS CLI), AWS SDKs and REST APIs.
- [Troubleshooting S3 Lifecycle for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-lifecycle-troubleshooting.html): The following information can help you troubleshoot common issues with Amazon S3 Lifecycle for directory buckets.
- [Using Batch Operations with S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops.html): Perform large-scale batch operations on objects stored in the Amazon S3 Express One Zone storage class.
- [Appending data to objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-append.html): Learn how to add data to existing objects in directory buckets.
- [Renaming an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-rename.html): Learn how to rename an object in a directory bucket.

### [Uploading an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-upload.html)

Learn how to upload objects to an Amazon S3 directory bucket.

- [Using multipart uploads with directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-using-multipart-upload.html): Learn how to use the multipart upload process to upload large objects to your Amazon S3 directory buckets.
- [Copying an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-copy.html): Learn how to copy objects to an Amazon S3 directory bucket.
- [Deleting an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-delete-object.html): Learn how to delete an object in an Amazon S3 directory bucket.
- [Downloading an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-GetExamples.html): See examples of how to use the GetObject API operation to download (retrieve) objects from an Amazon S3 directory bucket.
- [Generating presigned URLs to share objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-generate-presigned-url-Examples.html): See examples of how to generate presigned URLs to share objects from an Amazon S3 directory bucket.
- [Retrieving object metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-HeadObjectExamples.html): See examples of using the HeadObject and GetObjectAttributes API operation with Amazon S3 directory buckets.
- [Listing objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-listobjectsExamples.html): See examples of how to use the ListObjectsV2 API operation to list objects from an Amazon S3 directory bucket.

### [Security for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security.html)

Learn about the shared responsibility model for security when working with AWS services and directory buckets.

### [Data protection and encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-data-protection.html)

Learn about data protection and encryption for directory buckets.

- [Setting and monitoring bucket default encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html): Describes Amazon S3 bucket default encryption and how to use it.

### [SSE-KMS in directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-UsingKMSEncryption.html)

Use server-side encryption so that Amazon S3 directory buckets manages encryption and decryption for you.

- [Specifying SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-specifying-kms-encryption.html): Learn how to add server-side encryption with AWS Key Management Service (AWS KMS) keys to an Amazon S3 object in a directory bucket.

### [Authenticating and authorizing requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-authenticating-authorizing.html)

Learn about the authenticating and authorizing requests when working with directory buckets

### [Authorizing Regional endpoint API operations with IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html)

Learn how to use AWS Identity and Access Management (IAM) to control access to Regional endpoint API operations; for Amazon S3 directory buckets.

- [Identity-based policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-identity-policies.html): See examples of AWS Identity and Access Management (IAM) identity-based policies for use with the Amazon S3 Express One Zone storage class.
- [Bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-example-bucket-policies.html): See example directory bucket policies
- [Authorizing Zonal endpoint API operations with CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-create-session.html): Learn how to authenticate and authorize Zonal endpoint API operations through a session-based mechanism for the lowest latency.
- [Security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-best-practices.html): Learn about security best practices for using the Amazon S3 Express One Zone storage class.

### [Working with access points for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html)

Simplify managing data access at scale for directory buckets by creating and using access points for directory buckets.

- [Naming rules, restrictions, and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-restrictions-limitations-naming-rules.html): Learn about access points for directory buckets restrictions and limitations.
- [Referencing access points for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-naming.html): Referencing access points for directory buckets with access point names, access point aliases, or virtual-hostedâstyle URIs based on use cases.
- [Access points object operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-service-api-support.html): Access directory bucket objects and monitor requests with access points for directory buckets, using a compatible subset of S3 operations and other AWS services.
- [Configuring IAM policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-policies.html): Configure IAM policies to use access points for directory buckets.
- [Monitoring and logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-monitoring-logging.html): Monitor S3 access points for directory buckets using Amazon CloudWatch request metrics or Amazon S3 server access logs and AWS CloudTrail.
- [Creating access points for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points-directory-buckets.html): Create up to 10,000 access points to simplify managing data access at scale for directory buckets in Amazon S3.

### [Managing access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-manage.html)

Managing your access points for directory buckets by modifying scope, editing polices, viewing details, or deleting.

- [List your access points for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-list.html): This section explains how to list access points for a directory bucket using the AWS Management Console, AWS Command Line Interface (AWS CLI), REST API, or AWS SDKs.
- [View details for your access points for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-details.html): This section explains how to view details for your access point for directory buckets using the AWS Management Console, AWS CLI, AWS SDKs, or REST API.
- [Viewing, editing or deleting access point policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-policy.html): You can use an AWS Identity and Access Management (IAM) access point policy to control the principal and resource that can access the access point.
- [Manage the scope of your access points for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-manage-scope.html): This section explains how to view and modify the scope of your access points for directory buckets using the AWS Command Line Interface, REST API, or AWS SDKs.
- [Delete your access point for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-delete.html): This section explains how to delete your access point using the AWS Management Console, AWS Command Line Interface, REST API, or AWS SDKs.

### [Tagging Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-db-tagging.html)

Learn how to tag and untag access points for directory buckets and manage tagged access points for directory buckets.

- [Creating access points for directory buckets with tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-db-create-tag.html): Learn how to create an access point for directory buckets with tags and store objects in the Amazon S3 Express One Zone storage class.
- [Adding a tag to an access point for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-db-tag-add.html): Learn how to add a tag to an existing access point for directory bucket.
- [Viewing the tags of an access point for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-db-tag-view.html): Learn how to view the tags of an existing access point for directory buckets.
- [Deleting a tag from an access point for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-db-tag-delete.html): Learn how to delete a tag from an existing access point for directory buckets.

### [Logging with AWS CloudTrail for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-one-zone-logging.html)

Learn about logging with AWS CloudTrail for S3 Express One Zone.

- [](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-log-files.html): View CloudTrail event log file examples for directory buckets
- [Optimizing directory bucket performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-optimizing-performance.html): Learn about best practices and design patterns to optimize performance for directory buckets.

### [Developing with directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-developing.html)

Learn how to develop with the Amazon S3 Express One Zone storage class and directory buckets.

- [Regional and Zonal endpoints for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Regions-and-Zones.html): Learn about the Regional and Zonal endpoints for working with Amazon S3 Express One Zone storage class and directory buckets.
- [Working with directory buckets by using the S3 console, AWS CLI, and AWS SDKs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-SDKs.html): Learn which how to work with S3 Express One Zone by using the S3 console, AWS CLI, and AWS SDKs.
- [Directory bucket API operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-APIs.html): Learn which Amazon S3 API operations are supported for use with the Amazon S3 Express One Zone storage class.

### [Tagging directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html)

Learn how to tag and untag an Amazon S3 directory bucket, and manage tagged directory buckets.

- [Creating directory buckets with tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-create-tag.html): Learn how to create a directory bucket with tags and store objects in the Amazon S3 Express One Zone storage class.
- [Adding a tag to a directory bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-tag-add.html): Learn how to add a tag to an existing directory bucket.
- [Viewing directory bucket tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-tag-view.html): Learn how to view the tags of an existing directory bucket.
- [Deleting a tag from a directory bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-tag-delete.html): Learn how to delete a tag from an existing directory bucket.
- [Resilience testing](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-fis.html): Learn how to test the resilience of your applications that use Amazon S3 Express One Zone storage class with AWS Fault Injection Service.


## [Working with Amazon S3 Tables and table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html)

- [Tutorial: Getting started with S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-getting-started.html): Learn how to get started working with S3 Tables.

### [Table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html)

Learn about Amazon S3 buckets designed for storing and managing tables.

- [Table bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-naming.html): Use the table bucket naming rules to create table buckets and name tables and namespaces in Amazon S3 Tables.
- [Create a table bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-create.html): Learn how to create an Amazon S3 table bucket to store your tabular data by using the Amazon S3 console or AWS Command Line Interface (AWS CLI).
- [Delete a table bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-delete.html): Delete a table bucket.
- [Viewing table bucket details](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-details.html): Get details about an Amazon S3 table bucket.
- [Managing policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html): Learn how to add, delete, update, or view policies on your table buckets.
- [AWS managed table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-aws-managed-buckets.html): Learn about the differences between Amazon S3 AWS managed table buckets and customer-managed table buckets.

### [Tagging table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/table-bucket-tagging.html)

Learn how to tag and untag an Amazon S3 table bucket, and manage tagged table buckets.

- [Creating table buckets with tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/table-bucket-create-tag.html): Learn how to create an Amazon S3 table bucket with tags.
- [Adding a tag to a table bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/table-bucket-tag-add.html): Learn how to add a tag to an existing Amazon S3 table bucket.
- [Viewing table bucket tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/table-bucket-tag-view.html): Learn how to view the tags of an existing Amazon S3 table bucket.
- [Deleting a tag from a table bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/table-bucket-tag-delete.html): Learn how to delete a tag from an existing Amazon S3 table bucket.

### [S3 Tables maintenance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance-overview.html)

Use best practices for maintaining table buckets such as compaction, snapshot management, and unreferenced file removal.

- [S3 Tables maintenance job status](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance-status.html): S3 Tables maintenance jobs run periodically for your S3 tables or table buckets.
- [Table bucket maintenance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html): Use best practices for maintaining table buckets such with unreferenced file removal
- [Table maintenance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html): Use best practices for maintaining S3 tables such as compaction, snapshot management, and unreferenced file removal
- [Record expiration for tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-record-expiration.html): Use best practices for configuring automatic expiration and removal of records in S3 Tables.
- [Considerations and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-considerations.html): Considerations and limitations for S3 Tables, a storage solution purpose-built for tables and optimized for large-scale analytic workloads.
- [S3 Tables Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tables-intelligent-tiering.html): Automatically optimize storage costs for S3 Tables by using S3 Intelligent-Tiering, which moves data to cost-effective access tiers based on access patterns without retrieval fees or performance impact.

### [Namespaces](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace.html)

Learn about table namespaces in Amazon S3, how to organize tables logically, and understand namespace limitations and characteristics for effective table management.

- [Create a namespace](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-create.html): Learn how to create a namespace for grouping tables in Amazon S3 by using the console, AWS Command Line Interface (AWS CLI), or integrated query engines.
- [Delete a namespace](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-delete.html): Learn how to delete a table namespace in Amazon S3, including required permissions and an AWS Command Line Interface (AWS CLI) example.

### [Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html)

Learn about table resources in Amazon S3 table buckets.

- [Create a table](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-create.html): Learn how to create an Amazon S3 table in Apache Iceberg format by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), or query engines like Apache Spark.
- [Delete a table](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-delete.html): Learn how to delete Amazon S3 tables.
- [Viewing table details](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-table-details.html): Get details about an Amazon S3 table.
- [Managing policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-table-policy.html): Learn how to add, delete, or view policies for your tables.

### [Tagging tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/table-tagging.html)

Learn how to tag and untag an Amazon S3 table, and manage tagged tables.

- [Creating tables with tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/table-create-tag.html): Learn how to create an Amazon S3 table with tags.
- [Adding a tag to a table](https://docs.aws.amazon.com/AmazonS3/latest/userguide/table-tag-add.html): Learn how to add a tag to an existing Amazon S3table.
- [Viewing table tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/table-tag-view.html): Learn how to view the tags of an existing Amazon S3 table.
- [Deleting a tag from a table](https://docs.aws.amazon.com/AmazonS3/latest/userguide/table-tag-delete.html): Learn how to delete a tag from an existing Amazon S3 table.

### [Accessing tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-access.html)

Learn about different access methods for S3 tables

### [S3 Tables integration overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integration-overview.html)

Learn how Amazon S3 Tables integrates with AWS analytics services through AWS Glue Data Catalog and AWS Lake Formation.

- [Integrating S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html): Learn the prerequisites and step-by-step procedures to integrate Amazon S3 Tables with AWS analytics services and grant the necessary permissions for access.
- [Accessing tables using the AWS GlueÂ Iceberg REST endpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-glue-endpoint.html): Access S3 tables using the AWS GlueÂ Iceberg REST endpoint
- [Accessing tables using the Amazon S3 TablesÂ Iceberg REST endpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-open-source.html): Learn how you can access S3 tables directly using the Amazon S3 TablesÂ Iceberg REST endpoint
- [Accessing tables with the client catalog](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-client-catalog.html): Learn about how you can access S3 tables with the Amazon S3 Tables Catalog for Apache Iceberg
- [Amazon Athena](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-athena.html): Learn how to query Amazon S3 tables using Amazon Athena, an interactive SQL query service.
- [Amazon Redshift](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-redshift.html): Learn about how you can access tables with Amazon Redshift
- [Amazon EMR](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-emr.html): Learn about how you can access tables with Amazon EMR.
- [Quick](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-quicksight.html): Learn about how you can access tables with Quick
- [Amazon Data Firehose](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-firehose.html): Learn about how you can access tables with Firehose
- [AWS Glue ETL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-glue.html): Learn about how you can run ETL jobs on S3 tables with AWS Glue
- [Querying S3 Tables with SageMaker Unified Studio](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-sagemaker.html): Learn how to query and analyze S3 Tables using Amazon SageMaker Unified Studio through the Amazon S3 console.
- [Working with Apache Iceberg V3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/working-with-apache-iceberg-v3.html): Learn about working with Apache Iceberg V3

### [Replicating S3 tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-replication-tables.html)

Learn about S3 Tables replication.

- [How S3 Tables replication works](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-replication-how-replication-works.html): Learn how S3 Tables replication creates and maintains queryable copies of your Apache Iceberg tables across Regions and accounts.
- [Setting up S3 Tables replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-replication-setting-up.html): Learn how to configure and set up S3 Tables replication for your S3 Tables.
- [Managing S3 Tables replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-replication-managing.html): Learn how to monitor and manage S3 Tables replication for your S3 Tables.
- [AWS Regions, endpoints, and quotas](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-regions-quotas.html): Learn about the supported AWS Regions and service quotas for S3 Tables
- [Making requests over IPv6](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-ipv6.html): Learn how to access Amazon S3 Tables using IPv6 dual-stack endpoints.

### [Security for S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-security-overview.html)

Learn about supported security features and tools for S3 Tables.

### [Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-encryption.html)

Learn about option for encrypting your tables.

### [SSE-KMS in table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-encryption.html)

Learn about encrypting your tables with AWS KMS.

- [Enforcing SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tables-require-kms.html): You can use S3 Tables resource-based policies, KMS key policies, IAM identity-based policies, or any combination of these, to enforce the use of SSE-KMS for S3 tables and table buckets.
- [SSE-KMS permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html): Learn how to create permissions policies for using SSE-KMS with S3 tables and table buckets.
- [Specifying SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-specify.html): Learn how to encrypt your tables and table buckets with AWS KMS.

### [Access management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.html)

Learn about identity and access management for Amazon S3 Tables.

- [IAM identity-based policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-identity-based-policies.html): Learn about using IAM identity-based permissions policies to control access to your S3 Tables tables and table buckets.
- [Resource-based policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-resource-based-policies.html): Learn about using resource-based permissions policies to control access to your S3 Tables tables and table buckets.
- [AWS managed policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-security-iam-awsmanpol.html): Learn about AWS managed policies for S3 Tables and recent changes to those policies.
- [Granting access with SQL semantics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-sql.html): Use SQL semantics to grant access to table-level APIs in table policies or table bucket policies.
- [Managing access with Lake Formation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-permissions-tables.html): After your table buckets are integrated with the AWS analytics services, Lake Formation manages access to your tables and requires that each IAM principal (user or role) be authorized to perform actions them.
- [VPC connectivity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-VPC.html): Learn how to use VPC endpoints for Amazon S3 Tables.
- [Restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-restrictions.html): Learn about the security features and functionality that are restricted or unsupported for S3 Tables.

### [Logging and monitoring](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-monitoring-overview.html)

Use best practices for gaining insights into the availability and performance of your tables and table buckets.

### [Logging with AWS CloudTrail for S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-logging.html)

Learn about logging with AWS CloudTrail for S3 Tables

- [CloudTrail log examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-log-files.html): View AWS CloudTrail data event log file examples for S3 Tables.

### [Monitoring metrics with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-cloudwatch-metrics.html)

Use CloudWatch metrics to monitor the performance of your table buckets

- [Metrics and dimensions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-metrics-dimensions.html): Discover the metrics and dimensions available for tables and table buckets in CloudWatch
- [Accessing CloudWatch metrics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-accessing-cloudwatch-metrics.html): Learn how to access S3 Tables metrics using the console, AWS CLI, or CloudWatch API
- [Managing CloudWatch metrics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-managing-cloudwatch-metrics.html): Learn how to enable and disable request metrics for S3 Tables


## [Working with S3 Vectors and vector buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors.html)

- [Tutorial: Getting started with S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-getting-started.html): In this tutorial, you create an S3 vector bucket and a vector index in an AWS Region in the Amazon S3 console.

### [Vector buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-buckets.html)

Learn about Amazon S3 buckets designed for storing and managing vector records.

- [Vector bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-buckets-naming.html): Use the vector bucket naming rules to create vector buckets.
- [Creating a vector bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-buckets-create.html): Learn how to create an Amazon S3 vector bucket to store your data by using the Amazon S3 console or AWS Command Line Interface (AWS CLI).
- [Listing vector buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-buckets-list.html): View all your S3 vector buckets using the Amazon S3 console or the AWS CLI.
- [Viewing vector bucket attributes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-buckets-details.html): Learn how to view detailed information about vector buckets, including properties, encryption settings, and creation details using the AWS CLI.
- [Deleting a vector bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-buckets-delete.html): Delete a vector bucket.
- [Managing vector bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-bucket-policy.html): Learn how to add, delete, update, or view policies on your vector buckets.

### [Tagging vector buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-tags.html)

Learn about using tags with Amazon S3 vector buckets.

### [Managing tags for vector buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/managing-tags-vector-buckets.html)

You can add or manage tags for S3 vector buckets using the Amazon S3 Console, the AWS Command Line Interface (AWS CLI), the AWS SDKs, or using the S3 APIs: TagResource, UntagResource, and ListTagsForResource.

- [Creating vector buckets with tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-vector-buckets-with-tags.html): Learn how to create S3 vector buckets with tags.
- [Adding a tag to a vector bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/adding-tag-vector-bucket.html): Learn how to add tags to S3 vector buckets.
- [Viewing vector bucket tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/viewing-vector-bucket-tags.html): Learn how to view tags that are applied to S3 vector buckets.
- [Deleting a tag from a vector bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/deleting-tag-vector-bucket.html): Learn how to delete tags from S3 vector buckets.

### [Vector indexes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-indexes.html)

- [Creating a vector index in a vector bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-create-index.html)
- [Listing vector indexes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-index-list.html): You can view all vector indexes within a vector bucket.
- [Deleting a vector index](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-index-delete.html): You can delete a vector index when you no longer need it.

### [Tagging vector indexes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/vector-index-tagging.html)

Learn about using tags with Amazon S3 vector indexes.

### [Managing tags for vector indexes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/managing-tags-vector-indexes.html)

You can add or manage tags for S3 vector indexes using the Amazon S3 Console, the AWS Command Line Interface (AWS CLI), the AWS SDKs, or using the S3 APIs: TagResource, UntagResource, and ListTagsForResource.

- [Creating vector indexes with tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-vector-indexes-with-tags.html): Learn how to create S3 vector indexes with tags.
- [Adding a tag to a vector index](https://docs.aws.amazon.com/AmazonS3/latest/userguide/adding-tag-vector-index.html): Learn how to add tags to S3 vector indexes.
- [Viewing vector index tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/viewing-vector-index-tags.html): Learn how to view tags that are applied to S3 vector indexes.
- [Deleting a tag from a vector index](https://docs.aws.amazon.com/AmazonS3/latest/userguide/deleting-tag-vector-index.html): Learn how to delete tags from S3 vector indexes.

### [Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-vectors.html)

Each vector consists of a key, which uniquely identifies each vector in a vector index.

- [Inserting vectors into a vector index](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-index-create.html): Learn how to insert vectors into a vector index using the AWS CLI.
- [Listing vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-list.html): Learn how to list vectors in a vector bucket by using the AWS Command Line Interface (AWS CLI), or AWS SDKs.
- [Querying vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-query.html): You can run a similarity query with the QueryVectors API operation, where you specify the query vector, the number of relevant results to return (the top K nearest neighbors), and the index ARN.
- [Deleting vectors from a vector index](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-delete.html): You can delete specific vectors from a vector index by specifying their vector keys using the DeleteVectors API.
- [Metadata filtering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-metadata-filtering.html): Learn how to use metadata filtering to narrow down query results based on specific attributes attached to your vectors.
- [Limitations and restrictions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-limitations.html): Service limitations and restrictions for Amazon S3 Vectors.
- [S3 Vectors best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-best-practices.html): Learn about guidelines and best practices for S3 Vectors.
- [Creating and searching vector embeddings with s3vectors-embed-cli](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-cli.html): Learn how to use the S3 Vectors CLI to generate embeddings and perform semantic searches with Amazon Bedrock foundation models.

### [Using S3 Vectors with other AWS services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-integration.html)

S3 Vectors integrates with other AWS services to enhance your vector processing capabilities and provide comprehensive solutions for AI and machine learning workloads.

- [Using S3 Vectors with OpenSearch Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-opensearch.html): Amazon S3 Vectors integrates with OpenSearch to provide flexible vector storage and search capabilities.
- [Using S3 Vectors with Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-bedrock-kb.html): S3 Vectors integrates with Amazon Bedrock Knowledge Bases and Amazon SageMaker AI Unified Studio to simplify and reduce the cost of vector storage for retrieval augmented generation (RAG) applications.
- [AWS Regions, endpoints, and quotas for S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-regions-quotas.html): Information about supported AWS Regions, endpoints, and service quotas for S3 Vectors.

### [Security in S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-security.html)

Learn about security features and best practices for protecting your vector data in S3 Vectors.

### [Identity and Access management in S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-access-management.html)

Learn how to manage access to S3 Vectors resources using IAM policies and resource-based policies.

- [S3 Vectors identity-based policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-iam-policies.html): Learn how to use IAM identity-based policies to control access to S3 Vectors resources.
- [S3 Vectors resource-based policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-resource-based-policies.html): Resource-based policies are attached to a resource.

### [Data protection and encryption in S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-data-encryption.html)

Learn about data protection and encryption options for S3 Vectors, including server-side encryption with Amazon S3 managed keys (SSE-S3) and AWS KMS keys (SSE-KMS).

- [Setting encryption in S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-sectting-encryption.html): This topic explains how to set the encryption configuration for your S3 vector buckets and indexes.
- [Viewing encryption configuration in S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-viewing-encryption.html): Learn how to view encryption settings for your vector bucket.
- [VPC endpoints for S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-privatelink.html): Learn how to use AWS PrivateLink to access S3 Vectors privately from your VPC without using the internet.

### [Logging with AWS CloudTrail for S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-logging.html)

Amazon S3 Vectors is integrated with AWS CloudTrail, a service that provides a record of actions that are taken by a user, role, or an AWS service.

- [CloudTrail log file example for S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-cloudtrail-log-example.html): Examples of CloudTrail log entries for S3 Vectors data events.


## [Access control](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-management.html)

### [Identity and Access Management (IAM)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your Amazon S3 resources.

- [How Amazon S3 works with IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon S3, learn what IAM features are available to use with Amazon S3.

### [Request authorization](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-s3-evaluates-access-control.html)

How Amazon S3 evaluates access control to authorize requests.

- [For a bucket operation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-auth-workflow-bucket-operation.html): How Amazon S3 evaluates access control to authorize requests for bucket operations.
- [For an object operation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-auth-workflow-object-operation.html): How Amazon S3 evaluates access control to authorize requests for object operations.
- [Required permissions for S3 API operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html): How to specify permissions of Amazon S3 actions in a policy for Amazon S3 API operations
- [Policies and permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html): Learn about the AWS Identity and Access Management (IAM) policies and permissions that are available in Amazon S3.

### [Bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html)

Learn what Amazon S3 bucket policies are and when to use them.

- [Adding a bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html): Add a bucket policy to an Amazon S3 bucket to grant other AWS accounts or AWS Identity and Access Management (IAM) users access to the bucket.
- [Controlling VPC access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.html): An example of bucket policies for Amazon VPC endpoints for Amazon S3.
- [Bucket policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html): See examples of typical use cases for Amazon S3 bucket policies.
- [Condition key examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html): You can use access policy language to specify conditions when you grant permissions.

### [Identity-based policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security_iam_id-based-policy-examples.html)

By default, users and roles don't have permission to create or modify Amazon S3 resources.

- [Controlling bucket access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/walkthrough1.html): Use user permissions to control access to your bucket.
- [Identity-based policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html): Examples of AWS Identity and Access Management (IAM) identity-based policies for controlling access to Amazon S3.

### [Walkthroughs using policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access.html)

Console examples for managing access to Amazon S3 buckets and objects.

- [Setting up tools](https://docs.aws.amazon.com/AmazonS3/latest/userguide/policy-eval-walkthrough-download-awscli.html): Setting up for the Amazon S3 example walkthroughs.
- [Granting permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example1.html): Learn how an Amazon S3 bucket owner can grant users bucket permissions.
- [Granting cross-account permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.html): Learn how an Amazon S3 bucket owner can grant users cross-account bucket permissions.
- [Granting object permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example3.html): Learn how to granting users permissions to objects that the Amazon S3 bucket owner doesn't own.
- [Granting cross-account object permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example4.html): Learn how to grant cross-account permissions for objects that the Amazon S3 bucket owner doesn't own.
- [Using service-linked roles for Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give S3 Storage Lens access to resources to your AWS Organizations account.

### [Troubleshooting Amazon S3 identity and access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security_iam_troubleshoot.html)

Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon S3 and IAM.

- [Troubleshoot access denied (403 Forbidden) errors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshoot-403-errors.html): Learn how to troubleshoot access denied (HTTP 403 Forbidden) errors in Amazon S3.
- [AWS managed policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon S3 and recent changes to those policies.

### [Working with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html)

Simplify managing data access at scale for shared datasets by creating and using Amazon S3 access points.

- [Naming rules, restrictions, and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.html): Learn about Amazon S3 access points restrictions and limitations.
- [Referencing access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-naming.html): Referencing access points with ARNs, access point aliases, or virtual-hostedâstyle URIs based on use cases.
- [Access point compatibility](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-service-api-support.html): Access bucket objects and monitor requests with Amazon S3 access points, using a compatible subset of S3 operations and other AWS services.
- [Configuring IAM policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html): Configure IAM policies to use Amazon S3 access points.
- [Monitoring and logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-monitoring-logging.html): Monitor S3 access points using Amazon CloudWatch request metrics or Amazon S3 server access logs and AWS CloudTrail.

### [Creating an access point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html)

Create up to 10,000 access points to simplify managing data access at scale in Amazon S3.

- [Creating access points restricted to a VPC](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-vpc.html): Configuring Amazon S3 access points with a virtual private cloud (VPC)
- [Managing public access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-bpa-settings.html): Learn how to block public access to an S3 access point for a general purpose bucket.

### [Managing access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-manage.html)

Managing your Amazon S3 access points by editing polices, viewing details, or deleting.

- [List your access points for general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-list.html): This section explains how to list your access points for general purpose buckets using the AWS Management Console, AWS Command Line Interface, or REST API.
- [View details for your access point for general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-details.html): This section explains how to view details for your access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.
- [Delete your access point for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-delete.html): This section explains how to delete your access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.

### [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html)

Access bucket objects and monitor requests with Amazon S3 access points for general purpose buckets, using a compatible subset of S3 operations and other AWS services, such as AWS CloudTrail.

- [List objects through an access point for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/list-object-ap.html): This section explains how to list your objects through an access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.
- [Download an object through an access point for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/get-object-ap.html): This section explains how to download an object through an access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.
- [Configure access control lists (ACLs) through an access point for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/put-acl-permissions-ap.html): This section explains how to configure ACLs through an access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.
- [Upload an object through an access point for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/put-object-ap.html): This section explains how to upload an object through an access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.
- [Add a tag-set through an access point for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-tag-set-ap.html): This section explains how to add a tag-set through an access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.
- [Delete an object through an access point for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-object-ap.html): This section explains how to delete an object through an access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.

### [Tagging Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-tagging.html)

Learn how to tag and untag access points and manage tagged access points.

- [Creating access points with tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-create-tag.html): Learn how to create an access point with tags.
- [Adding a tag to an access point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-tag-add.html): Learn how to add a tag to an existing access point.
- [Viewing access point tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-tag-view.html): Learn how to view the tags of an existing access point.
- [Deleting a tag from an access point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-tag-delete.html): Learn how to delete a tag from an existing access point.

### [Managing access with S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants.html)

Manage access to your buckets and objects by using Amazon S3 Access Grants.

- [S3 Access Grants concepts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-concepts.html): Learn about Amazon S3 Access Grants concepts and how S3 Access Grants works.
- [S3 Access Grants and corporate directory identities](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-directory-ids.html): Learn how Amazon S3 Access Grants supports using corporate directory identities to grant access to your S3 data.
- [Getting started with S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-get-started.html): Learn how to get started with Amazon S3 Access Grants.

### [Working with S3 Access Grants instances](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance.html)

Learn how to create, view, delete, and update your S3 Access Grants instances.

- [Create an S3 Access Grants instance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance-create.html): Learn how to create an Amazon S3 Access Grants instance to manage access to your S3 data.
- [Get the details of an S3 Access Grants instance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance-view.html): Learn how to get the details of an Amazon S3 Access Grants instance.
- [List your S3 Access Grants instances](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance-list.html): Learn how to list your S3 Access Grants instances.
- [Associate or disassociate your IAM Identity Center instance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance-idc.html): Learn how to associate your Amazon S3 Access Grants instance with or dissociate it from an AWS IAM Identity Center instance.
- [Delete an S3 Access Grants instance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance-delete.html): Learn how to delete an Amazon S3 Access Grants instance.

### [Working with S3 Access Grants locations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location.html)

Learn how to register, get the details of, edit, and delete locations in S3 Access Grants

- [Register a location](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location-register.html): Learn how to register an Amazon S3 location path with an associated AWS Identity and Access Management (IAM) role, so that S3 Access Grants can assume this role to manage access to this location.
- [View the details of a registered location](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location-view.html): Learn how to view the details of a location that's registered in your Amazon S3 Access Grants instance.
- [Update a registered location](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location-edit.html): Learn how to update the AWS Identity and Access Management (IAM) role of a location that's registered in your Amazon S3 Access Grants instance.
- [Delete a registered location](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location-delete.html): Learn how to remove a registered location from your Amazon S3 Access Grants instance.

### [Working with grants in S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-grant.html)

Learn how to create, view, and delete an access grant in your Amazon S3 Access Grants instance.

- [Create grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-grant-create.html): Learn how to create an access grant in your Amazon S3 Access Grants instance.
- [View a grant](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-grant-view.html): Learn how to get the details of a grant from your Amazon S3 Access Grants instance.
- [Delete a grant](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-grant-delete.html): Learn how to delete a grant from your Amazon S3 Access Grants instance.

### [Getting S3 data using access grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-data.html)

Learn how to find access grants that were granted to you, request credentials from S3 Access Grants, use those credentials to access the S3 data, and which S3 operations are supported.

- [Request access to Amazon S3 data through S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-credentials.html): Learn how to get temporary access credentials from Amazon S3 Access Grants to access the Amazon S3 data that you have been granted access to.
- [Accessing S3 data using credentials vended by S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-get-data.html): Learn how to use the temporary credentials that you received from Amazon S3 Access Grants to get S3 data.
- [List the caller's access grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-list-grants.html): Learn how to find the access grants granted to you by a particular AWS account.
- [S3 Access Grants cross-account access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-cross-accounts.html): Learn about how to use Amazon S3 Access Grants to grant users in other AWS accounts access to your S3 Access Grants instance and S3 data.
- [Managing tags for S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-tagging.html): Learn how to add tags to or remove tags from Amazon S3 Access Grants resources, which include instances, locations, and grants.
- [S3 Access Grants limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-limitations.html): Learn about the quotas and limitations of Amazon S3 Access Grants.
- [S3 Access Grants integrations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-integrations.html): Learn about Amazon S3 Access Grants integrations available with other AWS services and from third parties.

### [Managing access with ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acls.html)

Manage access to your buckets and objects using ACLs to control permissions.

- [ACL overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html): Learn how to use access control lists (ACLs) to manage access to data in Amazon S3.
- [Configuring ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/managing-acls.html): Add grants to your resource ACL using the console, the REST API, or one of the AWS SDKs.
- [Policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies-condition-keys.html): Examples of policies for controlling access to Amazon S3 by using ACLs.

### [Blocking public access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

Learn how to use block public access with Amazon S3.

- [Configuring account settings](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-account.html)
- [Configuring bucket and access point settings](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-bucket.html): Amazon S3 Block Public Access provides settings for access points, buckets, organizations, and accounts to help you manage public access to Amazon S3 resources.
- [Reviewing bucket access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-analyzer.html): Use IAM Access Analyzer for S3 to review bucket access, including public buckets and buckets shared outside your AWS account.
- [Verifying bucket ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-owner-condition.html): Verify bucket owner for Amazon S3 operations.

### [Controlling object ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html)

Control ownership of new objects that are uploaded to your Amazon S3 bucket and disable access control lists (ACLs) for your bucket using S3 Object Ownership.

- [Prerequisites for disabling ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-migrating-acls-prerequisites.html): Prerequisites for applying the Bucket owner enforced setting for Object Ownership to disable access control lists (ACLs).
- [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-new-bucket.html): Apply the Bucket owner enforced setting for Object Ownership to disable access control lists (ACLs) when you create a bucket.
- [Setting Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-existing-bucket.html): Apply the Bucket owner enforced setting for Object Ownership to disable access control lists (ACLs) and take ownership of all the objects in your bucket.
- [Viewing Object Ownership settings](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-retrieving.html): Return the Object Ownership setting for a bucket.
- [Disabling ACLs for all new buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ensure-object-ownership.html): Disable access control lists (ACLs) for all newly created buckets.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-error-responses.html): Error responses for disabling access control lists (ACLs) with Object Ownership.


## [Security](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html)

- [Security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html): Learn about guidelines and best practices for addressing security issues in Amazon S3.
- [Data protection](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html): Keep your data protected through Amazon S3 with objects stored redundantly on multiple devices across multiple facilities.

### [Data encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html)

Use data encryption to provide added security for the data objects stored in your buckets.

### [Server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html)

Learn how to protect data by using server-side encryption in Amazon S3.

### [Setting default bucket encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html)

Describes Amazon S3 default bucket encryption and how to use it.

- [Configuring default encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html): Configure default encryption for an Amazon S3 bucket by using the S3 console, API, or AWS SDKs.
- [Monitoring default encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption-tracking.html)
- [Default encryption FAQ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html): Find answers to frequently asked questions about the new Amazon S3 feature that automatically encrypts all new object uploads.
- [Updating encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/update-sse-encryption.html): Learn how to update server-side encryption for existing Amazon S3 data.

### [Amazon S3 managed encryption keys (SSE-S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html)

With server-side encryption, Amazon S3 manages encryption and decryption for you.

- [Specifying SSE-S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-s3-encryption.html): How to add server-side encryption with Amazon S3 managed keys (SSE-S3) to an Amazon S3 object.

### [KMS keys stored in AWS KMS (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)

Use server-side encryption so that Amazon S3 manages encryption and decryption for you.

- [Specifying SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-kms-encryption.html): Learn how to add server-side encryption with AWS Key Management Service (AWS KMS) keys to an Amazon S3 object.

### [Using Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html)

Use S3 Bucket Keys to reduce the cost of server-side encryption requests when you're using AWS Key Management Service (AWS KMS) keys (SSE-KMS).

- [Configuring an S3 Bucket Key for your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-bucket-key.html): Configure a bucket to use an S3 Bucket Key for AWS KMS (SSE-KMS) on new objects.
- [Configuring an S3 Bucket Key for an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-bucket-key-object.html): Configure an S3 Bucket Key for an object by using Batch Operations, REST API, AWS SDKs, or AWS CLI.
- [Viewing the settings for an S3 Bucket Key](https://docs.aws.amazon.com/AmazonS3/latest/userguide/viewing-bucket-key-settings.html): View the setting for an S3 Bucket Key at the bucket or object level.

### [Dual-layer server-side encryption (DSSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingDSSEncryption.html)

Use dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys (DSSE-KMS) so that Amazon S3 manages encryption and decryption for you.

- [Specifying DSSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-dsse-encryption.html): Learn how to add dual-layer server-side encryption to an Amazon S3 object.

### [Customer-provided encryption keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html)

To use your own custom keys to encrypt the objects that you store on Amazon S3, use server-side encryption with customer-provided encryption keys (SSE-C).

- [Specifying SSE-C](https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-s3-c-encryption.html): How to add server-side encryption with customer-provided keys to an Amazon S3 object.
- [Blocking or unblocking SSE-C](https://docs.aws.amazon.com/AmazonS3/latest/userguide/blocking-unblocking-s3-c-encryption-gpb.html): How to block or unblock server-side encryption with customer-provided keys for a general purpose bucket.
- [Default SSE-C setting FAQ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-s3-c-encryption-setting-faq.html)
- [Using client-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingClientSideEncryption.html): Protect data in Amazon S3 by using client-side encryption.

### [Encryption for data in transit](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryptionInTransit.html)

Protect Amazon S3 data in transit by using TLS encryption, including post-quantum TLS.

### [Hybrid post-quantum TLS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryptionInTransit.PQ-TLS.html)

Protect Amazon S3 data in transit with quantum resistant cryptography by using the post-quantum key exchange option for TLS (PQ-TLS).

- [Configure PQ-TLS client](https://docs.aws.amazon.com/AmazonS3/latest/userguide/pqtls-how-to.html): To use PQ-TLS with Amazon S3, you need to configure your client to support post-quantum key exchange algorithms.

### [Internetwork traffic privacy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/inter-network-traffic-privacy.html)

Describes how Amazon S3 secures connections from the service to other locations.

- [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html): Connect to Amazon S3 by using AWS PrivateLink interface VPC endpoints in your virtual private cloud (VPC).
- [Compliance validation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/AmazonS3/latest/userguide/disaster-recovery-resiliency.html): Describes AWS architecture for data redundancy and specific Amazon S3 services for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/AmazonS3/latest/userguide/network-isolation.html): Describes how Amazon S3 isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/AmazonS3/latest/userguide/vulnerability-analysis-and-management.html): Describes the customer responsibility regarding updates and patches in Amazon S3.
- [Access management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-access-management.html): Amazon S3 provides a variety of access management tools.
- [Amazon S3 data inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-data-inventory.html): This chapter describes the data inventory for Amazon S3 to support functional equivalence requirements.


## [Data protection](https://docs.aws.amazon.com/AmazonS3/latest/userguide/data-protection.html)

### [Replicating objects within and across Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

Set up and configure replication to allow automatic, asynchronous copying of objects across Amazon S3 buckets.

- [What's replicated?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-what-is-isnot-replicated.html): Learn what is and what is not replicated during Amazon S3 replication.
- [Requirements and considerations for replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-requirements.html): Learn about the requirements for Amazon S3 replication.

### [Setting up live replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-how-setup.html)

Learn how to set up live replication for Amazon S3.

- [Replication configuration file](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-add-config.html): Learn about the elements of an Amazon S3 replication configuration file.
- [Setting up permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html): Learn how to create an AWS Identity and Access Management (IAM) role and set the necessary permissions for replication in Amazon S3.

### [Replication walkthroughs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-example-walkthroughs.html)

Learn how to set up live replication for various Same-Region Replication (SRR) and Cross-Region Replication (CRR) use cases in Amazon S3.

- [Configuring for buckets in the same account](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html): Set up replication in Amazon S3 where the source and destination buckets are owned by the same AWS account.

### [Configuring for buckets in different accounts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough-2.html)

Learn how to configure Amazon S3 replication when the source and destination buckets are owned by different AWS accounts.

- [Changing the replica owner](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-change-owner.html): Learn how to change the replica owner when the source and destination Amazon S3 buckets are owned by different accounts.
- [Using S3 Replication Time Control](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-time-control.html): Learn how to use Amazon S3 Replication Time Control (S3 RTC) to meet compliance requirements for replicating data.
- [Replicating encrypted objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-config-for-kms-objects.html): Learn how to replicate objects that have been encrypted by using server-side encryption in Amazon S3.
- [Replicating metadata changes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-for-metadata-changes.html): Learn how to replicate metadata changes such as tags, access control lists (ACLs), or Object Lock settings in Amazon S3.
- [Replicating delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-marker-replication.html): Learn how to replicate delete markers between Amazon S3 buckets.
- [Managing or pausing live replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/disable-replication.html): Learn how to pause replication or view, edit, enable, disable, or delete replication rules for an Amazon S3 bucket.

### [Replicating existing objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html)

Set up and configure on-demand S3 Batch Replication in Amazon S3 to replicate existing objects.

- [Configuring IAM role and policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-policies.html): Learn how to configure AWS Identity and Access Management (IAM) policies to use Amazon S3 Batch Replication.
- [Batch Replication for a first replication rule or new destination](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-new-config.html): Set up and configure on-demand replication in Amazon S3 by using Batch Operations.
- [Batch Replication for existing replication rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-existing-config.html): Set up and configure on-demand replication in Amazon S3 by using Batch Operations for existing objects.
- [Troubleshooting replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-troubleshoot.html): How to troubleshoot problems with replication for Amazon S3.

### [Monitoring progress and getting status](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-metrics.html)

Monitor Amazon S3 live replication and S3 Batch Replication with replication metrics, S3 Storage Lens metrics, S3 Event Notifications, and replication statuses.

- [Using S3 Replication metrics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/repl-metrics.html): Monitor the progress of replication with S3 Replication metrics by tracking bytes pending, operations pending, and replication latency.
- [Viewing replication metrics in S3 Storage Lens dashboards](https://docs.aws.amazon.com/AmazonS3/latest/userguide/viewing-replication-metrics-storage-lens.html): Learn how to view Amazon S3 Storage Lens replication metrics in your S3 Storage Lens dashboards.
- [Receiving replication failure events](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-metrics-events.html): View replication failure events and failure error codes.
- [Getting replication status](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-status.html): Learn how to find the replication status of an Amazon S3 object.

### [Managing multi-region traffic](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html)

Accelerate and manage multi-Region traffic with Multi-Region Access Points in Amazon S3.

### [Creating Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html)

Create a Multi-Region Access Point in Amazon S3 to provide a global endpoint that applications can use to fulfill requests from S3 buckets in multiple Regions.

- [Rules for naming Amazon S3 Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-naming.html): Follow these rules and conditions when naming your Amazon S3 Multi-Region Access Point.
- [Rules for choosing buckets for Amazon S3 Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-buckets.html): Follow these rules and conditions when choosing buckets for your Amazon S3 Multi-Region Access Point.
- [Create an Amazon S3 Multi-Region Access Point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-create-examples.html): Learn how to create an Amazon S3 Multi-Region Access Point.
- [Blocking public access with Amazon S3 Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-block-public-access.html): Learn how to block public access with Amazon S3 Multi-Region Access Points.
- [Viewing Amazon S3 Multi-Region Access Points configuration details](https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-view-examples.html): Learn how to view the configuration details for an Amazon S3 Multi-Region Access Point.
- [Deleting a Multi-Region Access Point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-delete-examples.html): Learn how to delete your Amazon S3 Multi-Region Access Point.

### [Configuring Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessConfiguration.html)

Configure Multi-Region Access Points in Amazon S3.

- [Configuring Multi-Region Access Point opt-in Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ConfiguringMrapOptInRegions.html): Configure Multi-Region Access Point opt-in Regions.
- [Configuring AWS PrivateLink](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointsPrivateLink.html): Configure AWS PrivateLink to work with a Multi-Region Access Point in Amazon S3.
- [Removing access to a Multi-Region Access Point from a VPC endpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RemovingMultiRegionAccessPointAccess.html): Remove access to an Amazon S3 Multi-Region Access Point from a VPC endpoint.

### [Using Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequests.html)

Send requests through a Multi-Region Access Point in Amazon S3.

- [Permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointPermissions.html): Manage access to Multi-Region Access Points by using permissions in Amazon S3.
- [Restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html): Learn about the restrictions and limitations for Multi-Region Access Points in Amazon S3.
- [Request routing](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequestRouting.html): Learn how requests are routed through Multi-Region Access Points in Amazon S3.

### [Failover configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapFailover.html)

Learn how to configure Amazon S3 Multi-Region Access Points failover controls.

- [Amazon S3 Multi-Region Access Points routing states](https://docs.aws.amazon.com/AmazonS3/latest/userguide/FailoverConfiguration.html): Amazon S3 Multi-Region Access Point failover configuration state.
- [Using Amazon S3 Multi-Region Access Point failover controls](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingFailover.html): Use Amazon S3 Multi-Region Access Point failover controls.
- [Amazon S3 Multi-Region Access Point failover controls errors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mrap-failover-errors.html): When you update the failover configuration for your Multi-Region Access Point, you might encounter one of these errors:

### [Bucket replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointBucketReplication.html)

Configure replication to support Multi-Region Access Points in Amazon S3.

- [Create one-way replication rules for your Multi-Region Access Point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mrap-create-one-way-replication-rules.html): Learn how and when to create one-way S3 Replication rules for your Multi-Region Access Point.
- [Create two-way replication rules for your Multi-Region Access Point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mrap-create-two-way-replication-rules.html): Learn how and when to create two-way (bidirectional) S3 Replication rules for your Multi-Region Access Point.
- [View the replication rules for your Multi-Region Access Point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mrap-view-replication-rules.html): Learn how to view your S3 Replication rules for your Multi-Region Access Point.
- [Supported API operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapOperations.html): Learn how to use Multi-Region Access Points with supported Amazon S3 API operations.
- [Monitoring and logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointMonitoring.html): Monitor and log all the requests for resources that are made to Amazon S3 through Multi-Region Access Points.

### [Retaining multiple versions of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

Use versioning in Amazon S3 to keep multiple variants of an object in the same bucket.

- [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html): Describes how Amazon S3 versions objects and behavior.
- [Enabling versioning on buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html): Examples for how to use the console, AWS CLI, and AWS SDKs to manage versioning for Amazon S3.
- [Configuring MFA delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html): Add a security layer by configuring an Amazon S3 bucket to enable MFA (multi-factor authentication) delete.

### [Working with versioning-enabled objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-objects-versioned-bucket.html)

Perform management operations like adding, deleting, and restoring objects in a versioning-enabled Amazon S3 bucket.

- [Adding objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/AddingObjectstoVersioningEnabledBuckets.html): Add objects to versioning-enabled buckets, and Amazon S3 automatically adds a unique version ID to every object.
- [Listing objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/list-obj-version-enabled-bucket.html): Retrieve an object listing from a versioning-enabled bucket in Amazon S3.

### [Retrieving object versions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RetrievingObjectVersions.html)

Get the current version or a specific version of an object from a versioning-enabled bucket.

- [Retrieving version metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RetMetaOfObjVersion.html): Get the metadata only and not the content of an object version in a versioning-enabled bucket.
- [Restoring previous versions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RestoringPreviousVersions.html): Retrieve a previous version of an object in a versioning-enabled bucket.

### [Deleting object versions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)

Delete an object in a versioning-enabled bucket by including the specific version ID of the object.

- [Working with delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html): Learn how to work with delete markers (placeholders for objects that are deleted in versioning-enabled buckets) in Amazon S3.
- [Managing delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingDelMarkers.html): Understanding the behaviour of removing delete markers.
- [Deleting with MFA delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingMFADelete.html): Delete an object in a versioning-enabled bucket that is MFA deleteâenabled by including the request header of the object version.
- [Configuring permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VersionedObjectPermissionsandACLs.html): Set and manage the permissions of each version of an object in a versioning-enabled bucket using ACLs.

### [Working with versioning-suspended objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VersionSuspendedBehavior.html)

Manage your objects when working in versioning-suspended buckets.

- [Adding objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/AddingObjectstoVersionSuspendedBuckets.html): Add objects to versioning-suspended buckets in Amazon S3 to create the object with a null version ID or overwrite any object version with a matching version ID.
- [Retrieving objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RetrievingObjectsfromVersioningSuspendedBuckets.html): Get objects from versioning-suspended buckets to retrieve the current version of the object.
- [Deleting objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectsfromVersioningSuspendedBuckets.html): Delete objects from versioning-suspended buckets to remove an object with a null version ID.
- [Troubleshooting versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshooting-versioning.html): Troubleshooting versioning issues and issue with having multiple versions of Amazon S3 objects.

### [Locking objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)

Prevent Amazon S3 objects from being deleted or overwritten for a fixed amount of time or indefinitely by using S3 Object Lock.

- [Object Lock considerations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html): You can use replication, delete markers, object lifecycle configurations, events, and notifications with Amazon S3 Object Lock.
- [Configuring Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-configure.html): Set and configure S3 Object Lock on an Amazon S3 bucket by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3 REST API.
- [Backing up your data](https://docs.aws.amazon.com/AmazonS3/latest/userguide/backup-for-s3.html): Use AWS Backup to automate the backup and restoration of Amazon S3 data.


## [Cost optimization](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cost-optimization.html)

### [Billing and usage reporting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketBilling.html)

Learn how to get more information about the AWS billing and usage reports for Amazon S3.

- [Using cost allocation tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html): Use cost allocation tags to label Amazon S3 buckets.
- [Billing reports](https://docs.aws.amazon.com/AmazonS3/latest/userguide/aws-billing-reports.html): Learn how to get more information about the AWS charges for using Amazon S3.
- [Usage reports](https://docs.aws.amazon.com/AmazonS3/latest/userguide/aws-usage-report.html): Describes the contents of and how to download an AWS usage report for Amazon S3.
- [Understanding billing and usage reports](https://docs.aws.amazon.com/AmazonS3/latest/userguide/aws-usage-report-understand.html): Learn how to understand an AWS usage bill and report for Amazon S3.
- [Billing for Amazon S3 error responses](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ErrorCodeBilling.html): Learn how to get more information about the AWS billing for Amazon S3 error responses.

### [Understanding and managing storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

Learn how to choose from a range of high durability storage classes for the objects that you store in Amazon S3, depending on your use case scenario and performance access requirements.

- [Setting the storage class of an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/sc-howtoset.html): You can specify a storage class for an object when you upload it.

### [Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html)

Describes Amazon S3 analytics Storage Class Analysis and how to use it.

- [Configuring storage class analysis](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configure-analytics-storage-class.html): How to configure Amazon S3 storage class analysis.

### [Managing storage costs with Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html)

Use S3 Intelligent-Tiering to optimize storage costs for data with unknown or changing access patterns.

- [How S3 Intelligent-Tiering works](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html): Learn about how Amazon S3 Intelligent-Tiering works, including which actions cause objects to move between the various S3 Intelligent-Tiering access tiers.
- [Using S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-intelligent-tiering.html): You can use the S3 Intelligent-Tiering storage class to automatically optimize storage costs.
- [Managing S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-managing.html): Learn how to manage and restore Amazon S3 objects that are archived in the S3 Intelligent-Tiering archive tiers.

### [Amazon S3 Glacier storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/glacier-storage-classes.html)

Learn about the Amazon S3 storage classes for long-term data: S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive.

- [Archival storage in S3 Glacier storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/archival-storage.html): S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive are archival storage classes.

### [Working with archived objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/archived-objects.html)

Access an archived object in Amazon S3 by initiating a restore request, which you can do programmatically or by using the console.

- [Understanding archive retrieval options](https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects-retrieval-options.html): learn about the different options available for restoring archived object in Amazon S3.
- [Restoring an archived object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects.html): Access an archived object in Amazon S3 by initiating a restore request, which you can do programmatically or by using the console.

### [Managing lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

Use Amazon S3 to manage your objects so that they're stored cost effectively throughout their lifecycle.

- [Transitioning objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html): Transition objects using S3 Lifecycle configurations.
- [Expiring objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-expire-general-considerations.html): Learn how to use Amazon S3 Lifecycle to expire or delete objects.
- [Setting lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html): Learn how to set an Amazon S3 Lifecycle configuration on a bucket programmatically or by using the Amazon S3 console.
- [Using other bucket configurations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-and-other-bucket-config.html): Learn how S3 Lifecycle interacts with other bucket configurations.
- [Configuring S3 Lifecycle event notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configure-notification.html): Learn how to set up Amazon S3 Event Notifications to be notified when lifecycle expiration and transition events occur.

### [Lifecycle configuration elements](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html)

Learn about the elements of an Amazon S3 Lifecycle configuration.

- [Adding filters to Lifecycle rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-filters.html): Learn about the filters you can use in an Amazon S3 Lifecycle configuration.
- [Lifecycle configuration conflicts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-conflicts.html): Learn how Amazon S3 resolves conflicts within Lifecycle configurations.
- [Examples of S3 Lifecycle configurations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html): Examples showing how to use S3 Lifecycle configurations.
- [Troubleshooting lifecycle issues](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshoot-lifecycle.html): Troubleshoot Amazon S3 Lifecycle issues.


## [Logging and monitoring](https://docs.aws.amazon.com/AmazonS3/latest/userguide/monitoring-overview.html)

- [Monitoring tools](https://docs.aws.amazon.com/AmazonS3/latest/userguide/monitoring-automated-manual.html): Configure AWS tools like CloudWatch and CloudTrail to monitor Amazon S3.
- [Logging options](https://docs.aws.amazon.com/AmazonS3/latest/userguide/logging-with-S3.html): Compare the logging options available for Amazon S3, including server-access logging and AWS CloudTrail logging.

### [Logging with CloudTrail](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-logging.html)

Describes the integration of AWS CloudTrail with Amazon S3.

- [CloudTrail events](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-logging-s3-info.html): Learn which Amazon S3 API operations are tracked by CloudTrail.
- [Example log files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-logging-understanding-s3-entries.html)
- [Enabling CloudTrail](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.html): Enable AWS CloudTrail event logging for your Amazon S3 buckets and objects.
- [Identifying S3 requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-request-identification.html): Identify Amazon S3 requests using AWS CloudTrail event logs.

### [Logging server access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html)

Enable Amazon S3 server access logging to track requests for access to your S3 buckets.

- [Enabling server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html): Enable Amazon S3 server access logging to track requests for access to your S3 buckets.
- [Log format](https://docs.aws.amazon.com/AmazonS3/latest/userguide/LogFormat.html): Learn about the format of server access logs, which report information about requests to access the server for the buckets that you own.
- [Deleting log files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/deleting-log-files-lifecycle.html): Delete server access Amazon S3 log objects when you no longer need them, or set up S3 Lifecycle configuration rules to automatically delete them.
- [Identifying S3 requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-s3-access-logs-to-identify-requests.html): Use Amazon S3 server access logs to identify Amazon S3 requests.
- [Troubleshoot server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshooting-server-access-logging.html): Learn how to troubleshoot server access logging issues.

### [Monitoring metrics with CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudwatch-monitoring.html)

Amazon CloudWatch metrics for Amazon S3.

- [Metrics and dimensions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metrics-dimensions.html): Learn about the storage metrics and dimensions that Amazon S3 sends to Amazon CloudWatch.
- [Accessing CloudWatch metrics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudwatch-monitoring-accessing.html): You can use the following procedures to view the storage metrics for Amazon S3.

### [CloudWatch metrics configurations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metrics-configurations.html)

Receive CloudWatch metrics, set CloudWatch alarms, and access CloudWatch dashboards to view near-real-time operations and performance of your Amazon S3 storage.

- [Creating a metrics configuration for all objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configure-request-metrics-bucket.html): When you configure request metrics, you can create a CloudWatch metrics configuration for all the objects in your bucket, or you can filter by prefix, object tag, or access point.
- [Filtering by prefix, object tag, or access point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metrics-configurations-filter.html): Describes how to create a metrics configuration that filters by object key name prefix, tag, or access point.
- [Deleting a metrics filter](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-request-metrics-filter.html): Delete a request metrics filter in Amazon S3 that uses tags or prefixes to limit scope.

### [Amazon S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)

Set up and configure notifications so that key events on buckets cause a message to be sent to an Amazon SNS topic.

- [Notification types and destinations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-event-types-and-destinations.html): Learn about using Amazon S3 event notification types and destinations, including Amazon Simple Notification Service (Amazon SNS) topics, Amazon Simple Queue Service (Amazon SQS) queues, AWS Lambda functions, and Amazon EventBridge, to track and respond to bucket events.

### [Using SQS, SNS, and Lambda](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-enable-disable-notification-intro.html)

Configure Amazon S3 event notifications to publish messages to Amazon Simple Queue Service (Amazon SQS) queues, Amazon Simple Notification Service (Amazon SNS) topics, or AWS Lambda functions when specific events occur in your S3 buckets.

- [Granting permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html): Grant the Amazon S3 principal the necessary permissions to call the relevant API to publish event notification messages to an SNS topic, an SQS queue, or a Lambda function.
- [Enabling notifications in the S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html): Receive notifications when specific Amazon S3 events such as object creation or deletion occur in an S3 bucket.
- [Walkthrough: Configuring SNS or SQS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ways-to-add-notification-config-to-bucket.html): Walk through an example that shows how to configure an Amazon S3 bucket for event notifications using Amazon SNS or Amazon SQS.
- [Configuring notifications using object key name filtering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-filtering.html): Configure Amazon S3 event notifications to be filtered by the prefix and suffix of the key name of objects.
- [Event message structure](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html): Learn about the JSON structure of event notification messages that Amazon S3 sends when events occur in your bucket, including field descriptions and example messages.

### [Using EventBridge](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventBridge.html)

Receive notifications when specific Amazon S3 events such as object creation or deletion occur in an Amazon S3 bucket with EventBridge.

- [EventBridge permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ev-permissions.html): Learn about the permissions required for Amazon S3 to deliver events to Amazon EventBridge.
- [Enabling EventBridge](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications-eventbridge.html): Enable Amazon EventBridge notifications for your Amazon S3 bucket by using the console, AWS Command Line Interface(AWS CLI), or REST API to receive alerts when bucket events occur.
- [EventBridge event message structure](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ev-events.html): Learn about the structure and fields of event messages that Amazon S3 sends to Amazon EventBridge, including JSON examples for object creation, deletion, and restoration events.
- [Amazon EventBridge mapping and troubleshooting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ev-mapping-troubleshooting.html): Learn how Amazon S3 event types map to Amazon EventBridge event types and find troubleshooting information for EventBridge events.

### [Monitoring your storage activity and usage with S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html)

Use Amazon S3 Storage Lens to assess your Amazon S3 storage to gain insights, help increase cost efficiency and performance, and apply access management and data protection best practices.

- [Understanding S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_basics_metrics_recommendations.html): Learn the basic concepts about Amazon S3 Storage Lens to start getting insights into your S3 storage.
- [Metrics glossary](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_metrics_glossary.html): Get names and descriptions for all Amazon S3 Storage Lens metrics.
- [Setting permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html): Set AWS Identity and Access Management (IAM) permissions to use Amazon S3 Storage Lens.
- [Table naming for S3 Tables export](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_s3_tables_naming.html): Learn about the naming conventions and structure for S3 Storage Lens tables exported to S3 Tables.

### [Working with S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3LensExamples.html)

Amazon S3 Storage Lens console, code examples, and video demonstration of how to use the feature.

- [Create a dashboard](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_creating_dashboard.html): Create Amazon S3 Storage Lens dashboards.
- [Update a dashboard](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_editing.html): Update Amazon S3 Storage Lens dashboards on the Amazon S3 console.
- [Disable a dashboard](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_disabling.html): You can disable an Amazon S3 Storage Lens dashboard from the Amazon S3 console.
- [Delete a dashboard](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_deleting.html): You can't delete the default dashboard.
- [List dashboards](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_list_dashboard.html)
- [View dashboard details](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_viewing.html): View Amazon S3 Storage Lens dashboard configuration details in the Amazon S3 console, AWS CLI, and SDK for Java.

### [Manage AWS resource tags with Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-manage-tags-dashboard.html)

Learn how to use AWS resource tags with Amazon S3 Storage Lens.

- [Add AWS resource tags to a dashboard](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-add-tags.html): Learn how to add AWS resource tags to an S3 Storage Lens dashboard.
- [Retrieve AWS resource tags for a dashboard](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-get-tags.html): Learn how to retrieve AWS resource tags for a S3 Storage Lens dashboard.
- [Update dashboard tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-update-tags.html): Learn how to update the user-defined AWS resource tags for an Amazon S3 Storage Lens dashboard.
- [Delete AWS resource tags from a dashboard](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-dashboard-delete-tags.html): Learn how to delete user-defined AWS resource tags from a Amazon S3 Storage Lens group.
- [Helper files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3LensHelperFilesCLI.html): Review these example helper files that you can use with Amazon S3 Storage Lens.

### [Viewing storage metrics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_view_metrics.html)

View your Amazon S3 Storage Lens metrics.

- [Viewing metrics on the dashboards](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_view_metrics_dashboard.html): View Amazon S3 Storage Lens metrics on the S3 Storage Lens dashboards.

### [Viewing metrics in a data export](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_view_metrics_export.html)

View the Amazon S3 Storage Lens metrics in a data export.

- [Encrypting metrics exports](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_encrypt_permissions.html): Use an AWS Key Management Service (AWS KMS) customer managed key for encrypting your metrics exports.
- [What is an export manifest?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_whatis_metrics_export_manifest.html): Use the S3 Storage Lens export manifest to find out where the metrics export files for that day are located.
- [S3 Storage Lens export schemas](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_understanding_metrics_export_schema.html): Learn about the schemas of the Amazon S3 Storage Lens exports for different destination types.

### [Monitor S3 Storage Lens metrics in CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_view_metrics_cloudwatch.html)

You can publish S3 Storage Lens metrics to Amazon CloudWatch to create a unified view of your operational health in CloudWatch dashboards.

- [S3 Storage Lens metrics and dimensions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-cloudwatch-metrics-dimensions.html): To send S3 Storage Lens metrics to CloudWatch, you must enable the CloudWatch publishing option within S3 Storage Lens advanced metrics.
- [Enabling CloudWatch publishing](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-cloudwatch-enable-publish-option.html): You can publish S3 Storage Lens metrics to Amazon CloudWatch to create a unified view of your operational health in CloudWatch dashboards.
- [Using CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-cloudwatch-monitoring-cloudwatch.html): You can publish S3 Storage Lens metrics to Amazon CloudWatch to create a unified view of your operational health in CloudWatch dashboards.

### [Amazon S3 Storage Lens metrics use cases](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-use-cases.html)

You can use Amazon S3 Storage Lens metrics to identify cost-optimization opportunities, apply data-protection best practices, and improve the performance of application workloads.

- [For cost optimization](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-optimize-storage.html): Use Amazon S3 Storage Lens metrics to optimize Amazon S3 storage costs.
- [For data protection](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-data-protection.html): Use Amazon S3 Storage Lens metrics to apply data-protection best practices to your Amazon S3 buckets.
- [For Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-access-management.html): Use Amazon S3 Storage Lens metrics to identify the S3 Object Ownership settings for your buckets.
- [For performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-detailed-status-code.html): Use Amazon S3 Storage Lens metrics to improve the performance of workloads that access your buckets.

### [Working with Organizations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_with_organizations.html)

Use Amazon S3 Storage Lens to collect storage metrics and usage data for all accounts that are part of your AWS Organizations hierarchy.

- [Enabling trusted access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_with_organizations_enabling_trusted_access.html): Enable trusted access for Amazon S3 Storage Lens.
- [Disabling trusted access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_with_organizations_disabling_trusted_access.html): Disable trusted access for Amazon S3 Storage Lens.
- [Registering a delegated administrator](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_with_organizations_registering_delegated_admins.html): Register a delegated administrator for Amazon S3 Storage Lens.
- [Deregistering a delegated administrator](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_with_organizations_deregistering_delegated_admins.html): Deregister a delegated administrator for Amazon S3 Storage Lens.

### [Working with Storage Lens groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-overview.html)

Use Amazon S3 Storage Lens groups to optimize cost reporting and to better understand your storage allocation based on prefixes, suffixes, object tags, object size, and object age.

- [How Storage Lens groups work](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups.html): Learn how Amazon S3 Storage Lens groups work with your Amazon S3 Storage Lens dashboards.

### [Using Storage Lens groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-group-tasks.html)

Learn how to use Amazon S3 Storage Lens groups to help analyze your storage usage based on filters, such as prefixes, suffixes, object tags, object size, and object age.

- [Create a Storage Lens group](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-create.html): Learn how to create an Amazon S3 Storage Lens group.
- [Attach or remove a Storage Lens group](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-dashboard-console.html): Learn how to attach or remove Amazon S3 Storage Lens groups to or from an S3 Storage Lens dashboard.
- [Visualize Storage Lens group data](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-visualize.html): Learn how to visualize Storage Lens groups data in your S3 Storage Lens dashboard.
- [Update a Storage Lens group](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-update.html): Learn how to update an Amazon S3 Storage Lens group.

### [Manage AWS resource tags with Storage Lens groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-manage-tags.html)

Learn how to use AWS resource tags with Amazon S3 Storage Lens groups.

- [Add an AWS resource tag to a Storage Lens group](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-add-tags.html): Learn how to add an AWS resource tag to an Amazon S3 Storage Lens group.
- [Update Storage Lens group tag values](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-update-tags.html): Learn how to update the user-defined AWS resource tags for an Amazon S3 Storage Lens group.
- [Delete an AWS resource tag from a Storage Lens group](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-delete-tags.html): Learn how to delete user-defined AWS resource tags from an Amazon S3 Storage Lens group.
- [List Storage Lens group tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-list-tags.html): Learn how to list the AWS resource tags for an Amazon S3 Storage Lens group.
- [List all Storage Lens groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-list.html): Learn how to list all Amazon S3 Storage Lens groups in an account and home Region.
- [View Storage Lens group details](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-view.html): Learn how to view the configuration details of an Amazon S3 Storage Lens group.
- [Delete a Storage Lens group](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-delete.html): Learn how to delete an Amazon S3 Storage Lens group.

### [Cataloging and analyzing your data](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html)

Learn what Amazon S3 Inventory is and how to use it to manage your storage.

- [Configuring Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configure-inventory.html): Configure Amazon S3 Inventory to generate automated reports about your objects and metadata.
- [Locating your inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory-location.html): Learn where Amazon S3 Inventory lists are located.
- [Setting up notifications for inventory completion](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory-notification.html): Learn how to set up Amazon S3 Event Notifications to be notified when an inventory list is published.
- [Querying inventory with Athena](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory-athena-query.html): Learn how to query an inventory by using Amazon Athena.
- [Converting empty version ID strings to null strings](https://docs.aws.amazon.com/AmazonS3/latest/userguide/inventory-configure-bops.html): Describes how to convert empty version ID strings in an "all versions" S3 Inventory report to null strings so that the report can be used as a manifest for S3 Batch Operations.
- [Working with the Object ACL field](https://docs.aws.amazon.com/AmazonS3/latest/userguide/objectacl.html): Learn how to work with the Object access control list (ACL) field in Amazon S3 Inventory.


## [Optimizing performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html)

- [Performance guidelines for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-guidelines.html): Describes Amazon S3 performance guidelines.
- [Performance design patterns for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-design-patterns.html): Describes high performance design patterns for Amazon S3.


## [Hosting a static website](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)

- [Website endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteEndpoints.html): Configure an Amazon S3 bucket for website hosting to make it available through the AWS Region-specific website endpoint.
- [Enabling website hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EnableWebsiteHosting.html): Enable website hosting through the Amazon S3 console.
- [Configuring an index document](https://docs.aws.amazon.com/AmazonS3/latest/userguide/IndexDocumentSupport.html): Configure your Amazon S3 bucket as a website by providing the name of an index document, which is the root of a website, often called the default page.
- [Configuring a custom error document](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CustomErrorDocSupport.html): Configure your Amazon S3 bucket as a website by providing a custom error document of HTTP response codes.
- [Setting permissions for website access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html): Configure your Amazon S3 bucket as a website by granting access permissions to the website through a bucket policy.
- [Logging web traffic](https://docs.aws.amazon.com/AmazonS3/latest/userguide/LoggingWebsiteTraffic.html): An optional step to configure web traffic logging for your static website.
- [Configuring a redirect](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-page-redirect.html): Configure your bucket as a website by setting up redirect locations where you can redirect requests for an object to another object.

### [Using CORS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html)

In Amazon S3, define a way for client web applications that are loaded in one domain to interact with resources in a different domain.

- [Elements of a CORS configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManageCorsUsing.html): Create an XML or JSON CORS configuration on your bucket.
- [Configuring CORS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enabling-cors-examples.html): Enable cross-origin resource sharing by setting a CORS configuration on your bucket using the AWS Management Console, the REST API, or the AWS SDKs.
- [Testing CORS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/testing-cors.html): Testing your CORS Configuration using curl.
- [Troubleshooting CORS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors-troubleshooting.html): Troubleshoot common problems encountered when you configure CORS for your bucket.

### [Static website tutorials](https://docs.aws.amazon.com/AmazonS3/latest/userguide/static-website-tutorials.html)

Tutorials or walkthroughs for using Amazon S3 to support static websites.

- [Hosting video streaming](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorial-s3-cloudfront-route53-video-streaming.html): Walk through an example of how to configure an S3 bucket to host on-demand video streaming using CloudFront for delivery and RouteÂ 53 for DNS and custom domain management.
- [Configuring a static website](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html): Walk through a code example of how to configure a bucket for website hosting using the Amazon S3 website endpoint.

### [Configuring a static website using a custom domain](https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-custom-domain-walkthrough.html)

Walk through a code example of how to set up a static website in Amazon S3 using a custom domain that is registered with RouteÂ 53.

- [Speeding up your website with Amazon CloudFront](https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-cloudfront-walkthrough.html): Walk through an example of how to set up Amazon CloudFront to speed up a static website on Amazon S3.
- [Cleaning up example resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/getting-started-cleanup.html): In Amazon S3, delete the AWS resources that you don't need.
- [Deploying a static website to Amplify from Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-amplify.html): Learn how to deploy a static website using Amplify Hosting.


## [Tagging buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging.html)

- [Enable bucket ABAC](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html): Learn how to enable ABAC for an Amazon S3 general purpose bucket.
- [Creating general purpose buckets with tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-create-tag.html): Learn how to create a general purpose bucket with tags.
- [Adding a tag to a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-tag-add.html): Learn how to add a tag to an existing bucket.
- [Viewing bucket tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-tag-view.html): Learn how to view the tags of an existing bucket.
- [Deleting a tag from a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-tag-delete.html): Learn how to delete a tag from an existing bucket.
