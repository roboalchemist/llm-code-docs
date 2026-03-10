# Source: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/llms.txt

# Amazon Elastic Container Registry Public API Reference

> Amazon Elastic Container Registry Public (Amazon ECR Public) is a managed container image registry service. Amazon ECR provides both public and private registries to host your container images. You can use the Docker CLI or your preferred client to push, pull, and manage images. Amazon ECR provides a secure, scalable, and reliable registry for your Docker or Open Container Initiative (OCI) images. Amazon ECR supports public repositories with this API. For information about the Amazon ECR API for private repositories, see Amazon Elastic Container Registry API Reference.

- [Welcome](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_Operations.html)

- [BatchCheckLayerAvailability](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_BatchCheckLayerAvailability.html): Checks the availability of one or more image layers that are within a repository in a public registry.
- [BatchDeleteImage](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_BatchDeleteImage.html): Deletes a list of specified images that are within a repository in a public registry.
- [CompleteLayerUpload](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_CompleteLayerUpload.html): Informs Amazon ECR that the image layer upload is complete for a specified public registry, repository name, and upload ID.
- [CreateRepository](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_CreateRepository.html): Creates a repository in a public registry.
- [DeleteRepository](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DeleteRepository.html): Deletes a repository in a public registry.
- [DeleteRepositoryPolicy](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DeleteRepositoryPolicy.html): Deletes the repository policy that's associated with the specified repository.
- [DescribeImages](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DescribeImages.html): Returns metadata that's related to the images in a repository in a public registry.
- [DescribeImageTags](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DescribeImageTags.html): Returns the image tag details for a repository in a public registry.
- [DescribeRegistries](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DescribeRegistries.html): Returns details for a public registry.
- [DescribeRepositories](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DescribeRepositories.html): Describes repositories that are in a public registry.
- [GetAuthorizationToken](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_GetAuthorizationToken.html): Retrieves an authorization token.
- [GetRegistryCatalogData](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_GetRegistryCatalogData.html): Retrieves catalog metadata for a public registry.
- [GetRepositoryCatalogData](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_GetRepositoryCatalogData.html): Retrieve catalog metadata for a repository in a public registry.
- [GetRepositoryPolicy](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_GetRepositoryPolicy.html): Retrieves the repository policy for the specified repository.
- [InitiateLayerUpload](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_InitiateLayerUpload.html): Notifies Amazon ECR that you intend to upload an image layer.
- [ListTagsForResource](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ListTagsForResource.html): List the tags for an Amazon ECR Public resource.
- [PutImage](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_PutImage.html): Creates or updates the image manifest and tags that are associated with an image.
- [PutRegistryCatalogData](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_PutRegistryCatalogData.html): Create or update the catalog data for a public registry.
- [PutRepositoryCatalogData](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_PutRepositoryCatalogData.html): Creates or updates the catalog data for a repository in a public registry.
- [SetRepositoryPolicy](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_SetRepositoryPolicy.html): Applies a repository policy to the specified public repository to control access permissions.
- [TagResource](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_TagResource.html): Associates the specified tags to a resource with the specified resourceArn.
- [UntagResource](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_UntagResource.html): Deletes specified tags from a resource.
- [UploadLayerPart](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_UploadLayerPart.html): Uploads an image layer part to Amazon ECR.


## [Data Types](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_Types.html)

- [AuthorizationData](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_AuthorizationData.html): An authorization token data object that corresponds to a public registry.
- [Image](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_Image.html): An object that represents an Amazon ECR image.
- [ImageDetail](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ImageDetail.html): An object that describes an image that's returned by a operation.
- [ImageFailure](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ImageFailure.html): An object that represents an Amazon ECR image failure.
- [ImageIdentifier](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ImageIdentifier.html): An object with identifying information for an Amazon ECR image.
- [ImageTagDetail](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ImageTagDetail.html): An object that represents the image tag details for an image.
- [Layer](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_Layer.html): An object that represents an Amazon ECR image layer.
- [LayerFailure](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_LayerFailure.html): An object that represents an Amazon ECR image layer failure.
- [ReferencedImageDetail](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ReferencedImageDetail.html): An object that describes the image tag details that are returned by a action.
- [Registry](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_Registry.html): The details of a public registry.
- [RegistryAlias](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_RegistryAlias.html): An object representing the aliases for a public registry.
- [RegistryCatalogData](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_RegistryCatalogData.html): The metadata for a public registry.
- [Repository](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_Repository.html): An object representing a repository.
- [RepositoryCatalogData](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_RepositoryCatalogData.html): The catalog data for a repository.
- [RepositoryCatalogDataInput](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_RepositoryCatalogDataInput.html): An object that contains the catalog data for a repository.
- [Tag](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_Tag.html): The metadata that you apply to a resource to help you categorize and organize them.
