# Source: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/llms.txt

# Extension development for CloudFormation CloudFormation Command Line Interface (CLI) User Guide

> The CloudFormation CLI (CFN-CLI) is an open-source tool for developing and testing AWS and third-party extensions, such as resource types and modules, and registering them for use in CloudFormation.

- [What is the CloudFormation Command Line Interface (CFN-CLI)?](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)
- [Hooks User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-ug-link.html)
- [Updating Lambda runtimes for resource types and hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/runtime-update.html)
- [Registering extensions](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-register.html)
- [Document history](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/glossary.html)

## [Creating resource types](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html)

### [Modeling resource types](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html)

Use the Resource type definition schema to define the resource, its properties and attributes, to use with CloudFormation.

- [Resource type schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html): Provides the structure of a typical resource type schema.
- [Patterns for modeling resources](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-howtos.html): Provides example patterns on specifying a property as a dependent, defining nested properties, and encapsulating complex logic.
- [Preventing false drift results](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model-false-drift.html): Use property transforms to prevent resources from being incorrectly reported as drifted.

### [Developing resource types](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-develop.html)

Develop your resource type by implementing the desired event handlers for your resource, and then testing the resource locally to ensure it works as expected.

### [Testing resource types](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html)

Describes how CloudFormation CLI performs contract tests to enforce the CloudFormation resource type handler contract.

- [Resource type handler contract](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-contract.html): Describes the resource type handler contract, which specifies the the expected and required behavior to which a resource must adhere in each given event handler.
- [Contract tests](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/contract-tests.html): Describes the contact tests that test the requirements contained in the resource type handler contract.
- [Handler error codes](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-contract-errors.html): Describes the potential error codes returned from a handler whenever there is a progress event with an operation status of FAILED.
- [ProgressEvent object schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-progressevent.html): Describes the ProgressEvent JSON object, which represents the current operation status of the handler, state of the resource, and other additional resource info.
- [Progress chaining, stabilization, and callback pattern](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-develop-stabilize.html): Describes the CloudFormation framework used to chain patterns, as well as handle error conditions and throttle when calling downstream API.
- [Walkthrough: Develop a resource type](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-walkthrough.html): Describes how to create a resource type, model the schema, and develop and test the handlers.
- [Resource type troubleshooting](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-troubleshooting.html): View the troubleshooting scenarios about resource type development.


## [Developing modules](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules.html)

- [Module structure](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules-structure.html): Describes the main components of modules, requirements, creating module template fragments, and generating the module schema.
- [Develop a module](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules-develop.html): Provides a procedure for developing and registering a module project.


## [Publishing extensions](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html)

- [Publishing extensions in multiple Regions using StackSets](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension-stacksets.html): Describes how to publish extensions to the public registry in all Regions using CloudFormation StackSets.


## [CloudFormation CLI reference](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli.html)

- [Global parameters](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-global-parameters.html): The following parameters can be used with any CloudFormation CLI command.
- [init](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-init.html)
- [generate](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-generate.html)
- [validate](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-validate.html)
- [invoke](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-invoke.html)
- [test](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-test.html)
- [submit](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html)
