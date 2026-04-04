# Source: https://docs.aws.amazon.com/memorydb/latest/APIReference/llms.txt

# Amazon MemoryDB API Reference

> MemoryDB is a fully managed, Redis OSS-compatible, in-memory database that delivers ultra-fast performance and Multi-AZ durability for modern applications built using microservices architectures. MemoryDB stores the entire database in-memory, enabling low latency and high throughput data access. It is compatible with Redis OSS, a popular open source data store, enabling you to leverage Redis OSSâ flexible and friendly data structures, APIs, and commands.

- [Welcome](https://docs.aws.amazon.com/memorydb/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/memorydb/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/memorydb/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Operations.html)

- [BatchUpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_BatchUpdateCluster.html): Apply the service update to a list of clusters supplied.
- [CopySnapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CopySnapshot.html): Makes a copy of an existing snapshot.
- [CreateACL](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateACL.html): Creates an Access Control List.
- [CreateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateCluster.html): Creates a cluster.
- [CreateMultiRegionCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateMultiRegionCluster.html): Creates a new multi-Region cluster.
- [CreateParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateParameterGroup.html): Creates a new MemoryDB parameter group.
- [CreateSnapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateSnapshot.html): Creates a copy of an entire cluster at a specific moment in time.
- [CreateSubnetGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateSubnetGroup.html): Creates a subnet group.
- [CreateUser](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateUser.html): Creates a MemoryDB user.
- [DeleteACL](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteACL.html): Deletes an Access Control List.
- [DeleteCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteCluster.html): Deletes a cluster.
- [DeleteMultiRegionCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteMultiRegionCluster.html): Deletes an existing multi-Region cluster.
- [DeleteParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteParameterGroup.html): Deletes the specified parameter group.
- [DeleteSnapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteSnapshot.html): Deletes an existing snapshot.
- [DeleteSubnetGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteSubnetGroup.html): Deletes a subnet group.
- [DeleteUser](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteUser.html): Deletes a user.
- [DescribeACLs](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeACLs.html): Returns a list of ACLs.
- [DescribeClusters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeClusters.html): Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cluster if a cluster name is supplied.
- [DescribeEngineVersions](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeEngineVersions.html): Returns a list of the available Redis OSS engine versions.
- [DescribeEvents](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeEvents.html): Returns events related to clusters, security groups, and parameter groups.
- [DescribeMultiRegionClusters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeMultiRegionClusters.html): Returns details about one or more multi-Region clusters.
- [DescribeParameterGroups](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeParameterGroups.html): Returns a list of parameter group descriptions.
- [DescribeParameters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeParameters.html): Returns the detailed parameter list for a particular parameter group.
- [DescribeReservedNodes](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeReservedNodes.html): Returns information about reserved nodes for this account, or about a specified reserved node.
- [DescribeReservedNodesOfferings](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeReservedNodesOfferings.html): Lists available reserved node offerings.
- [DescribeServiceUpdates](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeServiceUpdates.html): Returns details of the service updates.
- [DescribeSnapshots](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeSnapshots.html): Returns information about cluster snapshots.
- [DescribeSubnetGroups](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeSubnetGroups.html): Returns a list of subnet group descriptions.
- [DescribeUsers](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeUsers.html): Returns a list of users.
- [FailoverShard](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_FailoverShard.html): Used to failover a shard.
- [ListAllowedMultiRegionClusterUpdates](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListAllowedMultiRegionClusterUpdates.html): Lists the allowed updates for a multi-Region cluster.
- [ListAllowedNodeTypeUpdates](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListAllowedNodeTypeUpdates.html): Lists all available node types that you can scale to from your cluster's current node type.
- [ListTags](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListTags.html): Lists all tags currently on a named resource.
- [PurchaseReservedNodesOffering](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_PurchaseReservedNodesOffering.html): Allows you to purchase a reserved node offering.
- [ResetParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ResetParameterGroup.html): Modifies the parameters of a parameter group to the engine or system default value.
- [TagResource](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_TagResource.html): Use this operation to add tags to a resource.
- [UntagResource](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UntagResource.html): Use this operation to remove tags on a resource.
- [UpdateACL](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateACL.html): Changes the list of users that belong to the Access Control List.
- [UpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateCluster.html): Modifies the settings for a cluster.
- [UpdateMultiRegionCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateMultiRegionCluster.html): Updates the configuration of an existing multi-Region cluster.
- [UpdateParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateParameterGroup.html): Updates the parameters of a parameter group.
- [UpdateSubnetGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateSubnetGroup.html): Updates a subnet group.
- [UpdateUser](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateUser.html): Changes user password(s) and/or access string.


## [Data Types](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Types.html)

- [ACL](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ACL.html): An Access Control List.
- [ACLPendingChanges](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ACLPendingChanges.html): Returns the updates being applied to the ACL.
- [ACLsUpdateStatus](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ACLsUpdateStatus.html): The status of the ACL update
- [Authentication](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Authentication.html): Denotes the user's authentication properties, such as whether it requires a password to authenticate.
- [AuthenticationMode](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_AuthenticationMode.html): Denotes the user's authentication properties, such as whether it requires a password to authenticate.
- [AvailabilityZone](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_AvailabilityZone.html): Indicates if the cluster has a Multi-AZ configuration (multiaz) or not (singleaz).
- [Cluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Cluster.html): Contains all of the attributes of a specific cluster.
- [ClusterConfiguration](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ClusterConfiguration.html): A list of cluster configuration options.
- [ClusterPendingUpdates](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ClusterPendingUpdates.html): A list of updates being applied to the cluster
- [Endpoint](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Endpoint.html): Represents the information required for client programs to connect to the cluster and its nodes.
- [EngineVersionInfo](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_EngineVersionInfo.html): Provides details of the Redis OSS engine version
- [Event](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Event.html): Represents a single occurrence of something interesting within the system.
- [Filter](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Filter.html): Used to streamline results of a search based on the property being filtered.
- [MultiRegionCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_MultiRegionCluster.html): Represents a multi-Region cluster.
- [Node](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Node.html): Represents an individual node within a cluster.
- [Parameter](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Parameter.html): Describes an individual setting that controls some aspect of MemoryDB behavior.
- [ParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ParameterGroup.html): Represents the output of a CreateParameterGroup operation.
- [ParameterNameValue](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ParameterNameValue.html): Describes a name-value pair that is used to update the value of a parameter.
- [PendingModifiedServiceUpdate](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_PendingModifiedServiceUpdate.html): Update action that has yet to be processed for the corresponding apply/stop request
- [RecurringCharge](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_RecurringCharge.html): The recurring charge to run this reserved node.
- [RegionalCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_RegionalCluster.html): Represents a Regional cluster
- [ReplicaConfigurationRequest](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ReplicaConfigurationRequest.html): A request to configure the number of replicas in a shard
- [ReservedNode](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ReservedNode.html): Represents the output of a PurchaseReservedNodesOffering operation.
- [ReservedNodesOffering](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ReservedNodesOffering.html): The offering type of this node.
- [ReshardingStatus](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ReshardingStatus.html): The status of the online resharding
- [SecurityGroupMembership](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_SecurityGroupMembership.html): Represents a single security group and its status.
- [ServiceUpdate](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ServiceUpdate.html): An update that you can apply to your MemoryDB clusters.
- [ServiceUpdateRequest](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ServiceUpdateRequest.html): A request to apply a service update
- [Shard](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Shard.html): Represents a collection of nodes in a cluster.
- [ShardConfiguration](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ShardConfiguration.html): Shard configuration options.
- [ShardConfigurationRequest](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ShardConfigurationRequest.html): A request to configure the sharding properties of a cluster
- [ShardDetail](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ShardDetail.html): Provides details of a shard in a snapshot
- [SlotMigration](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_SlotMigration.html): Represents the progress of an online resharding operation.
- [Snapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Snapshot.html): Represents a copy of an entire cluster as of the time when the snapshot was taken.
- [Subnet](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Subnet.html): Represents the subnet associated with a cluster.
- [SubnetGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_SubnetGroup.html): Represents the output of one of the following operations:
- [Tag](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Tag.html): A tag that can be added to an MemoryDB resource.
- [UnprocessedCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UnprocessedCluster.html): A cluster whose updates have failed
- [User](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_User.html): You create users and assign them specific permissions by using an access string.
