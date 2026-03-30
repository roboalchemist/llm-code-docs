# Source: https://docs.aws.amazon.com/redshift/latest/mgmt/llms.txt

# Amazon Redshift Management Guide

> Launch an Amazon Redshift cluster or workgroup and manage the petabyte-scale data warehouse service in the cloud.

- [Tracks](https://docs.aws.amazon.com/redshift/latest/mgmt/tracks.html)
- [Quotas and limits](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html)
- [AWS Backup integration](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-aws-backup.html)
- [Cluster versions](https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html)
- [Behavior changes](https://docs.aws.amazon.com/redshift/latest/mgmt/behavior-changes.html)
- [Document history](https://docs.aws.amazon.com/redshift/latest/mgmt/document-history.html)

## [What Is Amazon Redshift?](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)

- [Amazon Redshift Serverless feature overview](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-considerations.html): Most of the features supported by an Amazon Redshift provisioned data warehouse are also supported by Amazon Redshift Serverless.
- [Amazon Redshift provisioned clusters overview](https://docs.aws.amazon.com/redshift/latest/mgmt/overview.html): Learn about the features and capabilities of Amazon Redshift provisioned clusters.
- [Comparing Amazon Redshift Serverless to an Amazon Redshift provisioned data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-comparison.html): For Amazon Redshift Serverless, some concepts and features are different than their corresponding feature for an Amazon Redshift provisioned data warehouse.

### [Using the Amazon Redshift management interfaces for provisioned clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/using-aws-sdk.html)

Create, manage, and delete Amazon Redshift clusters using several management interfaces.

- [Working with AWS SDKs](https://docs.aws.amazon.com/redshift/latest/mgmt/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.
- [Signing an HTTP request](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-signing-requests.html): Sign the requests that you send to the management API to meet the Amazon Redshift requirement.
- [Setting up the Amazon Redshift CLI](https://docs.aws.amazon.com/redshift/latest/mgmt/setting-up-rs-cli.html): Provides the steps to setup and run the Amazon Redshift command line interface.


## [Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-serverless.html)

### [What is Amazon Redshift Serverless?](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-whatis.html)

Amazon Redshift Serverless automatically provisions data warehouse capacity and intelligently scales the underlying resources.

- [Amazon Redshift Serverless console](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console.html): To learn how to get started with the Amazon Redshift Serverless console, watch the following video.
- [Considerations when using Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-usage-considerations.html): For a list of AWS Regions where the Amazon Redshift Serverless is available, see the endpoints listed for Redshift Serverless API in the Amazon Web Services General Reference.
- [Compute capacity for Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-capacity.html): With Amazon Redshift Serverless compute capacity scales automatically up and down to match your workload requirements.

### [Billing for Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-billing.html)

Billing for Amazon Redshift Serverless.

- [Billing for on-demand compute capacity](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-billing-on-demand.html): Billing for on-demand compute capacity.
- [Billing for serverless reservations](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-billing-reserved.html): Billing for serverless reservations.
- [Connecting to Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-connecting.html): Once you've set up your Amazon Redshift Serverless instance, you can connect to it in a variety of methods, outlined below.
- [Defining database roles for federated users](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-federated-db-roles.html): Passing database roles from an identity provider or IAM and mapping these to Amazon Redshift Serverless database roles.

### [Identity and access management in Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-iam.html)

Access to Amazon Redshift requires credentials that AWS can use to authenticate your requests.

- [Granting permissions](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-security-other-services.html): To access other AWS services, Amazon Redshift Serverless requires permissions.
- [Getting started with IAM credentials](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-iam-credentials.html): When you sign in to the Amazon Redshift console for the first time and first try out Amazon Redshift Serverless, we recommend that you sign in as a user with an attached IAM role that has the policies required.
- [Accessing database objects with database-role permissions](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-iam-credentials-use-case.html): Set up permissions for an IAM user, to give them access to QEV2 and query specific tables.
- [Migrating a provisioned cluster to Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-migration.html): Migrating from a provisioned cluster to Amazon Redshift Serverless takes three steps.

### [Workgroups and namespaces](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroup-namespace.html)

To isolate workloads and manage different resources in Amazon Redshift Serverless, you can create namespaces and workgroups and manage storage and compute resources separately.

### [Workgroups](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-configure-workgroup-working.html)

With Amazon Redshift Serverless, you can create and manage workgroups to isolate and control compute resources for different workloads or users.

- [Creating a workgroup with a namespace](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-workgroups-create-workgroup-wizard.html): Complete the following steps to create a workgroup.
- [Viewing properties for a workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-workgroups.html): In Amazon Redshift Serverless, a workgroup is a collection of compute resources available for use.
- [Deleting a workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless_delete-workgroup.html): Deleting a workgroup using the console.

### [Namespaces](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-configure-namespace-working.html)

In Amazon Redshift Serverless, a namespace defines a logical container for database objects.

- [Searching for a namespace](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-configure-namespace.html): From the Amazon Redshift menu, you can choose from the Namespaces list in order to view or edit the properties for a namespace.
- [Editing security and encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-configuration-edit-network-settings.html): Amazon Redshift Serverless is secured by means of KMS encryption.
- [Changing the AWS KMS key for a namespace](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroups-and-namespaces-rotate-kms-key.html): In Amazon Redshift, encryption protects data at rest.
- [Deleting a namespace](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-namespace-delete.html): If you want to delete a namespace with an associated workgroup, you have to first delete the workgroup.

### [Monitoring queries and workloads](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-monitoring.html)

Learn how to monitor queries and workloads.

- [Adding a query monitoring policy](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-monitor-access.html): Learn how to add a query monitoring policy.
- [Granting query monitoring permissions for a user](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-monitor-access-user.html): Learn how to grant query monitoring permissions for a user.
- [Granting query monitoring permissions for a role](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-monitor-access-role.html): Learn how to grant query monitoring permissions for a role.
- [Setting usage limits](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroup-max-rpu.html): Setting usage limits.
- [Setting query limits](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroup-query-limits.html): Setting query limits.
- [Setting query queues](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroup-query-queues.html): Setting query queues.
- [Checking summary data using the dashboard](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-dashboard.html): Learn how to check your summary data with the dashboard.
- [Audit logging](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-audit-logging.html): You can configure Amazon Redshift Serverless to export connection, user, and user-activity log data to a log group in Amazon CloudWatch Logs.

### [Snapshots and recovery points](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery-points.html)

Describes various scenarios when working with snapshots and recovery points with Amazon Redshift Serverless.

- [Creating a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots.html)
- [Creating a final snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshot-create-final.html): Learn how to create a final snapshot.
- [Sharing a snapshot or removing snapshot permissions](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshot-share.html): Learn how to share a snapshot.
- [Scheduling a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshot-scheduling.html): Learn how to schedule a snapshot
- [Updating a snapshot retention period](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshot-update.html): Learn how to update a snapshot retention period.
- [Deleting a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshot-delete.html): Learn how to deleting a snapshot.
- [Restoring a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshot-restore.html): Learn how to restore a snapshot.
- [Converting a recovery point](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-recovery-point-convert.html): Learn how to convert a recovery point to a snapshot.
- [Restoring a recovery point](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-recovery-point-restore.html): Learn how to restore a recovery point.
- [Copying backups to another AWS Region](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-backup-copy.html): Decribes how to copy snapshots and recovery points to another AWS Region.
- [Restoring a table](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-table-restore.html): Lean how to restore a table.

### [Data sharing](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-datasharing.html)

With data sharing, you have live access to data so that your users can see the most up-to-date and consistent information as it's updated in Amazon Redshift Serverless.

- [Granting access to view datashares](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless_datasharing_permissions.html): Grant access to view all datashares using the console
- [Registering namespaces to the AWS Glue Data Catalog](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless_datasharing-register-namespace.html): Register namespaces to the AWS Glue Data Catalog
- [Tagging resources](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-tagging-resources.html): Describes tagging resources within Amazon Redshift Serverless.


## [Amazon Redshift provisioned clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html)

- [Considerations for using provisioned clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-considerations.html): Considerations for using Amazon Redshift provisioned clusters.

### [Cluster operations](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-operations.html)

Learn about and walk through the ways to manage Amazon Redshift clusters.

- [Creating a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/create-cluster.html): Learn how to create a cluster.
- [Creating a disk space alarm](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-mgmt-edit-default-disk-space-alarm.html): Learn how to create a disk space alarm for a cluster.
- [Viewing a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/view-cluster.html): Learn how to view a cluster.
- [Modifying a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/modify-cluster.html): Learn how to modify a cluster.
- [Resizing a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/resizing-cluster.html): Learn about and walk through the ways to resize Amazon Redshift clusters.
- [Renaming a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-mgmt-rename-cluster.html): Learn how to rename a cluster.
- [Upgrading the release version of a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/upgrade-release-version-cluster.html): Learn how to upgrade the release version of a cluster.
- [Pausing and resuming a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-mgmt-pause-resume-cluster.html): Learn how to pause and resume a cluster.
- [Rebooting a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/reboot-cluster.html): Learn how to reboot a cluster.
- [Relocating a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-recovery.html): Learn about and walk through the ways to manage Amazon Redshift cluster relocation.
- [Setting a usage limit](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-mgmt-set-limit-cluster.html): Learn how to set a usage limit for an Amazon Redshift provisioned cluster..
- [Shutting down and deleting a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-mgmt-shutdown-delete-cluster.html): Learn how to shut down and delete a cluster.

### [Snapshots and backups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)

Learn the basics of creating and managing snapshots, a point-in-time backup of your Amazon Redshift clusters.

- [Creating a manual snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-create.html): Learn how to create a manual snapshot.
- [Creating a snapshot schedule](https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-schedule-create.html): Learn how to create a snapshot schedule.
- [Sharing a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-share-snapshot.html): Learn how to share a snapshot.
- [Copying an automated snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-copy.html): Learn how to copy an automated snapshot.
- [Copying a snapshot to another AWS Region](https://docs.aws.amazon.com/redshift/latest/mgmt/cross-region-snapshot-copy.html): Learn how to copy a snapshot to another AWS Region.
- [Restoring a cluster from a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-cluster-from-snapshot.html): Learn how to restore a cluster from a snapshot.
- [Restoring a table from a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-table-from-snapshot.html): Learn how to restore a table from a snapshot.
- [Restoring a serverless namespace from a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-restore-provisioned-to-serverless.html): Learn how to restore a serverless namespace from a snapshot.
- [Configuring cross-Region snapshot copy for a nonencrypted cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-crossregioncopy-configure.html): Learn how to configure cross-Region snapshot copy for a nonencrypted cluster.
- [Configuring cross-Region snapshot copy for an AWS KMSâencrypted cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/xregioncopy-kms-encrypted-snapshot.html): Learn how to configure cross-Region snapshot copy for an encrypted cluster.
- [Modifying the manual snapshot retention period](https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-manual-retention-period.html): Learn how to modify the manual snapshot retention period.
- [Modifying the retention period for cross-Region snapshot copy](https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-crossregioncopy-modify.html): Learn how to modify the retention period for a cross-Region snapshot copy.
- [Deleting a manual snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-delete.html): Learn how to delete a manual snapshot.
- [Registering a cluster to the AWS Glue Data Catalog](https://docs.aws.amazon.com/redshift/latest/mgmt/register-cluster.html): Learn how to register a cluster to the AWS Glue Data Catalog.

### [Multi-AZ deployment](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-multi-az.html)

Learn about and walk through the ways to manage Multi-AZ deployment in Amazon Redshift.

- [Setting up Multi-AZ deployment](https://docs.aws.amazon.com/redshift/latest/mgmt/overview-multi-az.html): Learn how to set up Multi-AZ deployment.
- [Setting up Multi-AZ when creating a new cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/create-cluster-multi-az.html): Learn how to set up Multi-AZ deployment when you create a new cluster.
- [Setting up Multi-AZ for a data warehouse restored from a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/restore-cluster-multi-az.html): Learn how to set up Multi-AZ deployment for a data warehouse restored from a snapshot.
- [Converting a Single-AZ data warehouse to a Multi-AZ data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/convert-saz-to-maz.html): Learn how to convert a Single-AZ data warehouse to a Multi-AZ data warehouse.
- [Converting a Multi-AZ data warehouse to a Single-AZ data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/convert-maz-to-saz.html): Learn how to convert a Multi-AZ data warehouse to a Single-AZ data warehouse.
- [Resizing a Multi-AZ data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/resize-maz.html): Learn how to resize a Multi-AZ data warehouse.
- [Failing over Multi-AZ deployment](https://docs.aws.amazon.com/redshift/latest/mgmt/test-cluster-multi-az.html): Learn how to fail over Multi-AZ deployment.
- [Viewing queries and loads for Multi-AZ data warehouses](https://docs.aws.amazon.com/redshift/latest/mgmt/viewing-multi-az-queries-loads.html): Learn how to view queries and loads for Multi-AZ data warehouses.
- [Monitoring a query in a Multi-AZ deployment](https://docs.aws.amazon.com/redshift/latest/mgmt/monitoring-multi-az-query.html): Learn how to monitor a query in a Multi-AZ deployment.
- [Terminating a query for a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/ending-cluster-multi-az.html): Learn how terminate a query for a cluster.

### [Monitoring cluster performance](https://docs.aws.amazon.com/redshift/latest/mgmt/metrics.html)

Monitor the performance of your Amazon Redshift clusters.

- [Performance data](https://docs.aws.amazon.com/redshift/latest/mgmt/metrics-listing.html): Work with the metrics and performance data available for assessing your Amazon Redshift cluster's health and performance.

### [Viewing performance data](https://docs.aws.amazon.com/redshift/latest/mgmt/performance-metrics-console.html)

View cluster performance data using the Amazon Redshift console.

- [Viewing cluster performance data](https://docs.aws.amazon.com/redshift/latest/mgmt/performance-metrics-perf.html): View cluster performance data using the Amazon Redshift console.
- [Viewing query history data](https://docs.aws.amazon.com/redshift/latest/mgmt/performance-metrics-query-history.html): View query history data using the Amazon Redshift console.
- [Viewing database performance data](https://docs.aws.amazon.com/redshift/latest/mgmt/performance-metrics-database-performance.html): View database performance data using the Amazon Redshift console.
- [Viewing workload concurrency and concurrency scaling data](https://docs.aws.amazon.com/redshift/latest/mgmt/performance-metrics-concurrency-scaling.html): View concurrency scaling data using the Amazon Redshift console.
- [Viewing automatic optimization data](https://docs.aws.amazon.com/redshift/latest/mgmt/performance-metrics-autonomics.html): View automatic optimization data using the Amazon Redshift console.
- [Viewing queries and loads](https://docs.aws.amazon.com/redshift/latest/mgmt/performance-metrics-queries.html): Learn about performance of queries that run in your Amazon Redshift database.
- [Viewing and analyzing query details](https://docs.aws.amazon.com/redshift/latest/mgmt/performance-metrics-query-execution-details.html): Find information about performance of queries that run in your Amazon Redshift database.
- [Viewing cluster performance as queries run](https://docs.aws.amazon.com/redshift/latest/mgmt/performance-metrics-query-cluster.html): View Amazon Redshift cluster performance during as queries run.
- [Viewing cluster metrics during load operations](https://docs.aws.amazon.com/redshift/latest/mgmt/performance-metrics-loads.html): View Amazon Redshift cluster metrics during load operations to identify queries that affect your cluster's performance.
- [Viewing the cluster workload breakdown chart](https://docs.aws.amazon.com/redshift/latest/mgmt/analyze-workload-performance.html): Use the workload execution breakdown chart to analyze Amazon Redshift query performance.
- [Analyzing query execution](https://docs.aws.amazon.com/redshift/latest/mgmt/analyzing-query-execution.html): Find out about performance of queries that run in your Amazon Redshift database.
- [Creating an alarm](https://docs.aws.amazon.com/redshift/latest/mgmt/performance-metrics-alarms.html): Create an alarm on any of the cluster metrics using the Amazon Redshift console.
- [Ending a running query](https://docs.aws.amazon.com/redshift/latest/mgmt/terminate-queries.html): Learn how to end a running query.
- [Performance metrics in the CloudWatch console](https://docs.aws.amazon.com/redshift/latest/mgmt/using-cloudwatch-console.html): Learn about best practices for working with Amazon Redshift performance metrics in the CloudWatch console.
- [Query profiler](https://docs.aws.amazon.com/redshift/latest/mgmt/using-query-plan-profiler.html): Find performance bottlenecks with Query profiler.
- [Query and Database Monitoring](https://docs.aws.amazon.com/redshift/latest/mgmt/metrics-enhanced-query-monitoring.html): Find performance bottlenecks with Query and Database Monitoring.
- [Sys View-based Queries and Database Monitoring](https://docs.aws.amazon.com/redshift/latest/mgmt/metrics-sys-view-based-queries.html): Find performance bottlenecks with Databse Query Monitoring.


## [Zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html)

- [Considerations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl.reqs-lims.html): The following considerations apply to zero-ETL integrations with Amazon Redshift.

### [Getting started with zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.setting-up.html)

This set of tasks walks you through setting up your first zero-ETL integration.

- [Create and configure a target Amazon Redshift data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-setting-up.rs-data-warehouse.html): In this step, you create and configure a target Amazon Redshift data warehouse, such as a Redshift Serverless workgroup or a provisioned cluster.
- [Turn on case sensitivity](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-setting-up.case-sensitivity.html): You can attach a parameter group and enable case sensitivity for a provisioned cluster during creation.
- [Configure authorization in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.redshift-iam.html): To replicate data from your integration source into your Amazon Redshift data warehouse, you must initially add the following two entities:

### [Create a zero-ETL integration](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-setting-up.create-integration.html)

First, you create a zero-ETL integration to replicate your source data to Amazon Redshift.

- [Create a zero-ETL integration for Aurora](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-setting-up.create-integration-aurora.html): In this step, you create an Aurora zero-ETL integration with Amazon Redshift.
- [Create a zero-ETL integration for Amazon RDS](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-setting-up.create-integration-rds.html): In this step, you create an Amazon RDS zero-ETL integration with Amazon Redshift.
- [Create a zero-ETL integration for DynamoDB](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-setting-up.create-integration-ddb.html): Before creating a zero-ETL integration, review the considerations and requirements outlined in .
- [Create a zero-ETL integration with applications](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-setting-up.create-integration-glue.html): In this step, you create a zero-ETL integration with applications with Amazon Redshift.
- [Creating destination databases](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.creating-db.html): To replicate data from your source into Amazon Redshift, you must create a database from your integration in Amazon Redshift.
- [Querying replicated data](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.querying-and-creating-materialized-views.html): Querying data replicated by zero-ETL integrations with Amazon Redshift.
- [Viewing zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.describing.html): Learn how to view and manage your zero-ETL integrations.
- [History mode](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-history-mode.html): Learn how to manage history mode for your zero-ETL integrations.
- [Sharing your data](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.share-data-redshift.html): >Learn how to share your data in Amazon Redshift
- [Monitoring zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-monitoring.html): You can monitor your zero-ETL integrations by querying the system views or with Amazon EventBridge.
- [Metrics for zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.metrics.html): You can use the metrics in the Amazon Redshift console and Amazon CloudWatch to learn about the health and performance of your zero-ETL integrations.
- [Modify a zero-ETL integration for DynamoDB](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-managing.modify-integration-ddb.html): In this step, you modify an DynamoDB zero-ETL integration with Amazon Redshift.
- [Delete a zero-ETL integration for DynamoDB](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-managing.delete-integration-ddb.html): When you delete an integration, the target data warehouse retains any previously replicated data.
- [Supported Regions](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.regions.html): Zero-ETL integration is a fully managed solution that makes transactional and operational data available in Amazon Redshift from multiple operational and transactional sources, as well as enterprise applications.
- [Troubleshooting zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.troubleshooting.html): Use the following sections to help troubleshoot problems that you have with zero-ETL integrations.


## [Query a database](https://docs.aws.amazon.com/redshift/latest/mgmt/query-databases.html)

- [Connecting to Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-syntax.html): Get the connection string you will use to connect to your Amazon Redshift cluster.

### [Querying a database using the Amazon Redshift query editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html)

Learn how to use the query editor v2 to query an Amazon Redshift database.

- [Configuring your AWS account](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-getting-started.html): Learn how to configure the query editor v2 to query an Amazon Redshift database.
- [Opening query editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-open.html): Learn how to open the query editor v2.
- [Connecting to an Amazon Redshift database](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-connecting.html): To connect to a database, choose the cluster or workgroup name in the tree-view panel.
- [Browsing an Amazon Redshift database](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-object-browse.html): Learn how to use the query editor v2 to manage databases.
- [Creating database objects](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-object-create.html): Learn how to use query editor v2 to create database objects, including databases, schemas, tables, and UDFs.
- [Viewing query and tab history](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-history.html): Learn how to use query editor v2 to view query and tab history.

### [Interacting with Amazon Q generative SQL](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-generative-ai.html)

Learn about how to interact with Amazon Q generative SQL.

- [Using generative SQL](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-generative-ai-interact.html): After the correct permissions are configured, when working with a notebook in query editor v2, you can choose an icon to start a conversation.
- [Updating generative SQL settings as an administrator](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-generative-ai-settings.html): Learn how to use query editor v2 to change generative SQL settings.
- [Tutorial: Using Amazon Q generative SQL capability with the TICKIT data](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-generative-ai-example.html): To author efficient prompts to generate SQL, you must learn about your database schema and your data.

### [Loading data into a database](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-loading.html)

Learn how to use the query editor v2 to load data into your database.

- [Loading data from Amazon S3](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-loading-data.html): Learn how to use query editor v2 to load data into an existing table from Amazon S3.
- [Loading data from a local file setup and workflow](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-loading-data-local.html): Learn how to use query editor v2 to load data into a table from a local file.
- [Authoring queries](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-query-run.html): Learn how to use the query editor v2 to run queries.

### [Notebooks](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-notebooks.html)

Learn how to use the query editor v2 to query an Amazon Redshift database with a notebook.

- [Creating a notebook](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-notebooks-create.html): Learn how to use the query editor v2 to create a notebook.
- [Importing into notebooks](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-notebooks-import.html): Learn how to use the query editor v2 to import into a notebook.
- [Querying the AWS Glue Data Catalog](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-glue.html): Learn how to use the query editor v2 to query an AWS Glue database.
- [Querying a data lake](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-querying-data-lake.html): Learn how to use query editor v2 to query data in a data lake on Amazon S3.

### [Datashares](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-datashare-using.html)

Learn how to use query editor v2 to create and query datashares.

- [Creating datashares](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-create-datashare.html): You create a datashare on the cluster that you want to use as the producer cluster.
- [Showing datashares](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-show-datashare.html): You can show the datashares that you've created on the producer cluster.
- [Creating the consumer database](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-datashare-consumer.html): On the consumer cluster, you create a database from the datashare.
- [Querying datashare objects](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-query-datashare.html): On the consumer cluster, you can query datashare objects using fully qualified object names expressed with the three-part notation: database, schema, and name of the object.

### [Scheduled queries](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-schedule-query.html)

Learn about how to schedule a query with query editor v2.

- [Creating a schedule](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-schedule-query-create.html): Learn about how to schedule a query with query editor v2.
- [Setting permissions to schedule a query](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-schedule-query-permissions.html): To schedule queries, the AWS Identity and Access Management (IAM) user defining the schedule and the IAM role associated with the schedule must be configured with the IAM permissions to use Amazon EventBridge and Amazon Redshift Data API.
- [Authenticating a scheduled query](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-schedule-query-authentication.html)
- [Setting up permissions to view schedule query history](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-schedule-query-view-history.html): To allow users to view schedule query history, edit the IAM role (that is specified with the schedule) Trust relationships to add permissions.
- [Monitoring the scheduled query](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-schedule-query-sns.html): For the Amazon SNS topic that you specify to send email notifications, create the Amazon SNS topic using the query editor v2 by navigating to the SNS notifications section, Turn on monitoring, and create the topic with Create SNS topic.
- [Troubleshooting scheduling a query](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-schedule-query-troubleshooting.html)
- [Finding details about scheduled queries with AWS CloudShell](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-schedule-query-troubleshooting-cloudshell.html): You can use AWS CloudShell to find out details about a schedule query.
- [Visualizing results](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-charts.html): Learn how to visualize query results by using charts.

### [Collaborating and sharing as a team](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-team.html)

Learn how to create and collaborate as a team.

- [Saving queries](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-save-queries.html): Learn how to save, browse for, and delete queries.
- [Sharing a query](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-query-share.html): You can share your queries with your team.
- [Managing query versions](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-query-versions.html): Every time you save a SQL query, the query editor v2 saves it as a new version.
- [Querying a database using the query editor v1](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor.html): Run queries from the Amazon Redshift console.

### [Connecting to a data warehouse using SQL client tools](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-to-cluster.html)

Connect to an Amazon Redshift data warehouse using SQL client tools that support JDBC and ODBC drivers.

### [Configuring connections in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/configuring-connections.html)

Connect to Amazon Redshift over JDBC, Python, and ODBC connections.

- [Finding your cluster connection string](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-connection-string.html): Find your cluster connection string.

### [Configuring a JDBC driver version 2.x connection](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-install.html)

Set up a JDBC driver version 2.x connection for an Amazon Redshift cluster.

- [Download the Amazon Redshift JDBC driver, version 2.1](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-download-driver.html): Download the JDBC driver version 2.x for Amazon Redshift.

### [Installing the Amazon Redshift JDBC driver, version 2.2](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-install-driver.html)

Install the Amazon Redshift JDBC driver version 2.x.

- [Referencing the JDBC driver libraries](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-driver-libraries.html): Reference the JDBC driver libraries for Amazon Redshift.
- [Registering the driver class](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-register-driver-class.html): Register the version 2.x class JDBC driver for Amazon Redshift.
- [Getting the JDBC URL](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-obtain-url.html): Learn about the format of the JDBC URL for Amazon Redshift.
- [Building the connection URL](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-build-connection-url.html): Build your connection URL for the Amazon Redshift JDBC driver version 2.x.
- [Configuring a JDBC connection with Apache Maven](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc20-connection-with-maven.html): Learn the steps to use Apache Maven to configure and build your projects to use a JDBC connection to connect to your Amazon Redshift cluster.

### [Configuring authentication and SSL](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-configure-authentication-ssl.html)

Configure JDBC driver version 2.x authentication and Secure Sockets Layer (SSL) for Amazon Redshift.

- [Using username and password only](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-authentication-username-password.html): Learn how to use authentication with a username and password.
- [Using SSL without identity verification](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-use-ssl-without-identity-verification.html): Learn how to use SSL authentication without identity verification.
- [Using one-way SSL authentication](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-use-one-way-SSL-authentication.html): Learn how to use one-way SSL authentication.

### [Configuring logging](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-configuring-logging.html)

Configure JDBC driver version 2.x logging options for Amazon Redshift.

- [Using log files](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-using-log-files.html): Only turn on logging long enough to capture an issue.
- [Using LogStream or LogWriter](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-logstream-option.html): Only turn on logging long enough to capture an issue.
- [Data type conversions](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-data-type-mapping.html): Convert between Amazon Redshift, SQL, and Java data types.
- [Using prepared statement support](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-prepared-statement-support.html): Learn about prepared statement support for the Amazon Redshift JDBC driver.
- [Differences between the 2.2 and 1.x versions of the JDBC driver](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-jdbc10-driver-differences.html): Learn the differences between the 2.2 and 1.x versions of the JDBC driver for Amazon Redshift.
- [Creating initialization (.ini) files for JDBC driver version 2.x](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-ini-file.html): Learn how to create an Amazon Redshift JDBC driver version 2.x initialization (.ini) file.
- [Options for JDBC driver version 2.x configuration](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-configuration-options.html): Learn what options you can specify for version 2.x of the Amazon Redshift JDBC driver.
- [Previous versions of JDBC driver version 2.x](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-previous-driver-version-20.html): Find previous versions of the Amazon Redshift JDBC driver version 2.x.

### [Amazon Redshift Python connector](https://docs.aws.amazon.com/redshift/latest/mgmt/python-redshift-driver.html)

Learn how to install and configure the Amazon Redshift Python connector.

- [Installing the Python connector](https://docs.aws.amazon.com/redshift/latest/mgmt/python-driver-install.html): Learn how to install the Amazon Redshift Python connector.
- [Configuration options](https://docs.aws.amazon.com/redshift/latest/mgmt/python-configuration-options.html): Learn about the configuration options that you can specify for the Python Amazon Redshift connector.
- [Importing the Python connector](https://docs.aws.amazon.com/redshift/latest/mgmt/python-start-import.html): Learn how to import the Python connector.
- [Integrating the Python connector with NumPy](https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-integrate-numpy.html): Integrate the Amazon Redshift Python connector with NumPy.
- [Integrating the Python connector with pandas](https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-integrate-pandas.html): Integrate the Amazon Redshift Python connector with pandas.
- [Using identity provider plugins](https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-identity-provider-plugins.html): Use identity provider plugins with the Amazon Redshift Python connector.
- [Examples](https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-examples.html): Find examples of how to use the Amazon Redshift Python connector.
- [API reference](https://docs.aws.amazon.com/redshift/latest/mgmt/python-api-reference.html): Learn about the Amazon Redshift Python connector API operations.

### [Amazon Redshift integration for Apache Spark](https://docs.aws.amazon.com/redshift/latest/mgmt/spark-redshift-connector.html)

Apache Spark is a distributed processing framework and programming model that helps you do machine learning, stream processing, or graph analytics.

- [Authentication with the Spark connector](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-spark-connector-authentication.html): The following diagram describes the authentication between Amazon S3, Amazon Redshift, the Spark driver, and Spark executors.
- [Performance improvements with pushdown](https://docs.aws.amazon.com/redshift/latest/mgmt/spark-redshift-connector-pushdown.html): The Spark connector automatically applies predicate and query pushdown to optimize for performance.
- [Other configuration options](https://docs.aws.amazon.com/redshift/latest/mgmt/spark-redshift-connector-other-config.html): On this page, you can find descriptions for the options that you can specify for the Amazon Redshift Spark connector.
- [Supported data types](https://docs.aws.amazon.com/redshift/latest/mgmt/spark-redshift-connector-data-types.html): The following data types in Amazon Redshift are supported with the Spark connector.

### [Configuring an ODBC driver version 2.x connection](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-install.html)

Set up an ODBC driver version 2.x connection for an Amazon Redshift cluster.

- [Getting the ODBC URL](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-getting-url.html): Get the ODBC URl for your Amazon Redshift provisioned cluster.

### [Using an ODBC driver on Microsoft Windows](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-install-config-win.html)

Install and configure the Amazon Redshift ODBC driver version 2.x for Microsoft Windows.

- [Downloading and installing the ODBC driver](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-install-win.html): Download and install the ODBC driver version 2.x.
- [Creating a system DSN entry for an ODBC connection](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-dsn-win.html): Create a system DSN entry for an ODBC connection.

### [Using an ODBC driver on Linux](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-install-config-linux.html)

Install and configure the Amazon Redshift ODBC driver version 2.x for Linux.

- [Downloading and installing the ODBC driver](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-install-linux.html): Install the ODBC driver version 2.x for Linux.
- [Using an ODBC driver manager to configure the ODBC driver](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-config-linux.html): Use an ODBC driver manager to configure the ODBC driver for Linux.

### [Using an ODBC driver on Apple macOS](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-install-config-mac.html)

Install and configure the Amazon Redshift ODBC driver version 2.x for Apple macOS.

- [Downloading and installing the ODBC driver](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-install-mac.html): Download and install the ODBC driver version 2.x.
- [Using an ODBC driver manager to configure the ODBC driver](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-config-mac.html): Use an ODBC driver manager to configure the ODBC driver for Apple macOS.
- [Authentication methods](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-authentication-ssl.html): Configure connection options for various ODBC authentication methods
- [Data types conversions](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-converting-data-types.html): See the supported data type mappings for converting between Amazon Redshift data types and SQL data types.
- [ODBC driver options](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-configuration-options.html): Configure ODBC driver options to control the behavior of the Amazon Redshift ODBC driver.
- [Previous ODBC driver versions](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-previous-versions.html): Download a previous version of the Amazon Redshift ODBC driver version 2.x only if your tool requires a specific version of the driver.

### [Configuring an ODBC driver version 1.x connection](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-odbc-connection.html)

Learn the steps to set up an ODBC driver version 1.x connection for an Amazon Redshift cluster.

- [Getting the ODBC URL](https://docs.aws.amazon.com/redshift/latest/mgmt/obtain-odbc-url.html): Get the ODBC URL for your cluster.

### [Using an ODBC driver on Microsoft Windows](https://docs.aws.amazon.com/redshift/latest/mgmt/install-odbc-driver-windows.html)

Install and configure the Amazon Redshift ODBC driver on your client computer running a Microsoft Windows operating system.

- [Downloading and installing the ODBC driver](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc-driver-windows-how-to-install.html): Download and install the ODBC driver version 1.x.
- [Creating a system DSN entry for an ODBC connection](https://docs.aws.amazon.com/redshift/latest/mgmt/create-dsn-odbc-windows.html): Create a system DSN entry for an ODBC connection.

### [Using an ODBC driver on Linux](https://docs.aws.amazon.com/redshift/latest/mgmt/install-odbc-driver-linux.html)

Install and configure the Amazon Redshift ODBC driver version 1.x for Linux.

- [Downloading and installing the ODBC driver](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc-driver-linux-how-to-install.html): Install the ODBC driver version 1.x for Linux.
- [Using an ODBC driver manager to configure the driver](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc-driver-configure-linux.html): Use an ODBC driver manager to configure the Amazon Redshift ODBC driver on your client computers running a Linux operating system.

### [Using an ODBC driver on macOS X](https://docs.aws.amazon.com/redshift/latest/mgmt/install-odbc-driver-mac.html)

Install and configure the Amazon Redshift ODBC driver version 1.x for macOS X.

- [Downloading and installing the ODBC driver](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc-driver-mac-how-to-install.html): Install the ODBC driver version 1.x for macOS x.
- [Use an ODBC driver manager to configure the driver](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc-driver-configure-mac.html): Use an ODBC driver manager to configure the Amazon Redshift ODBC driver on your client computers running a macOS X operating system.
- [ODBC driver options](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-odbc-options.html): Learn about options to configure the Amazon Redshift ODBC driver on your client computer.
- [Previous ODBC driver versions](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc-previous-versions.html): Learn about previous ODBC driver versions.

### [Configuring security options for connections](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html)

Configure your Amazon Redshift connection to require an SSL certificate to encrypt data that moves between your client and cluster.

- [Transitioning to ACM certificates for SSL connections](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-transitioning-to-acm-certs.html): Use ACM certificates to make SSL connections with Amazon Redshift clusters.

### [Connecting from client tools and code](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-via-client-tools.html)

Learn about third-party tools to connect to your Amazon Redshift data.

### [Connecting with Amazon Redshift RSQL](https://docs.aws.amazon.com/redshift/latest/mgmt/rsql-query-tool.html)

Learn how to query your Amazon Redshift database with RSQL.

- [Getting started with Amazon Redshift RSQL](https://docs.aws.amazon.com/redshift/latest/mgmt/rsql-query-tool-getting-started.html): Download and install Amazon Redshift RSQL.
- [Amazon Redshift RSQL change log](https://docs.aws.amazon.com/redshift/latest/mgmt/rsql-query-tool-changelog.html): This topic details changes in specific versions.
- [Connect to a cluster with Amazon Redshift RSQL](https://docs.aws.amazon.com/redshift/latest/mgmt/rsql-query-tool-starting-tool-connection.html): Connecting to a cluster with Amazon Redshift RSQL.
- [Amazon Redshift RSQL meta commands](https://docs.aws.amazon.com/redshift/latest/mgmt/rsql-query-tool-commands.html): Find a description of Amazon Redshift RSQL meta commands.
- [Amazon Redshift RSQL variables](https://docs.aws.amazon.com/redshift/latest/mgmt/rsql-query-tool-variables.html): Amazon Redshift RSQL variables.
- [Amazon Redshift RSQL error codes](https://docs.aws.amazon.com/redshift/latest/mgmt/rsql-query-tool-error-codes.html): Amazon Redshift RSQL error codes.
- [Amazon Redshift RSQL environment variables](https://docs.aws.amazon.com/redshift/latest/mgmt/rsql-query-tool-environment-variables.html): Amazon Redshift RSQL environment variables.

### [Using an authentication profile to connect to Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-with-authentication-profiles.html)

Use an authentication profile to connect to Amazon Redshift.

- [Creating an authentication profile](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-with-authentication-profiles-creating.html): Learn how to create an authentication profile.
- [Connecting with an authentication profile](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-with-authentication-profiles-using.html): Learn how to connect with an authentication profile.
- [Getting authentication profiles](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-with-authentication-profiles-getting.html): Learn how to get an authentication profile
- [Troubleshooting connection issues in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/troubleshooting-connections.html): Learn about issues about connecting from SQL client tools to Amazon Redshift clusters.

### [Using the Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html)

Access your Amazon Redshift database using the built-in Amazon Redshift Data API.

### [Authorizing access](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-access.html)

Learn how to authorize access to the Amazon Redshift Data API.

- [Configuring IAM permissions](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-iam.html): Learn how to configure IAM permission.
- [Storing credentials in a secret](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-secrets.html): Learn how to store database credentials in AWS Secrets Manager
- [Creating an Amazon VPC endpoint](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-vpc-endpoint.html): Learn how to create an Amazon VPC endpoint for the Data API.
- [Joining database groups](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-dbgroups.html): Learn how to join database groups.
- [Trusted identity propagation](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-trusted-identity-propagation.html): Learn how to use Data API with trusted identity propagation.

### [Calling the Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-calling.html)

Learn how to call the Data API.

- [Passing SQL statements to a data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/pass-sql-statements.html): Learn how to pass SQL statements to an Amazon Redshift data warehouse.
- [List metadata about SQL statements](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-calling-cli-list-statements.html): To list metadata about SQL statements, use the aws redshift-data list-statements AWS CLI command.
- [Describe metadata about a SQL statement](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-calling-cli-describe-statement.html): To get descriptions of metadata for a SQL statement, use the aws redshift-data describe-statement AWS CLI command.
- [Fetch the results of a SQL statement](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-calling-cli-get-statement-result.html): To fetch the result from a SQL statement that ran, use the redshift-data get-statement-result or redshift-data get-statement-result-v2 AWS CLI command.
- [Describe a table](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-calling-cli-describe-table.html): To get metadata that describes a table, use the aws redshift-data describe-table AWS CLI command.
- [List databases in a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-calling-cli-list-databases.html): To list the databases in a cluster, use the aws redshift-data list-databases AWS CLI command.
- [List schemas in a database](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-calling-cli-list-schemas.html): Learn how to list schemas in a database.
- [List tables in a database](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-calling-cli-list-tables.html): Learn how to list tables in a database.
- [Troubleshooting Data API issues](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-troubleshooting.html): Troubleshoot Amazon Redshift Data API issues.
- [Scheduling Data API operations with Amazon EventBridge](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-calling-event-bridge.html): Perform scheduling for the Amazon Redshift Data API with Amazon EventBridge.

### [Monitoring the Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-monitoring.html)

Learn about monitoring the Data API.

- [Monitoring Data API events in Amazon EventBridge](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-monitoring-events.html): Find a list of the monitoring events for the Data API with Amazon EventBridge.
- [Using AWS KMS with the Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-kms.html): Learn how to use AWS KMS with the Data API
- [Using Amazon Sagemaker Unified Studio](https://docs.aws.amazon.com/redshift/latest/mgmt/sagemaker-unified-studio.html): Learn how to use Sagemaker Unified Studio to query databases.


## [Parameter groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html)

- [Workload management](https://docs.aws.amazon.com/redshift/latest/mgmt/workload-mgmt-config.html): Use workload management (WLM) to query queues and query routing in Amazon Redshift.
- [Creating a parameter group](https://docs.aws.amazon.com/redshift/latest/mgmt/parameter-group-create.html): Create parameter groups using the Amazon Redshift console.
- [Modifying a parameter group](https://docs.aws.amazon.com/redshift/latest/mgmt/parameter-group-modify.html): You can view any of your parameter groups to see a summary of the values for parameters and workload management (WLM) configuration.
- [Creating a query monitoring rule](https://docs.aws.amazon.com/redshift/latest/mgmt/parameter-group-modify-qmr-console.html): You can use the Amazon Redshift console to create and modify WLM query monitoring rules.
- [Deleting a parameter group](https://docs.aws.amazon.com/redshift/latest/mgmt/parameter-group-delete.html): You can delete a parameter group if you no longer need it and it is not associated with any clusters.


## [Integrate with an AWS Partner](https://docs.aws.amazon.com/redshift/latest/mgmt/partner-integration.html)

- [Loading data with AWS partners](https://docs.aws.amazon.com/redshift/latest/mgmt/partner-integration-data-load.html): Learn how to load data with AWS partners


## [Reserved nodes](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html)

- [Purchasing a reserved node](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-offering-console.html): Learn how to purchase and view reserved node offerings.


## [Security](https://docs.aws.amazon.com/redshift/latest/mgmt/iam-redshift-user-mgmt.html)

### [Data protection](https://docs.aws.amazon.com/redshift/latest/mgmt/security-data-protection.html)

Keep your data protected through Amazon Redshift with objects stored redundantly on multiple devices across multiple facilities.

### [Data encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/security-encryption.html)

Use data encryption to provide added security for your Amazon Redshift data objects stored in your databases.

### [Encryption at rest](https://docs.aws.amazon.com/redshift/latest/mgmt/security-server-side-encryption.html)

How to protect data at rest with server-side encryption in Amazon Redshift.

### [Database encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html)

Set up database encryption on your Amazon Redshift clusters to help protect your data.

- [Changing cluster encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/changing-cluster-encryption.html): Encrypt an Amazon Redshift cluster.
- [Migrating to an HSM-encrypted cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/migrating-to-an-encrypted-cluster.html): To migrate an unencrypted cluster to a cluster encrypted using a hardware security module (HSM), you create a new encrypted cluster and move your data to the new cluster.
- [Rotating encryption keys](https://docs.aws.amazon.com/redshift/latest/mgmt/manage-key-rotation-console.html): Rotate encryption keys by using the Amazon Redshift console.

### [Encryption in transit](https://docs.aws.amazon.com/redshift/latest/mgmt/security-encryption-in-transit.html)

How to protect Amazon Redshift data in transit.

- [VPC encryption controls](https://docs.aws.amazon.com/redshift/latest/mgmt/security-vpc-encryption-controls.html): Amazon Redshift supports VPC encryption controls, a security feature that helps you enforce encryption in transit for all traffic within and across VPCs in a Region.
- [Key management](https://docs.aws.amazon.com/redshift/latest/mgmt/security-key-management.html): How to protect Amazon Redshift data with key management.
- [Data tokenization](https://docs.aws.amazon.com/redshift/latest/mgmt/data-tokenization.html): Learn how to use data tokenization with Amazon Redshift.
- [Routing internetwork traffic](https://docs.aws.amazon.com/redshift/latest/mgmt/network-isolation.html): How to route traffic through known and private network routes for Amazon Redshift.

### [Identity and access management](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-authentication-access-control.html)

Protect Amazon Redshift resources using AWS Identity and Access Management (IAM).

- [Overview of managing access](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html): Use permission policies to control access in Amazon Redshift.
- [Using identity-based policies (IAM policies)](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html): Find examples of permission policies attached to IAM users, groups, or roles to access Amazon Redshift.

### [Native identity provider (IdP) federation](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-native-idp.html)

Native identity provider (IdP) federation for Amazon Redshift.

- [Setting up the identity provider on Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-native-idp-setup.html): Setting up the identity provider on Amazon Redshift.
- [Automatically creating roles for identity providers](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-native-idp-autocreate.html): Learn how to automatically create Amazon Redshift roles for identity providers.

### [Single sign-on experience](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html)

Connect Redshift with AWS IAM Identity Center to give users a single sign-on experience.

- [Setting up AWS IAM Identity Center integration with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect-console.html): Setting up integration with Amazon Redshift.
- [Automatically creating roles for AWS IAM Identity Center](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-sso-autocreate.html): Learn how to automatically create Amazon Redshift roles for identity providers.
- [Amazon S3 Access Grants](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-sso-s3idc.html): Control access to Amazon S3 using IAM Identity Center.
- [Querying data through AWS Lake Formation](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-analytics-connecting-steps.html): Using AWS Lake Formation makes it easier to centrally govern and secure your data lake, and to provide data access.
- [Integrating your application or tool with OAuth using a trusted token issuer](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect-oauth.html): Integrating your application or tool with OAuth using a trusted token issuer.
- [Troubleshooting connections](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect-troubleshooting.html): Troubleshooting connections.
- [Using service-linked roles](https://docs.aws.amazon.com/redshift/latest/mgmt/using-service-linked-roles.html): Learn how to use service-linked roles to give Amazon Redshift access to resources in your AWS account.

### [Using IAM authentication to generate database user credentials](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-user-credentials.html)

To better manage the access your users have to your Amazon Redshift database, you can use AWS Identity and Access Management (IAM) to generate temporary database credentials.

- [Creating temporary IAM credentials](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-iam-credentials-steps.html): Generate temporary database user credentials based on AWS Identity and Access Management (IAM) for Amazon Redshift.

### [Options for providing IAM credentials](https://docs.aws.amazon.com/redshift/latest/mgmt/options-for-providing-iam-credentials.html)

Use different ways to provide IAM (IAM) credentials for JDBC or OBDBC connections for Amazon Redshift.

- [Generating database credentials for an IAM identity](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-iam-credentials-cli-api.html): Use the AWS CLI or Amazon Redshift API to generate IAM (IAM) database credentials for Amazon Redshift.

### [Setting up JDBC or ODBC single sign-on authentication](https://docs.aws.amazon.com/redshift/latest/mgmt/setup-azure-ad-identity-provider.html)

Learn how to set up JDBC or ODBC single sign-on authentication with AD FS.

- [AD FS](https://docs.aws.amazon.com/redshift/latest/mgmt/setup-identity-provider-adfs.html): Learn how to set up JDBC or ODBC single sign-on authentication with AD FS.
- [Azure](https://docs.aws.amazon.com/redshift/latest/mgmt/setup-identity-provider-azure.html): Learn how to set up JDBC or ODBC single sign-on authentication with Azure.
- [Ping Identity](https://docs.aws.amazon.com/redshift/latest/mgmt/setup-identity-provider-ping.html): Learn how to set up JDBC or ODBC single sign-on authentication with Ping Identity.
- [Okta](https://docs.aws.amazon.com/redshift/latest/mgmt/setup-identity-provider-okta.html): Learn how to set up JDBC or ODBC single sign-on authentication with Okta.

### [Authorizing access to AWS services](https://docs.aws.amazon.com/redshift/latest/mgmt/authorizing-redshift-service.html)

Authorize Amazon Redshift to access other AWS services on your behalf.

- [Restricting access to IAM roles](https://docs.aws.amazon.com/redshift/latest/mgmt/authorizing-redshift-service-database-users.html): Learn how to restrict access to an IAM role.
- [Restricting an IAM role to an AWS Region](https://docs.aws.amazon.com/redshift/latest/mgmt/authorizing-redshift-service-regions.html): Learn how to restrict an IAM role to an AWS Region.
- [Chaining IAM roles](https://docs.aws.amazon.com/redshift/latest/mgmt/authorizing-redshift-service-chaining-roles.html): Learn how to chain an IAM role

### [Authorizing operations using IAM roles](https://docs.aws.amazon.com/redshift/latest/mgmt/copy-unload-iam-role.html)

Create IAM policies to authorize Amazon Redshift COPY, UNLOAD, CREATE EXTERNAL FUNCTION, and CREATE EXTERNAL SCHEMA operations using IAM roles.

- [Associating IAM roles with clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/copy-unload-iam-role-associating-with-clusters.html): Associate an IAM role with a cluster.
- [Creating an IAM role as default](https://docs.aws.amazon.com/redshift/latest/mgmt/default-iam-role.html): Create a default IAM role through the Amazon Redshift console that has a policy with permissions to run SQL commands.
- [Using a federated identity to manage access to local resources and external tables](https://docs.aws.amazon.com/redshift/latest/mgmt/authorization-fas-spectrum.html): Learn how to use a federated identity to manage access to local resources and external tables.

### [Managing admin passwords](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-secrets-manager-integration.html)

Manage your admin credentials using AWS Secrets Manager

- [Retrieving the ARN of the secret](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-secrets-manager-integration-retrieving-secret.html): Learn how to retrieve the ARN of the secret.
- [Creating a secret for database connection credentials](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-secrets-manager-integration-create.html): Learn how to create a secret for database connection credentials.

### [Logging and monitoring](https://docs.aws.amazon.com/redshift/latest/mgmt/security-incident-response.html)

Work with tools for monitoring and responding to incidents for Amazon Redshift.

### [Database audit logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html)

Monitor the database for security and troubleshooting purposes, called database auditing, with Amazon Redshift logs of connections and activities.

- [Enabling audit logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing-console.html): Configure Amazon Redshift to export audit log data.
- [Secure logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing-secure-logging.html): Amazon Redshift automatically masks potentially sensitive system table fields when logging query metadata.
- [Logging with CloudTrail](https://docs.aws.amazon.com/redshift/latest/mgmt/logging-with-cloudtrail.html): Describes logging options in Amazon Redshift.
- [Compliance validation](https://docs.aws.amazon.com/redshift/latest/mgmt/security-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/redshift/latest/mgmt/security-disaster-recovery-resiliency.html): Work with AWS architecture for data redundancy in addition to specific Amazon Redshift services for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/redshift/latest/mgmt/security-network-isolation.html): Learn how Amazon Redshift isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/redshift/latest/mgmt/security-vulnerability-analysis-and-management.html): Learn about the customer responsibility regarding updates and patches for Amazon Redshift.


## [Using Identity Center authentication](https://docs.aws.amazon.com/redshift/latest/mgmt/identity-center-authentication.html)

- [Troubleshooting](https://docs.aws.amazon.com/redshift/latest/mgmt/identity-center-auth-errors.html): Troubleshoot Identity Center authentication issues.


## [Networking tasks](https://docs.aws.amazon.com/redshift/latest/mgmt/networking-tasks.html)

### [Custom domain names for client connections](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-connection-CNAME.html)

Using a custom domain name for client connections.

- [Registering a domain name](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-connection-CNAME-certificates.html): Learn how to register a domain name.
- [Requesting a certificate for a domain name](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-connection-CNAME-security.html): Amazon Redshift or Amazon Redshift Serverless require a validated Secure Sockets Layer (SSL) certificate for a custom endpoint to keep communication secure and to verify ownership of the domain name.
- [Configuring a custom domain](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-connection-CNAME-create-custom-domain.html): Learn how to configure a custom domain.
- [Connecting to your provisioned cluster or workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-connection-CNAME-client.html): Learn how to connect to your provisioned cluster or .
- [Renaming a cluster that has a custom domain assigned](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-connection-CNAME-rename-cluster.html): Learn how to rename a cluster that has a custom domain assigned.
- [Describing custom domain associations](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-connection-CNAME-describe-api.html): Learn how to describe custom domain associations.
- [Associating a custom domain with a different certificate](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-connection-CNAME-change-api.html): Learn how to associate the custom domain with a different certificate.
- [Deleting a custom domain](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-connection-CNAME-delete-api.html): Learn how to delete a custom domain.

### [Redshift-managed VPC endpoints](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-cross-vpc.html)

Learn about and walk through the ways to create Redshift-managed VPC endpoints in Amazon Redshift.

- [Granting access to a VPC](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-cross-vpc-console-grantor.html): Learn how to grant access to a VPC in another account.
- [Creating a Redshift-managed VPC endpoint](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-cross-vpc-console-grantee.html): Learn how to create a Redshift-managed VPC endpoint.

### [Redshift resources in a VPC](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-vpc.html)

Manage your Redshift resources in a virtual private cloud (VPC) based on the Amazon VPC service.

- [Creating a cluster or workgroup in a VPC](https://docs.aws.amazon.com/redshift/latest/mgmt/getting-started-cluster-in-vpc.html): Create your Amazon Redshift resources in a virtual private cloud (VPC).
- [VPC security groups](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-vpc-security-groups.html): Manage virtual private cloud (VPC) security groups.
- [Configuring security settings for a cluster or workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-security-group-public-private.html): This topic helps you configure your security groups to route and receive network traffic appropriately.

### [Subnets for Redshift resources](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html)

Provides the basics of creating and managing subnets for Redshift.

- [Creating a cluster subnet group](https://docs.aws.amazon.com/redshift/latest/mgmt/create-cluster-subnet-group.html): Create subnets for Redshift resources using the console.
- [Modifying a cluster subnet group](https://docs.aws.amazon.com/redshift/latest/mgmt/modify-cluster-subnet-group.html): Modify subnets for Redshift resources using the console.
- [Deleting a cluster subnet group for a provisioned cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/delete-cluster-subnet-group.html): Delete subnets for Redshift resources using the console.
- [Blocking public access to VPCs and subnets](https://docs.aws.amazon.com/redshift/latest/mgmt/block-public-access.html): VPC Block Public Access (BPA) is a centralized security feature that you can use to block resources in VPCs and subnets that you own in an AWS Region from reaching the internet or being reached from the internet through internet gateways and egress-only internet gateways.

### [Controlling network traffic with enhanced VPC routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html)

Use enhanced VPC routing with Amazon Redshift and Amazon Redshift Serverless to force all COPY and UNLOAD traffic between your provisioned cluster or workgroup and your data repositories through your virtual private cloud (VPC).

- [Controlling database traffic with VPC endpoints](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-working-with-endpoints.html): Create an Amazon Redshift connection with a VPC endpoint.
- [Turning on enhanced VPC routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-enabling-cluster.html): Turn on enhanced VPC routing.
- [Accessing Amazon S3 buckets with Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/mgmt/spectrum-enhanced-vpc.html): You can't use enhanced VPC routing with Redshift Spectrum.


## [Events](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-events.html)

- [Cluster event notification subscriptions](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications-subscribe.html): Understand subscriptions to event notifications
- [Creating an event notification subscription](https://docs.aws.amazon.com/redshift/latest/mgmt/event-subscribe.html): Create and manage event notification subscriptions for a specified cluster.
- [Provisioned cluster event notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html): Get notification of Amazon Redshift events, using Amazon SNS, by creating event subscriptions.
- [Amazon Redshift Serverless event notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-event-notifications-eventbridge.html): Amazon Redshift Serverless event notifications with Amazon EventBridge.
- [Zero-ETL integration event notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/integration-event-notifications.html): Zero-ETL integration event notifications with Amazon EventBridge.


## [Tag resources](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-tagging.html)

- [Managing resource tags](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-mgmt-tagging-console.html): Manage resource tags in Amazon Redshift.


## [Code examples](https://docs.aws.amazon.com/redshift/latest/mgmt/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/redshift/latest/mgmt/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon Redshift with AWS SDKs.

- [Hello Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/example_redshift_Hello_section.html): Hello Amazon Redshift
- [Learn the basics](https://docs.aws.amazon.com/redshift/latest/mgmt/example_redshift_Scenario_section.html): Learn the basics of Amazon Redshift with an AWS SDK

### [Actions](https://docs.aws.amazon.com/redshift/latest/mgmt/service_code_examples_actions.html)

The following code examples show how to use Amazon Redshift with AWS SDKs.

- [CreateCluster](https://docs.aws.amazon.com/redshift/latest/mgmt/example_redshift_CreateCluster_section.html): Use CreateCluster with an AWS SDK or CLI
- [DeleteCluster](https://docs.aws.amazon.com/redshift/latest/mgmt/example_redshift_DeleteCluster_section.html): Use DeleteCluster with an AWS SDK or CLI
- [DescribeClusters](https://docs.aws.amazon.com/redshift/latest/mgmt/example_redshift_DescribeClusters_section.html): Use DescribeClusters with an AWS SDK or CLI
- [DescribeStatement](https://docs.aws.amazon.com/redshift/latest/mgmt/example_redshift_DescribeStatement_section.html): Use DescribeStatement with an AWS SDK
- [ExecuteStatement](https://docs.aws.amazon.com/redshift/latest/mgmt/example_redshift_ExecuteStatement_section.html): Use ExecuteStatement with an AWS SDK
- [GetStatementResult](https://docs.aws.amazon.com/redshift/latest/mgmt/example_redshift_GetStatementResult_section.html): Use GetStatementResult with an AWS SDK
- [ListDatabases](https://docs.aws.amazon.com/redshift/latest/mgmt/example_redshift_ListDatabases_section.html): Use ListDatabases with an AWS SDK
- [ModifyCluster](https://docs.aws.amazon.com/redshift/latest/mgmt/example_redshift_ModifyCluster_section.html): Use ModifyCluster with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/redshift/latest/mgmt/service_code_examples_scenarios.html)

The following code examples show how to use Amazon Redshift with AWS SDKs.

- [Create a web application to track Amazon Redshift data](https://docs.aws.amazon.com/redshift/latest/mgmt/example_cross_RedshiftDataTracker_section.html): Create an Amazon Redshift item tracker
