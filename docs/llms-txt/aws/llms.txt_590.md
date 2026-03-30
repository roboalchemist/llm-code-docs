# Source: https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/llms.txt

# Migration Hub Strategy Recommendations User Guide

- [AWS Migration Hub availability change](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/migrationhub-availability-change.html)
- [Setting up](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/setting-up.html)
- [Quotas](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/quotas.html)
- [Release notes](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/release-notes.html)
- [Document history](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/doc-ver-history.html)

## [What is Migration Hub Strategy Recommendations?](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/what-is-mhub-strategy.html)

- [Overview](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/overview.html): Gives an overview of Strategy Recommendations


## [Getting started](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/getting-started-prerequisites.html): Prerequisites for using Strategy Recommendations.
- [Step 1: Download the collector](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/getting-started-dowmload-collector.html): Migration Hub Strategy Recommendations application data collector is a virtual appliance that you can install in your on-premises VMware environment.
- [Step 2: Deploy the collector](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/getting-started-deploy.html): This section describes how to deploy the Strategy Recommendations application data collector.
- [Step 3: Sign in to the collector](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/getting-started-login-vm.html): This section describes how to sign in to the deployed Migration Hub Strategy Recommendations application data collector.
- [Step 4: Set up the collector](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/getting-started-collector-setup.html): Describes how to set up the Strategy Recommendations application data collector using the AWS CLI.
- [Step 5: Get recommendations](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/getting-started-get-recommendations.html): Learn how to use Strategy Recommendations in the Migration Hub console to get migration recommendations for the first time.


## [Recommendations](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/recommendations.html)

- [Viewing strategy recommendations](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/viewing-recommendations.html): How to view migration and modernization initiative recommendations in Strategy Recommendations.

### [Application component recommendations](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/recommendations-app-components.html)

Learn how to view migration strategy recommendations for application components in Strategy Recommendations.

- [Working with application components](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/recommendations-view-app-components.html): How to view and configure migration and modernization recommendations for application components in Strategy Recommendations.
- [Source code analysis](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/source-code-analysis.html): Learn about using Strategy Recommendations to analyze source code that you are migrating to AWS.
- [Database analysis](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/database-analysis.html): Learn about using Strategy Recommendations to analyze databases that you are migrating.
- [Binary analysis](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/binary-analysis.html): Migration Hub Strategy Recommendations automatically identifies the applications in your portfolio and the application components that belong to them.
- [Server recommendations](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/recommendations-servers.html): How to view server migration and modernization recommendations in Strategy Recommendations.
- [Preferences](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/recommendations-preferences.html): Learn how to view and edit Strategy Recommendations preferences.


## [Data sources](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/data-sources.html)

- [Viewing data sources](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/viewing-data-sources.html): Describes how to view Strategy Recommendations data sources.
- [Application data collector](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/application-data-collector.html): Learn about the Strategy Recommendations application data collector.
- [Importing data](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/importing-data.html): Describes how to use the application import template to import data into Strategy Recommendations in the Migration Hub console.
- [Removing data](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/removing-data.html): Describes how to remove your data from Strategy Recommendations.


## [Security](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Strategy Recommendations.

### [Identity and access management](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Strategy Recommendations resources.

- [How Migration Hub Strategy Recommendations works with IAM](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/security_iam_service-with-iam.html): Describes how Strategy Recommendations works with IAM.
- [AWS managed policies](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Strategy Recommendations and recent changes to those policies.
- [Identity-based policy examples](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Strategy Recommendations resources.
- [Troubleshooting](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Strategy Recommendations and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give Strategy Recommendations access to resources in your AWS account.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create private connections between your VPC and Strategy Recommendations.
- [Compliance validation](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.


## [Working with other services](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/service-integrations.html)

- [AWS CloudTrail](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/logging-using-cloudtrail.html): Learn about logging Migration Hub Strategy Recommendations with AWS CloudTrail.
