# Source: https://docs.aws.amazon.com/resilience-hub/latest/userguide/llms.txt

# AWS Resilience Hub User Guide

> This guide describes how to use AWS Resilience Hub to analyze your infrastructure, get recommendations to improve the resiliency of your AWS apps, review resiliency scores, and more.

- [Resilience Checks for AWS services](https://docs.aws.amazon.com/resilience-hub/latest/userguide/resilience-checks.html)
- [Document history](https://docs.aws.amazon.com/resilience-hub/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/resilience-hub/latest/userguide/glossary.html)

## [What is AWS Resilience Hub?](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html)

- [AWS Resilience Hub â Resilience management](https://docs.aws.amazon.com/resilience-hub/latest/userguide/arh-mgmt.html): AWS Resilience Hub allows you to start with analyzing your application, or to start with testing your resiliency using AWS Fault Injection Service (AWS FIS) tests.
- [AWS Resilience Hub â Resilience testing](https://docs.aws.amazon.com/resilience-hub/latest/userguide/arh-testing.html): AWS Resilience Hub allows you to start with analyzing your application, or to start with testing your resiliency using AWS Fault Injection Service tests.
- [AWS Resilience Hub concepts](https://docs.aws.amazon.com/resilience-hub/latest/userguide/concepts-terms.html): Describes concepts to help you better understand the AWS Resilience Hub service.
- [AWS Resilience Hub personas](https://docs.aws.amazon.com/resilience-hub/latest/userguide/arh-personas.html): Describes different personas from different teams who contribute towards creating and managing applications on AWS Resilience Hub.
- [Supported AWS Resilience Hub resources](https://docs.aws.amazon.com/resilience-hub/latest/userguide/supported-resources.html): Describes the supported resources in AWS Resilience Hub.
- [AWS Resilience Hub and myApplications](https://docs.aws.amazon.com/resilience-hub/latest/userguide/arh-myApplication-integration.html): The Resiliency widget in the myApplications dashboard streamlines the process of assessing and monitoring the resilience of your applications.


## [Getting started](https://docs.aws.amazon.com/resilience-hub/latest/userguide/getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/resilience-hub/latest/userguide/prerequisites.html): To start using AWS Resilience Hub, make sure that you have the required setup.

### [Add an application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/describe-applicationlication.html)

For AWS Resilience Hub to prepare and protect an application from disruptions, you must describe the application.

- [Get started by adding an application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/describe-app-intro.html): Get started with AWS Resilience Hub by describing the details of your AWS application and running a report to assess resiliency.
- [Manage your application resources](https://docs.aws.amazon.com/resilience-hub/latest/userguide/how-app-manage.html): In addition to AWS CloudFormation stacks, AWS Resource Groups, myApplications applications, and Terraform state files, you can add resources that are located on Amazon Elastic Kubernetes Service (Amazon EKS) clusters.
- [Add resources to your AWS Resilience Hub application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/discover-structure.html): Add the resources for your application in AWS Resilience Hub.
- [Set RTO and RPO](https://docs.aws.amazon.com/resilience-hub/latest/userguide/setup-resiliency-policy.html): AWS Resilience Hub assesses your application against the recovery targets that you are defining in this policy.
- [Setup scheduled assessment and drift notification](https://docs.aws.amazon.com/resilience-hub/latest/userguide/scheduled-assessment.html): Allow AWS Resilience Hub to automatically run a daily assessment on your application or turn it off.
- [Setup permissions](https://docs.aws.amazon.com/resilience-hub/latest/userguide/setup-permissions.html): Configure the necessary permissions to allow AWS Resilience Hub to discover and assess the resources.
- [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html): If you have deployed AWS Elastic Disaster Recovery, indicate your failover Region and failover account in AWS Resilience Hub.
- [Add tags to your application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/add-tags.html): Add tags to your application in AWS Resilience Hub.
- [Review and publish](https://docs.aws.amazon.com/resilience-hub/latest/userguide/review-and-publish.html): Review and publish your AWS Resilience Hub application.
- [Run an assessment](https://docs.aws.amazon.com/resilience-hub/latest/userguide/run-assessment-start.html): After you publish your AWS Resilience Hub application, you can assess it.


## [Using AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/using-resilience-hub.html)

- [AWS Resilience Hub summary](https://docs.aws.amazon.com/resilience-hub/latest/userguide/view-arh-summary-ug.html): Describes the AWS Resilience Hub console application summary page.
- [AWS Resilience Hub dashboard](https://docs.aws.amazon.com/resilience-hub/latest/userguide/view-app-dashboard.html): Describes AWS Resilience Hub dashboard.

### [Managing applications](https://docs.aws.amazon.com/resilience-hub/latest/userguide/applications.html)

Create and manage AWS Resilience Hub applications.

- [Viewing application summary](https://docs.aws.amazon.com/resilience-hub/latest/userguide/view-app-summary.html): Describes the AWS Resilience Hub console application summary page.
- [Editing application resources](https://docs.aws.amazon.com/resilience-hub/latest/userguide/application-resources.html): Describes how to edit your application resources.

### [Managing Application Components](https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.html)

An Application Component (AppComponent) is a group of related AWS resources that work and fail as a single unit.

### [Grouping resources in an Application Component](https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html)

When the application is imported into AWS Resilience Hub along with its resources, AWS Resilience Hub makes its best effort to group related resources into the same AppComponent when you import your application, but the grouping might not always be 100 percent accurate.

- [Blocked services for manual grouping](https://docs.aws.amazon.com/resilience-hub/latest/userguide/blocked-services-for-manual-grouping.html): AWS Resilience Hub blocks you from manually grouping resources of certain AWS services to prevent configuration errors that could affect the resilience assessment and recommendations for your application.
- [AWS Resilience Hub resource grouping recommendations](https://docs.aws.amazon.com/resilience-hub/latest/userguide/grouping-recommendation.html): This section explains how to generate and review resource grouping recommendations in AWS Resilience Hub.
- [Manually grouping resources into an AppComponent](https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent-manual-grouping.html): This section explains how to manually group resources into an AppComponent and assigning different AppComponent to a resource in AWS Resilience Hub.
- [Publish a new application version](https://docs.aws.amazon.com/resilience-hub/latest/userguide/applications-publish.html): After you make changes to your AWS Resilience Hub application resources as described in , you must publish a new version of your application to run an accurate resiliency assessment.
- [Viewing application versions](https://docs.aws.amazon.com/resilience-hub/latest/userguide/view-application-version.html): To help track the application changes, AWS Resilience Hub displays the previous versions of your application from the time it was created on AWS Resilience Hub.
- [Viewing resources of your application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/view-resources.html): Viewing the resources of an AWS Resilience Hub application.
- [Deleting an application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/applications-delete.html): Delete an AWS Resilience Hub application.

### [Application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config.html)

In AWS Resilience Hub, provide the failover account ID and failover Region of AWS Elastic Disaster Recovery deployment.

- [Updating application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/update-app-config.html): If you have deployed AWS Elastic Disaster Recovery, indicate your failover Region and failover account in AWS Resilience Hub.

### [Managing resiliency policies](https://docs.aws.amazon.com/resilience-hub/latest/userguide/resiliency-policies.html)

Create and manage resiliency policies in AWS Resilience Hub.

- [Creating resiliency policies](https://docs.aws.amazon.com/resilience-hub/latest/userguide/create-policy.html): AWS Resilience Hub enables you to create resiliency policies in Applications and in Resiliency policies.

### [Managing resiliency assessments in AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/resil-assessments.html)

Manage and run resiliency assessments in AWS Resilience Hub.

- [Running resiliency assessments in AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/run-assessment.html): Running resiliency assessments in AWS Resilience Hub

### [Reviewing assessments reports](https://docs.aws.amazon.com/resilience-hub/latest/userguide/review-assessment.html)

Learn how to run and view resiliency assessment reports.

- [Reviewing resiliency recommendations](https://docs.aws.amazon.com/resilience-hub/latest/userguide/resil-recs.html): Learn how to view resiliency assessment recommendations in AWS Resilience Hub.
- [Reviewing operational recommendations](https://docs.aws.amazon.com/resilience-hub/latest/userguide/ops.reqs.html): Describes the resiliency assessment recommendations in AWS Resilience Hub.
- [Including or excluding operational recommendations](https://docs.aws.amazon.com/resilience-hub/latest/userguide/exclude-recommend.html): In AWS Resilience Hub, you can include or exclude the operational recommendations that were recommended for improving the resiliency of your application.
- [Deleting resiliency assessments](https://docs.aws.amazon.com/resilience-hub/latest/userguide/delete-assessment.html): Learn how to delete resiliency assessment in AWS Resilience Hub.

### [Managing resiliency assessments from Resiliency widget](https://docs.aws.amazon.com/resilience-hub/latest/userguide/resil-assessments-resiliency-widget.html)

Manage and run resiliency assessments from Resiliency widget.

- [Running resiliency assessments from Resiliency widget](https://docs.aws.amazon.com/resilience-hub/latest/userguide/run-assessment-resiliency-widget.html): Create and manage resiliency policies in AWS Resilience Hub.
- [Reviewing assessment summary in Resiliency widget](https://docs.aws.amazon.com/resilience-hub/latest/userguide/review-assessment-resliency-widget.html): Review resiliency assessment summary in Resiliency widget.

### [Managing alarms](https://docs.aws.amazon.com/resilience-hub/latest/userguide/alarms.html)

In AWS Resilience Hub, set up Amazon CloudWatch alarms to monitor the resiliency of your application.

- [Creating alarms from the operational recommendations](https://docs.aws.amazon.com/resilience-hub/latest/userguide/create-alarm.html): In AWS Resilience Hub, create alarms to monitor the resiliency of your application.
- [Viewing alarms](https://docs.aws.amazon.com/resilience-hub/latest/userguide/view-alarm.html): In AWS Resilience Hub, view the alarms that you set up to monitor the resiliency of your application.

### [Managing standard operating procedures](https://docs.aws.amazon.com/resilience-hub/latest/userguide/sops.html)

In AWS Resilience Hub, standard operating procedures (SOPs) help recover your application in the event of an outage or alarm.

- [Building an SOP based on AWS Resilience Hub recommendations](https://docs.aws.amazon.com/resilience-hub/latest/userguide/building-sops.html): To build an SOP based on AWS Resilience Hub recommendations, you need an AWS Resilience Hub application with a resiliency policy attached to it, and you need to have run a resiliency assessment against that application.
- [Creating a custom SSM document](https://docs.aws.amazon.com/resilience-hub/latest/userguide/create-custom-ssm-doc.html): To fully automate the recovery of your application, you may need to create a custom SSM document for your SOP in Systems Manager console.
- [Using a custom SSM document instead of the default](https://docs.aws.amazon.com/resilience-hub/latest/userguide/using-different-ssm-doc.html): To replace the SSM document AWS Resilience Hub suggested for your SOP with a custom document you've created, work directly in your code base.
- [Testing SOPs](https://docs.aws.amazon.com/resilience-hub/latest/userguide/testing-sops.html): As previously mentioned, best practice is to add AWS FIS experiments to your CI/CD pipelines to test your SOPs regularly; this ensures they're ready to go if an outage occurs.
- [Viewing standard operating procedures](https://docs.aws.amazon.com/resilience-hub/latest/userguide/view-sops.html): In AWS Resilience Hub, view the standard operating procedures (SOPs) that you set up to efficiently recover your application in the event of an outage or alarm.

### [Managing AWS Fault Injection Service experiments](https://docs.aws.amazon.com/resilience-hub/latest/userguide/testing.html)

Describes how AWS Fault Injection Service works in AWS Resilience Hub.

- [Initiating, creating, and running AWS FIS experiments](https://docs.aws.amazon.com/resilience-hub/latest/userguide/test-assessment-report.html): This section explains how to create and run AWS FIS experiments for your application after running an assessment report.
- [Viewing AWS FIS experiments](https://docs.aws.amazon.com/resilience-hub/latest/userguide/view-fis-experiment.html): In AWS Resilience Hub, view the AWS FIS experiments that you set up to measure the resiliency of your AWS resources and the amount of time it takes to recover from application, infrastructure, availability zone, and AWS Region incidents.

### [AWS Fault Injection Service experiment failures/status check](https://docs.aws.amazon.com/resilience-hub/latest/userguide/test-failures.html)

AWS Resilience Hub allows you to track the status of your AWS Fault Injection Service experiment that you have started from different parts of the AWS Resilience Hub console.

- [Analyzing AWS FIS experiment execution using AWS Systems Manager](https://docs.aws.amazon.com/resilience-hub/latest/userguide/test-failures-ssm.html): In AWS Resilience Hub, you can track the status of your experiment after running an assessment report.
- [AWS FIS experiment failures while testing Kubernetes pods running in your Amazon Elastic Kubernetes Service clusters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/test-failures-eks.html): In AWS Resilience Hub, you can track the status of your experiment after running an assessment report.

### [Understanding resiliency scores](https://docs.aws.amazon.com/resilience-hub/latest/userguide/resil-score.html)

Describes how AWS Resilience Hub indicates application readiness through a resiliency score.

- [Accessing the Resiliency score of your applications](https://docs.aws.amazon.com/resilience-hub/latest/userguide/access-score.html): Describes how to access Resiliency scores in AWS Resilience Hub.
- [Calculating resiliency scores](https://docs.aws.amazon.com/resilience-hub/latest/userguide/calculate-score.html): Computes the resiliency score of your application and resiliency score for each combination of Application Component (AppComponent) and disruption type.
- [Integrating recommendations into applications](https://docs.aws.amazon.com/resilience-hub/latest/userguide/cfn-integration.html): In AWS Resilience Hub, you can add an operational recommendations such as a alarm, standard operating procedure, or fault injection experiment using CloudFormation.


## [Using AWS Resilience Hub APIs to describe and manage application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/using-api.html)

- [Preparing the application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/prepare-app-using-api.html): Using AWS Resilience Hub APIs to prepare an application.
- [Running and analyzing the application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/running-app-using-api.html): Using AWS Resilience Hub APIs to run and analyze the assessment.
- [Modify your application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/modify-application-using-api.html): Using AWS Resilience Hub APIs to modify your application.


## [Security](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/resilience-hub/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Resilience Hub.

### [Identity and Access Management](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your AWS Resilience Hub resources.

### [How AWS Resilience Hub works with IAM](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security_iam_service-with-iam.html)

Before you use IAM to manage access to AWS Resilience Hub, learn what IAM features are available to use with AWS Resilience Hub.

- [Identity-based policy examples](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS Resilience Hub resources.
- [Setup IAM roles and permissions](https://docs.aws.amazon.com/resilience-hub/latest/userguide/setting-up-permissions.html): AWS Resilience Hub allows you to configure the IAM roles you would like to use while running assessments for your application.
- [Troubleshooting](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Resilience Hub and IAM.

### [AWS Resilience Hub access permissions reference](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security-iam-resilience-hub-permissions.html)

You can use AWS Identity and Access Management (IAM) to manage access to the application resources and create IAM policies that apply to users, groups, or roles.

### [Using IAM role](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security-iam-resilience-hub-using-iam-role.html)

AWS Resilience Hub will use a predefined existing IAM role to access your resources in the primary account or secondary/resources account.

- [Invoker role](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security-iam-resilience-hub-invoker-role.html): The AWS Resilience Hub invoker role is an AWS Identity and Access Management (IAM) role that AWS Resilience Hub assumes to access AWS services and resources.
- [Roles in different AWS account for cross-account access](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security-iam-resilience-cross-account-roles.html): When your resources are located in secondary/resource accounts, you must create roles in each of these accounts to enable AWS Resilience Hub to successfully assess your application.
- [Using current IAM user permissions](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security-iam-resilience-hub-current-user-permissions.html): Use this method if you want to use your current IAM user permissions to create and run an assessment.
- [AWS managed policies](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Resilience Hub and recent changes to those policies.
- [AWS Resilience Hub personas and IAM permissions reference](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security-iam-resilience-hub-personas.html): You can grant the IAM permissions to personas that are required to work with AWS Resilience Hub by using AWSResilienceHubAsssessmentExecutionPolicy AWS managed policy and one of the following persona-specific policies.
- [Importing Terraform state file into AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security-iam-resilience-hub-terraform-secondary.html): AWS Resilience Hub supports importing Terraform state files that are encrypted using server-side encryption (SSE) with Amazon Simple Storage Service managed keys (SSE-S3) or with AWS Key Management Service managed keys (SSE-KMS).

### [Enabling AWS Resilience Hub access to your Amazon EKS cluster](https://docs.aws.amazon.com/resilience-hub/latest/userguide/enabling-eks-in-arh.html)

AWS Resilience Hub assesses the resiliency of an Amazon Elastic Kubernetes Service (Amazon EKS) cluster by analyzing the infrastructure of your Amazon EKS cluster.

- [Granting AWS Resilience Hub access to resources in your Amazon EKS cluster](https://docs.aws.amazon.com/resilience-hub/latest/userguide/grant-permissions-to-eks-in-arh.html): AWS Resilience Hub allows you to access resources located on Amazon EKS clusters provided you have configured the required permissions.
- [Enabling AWS Resilience Hub to publish to your Amazon SNS topics](https://docs.aws.amazon.com/resilience-hub/latest/userguide/enabling-sns-in-arh.html): This section explains about how to enable AWS Resilience Hub to publish notifications about the application to your Amazon Simple Notification Service (Amazon SNS) topics.
- [Limiting permissions to include or exclude AWS Resilience Hub recommendations](https://docs.aws.amazon.com/resilience-hub/latest/userguide/include-exclude-limit-permissions.html): AWS Resilience Hub enables you to restrict permissions to include or exclude recommendations per application.
- [Infrastructure security](https://docs.aws.amazon.com/resilience-hub/latest/userguide/infrastructure-security.html): Describes how AWS Resilience Hub keeps its service traffic secure.


## [Working with other services](https://docs.aws.amazon.com/resilience-hub/latest/userguide/service-integrations.html)

- [AWS CloudFormation](https://docs.aws.amazon.com/resilience-hub/latest/userguide/creating-resources-with-cloudformation.html): Create resources for AWS Resilience Hub using an AWS CloudFormation template.
- [AWS CloudTrail](https://docs.aws.amazon.com/resilience-hub/latest/userguide/integrate-cloudtrail.html): This section describes how AWS CloudTrail interacts with AWS Resilience Hub.
- [AWS Systems Manager](https://docs.aws.amazon.com/resilience-hub/latest/userguide/integrate-ssm.html): This section describes how Systems Manager interacts with AWS Resilience Hub.
- [AWS Trusted Advisor](https://docs.aws.amazon.com/resilience-hub/latest/userguide/integrate-ta.html): This section describes how AWS Trusted Advisor interacts with AWS Resilience Hub.
