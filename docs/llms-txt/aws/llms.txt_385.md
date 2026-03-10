# Source: https://docs.aws.amazon.com/finspace/latest/data-api/llms.txt

# Amazon FinSpace Data API Reference

> Provides detailed development instructions for using FinSpace features.

- [Welcome](https://docs.aws.amazon.com/finspace/latest/data-api/fs-api-welcome.html)
- [Using the dataset browser API](https://docs.aws.amazon.com/finspace/latest/data-api/fs-using-the-finspace-api.html)
- [Operations by topic](https://docs.aws.amazon.com/finspace/latest/data-api/fs-api-operations-by-topic.html)
- [AWS Glossary](https://docs.aws.amazon.com/finspace/latest/data-api/glossary.html)

## [API reference index](https://docs.aws.amazon.com/finspace/latest/data-api/API_Reference.html)

### [Actions](https://docs.aws.amazon.com/finspace/latest/data-api/API_Operations.html)

The following actions are supported:

- [AssociateUserToPermissionGroup](https://docs.aws.amazon.com/finspace/latest/data-api/API_AssociateUserToPermissionGroup.html): Adds a user to a permission group to grant permissions for actions a user can perform in FinSpace.
- [CreateChangeset](https://docs.aws.amazon.com/finspace/latest/data-api/API_CreateChangeset.html): Creates a new Changeset in a FinSpace Dataset.
- [CreateDataset](https://docs.aws.amazon.com/finspace/latest/data-api/API_CreateDataset.html): Creates a new FinSpace Dataset.
- [CreateDataView](https://docs.aws.amazon.com/finspace/latest/data-api/API_CreateDataView.html): Creates a Dataview for a Dataset.
- [CreatePermissionGroup](https://docs.aws.amazon.com/finspace/latest/data-api/API_CreatePermissionGroup.html): Creates a group of permissions for various actions that a user can perform in FinSpace.
- [CreateUser](https://docs.aws.amazon.com/finspace/latest/data-api/API_CreateUser.html): Creates a new user in FinSpace.
- [DeleteDataset](https://docs.aws.amazon.com/finspace/latest/data-api/API_DeleteDataset.html): Deletes a FinSpace Dataset.
- [DeletePermissionGroup](https://docs.aws.amazon.com/finspace/latest/data-api/API_DeletePermissionGroup.html): Deletes a permission group.
- [DisableUser](https://docs.aws.amazon.com/finspace/latest/data-api/API_DisableUser.html): Denies access to the FinSpace web application and API for the specified user.
- [DisassociateUserFromPermissionGroup](https://docs.aws.amazon.com/finspace/latest/data-api/API_DisassociateUserFromPermissionGroup.html): Removes a user from a permission group.
- [EnableUser](https://docs.aws.amazon.com/finspace/latest/data-api/API_EnableUser.html): Allows the specified user to access the FinSpace web application and API.
- [GetChangeset](https://docs.aws.amazon.com/finspace/latest/data-api/API_GetChangeset.html): Get information about a Changeset.
- [GetDataset](https://docs.aws.amazon.com/finspace/latest/data-api/API_GetDataset.html): Returns information about a Dataset.
- [GetDataView](https://docs.aws.amazon.com/finspace/latest/data-api/API_GetDataView.html): Gets information about a Dataview.
- [GetExternalDataViewAccessDetails](https://docs.aws.amazon.com/finspace/latest/data-api/API_GetExternalDataViewAccessDetails.html): Returns the credentials to access the external Dataview from an S3 location.
- [GetPermissionGroup](https://docs.aws.amazon.com/finspace/latest/data-api/API_GetPermissionGroup.html): Retrieves the details of a specific permission group.
- [GetProgrammaticAccessCredentials](https://docs.aws.amazon.com/finspace/latest/data-api/API_GetProgrammaticAccessCredentials.html): Request programmatic credentials to use with FinSpace SDK.
- [GetUser](https://docs.aws.amazon.com/finspace/latest/data-api/API_GetUser.html): Retrieves details for a specific user.
- [GetWorkingLocation](https://docs.aws.amazon.com/finspace/latest/data-api/API_GetWorkingLocation.html): A temporary Amazon S3 location, where you can copy your files from a source location to stage or use as a scratch space in FinSpace notebook.
- [ListChangesets](https://docs.aws.amazon.com/finspace/latest/data-api/API_ListChangesets.html): Lists the FinSpace Changesets for a Dataset.
- [ListDatasets](https://docs.aws.amazon.com/finspace/latest/data-api/API_ListDatasets.html): Lists all of the active Datasets that a user has access to.
- [ListDataViews](https://docs.aws.amazon.com/finspace/latest/data-api/API_ListDataViews.html): Lists all available Dataviews for a Dataset.
- [ListPermissionGroups](https://docs.aws.amazon.com/finspace/latest/data-api/API_ListPermissionGroups.html): Lists all available permission groups in FinSpace.
- [ListPermissionGroupsByUser](https://docs.aws.amazon.com/finspace/latest/data-api/API_ListPermissionGroupsByUser.html): Lists all the permission groups that are associated with a specific user.
- [ListUsers](https://docs.aws.amazon.com/finspace/latest/data-api/API_ListUsers.html): Lists all available users in FinSpace.
- [ListUsersByPermissionGroup](https://docs.aws.amazon.com/finspace/latest/data-api/API_ListUsersByPermissionGroup.html): Lists details of all the users in a specific permission group.
- [ResetUserPassword](https://docs.aws.amazon.com/finspace/latest/data-api/API_ResetUserPassword.html): Resets the password for a specified user ID and generates a temporary one.
- [UpdateChangeset](https://docs.aws.amazon.com/finspace/latest/data-api/API_UpdateChangeset.html): Updates a FinSpace Changeset.
- [UpdateDataset](https://docs.aws.amazon.com/finspace/latest/data-api/API_UpdateDataset.html): Updates a FinSpace Dataset.
- [UpdatePermissionGroup](https://docs.aws.amazon.com/finspace/latest/data-api/API_UpdatePermissionGroup.html): Modifies the details of a permission group.
- [UpdateUser](https://docs.aws.amazon.com/finspace/latest/data-api/API_UpdateUser.html): Modifies the details of the specified user.

### [Data Types](https://docs.aws.amazon.com/finspace/latest/data-api/API_Types.html)

The following data types are supported:

- [AwsCredentials](https://docs.aws.amazon.com/finspace/latest/data-api/API_AwsCredentials.html): The credentials required to access the external Dataview from the S3 location.
- [ChangesetErrorInfo](https://docs.aws.amazon.com/finspace/latest/data-api/API_ChangesetErrorInfo.html): The structure with error messages.
- [ChangesetSummary](https://docs.aws.amazon.com/finspace/latest/data-api/API_ChangesetSummary.html): A Changeset is unit of data in a Dataset.
- [ColumnDefinition](https://docs.aws.amazon.com/finspace/latest/data-api/API_ColumnDefinition.html): The definition of a column in a tabular Dataset.
- [Credentials](https://docs.aws.amazon.com/finspace/latest/data-api/API_Credentials.html): Short term API credentials.
- [Dataset](https://docs.aws.amazon.com/finspace/latest/data-api/API_Dataset.html): The structure for a Dataset.
- [DatasetOwnerInfo](https://docs.aws.amazon.com/finspace/latest/data-api/API_DatasetOwnerInfo.html): A structure for Dataset owner info.
- [DataViewDestinationTypeParams](https://docs.aws.amazon.com/finspace/latest/data-api/API_DataViewDestinationTypeParams.html): Structure for the Dataview destination type parameters.
- [DataViewErrorInfo](https://docs.aws.amazon.com/finspace/latest/data-api/API_DataViewErrorInfo.html): The structure with error messages.
- [DataViewSummary](https://docs.aws.amazon.com/finspace/latest/data-api/API_DataViewSummary.html): Structure for the summary of a Dataview.
- [PermissionGroup](https://docs.aws.amazon.com/finspace/latest/data-api/API_PermissionGroup.html): The structure for a permission group.
- [PermissionGroupByUser](https://docs.aws.amazon.com/finspace/latest/data-api/API_PermissionGroupByUser.html): The structure of a permission group associated with a user.
- [PermissionGroupParams](https://docs.aws.amazon.com/finspace/latest/data-api/API_PermissionGroupParams.html): Permission group parameters for Dataset permissions.
- [ResourcePermission](https://docs.aws.amazon.com/finspace/latest/data-api/API_ResourcePermission.html): Resource permission for a dataset.
- [S3Location](https://docs.aws.amazon.com/finspace/latest/data-api/API_S3Location.html): The location of an external Dataview in an S3 bucket.
- [SchemaDefinition](https://docs.aws.amazon.com/finspace/latest/data-api/API_SchemaDefinition.html): Definition for a schema on a tabular Dataset.
- [SchemaUnion](https://docs.aws.amazon.com/finspace/latest/data-api/API_SchemaUnion.html): A union of schema types.
- [User](https://docs.aws.amazon.com/finspace/latest/data-api/API_User.html): The details of the user.
- [UserByPermissionGroup](https://docs.aws.amazon.com/finspace/latest/data-api/API_UserByPermissionGroup.html): The structure of a user associated with a permission group.
- [Common Errors](https://docs.aws.amazon.com/finspace/latest/data-api/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
- [Common Parameters](https://docs.aws.amazon.com/finspace/latest/data-api/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
