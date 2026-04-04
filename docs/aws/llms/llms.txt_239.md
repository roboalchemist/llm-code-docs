# Source: https://docs.aws.amazon.com/compute-optimizer/latest/ug/llms.txt

# AWS Compute Optimizer User Guide

> This is Amazon Web Services (AWS) documentation for AWS Compute Optimizer. This User Guide describes Compute Optimizer concepts, and provides instructions on using the various features with both the console and the command line interface.

- [What is Compute Optimizer?](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)
- [Supported resources](https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html)
- [Resource requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html)
- [Using the dashboard](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-dashboard.html)
- [Troubleshooting](https://docs.aws.amazon.com/compute-optimizer/latest/ug/troubleshooting-account-opt-in.html)
- [Document history](https://docs.aws.amazon.com/compute-optimizer/latest/ug/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html)

### [Opting in to Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html)

Learn about how to opt your accounts in to Compute Optimizer using the console or the AWS CLI.

- [Opting out](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-out.html): Learn about how to opt your accounts out of Compute Optimizer using the AWS CLI.
- [Identity and Access Management](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html): Use AWS Identity and Access Management to opt in to AWS Compute Optimizer and use policies to control who has access to Compute Optimizer.
- [AWS managed policies](https://docs.aws.amazon.com/compute-optimizer/latest/ug/managed-policies.html): Learn about AWS managed policies for Compute Optimizer and recent changes to those policies.
- [Using Service-Linked Roles](https://docs.aws.amazon.com/compute-optimizer/latest/ug/using-service-linked-roles.html): Learn how to use service-linked roles to give AWS Compute Optimizer access to resources in your AWS account.
- [Using Service-Linked Roles for Automation](https://docs.aws.amazon.com/compute-optimizer/latest/ug/using-service-linked-roles-automation.html): Learn how to use service-linked roles to give AWS Compute Optimizer access to resources in your AWS account.


## [Metrics analyzed](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html)

- [EC2 instance metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ec2-metrics-analyzed.html)
- [EBS volume metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ebs-metrics-analyzed.html): Compute Optimizer analyzes the following CloudWatch metrics of your EBS volumes.
- [Lambda function metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/lambda-metrics-analyzed.html): Compute Optimizer analyzes the following CloudWatch metrics of your Lambda functions.
- [Metrics for Amazon ECS services on Fargate](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ecs-fargate-metrics-analyzed.html): Compute Optimizer analyzes the following CloudWatch and Amazon ECS utilization metrics of your Amazon ECS services on Fargate.
- [Metrics for commercial software licenses](https://docs.aws.amazon.com/compute-optimizer/latest/ug/license-metrics-analyzed.html): Compute Optimizer analyzes the following metric to generate recommendations for commercial software licenses.
- [Aurora and RDS database metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rds-metrics-analyzed.html): Compute Optimizer analyzes the following CloudWatch metrics of your Amazon Aurora and RDS databases.


## [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html)

### [EC2 instance recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html)

Learn how to view AWS Compute Optimizer recommendations for EC2 instances.

- [Accessing EC2 instance recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ec2-view-recommendations.html): Abstract

### [EC2 Auto Scaling group recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-asg-recommendations.html)

Learn how to view AWS Compute Optimizer recommendations for Auto Scaling groups.

- [Accessing EC2 Auto Scaling group recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/asg-view-recommendations.html): Abstract

### [EBS volume recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ebs-recommendations.html)

Learn how to view AWS Compute Optimizer recommendations for EBS volumes.

- [Accessing EBS volumes recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ebs-view-recommendations.html): Abstract

### [Lambda function recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-lambda-recommendations.html)

Learn how to view AWS Compute Optimizer recommendations for AWS Lambda functions.

- [Accessing Lambda function recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/lambda-view-recommendations.html): Abstract

### [ECS service recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ecs-recommendations.html)

Learn how to view AWS Compute Optimizer recommendations for Amazon ECS services on Fargate.

- [Accessing ECS service recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ecs-view-recommendations.html): Abstract

### [Commercial software license recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-license-recommendations.html)

Learn how to view AWS Compute Optimizer recommendations for AWS Lambda functions.

- [Accessing license recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/license-view-recommendations.html): Abstract

### [Aurora and RDS database recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations.html)

Learn how to view AWS Compute Optimizer recommendations for Aurora and RDS databases.

- [Accessing Aurora and RDS recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rds-view-recommendations.html): Abstract
- [Idle resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html): Learn how to view AWS Compute Optimizer recommendations for idle resources.


## [Automation](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation.html)

- [Enabling Automation](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-enable.html): When you access the Automation section of the Compute Optimizer console for the first time, you're asked to enable the feature using the account that youâre signed in with.
- [Enabling Automation for your organization](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-org.html): When you enable Automation for your organizationâs management account, you can also configure Automation for your organizationâs member accounts, enabling centralized implementation of optimization actions across your organization.

### [Recommended actions](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rec.html)

Recommended actions are optimization opportunities that you can implement through Compute Optimizer.

- [Viewing recommended actions](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rec-view.html): The Recommended actions page displays a summary of your recommended actions and a table with details for individual actions.
- [Apply recommended actions](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rec-apply.html): You can select up to 10 recommended actions at a time to apply.

### [Automation rules](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rules.html)

Automation rules automatically implement recommended actions based on your defined criteria and schedule.

- [Creating automation rules](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rules-create.html): You can use an automation rule to manage automated implementation of recommended actions in Compute Optimizer.
- [Viewing automation rule](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rules-view.html): The Automation rules page displays your automation rules and allows you to create and manage them.
- [Updating automation rules](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rules-update.html): You can update rules at any time.
- [Editing automation rule order](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rules-edit.html): Rule order determines which rule applies when a recommended action in an account matches multiple rules.
- [Deleting or disabling automation rules](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rules-delete.html): When you delete an automation rule, Compute Optimizer permanently removes it from your account, and it no longer implements recommended actions.
- [Creating automation rules with CloudFormation](https://docs.aws.amazon.com/compute-optimizer/latest/ug/creating-automation-rules-with-cloudformation.html): Learn how to use AWS CloudFormation to create and manage automation rules.

### [Automation events](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-events.html)

The Automation events page is centralized dashboard that displays information about the automated actions initiated through Compute Optimizer.

### [View automation events](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-events-view-details.html)

This Automation events page displays automation events initiated by Compute Optimizer.

- [View automation events details](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-events-view.html): Select an automation event ID to view more details and step history on Event details page.
- [Roll back automation events](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-events-rb.html): You can also initiate rollback for automation events if necessary.
- [Disabling Automation](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-disable.html): You can disable the Automation feature at any time.


## [Recommendation preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendation-preferences.html)

### [Rightsizing preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rightsizing-preferences.html)

Learn about the rightsizing preferences feature of AWS Compute Optimizer and how it can enhance recommendations.

- [Setting rightsizing preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rightsizing-preferences-process.html): This section provides you with instructions on how to set your rightsizing recommendation preferences in AWS Compute Optimizer.

### [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html)

Learn about the enhanced infrastructure metrics paid feature of AWS Compute Optimizer and how to activate and deactivate this feature.

- [Activating EIM at the resource level](https://docs.aws.amazon.com/compute-optimizer/latest/ug/activating-eim-resource-level.html): This section provides you with instructions on how to activate or deactivate enhanced infrastructure metrics at the resource level.
- [Activating EIM at the organization or account level](https://docs.aws.amazon.com/compute-optimizer/latest/ug/activating-eim-level.html): This section provides you with instructions on how to activate or deactivate enhanced infrastructure metrics for member accounts of an AWS Organization or an individual AWS account holder.

### [External metrics ingestion](https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion.html)

Learn about the external metrics ingestion feature of AWS Compute Optimizer and how to configure and opt out this feature.

- [Configuring external metrics ingestion](https://docs.aws.amazon.com/compute-optimizer/latest/ug/configure-external-metrics-ingestion.html): This section provides you with instructions on how to configure external metric ingestion.
- [Opting out of external metrics ingestion](https://docs.aws.amazon.com/compute-optimizer/latest/ug/deactivate-external-metrics-ingestion.html): This section provides you with instructions on how to opt out of external metric ingestion.

### [Inferred workload type](https://docs.aws.amazon.com/compute-optimizer/latest/ug/inferred-workload-type.html)

Learn about the inferred workload type feature of AWS Compute Optimizer and how to activate and deactivate this feature.

- [Activating inferred workload type](https://docs.aws.amazon.com/compute-optimizer/latest/ug/activating-inferred-workload-type-steps.html): This section provides you with instructions on how to activate the inferred workload type feature for member accounts of an AWS Organization or an individual AWS account holder.

### [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode.html)

Learn about the savings estimation mode that you can activate to enhance AWS Compute Optimizer recommendations.

- [Activating savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/activate-savings-estimation-mode.html): Learn about how to activate the savings estimation mode preference.
- [AWS Graviton-based instance recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/graviton-recommendations.html): Learn how to view price and performance impact of running workloads on AWS Graviton-based instances by choosing Graviton (aws-arm64) in CPU architecture preference dropdown when viewing EC2 instance and EC2 Auto Scaling group recommendations.


## [Managing accounts and preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-accounts.html)

- [Viewing member account status](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-account-opt-in.html): Learn how to view the accounts that are opted in to AWS Compute Optimizer and their recommendation preferences.
- [Delegating an administrator account](https://docs.aws.amazon.com/compute-optimizer/latest/ug/delegate-administrator-account.html): Learn how to register, update, and deregister a delegated administrator from the member accounts listed in your organization.


## [Exporting recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html)

### [Specifying S3 bucket for recommendations export](https://docs.aws.amazon.com/compute-optimizer/latest/ug/create-s3-bucket-policy-for-compute-optimizer.html)

Add a policy to an Amazon S3 bucket that allows AWS Compute Optimizer to write recommendation export files to it.

- [Using encrypted S3 buckets for exports](https://docs.aws.amazon.com/compute-optimizer/latest/ug/using-encrypted-s3-buckets.html): For the destination of your Compute Optimizer recommendations exports, you can specify S3 buckets that are encrypted with either Amazon S3 customer managed keys or AWS Key Management Service (KMS) keys.
- [Exporting your recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-your-recommendations.html): This section provides you with instructions on how to export your AWS Compute Optimizer recommendations.
- [Viewing your export jobs](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-your-exports.html): This section provides you with instructions on how to view the export jobs that you created in the last seven days.
- [Exported files](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exported-files.html): Recommendations are exported in a CSV file, and the metadata in a JSON file, to the Amazon S3 bucket that you specified when you created the export job.


## [Security](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security.html)

- [Data protection](https://docs.aws.amazon.com/compute-optimizer/latest/ug/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Compute Optimizer.
- [Compliance validation](https://docs.aws.amazon.com/compute-optimizer/latest/ug/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.

### [Monitoring Compute Optimizer Automation](https://docs.aws.amazon.com/compute-optimizer/latest/ug/monitoring-overview.html)

Monitor Compute Optimizer Automation to maintain reliability, availability, and performance.

- [CloudTrail logs](https://docs.aws.amazon.com/compute-optimizer/latest/ug/logging-using-cloudtrail.html): Learn about logging AWS Compute Optimizer Automation with AWS CloudTrail.
