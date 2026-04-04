# Source: https://docs.aws.amazon.com/fis/latest/userguide/llms.txt

# AWS Fault Injection Service User Guide

> Use AWS Fault Injection Service (AWS FIS) to run fault injection experiments on your AWS workloads.

- [What is AWS FIS?](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)
- [Planning your experiments](https://docs.aws.amazon.com/fis/latest/userguide/getting-started-planning.html)
- [Safety levers](https://docs.aws.amazon.com/fis/latest/userguide/safety-lever.html)
- [Troubleshooting](https://docs.aws.amazon.com/fis/latest/userguide/troubleshooting.html)
- [Tagging your resources](https://docs.aws.amazon.com/fis/latest/userguide/tagging.html)
- [Quotas and limitations](https://docs.aws.amazon.com/fis/latest/userguide/fis-quotas.html)
- [Document history](https://docs.aws.amazon.com/fis/latest/userguide/doc-history.html)

## [Experiment template components](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html)

- [Actions](https://docs.aws.amazon.com/fis/latest/userguide/action-sequence.html): Organize your AWS FIS actions into a specific set of actions.
- [Targets](https://docs.aws.amazon.com/fis/latest/userguide/targets.html): Define targets for your AWS Fault Injection Service experiments.
- [Stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html): Define and implement stop conditions for your experiment.
- [Experiment role](https://docs.aws.amazon.com/fis/latest/userguide/getting-started-iam-service-role.html): AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources.
- [Experiment report configuration](https://docs.aws.amazon.com/fis/latest/userguide/experiment-report-configuration.html): You can enable AWS Fault Injection Service (FIS) to generate reports for experiments, making it easier to produce evidence of resilience testing.
- [Experiment options](https://docs.aws.amazon.com/fis/latest/userguide/experiment-options.html): Learn about AWS Fault Injection Service experiment options for an experiment template.


## [Actions reference](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)

- [SSM document actions](https://docs.aws.amazon.com/fis/latest/userguide/actions-ssm-agent.html): Configure SSM Agent on targets to allow AWS FIS to run actions on those targets.
- [ECS task actions](https://docs.aws.amazon.com/fis/latest/userguide/ecs-task-actions.html): Learn about the prerequisites for the AWS FIS aws:ecs:task actions.
- [EKS Pod actions](https://docs.aws.amazon.com/fis/latest/userguide/eks-pod-actions.html): Learn about the prerequisites for the AWS FIS aws:eks:pod actions.

### [AWS Lambda actions](https://docs.aws.amazon.com/fis/latest/userguide/use-lambda-actions.html)

You can use the aws:lambda:function actions to inject faults into invocations of your AWS Lambda functions.

- [AWS FIS Lambda extension versions](https://docs.aws.amazon.com/fis/latest/userguide/actions-lambda-extension-arns.html): This section includes information about the AWS FIS Lambda extension versions.


## [Managing experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/manage-experiment-template.html)

- [Create an experiment template](https://docs.aws.amazon.com/fis/latest/userguide/create-template.html): Before you begin, complete the following tasks:
- [View experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/view-template.html): You can view the experiment templates that you created.
- [Generate a target preview](https://docs.aws.amazon.com/fis/latest/userguide/generate-target-preview.html): Before you start an experiment, you can generate a target preview to verify that your experiment template is configured to target the expected resources.
- [Start an experiment from a template](https://docs.aws.amazon.com/fis/latest/userguide/start-experiment-from-template.html): After you have created an experiment template, you can start experiments using that template.
- [Update an experiment template](https://docs.aws.amazon.com/fis/latest/userguide/update-template.html): You can update an existing experiment template.
- [Tag experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/tag-experiment-template.html): You can apply your own tags to experiment templates to help you organize them.
- [Delete an experiment template](https://docs.aws.amazon.com/fis/latest/userguide/delete-template.html): If you no longer need an experiment template, you can delete it.
- [Example templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-template-example.html): View example experiment templates for AWS Fault Injection Service.


## [Managing experiments](https://docs.aws.amazon.com/fis/latest/userguide/experiments.html)

- [Start an experiment](https://docs.aws.amazon.com/fis/latest/userguide/run-experiment.html): You start an experiment from an experiment template.
- [View your experiments](https://docs.aws.amazon.com/fis/latest/userguide/view-experiment-progress.html): You can view the progress of a running experiment, and you can view experiments that have completed, stopped, or failed.
- [Tag an experiment](https://docs.aws.amazon.com/fis/latest/userguide/tag-experiment.html): You can apply tags to experiments to help you organize them.
- [Stop an experiment](https://docs.aws.amazon.com/fis/latest/userguide/stop-experiment.html): You can stop a running experiment at any time.
- [List resolved targets](https://docs.aws.amazon.com/fis/latest/userguide/list-experiment-resolved-targets.html): You can view information for resolved targets for an experiment after target resolution has ended.


## [Tutorials](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorials.html)

- [Test instance stop and start](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorial-stop-instances.html): Learn how to test instance stop and start
- [Run CPU stress on an instance](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorial-run-cpu-stress.html): Learn how to run CPU stress experiments
- [Test Spot Instance interruptions](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorial-spot-interruptions.html): Learn how to test spot instance interruptions
- [Simulate a connectivity event](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorial-disrupt-connectivity.html): Step through a tutorial to simulate connectivity issues or events by using AWS FIS.
- [Schedule a recurring experiment](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorial-recurring-experiment.html): How-to guide on scheduling a recurring experiment with AWS Fault Injection Service.


## [Working with the scenario library](https://docs.aws.amazon.com/fis/latest/userguide/scenario-library.html)

### [Scenarios reference](https://docs.aws.amazon.com/fis/latest/userguide/scenario-library-scenarios.html)

Learn more about the scenarios provided with the AWS FIS scenario library.

- [AZ Availability: Power Interruption](https://docs.aws.amazon.com/fis/latest/userguide/az-availability-scenario.html): AZ Availability: Power Interruption
- [AZ: Application Slowdown](https://docs.aws.amazon.com/fis/latest/userguide/az-application-slowdown-scenario.html): AZ: Application Slowdown
- [Cross-AZ: Traffic Slowdown](https://docs.aws.amazon.com/fis/latest/userguide/cross-az-traffic-slowdown-scenario.html): Cross-AZ: Traffic Slowdown
- [Cross-Region: Connectivity](https://docs.aws.amazon.com/fis/latest/userguide/cross-region-scenario.html): You can use the Cross-Region: Connectivity scenario to block application network traffic from the experiment Region to the destination Region and pause cross-Region replication for Amazon S3 and Amazon DynamoDB multi-Region global tables.


## [Working with multi-account experiments](https://docs.aws.amazon.com/fis/latest/userguide/multi-account.html)

- [Prerequisites](https://docs.aws.amazon.com/fis/latest/userguide/multi-account-prerequisites.html): To use stop conditions for a multi-account experiment, you must first configure cross-account alarms.
- [Create a multi-account experiment template](https://docs.aws.amazon.com/fis/latest/userguide/create.html)
- [Update a target account configuration](https://docs.aws.amazon.com/fis/latest/userguide/update.html): You can update an existing target account configuration if you want to change the role ARN or description for the the account.
- [Delete a target account configuration](https://docs.aws.amazon.com/fis/latest/userguide/delete.html): If you no longer need a target account configuration, you can delete it.


## [Scheduling experiments](https://docs.aws.amazon.com/fis/latest/userguide/experiment-scheduler.html)

- [Create a scheduler role](https://docs.aws.amazon.com/fis/latest/userguide/getting-started.html): An execution role is an IAM role that AWS FIS assumes in order to interact with EventBridge scheduler and for Event Bridge scheduler to Start FIS Experiment.
- [Create an experiment schedule](https://docs.aws.amazon.com/fis/latest/userguide/scheduling-an-experiment.html): Before you schedule an experiment, you need one or more for your schedule to invoke.
- [Update an experiment schedule](https://docs.aws.amazon.com/fis/latest/userguide/update-schedule.html): You can update an experiment schedule so that it occurs at a specific date and time that suits you.
- [Disable or delete an experiment schedule](https://docs.aws.amazon.com/fis/latest/userguide/delete-schedule.html): To stop an experiment from executing or running on a schedule, you can delete or disable the rule.


## [Monitoring experiments](https://docs.aws.amazon.com/fis/latest/userguide/monitoring-experiments.html)

- [Monitor using CloudWatch](https://docs.aws.amazon.com/fis/latest/userguide/monitoring-cloudwatch.html): View CloudWatch usage metrics for resources.
- [Monitor using EventBridge](https://docs.aws.amazon.com/fis/latest/userguide/monitoring-eventbridge.html): View status events for your experiments.
- [Experiment logging](https://docs.aws.amazon.com/fis/latest/userguide/monitoring-logging.html): Learn how to monitor your experiment using logging provided by AWS FIS.
- [Log API calls with AWS CloudTrail](https://docs.aws.amazon.com/fis/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS Fault Injection Service API calls with AWS CloudTrail.


## [Security](https://docs.aws.amazon.com/fis/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/fis/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Fault Injection Service (AWS FIS).

### [Identity and access management](https://docs.aws.amazon.com/fis/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your AWS FIS resources.

- [How AWS Fault Injection Service works with IAM](https://docs.aws.amazon.com/fis/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS FIS, learn what IAM features are available to use with AWS FIS.
- [Policy examples](https://docs.aws.amazon.com/fis/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS FIS resources.
- [Use service-linked roles](https://docs.aws.amazon.com/fis/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give AWS FIS access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/fis/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS FIS and recent changes to those policies.
- [Infrastructure security](https://docs.aws.amazon.com/fis/latest/userguide/infrastructure-security.html): Learn how AWS Fault Injection Service isolates service traffic.
- [AWS PrivateLink](https://docs.aws.amazon.com/fis/latest/userguide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and AWS Fault Injection Service without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
