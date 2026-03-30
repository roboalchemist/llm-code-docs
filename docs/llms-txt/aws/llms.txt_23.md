# Source: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/llms.txt

# Amazon Elastic Container Registry API Reference

> Amazon Elastic Container Registry (Amazon ECR) is a managed container image registry service. Customers can use the familiar Docker CLI, or their preferred client, to push, pull, and manage images. Amazon ECR provides a secure, scalable, and reliable registry for your Docker or Open Container Initiative (OCI) images. Amazon ECR supports private repositories with resource-based permissions using IAM so that specific users or Amazon EC2 instances can access repositories and images.

- [Welcome](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Operations.html)

- [BatchCheckLayerAvailability](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchCheckLayerAvailability.html): Checks the availability of one or more image layers in a repository.
- [BatchDeleteImage](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchDeleteImage.html): Deletes a list of specified images within a repository.
- [BatchGetImage](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchGetImage.html): Gets detailed information for an image.
- [BatchGetRepositoryScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchGetRepositoryScanningConfiguration.html): Gets the scanning configuration for one or more repositories.
- [CompleteLayerUpload](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CompleteLayerUpload.html): Informs Amazon ECR that the image layer upload has completed for a specified registry, repository name, and upload ID.
- [CreatePullThroughCacheRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CreatePullThroughCacheRule.html): Creates a pull through cache rule.
- [CreateRepository](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CreateRepository.html): Creates a repository.
- [CreateRepositoryCreationTemplate](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CreateRepositoryCreationTemplate.html): Creates a repository creation template.
- [DeleteLifecyclePolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteLifecyclePolicy.html): Deletes the lifecycle policy associated with the specified repository.
- [DeletePullThroughCacheRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeletePullThroughCacheRule.html): Deletes a pull through cache rule.
- [DeleteRegistryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRegistryPolicy.html): Deletes the registry permissions policy.
- [DeleteRepository](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRepository.html): Deletes a repository.
- [DeleteRepositoryCreationTemplate](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRepositoryCreationTemplate.html): Deletes a repository creation template.
- [DeleteRepositoryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRepositoryPolicy.html): Deletes the repository policy associated with the specified repository.
- [DeleteSigningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteSigningConfiguration.html): Deletes the registry's signing configuration.
- [DeregisterPullTimeUpdateExclusion](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeregisterPullTimeUpdateExclusion.html): Removes a principal from the pull time update exclusion list for a registry.
- [DescribeImageReplicationStatus](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageReplicationStatus.html): Returns the replication status for a specified image.
- [DescribeImages](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImages.html): Returns metadata about the images in a repository.
- [DescribeImageScanFindings](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageScanFindings.html): Returns the scan findings for the specified image.
- [DescribeImageSigningStatus](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageSigningStatus.html): Returns the signing status for a specified image.
- [DescribePullThroughCacheRules](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribePullThroughCacheRules.html): Returns the pull through cache rules for a registry.
- [DescribeRegistry](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRegistry.html): Describes the settings for a registry.
- [DescribeRepositories](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRepositories.html): Describes image repositories in a registry.
- [DescribeRepositoryCreationTemplates](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRepositoryCreationTemplates.html): Returns details about the repository creation templates in a registry.
- [GetAccountSetting](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAccountSetting.html): Retrieves the account setting value for the specified setting name.
- [GetAuthorizationToken](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAuthorizationToken.html): Retrieves an authorization token.
- [GetDownloadUrlForLayer](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetDownloadUrlForLayer.html): Retrieves the pre-signed Amazon S3 download URL corresponding to an image layer.
- [GetLifecyclePolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetLifecyclePolicy.html): Retrieves the lifecycle policy for the specified repository.
- [GetLifecyclePolicyPreview](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetLifecyclePolicyPreview.html): Retrieves the results of the lifecycle policy preview request for the specified repository.
- [GetRegistryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRegistryPolicy.html): Retrieves the permissions policy for a registry.
- [GetRegistryScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRegistryScanningConfiguration.html): Retrieves the scanning configuration for a registry.
- [GetRepositoryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRepositoryPolicy.html): Retrieves the repository policy for the specified repository.
- [GetSigningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetSigningConfiguration.html): Retrieves the registry's signing configuration, which defines rules for automatically signing images using AWS Signer.
- [InitiateLayerUpload](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_InitiateLayerUpload.html): Notifies Amazon ECR that you intend to upload an image layer.
- [ListImageReferrers](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListImageReferrers.html): Lists the artifacts associated with a specified subject image.
- [ListImages](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListImages.html): Lists all the image IDs for the specified repository.
- [ListPullTimeUpdateExclusions](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListPullTimeUpdateExclusions.html): Lists the IAM principals that are excluded from having their image pull times recorded.
- [ListTagsForResource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListTagsForResource.html): List the tags for an Amazon ECR resource.
- [PutAccountSetting](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutAccountSetting.html): Allows you to change the basic scan type version or registry policy scope.
- [PutImage](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutImage.html): Creates or updates the image manifest and tags associated with an image.
- [PutImageScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutImageScanningConfiguration.html)
- [PutImageTagMutability](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutImageTagMutability.html): Updates the image tag mutability settings for the specified repository.
- [PutLifecyclePolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutLifecyclePolicy.html): Creates or updates the lifecycle policy for the specified repository.
- [PutRegistryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutRegistryPolicy.html): Creates or updates the permissions policy for your registry.
- [PutRegistryScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutRegistryScanningConfiguration.html): Creates or updates the scanning configuration for your private registry.
- [PutReplicationConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutReplicationConfiguration.html): Creates or updates the replication configuration for a registry.
- [PutSigningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutSigningConfiguration.html): Creates or updates the registry's signing configuration, which defines rules for automatically signing images with AWS Signer.
- [RegisterPullTimeUpdateExclusion](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RegisterPullTimeUpdateExclusion.html): Adds an IAM principal to the pull time update exclusion list for a registry.
- [SetRepositoryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_SetRepositoryPolicy.html): Applies a repository policy to the specified repository to control access permissions.
- [StartImageScan](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_StartImageScan.html): Starts a basic image vulnerability scan.
- [StartLifecyclePolicyPreview](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_StartLifecyclePolicyPreview.html): Starts a preview of a lifecycle policy for the specified repository.
- [TagResource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_TagResource.html): Adds specified tags to a resource with the specified ARN.
- [UntagResource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UntagResource.html): Deletes specified tags from a resource.
- [UpdateImageStorageClass](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UpdateImageStorageClass.html): Transitions an image between storage classes.
- [UpdatePullThroughCacheRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UpdatePullThroughCacheRule.html): Updates an existing pull through cache rule.
- [UpdateRepositoryCreationTemplate](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UpdateRepositoryCreationTemplate.html): Updates an existing repository creation template.
- [UploadLayerPart](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UploadLayerPart.html): Uploads an image layer part to Amazon ECR.
- [ValidatePullThroughCacheRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ValidatePullThroughCacheRule.html): Validates an existing pull through cache rule for an upstream registry that requires authentication.


## [Data Types](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Types.html)

- [Attribute](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Attribute.html): This data type is used in the data type.
- [AuthorizationData](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_AuthorizationData.html): An object representing authorization data for an Amazon ECR registry.
- [AwsEcrContainerImageDetails](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_AwsEcrContainerImageDetails.html): The image details of the Amazon ECR container image.
- [CvssScore](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CvssScore.html): The CVSS score for a finding.
- [CvssScoreAdjustment](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CvssScoreAdjustment.html): Details on adjustments Amazon Inspector made to the CVSS score for a finding.
- [CvssScoreDetails](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CvssScoreDetails.html): Information about the CVSS score.
- [DescribeImagesFilter](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImagesFilter.html): An object representing a filter on a operation.
- [EncryptionConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_EncryptionConfiguration.html): The encryption configuration for the repository.
- [EncryptionConfigurationForRepositoryCreationTemplate](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_EncryptionConfigurationForRepositoryCreationTemplate.html): The encryption configuration to associate with the repository creation template.
- [EnhancedImageScanFinding](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_EnhancedImageScanFinding.html): The details of an enhanced image scan.
- [Image](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Image.html): An object representing an Amazon ECR image.
- [ImageDetail](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageDetail.html): An object that describes an image returned by a operation.
- [ImageFailure](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageFailure.html): An object representing an Amazon ECR image failure.
- [ImageIdentifier](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageIdentifier.html): An object with identifying information for an image in an Amazon ECR repository.
- [ImageReferrer](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageReferrer.html): An object representing an artifact associated with a subject image.
- [ImageReplicationStatus](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageReplicationStatus.html): The status of the replication process for an image.
- [ImageScanFinding](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageScanFinding.html): Contains information about an image scan finding.
- [ImageScanFindings](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageScanFindings.html): The details of an image scan.
- [ImageScanFindingsSummary](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageScanFindingsSummary.html): A summary of the last completed image scan.
- [ImageScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageScanningConfiguration.html): The image scanning configuration for a repository.
- [ImageScanStatus](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageScanStatus.html): The current status of an image scan.
- [ImageSigningStatus](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageSigningStatus.html): The signing status for an image.
- [ImageTagMutabilityExclusionFilter](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageTagMutabilityExclusionFilter.html): A filter that specifies which image tags should be excluded from the repository's image tag mutability setting.
- [Layer](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Layer.html): An object representing an Amazon ECR image layer.
- [LayerFailure](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_LayerFailure.html): An object representing an Amazon ECR image layer failure.
- [LifecyclePolicyPreviewFilter](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_LifecyclePolicyPreviewFilter.html): The filter for the lifecycle policy preview.
- [LifecyclePolicyPreviewResult](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_LifecyclePolicyPreviewResult.html): The result of the lifecycle policy preview.
- [LifecyclePolicyPreviewSummary](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_LifecyclePolicyPreviewSummary.html): The summary of the lifecycle policy preview request.
- [LifecyclePolicyRuleAction](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_LifecyclePolicyRuleAction.html): The type of action to be taken.
- [ListImageReferrersFilter](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListImageReferrersFilter.html): An object representing a filter on a operation.
- [ListImagesFilter](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListImagesFilter.html): An object representing a filter on a operation.
- [PackageVulnerabilityDetails](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PackageVulnerabilityDetails.html): Information about a package vulnerability finding.
- [PullThroughCacheRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PullThroughCacheRule.html): The details of a pull through cache rule.
- [Recommendation](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Recommendation.html): Details about the recommended course of action to remediate the finding.
- [RegistryScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RegistryScanningConfiguration.html): The scanning configuration for a private registry.
- [RegistryScanningRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RegistryScanningRule.html): The details of a scanning rule for a private registry.
- [Remediation](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Remediation.html): Information on how to remediate a finding.
- [ReplicationConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ReplicationConfiguration.html): The replication configuration for a registry.
- [ReplicationDestination](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ReplicationDestination.html): An array of objects representing the destination for a replication rule.
- [ReplicationRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ReplicationRule.html): An array of objects representing the replication destinations and repository filters for a replication configuration.
- [Repository](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Repository.html): An object representing a repository.
- [RepositoryCreationTemplate](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RepositoryCreationTemplate.html): The details of the repository creation template associated with the request.
- [RepositoryFilter](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RepositoryFilter.html): The filter settings used with image replication.
- [RepositoryScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RepositoryScanningConfiguration.html): The details of the scanning configuration for a repository.
- [RepositoryScanningConfigurationFailure](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RepositoryScanningConfigurationFailure.html): The details about any failures associated with the scanning configuration of a repository.
- [Resource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Resource.html): Details about the resource involved in a finding.
- [ResourceDetails](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ResourceDetails.html): Contains details about the resource involved in the finding.
- [ScanningRepositoryFilter](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ScanningRepositoryFilter.html): The details of a scanning repository filter.
- [ScoreDetails](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ScoreDetails.html): Information about the Amazon Inspector score given to a finding.
- [SigningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_SigningConfiguration.html): The signing configuration for a registry, which specifies rules for automatically signing images when pushed.
- [SigningRepositoryFilter](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_SigningRepositoryFilter.html): A repository filter used to determine which repositories have their images automatically signed on push.
- [SigningRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_SigningRule.html): A signing rule that specifies a signing profile and optional repository filters.
- [SubjectIdentifier](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_SubjectIdentifier.html): An object that identifies an image subject.
- [Tag](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Tag.html): The metadata to apply to a resource to help you categorize and organize them.
- [TransitioningImageTotalCount](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_TransitioningImageTotalCount.html): The total count of images transitioning to a storage class.
- [VulnerablePackage](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_VulnerablePackage.html): Information on the vulnerable package identified by a finding.
