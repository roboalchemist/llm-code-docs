# Source: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/llms.txt

# Amazon OpenSearch Service Developer Guide

- [What is Amazon OpenSearch Service?](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
- [Setting up](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/setting-up.html)
- [OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/dashboards.html)
- [Security Analytics](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-analytics.html)
- [Amazon OpenSearch Service rename](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html)
- [Troubleshooting](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/handling-errors.html)
- [Document history](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/release-notes.html)
- [AWS Glossary](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/glossary.html)

## [Getting started](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html)

- [Create a domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsgcreate-domain.html): Set up your first Amazon OpenSearch Service domain to start working with search and analytics capabilities.
- [Upload data for indexing](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsgupload-data.html): Index your first documents in Amazon OpenSearch Service using HTTP requests to make your data searchable.
- [Search documents](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsgsearch.html): Query your indexed data in Amazon OpenSearch Service using the search API to find relevant information quickly.
- [Delete a domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsgdeleting.html): Remove an Amazon OpenSearch Service domain when you no longer need it to avoid incurring unnecessary charges.


## [Amazon OpenSearch Ingestion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html)

- [Key concepts](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion-process.html): Understand the fundamental concepts of Amazon OpenSearch Ingestion for data processing and loading.
- [Limitations](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion-limitations.html): Learn about the current limitations and constraints when using Amazon OpenSearch Ingestion.
- [Scaling pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion-scaling.html): Configure and optimize scaling for your Amazon OpenSearch Ingestion pipelines to handle varying workloads.

### [Setting up roles and users](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-security-overview.html)

Configure the required roles to create Amazon OpenSearch Ingestion pipelines.

- [Granting pipelines access to domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-domain-access.html): Learn how to provide pipelines access to OpenSearch Service domains.
- [Granting pipelines access to collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-collection-access.html): Learn how to provide pipelines access to OpenSearch Serverless collections.

### [Getting started with OpenSearch Ingestion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-getting-started-tutorials.html)

Learn how to get started with Amazon OpenSearch Ingestion.

- [Tutorial: Ingest data into a domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-get-started.html): Get started creating pipelines and ingesting data in Amazon OpenSearch Ingestion.
- [Tutorial: Ingest data into a collection](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-serverless-get-started.html): Get started creating pipelines and ingesting data in OpenSearch Serverless.
- [Pipeline features](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-features-overview.html): Learn about the most commonly used features in Amazon OpenSearch Ingestion.

### [Creating pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html)

Learn how to create OpenSearch Ingestion pipelines in Amazon OpenSearch Service.

- [Working with blueprints](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-blueprint.html): Use pipeline blueprints to quickly create and configure Amazon OpenSearch Ingestion pipelines.
- [Viewing pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/list-pipeline.html): Learn how to view OpenSearch Ingestion pipelines in Amazon OpenSearch Service.
- [Updating pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/update-pipeline.html): Learn how to create and manage OpenSearch Ingestion pipelines in Amazon OpenSearch Service.

### [Managing pipeline costs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline--stop-start.html)

Stop and start an Amazon OpenSearch Ingestion pipeline.

- [Stopping a pipeline](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline--stop.html): Learn how to start and manage Amazon OpenSearch Ingestion pipelines through the AWS Management Console.
- [Starting a pipeline](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline--start.html): Learn about starting an Amazon OpenSearch Ingestion pipeline and how to use this feature in Amazon OpenSearch Service.
- [Deleting pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/delete-pipeline.html): Learn how to delete OpenSearch Ingestion pipelines in Amazon OpenSearch Service.
- [Supported plugins and options](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-config-reference.html): Explore the available sources, processors, and sinks for building effective data pipelines in Amazon OpenSearch Ingestion.

### [Integrating pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client.html)

Configure client applications to send data to Amazon OpenSearch Ingestion pipelines for efficient data processing.

### [Atlassian Services](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-atlassian.html)

Configure Amazon OpenSearch Ingestion pipelines to process data from Atlassian Jira and Confluence.

- [Connecting an Amazon OpenSearch Ingestion pipeline to Atlassian Jira or Confluence using OAuth 2.0](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-atlassian-OAuth2-setup.html): Learn how to connect your Amazon OpenSearch Ingestion pipeline to Atlassian Jira or Confluence using OAuth 2.0 authentication credentials.

### [Amazon Aurora](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-aurora.html)

You can use an OpenSearch Ingestion pipeline with Amazon Aurora to export existing data and stream changes (such as create, update, and delete) to Amazon OpenSearch Service domains and collections.

- [Aurora MySQL](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/aurora-mysql.html): Complete the following steps to configure an OpenSearch Ingestion pipeline with Amazon Aurora for Aurora MySQL.
- [Aurora PostgreSQL](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/aurora-PostgreSQL.html): Complete the following steps to configure an OpenSearch Ingestion pipeline with Amazon Aurora for Aurora PostgreSQL.
- [Amazon DynamoDB](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-ddb.html): Stream table events from Amazon Amazon DynamoDB to OpenSearch Service using ingestion pipelines to enable real-time search and analytics on your NoSQL data.
- [Amazon DocumentDB](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-docdb.html): Configure an OpenSearch Ingestion pipeline to stream document changes from Amazon DocumentDB to OpenSearch Service for real-time data processing.
- [Confluent Cloud Kafka](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-confluent-kafka.html): Stream data from Confluent Cloud Kafka clusters to OpenSearch Service using ingestion pipelines with public or private network configurations.
- [Amazon MSK](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-msk.html): Configure Amazon OpenSearch Ingestion pipelines to process data from Amazon MSK.

### [Amazon RDS](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-rds.html)

You can use an OpenSearch Ingestion pipeline with Amazon RDS to export existing data and stream changes (such as create, update, and delete) to Amazon OpenSearch Service domains and collections.

- [RDS for MySQL](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rds-mysql.html): Complete the following steps to configure an OpenSearch Ingestion pipeline with Amazon RDS for RDS for MySQL.
- [RDS for PostgreSQL](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rds-PostgreSQL.html): Complete the following steps to configure an OpenSearch Ingestion pipeline with Amazon RDS for RDS for PostgreSQL.
- [Amazon S3](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-s3.html): Using an OpenSearch Ingestion pipeline with Amazon S3 to optimize your search operations and data management.

### [Amazon Security Lake](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-security-lake.html)

Using an OpenSearch Ingestion pipeline with Amazon Security Lake to optimize your search operations and data management.

- [Amazon Security Lake as a source](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-source-security-lake.html): Connect Amazon OpenSearch Ingestion pipelines to Security Lake for data processing.
- [Amazon Security Lake as a sink](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-sink-security-lake.html): Using an OpenSearch Ingestion pipeline with Amazon Security Lake as a sink to optimize your search operations and data management.
- [Fluent Bit](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-fluentbit.html): This sample Fluent Bit configuration file sends log data from Fluent Bit to an OpenSearch Ingestion pipeline.
- [Fluentd](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-fluentd.html): Fluentd is an open-source data collection ecosystem that provides SDKs for different languages and sub-projects like Fluent Bit.
- [ML offline batch inference](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-clients-ml-commons-batch.html): Amazon OpenSearch Ingestion (OSI) pipelines support machine learning (ML) offline batch inference processing to efficiently enrich large volumes of data at low cost.
- [OpenTelemetry Collector](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-otel.html): You can use the OpenTelemetry Collector to ingest logs, traces, and metrics into OpenSearch Ingestion pipelines.
- [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-prometheus.html): Configure Amazon OpenSearch Ingestion pipelines to send metrics data to Amazon Managed Service for Prometheus for monitoring and alerting.
- [Self-managed Kafka](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-self-managed-kafka.html): Stream data from self-managed Kafka clusters to OpenSearch Service using ingestion pipelines for real-time analytics and visualization.
- [Self-managed OpenSearch clusters](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-self-managed-opensearch.html): Migrate data from self-managed OpenSearch or Elasticsearch clusters to Amazon OpenSearch Service using ingestion pipelines with public or VPC configurations.
- [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-kinesis.html): Stream data from Amazon Kinesis Data Streams to Amazon OpenSearch Service using ingestion pipelines for real-time analytics and visualization.
- [AWS Lambda](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-lambda.html): Use the AWS Lambda processor to enrich data from any source or destination supported by OpenSearch Ingestion using custom code.
- [Migrating data between domains and collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-opensearch-service-pipeline.html): Learn how to configure OpenSearch Ingestion pipelines to migrate data between Amazon OpenSearch Service domains or OpenSearch Serverless VPC collections.
- [Managing pipelines with the AWS SDKs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-sdk.html): Programmatically create and manage Amazon OpenSearch Ingestion pipelines using the AWS SDKs for automated data processing.

### [Security in OpenSearch Ingestion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-security-model.html)

Configure Amazon OpenSearch Ingestion to meet your security and compliance objectives.

- [Configuring VPC access for pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-security.html): Learn how to secure your pipelines using a virtual private cloud.
- [Configuring pipelines for cross-account ingestion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-account-pipelines.html): Learn how to configure VPCs to share pipelines across AWS accounts.
- [Identity and Access Management](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-ingestion.html): How to authenticate requests and manage access to your OpenSearch Ingestion resources.
- [Monitoring with CloudTrail](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-logging-using-cloudtrail.html): Learn about logging Amazon OpenSearch Ingestion with AWS CloudTrail.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-access-apis-using-privatelink.html): How to access OpenSearch Ingestion APIs using AWS PrivateLink.
- [Tagging pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-pipeline.html): Create, view, edit, and delete tags on pipelines in Amazon OpenSearch Ingestion.

### [Logging and monitoring](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-pipelines.html)

Monitor your Amazon OpenSearch Ingestion pipelines using Amazon CloudWatch metrics and logs to ensure optimal performance.

- [Monitoring pipeline logs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-pipeline-logs.html): Learn about monitoring pipeline logs to optimize your search operations and data management.
- [Monitoring pipeline metrics](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-pipeline-metrics.html): Track and analyze performance metrics for your Amazon OpenSearch Ingestion pipelines.
- [Best practices](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-best-practices.html): Learn about best practices for configuring and managing Amazon OpenSearch Ingestion pipelines.


## [Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.html)

### [What is Amazon OpenSearch Serverless?](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html)

Discover Amazon OpenSearch Serverless, a fully managed, on-demand, auto-scaling configuration for OpenSearch Service.

- [Comparing OpenSearch Service and OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-comparison.html): Compare the features and capabilities of Amazon OpenSearch Service and Amazon OpenSearch Serverless to choose the right option.
- [Tutorial: Getting started with OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-getting-started.html): Use Amazon OpenSearch Serverless to quickly create and configure a test search collection, index data, and send search requests to your collection.

### [Collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collections.html)

Learn how to create, configure, and manage collections in Amazon OpenSearch Service.

### [Managing collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html)

Create and manage OpenSearch Serverless collections to store, search, and analyze your data without managing infrastructure or capacity planning.

- [Configuring permissions for collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collection-permissions.html): OpenSearch Serverless uses the following AWS Identity and Access Management (IAM) permissions for creating and managing collections.
- [Automatic semantic enrichment for Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-semantic-enrichment.html): Learn how automatic semantic enrichment enhances search capabilities in OpenSearch Serverless by understanding query intent and context.

### [Creating collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-create.html)

You can use the console or the AWS CLI to create a serverless collection.

- [Create a collection (console)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-create-console.html): Use the procedures in this section to create a collection by using the AWS Management Console.
- [Create a collection (CLI)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-create-cli.html): Use the procedures in this section to create an OpenSearch Serverless collection using the AWS CLI.
- [Accessing OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-dashboards.html): After you create a collection with the AWS Management Console, you can navigate to the collection's OpenSearch Dashboards URL.
- [Viewing collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-list.html): You can view the existing collections in your AWS account on the Collections tab of the Amazon OpenSearch Service console.
- [Deleting collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-delete.html): Deleting a collection deletes all data and indexes in the collection.
- [Working with vector search collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-search.html): In this tutorial, create and configure a test vector search collection.
- [Using data lifecycle policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html): Configure data lifecycle policies for OpenSearch Serverless time series collections to automatically manage data retention and deletion based on age.
- [Managing collections with the AWS SDKs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-sdk.html): Integrate OpenSearch Serverless with your applications using AWS SDKs to programmatically create and manage collections and security policies.
- [Creating collections with CloudFormation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-cfn.html): Automate the creation and management of OpenSearch Serverless resources using AWS CloudFormation templates for infrastructure as code deployments.
- [Backing up collections using snapshots](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-snapshots.html): Snapshots are point-in-time backups of your Amazon OpenSearch Serverless collections that provide disaster recovery capabilities.

### [Collection groups](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collection-groups.html)

Organize and share compute resources across multiple OpenSearch Serverless collections

- [Collection group capacity limits](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/collection-groups-capacity-limits.html): Set minimum and maximum OCU limits at the collection group level to control resource allocation and optimize costs.
- [Encryption and KMS keys in collection groups](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/collection-groups-kms-keys.html): Configure encryption keys for collections in collection groups using security policies or the CreateCollection API.
- [Create collection groups](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collection-groups-procedures.html): Create OpenSearch Serverless collection groups to store, search, and analyze your data without managing infrastructure or capacity planning.
- [Manage collection groups](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/manage-collection-group.html): Use the following procedures to update collection group settings, move collections between groups, monitor collection group details, and delete collection groups.
- [Managing capacity limits](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-scaling.html): Configure capacity limits for OpenSearch Serverless to control resource allocation and optimize costs while maintaining performance for your workloads.
- [Ingesting data into collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-clients.html): Explore various methods to ingest data into OpenSearch Serverless collections including direct API calls, ingestion pipelines, and AWS service integrations.

### [Configure Machine Learning](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-configure-machine-learning.html)

Use machine learning on Amazon OpenSearch Serverless.

- [Unsupported APIs and features](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-machine-learning-unsupported-features.html): Learn about machine learning API features that are not available on Amazon OpenSearch Serverless, including local model functionality, training APIs, prediction algorithms, agents, and inference processors.
- [Configure Neural and Hybrid Search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-configure-neural-search.html): Configure Neural and Hybrid Search on Amazon OpenSearch Serverless.
- [Configure Workflows](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-configure-workflows.html): Using Workflows on Amazon OpenSearch Serverless.

### [Security in OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-security.html)

Configure Amazon OpenSearch Serverless to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your OpenSearch Serverless resources.

### [Getting started with security](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-tutorials.html)

Get started with configuring security policies in Amazon OpenSearch Serverless using the AWS Management Console or the AWS CLI.

- [Tutorial: Getting started with security (console)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg-serverless.html): Use Amazon OpenSearch Serverless to quickly create and configure a test collection, index data, and send search requests to your collection.
- [Tutorial: Getting started with security (CLI)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg-serverless-cli.html): Follow this step-by-step guide to getting started with security in Amazon OpenSearch Serverless using the AWS CLI.

### [Identity and Access Management](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-serverless.html)

How to authenticate requests and manage access to your OpenSearch Serverless resources.

- [IAM Identity Center support for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-iam-identity-center.html): Configure AWS Identity and Access Management integration with OpenSearch Serverless to enable single sign-on authentication for secure access to your collections.
- [Encryption](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html): Protect your OpenSearch Serverless data with encryption at rest and in transit using AWS KMS keys or service-owned keys for enhanced security.
- [Network access](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html): Configure network policies for OpenSearch Serverless to control access to your collections through public endpoints or private VPC connections.

### [FIPS compliance](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fips-compliance-opensearch-serverless.html)

Learn how Amazon OpenSearch Serverless supports Federal Information Processing Standards (FIPS) compliance requirements, and provides guidance on configuring FIPS-compliant endpoints.

- [Troubleshoot FIPS Private Hosted Zones](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-fips-endpoint-issues.html): Learn how to diagnose and fix connectivity issues with FIPS endpoints by configuring private hosted zones in Amazon RouteÂ 53 for your Amazon OpenSearch Serverless collections.
- [Data access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html): Configure fine-grained data access policies for OpenSearch Serverless collections to control who can access your data and what actions they can perform.
- [Data plane VPC endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html): Create a data plane VPC endpoint to privately access Amazon OpenSearch Serverless collection data from your VPC.
- [Control plane VPC endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc-cp.html): Create a control plane AWS PrivateLink endpoint to privately access Amazon OpenSearch Serverless API operations from your VPC.
- [SAML authentication](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html): Configure SAML authentication for OpenSearch Serverless to enable secure single sign-on access to your collections using your existing identity provider.
- [Compliance validation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.

### [Tagging collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html)

Create, view, edit, and delete tags on collections in Amazon OpenSearch Serverless.

- [Tagging collections (console)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection-console.html): Apply tags to Amazon OpenSearch Service collections using the AWS Management Console.
- [Tagging collections (AWS CLI)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection-cli.html): Learn about tagging collections using the AWS CLI and how to use this feature in Amazon OpenSearch Service.
- [Supported operations and plugins](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-genref.html): Discover the OpenSearch plugins and API operations supported in OpenSearch Serverless to optimize your search and analytics implementations.

### [Monitoring OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-monitoring.html)

Monitor Amazon OpenSearch Serverless to maintain reliability, availability, and performance.

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-cloudwatch.html): Monitoring OpenSearch Serverless with Amazon CloudWatch to optimize your search operations and data management.
- [Monitoring with CloudTrail](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/logging-using-cloudtrail.html): Learn about logging OpenSearch Serverless with AWS CloudTrail.
- [Monitoring with EventBridge](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-monitoring-events.html): Manage OpenSearch Serverless events with Amazon EventBridge.


## [Creating and managing domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html)

- [Automatic semantic enrichment](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/opensearch-semantic-enrichment.html): Learn how automatic semantic enrichment enhances search capabilities in Amazon OpenSearch Service managed domains by understanding query intent and context.
- [Configuration changes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html): Understand how Amazon OpenSearch Service uses blue/green deployments to safely implement configuration changes to your domains.
- [Service software updates](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html): Manage and apply service software updates to keep your Amazon OpenSearch Service domains secure and up-to-date with the latest features.
- [Off-peak windows](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html): Configure daily off-peak windows to schedule service updates and optimizations during low-traffic periods for your OpenSearch domains.
- [Notifications](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-notifications.html): Understand and manage notifications.
- [Configuring a multi-AZ domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html): Distribute nodes across multiple Availability Zones to prevent data loss and minimize downtime in Amazon OpenSearch Service.
- [VPC support](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html): Learn how to launch your OpenSearch Service domain within a VPC.

### [Creating index snapshots](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-snapshots.html)

Learn how to create, restore, and manage Amazon OpenSearch Service snapshots.

- [Registering a manual snapshot repository](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-snapshot-registerdirectory.html): Register an Amazon S3 bucket as a snapshot repository to store and manage backups of your OpenSearch Service domain data.
- [Taking manual snapshots](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-snapshot-create.html): Create point-in-time backups of your OpenSearch Service domain to protect your data and enable migration between domains.
- [Restoring snapshots](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-snapshot-restore.html): Recover your OpenSearch Service domain data from automated or manual snapshots to restore indexes after data loss or migration.

### [Automating snapshots with Snapshot Management](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-snapshot-mgmt.html)

Configure Snapshot Management policies to automate the creation and deletion of snapshots for groups of indexes on a schedule.

- [Configure permissions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sm-security.html): Set up the necessary security roles and permissions to enable users to manage snapshots in your OpenSearch Service domain.

### [Upgrading domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/version-migration.html)

Learn how to upgrade an Amazon OpenSearch Service domain to a newer OpenSearch or Elasticsearch version.

- [Upgrading a domain (console)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/starting-upgrades.html): Learn how to upgrade your Amazon OpenSearch Service domain to a newer version using the AWS Management Console.
- [Upgrading a domain (CLI)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/starting-upgrades-cli.html): Use AWS CLI commands to check compatibility, initiate upgrades, and monitor upgrade status for your OpenSearch Service domains.
- [Upgrading a domain (SDK)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/starting-upgrades-sdk.html): Automate OpenSearch Service domain upgrades using AWS SDK code examples with Python to check eligibility and monitor progress.
- [Using a snapshot to migrate data](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/snapshot-based-migration.html): Migrate data between OpenSearch Service domains of different versions using snapshots when in-place upgrades aren't possible.
- [Creating a custom endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/customendpoint.html): Create branded, memorable URLs for your Amazon OpenSearch Service domain to simplify access to OpenSearch and OpenSearch Dashboards.

### [Auto-Tune](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html)

Learn how to use Auto-Tune for Amazon OpenSearch Service to optimize your cluster performance.

- [Enabling or disabling Auto-Tune](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune-enable.html): Learn how to enable or disable Auto-Tune for your Amazon OpenSearch Service domains to optimize performance.
- [Scheduling Auto-Tune enhancements](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune-schedule.html): Configure Auto-Tune to apply optimizations during off-peak hours to minimize impact on your production workloads.

### [Tagging domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html)

Organize and track costs for your Amazon OpenSearch Service domains by applying customizable tags to categorize resources.

- [Tagging domains (console)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging-console.html): Learn about tagging domains using the console and how to use this feature in Amazon OpenSearch Service.
- [Tagging domains (AWS CLI)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging-cli.html): Use the AWS CLI to add, modify, and manage tags for your Amazon OpenSearch Service domains.
- [Tagging domains (AWS SDKs)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging-sdk.html): Learn about tagging domains using the AWS SDKs and how to use this feature in Amazon OpenSearch Service.

### [Performing administrative actions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/admin-options.html)

Learn how to use the AWS Management Console to perform administrative tasks

- [Restarting the OpenSearch process on a data node](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/restart-process.html): Restart the OpenSearch Dashboards process on Amazon OpenSearch Service nodes to resolve issues.
- [Rebooting a data node](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/restart-node.html): Learn how to safely reboot data nodes in Amazon OpenSearch Service to minimize disruption.
- [Restarting the Dashboards process](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/restart-dashboards.html): Learn about restarting the OpenSearch Dashboards process on a node in Amazon OpenSearch Service.


## [Working with direct queries](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query.html)

- [Pricing](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-pricing.html): Understand the pricing model for direct query features in Amazon OpenSearch Service.
- [Limitations](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-limitations.html): Learn about the limitations when using direct query capabilities in Amazon OpenSearch Service.
- [Recommendations](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-recommendations.html): Follow best practices for optimizing direct queries in Amazon OpenSearch Service for better performance.

### [Direct queries in S3](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-overview.html)

Query data stored in Amazon S3 directly from Amazon OpenSearch Service without ingestion.

- [Creating an S3 data source](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-creating.html): Query data stored in Amazon S3 directly from Amazon OpenSearch Service without ingestion.
- [Configuring an S3 data source](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-configure.html): Set up and query Amazon S3 data sources through AOS-dashboards in Amazon OpenSearch Service.

### [Direct queries in CloudWatch Logs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-cloudwatch-logs-overview.html)

Learn about directly querying Amazon CloudWatch Logs data in Amazon OpenSearch Service.

- [Creating a CloudWatch Logs data source](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-cloudwatch-logs-creating.html): Query logs in Amazon CloudWatch Logs data directly from Amazon OpenSearch Service without ingestion.
- [Configuring a CloudWatch Logs data source](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-cloudwatch-logs-configure.html): Configuring and querying a CloudWatch Logs data source in OpenSearch Dashboards to optimize your search operations and data management.

### [Direct queries in Security Lake](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-security-lake-overview.html)

Learn about directly querying Amazon Security Lake data in Amazon OpenSearch Service.

- [Creating a Security Lake data source](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-security-lake-creating.html): Query Security Lake data directly from Amazon OpenSearch Service without ingestion.
- [Configuring a Security Lake data source](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-security-lake-configure.html): Configuring and querying a Security Lake data source in OpenSearch Dashboards to optimize your search operations and data management.
- [Managing a data source](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-managing-data-sources.html): Monitor and manage data sources connected to Amazon OpenSearch Service for direct querying.
- [Optimizing query performance](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-configure-accelerate.html): Improve query performance when working with external data sources in Amazon OpenSearch Service.

### [Supported SQL and PPL commands](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-supported-commands.html)

Learn about the SQL and Piped Processing Language (PPL) commands supported for querying data in Amazon OpenSearch Service.

- [Supported SQL commands](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-directquery-sql.html): Learn about supported OpenSearch SQL commands and functions and how to use this feature in Amazon OpenSearch Service.
- [Supported PPL commands](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-ppl.html): Learn about the Piped Processing Language (PPL) commands supported for direct queries in Amazon OpenSearch Service.


## [Monitoring domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring.html)

- [Monitoring cluster metrics](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.html): Track and analyze performance metrics for your Amazon OpenSearch Service domains using Amazon CloudWatch.
- [Monitoring logs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html): Configure and publish OpenSearch error logs and slow logs to Amazon CloudWatch for troubleshooting performance and stability issues.
- [Monitoring audit logs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/audit-logs.html): Track user activity on your OpenSearch clusters with customizable audit logs to enhance security and meet compliance requirements.

### [Monitoring events](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-events.html)

Manage OpenSearch Service events in Amazon EventBridge

- [Tutorial: Listening for OpenSearch Service events](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/listening-events.html): Create an EventBridge rule to listen for OpenSearch Service events
- [Tutorial: Sending SNS alerts for available updates](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sns-events.html): Send an email from Amazon SNS when a service software update is available in OpenSearch Service
- [Monitoring with CloudTrail](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-cloudtrailauditing.html): Track and audit configuration changes in Amazon OpenSearch Service by monitoring API calls with AWS CloudTrail.


## [Cluster Insights](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cluster-insights.html)

- [Insights Catalog](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/insights-catalog.html): Cluster Insights delivers the following actionable insights on impacted Clusters


## [Security](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security.html)

### [Data protection](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/data-protection.html)

Implement encryption at rest and in transit to protect data in Amazon OpenSearch Service.

- [Encryption at rest](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/encryption-at-rest.html): Learn how to use encryption of data at rest for Amazon OpenSearch Service.
- [Node-to-node encryption](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html): Learn how to enable node-to-node encryption for Amazon OpenSearch Service.

### [Identity and Access Management](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html)

Learn about the identity and access management options available in Amazon OpenSearch Service.

- [Making and signing OpenSearch Service requests](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-signing-service-requests.html): Understand how to properly authenticate and sign requests to Amazon OpenSearch Service APIs.
- [API permissions reference](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac-permissions-ref.html): Create resource-level permissions that specify which Amazon OpenSearch Service resources that IAM users are allowed to perform actions on.
- [AWS managed policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac-managed.html): Learn about AWS managed policies for Amazon OpenSearch Service that you can use to grant permissions.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-service-confused-deputy-prevention.html): Protect your Amazon OpenSearch Service resources from cross-service impersonation attacks by implementing security best practices.

### [Fine-grained access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html)

Learn how to protect your Amazon OpenSearch Service data using fine-grained access control.

- [Tutorial: Fine-grained access control with Cognito authentication](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac-iam.html): Set up fine-grained access control with IAM master users and Amazon Cognito authentication for OpenSearch Service.
- [Tutorial: Internal user database with basic authentication](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac-http-auth.html): Configure fine-grained access control using internal user database and HTTP basic authentication in OpenSearch Service.
- [Compliance validation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon OpenSearch Service features for data resiliency.
- [JSON Web Tokens](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/JSON-Web-tokens.html): Use JSON Web Tokens to authenticate and authorize access to OpenSearch Service domains.

### [Infrastructure Security](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/infrastructure-security.html)

Learn how Amazon OpenSearch Service isolates service traffic.

- [Working with OpenSearch Service-managed VPC endpoints](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and Amazon OpenSearch Service.
- [SAML authentication for OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/saml.html): Configure SAML authentication for OpenSearch Dashboards to enable single sign-on capabilities.
- [IAM Identity Center Support for OpenSearch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/idc-aos.html): Use IAM Identity Center to authenticate and authorize access to OpenSearch Service domains.
- [Amazon Cognito authentication for OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html): Learn how to configure Amazon Cognito authentication for the OpenSearch Service default installation of OpenSearch Dashboards.

### [Using service-linked roles](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr.html)

How to use service-linked roles to give OpenSearch Service access to resources in your AWS account.

- [VPC domain and data source creation role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr-aos.html): How to use service-linked roles to give OpenSearch Service access to resources in your AWS account.
- [Collection creation role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-service-linked-roles.html): How to use service-linked roles to give OpenSearch Service access to resources in your AWS account.
- [Pipeline creation role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr-osis.html): Learn how to use service-linked roles to give Amazon OpenSearch Ingestion access to resources in your AWS account.


## [Sample code](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/samplecode.html)

- [Compressing HTTP requests](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gzip.html): Learn how to use gzip compression with Amazon OpenSearch Service.
- [Using the AWS SDKs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configuration-samples.html): Learn how to programmatically create, update, and delete Amazon OpenSearch Service domains using AWS SDK code examples.


## [Indexing data](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/indexing.html)

### [Loading streaming data into OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations.html)

Describes how to integrate Amazon OpenSearch Service with other AWS services.

- [Loading streaming data from OpenSearch Ingestion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations-osis.html): Set up data streaming from Amazon S3 to OpenSearch Service using AWS Lambda functions.
- [Loading streaming data from Amazon S3](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations-s3-lambda.html): Learn about loading streaming data from Amazon S3 and how to use this feature in Amazon OpenSearch Service.

### [Loading streaming data from Amazon Kinesis Data Streams](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations-kinesis.html)

Learn about loading streaming data from Amazon Kinesis Data Streams and how to use this feature in Amazon OpenSearch Service.

- [Create the Lambda function](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations-kinesis-lambda.html): Learn to create the Lambda function and how to use this feature in Amazon OpenSearch Service.
- [Test the Lambda Function](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations-kinesis-testing.html): Verify your Lambda function correctly processes and loads data into Amazon OpenSearch Service.
- [Loading streaming data from Amazon DynamoDB](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations-dynamodb.html): Learn about loading streaming data from Amazon DynamoDB and how to use this feature in Amazon OpenSearch Service.
- [Loading streaming data from Amazon Data Firehose](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations-fh.html): Learn about loading streaming data from Amazon Data Firehose and how to use this feature in Amazon OpenSearch Service.
- [Loading streaming data from Amazon CloudWatch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations-cloudwatch.html): Learn about loading streaming data from Amazon CloudWatch and how to use this feature in Amazon OpenSearch Service.
- [Loading data with Logstash](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-logstash.html): Use Logstash to efficiently ingest and transform data from various sources into your Amazon OpenSearch Service domain.


## [Searching data](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/searching.html)

### [Packages](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html)

Add custom dictionaries to your OpenSearch Service domain to improve your search results.

### [Custom plugins](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-plugins.html)

Learn how to install and manage custom plugins in Amazon OpenSearch Service to extend functionality.

- [Amazon OpenSearch Service custom package AWS KMS integration](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-package-kms-integration.html): Learn how to use AWS KMS encryption with Amazon OpenSearch Service custom packages.
- [Third-party plugins](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/plugins-third-party.html): Follow the steps to install and configure third-party plugins in Amazon OpenSearch Service.
- [SQL support](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sql-support.html): Learn how to use SQL to query your data in Amazon OpenSearch Service.
- [Cross-cluster search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html): Search across multiple connected Amazon OpenSearch Service domains.
- [Learning to Rank](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/learning-to-rank.html): Learn how to use Learning to Rank to use machine learning to improve search results.
- [Asynchronous search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/asynchronous-search.html): Use asynchronous search to run search requests in the background.
- [Point in time](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pit.html): Use point in time to run search requests.
- [Agentic search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/agentic-search.html): Agentic search in OpenSearch Service enables natural language queries with automated planning and execution.
- [Semantic search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/semantic-search.html): Use semantic search to determine the intention of your queries in the search context and improve search relevance.
- [Concurrent segment search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/concurrent-segment-search.html): Use concurrent segment search to search segments in parallel during the query phase.
- [Natural language query generation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/natural-language-query.html): Query your operational and security log data using natural language instead of complex query syntax in Amazon OpenSearch Service.


## [Vector search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vector-search.html)

- [Import from Amazon S3 Vectors to OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/s3-opensearch-vector-bucket-integration.html): Amazon S3 Vectors delivers the first cloud object store with native support to store and query vectors.
- [Advanced search capabilities with an Amazon S3 vector engine](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/s3-vector-opensearch-integration-engine.html): Amazon OpenSearch Service offers the ability to use Amazon S3 as a vector engine for vector indexes.
- [k-NN search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html): Use k-NN to find the "nearest neighbors" for points in a vector space.

### [Vector ingestion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-ingestion.html)

Vector ingestion quickly ingests and indexes OpenSearch domains and OpenSearch Serverless collections.

- [Export Amazon S3 vector index to OpenSearch Service vector engine](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/export-s3-vector-index.html): Export your selected Amazon S3 vector index to OpenSearch Service for advanced search functionality and performance optimization.
- [Import Amazon S3 vector namespace to OpenSearch Service vector engine](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/import-s3-vector-namespace.html): Import Amazon S3 vector data to OpenSearch Service for analysis, requiring one-time OpenSearch Service collection and IAM permission setup.
- [View vector ingestion jobs and import history](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/view-vector-ingestion-jobs.html): Monitor vector ingestion jobs and track S3 vector import history with detailed status information.

### [Auto-optimize](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-auto-optimize.html)

Learn how to use auto-optimize to automatically analyze your workload and recommend optimal configuration parameters for vector indexes in Amazon OpenSearch Service.

- [Using auto-optimize in the console](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-optimize-console.html): Learn how to create and manage auto-optimize jobs using the Amazon OpenSearch Service console.

### [GPU-acceleration for vector indexing](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gpu-acceleration-vector-index.html)

GPU-acceleration helps you build large-scale vector databases faster and more efficiently.

- [Enable GPU-acceleration](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gpu-acceleration-enabling.html): Learn how to enable GPU-acceleration for Amazon OpenSearch Service domains to improve vector search performance.
- [Create GPU-accelerated vector indexes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gpu-acceleration-creating-indexes.html): Learn how to create GPU-accelerated vector indexes in Amazon OpenSearch Service with the AWS SDK.
- [Index and force-merge](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gpu-acceleration-index-force-merge.html): Learn how to index vector data and perform force-merge operations with GPU-acceleration in Amazon OpenSearch Service.


## [OpenSearch UI](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html)

- [Release history](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-release-history.html): Explore the release history of Amazon OpenSearch Service support for OpenSearch UI, including new features, integrations, and enhancements for improved data analysis and visualization.
- [Getting started](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-getting-started.html): Learn how to create and manage OpenSearch UI applications in Amazon OpenSearch Service, including setting up authentication, granting administrator permissions, and using AWS Identity and Access Management or AWS IAM Identity Center for access control.
- [Encryption and Customer Managed Key](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-encryption-cmk.html): Learn how to encrypt OpenSearch UI application metadata using your own customer managed keys (CMK) from AWS Key Management Service to meet regulatory and compliance requirements.
- [Enabling SAML federation with IAM](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-enable-SAML-identity-federation.html): Configure SAML identity federation with AWS Identity and Access Management for OpenSearch UI, enabling single sign-on access and fine-grained control using identity providers like Okta.
- [Managing data source associations and VPC access permissions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-data-sources-and-vpc.html): Learn how to manage data source associations and to configure any needed access permissions for a virtual private cloud (VPC) for use with an OpenSearch UI application.
- [Using Amazon OpenSearch Service workspaces](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-workspaces.html): Learn how to create and manage workspaces in Amazon OpenSearch Service for OpenSearch UI, including setting privacy levels, managing collaborators, and understanding different workspace types for various use cases.
- [Cross-Region and cross-account data access with cross-cluster search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-cross-cluster-search.html): Learn how to use cross-cluster search in Amazon OpenSearch Serverless to query data across multiple domains, including setup, permissions, and best practices for cross-Region and cross-account access.
- [Managing access to the OpenSearch UI from a VPC endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-access-ui-from-vpc-endpoint.html): Learn how to create a private connection between your VPC and OpenSearch UI using AWS PrivateLink, enhancing security and simplifying network architecture.
- [Migrate from OpenSearch Dashboard](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-migration.html): Learn how to migrate saved objects such as dashboards, visualizations, index patterns, and searches from OpenSearch Dashboards to OpenSearch UI workspaces in Amazon OpenSearch Service.
- [Endpoints and quotas](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/opensearch-ui-endpoints-quotas.html): Find endpoints and quotas for OpenSearch UI


## [Managing indexes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managing-indices.html)

- [OpenSearch optimized instances](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/or1.html): Use OpenSearch optimized instances for Amazon OpenSearch Service domains.
- [Multi-tier storage](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/multi-tier-storage.html): Optimize performance and costs with intelligent data management across different storage tiers.
- [UltraWarm storage](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ultrawarm.html): Add UltraWarm storage to domains and move indexes from hot to warm storage.
- [Cold storage](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cold-storage.html): Enable cold storage on Amazon OpenSearch Service domains and move indexes from warm to cold storage.

### [Index State Management](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism.html)

Learn how to define custom management policies to automate administrative operations on indexes.

- [Tutorial: Automating ISM processes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism-tutorial.html): Automatically transition indexes between storage tiers using Index State Management.
- [Index rollups](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rollup.html): Learn how to summarize indexes using index rollups.
- [Index transforms](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/transforms.html): Learn how to analyze indexes using index transforms.
- [Cross-cluster replication](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/replication.html): Replicate data between Amazon OpenSearch Service domains.
- [Remote reindex](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/remote-reindex.html): Learn how to migrate indexes from one cluster to another.
- [Data streams](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/data-streams.html): Learn how to manage time-series data using data streams.


## [Monitoring data](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-data.html)

- [Alerting](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/alerting.html): Learn how to create monitors and generate alerts on data in OpenSearch Service.

### [Anomaly detection](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ad.html)

Learn how to use anomaly detection to automatically detect anomalies in your OpenSearch data.

- [Tutorial: Detect high CPU usage with anomaly detection](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createanomalydetector-tutorial.html): Create an anomaly detector in Amazon OpenSearch Service to detect high CPU usage.


## [AI Assistant](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/AI-assistant-support.html)

- [Setting up AI Assistant for OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/AI-Assistant-setting-up.html): Configure AI Assistant for Amazon OpenSearch Service to enable AI-powered assistance for your search operations.
- [Generate visualizations using natural language](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/AI-Assistant-generate-visualizations.html): Create powerful data visualizations in Amazon OpenSearch Service using natural language prompts with AI Assistant.
- [View alert summaries and insights](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/AI-assistant-alert-summary.html): Quickly understand and troubleshoot alerts with AI-generated summaries and insights that help identify root causes of issues.
- [View AI Assistant generated query result summaries on the Discover page](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/AI-assistant-query-summary.html): Get natural language summaries of your query results to quickly understand data patterns without writing complex queries.
- [View recommended anomaly detectors](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/AI-assistant-anomaly-detectors.html): Generate suggested anomaly detectors based on your data sources to automatically identify unusual patterns in your OpenSearch data.
- [Access AI Assistant chat for OpenSearch Service questions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/AI-assistant-chat-interface.html): Get answers to your OpenSearch Service questions through a conversational chat interface that preserves context and saves conversation history.


## [Machine learning](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml.html)

- [Connectors for AWS services](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-amazon-connector.html): Use connectors with AWS services to invoke endpoints to enrich query results and data pipelines.
- [Connectors for external platforms](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-external-connector.html): Use connectors with third-party platforms to invoke endpoints to enrich query results and data pipelines.

### [CloudFormation template integrations](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cfn-template.html)

Deploy machine learning models for semantic search using CloudFormation templates to connect OpenSearch with remote inference services.

- [Amazon Bedrock templates](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cfn-template-bedrock.html): The Amazon Bedrock CloudFormation templates provision the AWS resources needed to create connectors between OpenSearch Service and Amazon Bedrock.
- [Configuring Agentic Search with Bedrock Claude](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cfn-template-agentic-search.html): Agentic search leverages autonomous agents to execute complex searches on your behalf by understanding user intent, orchestrating the right tools, generating optimized queries, and providing transparent summaries of their decisions through a natural language interface.
- [MCP server integration templates](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cfn-template-mcp-server.html): With the Model Context Protocol (MCP) server templates, you can deploy an OpenSearch hosted MCP server on Amazon Bedrock AgentCore, reducing the integration complexity between AI agents and OpenSearch tools.
- [Amazon SageMaker templates](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cfn-template-sm.html): The Amazon SageMaker CloudFormation templates define multiple AWS resources in order to set up the neural plugin and semantic search for you.

### [Flow framework plugin](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-workflow-framework.html)

Automate complex OpenSearch setup tasks using flow framework templates to configure machine learning workflows and generative AI components.

- [Creating ML connectors in OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-create.html): Connect OpenSearch to AWS services and third-party platforms using ML connectors to enable advanced machine learning capabilities.
- [Configure permissions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/flow-framework-permissions.html): Set up the necessary security roles and permissions to enable users to manage flow framework features in your OpenSearch domain.


## [Observability](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability.html)

- [Logs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-analyze-logs.html): Use OpenSearch Service to transform unstructured logs into structured data, query with PPL or Q, create dashboards, and set up automated alerts for monitoring.
- [Traces](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-analyze-traces.html): Use OpenSearch Service to track distributed system requests, filter by service attributes, visualize dependencies with service maps, and identify bottlenecks using waterfall views.


## [Best practices](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp.html)

- [Recommended CloudWatch alarms](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cloudwatch-alarms.html): Set up CloudWatch alarms to monitor the health and performance of your Amazon OpenSearch Service domains.

### [Sizing domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sizing-domains.html)

Learn how to properly size your Amazon OpenSearch Service domains for optimal performance and cost efficiency.

- [Calculating storage requirements](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp-storage.html): Learn how to properly size your Amazon OpenSearch Service domains for optimal performance and cost efficiency.
- [Choosing the number of shards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp-sharding.html): Determine the optimal number of shards for your Amazon OpenSearch Service indices to balance performance and resource usage.
- [Choosing instance types and testing](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp-instances.html): Select appropriate instance types and conduct testing to ensure your Amazon OpenSearch Service domain meets performance requirements.
- [Petabyte scale](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/petabyte-scale.html): Review the considerations for creating especially large Amazon OpenSearch Service domains.
- [Dedicated coordinator nodes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/Dedicated-coordinator-nodes.html): Dedicated coordinator nodes in Amazon OpenSearch Service offload coordination tasks from data nodes, improving cluster performance, resource utilization, and query efficiency while reducing VPC IP address requirements.
- [Dedicated master nodes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.html): Understand the role of dedicated master nodes and how to configure them for stability in Amazon OpenSearch Service.


## [General reference](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/genref.html)

- [Supported instance types](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html): Learn about the various instance types available for Amazon OpenSearch Service domains and their specifications.
- [Features by engine version](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/features-by-version.html): Explore the features available in different OpenSearch and Elasticsearch versions supported by Amazon OpenSearch Service.
- [Plugins by engine version](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-plugins.html): Discover which plugins are available for each OpenSearch and Elasticsearch version in Amazon OpenSearch Service.
- [Supported operations](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-operations.html): Review the operations supported by the Amazon OpenSearch Service API and their compatibility across service versions.
- [Quotas](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html): View the quotas for Amazon OpenSearch Service resources.

### [Reserved Instances](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html)

Reserve OpenSearch Service instances for significant discounts.

- [Purchasing Reserved Instances (console)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri-console.html): Use the AWS CLI to purchase Reserved Instances for Amazon OpenSearch Service to reduce costs.
- [Purchasing Reserved Instances (AWS CLI)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri-cli.html): Learn about purchasing reserved instances using the AWS CLI and how to use this feature in Amazon OpenSearch Service.
- [Purchasing Reserved Instances (AWS SDKs)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri-sdk.html): Learn about purchasing reserved instances using the AWS SDKs and how to use this feature in Amazon OpenSearch Service.
- [Cost optimization](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cost-optimization.html): Learn techniques to optimize costs for Amazon OpenSearch Service managed clusters and serverless collections.
- [Other supported resources](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-resources.html): Find additional resources and components supported by Amazon OpenSearch Service for your data solutions.


## [Tutorials](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tutorials.html)

- [Creating and searching for documents](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/quick-start.html): Create and search for a document in Amazon OpenSearch Service.
- [Migrating to OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/migration.html): Learn how to move a snapshot to Amazon S3 and restore it in Amazon OpenSearch Service.
- [Creating a search application](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/search-example.html): Create a search application using Amazon OpenSearch Service, AWS Lambda, and Amazon API Gateway.
- [Visualizing support calls](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/walkthrough.html): Visualize customer support call transcripts using Amazon OpenSearch Service and OpenSearch Dashboards.
