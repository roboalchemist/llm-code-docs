# Source: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/llms.txt

# AWS Cloud Control API API Reference

> This is the API Reference for AWS Cloud Control API. With Cloud Control API, you can create, read, update, delete, and list (CRUD-L) your cloud resources that belong to AWS and third-party services. With the Cloud Control API standardized set of application programming interfaces (APIs), you can perform CRUD-L operations on any supported resources in your AWS account. Using Cloud Control API, you won't have to generate code or scripts specific to each individual service responsible for those resources.

- [Welcome](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_Operations.html)

- [CancelResourceRequest](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_CancelResourceRequest.html): Cancels the specified resource operation request.
- [CreateResource](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_CreateResource.html): Creates the specified resource.
- [DeleteResource](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_DeleteResource.html): Deletes the specified resource.
- [GetResource](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResource.html): Returns information about the current state of the specified resource.
- [GetResourceRequestStatus](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html): Returns the current status of a resource operation request.
- [ListResourceRequests](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ListResourceRequests.html): Returns existing resource operation requests.
- [ListResources](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ListResources.html): Returns information about the specified resources.
- [UpdateResource](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_UpdateResource.html): Updates the specified property values in the resource.


## [Data Types](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_Types.html)

- [HookProgressEvent](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_HookProgressEvent.html): Represents the current status of a Hook operation request for the target resource.
- [ProgressEvent](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ProgressEvent.html): Represents the current status of a resource operation request.
- [ResourceDescription](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ResourceDescription.html): Represents information about a provisioned resource.
- [ResourceRequestStatusFilter](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ResourceRequestStatusFilter.html): The filter criteria to use in determining the requests returned.
