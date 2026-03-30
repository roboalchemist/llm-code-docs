# Source: https://docs.aws.amazon.com/autoscaling/ec2/userguide/llms.txt

# Amazon EC2 Auto Scaling User Guide

> Use Amazon EC2 Auto Scaling to launch or terminate EC2 instances based on automatic scaling and health status.

- [Set up](https://docs.aws.amazon.com/autoscaling/ec2/userguide/setting-up.html)
- [Working with AWS SDKs](https://docs.aws.amazon.com/autoscaling/ec2/userguide/sdk-general-information-section.html)
- [Related information](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-resources.html)
- [Document history](https://docs.aws.amazon.com/autoscaling/ec2/userguide/DocumentHistory.html)

## [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)

- [Auto Scaling benefits](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html): Benefits of Amazon EC2 Auto Scaling for fault tolerance, availability, and cost management of your application architecture.
- [Instance lifecycle](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html): Lifecycle of the Amazon EC2 instances within an Auto Scaling group from pending to in-service to terminating states and lifecycle hooks.
- [Amazon EC2 Auto Scaling quotas](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html): View quotas for Auto Scaling resources, group configurations, and group API operations.


## [Get started](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html)

- [Tutorial: Create your first Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-your-first-auto-scaling-group.html): Get started with a hands-on introduction to Amazon EC2 Auto Scaling.
- [Tutorial: Set up a scaled and load-balanced application](https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-ec2-auto-scaling-load-balancer.html): Learn how to set up your Auto Scaling group to receive traffic from an Elastic Load Balancing load balancer.


## [Launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html)

- [Create a launch template for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html): Learn how to create a launch template for use with an Auto Scaling group.

### [Create a launch template using advanced settings](https://docs.aws.amazon.com/autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.html)

Learn how to define additional capabilities for your Auto Scaling instances by configuring advanced settings in your launch template.

- [Request Spot Instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-template-spot-instances.html): Learn how to request Amazon EC2 Spot Instances with a launch template.
- [Capacity Blocks for ML](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-template-capacity-blocks.html): Learn how to configure a Capacity Block reservation within a launch template and use Amazon EC2 Auto Scaling to launch instances into the reserved capacity.
- [Migrate your Auto Scaling groups to launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/migrate-to-launch-templates.html): Migrating your Auto Scaling group from a launch configuration to a launch template takes four steps.
- [Migrate CloudFormation stacks to launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/migrate-launch-configurations-with-cloudformation.html): Learn how to migrate AWS CloudFormation stacks from launch configurations to launch templates.
- [AWS CLI examples for working with launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/examples-launch-templates-aws-cli.html): Learn how to create and manage launch templates by using the AWS CLI.
- [Use Systems Manager parameters instead of AMI IDs](https://docs.aws.amazon.com/autoscaling/ec2/userguide/using-systems-manager-parameters.html): Learn how to use a parameter instead of an AMI ID in your launch template.


## [Launch configurations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-configurations.html)

- [Create a launch configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html): Learn how to create a launch configuration.
- [Change a launch configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/change-launch-config.html)


## [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)

### [Create Auto Scaling groups using launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-auto-scaling-groups-launch-template.html)

Learn the different ways to create Auto Scaling groups using launch templates using the Amazon EC2 console.

- [Create a group using a launch template](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html): Learn how to create an Auto Scaling group using a launch template.
- [Create a group using the EC2 launch wizard](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-ec2-wizard.html): Learn how to create an Auto Scaling group using the Amazon EC2 launch wizard.

### [Use multiple instance types and purchase options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html)

Launch and automatically scale a fleet of Spot and On-Demand Instances in an Auto Scaling group.

- [Setup overview for creating a mixed instances group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/mixed-instances-groups-set-up-overview.html): Provides an overview and best practices for creating a mixed instances Auto Scaling group.
- [Allocation strategies for multiple instance types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/allocation-strategies.html): Use allocation strategies to manage how Auto Scaling fulfills On-Demand and Spot capacities from the multiple instance types.
- [Create a group using attribute-based instance type selection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html): Match instance types to your compute needs with attribute-based instance type selection for Auto Scaling groups
- [Create a group using manual instance type selection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-manual-instance-type-selection.html): This topic shows you how to launch multiple instance types in a single Auto Scaling group by manually choosing your instance types.

### [Use instance weights](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups-instance-weighting.html)

Learn how to define how many units an instance type contributes to the desired capacity of the Auto Scaling group.

- [Configure an Auto Scaling group to use weights](https://docs.aws.amazon.com/autoscaling/ec2/userguide/configue-auto-scaling-group-to-use-weights.html): You can configure an Auto Scaling group to use weights, as shown in the following AWS CLI examples.
- [Spot price per unit hour example](https://docs.aws.amazon.com/autoscaling/ec2/userguide/weights-spot-price-per-unit-hour-example.html): The following table compares the hourly price for Spot Instances in different Availability Zones in US East (Northern Virginia) with the price for On-Demand Instances in the same Region.
- [Use multiple launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups-launch-template-overrides.html): Learn how to launch instances with an Arm-compatible AMI and an Intel x86-compatible AMI in the same Auto Scaling group.

### [Create Auto Scaling groups using launch configurations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-auto-scaling-groups-launch-configuration.html)

Learn the different ways to create Auto Scaling groups using launch configurations using the Amazon EC2 console.

- [Create a group using a launch configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-configuration.html): Learn how to create an Auto Scaling group using a launch configuration.
- [Create a group from instance using AWS CLI](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-from-instance.html): Learn how to create an Auto Scaling group using an existing EC2 instance with a launch configuration.

### [Synchronous provisioning](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-instances-synchronously.html)

Learn how to use synchronous provisioning to launch instances with immediate feedback and precise control over Availability Zone placement.

- [Launching instances with synchronous provisioning](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launching-instances-synchronous-provisioning.html): You can use the LaunchInstances API to synchronously launch a specific number of instances in your Auto Scaling group.
- [Update an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/update-auto-scaling-group.html): Learn how to update the configuration of your Auto Scaling group.

### [Tag groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html)

Learn how to use tags on Auto Scaling groups.

- [Tag your Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/add-tags.html): When you add a tag to your Auto Scaling group, you can specify whether it should be added to instances launched in the Auto Scaling group.
- [Delete tags](https://docs.aws.amazon.com/autoscaling/ec2/userguide/delete-tag.html): You can delete a tag associated with your Auto Scaling group at any time.
- [Tags for security](https://docs.aws.amazon.com/autoscaling/ec2/userguide/tag-security.html): Use tags to verify that the requester (such as an IAM user or role) has permissions to create, modify, or delete specific Auto Scaling groups.
- [Control access to tags](https://docs.aws.amazon.com/autoscaling/ec2/userguide/tag-permissions.html): Use tags to verify that the requester (such as an IAM user or role) has permissions to add, modify, or delete tags for Auto Scaling groups.
- [Use tags to filter Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-tag-filters-aws-cli.html): The following examples show you how to use filters with the describe-auto-scaling-groups command to describe Auto Scaling groups with specific tags.

### [Instance maintenance policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.html)

Set up an instance maintenance policy to control instance replacement behavior on your Auto Scaling group when certain events occur.

- [Overview](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-maintenance-policy-overview-and-considerations.html): This topic provides an overview of the options available and describes what to consider when you create an instance maintenance policy.

### [Set an instance maintenance policy on your group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/set-instance-maintenance-policy-on-group.html)

You can create an instance maintenance policy when you create an Auto Scaling group.

- [Set an instance maintenance policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/set-instance-maintenance-policy.html): To set an instance maintenance policy on an Auto Scaling group, use one of the following methods:
- [Remove an instance maintenance policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/remove-instance-maintenance-policy.html): If you want to stop using an instance maintenance policy with your Auto Scaling group, you can remove it.

### [Lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)

Learn about lifecycle hooks for Amazon EC2 Auto Scaling which let you create solutions that are aware of events in the instance lifecycle.

- [How lifecycle hooks work in Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks-overview.html): Lifecycle hooks allow you to create custom actions when instances transition through different states in your Auto Scaling group.
- [Prepare to add a lifecycle hook](https://docs.aws.amazon.com/autoscaling/ec2/userguide/prepare-for-lifecycle-notifications.html): Learn how to prepare for lifecycle notifications before adding a lifecycle hook to your Auto Scaling group.

### [Control instance retention with instance lifecycle policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-lifecycle-policy.html)

Instance lifecycle policies provide protection against Amazon EC2 Auto Scaling terminations when a termination lifecycle action is abandoned.

- [Configure instance retention](https://docs.aws.amazon.com/autoscaling/ec2/userguide/configure-instance-retention.html): Set up your Amazon EC2 Auto Scaling group to retain instances when termination lifecycle actions fail.
- [Manage retained instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/manage-retained-instances.html): Monitor and control Amazon EC2 instances that have been moved to a retained state.
- [Retrieve the target lifecycle state](https://docs.aws.amazon.com/autoscaling/ec2/userguide/retrieving-target-lifecycle-state-through-imds.html): Learn how to retrieve the target lifecycle state through instance metadata.
- [Add lifecycle hooks to your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/adding-lifecycle-hooks.html): Learn how to add a lifecycle hook to an Auto Scaling group.
- [Complete a lifecycle action in an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/completing-lifecycle-hooks.html): How to complete a lifecycle action for a specified token or instance.
- [Tutorial: Use instance metadata to retrieve lifecycle state](https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-lifecycle-hook-instance-metadata.html): Use the Instance Metadata Service to retrieve the target lifecycle state of the instances in your Auto Scaling group.
- [Tutorial: Configure a lifecycle hook that invokes a Lambda function](https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-lifecycle-hook-lambda.html): Learn how to use Amazon EventBridge to invoke a Lambda function to perform a custom action when instances launch.

### [Warm pools](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html)

Decrease latency for applications with long boot times using warm pools without having to over provision your Auto Scaling groups.

- [Use lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/warm-pool-instance-lifecycle.html): Learn about using lifecycle hooks with your warm pool.
- [Create a warm pool for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-warm-pool.html): This topic describes how to create a warm pool for your Auto Scaling group.
- [View health check status](https://docs.aws.amazon.com/autoscaling/ec2/userguide/warm-pools-health-checks-monitor-view-status.html): Learn about Amazon EC2 Auto Scaling health checks for instances in a warm pool.
- [AWS CLI examples for working with warm pools](https://docs.aws.amazon.com/autoscaling/ec2/userguide/examples-warm-pools-aws-cli.html): Learn how to create and manage warm pools by using the AWS CLI.

### [Auto Scaling group zonal shift](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html)

Learn how to use zonal shift in Amazon Application Recovery Controller (ARC) to quickly recover from Availability Zone impairments for your Auto Scaling groups.

- [Enable zonal shift using the AWS Management Console or the AWS CLI](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-zonal-shift-enable.html): Learn how to enable zonal shift using the AWS Management Console or the AWS CLI.
- [Availability Zone distribution](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-availability-zone-balanced.html): Learn about Auto Scaling group Availability Zone strategies to maintain instance distribution across zones for improved redundancy and fault tolerance.
- [Detach-attach instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-detach-attach-instances.html): Learn how to detach instances from your Auto Scaling group to manage independently or attach to another group.
- [Temporarily remove instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html): Learn how to place EC2 instances in your Auto Scaling group on standby.

### [Delete your Auto Scaling infrastructure](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-process-shutdown.html)

Learn how to shut down your automatic scaling processes.

- [Resource deletion protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/resource-deletion-protection.html): Learn how to configure resource deletion protection for your Amazon EC2 Auto Scaling resources.


## [Replace your instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-group-replacing-instances.html)

### [Instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html)

Learn how to update the instances in your Auto Scaling group in a rolling fashion when you update your Amazon Machine Image (AMI) or instance types.

- [How an instance refresh works](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-refresh-overview.html): This topic describes how an instance refresh works and introduces the key concepts you need to understand to use it effectively.
- [Understand the default values](https://docs.aws.amazon.com/autoscaling/ec2/userguide/understand-instance-refresh-default-values.html): Understand the various default values for an instance refresh.
- [Start an instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/start-instance-refresh.html): Describes how to start an instance refresh using the AWS Management Console or AWS CLI.
- [Monitor an instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/check-status-instance-refresh.html): Learn how to check the status of an instance refresh and monitor an in progress instance refresh.
- [Replace root volumes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/replace-root-volume.html): Contents
- [Cancel an instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/cancel-instance-refresh.html): Cancel an instance refresh that is in progress to stop any changes.
- [Undo changes with a rollback](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-refresh-rollback.html): Roll back an instance refresh that is in progress to undo any changes with a manual or auto rollback.
- [Use skip matching](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh-skip-matching.html): Avoid replacing more instances than you need to by using skip matching.

### [Add checkpoints](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-adding-checkpoints-instance-refresh.html)

Learn how to add checkpoints to an instance refresh.

- [Enable checkpoints](https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-checkpoints-console-cli.html): You can use the AWS Management Console or AWS CLI to enable checkpoints.
- [Maximum instance lifetime](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html): Learn how to maintain an up-to-date Auto Scaling group by specifying the maximum amount of time an instance can exist before being terminated and replaced.


## [Scale your group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html)

- [Choose your scaling method](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scaling-overview.html): Amazon EC2 Auto Scaling provides several ways for you to scale your Auto Scaling group.
- [Set scaling limits](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html): Set the scaling limits for your Auto Scaling group.

### [Set the default instance warmup](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html)

Set the default instance warmup time for your Auto Scaling group.

- [Enable the default instance warmup for a group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-default-instance-warmup.html): You can enable the default instance warmup when you create an Auto Scaling group.
- [Verify the default instance warmup time for a group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/verify-default-instance-warmup.html): Use the following procedure to verify the default instance warmup time for an Auto Scaling group using the AWS CLI.
- [Find scaling policies with a previously set instance warmup time](https://docs.aws.amazon.com/autoscaling/ec2/userguide/find-policies-with-a-previously-set-instance-warmup.html): To identify whether you have policies that have their own warmup time for EstimatedInstanceWarmup, run the following describe-policies command using the AWS CLI.
- [Clear the previously set instance warmup for a scaling policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/clearing-the-previously-set-instance-warmup.html): After enabling the default instance warmup, update any scaling policies that have still their own warmup time to clear the previously set value.
- [Manual scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-manually.html): Manually scale your Auto Scaling group by changing the desired capacity of an existing Auto Scaling group or terminating instances.

### [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)

Configure your Auto Scaling group to scale automatically as a function of date and time.

- [Create a scheduled action](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scheduled-scaling-create-scheduled-action.html): To create a scheduled action for your Auto Scaling group, use one of the following methods:
- [View scheduled action details](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scheduled-scaling-view-scheduled-actions.html): To view details of upcoming scheduled actions for your Auto Scaling group, use one of the following methods:
- [Delete a scheduled action](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scheduled-scaling-delete-scheduled-action.html): To delete a scheduled action, use one of the following methods:

### [Dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)

Scale your Auto Scaling group as traffic changes occur with dynamic scaling.

### [Target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)

Configure target tracking scaling policies to automatically adjust EC2 capacity in Auto Scaling groups based on metric targets for optimal performance and cost efficiency.

- [Create a target tracking scaling policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/policy_creating.html): Create a target tracking scaling policy for your Auto Scaling group using the AWS Management Console or AWS CLI.
- [Create a policy using high-resolution metrics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/policy-creating-high-resolution-metrics.html): Configure target tracking policies with high-resolution CloudWatch metrics to improve scaling precision for applications with volatile demand patterns.
- [Use metric math](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-target-tracking-metric-math.html): Learn how to use metric math to further customize the metrics that you use with target tracking scaling policies.

### [Step and simple scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html)

Learn about step and simple scaling policies for Amazon EC2 Auto Scaling.

- [Create a step scaling policy for scale out](https://docs.aws.amazon.com/autoscaling/ec2/userguide/step-scaling-create-scale-out-policy.html): To create a step scaling policy for scale out for your Auto Scaling group, use one of the following methods:
- [Create a step scaling policy for scale in](https://docs.aws.amazon.com/autoscaling/ec2/userguide/step-scaling-create-scale-in-policy.html): To create a step scaling policy for scale in for your Auto Scaling group, use one of the following methods:
- [Simple scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/simple-scaling-policies.html): The following examples show how you can use CLI commands to create simple scaling policies.
- [Scaling cooldowns](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html): Learn how to configure the cooldown period that's used when scaling your Auto Scaling group with simple scaling policies.

### [Scaling policy based on Amazon SQS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html)

Learn how to create a target tracking scaling policy to scale your Auto Scaling group using your Amazon SQS queue backlog.

- [Configure scaling based on Amazon SQS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-sqs-queue-cli.html): The following procedure describes how to configure automatic scaling based on Amazon SQS.
- [Verify a scaling activity](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html): Learn about verifying scaling activities for Amazon EC2 Auto Scaling.
- [Disable a scaling policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enable-disable-scaling-policy.html): Temporarily disable scaling policy so instance count stays the same while preserving the scaling policy configuration details.
- [Delete a scaling policy for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/deleting-scaling-policy.html): Delete a scaling policy for Auto Scaling group along with the CloudWatch alarms if needed.
- [AWS CLI examples for scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/examples-scaling-policies.html): You can create scaling policies for Amazon EC2 Auto Scaling through the AWS Management Console, AWS Command Line Interface (AWS CLI), or SDKs.

### [Predictive scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)

Configure predictive scaling to proactively increase capacity of your Auto Scaling group to match anticipated load based on analysis of historical data.

- [How predictive scaling works](https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-policy-overview.html): This topic explains how predictive scaling works and describes what to consider when you create a predictive scaling policy.
- [Create a predictive scaling policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-create-policy.html): Create a predictive scaling policy for Amazon EC2 Auto Scaling using the AWS Management Console or AWS CLI..

### [Evaluate your predictive scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-graphs.html)

Evaluate your predictive scaling policies by reviewing the recommendations and other data.

- [Monitor metrics with CloudWatch](https://docs.aws.amazon.com/autoscaling/ec2/userguide/monitor-predictive-scaling-cloudwatch.html): Depending on your needs, you might prefer to access monitoring data for predictive scaling from Amazon CloudWatch instead of the Amazon EC2 Auto Scaling console.
- [Override the forecast](https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-overriding-forecast-capacity.html): Override predictive scaling forecast values using scheduled actions.

### [Use custom metrics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-customized-metric-specification.html)

Use a custom metrics configuration in an Auto Scaling predictive scaling policy.

### [Constructing the JSON for custom metrics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/construct-json-custom-metrics.html)

The following section contains examples for how to configure predictive scaling to query data from CloudWatch.

- [Use metric math expressions](https://docs.aws.amazon.com/autoscaling/ec2/userguide/using-math-expression-examples.html): The following section provides information and examples of predictive scaling policies that show how you can use metric math in your policy.
- [Considerations for custom metrics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/custom-metrics-troubleshooting.html): If an issue occurs while using custom metrics, we recommend that you do the following:

### [Control instance termination](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html)

Customize instance termination order and protect instances from premature termination using Auto Scaling custom policies or instance scale in protection.

### [Configure termination policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html)

Configure termination policies to control instance termination order in Auto Scaling.

- [Change the termination policy for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/custom-termination-policy.html): To change the termination policy for your Auto Scaling group, use one of the following methods.
- [Create a custom termination policy with Lambda](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lambda-custom-termination-policy.html): Learn how to create a custom termination policy with Lambda.
- [Use instance scale-in protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html): Use instance scale-in protection to protect instances from unwanted terminations in Amazon EC2 Auto Scaling.
- [Design for graceful instance termination](https://docs.aws.amazon.com/autoscaling/ec2/userguide/gracefully-handle-instance-termination.html): Prevent unexpected instance termination when Auto Scaling responds to a scale in event by gracefully handling instance termination.

### [Suspend-resume processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html)

Suspend and then resume one or more of the standard processes that are built into Amazon EC2 Auto Scaling.

- [Considerations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/suspend-resume-considerations.html): Consider the following before suspending processes:
- [Suspend processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/suspend-processes.html): To suspend a process for an Auto Scaling group, use one of the following methods:
- [Resume processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/resume-processes.html): To resume a suspended process for an Auto Scaling group, use one of the following methods:
- [How suspended processes affect other processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/understand-how-suspending-processes-affects-other-processes.html): The following sections describe what happens when different processes are suspended individually.


## [Monitor](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-monitoring-features.html)

### [Health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html)

Learn how Amazon EC2 Auto Scaling monitors and responds to health check failures and mitigates against the possibility of false positives.

- [About health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html): Learn about Amazon EC2, Elastic Load Balancing, VPC Lattice, and custom health checks to minimize downtime for your Auto Scaling groups.
- [Set the health check grace period](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html): Learn how to set the health check grace period for your Auto Scaling group.

### [Monitor for impaired Amazon EBS volumes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/monitor-and-replace-instances-with-impaired-ebs-volumes.html)

Learn how to turn on the Amazon EBS health checks for your Auto Scaling group to make sure that Auto Scaling monitors the entire system.

- [Turn off Amazon EBS health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/turn-off-ebs-health-checks.html): Learn how to turn off Amazon EBS health checks for your Auto Scaling group.
- [Set up a custom health check](https://docs.aws.amazon.com/autoscaling/ec2/userguide/set-up-a-custom-health-check.html): Describes how to integrate your custom health checks with the existing health check options provided by Amazon EC2 Auto Scaling.
- [View the reason for health check failures](https://docs.aws.amazon.com/autoscaling/ec2/userguide/replace-unhealthy-instance.html): Using the following procedure, you can view information about any instances replaced due to a health check.
- [Troubleshoot unhealthy instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-healthchecks.html): Troubleshoot unhealthy instances with the error messages returned by Amazon EC2 Auto Scaling.
- [Monitor with Health Dashboard](https://docs.aws.amazon.com/autoscaling/ec2/userguide/monitoring-personal-health-dashboard.html): Your Health Dashboard provides support for notifications that come from Amazon EC2 Auto Scaling.

### [Monitor CloudWatch metrics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.html)

Learn how to monitor CloudWatch metrics for your Auto Scaling groups and instances.

- [View monitoring graphs in the Amazon EC2 Auto Scaling console](https://docs.aws.amazon.com/autoscaling/ec2/userguide/viewing-monitoring-graphs.html): Monitor minute-by-minute progress of individual Auto Scaling groups using CloudWatch metrics.
- [CloudWatch metrics for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-metrics.html): Learn about the aggregated metrics and dimensions Amazon EC2 Auto Scaling sends to CloudWatch and the procedures to use to enable or disable Auto Scaling group metrics.
- [Configure monitoring for Auto Scaling instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-as-instance-metrics.html): Learn how to configure CloudWatch monitoring for your Auto Scaling instances.
- [Log API calls using CloudTrail](https://docs.aws.amazon.com/autoscaling/ec2/userguide/logging-using-cloudtrail.html): Learn about logging Amazon EC2 Auto Scaling with AWS CloudTrail.
- [Amazon SNS notification options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-sns-notifications.html): Learn how to get notifications from Amazon SNS when your Auto Scaling group launches or terminates instances.


## [Work with other services](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-integrations.html)

### [Capacity Rebalancing](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html)

Learn how Capacity Rebalancing in Auto Scaling helps maintain workload availability by proactively replacing Spot Instance that have received a rebalance recommendation.

- [Enable Capacity Rebalancing](https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-capacity-rebalancing-console-cli.html): learn how to use the AWS Management Console or AWS CLI to enable Capacity Rebalancing to proactively replace Spot Instances that have received a rebalance recommendation.

### [Capacity Reservations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-ec2-capacity-reservations.html)

Learn how to reserve capacity in specific Availability Zones with On-Demand Capacity Reservation using Auto Scaling group and targeted reservations.

- [Use Capacity Reservation preference](https://docs.aws.amazon.com/autoscaling/ec2/userguide/capacity-reservation-create-asg-procedure.html): Use Capacity Reservations with your Auto Scaling group.
- [Interruptible Capacity Reservations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-interruptible-capacity-reservations.html): Learn how to use Interruptible Capacity Reservations with Auto Scaling groups for interruptible workloads that can handle capacity reclamation with 2-minute notice.
- [AWS CloudShell](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-auto-scaling-groups-with-cloudshell.html): Learn how to get started building with AWS CloudShell in the AWS Management Console.
- [CloudFormation](https://docs.aws.amazon.com/autoscaling/ec2/userguide/creating-auto-scaling-groups-with-cloudformation.html): Learn how to create Auto Scaling groups using AWS CloudFormation.
- [Compute Optimizer](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-getting-recommendations.html): Learn how to get instance type recommendations and decide whether to move to a new instance type for your Auto Scaling group with AWS Compute Optimizer.

### [Elastic Load Balancing](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html)

Learn how to use Elastic Load Balancing with your Auto Scaling group to distribute traffic across the instances in your Auto Scaling group.

- [Prepare to attach a load balancer](https://docs.aws.amazon.com/autoscaling/ec2/userguide/getting-started-elastic-load-balancing.html): Discover how to complete the prerequisites for using Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group.
- [Attach a load balancer](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html): Learn how to attach and detach an Elastic Load Balancing load balancer to your Auto Scaling group and enable the Elastic Load Balancing health checks.
- [Configure a load balancer](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-create-load-balancer-console.html): Learn how to create or attach an Application Load Balancer or Network Load Balancer using the Amazon EC2 Auto Scaling console.
- [Verify the attachment status](https://docs.aws.amazon.com/autoscaling/ec2/userguide/load-balancer-status.html): Discover how to verify the attachment status of your load balancer after attaching it to your Auto Scaling group.
- [Add an Availability Zone](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-az-console.html): Learn how to use geographic redundancy to enhance reliability by spanning Auto Scaling groups across multiple Availability Zones and attaching a load balancer to distribute incoming traffic.
- [Remove an Availability Zone](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-remove-az-console.html): Learn how to remove an Availability Zone from your Auto Scaling group and load balancer.
- [Detach a load balancer](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-remove-load-balancer.html): Learn how to detach a load balancer from your Auto Scaling group when you no longer need it.
- [AWS CLI examples for working with Elastic Load Balancing](https://docs.aws.amazon.com/autoscaling/ec2/userguide/examples-elastic-load-balancing-aws-cli.html): Learn how to use the AWS CLI to work with Elastic Load Balancing by attaching, detaching, and describing load balancers and target groups.

### [VPC Lattice](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-vpc-lattice.html)

Learn how to use VPC Lattice to manage traffic flow and API calls between your applications and services that run on separate resources.

- [Prepare to attach a target group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/getting-started-vpc-lattice.html): Complete the prerequisites for using VPC Lattice to route traffic to your Auto Scaling group.
- [Attach a VPC Lattice target group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-vpc-lattice-target-group-asg.html): Learn how to attach and detach a VPC Lattice target group to an Auto Scaling group and enable the VPC Lattice health checks.
- [Verify the attachment status](https://docs.aws.amazon.com/autoscaling/ec2/userguide/verify-target-group-attachment-status.html): Explains how to verify the attachment status of your target group after attaching it to your Auto Scaling group.

### [EventBridge](https://docs.aws.amazon.com/autoscaling/ec2/userguide/automating-ec2-auto-scaling-with-eventbridge.html)

Learn how to use EventBridge to handle events that are specific to Amazon EC2 Auto Scaling.

- [Amazon EC2 Auto Scaling event reference](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-event-reference.html): Learn about the EventBridge event types that you can use to filter for events specific to Amazon EC2 Auto Scaling.
- [Instance refresh example events and patterns](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-refresh-eventbridge-events.html): Learn how to filter events that match specific values when creating EventBridge rules for instance refresh in an Auto Scaling group.
- [Warm pool example events and patterns](https://docs.aws.amazon.com/autoscaling/ec2/userguide/warm-pools-eventbridge-events.html): Learn how to filter events that match specific values when creating EventBridge rules for an Auto Scaling group that has a warm pool.

### [EventBridge rules](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-eventbridge-rules.html)

Learn how to write rules that automate the actions to take when an event pattern matches the rule. using Amazon EventBridge.

- [Create EventBridge rules for instance refresh events](https://docs.aws.amazon.com/autoscaling/ec2/userguide/monitor-events-eventbridge-sns.html): Learn how to create an EventBridge rule that notifies you when a checkpoint is reached during an instance refresh.
- [Create EventBridge rules for warm pool events](https://docs.aws.amazon.com/autoscaling/ec2/userguide/warm-pool-events-eventbridge-rules.html): Learn how to create EventBridge rules that act when your Auto Scaling group with a warm pool emits an event.
- [Amazon VPC](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html): Learn about using Amazon VPC to provide network connectivity for your Auto Scaling instances.


## [Security](https://docs.aws.amazon.com/autoscaling/ec2/userguide/security.html)

- [Infrastructure security](https://docs.aws.amazon.com/autoscaling/ec2/userguide/infrastructure-security.html): Learn how Amazon EC2 Auto Scaling isolates service traffic.
- [Resilience](https://docs.aws.amazon.com/autoscaling/ec2/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon EC2 Auto Scaling features for application resiliency.

### [Data protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon EC2 Auto Scaling.

- [AWS KMS key policy for use with encrypted volumes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html): How to configure key policies for Amazon EC2 Auto Scaling.

### [Identity and Access Management](https://docs.aws.amazon.com/autoscaling/ec2/userguide/security-iam.html)

How to authenticate requests and manage access to your Amazon EC2 Auto Scaling resources.

- [How Amazon EC2 Auto Scaling works with IAM](https://docs.aws.amazon.com/autoscaling/ec2/userguide/control-access-using-iam.html): Understand how Amazon EC2 Auto Scaling works with IAM.
- [API permissions](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-api-permissions.html): Learn about the permissions that you must grant users so that they can call specific Amazon EC2 Auto Scaling API actions.
- [Managed policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/security-iam-awsmanpol.html): Learn about Amazon EC2 Auto Scaling managed policies and recent changes to those policies.
- [Service-linked roles](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-service-linked-role.html): Amazon EC2 Auto Scaling uses service-linked roles for the permissions that it requires to call other AWS services on your behalf.
- [Identity-based policy examples](https://docs.aws.amazon.com/autoscaling/ec2/userguide/security_iam_id-based-policy-examples.html): By default, a brand new user in your AWS account has no permissions to do anything.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/autoscaling/ec2/userguide/cross-service-confused-deputy-prevention.html): How to prevent the cross-service confused deputy problem for Amazon EC2 Auto Scaling resources.
- [Control Amazon EC2 launch template usage in Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html): Learn how to set Amazon EC2 launch template permissions.
- [IAM role for applications that run on Amazon EC2 instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html): How to launch Amazon EC2 instances with an IAM role.
- [Compliance validation](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Use VPC endpoints for private connectivity](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-vpc-endpoints.html): Access the Amazon EC2 Auto Scaling API from your VPC without sending traffic over the internet.


## [Code examples](https://docs.aws.amazon.com/autoscaling/ec2/userguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/service_code_examples_basics.html)

The following code examples show how to use the basics of Auto Scaling with AWS SDKs.

- [Hello Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_Hello_section.html): Hello Auto Scaling
- [Learn the basics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_Scenario_GroupsAndInstances_section.html): Learn the basics of Auto Scaling with an AWS SDK

### [Actions](https://docs.aws.amazon.com/autoscaling/ec2/userguide/service_code_examples_actions.html)

The following code examples show how to use Auto Scaling with AWS SDKs.

- [AttachInstances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_AttachInstances_section.html): Use AttachInstances with a CLI
- [AttachLoadBalancerTargetGroups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_AttachLoadBalancerTargetGroups_section.html): Use AttachLoadBalancerTargetGroups with an AWS SDK or CLI
- [AttachLoadBalancers](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_AttachLoadBalancers_section.html): Use AttachLoadBalancers with a CLI
- [CompleteLifecycleAction](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_CompleteLifecycleAction_section.html): Use CompleteLifecycleAction with a CLI
- [CreateAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_CreateAutoScalingGroup_section.html): Use CreateAutoScalingGroup with an AWS SDK or CLI
- [CreateLaunchConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_CreateLaunchConfiguration_section.html): Use CreateLaunchConfiguration with a CLI
- [CreateOrUpdateTags](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_CreateOrUpdateTags_section.html): Use CreateOrUpdateTags with a CLI
- [DeleteAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DeleteAutoScalingGroup_section.html): Use DeleteAutoScalingGroup with an AWS SDK or CLI
- [DeleteLaunchConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DeleteLaunchConfiguration_section.html): Use DeleteLaunchConfiguration with a CLI
- [DeleteLifecycleHook](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DeleteLifecycleHook_section.html): Use DeleteLifecycleHook with a CLI
- [DeleteNotificationConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DeleteNotificationConfiguration_section.html): Use DeleteNotificationConfiguration with a CLI
- [DeletePolicy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DeletePolicy_section.html): Use DeletePolicy with a CLI
- [DeleteScheduledAction](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DeleteScheduledAction_section.html): Use DeleteScheduledAction with a CLI
- [DeleteTags](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DeleteTags_section.html): Use DeleteTags with a CLI
- [DescribeAccountLimits](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeAccountLimits_section.html): Use DescribeAccountLimits with a CLI
- [DescribeAdjustmentTypes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeAdjustmentTypes_section.html): Use DescribeAdjustmentTypes with a CLI
- [DescribeAutoScalingGroups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeAutoScalingGroups_section.html): Use DescribeAutoScalingGroups with an AWS SDK or CLI
- [DescribeAutoScalingInstances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeAutoScalingInstances_section.html): Use DescribeAutoScalingInstances with an AWS SDK or CLI
- [DescribeAutoScalingNotificationTypes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeAutoScalingNotificationTypes_section.html): Use DescribeAutoScalingNotificationTypes with a CLI
- [DescribeLaunchConfigurations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeLaunchConfigurations_section.html): Use DescribeLaunchConfigurations with a CLI
- [DescribeLifecycleHookTypes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeLifecycleHookTypes_section.html): Use DescribeLifecycleHookTypes with a CLI
- [DescribeLifecycleHooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeLifecycleHooks_section.html): Use DescribeLifecycleHooks with a CLI
- [DescribeLoadBalancers](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeLoadBalancers_section.html): Use DescribeLoadBalancers with a CLI
- [DescribeMetricCollectionTypes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeMetricCollectionTypes_section.html): Use DescribeMetricCollectionTypes with a CLI
- [DescribeNotificationConfigurations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeNotificationConfigurations_section.html): Use DescribeNotificationConfigurations with a CLI
- [DescribePolicies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribePolicies_section.html): Use DescribePolicies with a CLI
- [DescribeScalingActivities](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeScalingActivities_section.html): Use DescribeScalingActivities with an AWS SDK or CLI
- [DescribeScalingProcessTypes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeScalingProcessTypes_section.html): Use DescribeScalingProcessTypes with a CLI
- [DescribeScheduledActions](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeScheduledActions_section.html): Use DescribeScheduledActions with a CLI
- [DescribeTags](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeTags_section.html): Use DescribeTags with a CLI
- [DescribeTerminationPolicyTypes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeTerminationPolicyTypes_section.html): Use DescribeTerminationPolicyTypes with a CLI
- [DetachInstances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DetachInstances_section.html): Use DetachInstances with a CLI
- [DetachLoadBalancers](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DetachLoadBalancers_section.html): Use DetachLoadBalancers with a CLI
- [DisableMetricsCollection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DisableMetricsCollection_section.html): Use DisableMetricsCollection with an AWS SDK or CLI
- [EnableMetricsCollection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_EnableMetricsCollection_section.html): Use EnableMetricsCollection with an AWS SDK or CLI
- [EnterStandby](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_EnterStandby_section.html): Use EnterStandby with a CLI
- [ExecutePolicy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_ExecutePolicy_section.html): Use ExecutePolicy with a CLI
- [ExitStandby](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_ExitStandby_section.html): Use ExitStandby with a CLI
- [PutLifecycleHook](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_PutLifecycleHook_section.html): Use PutLifecycleHook with a CLI
- [PutNotificationConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_PutNotificationConfiguration_section.html): Use PutNotificationConfiguration with a CLI
- [PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_PutScalingPolicy_section.html): Use PutScalingPolicy with a CLI
- [PutScheduledUpdateGroupAction](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_PutScheduledUpdateGroupAction_section.html): Use PutScheduledUpdateGroupAction with a CLI
- [RecordLifecycleActionHeartbeat](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_RecordLifecycleActionHeartbeat_section.html): Use RecordLifecycleActionHeartbeat with a CLI
- [ResumeProcesses](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_ResumeProcesses_section.html): Use ResumeProcesses with a CLI
- [SetDesiredCapacity](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_SetDesiredCapacity_section.html): Use SetDesiredCapacity with an AWS SDK or CLI
- [SetInstanceHealth](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_SetInstanceHealth_section.html): Use SetInstanceHealth with a CLI
- [SetInstanceProtection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_SetInstanceProtection_section.html): Use SetInstanceProtection with a CLI
- [SuspendProcesses](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_SuspendProcesses_section.html): Use SuspendProcesses with a CLI
- [TerminateInstanceInAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_TerminateInstanceInAutoScalingGroup_section.html): Use TerminateInstanceInAutoScalingGroup with an AWS SDK or CLI
- [UpdateAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_UpdateAutoScalingGroup_section.html): Use UpdateAutoScalingGroup with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/autoscaling/ec2/userguide/service_code_examples_scenarios.html)

The following code examples show how to use Auto Scaling with AWS SDKs.

- [Build and manage a resilient service](https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_cross_ResilientService_section.html): Build and manage a resilient service using an AWS SDK


## [Troubleshoot](https://docs.aws.amazon.com/autoscaling/ec2/userguide/CHAP_Troubleshooting.html)

- [Instance launch failure](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-instancelaunchfailure.html): Troubleshoot issues with Amazon EC2 Auto Scaling with EC2 instances that fail to launch.
- [AMI issues](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-ami.html): Troubleshoot issues with Auto Scaling with your Amazon EC2 AMIs.
- [Load balancer issues](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-loadbalancer.html): Troubleshoot scaling issues caused by the load balancer configuration.
- [Launch template issues](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-launch-template.html): Troubleshoot issues with Amazon EC2 Auto Scaling with launch templates.
