# Source: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/llms.txt

# Amazon Aurora DSQL Welcome

> This is an interface reference for Amazon Aurora DSQL. It contains documentation for one of the programming or command line interfaces you can use to manage Amazon Aurora DSQL.

- [Welcome](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_Operations.html)

- [CreateCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateCluster.html): The CreateCluster API allows you to create both single-Region clusters and multi-Region clusters.
- [DeleteCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_DeleteCluster.html): Deletes a cluster in Amazon Aurora DSQL.
- [DeleteClusterPolicy](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_DeleteClusterPolicy.html): Deletes the resource-based policy attached to a cluster.
- [GetCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetCluster.html): Retrieves information about a cluster.
- [GetClusterPolicy](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetClusterPolicy.html): Retrieves the resource-based policy document attached to a cluster.
- [GetVpcEndpointServiceName](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetVpcEndpointServiceName.html): Retrieves the VPC endpoint service name.
- [ListClusters](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListClusters.html): Retrieves information about a list of clusters.
- [ListTagsForResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListTagsForResource.html): Lists all of the tags for a resource.
- [PutClusterPolicy](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_PutClusterPolicy.html): Attaches a resource-based policy to a cluster.
- [TagResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_TagResource.html): Tags a resource with a map of key and value pairs.
- [UntagResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_UntagResource.html): Removes a tag from a resource.
- [UpdateCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_UpdateCluster.html): The UpdateCluster API allows you to modify both single-Region and multi-Region cluster configurations.


## [Data Types](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_Types.html)

- [ClusterSummary](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ClusterSummary.html): A summary of the properties of a cluster.
- [EncryptionDetails](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_EncryptionDetails.html): Configuration details about encryption for the cluster including the AWS KMS key ARN, encryption type, and encryption status.
- [MultiRegionProperties](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_MultiRegionProperties.html): Defines the structure for multi-Region cluster configurations, containing the witness region and linked cluster settings.
- [ValidationExceptionField](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ValidationExceptionField.html): Stores information about a field passed inside a request that resulted in an validation error.
