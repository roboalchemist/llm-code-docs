# Source: https://docs.aws.amazon.com/dtconsole/latest/userguide/llms.txt

# Developer Tools console User Guide

> Create and manage notifications for events in AWS CodeCommit, AWS CodeBuild, AWS CodeDeploy and AWS CodePipeline.

- [Connections rename - Summary of changes](https://docs.aws.amazon.com/dtconsole/latest/userguide/rename.html)
- [Document history](https://docs.aws.amazon.com/dtconsole/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/dtconsole/latest/userguide/glossary.html)

## [What is the Developer Tools console?](https://docs.aws.amazon.com/dtconsole/latest/userguide/what-is-dtconsole.html)

### [What are notifications?](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome.html)

Introduces a notification feature that you can use to subscribe to events in AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, and AWS CodePipeline.

- [Notification concepts](https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html): Learn about important notification concepts.

### [Setting up](https://docs.aws.amazon.com/dtconsole/latest/userguide/setting-up.html)

Set up notifications so you can monitor activity on builds, pipelines, and repositories.

- [Configure Amazon SNS topics for notifications](https://docs.aws.amazon.com/dtconsole/latest/userguide/set-up-sns.html): The easiest way to set up notifications is to create an Amazon SNS topic when you create a notification rule.
- [Subscribe users to Amazon SNS topics that are targets](https://docs.aws.amazon.com/dtconsole/latest/userguide/subscribe-users-sns.html): Before users can receive notifications, they must be subscribed to the Amazon SNS topic that is the target of the notification rule.

### [Getting started with notifications](https://docs.aws.amazon.com/dtconsole/latest/userguide/getting-started.html)

Get started with notifications by setting up a notification rule on a build, deployment application, pipeline, or repository.

- [Create a notification rule for a repository](https://docs.aws.amazon.com/dtconsole/latest/userguide/getting-started-repository.html): You can create notification rules to send notifications about repository events that are important to you.
- [Create a notification rule for a build project](https://docs.aws.amazon.com/dtconsole/latest/userguide/getting-started-build.html): You can create notification rules to send notifications about the events on your build project that are important to you.
- [Create a notification rule for a deployment application](https://docs.aws.amazon.com/dtconsole/latest/userguide/getting-started-deploy.html): You can create notification rules to send notifications about the events on your deployment application that are important to you.
- [Create a notification rule for a pipeline](https://docs.aws.amazon.com/dtconsole/latest/userguide/getting-started-pipeline.html): You can create notification rules to send notifications about the events on your pipeline that are important to you.

### [Working with notification rules](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-rules.html)

Learn how to work with notification rules for AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, and AWS CodePipeline resources.

- [Create a notification rule](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-rule-create.html): Learn how to create a notification rule for AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, and AWS CodePipeline resources.
- [View notification rules](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-rule-view.html): Learn how to view all of the notification rules in an AWS Region in your AWS account.
- [Edit a notification rule](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-rule-edit.html): Learn how to edit a notification rule for AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, and AWS CodePipeline resources.
- [Enable or disable notifications for a notification rule](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-rule-enable-disable.html): Learn how to enable or disable notifications for a notification rule for AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, and AWS CodePipeline resources.
- [Delete a notification rule](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-rule-delete.html): Learn how to delete a notification rule for AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, and AWS CodePipeline resources.

### [Working with notification rule targets](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-targets.html)

Configure notification rule targets using Amazon SNS topics and AWS Chatbot clients that are configured for Slack or Microsoft Teams channels.

- [Create or configure a notification rule target](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-target-create.html): Create a notification rule target using Amazon SNS topics or AWS Chatbot clients configured for Slack or Microsoft Teams channels.
- [View notification rule targets](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-target-view.html): Learn how to view all the notification rule targets in an AWS Region in your AWS account.
- [Add or remove a target for a notification rule](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-target-change-rule.html): Learn how to add or remove an Amazon SNS topic as a target to a notification rule.
- [Delete a notification rule target](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-target-delete.html): Learn how to delete a notification rule target for AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, and AWS CodePipeline resources.
- [Configure integration between notifications and AWS Chatbot](https://docs.aws.amazon.com/dtconsole/latest/userguide/notifications-chatbot.html): Learn how to configure integration between notifications and AWS Chatbot so that notifications can be sent to a Slack or Microsoft Teams channel or Amazon Chime chatroom.
- [Logging AWS CodeStar Notifications API calls with AWS CloudTrail](https://docs.aws.amazon.com/dtconsole/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS CodeStar Notifications with AWS CloudTrail.
- [Troubleshooting](https://docs.aws.amazon.com/dtconsole/latest/userguide/troubleshooting.html): Learn how to resolve common problems with notifications.
- [Quotas](https://docs.aws.amazon.com/dtconsole/latest/userguide/limits.html): Provides information about the quotas (sometimes called limits) for notifications in the Developer Tools console.

### [What are connections?](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html)

Introduces a connection feature that you can use to add connections to resources in AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline.

- [What third-party providers can I create connections for?](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections-supported-providers.html): Learn how you can use connections to integrate third-party resources with AWS resources.

### [How do connections work?](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections-how-it-works.html)

Learn about how you can create a connection.

- [How connections in AWS CodeConnections work with organizations](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections-how-it-works-github-organizations.html): For organizations with a provider, such as GitHub Organizations, you cannot install a GitHub app into multiple GitHub Organizations.
- [Workflow to create or update connections](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections-workflow.html): When you create a connection, you also create or use an existing connector app installation for the auth handshake with the third-party provider.
- [Workflow to create or update a host](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-hosts-workflow.html): When you create a connection for an installed provider (on-prem), you use a host resource.
- [Global resources in AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections-how-it-works-global.html): Connections are global resources, meaning that the resource is replicated across all AWS Regions.
- [Connections concepts](https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts-connections.html): Learn about important concepts and terminology for the connections feature in the Developer Tools console.
- [AWS CodeConnections supported providers and versions](https://docs.aws.amazon.com/dtconsole/latest/userguide/supported-versions-connections.html): This chapter provides information about the providers and versions that AWS CodeConnections supports.
- [Product and service integrations with AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/integrations-connections.html): Learn about different AWS services and partner products and services that are integrated with AWS CodeConnections.
- [Setting up connections](https://docs.aws.amazon.com/dtconsole/latest/userguide/setting-up-connections.html): Get set up and start using the connections feature in the Developer Tools console
- [Getting started with connections](https://docs.aws.amazon.com/dtconsole/latest/userguide/getting-started-connections.html): Get started with connections by setting up a connection between your third-party source repository and your AWS resources.

### [Working with connections](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html)

Connect AWS resources to external code repositories using connections.

- [Create a connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create.html): Create a connection to a third-party provider using the console or the AWS CLI.
- [Create a connection to Azure DevOps](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-azure.html): Create a connection to Azure DevOps using the console or the AWS CLI.
- [Create a connection to Bitbucket](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-bitbucket.html): Create a connection to Bitbucket using the console or the AWS CLI.
- [Create a connection to GitHub](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-github.html): Create a connection to GitHub using the console or the AWS CLI.

### [Create a connection to GitHub Enterprise Server](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-gheserver.html)

Create a connection to GitHub Enterprise Server

- [Create a connection to GitHub Enterprise Server (console)](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-gheserver-console.html): To create a GitHub Enterprise Server connection, you provide information for where your GitHub Enterprise Server is installed and authorize the connection creation with your GitHub Enterprise credentials.
- [Create a connection to GitHub Enterprise Server (CLI)](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-gheserver-cli.html): You can use the AWS Command Line Interface (AWS CLI) to create a connection.
- [Create a connection to GitLab](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-gitlab.html): Create a connection to GitLab using the console or the AWS CLI.
- [Create a connection to GitLab self-managed](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-gitlab-managed.html): Create a connection to GitLab self-managed using the console or the AWS CLI.
- [Update a pending connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-update.html): Update a pending connection using the AWS Developer Tools console.
- [List connections](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-list.html): Use the Developer Tools console or AWS CLI to list your connections to third-party code repositories.
- [Delete a connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-delete.html): Use the Developer Tools console or the AWS CLI to delete a connection.
- [Tag connections resources](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-tag.html): Describes how to use the AWS CLI to tag your connections resources.
- [View connection details](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-view-details.html): Describes how to view details for a connection.
- [Share connections with AWS accounts](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-share.html): Share a connection using the console or the AWS CLI.

### [Working with hosts](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-hosts.html)

Use connections for installed provider types with hosts.

- [Create a host](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-create.html): Create a host for installed connection provider types using the console or the AWS CLI.
- [Set up a pending host](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-setup.html): Set up a pending host using the AWS Developer Tools console or CLI.
- [List hosts](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-list.html): Use the Developer Tools console or AWS CLI to list your hosts.
- [Edit a host](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-edit.html): Edit a host using the Developer Tools console.
- [Delete a host](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-delete.html): Use the Developer Tools console or the AWS CLI to delete a host.
- [View host details](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-view.html): Use the Developer Tools console or AWS CLI to view host details.

### [Working with sync configurations for linked repositories](https://docs.aws.amazon.com/dtconsole/latest/userguide/configurations.html)

Configure sync configurations for AWS resources and linked repositories.

### [Working with repository links](https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks.html)

Connect AWS resources to external code repositories using connections for sync configurations.

- [Create a repository link](https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks-create.html): Use the AWS CLI to create a repository link.
- [Update a repository link](https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks-update.html): Update a repository link.
- [List repository links](https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks-list.html): Use the AWS CLI to list your repository links with third-party code repositories.
- [Delete a repository link](https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks-delete.html): Use the AWS CLI to delete a repository link.
- [View repository link details](https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks-view-details.html): Describes how to view details for a repository link.

### [Working with sync configurations](https://docs.aws.amazon.com/dtconsole/latest/userguide/syncconfigurations.html)

Configure repositories and AWS resources to use connections for sync configurations.

- [Create a sync configuration](https://docs.aws.amazon.com/dtconsole/latest/userguide/syncconfigurations-create.html): Create a sync configuration with a third-party provider using the AWS CLI.
- [Update a sync configuration](https://docs.aws.amazon.com/dtconsole/latest/userguide/syncconfigurations-update.html): Update a sync configuration using the CLI.
- [List sync configurations](https://docs.aws.amazon.com/dtconsole/latest/userguide/syncconfigurations-list.html): Use the AWS CLI to list your repository links with third-party code repositories.
- [Delete a sync configuration](https://docs.aws.amazon.com/dtconsole/latest/userguide/syncconfigurations-delete.html): Use the AWS CLI to delete a sync configuration.
- [View sync configuration details](https://docs.aws.amazon.com/dtconsole/latest/userguide/syncconfigurations-view-details.html): Describes how to view details for a sync configuration.
- [Logging connections API calls with CloudTrail](https://docs.aws.amazon.com/dtconsole/latest/userguide/logging-using-cloudtrail-connections.html): Learn about logging AWS CodeConnections API calls with AWS CloudTrail.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/dtconsole/latest/userguide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and AWS CodeConnections without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Troubleshooting connections](https://docs.aws.amazon.com/dtconsole/latest/userguide/troubleshooting-connections.html): Learn how to resolve common problems with connections to resources in AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline.
- [Quotas](https://docs.aws.amazon.com/dtconsole/latest/userguide/limits-connections.html): Provides information about the quotas (sometimes called limits) for connections in the Developer Tools console.
- [IP addresses to add to your allow list](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-ip-address.html): If you implement IP filtering, or allowing certain IP addresses on Amazon EC2 instances, add the following IP addresses to your allow list.


## [Security](https://docs.aws.amazon.com/dtconsole/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/dtconsole/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS CodeStar Notifications and AWS CodeConnections.

### [Identity and access management](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your AWS CodeStar Notifications and AWS CodeConnections resources.

- [How features in the developer tools console work with IAM](https://docs.aws.amazon.com/dtconsole/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to features in the Developer Tools console, you should understand which IAM features are available to use with it.

### [Identity-based policy examples](https://docs.aws.amazon.com/dtconsole/latest/userguide/security_iam_id-based-policy-examples.html)

Learn about identity-based policy examples for AWS CodeCommit, AWS CodeBuild, AWS CodeDeploy, or AWS CodePipeline.

- [Permissions and examples for AWS CodeStar Notifications](https://docs.aws.amazon.com/dtconsole/latest/userguide/security_iam_id-based-policy-examples-notifications.html): Learn about permissions and examples for AWS CodeStar Notifications.
- [Permissions and examples for AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/security_iam_id-based-policy-examples-connections.html): Learn about policy statements and examples for AWS CodeConnections.
- [Using tags to control access to AWS CodeConnections resources](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-tag-based-access-control.html): Lists example tag-based access control policies for AWS CodeConnections.
- [Troubleshooting](https://docs.aws.amazon.com/dtconsole/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with notifications and IAM.
- [Using service-linked roles for AWS CodeStar Notifications](https://docs.aws.amazon.com/dtconsole/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give AWS CodeStar Notifications access to resources in your AWS account.
- [Using service-linked roles for AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/service-linked-role-connections.html): How to use service-linked roles to give AWS CodeConnections access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS CodeConnections and recent changes to those policies.
- [Compliance validation](https://docs.aws.amazon.com/dtconsole/latest/userguide/compliance.html): Learn which AWS services are in scope of compliance programs.
- [Resilience](https://docs.aws.amazon.com/dtconsole/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy and learn about AWS CodeStar Notifications and AWS CodeConnections features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/dtconsole/latest/userguide/infrastructure-security.html): Learn how AWS CodeStar Notifications and AWS CodeConnections isolate service traffic.
