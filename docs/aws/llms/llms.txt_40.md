# Source: https://docs.aws.amazon.com/AmazonS3/latest/API/llms.txt

# Amazon Simple Storage Service API Reference

> Explains how to use the Amazon S3 API to store data in the cloud.

- [Welcome](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)
- [Common request headers](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonRequestHeaders.html)
- [Common response headers](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonResponseHeaders.html)
- [AWS Glossary](https://docs.aws.amazon.com/AmazonS3/latest/API/glossary.html)
- [Resources](https://docs.aws.amazon.com/AmazonS3/latest/API/RelatedResources.html)
- [Document History](https://docs.aws.amazon.com/AmazonS3/latest/API/WhatsNew.html)

## [S3 API Reference](https://docs.aws.amazon.com/AmazonS3/latest/API/Type_API_Reference.html)

### [Actions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations.html)

The following actions are supported by Amazon S3:

### [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_Simple_Storage_Service.html)

The following actions are supported by Amazon S3:

- [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html): This operation aborts a multipart upload.
- [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html): Completes a multipart upload by assembling previously uploaded parts.
- [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html): Creates a copy of an object that is already stored in Amazon S3.
- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
- [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html): Creates an S3 Metadata V2 metadata configuration for a general purpose bucket.
- [CreateBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataTableConfiguration.html)
- [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
- [CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html): Creates a session that establishes temporary security credentials to support fast authentication and authorization for the Zonal endpoint API operations on directory buckets.
- [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html): Deletes the S3 bucket.
- [DeleteBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketAnalyticsConfiguration.html)
- [DeleteBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketCors.html)
- [DeleteBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html): This implementation of the DELETE action resets the default encryption for the bucket as server-side encryption with Amazon S3 managed keys (SSE-S3).
- [DeleteBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketIntelligentTieringConfiguration.html)
- [DeleteBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketInventoryConfiguration.html)
- [DeleteBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html): Deletes the lifecycle configuration from the specified bucket.
- [DeleteBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataConfiguration.html): Deletes an S3 Metadata configuration from a general purpose bucket.
- [DeleteBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataTableConfiguration.html)
- [DeleteBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetricsConfiguration.html)
- [DeleteBucketOwnershipControls](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketOwnershipControls.html)
- [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html): Deletes the policy of a specified bucket.
- [DeleteBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketReplication.html)
- [DeleteBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html)
- [DeleteBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketWebsite.html)
- [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html): Removes an object from a bucket.
- [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html): This operation enables you to delete multiple objects from a bucket using a single HTTP request.
- [DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)
- [DeletePublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletePublicAccessBlock.html)
- [GetBucketAbac](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAbac.html): Returns the attribute-based access control (ABAC) property of the general purpose bucket.
- [GetBucketAccelerateConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAccelerateConfiguration.html)
- [GetBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html)
- [GetBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAnalyticsConfiguration.html)
- [GetBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html)
- [GetBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html): Returns the default encryption configuration for an Amazon S3 bucket.
- [GetBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketIntelligentTieringConfiguration.html)
- [GetBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html)
- [GetBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycle.html)
- [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html): Returns the lifecycle configuration information set on the bucket.
- [GetBucketLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html)
- [GetBucketLogging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLogging.html)
- [GetBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfiguration.html): Retrieves the S3 Metadata configuration for a general purpose bucket.
- [GetBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfiguration.html)
- [GetBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetricsConfiguration.html)
- [GetBucketNotification](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotification.html)
- [GetBucketNotificationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html)
- [GetBucketOwnershipControls](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketOwnershipControls.html)
- [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html): Returns the policy of a specified bucket.
- [GetBucketPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html)
- [GetBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketReplication.html)
- [GetBucketRequestPayment](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketRequestPayment.html)
- [GetBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html)
- [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html)
- [GetBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketWebsite.html)
- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html): Retrieves an object from Amazon S3.
- [GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html)
- [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html): Retrieves all of the metadata from an object without returning the object itself.
- [GetObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html)
- [GetObjectLockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLockConfiguration.html)
- [GetObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html)
- [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html)
- [GetObjectTorrent](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTorrent.html)
- [GetPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)
- [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html): You can use this operation to determine if a bucket exists and if you have permission to access it.
- [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html): The HEAD operation retrieves metadata from an object without returning the object itself.
- [ListBucketAnalyticsConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketAnalyticsConfigurations.html)
- [ListBucketIntelligentTieringConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketIntelligentTieringConfigurations.html)
- [ListBucketInventoryConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketInventoryConfigurations.html)
- [ListBucketMetricsConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketMetricsConfigurations.html)
- [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)
- [ListDirectoryBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html): Returns a list of all Amazon S3 directory buckets owned by the authenticated sender of the request.
- [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html): This operation lists in-progress multipart uploads in a bucket.
- [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html)
- [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html): Returns some or all (up to 1,000) of the objects in a bucket with each request.
- [ListObjectVersions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html)
- [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html): Lists the parts that have been uploaded for a specific multipart upload.
- [PutBucketAbac](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAbac.html): Sets the attribute-based access control (ABAC) property of the general purpose bucket.
- [PutBucketAccelerateConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html)
- [PutBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html)
- [PutBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAnalyticsConfiguration.html)
- [PutBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html)
- [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html): This operation configures default encryption and Amazon S3 Bucket Keys for an existing bucket.
- [PutBucketIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketIntelligentTieringConfiguration.html)
- [PutBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html)
- [PutBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycle.html)
- [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html): Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle configuration.
- [PutBucketLogging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html)
- [PutBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketMetricsConfiguration.html)
- [PutBucketNotification](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotification.html)
- [PutBucketNotificationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotificationConfiguration.html)
- [PutBucketOwnershipControls](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketOwnershipControls.html)
- [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html): Applies an Amazon S3 bucket policy to an Amazon S3 bucket.
- [PutBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketReplication.html)
- [PutBucketRequestPayment](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketRequestPayment.html)
- [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html)
- [PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html)
- [PutBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html)
- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
- [PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html)
- [PutObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLegalHold.html)
- [PutObjectLockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLockConfiguration.html)
- [PutObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectRetention.html)
- [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)
- [PutPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html)
- [RenameObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RenameObject.html): Renames an existing object in a directory bucket that uses the S3 Express One Zone storage class.
- [RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html)
- [SelectObjectContent](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SelectObjectContent.html)
- [UpdateBucketMetadataInventoryTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataInventoryTableConfiguration.html): Enables or disables a live inventory table for an S3 Metadata configuration on a general purpose bucket.
- [UpdateBucketMetadataJournalTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataJournalTableConfiguration.html): Enables or disables journal table record expiration for an S3 Metadata configuration on a general purpose bucket.
- [UpdateObjectEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateObjectEncryption.html)
- [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html): Uploads a part in a multipart upload.
- [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html): Uploads a part by copying data from an existing object as data source.
- [WriteGetObjectResponse](https://docs.aws.amazon.com/AmazonS3/latest/API/API_WriteGetObjectResponse.html)

### [Amazon S3 Control](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_AWS_S3_Control.html)

The following actions are supported by Amazon S3 Control:

- [AssociateAccessGrantsIdentityCenter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AssociateAccessGrantsIdentityCenter.html): Associate your S3 Access Grants instance with an AWS IAM Identity Center instance.
- [CreateAccessGrant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrant.html): Creates an access grant that gives a grantee access to your S3 data.
- [CreateAccessGrantsInstance](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsInstance.html): Creates an S3 Access Grants instance, which serves as a logical grouping for access grants.
- [CreateAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsLocation.html): The S3 data location that you would like to register in your S3 Access Grants instance.
- [CreateAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html): Creates an access point and associates it to a specified bucket.
- [CreateAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html)
- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucket.html)
- [CreateJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html): This operation creates an S3 Batch Operations job.
- [CreateMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html)
- [CreateStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateStorageLensGroup.html): Creates a new S3 Storage Lens group and associates it with the specified AWS account ID.
- [DeleteAccessGrant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrant.html): Deletes the access grant from the S3 Access Grants instance.
- [DeleteAccessGrantsInstance](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsInstance.html): Deletes your S3 Access Grants instance.
- [DeleteAccessGrantsInstanceResourcePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsInstanceResourcePolicy.html): Deletes the resource policy of the S3 Access Grants instance.
- [DeleteAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsLocation.html): Deregisters a location from your S3 Access Grants instance.
- [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html): Deletes the specified access point.
- [DeleteAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html)
- [DeleteAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html): Deletes the access point policy for the specified access point.
- [DeleteAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html)
- [DeleteAccessPointScope](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointScope.html): Deletes an existing access point scope for a directory bucket.
- [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucket.html)
- [DeleteBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketLifecycleConfiguration.html)
- [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketPolicy.html)
- [DeleteBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketReplication.html)
- [DeleteBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketTagging.html)
- [DeleteJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html): Removes the entire tag set from the specified S3 Batch Operations job.
- [DeleteMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html)
- [DeletePublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeletePublicAccessBlock.html)
- [DeleteStorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensConfiguration.html)
- [DeleteStorageLensConfigurationTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensConfigurationTagging.html)
- [DeleteStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensGroup.html): Deletes an existing S3 Storage Lens group.
- [DescribeJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html): Retrieves the configuration parameters and status for a Batch Operations job.
- [DescribeMultiRegionAccessPointOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html)
- [DissociateAccessGrantsIdentityCenter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DissociateAccessGrantsIdentityCenter.html): Dissociates the AWS IAM Identity Center instance from the S3 Access Grants instance.
- [GetAccessGrant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrant.html): Get the details of an access grant from your S3 Access Grants instance.
- [GetAccessGrantsInstance](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstance.html): Retrieves the S3 Access Grants instance for a Region in your account.
- [GetAccessGrantsInstanceForPrefix](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstanceForPrefix.html): Retrieve the S3 Access Grants instance that contains a particular prefix.
- [GetAccessGrantsInstanceResourcePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstanceResourcePolicy.html): Returns the resource policy of the S3 Access Grants instance.
- [GetAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsLocation.html): Retrieves the details of a particular location registered in your S3 Access Grants instance.
- [GetAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html): Returns configuration information about the specified access point.
- [GetAccessPointConfigurationForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointConfigurationForObjectLambda.html)
- [GetAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointForObjectLambda.html)
- [GetAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html): Returns the access point policy associated with the specified access point.
- [GetAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyForObjectLambda.html)
- [GetAccessPointPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyStatus.html)
- [GetAccessPointPolicyStatusForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyStatusForObjectLambda.html)
- [GetAccessPointScope](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointScope.html): Returns the access point scope for a directory bucket.
- [GetBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html): Gets an Amazon S3 on Outposts bucket.
- [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html)
- [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketPolicy.html)
- [GetBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketReplication.html)
- [GetBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketTagging.html)
- [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketVersioning.html)
- [GetDataAccess](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetDataAccess.html): Returns a temporary access credential from S3 Access Grants to the grantee or client application.
- [GetJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html): Returns the tags on an S3 Batch Operations job.
- [GetMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html)
- [GetMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicy.html)
- [GetMultiRegionAccessPointPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicyStatus.html)
- [GetMultiRegionAccessPointRoutes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointRoutes.html)
- [GetPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetPublicAccessBlock.html)
- [GetStorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensConfiguration.html)
- [GetStorageLensConfigurationTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensConfigurationTagging.html)
- [GetStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensGroup.html): Retrieves the Storage Lens group configuration details.
- [ListAccessGrants](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrants.html): Returns the list of access grants in your S3 Access Grants instance.
- [ListAccessGrantsInstances](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsInstances.html): Returns a list of S3 Access Grants instances.
- [ListAccessGrantsLocations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsLocations.html): Returns a list of the locations registered in your S3 Access Grants instance.
- [ListAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html)
- [ListAccessPointsForDirectoryBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForDirectoryBuckets.html): Returns a list of the access points that are owned by the AWS account and that are associated with the specified directory bucket.
- [ListAccessPointsForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html)
- [ListCallerAccessGrants](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListCallerAccessGrants.html): Use this API to list the access grants that grant the caller access to Amazon S3 data through S3 Access Grants.
- [ListJobs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html): Lists current S3 Batch Operations jobs as well as the jobs that have ended within the last 90 days for the AWS account making the request.
- [ListMultiRegionAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html)
- [ListRegionalBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListRegionalBuckets.html)
- [ListStorageLensConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensConfigurations.html)
- [ListStorageLensGroups](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensGroups.html): Lists all the Storage Lens groups in the specified home Region.
- [ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListTagsForResource.html): This operation allows you to list all of the tags for a specified resource.
- [PutAccessGrantsInstanceResourcePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessGrantsInstanceResourcePolicy.html): Updates the resource policy of the S3 Access Grants instance.
- [PutAccessPointConfigurationForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointConfigurationForObjectLambda.html)
- [PutAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html): Associates an access policy with the specified access point.
- [PutAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicyForObjectLambda.html)
- [PutAccessPointScope](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointScope.html): Creates or replaces the access point scope for a directory bucket.
- [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html)
- [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketPolicy.html)
- [PutBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketReplication.html)
- [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketTagging.html)
- [PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketVersioning.html)
- [PutJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutJobTagging.html): Sets the supplied tag-set on an S3 Batch Operations job.
- [PutMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html)
- [PutPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutPublicAccessBlock.html)
- [PutStorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfiguration.html)
- [PutStorageLensConfigurationTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfigurationTagging.html)
- [SubmitMultiRegionAccessPointRoutes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SubmitMultiRegionAccessPointRoutes.html)
- [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html): Creates a new user-defined tag or updates an existing tag.
- [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html): This operation removes the specified user-defined tags from an S3 resource.
- [UpdateAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateAccessGrantsLocation.html): Updates the IAM role of a registered location in your S3 Access Grants instance.
- [UpdateJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html): Updates an existing S3 Batch Operations job's priority.
- [UpdateJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html): Updates the status for the specified job.
- [UpdateStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateStorageLensGroup.html): Updates the existing Storage Lens group.

### [Amazon S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_on_Outposts.html)

The following actions are supported by Amazon S3 on Outposts:

- [CreateEndpoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html): Creates an endpoint and associates it with the specified Outpost.
- [DeleteEndpoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html): Deletes an endpoint.
- [ListEndpoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListEndpoints.html): Lists endpoints associated with the specified Outpost.
- [ListOutpostsWithS3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListOutpostsWithS3.html): Lists the Outposts with S3 on Outposts capacity for your AWS account.
- [ListSharedEndpoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListSharedEndpoints.html): Lists all endpoints associated with an Outpost that has been shared by AWS Resource Access Manager (RAM).

### [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html)

The following actions are supported by Amazon S3 Tables:

- [CreateNamespace](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateNamespace.html): Creates a namespace.
- [CreateTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateTable.html): Creates a new table associated with the given namespace in a table bucket.
- [CreateTableBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateTableBucket.html): Creates a table bucket.
- [DeleteNamespace](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteNamespace.html): Deletes a namespace.
- [DeleteTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTable.html): Deletes a table.
- [DeleteTableBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucket.html): Deletes a table bucket.
- [DeleteTableBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucketEncryption.html): Deletes the encryption configuration for a table bucket.
- [DeleteTableBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucketMetricsConfiguration.html): Deletes the metrics configuration for a table bucket.
- [DeleteTableBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucketPolicy.html): Deletes a table bucket policy.
- [DeleteTableBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucketReplication.html): Deletes the replication configuration for a table bucket.
- [DeleteTablePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTablePolicy.html): Deletes a table policy.
- [DeleteTableReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableReplication.html): Deletes the replication configuration for a specific table.
- [GetNamespace](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetNamespace.html): Gets details about a namespace.
- [GetTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTable.html): Gets details about a table.
- [GetTableBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucket.html): Gets details on a table bucket.
- [GetTableBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketEncryption.html): Gets the encryption configuration for a table bucket.
- [GetTableBucketMaintenanceConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketMaintenanceConfiguration.html): Gets details about a maintenance configuration for a given table bucket.
- [GetTableBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketMetricsConfiguration.html): Gets the metrics configuration for a table bucket.
- [GetTableBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketPolicy.html): Gets details about a table bucket policy.
- [GetTableBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketReplication.html): Retrieves the replication configuration for a table bucket.This operation returns the IAM role, versionToken, and replication rules that define how tables in this bucket are replicated to other buckets.
- [GetTableBucketStorageClass](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketStorageClass.html): Retrieves the storage class configuration for a specific table.
- [GetTableEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableEncryption.html): Gets the encryption configuration for a table.
- [GetTableMaintenanceConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableMaintenanceConfiguration.html): Gets details about the maintenance configuration of a table.
- [GetTableMaintenanceJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableMaintenanceJobStatus.html): Gets the status of a maintenance job for a table.
- [GetTableMetadataLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableMetadataLocation.html): Gets the location of the table metadata.
- [GetTablePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTablePolicy.html): Gets details about a table policy.
- [GetTableRecordExpirationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableRecordExpirationConfiguration.html): Retrieves the expiration configuration settings for records in a table, and the status of the configuration.
- [GetTableRecordExpirationJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableRecordExpirationJobStatus.html): Retrieves the status, metrics, and details of the latest record expiration job for a table.
- [GetTableReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableReplication.html): Retrieves the replication configuration for a specific table.
- [GetTableReplicationStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableReplicationStatus.html): Retrieves the replication status for a table, including the status of replication to each destination.
- [GetTableStorageClass](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableStorageClass.html): Retrieves the storage class configuration for a specific table.
- [ListNamespaces](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListNamespaces.html): Lists the namespaces within a table bucket.
- [ListTableBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListTableBuckets.html): Lists table buckets for your account.
- [ListTables](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListTables.html): List tables in the given table bucket.
- [ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListTagsForResource.html): Lists all of the tags applied to a specified Amazon S3 Tables resource.
- [PutTableBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketEncryption.html): Sets the encryption configuration for a table bucket.
- [PutTableBucketMaintenanceConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketMaintenanceConfiguration.html): Creates a new maintenance configuration or replaces an existing maintenance configuration for a table bucket.
- [PutTableBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketMetricsConfiguration.html): Sets the metrics configuration for a table bucket.
- [PutTableBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketPolicy.html): Creates a new table bucket policy or replaces an existing table bucket policy for a table bucket.
- [PutTableBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketReplication.html): Creates or updates the replication configuration for a table bucket.
- [PutTableBucketStorageClass](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketStorageClass.html): Sets or updates the storage class configuration for a table bucket.
- [PutTableMaintenanceConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableMaintenanceConfiguration.html): Creates a new maintenance configuration or replaces an existing maintenance configuration for a table.
- [PutTablePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTablePolicy.html): Creates a new table policy or replaces an existing table policy for a table.
- [PutTableRecordExpirationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableRecordExpirationConfiguration.html): Creates or updates the expiration configuration settings for records in a table, including the status of the configuration.
- [PutTableReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableReplication.html): Creates or updates the replication configuration for a specific table.
- [RenameTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_RenameTable.html): Renames a table or a namespace.
- [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TagResource.html): Applies one or more user-defined tags to an Amazon S3 Tables resource or updates existing tags.
- [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_UntagResource.html): Removes the specified user-defined tags from an Amazon S3 Tables resource.
- [UpdateTableMetadataLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_UpdateTableMetadataLocation.html): Updates the metadata location for a table.

### [Amazon S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Vectors.html)

The following actions are supported by Amazon S3 Vectors:

- [CreateIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateIndex.html): Creates a vector index within a vector bucket.
- [CreateVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateVectorBucket.html): Creates a vector bucket in the AWS Region that you want your bucket to be in.
- [DeleteIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteIndex.html): Deletes a vector index.
- [DeleteVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectorBucket.html): Deletes a vector bucket.
- [DeleteVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectorBucketPolicy.html): Deletes a vector bucket policy.
- [DeleteVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectors.html): Deletes one or more vectors in a vector index.
- [GetIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetIndex.html): Returns vector index attributes.
- [GetVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucket.html): Returns vector bucket attributes.
- [GetVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucketPolicy.html): Gets details about a vector bucket policy.
- [GetVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectors.html): Returns vector attributes.
- [ListIndexes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListIndexes.html): Returns a list of all the vector indexes within the specified vector bucket.
- [ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListTagsForResource.html): Lists all of the tags applied to a specified Amazon S3 Vectors resource.
- [ListVectorBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectorBuckets.html): Returns a list of all the vector buckets that are owned by the authenticated sender of the request.
- [ListVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectors.html): List vectors in the specified vector index.
- [PutVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectorBucketPolicy.html): Creates a bucket policy for a vector bucket.
- [PutVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectors.html): Adds one or more vectors to a vector index.
- [QueryVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryVectors.html): Performs an approximate nearest neighbor search query in a vector index using a query vector.
- [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_TagResource.html): Applies one or more user-defined tags to an Amazon S3 Vectors resource or updates existing tags.
- [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_UntagResource.html): Removes the specified user-defined tags from an Amazon S3 Vectors resource.

### [Data Types](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types.html)

The following data types are supported by Amazon S3:

### [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_Amazon_Simple_Storage_Service.html)

The following data types are supported by Amazon S3:

- [AbacStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbacStatus.html): The ABAC status of the general purpose bucket.
- [AbortIncompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortIncompleteMultipartUpload.html): Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload.
- [AccelerateConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AccelerateConfiguration.html): Configures the transfer acceleration state for an Amazon S3 bucket.
- [AccessControlPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AccessControlPolicy.html): Contains the elements that set the ACL permissions for an object per grantee.
- [AccessControlTranslation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AccessControlTranslation.html): A container for information about access control for replicas.
- [AnalyticsAndOperator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnalyticsAndOperator.html): A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter.
- [AnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnalyticsConfiguration.html): Specifies the configuration and any analyses for the analytics filter of an Amazon S3 bucket.
- [AnalyticsExportDestination](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnalyticsExportDestination.html): Where to publish the analytics results.
- [AnalyticsFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnalyticsFilter.html): The filter used to describe a set of objects for analyses.
- [AnalyticsS3BucketDestination](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnalyticsS3BucketDestination.html): Contains information about where to publish the analytics results.
- [BlockedEncryptionTypes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_BlockedEncryptionTypes.html): A bucket-level setting for Amazon S3 general purpose buckets used to prevent the upload of new objects encrypted with the specified server-side encryption type.
- [Bucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Bucket.html): In terms of implementation, a Bucket is a resource.
- [BucketInfo](https://docs.aws.amazon.com/AmazonS3/latest/API/API_BucketInfo.html): Specifies the information about the bucket that will be created.
- [BucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_BucketLifecycleConfiguration.html): Specifies the lifecycle configuration for objects in an Amazon S3 bucket.
- [BucketLoggingStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_BucketLoggingStatus.html): Container for logging status information.
- [Checksum](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Checksum.html): Contains all the possible checksum or digest values for an object.
- [CloudFunctionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CloudFunctionConfiguration.html): Container for specifying the AWS Lambda notification configuration.
- [CommonPrefix](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CommonPrefix.html): Container for all (if there are any) keys between Prefix and the next occurrence of the string specified by a delimiter.
- [CompletedMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompletedMultipartUpload.html): The container for the completed multipart upload details.
- [CompletedPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompletedPart.html): Details of the parts that were uploaded.
- [Condition](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Condition.html): A container for describing a condition that must be met for the specified redirect to apply.
- [ContinuationEvent](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ContinuationEvent.html)
- [CopyObjectResult](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObjectResult.html): Container for all response elements.
- [CopyPartResult](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyPartResult.html): Container for all response elements.
- [CORSConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CORSConfiguration.html): Describes the cross-origin access configuration for objects in an Amazon S3 bucket.
- [CORSRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CORSRule.html): Specifies a cross-origin access rule for an Amazon S3 bucket.
- [CreateBucketConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketConfiguration.html): The configuration information for the bucket.
- [CSVInput](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CSVInput.html): Describes how an uncompressed comma-separated values (CSV)-formatted input object is formatted.
- [CSVOutput](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CSVOutput.html): Describes how uncompressed comma-separated values (CSV)-formatted results are formatted.
- [DefaultRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DefaultRetention.html): The container element for optionally specifying the default Object Lock retention settings for new objects placed in the specified bucket.
- [Delete](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Delete.html): Container for the objects to delete.
- [DeletedObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletedObject.html): Information about the deleted object.
- [DeleteMarkerEntry](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteMarkerEntry.html): Information about the delete marker.
- [DeleteMarkerReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteMarkerReplication.html): Specifies whether Amazon S3 replicates delete markers.
- [Destination](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Destination.html): Specifies information about where to publish analysis or configuration results for an Amazon S3 bucket and S3 Replication Time Control (S3 RTC).
- [DestinationResult](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DestinationResult.html): The destination information for the S3 Metadata configuration.
- [Encryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Encryption.html): Contains the type of server-side encryption used.
- [EncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_EncryptionConfiguration.html): Specifies encryption-related information for an Amazon S3 bucket that is a destination for replicated objects.
- [EndEvent](https://docs.aws.amazon.com/AmazonS3/latest/API/API_EndEvent.html): A message that indicates the request is complete and no more messages will be sent.
- [Error](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Error.html): Container for all error elements.
- [ErrorDetails](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ErrorDetails.html): If an S3 Metadata V1 CreateBucketMetadataTableConfiguration or V2 CreateBucketMetadataConfiguration request succeeds, but S3 Metadata was unable to create the table, this structure contains the error code and error message.
- [ErrorDocument](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ErrorDocument.html): The error information.
- [EventBridgeConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_EventBridgeConfiguration.html): A container for specifying the configuration for Amazon EventBridge.
- [ExistingObjectReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ExistingObjectReplication.html): Optional configuration to replicate existing source bucket objects.
- [FilterRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_FilterRule.html): Specifies the Amazon S3 object key name to filter on.
- [GetBucketMetadataConfigurationResult](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfigurationResult.html): The S3 Metadata configuration for a general purpose bucket.
- [GetBucketMetadataTableConfigurationResult](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfigurationResult.html): The V1 S3 Metadata configuration for a general purpose bucket.
- [GetObjectAttributesParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributesParts.html): A collection of parts associated with a multipart upload.
- [GlacierJobParameters](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GlacierJobParameters.html): Container for S3 Glacier job parameters.
- [Grant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Grant.html): Container for grant information.
- [Grantee](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Grantee.html): Container for the person being granted permissions.
- [IndexDocument](https://docs.aws.amazon.com/AmazonS3/latest/API/API_IndexDocument.html): Container for the Suffix element.
- [Initiator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Initiator.html): Container element that identifies who initiated the multipart upload.
- [InputSerialization](https://docs.aws.amazon.com/AmazonS3/latest/API/API_InputSerialization.html): Describes the serialization format of the object.
- [IntelligentTieringAndOperator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_IntelligentTieringAndOperator.html): A container for specifying S3 Intelligent-Tiering filters.
- [IntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_IntelligentTieringConfiguration.html): Specifies the S3 Intelligent-Tiering configuration for an Amazon S3 bucket.
- [IntelligentTieringFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_IntelligentTieringFilter.html): The Filter is used to identify objects that the S3 Intelligent-Tiering configuration applies to.
- [InventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryConfiguration.html): Specifies the S3 Inventory configuration for an Amazon S3 bucket.
- [InventoryDestination](https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryDestination.html): Specifies the S3 Inventory configuration for an Amazon S3 bucket.
- [InventoryEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryEncryption.html): Contains the type of server-side encryption used to encrypt the S3 Inventory results.
- [InventoryFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryFilter.html): Specifies an S3 Inventory filter.
- [InventoryS3BucketDestination](https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryS3BucketDestination.html): Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where S3 Inventory results are published.
- [InventorySchedule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventorySchedule.html): Specifies the schedule for generating S3 Inventory results.
- [InventoryTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryTableConfiguration.html): The inventory table configuration for an S3 Metadata configuration.
- [InventoryTableConfigurationResult](https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryTableConfigurationResult.html): The inventory table configuration for an S3 Metadata configuration.
- [InventoryTableConfigurationUpdates](https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryTableConfigurationUpdates.html): The specified updates to the S3 Metadata inventory table configuration.
- [JournalTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_JournalTableConfiguration.html): The journal table configuration for an S3 Metadata configuration.
- [JournalTableConfigurationResult](https://docs.aws.amazon.com/AmazonS3/latest/API/API_JournalTableConfigurationResult.html): The journal table configuration for the S3 Metadata configuration.
- [JournalTableConfigurationUpdates](https://docs.aws.amazon.com/AmazonS3/latest/API/API_JournalTableConfigurationUpdates.html): The specified updates to the S3 Metadata journal table configuration.
- [JSONInput](https://docs.aws.amazon.com/AmazonS3/latest/API/API_JSONInput.html): Specifies JSON as object's input serialization format.
- [JSONOutput](https://docs.aws.amazon.com/AmazonS3/latest/API/API_JSONOutput.html): Specifies JSON as request's output serialization format.
- [LambdaFunctionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_LambdaFunctionConfiguration.html): A container for specifying the configuration for AWS Lambda notifications.
- [LifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_LifecycleConfiguration.html): Container for lifecycle rules.
- [LifecycleExpiration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_LifecycleExpiration.html): Container for the expiration for the lifecycle of the object.
- [LifecycleRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_LifecycleRule.html): A lifecycle rule for individual objects in an Amazon S3 bucket.
- [LifecycleRuleAndOperator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_LifecycleRuleAndOperator.html): This is used in a Lifecycle Rule Filter to apply a logical AND to two or more predicates.
- [LifecycleRuleFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_LifecycleRuleFilter.html): The Filter is used to identify objects that a Lifecycle Rule applies to.
- [LocationInfo](https://docs.aws.amazon.com/AmazonS3/latest/API/API_LocationInfo.html): Specifies the location where the bucket will be created.
- [LoggingEnabled](https://docs.aws.amazon.com/AmazonS3/latest/API/API_LoggingEnabled.html): Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a bucket.
- [MetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetadataConfiguration.html): The S3 Metadata configuration for a general purpose bucket.
- [MetadataConfigurationResult](https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetadataConfigurationResult.html): The S3 Metadata configuration for a general purpose bucket.
- [MetadataEntry](https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetadataEntry.html): A metadata key-value pair to store with an object.
- [MetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetadataTableConfiguration.html): The V1 S3 Metadata configuration for a general purpose bucket.
- [MetadataTableConfigurationResult](https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetadataTableConfigurationResult.html): The V1 S3 Metadata configuration for a general purpose bucket.
- [MetadataTableEncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetadataTableEncryptionConfiguration.html): The encryption settings for an S3 Metadata journal table or inventory table configuration.
- [Metrics](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Metrics.html): A container specifying replication metrics-related settings enabling replication metrics and events.
- [MetricsAndOperator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetricsAndOperator.html): A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter.
- [MetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetricsConfiguration.html): Specifies a metrics configuration for the CloudWatch request metrics (specified by the metrics configuration ID) from an Amazon S3 bucket.
- [MetricsFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetricsFilter.html): Specifies a metrics configuration filter.
- [MultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_MultipartUpload.html): Container for the MultipartUpload for the Amazon S3 object.
- [NoncurrentVersionExpiration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_NoncurrentVersionExpiration.html): Specifies when noncurrent object versions expire.
- [NoncurrentVersionTransition](https://docs.aws.amazon.com/AmazonS3/latest/API/API_NoncurrentVersionTransition.html): Container for the transition rule that describes when noncurrent objects transition to the STANDARD_IA, ONEZONE_IA, INTELLIGENT_TIERING, GLACIER_IR, GLACIER, or DEEP_ARCHIVE storage class.
- [NotificationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_NotificationConfiguration.html): A container for specifying the notification configuration of the bucket.
- [NotificationConfigurationDeprecated](https://docs.aws.amazon.com/AmazonS3/latest/API/API_NotificationConfigurationDeprecated.html)
- [NotificationConfigurationFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_NotificationConfigurationFilter.html): Specifies object key name filtering rules.
- [Object](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Object.html): An object consists of data and its descriptive metadata.
- [ObjectEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectEncryption.html): The updated server-side encryption type for this object.
- [ObjectIdentifier](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectIdentifier.html): Object Identifier is unique value to identify objects.
- [ObjectLockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectLockConfiguration.html): The container element for Object Lock configuration parameters.
- [ObjectLockLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectLockLegalHold.html): A legal hold configuration for an object.
- [ObjectLockRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectLockRetention.html): A Retention configuration for an object.
- [ObjectLockRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectLockRule.html): The container element for an Object Lock rule.
- [ObjectPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectPart.html): A container for elements related to an individual part.
- [ObjectVersion](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectVersion.html): The version of an object.
- [OutputLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_OutputLocation.html): Describes the location where the restore job's output is stored.
- [OutputSerialization](https://docs.aws.amazon.com/AmazonS3/latest/API/API_OutputSerialization.html): Describes how results of the Select job are serialized.
- [Owner](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Owner.html): Container for the owner's display name and ID.
- [OwnershipControls](https://docs.aws.amazon.com/AmazonS3/latest/API/API_OwnershipControls.html): The container element for a bucket's ownership controls.
- [OwnershipControlsRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_OwnershipControlsRule.html): The container element for an ownership control rule.
- [ParquetInput](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ParquetInput.html): Container for Parquet.
- [Part](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Part.html): Container for elements related to a part.
- [PartitionedPrefix](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PartitionedPrefix.html): Amazon S3 keys for log objects are partitioned in the following format:
- [PolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PolicyStatus.html): The container element for a bucket's policy status.
- [Progress](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Progress.html): This data type contains information about progress of an operation.
- [ProgressEvent](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ProgressEvent.html): This data type contains information about the progress event of an operation.
- [PublicAccessBlockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PublicAccessBlockConfiguration.html): The PublicAccessBlock configuration that you want to apply to this Amazon S3 bucket.
- [QueueConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_QueueConfiguration.html): Specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.
- [QueueConfigurationDeprecated](https://docs.aws.amazon.com/AmazonS3/latest/API/API_QueueConfigurationDeprecated.html): This data type is deprecated.
- [RecordExpiration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RecordExpiration.html): The journal table record expiration settings for a journal table in an S3 Metadata configuration.
- [RecordsEvent](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RecordsEvent.html): The container for the records event.
- [Redirect](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Redirect.html): Specifies how requests are redirected.
- [RedirectAllRequestsTo](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RedirectAllRequestsTo.html): Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket.
- [ReplicaModifications](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ReplicaModifications.html): A filter that you can specify for selection for modifications on replicas.
- [ReplicationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ReplicationConfiguration.html): A container for replication rules.
- [ReplicationRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ReplicationRule.html): Specifies which Amazon S3 objects to replicate and where to store the replicas.
- [ReplicationRuleAndOperator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ReplicationRuleAndOperator.html): A container for specifying rule filters.
- [ReplicationRuleFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ReplicationRuleFilter.html): A filter that identifies the subset of objects to which the replication rule applies.
- [ReplicationTime](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ReplicationTime.html): A container specifying S3 Replication Time Control (S3 RTC) related information, including whether S3 RTC is enabled and the time when all objects and operations on objects must be replicated.
- [ReplicationTimeValue](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ReplicationTimeValue.html): A container specifying the time value for S3 Replication Time Control (S3 RTC) and replication metrics EventThreshold.
- [RequestPaymentConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RequestPaymentConfiguration.html): Container for Payer.
- [RequestProgress](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RequestProgress.html): Container for specifying if periodic QueryProgress messages should be sent.
- [RestoreRequest](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreRequest.html): Container for restore job parameters.
- [RestoreStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreStatus.html): Specifies the restoration status of an object.
- [RoutingRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RoutingRule.html): Specifies the redirect behavior and when a redirect is applied.
- [Rule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Rule.html): Specifies lifecycle rules for an Amazon S3 bucket.
- [S3KeyFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3KeyFilter.html): A container for object key name prefix and suffix filtering rules.
- [S3Location](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Location.html): Describes an Amazon S3 location that will receive the results of the restore request.
- [S3TablesDestination](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3TablesDestination.html): The destination information for a V1 S3 Metadata configuration.
- [S3TablesDestinationResult](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3TablesDestinationResult.html): The destination information for a V1 S3 Metadata configuration.
- [ScanRange](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ScanRange.html): Specifies the byte range of the object to get the records from.
- [SelectObjectContentEventStream](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SelectObjectContentEventStream.html): The container for selecting objects from a content event stream.
- [SelectParameters](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SelectParameters.html)
- [ServerSideEncryptionByDefault](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ServerSideEncryptionByDefault.html): Describes the default server-side encryption to apply to new objects in the bucket.
- [ServerSideEncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ServerSideEncryptionConfiguration.html): Specifies the default server-side-encryption configuration.
- [ServerSideEncryptionRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ServerSideEncryptionRule.html): Specifies the default server-side encryption configuration.
- [SessionCredentials](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SessionCredentials.html): The established temporary security credentials of the session.
- [SimplePrefix](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SimplePrefix.html): To use simple format for S3 keys for log objects, set SimplePrefix to an empty object.
- [SourceSelectionCriteria](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SourceSelectionCriteria.html): A container that describes additional filters for identifying the source objects that you want to replicate.
- [SSEKMS](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SSEKMS.html): Specifies the use of SSE-KMS to encrypt delivered inventory reports.
- [SseKmsEncryptedObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SseKmsEncryptedObjects.html): A container for filter information for the selection of S3 objects encrypted with AWS KMS.
- [SSEKMSEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SSEKMSEncryption.html): If SSEKMS is specified for ObjectEncryption, this data type specifies the AWS KMS key Amazon Resource Name (ARN) to use and whether to use an S3 Bucket Key for server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS).
- [SSES3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SSES3.html): Specifies the use of SSE-S3 to encrypt delivered inventory reports.
- [Stats](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Stats.html): Container for the stats details.
- [StatsEvent](https://docs.aws.amazon.com/AmazonS3/latest/API/API_StatsEvent.html): Container for the Stats Event.
- [StorageClassAnalysis](https://docs.aws.amazon.com/AmazonS3/latest/API/API_StorageClassAnalysis.html): Specifies data related to access patterns to be collected and made available to analyze the tradeoffs between different storage classes for an Amazon S3 bucket.
- [StorageClassAnalysisDataExport](https://docs.aws.amazon.com/AmazonS3/latest/API/API_StorageClassAnalysisDataExport.html): Container for data related to the storage class analysis for an Amazon S3 bucket for export.
- [Tag](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Tag.html): A container of a key value name pair.
- [Tagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Tagging.html): Container for TagSet elements.
- [TargetGrant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_TargetGrant.html): Container for granting information.
- [TargetObjectKeyFormat](https://docs.aws.amazon.com/AmazonS3/latest/API/API_TargetObjectKeyFormat.html): Amazon S3 key format for log objects.
- [Tiering](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Tiering.html): The S3 Intelligent-Tiering storage class is designed to optimize storage costs by automatically moving data to the most cost-effective storage access tier, without additional operational overhead.
- [TopicConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_TopicConfiguration.html): A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
- [TopicConfigurationDeprecated](https://docs.aws.amazon.com/AmazonS3/latest/API/API_TopicConfigurationDeprecated.html): A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
- [Transition](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Transition.html): Specifies when an object transitions to a specified storage class.
- [VersioningConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_VersioningConfiguration.html): Describes the versioning state of an Amazon S3 bucket.
- [WebsiteConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_WebsiteConfiguration.html): Specifies website configuration parameters for an Amazon S3 bucket.

### [Amazon S3 Control](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_AWS_S3_Control.html)

The following data types are supported by Amazon S3 Control:

- [AbortIncompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AbortIncompleteMultipartUpload.html): The container for abort incomplete multipart upload
- [AccessControlTranslation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AccessControlTranslation.html): A container for information about access control for replicas.
- [AccessGrantsLocationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AccessGrantsLocationConfiguration.html): The configuration options of the S3 Access Grants location.
- [AccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AccessPoint.html): An access point used to access a bucket.
- [AccountLevel](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AccountLevel.html): A container element for the account-level Amazon S3 Storage Lens configuration.
- [ActivityMetrics](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ActivityMetrics.html): The container element for Amazon S3 Storage Lens activity metrics.
- [AdvancedCostOptimizationMetrics](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AdvancedCostOptimizationMetrics.html): The container element for Amazon S3 Storage Lens advanced cost-optimization metrics.
- [AdvancedDataProtectionMetrics](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AdvancedDataProtectionMetrics.html): The container element for Amazon S3 Storage Lens advanced data-protection metrics.
- [AdvancedPerformanceMetrics](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AdvancedPerformanceMetrics.html): The container element for S3 Storage Lens advanced performance metrics.
- [AsyncErrorDetails](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AsyncErrorDetails.html): Error details for the failed asynchronous operation.
- [AsyncOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AsyncOperation.html): A container for the information about an asynchronous operation.
- [AsyncRequestParameters](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AsyncRequestParameters.html): A container for the request parameters associated with an asynchronous request.
- [AsyncResponseDetails](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AsyncResponseDetails.html): A container for the response details that are returned when querying about an asynchronous request.
- [AwsLambdaTransformation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AwsLambdaTransformation.html): AWS Lambda function used to transform objects through an Object Lambda Access Point.
- [BucketLevel](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_BucketLevel.html): A container for the bucket-level configuration for Amazon S3 Storage Lens.
- [CloudWatchMetrics](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CloudWatchMetrics.html): A container for enabling Amazon CloudWatch publishing for S3 Storage Lens metrics.
- [CreateBucketConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucketConfiguration.html): The container for the bucket configuration.
- [CreateMultiRegionAccessPointInput](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPointInput.html): A container for the information associated with a CreateMultiRegionAccessPoint request.
- [Credentials](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Credentials.html): The AWS Security Token Service temporary credential that S3 Access Grants vends to grantees and client applications.
- [DeleteMarkerReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMarkerReplication.html): Specifies whether S3 on Outposts replicates delete markers.
- [DeleteMultiRegionAccessPointInput](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPointInput.html): A container for the information associated with a DeleteMultiRegionAccessPoint request.
- [Destination](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Destination.html): Specifies information about the replication destination bucket and its settings for an S3 on Outposts replication configuration.
- [DetailedStatusCodesMetrics](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DetailedStatusCodesMetrics.html): The container element for Amazon S3 Storage Lens detailed status code metrics.
- [DSSEKMSFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DSSEKMSFilter.html): A filter that returns objects that are encrypted by dual-layer server-side encryption with AWS Key Management Service (KMS) keys (DSSE-KMS).
- [EncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_EncryptionConfiguration.html): Specifies encryption-related information for an Amazon S3 bucket that is a destination for replicated objects.
- [EstablishedMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_EstablishedMultiRegionAccessPointPolicy.html): The last established access control policy for a Multi-Region Access Point.
- [Exclude](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Exclude.html): A container for what Amazon S3 Storage Lens will exclude.
- [ExistingObjectReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ExistingObjectReplication.html): An optional configuration to replicate existing source bucket objects.
- [GeneratedManifestEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GeneratedManifestEncryption.html): The encryption configuration to use when storing the generated manifest.
- [Grantee](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Grantee.html): The user, group, or role to which you are granting access.
- [Include](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Include.html): A container for what Amazon S3 Storage Lens configuration includes.
- [JobDescriptor](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobDescriptor.html): A container element for the job configuration and status information returned by a Describe Job request.
- [JobFailure](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobFailure.html): If this job failed, this element indicates why the job failed.
- [JobListDescriptor](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobListDescriptor.html): Contains the configuration and status information for a single job retrieved as part of a job list.
- [JobManifest](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobManifest.html): Contains the configuration information for a job's manifest.
- [JobManifestGenerator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobManifestGenerator.html): Configures the type of the job's ManifestGenerator.
- [JobManifestGeneratorFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobManifestGeneratorFilter.html): The filter used to describe a set of objects for the job's manifest.
- [JobManifestLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobManifestLocation.html): Contains the information required to locate a manifest object.
- [JobManifestSpec](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobManifestSpec.html): Describes the format of a manifest.
- [JobOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobOperation.html): The operation that you want this job to perform on every object listed in the manifest.
- [JobProgressSummary](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobProgressSummary.html): Describes the total number of tasks that the specified job has started, the number of tasks that succeeded, and the number of tasks that failed.
- [JobReport](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobReport.html): Contains the configuration parameters for a job-completion report.
- [JobTimers](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobTimers.html): Provides timing details for the job.
- [KeyNameConstraint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_KeyNameConstraint.html): If provided, the generated manifest includes only source bucket objects whose object keys match the string constraints specified for MatchAnyPrefix, MatchAnySuffix, and MatchAnySubstring.
- [LambdaInvokeOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_LambdaInvokeOperation.html): Contains the configuration parameters for a Lambda Invoke operation.
- [LifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_LifecycleConfiguration.html): The container for the Outposts bucket lifecycle configuration.
- [LifecycleExpiration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_LifecycleExpiration.html): The container of the Outposts bucket lifecycle expiration.
- [LifecycleRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_LifecycleRule.html): The container for the Outposts bucket lifecycle rule.
- [LifecycleRuleAndOperator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_LifecycleRuleAndOperator.html): The container for the Outposts bucket lifecycle rule and operator.
- [LifecycleRuleFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_LifecycleRuleFilter.html): The container for the filter of the lifecycle rule.
- [ListAccessGrantEntry](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantEntry.html): Information about the access grant.
- [ListAccessGrantsInstanceEntry](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsInstanceEntry.html): Information about the S3 Access Grants instance.
- [ListAccessGrantsLocationsEntry](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsLocationsEntry.html): A container for information about the registered location.
- [ListCallerAccessGrantsEntry](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListCallerAccessGrantsEntry.html): Part of ListCallerAccessGrantsResult.
- [ListStorageLensConfigurationEntry](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensConfigurationEntry.html): Part of ListStorageLensConfigurationResult.
- [ListStorageLensGroupEntry](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensGroupEntry.html): Each entry contains a Storage Lens group that exists in the specified home Region.
- [MatchObjectAge](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_MatchObjectAge.html): A filter condition that specifies the object age range of included objects in days.
- [MatchObjectSize](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_MatchObjectSize.html): A filter condition that specifies the object size range of included objects in bytes.
- [Metrics](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Metrics.html): A container that specifies replication metrics-related settings.
- [MultiRegionAccessPointPolicyDocument](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_MultiRegionAccessPointPolicyDocument.html): The Multi-Region Access Point access control policy.
- [MultiRegionAccessPointRegionalResponse](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_MultiRegionAccessPointRegionalResponse.html): Status information for a single Multi-Region Access Point Region.
- [MultiRegionAccessPointReport](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_MultiRegionAccessPointReport.html): A collection of statuses for a Multi-Region Access Point in the various Regions it supports.
- [MultiRegionAccessPointRoute](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_MultiRegionAccessPointRoute.html): A structure for a Multi-Region Access Point that indicates where Amazon S3 traffic can be routed.
- [MultiRegionAccessPointsAsyncResponse](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_MultiRegionAccessPointsAsyncResponse.html): The Multi-Region Access Point details that are returned when querying about an asynchronous request.
- [NoncurrentVersionExpiration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_NoncurrentVersionExpiration.html): The container of the noncurrent version expiration.
- [NoncurrentVersionTransition](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_NoncurrentVersionTransition.html): The container for the noncurrent version transition.
- [NotSSEFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_NotSSEFilter.html): A filter that returns objects that aren't server-side encrypted.
- [ObjectEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectEncryption.html): The updated server-side encryption type for this object.
- [ObjectEncryptionFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectEncryptionFilter.html): An optional filter for the S3JobManifestGenerator that identifies the subset of objects by encryption type.
- [ObjectLambdaAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectLambdaAccessPoint.html): An access point with an attached AWS Lambda function used to access transformed data from an Amazon S3 bucket.
- [ObjectLambdaAccessPointAlias](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectLambdaAccessPointAlias.html): The alias of an Object Lambda Access Point.
- [ObjectLambdaConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectLambdaConfiguration.html): A configuration used when creating an Object Lambda Access Point.
- [ObjectLambdaContentTransformation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectLambdaContentTransformation.html): A container for AwsLambdaTransformation.
- [ObjectLambdaTransformationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectLambdaTransformationConfiguration.html): A configuration used when creating an Object Lambda Access Point transformation.
- [PolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PolicyStatus.html): Indicates whether this access point policy is public.
- [PrefixLevel](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PrefixLevel.html): A container for the prefix-level configuration.
- [PrefixLevelStorageMetrics](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PrefixLevelStorageMetrics.html): A container for the prefix-level storage metrics for S3 Storage Lens.
- [ProposedMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ProposedMultiRegionAccessPointPolicy.html): The proposed access control policy for the Multi-Region Access Point.
- [PublicAccessBlockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PublicAccessBlockConfiguration.html): The PublicAccessBlock configuration that you want to apply to this Amazon S3 account.
- [PutMultiRegionAccessPointPolicyInput](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicyInput.html): A container for the information associated with a PutMultiRegionAccessPoint request.
- [Region](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Region.html): A Region that supports a Multi-Region Access Point as well as the associated bucket for the Region.
- [RegionalBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_RegionalBucket.html): The container for the regional bucket.
- [RegionReport](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_RegionReport.html): A combination of a bucket and Region that's part of a Multi-Region Access Point.
- [ReplicaModifications](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ReplicaModifications.html): A filter that you can use to specify whether replica modification sync is enabled.
- [ReplicationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ReplicationConfiguration.html): A container for one or more replication rules.
- [ReplicationRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ReplicationRule.html): Specifies which S3 on Outposts objects to replicate and where to store the replicas.
- [ReplicationRuleAndOperator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ReplicationRuleAndOperator.html): A container for specifying rule filters.
- [ReplicationRuleFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ReplicationRuleFilter.html): A filter that identifies the subset of objects to which the replication rule applies.
- [ReplicationTime](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ReplicationTime.html): A container that specifies S3 Replication Time Control (S3 RTC) related information, including whether S3 RTC is enabled and the time when all objects and operations on objects must be replicated.
- [ReplicationTimeValue](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ReplicationTimeValue.html): A container that specifies the time value for S3 Replication Time Control (S3 RTC).
- [S3AccessControlList](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3AccessControlList.html)
- [S3AccessControlPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3AccessControlPolicy.html)
- [S3BucketDestination](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3BucketDestination.html): A container for the bucket where the Amazon S3 Storage Lens metrics export files are located.
- [S3ComputeObjectChecksumOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3ComputeObjectChecksumOperation.html): Directs the specified job to invoke the ComputeObjectChecksum operation on every object listed in the job's manifest.
- [S3CopyObjectOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3CopyObjectOperation.html): Contains the configuration parameters for a PUT Copy object operation.
- [S3DeleteObjectTaggingOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3DeleteObjectTaggingOperation.html): Contains no configuration parameters because the DELETE Object tagging (DeleteObjectTagging) API operation accepts only the bucket name and key name as parameters, which are defined in the job's manifest.
- [S3GeneratedManifestDescriptor](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3GeneratedManifestDescriptor.html): Describes the specified job's generated manifest.
- [S3Grant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3Grant.html)
- [S3Grantee](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3Grantee.html)
- [S3InitiateRestoreObjectOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3InitiateRestoreObjectOperation.html): Contains the configuration parameters for a POST Object restore job.
- [S3JobManifestGenerator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3JobManifestGenerator.html): The container for the service that will create the S3 manifest.
- [S3ManifestOutputLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3ManifestOutputLocation.html): Location details for where the generated manifest should be written.
- [S3ObjectLockLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3ObjectLockLegalHold.html): Whether S3 Object Lock legal hold will be applied to objects in an S3 Batch Operations job.
- [S3ObjectMetadata](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3ObjectMetadata.html)
- [S3ObjectOwner](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3ObjectOwner.html)
- [S3ReplicateObjectOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3ReplicateObjectOperation.html): Directs the specified job to invoke ReplicateObject on every object in the job's manifest.
- [S3Retention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3Retention.html): Contains the S3 Object Lock retention mode to be applied to all objects in the S3 Batch Operations job.
- [S3SetObjectAclOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3SetObjectAclOperation.html): Contains the configuration parameters for a PUT Object ACL operation.
- [S3SetObjectLegalHoldOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3SetObjectLegalHoldOperation.html): Contains the configuration for an S3 Object Lock legal hold operation that an S3 Batch Operations job passes to every object to the underlying PutObjectLegalHold API operation.
- [S3SetObjectRetentionOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3SetObjectRetentionOperation.html): Contains the configuration parameters for the Object Lock retention action for an S3 Batch Operations job.
- [S3SetObjectTaggingOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3SetObjectTaggingOperation.html): Contains the configuration parameters for a PUT Object Tagging operation.
- [S3Tag](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3Tag.html): A container for a key-value name pair.
- [S3UpdateObjectEncryptionOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3UpdateObjectEncryptionOperation.html): With the UpdateObjectEncryption operation, you can atomically update the server-side encryption type of an existing object in a general purpose bucket without any data movement.
- [S3UpdateObjectEncryptionSSEKMS](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3UpdateObjectEncryptionSSEKMS.html): If SSEKMS is specified for UpdateObjectEncryption, this data type specifies the AWS KMS key Amazon Resource Name (ARN) to use and whether to use an S3 Bucket Key for server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS).
- [Scope](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Scope.html): You can use the access point scope to restrict access to specific prefixes, API operations, or a combination of both.
- [SelectionCriteria](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SelectionCriteria.html)
- [SourceSelectionCriteria](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SourceSelectionCriteria.html): A container that describes additional filters for identifying the source objects that you want to replicate.
- [SSECFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SSECFilter.html): A filter that returns objects that are encrypted by server-side encryption with customer-provided keys (SSE-C).
- [SSEKMS](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SSEKMS.html)
- [SseKmsEncryptedObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SseKmsEncryptedObjects.html): A container for filter information that you can use to select S3 objects that are encrypted with AWS Key Management Service (AWS KMS).
- [SSEKMSEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SSEKMSEncryption.html): Configuration for the use of SSE-KMS to encrypt generated manifest objects.
- [SSEKMSFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SSEKMSFilter.html): A filter that returns objects that are encrypted by server-side encryption with AWS KMS (SSE-KMS).
- [SSES3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SSES3.html)
- [SSES3Encryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SSES3Encryption.html): Configuration for the use of SSE-S3 to encrypt generated manifest objects.
- [SSES3Filter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SSES3Filter.html): A filter that returns objects that are encrypted by server-side encryption with Amazon S3 managed keys (SSE-S3).
- [StorageLensAwsOrg](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensAwsOrg.html): The AWS organization for your S3 Storage Lens.
- [StorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensConfiguration.html): A container for the Amazon S3 Storage Lens configuration.
- [StorageLensDataExport](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensDataExport.html): A container to specify the properties of your S3 Storage Lens metrics export, including the destination, schema, and format.
- [StorageLensDataExportEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensDataExportEncryption.html): A container for the encryption of the S3 Storage Lens metrics exports.
- [StorageLensExpandedPrefixesDataExport](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensExpandedPrefixesDataExport.html): A container for your S3 Storage Lens expanded prefix metrics report configuration.
- [StorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensGroup.html): A custom grouping of objects that include filters for prefixes, suffixes, object tags, object size, or object age.
- [StorageLensGroupAndOperator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensGroupAndOperator.html): A logical operator that allows multiple filter conditions to be joined for more complex comparisons of Storage Lens group data.
- [StorageLensGroupFilter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensGroupFilter.html): The filter element sets the criteria for the Storage Lens group data that is displayed.
- [StorageLensGroupLevel](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensGroupLevel.html): Specifies the Storage Lens groups to include in the Storage Lens group aggregation.
- [StorageLensGroupLevelSelectionCriteria](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensGroupLevelSelectionCriteria.html): Indicates which Storage Lens group ARNs to include or exclude in the Storage Lens group aggregation.
- [StorageLensGroupOrOperator](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensGroupOrOperator.html): A container element for specifying Or rule conditions.
- [StorageLensTableDestination](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensTableDestination.html): A container for configuring your S3 Storage Lens reports to export to read-only S3 table buckets.
- [StorageLensTag](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensTag.html)
- [Tag](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Tag.html): A key-value pair that you use to label your resources.
- [Tagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Tagging.html)
- [Transition](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Transition.html): Specifies when an object transitions to a specified storage class.
- [VersioningConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_VersioningConfiguration.html): Describes the versioning state of an Amazon S3 on Outposts bucket.
- [VpcConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_VpcConfiguration.html): The virtual private cloud (VPC) configuration for an access point.

### [Amazon S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_Amazon_S3_on_Outposts.html)

The following data types are supported by Amazon S3 on Outposts:

- [Endpoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_Endpoint.html): Amazon S3 on Outposts Access Points simplify managing data access at scale for shared datasets in S3 on Outposts.
- [FailedReason](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_FailedReason.html): The failure reason, if any, for a create or delete endpoint operation.
- [NetworkInterface](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_NetworkInterface.html): The container for the network interface.
- [Outpost](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_Outpost.html): Contains the details for the Outpost object.

### [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_Amazon_S3_Tables.html)

The following data types are supported by Amazon S3 Tables:

- [EncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_EncryptionConfiguration.html): Configuration specifying how data should be encrypted.
- [IcebergCompactionSettings](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergCompactionSettings.html): Contains details about the compaction settings for an Iceberg table.
- [IcebergMetadata](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergMetadata.html): Contains details about the metadata for an Iceberg table.
- [IcebergPartitionField](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergPartitionField.html): Defines a single partition field in an Iceberg partition specification.
- [IcebergPartitionSpec](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergPartitionSpec.html): Defines how data in an Iceberg table is partitioned.
- [IcebergSchema](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergSchema.html): Contains details about the schema for an Iceberg table.
- [IcebergSnapshotManagementSettings](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergSnapshotManagementSettings.html): Contains details about the snapshot management settings for an Iceberg table.
- [IcebergSortField](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergSortField.html): Defines a single sort field in an Iceberg sort order specification.
- [IcebergSortOrder](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergSortOrder.html): Defines the sort order for data within an Iceberg table.
- [IcebergUnreferencedFileRemovalSettings](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergUnreferencedFileRemovalSettings.html): Contains details about the unreferenced file removal settings for an Iceberg table bucket.
- [LastSuccessfulReplicatedUpdate](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_LastSuccessfulReplicatedUpdate.html): Contains information about the most recent successful replication update to a destination.
- [ManagedTableInformation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ManagedTableInformation.html): Contains information about tables that are managed by S3 Tables, including replication information for replica tables.
- [NamespaceSummary](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_NamespaceSummary.html): Contains details about a namespace.
- [ReplicationDestination](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ReplicationDestination.html): Specifies a destination table bucket for replication.
- [ReplicationDestinationStatusModel](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ReplicationDestinationStatusModel.html): Contains status information for a replication destination, including the current replication state, last successful update, and any error messages.
- [ReplicationInformation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ReplicationInformation.html): Contains information about the source of a replicated table.
- [SchemaField](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_SchemaField.html): Contains details about a schema field.
- [StorageClassConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_StorageClassConfiguration.html): The configuration details for the storage class of tables or table buckets.
- [TableBucketMaintenanceConfigurationValue](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableBucketMaintenanceConfigurationValue.html): Details about the values that define the maintenance configuration for a table bucket.
- [TableBucketMaintenanceSettings](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableBucketMaintenanceSettings.html): Contains details about the maintenance settings for the table bucket.
- [TableBucketReplicationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableBucketReplicationConfiguration.html): The replication configuration for a table bucket.
- [TableBucketReplicationRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableBucketReplicationRule.html): Defines a rule for replicating tables from a source table bucket to one or more destination table buckets.
- [TableBucketSummary](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableBucketSummary.html): Contains details about a table bucket.
- [TableMaintenanceConfigurationValue](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableMaintenanceConfigurationValue.html): The values that define a maintenance configuration for a table.
- [TableMaintenanceJobStatusValue](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableMaintenanceJobStatusValue.html): Details about the status of a maintenance job.
- [TableMaintenanceSettings](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableMaintenanceSettings.html): Contains details about maintenance settings for the table.
- [TableMetadata](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableMetadata.html): Contains details about the table metadata.
- [TableRecordExpirationConfigurationValue](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableRecordExpirationConfigurationValue.html): The expiration configuration settings for records in a table, and the status of the configuration.
- [TableRecordExpirationJobMetrics](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableRecordExpirationJobMetrics.html): Provides metrics for the record expiration job that most recently ran for a table.
- [TableRecordExpirationSettings](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableRecordExpirationSettings.html): The record expiration setting that specifies when records expire and are automatically removed from a table.
- [TableReplicationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableReplicationConfiguration.html): The replication configuration for an individual table.
- [TableReplicationRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableReplicationRule.html): Defines a rule for replicating a table to one or more destination tables.
- [TableSummary](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableSummary.html): Contains details about a table.

### [Amazon S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_Amazon_S3_Vectors.html)

The following data types are supported by Amazon S3 Vectors:

- [EncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_EncryptionConfiguration.html): The encryption configuration for a vector bucket or index.
- [GetOutputVector](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetOutputVector.html): The attributes of a vector returned by the GetVectors operation.
- [Index](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_Index.html): The attributes of a vector index.
- [IndexSummary](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_IndexSummary.html): Summary information about a vector index.
- [ListOutputVector](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListOutputVector.html): The attributes of a vector returned by the ListVectors operation.
- [MetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_MetadataConfiguration.html): The metadata configuration for a vector index.
- [PutInputVector](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutInputVector.html): The attributes of a vector to add to a vector index.
- [QueryOutputVector](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryOutputVector.html): The attributes of a vector in the approximate nearest neighbor search.
- [ValidationExceptionField](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ValidationExceptionField.html): Contains information about a validation exception.
- [VectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_VectorBucket.html): The attributes of a vector bucket.
- [VectorBucketSummary](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_VectorBucketSummary.html): Summary information about a vector bucket.
- [VectorData](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_VectorData.html): The vector data in different formats.


## [Developing with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/developing-s3.html)

### [Making requests](https://docs.aws.amazon.com/AmazonS3/latest/API/MakingRequests.html)

Send requests to Amazon S3 either anonymously or through authentication that verifies your identity to the service.

### [Making requests over IPv6](https://docs.aws.amazon.com/AmazonS3/latest/API/ipv6-access.html)

Explains how to access Amazon S3 using the IPv6 protocols.

- [Using dual-stack endpoints](https://docs.aws.amazon.com/AmazonS3/latest/API/dual-stack-endpoints.html): Explains how to make requests to Amazon S3 dual-stack endpoints.

### [Making requests using the AWS SDKs](https://docs.aws.amazon.com/AmazonS3/latest/API/MakingAuthenticatedRequests.html)

Make authenticated requests using AWS SDKs to access your AWS resources.

- [Using AWS account or IAM user credentials](https://docs.aws.amazon.com/AmazonS3/latest/API/AuthUsingAcctOrUserCredentials.html): Make requests using your AWS account or IAM user credentials to access your AWS resources.
- [Using IAM user temporary credentials](https://docs.aws.amazon.com/AmazonS3/latest/API/AuthUsingTempSessionToken.html): Make requests using your IAM user temporary security credentials to access your AWS resources using the AWS SDK for Java.
- [Using federated user temporary credentials](https://docs.aws.amazon.com/AmazonS3/latest/API/AuthUsingTempFederationToken.html): Make requests using your temporary security credentials to access your AWS resources.

### [Making requests using the REST API](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTAPI.html)

Make requests to Amazon S3 for accessing objects and buckets using the REST API.

- [Request redirection and the REST API](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTRedirect.html): Process HTTP redirects by using the Amazon S3 REST API.
- [Request routing](https://docs.aws.amazon.com/AmazonS3/latest/API/UsingRouting.html): Describes routing requests and DNS issues to consider when designing your service or application.
- [Using the AWS CLI](https://docs.aws.amazon.com/AmazonS3/latest/API/setup-aws-cli.html): Setting up for the Amazon S3 example walkthroughs.

### [Developing with AWS SDKs](https://docs.aws.amazon.com/AmazonS3/latest/API/sdk-general-information-section.html)

Develop Amazon S3 applications with the AWS SDKs.

- [Specifying the Signature Version in request authentication](https://docs.aws.amazon.com/AmazonS3/latest/API/specify-signature-version.html): Amazon S3 supports only AWS Signature Version 4 in most AWS Regions.
- [Get Amazon S3 request IDs for Support](https://docs.aws.amazon.com/AmazonS3/latest/API/get-request-ids.html): Get Amazon S3 request IDs for contacting Support.
- [Supported S3 object-level API operations for S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/API/developing-s3-tables-APIs.html): The following table includes supported S3 object-level API operations and corresponding headers for S3 Tables.


## [Code examples](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples.html)

### [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3.html)

Code examples that show how to use Amazon S3 with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3_basics.html)

The following code examples show how to use the basics of Amazon S3 with AWS SDKs.

- [Hello Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Hello_section.html): Hello Amazon S3
- [Learn the basics](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_GettingStarted_section.html): Learn the basics of Amazon S3 with an AWS SDK

### [Actions](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3_actions.html)

The following code examples show how to use Amazon S3 with AWS SDKs.

- [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_AbortMultipartUpload_section.html): Use AbortMultipartUpload with an AWS SDK or CLI
- [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_CompleteMultipartUpload_section.html): Use CompleteMultipartUpload with an AWS SDK or CLI
- [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_CopyObject_section.html): Use CopyObject with an AWS SDK or CLI
- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_CreateBucket_section.html): Use CreateBucket with an AWS SDK or CLI
- [CreateMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_CreateMultiRegionAccessPoint_section.html): Use CreateMultiRegionAccessPoint with an AWS SDK
- [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_CreateMultipartUpload_section.html): Use CreateMultipartUpload with an AWS SDK or CLI
- [CreatePresignedPost](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_CreatePresignedPost_section.html): Use CreatePresignedPost with an AWS SDK
- [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteBucket_section.html): Use DeleteBucket with an AWS SDK or CLI
- [DeleteBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteBucketAnalyticsConfiguration_section.html): Use DeleteBucketAnalyticsConfiguration with a CLI
- [DeleteBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteBucketCors_section.html): Use DeleteBucketCors with an AWS SDK or CLI
- [DeleteBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteBucketEncryption_section.html): Use DeleteBucketEncryption with a CLI
- [DeleteBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteBucketInventoryConfiguration_section.html): Use DeleteBucketInventoryConfiguration with a CLI
- [DeleteBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteBucketLifecycle_section.html): Use DeleteBucketLifecycle with an AWS SDK or CLI
- [DeleteBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteBucketMetricsConfiguration_section.html): Use DeleteBucketMetricsConfiguration with a CLI
- [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteBucketPolicy_section.html): Use DeleteBucketPolicy with an AWS SDK or CLI
- [DeleteBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteBucketReplication_section.html): Use DeleteBucketReplication with a CLI
- [DeleteBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteBucketTagging_section.html): Use DeleteBucketTagging with a CLI
- [DeleteBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteBucketWebsite_section.html): Use DeleteBucketWebsite with an AWS SDK or CLI
- [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteObject_section.html): Use DeleteObject with an AWS SDK or CLI
- [DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteObjectTagging_section.html): Use DeleteObjectTagging with a CLI
- [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeleteObjects_section.html): Use DeleteObjects with an AWS SDK or CLI
- [DeletePublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DeletePublicAccessBlock_section.html): Use DeletePublicAccessBlock with a CLI
- [GetBucketAccelerateConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketAccelerateConfiguration_section.html): Use GetBucketAccelerateConfiguration with a CLI
- [GetBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketAcl_section.html): Use GetBucketAcl with an AWS SDK or CLI
- [GetBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketAnalyticsConfiguration_section.html): Use GetBucketAnalyticsConfiguration with a CLI
- [GetBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketCors_section.html): Use GetBucketCors with an AWS SDK or CLI
- [GetBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketEncryption_section.html): Use GetBucketEncryption with an AWS SDK or CLI
- [GetBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketInventoryConfiguration_section.html): Use GetBucketInventoryConfiguration with a CLI
- [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketLifecycleConfiguration_section.html): Use GetBucketLifecycleConfiguration with an AWS SDK or CLI
- [GetBucketLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketLocation_section.html): Use GetBucketLocation with an AWS SDK or CLI
- [GetBucketLogging](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketLogging_section.html): Use GetBucketLogging with a CLI
- [GetBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketMetricsConfiguration_section.html): Use GetBucketMetricsConfiguration with a CLI
- [GetBucketNotification](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketNotification_section.html): Use GetBucketNotification with a CLI
- [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketPolicy_section.html): Use GetBucketPolicy with an AWS SDK or CLI
- [GetBucketPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketPolicyStatus_section.html): Use GetBucketPolicyStatus with a CLI
- [GetBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketReplication_section.html): Use GetBucketReplication with an AWS SDK or CLI
- [GetBucketRequestPayment](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketRequestPayment_section.html): Use GetBucketRequestPayment with a CLI
- [GetBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketTagging_section.html): Use GetBucketTagging with a CLI
- [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketVersioning_section.html): Use GetBucketVersioning with a CLI
- [GetBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetBucketWebsite_section.html): Use GetBucketWebsite with an AWS SDK or CLI
- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetObject_section.html): Use GetObject with an AWS SDK or CLI
- [GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetObjectAcl_section.html): Use GetObjectAcl with an AWS SDK or CLI
- [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetObjectAttributes_section.html): Use GetObjectAttributes with an AWS SDK or CLI
- [GetObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetObjectLegalHold_section.html): Use GetObjectLegalHold with an AWS SDK or CLI
- [GetObjectLockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetObjectLockConfiguration_section.html): Use GetObjectLockConfiguration with an AWS SDK or CLI
- [GetObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetObjectRetention_section.html): Use GetObjectRetention with an AWS SDK or CLI
- [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetObjectTagging_section.html): Use GetObjectTagging with a CLI
- [GetPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetPublicAccessBlock_section.html): Use GetPublicAccessBlock with a CLI
- [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_HeadBucket_section.html): Use HeadBucket with an AWS SDK or CLI
- [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_HeadObject_section.html): Use HeadObject with an AWS SDK or CLI
- [ListBucketAnalyticsConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_ListBucketAnalyticsConfigurations_section.html): Use ListBucketAnalyticsConfigurations with a CLI
- [ListBucketInventoryConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_ListBucketInventoryConfigurations_section.html): Use ListBucketInventoryConfigurations with a CLI
- [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_ListBuckets_section.html): Use ListBuckets with an AWS SDK or CLI
- [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_ListMultipartUploads_section.html): Use ListMultipartUploads with an AWS SDK or CLI
- [ListObjectVersions](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_ListObjectVersions_section.html): Use ListObjectVersions with an AWS SDK or CLI
- [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_ListObjects_section.html): Use ListObjects with a CLI
- [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_ListObjectsV2_section.html): Use ListObjectsV2 with an AWS SDK or CLI
- [PutBucketAccelerateConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketAccelerateConfiguration_section.html): Use PutBucketAccelerateConfiguration with an AWS SDK or CLI
- [PutBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketAcl_section.html): Use PutBucketAcl with an AWS SDK or CLI
- [PutBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketCors_section.html): Use PutBucketCors with an AWS SDK or CLI
- [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketEncryption_section.html): Use PutBucketEncryption with an AWS SDK or CLI
- [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketLifecycleConfiguration_section.html): Use PutBucketLifecycleConfiguration with an AWS SDK or CLI
- [PutBucketLogging](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketLogging_section.html): Use PutBucketLogging with an AWS SDK or CLI
- [PutBucketNotification](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketNotification_section.html): Use PutBucketNotification with a CLI
- [PutBucketNotificationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketNotificationConfiguration_section.html): Use PutBucketNotificationConfiguration with an AWS SDK or CLI
- [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketPolicy_section.html): Use PutBucketPolicy with an AWS SDK or CLI
- [PutBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketReplication_section.html): Use PutBucketReplication with an AWS SDK or CLI
- [PutBucketRequestPayment](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketRequestPayment_section.html): Use PutBucketRequestPayment with a CLI
- [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketTagging_section.html): Use PutBucketTagging with a CLI
- [PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketVersioning_section.html): Use PutBucketVersioning with an AWS SDK or CLI
- [PutBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutBucketWebsite_section.html): Use PutBucketWebsite with an AWS SDK or CLI
- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutObject_section.html): Use PutObject with an AWS SDK or CLI
- [PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutObjectAcl_section.html): Use PutObjectAcl with an AWS SDK or CLI
- [PutObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutObjectLegalHold_section.html): Use PutObjectLegalHold with an AWS SDK or CLI
- [PutObjectLockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutObjectLockConfiguration_section.html): Use PutObjectLockConfiguration with an AWS SDK or CLI
- [PutObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_PutObjectRetention_section.html): Use PutObjectRetention with an AWS SDK or CLI
- [RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_RestoreObject_section.html): Use RestoreObject with an AWS SDK or CLI
- [SelectObjectContent](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_SelectObjectContent_section.html): Use SelectObjectContent with an AWS SDK or CLI
- [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_UploadPart_section.html): Use UploadPart with an AWS SDK or CLI
- [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_UploadPartCopy_section.html): Use UploadPartCopy with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3_scenarios.html)

The following code examples show how to use Amazon S3 with AWS SDKs.

- [Check if a bucket exists](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_DoesBucketExist_section.html): Check if a bucket exists
- [Convert text to speech and back to text](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_cross_Telephone_section.html): Convert text to speech and back to text using an AWS SDK
- [Create a presigned URL](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_PresignedUrl_section.html): Create a presigned URL for Amazon S3 using an AWS SDK
- [Create a serverless application to manage photos](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_cross_PAM_section.html): Create a photo asset management application that lets users manage photos using labels
- [Create a web page that lists Amazon S3 objects](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_ListObjectsWeb_section.html): A web page that lists Amazon S3 objects using an AWS SDK
- [Create an Amazon Textract explorer application](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_cross_TextractExplorer_section.html): Create an Amazon Textract explorer application
- [Delete all objects in a bucket](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_DeleteAllObjects_section.html): Delete all objects in a given Amazon S3 bucket using an AWS SDK
- [Delete incomplete multipart uploads](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_AbortMultipartUpload_section.html): Delete incomplete multipart uploads to Amazon S3 using an AWS SDK
- [Detect PPE in images](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_cross_RekognitionPhotoAnalyzerPPE_section.html): Detect PPE in images with Amazon Rekognition using an AWS SDK
- [Detect entities in text extracted from an image](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_cross_TextractComprehendDetectEntities_section.html): Detect entities in text extracted from an image using an AWS SDK
- [Detect faces in an image](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_cross_DetectFaces_section.html): Detect faces in an image using an AWS SDK
- [Detect objects in images](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_cross_RekognitionPhotoAnalyzer_section.html): Detect objects in images with Amazon Rekognition using an AWS SDK
- [Detect people and objects in a video](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_cross_RekognitionVideoDetection_section.html): Detect people and objects in a video with Amazon Rekognition using an AWS SDK
- [Download S3 'directories'](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_DownloadS3Directory_section.html): Download S3 'directories' from an Amazon Simple Storage Service (Amazon S3) bucket
- [Download objects to a local directory](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_DownloadBucketToDirectory_section.html): Download all objects in an Amazon Simple Storage Service (Amazon S3) bucket to a local directory
- [Download stream of unknown size](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_DownloadStream_section.html): Download a stream of unknown size from an Amazon S3 object using an AWS SDK
- [Get an object from a Multi-Region Access Point](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetObject_MRAP_section.html): Get an Amazon S3 object from a Multi-Region Access Point by using an AWS SDK
- [Get an object from a bucket if it has been modified](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GetObject_IfModifiedSince_section.html): Get an object from an Amazon S3 bucket using an AWS SDK, specifying an If-Modified-Since header
- [Get started with S3](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_GettingStarted_section.html): Get started with Amazon S3 using the CLI
- [Get started with encryption](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Encryption_section.html): Get started with encryption for Amazon S3 objects using an AWS SDK
- [Get started with tags](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_Tagging_section.html): Get started with tags for Amazon S3 objects using an AWS SDK
- [Lock Amazon S3 objects](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_ObjectLock_section.html): Work with Amazon S3 object lock features using an AWS SDK
- [Make conditional requests](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_ConditionalRequests_section.html): Make Amazon S3 conditional requests using an AWS SDK
- [Manage access control lists (ACLs)](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_ManageACLs_section.html): Manage access control lists (ACLs) for Amazon S3 buckets using an AWS SDK
- [Manage large messages using S3](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_sqs_Scenario_SqsExtendedClient_section.html): Manage large Amazon SQS messages using Amazon S3 with an AWS SDK
- [Manage versioned objects in batches with a Lambda function](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_BatchObjectVersioning_section.html): Manage versioned Amazon S3 objects in batches with a Lambda function using an AWS SDK
- [Parse URIs](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_URIParsing_section.html): Parse Amazon S3 URIs using an AWS SDK
- [Perform a multipart copy](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_MultipartCopy_section.html): Perform a multipart copy of an Amazon S3 object using an AWS SDK
- [Process S3 event notifications](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_ProcessS3EventNotification_section.html): Receive and process Amazon S3 event notifications by using an AWS SDK
- [Save EXIF and other image information](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_cross_DetectLabels_section.html): Save EXIF and other image information using an AWS SDK
- [Send event notifications to EventBridge](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_PutBucketNotificationConfiguration_section.html): Send S3 event notifications to Amazon EventBridge using an AWS SDK
- [Track uploads and downloads](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_TrackUploadDownload_section.html): Track an Amazon S3 object upload or download using an AWS SDK
- [Transform data with S3 Object Lambda](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_cross_ServerlessS3DataTransformation_section.html): Transform data for your application with S3 Object Lambda
- [Unit and integration test with an SDK](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_cross_Testing_section.html): Example approaches for unit and integration testing with an AWS SDK
- [Upload directory to a bucket](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_UploadDirectoryToBucket_section.html): Recursively upload a local directory to an Amazon Simple Storage Service (Amazon S3) bucket
- [Upload or download large files](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_UsingLargeFiles_section.html): Upload or download large files to and from Amazon S3 using an AWS SDK
- [Upload stream of unknown size](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_UploadStream_section.html): Upload a stream of unknown size to an Amazon S3 object using an AWS SDK
- [Use checksums](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_UseChecksums_section.html): Use checksums to work with an Amazon S3 object using an AWS SDK
- [Work with Amazon S3 object integrity](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_ObjectIntegrity_section.html): Work with Amazon S3 object integrity features using an AWS SDK
- [Work with versioned objects](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_s3_Scenario_ObjectVersioningUsage_section.html): Work with Amazon S3 versioned objects using an AWS SDK

### [Serverless examples](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3_serverless_examples.html)

The following code examples show how to use Amazon S3 with AWS SDKs.

- [Invoke a Lambda function from an Amazon S3 trigger](https://docs.aws.amazon.com/AmazonS3/latest/API/s3_example_serverless_S3_Lambda_section.html): Invoke a Lambda function from an Amazon S3 trigger

### [Amazon S3 Control](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3-control.html)

Code examples that show how to use Amazon S3 Control with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3-control_basics.html)

The following code examples show how to use the basics of Amazon S3 Control with AWS SDKs.

- [Hello Amazon S3 Control](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_Hello_section.html): Hello Amazon S3 Control
- [Learn the basics](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_Basics_section.html): Learn the basics of Amazon S3 Control with an AWS SDK

### [Actions](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3-control_actions.html)

The following code examples show how to use Amazon S3 Control with AWS SDKs.

- [CreateJob](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_CreateJob_section.html): Use CreateJob with an AWS SDK or CLI
- [DeleteJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_DeleteJobTagging_section.html): Use DeleteJobTagging with an AWS SDK
- [DescribeJob](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_DescribeJob_section.html): Use DescribeJob with an AWS SDK or CLI
- [GetJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_GetJobTagging_section.html): Use GetJobTagging with an AWS SDK
- [PutJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_PutJobTagging_section.html): Use PutJobTagging with an AWS SDK
- [UpdateJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_UpdateJobPriority_section.html): Use UpdateJobPriority with an AWS SDK or CLI
- [UpdateJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_UpdateJobStatus_section.html): Use UpdateJobStatus with an AWS SDK or CLI

### [S3 Directory Buckets](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3-directory-buckets.html)

Code examples that show how to use S3 Directory Buckets with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3-directory-buckets_basics.html)

The following code examples show how to use the basics of S3 Directory Buckets with AWS SDKs.

- [Hello Amazon S3 directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_Hello_section.html): Hello Amazon S3 directory buckets
- [Learn the basics](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_Scenario_ExpressBasics_section.html): Learn the basics of S3 Directory Buckets with an AWS SDK

### [Actions](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3-directory-buckets_actions.html)

The following code examples show how to use S3 Directory Buckets with AWS SDKs.

- [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_AbortMultipartUpload_section.html): Use AbortMultipartUpload with an AWS SDK
- [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_CompleteMultipartUpload_section.html): Use CompleteMultipartUpload with an AWS SDK
- [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_CopyObject_section.html): Use CopyObject with an AWS SDK
- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_CreateBucket_section.html): Use CreateBucket with an AWS SDK
- [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_CreateMultipartUpload_section.html): Use CreateMultipartUpload with an AWS SDK
- [CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_CreateSession_section.html): Use CreateSession with an AWS SDK
- [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_DeleteBucket_section.html): Use DeleteBucket with an AWS SDK
- [DeleteBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_DeleteBucketEncryption_section.html): Use DeleteBucketEncryption with an AWS SDK
- [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_DeleteBucketPolicy_section.html): Use DeleteBucketPolicy with an AWS SDK
- [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_DeleteObject_section.html): Use DeleteObject with an AWS SDK
- [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_DeleteObjects_section.html): Use DeleteObjects with an AWS SDK
- [GetBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_GetBucketEncryption_section.html): Use GetBucketEncryption with an AWS SDK
- [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_GetBucketPolicy_section.html): Use GetBucketPolicy with an AWS SDK
- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_GetObject_section.html): Use GetObject with an AWS SDK
- [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_GetObjectAttributes_section.html): Use GetObjectAttributes with an AWS SDK
- [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_HeadBucket_section.html): Use HeadBucket with an AWS SDK
- [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_HeadObject_section.html): Use HeadObject with an AWS SDK
- [ListDirectoryBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_ListDirectoryBuckets_section.html): Use ListDirectoryBuckets with an AWS SDK
- [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_ListMultipartUploads_section.html): Use ListMultipartUploads with an AWS SDK
- [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_ListObjectsV2_section.html): Use ListObjectsV2 with an AWS SDK
- [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_ListParts_section.html): Use ListParts with an AWS SDK
- [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_PutBucketEncryption_section.html): Use PutBucketEncryption with an AWS SDK
- [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_PutBucketPolicy_section.html): Use PutBucketPolicy with an AWS SDK
- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_PutObject_section.html): Use PutObject with an AWS SDK
- [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_UploadPart_section.html): Use UploadPart with an AWS SDK
- [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_UploadPartCopy_section.html): Use UploadPartCopy with an AWS SDK

### [Scenarios](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples_s3-directory-buckets_scenarios.html)

The following code examples show how to use S3 Directory Buckets with AWS SDKs.

- [Create a presigned URL to get an object](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-directory-buckets_example_s3-directory-buckets_GeneratePresignedGetURLForDirectoryBucket_section.html): Create a presigned URL for Amazon S3 directory buckets to get an object using an AWS SDK


## [Authenticating Requests (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html)

### [Using an Authorization Header](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-auth-using-authorization-header.html)

Use the HTTP authorization header to provide authentication of the request.

- [Signature Calculation: Transfer Payload in a Single Chunk](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-header-based-auth.html): Authenticate requests using the HTTP authorization header to compute a checksum for smaller payloads.
- [Signature Calculation: Transfer Payload in Multiple Chunks](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-streaming.html): Perform a chunked upload to authenticate requests using the HTTP authorization header.
- [Signature Calculation: Including Trailing Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-streaming-trailers.html): Perform a chunked upload that includes trailing headers to authenticate requests using the HTTP authorization header.
- [Using Query Parameters](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html): Authenticate requests using the query parameters to express a request entirely in a URL.
- [Examples: Signature Calculations](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-examples-using-sdks.html): Provides code samples of signature calculations written in Java and C# in AWS Signature Version 4.
- [Authenticating HTTP POST Requests](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-authentication-HTTPPOST.html): How to authenticate AWS Signature Version 4 HTTPPOST requests for Amazon S3.
- [Amazon S3 Signature Version 4 Authentication Specific Policy Keys](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html): How to use AWS Signature Version 4 authentication specific policy keys.


## [Browser-Based Uploads Using POST](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-UsingHTTPPOST.html)

### [POST Object](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html)

The Amazon S3 POST Object REST operation adds an object to a specified bucket by using HTML forms.

- [Versioning](https://docs.aws.amazon.com/AmazonS3/latest/API/postVersions.html): Add an object with a unique version ID for a versioning-enabled bucket using the POST Object REST operation.
- [POST Object restore](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOSTrestore.html): Restore a temporary copy of an archived Amazon S3 object using the POST Object restore REST operation.
- [Creating HTML Forms](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-HTTPPOSTForms.html): Upload content to Amazon S3 by using their browsers with HTML forms using AWS Signature Version 4.
- [POST Policy](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-HTTPPOSTConstructPolicy.html): How to create a POST policy.
- [POST Upload Example](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-post-example.html): Provides code samples of uploading objects using POST through your browser and using the signature calculation in AWS Signature Version 4.
- [Browser-based uploads using AWS Amplify](https://docs.aws.amazon.com/AmazonS3/latest/API/browser-based-uploads-aws-amplify.html): Discusses using the AWS Amplify JavaScript library for uploading objects directly to Amazon S3.


## [Error responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html)

- [Amazon S3 error best practices](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorBestPractices.html): Follow these best practices for handling errors when designing your application.


## [Appendix](https://docs.aws.amazon.com/AmazonS3/latest/API/appendix.html)

- [Appendix: SelectObjectContent Response](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTSelectObjectAppendix.html): Discusses the nature of the response body of a Amazon S3 Select Response request.
- [Appendix: OPTIONS object](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTOPTIONSobject.html): Send a test request to evaluate if you can send an actual cross-origin request using the OPTIONS object REST operation.

### [Appendix: SOAP API](https://docs.aws.amazon.com/AmazonS3/latest/API/APISoap.html)

Describes the SOAP API with respect to service, bucket, and object operations that you can perform on the Amazon S3 web service.

### [Operations on the Service (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPServiceOps.html)

Describes SOAP operations you can perform on the Amazon S3 web service.

- [ListAllMyBuckets (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPListAllMyBuckets.html): Returns a list of all buckets owned by the sender of the request using the ListAllMyBuckets SOAP operation.

### [Operations on Buckets (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPBucketsOps.html)

Describes SOAP operations that you can perform on Amazon S3 buckets.

- [CreateBucket (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPCreateBucket.html): Creates a bucket with a unique bucket name using the CreateBucket SOAP operation.
- [DeleteBucket (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPDeleteBucket.html): Removes the bucket after all objects in the bucket are deleted using the DeleteBucket SOAP operation.
- [ListBucket (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPListBucket.html): Returns information about some of the items in the bucket using the ListBucket SOAP operation.
- [GetBucketAccessControlPolicy (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPGetBucketAccessControlPolicy.html): Returns the access control policy for a bucket using the GetBucketAccessControlPolicy SOAP operation.
- [SetBucketAccessControlPolicy (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPSetBucketAccessControlPolicy.html): Sets the access control policy for an existing bucket using the SetBucketAccessControlPolicy SOAP operation.
- [GetBucketLoggingStatus (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPGetBucketLoggingStatus.html): Returns the logging status for an existing bucket using the GetBucketLoggingStatus SOAP operation.
- [SetBucketLoggingStatus (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPSetBucketLoggingStatus.html): Enables server access logging for bucket and configures the logs using the SetBucketLoggingStatus SOAP operation.

### [Operations on Objects (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPObjectsOps.html)

Describes SOAP operations that you can perform on Amazon S3 objects.

- [PutObjectInline (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPPutObjectInline.html): Adds an object to a bucket using the PutObjectInline SOAP operation where the data for the object is included in the body of the SOAP message.
- [PutObject (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPPutObject.html): Adds an object to a bucket using the PutObject SOAP operation.
- [CopyObject (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPCopyObject.html): Creates a copy of a specified object using the CopyObject SOAP operation.
- [GetObject (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPGetObject.html): Returns the current version of the object using the GetObject SOAP operation.
- [GetObjectExtended (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPGetObjectExtended.html): Returns the current version of the object with additional elements using the GetObjectExtended SOAP operation.
- [DeleteObject (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPDeleteObject.html): Removes the specified object from Amazon S3 bucket using the DeleteObject SOAP operation.
- [GetObjectAccessControlPolicy (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPGetObjectAccessControlPolicy.html): Returns the access control policy for an object using the GetObjectAccessControlPolicy SOAP operation.
- [SetObjectAccessControlPolicy (SOAP API)](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPSetObjectAccessControlPolicy.html): Sets the access control policy for an existing object using the SetObjectAccessControlPolicy SOAP operation.
- [Authenticating SOAP requests](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPAuthentication.html): Establish the identity of the principal making the SOAP request by including authentication information.
- [Setting access policy with SOAP](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPAccessPolicy.html): Set the access control for a bucket or object using SOAP.
- [SOAP Error Responses](https://docs.aws.amazon.com/AmazonS3/latest/API/SOAPErrorResponses.html): Describes the SOAP error responses comprised of a standard SOAP fault code concatenated with the Amazon S3-specific error code.

### [Appendix: Authenticating requests (AWS signature version 2)](https://docs.aws.amazon.com/AmazonS3/latest/API/Appendix-Sigv2.html)

How to authenticate requests to Amazon S3 using AWS Signature Version 2.

- [Authenticating requests using the REST API (AWS signature version 2)](https://docs.aws.amazon.com/AmazonS3/latest/API/S3_Authentication2.html): Provide the request elements that include the access key ID, signature, time stamp, and date for the request to be authenticated.
- [Signing and authenticating REST requests (AWS signature version 2)](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTAuthentication.html): Control access to your system by signing and authenticating your requests.

### [Browser-based uploads using POST (AWS signature version 2)](https://docs.aws.amazon.com/AmazonS3/latest/API/UsingHTTPPOST.html)

Upload content using POST to simplify uploads, reduce upload latency, and save money on applications where users upload data to Amazon S3.

- [HTML forms](https://docs.aws.amazon.com/AmazonS3/latest/API/HTTPPOSTForms.html): Upload content with POST through your browser by using HTML forms.
- [Upload examples](https://docs.aws.amazon.com/AmazonS3/latest/API/HTTPPOSTExamples.html): Code example of the complete process for constructing a policy and form for uploading a file attachment.
- [POST with adobe flash (AWS signature version 2)](https://docs.aws.amazon.com/AmazonS3/latest/API/HTTPPOSTFlash.html): Set up your bucket to allow Adobe Flash to accept POST with uploads with a publicly readable crossdomain.xml file.

### [Appendix: Lifecycle Configuration APIs (Deprecated)](https://docs.aws.amazon.com/AmazonS3/latest/API/lifecycle-old-api.html)

Bucket lifecycle configuration is updated to support filters based on object tags.

- [PUT Bucket lifecycle (Deprecated)](https://docs.aws.amazon.com/AmazonS3/latest/API/v1-rel-RESTBucketPUTlifecycle.html): Creates a new lifecycle configuration or replaces an existing lifecycle configuration for a bucket with the PUT Bucket lifecycle REST operation.
- [GET Bucket lifecycle (Deprecated)](https://docs.aws.amazon.com/AmazonS3/latest/API/v1-rel-RESTBucketGETlifecycle.html): Returns the lifecycle configuration information set on a specified bucket using the GET Bucket lifecycle REST operation.
