# Source: https://docs.aws.amazon.com/healthlake/latest/devguide/llms.txt

# AWS HealthLake Developer Guide

> Provides a conceptual overview of AWS HealthLake and detailed instructions for using its features.

- [What is AWS HealthLake?](https://docs.aws.amazon.com/healthlake/latest/devguide/what-is.html)
- [Releases](https://docs.aws.amazon.com/healthlake/latest/devguide/releases.html)

## [Getting started](https://docs.aws.amazon.com/healthlake/latest/devguide/getting-started.html)

- [Concepts](https://docs.aws.amazon.com/healthlake/latest/devguide/getting-started-concepts.html): Learn concepts and terminology for AWS HealthLake.
- [Setting up](https://docs.aws.amazon.com/healthlake/latest/devguide/getting-started-setting-up.html): Learn how to set up AWS HealthLake in preparation for FHIR data imports.
- [Tutorial](https://docs.aws.amazon.com/healthlake/latest/devguide/getting-started-tutorial.html): Learn to use AWS HealthLake with a getting started tutorial.


## [Managing data stores](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-data-stores.html)

- [Creating a data store](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-data-stores-create.html): Learn how to create a data store with AWS HealthLake.
- [Getting data store properties](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-data-stores-describe.html): Learn how to describe data store properties with AWS HealthLake.
- [Listing data stores](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-data-stores-list.html): Learn how to list data stores with AWS HealthLake.
- [Tagging data stores](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-data-stores-tagging.html): Learn how to tag, list tags for, and untag data stores with AWS HealthLake.
- [Deleting a data store](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-data-stores-delete.html): Learn how to delete a data store with AWS HealthLake.


## [Managing FHIR Subscriptions](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-subscriptions.html)

- [Subscription lifecycle](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-subscriptions-lifecycle.html): Learn how the FHIR Subscription lifecyle works with AWS HealthLake.

### [Creating a Subscription](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-subscriptions-create.html)

Learn how to create a FHIR Subscription with AWS HealthLake.

- [Example Subscription payloads](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-subs-ex-sub-payload.html): Learn how to create a FHIR Subscription payload with AWS HealthLake.
- [Example notification payloads](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-subs-ex-notif-payload.html): Learn how to create a Notification payload with AWS HealthLake.
- [Searching for Subscriptions](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-subscriptions-searching.html): Learn how to search for FHIR Subscriptions with AWS HealthLake.
- [Filtering notifications](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-subscriptions-filter-notif.html): Learn how to filter notifications with AWS HealthLake.


## [Importing FHIR data](https://docs.aws.amazon.com/healthlake/latest/devguide/importing-fhir-data.html)

- [Starting an import job](https://docs.aws.amazon.com/healthlake/latest/devguide/importing-fhir-data-start.html): Learn how to start a FHIR import job with AWS HealthLake.
- [Getting import job properties](https://docs.aws.amazon.com/healthlake/latest/devguide/importing-fhir-data-describe.html): Learn how to get FHIR import job properties with AWS HealthLake.
- [Listing import jobs](https://docs.aws.amazon.com/healthlake/latest/devguide/importing-fhir-data-list.html): Learn how to list FHIR import jobs with AWS HealthLake.


## [Managing FHIR resources](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources.html)

- [Creating a resource](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources-create.html): Learn how to create a FHIR resource in AWS HealthLake.
- [Reading a resource](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources-read.html): Learn how to read a FHIR resource in AWS HealthLake.
- [Reading resource history](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources-read-history.html): Learn how to read FHIR resource history using AWS HealthLake.
- [Updating a resource](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources-update.html): Learn how to update a FHIR resource in AWS HealthLake.
- [Modifying a resource](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources-patch.html): Learn how to use the PATCH operation to modify specific elements of FHIR resources in AWS HealthLake.
- [Bundling resources](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources-bundle.html): Learn how to bundle FHIR resources in AWS HealthLake.
- [Deleting a resource](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources-delete.html): Learn how to delete a FHIR resource in AWS HealthLake.
- [Idempotency and Concurrency](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources-idempotency.html): Learn how to use idempotency keys with AWS HealthLake FHIR operations


## [Searching FHIR resources](https://docs.aws.amazon.com/healthlake/latest/devguide/searching-fhir-resources.html)

- [Searching with GET](https://docs.aws.amazon.com/healthlake/latest/devguide/searching-fhir-resources-get.html): Learn how to search for FHIR resources with GET using AWS HealthLake.
- [Searching with POST](https://docs.aws.amazon.com/healthlake/latest/devguide/searching-fhir-resources-post.html): Learn how to search FHIR resources with POST using AWS HealthLake.
- [Search Consistency Levels](https://docs.aws.amazon.com/healthlake/latest/devguide/searching-fhir-consistency-levels.html): Learn how to control search consistency levels in AWS HealthLake.


## [Exporting FHIR data](https://docs.aws.amazon.com/healthlake/latest/devguide/exporting-fhir-data.html)

- [Starting an export job](https://docs.aws.amazon.com/healthlake/latest/devguide/exporting-fhir-data-start.html): Learn about starting a FHIR export job with AWS HealthLake.
- [Getting export job properties](https://docs.aws.amazon.com/healthlake/latest/devguide/exporting-fhir-data-describe.html): Learn how to describe FHIR export job properties with AWS HealthLake.
- [Listing export jobs](https://docs.aws.amazon.com/healthlake/latest/devguide/exporting-fhir-data-list.html): Learn how to list FHIR export jobs for AWS HealthLake.


## [Code examples](https://docs.aws.amazon.com/healthlake/latest/devguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/healthlake/latest/devguide/service_code_examples_basics.html)

The following code examples show how to use the basics of HealthLake with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/healthlake/latest/devguide/service_code_examples_actions.html)

The following code examples show how to use HealthLake with AWS SDKs.

- [CreateFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_CreateFHIRDatastore_section.html): Use CreateFHIRDatastore with an AWS SDK or CLI
- [DeleteFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_DeleteFHIRDatastore_section.html): Use DeleteFHIRDatastore with an AWS SDK or CLI
- [DescribeFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_DescribeFHIRDatastore_section.html): Use DescribeFHIRDatastore with an AWS SDK or CLI
- [DescribeFHIRExportJob](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_DescribeFHIRExportJob_section.html): Use DescribeFHIRExportJob with an AWS SDK or CLI
- [DescribeFHIRImportJob](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_DescribeFHIRImportJob_section.html): Use DescribeFHIRImportJob with an AWS SDK or CLI
- [ListFHIRDatastores](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_ListFHIRDatastores_section.html): Use ListFHIRDatastores with an AWS SDK or CLI
- [ListFHIRExportJobs](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_ListFHIRExportJobs_section.html): Use ListFHIRExportJobs with an AWS SDK or CLI
- [ListFHIRImportJobs](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_ListFHIRImportJobs_section.html): Use ListFHIRImportJobs with an AWS SDK or CLI
- [ListTagsForResource](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_ListTagsForResource_section.html): Use ListTagsForResource with an AWS SDK or CLI
- [StartFHIRExportJob](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_StartFHIRExportJob_section.html): Use StartFHIRExportJob with an AWS SDK or CLI
- [StartFHIRImportJob](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_StartFHIRImportJob_section.html): Use StartFHIRImportJob with an AWS SDK or CLI
- [TagResource](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_TagResource_section.html): Use TagResource with an AWS SDK or CLI
- [UntagResource](https://docs.aws.amazon.com/healthlake/latest/devguide/example_healthlake_UntagResource_section.html): Use UntagResource with an AWS SDK or CLI


## [Integrating](https://docs.aws.amazon.com/healthlake/latest/devguide/integrating.html)

### [Natural language processing](https://docs.aws.amazon.com/healthlake/latest/devguide/integrating-nlp.html)

Learn how to integrate natural language processing (NLP) libraries with AWS HealthLake to extract meaningful health data from unstructured medical text, identify entities, and link to ontology libraries.

- [NLP libraries](https://docs.aws.amazon.com/healthlake/latest/devguide/med-example.html): HealthLake infers data found in the DocumentReference resource type using Amazon Comprehend Medical libraries.
- [Using FHIR APIs](https://docs.aws.amazon.com/healthlake/latest/devguide/nlp-rest-api.html): By default, traits detected by the Amazon Comprehend Medical API operations are not returned when making a GET request.
- [Search parameters](https://docs.aws.amazon.com/healthlake/latest/devguide/search-parameters-med.html): The following table lists the searchable attributes for HealthLake integrated NLP.
- [Example requests](https://docs.aws.amazon.com/healthlake/latest/devguide/cm-api-results.html): Example 1: Patient record ingested into a HealthLake data store

### [SQL index and query](https://docs.aws.amazon.com/healthlake/latest/devguide/integrating-athena.html)

Learn how to integrate HealthLake with Amazon Athena to query FHIR data with SQL.

- [Getting started](https://docs.aws.amazon.com/healthlake/latest/devguide/integrating-athena-getting-started.html): Learn about connecting your HealthLake data store to Athena and how you can use IAM to grant and restrict permissions to specific databases and tables.
- [Querying with SQL](https://docs.aws.amazon.com/healthlake/latest/devguide/integrating-athena-query-sql.html): Learn how to query your HealthLake data with SQL using Amazon Athena.
- [Example queries](https://docs.aws.amazon.com/healthlake/latest/devguide/integrating-athena-complex-filtering.html): The following examples demonstrate how to use Amazon Athena SQL queries with complex filtering to locate FHIR data from a HealthLake data store.


## [Monitoring](https://docs.aws.amazon.com/healthlake/latest/devguide/monitoring.html)

- [CloudTrail (API calls)](https://docs.aws.amazon.com/healthlake/latest/devguide/monitoring-cloudtrail.html): Learn how to use AWS CloudTrail with AWS HealthLake to log user activity and API usage.
- [CloudWatch (Metrics)](https://docs.aws.amazon.com/healthlake/latest/devguide/monitoring-cloudwatch.html): Learn how to use Amazon CloudWatch to observe and monitor AWS HealthLake.
- [EventBridge (Events)](https://docs.aws.amazon.com/healthlake/latest/devguide/monitoring-eventbridge.html): Learn how to use Amazon EventBridge to create scalable, event-driven applications by creating rules that route AWS HealthLake events to targets.


## [Security](https://docs.aws.amazon.com/healthlake/latest/devguide/security.html)

- [Data Protection](https://docs.aws.amazon.com/healthlake/latest/devguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS HealthLake.
- [Encryption at rest](https://docs.aws.amazon.com/healthlake/latest/devguide/encryption-at-rest.html): HealthLake provides encryption by default to protect sensitive customer data at rest by using a service owned AWS Key Management Service (AWS KMS) key.
- [Encryption in transit](https://docs.aws.amazon.com/healthlake/latest/devguide/encryption-in-transit.html): AWS HealthLake uses TLS 1.2 to encrypt data in transit through the public endpoint and through backend services.

### [Identity and access management](https://docs.aws.amazon.com/healthlake/latest/devguide/security-iam.html)

How to authenticate requests and manage access your HealthLake resources.

- [How AWS HealthLake works with IAM](https://docs.aws.amazon.com/healthlake/latest/devguide/security_iam_service-with-iam.html): Before you use IAM to manage access to HealthLake, learn what IAM features are available to use with HealthLake.
- [Identity-based policy examples](https://docs.aws.amazon.com/healthlake/latest/devguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify HealthLake resources.
- [AWS managed policies](https://docs.aws.amazon.com/healthlake/latest/devguide/security-iam-awsmanpol.html): Learn about AWS managed policies for HealthLake and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/healthlake/latest/devguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with HealthLake and IAM.
- [Compliance validation](https://docs.aws.amazon.com/healthlake/latest/devguide/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Infrastructure security](https://docs.aws.amazon.com/healthlake/latest/devguide/infrastructure-security.html): Learn how AWS HealthLake isolates service traffic.
- [Infrastructure as code](https://docs.aws.amazon.com/healthlake/latest/devguide/creating-resources-with-cloudformation.html): Learn about how to create resources for AWS HealthLake using an AWS CloudFormation template.
- [VPC endpoints](https://docs.aws.amazon.com/healthlake/latest/devguide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and AWS HealthLake without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Best practices](https://docs.aws.amazon.com/healthlake/latest/devguide/best-practices-security.html): Learn the best security practices for AWS HealthLake.
- [Resilience](https://docs.aws.amazon.com/healthlake/latest/devguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS HealthLake features for data resiliency.


## [Reference](https://docs.aws.amazon.com/healthlake/latest/devguide/reference.html)

### [SMART on FHIR](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-smart-on-fhir.html)

Learn about SMART on FHIR support for AWS HealthLake, including authentication requirements, supported scopes, token validation, fine-grained authorization, discovery document, and code examples.

- [Getting started](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-smart-on-fhir-getting-started.html): This topic provides the information necessary to get started with SMART on FHIR authentication for AWS HealthLake.
- [Authentication](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-smart-on-fhir-authentication.html): This topic provides the information necessary to configure an authentication server to work with AWS HealthLake.
- [OAuth 2.0 scopes](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-smart-on-fhir-oauth-scopes.html): HealthLake uses OAuth 2.0 as an authorization protocol.
- [Token validation](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-smart-on-fhir-token-validation.html): When you create a HealthLake SMART on FHIR enabled data store, you must provide the ARN of the AWS Lambda function in the CreateFHIRDatastore request.
- [Fine-grained authorization](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-smart-on-fhir-fine-grained-authorization.html): Scopes alone do not provide you with the necessary specificity about what data a requester is authorized to access in a data store.
- [Discovery Document](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-smart-on-fhir-discovery-document.html): SMART defines a Discovery Document that allows clients to learn the authorization endpoint URLs and features a HealthLake data store supports.
- [Request example](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-smart-on-fhir-request-example.html): You can make FHIR REST API requests on a SMART on FHIR-enabled HealthLake data store.

### [FHIR R4](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir.html)

Learn about FHIR R4 support for AWS HealthLake, including reference material for supported capability statement, profile validations, resource types, search parameters, and operations.

- [Capability Statement](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-capability-statement.html): Learn about the AWS HealthLake Capability Statement for FHIR R4 support.
- [Profile validations](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-profile-validations.html): Learn about FHIR profile validations for AWS HealthLake.
- [Resource types](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-resource-types.html): Learn about FHIR R4 resource types supported by AWS HealthLake.
- [Search parameters](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-search-parameters.html): Learn about FHIR R4 search parameters for AWS HealthLake.

### [$Operations](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations.html)

Learn about supported FHIR R4 operations for AWS HealthLake.

- [$attribution-status](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-attribution-status.html): Learn about the FHIR R4 $attribution-status operation for AWS HealthLake.
- [$bulk-delete](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-bulk-delete.html): Learn how to use the $bulk-delete operation to delete all resources of a specific type in AWS HealthLake.
- [$confirm-attribution-list](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-confirm-attribution-list.html): Learn about the FHIR R4 $confirm-attribution-list operation for AWS HealthLake.
- [$davinci-data-export](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-davinci-data-export.html): Learn about the FHIR R4 $davinci-data-export operation for AWS HealthLake.
- [$document](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-document.html): Learn how to use the $document operation to generate complete clinical documents from Composition resources in AWS HealthLake.
- [$erase](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-erase.html): Learn how to use the $erase operation to permanently delete specific resources and their history versions in AWS HealthLake.
- [$everything](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-everything.html): The Patient/$everything operation is used to query a FHIR Patient resource, along with any other resources related to that Patient.
- [$expand](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-expand.html): Learn how to use the $expand operation to retrieve the complete list of codes contained within ValueSet resources in AWS HealthLake.
- [$export](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-export.html): Learn how to use the FHIR $export operation to export data from your HealthLake data store.
- [$inquire](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-inquire.html): Learn how to use the FHIR $inquire operation to check the status of prior authorization requests.
- [$lookup](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-lookup.html): Learn how to use the $lookup operation to retrieve details about specific concepts in CodeSystem resources in AWS HealthLake.
- [$member-add](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-member-add.html): Learn about the $member-add operation for AWS HealthLake.
- [$member-match](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-member-match.html): Learn about the $member-match operation for AWS HealthLake.
- [$member-remove](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-member-remove.html): Learn about the $member-remove operation for AWS HealthLake.
- [$purge](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-purge.html): Learn how to use the $purge operation to permanently delete all resources within a patient's compartment in AWS HealthLake.
- [$questionnaire-package](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-questionnaire-package.html): Learn how to use the FHIR $questionnaire-package operation to retrieve questionnaire packages with dependencies.
- [$submit](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-submit.html): Learn how to use the FHIR $submit operation to submit prior authorization requests.
- [$validate](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-validate.html): Learn how to use the $validate operation to validate FHIR resources against specifications and profiles in AWS HealthLake.

### [Compliance](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-compliance.html)

Learn about compliance features and requirements for AWS HealthLake.

- [CMS](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-compliance-cms.html): Learn about AWS HealthLake features that support CMS interoperability and compliance requirements.

### [HealthLake](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-healthlake.html)

Learn about reference material for AWS HealthLake service endpoints, service quotas, and samples projects.

- [Endpoints and quotas](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-healthlake-endpoints-quotas.html): Learn about AWS HealthLake service endpoints and quotas.
- [Preloaded data types](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-healthlake-preloaded-data-types.html): Learn about Synthea preloaded data types for AWS HealthLake.
- [Sample projects](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-healthlake-sample-projects.html): Learn about sample blogs and sample projects for AWS HealthLake.
- [Troubleshooting](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-healthlake-troubleshooting.html): Learn how to troubleshoot common issues for AWS HealthLake.
- [Working with AWS SDKs](https://docs.aws.amazon.com/healthlake/latest/devguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.
