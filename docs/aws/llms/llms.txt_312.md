# Source: https://docs.aws.amazon.com/documentdb/latest/developerguide/llms.txt

# Amazon DocumentDB Developer Guide

> Provides a conceptual overview of Amazon DocumentDB and provides instructions on using the various features with both the console and the command line interface.

- [Get started guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html)
- [Quick start using CloudFormation](https://docs.aws.amazon.com/documentdb/latest/developerguide/quick_start_cfn.html)
- [MongoDB compatibility](https://docs.aws.amazon.com/documentdb/latest/developerguide/compatibility.html)
- [Transactions](https://docs.aws.amazon.com/documentdb/latest/developerguide/transactions.html)
- [Best practices](https://docs.aws.amazon.com/documentdb/latest/developerguide/best_practices.html)
- [Functional differences with MongoDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/functional-differences.html)
- [Supported MongoDB APIs, operations, and data types](https://docs.aws.amazon.com/documentdb/latest/developerguide/mongo-apis.html)
- [OpenSearch integration](https://docs.aws.amazon.com/documentdb/latest/developerguide/openSearch-zero-etl.html)
- [Quotas and limits](https://docs.aws.amazon.com/documentdb/latest/developerguide/limits.html)
- [Release notes](https://docs.aws.amazon.com/documentdb/latest/developerguide/release-notes.html)
- [Document history](https://docs.aws.amazon.com/documentdb/latest/developerguide/doc-history.html)

## [What is Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html)

- [How it works](https://docs.aws.amazon.com/documentdb/latest/developerguide/how-it-works.html): Overview of Amazon DocumentDB, a fully managed, MongoDB-compatible database service.

### [What is a document database?](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is-document-db.html)

Overview of what a document database is, and examples that demonstrate how to use the MongoDB API to work with documents.

- [Use cases](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-database-use-cases.html): Scenarios in which you might consider using a document database like Amazon DocumentDB to manage your data.
- [Understanding documents](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-database-documents-understanding.html): Overview of documents and the terminology used in document databases.
- [Working with documents](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-database-working-with-documents.html): Examples that use the MongoDB API to add, query, update, and delete documents in a document database.


## [Generative AI](https://docs.aws.amazon.com/documentdb/latest/developerguide/generative-ai.html)

- [SageMaker Canvas](https://docs.aws.amazon.com/documentdb/latest/developerguide/no-code-machine-learning.html): Amazon DocumentDB integration with Amazon SageMaker AI Canvas
- [Vector Search](https://docs.aws.amazon.com/documentdb/latest/developerguide/vector-search.html): Insert your chapter abstract text here.


## [Migrating to DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-migration.html)

- [Quick start guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/migration-quick-start.html): AWS Database Migration Service (DMS) enables migration to Amazon DocumentDB by setting up a replication instance and configuring source/target endpoints to perform either one-time data migration or continuous replication between your existing database and DocumentDB cluster.
- [Migration runbook](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-migration-runbook.html): Insert your chapter abstract text here.
- [Migration from Couchbase Server](https://docs.aws.amazon.com/documentdb/latest/developerguide/migration-from-couchbase.html): Migrating from Couchbase Server to Amazon DocumentDB.


## [Upgrading DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/upgrade-docdb.html)

- [Engine version support dates](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-version-support-dates.html): ???
- [Upgrading the Amazon DocumentDB engine version](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-mvu.html): Performing an Amazon DocumentDB engine version upgrade using in-place MVU (major version upgrade).
- [Upgrading using AWS DMS](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-migration.versions.html): How to upgrade from one version of Amazon DocumentDB to another using AWS DMS.
- [Using a long-term support (LTS) release](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-lts-release.html): Information about using long-term support releases in Amazon DocumentDB.


## [Extended Support](https://docs.aws.amazon.com/documentdb/latest/developerguide/extended-support.html)

- [Extended Support charges](https://docs.aws.amazon.com/documentdb/latest/developerguide/support-charges.html): You will incur charges for all clusters running on Extended Support beginning the day after the Amazon DocumentDB version 3.6 end of standard support date.
- [Responsibilities](https://docs.aws.amazon.com/documentdb/latest/developerguide/support-responsibilities.html): The following are the Amazon DocumentDB responsibilities and your responsibilities with Amazon DocumentDB Extended Support.


## [Security](https://docs.aws.amazon.com/documentdb/latest/developerguide/security.html)

- [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-secrets-manager.html): Insert your chapter abstract text here.

### [Data protection](https://docs.aws.amazon.com/documentdb/latest/developerguide/security.data-protection.html)

The AWS shared responsibility model applies to data protection in Amazon DocumentDB (with MongoDB compatibility).

- [Client-side field level encryption](https://docs.aws.amazon.com/documentdb/latest/developerguide/field-level-encryption.html): Encrypting client data before it is sent to a Amazon DocumentDB cluster.
- [Encrypting data at rest](https://docs.aws.amazon.com/documentdb/latest/developerguide/encryption-at-rest.html): Overview of the storage encryption features in Amazon DocumentDB.
- [Encrypting data in transit](https://docs.aws.amazon.com/documentdb/latest/developerguide/security.encryption.ssl.html): Connect to an Amazon DocumentDB cluster using Transport Layer Security (TLS).
- [Key management](https://docs.aws.amazon.com/documentdb/latest/developerguide/security.encryption.ssl.public-key.html): Amazon DocumentDB uses AWS Key Management Service (AWS KMS) to retrieve and manage encryption keys.

### [Identity and Access Management](https://docs.aws.amazon.com/documentdb/latest/developerguide/security-iam.html)

How to authenticate requests and manage access to your Amazon DocumentDB resources.

- [How Amazon DocumentDB works with IAM](https://docs.aws.amazon.com/documentdb/latest/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon DocumentDB, learn what IAM features are available to use with Amazon DocumentDB.
- [Identity-based policy examples](https://docs.aws.amazon.com/documentdb/latest/developerguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon DocumentDB resources.
- [Troubleshooting](https://docs.aws.amazon.com/documentdb/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon DocumentDB and IAM.
- [Managing access permissions to your Amazon DocumentDB resources](https://docs.aws.amazon.com/documentdb/latest/developerguide/UsingWithRDS.IAM.AccessControl.Overview.html): Manage permissions for accessing and performing actions on Amazon DocumentDB resources.
- [Using identity-based policies (IAM policies)](https://docs.aws.amazon.com/documentdb/latest/developerguide/UsingWithRDS.IAM.AccessControl.IdentityBased.html): Use IAM policies to attach permissions to users, groups and roles in Amazon DocumentDB.
- [AWS managed policies for Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-managed-policies.html): Managed policies
- [Amazon DocumentDB API permissions reference](https://docs.aws.amazon.com/documentdb/latest/developerguide/UsingWithRDS.IAM.ResourcePermissions.html): Create fine-grained permissions that specify which Amazon DocumentDB resources users can perform actions on.
- [Authentication using IAM identity](https://docs.aws.amazon.com/documentdb/latest/developerguide/iam-identity-auth.html): Use IAM identity for Amazon DocumentDB cluster authentication.
- [Managing Amazon DocumentDB users](https://docs.aws.amazon.com/documentdb/latest/developerguide/security.managing-users.html): How to manage users in Amazon DocumentDB (with MongoDB compatibility), including working with the primary user and creating additional users.
- [Role-Based Access Control](https://docs.aws.amazon.com/documentdb/latest/developerguide/role_based_access_control.html): Use built-in roles and role-based access control to control user access in Amazon DocumentDB.
- [Logging and monitoring](https://docs.aws.amazon.com/documentdb/latest/developerguide/logging-and-monitoring.html): Use CloudWatch metrics to monitor the health and performance of your Amazon DocumentDB clusters.
- [Updating certificates](https://docs.aws.amazon.com/documentdb/latest/developerguide/ca_cert_rotation.html): Instructions for updating CA certificates to use the new CA certificate to create TLS connections in Amazon DocumentDB.
- [Updating certificates â GovCloud](https://docs.aws.amazon.com/documentdb/latest/developerguide/ca_cert_rotation_pdt.html): Instructions for updating CA certificates to use a new CA certificate to create TLS connections in Amazon DocumentDB.
- [Compliance validation](https://docs.aws.amazon.com/documentdb/latest/developerguide/security.compliance-validation.html): The security and compliance of Amazon DocumentDB is assessed by third-party auditors as part of multiple AWS compliance programs, including the following:
- [Resilience](https://docs.aws.amazon.com/documentdb/latest/developerguide/security.disaster-recovery-resiliency.html): The AWS global infrastructure is built around AWS Regions and Availability Zones.
- [Infrastructure security](https://docs.aws.amazon.com/documentdb/latest/developerguide/security.infrastructure.html): As a managed service, Amazon DocumentDB is protected by AWS global network security.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-private-link.html): AWS PrivateLink integration with Amazon DocumentDB
- [Security best practices](https://docs.aws.amazon.com/documentdb/latest/developerguide/security_best_practices.html): For security best practices, you must use AWS Identity and Access Management (IAM) accounts to control access to Amazon DocumentDB API operations, especially operations that create, modify, or delete Amazon DocumentDB resources.
- [Auditing events](https://docs.aws.amazon.com/documentdb/latest/developerguide/event-auditing.html): Audit events that were performed in your cluster in Amazon DocumentDB.

### [Amazon VPC and Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/vpc-docdb.html)

Amazon VPC enables DocumentDB deployment in customizable virtual networks with IPv4-only or dual-stack options at no extra cost.

- [DocumentDB clusters in a VPC](https://docs.aws.amazon.com/documentdb/latest/developerguide/vpc-clusters.html): Amazon DocumentDB clusters operate within Amazon VPC environments, providing logical isolation with subnet organization and IP addressing options, while offering guidance on cluster creation and management within these virtual networks.
- [Accessing a cluster in a VPC](https://docs.aws.amazon.com/documentdb/latest/developerguide/access-cluster-vpc.html): Amazon DocumentDB provides flexible connectivity options for accessing clusters within VPC environments, supporting scenarios for connections from EC2 instances in both the same VPC and across different VPCs.
- [Create an IPv4-only VPC for a cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-vpc-create-ipv4.html): create an Amazon DocumentDB clusters with IPv4-only) networking in a VPC environment.
- [Create a dual-stack VPC for a cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-vpc-create-dual-stack.html): Create an Amazon DocumentDB clusters with dual-stack (IPv4 and IPv6) networking in a VPC environment.


## [Backing up and restoring](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore.html)

- [Back up and restore: concepts](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-nouns_verbs.html)
- [Understanding backup storage usage](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-understanding_backup_storage_usage.html): Amazon DocumentDB backup storage consists of continuous backups within the backup retention period and manual snapshots outside the retention period.
- [Dumping, restoring, importing, and exporting data](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-dump_restore_import_export_data.html): You can use the mongodump, mongorestore, mongoexport, and mongoimport utilities to move data in and out of your Amazon DocumentDB cluster.
- [Cluster snapshot considerations](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-cluster_snapshot_considerations.html): Issues to consider when using Amazon DocumentDB automatic and manual snapshots.
- [Comparing automatic and manual snapshots](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-compare_automatic_manual_snapshots.html): Compare the key features of Amazon DocumentDB automatic and manual snapshots.
- [Creating a manual cluster snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-create_manual_cluster_snapshot.html): Create a manual cluster snapshot in Amazon DocumentDB using the console or AWS CLI.
- [Copying a cluster snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-copy_cluster_snapshot.html): Copy an Amazon DocumentDB cluster snapshot using the AWS Management Console or AWS CLI.
- [Sharing a cluster snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-share_cluster_snapshots.html): How to share Amazon DocumentDB snapshots.
- [Restoring from a cluster snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-restore_from_snapshot.html): Restore an Amazon DocumentDB cluster from a snapshot.
- [Restoring to a point in time](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-point_in_time_recovery.html): Restore a cluster in Amazon DocumentDB to any point in time within the backup retention period using the AWS CLI.
- [Deleting a cluster snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-delete_cluster_snapshot.html): Delete a cluster snapshot in Amazon DocumentDB using the console or the AWS CLI.


## [Managing Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/managing-documentdb.html)

- [Operational tasks overview](https://docs.aws.amazon.com/documentdb/latest/developerguide/operational_tasks.html): Overview of operational tasks for an Amazon DocumentDB cluster and how to accomplish these tasks using the AWS CLI.

### [Global clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/global-clusters.html)

With an global cluster, you can run globally distributed applications using a single cluster that spans multiple AWS Regions.

- [Quick start guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/global-clusters.get-started.html)
- [Managing global clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/global-clusters.manage.html): You perform most management operations on the individual clusters that make up a global cluster.
- [Connecting global clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/global-clusters-connect.html): How you connect to a global cluster depends on whether you need to write to the cluster or read from the cluster:
- [Monitoring global clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/global-clusters-monitor.html): Amazon DocumentDB (with MongoDB compatibility) integrates with CloudWatch so that you can gather and analyze operational metrics for your clusters.
- [Disaster recovery](https://docs.aws.amazon.com/documentdb/latest/developerguide/global-clusters-disaster-recovery.html): Topics

### [Managing clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-clusters.html)

Overview of creating, connecting to, viewing, modifying, and managing Amazon DocumentDB clusters.

- [Understanding clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-clusters-understanding.html): Amazon DocumentDB separates compute and storage, and offloads data replication and backup to the cluster volume.
- [Cluster settings](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-parameters.html): When you create or modify a cluster, it is important to understand which parameters are immutable and which are modifiable after the cluster has been created.
- [Cluster storage configurations](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-storage-configs.html): Starting from Amazon DocumentDB 5.0, instance-based clusters support two storage configuration types:
- [Determining a cluster's status](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-status.html): You can determine a cluster's status using the AWS Management Console or AWS CLI.

### [Cluster lifecycle](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-life-cycle.html)

The lifecycle of an Amazon DocumentDB cluster includes creating, describing, modifying, and deleting the cluster.

- [Creating a cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-create.html): An Amazon DocumentDB cluster consists of instances and a cluster volume that represents the data for the cluster.
- [Describing clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-view-details.html): View the details of your Amazon DocumentDB cluster using the AWS Management Console or the AWS CLI.
- [Modifying a cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-modify.html): Modify a specific Amazon DocumentDB cluster using the AWS Management Console or the AWS CLI.
- [Determining pending maintenance](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-determine-pending-maintenance.html): You can determine whether you have the latest Amazon DocumentDB engine version by determining whether you have pending cluster maintenance.
- [Patch updating a cluster's engine version](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-version-upgrade.html): In this section, we will explain how to deploy a patch update using the AWS Management Console or the AWS CLI.
- [Stopping and starting a cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-stop-start.html): Stopping and starting Amazon DocumentDB clusters can help you manage costs for development and test environments.
- [Deleting a cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-delete.html): Delete an Amazon DocumentDB cluster using the AWS Management Console or the AWS CLI.
- [Scaling clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-manage-performance.html): Amazon DocumentDB enables you to scale the storage and compute in your clusters based on your needs.
- [Cloning a volume for a cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-cloning.html)
- [Understanding cluster fault tolerance](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-fault-tolerance.html): Amazon DocumentDB clusters are fault tolerant by design.

### [Managing instances](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instances.html)

Overview of management tasks for Amazon DocumentDB (with MongoDB compatibility) instances, including creating, viewing, and modifying.

### [Instance lifecycle](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-life-cycle.html)

Overview of the lifecycle of an Amazon DocumentDB (with MongoDB compatibility) instance, including creation, maintenance, and deletion.

- [Adding an instance](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-add.html): Add an Amazon DocumentDB instance using the AWS Management Console or the AWS CLI.
- [Describing instances](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-view-details.html): See details about your Amazon DocumentDB instance using the AWS Management Console or the AWS CLI.
- [Modifying an instance](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-modify.html): Modify your Amazon DocumentDB instance using the AWS Management Console or the AWS CLI.
- [Rebooting an instance](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-reboot.html): Reboot your Amazon DocumentDB instance using the AWS Management Console or the AWS CLI.
- [Deleting an instance](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-delete.html): Delete an Amazon DocumentDB instance using the AWS Management Console or the AWS CLI.
- [Managing instance classes](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-classes.html): Overview of Amazon DocumentDB instance classes, which determine the computation and memory capacity of an instance.
- [NVMe-backed instances](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-nvme.html): Insert your chapter abstract text here.

### [Managing subnet groups](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-db-subnet-groups.html)

A virtual private cloud (VPC) is a virtual network dedicated to your AWS account.

- [Creating a subnet group](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-db-subnet-group-create.html): When creating an Amazon DocumentDB cluster, you must choose a Amazon VPC and corresponding subnet group within that Amazon VPC to launch your cluster.
- [Describing a subnet group](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-db-subnet-group-describe.html): You can use the AWS Management Console or the AWS CLI to get the details of an Amazon DocumentDB subnet group.
- [Modifying a subnet group](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-db-subnet-group-modify.html): You can use the AWS Management Console or AWS CLI to modify a subnet group's description or to add or remove subnets from an Amazon DocumentDB subnet group.
- [Deleting a subnet group](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-db-subnet-group-delete.html): You can use the AWS Management Console or AWS CLI to delete an Amazon DocumentDB subnet group.

### [High availability and replication](https://docs.aws.amazon.com/documentdb/latest/developerguide/replication.html)

You can achieve high availability and read scaling in Amazon DocumentDB (with MongoDB compatibility) by using replica instances.

- [Failover](https://docs.aws.amazon.com/documentdb/latest/developerguide/failover.html): In certain cases, such as certain types of planned maintenance, or in the unlikely event of a primary node or Availability Zone failure, Amazon DocumentDB (with MongoDB compatibility) detects the failure and replaces the primary node.
- [Managing indexes](https://docs.aws.amazon.com/documentdb/latest/developerguide/managing-indexes.html)
- [Managing document compression](https://docs.aws.amazon.com/documentdb/latest/developerguide/doc-compression.html): Insert your chapter abstract text here.
- [Managing dictionary-based compression](https://docs.aws.amazon.com/documentdb/latest/developerguide/dict-compression.html): This section describes dictionary-based compression and steps to manage it in Amazon DocumentDB 8.0.
- [Managing events](https://docs.aws.amazon.com/documentdb/latest/developerguide/managing-events.html): Amazon DocumentDB (with MongoDB compatibility) keeps a record of events that relate to your clusters, instances, snapshots, security groups, and cluster parameter groups.
- [Choosing regions and availability zones](https://docs.aws.amazon.com/documentdb/latest/developerguide/regions-and-azs.html): Amazon cloud computing resources are hosted in multiple locations worldwide.

### [Managing cluster parameter groups](https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_groups.html)

You can manage Amazon DocumentDB engine configuration by using parameters in a cluster parameter group.

- [Describing cluster parameter groups](https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_groups-describe.html): A default cluster parameter group is created automatically when you create the first Amazon DocumentDB cluster in new region or are using a new engine.
- [Creating cluster parameter groups](https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_groups-create.html): Manage the parameters of your Amazon DocumentDB clusters by creating a new cluster parameter group and associating it to a cluster.
- [Modifying cluster parameter groups](https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_groups-modify.html): Modify the ParameterValue, Description, or ApplyMethod of any modifiable parameter in a cluster parameter group in Amazon DocumentDB.
- [Modifying clusters to use customized cluster parameter groups](https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_groups-modify_clusters.html): When you create an Amazon DocumentDB cluster, a default.docdb4.0 parameter group is automatically created for that cluster.
- [Copying cluster parameter groups](https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_groups-copy.html): Make a copy of a cluster parameter group in Amazon DocumentDB using the AWS CLI.
- [Resetting cluster parameter groups](https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_groups-reset.html): Reset some or all of an Amazon DocumentDB cluster parameter group's values to the default values by resetting the cluster parameter group.
- [Deleting cluster parameter groups](https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_groups-delete.html): Delete a custom cluster parameter group in Amazon DocumentDB using the console or AWS CLI.

### [Cluster parameters reference](https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_groups-list_of_parameters.html)

View the parameters that apply to all instances in an Amazon DocumentDB cluster.

- [Modifying cluster parameters](https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_groups-parameters.html): In Amazon DocumentDB, cluster parameter groups consist of parameters that apply to all of the instances that you create in the cluster.

### [Understanding endpoints](https://docs.aws.amazon.com/documentdb/latest/developerguide/endpoints.html)

You can use Amazon DocumentDB (with MongoDB compatibility) endpoints to connect to a cluster or instance.

- [Finding a cluster's endpoints](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-endpoints-find.html): You can find a cluster's cluster endpoint and reader endpoint using the Amazon DocumentDB console or AWS CLI.
- [Finding an instance's endpoint](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-endpoint-find.html): You can find the endpoint for an instance using the Amazon DocumentDB console or the AWS CLI.
- [Connecting to endpoints](https://docs.aws.amazon.com/documentdb/latest/developerguide/endpoints-connecting.html): When you have your endpoint, either cluster or instance, you can connect to it using the mongo shell or a connection string.
- [Understanding Amazon DocumentDB ARNs](https://docs.aws.amazon.com/documentdb/latest/developerguide/documentdb-arns.html): Overview of creating and using ARNs in Amazon DocumentDB (with MongoDB compatibility).
- [Tagging resources](https://docs.aws.amazon.com/documentdb/latest/developerguide/tagging.html): Using tags in Amazon DocumentDB to add metadata to your resources.
- [Maintaining Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-maintain.html): Periodically, Amazon DocumentDB performs maintenance on Amazon DocumentDB resources.
- [Understanding service-linked roles](https://docs.aws.amazon.com/documentdb/latest/developerguide/service-linked-roles.html): Amazon DocumentDB (with MongoDB compatibility) uses AWS Identity and Access Management (IAM) service-linked roles.
- [Using change streams](https://docs.aws.amazon.com/documentdb/latest/developerguide/change_streams.html): Get a time-ordered sequence of change events that occur within your clusterâs collections using change streams in Amazon DocumentDB.
- [Using Collation](https://docs.aws.amazon.com/documentdb/latest/developerguide/collation.html): This section describes the steps to set up and manage collation in Amazon DocumentDB 8.0.
- [Using Views](https://docs.aws.amazon.com/documentdb/latest/developerguide/views.html): This section describes the steps to set up and manage views in Amazon DocumentDB 8.0.
- [Using AWS Lambda with change streams](https://docs.aws.amazon.com/documentdb/latest/developerguide/using-lambda.html): Using AWS Lambda to process records in Amazon DocumentDB change streams.


## [Using elastic clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-using-elastic-clusters.html)

- [How it works](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-how-it-works.html): Overview of Amazon DocumentDB, a fully managed, MongoDB-compatible database service.
- [Get started](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-get-started.html): Amazon DocumentDB Elastic clusters getting started.
- [Best practices](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-best-practices.html): Insert your chapter abstract text here.

### [Managing elastic clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-managing.html)

Managing elastic cluster configuration

- [Managing elastic cluster snapshots](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-manage-snapshots.html): Manual snapshots can be taken after an elastic cluster has been created.
- [Stopping and starting an elastic cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-cluster-stop-start.html): Stopping and starting Amazon DocumentDB elastic clusters can help you manage costs for development and test environments.
- [Maintaining elastic clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-cluster-maintenance.html): Topics
- [Data encryption at rest](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-encryption.html): Encrypting Amazon DocumentDB elastic cluster data at rest.
- [Service-linked roles](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-service-linked-roles.html): Insert your chapter abstract text here.


## [Monitoring Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/monitoring_docdb.html)

- [Monitoring a cluster's status](https://docs.aws.amazon.com/documentdb/latest/developerguide/monitoring_docdb-cluster_status.html): The status of a cluster indicates the health of the cluster.
- [Monitoring an instance's status](https://docs.aws.amazon.com/documentdb/latest/developerguide/monitoring_docdb-instance_status.html): Overview of how to view Amazon DocumentDB instance statuses.
- [Viewing Amazon DocumentDB recommendations](https://docs.aws.amazon.com/documentdb/latest/developerguide/view-docdb-recommendations.html): Amazon DocumentDB provides a list of automated recommendations for database resources, such as instances and clusters.

### [Event subscriptions](https://docs.aws.amazon.com/documentdb/latest/developerguide/event-subscriptions.html)

Amazon DocumentDB uses Amazon Simple Notification Service (Amazon SNS) to provide notifications when an Amazon DocumentDB event occurs.

- [Subscribing to events](https://docs.aws.amazon.com/documentdb/latest/developerguide/event-subscriptions.subscribe.html): You can use the Amazon DocumentDB console to subscribe to event subscriptions, as follows:
- [Manage subscriptions](https://docs.aws.amazon.com/documentdb/latest/developerguide/event-subscriptions.managing.html): If you choose Event subscriptions in the navigation pane of the Amazon DocumentDB console, you can view subscription categories and a list of your current subscriptions.
- [Categories and messages](https://docs.aws.amazon.com/documentdb/latest/developerguide/event-subscriptions.categories-messages.html): Amazon DocumentDB generates a significant number of events in categories that you can subscribe to using the console.
- [Monitoring Amazon DocumentDB with CloudWatch](https://docs.aws.amazon.com/documentdb/latest/developerguide/cloud_watch.html): Use CloudWatch metrics to monitor the health and performance of your Amazon DocumentDB clusters.
- [Logging Amazon DocumentDB API calls with CloudTrail](https://docs.aws.amazon.com/documentdb/latest/developerguide/logging-with-cloudtrail.html): Use CloudWatch metrics to monitor the health and performance of your Amazon DocumentDB clusters.
- [Profiling operations](https://docs.aws.amazon.com/documentdb/latest/developerguide/profiling.html): Use the profiler to log the execution time and details of operations that were performed on your Amazon DocumentDB cluster.

### [Monitoring with Performance Insights](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights.html)

Learn how Performance Insights can help illustrate your cluster performance and analyze any issues that affect it.

- [Performance Insights concepts](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-concepts.html): Learn the key concepts needed to use Performance Insights with Amazon DocumentDB
- [Enabling and disabling Performance Insights](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-enabling.html): Learn how to enable and disable Performance Insights monitoring.
- [Configuring access policies for Performance Insights](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-policies.html): Learn how to configure access policies for Performance Insights

### [Analyzing metrics with the Performance Insights dashboard](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-analyzing.html)

Learn about the different database performance information available through the Performance Insights dashboard.

- [Overview of the Performance Insights dashboard](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-dashboard-overview.html): Get an overview of the Performance Insights dashboard.
- [Opening the Performance Insights dashboard](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-dashboard-opening.html): Learn how to open the Performance Insights dashboard.
- [Analyzing database load by wait states](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-analyzing-db-load.html): Learn how to analyze your database load with Performance Insights.
- [Overview of the Top queries tab](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-top-queries.html): Learn how to interact with the Top queries tab.
- [Zooming in on the database load chart](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-zoom-db-load.html): Learn about the different components in the database load chart.
- [Retrieving metrics with the Performance Insights API](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-metrics.html): Learn how to retrieve metrics with the Performance Insights API
- [Amazon CloudWatch metrics for Performance Insights](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-cloudwatch.html): Learn how Performance Insights interacts with CloudWatch
- [Performance Insights for counter metrics](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights-counter-metrics.html): Learn about the operating system metrics in the Performance Insights dashboard for Amazon DocumentDB


## [Using DocumentDB serverless](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-serverless.html)

- [How serverless works](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-serverless-how-it-works.html): How AWS serverless works in Amazon DocumentDB, including supported configurations, scaling, and idle state.
- [Serverless requirements and limitations](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-serverless-limitations.html): Amazon DocumentDB requirements and limitations including region availability.
- [Creating a cluster that uses serverless](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-serverless-create-cluster.html): Creating an Amazon DocumentDB serverless cluster.
- [Migrating to serverless](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-serverless-migrating.html): Migrating to an Amazon DocumentDB serverless cluster from an existing DocumentDB provisioned cluster or from MongoDB.
- [Managing serverless](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-serverless-managing.html): Managing Amazon DocumentDB serverless clusters.
- [Serverless instance limits](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-serverless-instance-limits.html): Amazon DocumentDB serverless instance limits including instance memory, connections, cursor limit, open transactions, and active connections.
- [Serverless scaling configuration](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-serverless-scaling-config.html): Amazon DocumentDB serverless scaling configuration including capacity range and avoiding out-of-memory errors.
- [Monitoring serverless](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-serverless-monitoring.html): Monitoring Amazon DocumentDB serverless using Amazon CloudWatch or Performance Insights.


## [Developing with Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/documentdb-development.html)

### [Connect to DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-docdb.html)

Amazon DocumentDB provides multiple connection options, including programmatic connections using MongoDB drivers, connecting from outside a VPC through SSH tunneling or AWS VPN, and popular tools like Studio 3T and DataGrip.

- [Connecting programmatically](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect_programmatically.html): This section contains code examples that demonstrate how to connect to Amazon DocumentDB (with MongoDB compatibility) using several different languages.
- [Connecting from outside an Amazon VPC](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-from-outside-a-vpc.html): Use SSH tunneling to connect to an Amazon DocumentDB cluster.
- [Connecting as a replica set](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-to-replica-set.html): Connect to your Amazon DocumentDB cluster as a replica set and distribute reads to replica instances.
- [Connect using Studio 3T](https://docs.aws.amazon.com/documentdb/latest/developerguide/studio3t.html): Studio 3T is a popular GUI and IDE for developers and data engineers who work with MongoDB.
- [Connect using DataGrip](https://docs.aws.amazon.com/documentdb/latest/developerguide/data-grip-connect.html): DataGrip is a powerful integrated development environment (IDE) that supports various database systems, including Amazon DocumentDB.

### [Connect using Amazon EC2](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-ec2.html)

Step-by-step example of how to set up connectivity between an Amazon DocumentDB cluster and Amazon EC2 and interact with it.

- [Connect Amazon EC2 automatically](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-ec2-auto.html): Topics
- [Connect Amazon EC2 manually](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-ec2-manual.html): Topics

### [Connect using the JDBC driver](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-jdbc.html)

Step-by-step example of how to use Amazon DocumentDB JDBC driver to connect from BI tools such as Tableau and PowerBI.

- [Connect from Tableau Desktop](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-jdbc-tableau.html): Step-by-step example of how to use Amazon DocumentDB JDBC driver to connect from Tableau.
- [Connect from DbVisualizer](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-jdbc-DbVisualizer.html): Step-by-step example of how to use Amazon DocumentDB JDBC driver to connect from DbVisualizer.
- [JDBC automatic schema generation](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-jdbc-autoschemagen.html): Amazon DocumentDB is a document database and therefore does not have the concept of tables and schema.
- [SQL support and limitations](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-jdbc-sqlandlimits.html): The Amazon DocumentDB JDBC driver is a read-only driver that supports a subset of SQL-92 and some common extensions.
- [Troubleshooting](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-jdbc-troubleshooting.html): If you are having problems using the Amazon DocumentDB JDBC driver, refer to the Troubleshooting Guide.

### [Connect using the ODBC driver](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-odbc.html)

Step-by-step example of how to use Amazon DocumentDB ODBC driver to connect from BI tools such as BI Desktop and Microsoft tools such as Excel.

- [Setting up the ODBC driver in Windows](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-odbc-setup-windows.html): Use the following procedure to set up the Amazon DocumentDB ODBC driver in Windows:
- [Connect from Microsoft Excel](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-odbc-excel.html)
- [Connect from Microsoft Power BI Desktop](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-odbc-power-bi.html): Topics
- [Automatic schema generation](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-odbc-schema.html): The ODBC driver is utilizing the Amazon DocumentDB JDBC driver through JNI (Java Native Interface) - making the automatic schema generation feature to work similarly in the JDBC driver.
- [SQL support and limitations](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-odbc-sql-support.html): The Amazon DocumentDB ODBC driver is a read-only driver that supports a subset of SQL-92 and some common extensions.
- [Troubleshooting](https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-odbc-troubleshooting.html): If you are having problems using the Amazon DocumentDB ODBC driver, refer to the Troubleshooting Guide.

### [Program with DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/program-docdb.html)

The service supports JSON schema validation.

### [DocumentDB Java programming guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-java-pg.html)

This comprehensive guide provides a detailed walk through for working with Amazon DocumentDB using MongoDBâs Java drivers, covering essential aspects of database operations and management.

- [Connecting with a Java driver](https://docs.aws.amazon.com/documentdb/latest/developerguide/java-pg-connect-mongo-driver.html): This section provides a step-by-step guide for connecting to Amazon DocumentDB using Java drivers.
- [CRUD operations with Java](https://docs.aws.amazon.com/documentdb/latest/developerguide/java-crud-operations.html): This section discusses performing CRUD (create, read, update, delete) operation in Amazon DocumentDB using MongoDB Java drivers.
- [Index management with Java](https://docs.aws.amazon.com/documentdb/latest/developerguide/index-management-java.html): Indexes allow efficient retrieval of data from an Amazon DocumentDB collection.
- [Event-driven programming](https://docs.aws.amazon.com/documentdb/latest/developerguide/event-driven-programming.html): Event-driven programming in the context of Amazon DocumentDB represents a powerful architectural pattern where database changes serve as the primary event generators that trigger subsequent business logic and processes.
- [Using JSON schema validation](https://docs.aws.amazon.com/documentdb/latest/developerguide/json-schema-validation.html): Amazon DocumentDB collections with JSON schema validation.


## [Querying](https://docs.aws.amazon.com/documentdb/latest/developerguide/querying.html)

- [Query planner v2](https://docs.aws.amazon.com/documentdb/latest/developerguide/query-planner.html): The new query planner for Amazon DocumentDB (planner version 2.0) features advanced query optimization capabilities and improved performance.
- [Query planner v3](https://docs.aws.amazon.com/documentdb/latest/developerguide/query-planner-v3.html): Planner Version 3 in Amazon DocumentDB 8.0 supports 21 aggregation stages, including 6 new stages.
- [Geospatial data](https://docs.aws.amazon.com/documentdb/latest/developerguide/geospatial.html): This section covers how you can query Geospatial data with Amazon Amazon DocumentDB.
- [Partial index](https://docs.aws.amazon.com/documentdb/latest/developerguide/partial-index.html): Insert your chapter abstract text here.
- [Text search](https://docs.aws.amazon.com/documentdb/latest/developerguide/text-search.html): Text index for native text searching.


## [Troubleshooting](https://docs.aws.amazon.com/documentdb/latest/developerguide/troubleshooting.html)

- [Connection issues](https://docs.aws.amazon.com/documentdb/latest/developerguide/troubleshooting.connecting.html): Having trouble connecting? Here are some common scenarios and how to resolve them.
- [Indexes](https://docs.aws.amazon.com/documentdb/latest/developerguide/troubleshooting.index-creation.html): The following topics address what to do if your index or background index build fails.
- [Performance and resource utilization](https://docs.aws.amazon.com/documentdb/latest/developerguide/user_diagnostics.html): Covers common questions and solutions for your Amazon DocumentDB deployment, such as how to determine running tasks, terminate blocked queries, optimize your query plan, and more.
- [Garbage collection](https://docs.aws.amazon.com/documentdb/latest/developerguide/garbage-collection.html): ???


## [Resource management API reference](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.html)

### [Actions](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Operations.html)

The following actions are supported by Amazon DocumentDB (with MongoDB compatibility):

### [Amazon DocumentDB (with MongoDB compatibility)](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Operations_Amazon_DocumentDB_with_MongoDB_compatibility.html)

The following actions are supported by Amazon DocumentDB (with MongoDB compatibility):

- [AddSourceIdentifierToSubscription](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_AddSourceIdentifierToSubscription.html): Adds a source identifier to an existing event notification subscription.
- [AddTagsToResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_AddTagsToResource.html): Adds metadata tags to an Amazon DocumentDB resource.
- [ApplyPendingMaintenanceAction](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ApplyPendingMaintenanceAction.html): Applies a pending maintenance action to a resource (for example, to an Amazon DocumentDB instance).
- [CopyDBClusterParameterGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CopyDBClusterParameterGroup.html): Copies the specified cluster parameter group.
- [CopyDBClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CopyDBClusterSnapshot.html): Copies a snapshot of a cluster.
- [CreateDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBCluster.html): Creates a new Amazon DocumentDB cluster.
- [CreateDBClusterParameterGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBClusterParameterGroup.html): Creates a new cluster parameter group.
- [CreateDBClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBClusterSnapshot.html): Creates a snapshot of a cluster.
- [CreateDBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBInstance.html): Creates a new instance.
- [CreateDBSubnetGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBSubnetGroup.html): Creates a new subnet group. subnet groups must contain at least one subnet in at least two Availability Zones in the AWS Region.
- [CreateEventSubscription](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateEventSubscription.html): Creates an Amazon DocumentDB event notification subscription.
- [CreateGlobalCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateGlobalCluster.html): Creates an Amazon DocumentDB global cluster that can span multiple multiple AWS Regions.
- [DeleteDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DeleteDBCluster.html): Deletes a previously provisioned cluster.
- [DeleteDBClusterParameterGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DeleteDBClusterParameterGroup.html): Deletes a specified cluster parameter group.
- [DeleteDBClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DeleteDBClusterSnapshot.html): Deletes a cluster snapshot.
- [DeleteDBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DeleteDBInstance.html): Deletes a previously provisioned instance.
- [DeleteDBSubnetGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DeleteDBSubnetGroup.html): Deletes a subnet group.
- [DeleteEventSubscription](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DeleteEventSubscription.html): Deletes an Amazon DocumentDB event notification subscription.
- [DeleteGlobalCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DeleteGlobalCluster.html): Deletes a global cluster.
- [DescribeCertificates](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeCertificates.html): Returns a list of certificate authority (CA) certificates provided by Amazon DocumentDB for this AWS account.
- [DescribeDBClusterParameterGroups](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBClusterParameterGroups.html): Returns a list of DBClusterParameterGroup descriptions.
- [DescribeDBClusterParameters](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBClusterParameters.html): Returns the detailed parameter list for a particular cluster parameter group.
- [DescribeDBClusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBClusters.html): Returns information about provisioned Amazon DocumentDB clusters.
- [DescribeDBClusterSnapshotAttributes](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBClusterSnapshotAttributes.html): Returns a list of cluster snapshot attribute names and values for a manual DB cluster snapshot.
- [DescribeDBClusterSnapshots](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBClusterSnapshots.html): Returns information about cluster snapshots.
- [DescribeDBEngineVersions](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBEngineVersions.html): Returns a list of the available engines.
- [DescribeDBInstances](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBInstances.html): Returns information about provisioned Amazon DocumentDB instances.
- [DescribeDBSubnetGroups](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBSubnetGroups.html): Returns a list of DBSubnetGroup descriptions.
- [DescribeEngineDefaultClusterParameters](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeEngineDefaultClusterParameters.html): Returns the default engine and system parameter information for the cluster database engine.
- [DescribeEventCategories](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeEventCategories.html): Displays a list of categories for all event source types, or, if specified, for a specified source type.
- [DescribeEvents](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeEvents.html): Returns events related to instances, security groups, snapshots, and DB parameter groups for the past 14 days.
- [DescribeEventSubscriptions](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeEventSubscriptions.html): Lists all the subscription descriptions for a customer account.
- [DescribeGlobalClusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeGlobalClusters.html): Returns information about Amazon DocumentDB global clusters.
- [DescribeOrderableDBInstanceOptions](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeOrderableDBInstanceOptions.html): Returns a list of orderable instance options for the specified engine.
- [DescribePendingMaintenanceActions](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribePendingMaintenanceActions.html): Returns a list of resources (for example, instances) that have at least one pending maintenance action.
- [FailoverDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_FailoverDBCluster.html): Forces a failover for a cluster.
- [FailoverGlobalCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_FailoverGlobalCluster.html): Promotes the specified secondary DB cluster to be the primary DB cluster in the global cluster when failing over a global cluster occurs.
- [ListTagsForResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ListTagsForResource.html): Lists all tags on an Amazon DocumentDB resource.
- [ModifyDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyDBCluster.html): Modifies a setting for an Amazon DocumentDB cluster.
- [ModifyDBClusterParameterGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyDBClusterParameterGroup.html): Modifies the parameters of a cluster parameter group.
- [ModifyDBClusterSnapshotAttribute](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyDBClusterSnapshotAttribute.html): Adds an attribute and values to, or removes an attribute and values from, a manual cluster snapshot.
- [ModifyDBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyDBInstance.html): Modifies settings for an instance.
- [ModifyDBSubnetGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyDBSubnetGroup.html): Modifies an existing subnet group. subnet groups must contain at least one subnet in at least two Availability Zones in the AWS Region.
- [ModifyEventSubscription](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyEventSubscription.html): Modifies an existing Amazon DocumentDB event notification subscription.
- [ModifyGlobalCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyGlobalCluster.html): Modify a setting for an Amazon DocumentDB global cluster.
- [RebootDBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_RebootDBInstance.html): You might need to reboot your instance, usually for maintenance reasons.
- [RemoveFromGlobalCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_RemoveFromGlobalCluster.html): Detaches an Amazon DocumentDB secondary cluster from a global cluster.
- [RemoveSourceIdentifierFromSubscription](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_RemoveSourceIdentifierFromSubscription.html): Removes a source identifier from an existing Amazon DocumentDB event notification subscription.
- [RemoveTagsFromResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_RemoveTagsFromResource.html): Removes metadata tags from an Amazon DocumentDB resource.
- [ResetDBClusterParameterGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ResetDBClusterParameterGroup.html): Modifies the parameters of a cluster parameter group to the default value.
- [RestoreDBClusterFromSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_RestoreDBClusterFromSnapshot.html): Creates a new cluster from a snapshot or cluster snapshot.
- [RestoreDBClusterToPointInTime](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_RestoreDBClusterToPointInTime.html): Restores a cluster to an arbitrary point in time.
- [StartDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_StartDBCluster.html): Restarts the stopped cluster that is specified by DBClusterIdentifier.
- [StopDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_StopDBCluster.html): Stops the running cluster that is specified by DBClusterIdentifier.
- [SwitchoverGlobalCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_SwitchoverGlobalCluster.html): Switches over the specified secondary Amazon DocumentDB cluster to be the new primary Amazon DocumentDB cluster in the global database cluster.

### [Amazon DocumentDB Elastic Clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Operations_Amazon_DocumentDB_Elastic_Clusters.html)

The following actions are supported by Amazon DocumentDB Elastic Clusters:

- [ApplyPendingMaintenanceAction](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ApplyPendingMaintenanceAction.html): The type of pending maintenance action to be applied to the resource.
- [CopyClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_CopyClusterSnapshot.html): Copies a snapshot of an elastic cluster.
- [CreateCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_CreateCluster.html): Creates a new Amazon DocumentDB elastic cluster and returns its cluster structure.
- [CreateClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_CreateClusterSnapshot.html): Creates a snapshot of an elastic cluster.
- [DeleteCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_DeleteCluster.html): Delete an elastic cluster.
- [DeleteClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_DeleteClusterSnapshot.html): Delete an elastic cluster snapshot.
- [GetCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_GetCluster.html): Returns information about a specific elastic cluster.
- [GetClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_GetClusterSnapshot.html): Returns information about a specific elastic cluster snapshot
- [GetPendingMaintenanceAction](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_GetPendingMaintenanceAction.html): Retrieves all maintenance actions that are pending.
- [ListClusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ListClusters.html): Returns information about provisioned Amazon DocumentDB elastic clusters.
- [ListClusterSnapshots](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ListClusterSnapshots.html): Returns information about snapshots for a specified elastic cluster.
- [ListPendingMaintenanceActions](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ListPendingMaintenanceActions.html): Retrieves a list of all maintenance actions that are pending.
- [ListTagsForResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ListTagsForResource.html): Lists all tags on a elastic cluster resource
- [RestoreClusterFromSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_RestoreClusterFromSnapshot.html): Restores an elastic cluster from a snapshot.
- [StartCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_StartCluster.html): Restarts the stopped elastic cluster that is specified by clusterARN.
- [StopCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_StopCluster.html): Stops the running elastic cluster that is specified by clusterArn.
- [TagResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_TagResource.html): Adds metadata tags to an elastic cluster resource
- [UntagResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_UntagResource.html): Removes metadata tags from an elastic cluster resource
- [UpdateCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_UpdateCluster.html): Modifies an elastic cluster.

### [Data Types](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Types.html)

The following data types are supported by Amazon DocumentDB (with MongoDB compatibility):

### [Amazon DocumentDB (with MongoDB compatibility)](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Types_Amazon_DocumentDB_with_MongoDB_compatibility.html)

The following data types are supported by Amazon DocumentDB (with MongoDB compatibility):

- [AvailabilityZone](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_AvailabilityZone.html): Information about an Availability Zone.
- [Certificate](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Certificate.html): A certificate authority (CA) certificate for an AWS account.
- [CertificateDetails](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CertificateDetails.html): Returns the details of the DB instanceâs server certificate.
- [CloudwatchLogsExportConfiguration](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CloudwatchLogsExportConfiguration.html): The configuration setting for the log types to be enabled for export to Amazon CloudWatch Logs for a specific instance or cluster.
- [ClusterMasterUserSecret](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ClusterMasterUserSecret.html): Contains the secret managed by Amazon DocumentDB in AWS Secrets Manager for the master user password.
- [DBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBCluster.html): Detailed information about a cluster.
- [DBClusterMember](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBClusterMember.html): Contains information about an instance that is part of a cluster.
- [DBClusterParameterGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBClusterParameterGroup.html): Detailed information about a cluster parameter group.
- [DBClusterRole](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBClusterRole.html): Describes an AWS Identity and Access Management (IAM) role that is associated with a cluster.
- [DBClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBClusterSnapshot.html): Detailed information about a cluster snapshot.
- [DBClusterSnapshotAttribute](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBClusterSnapshotAttribute.html): Contains the name and values of a manual cluster snapshot attribute.
- [DBClusterSnapshotAttributesResult](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBClusterSnapshotAttributesResult.html): Detailed information about the attributes that are associated with a cluster snapshot.
- [DBEngineVersion](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBEngineVersion.html): Detailed information about an engine version.
- [DBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBInstance.html): Detailed information about an instance.
- [DBInstanceStatusInfo](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBInstanceStatusInfo.html): Provides a list of status information for an instance.
- [DBSubnetGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBSubnetGroup.html): Detailed information about a subnet group.
- [Endpoint](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Endpoint.html): Network information for accessing a cluster or instance.
- [EngineDefaults](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_EngineDefaults.html): Contains the result of a successful invocation of the DescribeEngineDefaultClusterParameters operation.
- [Event](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Event.html): Detailed information about an event.
- [EventCategoriesMap](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_EventCategoriesMap.html): An event source type, accompanied by one or more event category names.
- [EventSubscription](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_EventSubscription.html): Detailed information about an event to which you have subscribed.
- [FailoverState](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_FailoverState.html): Contains the state of scheduled or in-process operations on an Amazon DocumentDB global cluster.
- [Filter](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Filter.html): A named set of filter values, used to return a more specific list of results.
- [GlobalCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_GlobalCluster.html): A data type representing an Amazon DocumentDB global cluster.
- [GlobalClusterMember](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_GlobalClusterMember.html): A data structure with information about any primary and secondary clusters associated with an Amazon DocumentDB global clusters.
- [OrderableDBInstanceOption](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_OrderableDBInstanceOption.html): The options that are available for an instance.
- [Parameter](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Parameter.html): Detailed information about an individual parameter.
- [PendingCloudwatchLogsExports](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_PendingCloudwatchLogsExports.html): A list of the log types whose configuration is still pending.
- [PendingMaintenanceAction](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_PendingMaintenanceAction.html): Provides information about a pending maintenance action for a resource.
- [PendingModifiedValues](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_PendingModifiedValues.html): One or more modified settings for an instance.
- [ResourcePendingMaintenanceActions](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ResourcePendingMaintenanceActions.html): Represents the output of .
- [ServerlessV2FeaturesSupport](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ServerlessV2FeaturesSupport.html): Specifies any Amazon DocumentDB Serverless properties or limits that differ between Amazon DocumentDB engine versions.
- [ServerlessV2ScalingConfiguration](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ServerlessV2ScalingConfiguration.html): Sets the scaling configuration of an Amazon DocumentDB Serverless cluster.
- [ServerlessV2ScalingConfigurationInfo](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ServerlessV2ScalingConfigurationInfo.html): Retrieves the scaling configuration for an Amazon DocumentDB Serverless cluster.
- [Subnet](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Subnet.html): Detailed information about a subnet.
- [Tag](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Tag.html): Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
- [UpgradeTarget](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_UpgradeTarget.html): The version of the database engine that an instance can be upgraded to.
- [VpcSecurityGroupMembership](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_VpcSecurityGroupMembership.html): Used as a response element for queries on virtual private cloud (VPC) security group membership.

### [Amazon DocumentDB Elastic Clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Types_Amazon_DocumentDB_Elastic_Clusters.html)

The following data types are supported by Amazon DocumentDB Elastic Clusters:

- [Cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_Cluster.html): Returns information about a specific elastic cluster.
- [ClusterInList](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ClusterInList.html): A list of Amazon DocumentDB elastic clusters.
- [ClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ClusterSnapshot.html): Returns information about a specific elastic cluster snapshot.
- [ClusterSnapshotInList](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ClusterSnapshotInList.html): A list of elastic cluster snapshots.
- [PendingMaintenanceActionDetails](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_PendingMaintenanceActionDetails.html): Retrieves the details of maintenance actions that are pending.
- [ResourcePendingMaintenanceAction](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ResourcePendingMaintenanceAction.html): Provides information about a pending maintenance action for a resource.
- [Shard](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_Shard.html): The name of the shard.
- [ValidationExceptionField](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ValidationExceptionField.html): A specific field in which a given validation exception occurred.
- [Common Errors](https://docs.aws.amazon.com/documentdb/latest/developerguide/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
- [Common Parameters](https://docs.aws.amazon.com/documentdb/latest/developerguide/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
