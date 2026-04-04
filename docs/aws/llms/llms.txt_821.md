# Source: https://docs.aws.amazon.com/tnb/latest/APIReference/llms.txt

# AWS Telco Network Builder API Reference

> AWS Telco Network Builder (TNB) is a network automation service that helps you deploy and manage telecom networks. AWS TNB helps you with the lifecycle management of your telecommunication network functions throughout planning, deployment, and post-deployment activities.

- [Welcome](https://docs.aws.amazon.com/tnb/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/tnb/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/tnb/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/tnb/latest/APIReference/API_Operations.html)

- [CancelSolNetworkOperation](https://docs.aws.amazon.com/tnb/latest/APIReference/API_CancelSolNetworkOperation.html): Cancels a network operation.
- [CreateSolFunctionPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolFunctionPackage.html): Creates a function package.
- [CreateSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolNetworkInstance.html): Creates a network instance.
- [CreateSolNetworkPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolNetworkPackage.html): Creates a network package.
- [DeleteSolFunctionPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_DeleteSolFunctionPackage.html): Deletes a function package.
- [DeleteSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_DeleteSolNetworkInstance.html): Deletes a network instance.
- [DeleteSolNetworkPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_DeleteSolNetworkPackage.html): Deletes network package.
- [GetSolFunctionInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionInstance.html): Gets the details of a network function instance, including the instantiation state and metadata from the function package descriptor in the network function package.
- [GetSolFunctionPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionPackage.html): Gets the details of an individual function package, such as the operational state and whether the package is in use.
- [GetSolFunctionPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionPackageContent.html): Gets the contents of a function package.
- [GetSolFunctionPackageDescriptor](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionPackageDescriptor.html): Gets a function package descriptor in a function package.
- [GetSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkInstance.html): Gets the details of the network instance.
- [GetSolNetworkOperation](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkOperation.html): Gets the details of a network operation, including the tasks involved in the network operation and the status of the tasks.
- [GetSolNetworkPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkPackage.html): Gets the details of a network package.
- [GetSolNetworkPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkPackageContent.html): Gets the contents of a network package.
- [GetSolNetworkPackageDescriptor](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkPackageDescriptor.html): Gets the content of the network service descriptor.
- [InstantiateSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_InstantiateSolNetworkInstance.html): Instantiates a network instance.
- [ListSolFunctionInstances](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionInstances.html): Lists network function instances.
- [ListSolFunctionPackages](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionPackages.html): Lists information about function packages.
- [ListSolNetworkInstances](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkInstances.html): Lists your network instances.
- [ListSolNetworkOperations](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkOperations.html): Lists details for a network operation, including when the operation started and the status of the operation.
- [ListSolNetworkPackages](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkPackages.html): Lists network packages.
- [ListTagsForResource](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListTagsForResource.html): Lists tags for AWS TNB resources.
- [PutSolFunctionPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolFunctionPackageContent.html): Uploads the contents of a function package.
- [PutSolNetworkPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolNetworkPackageContent.html): Uploads the contents of a network package.
- [TagResource](https://docs.aws.amazon.com/tnb/latest/APIReference/API_TagResource.html): Tags an AWS TNB resource.
- [TerminateSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_TerminateSolNetworkInstance.html): Terminates a network instance.
- [UntagResource](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UntagResource.html): Untags an AWS TNB resource.
- [UpdateSolFunctionPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolFunctionPackage.html): Updates the operational state of function package.
- [UpdateSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkInstance.html): Update a network instance.
- [UpdateSolNetworkPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkPackage.html): Updates the operational state of a network package.
- [ValidateSolFunctionPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ValidateSolFunctionPackageContent.html): Validates function package content.
- [ValidateSolNetworkPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ValidateSolNetworkPackageContent.html): Validates network package content.


## [Data Types](https://docs.aws.amazon.com/tnb/latest/APIReference/API_Types.html)

- [ErrorInfo](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ErrorInfo.html): Provides error information.
- [FunctionArtifactMeta](https://docs.aws.amazon.com/tnb/latest/APIReference/API_FunctionArtifactMeta.html): Metadata for function package artifacts.
- [GetSolFunctionInstanceMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionInstanceMetadata.html): The metadata of a network function instance.
- [GetSolFunctionPackageMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionPackageMetadata.html): Metadata related to the function package.
- [GetSolInstantiatedVnfInfo](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolInstantiatedVnfInfo.html): Information about a network function.
- [GetSolNetworkInstanceMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkInstanceMetadata.html): The metadata of a network instance.
- [GetSolNetworkOperationMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkOperationMetadata.html): Metadata related to a network operation occurrence.
- [GetSolNetworkOperationTaskDetails](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkOperationTaskDetails.html): Gets the details of a network operation.
- [GetSolNetworkPackageMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkPackageMetadata.html): Metadata associated with a network package.
- [GetSolVnfcResourceInfo](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolVnfcResourceInfo.html): Details of resource associated with a network function.
- [GetSolVnfcResourceInfoMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolVnfcResourceInfoMetadata.html): The metadata of a network function.
- [GetSolVnfInfo](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolVnfInfo.html): Information about the network function.
- [InstantiateMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_InstantiateMetadata.html): Metadata related to the configuration properties used during instantiation of the network instance.
- [LcmOperationInfo](https://docs.aws.amazon.com/tnb/latest/APIReference/API_LcmOperationInfo.html): Lifecycle management operation details on the network instance.
- [ListSolFunctionInstanceInfo](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionInstanceInfo.html): Lists information about a network function instance.
- [ListSolFunctionInstanceMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionInstanceMetadata.html): Lists network function instance metadata.
- [ListSolFunctionPackageInfo](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionPackageInfo.html): Information about a function package.
- [ListSolFunctionPackageMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionPackageMetadata.html): Details for the function package metadata.
- [ListSolNetworkInstanceInfo](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkInstanceInfo.html): Info about the specific network instance.
- [ListSolNetworkInstanceMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkInstanceMetadata.html): Metadata details for a network instance.
- [ListSolNetworkOperationsInfo](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkOperationsInfo.html): Information parameters for a network operation.
- [ListSolNetworkOperationsMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkOperationsMetadata.html): Metadata related to a network operation.
- [ListSolNetworkPackageInfo](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkPackageInfo.html): Details of a network package.
- [ListSolNetworkPackageMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkPackageMetadata.html): Metadata related to a network package.
- [ModifyVnfInfoMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ModifyVnfInfoMetadata.html): Metadata related to the configuration properties used during update of a specific network function in a network instance.
- [NetworkArtifactMeta](https://docs.aws.amazon.com/tnb/latest/APIReference/API_NetworkArtifactMeta.html): Metadata for network package artifacts.
- [ProblemDetails](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ProblemDetails.html): Details related to problems with AWS TNB resources.
- [PutSolFunctionPackageContentMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolFunctionPackageContentMetadata.html): Update metadata in a function package.
- [PutSolNetworkPackageContentMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolNetworkPackageContentMetadata.html): Update metadata in a network package.
- [ToscaOverride](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ToscaOverride.html): Overrides of the TOSCA node.
- [UpdateNsMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateNsMetadata.html): Metadata related to the configuration properties used during update of a network instance.
- [UpdateSolNetworkModify](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkModify.html): Information parameters and/or the configurable properties for a network function.
- [UpdateSolNetworkServiceData](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkServiceData.html): Information parameters and/or the configurable properties for a network descriptor used for update.
- [ValidateSolFunctionPackageContentMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ValidateSolFunctionPackageContentMetadata.html): Validates function package content metadata.
- [ValidateSolNetworkPackageContentMetadata](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ValidateSolNetworkPackageContentMetadata.html): Validates network package content metadata.
