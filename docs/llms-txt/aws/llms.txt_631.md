# Source: https://docs.aws.amazon.com/omics/latest/dev/llms.txt

# AWS HealthOmics User Guide

- [What is AWS HealthOmics?](https://docs.aws.amazon.com/omics/latest/dev/what-is-healthomics.html)
- [AWS HealthOmics variant store and annotation store availability change](https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html)
- [Setting up HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/setting-up-new.html)
- [Getting started](https://docs.aws.amazon.com/omics/latest/dev/getting-started.html)
- [Resource sharing](https://docs.aws.amazon.com/omics/latest/dev/resource-sharing.html)
- [Troubleshooting](https://docs.aws.amazon.com/omics/latest/dev/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/omics/latest/dev/doc-history.html)

## [Private workflows](https://docs.aws.amazon.com/omics/latest/dev/private-workflows.html)

### [Creating workflows](https://docs.aws.amazon.com/omics/latest/dev/workflows-setup.html)

Learn how to set up the required resources and create a HealthOmics workflow.

- [Git repository integration](https://docs.aws.amazon.com/omics/latest/dev/workflows-git-integration.html): Learn about workflow integration with Git-based repositories.

### [Workflow definition files](https://docs.aws.amazon.com/omics/latest/dev/workflow-definition-files.html)

Learn how to create HealthOmics workflow definition files.

- [Workflow definition requirements](https://docs.aws.amazon.com/omics/latest/dev/workflow-defn-requirements.html): The HealthOmics workflow definition files must meet the following requirements:
- [Workflow language version support](https://docs.aws.amazon.com/omics/latest/dev/workflows-lang-versions.html): Learn about HealthOmics support for workflow definition language versions.
- [Compute and memory](https://docs.aws.amazon.com/omics/latest/dev/memory-and-compute-tasks.html): Learn how to set memory and compute requirements for tasks, and how HealthOmics maps these requirements to omic instances.
- [Task outputs](https://docs.aws.amazon.com/omics/latest/dev/workflows-task-outputs.html): Learn about specifying task outputs for private workflow tasks in HealthOmics.
- [Task resources](https://docs.aws.amazon.com/omics/latest/dev/task-resources.html): In the workflow definition, define the following for each task:
- [Task accelerators](https://docs.aws.amazon.com/omics/latest/dev/task-accelerators.html): In the workflow definition, you can optionally specify the GPU accelerator-spec for a task.
- [WDL specifics](https://docs.aws.amazon.com/omics/latest/dev/workflow-languages-wdl.html): Learn how to create workflow definitions using WDL in HealthOmics.
- [Nextflow specifics](https://docs.aws.amazon.com/omics/latest/dev/workflow-definition-nextflow.html): Learn how to create workflow definitions using Nextflow in HealthOmics.
- [CWL specifics](https://docs.aws.amazon.com/omics/latest/dev/workflow-languages-cwl.html): Learn how to create workflow definitions using CWL in HealthOmics.
- [Examples](https://docs.aws.amazon.com/omics/latest/dev/workflow-definition-examples.html): The following example shows the same workflow definition in WDL, Nextflow, and CWL.
- [Parameter template files](https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html): Learn about HealthOmics parameter templates for private workflows.
- [Container images](https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html): Learn about creating container images in Amazon ECR for private workflows.
- [Workflow README files](https://docs.aws.amazon.com/omics/latest/dev/workflows-readme.html): Upload a README.md file containing instructions, diagrams, and essential information for your workflow.
- [Optional: Sentieon licenses](https://docs.aws.amazon.com/omics/latest/dev/private-workflows-subscribe.html): Learn how to request a Sentieon license for private workflows.
- [Workflow linters](https://docs.aws.amazon.com/omics/latest/dev/workflows-linter.html): Learn how to use linters to detect errors in HealthOmics workflow definition files.

### [Workflow operations](https://docs.aws.amazon.com/omics/latest/dev/creating-private-workflows.html)

Learn how to create, update, and delete HealthOmics private workflows.

- [Create a workflow](https://docs.aws.amazon.com/omics/latest/dev/create-private-workflow.html): Learn about how to create HealthOmics private workflows.
- [Update a workflow](https://docs.aws.amazon.com/omics/latest/dev/update-private-workflow.html): Learn about how to update HealthOmics private workflows.
- [Delete a workflow](https://docs.aws.amazon.com/omics/latest/dev/delete-private-workflow.html): Learn how to delete HealthOmics private workflows.
- [Verify the workflow status](https://docs.aws.amazon.com/omics/latest/dev/using-get-workflow.html): After you create your workflow, you can verify the status and view other details of the workflow using get-workflow, as shown.
- [Referencing genome files from a workflow definition](https://docs.aws.amazon.com/omics/latest/dev/create-ref-files.html): An HealthOmics reference store object can be referred to with a URI like the following.

### [Workflow versioning](https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html)

Learn about how to use HealthOmics private workflow versions.

- [Default version](https://docs.aws.amazon.com/omics/latest/dev/workflows-default-version.html): Learn about the default workflow version.
- [Create a version](https://docs.aws.amazon.com/omics/latest/dev/workflows-version-create.html): Learn about how to create HealthOmics private workflow versions.
- [Update a version](https://docs.aws.amazon.com/omics/latest/dev/workflows-version-update.html): Learn about how to update HealthOmics private workflow versions.
- [Delete a version](https://docs.aws.amazon.com/omics/latest/dev/workflows-version-delete.html): Learn about how to delete HealthOmics private workflow versions.

### [HealthOmics runs](https://docs.aws.amazon.com/omics/latest/dev/running-workflows.html)

Learn about starting HealthOmics runs.

- [Run storage types](https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html): Learn about run storage types for HealthOmics workflows.
- [Run retention modes](https://docs.aws.amazon.com/omics/latest/dev/run-retention.html): Learn about run retention mode in HealthOmics .
- [Run inputs](https://docs.aws.amazon.com/omics/latest/dev/workflows-run-inputs.html): Learn about specifying input formats for private workflows runs in HealthOmics.
- [Run lifecycle](https://docs.aws.amazon.com/omics/latest/dev/monitoring-runs.html): Learn about run status values for HealthOmics runs.
- [Run outputs](https://docs.aws.amazon.com/omics/latest/dev/workflows-run-outputs.html): Learn about run outputs for a HealthOmics run.
- [Run failure reasons](https://docs.aws.amazon.com/omics/latest/dev/workflows-run-errors.html): Troubleshooting error and status messages for run failure in HealthOmics.
- [Task lifecycle](https://docs.aws.amazon.com/omics/latest/dev/workflow-run-tasks.html): Learn about the task lifecycle in a HealthOmics run.
- [Run optimization](https://docs.aws.amazon.com/omics/latest/dev/workflows-run-optimize.html): Learn about run optimization in a HealthOmics workflow.

### [Run operations](https://docs.aws.amazon.com/omics/latest/dev/run-operations.html)

Learn about the operations for a HealthOmics run.

- [Start a run](https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html): Learn about how to start a HealthOmics workflow run using the console and API.
- [Rerun a run](https://docs.aws.amazon.com/omics/latest/dev/rerun-a-run.html): Learn how to cancel HealthOmics runs.
- [Clone a run](https://docs.aws.amazon.com/omics/latest/dev/workflows-run-clone.html): Learn about how to clone a HealthOmics workflow run using the HealthOmics console.
- [Cancel a run](https://docs.aws.amazon.com/omics/latest/dev/canceling-runs.html): Learn how to cancel HealthOmics runs.
- [Delete a run](https://docs.aws.amazon.com/omics/latest/dev/deleting-runs.html): Learn how to delete HealthOmics runs.
- [Run groups](https://docs.aws.amazon.com/omics/latest/dev/creating-run-groups.html): Learn how to create and delete HealthOmics run groups.

### [Call caching](https://docs.aws.amazon.com/omics/latest/dev/workflows-call-caching.html)

Learn about using cached data for HealthOmics runs.

- [How call caching works](https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html): Learn about using cached data for HealthOmics runs.
- [Creating a run cache](https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-create.html): Learn how to create a run cache.
- [Updating a run cache](https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-update.html): Learn how to update a run cache.
- [Deleting a run cache](https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-delete.html): Learn how to delete a run cache.
- [Contents of a run cache](https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-contents.html): Learn about the contents and stucture of a run cache.
- [Engine-specific caching features](https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-per-engine.html): Learn about the Engine-specific features for call caching.
- [Using the run cache](https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-startrun.html): Learn about using the call caching in a run.
- [Sharing workflows](https://docs.aws.amazon.com/omics/latest/dev/sharing-workflows.html): Learn about sharing HealthOmics workflows.


## [Ready2Run workflows](https://docs.aws.amazon.com/omics/latest/dev/Ready2Run-workflows.html)

- [Available workflows](https://docs.aws.amazon.com/omics/latest/dev/workflows-r2r-table.html): Learn about the available Ready2Run workflows.
- [Subscribing to Sentieon workflows](https://docs.aws.amazon.com/omics/latest/dev/Ready2Run-workflows-subscribe.html): Learn how to subscribe to a Ready2Run workflow.
- [Starting Ready2Run workflows (console)](https://docs.aws.amazon.com/omics/latest/dev/Ready2Run-workflows-console.html): Learn about using Ready2Run workflows in the console.
- [Starting Ready2Run workflows (API)](https://docs.aws.amazon.com/omics/latest/dev/Ready2Run-workflows-API.html): Learn about using Ready2Run workflows in the API.


## [HealthOmics storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)

- [HealthOmics ETags](https://docs.aws.amazon.com/omics/latest/dev/etags-and-provenance.html): Learn about how HealthOmics calculates ETags and maintains data provenance.
- [Creating a reference store](https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html): Learn how to create a HealthOmics reference store using the console or CLI.
- [Creating a sequence store](https://docs.aws.amazon.com/omics/latest/dev/create-sequence-store.html): Learn about managing HealthOmics sequence stores.
- [Deleting stores](https://docs.aws.amazon.com/omics/latest/dev/deleting-reference-and-sequence-stores.html): Learn how to delete reference stores and sequence stores.
- [Importing read sets into a sequence store](https://docs.aws.amazon.com/omics/latest/dev/import-sequence-store.html): Learn how to use read sets to import files into HealthOmics storage.
- [Direct upload to a sequence store](https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html): Learn about synchronous uploads into a HealthOmics sequence store.
- [Exporting read sets](https://docs.aws.amazon.com/omics/latest/dev/read-set-exports.html): Learn about exporting read sets
- [Accessing read sets with Amazon S3 URIs](https://docs.aws.amazon.com/omics/latest/dev/s3-access.html): Use Amazon S3 access paths to read data in HealthOmics Storage.
- [Activating read sets](https://docs.aws.amazon.com/omics/latest/dev/activating-read-sets.html): Learn about how to activate archived read sets in HealthOmics storage.


## [HealthOmics analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)

- [Creating variant stores](https://docs.aws.amazon.com/omics/latest/dev/creating-variant-stores.html): Learn how to create and manage HealthOmics variant stores using the console and the AWS CLI.
- [Creating variant store import jobs](https://docs.aws.amazon.com/omics/latest/dev/parsing-annotation-stores.html): Learn about import jobs for variant data.
- [Creating annotation stores](https://docs.aws.amazon.com/omics/latest/dev/creating-and-managing-annotation-store.html): Learn how to create and manage HealthOmics annotation stores.
- [Creating annotation store import jobs](https://docs.aws.amazon.com/omics/latest/dev/annotation-store-import-jobs.html): Learn more about importing jobs for HealthOmics annotation stores.
- [Creating annotation store versions](https://docs.aws.amazon.com/omics/latest/dev/annotation-store-versioning.html): Learn more about creating and using different versions of annotation stores in HealthOmics.
- [Deleting analytics stores](https://docs.aws.amazon.com/omics/latest/dev/deleting-a-store-examples.html): Learn how to permanently delete variant or annotation analytics stores and all associated data in HealthOmics.

### [Querying analytics data](https://docs.aws.amazon.com/omics/latest/dev/analytics-query-data.html)

Learn how to query the parsed annotation schemas created from your imported variant data.

- [Configuring Lake Formation](https://docs.aws.amazon.com/omics/latest/dev/setting-up-lf.html): Learn how to configure Lake Formation to use HealthOmics Analytics data stores.
- [Configuring Athena for queries](https://docs.aws.amazon.com/omics/latest/dev/analytics-setting-up-athena.html): Learn how to query the parsed annotation schemas created from your imported variant data.
- [Runnning queries](https://docs.aws.amazon.com/omics/latest/dev/analytics-run-queries.html): Learn how to query the parsed annotation schemas created from your imported HealthOmics variant data.
- [Sharing analytics stores](https://docs.aws.amazon.com/omics/latest/dev/cross-account-sharing.html): Learn how to share data from one of your analytics stores.


## [Tagging resources in HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/tagging.html)

- [Adding a tag](https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html): Learn about adding a tag to a HealthOmics resource
- [Listing tags](https://docs.aws.amazon.com/omics/latest/dev/list-tags.html): Learn about listing tags for an HealthOmics resource
- [Removing tags](https://docs.aws.amazon.com/omics/latest/dev/remove-tags.html): Learn about removing a tag from an HealthOmics resource


## [Permissions](https://docs.aws.amazon.com/omics/latest/dev/omics-permissions.html)

- [User policies](https://docs.aws.amazon.com/omics/latest/dev/permissions-user.html): Grant IAM users, groups, and roles permission to use HealthOmics.
- [Service roles](https://docs.aws.amazon.com/omics/latest/dev/permissions-service.html): Use service roles to grant AWS HealthOmics permission to access data in Amazon S3, invoke functions in AWS Lambda, and send alerts to Amazon SNS.
- [Amazon ECR permissions](https://docs.aws.amazon.com/omics/latest/dev/permissions-ecr.html): Learn about how to configure resource permissions for using HealthOmics with Amazon ECR.
- [Resource permissions](https://docs.aws.amazon.com/omics/latest/dev/permissions-resource.html): Learn about how to configure resource permissions for using HealthOmics with other services.
- [Amazon S3 URI Permissions](https://docs.aws.amazon.com/omics/latest/dev/s3-sharing.html): Use Amazon S3 access paths to share data in HealthOmics Storage.


## [Security](https://docs.aws.amazon.com/omics/latest/dev/security.html)

- [Data protection](https://docs.aws.amazon.com/omics/latest/dev/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS HealthOmics.

### [Identity and access management](https://docs.aws.amazon.com/omics/latest/dev/security-iam.html)

Discover how IAM securely controls access to HealthOmics resources through user authentication and policy-based permissions management.

### [How AWS HealthOmics works with IAM](https://docs.aws.amazon.com/omics/latest/dev/security_iam_service-with-iam.html)

Learn how to use IAM to secure HealthOmics resources.

- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/omics/latest/dev/cross-service-confused-deputy-prevention.html): Learn about cross-service confused deputy prevention.
- [Identity-based policy examples](https://docs.aws.amazon.com/omics/latest/dev/security_iam_id-based-policy-examples.html): Learn about identity-based policy examples for HealthOmics.
- [AWS managed policies](https://docs.aws.amazon.com/omics/latest/dev/security-iam-awsmanpol.html): Learn about AWS managed policies for HealthOmics and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/omics/latest/dev/security_iam_troubleshoot.html): Learn how to troubleshoot identity and access issues with HealthOmics.
- [Compliance validation](https://docs.aws.amazon.com/omics/latest/dev/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/omics/latest/dev/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific HealthOmics features for data resiliency.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/omics/latest/dev/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and AWS HealthOmics that doesn't require access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.


## [Monitoring AWS HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/monitoring-overview.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch.html): Learn how to use CloudWatch metrics for monitoring and troubleshooting HealthOmics.
- [CloudWatch Logs](https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html): Learn how to use CloudWatch Logs for monitoring and troubleshooting HealthOmics workflows.
- [CloudTrail logs](https://docs.aws.amazon.com/omics/latest/dev/logging-using-cloudtrail.html): Learn about logging AWS HealthOmics with AWS CloudTrail.
- [EventBridge](https://docs.aws.amazon.com/omics/latest/dev/eventbridge.html): Learn about the EventBridge events for AWS HealthOmics.


## [Quotas](https://docs.aws.amazon.com/omics/latest/dev/quotas.html)

- [Service quotas](https://docs.aws.amazon.com/omics/latest/dev/service-quotas.html): Learn about the service quotas for HealthOmics.
- [Fixed size quotas](https://docs.aws.amazon.com/omics/latest/dev/fixed-quotas.html): Learn about the fixed-size quotas for HealthOmics.
- [API quotas](https://docs.aws.amazon.com/omics/latest/dev/api-quotas.html): Learn about API quotas for HealthOmics.
