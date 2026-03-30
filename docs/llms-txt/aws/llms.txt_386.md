# Source: https://docs.aws.amazon.com/finspace/latest/management-api/llms.txt

# Amazon FinSpace Management API Reference

> Provides detailed development instructions for managing an Amazon FinSpace environment.

- [What is Amazon FinSpace](https://docs.aws.amazon.com/finspace/latest/management-api/fs-api-welcome.html)
- [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html)
- [AWS Glossary](https://docs.aws.amazon.com/finspace/latest/management-api/glossary.html)

## [API Operations by Topic](https://docs.aws.amazon.com/finspace/latest/management-api/fs-api-operations-by-topic.html)

- [Dataset browser environment operations](https://docs.aws.amazon.com/finspace/latest/management-api/environment.html): The API operations in this section control FinSpace environment.
- [Managed kdb environment operations](https://docs.aws.amazon.com/finspace/latest/management-api/kx-environment.html): The API operations in this section control Managed kdb environment.
- [Managed kdb database operations](https://docs.aws.amazon.com/finspace/latest/management-api/kx-database.html): The API operations in this section control Managed kdb database.
- [Managed kdb volumes operations](https://docs.aws.amazon.com/finspace/latest/management-api/kx-volumes.html): The API operations in this section control Managed kdb volumes.
- [Managed kdb scaling groups operations](https://docs.aws.amazon.com/finspace/latest/management-api/kx-sg.html): The API operations in this section control Managed kdb scaling groups.
- [Managed kdb cluster operations](https://docs.aws.amazon.com/finspace/latest/management-api/kx-cluster.html): The API operations in this section control Managed kdb cluster.
- [Tagging operations](https://docs.aws.amazon.com/finspace/latest/management-api/tag.html): The API operations in this section control tagging in FinSpace.


## [API Reference Index](https://docs.aws.amazon.com/finspace/latest/management-api/API_Reference.html)

### [Actions](https://docs.aws.amazon.com/finspace/latest/management-api/API_Operations.html)

The following actions are supported:

- [CreateEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateEnvironment.html): Create a new FinSpace environment.
- [CreateKxChangeset](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxChangeset.html): Creates a changeset for a kdb database.
- [CreateKxCluster](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxCluster.html): Creates a new kdb cluster.
- [CreateKxDatabase](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxDatabase.html): Creates a new kdb database in the environment.
- [CreateKxDataview](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxDataview.html): Creates a snapshot of kdb database with tiered storage capabilities and a pre-warmed cache, ready for mounting on kdb clusters.
- [CreateKxEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxEnvironment.html): Creates a managed kdb environment for the account.
- [CreateKxScalingGroup](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxScalingGroup.html): Creates a new scaling group.
- [CreateKxUser](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxUser.html): Creates a user in FinSpace kdb environment with an associated IAM role.
- [CreateKxVolume](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxVolume.html): Creates a new volume with a specific amount of throughput and storage capacity.
- [DeleteEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteEnvironment.html): Delete an FinSpace environment.
- [DeleteKxCluster](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxCluster.html): Deletes a kdb cluster.
- [DeleteKxClusterNode](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxClusterNode.html): Deletes the specified nodes from a cluster.
- [DeleteKxDatabase](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxDatabase.html): Deletes the specified database and all of its associated data.
- [DeleteKxDataview](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxDataview.html): Deletes the specified dataview.
- [DeleteKxEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxEnvironment.html): Deletes the kdb environment.
- [DeleteKxScalingGroup](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxScalingGroup.html): Deletes the specified scaling group.
- [DeleteKxUser](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxUser.html): Deletes a user in the specified kdb environment.
- [DeleteKxVolume](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxVolume.html): Deletes a volume.
- [GetEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetEnvironment.html): Returns the FinSpace environment object.
- [GetKxChangeset](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxChangeset.html): Returns information about a kdb changeset.
- [GetKxCluster](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxCluster.html): Retrieves information about a kdb cluster.
- [GetKxConnectionString](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxConnectionString.html): Retrieves a connection string for a user to connect to a kdb cluster.
- [GetKxDatabase](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxDatabase.html): Returns database information for the specified environment ID.
- [GetKxDataview](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxDataview.html): Retrieves details of the dataview.
- [GetKxEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxEnvironment.html): Retrieves all the information for the specified kdb environment.
- [GetKxScalingGroup](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxScalingGroup.html): Retrieves details of a scaling group.
- [GetKxUser](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxUser.html): Retrieves information about the specified kdb user.
- [GetKxVolume](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxVolume.html): Retrieves the information about the volume.
- [ListEnvironments](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListEnvironments.html): A list of all of your FinSpace environments.
- [ListKxChangesets](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxChangesets.html): Returns a list of all the changesets for a database.
- [ListKxClusterNodes](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxClusterNodes.html): Lists all the nodes in a kdb cluster.
- [ListKxClusters](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxClusters.html): Returns a list of clusters.
- [ListKxDatabases](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxDatabases.html): Returns a list of all the databases in the kdb environment.
- [ListKxDataviews](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxDataviews.html): Returns a list of all the dataviews in the database.
- [ListKxEnvironments](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxEnvironments.html): Returns a list of kdb environments created in an account.
- [ListKxScalingGroups](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxScalingGroups.html): Returns a list of scaling groups in a kdb environment.
- [ListKxUsers](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxUsers.html): Lists all the users in a kdb environment.
- [ListKxVolumes](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxVolumes.html): Lists all the volumes in a kdb environment.
- [ListTagsForResource](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListTagsForResource.html): A list of all tags for a resource.
- [TagResource](https://docs.aws.amazon.com/finspace/latest/management-api/API_TagResource.html): Adds metadata tags to a FinSpace resource.
- [UntagResource](https://docs.aws.amazon.com/finspace/latest/management-api/API_UntagResource.html): Removes metadata tags from a FinSpace resource.
- [UpdateEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateEnvironment.html): Update your FinSpace environment.
- [UpdateKxClusterCodeConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxClusterCodeConfiguration.html): Allows you to update code configuration on a running cluster.
- [UpdateKxClusterDatabases](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxClusterDatabases.html): Updates the databases mounted on a kdb cluster, which includes the changesetId and all the dbPaths to be cached.
- [UpdateKxDatabase](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxDatabase.html): Updates information for the given kdb database.
- [UpdateKxDataview](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxDataview.html): Updates the specified dataview.
- [UpdateKxEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxEnvironment.html): Updates information for the given kdb environment.
- [UpdateKxEnvironmentNetwork](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxEnvironmentNetwork.html): Updates environment network to connect to your internal network by using a transit gateway.
- [UpdateKxUser](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxUser.html): Updates the user details.
- [UpdateKxVolume](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxVolume.html): Updates the throughput or capacity of a volume.

### [Data Types](https://docs.aws.amazon.com/finspace/latest/management-api/API_Types.html)

The following data types are supported:

- [AutoScalingConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_AutoScalingConfiguration.html): The configuration based on which FinSpace will scale in or scale out nodes in your cluster.
- [CapacityConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_CapacityConfiguration.html): A structure for the metadata of a cluster.
- [ChangeRequest](https://docs.aws.amazon.com/finspace/latest/management-api/API_ChangeRequest.html): A list of change request objects.
- [CodeConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_CodeConfiguration.html): The structure of the customer code available within the running cluster.
- [CustomDNSServer](https://docs.aws.amazon.com/finspace/latest/management-api/API_CustomDNSServer.html): A list of DNS server name and server IP.
- [Environment](https://docs.aws.amazon.com/finspace/latest/management-api/API_Environment.html): Represents an FinSpace environment.
- [ErrorInfo](https://docs.aws.amazon.com/finspace/latest/management-api/API_ErrorInfo.html): Provides details in the event of a failed flow, including the error type and the related error message.
- [FederationParameters](https://docs.aws.amazon.com/finspace/latest/management-api/API_FederationParameters.html): Configuration information when authentication mode is FEDERATED.
- [IcmpTypeCode](https://docs.aws.amazon.com/finspace/latest/management-api/API_IcmpTypeCode.html): Defines the ICMP protocol that consists of the ICMP type and code.
- [KxAttachedCluster](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxAttachedCluster.html): The structure containing the metadata of the attached clusters.
- [KxCacheStorageConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxCacheStorageConfiguration.html): The configuration for read only disk cache associated with a cluster.
- [KxChangesetListEntry](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxChangesetListEntry.html): Details of changeset.
- [KxCluster](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxCluster.html): The details of a kdb cluster.
- [KxClusterCodeDeploymentConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxClusterCodeDeploymentConfiguration.html): The configuration that allows you to choose how you want to update code on a cluster.
- [KxCommandLineArgument](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxCommandLineArgument.html): Defines the key-value pairs to make them available inside the cluster.
- [KxDatabaseCacheConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDatabaseCacheConfiguration.html): The structure of database cache configuration that is used for mapping database paths to cache types in clusters.
- [KxDatabaseConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDatabaseConfiguration.html): The configuration of data that is available for querying from this database.
- [KxDatabaseListEntry](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDatabaseListEntry.html): Details about a FinSpace managed kdb database
- [KxDataviewActiveVersion](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDataviewActiveVersion.html): The active version of the dataview that is currently in use by this cluster.
- [KxDataviewConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDataviewConfiguration.html): The structure that stores the configuration details of a dataview.
- [KxDataviewListEntry](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDataviewListEntry.html): A collection of kdb dataview entries.
- [KxDataviewSegmentConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDataviewSegmentConfiguration.html): The configuration that contains the database path of the data that you want to place on each selected volume.
- [KxDeploymentConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDeploymentConfiguration.html): The configuration that allows you to choose how you want to update the databases on a cluster.
- [KxEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxEnvironment.html): The details of a kdb environment.
- [KxNAS1Configuration](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxNAS1Configuration.html): The structure containing the size and type of the network attached storage (NAS_1) file system volume.
- [KxNode](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxNode.html): A structure that stores metadata for a kdb node.
- [KxSavedownStorageConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxSavedownStorageConfiguration.html): The size and type of temporary storage that is used to hold data during the savedown process.
- [KxScalingGroup](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxScalingGroup.html): A structure for storing metadata of scaling group.
- [KxScalingGroupConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxScalingGroupConfiguration.html): The structure that stores the capacity configuration details of a scaling group.
- [KxUser](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxUser.html): A structure that stores metadata for a kdb user.
- [KxVolume](https://docs.aws.amazon.com/finspace/latest/management-api/API_KxVolume.html): The structure that contains the metadata of the volume.
- [NetworkACLEntry](https://docs.aws.amazon.com/finspace/latest/management-api/API_NetworkACLEntry.html): The network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets.
- [PortRange](https://docs.aws.amazon.com/finspace/latest/management-api/API_PortRange.html): The range of ports the rule applies to.
- [SuperuserParameters](https://docs.aws.amazon.com/finspace/latest/management-api/API_SuperuserParameters.html): Configuration information for the superuser.
- [TickerplantLogConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_TickerplantLogConfiguration.html): A configuration to store the Tickerplant logs.
- [TransitGatewayConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_TransitGatewayConfiguration.html): The structure of the transit gateway and network configuration that is used to connect the kdb environment to an internal network.
- [Volume](https://docs.aws.amazon.com/finspace/latest/management-api/API_Volume.html): The structure that consists of name and type of volume.
- [VpcConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_VpcConfiguration.html): Configuration details about the network where the Privatelink endpoint of the cluster resides.
- [Common Errors](https://docs.aws.amazon.com/finspace/latest/management-api/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
- [Common Parameters](https://docs.aws.amazon.com/finspace/latest/management-api/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
