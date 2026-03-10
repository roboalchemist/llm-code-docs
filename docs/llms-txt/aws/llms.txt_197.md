# Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/llms.txt

# CloudFormation Hooks User Guide

> Use CloudFormation Hooks to provide code that proactively inspects the configuration of your AWS resources before provisioning. If non-compliant resources are found, CloudFormation either fails the operation and prevents the resources from being provisioned, or emits a warning and allows the provisioning operation to continue.

- [What are CloudFormation Hooks?](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html)
- [Disable-enable Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-disable-enable.html)
- [View Hook invocation results](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-view-invocations.html)
- [Create Hooks using CloudFormation templates](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/creating-hooks-with-cloudformation.html)
- [Document history](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/doc-history.html)

## [Creating and managing Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/creating-and-managing-hooks.html)

- [Concepts](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-concepts.html): Describes the fundamentals, concepts, and terminology you need to know for working with CloudFormation Hooks.

### [Proactive controls as Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/proactive-controls-hooks.html)

Discover and use AWS Control Tower-supplied proactive controls as Hooks.

- [Activate a proactive control-based Hook](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/proactive-controls-hooks-activate-hooks.html): Learn how to activate a proactive control-based Hook so it's available for use in your account.
- [Delete proactive control-based Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/proactive-controls-hooks-delete-hooks.html): Discover how to delete a proactive control-based Hook you previously activated in your account.

### [Guard Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks.html)

Discover and use Guard policy-as-code rules as Hooks.

- [Write Guard rules for Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-write-rules.html): Provides guidance for creating Guard rules for Guard Hooks.
- [Prepare to create a Guard Hook](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-prepare-to-create-hook.html): Describes the prerequisites for creating a Guard Hook, such as required Hook execution role and trust policy.
- [Activate a Guard Hook](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-activate-hooks.html): Learn how to activate a Guard Hook so it's available for use in your account.
- [View logs for Guard Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-view-logs.html): Discover how to view logs for a Guard Hook you activated in your account.
- [Delete Guard Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-delete-hooks.html): Discover how to delete a Guard Hook you previously activated in your account.

### [Lambda Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks.html)

Discover and use Lambda functions as Hooks.

- [Create Lambda functions for Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-create-lambda-function.html): Provides guidance on creating Lambda functions for Lambda Hooks.
- [Prepare to create a Lambda Hook](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-prepare-to-create-hook.html): Describes the prerequisites for creating a Lambda Hook, such as required Hook execution role and trust policy.
- [Activate a Lambda Hook](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-activate-hooks.html): Learn how to activate a Lambda Hook so it's available for use in your account.
- [View logs for Lambda Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-view-logs.html): Discover how to view logs for a Lambda Hook you activated in your account.
- [Delete Lambda Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-delete-hooks.html): Discover how to delete a Lambda Hook you previously activated in your account.

### [Custom Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-develop.html)

Learn to initiate, model, and register your own CloudFormation Hooks with Python or Java.

- [Prerequisites](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-prerequisites.html): A list of prerequisites for developing CloudFormation Hooks with Java or Python.
- [Initiating a Hooks project](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-init.html): Learn how to initiate a CloudFormation Hooks project for Python or Java so that you can develop your own custom Hooks.

### [Modeling Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-model.html)

Learn how to model custom CloudFormation Hooks so that you can ensure that your AWS resources are compliant with your standards and policies when they are provisioned.

- [Using Java](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-model-java.html): Learn how to model a custom Hook using Java so that you can ensure that your AWS resources are compliant with your standards and policies when they are provisioned.
- [Using Python](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-model-python.html): Learn how to model a custom Hook using Python so that you can ensure that your AWS resources are compliant with your standards and policies when they are provisioned.
- [Registering Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/registering-hooks.html): Learn how to package and register a custom Hook so that you can use it in your AWS account.
- [Testing Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/testing-hooks.html): Learn how to test your custom Hook by provisioning a CloudFormation stack.
- [Updating Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/updating-registered-hook.html): Learn how to update a custom Hook and allow revisions in the Hook to be made available in the CloudFormation registry.
- [Deregistering Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/deregistering-hooks.html): Learn how to deregister a custom Hook to mark the extension or extension version as DEPRECATED.

### [Publishing Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-publishing.html)

Learn how to publish a Hook so it can be used by anyone.

- [Testing Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-testing-registered-hooks.html): Learn how to test public CloudFormation Hooks.
- [Specifying input](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-input-data-contract-test.html): Learn how to specify input for a contract test of CloudFormation Hooks.
- [Schema syntax](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-schema.html): Describes the syntax of the schema that you use to develop CloudFormation Hooks.


## [Configuration schema](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.html)

- [Stack level filters](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-stack-level-filtering.html): Learn more about CloudFormation Hooks stack level filters that you can use to create Hook that targets specific stacks.
- [Target filters](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-target-filtering.html): Learn about specifying target names, action, and invocation points for Hook targets.
- [Using wildcards](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/wildcard-hook-targets.html): Learn about using wildcards in Hook target names.


## [Grant IAM permissions](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/grant-iam-permissions-for-hooks.html)

- [AWS KMS key policy and permissions](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-kms-key-policy.html): Learn about the AWS KMS key policy and permissions required to encrypt annotations data with your customer managed key.
