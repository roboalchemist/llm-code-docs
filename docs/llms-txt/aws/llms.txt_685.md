# Source: https://docs.aws.amazon.com/r53recovery/latest/dg/llms.txt

# Amazon Application Recovery Controller (ARC) Developer Guide

> Amazon Application Recovery Controller (ARC) features improve application availability by allowing you to centrally coordinate failover within an AWS Region, with multiple Availability Zones, or across multiple Regions. ARC provides continuous recovery readiness checks for Regional failover, to audit whether your applications are configured the same across Regions. Then, ARC provides extremely reliable failover, through routing control or zonal shift, to recover applications during events.

- [What is ARC?](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html)
- [Compare multi-AZ and multi-Region capabilities](https://docs.aws.amazon.com/r53recovery/latest/dg/compare-capabilities.html)
- [Document history](https://docs.aws.amazon.com/r53recovery/latest/dg/doc-history.html)

## [Multi-AZ recovery](https://docs.aws.amazon.com/r53recovery/latest/dg/multi-az.html)

### [Zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html)

Zonal shifts in Amazon Application Recovery Controller (ARC)remove capacity from a live application, so it's important to be careful when you use these capabilities in production.

- [How a zonal shift works](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.how-it-works.html): When you start a zonal shift for a supported resource, traffic for the resource is moved away from the Availability Zone (AZ) that you've specified.
- [AWS Regions](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-regions-zonal.html): An overview of the Regional support for Amazon Application Recovery Controller (ARC).
- [Zonal shift components](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-components-zonal.html): Description of the components in Amazon Application Recovery Controller (ARC) zonal shift.
- [Data and control planes](https://docs.aws.amazon.com/r53recovery/latest/dg/data-and-control-planes-zonal-shift.html): Learn how the data plane and control plane structures for zonal shift.
- [Pricing](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-pricing-zonal-shift.html): For zonal shift, you can start a zonal shift for supported resources, to recover your application from an issue in an Availability Zone.
- [Best practices](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.zonal-shifts.html): We recommend the following best practices for using zonal shifts for multi-AZ recovery in ARC.
- [API operations](https://docs.aws.amazon.com/r53recovery/latest/dg/actions.zonalshift.html): The following table lists ARC API operations that you can use using zonal shift, which moves traffic away from an Availability Zone for multi-AZ applications.
- [Examples of using CLI operations](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonalshift.html): This section provides application examples of using zonal shift, using the AWS Command Line Interface to work with the zonal shift capability in Amazon Application Recovery Controller (ARC) using API operations.

### [Supported resources](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.html)

Amazon Application Recovery Controller (ARC) currently supports enabling the following resources for zonal shift and zonal autoshift:

- [Auto Scaling groups](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html): An Amazon EC2 Auto Scaling group contains a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management.
- [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html): Amazon EKS provides features that enable you to make your applications more resilient to events such as the degraded health or the impairment of an Availability Zone.
- [Application Load Balancers](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html)
- [Network Load Balancers](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html)
- [Starting, updating, or canceling a zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.start-cancel.html): This section provides procedures for working with zonal shifts, including starting a zonal shift and canceling a zonal shift.

### [Logging and monitoring](https://docs.aws.amazon.com/r53recovery/latest/dg/monitoring-zonal-shift.html)

Use AWS CloudTrail for monitoring for zonal shift in Amazon Application Recovery Controller (ARC).

- [CloudTrail logs](https://docs.aws.amazon.com/r53recovery/latest/dg/cloudtrail-zonal-shift.html): Learn about logging zonal shift in ARC with AWS CloudTrail.

### [IAM for zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-zonalshift.html)

Learn how to authenticate requests and manage access to zonal shift resources.

- [How zonal shift works with IAM](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_service-with-iam-zs.html): Before you use IAM to manage access to zonal shift in Amazon Application Recovery Controller (ARC), learn what IAM features are available to use with zonal shift.
- [Permissions for zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_service-with-iam-zonal-shift.html): This section provides additional information about how permissions work for the zonal shift feature in Amazon Application Recovery Controller (ARC), especially if you work with the feature from another AWS service, such as Elastic Load Balancing.
- [Identity-based policy examples](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_id-based-policy-examples-zonal.html): By default, users and roles don't have permission to create or modify ARC resources.

### [Zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.html)

With zonal autoshift in Amazon Application Recovery Controller (ARC), AWS shifts traffic for an AWS resource away from a potentially impaired Availability Zone, on your behalf, to healthy AZs in the AWS Region.

### [How zonal autoshift works](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html)

The zonal autoshift capability in Amazon Application Recovery Controller (ARC) allows AWS to shift traffic for a resource away from an Availability Zone, on your behalf, when AWS determines that there's an impairment that could potentially affect customers in the Availability Zone.

- [About zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.about.html): Zonal autoshift is a capability where AWS shifts application resource traffic away from an Availability Zone, on your behalf.
- [When AWS starts and stops autoshifts](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.start-stop-auto.html): When you enable zonal autoshift for a resource, you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery.
- [When ARC schedules, starts, and ends practice runs](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.scheduled-practice-runs.html): ARC schedules a practice run for a resource weekly, for about 30 minutes.
- [Capacity checks for practice runs](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.capacity-check.html): When a practice run starts, to temporarily move traffic away from an Availability Zone, ARC runs a check to verify that you have enough capacity in other Availability Zones to safely move traffic away from the AZ.
- [Notification for practice runs and autoshifts](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.notifications.html): You can choose to be notified about practice runs and autoshifts for your resource by setting up Amazon EventBridge notifications.
- [Precedence for zonal shifts](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.precedence.html): There can be no more than one applied zonal shift at a given time.
- [Stopping an active autoshift or practice run](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.stop-shift.html): To stop an in-progress autoshift for a resource you must cancel the zonal shift.
- [How traffic is shifted away](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.how-traffic-shifted.html): For autoshifts and for practice run zonal shifts, traffic is shifted away from an Availability Zone using the same mechanism that ARC uses for customer-initiated zonal shifts.
- [Alarms for practice runs](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.alarms.html): You can specify two types of CloudWatch alarms for practice runs in zonal autoshift: outcome alarms and blocking alarms.
- [Blocked windows and allowed windows (in UTC)](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.blocked-windows.html): You have the option to block or allow practice runs for specific calendar dates, or for specific time windows, that is, days and times, specified in UTC.
- [AWS Regions](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-region-zonal-autoshift.html): An overview of the Regional support for Amazon Application Recovery Controller (ARC).
- [Zonal autoshift components](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-components-zonal-autoshift.html): Description of the components in Amazon Application Recovery Controller (ARC) zonal autoshift.
- [Data and control planes](https://docs.aws.amazon.com/r53recovery/latest/dg/data-and-control-planes-zonal-autoshift.html): Learn how the data plane and control plane structures for zonal autoshift.
- [Pricing](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-pricing-zonal-autoshift.html): For zonal autoshift, AWS shifts traffic away from an Availability Zone on your behalf for supported resources when AWS determines that there is a potential issue that can adversely affect customer applications.
- [Best practices](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html): Be aware of the following best practices and considerations when you enable zonal autoshift in Amazon Application Recovery Controller (ARC).
- [API operations](https://docs.aws.amazon.com/r53recovery/latest/dg/actions.zonalautoshift.html): The following table lists ARC API operations that you can use with zonal autoshift.

### [Examples of using CLI operations](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonal-autoshift.html)

This section walks through simple application examples of working with zonal autoshift, using the AWS Command Line Interface to work with the zonal autoshift capability in Amazon Application Recovery Controller (ARC) using API operations.

- [Create a practice run configuration](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-update-zonal_autoshift.create-practice-run.html): Before you can enable zonal autoshift for a resource, you must create a practice run configuration for the resource, to choose options for the required practice runs.
- [Enable or disable autoshifts](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonal-autoshift.update-autoshift.html): You enable or disable autoshifts for a resource by updating the zonal autoshift status with the CLI.
- [Start an on-demand practice run](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonal-autoshift.start-practice-run.html): You can start an on-demand practice run zonal shift with the CLI by using the start-practice-run command.
- [Cancel an in-progress practice run](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonal-autoshift.cancel-practice-run.html): You can cancel an in-progress practice run with the CLI by using the cancel-practice-run command.
- [Cancel an in-progress autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonal-autoshift.cancel-autoshift.html): You can cancel an in-progress autoshift with the CLI by canceling the zonal autoshift for the resource.
- [Edit a practice run configuration](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonal_autoshift.edit-practice-run-config.html): You can edit a practice run configuration for a resource with the CLI to update different configuration options, such as changing the alarms for practice runs or updating the blocked dates or blocked windows, when ARC won't start practice runs.
- [Delete a practice run configuration](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonal-autoshift.delete-practice-run-config.html): You can delete a practice run configuration for a resource, but you must first disable zonal autoshift for the resource.

### [Enabling and working with zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.start-cancel.html)

This section provides procedures for working with zonal autoshifts in Amazon Application Recovery Controller (ARC).

- [Configuring, editing, or deleting a practice run configuration](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.edit-delete-practice-run.html): The steps in this section explain how to edit or delete a practice run configuration on the Amazon Application Recovery Controller (ARC) console.
- [Canceling a zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.canceling-an-autoshift.html): To stop an in-progress zonal autoshift for a resource, you must cancel the zonal autoshift.
- [Starting a practice run zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.start-practice-run.html): The steps in this section explain how to start an on-demand practice run zonal shift on the ARC console.
- [Canceling a practice run zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.cancel-practice-run.html): The steps in this section explain how to cancel a zonal shift on the ARC console.
- [Enabling or disabling autoshift observer notification](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.enable-autoshift-observer.html): You can configure zonal autoshift to notify you, through Amazon EventBridge, whenever AWS starts an autoshift to shift traffic away from a potentially impaired Availability Zone.
- [Testing zonal autoshift with AWS FIS](https://docs.aws.amazon.com/r53recovery/latest/dg/testing-zonal-autoshift-fis.html): You can use AWS Fault Injection Service to set up and run experiments that help you simulate real-world conditions, such as the AZ Availability: Power Interruption scenario, that will demonstrate what happens when AWS starts a zonal autoshift on your autoshift-enabled resources during a potentially widespread AZ impairment.

### [Logging and monitoring](https://docs.aws.amazon.com/r53recovery/latest/dg/monitoring-zonal-autoshift.html)

Use AWS CloudTrail for monitoring for zonal autoshift in Amazon Application Recovery Controller (ARC).

- [CloudTrail logs](https://docs.aws.amazon.com/r53recovery/latest/dg/cloudtrail-zonal-autoshift.html): Learn about logging ARC with AWS CloudTrail.
- [EventBridge](https://docs.aws.amazon.com/r53recovery/latest/dg/eventbridge-zonal-autoshift.html): Learn about monitoring zonal autoshift in ARC with Amazon EventBridge

### [Identity and Access Management](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-zonalautoshift.html)

Learn how to authenticate requests and manage access to your ARC zonal autoshift resources.

- [How zonal autoshift works with IAM](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_service-with-iam-zonalautoshift.html): Before you use IAM to manage access to zonal autoshift in Amazon Application Recovery Controller (ARC), learn what IAM features are available to use with zonal autoshift.
- [Identity-based policy examples](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_id-based-policy-examples-zonalautoshift.html): By default, users and roles don't have permission to create or modify ARC resources.
- [Service-linked role](https://docs.aws.amazon.com/r53recovery/latest/dg/using-service-linked-roles-zonal-autoshift.html): How to use service-linked roles to give ARC access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol-zonal-autoshift.html): Learn about AWS managed policies for ARC and recent changes to those policies.
- [Quotas](https://docs.aws.amazon.com/r53recovery/latest/dg/quotas.zonal-autoshift.html): Zonal autoshift in Amazon Application Recovery Controller (ARC) is subject to the following quotas.


## [Multi-Region recovery](https://docs.aws.amazon.com/r53recovery/latest/dg/multi-region.html)

### [Routing control](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html)

Set up routing control in Amazon Application Recovery Controller (ARC) so that you can manage traffic failover by rerouting traffic from one cell (Availability Zone or Region) to another.

- [About routing control](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.about.html): Routing control redirects traffic by using health checks in Amazon RouteÂ 53 that are configured with DNS records associated with the top-level resource of the cells in your recovery group, such as an Elastic Load Balancing load balancer.
- [AWS Regions](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-regions-routing.html): An overview of the Regional support for Amazon Application Recovery Controller (ARC) routing control.
- [Components](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-components-routing.html): Description of the components in Amazon Application Recovery Controller (ARC) routing control.
- [Data and control planes](https://docs.aws.amazon.com/r53recovery/latest/dg/data-and-control-planes.html): Learn how the data plane and control plane structures for routing control.
- [Tagging](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-tagging-routing-control.html): Tags are words or phrases (meta data) that you use to identify and organize your AWS resources.
- [Pricing](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-pricing-routing-control.html): For routing control in ARC, you pay an hourly cost per cluster that you create.
- [Getting started with multi-Region recovery](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started.html): Get started with multi-Region recovery in Amazon Application Recovery Controller (ARC) by analyzing and reviewing your architecture.
- [Best practices](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.regional.html): We recommend the following best practices for recovery and failover preparedness for routing control in ARC.

### [API operations](https://docs.aws.amazon.com/r53recovery/latest/dg/actions.routing-control.html)

This section includes tables with lists API operations that you can use for setting up and using routing control in Amazon Application Recovery Controller (ARC), with links to relevant documentation.

- [Working with AWS SDKs](https://docs.aws.amazon.com/r53recovery/latest/dg/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.

### [Examples of using CLI operations](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-routing.html)

This section walks through simple application examples of working with routing control, using the AWS Command Line Interface to work with the routing control capability in Amazon Application Recovery Controller (ARC) using API operations.

- [Set up routing control components](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-routing-config.html): Our first step is to create a cluster.
- [Update control states with the CLI](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-routing.control-state.html): After you create your Amazon Application Recovery Controller (ARC) resources, such as cluster, routing controls, and control panels, you can interact with the cluster to list and update routing control states for failover.

### [Working with routing control components](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.working-with.html)

### [Creating routing control components](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.create.html)

This section explains how to create a cluster, routing controls, health checks, and control panels for working with routing control in Amazon Application Recovery Controller (ARC).

- [Creating a cluster](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.create-cluster.html): You must create a cluster to host routing controls and control panels in ARC.
- [Creating a routing control](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.create-control.html): Create a routing control for each cell that you want to route traffic to.
- [Creating a routing control health check](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.create-health-check.html): You associate a routing control health check with each routing control that you want to use for rerouting traffic.
- [Creating a control panel](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.create-control-panel.html): A control panel in Amazon Application Recovery Controller (ARC) lets you group together related routing controls.

### [Viewing and updating routing control states](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.html)

This section describes how to view and update routing control states in Amazon Application Recovery Controller (ARC).

- [Getting and updating routing control states using the API](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.api.html): We recommend that you use Amazon Application Recovery Controller (ARC) API operations to get or update routing control states, by using an AWS CLI command or by using code that you have developed to use ARC API operations with one of the AWS SDKs.
- [Getting and updating routing control states using the console](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.console.html): You can get and update routing control states in the AWS Management Console.

### [Creating safety rules](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.safety-rules.html)

When you work with several routing controls at the same time, you might decide that you want safeguards in place to avoid unintended consequences.

- [Creating a safety rule](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.create-safety-rule.html): The steps in this section explain how to create a safety rule on the ARC console.
- [Editing or deleting a safety rule](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.edit-delete-safety-rule.html): The steps in this section explain how to edit or delete a safety rule on the ARC console.
- [Overriding safety rules](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html): There are scenarios when you might want to bypass the routing control safeguards that are enforced with safety rules that you've configured.
- [Support cross-account clusters](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.failover-different-accounts.html): Amazon Application Recovery Controller (ARC) integrates with AWS Resource Access Manager to enable resource sharing.

### [Logging and monitoring](https://docs.aws.amazon.com/r53recovery/latest/dg/monitoring-routing.html)

Use AWS CloudTrail for monitoring for routing control in Amazon Application Recovery Controller (ARC).

- [CloudTrail logs](https://docs.aws.amazon.com/r53recovery/latest/dg/cloudtrail-routing.html): Learn about logging Amazon Application Recovery Controller (ARC) with AWS CloudTrail.

### [Identity and Access Management](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-routing.html)

Learn how to authenticate requests and manage access to your ARC resources.

- [How routing control works with IAM](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_service-with-iam-routing.html): Before you use IAM to manage access to routing control in Amazon Application Recovery Controller (ARC), learn what IAM features are available to use with routing control.
- [Identity-based policy examples](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_id-based-policy-examples-routing.html): By default, users and roles don't have permission to create or modify ARC resources.
- [AWS managed policies](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol-routing.html): Learn about AWS managed policies for ARC and recent changes to those policies.
- [Quotas](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.quotas.html): View the quotas (also known as limits) for Amazon Application Recovery Controller (ARC) routing control.

### [Readiness check](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.html)

Use readiness check in Amazon Application Recovery Controller (ARC) to help prepare for failover recovery.

### [What is readiness check?](https://docs.aws.amazon.com/r53recovery/latest/dg/readiness-what-is.html)

A readiness check in ARC continually (at one-minute intervals) audits for mismatches in AWS provisioned capacity, service quotas, throttle limits, and configuration and version discrepancies for the resources included in the check.

- [How readiness status works](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.rules.html): ARC readiness checks determine readiness status based on the predefined rules for each resource type and the way those rules are defined.
- [How components work together](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.recovery-groups.readiness-scope.html): Readiness checks always audit groups of resources in resource sets.
- [Auditing resiliency readiness](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.readiness-checks.architectural.html): With DNS target resource readiness checks in ARC, you can audit the architectural and resiliency readiness of your application.
- [Readiness and disaster recovery](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.disaster.html): ARC readiness checks give you insights into whether your applications and resources are ready for recovery by helping you make sure that your applications are scaled to handle failover traffic.
- [AWS Regions](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-regions-readiness.html): An overview of the Regional support for Amazon Application Recovery Controller (ARC) readiness check.
- [Components](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-components-readiness.html): Description of the components in Amazon Application Recovery Controller (ARC) readiness check.
- [Data and control planes](https://docs.aws.amazon.com/r53recovery/latest/dg/data-and-control-planes-readiness.html): Learn how the data plane and control plane structures for readiness check.
- [Tagging](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-tagging-readiness.html): Tags are words or phrases (meta data) that you use to identify and organize your AWS resources.
- [Pricing](https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-pricing-readiness.html): You pay an hourly cost per readiness check that you configure.
- [Best practices](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.readiness.html): We recommend the following best practice for readiness check in Amazon Application Recovery Controller (ARC).
- [API operations](https://docs.aws.amazon.com/r53recovery/latest/dg/actions.readiness.html): The following table lists ARC operations that you can use for recovery readiness (readiness check), with links to relevant documentation.
- [Examples of using CLI operations](https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-readiness.html): This section walks through simple application examples, using the AWS Command Line Interface to work with readiness check features in Amazon Application Recovery Controller (ARC) using API operations.

### [Working with recovery groups and readiness checks](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.recovery-groups-and-readiness-checks.html)

This section describes and provides procedures for recovery groups and readiness checks, including creating, updating, and deleting these resources.

- [Creating and updating recovery groups](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.recovery-groups.html): A recovery group represents your application in Amazon Application Recovery Controller (ARC).
- [Creating and updating readiness checks](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.create-readiness-check-or-set.html): This section provides procedures for readiness checks and resource sets, including creating, updating, and deleting these resources.
- [Monitoring readiness status](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.status.html): You can see readiness for your application in Amazon Application Recovery Controller (ARC) at the following levels:
- [Getting architecture recommendations](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.evaluate-arch.html): If you have an existing application, Amazon Application Recovery Controller (ARC) can evaluate the architecture of your application and routing policies to provide recommendations for modifying the design to improve your application's recovery resiliency.
- [Creating cross-account authorizations](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.cross-account.html): You might have your resources distributed across multiple AWS accounts, which can make it challenging to get a comprehensive view of your applicationâs health.

### [Readiness rules, resource types, and ARNS](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.rules-and-resource-types.html)

This section includes reference information about the readiness rules descriptions, and supported resource types and the format for Amazon Resource Names (ARNs) that you use for resource sets.

- [Readiness rules descriptions](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.rules-resources.html): This section lists the readiness rules descriptions for all the types of resources supported by Amazon Application Recovery Controller (ARC).
- [Resource types and ARNs](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.resource-types-arns.html): When you create a resource set in Amazon Application Recovery Controller (ARC), you specify the type of resource to include in the set and Amazon Resource Names (ARNs) for each of the resources to include.

### [Logging and monitoring](https://docs.aws.amazon.com/r53recovery/latest/dg/monitoring-readiness.html)

Use Amazon CloudWatch, AWS CloudTrail, and Amazon EventBridge for monitoring for readiness check in Amazon Application Recovery Controller (ARC).

- [CloudWatch monitoring](https://docs.aws.amazon.com/r53recovery/latest/dg/cloudwatch-readiness.html): Learn about monitoring readiness check in ARC with Amazon CloudWatch.
- [CloudTrail logs](https://docs.aws.amazon.com/r53recovery/latest/dg/cloudtrail-readiness.html): Learn about logging readiness check with AWS CloudTrail.
- [EventBridge](https://docs.aws.amazon.com/r53recovery/latest/dg/eventbridge-readiness.html): Learn about monitoring readiness check in ARC with Amazon EventBridge.

### [Identity and Access Management](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-readiness.html)

Learn how to authenticate requests and manage access to your ARC resources.

- [How readiness check works with IAM](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_service-with-iam-readiness.html): Before you use IAM to manage access to ARC, learn what IAM features are available to use with ARC.
- [Identity-based policy examples](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_id-based-policy-examples-readiness.html): By default, users and roles don't have permission to create or modify ARC resources.
- [Service-linked roles](https://docs.aws.amazon.com/r53recovery/latest/dg/using-service-linked-roles-readiness.html): How to use service-linked roles to give ARC access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol-readiness.html): Learn about AWS managed policies for ARC and recent changes to those policies.
- [Quotas](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.quotas.html): View the quotas (also known as limits) for Amazon Application Recovery Controller (ARC) readiness check.

### [Region switch](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html)

Learn about Region switch in ARC, which provides a centralized, automated, and observable solution for multi-Region application recovery.

### [About Region switch](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch-plans.html)

With Region switch, you can orchestrate the specific steps to switch the AWS Region that your multi-Region application is running in.

- [AWS Regions](https://docs.aws.amazon.com/r53recovery/latest/dg/aws-regions-rs.html): Region switch is available in all commercial AWS Regions, as well as AWS GovCloud (US) Regions.
- [Components](https://docs.aws.amazon.com/r53recovery/latest/dg/components-rs.html): The following are components of, and concepts about, the Region switch feature in Amazon Application Recovery Controller (ARC).
- [Data and control planes](https://docs.aws.amazon.com/r53recovery/latest/dg/data-and-control-planes-rs.html): Learn about the data plane and control plane structures for Region switch.
- [Tagging](https://docs.aws.amazon.com/r53recovery/latest/dg/tagging.region-switch.html): Tags are words or phrases (meta data) that you use to identify and organize your AWS resources.
- [Pricing](https://docs.aws.amazon.com/r53recovery/latest/dg/pricing-rs.html): You pay a fixed monthly cost per Region switch plan that you configure.
- [Best practices](https://docs.aws.amazon.com/r53recovery/latest/dg/best-practices.region-switch.html): We recommend the following best practices for recovery and failover preparedness with Region switch in Amazon Application Recovery Controller (ARC).
- [Tutorial: active/passive plan](https://docs.aws.amazon.com/r53recovery/latest/dg/tutorial-region-switch.html): This tutorial guides you through creating an active/passive Region switch plan for an application running in us-east-1 and recovering into us-west-2.
- [Tutorial: Report autogeneration](https://docs.aws.amazon.com/r53recovery/latest/dg/tutorial-report-generation.html): This tutorial guides you through configuring plan execution report autogeneration for a Region switch plan.
- [Tutorial: Execute an RDS post-recovery workflow](https://docs.aws.amazon.com/r53recovery/latest/dg/tutorial-post-recovery.html): This tutorial guides you through executing a post-recovery workflow after a successful RDS failover.
- [API operations](https://docs.aws.amazon.com/r53recovery/latest/dg/actions.region-switch.html): The following table lists ARC operations that you can use for Region switch, with links to relevant documentation.

### [Working with Region switch](https://docs.aws.amazon.com/r53recovery/latest/dg/working-with-rs.html)

This section provides step-by-step instructions for working with Region switch plans, which you can use to recover multi-Region applications.

- [Create a plan](https://docs.aws.amazon.com/r53recovery/latest/dg/working-with-rs-create-plan.html): You can create two different kinds of plans in Region switch: an active/active plan or an active/passive plan.
- [Create workflows](https://docs.aws.amazon.com/r53recovery/latest/dg/working-with-rs-workflows.html): After you create a Region switch plan, you need to define and create workflows that specify the recovery process for your application.

### [Add execution blocks](https://docs.aws.amazon.com/r53recovery/latest/dg/working-with-rs-execution-blocks.html)

You add steps to workflows in your Region switch plan, to perform the individual steps to complete failover or switchover for your application.

- [Region switch plan execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch-plan-block.html): The Region switch plan execution block allows you to orchestrate the order in which multiple applications switch over to the Region that you want to activate, by referencing other, child Region switch plans.
- [EC2 Auto Scaling group execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/ec2-auto-scaling-block.html): The EC2 Auto Scaling group execution block allows you to scale EC2 instances as part of your multi-Region recovery process.
- [EKS resource scaling execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/eks-resource-scaling-block.html): The EKS resource scaling execution block enables you to scale EKS resources as part of your multi-Region recovery process.
- [ECS service scaling execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/ecs-service-scaling-block.html): The ECS service scaling execution block allows you to scale your ECS service in a destination Region as part of your multi-Region recovery process.
- [ARC routing control execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-routing-controls-block.html): If you've configured Amazon Application Recovery Controller (ARC) routing control for your application, you can add a ARC routing control step to redirect application traffic.
- [Aurora Global Database execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/aurora-global-database-block.html): The Amazon Aurora Global Database execution block allows you to perform a failover or switchover recovery workflow for a global database.
- [Amazon DocumentDB Global Cluster execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/documentdb-global-cluster-block.html): The Amazon DocumentDB Global Cluster execution block allows you to perform a failover or switchover recovery workflow for a global cluster.
- [Amazon RDS Promote Read Replica execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/rds-promote-read-replica-block.html): The Amazon RDS Promote Read Replica execution block allows you to promote an Amazon RDS read replica to a standalone database instance as part of your multi-Region recovery process.
- [Amazon RDS Create Cross-Region Replica execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/rds-create-cross-region-replica-block.html): The Amazon RDS Create Cross-Region Replica execution block allows you to create a cross-Region read replica for an Amazon RDS database instance as part of your post-recovery process.
- [Manual approval execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/manual-approval-block.html): The manual approval execution block enables you to insert an approval step that you associate with an IAM role.
- [Custom action Lambda execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/custom-action-lambda-block.html): The custom action Lambda execution block enables you to add a customized step to a plan by using a Lambda function.
- [Amazon RouteÂ 53 health check execution block](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-health-check-block.html): The Amazon RouteÂ 53 health check execution block enables you to specify the Regions that your application's traffic will be redirected to during failover.
- [Create child plans](https://docs.aws.amazon.com/r53recovery/latest/dg/working-with-rs-child-plan.html): To support more complex recovery scenarios, you can create child plans by adding them with Region switch plan execution blocks.
- [Create triggers](https://docs.aws.amazon.com/r53recovery/latest/dg/working-with-rs-triggers.html): If you want to automate recovery for your application in Region switch, you can create one or more triggers for your Region switch plan.
- [Execute a plan](https://docs.aws.amazon.com/r53recovery/latest/dg/plan-execution-rs.html): To recover an application when an AWS Region is impaired, you execute a Region switch plan in Amazon Application Recovery Controller (ARC).
- [Dashboards](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.dashboarding-and-reports.html): Region switch includes a global dashboard that you can use to observe the state of Region switch plans across your organization and Regions.

### [Cross-account support](https://docs.aws.amazon.com/r53recovery/latest/dg/cross-account-resources-rs.html)

In Region switch, you can add resources from other accounts to your plans.

- [Support sharing plans across accounts](https://docs.aws.amazon.com/r53recovery/latest/dg/resource-sharing.region-switch.html): Amazon Application Recovery Controller (ARC) integrates with AWS Resource Access Manager to enable resource sharing.

### [Identity and Access Management](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-region-switch.html)

Learn how to authenticate requests and manage access to your ARC resources.

- [How Region switch works with IAM](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_service-with-iam-region-switch.html): Before you use IAM to manage access to ARC, learn what IAM features are available to use with ARC.

### [Identity-based policy examples](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_id-based-policy-examples-region-switch.html)

By default, users and roles don't have permission to create or modify ARC resources.

- [Plan execution role trust policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_trust_policy.html): This is the trust policy required for the plan's execution role, so that ARC can run a Region switch plan.
- [Full access permissions](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_full_access.html): The following IAM policy grants full access for all Region switch APIs:
- [Read-only permissions](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_read_only.html): The following IAM policy grants read-only access permissions for Region switch:

### [Execution block permissions](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_execution_blocks.html)

The following sections provide sample IAM policies that provide the required permissions for specific execution blocks that you add to a Region switch plan.

- [EC2 Auto Scaling execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_ec2_autoscaling.html): The following is a sample policy to attach if you add execution blocks to a Region switch plan for EC2 Auto Scaling groups.
- [Amazon EKS resource scaling execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_eks.html): The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon EKS resource scaling.
- [Amazon ECS service scaling execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_ecs.html): The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon ECS service scaling.
- [ARC routing controls execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_arc_routing.html): Note: The Amazon ARC routing controls execution block requires that any service control policies (SCPs) applied to the plan's execution role allow the access to the following Regions for these services:
- [Aurora Global Database execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_aurora.html): The following is a sample policy to attach if you add execution blocks to a Region switch plan for Aurora databases.
- [Amazon DocumentDB Global Cluster execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_documentdb.html): The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon DocumentDB global clusters.
- [Amazon RDS execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_rds.html): The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon RDS read replica promotion or cross-Region replica creation.
- [Manual approval execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_manual_approval.html): The following is a sample policy to attach if you add execution blocks to a Region switch plan for manual approvals.
- [Custom action Lambda execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_lambda.html): The following is a sample policy to attach if you add execution blocks to a Region switch plan for Lambda functions.
- [RouteÂ 53 health check execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_route53.html): The following is a sample policy to attach if you add execution blocks to a Region switch plan for RouteÂ 53 health checks.
- [Region switch plan execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_plan_execution.html): The following is a sample policy to attach if you add execution blocks to a Region switch plan to run child plans.
- [CloudWatch alarms for application health permissions](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_cloudwatch.html): The following is a sample policy to attach to access CloudWatch alarms for application health, which are used to help determine actual recovery time.
- [Automatic plan execution reports permissions](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_reports.html): The following is a sample policy to attach if you configure automatic report generation for a Region switch plan.
- [Cross-account resource permissions](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_cross_account.html): If resources are in different accounts, you'll need a cross-account role.
- [Complete plan execution role permissions](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_complete_policy.html): Creating a comprehensive policy that includes permissions for all execution blocks would require a policy that is quite large.

### [Logging and monitoring](https://docs.aws.amazon.com/r53recovery/latest/dg/logging-and-monitoring-rs.html)

Use Amazon CloudWatch, AWS CloudTrail, and Amazon EventBridge for monitoring for readiness check in Amazon Application Recovery Controller (ARC).

- [CloudTrail logs](https://docs.aws.amazon.com/r53recovery/latest/dg/cloudtrail-region-switch.html): Learn about logging Region switch with AWS CloudTrail.
- [EventBridge](https://docs.aws.amazon.com/r53recovery/latest/dg/eventbridge-region-switch.html): Learn about monitoring Region switch in ARC with Amazon EventBridge.
- [Quotas](https://docs.aws.amazon.com/r53recovery/latest/dg/quotas.region-switch.html): Region switch in Amazon Application Recovery Controller (ARC) is subject to the following quotas.


## [Code examples](https://docs.aws.amazon.com/r53recovery/latest/dg/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/r53recovery/latest/dg/service_code_examples_basics.html)

The following code examples show how to use the basics of Application Recovery Controller with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/r53recovery/latest/dg/service_code_examples_actions.html)

The following code examples show how to use Application Recovery Controller with AWS SDKs.

- [GetRoutingControlState](https://docs.aws.amazon.com/r53recovery/latest/dg/example_route53-recovery-cluster_GetRoutingControlState_section.html): Use GetRoutingControlState with an AWS SDK
- [UpdateRoutingControlState](https://docs.aws.amazon.com/r53recovery/latest/dg/example_route53-recovery-cluster_UpdateRoutingControlState_section.html): Use UpdateRoutingControlState with an AWS SDK


## [Security](https://docs.aws.amazon.com/r53recovery/latest/dg/security.html)

- [Data protection](https://docs.aws.amazon.com/r53recovery/latest/dg/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in ARC.

### [Identity and Access Management](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam.html)

Learn how to authenticate requests and manage access to your Amazon Application Recovery Controller (ARC) resources.

- [How Amazon Application Recovery Controller (ARC) capabilities work with IAM](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_service-with-iam.html): For information about how each Amazon Application Recovery Controller (ARC) capability works with IAM, see the following topics:
- [Identity-based policy examples](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_id-based-policy-examples.html): To see identity-based policy examples for each capability in Amazon Application Recovery Controller (ARC), see the following topics in the AWS Identity and Access Management chapters for each capability:
- [AWS managed policies](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for ARC and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_troubleshoot.html): Learn how to troubleshoot IAM issues.
- [AWS PrivateLink](https://docs.aws.amazon.com/r53recovery/latest/dg/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and Amazon Application Recovery Controller (ARC) zonal shift.
- [Logging and monitoring](https://docs.aws.amazon.com/r53recovery/latest/dg/logging-and-monitoring.html): Learn how AWS supports you in maintaining availability and performance in ARC by providing tools for logging and monitoring ARC activity.
- [Compliance validation](https://docs.aws.amazon.com/r53recovery/latest/dg/r53-recovery-controller-compliance.html): Learn the AWS services that are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/r53recovery/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Application Recovery Controller features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/r53recovery/latest/dg/infrastructure-security.html): Learn how Amazon Application Recovery Controller isolates service traffic.
