# Source: https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/llms.txt

# Amazon S3 on Outposts User Guide

> Learn how to use Amazon Simple Storage Service (Amazon S3) to store and retrieve any amount of data from anywhere. This guide explains Amazon S3 concepts, such as buckets, objects, and related configurations, and includes code examples for common operations.

- [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3onOutposts.html)
- [Setting up your Outpost](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/OrderOutposts.html)
- [How S3 on Outposts is different](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OnOutpostsRestrictionsLimitations.html)
- [Networking for S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsNetworking.html)

## [Getting started with S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsGS.html)

- [Using the S3 console](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsGSConsole.html): Using the console, get started with Amazon S3 on Outposts by creating a bucket, an access point, and an endpoint so that you can easily store and retrieve objects on premises for applications that require local data access, local data processing, and data residency.
- [Using the AWS CLI and SDK for Java](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsGSCLIJava.html): Using the AWS CLI and the SDK for Java, get started with Amazon S3 on Outposts by creating a bucket, an access point, and an endpoint so that you can easily store and retrieve objects on premises for applications that require local data access, local data processing, and data residency.


## [Working with S3 on Outposts buckets](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsWorkingBuckets.html)

- [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsCreateBucket.html): Create Amazon S3 buckets on your AWS Outposts so that you can easily store and retrieve objects on premises for applications that require local data access, local data processing, and data residency.
- [Adding tags](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsBucketTags.html): Provides information about how to add tags to Amazon S3 on Outposts bucket to track storage costs or other criteria.

### [Using bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsBucketPolicy.html)

Provides information about managing access to your Amazon S3 on Outposts bucket by using bucket policies.

- [Adding a bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsBucketPolicyEdit.html): Provides information about how to add or edit a bucket policy for your Amazon S3 on Outposts bucket.
- [Viewing a bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsBucketPolicyGet.html): Provides information about how to view the bucket policy for your Amazon S3 on Outposts bucket.
- [Deleting a bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsBucketPolicyDelete.html): Provides information about how to delete the bucket policy for your Amazon S3 on Outposts bucket.
- [Bucket policy examples](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3Outposts-example-bucket-policies.html): See examples of typical use cases for S3 on Outposts bucket policies.
- [Listing buckets](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsListBuckets.html): Discusses how to return a list of your Amazon S3 on Outposts buckets.
- [Getting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsGetBucket.html): Discusses how to get an Amazon S3 on Outposts bucket.
- [Deleting your bucket](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsDeleteBucket.html): Learn how to delete your Amazon S3 on Outposts buckets.

### [Working with access points](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsAccessPoints.html)

Learn how to work with Amazon S3 on Outposts access points.

- [Creating an access point](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsCreateAccessPoint.html): Create an access point for an Amazon S3 on Outposts bucket.
- [Using a bucket-style alias for your access point](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/s3-outposts-access-points-alias.html): Learn how to use bucket-style aliases instead of Amazon Resource Names (ARNs) to refer to your Amazon S3 on Outposts buckets.
- [Viewing access point configuration](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsAccessPointGet.html): Discusses how to return configuration information for an Amazon S3 on Outposts bucket's access point.
- [Listing access points](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsAccessPointList.html): Learn how to list your Amazon S3 on Outposts access points.
- [Deleting an access point](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsAccessPointsDelete.html): Learn how to delete an access point for an Amazon S3 on Outposts bucket.
- [Adding an access point policy](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsAccessPointEditPolicy.html): Discusses how to add or edit the access point policy for your Amazon S3 on Outposts bucket.
- [Viewing an access point policy](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsAccessPointGetPolicy.html): Learn how to return an access point policy for an Amazon S3 on Outposts bucket's access point.

### [Working with endpoints](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsEndpointsWorking.html)

Discusses how to create, list, and delete Amazon S3 on Outposts endpoints.

- [Creating an endpoint](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsCreateEndpoint.html): Create an endpoint to route requests to your Amazon S3 on Outposts access point.
- [Listing endpoints](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsListEndpoints.html): To route requests to an Amazon S3 on Outposts access point, you must create and configure an S3 on Outposts endpoints.
- [Deleting an endpoint](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsDeleteEndpoints.html): Discusses how to delete your Amazon S3 on Outposts endpoint.


## [Working with S3 on Outposts objects](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsWorkingObjects.html)

- [Upload an object](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsUploadObjects.html): Objects are the fundamental entities stored in Amazon S3 on Outposts.
- [Copying an object](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsCopyObject.html): Learn how to copy an object that's stored in an Amazon S3 on Outposts bucket.
- [Getting an object](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsGetObject.html): Download (get) an S3 on Outposts object using the AWS CLI or the SDK for Java.
- [Listing objects](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsListObjects.html): Amazon S3 on Outposts list objects AWS CLI and SDK for Java examples.
- [Deleting objects](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsDeleteObject.html): Learn how to delete objects in an Amazon S3 on Outposts bucket by using the AWS CLI and SDK for Java.
- [Using HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsHeadBucket.html): Use the HeadBucket API operation to determine if an Amazon S3 on Outposts bucket exists and whether you have permission to access it.
- [Performing a multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsMPU.html): Amazon S3 on Outposts AWS SDK for Java examples for performing and managing a multipart upload.

### [Using presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsPresignedURL.html)

Use a presigned URL to share or upload objects in Amazon S3 on Outposts without requiring AWS security credentials or permissions.

- [Sharing objects](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsShareObjectPresignedURL.html): Describes how to set up your Amazon S3 on Outposts objects so that you can share them with others by creating a presigned URL to download the objects.
- [Uploading an object](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsPresignedUrlUploadObject.html): Upload Amazon S3 on Outposts objects by using presigned URLs when someone has given you permissions to access the object identified in the URL.
- [Amazon S3 on Outposts with local Amazon EMR](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/s3-outposts-emr.html): Learn about Amazon EMR support for Amazon S3 on Outposts.
- [Authorization and authentication caching](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/s3-outposts-auth-cache.html): Learn about Amazon S3 on Outposts local authentication and authorization data caching.


## [Security](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/s3outposts-security.html)

- [Setting up IAM](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsIAM.html): Securely control access to your AWS Outposts resources by using AWS Identity and Access Management (IAM) with Amazon S3 on Outposts.
- [Data encryption](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/s3-outposts-data-encryption.html): Learn how the AWS shared responsibility model applies to data protection in Amazon S3 on Outposts.
- [AWS PrivateLink for S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/s3-outposts-privatelink-interface-endpoints.html): Access S3 on Outposts bucket management and endpoint management APIs using AWS PrivateLinkÂ interface VPC endpoints in your VPC.
- [Signature Version 4 (SigV4) policy keys](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/s3-outposts-bucket-policy-s3-sigv4-conditions.html): How to use AWS Signature Version 4 authentication-specific policy keys.
- [AWS managed policies](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/s3-outposts-aws-manpol.html): Learn about AWS managed policies for Amazon S3 on Outposts and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsServiceLinkedRoles.html): How to use service-linked roles to give S3 on Outposts access to resources in your AWS account.


## [Managing S3 on Outposts storage](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsManaging.html)

- [Managing S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsManagingVersioning.html): Enable or suspend S3 Versioning for your Amazon S3 on Outposts bucket to maintain multiple, distinct copies of the objects in your bucket.

### [Creating and managing a lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsLifecycleManaging.html)

Create S3 Lifecycle rules to manage objects in your S3 on Outposts bucket so that they are stored cost effectively throughout their lifecycle.

- [Using the console](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsLifecycleConsole.html): Discusses how to create and manage your Amazon S3 on Outposts lifecycle rule by using the AWS Management Console.
- [Using the AWS CLI and SDK for Java](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsLifecycleCLIJava.html): Discusses how to create and manage your Amazon S3 on Outposts lifecycle configuration by using the AWS Management Console.

### [Replicating objects for S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsReplication.html)

Set up and configure automatic replication to allow automatic copying of objects across Amazon S3 on Outposts.

### [Setting up replication](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/outposts-replication-how-setup.html)

Learn how to set up replication for Amazon S3 on Outposts.

- [Prerequisites for creating replication rules](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/outposts-replication-prerequisites-config.html): Learn about the prerequisite steps for S3 Replication on Outposts.
- [Creating replication rules on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/replication-between-outposts.html): Set up replication in Amazon S3 where the source and destination Outposts buckets are owned by different Outposts.

### [Managing your replication](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/manage-outposts-replication.html)

Learn about additional replication configuration options for Amazon S3 on Outposts, how to get the replication status, and how to troubleshoot replication.

- [Using EventBridge](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/outposts-replication-eventbridge.html): Learn how to use Amazon EventBridge to monitor S3 Replication on Outposts.
- [Sharing S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/outposts-sharing-with-ram.html): Share Amazon S3 on Outposts resources with other AWS accounts by using AWS Resource Access Manager.
- [Other services](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsOtherServices.html): Other AWS services that use Amazon S3 on Outposts, including Amazon S3, Amazon Elastic Block Store, and Amazon Relational Database Service.


## [Monitoring S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsMonitoring.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsCapacity.html): To help manage the fixed S3 capacity on your Outpost, we recommend that you create CloudWatch alerts that tell you when your storage utilization exceeds a certain threshold.
- [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsNotificationsCWE.html): You can use CloudWatch Events to create a rule for any Amazon S3 on Outposts API event.
- [CloudTrail logs](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsCloudtrail.html): Amazon S3 on Outposts is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in S3 on Outposts.


## [Developing with S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsDeveloping.html)

- [Supported regions](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsRegions.html): Find the list of AWS Regions where S3 on Outposts is supported, including regions in North America, South America, Europe, Middle East, Africa, and Asia Pacific.
- [S3 on Outposts APIs](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsAPI.html): Provides a list of Amazon S3 and Amazon S3 on Outposts API operations for object, bucket, and endpoint operations.
- [Configuring S3 control client](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsCongfigureS3ControlClientJava.html): AWS SDK for Java example of how to configure the Amazon S3 control client for Amazon S3 on Outposts.

### [Making requests over IPv6](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsIPv6-access.html)

Explains how to access S3 on Outposts using the IPv6 protocols.

- [Using dual-stack endpoints](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/s3-outposts-dual-stack-endpoints.html): Explains how to make requests to S3 on Outposts dual-stack endpoints.
