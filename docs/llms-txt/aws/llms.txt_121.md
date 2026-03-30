# Source: https://docs.aws.amazon.com/autoscaling/application/userguide/llms.txt

# Application Auto Scaling User Guide

> Use Application Auto Scaling to configure auto scaling for scalable resources for individual Amazon Web Services beyond Amazon EC2 and for custom resources.

- [Configure scaling using CloudFormation](https://docs.aws.amazon.com/autoscaling/application/userguide/creating-resources-with-cloudformation.html)
- [Tutorial: Configure auto scaling to handle a heavy workload](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-tutorial.html)
- [Suspend scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.html)
- [Scaling activities](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scaling-activities.html)
- [Working with AWS SDKs](https://docs.aws.amazon.com/autoscaling/application/userguide/sdk-general-information-section.html)
- [Tagging support](https://docs.aws.amazon.com/autoscaling/application/userguide/resource-tagging-support.html)
- [Quotas](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-quotas.html)
- [Document history](https://docs.aws.amazon.com/autoscaling/application/userguide/doc-history.html)

## [What is Application Auto Scaling?](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html)

- [Concepts](https://docs.aws.amazon.com/autoscaling/application/userguide/getting-started.html): Get started with Application Auto Scaling by learning basic terms and concepts.


## [Services that integrate](https://docs.aws.amazon.com/autoscaling/application/userguide/integrated-services-list.html)

- [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-appstream.html): Learn how to integrate WorkSpaces Applications with Application Auto Scaling.
- [Amazon Aurora](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-aurora.html): Learn how to integrate Aurora with Application Auto Scaling.
- [Amazon Comprehend](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-comprehend.html): Learn how to integrate Amazon Comprehend with Application Auto Scaling.
- [Amazon DynamoDB](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-dynamodb.html): Learn how to integrate DynamoDB with Application Auto Scaling.
- [Amazon ECS](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-ecs.html): Learn how to integrate Amazon ECS with Application Auto Scaling.
- [Amazon ElastiCache](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-elasticache.html): Learn how to integrate ElastiCache with Application Auto Scaling.
- [Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-keyspaces.html): Learn how to integrate Amazon Keyspaces with Application Auto Scaling.
- [AWS Lambda](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-lambda.html): Learn how to integrate Lambda with Application Auto Scaling.
- [Amazon Managed Streaming for Apache Kafka (MSK)](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-msk.html): Learn how to integrate Amazon MSK with Application Auto Scaling.
- [Amazon Neptune](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-neptune.html): Learn how to integrate Neptune with Application Auto Scaling.
- [Amazon SageMaker AI](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-sagemaker.html): Learn how to integrate SageMaker AI with Application Auto Scaling.
- [Spot Fleet (Amazon EC2)](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-ec2.html): Learn how to integrate Spot Fleet with Application Auto Scaling.
- [Amazon WorkSpaces](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-workspaces.html): Learn how to integrate WorkSpaces with Application Auto Scaling.
- [Custom resources](https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-custom.html): Learn how to integrate custom resources with Application Auto Scaling.


## [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html)

- [How scheduled scaling works](https://docs.aws.amazon.com/autoscaling/application/userguide/scheduled-scaling-policy-overview.html): Understand how Application Auto Scaling can automatically scale your application based on a target metric value.
- [Create scheduled actions](https://docs.aws.amazon.com/autoscaling/application/userguide/create-scheduled-actions.html): Create scheduled actions for Application Auto Scaling using the AWS CLI put-scheduled-action command.
- [Describe scheduled scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/describe-scheduled-scaling.html): Describe scaling activities and scheduled actions for Application Auto Scaling using the AWS CLI.
- [Schedule recurring scaling actions](https://docs.aws.amazon.com/autoscaling/application/userguide/scheduled-scaling-using-cron-expressions.html): How to schedule recurring scaling actions for Application Auto Scaling using cron expressions.
- [Turn off scheduled scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/suspend-scheduled-scaling.html): Suspend scheduled scaling for Application Auto Scaling using the AWS CLI.
- [Delete a scheduled action](https://docs.aws.amazon.com/autoscaling/application/userguide/delete-scheduled-action.html): Delete a scheduled action for Application Auto Scaling using the AWS CLI.


## [Target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html)

- [How target tracking works](https://docs.aws.amazon.com/autoscaling/application/userguide/target-tracking-scaling-policy-overview.html): Understand how Application Auto Scaling can automatically scale your application based on a target metric value.
- [Create a target tracking scaling policy](https://docs.aws.amazon.com/autoscaling/application/userguide/create-target-tracking-policy-cli.html): Create and manage a target tracking scaling policy for Application Auto Scaling using the AWS CLI.
- [Delete a target tracking scaling policy](https://docs.aws.amazon.com/autoscaling/application/userguide/delete-target-tracking-policy.html): Delete a target tracking scaling policy for Application Auto Scaling using the AWS CLI.
- [Use metric math](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking-metric-math.html): Learn how to use metric math to create new time series based on multiple metrics, and understand the considerations for building metric math expressions.


## [Step scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html)

- [How step scaling works](https://docs.aws.amazon.com/autoscaling/application/userguide/step-scaling-policy-overview.html): Understand how Application Auto Scaling can scale your application in predefined increments.
- [Create a step scaling policy](https://docs.aws.amazon.com/autoscaling/application/userguide/create-step-scaling-policy-cli.html): Create a step scaling policy for Application Auto Scaling using the AWS CLI.
- [Describe step scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/describe-step-scaling-policy.html): Describe your step scaling policies for Application Auto Scaling using the AWS CLI.
- [Delete a step scaling policy](https://docs.aws.amazon.com/autoscaling/application/userguide/delete-step-scaling-policy.html): Delete a step scaling policy for Application Auto Scaling using the AWS CLI.


## [Predictive scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-predictive-scaling.html)

- [How it works](https://docs.aws.amazon.com/autoscaling/application/userguide/aas-predictive-scaling-how-it-works.html): Learn how to create and use predictive scaling policies to automatically adjust capacity based on forecasted demand using CloudWatch metrics and historical data analysis.
- [Create a predictive scaling policy](https://docs.aws.amazon.com/autoscaling/application/userguide/aas-create-predictive-scaling-policy.html): Configure a predictive scaling policy for Amazon ECS services and learn about specifying CloudWatch metrics for the policy.
- [Override the forecast](https://docs.aws.amazon.com/autoscaling/application/userguide/aas-predictive-scaling-overriding-forecast-capacity.html): Learn how to override forecast calculations in Application Auto Scaling using scheduled actions to accommodate future capacity needs for events or demand fluctuations.

### [Use custom metrics](https://docs.aws.amazon.com/autoscaling/application/userguide/aas-predictive-scaling-customized-metric-specification.html)

Learn how to use custom metrics and metric math in predictive scaling policies for Application Auto Scaling to better describe your application load and create aggregates.

### [Constructing the JSON for custom metrics](https://docs.aws.amazon.com/autoscaling/application/userguide/construct-json-custom-metrics.html)

Learn how to configure predictive scaling to query CloudWatch data.

- [Use metric math expressions](https://docs.aws.amazon.com/autoscaling/application/userguide/using-math-expression-examples.html): The following section provides information and examples of predictive scaling policies that show how you can use metric math in your policy.
- [Considerations for custom metrics](https://docs.aws.amazon.com/autoscaling/application/userguide/custom-metrics-troubleshooting.html): Troubleshoot issues with custom metrics including validating expressions, resolving errors, and understanding limitations when using metric specifications and search expressions.


## [Monitoring](https://docs.aws.amazon.com/autoscaling/application/userguide/monitoring-overview.html)

- [Monitor using CloudWatch](https://docs.aws.amazon.com/autoscaling/application/userguide/monitoring-cloudwatch.html): Learn about the CloudWatch metrics that you can use to monitor resource usage and plan capacity.
- [Log API calls using CloudTrail](https://docs.aws.amazon.com/autoscaling/application/userguide/logging-using-cloudtrail.html): Learn about how Application Auto Scaling API calls are logged using AWS CloudTrail.
- [Amazon EventBridge](https://docs.aws.amazon.com/autoscaling/application/userguide/monitoring-eventbridge.html): Learn about the EventBridge event types that you can use to filter for events specific to Application Auto Scaling through Amazon EventBridge.


## [Code examples](https://docs.aws.amazon.com/autoscaling/application/userguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/autoscaling/application/userguide/service_code_examples_basics.html)

The following code examples show how to use the basics of Application Auto Scaling with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/autoscaling/application/userguide/service_code_examples_actions.html)

The following code examples show how to use Application Auto Scaling with AWS SDKs.

- [DeleteScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/userguide/example_application-auto-scaling_DeleteScalingPolicy_section.html): Use DeleteScalingPolicy with an AWS SDK or CLI
- [DeleteScheduledAction](https://docs.aws.amazon.com/autoscaling/application/userguide/example_application-auto-scaling_DeleteScheduledAction_section.html): Use DeleteScheduledAction with a CLI
- [DeregisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/userguide/example_application-auto-scaling_DeregisterScalableTarget_section.html): Use DeregisterScalableTarget with a CLI
- [DescribeScalableTargets](https://docs.aws.amazon.com/autoscaling/application/userguide/example_application-auto-scaling_DescribeScalableTargets_section.html): Use DescribeScalableTargets with a CLI
- [DescribeScalingActivities](https://docs.aws.amazon.com/autoscaling/application/userguide/example_application-auto-scaling_DescribeScalingActivities_section.html): Use DescribeScalingActivities with a CLI
- [DescribeScalingPolicies](https://docs.aws.amazon.com/autoscaling/application/userguide/example_application-auto-scaling_DescribeScalingPolicies_section.html): Use DescribeScalingPolicies with an AWS SDK or CLI
- [DescribeScheduledActions](https://docs.aws.amazon.com/autoscaling/application/userguide/example_application-auto-scaling_DescribeScheduledActions_section.html): Use DescribeScheduledActions with a CLI
- [PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/userguide/example_application-auto-scaling_PutScalingPolicy_section.html): Use PutScalingPolicy with a CLI
- [PutScheduledAction](https://docs.aws.amazon.com/autoscaling/application/userguide/example_application-auto-scaling_PutScheduledAction_section.html): Use PutScheduledAction with a CLI
- [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/userguide/example_application-auto-scaling_RegisterScalableTarget_section.html): Use RegisterScalableTarget with an AWS SDK or CLI


## [Security](https://docs.aws.amazon.com/autoscaling/application/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Application Auto Scaling.

### [Identity and Access Management](https://docs.aws.amazon.com/autoscaling/application/userguide/auth-and-access-control.html)

How to use IAM to control access to your Application Auto Scaling resources.

- [How Application Auto Scaling works with IAM](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html): Learn how Application Auto Scaling works with IAM.
- [AWS managed policies](https://docs.aws.amazon.com/autoscaling/application/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Application Auto Scaling and recent changes to those policies.
- [Service-linked roles](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html): Learn about service-linked roles in Application Auto Scaling and how they provide secure, managed permissions for interacting with other AWS services on your behalf.
- [Identity-based policy examples](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_id-based-policy-examples.html): Provides examples of identity-based policies that allow access to Application Auto Scaling API operations.
- [Troubleshooting](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_troubleshoot.html): Troubleshoot common issues with IAM in Application Auto Scaling.
- [Permissions validation](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_permission_validation.html): Learn how Application Auto Scaling validates permissions to access target services.
- [AWS PrivateLink](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-vpc-endpoints.html): Create a private connection between your VPC and Application Auto Scaling using AWS PrivateLink, enabling secure access without public internet exposure.
- [Resilience](https://docs.aws.amazon.com/autoscaling/application/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Application Auto Scaling features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/autoscaling/application/userguide/infrastructure-security.html): Learn how Application Auto Scaling isolates service traffic.
- [Compliance validation](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-compliance.html): Learn about AWS service compliance with specific programs, access audit reports, and understand your compliance responsibilities when using AWS services.
