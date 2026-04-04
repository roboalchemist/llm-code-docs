# Source: https://docs.aws.amazon.com/amazonswf/latest/developerguide/llms.txt

# Amazon Simple Workflow Service Developer Guide

> Build applications that coordinate work across distributed components with Amazon SWF.

- [What is Amazon SWF?](https://docs.aws.amazon.com/amazonswf/latest/developerguide/welcome.html)
- [Workflow components](https://docs.aws.amazon.com/amazonswf/latest/developerguide/intro.html)
- [Working in the console](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-using-console.html)
- [Using the AWS CLI](https://docs.aws.amazon.com/amazonswf/latest/developerguide/using-cli.html)
- [Quotas](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-limits.html)
- [Document history](https://docs.aws.amazon.com/amazonswf/latest/developerguide/WhatsNew.html)

## [Getting started](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-sns-tutorial.html)

- [Part 1: Using Amazon SWF with the SDK for Ruby](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-sns-tutorial-setup-swf.html): Walks through how to use Amazon SWF with the AWS SDK for Ruby.
- [Part 2: Implementing the Workflow](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-sns-tutorial-implementing-workflow.html): Walks through how to define what our workflow does, and what activities we'll need to implement it.
- [Part 3: Implementing the Activities](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-sns-tutorial-implementing-activities.html): Walks through how to implement each of the activities in our workflow.
- [Part 4: Implementing the Activities Task Poller](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-sns-tutorial-implementing-activities-poller.html): Walks through how to implement a basic activity poller to handle these tasks for our workflow, and use it to launch our activities.
- [Running the Workflow](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-sns-tutorial-running-the-workflow.html): Walks through how to run the workflow in Amazon SWF.


## [Basic concepts](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-basic.html)

- [Creating a workflow](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-create-workflow.html): Create a basic sequential workflow by modeling a workflow, and then developing and launching activity workers, deciders, and workflow starters.
- [Running workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-run-workflows.html): Implement distributed, asynchronous applications as workflows to coordinate and manage execution of activities using Amazon SWF.
- [Workflow history](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-about-workflow-history.html): Provides a detailed, complete, and consistent record of every event that occurred since the workflow execution started.
- [Object identifiers](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-obj-ident.html): Lists the how Amazon SWF object identifiers, such as workflow executions, and how they are uniquely identified.
- [Domains](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-domains.html): Scope Amazon SWF resources within your AWS account using domains.
- [Actors](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-actors.html): Interact with a number of different types of programmatic actors which can be workflow starters, deciders, or activity workers using Amazon SWF.
- [Tasks](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-tasks.html): Interact with activity workers and deciders by providing them with work assignments known as tasks with Amazon SWF.
- [Task lists](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-task-lists.html): Organize the various tasks associated with a workflow using the Amazon SWF task lists.
- [Workflow execution closure](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-workflow-exec-closure.html): Close an open workflow execution as completed, canceled, failed, or timed out.
- [Workflow execution life cycle](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-workflow-exec-lifecycle.html): Describes the life cycle of an Amazon SWF workflow execution.
- [Polling for tasks](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-comm-proto.html): Describes long polling for tasks, which is how deciders and activity workers communicate with Amazon SWF.


## [Advanced concepts](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-adv.html)

- [Versioning](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-adv-versioning.html): Business needs often require you to have different implementations or variations of the same workflow or activity running simultaneously.
- [Signals](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-adv-signals.html): Signals enable you to inject information into a running workflow execution.
- [Child workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-adv-child-workflows.html): Complicated workflows can be broken into smaller, more manageable, and potentially reusable components by using child workflows.
- [Markers](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-adv-markers.html): At times, you might want to record information in the workflow history of a workflow execution that is specific to your use case.
- [Tags](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-adv-tags.html): Amazon SWF supports tagging a workflow execution.
- [Exclusive choice](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-exclusive-choice.html): Learn about implementing exclusive choice with Amazon SWF.
- [Timers](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-timers.html): Learn about Amazon SWF timers.
- [Cancelling activity tasks](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-task-cancellation.html): Learn about Amazon SWF activity task cancellation.


## [Security](https://docs.aws.amazon.com/amazonswf/latest/developerguide/security.html)

### [Data Protection](https://docs.aws.amazon.com/amazonswf/latest/developerguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Simple Workflow Service.

- [Encryption](https://docs.aws.amazon.com/amazonswf/latest/developerguide/security-encryption.html)

### [Identity and Access Management](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html)

Describes how to write a policy and the logic AWS uses to evaluate policies and decide whether to grant the requester access to the resource.

- [How Amazon Simple Workflow Service works with IAM](https://docs.aws.amazon.com/amazonswf/latest/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon SWF, learn what IAM features are available to use with Amazon SWF.
- [Identity-based policy examples](https://docs.aws.amazon.com/amazonswf/latest/developerguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon SWF resources.
- [Basic Principles](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.basic.html): Amazon SWF access control is based primarily on two types of permissions:
- [Amazon SWF IAM Policies](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.policies.html): Describes about IAM policies for Amazon SWF and contains example policies.
- [API Summary](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.api.html): Learn about how you can use IAM policies to control how an actor can use each API and pseudo APIs to access Amazon SWF resources.
- [Tag-based Policies](https://docs.aws.amazon.com/amazonswf/latest/developerguide/tag-based-policies.html): Contains examples of tag-based IAM policies for accessing Amazon SWF resources.

### [Amazon VPC endpoints](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-vpc-endpoints.html)

Access Amazon Simple Workflow Service directly from Amazon Virtual Private Cloud.

- [Endpoint Policies](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-vpc-iam.html): You can create an Amazon VPC endpoint policy for Amazon SWF in which you specify the following:
- [Troubleshooting](https://docs.aws.amazon.com/amazonswf/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon SWF and IAM.

### [Logging and Monitoring](https://docs.aws.amazon.com/amazonswf/latest/developerguide/logging-monitoring.html)

Learn about logging and monitoring in Amazon SWF.

- [Amazon SWF Metrics for CloudWatch](https://docs.aws.amazon.com/amazonswf/latest/developerguide/cw-metrics.html): Find out how to view Amazon SWF metrics for CloudWatch using the AWS Management Console.
- [Viewing Amazon SWF Metrics](https://docs.aws.amazon.com/amazonswf/latest/developerguide/cw-metrics-console.html): Find out how to view CloudWatch metrics and set CloudWatch alarms for Amazon SWF using the AWS Management Console.
- [Recording to CloudTrail](https://docs.aws.amazon.com/amazonswf/latest/developerguide/ct-logging.html): Learn about logging Amazon Simple Workflow Service with AWS CloudTrail.
- [EventBridge for Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/ev-events.html): Learn how to use Amazon EventBridge (EventBridge) for Amazon Simple Workflow Service execution changes.
- [Using AWS User Notifications with Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/using-user-notifications-swf.html): Learn how to get notifications for Amazon Simple Workflow Service.
- [Compliance Validation](https://docs.aws.amazon.com/amazonswf/latest/developerguide/SWF-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/amazonswf/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Simple Workflow Service features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/amazonswf/latest/developerguide/infrastructure-security.html): Learn how the AWS shared responsibility model applies to data protection in Amazon Simple Workflow Service.
- [Configuration and Vulnerability Analysis](https://docs.aws.amazon.com/amazonswf/latest/developerguide/configuration-vulnerability.html): Learn about Amazon Simple Workflow Service configuration and vulnerability analysis.


## [Working with APIs](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-using-swf-api.html)

### [Making HTTP Requests](https://docs.aws.amazon.com/amazonswf/latest/developerguide/UsingJSON-swf.html)

Make HTTP requests to Amazon SWF using the POST request method.

- [Calculating the HMAC-SHA Signature](https://docs.aws.amazon.com/amazonswf/latest/developerguide/HMACAuth-swf.html): Learn about calculating the HMAC-SHA signature for Amazon SWF authentication requests.
- [List of Amazon SWF Actions](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-api-by-category.html): Lists the reference topics for Amazon SWF actions in the Amazon SWF application programming interface (API).
- [Registering a Domain](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-register-domain-api.html): Walks through how to register a domain by using the AWS Management Console or by using the Amazon SWF API.
- [Setting timeout values](https://docs.aws.amazon.com/amazonswf/latest/developerguide/setting-timeouts.html): Walks through how to set timeout values in Amazon SWF.
- [Registering a Workflow Type](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-register-workflow.html): Walks through how to register a workflow type by using the Amazon SWF API.
- [Registering an Activity Type](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-register-activity.html): Walks through how to register an activity type by using the Amazon SWF API.
- [Lambda tasks](https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html): Describes the Lambda task type for the Amazon Simple Workflow Service
- [Developing an Activity Worker](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-develop-activity.html): Develop an activity worker that provides the implementation of one or more activity types in Amazon SWF.
- [Developing deciders](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-dev-deciders.html): Develop deciders which are implementations of the coordination logic of your workflow type that runs during the execution of your workflow.
- [Starting workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-start-workflow-exec.html): Walks through how to start workflow executions with Amazon SWF.
- [Setting task priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html): Learn about setting task priority.
- [Handling errors](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-error-handling.html): Troubleshoot errors for a number of different types of errors that can occur during the course of a workflow execution.


## [Additional resources](https://docs.aws.amazon.com/amazonswf/latest/developerguide/resources.html)

- [Timeout Types](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-timeout-types.html): Learn about Amazon SWF timeout types.
