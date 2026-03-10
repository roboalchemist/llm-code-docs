# Source: https://docs.aws.amazon.com/entityresolution/latest/userguide/llms.txt

# AWS Entity Resolution User Guide

> Provides a conceptual overview of AWS Entity Resolution and offers step-by-step instructions for matching and resolving data.

- [What is AWS Entity Resolution?](https://docs.aws.amazon.com/entityresolution/latest/userguide/what-is-service.html)
- [AWS CloudFormation resources](https://docs.aws.amazon.com/entityresolution/latest/userguide/creating-resources-with-cloudformation.html)
- [Quotas](https://docs.aws.amazon.com/entityresolution/latest/userguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/entityresolution/latest/userguide/doc-history.html)
- [Glossary](https://docs.aws.amazon.com/entityresolution/latest/userguide/glossary.html)

## [Setting up](https://docs.aws.amazon.com/entityresolution/latest/userguide/setting-up.html)

- [Creating an IAM role for a console user](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-iam-role.html): Learn how to create an IAM role for using the AWS Entity Resolution console.
- [Creating a workflow job role](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-workflow-job-role.html): Learn how to create a workflow job role to run a workflow in AWS Entity Resolution.


## [Prepare input data tables](https://docs.aws.amazon.com/entityresolution/latest/userguide/prepare-data-tables.html)

- [Preparing first-party input data](https://docs.aws.amazon.com/entityresolution/latest/userguide/prepare-input-data.html): Learn how to prepare first-party data tables for use in AWS Entity Resolution.
- [Preparing third-party input data](https://docs.aws.amazon.com/entityresolution/latest/userguide/prepare-third-party-input-data.html): Learn how to prepare third-party data tables for use in AWS Entity Resolution.


## [Schema mapping](https://docs.aws.amazon.com/entityresolution/latest/userguide/schema-mapping.html)

- [Creating a schema mapping](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-schema-mapping.html): Learn how to prepare and define your data input in AWS Entity Resolution by creating a schema mapping.
- [Cloning a schema mapping](https://docs.aws.amazon.com/entityresolution/latest/userguide/clone-schema-mapping.html): Learn how to clone a schema mapping in AWS Entity Resolution.
- [Editing a schema mapping](https://docs.aws.amazon.com/entityresolution/latest/userguide/edit-schema-mapping.html): Learn how to edit a schema mapping in AWS Entity Resolution.
- [Deleting a schema mapping](https://docs.aws.amazon.com/entityresolution/latest/userguide/delete-schema-mapping.html): Learn how to delete a schema mapping in AWS Entity Resolution.


## [ID namespace](https://docs.aws.amazon.com/entityresolution/latest/userguide/id-namespace.html)

### [ID namespace source](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-source.html)

Learn how to create an ID namespace source in AWS Entity Resolution.

- [Creating an ID namespace source (rule-based)](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-source-rule-based.html): Learn how to create an ID namespace source using the rule-based method in AWS Entity Resolution.
- [Creating an ID namespace source (provider services)](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-source-provider-services.html): Learn how to create an ID namespace source using the provider services method in AWS Entity Resolution.

### [ID namespace target](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-target.html)

Learn how to create an ID namespace target in AWS Entity Resolution.

- [Creating an ID namespace target (rule-based method)](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-target-rule-based.html): Learn how to create an ID namespace target using the rule-based method in AWS Entity Resolution.
- [Creating an ID namespace target (provider services method)](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-target-provider-services.html): Learn how to create an ID namespace target using the provider services method in AWS Entity Resolution.
- [Editing an ID namespace](https://docs.aws.amazon.com/entityresolution/latest/userguide/edit-id-namespaces.html): Learn how to edit an ID namespace in AWS Entity Resolution.
- [Deleting an ID namespace](https://docs.aws.amazon.com/entityresolution/latest/userguide/delete-id-namespace.html): Learn how to delete an ID namespace in AWS Entity Resolution.
- [Adding or updating a resource policy for an ID namespace](https://docs.aws.amazon.com/entityresolution/latest/userguide/add-update-resource-policy-id-namespace.html): Learn how to add or update a resource policy to allow access to your ID namespace in AWS Entity Resolution.


## [Matching workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-matching-workflow.html)

### [Creating a rule-based matching workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/creating-matching-workflow-rule-based.html)

Learn how to create a rule-based matching workflow with AWS Entity Resolution.

- [Advanced rule type](https://docs.aws.amazon.com/entityresolution/latest/userguide/rule-based-mw-advanced.html): Learn how to create rule-based matching workflows in AWS Entity Resolution using Advanced rule types to identify and match related records across your datasets.
- [Simple rule type](https://docs.aws.amazon.com/entityresolution/latest/userguide/rule-based-mw-simple.html): Learn how to create rule-based matching workflows in AWS Entity Resolution using Advanced rule types to identify and match related records across your datasets.
- [Creating a machine learning-based matching workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-matching-workflow-ml.html): Learn how to create a machine learning-based matching workflow with AWS Entity Resolution.
- [Creating a provider service-based matching workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-matching-workflow-provider.html): Learn how to create a provider service-based matching workflow with AWS Entity Resolution.
- [Editing a matching workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/edit-matching-workflow.html): Learn how to edit a matching workflow with AWS Entity Resolution.
- [Deleting a matching workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/delete-matching-workflow.html): Learn how to delete a matching workflow with AWS Entity Resolution.
- [Modifying or generating a Match ID](https://docs.aws.amazon.com/entityresolution/latest/userguide/generate-match-id.html): Learn how to find, modify, or generate Match IDs for rule-based matching workflows in AWS Entity Resolution using the console or API.
- [Looking up a Match ID](https://docs.aws.amazon.com/entityresolution/latest/userguide/find-match-id.html): Learn how to find a Match ID for a rule-based matching workflow with AWS Entity Resolution.
- [Deleting records from a rule-based or ML-based matching workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/delete-records.html): Learn how to delete records from a rule-based or ML-based matching workflow with AWS Entity Resolution.
- [Troubleshooting](https://docs.aws.amazon.com/entityresolution/latest/userguide/troubleshooting.html): Identify, diagnose, and resolve problems or issues they may encounter when using AWS Entity Resolution.


## [ID mapping workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-mapping-workflow.html)

### [ID mapping workflow for one AWS account](https://docs.aws.amazon.com/entityresolution/latest/userguide/creating-id-mapping-workflow-same-account.html)

Learn how to create an ID mapping workflow for one AWS account using the rule-based ID mapping method in AWS Entity Resolution.

- [Prerequisites](https://docs.aws.amazon.com/entityresolution/latest/userguide/id-mapping-workflow-prerequisite.html): Learn how to complete the prerequisites for an ID mapping workflow for one AWS account using either the rule-based or provider services ID mapping method in AWS Entity Resolution.
- [Creating an ID mapping workflow (rule-based)](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-IDMW-rule-based-one-acct.html): Learn how create an ID mapping workflow for one AWS account using the rule-based ID mapping method in AWS Entity Resolution.
- [Creating an ID mapping workflow (provider services)](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-IDMW-provider-services-one-acct.html): Learn how to create an ID mapping workflow for one AWS account using the provider services ID mapping method in AWS Entity Resolution.

### [ID mapping workflow across two AWS accounts](https://docs.aws.amazon.com/entityresolution/latest/userguide/creating-id-mapping-workflow-two-accounts.html)

Learn how to create an ID mapping workflow across two AWS accounts in AWS Entity Resolution.

- [Prerequisites](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-idmw-two-accounts-prerequisite.html): Learn how to complete the prerequisites for an ID mapping workflow for two AWS accounts using either the rule-based or provider services ID mapping method in AWS Entity Resolution.
- [Creating an ID mapping workflow (rule-based)](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-mapping-workflow-procedure.html): Learn how create an ID mapping workflow for two AWS accounts using the rule-based ID mapping method in AWS Entity Resolution.
- [Creating an ID mapping workflow (provider services)](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-mapping-workflow-provider-services.html): Learn how create an ID mapping workflow for two AWS accounts using the provider services ID mapping method in AWS Entity Resolution.
- [Running an ID mapping workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/run-id-mapping-workflow.html): Learn how to run an ID mapping workflow in AWS Entity Resolution.
- [Running a custom ID mapping workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/run-workflow-new-output-destination.html): Learn how to run an ID mapping workflow with a new output destination in AWS Entity Resolution.
- [Editing an ID mapping workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/edit-id-mapping-workflow.html): Learn how to edit an ID mapping workflow in AWS Entity Resolution.
- [Deleting an ID mapping workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/delete-id-mapping-workflow.html): Learn how to delete an ID mapping workflow in AWS Entity Resolution.
- [Adding or updating a resource policy for an ID mapping workflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/add-update-resource-policy-id-mapping.html): Learn how to add or update a resource policy to provide access to your an ID mapping workflow in AWS Entity Resolution.


## [Provider integration](https://docs.aws.amazon.com/entityresolution/latest/userguide/provider-integration.html)

- [Requirements](https://docs.aws.amazon.com/entityresolution/latest/userguide/requirements.html): Learn about the requirements you need to complete before integrating with AWS Entity Resolution as a provider.
- [Using the OpenAPI specification](https://docs.aws.amazon.com/entityresolution/latest/userguide/entity-resolution-open-api.html): Learn how to use the OpenAPI specification to integrate with AWS Entity Resolution.
- [Testing a provider integration](https://docs.aws.amazon.com/entityresolution/latest/userguide/testing-provider-integration.html): Learn how to test a provider integration with AWS Entity Resolution.


## [Security](https://docs.aws.amazon.com/entityresolution/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/entityresolution/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS Entity Resolution.

- [AWS PrivateLink](https://docs.aws.amazon.com/entityresolution/latest/userguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and AWS Entity Resolution.

### [Identity and access management](https://docs.aws.amazon.com/entityresolution/latest/userguide/security-iam.html)

How to authenticate requests and manage access your AWS Entity Resolution resources.

- [How AWS Entity Resolution works with IAM](https://docs.aws.amazon.com/entityresolution/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Entity Resolution, learn what IAM features are available to use with AWS Entity Resolution.
- [Identity-based policy examples](https://docs.aws.amazon.com/entityresolution/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS Entity Resolution resources.
- [AWS managed policies](https://docs.aws.amazon.com/entityresolution/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Entity Resolution and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/entityresolution/latest/userguide/security_iam_troubleshoot.html): Learn how to troubleshoot issues with AWS Entity Resolution identity and access.
- [Compliance validation](https://docs.aws.amazon.com/entityresolution/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/entityresolution/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Entity Resolution features for data resiliency.


## [Monitoring](https://docs.aws.amazon.com/entityresolution/latest/userguide/monitoring-overview.html)

- [CloudTrail logs](https://docs.aws.amazon.com/entityresolution/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS Entity Resolution with AWS CloudTrail.
- [CloudWatch Logs](https://docs.aws.amazon.com/entityresolution/latest/userguide/cloudwatch-logs.html): Learn how to monitor and analyze AWS Entity Resolution workflows using Amazon CloudWatch Logs.
