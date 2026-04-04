# Source: https://docs.aws.amazon.com/memorydb/latest/devguide/llms.txt

# Amazon MemoryDB Developer Guide

> Amazon MemoryDB is a fully managed, Valkey and Redis OSS-compatible, in-memory database that delivers ultra-fast performance and Multi-AZ durability for modern applications built using microservices architectures.

- [Getting started with MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/getting-started.html)
- [Quotas](https://docs.aws.amazon.com/memorydb/latest/devguide/quota-limits.html)
- [Document history](https://docs.aws.amazon.com/memorydb/latest/devguide/doc-history.html)

## [What is MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html)

- [Features of MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/servicename-feature-overview.html): Amazon MemoryDB is a durable, in-memory database service that delivers ultra-fast performance.
- [MemoryDB core components](https://docs.aws.amazon.com/memorydb/latest/devguide/components.html): MemoryDB data model: nodes, clusters, snapshots, parameter groups.
- [Related services](https://docs.aws.amazon.com/memorydb/latest/devguide/related-services-choose-between-memorydb-and-redis.html): ElastiCache
- [Choosing Regions and Availability Zones](https://docs.aws.amazon.com/memorydb/latest/devguide/regionsandazs.html): Provide additional scalability and reliability to your clusters by designating the regions and Availability Zones using the corresponding endpoint.
- [Accessing MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/nodes-connecting.html): Each MemoryDB cluster endpoint contains an address and a port.
- [MemoryDB security](https://docs.aws.amazon.com/memorydb/latest/devguide/memorydb-security.html): Security for MemoryDB is managed at three levels:


## [Managing nodes](https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.html)

- [MemoryDB nodes and shards](https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.nodegroups.html): A shard is a hierarchical arrangement of nodes, each wrapped in a cluster.
- [Supported node types](https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.supportedtypes.html): MemoryDB supports the following node types.

### [Reserved nodes](https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reservednodes.html)

Reserved nodes provide you with a significant discount compared to on-demand node pricing.

- [Overview of reserved nodes](https://docs.aws.amazon.com/memorydb/latest/devguide/reserved-nodes-overview.html): When you purchase a MemoryDB reserved node, you purchase a commitment to getting a discounted rate, on a specific node type, for the duration of the reserved node.
- [Offering types](https://docs.aws.amazon.com/memorydb/latest/devguide/reserved-nodes-offerings.html): Reserved nodes are available in three varieties â No Upfront, Partial Upfront, and All Upfront â that let you optimize your MemoryDB costs based on your expected usage.
- [Size flexible reserved nodes](https://docs.aws.amazon.com/memorydb/latest/devguide/reserved-nodes-size.html): When you purchase a reserved node, one thing that you specify is the node type, for example db.r6g.xlarge.
- [Upgrading nodes from Redis OSS to Valkey](https://docs.aws.amazon.com/memorydb/latest/devguide/reserved-nodes.html): With the launch of Valkey in MemoryDB, you can now apply your Redis OSS reserved node discount to the Valkey engine.
- [Deleting a reserved node](https://docs.aws.amazon.com/memorydb/latest/devguide/reserved-nodes-deleting.html): The terms for a reserved node involve a one-year or three-year commitment.
- [Working with reserved nodes](https://docs.aws.amazon.com/memorydb/latest/devguide/reserved-nodes-working-with.html): You can use the AWS Management Console, the AWS Command Line Interface, and MemoryDB API to work with reserved nodes.
- [Replacing nodes](https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.nodereplacement.html): MemoryDB frequently upgrades its fleet with patches and upgrades, usually seamlessly.


## [Managing clusters](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.html)

### [Data tiering](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html)

Data tiering

- [Best practices](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering-best-practices.html): Best practices
- [Data tiering limitations](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering-prerequisites.html): Limitations
- [Data tiering pricing](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering-pricing.html): Data tiering pricing
- [Data tiering monitoring](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering-monitoring.html): Monitoring
- [Using data tiering](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering-enabling.html): Using data tiering
- [Restoring data from a snapshot into clusters](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering-enabling-snapshots.html): Restoring data from a snapshot into clusters

### [Preparing a cluster](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.prepare.html)

Following, you can find instructions on creating a cluster using the MemoryDB console, the AWS CLI, or the MemoryDB API.

- [Determining your requirements](https://docs.aws.amazon.com/memorydb/latest/devguide/cluster-create-determine-requirements.html): Before creating a cluster, determine your requirements for the cluster: memory, engine, scaling, automatic failover, access, and AWS Region.
- [Creating a cluster](https://docs.aws.amazon.com/memorydb/latest/devguide/cluster.create.html): MemoryDB offers three ways to create a cluster.
- [Viewing a cluster's details](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.viewdetails.html): You can view detail information about one or more clusters using the MemoryDB console, AWS CLI, or MemoryDB API.
- [Modifying a cluster](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.modify.html): In addition to adding or removing nodes from a cluster, there can be times where you need to make other changes to an existing cluster, such as adding a security group, changing the maintenance window or a parameter group.
- [Adding / Removing nodes from a cluster](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.deletenode.html): You can add or remove nodes from a cluster using the AWS Management Console, the AWS CLI, or the MemoryDB API.
- [Accessing your cluster](https://docs.aws.amazon.com/memorydb/latest/devguide/accessing-memorydb.html): Access MemoryDB instances.
- [Finding connection endpoints](https://docs.aws.amazon.com/memorydb/latest/devguide/endpoints.html): Discusses connection endpoint in MemoryDB; how to find and use it.
- [Shards](https://docs.aws.amazon.com/memorydb/latest/devguide/shards.html): A shard is a collection of one to 6 nodes.


## [Managing your MemoryDB implementation](https://docs.aws.amazon.com/memorydb/latest/devguide/managing-memorydb.html)

- [Engine versions](https://docs.aws.amazon.com/memorydb/latest/devguide/engine-versions.html): Provides guidance in selecting an engine for your application

### [Getting started with JSON](https://docs.aws.amazon.com/memorydb/latest/devguide/json-gs.html)

Getting started with JSON

- [JSON Datatype overview](https://docs.aws.amazon.com/memorydb/latest/devguide/json-document-overview.html): Valkey and Redis OSS JSON Datatype overview

### [Supported commands](https://docs.aws.amazon.com/memorydb/latest/devguide/json-list-commands.html)

Supported commands

- [JSON.ARRAPPEND](https://docs.aws.amazon.com/memorydb/latest/devguide/json-arrappend.html): JSON.ARRAPPEND
- [JSON.ARRINDEX](https://docs.aws.amazon.com/memorydb/latest/devguide/json-arrindex.html): JSON.ARRINDEX
- [JSON.ARRINSERT](https://docs.aws.amazon.com/memorydb/latest/devguide/json-arrinsert.html): JSON.ARRINSERT
- [JSON.ARRLEN](https://docs.aws.amazon.com/memorydb/latest/devguide/json-arrlen.html): JSON.ARRLEN
- [JSON.ARRPOP](https://docs.aws.amazon.com/memorydb/latest/devguide/json-arrpop.html): JSON.ARRPOP
- [JSON.ARRTRIM](https://docs.aws.amazon.com/memorydb/latest/devguide/json-arrtrim.html): JSON.ARRTRIM
- [JSON.CLEAR](https://docs.aws.amazon.com/memorydb/latest/devguide/json-clear.html): JSON.CLEAR
- [JSON.DEBUG](https://docs.aws.amazon.com/memorydb/latest/devguide/json-debug.html): JSON.DEBUG
- [JSON.DEL](https://docs.aws.amazon.com/memorydb/latest/devguide/json-del.html): JSON.DEL
- [JSON.FORGET](https://docs.aws.amazon.com/memorydb/latest/devguide/json-forget.html): JSON.FORGET
- [JSON.GET](https://docs.aws.amazon.com/memorydb/latest/devguide/json-get.html): JSON.GET
- [JSON.MGET](https://docs.aws.amazon.com/memorydb/latest/devguide/json-mget.html): JSON.MGET
- [JSON.NUMINCRBY](https://docs.aws.amazon.com/memorydb/latest/devguide/json-numincrby.html): JSON.NUMINCRBY
- [JSON.NUMMULTBY](https://docs.aws.amazon.com/memorydb/latest/devguide/json-nummultby.html): JSON.NUMMULTBY
- [JSON.OBJLEN](https://docs.aws.amazon.com/memorydb/latest/devguide/json-objlen.html): JSON.OBJLEN
- [JSON.OBJKEYS](https://docs.aws.amazon.com/memorydb/latest/devguide/json-objkeys.html): JSON.OBJKEYS
- [JSON.RESP](https://docs.aws.amazon.com/memorydb/latest/devguide/json-resp.html): JSON.RESP
- [JSON.SET](https://docs.aws.amazon.com/memorydb/latest/devguide/json-set.html): JSON.SET
- [JSON.STRAPPEND](https://docs.aws.amazon.com/memorydb/latest/devguide/json-strappend.html): JSON.STRAPPEND
- [JSON.STRLEN](https://docs.aws.amazon.com/memorydb/latest/devguide/json-strlen.html): JSON.STRLEN
- [JSON.TOGGLE](https://docs.aws.amazon.com/memorydb/latest/devguide/json-toggle.html): JSON.TOGGLE
- [JSON.TYPE](https://docs.aws.amazon.com/memorydb/latest/devguide/json-type.html): JSON.TYPE

### [Tagging your MemoryDB resources](https://docs.aws.amazon.com/memorydb/latest/devguide/tagging-resources.html)

Organize and manage your MemoryDB resources using tags.

- [Monitoring costs with tags](https://docs.aws.amazon.com/memorydb/latest/devguide/tagging.html): Monitoring costs with cost allocation tags.
- [Managing tags using the AWS CLI](https://docs.aws.amazon.com/memorydb/latest/devguide/tagging.managing.cli.html): You can use the AWS CLI to add, modify, or remove cost allocation tags.
- [Managing tags using the MemoryDB API](https://docs.aws.amazon.com/memorydb/latest/devguide/tagging.managing.api.html): You can use the MemoryDB API to add, modify, or remove cost allocation tags.
- [Managing maintenance](https://docs.aws.amazon.com/memorydb/latest/devguide/maintenance-window.html): Describes MemoryDB cluster maintenance windows and lists global default windows.

### [Best practices](https://docs.aws.amazon.com/memorydb/latest/devguide/bestpractices.html)

recommended best practices

### [Resilience](https://docs.aws.amazon.com/memorydb/latest/devguide/disaster-recovery-resiliency.html)

Learn how AWS architecture supports data redundancy, and learn about specific MemoryDB features for data resiliency.

- [Mitigating Failures](https://docs.aws.amazon.com/memorydb/latest/devguide/faulttolerance.html): Discusses approaches to fault tolerance.
- [Best practices: Pub/Sub and Enhanced I/O Multiplexing](https://docs.aws.amazon.com/memorydb/latest/devguide/best-practices-pubsub.html): When using Valkey or Redis OSS version 7 or later, we recommend using sharded Pub/Sub.
- [Best practices: Online cluster resizing](https://docs.aws.amazon.com/memorydb/latest/devguide/best-practices-online-resharding.html): Resharding involves adding and removing shards or nodes to your cluster and redistributing key spaces.

### [Understanding MemoryDB replication](https://docs.aws.amazon.com/memorydb/latest/devguide/replication.html)

Understanding MemoryDB replication

- [Consistency](https://docs.aws.amazon.com/memorydb/latest/devguide/consistency.html): Consistency in MemoryDB.
- [Minimizing downtime with Multi-AZ](https://docs.aws.amazon.com/memorydb/latest/devguide/autofailover.html): Minimize downtime in MemoryDB by using Multi-AZ.
- [Changing the number of replicas](https://docs.aws.amazon.com/memorydb/latest/devguide/update-replica-count.html): You can dynamically increase or decrease the number of read replicas in your MemoryDB cluster using the AWS Management Console, the AWS CLI, or the MemoryDB API.

### [Snapshot and restore](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots.html)

Create automatic or manual snapshots of your MemoryDB cluster, for snapshot and restore purposes.

- [Constraints](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-constraints.html): Consider the following constraints when planning or making snapshots:
- [Costs](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-costs.html): Using MemoryDB, you can store one snapshot for each active MemoryDB cluster free of charge.
- [Scheduling automatic snapshots](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-automatic.html): For any MemoryDB cluster, you can enable automatic snapshots.
- [Making manual snapshots](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-manual.html): In addition to automatic snapshots, you can create a manual snapshot at any time.
- [Creating a final snapshot](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-final.html): You can create a final snapshot using the MemoryDB console, the AWS CLI, or the MemoryDB API.
- [Describing snapshots](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-describing.html): The following procedures show you how to display a list of your snapshots.
- [Copying a snapshot](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-copying.html): You can make a copy of any snapshot, whether it was created automatically or manually.
- [Exporting a snapshot](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-exporting.html): MemoryDB supports exporting your MemoryDB snapshot to an Amazon Simple Storage Service (Amazon S3) bucket, which gives you access to it from outside MemoryDB.
- [Restoring from a snapshot](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-restoring.html): You can restore the data from a MemoryDB or ElastiCache (Redis OSS) .rdb snapshot file to a new cluster at any time.
- [Seeding a cluster with a snapshot](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-seeding-redis.html): When you create a new MemoryDB cluster, you can seed it with data from a Valkey or Redis OSS .rdb snapshot file.
- [Tagging snapshots](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-tagging.html): You can assign your own metadata to each snapshot in the form of tags.
- [Deleting a snapshot](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-deleting.html): An automatic snapshot is automatically deleted when its retention limit expires.

### [Scaling](https://docs.aws.amazon.com/memorydb/latest/devguide/scaling.html)

How to scale your clusterâout or in, or up or down.

### [Scaling MemoryDB clusters](https://docs.aws.amazon.com/memorydb/latest/devguide/scaling-cluster.html)

As demand on your clusters changes, you might decide to improve performance or reduce costs by changing the number of shards in your MemoryDB cluster.

- [Offline resharding for MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/cluster-resharding-offline.html): The main advantage you get from offline shard reconfiguration is that you can do more than merely add or remove shards from your cluster.
- [Online resharding for MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/cluster-resharding-online.html): Learn about how to scale MemoryDB in or out with no cluster downtime.

### [Online vertical scaling by modifying node type](https://docs.aws.amazon.com/memorydb/latest/devguide/cluster-vertical-scaling.html)

By using online vertical scaling with MemoryDB, you can scale your cluster dynamically with minimal downtime.

- [Online scaling up](https://docs.aws.amazon.com/memorydb/latest/devguide/cluster-vertical-scaling-scaling-up.html)
- [Online scaling down](https://docs.aws.amazon.com/memorydb/latest/devguide/cluster-vertical-scaling-scaling-down.html)

### [Configuring engine parameters using parameter groups](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.html)

Identifies common customer issues and provides guidance on how to avoid these issues.

- [Parameter management](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.management.html): Parameters are grouped together into named parameter groups for easier parameter management.
- [Parameter group tiers](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.tiers.html): MemoryDB parameter group tiers
- [Creating a parameter group](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.creating.html): You need to create a new parameter group if there is one or more parameter values that you want changed from the default values.
- [Listing parameter groups by name](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.listingGroups.html): You can list the parameter groups using the MemoryDB console, the AWS CLI, or the MemoryDB API.
- [Listing a parameter group's values](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.listingValues.html): You can list the parameters and their values for a parameter group using the MemoryDB console, the AWS CLI, or the MemoryDB API.
- [Modifying a parameter group](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.modifying.html)
- [Deleting a parameter group](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.deleting.html): You can delete a custom parameter group using the MemoryDB console, the AWS CLI, or the MemoryDB API.
- [Engine specific parameters](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.redis.html): If you do not specify a parameter group for your Valkey or Redis OSS cluster, then a default parameter group appropriate to your engine version will be used.
- [Restricted commands](https://docs.aws.amazon.com/memorydb/latest/devguide/restrictedcommands.html): Restricted commands.
- [Tutorial: Configuring a Lambda function to access MemoryDB in an Amazon VPC](https://docs.aws.amazon.com/memorydb/latest/devguide/LambdaMemoryDB.html): Configuring Lambda to access MemoryDB in an Amazon VPC.


## [Vector search](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search.html)

- [Vector search overview](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-overview.html): Vector search is built on the creation, maintenance and use of indexes.
- [Use cases](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-examples.html): Following are use cases of vector search.
- [Vector search features and limits](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-limits.html)
- [Create a cluster enabled for vector search](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-cluster.html): You can create a cluster that is enabled for vector search by using the AWS Management Console, or the AWS Command Line Interface.

### [Vector search commands](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands.html)

Following are a list of supported commands for vector search.

- [FT.CREATE](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.create.html): Creates an index and initiates a backfill of that index.
- [FT.SEARCH](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.search.html): Uses the provided query expression to locate keys within an index.
- [FT.AGGREGATE](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.aggregate.html): A superset of the FT.SEARCH command, it allows substantial additional processing of the keys selected by the query expression.
- [FT.DROPINDEX](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.dropindex.html): Drop an index.
- [FT.INFO](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.info.html): Syntax
- [FT._LIST](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.list.html): List all indexes.
- [FT.ALIASADD](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.aliasadd.html): Add an alias for an index.
- [FT.ALIASDEL](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.aliasdel.html): Delete an existing alias for an index.
- [FT.ALIASUPDATE](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.aliasupdate.html): Update an existing alias to point to a different physical index.
- [FT._ALIASLIST](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.aliaslist.html): List the index aliases.
- [FT.PROFILE](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.profile.html): Run a query and return profile information about that query.
- [FT.EXPLAIN](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.explain.html): Parse a query and return information about how that query was parsed.
- [FT.EXPLAINCLI](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-commands-ft.explain-cli.html): Same as the FT.EXPLAIN command except that the results are displayed in a different format more useful with the redis-cli.


## [MemoryDB Multi-Region](https://docs.aws.amazon.com/memorydb/latest/devguide/multi-region.html)

- [Prerequisites and limitations](https://docs.aws.amazon.com/memorydb/latest/devguide/multi-region.prereq.html): Before getting started with MemoryDB Multi-Region, be aware of the following:
- [How it works](https://docs.aws.amazon.com/memorydb/latest/devguide/multi-region.how.html): Here's how MemoryDB Multi-Region works.
- [Using MemoryDB Multi-Region with the console](https://docs.aws.amazon.com/memorydb/latest/devguide/multi-Region.console.html): Here are ways to use MemoryDB Multi-Region with the console.
- [Using MemoryDB Multi-Region with the CLI](https://docs.aws.amazon.com/memorydb/latest/devguide/multi-Region.cli.html): Below are ways to use MemoryDB Multi-Region with the CLI
- [Monitoring MemoryDB Multi-Region](https://docs.aws.amazon.com/memorydb/latest/devguide/multi-Region.monitoring.html): You can use Amazon CloudWatch to monitor the behavior and performance of a Multi-Region cluster.
- [Scaling with MemoryDB Multi-Region](https://docs.aws.amazon.com/memorydb/latest/devguide/multi-Region.Scaling.html): As demand on your clusters changes, you might decide to improve performance or reduce costs by changing the node type or the number of shards in your MemoryDB cluster.
- [Supported and unsupported commands](https://docs.aws.amazon.com/memorydb/latest/devguide/multi-Region.SupportedCommands.html): Supported commands


## [Security](https://docs.aws.amazon.com/memorydb/latest/devguide/security.html)

### [Data protection](https://docs.aws.amazon.com/memorydb/latest/devguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in MemoryDB.

- [Data security in MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/encryption.html): Encrypt data with MemoryDB.
- [At-Rest Encryption](https://docs.aws.amazon.com/memorydb/latest/devguide/at-rest-encryption.html): Encrypt data in the transcation log and on disk during snapshot operations with MemoryDB.
- [In-transit encryption (TLS)](https://docs.aws.amazon.com/memorydb/latest/devguide/in-transit-encryption.html): Encrypt data in transit with MemoryDB.
- [Authenticating users with ACLs](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html): Use Valkey and Redis OSS Access Control Lists (ACLs) to protect access to your data in MemoryDB.
- [Authenticating with IAM](https://docs.aws.amazon.com/memorydb/latest/devguide/auth-iam.html)

### [Identity and access management](https://docs.aws.amazon.com/memorydb/latest/devguide/iam.html)

Identifies methods for controlling access to your MemoryDB resources.

- [How MemoryDB works with IAM](https://docs.aws.amazon.com/memorydb/latest/devguide/security_iam_service-with-iam.html): Before you use IAM to manage access to MemoryDB, learn what IAM features are available to use with MemoryDB.
- [Identity-based policy examples](https://docs.aws.amazon.com/memorydb/latest/devguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify MemoryDB resources.
- [Troubleshooting](https://docs.aws.amazon.com/memorydb/latest/devguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with MemoryDB and IAM.

### [Overview of managing access](https://docs.aws.amazon.com/memorydb/latest/devguide/iam.overview.html)

Every AWS resource is owned by an AWS account, and permissions to create or access a resource are governed by permissions policies.

- [Using identity-based policies (IAM policies)](https://docs.aws.amazon.com/memorydb/latest/devguide/iam.identitybasedpolicies.html): This topic provides examples of identity-based policies in which an account administrator can attach permissions policies to IAM identities (that is, users, groups, and roles).
- [Resource-level permissions](https://docs.aws.amazon.com/memorydb/latest/devguide/iam.resourcelevelpermissions.html): You can restrict the scope of permissions by specifying resources in an IAM policy.
- [Using Service-Linked Roles](https://docs.aws.amazon.com/memorydb/latest/devguide/using-service-linked-roles.html): How to use service-linked roles to give MemoryDB access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/memorydb/latest/devguide/security-iam-awsmanpol.html): Learn about AWS managed policies for MemoryDB and recent changes to those policies.
- [MemoryDB API permissions reference](https://docs.aws.amazon.com/memorydb/latest/devguide/iam.APIReference.html): When you set up access control and write permissions policies to attach to an IAM policy (either identity-based or resource-based), use the following table as a reference.

### [Logging and monitoring](https://docs.aws.amazon.com/memorydb/latest/devguide/monitoring-overview.html)

Monitor MemoryDB to maintain reliability, availability, and performance.

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/memorydb/latest/devguide/monitoring-cloudwatch.html)

You can monitor MemoryDB using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.

- [Host-Level Metrics](https://docs.aws.amazon.com/memorydb/latest/devguide/metrics.HostLevel.html): The AWS/MemoryDB namespace includes the following host-level metrics for individual nodes.
- [Metrics for MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/metrics.memorydb.html): The AWS/MemoryDB namespace includes the following metrics.
- [Which Metrics Should I Monitor?](https://docs.aws.amazon.com/memorydb/latest/devguide/metrics.whichshouldimonitor.html): Lists best practices for which CloudWatch metrics to use to monitor your MemoryDB performance.
- [Choosing Metric Statistics and Periods](https://docs.aws.amazon.com/memorydb/latest/devguide/metrics.ChoosingStatisticsAndPeriods.html): While CloudWatch will allow you to choose any statistic and period for each metric, not all combinations will be useful.
- [Monitoring CloudWatch metrics](https://docs.aws.amazon.com/memorydb/latest/devguide/cloudwatchmetrics.html): Monitor your cluster and nodes with metrics using CloudWatch.

### [Monitoring events](https://docs.aws.amazon.com/memorydb/latest/devguide/monitoring-events.html)

When significant events happen for a cluster, MemoryDB sends notification to a specific Amazon SNS topic.

- [Managing MemoryDB Amazon SNS notifications](https://docs.aws.amazon.com/memorydb/latest/devguide/mdbevents.sns.html): You can configure MemoryDB to send notifications for important cluster events using Amazon Simple Notification Service (Amazon SNS).
- [Viewing MemoryDB events](https://docs.aws.amazon.com/memorydb/latest/devguide/mdbevents.viewing.html): MemoryDB logs events that relate to your clusters, security groups, and parameter groups.
- [Event Notifications and Amazon SNS](https://docs.aws.amazon.com/memorydb/latest/devguide/memorydbsns.html): Lists the notifications of significant events that happen on a cluster with MemoryDB and Amazon SNS messages.
- [Logging MemoryDB API calls with AWS CloudTrail](https://docs.aws.amazon.com/memorydb/latest/devguide/logging-using-cloudtrail.html): Learn about logging MemoryDB with AWS CloudTrail.
- [Compliance validation](https://docs.aws.amazon.com/memorydb/latest/devguide/memorydb-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Infrastructure security](https://docs.aws.amazon.com/memorydb/latest/devguide/infrastructure-security.html): Learn how MemoryDB isolates service traffic.

### [Internetwork traffic privacy](https://docs.aws.amazon.com/memorydb/latest/devguide/Security.traffic.html)

Identifies methods for controlling access to your MemoryDB resources.

### [MemoryDB and Amazon VPC](https://docs.aws.amazon.com/memorydb/latest/devguide/vpcs.html)

Add a MemoryDB cluster to a virtual network and control access to the cluster by using Amazon VPC security groups.

- [Understanding MemoryDB and VPCs](https://docs.aws.amazon.com/memorydb/latest/devguide/vpcs.mdb.html): Manage software upgrades, patching, failure detection and recovery with MemoryDB whether your clusters are deployed inside or outside a VPC based on the Amazon VPC service.
- [Amazon VPC Access Patterns](https://docs.aws.amazon.com/memorydb/latest/devguide/memorydb-vpc-accessing.html): Access patterns for accessing a MemoryDB cluster in a VPC.
- [Creating a Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/memorydb/latest/devguide/VPCs.creatingVPC.html): Create a virtual private cloud with a private subnet for each Availability Zone.

### [Subnets and subnet groups](https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.html)

Identifies methods for controlling access to your MemoryDB resources.

- [MemoryDB and IPV6](https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.ipv6.html): You can create new dual stack and ipv6-only clusters with both Valkey and Redis OSS engines, by providing subnet groups with dual stack and ipv6-only subnets.
- [Creating a subnet group](https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.creating.html): When you create a new subnet group, note the number of available IP addresses.
- [Updating a subnet group](https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.modifying.html): You can update a subnet group's description, or modify the list of subnet IDs associated with the subnet group.
- [Viewing subnet group details](https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.Viewing.html): The following procedures show you how to view details a subnet group.
- [Deleting a subnet group](https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.deleting.html): If you decide that you no longer need your subnet group, you can delete it.
- [MemoryDB API and interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/memorydb/latest/devguide/memorydb-privatelink.html): You can establish a private connection between your VPC and MemoryDB API endpoints by creating an interface VPC endpoint.
- [Addressed security vulnerabilities](https://docs.aws.amazon.com/memorydb/latest/devguide/cve.html): Common Vulnerabilities and Exposures (CVE) is a list of entries for publicly known cybersecurity vulnerabilities.

### [Service updates](https://docs.aws.amazon.com/memorydb/latest/devguide/service-updates.html)

Use service updates to manage and control updates to your MemoryDB MemoryDB.

- [Managing the service updates](https://docs.aws.amazon.com/memorydb/latest/devguide/managing-updates.html): MemoryDB service updates are released on a regular basis.
- [Applying the service updates](https://docs.aws.amazon.com/memorydb/latest/devguide/applying-updates.html): You can start applying the service updates to your fleet from the time that the updates have an available status.


## [Reference](https://docs.aws.amazon.com/memorydb/latest/devguide/memorydb-api-reference.html)

### [Using the MemoryDB API](https://docs.aws.amazon.com/memorydb/latest/devguide/programmingguide.html)

Describes the basics of how to use the MemoryDB API.

- [Using the query API](https://docs.aws.amazon.com/memorydb/latest/devguide/programmingguide.queryapi.html): Use the Query API to make requests that include common parameters to handle authentication and chosen actions.
- [Available libraries](https://docs.aws.amazon.com/memorydb/latest/devguide/using-libraries.html): >Build your MemoryDB applications with language-specific APIs and libraries provided by AWS.
- [Troubleshooting applications](https://docs.aws.amazon.com/memorydb/latest/devguide/troubleshooting.html): Troubleshoot issues to diagnose and resolve problems that you may encounter while interacting with the MemoryDB API.
