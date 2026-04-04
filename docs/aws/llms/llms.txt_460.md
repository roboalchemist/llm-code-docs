# Source: https://docs.aws.amazon.com/inspector/latest/user/llms.txt

# Amazon Inspector User Guide

> Amazon Inspector is a vulnerability management service that automatically discovers workloads and continually scans them for software vulnerabilities and unintended network exposure.

- [What is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)
- [Dashboard](https://docs.aws.amazon.com/inspector/latest/user/understanding-dashboard.html)
- [Searching the vulnerability database](https://docs.aws.amazon.com/inspector/latest/user/vulnerability-search.html)
- [Exporting SBOMs](https://docs.aws.amazon.com/inspector/latest/user/sbom-export.html)
- [EventBridge schema](https://docs.aws.amazon.com/inspector/latest/user/eventbridge-integration.html)
- [SSM plugin](https://docs.aws.amazon.com/inspector/latest/user/inspector-ssm-plugin.html)
- [Assessing coverage](https://docs.aws.amazon.com/inspector/latest/user/assessing-coverage.html)
- [Usage](https://docs.aws.amazon.com/inspector/latest/user/usage.html)
- [Supported operating systems and programming languages](https://docs.aws.amazon.com/inspector/latest/user/supported.html)
- [Deactivating Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/deactivating-best-practices.html)
- [Quotas](https://docs.aws.amazon.com/inspector/latest/user/quotas.html)
- [Regions and endpoints](https://docs.aws.amazon.com/inspector/latest/user/inspector_regions.html)
- [Document history](https://docs.aws.amazon.com/inspector/latest/user/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/inspector/latest/user/glossary.html)

## [Getting started](https://docs.aws.amazon.com/inspector/latest/user/getting_started.html)

- [Getting started tutorial: Activating Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html): Complete the tutorial to activate Amazon Inspector.


## [Automated scans](https://docs.aws.amazon.com/inspector/latest/user/scanning-resources.html)

- [Activating a scan type](https://docs.aws.amazon.com/inspector/latest/user/activate-scans.html): Learn about how to activate a scan type.

### [Amazon EC2 instance scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-ec2.html)

Learn how Amazon Inspector scans Amazon EC2 instances and how to configure instances for scans.

- [Deep inspection for Linux instances](https://docs.aws.amazon.com/inspector/latest/user/deep-inspection.html): Learn about how to manage Amazon Inspector deep inspection for Amazon EC2 Linux instances.
- [Scanning Windows EC2 instance](https://docs.aws.amazon.com/inspector/latest/user/windows-scanning.html): Learn about how to scan Windows Amazon EC2 instances with Amazon Inspector.

### [Amazon ECR container image scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html)

Learn about which images in Amazon Elastic Container Registry that Amazon Inspector scans and how to configure Amazon ECR scanning.

- [Configuring the Amazon ECR re-scan duration](https://docs.aws.amazon.com/inspector/latest/user/scanning_resources_configure_duration_setting_ecr.html): Learn how Amazon Inspector discovers and monitors AWS resources and the different scan type options.

### [Lambda function scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html)

Learn about how to scan Lambda functions with Amazon Inspector.

### [Amazon Inspector Lambda standard scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning_resources_lambda.html)

Learn about Amazon Inspector Lambda standard scanning.

- [Excluding functions from Lambda standard scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning_resources_lambda_exclude_functions.html): Learn about how to exclude functions from Lambda standard scanning.

### [Amazon Inspector Lambda code scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning_resources_lambda_code.html)

Learn about Amazon Inspector Lambda code scanning.

- [Excluding functions from Lambda code scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning_resources_lambda_code_exclude_functions.html): Learn about how to exclude functions from Lambda code scanning
- [Deactivating a scan type](https://docs.aws.amazon.com/inspector/latest/user/deactivate-scans.html): Learn about how to deactivate a scan type in Amazon Inspector.


## [CIS scans](https://docs.aws.amazon.com/inspector/latest/user/scanning-cis.html)

- [Creating a CIS scan configuration](https://docs.aws.amazon.com/inspector/latest/user/scanning-cis-create-cis-scan-configuration.html): Learn about how to create a CIS scan configuration
- [Viewing CIS scan results](https://docs.aws.amazon.com/inspector/latest/user/scanning-cis-view-cis-scan-configuration.html): Learn about how to details for a CIS scan.
- [Editing a CIS scan configuration](https://docs.aws.amazon.com/inspector/latest/user/scanning-cis-view-edit-cis-scan-configuration.html): Learn about how to view and edit a CIS scan configuration
- [Downloading a CIS scan results](https://docs.aws.amazon.com/inspector/latest/user/scanning-cis-view-download-cis-scan-configuration.html): Learn about how to download a CIS scan configuration


## [Amazon Inspector Code Security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html)

### [Prerequisites](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-prerequisites.html)

Describes the prerequisites for Code Security.

- [Activating Code Security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-activate.html): Learn about how to activate Code Security.
- [Creating a customer managed key to access AWS KMS](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-creating-a-key.html): Learn about using a customer managed key for Amazon Inspector Code Security.

### [Creating an integration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-create-integration.html)

Learn about how to create an integration.

- [Creating an integration for GitHub](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-connect-github.html): Learn about how to create a connection for Code Security
- [Creating an integration for GitLab Self Managed](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-connect-gitlab.html): Learn about how to create a connection for Code Security
- [Viewing integrations](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-connect-view-integrations.html): Learn about how to view code integrations.

### [Viewing code repositories](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-connect-view-repositories.html)

Learn about how to view code repositories

- [Viewing details for a project](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-connect-view-details-for-repositories.html): Learn about how to view details for a project.
- [Deleting an integration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-connect-delete-integrations.html): Learn about how to delete an integration.

### [Creating a scan configuration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-create-configuration.html)

Learn about how to create a scan configuration for Amazon Inspector Code Security.

### [Viewing scan configurations](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-view-configurations.html)

Learn about how to view scan configurations.

- [Viewing details for a scan configuration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-view-details-for-configurations.html): Learn about how to view details for a scan configuration.
- [Editing a scan configuration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-edit-configuration.html): Learn about how to edit a scan configuration.
- [Deleting a scan configuration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-delete-configuration.html): Learn about how to delete a scan configuration
- [Performing an on-demand scan](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-on-demand-scan.html): Learn about how to perform an on-demand scan.
- [Supported languages](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-supported-languages.html): Learn about how to use Amazon Inspector code security
- [Deactivating Code Security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-deactivate.html): Learn about how to activate Code Security.


## [Understanding findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding.html)

- [Finding types](https://docs.aws.amazon.com/inspector/latest/user/findings-types.html): Learn about the different Amazon Inspector finding types.
- [Viewing findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-locating-analyzing.html): Learn about how to view findings in the Amazon Inspector console and with the Amazon Inspector API.
- [Viewing finding details](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-details.html): Learn about how to view details for Amazon Inspector findings.
- [Viewing the Amazon Inspector score](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-score.html): Learn about how to interpret the Amazon Inspector score and understand vulnerability intelligence details in the console.
- [Understanding severity levels for findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html): Learn about the different severity levels for Amazon Inspector findings.


## [Managing findings](https://docs.aws.amazon.com/inspector/latest/user/findings-managing.html)

- [Filtering findings](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-filtering.html): Learn about how to filter your Amazon Inspector findings.
- [Suppressing findings](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-supression-rules.html): Learn how to create suppression rules to hide unwanted findings from results
- [Exporting findings reports](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-exporting-reports.html): Learn about how to export Amazon Inspector findings reports.
- [Automating responses to findings with EventBridge](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-automating-responses.html): Learn about how to use Amazon EventBridge to route events from Amazon Inspector, and learn how to create an Amazon EventBridge rule to send notifications about findings through SNS, Amazon Chime, or Slack.


## [Amazon Inspector SBOM Generator](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator.html)

- [Previous versions](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-versions.html): Access links to previous versions of the Amazon Inspector SBOM Generator.
- [Operating system collection](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-operating-system-collection.html): Learn about the operating systems the Amazon Inspector SBOM Generator support.
- [Dependency collection](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-dependency-collection.html): Learn about the dependencies the Amazon Inspector SBOM Generator support.
- [Ecosystem collection](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-ecosystem-collection.html): Learn about the dependencies the Amazon Inspector SBOM Generator support.
- [SSL/TLS certificate scans](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-ssl-tls-certificate-scans.html): Learn about SSL/TLS certificate scans.
- [License collection](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html): Learn about the licenses Amazon Inspector SBOM Generator support.
- [Package URLs](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-purl-sbom.html): Learn about package URLs.
- [Version references](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-unresolved-non-standard-version-reference.html): Learn about how to handle unresolved or non-standard version references.
- [Using CycloneDX namespaces](https://docs.aws.amazon.com/inspector/latest/user/cyclonedx-namespace.html): Learn about the CycloneDX namespaces that Amazon Inspector provides.


## [CI/CD integration](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html)

- [Set up an account for CI/CD integration](https://docs.aws.amazon.com/inspector/latest/user/configure-cicd-account.html): Learn about how to set up an AWS account with an IAM role that allows you to use the Amazon Inspector CI/CD integration.
- [Amazon Inspector Dockerfile checks](https://docs.aws.amazon.com/inspector/latest/user/dockerfile-checks.html): Learn about how Amazon Inspector scans Dockerfiles and Docker container images.
- [Creating a custom CI/CD integration](https://docs.aws.amazon.com/inspector/latest/user/cicd-custom.html): Learn about how to create your own custom CI/CD integration for your pipeline using Amazon Inspector Scan.
- [Jenkins plugin](https://docs.aws.amazon.com/inspector/latest/user/cicd-jenkins.html): Learn about how to integrate Amazon Inspector scans into your Jenkins pipeline.
- [TeamCity plugin](https://docs.aws.amazon.com/inspector/latest/user/cicd-teamcity.html): Learn how to integrate Amazon Inspector scans into your TeamCity pipeline.
- [GitHub actions](https://docs.aws.amazon.com/inspector/latest/user/cicd-inspector-github-actions.html): Learn about how to use GitHub actions with Amazon Inspector.
- [GitLab components](https://docs.aws.amazon.com/inspector/latest/user/cicd-inspector-gitlab-components.html): Learn about how to use GitLab components with Amazon Inspector.
- [Using CodeCatalyst actions](https://docs.aws.amazon.com/inspector/latest/user/cicd-inspector-codecatalyst-actions.html): Learn about how to use CodeCatalyst actions in Amazon Inspector vulnerability scans.
- [Using Amazon Inspector Scan actions](https://docs.aws.amazon.com/inspector/latest/user/cicd-inspector-codepipeline-actions.html): Learn about how to use Amazon Inspector Scan actions with CodePipeline.


## [Managing multiple accounts](https://docs.aws.amazon.com/inspector/latest/user/managing-multiple-accounts.html)

- [Understanding the delegated administrator account and member account](https://docs.aws.amazon.com/inspector/latest/user/admin-member-relationship.html): Learn about the differences between a delegated administrator account and member account in Amazon Inspector.

### [Designating an administrator account](https://docs.aws.amazon.com/inspector/latest/user/designating-admin.html)

Learn about how to designate a delegated administrator account for Amazon Inspector.

- [Activating Amazon Inspector scans for member accounts](https://docs.aws.amazon.com/inspector/latest/user/adding-member-accounts.html): Learn about how to activate Amazon EC2 scanning and Amazon ECR scanning for member accounts.
- [Disassociating member accounts](https://docs.aws.amazon.com/inspector/latest/user/disassociating-member-accounts.html): Learn about how to disassociate a member account .
- [Removing the delegated administrator](https://docs.aws.amazon.com/inspector/latest/user/remove-delegated-admin.html): Learn about how to remove a delegated administrator in Amazon Inspector.


## [Tagging resources](https://docs.aws.amazon.com/inspector/latest/user/tagging-resources.html)

- [Tagging fundamentals](https://docs.aws.amazon.com/inspector/latest/user/tagging-fundamentals.html): Learn about tagging fundamentals.
- [Adding tags](https://docs.aws.amazon.com/inspector/latest/user/tagging-add.html): Learn about how to agg a tag to an Amazon Inspector resource.
- [Removing tags](https://docs.aws.amazon.com/inspector/latest/user/tagging-remove.html): Learn about how to remove a tag from an Amazon Inspector resource.


## [Security](https://docs.aws.amazon.com/inspector/latest/user/security.html)

### [Data protection](https://docs.aws.amazon.com/inspector/latest/user/data-protection.html)

Learn about how the AWS shared responsibility model applies to data protection in Amazon Inspector

- [Encryption at rest](https://docs.aws.amazon.com/inspector/latest/user/encryption-rest.html): Learn about the default encryption options for data Amazon Inspector collects.
- [Encryption in transit](https://docs.aws.amazon.com/inspector/latest/user/encryption-transit.html): Learn about how AWS encrypts data in transit between AWS internal systems.

### [Identity and Access Management](https://docs.aws.amazon.com/inspector/latest/user/security-iam.html)

How to authenticate requests and manage access to your Amazon Inspector resources.

- [How Amazon Inspector works with IAM](https://docs.aws.amazon.com/inspector/latest/user/security_iam_service-with-iam.html): Learn about how IAM works with Amazon Inspector.
- [Identity-based policy examples](https://docs.aws.amazon.com/inspector/latest/user/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Inspector resources.
- [AWS managed policies](https://docs.aws.amazon.com/inspector/latest/user/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Inspector and recent changes to those policies.

### [Using service-linked roles](https://docs.aws.amazon.com/inspector/latest/user/using-service-linked-roles.html)

How to use service-linked roles to give Amazon Inspector access to resources in your AWS account.

- [Service-linked role permissions for Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/slr-permissions.html): Amazon Inspector uses the managed policy named AWSServiceRoleForAmazonInspector2.
- [Service-linked role permissions for Amazon Inspector agentless scans](https://docs.aws.amazon.com/inspector/latest/user/slr-permissions-agentless.html): Amazon Inspector agentless scanning uses the service-linked role named AWSServiceRoleForAmazonInspector2Agentless.
- [Troubleshooting](https://docs.aws.amazon.com/inspector/latest/user/security_iam_troubleshoot.html): Learn about how to diagnose and fix common issues you might encounter when working with Amazon Inspector and IAM.

### [Monitoring Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/monitoring-overview.html)

Learn about the importance of monitoring in Amazon Inspector.

- [CloudTrail logs](https://docs.aws.amazon.com/inspector/latest/user/logging-using-cloudtrail.html): Learn about logging Amazon Inspector with AWS CloudTrail.
- [Compliance validation](https://docs.aws.amazon.com/inspector/latest/user/inspector-compliance.html): Learn about how AWS services within the scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/inspector/latest/user/disaster-recovery-resiliency.html): Learn about how the AWS architecture supports data redundancy, and learn about specific Amazon Inspector features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/inspector/latest/user/infrastructure-security.html): Learn about how Amazon Inspector isolates service traffic.
- [Incident response](https://docs.aws.amazon.com/inspector/latest/user/security-incident-response.html): Learn about how Amazon Inspector responds to security incidents.
- [AWS PrivateLink](https://docs.aws.amazon.com/inspector/latest/user/vpc-interface-endpoints-inspector.html): You can use an AWS PrivateLink to create a private connection between your VPC and Amazon Inspector.


## [Integrations](https://docs.aws.amazon.com/inspector/latest/user/integrations.html)

- [Amazon ECR integration](https://docs.aws.amazon.com/inspector/latest/user/ecr-integration.html): Learn about how to use the Amazon Inspector integration with Amazon Elastic Container Registry (Amazon ECR).
- [Security Hub CSPM integration](https://docs.aws.amazon.com/inspector/latest/user/securityhub-integration.html): Learn about how to use the Amazon Inspector integration with AWS Security Hub CSPM.
