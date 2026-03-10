# Source: https://docs.aws.amazon.com/codeconnections/latest/APIReference/llms.txt

# AWS CodeConnections API Reference

> This AWS CodeConnections API Reference provides descriptions and usage examples of the operations and data types for the AWS CodeConnections API. You can use the connections API to work with connections and installations.

- [Welcome](https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/codeconnections/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/codeconnections/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_Operations.html)

- [CreateConnection](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateConnection.html): Creates a connection that can then be given to other AWS services like CodePipeline so that it can access third-party code repositories.
- [CreateHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateHost.html): Creates a resource that represents the infrastructure where a third-party provider is installed.
- [CreateRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateRepositoryLink.html): Creates a link to a specified external Git repository.
- [CreateSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateSyncConfiguration.html): Creates a sync configuration which allows AWS to sync content from a Git repository to update a specified AWS resource.
- [DeleteConnection](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteConnection.html): The connection to be deleted.
- [DeleteHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteHost.html): The host to be deleted.
- [DeleteRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteRepositoryLink.html): Deletes the association between your connection and a specified external Git repository.
- [DeleteSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteSyncConfiguration.html): Deletes the sync configuration for a specified repository and connection.
- [GetConnection](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetConnection.html): Returns the connection ARN and details such as status, owner, and provider type.
- [GetHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetHost.html): Returns the host ARN and details such as status, provider type, endpoint, and, if applicable, the VPC configuration.
- [GetRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetRepositoryLink.html): Returns details about a repository link.
- [GetRepositorySyncStatus](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetRepositorySyncStatus.html): Returns details about the sync status for a repository.
- [GetResourceSyncStatus](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetResourceSyncStatus.html): Returns the status of the sync with the Git repository for a specific AWS resource.
- [GetSyncBlockerSummary](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetSyncBlockerSummary.html): Returns a list of the most recent sync blockers.
- [GetSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetSyncConfiguration.html): Returns details about a sync configuration, including the sync type and resource name.
- [ListConnections](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListConnections.html): Lists the connections associated with your account.
- [ListHosts](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListHosts.html): Lists the hosts associated with your account.
- [ListRepositoryLinks](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListRepositoryLinks.html): Lists the repository links created for connections in your account.
- [ListRepositorySyncDefinitions](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListRepositorySyncDefinitions.html): Lists the repository sync definitions for repository links in your account.
- [ListSyncConfigurations](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListSyncConfigurations.html): Returns a list of sync configurations for a specified repository.
- [ListTagsForResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListTagsForResource.html): Gets the set of key-value pairs (metadata) that are used to manage the resource.
- [TagResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_TagResource.html): Adds to or modifies the tags of the given resource.
- [UntagResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UntagResource.html): Removes tags from an AWS resource.
- [UpdateHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateHost.html): Updates a specified host with the provided configurations.
- [UpdateRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateRepositoryLink.html): Updates the association between your connection and a specified external Git repository.
- [UpdateSyncBlocker](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateSyncBlocker.html): Allows you to update the status of a sync blocker, resolving the blocker and allowing syncing to continue.
- [UpdateSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateSyncConfiguration.html): Updates the sync configuration for your connection and a specified external Git repository.


## [Data Types](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_Types.html)

- [Connection](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_Connection.html): A resource that is used to connect third-party source providers with services like CodePipeline.
- [Host](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_Host.html): A resource that represents the infrastructure where a third-party provider is installed.
- [RepositoryLinkInfo](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_RepositoryLinkInfo.html): Information about the repository link resource, such as the repository link ARN, the associated connection ARN, encryption key ARN, and owner ID.
- [RepositorySyncAttempt](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_RepositorySyncAttempt.html): Information about a repository sync attempt for a repository with a sync configuration.
- [RepositorySyncDefinition](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_RepositorySyncDefinition.html): The definition for a repository with a sync configuration.
- [RepositorySyncEvent](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_RepositorySyncEvent.html): Information about a repository sync event.
- [ResourceSyncAttempt](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ResourceSyncAttempt.html): Information about a resource sync attempt.
- [ResourceSyncEvent](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ResourceSyncEvent.html): Information about a resource sync event for the resource associated with a sync configuration.
- [Revision](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_Revision.html): Information about the revision for a specific sync event, such as the branch, owner ID, and name of the repository.
- [SyncBlocker](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_SyncBlocker.html): Information about a blocker for a sync event.
- [SyncBlockerContext](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_SyncBlockerContext.html): The context for a specific sync blocker.
- [SyncBlockerSummary](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_SyncBlockerSummary.html): A summary for sync blockers.
- [SyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_SyncConfiguration.html): Information, such as repository, branch, provider, and resource names for a specific sync configuration.
- [Tag](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_Tag.html): A tag is a key-value pair that is used to manage the resource.
- [VpcConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_VpcConfiguration.html): The VPC configuration provisioned for the host.
