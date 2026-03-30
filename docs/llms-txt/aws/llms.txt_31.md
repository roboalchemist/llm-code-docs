# Source: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/llms.txt

# Amazon ElastiCache User Guide

> Amazon ElastiCache is a web service that makes it easy to set up, manage, and scale a distributed in-memory data store or cache in the cloud.

- [Quotas](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/quota-limits.html)
- [ElastiCache Documentation history](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatsNew.html)
- [AWS Glossary](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/glossary.html)

## [What is ElastiCache?](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)

- [Related services](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/related-services-choose-between-memorydb-and-redis.html): MemoryDB

### [How it works](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.corecomponents.html)

Here you can find an overview of the major components of an ElastiCache deployment.

- [Choosing between deployment options](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.deployment.html): Amazon ElastiCache has two deployment options:
- [ElastiCache resources](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.FirstTimeUser.html): We recommend that first time users begin by reading the following sections, and refer to them as needed.
- [AWS Regions and Availability Zones](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.AZs.html): Amazon cloud computing resources are housed in highly available data center facilities in different areas of the world (for example, North America, Europe, or Asia).
- [Use Cases](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-use-cases.html): Work with common ElastiCache use cases.


## [Getting started with ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.html)

- [Setting up ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/set-up.html): Set up a cache for ElastiCache.

### [Create a Valkey serverless cache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.serverless-valkey.step1.html)

Create a Valkey serverless cache

- [Read and write data](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.serverless-valkey.step2.html): Read and write data to the cache
- [Clean up](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.serverless-valkey.step3.html): As long as a cache is in the available state, you are being charged for it, whether or not you are actively using it.
- [Next Steps](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.serverless-valkey.next-steps.html): For more information about ElastiCache see the following pages:

### [Create a Redis OSS serverless cache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.serverless-redis.step1.html)

Create a Redis OSS serverless cache

- [Read and write data](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.serverless-redis.step2.html): Read and write data to the cache
- [Clean up](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.serverless-redis.step3.html): As long as a cache is in the available state, you are being charged for it, whether or not you are actively using it.
- [Next Steps](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.serverless-redis.next-steps.html): For more information about ElastiCache see the following pages:

### [Create a Memcached serverless cache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/create-serverless-cache-mem.html)

AWS Management Console

- [Read and write data](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/read-write-cache-mem.html): Read and write data
- [Clean up](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/read-write-cleanup-mem.html): As long as a cache is in the available state, you are being charged for it, whether or not you are actively using it.
- [Next Steps](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/next-steps-mem.html): Next steps and further information

### [Tutorials: Getting started with Python and ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ElastiCache-Getting-Started-Tutorials.html)

Provides tutorials on how to use the programming language Python with ElastiCache.

- [Python and ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ElastiCache-Getting-Started-Tutorials-Python.html): Discusses Python and ElastiCache for Redis OSS;
- [Tutorial: Configuring Lambda to access ElastiCache in a VPC](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/LambdaRedis.html): Configuring Lambda to access Amazon ElastiCache in an Amazon VPC.


## [Creating and managing a node-based ElastiCache cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/designing-elasticache-cluster.html)

- [Components and features](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.Components.html): Learn ElastiCache concepts and terminology, including definitions of nodes, clusters, security configuration, and Valkey and Redis OSS replication groups.
- [ElastiCache terminology](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.Terms.html): In October 2016, Amazon ElastiCache launched support for Redis OSS 3.2.

### [Tutorial: How to create a node-based ElastiCache cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.designing-cluster-pre.html)

Here is how to create a node-based ElastiCache cluster for Valkey, Memcached and Redis OSS.

- [Creating a node-based ElastiCache cluster for Valkey](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.designing-cluster-pre.valkey.html): Following are the one-time actions you must take to create a node-based ElastiCache cluster for Valkey.
- [Creating a node-based ElastiCache cluster for Redis OSS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.designing-cluster-pre.redis.html): Following are the one-time actions you must take in order to create a node-based ElastiCache cluster for Redis OSS.
- [Deleting a cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.Delete-gs.redis.html): As long as a cluster is in the available state, you are being charged for it, whether or not you are actively using it.
- [Other tutorials and videos](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Tutorials.html): Additional tutorials showing key scenarios for ElastiCache and using ElastiCache with other AWS services.

### [Managing nodes in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.html)

Identifies common customer issues relating to managing nodes in ElastiCache, and provides guidance on how to avoid these issues.

- [Viewing ElastiCache Node Status](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Nodes.viewing.html): View your node status.
- [Valkey or Redis OSS nodes and shards](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.NodeGroups.html): A shard (in the API and CLI, a node group) is a hierarchical arrangement of nodes, each wrapped in a cluster.
- [Connecting to nodes](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/nodes-connecting.html)
- [Supported node types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html): ElastiCache supports the following node types.
- [Rebooting nodes](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/nodes.rebooting.html): Some changes require that a Valkey, Memcached, or Redis OSS cluster reboot for the changes to be applied.
- [Replacing nodes (Valkey and Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.NodeReplacement.html): Amazon ElastiCache frequently upgrades its fleet with patches and upgrades being applied to instances seamlessly.
- [Replacing nodes (Memcached)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.NodeReplacement-mc.html): Amazon ElastiCache for Memcached frequently upgrades its fleet with patches and upgrades being applied to instances seamlessly.
- [Reserved nodes](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.Reserved.html): How to reserve ElastiCache nodes to help reduce costs.
- [Migrating previous generation nodes](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.NodeMigration.html): Previous generation nodes are node types that are being phased out.

### [Managing clusters in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.html)

Define and perform cluster management operations in ElastiCache.

- [Choosing a network type in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/network-type.html): Choose a network type in ElastiCache.

### [Auto Discovery (Memcached)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoDiscovery.html)

Identify all of the nodes in a Memcached cluster automatically, and initiate and maintain connections to all of these nodes using Auto Discovery.

- [Benefits of Auto Discovery with Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoDiscovery.Benefits.html): Benefits of using automatic discovery with your Amazon ElastiCache for Memcached clusters.
- [How Auto Discovery Works](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoDiscovery.HowAutoDiscoveryWorks.html): Describes the architecture of how client application manage cache node connections and interact with cache data items with Auto Discovery.

### [Using Auto Discovery](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoDiscovery.Using.html)

To begin using Auto Discovery with ElastiCache for Memcached, follow these steps:

- [Using the ElastiCache Cluster Client for Java](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoDiscovery.Using.ModifyApp.Java.html): The program below demonstrates how to use the ElastiCache Cluster Client to connect to a cluster configuration endpoint and add a data item to the cache.
- [Using the ElastiCache Cluster Client for PHP](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoDiscovery.Using.ModifyApp.PHP.html): The program below demonstrates how to use the ElastiCache Cluster Client to connect to a cluster configuration endpoint and add a data item to the cache.
- [Using the ElastiCache Cluster Client for .NET](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoDiscovery.Using.ModifyApp.DotNET.html)
- [Connecting to Memcached Cache Nodes Manually](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoDiscovery.Manual.html): Connect manually to each of the cache nodes which is the default behavior for Memcached clients.
- [Adding Auto Discovery to your Memcached client library](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoDiscovery.AddingToYourClientLibrary.html): Configure your client library to add Auto Discovery in each Memcached cluster node.

### [Auto discovery clients](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clients.html)

How to use ElastiCache clients with auto discovery.

### [Installing & compiling clients](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Appendix.InstallingClients.html)

Install, update, and remove components for the ElastiCache Cluster Client.

- [Installing the .NET cluster client](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Appendix.DotNETAutoDiscoverySetup.html): How to set up and install the ElastiCache cluster client for .NET.

### [Installing the PHP cluster client](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Appendix.PHPAutoDiscoverySetup.html)

Install, update, and remove the PHP components for the ElastiCache Cluster Client.

- [Downloading the installation package](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Appendix.PHPAutoDiscoverySetup.Downloading.html): To ensure that you use the correct version of the ElastiCache Cluster Client for PHP, you will need to know what version of PHP is installed on your Amazon EC2 instance.
- [Installation steps for new users](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Appendix.PHPAutoDiscoverySetup.Installing.html)
- [Removing the PHP cluster client](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Appendix.PHPAutoDiscoverySetup.Removing.html)
- [Compiling the source code for the PHP cluster client](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Appendix.PHPAutoDiscoveryCompile.html): How to compile the source code for the PHP cluster client.

### [Configuring clients](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ClientConfig.html)

Configure your ElastiCache cluster clients depending on whether you used the Memcached or Redis cache engine when you created the cluster.

- [Restricted commands](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ClientConfig.RestrictedCommands.html): To deliver a managed service experience, ElastiCache restricts access to certain cache engine-specific commands that require advanced privileges.
- [Finding node endpoints and port numbers](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ClientConfig.FindingEndpointsAndPorts.html): To connect to a cache node, your application needs to know the endpoint and port number for that node.
- [Connecting for using auto discovery](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ClientConfig.AutoDiscovery.html): If your applications use Auto Discovery, you only need to know the configuration endpoint for the cluster, rather than the individual endpoints for each cache node.
- [Connecting to nodes in a Valkey or Redis OSS cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ClientConfig.ReplicationGroup.html)
- [DNS names and underlying IP](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ClientConfig.DNS.html): Clients maintain a server list containing the addresses and ports of the servers holding the cache data.
- [Data tiering in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html): Using data tiering and replication groups with ElastiCache.

### [Preparing a cluster in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.Prepare.html)

Following, you can find instructions on creating a cluster using the ElastiCache console, the AWS CLI, or the ElastiCache API.

- [Determining your ElastiCache cluster requirements](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/cluster-create-determine-requirements.html): Before creating a cluster, determine your requirements for the cluster: memory, engine, scaling, automatic failover, access, and AWS Region.
- [Choosing your node size](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SelectSize.html): Considerations for selecting your node size, including impact on costs, performance, and fault tolerance.
- [Creating a cluster for Valkey or Redis OSS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.Create.html): The following examples show how to create a Valkey or Redis OSS cluster using the AWS Management Console, AWS CLI and ElastiCache API.
- [Creating a cluster for Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.Create-mc.html): The following examples show how to create a cluster using the AWS Management Console, AWS CLI and ElastiCache API.
- [Viewing an ElastiCache cluster's details](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.ViewDetails.html): You can view detail information about one or more clusters using the ElastiCache console, AWS CLI, or ElastiCache API.
- [Modifying an ElastiCache cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.Modify.html): In addition to adding or removing nodes from an ElastiCache cluster, there can be times where you need to make other changes such as adding a security group, changing the maintenance window or a parameter group.
- [Adding nodes to an ElastiCache cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.AddNode.html): Adding nodes to a Memcached cluster increases the number of your cluster's partitions.
- [Removing nodes from an ElastiCache cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.DeleteNode.html): You can delete a node from a Valkey, Memcached, or Redis OSS cluster using the AWS Management Console, the AWS CLI, or the ElastiCache API.
- [Canceling pending add or delete node operations in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.CancelPending.html): If you elected to not apply an ElastiCache cluster change immediately, the operation has pending status until it is performed at your next maintenance window.
- [Deleting a cluster in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.Delete.html): As long as an ElastiCache cluster is in the available state, you are being charged for it, whether or not you are actively using it.
- [Accessing your ElastiCache cluster or replication group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/accessing-elasticache.html): Access Amazon ElastiCache instances.
- [Finding connection endpoints in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Endpoints.html): Discusses connection endpoints in ElastiCache, how to find them and how to use them.
- [Shards in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Shards.html): How to use shards with ElastiCache
- [Comparing node-based Valkey, Memcached, and Redis OSS clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html): Select the better engine for your application's node-based clusterâValkey, Memcached, or Redis OSS.

### [Online Migration for Valkey or Redis OSS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/OnlineMigration.html)

Use Online migration to migrate your data from self-hosted Valkey or Redis OSS to Amazon ElastiCache.

- [Preparing your source and target for migration](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Migration-Prepare.html): With these steps you can prepare to migrate your data from a self-hosted Valkey or Redis source on EC2 to ElastiCache, or from a Redis OSS cluster to an ElastiCache Valkey cluster.
- [Testing the data migration](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Migration-Test.html): After all prerequisites are complete, you can validate migration setup using the AWS Management Console, ElastiCache API, or AWS CLI.
- [Starting migration](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Migration-Initiate.html): After all prerequisites are complete, you can begin data migration using the AWS Management Console, ElastiCache API, or AWS CLI.
- [Verifying the data migration progress](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Migration-Verify.html): After the data migration has begun, you can do the following to track its progress:
- [Completing the data migration](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Migration-Complete.html): When you are ready to cut over to the ElastiCache cluster, use the complete-migration CLI command with the following parameters:
- [Performing online data migration using the Console](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Migration-Console.html): You can use the AWS Management Console to migrate your data from your cluster to your Valkey or Redis OSS cluster.

### [Choosing regions and availability zones for ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/RegionsAndAZs.html)

Provide additional scalability and reliability to your clusters by designating the regions and Availability Zones using the corresponding endpoint.

- [Using Local zones with ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Local_zones.html): Use Local Zones with ElastiCache.
- [Using Outposts with ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ElastiCache-Outposts.html): How to use AWS Outposts with ElastiCache.


## [Working with ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WorkingWithElastiCache.html)

### [Snapshot and restore](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups.html)

Create automatic or manual backups of your Valkey cache, Redis OSS cache, or Serverless Memcached cache for backup and restore purposes.

- [Scheduling automatic backups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-automatic.html): You can enable automatic backups for any Valkey or Redis OSS serverless cache or node-based cluster.
- [Taking manual backups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-manual.html): In addition to automatic backups, you can create a manual backup at any time.
- [Creating a final backup](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-final.html): You can create a final backup using the ElastiCache console, the AWS CLI, or the ElastiCache API.
- [Describing backups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-describing.html): The following procedures show you how to display a list of your backups.
- [Copying backups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-copying.html): You can create a copy of any backup, whether it was created automatically or manually.
- [Exporting a backup](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html): Amazon ElastiCache supports exporting your ElastiCache for Redis OSS backup to an Amazon Simple Storage Service (Amazon S3) bucket, which gives you access to it from outside ElastiCache.
- [Restoring from a backup](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-restoring.html): You can restore an existing backup from Valkey into a new Valkey cache or node-based cluster, and restore an existing Redis OSS backup into a new Redis OSS cache or node-based cluster.
- [Deleting a backup](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-deleting.html): An automatic backup is automatically deleted when its retention limit expires.
- [Tagging backups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-tagging.html): You can assign your own metadata to each backup in the form of tags.
- [Tutorial: Seeding a node-based cluster with a backup](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-seeding-redis.html): When you create a new Valkey or Redis OSS node-based cluster, you can seed it with data from a Valkey or Redis OSS .rdb backup file.

### [Engine versions and upgrading in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/engine-versions.html)

This section covers the supported Valkey, Memcached, and Redis OSS engines and how to upgrade.

- [Upgrading engine versions](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VersionManagement.HowTo.html): Valkey and Redis OSS

### [Extended Support](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/extended-support.html)

Learn about ElastiCache Extended Support and how to continue to use engine versions past the Aurora end of standard support dates.

- [Extended Support charges](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/extended-support-charges.html): Learn about charges associated with ElastiCache Extended Support.
- [Versions with Extended Support](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/extended-support-versions.html): Learn which engine versions support ElastiCache Extended Support.
- [Responsibilities with Extended Support](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/extended-support-responsibilities.html): Learn about customer responsibilities with ElastiCache Extended Support.
- [Version Management for ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VersionManagement.html): Manage if and when the ElastiCache Serverless cache is upgraded and perform version upgrades on your own terms and timelines.
- [Major engine version behavior and compatibility differences with Valkey](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VersionManagementConsiderations-valkey.html): Options to consider if and when the Valkey cache engine software is upgraded and perform version upgrades on your own terms and timelines.
- [Major engine version behavior and compatibility differences with Redis OSS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VersionManagementConsiderations.html): Options to consider if and when the Redis OSS cache engine software is upgraded and perform version upgrades on your own terms and timelines.
- [Upgrade considerations when working with node-based clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VersionManagement-upgrade-considerations.html): Upgrade considerations

### [Best practices and caching strategies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.html)

Identifies common customer issues and provides guidance on how to avoid these issues.

- [Overall best practices](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WorkingWithRedis.html): Below you can find information about best practices for using the Valkey, Memcached, and Redis OSS interfaces within ElastiCache.
- [Best Practices for using Read Replicas](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ReadReplicas.html): How to use read replicas with Amazon ElastiCache serverless caches and node-based clusters to significantly improve performance.
- [Supported and restricted Valkey, Memcached, and Redis OSS commands](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SupportedCommands.html)
- [Valkey and Redis OSS configuration and limits](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/RedisConfiguration.html): The Valkey and Redis OSS engines each provides a number of configuration parameters, some of which are modifiable in ElastiCache for Redis OSS and some of which are not modifiable to provide stable performance and reliability.
- [IPv6 client examples for Valkey, Memcached, and Redis OSS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/network-type-best-practices.html): IPv6 Client Examples

### [Best practices for clients (Valkey and Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients.redis.html)

Learn best practices for common scenarios and follow along with code examples of some of the most popular open source Valkey and Redis OSS client libraries (redis-py, PHPRedis, and Lettuce), as well as best practices for interacting with ElastiCache resources with commonly used open-source Memcached client libraries.

- [Large number of connections (Valkey and Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients.Redis.Connections.html): Serverless caches and individual ElastiCache for Redis OSS nodes support up to 65,000 concurrent client connections.
- [Cluster client discovery and exponential backoff (Valkey and Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients.Redis.Discovery.html): When connecting to an ElastiCache Valkey or Redis OSS cluster in cluster mode enabled, the corresponding client library must be cluster aware.
- [Configure a client-side timeout (Valkey and Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients.Redis.ClientTimeout.html): Configuring the client-side timeout
- [Configure a server-side idle timeout (Valkey and Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients.Redis.ServerTimeout.html): We have observed cases when a customer's application has a high number of idle clients connected, but isn't actively sending commands.
- [Lua scripts](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients.Redis.LuaScripts.html): Valkey and Redis OSS supports more than 200 commands, including those to run Lua scripts.
- [Storing large composite items (Valkey and Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients.Redis.LargeItems.html): In some scenarios, an application may store large composite items in Valkey or Redis OSS (such as a multi-GB hash dataset).

### [Lettuce client configuration (Valkey and Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients-lettuce.html)

This section describes the recommended Java and Lettuce configuration options, and how they apply to ElastiCache clusters.

- [Example: Lettuce config for cluster mode, TLS enabled](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients-lettuce-cme.html)
- [Example: Lettuce config for cluster mode disabled, TLS enabled](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients-lettuce-cmd.html)

### [Best practices for clients (Memcached)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients.memcached.html)

Learn best practices for common scenarios with ElastiCache for Memcached clusters.

- [Configuring your ElastiCache client for efficient load balancing (Memcached)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.LoadBalancing.html)
- [Validated clients with Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/network-type-validated-clients-memcached.html): Validated clients
- [Configuring a preferred protocol for dual stack clusters (Memcached)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/network-type-configuring-dual-stack-memcached.html): Configuring a preferred protocol for dual stack clusters
- [Managing reserved memory for Valkey and Redis OSS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/redis-memory-management.html): Manage reserved memory for Valkey and Redis OSS

### [Best practices when working with Valkey and Redis OSS node-based clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.SelfDesigned.html)

Multi-AZ use, having sufficient memory, cluster resizing and minimizing downtime are all useful concepts to keep in mind when working with node-based clusters in Valkey or Redis OSS.

- [Minimizing downtime with Multi-AZ](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/multi-az.html): There are a number of instances where ElastiCache Valkey or Redis OSS may need to replace a primary node; these include certain types of planned maintenance and the unlikely event of a primary node or Availability Zone failure.
- [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.BGSAVE.html)
- [Online cluster resizing](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/best-practices-online-resharding.html): Resharding involves adding and removing shards or nodes to your cluster and redistributing key spaces.
- [Minimizing downtime during maintenance](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.MinimizeDowntime.html): Cluster mode configuration has the best availability during managed or unmanaged operations.
- [Caching strategies for Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html): Strategies for populating and maintaining your cache.

### [Managing your node-based cluster in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/manage-self-designed-cluster.html)

Provides guidance for managing your node-based cluster in ElastiCache

### [Auto Scaling Valkey and Redis OSS clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling.html)

How to autoscale your clusterâout or in, or up or down.

- [Auto Scaling policies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Policies.html): Auto Scaling policies overview

### [Using Auto Scaling with shards](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Using-Shards.html)

Using Auto Scaling

- [Target tracking scaling policies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Scaling-Policies-Target.html): Target tracking scaling policies
- [Adding a scaling policy](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Scaling-Adding-Policy-Shards.html): Adding a scaling policy
- [Registering a Scalable Target](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Scaling-Registering-Policy-CLI.html): Registering Scalable Target
- [Defining a scaling policy](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Scaling-Defining-Policy-API.html): Defining a scaling policy
- [Disabling scale-in activity](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Scaling-Disabling-Scale-in.html): Disabling scale-in activity
- [Applying a scaling policy](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Scaling-Applying-a-Scaling-Policy.html): Applying a scaling policy to an ElastiCache cluster using the AWS CLI
- [Editing a scaling policy](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Scaling-Editing-a-Scaling-Policy.html): Editing a scaling policy
- [Deleting a scaling policy](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Scaling-Deleting-a-Scaling-Policy.html): Deleting a scaling policy
- [Use CloudFormation for Auto Scaling policies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-with-Cloudformation-Shards.html): Use CloudFormation for Auto Scaling policies
- [Scheduled scaling](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-with-Scheduled-Scaling-Shards.html): Scheduled scaling

### [Using Auto Scaling with replicas](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Using-Replicas.html)

Using Auto Scaling with replicas

- [Target tracking scaling policies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Scaling-Policies-Replicas-Replicas.html): Target tracking scaling policies
- [Adding a scaling policy](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Adding-Policy-Replicas.html): Adding and registering scaling policy
- [Registering a Scalable Target](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Register-Policy.html): registering scaling policy

### [Defining a scaling policy](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Defining-Policy.html)

Defining a scaling policy

- [Editing a scaling policy](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Editing-Policy.html): Editing a scaling policy
- [Deleting a scaling policy](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-Deleting-Policy.html): Deleting a scaling policy
- [Use CloudFormation for Auto Scaling policies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-with-Cloudformation.html): Use CloudFormation for Auto Scaling policies
- [Scheduled scaling](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling-with-Scheduled-Scaling-Replicas.html): Scheduled scaling
- [Modifying cluster mode](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/modify-cluster-mode.html): Provides guidance for modifying cluster mode

### [Replication across AWS Regions using global datastores](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Redis-Global-Datastore.html)

Replicate data across AWS Regions using the Global Datastore feature in Amazon ElastiCache.

- [Prerequisites and limitations](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Redis-Global-Datastores-Getting-Started.html): Before getting started with global datastores, be aware of the following:
- [Using global datastores (console)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Redis-Global-Datastores-Console.html): To create a global datastore using the console, follow this two-step process:
- [Using global datastores (CLI)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Redis-Global-Datastores-CLI.html): You can use the AWS Command Line Interface (AWS CLI) to control multiple AWS services from the command line and automate them through scripts.

### [High availability using replication groups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.html)

Create a replication group to enhance scalability and guard against data loss if your cluster is running Valkey or Redis OSS.

- [Understanding Valkey and Redis OSS replication](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.Redis.Groups.html)
- [Replication: Valkey and Redis OSS Cluster Mode Disabled vs. Enabled](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.Redis-RedisCluster.html): Beginning with Valkey 7.2 and Redis OSS version 3.2, you have the ability to create one of two distinct types of clusters (API/CLI: replication groups).
- [Minimizing downtime with Multi-AZ](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html): Minimize downtime in ElastiCache by using Multi-AZ with Valkey and Redis OSS.
- [How synchronization and backup are implemented](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.Redis.Versions.html): All supported versions of Valkey and Redis OSS support backup and synchronization between the primary and replica nodes.

### [Creating a replication group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.CreatingRepGroup.html)

You have the following options for creating a cluster with replica nodes.

- [Creating a replication group using an existing cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.CreatingReplGroup.ExistingCluster.html): The following procedure adds a replication group to your Valkey or Redis OSS (cluster mode disabled) single-node cluster, which is necessary in order to upgrade your cluster to the latest version of Valkey.

### [Creating a Valkey or Redis OSS replication group from scratch](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.CreatingReplGroup.NoExistingCluster.html)

Following, you can find how to create a Valkey or Redis OSS replication group without using an existing Valkey or Redis OSS cluster as the primary.

- [Creating a Valkey or Redis OSS (Cluster Mode Disabled) replication group from scratch](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.CreatingReplGroup.NoExistingCluster.Classic.html): You can create a Valkey or Redis OSS (cluster mode disabled) replication group from scratch using the ElastiCache console, the AWS CLI, or the ElastiCache API.
- [Creating a replication group in Valkey or Redis OSS (Cluster Mode Enabled) from scratch](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.CreatingReplGroup.NoExistingCluster.Cluster.html): You can create a Valkey or Redis OSS (cluster mode enabled) cluster (API/CLI: replication group) using the ElastiCache console, the AWS CLI, or the ElastiCache API.

### [Viewing a replication group's details](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.ViewDetails.html)

There are times you may want to view the details of a replication group.

- [Viewing a Valkey or Redis OSS (Cluster Mode Disabled) with replicas](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.ViewDetails.Redis.html): You can view the details of a Valkey or Redis OSS (cluster mode disabled) cluster with replicas (API/CLI: replication group) using the ElastiCache console, the AWS CLI for ElastiCache, or the ElastiCache API.
- [Viewing a replication group: Valkey or Redis OSS (Cluster Mode Enabled)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.ViewDetails.RedisCluster.html)
- [Viewing a replication group's details (AWS CLI)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.ViewDetails.CLI.html): You can view the details for a replication group using the AWS CLI describe-replication-groups command.
- [Viewing a replication group's details (ElastiCache API)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.ViewDetails.API.html): You can view the details for a replication using the AWS CLI DescribeReplicationGroups operation.
- [Finding replication group endpoints](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.Endpoints.html): An application can connect to any node in a replication group, provided that it has the DNS endpoint and port number for that node.
- [Modifying a replication group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.Modify.html)
- [Deleting a replication group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.DeletingRepGroup.html): If you no longer need one of your clusters with replicas (called replication groups in the API/CLI), you can delete it.

### [Changing the number of replicas](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/increase-decrease-replica-count.html)

You can dynamically increase or decrease the number of read replicas in your Valkey or Redis OSS replication group using the AWS Management Console, the AWS CLI, or the ElastiCache API.

- [Increasing the Number of Replicas](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/increase-replica-count.html): You can increase the number of replicas in a Valkey or Redis OSS (cluster mode enabled) shard or Valkey or Redis OSS (cluster mode disabled) replication group up to a maximum of five.
- [Decreasing the Number of Replicas](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/decrease-replica-count.html): You can decrease the number of replicas in a shard for Valkey or Redis OSS (cluster mode enabled), or in a replication group for Valkey or Redis OSS (cluster mode disabled):
- [Adding a read replica for Valkey or Redis OSS (Cluster Mode Disabled)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.AddReadReplica.html): Information in the following topic applies to Valkey or Redis OSS (cluster mode disabled) replication groups only.
- [Deleting a read replica for Valkey or Redis OSS (Cluster Mode Disabled)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.RemoveReadReplica.html): Information in the following topic applies to Valkey or Redis OSS (cluster mode disabled) replication groups only.
- [Promoting a read replica](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.PromoteReplica.html): Information in the following topic applies to only Valkey or Redis OSS (cluster mode disabled) replication groups.
- [Managing ElastiCache cluster maintenance](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/maintenance-window.html): Describes Amazon ElastiCache cluster maintenance windows and lists global default windows.

### [Configuring engine parameters using ElastiCache parameter groups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.html)

Identifies common customer issues with ElastiCache parameter groups, and provides guidance on how to avoid these issues.

- [Parameter management in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.Management.html): ElastiCache parameters are grouped together into named parameter groups for easier parameter management.
- [Parameter group tiers in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.Tiers.html): Amazon ElastiCache has three tiers of cache parameter groups as shown following.
- [Creating an ElastiCache parameter group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.Creating.html): You need to create a new parameter group if there is one or more parameter values that you want changed from the default values.
- [Listing ElastiCache parameter groups by name](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.ListingGroups.html): You can list the parameter groups using the ElastiCache console, the AWS CLI, or the ElastiCache API.
- [Listing an ElastiCache parameter group's values](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.ListingValues.html): You can list the parameters and their values for a parameter group using the ElastiCache console, the AWS CLI, or the ElastiCache API.
- [Modifying an ElastiCache parameter group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.Modifying.html)
- [Deleting an ElastiCache parameter group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.Deleting.html): You can delete a custom parameter group using the ElastiCache console, the AWS CLI, or the ElastiCache API.
- [Engine specific parameters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.Engine.html): Valkey and Redis OSS
- [Connecting an EC2 instance and an ElastiCache cache automatically](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/compute-connection.html): Connect an EC2 instance and ElastiCache.

### [Scaling ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Scaling.html)

How to scale your cache âout or in, or up or down.

### [Scaling node-based clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Scaling-self-designed.html)

How to scale your ElastiCache node-based clusters

- [On-demand scaling for Memcached clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Scaling-self-designed.mem-heading.html): How to scale your ElastiCache for Memcached clusters on demand
- [Manual scaling for Memcached clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Scaling.Memcached.manually.html): Guidance on manually scaling your Memcached cluster both vertically and horizontally.
- [Scaling for Valkey or Redis OSS (Cluster Mode Disabled) clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/scaling-redis-classic.html): Valkey or Redis OSS (cluster mode disabled) clusters can be a single-node cluster with 0 shards or multi-node clusters with 1 shard.
- [Scaling replica nodes for Valkey or Redis OSS (Cluster Mode Disabled)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Scaling.RedisReplGrps.html): A Valkey or Redis OSS cluster with replica nodes (called replication group in the API/CLI) provides high availability via replication that has Multi-AZ with automatic failover enabled.

### [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/scaling-redis-cluster-mode-enabled.html)

As demand on your clusters changes, you might decide to improve performance or reduce costs by changing the number of shards in your Valkey or Redis OSS (cluster mode enabled) cluster.

- [Online vertical scaling by modifying node type](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/redis-cluster-vertical-scaling.html): By using online vertical scaling with Valkey version 7.2 or newer, or Redis OSS version 3.2.10 or newer, you can scale your Valkey or Redis OSS clusters dynamically with minimal downtime.
- [Getting started with Bloom filters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BloomFilters.html): How to use Bloom filters with ElastiCache
- [Getting started with Watch in Serverless](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ServerlessWatch.html): How to use Watch in Serverless with ElastiCache

### [Getting started with Vector Search](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/vector-search.html)

Learn how to use vector search with Amazon ElastiCache for Valkey to store, search, and update high-dimensional vector embeddings.

- [Vector Search Overview](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/vector-search-overview.html): Amazon ElastiCache for Valkey supports vector search, enabling you to store, search, and update billions of high-dimensional vector embeddings in-memory with latencies as low as microseconds with recall up to 99%.
- [Vector search features and limits](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/vector-search-features-limits.html)
- [Choosing the appropriate configuration](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/choosing-configuration.html): Within the console experience, ElastiCache offers an easy way to choose the right instance type based on the memory and cpu requirements of your vector workload.

### [Vector Search Commands](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/vector-search-commands.html)

Following are a list of supported commands for vector search.

- [FT.CREATE](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/vector-search-commands-ft.create.html): The FT.CREATE command creates an empty index and initiates the backfill process.
- [FT.SEARCH](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/vector-search-commands-ft.search.html): Performs a search of the specified index.
- [FT.DROPINDEX](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/vector-search-commands-ft.dropindex.html): Syntax
- [FT.INFO](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/vector-search-commands-ft.info.html): Syntax
- [FT._LIST](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/vector-search-commands-ft.list.html): List all indexes.

### [Getting started with JSON for Valkey and Redis OSS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-gs.html)

Getting started with JSON

- [JSON data type overview](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-document-overview.html): JSON data type overview

### [JSON commands](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-list-commands.html)

Supported commands

- [JSON.ARRAPPEND](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-arrappend.html): JSON.ARRAPPEND
- [JSON.ARRINDEX](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-arrindex.html): JSON.ARRINDEX
- [JSON.ARRINSERT](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-arrinsert.html): JSON.ARRINSERT
- [JSON.ARRLEN](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-arrlen.html): JSON.ARRLEN
- [JSON.ARRPOP](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-arrpop.html): JSON.ARRPOP
- [JSON.ARRTRIM](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-arrtrim.html): JSON.ARRTRIM
- [JSON.CLEAR](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-clear.html): JSON.CLEAR
- [JSON.DEBUG](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-debug.html): JSON.DEBUG
- [JSON.DEL](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-del.html): JSON.DEL
- [JSON.FORGET](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-forget.html): JSON.FORGET
- [JSON.GET](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-get.html): JSON.GET
- [JSON.MGET](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-mget.html): JSON.MGET
- [JSON.MSET](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-mset.html): JSON.MSET
- [JSON.NUMINCRBY](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-numincrby.html): JSON.NUMINCRBY
- [JSON.NUMMULTBY](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-nummultby.html): JSON.NUMMULTBY
- [JSON.OBJLEN](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-objlen.html): JSON.OBJLEN
- [JSON.OBJKEYS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-objkeys.html): JSON.OBJKEYS
- [JSON.RESP](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-resp.html): JSON.RESP
- [JSON.SET](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-set.html): JSON.SET
- [JSON.STRAPPEND](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-strappend.html): JSON.STRAPPEND
- [JSON.STRLEN](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-strlen.html): JSON.STRLEN
- [JSON.TOGGLE](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-toggle.html): JSON.TOGGLE
- [JSON.TYPE](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/json-type.html): JSON.TYPE

### [Tagging your ElastiCache resources](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Tagging-Resources.html)

Organize and manage your ElastiCache resources using tags.

- [Monitoring costs with tags](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Tagging.html): Monitoring costs with cost allocation tags.
- [Managing tags using the AWS CLI](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Tagging.Managing.CLI.html): You can use the AWS CLI to add, modify, or remove cost allocation tags.
- [Managing tags using the ElastiCache API](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Tagging.Managing.API.html): You can use the ElastiCache API to add, modify, or remove cost allocation tags.

### [Amazon ElastiCache Well-Architected Lens](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WellArchitechtedLens.html)

Using the Amazon ElastiCache Well-Architected Lens

- [Operational Excellence Pillar](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/OperationalExcellencePillar.html): Amazon ElastiCache Well-Architected Lens Operational Excellence Pillar
- [Security Pillar](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SecurityPillar.html): Amazon ElastiCache Well-Architected Lens Security Pillar
- [Reliability Pillar](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ReliabilityPillar.html): Amazon ElastiCache Well-Architected Lens Reliability Pillar
- [Performance Efficiency Pillar](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/PerformanceEfficiencyPillar.html): Amazon ElastiCache Well-Architected Lens Performance Efficiency Pillar
- [Cost Optimization Pillar](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CostOptimizationPillar.html): Amazon ElastiCache Well-Architected Lens Cost Optimization Pillar

### [Troubleshooting in ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/wwe-troubleshooting.html)

Common troubleshooting steps and best practices for ElastiCache serverless cache or node-based cluster.

- [Persistent connection issues](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/TroubleshootingConnections.html): Additional troubleshooting steps for persistent connection issues


## [Security](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/security.html)

### [Data protection](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon ElastiCache.

### [Data security in Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/encryption.html)

Encrypt data with Amazon ElastiCache.

### [In-transit encryption (TLS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/in-transit-encryption.html)

Encrypt data in transit with Amazon ElastiCache.

- [Enabling in-transit encryption](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/in-transit-encryption-enable.html): Implement in-transit encryption using the Amazon ElastiCache console, the AWS CLI, and the ElastiCache API.
- [Connect to TLS-enabled Valkey or Redis OSS with valkey-cli](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/connect-tls.html): Shows how to connect to a TLS enabled Valkey or Redis OSS cache.
- [Enabling in-transit encryption using Python](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/in-transit-encryption-enable-python.html): Implement in-transit encryption for a Redis OSS replication group using Python.
- [Best practices when enabling in-transit encryption](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/enable-python-best-practices.html)
- [At-Rest Encryption](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/at-rest-encryption.html): Encrypt data on disk during sync and backup operations with Amazon ElastiCache.

### [Authentication and Authorization](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth-redis.html)

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources.

### [Role-Based Access Control (RBAC)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.RBAC.html)

Use Role-Based Access Control (RBAC) Valkey or Redis OSS to protect access to your data in ElastiCache.

- [Automatically rotating passwords for users](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/User-Secrets-Manager.html): Use Secrets Manager to rotate passwords for your user.
- [Authenticating with IAM](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth-iam.html): How to authenticate with IAM.
- [Authenticating with AUTH](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html): Use the Valkey and Redis OSS AUTH command to protect access to your data in Amazon ElastiCache.
- [Disabling access control on an ElastiCache Valkey or Redis OSS cache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/in-transit-encryption-disable.html): Follow the instructions below to disable access control on a Valkey or Redis OSS TLS-enabled cache.

### [Internetwork traffic privacy](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Security.html)

Identifies methods for controlling access to your ElastiCache resources.

### [Amazon VPCs and ElastiCache security](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VPCs.html)

Because data security is important, ElastiCache provides means for you to control who has access to your data.

- [Understanding ElastiCache and Amazon VPCs](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VPCs.EC.html): Manage software upgrades, patching, failure detection and recovery with ElastiCache whether your clusters are deployed inside or outside an Amazon VPC.
- [Amazon VPC Access Patterns](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-vpc-accessing.html): Access patterns for accessing an ElastiCache cache in a VPC.
- [Creating a Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VPCs.CreatingVPC.html): Create a virtual private cloud with a private subnet for each Availability Zone.
- [Connecting to a cache running in an Amazon VPC](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VPCs.Connecting.html): Launch an Amazon EC2 instance in your Amazon VPC and connect to a cache that is running in the Amazon VPC.
- [ElastiCache API and interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-privatelink.html): You can establish a private connection between your VPC and Amazon ElastiCache API endpoints by creating an interface VPC endpoint.

### [Subnets and subnet groups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.html)

Identifies methods for controlling access to your ElastiCache resources.

- [Creating a subnet group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.Creating.html): A cache subnet group is a collection of subnets that you may want to designate for your caches in a VPC.
- [Assigning a subnet group to a cache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.Assigning.html): After you have created a subnet group, you can launch a cache in an Amazon VPC.
- [Modifying a subnet group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.Modifying.html): You can modify a subnet group's description, or modify the list of subnet IDs associated with the subnet group.
- [Deleting a subnet group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.Deleting.html): If you decide that you no longer need your subnet group, you can delete it.

### [Identity and Access Management](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.html)

How to authenticate requests and manage access your ElastiCache resources.

- [How Amazon ElastiCache works with IAM](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to ElastiCache, learn what IAM features are available to use with ElastiCache.
- [Identity-based policy examples](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify ElastiCache resources.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with ElastiCache and IAM.

### [Overview of managing access](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.Overview.html)

Every AWS resource is owned by an AWS account, and permissions to create or access a resource are governed by permissions policies.

- [AWS managed policies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for ElastiCache and recent changes to those policies.
- [Using identity-based policies (IAM policies)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.IdentityBasedPolicies.html): This topic provides examples of identity-based policies in which an account administrator can attach permissions policies to IAM identities (that is, users, groups, and roles).
- [Resource-level permissions](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.ResourceLevelPermissions.html): You can restrict the scope of permissions by specifying resources in an IAM policy.
- [Using condition keys](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.ConditionKeys.html): You can specify conditions that determine how an IAM policy takes effect.
- [Using Service-Linked Roles](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/using-service-linked-roles.html): How to use service-linked roles to give Amazon ElastiCache access to resources in your AWS account.
- [ElastiCache API permissions reference](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.APIReference.html): When you set up access control and write permissions policies to attach to an IAM policy (either identity-based or resource-based), use the following table as a reference.
- [Compliance validation](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon ElastiCache features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/infrastructure-security.html): Learn how AWS ElastiCache isolates service traffic.
- [Service updates](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Self-Service-Updates.html): Use service updates to manage and control updates to your ElastiCache.
- [Addressed security vulnerabilities](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/cve.html): Common Vulnerabilities and Exposures (CVE) is a list of entries for publicly known cybersecurity vulnerabilities.


## [Logging and monitoring](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/MonitoringECMetrics.html)

- [Metrics and events for Valkey and Redis OSS serverless](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/serverless-metrics-events-redis.html): Metrics and events you can monitor when working with Valkey and Redis OSS serverless caches.
- [Metrics and events for node-based Valkey and Redis OSS clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/self-designed-metrics-events.valkey-and-redis.html): Configure Amazon ElastiCache to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your ElastiCache resources.
- [Metrics and events for Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/serverless-metrics-events.memcached.html): Metrics and events you can monitor when working with Memcached serverless and node-based clusters.
- [Logging Amazon ElastiCache API calls with AWS CloudTrail](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/logging-using-cloudtrail.html): Learn about logging Amazon ElastiCache with AWS CloudTrail.

### [Amazon SNS event monitoring](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ECEvents.html)

Describes ElastiCache events and how to view them with Amazon SNS.

- [Managing ElastiCache Amazon SNS notifications](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ECEvents.SNS.html): You can configure ElastiCache to send notifications for important cluster events using Amazon Simple Notification Service (Amazon SNS).
- [Viewing ElastiCache events](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ECEvents.Viewing.html): ElastiCache logs events that relate to your cluster instances, security groups, and parameter groups.
- [Event Notifications and Amazon SNS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ElastiCacheSNS.html): Lists the notifications of significant events that happen on a cluster with ElastiCache and Amazon SNS messages.

### [Log delivery](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Log_Delivery.html)

Logging and log delivery for your ElastiCache caches and clusters.

- [ElastiCache logging destinations](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Logging-destinations.html): Covers destination specs.
- [Specifying log delivery using the Console](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Console_Log.html): Covers log delivery using console
- [Specifying log delivery using the AWS CLI](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CLI_Log.html): Covers log delivery using CLI

### [Monitoring use](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.html)

Access metrics so you can monitor your clusters using Amazon CloudWatch with ElastiCache.

- [Host-Level Metrics](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.HostLevel.html): The AWS/ElastiCache namespace includes the following host-level metrics for individual cache nodes.
- [Metrics for Valkey and Redis OSS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.Redis.html): The Amazon ElastiCache namespace includes the following Valkey and Redis OSS metrics.
- [Metrics for Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.Memcached.html): The AWS/ElastiCache namespace includes the following Memcached metrics.
- [Which Metrics Should I Monitor?](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.WhichShouldIMonitor.html): Lists best practices for which CloudWatch metrics to use to monitor your ElastiCache performance.
- [Choosing Metric Statistics and Periods](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.ChoosingStatisticsAndPeriods.html): While CloudWatch will allow you to choose any statistic and period for each metric, not all combinations will be useful.
- [Monitoring CloudWatch Cluster and Node Metrics](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CloudWatchMetrics.html): Monitor your ElastiCache cluster and nodes with metrics using CloudWatch.


## [Reference](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-api-reference.html)

### [Using the ElastiCache API](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ProgrammingGuide.html)

Describes the basics of how to use the ElastiCache API.

- [Using the query API](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ProgrammingGuide.QueryAPI.html): Use the Query API to make requests that include common parameters to handle authentication and chosen actions.
- [Available libraries](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/using-libraries.html): >Build your ElastiCache applications with language-specific APIs and libraries provided by AWS.
- [Troubleshooting applications](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Troubleshooting.html): Troubleshoot issues to diagnose and resolve problems that you may encounter while interacting with the ElastiCache API.
- [Error messages](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ErrorMessages.html): Lists and describes ElastiCache error messages.
- [Notifications](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-notifications.html): Identifies common customer issues and provides guidance on how to avoid these issues.
