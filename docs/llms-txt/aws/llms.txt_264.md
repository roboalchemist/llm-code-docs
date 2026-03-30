# Source: https://docs.aws.amazon.com/data-exchange/latest/apireference/llms.txt

# AWS Data Exchange API Reference

> This is official Amazon Web Services (AWS) documentation for AWS Data Exchange.

- [Welcome](https://docs.aws.amazon.com/data-exchange/latest/apireference/welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/data-exchange/latest/apireference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/data-exchange/latest/apireference/CommonErrors.html)
- [Document history](https://docs.aws.amazon.com/data-exchange/latest/apireference/doc-history.html)

## [Actions](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_Operations.html)

- [AcceptDataGrant](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_AcceptDataGrant.html): This operation accepts a data grant.
- [CancelJob](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CancelJob.html): This operation cancels a job.
- [CreateDataGrant](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateDataGrant.html): This operation creates a data grant.
- [CreateDataSet](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateDataSet.html): This operation creates a data set.
- [CreateEventAction](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateEventAction.html): This operation creates an event action.
- [CreateJob](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateJob.html): This operation creates a job.
- [CreateRevision](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateRevision.html): This operation creates a revision for a data set.
- [DeleteAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteAsset.html): This operation deletes an asset.
- [DeleteDataGrant](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteDataGrant.html): This operation deletes a data grant.
- [DeleteDataSet](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteDataSet.html): This operation deletes a data set.
- [DeleteEventAction](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteEventAction.html): This operation deletes the event action.
- [DeleteRevision](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteRevision.html): This operation deletes a revision.
- [GetAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetAsset.html): This operation returns information about an asset.
- [GetDataGrant](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetDataGrant.html): This operation returns information about a data grant.
- [GetDataSet](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetDataSet.html): This operation returns information about a data set.
- [GetEventAction](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetEventAction.html): This operation retrieves information about an event action.
- [GetJob](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetJob.html): This operation returns information about a job.
- [GetReceivedDataGrant](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetReceivedDataGrant.html): This operation returns information about a received data grant.
- [GetRevision](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetRevision.html): This operation returns information about a revision.
- [ListDataGrants](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListDataGrants.html): This operation returns information about all data grants.
- [ListDataSetRevisions](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListDataSetRevisions.html): This operation lists a data set's revisions sorted by CreatedAt in descending order.
- [ListDataSets](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListDataSets.html): This operation lists your data sets.
- [ListEventActions](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListEventActions.html): This operation lists your event actions.
- [ListJobs](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListJobs.html): This operation lists your jobs sorted by CreatedAt in descending order.
- [ListReceivedDataGrants](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListReceivedDataGrants.html): This operation returns information about all received data grants.
- [ListRevisionAssets](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListRevisionAssets.html): This operation lists a revision's assets sorted alphabetically in descending order.
- [ListTagsForResource](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListTagsForResource.html): This operation lists the tags on the resource.
- [RevokeRevision](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RevokeRevision.html): This operation revokes subscribers' access to a revision.
- [SendApiAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_SendApiAsset.html): This operation invokes an API Gateway API asset.
- [SendDataSetNotification](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_SendDataSetNotification.html): The type of event associated with the data set.
- [StartJob](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_StartJob.html): This operation starts a job.
- [TagResource](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_TagResource.html): This operation tags a resource.
- [UntagResource](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UntagResource.html): This operation removes one or more tags from a resource.
- [UpdateAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UpdateAsset.html): This operation updates an asset.
- [UpdateDataSet](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UpdateDataSet.html): This operation updates a data set.
- [UpdateEventAction](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UpdateEventAction.html): This operation updates the event action.
- [UpdateRevision](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UpdateRevision.html): This operation updates a revision.


## [Data Types](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_Types.html)

- [Action](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_Action.html): What occurs after a certain event.
- [ApiGatewayApiAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ApiGatewayApiAsset.html): The API Gateway API that is the asset.
- [AssetDestinationEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_AssetDestinationEntry.html): The destination for the asset.
- [AssetDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_AssetDetails.html): Details about the asset.
- [AssetEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_AssetEntry.html): An asset in AWS Data Exchange is a piece of data (Amazon S3 object) or a means of fulfilling data (Amazon Redshift datashare or Amazon API Gateway API, AWS Lake Formation data permission, or Amazon S3 data access).
- [AssetSourceEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_AssetSourceEntry.html): The source of the assets.
- [AutoExportRevisionDestinationEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_AutoExportRevisionDestinationEntry.html): A revision destination is the Amazon S3 bucket folder destination to where the export will be sent.
- [AutoExportRevisionToS3RequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_AutoExportRevisionToS3RequestDetails.html): Details of the operation to be performed by the job.
- [CreateS3DataAccessFromS3BucketRequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateS3DataAccessFromS3BucketRequestDetails.html): Details of the operation to create an Amazon S3 data access from an S3 bucket.
- [CreateS3DataAccessFromS3BucketResponseDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateS3DataAccessFromS3BucketResponseDetails.html): Details about the response of the operation to create an S3 data access from an S3 bucket.
- [DatabaseLFTagPolicy](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DatabaseLFTagPolicy.html): The LF-tag policy for database resources.
- [DatabaseLFTagPolicyAndPermissions](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DatabaseLFTagPolicyAndPermissions.html): The LF-tag policy and permissions for database resources.
- [DataGrantSummaryEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DataGrantSummaryEntry.html): Information about a data grant.
- [DataSetEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DataSetEntry.html): A data set is an AWS resource with one or more revisions.
- [DataUpdateRequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DataUpdateRequestDetails.html): Extra details specific to a data update type notification.
- [DeprecationRequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeprecationRequestDetails.html): Extra details specific to a deprecation type notification.
- [Details](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_Details.html): Information about the job error.
- [Event](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_Event.html): What occurs to start an action.
- [EventActionEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_EventActionEntry.html): An event action is an object that defines the relationship between a specific event and an automated action that will be taken on behalf of the customer.
- [ExportAssetsToS3RequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportAssetsToS3RequestDetails.html): Details of the operation to be performed by the job.
- [ExportAssetsToS3ResponseDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportAssetsToS3ResponseDetails.html): Details about the export to Amazon S3 response.
- [ExportAssetToSignedUrlRequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportAssetToSignedUrlRequestDetails.html): Details of the operation to be performed by the job.
- [ExportAssetToSignedUrlResponseDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportAssetToSignedUrlResponseDetails.html): The details of the export to signed URL response.
- [ExportRevisionsToS3RequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportRevisionsToS3RequestDetails.html): Details of the operation to be performed by the job.
- [ExportRevisionsToS3ResponseDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportRevisionsToS3ResponseDetails.html): Details about the export revisions to Amazon S3 response.
- [ExportServerSideEncryption](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportServerSideEncryption.html): Encryption configuration of the export job.
- [ImportAssetFromApiGatewayApiRequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetFromApiGatewayApiRequestDetails.html): The request details.
- [ImportAssetFromApiGatewayApiResponseDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetFromApiGatewayApiResponseDetails.html): The response details.
- [ImportAssetFromSignedUrlJobErrorDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetFromSignedUrlJobErrorDetails.html): Details about the job error.
- [ImportAssetFromSignedUrlRequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetFromSignedUrlRequestDetails.html): Details of the operation to be performed by the job.
- [ImportAssetFromSignedUrlResponseDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetFromSignedUrlResponseDetails.html): The details in the response for an import request, including the signed URL and other information.
- [ImportAssetsFromLakeFormationTagPolicyRequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetsFromLakeFormationTagPolicyRequestDetails.html): Details about the assets imported from an AWS Lake Formation tag policy request.
- [ImportAssetsFromLakeFormationTagPolicyResponseDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetsFromLakeFormationTagPolicyResponseDetails.html): Details from an import AWS Lake Formation tag policy job response.
- [ImportAssetsFromRedshiftDataSharesRequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetsFromRedshiftDataSharesRequestDetails.html): Details from an import from Amazon Redshift datashare request.
- [ImportAssetsFromRedshiftDataSharesResponseDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetsFromRedshiftDataSharesResponseDetails.html): Details from an import from Amazon Redshift datashare response.
- [ImportAssetsFromS3RequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetsFromS3RequestDetails.html): Details of the operation to be performed by the job.
- [ImportAssetsFromS3ResponseDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetsFromS3ResponseDetails.html): Details from an import from Amazon S3 response.
- [JobEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_JobEntry.html): AWS Data Exchange Jobs are asynchronous import or export operations used to create or copy assets.
- [JobError](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_JobError.html): An error that occurred with the job request.
- [KmsKeyToGrant](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_KmsKeyToGrant.html): The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the shared S3 objects.
- [LakeFormationDataPermissionAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_LakeFormationDataPermissionAsset.html): The AWS Lake Formation data permission asset.
- [LakeFormationDataPermissionDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_LakeFormationDataPermissionDetails.html): Details about the AWS Lake Formation data permission.
- [LakeFormationTagPolicyDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_LakeFormationTagPolicyDetails.html): Extra details specific to the affected scope in this LF data set.
- [LFResourceDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_LFResourceDetails.html): Details about the AWS Lake Formation resource (Table or Database) included in the AWS Lake Formation data permission.
- [LFTag](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_LFTag.html): A structure that allows an LF-admin to grant permissions on certain conditions.
- [LFTagPolicyDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_LFTagPolicyDetails.html): Details about the LF-tag policy.
- [NotificationDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_NotificationDetails.html): Extra details specific to this notification.
- [OriginDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_OriginDetails.html): Details about the origin of the data set.
- [ReceivedDataGrantSummariesEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ReceivedDataGrantSummariesEntry.html): Information about a received data grant.
- [RedshiftDataShareAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RedshiftDataShareAsset.html): The Amazon Redshift datashare asset.
- [RedshiftDataShareAssetSourceEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RedshiftDataShareAssetSourceEntry.html): The source of the Amazon Redshift datashare asset.
- [RedshiftDataShareDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RedshiftDataShareDetails.html): Extra details specific to the affected scope in this Redshift data set.
- [RequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RequestDetails.html): The details for the request.
- [ResponseDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ResponseDetails.html): Details for the response.
- [RevisionDestinationEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RevisionDestinationEntry.html): The destination where the assets in the revision will be exported.
- [RevisionEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RevisionEntry.html): A revision is a container for one or more assets.
- [RevisionPublished](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RevisionPublished.html): Information about the published revision.
- [S3DataAccessAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_S3DataAccessAsset.html): The Amazon S3 data access that is the asset.
- [S3DataAccessAssetSourceEntry](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_S3DataAccessAssetSourceEntry.html): Source details for an Amazon S3 data access asset.
- [S3DataAccessDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_S3DataAccessDetails.html): Extra details specific to the affected scope in this S3 Data Access data set.
- [S3SnapshotAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_S3SnapshotAsset.html): The Amazon S3 object that is the asset.
- [SchemaChangeDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_SchemaChangeDetails.html): Object encompassing information about a schema change to a single, particular field, a notification can have up to 100 of these.
- [SchemaChangeRequestDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_SchemaChangeRequestDetails.html): Extra details specific to this schema change type notification.
- [ScopeDetails](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ScopeDetails.html): Details about the scope of the notifications such as the affected resources.
- [TableLFTagPolicy](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_TableLFTagPolicy.html): The LF-tag policy for a table resource.
- [TableLFTagPolicyAndPermissions](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_TableLFTagPolicyAndPermissions.html): The LF-tag policy and permissions that apply to table resources.
