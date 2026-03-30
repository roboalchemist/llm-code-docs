# Source: https://docs.aws.amazon.com/chatbot/latest/adminguide/llms.txt

# Amazon Q Developer in chat applications Administrator Guide

> Describes how to set up, configure, and use Amazon Q Developer in chat applications.

- [Tagging your resources](https://docs.aws.amazon.com/chatbot/latest/adminguide/tagging-resources.html)
- [Troubleshooting](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/chatbot/latest/adminguide/doc-history.html)

## [What is Amazon Q Developer in chat applications?](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html)

- [Amazon Q Developer in chat applications service rename](https://docs.aws.amazon.com/chatbot/latest/adminguide/service-rename.html): On February 19, 2025, we renamed AWS Chatbot to Amazon Q Developer.
- [Regions and quotas](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-regions.html): Although most AWS Regions are active by default for your AWS account, certain Regions are activated only when you manually select them.
- [Supported services](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-services.html): Amazon Q Developer in chat applications supports AWS services that emit events to Amazon EventBridge, including Amazon GuardDuty, CloudFormation, AWS Cost Anomaly Detection, and AWS Budgets.


## [Getting started](https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html)

- [Tutorial: Get started (Amazon Chime)](https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html): Get started with Amazon Q Developer in chat applications by setting up Amazon Chime chat channels and testing that your notifications work, and learn how to customize IAM roles to work with Amazon Q Developer in chat applications
- [Tutorial: Get started (Teams)](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html): Get started with Amazon Q Developer in chat applications by setting up Microsoft Teams chat channels, testing that your notifications work, and learn how to customize IAM roles to work with Amazon Q Developer in chat applications
- [Tutorial: Get started (Slack)](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html): Get started with Amazon Q Developer in chat applications by setting up Slack chat channels, testing that your notifications work, and learn how to customize IAM roles to work with Amazon Q Developer in chat applications
- [Tutorial: Receive Developer Tools notifications in Microsoft Teams](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-codestar.html): Learn how to receive Developer Tools notifications in your Amazon Q Developer in chat applications configurations for Microsoft Teams.
- [Tutorial: Subscribing an Amazon SNS topic to Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/subscribe-sns-topic.html): Learn how to subscribe an Amazon Simple Notification Service topic to Amazon Q Developer in chat applications
- [Test notifications with Amazon Q Developer in chat applications using CloudWatch](https://docs.aws.amazon.com/chatbot/latest/adminguide/test-notifications-cw.html): Learn how to test your notifications for Amazon Q Developer in chat applications by using CloudWatch


## [Permissions](https://docs.aws.amazon.com/chatbot/latest/adminguide/understanding-permissions.html)

### [Securing your AWS organization](https://docs.aws.amazon.com/chatbot/latest/adminguide/securing-orgs.html)

You can secure your AWS organization or organizational units (OUs) using organization policies.

### [Amazon Q Developer in chat applications organization policies](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-orgs-policy.html)

Organization administrators can manage multiple Amazon Q Developer in chat applications settings across all accounts within an organization using Amazon Q Developer in chat applications chat applications policies (chat applications policies).

- [Tutorial: Creating chat applications policies](https://docs.aws.amazon.com/chatbot/latest/adminguide/org-policy-tutorial.html): In this tutorial, you use the Amazon Q Developer in chat applications console to create a chat applications policy that:
- [Editing chat applications policies](https://docs.aws.amazon.com/chatbot/latest/adminguide/edit-org-pol.html): If you need to make changes to your chat applications policy, you can edit it.
- [Deleting chat applications policies](https://docs.aws.amazon.com/chatbot/latest/adminguide/delete-org-pol.html): If you no longer need a Chat applications policy, you can delete it.
- [Service control policies](https://docs.aws.amazon.com/chatbot/latest/adminguide/scp.html): Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization.
- [App permissions](https://docs.aws.amazon.com/chatbot/latest/adminguide/app-permissions.html): When you install Amazon Q Developer in chat applications on Microsoft Teams and Slack applications, each authorization process requests approval to grant Amazon Q Developer in chat applications app permissions.

### [Managing IAM roles](https://docs.aws.amazon.com/chatbot/latest/adminguide/manage-user-roles.html)

You can manage the IAM roles used as channel and user roles by editing them.

- [Editing IAM roles](https://docs.aws.amazon.com/chatbot/latest/adminguide/editing-iam-roles-for-chatbot.html): You can create new IAM roles in the Amazon Q Developer in chat applications console.
- [User roles - administrators](https://docs.aws.amazon.com/chatbot/latest/adminguide/adm-container.html): Administrators can unmap user roles from channel members' chat client IDs from the User permissions page in the Amazon Q Developer in chat applications console.
- [User roles - channel members](https://docs.aws.amazon.com/chatbot/latest/adminguide/cm-container.html): Channel members can switch their user roles from their chat channels.


## [Monitoring](https://docs.aws.amazon.com/chatbot/latest/adminguide/monitoring.html)

### [Monitoring AWS services](https://docs.aws.amazon.com/chatbot/latest/adminguide/related-services.html)

Amazon Q Developer in chat applications operates with a number of strategic AWS services, including Amazon CloudWatch, AWS Security Hub CSPM, and AWS Health.

- [Tutorial: Creating an Amazon EventBridge rule for Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/create-eventbridge-rule.html): Amazon Q Developer in chat applications currently supports notifications for most service events that are handled by Amazon EventBridge.

### [Monitoring investigations with Amazon Q](https://docs.aws.amazon.com/chatbot/latest/adminguide/monitoring-investigations.html)

Amazon Q Developer in chat applications operates with a number of strategic AWS services, including Amazon CloudWatch, AWS Security Hub CSPM, and AWS Health.

- [Tutorial: Configuring Amazon Q Developer in chat applications for operational investigations](https://docs.aws.amazon.com/chatbot/latest/adminguide/config-cbt-investigations.html): To set up Amazon Q operational investigations in your chat applications, you must add the following policies to enable two-way communication between investigations and Amazon Q Developer in chat applications.

### [Monitoring Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/monitoring-chatbot.html)

Monitor Amazon Q Developer in chat applications to maintain reliability, availability, and performance.

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/chatbot/latest/adminguide/monitoring-cloudwatch.html): You can monitor Amazon Q Developer in chat applications using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [CloudWatch Logs](https://docs.aws.amazon.com/chatbot/latest/adminguide/cloudwatch-logs.html)
- [Logging Amazon Q Developer in chat applications API calls with AWS CloudTrail](https://docs.aws.amazon.com/chatbot/latest/adminguide/logging-using-cloudtrail.html)


## [Customizing](https://docs.aws.amazon.com/chatbot/latest/adminguide/customizing-chatbot.html)

### [Custom notifications](https://docs.aws.amazon.com/chatbot/latest/adminguide/custom-notifs.html)

You can change the messaging of Amazon Q Developer in chat applications notifications by customizing them.

- [Testing custom notifications](https://docs.aws.amazon.com/chatbot/latest/adminguide/creating-custom-notifications.html): You can create custom notification content and post the message to the Amazon SNS topic used in your Amazon Q Developer in chat applications configuration.

### [Custom actions](https://docs.aws.amazon.com/chatbot/latest/adminguide/custom-actions.html)

Custom actions are preconfigured buttons you add to custom and default notifications.

- [Creating custom actions](https://docs.aws.amazon.com/chatbot/latest/adminguide/creating-custom-actions.html): You can create custom actions using AWS CLI commands, Automation runbooks and Lambda functions in your account, or by using the Amazon Q Developer in chat applications in chat applications API.
- [Sample use cases](https://docs.aws.amazon.com/chatbot/latest/adminguide/sample-custom-action.html): This page includes examples of functional use cases for custom actions that you can leverage for your specific needs.
- [Command aliases](https://docs.aws.amazon.com/chatbot/latest/adminguide/creating-aliases.html): Amazon Q Developer in chat applications supports the creation of command aliases to make running commonly used CLI commands easier.

### [Invoking Amazon Bedrock Agents](https://docs.aws.amazon.com/chatbot/latest/adminguide/connect-bedrock-agents.html)

You can invoke Amazon Bedrock Agents directly from your chat channels using Amazon Q Developer in chat applications.

- [Connecting Amazon Bedrock](https://docs.aws.amazon.com/chatbot/latest/adminguide/bedrock-connectors.html): To connect an agent to a chat channel, you must set up a connector.
- [Conversing with Amazon Bedrock Agent connectors](https://docs.aws.amazon.com/chatbot/latest/adminguide/bedrock-converse.html): To start a conversation with your agent, run:
- [Updating connectors](https://docs.aws.amazon.com/chatbot/latest/adminguide/bedrock-update.html): If you're publishing a new alias for a Amazon Bedrock, you must replace the connector to converse with this new version.
- [Quotas](https://docs.aws.amazon.com/chatbot/latest/adminguide/bedrock-limits.html): Your AWS account has the following default quotas, formerly referred to as limits, for Amazon Bedrock.


## [Performing actions](https://docs.aws.amazon.com/chatbot/latest/adminguide/performing-actions.html)

- [Getting help](https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-help.html): You can ask Amazon Q Developer in chat applications for help and get information about Amazon Q Developer in chat applications capabilities.
- [Chatting](https://docs.aws.amazon.com/chatbot/latest/adminguide/asking-questions.html): You can search and discover information about AWS services and your AWS resources by asking Amazon Q Developer in chat applications natural language questions.

### [Running AWS CLI commands](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-cli-commands.html)

You can use chat channels to run the AWS command set on your AWS services.

- [Command syntax](https://docs.aws.amazon.com/chatbot/latest/adminguide/intro-to-the-aws-cli-in-slack.html): After you set up the Amazon Q Developer in chat applications, you run commands with the following prefix:
- [Running commands](https://docs.aws.amazon.com/chatbot/latest/adminguide/Things-to-know-about-cli.html): Amazon Q Developer in chat applications tracks your use of command options and prompts you for any missing parameters before it runs the command you want.
- [Configuring commands support on an existing chat channel](https://docs.aws.amazon.com/chatbot/latest/adminguide/setting-up-aws-cli-on-slack.html): If you have existing chat channels using the Amazon Q Developer in chat applications, you can reconfigure them in a few steps to support the AWS CLI.
- [Enabling multiple accounts to use commands](https://docs.aws.amazon.com/chatbot/latest/adminguide/multiple-accounts-in-a-channel.html): You can configure Amazon Q Developer in chat applications for multiple AWS accounts in the same chat channel.
- [AWS CLI commands - Common use cases](https://docs.aws.amazon.com/chatbot/latest/adminguide/common-use-cases.html): Common use cases for using Amazon Q Developer in chat applications in your chat channels involve running CLI commands.
- [Tutorial: Using Amazon Q Developer in chat applications to run an AWS Lambda function remotely](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-run-lambda-function-remotely-tutorial.html): In this tutorial you use Amazon Q Developer in chat applications to run a Lambda function remotely and check the status of the Lambda function using Amazon CloudWatch.
- [Managing AWS Support cases](https://docs.aws.amazon.com/chatbot/latest/adminguide/manage-support-cases.html): You can search and discover information about AWS services and your AWS resources by asking Amazon Q Developer in chat applications natural language questions.


## [Security](https://docs.aws.amazon.com/chatbot/latest/adminguide/security.html)

### [Identity and Access Management for Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/security-iam.html)

How to authenticate requests and manage access your Amazon Q Developer resources.

- [IAM policies for Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html): This section describes the IAM permissions and policies that Amazon Q Developer in chat applications uses to secure its operations with other AWS services.
- [Identity-based IAM policies for Amazon Q Developer](https://docs.aws.amazon.com/chatbot/latest/adminguide/security_iam_service-with-iam-id-based-policies.html): A policy is an object in AWS that, when you attach it to an identity, defines their permissions.
- [IAM resource-level permissions for Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/security_iam_service-with-iam-resource-based-policies.html): Resource-level permissions define the AWS resources on which you allow assigned entities (users, groups, and roles) to perform actions.

### [Using Service-Linked Roles](https://docs.aws.amazon.com/chatbot/latest/adminguide/using-service-linked-roles.html)

How to use service-linked roles to give Amazon Q Developer access to resources in your AWS account.

- [Service-linked role for performing operations on Amazon SNS topics and CloudWatch Logs](https://docs.aws.amazon.com/chatbot/latest/adminguide/slr-permissions.html): Amazon Q Developer uses the service-linked role named AWSServiceRoleForAWSChatbot.
- [Troubleshooting](https://docs.aws.amazon.com/chatbot/latest/adminguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Q Developer and IAM.
- [Connecting to Amazon Q Developer in chat applications with interface VPC endpoints](https://docs.aws.amazon.com/chatbot/latest/adminguide/vpc.html): Learn how to connect to Amazon Q Developer in chat applications using interface VPC endpoints.
- [Compliance validation for Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-compliance.html): Learn which compliance programs are in scope for Amazon Q Developer in chat applications.
- [Resilience in Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy for Amazon Q Developer in chat applications.
- [Infrastructure security](https://docs.aws.amazon.com/chatbot/latest/adminguide/infrastructure-security.html): Learn how Amazon Q Developer in chat applications isolates service traffic.
