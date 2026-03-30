# Source: https://docs.aws.amazon.com/migrationhub/latest/ug/llms.txt

# AWS Migration Hub User Guide

> AWS Migration Hub provides you with a single location to track migration tasks across multiple AWS tools and partner solutions to migrate to the AWS cloud.

- [AWS Migration Hub availability change](https://docs.aws.amazon.com/migrationhub/latest/ug/migrationhub-availability-change.html)
- [Tracking metrics in the dashboard](https://docs.aws.amazon.com/migrationhub/latest/ug/dashboards-tracking-wt.html)
- [Tagging migration resources](https://docs.aws.amazon.com/migrationhub/latest/ug/tagging-migration-resources.html)
- [Quotas](https://docs.aws.amazon.com/migrationhub/latest/ug/limits.html)
- [Troubleshooting](https://docs.aws.amazon.com/migrationhub/latest/ug/troubleshooting.html)
- [Logging Migration Hub API calls with AWS CloudTrail](https://docs.aws.amazon.com/migrationhub/latest/ug/logging-using-cloudtrail.html)
- [Document history](https://docs.aws.amazon.com/migrationhub/latest/ug/document-history.html)

## [What Is AWS Migration Hub?](https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/migrationhub/latest/ug/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Setting up](https://docs.aws.amazon.com/migrationhub/latest/ug/setting-up.html)

- [Sign up for AWS](https://docs.aws.amazon.com/migrationhub/latest/ug/setting-up-signup.html): When you sign up for Amazon Web Services (AWS), you are charged only for the services that you use.


## [Getting started](https://docs.aws.amazon.com/migrationhub/latest/ug/getting-started.html)

- [Discover](https://docs.aws.amazon.com/migrationhub/latest/ug/gs-new-user-discovery.html): AWS Migration Hub (Migration Hub) provides a single place to discover your existing servers, plan migrations, and track the status of each application migration.
- [Migrate](https://docs.aws.amazon.com/migrationhub/latest/ug/gs-new-user-migration.html): You can start migrating with or without first using the AWS Migration Hub discovery tools.
- [Track](https://docs.aws.amazon.com/migrationhub/latest/ug/migrate-wt-track.html): Track migrations in AWS Migration Hub.


## [Automation](https://docs.aws.amazon.com/migrationhub/latest/ug/mha.html)

- [Managed automation units](https://docs.aws.amazon.com/migrationhub/latest/ug/mha-managed-units.html): Learn about managed automation units.
- [Custom automation units](https://docs.aws.amazon.com/migrationhub/latest/ug/mha-custom-units.html): Learn how to create and manage custom automation units.
- [Automation runs](https://docs.aws.amazon.com/migrationhub/latest/ug/mha-runs.html): Learn about how to start and manage automation runs.
- [IAM roles and permissions](https://docs.aws.amazon.com/migrationhub/latest/ug/mha-iam-roles.html): Learn how to set up the IAM roles and permissions that are required for automation units.
- [Associating an IAM role](https://docs.aws.amazon.com/migrationhub/latest/ug/associate-role-with-unit.html)


## [Tracking migration updates](https://docs.aws.amazon.com/migrationhub/latest/ug/updates-tracking-wt.html)

- [Tracking when you perform discovery first and then migrate](https://docs.aws.amazon.com/migrationhub/latest/ug/updates-tracking-wt-disco-first.html): Tracking when you perform discovery first and then migrate details in AWS Migration Hub Manual mapping.
- [Tracking when you migrate without performing discovery](https://docs.aws.amazon.com/migrationhub/latest/ug/updates-tracking-wt-no-disco.html): Tracking when you migrate without performing discovery details in AWS Migration Hub.
- [Troubleshooting and manually mapping migration updates](https://docs.aws.amazon.com/migrationhub/latest/ug/updates-tracking-wt-troubleshooting.html): Troubleshooting Migration Updates How to track and map migration updates to servers in AWS Migration Hub Manual mapping manually map.


## [Home Region](https://docs.aws.amazon.com/migrationhub/latest/ug/home-region.html)

- [Choose a home Region](https://docs.aws.amazon.com/migrationhub/latest/ug/select-home-region.html): When you first use the AWS Migration Hub console, choose a Migration Hub home Region.
- [Changing your home Region](https://docs.aws.amazon.com/migrationhub/latest/ug/change-home-region.html)
- [Discovery requires the home Region](https://docs.aws.amazon.com/migrationhub/latest/ug/home-region-with-discovery.html): To start discovery and planning, you can deploy data collectors, such as AWS Application Discovery Agent (Discovery Agent) or Application Discovery Service Agentless Collector (Agentless Collector), into your data centers.
- [Migration progress is stored in the home Region](https://docs.aws.amazon.com/migrationhub/latest/ug/migration-reporting.html): When youâre ready to migrate, use the migration tools that best fit your needs.


## [Amazon EC2 recommendations](https://docs.aws.amazon.com/migrationhub/latest/ug/ec2-recommendations.html)

- [Prerequisites](https://docs.aws.amazon.com/migrationhub/latest/ug/ec2-recommendation-prerequisites.html): Before you can get Amazon EC2 instance recommendations, you must have data about your on-premises servers in Migration Hub.
- [How Amazon EC2 instance recommendations work](https://docs.aws.amazon.com/migrationhub/latest/ug/how-ec2-recommendations-work.html): This feature recommends the most cost-effective Amazon Elastic Compute Cloud instance type that can satisfy your existing server specifications and utilization requirements while taking into account your selected instance preferences.
- [Generating Amazon EC2 recommendations](https://docs.aws.amazon.com/migrationhub/latest/ug/generating-ec2-recommendations.html): In the Export Amazon EC2 instance recommendations page of the Migration Hub console, you'll choose your recommendation preferences.
- [Understanding your Amazon EC2 recommendations](https://docs.aws.amazon.com/migrationhub/latest/ug/understanding-ec2-recommendations.html): The downloaded EC2InstanceRecommendations-{type}-{date}.csv file contains the following information.
- [Additional considerations](https://docs.aws.amazon.com/migrationhub/latest/ug/ec2-rec-considerations.html): Keep the following considerations in mind when generating Amazon EC2 instance recommendations.


## [Viewing network connections](https://docs.aws.amazon.com/migrationhub/latest/ug/network-diagram.html)

- [Prerequisites](https://docs.aws.amazon.com/migrationhub/latest/ug/network-diagram-prerequisites.html): Lists the prerequisites for using the network diagram in AWS Migration Hub.
- [How to use the network diagram](https://docs.aws.amazon.com/migrationhub/latest/ug/network-diagram-how-to.html): Describes how to use the network diagram in Migration Hub.
- [Troubleshooting](https://docs.aws.amazon.com/migrationhub/latest/ug/network-diagram-troubleshooting.html): Troubleshooting information for the network diagram in AWS Migration Hub.


## [Code examples](https://docs.aws.amazon.com/migrationhub/latest/ug/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/migrationhub/latest/ug/service_code_examples_basics.html)

The following code examples show how to use the basics of Migration Hub with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/migrationhub/latest/ug/service_code_examples_actions.html)

The following code examples show how to use Migration Hub with AWS SDKs.

- [DeleteProgressUpdateStream](https://docs.aws.amazon.com/migrationhub/latest/ug/example_migration-hub_DeleteProgressUpdateStream_section.html): Use DeleteProgressUpdateStream with an AWS SDK
- [DescribeApplicationState](https://docs.aws.amazon.com/migrationhub/latest/ug/example_migration-hub_DescribeApplicationState_section.html): Use DescribeApplicationState with an AWS SDK
- [DescribeMigrationTask](https://docs.aws.amazon.com/migrationhub/latest/ug/example_migration-hub_DescribeMigrationTask_section.html): Use DescribeMigrationTask with an AWS SDK
- [ImportMigrationTask](https://docs.aws.amazon.com/migrationhub/latest/ug/example_migration-hub_ImportMigrationTask_section.html): Use ImportMigrationTask with an AWS SDK
- [ListApplications](https://docs.aws.amazon.com/migrationhub/latest/ug/example_migration-hub_ListApplications_section.html): Use ListApplications with an AWS SDK
- [ListCreatedArtifacts](https://docs.aws.amazon.com/migrationhub/latest/ug/example_migration-hub_ListCreatedArtifacts_section.html): Use ListCreatedArtifacts with an AWS SDK
- [ListMigrationTasks](https://docs.aws.amazon.com/migrationhub/latest/ug/example_migration-hub_ListMigrationTasks_section.html): Use ListMigrationTasks with an AWS SDK


## [Security](https://docs.aws.amazon.com/migrationhub/latest/ug/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/migrationhub/latest/ug/auth-and-access-control.html)

Identifies methods for controlling access to your AWS Migration Hub resources.

### [Roles & Policies](https://docs.aws.amazon.com/migrationhub/latest/ug/policy-templates.html)

Roles and Policy Templates in AWS Migration Hub.

- [New User IAM Setup](https://docs.aws.amazon.com/migrationhub/latest/ug/new-customer-setup.html): AWS Migration Hub New User IAM New Customer Setup template.
- [Custom Policies for Migration Tools](https://docs.aws.amazon.com/migrationhub/latest/ug/customer-managed-vendor.html): AWS Migration Hub Third-party vendor customer managed policies.
- [API Permissions Reference](https://docs.aws.amazon.com/migrationhub/latest/ug/migrationhub-api-permissions-ref.html): AWS Migration Hub API Permissions Actions and Resources Reference.
- [Authentication & Access Explained](https://docs.aws.amazon.com/migrationhub/latest/ug/auth-and-access-explained.html): Authentication and Access Control Explained in AWS Migration Hub.

### [Using Service-Linked Roles](https://docs.aws.amazon.com/migrationhub/latest/ug/using-service-linked-roles.html)

How to use service-linked roles to give Migration Hub access to resources in your AWS account.

- [Application Discovery Service Role](https://docs.aws.amazon.com/migrationhub/latest/ug/using-service-linked-roles-discovery-service-role.html): How to use service-linked roles to give Migration Hub access to resources in your AWS account.
- [AWS DMS Role](https://docs.aws.amazon.com/migrationhub/latest/ug/using-service-linked-roles-dms-service-role.html): How to use service-linked roles to give Migration Hub access to resources in your AWS account.
- [Logging and monitoring in AWS Migration Hub](https://docs.aws.amazon.com/migrationhub/latest/ug/logging-monitoring.html): Learn about logging and monitoring in AWS Migration Hub.


## [AWS Migration Hub API](https://docs.aws.amazon.com/migrationhub/latest/ug/api-reference.html)

### [Actions](https://docs.aws.amazon.com/migrationhub/latest/ug/API_Operations.html)

The following actions are supported:

- [AssociateCreatedArtifact](https://docs.aws.amazon.com/migrationhub/latest/ug/API_AssociateCreatedArtifact.html): Associates a created artifact of an AWS cloud resource, the target receiving the migration, with the migration task performed by a migration tool.
- [AssociateDiscoveredResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_AssociateDiscoveredResource.html): Associates a discovered resource ID from Application Discovery Service with a migration task.
- [AssociateSourceResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_AssociateSourceResource.html): Associates a source resource with a migration task.
- [CreateProgressUpdateStream](https://docs.aws.amazon.com/migrationhub/latest/ug/API_CreateProgressUpdateStream.html): Creates a progress update stream which is an AWS resource used for access control as well as a namespace for migration task names that is implicitly linked to your AWS account.
- [DeleteProgressUpdateStream](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DeleteProgressUpdateStream.html): Deletes a progress update stream, including all of its tasks, which was previously created as an AWS resource used for access control.
- [DescribeApplicationState](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DescribeApplicationState.html): Gets the migration status of an application.
- [DescribeMigrationTask](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DescribeMigrationTask.html): Retrieves a list of all attributes associated with a specific migration task.
- [DisassociateCreatedArtifact](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DisassociateCreatedArtifact.html): Disassociates a created artifact of an AWS resource with a migration task performed by a migration tool that was previously associated.
- [DisassociateDiscoveredResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DisassociateDiscoveredResource.html): Disassociate an Application Discovery Service discovered resource from a migration task.
- [DisassociateSourceResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DisassociateSourceResource.html): Removes the association between a source resource and a migration task.
- [ImportMigrationTask](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ImportMigrationTask.html): Registers a new migration task which represents a server, database, etc., being migrated to AWS by a migration tool.
- [ListApplicationStates](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListApplicationStates.html): Lists all the migration statuses for your applications.
- [ListCreatedArtifacts](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListCreatedArtifacts.html): Lists the created artifacts attached to a given migration task in an update stream.
- [ListDiscoveredResources](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListDiscoveredResources.html): Lists discovered resources associated with the given MigrationTask.
- [ListMigrationTasks](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListMigrationTasks.html): Lists all, or filtered by resource name, migration tasks associated with the user account making this call.
- [ListMigrationTaskUpdates](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListMigrationTaskUpdates.html): This is a paginated API that returns all the migration-task states for the specified MigrationTaskName and ProgressUpdateStream.
- [ListProgressUpdateStreams](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListProgressUpdateStreams.html): Lists progress update streams associated with the user account making this call.
- [ListSourceResources](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListSourceResources.html): Lists all the source resource that are associated with the specified MigrationTaskName and ProgressUpdateStream.
- [NotifyApplicationState](https://docs.aws.amazon.com/migrationhub/latest/ug/API_NotifyApplicationState.html): Sets the migration state of an application.
- [NotifyMigrationTaskState](https://docs.aws.amazon.com/migrationhub/latest/ug/API_NotifyMigrationTaskState.html): Notifies Migration Hub of the current status, progress, or other detail regarding a migration task.
- [PutResourceAttributes](https://docs.aws.amazon.com/migrationhub/latest/ug/API_PutResourceAttributes.html): Provides identifying details of the resource being migrated so that it can be associated in the Application Discovery Service repository.

### [Data Types](https://docs.aws.amazon.com/migrationhub/latest/ug/API_Types.html)

The following data types are supported:

- [ApplicationState](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ApplicationState.html): The state of an application discovered through Migration Hub import, the AWS Agentless Discovery Connector, or the AWS Application Discovery Agent.
- [CreatedArtifact](https://docs.aws.amazon.com/migrationhub/latest/ug/API_CreatedArtifact.html): An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2 instance, RDS instance, etc.).
- [DiscoveredResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DiscoveredResource.html): Object representing the on-premises resource being migrated.
- [MigrationTask](https://docs.aws.amazon.com/migrationhub/latest/ug/API_MigrationTask.html): Represents a migration task in a migration tool.
- [MigrationTaskSummary](https://docs.aws.amazon.com/migrationhub/latest/ug/API_MigrationTaskSummary.html): MigrationTaskSummary includes MigrationTaskName, ProgressPercent, ProgressUpdateStream, Status, and UpdateDateTime for each task.
- [MigrationTaskUpdate](https://docs.aws.amazon.com/migrationhub/latest/ug/API_MigrationTaskUpdate.html): A migration-task progress update.
- [ProgressUpdateStreamSummary](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ProgressUpdateStreamSummary.html): Summary of the AWS resource used for access control that is implicitly linked to your AWS account.
- [ResourceAttribute](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ResourceAttribute.html): Attribute associated with a resource.
- [SourceResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_SourceResource.html): A source resource can be a source server, a migration wave, an application, or any other resource that you track.
- [Task](https://docs.aws.amazon.com/migrationhub/latest/ug/API_Task.html): Task object encapsulating task information.
