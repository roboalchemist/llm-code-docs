# Source: https://docs.aws.amazon.com/lambda/latest/dg/llms.txt

# AWS Lambda Developer Guide

> Lambda is a compute service that lets you run code without provisioning or managing servers.

- [Create your first function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
- [Best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [Testing serverless functions](https://docs.aws.amazon.com/lambda/latest/dg/testing-guide.html)
- [Sample applications](https://docs.aws.amazon.com/lambda/latest/dg/lambda-samples.html)
- [Working with AWS SDKs](https://docs.aws.amazon.com/lambda/latest/dg/sdk-general-information-section.html)
- [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- [Document history](https://docs.aws.amazon.com/lambda/latest/dg/lambda-releases.html)

## [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

### [How it works](https://docs.aws.amazon.com/lambda/latest/dg/concepts-basics.html)

Learn about basic Lambda concepts such as functions, execution environments, deployment packages, layers, runtimes, extensions, events, and concurrency.

### [Running code](https://docs.aws.amazon.com/lambda/latest/dg/concepts-how-lambda-runs-code.html)

Learn how Lambda runs your function code using a programming model that is common to all supported runtimes and an execution environment.

- [Programming model](https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html): Learn how Lambda runs your function code using a programming model that is common to all supported runtimes.
- [Execution environment](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html): Lambda invokes your function in an execution environment, which provides a secure and isolated runtime environment.
- [Creating event-driven architectures](https://docs.aws.amazon.com/lambda/latest/dg/concepts-event-driven-architectures.html): Understand how events drive serverless applications, which informs the design of your workload and how Lambda fits into this paradigm.
- [Designing an application](https://docs.aws.amazon.com/lambda/latest/dg/concepts-application-design.html): Understand criteria for a well-architected event-driven serverless application and how Lambda fits in.


## [Example apps and patterns](https://docs.aws.amazon.com/lambda/latest/dg/example-apps.html)

- [File-processing app](https://docs.aws.amazon.com/lambda/latest/dg/file-processing-app.html): One of the most common use cases for Lambda is to perform file processing tasks.
- [Scheduled-maintenance app](https://docs.aws.amazon.com/lambda/latest/dg/scheduled-task-app.html): You can use AWS Lambda to replace scheduled processes such as automated system backups, file conversions, and maintenance tasks.
- [Creating an Order Processing System with Lambda Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/order-processing-app.html): Create a serverless application that processes orders through multiple stages while maintaining state between steps.


## [Development tools](https://docs.aws.amazon.com/lambda/latest/dg/tools-to-develop-deploy-manage.html)

- [Local development](https://docs.aws.amazon.com/lambda/latest/dg/foundation-iac-local-development.html): Develop Lambda functions locally using Visual Studio Code
- [GitHub Actions](https://docs.aws.amazon.com/lambda/latest/dg/deploying-github-actions.html): Deploy Lambda functions using GitHub Actions.

### [Infrastructure as code (IaC)](https://docs.aws.amazon.com/lambda/latest/dg/foundation-iac.html)

Deploy and update Lambda functions using AWS IaC tools

- [Using AWS SAM and Infrastructure Composer](https://docs.aws.amazon.com/lambda/latest/dg/foundation-iac-getting-started.html): In this tutorial, you can get started using IaC with Lambda by creating an AWS SAM template from an existing Lambda function and then building out a serverless application in Infrastructure Composer by adding other AWS resources.
- [Using AWS CDK](https://docs.aws.amazon.com/lambda/latest/dg/lambda-cdk-tutorial.html): Learn how to deploy a Lambda function using the AWS Cloud Development Kit (AWS CDK).
- [Powertools for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/powertools-for-lambda.html): Using Powertools for AWS Lambda to implement serverless best practices
- [Workflows and events](https://docs.aws.amazon.com/lambda/latest/dg/workflow-event-management.html): Tools for orchestrating workflows and managing events in Lambda applications


## [Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)

- [Basic concepts](https://docs.aws.amazon.com/lambda/latest/dg/durable-basic-concepts.html): Understand the fundamental concepts that enable long-running workflows: DurableContext, steps, and wait states with practical examples.

### [Creating durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-getting-started.html)

Get started with Lambda durable functions by creating and testing your first durable function in the console.

- [Deploy with CLI](https://docs.aws.amazon.com/lambda/latest/dg/durable-getting-started-cli.html): Create, deploy, and invoke durable functions using AWS CLI commands.
- [Using Infrastructure as Code](https://docs.aws.amazon.com/lambda/latest/dg/durable-getting-started-iac.html): Deploy durable functions using AWS CloudFormation, AWS CDK, AWS Serverless Application Model, or Terraform templates.
- [Durable functions or Step Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-step-functions.html): Compare Lambda durable functions and Step Functions to choose the right approach for your workflow orchestration needs.
- [Examples](https://docs.aws.amazon.com/lambda/latest/dg/durable-examples.html): Explore practical examples of durable functions including distributed transactions, long-running workflows, and complex orchestration patterns.
- [Security and permissions](https://docs.aws.amazon.com/lambda/latest/dg/durable-security.html): Configure IAM permissions for durable functions and understand security features including state encryption and CloudTrail logging.

### [Durable execution SDK](https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-sdk.html)

Understand the durable execution SDK, how it manages checkpoints and replay, and the operations available through DurableContext.

- [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/durable-supported-runtimes.html): Understand which Lambda runtimes support durable functions and how to use durable functions with container images.

### [Invoking durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-invoking.html)

Invoke durable Lambda functions using the same methods as standard functions, with support for synchronous, asynchronous, and event source mapping invocations.

- [Event source mappings](https://docs.aws.amazon.com/lambda/latest/dg/durable-invoking-esm.html): Configure event source mappings to automatically invoke durable functions from streams and queues, with important considerations for execution duration limits.
- [Retries](https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-sdk-retries.html): Configure retry strategies for durable functions to handle transient failures and build resilient applications with automatic recovery.
- [Idempotency](https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-idempotency.html): Understand how durable functions handle idempotent execution starts through execution names and how to implement idempotency in your business logic.
- [Testing durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-testing.html): Test durable functions locally and in the cloud using dedicated testing SDKs that provide test runners, execution inspection, and assertion capabilities.
- [Monitoring durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-monitoring.html): Monitor durable functions using CloudWatch metrics, CloudWatch Logs, and tracing to track execution progress, state transitions, and performance.
- [Best practices](https://docs.aws.amazon.com/lambda/latest/dg/durable-best-practices.html): Learn best practices for building reliable, maintainable durable functions including deterministic code, idempotency, state management, and performance optimization.


## [Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html)

- [Getting started](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-getting-started.html): Create your first Lambda Managed Instance function using the console or AWS CLI.

### [Core concepts](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-core-concepts.html)

Understand the fundamental concepts of Lambda Managed Instances including capacity providers, scaling, security, and permissions.

- [Capacity providers](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-capacity-providers.html): A capacity provider defines the compute capacity where your Lambda functions run when using Lambda Managed Instances.
- [Scaling](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-scaling.html): Lambda Managed Instances scales differently from Lambda (default) compute type to optimize for steady-state workloads while maintaining high availability and resource utilization.
- [Security](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-security.html): When using Lambda Managed Instances, you need operator role permissions to manage EC2 resources in your capacity providers.
- [Operator role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-operator-role.html): An operator role is an AWS Identity and Access Management (IAM) role that grants permissions to manage Lambda Managed Instances capacity providers in your account.
- [Execution environment](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-execution-environment.html): Lambda Managed Instances provide an alternative deployment model that runs your function code on customer-owned Amazon EC2 instances while Lambda manages the operational aspects.
- [Version publishing](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-version-publishing.html): The $LATEST.PUBLISHED version is a version type for Lambda Managed Instances functions that allows you to create or republish a latest published version without maintaining numbered versions.

### [Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-runtimes.html)

Lambda processes requests differently when using Lambda Managed Instances, with multi-concurrent execution requiring runtime-specific considerations for thread safety and state management.

- [Java runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-java-runtime.html): For Java runtimes, Lambda Managed Instances use OS threads for concurrency, requiring thread-safe handling of state and shared resources.
- [Node.js runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-nodejs-runtime.html): For Node.js runtimes, Lambda Managed Instances uses worker threads with async/await-based execution to handle concurrent requests.
- [Python runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-python-runtime.html): The Lambda runtime uses multiple Python processes to handle concurrent requests, with each concurrent request running in a separate process with its own memory space and initialization.
- [.NET runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-dotnet-runtime.html): For .NET runtimes, Lambda Managed Instances use a single .NET process per execution environment with multiple concurrent requests processed using .NET Tasks.
- [Networking](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-networking.html): Configure network connectivity to enable your Lambda Managed Instances functions to access resources outside the VPC.
- [Monitoring](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-monitoring.html): Monitor Lambda Managed Instances using CloudWatch metrics to track resource utilization, costs, and performance.
- [Quotas](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-quotas.html): Service quotas for AWS Lambda Managed Instances, separate from AWS Lambda (default) quotas.
- [Best practices](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-best-practices.html): Recommendations for optimizing Lambda Managed Instances for performance, cost, security, and reliability.
- [Troubleshooting](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-troubleshooting.html): Common issues you might encounter when using Lambda Managed Instances and solutions to resolve them.


## [Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)

### [Runtime version updates](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html)

Learn how Lambda updates the runtime version of your function, and how you can configure these updates.

- [Configuring runtime management](https://docs.aws.amazon.com/lambda/latest/dg/runtime-management-configure-settings.html): Learn how to configure Lambda runtime management settings.
- [Runtime version roll-back](https://docs.aws.amazon.com/lambda/latest/dg/runtime-management-rollback.html): Learn how to roll back to a previous version of a Lambda runtime.
- [Runtime version updates](https://docs.aws.amazon.com/lambda/latest/dg/runtime-management-identify.html): Learn how to identify which Lambda runtime version a function is using.
- [Shared responsibility model](https://docs.aws.amazon.com/lambda/latest/dg/runtime-management-shared.html): Learn about the shared responsibility model for Lambda runtime version updates.
- [Permissions](https://docs.aws.amazon.com/lambda/latest/dg/runtime-management-hc-applications.html): Learn about the permissions required for for Lambda runtime version updates.
- [Get data about functions by runtime](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-list-deprecated.html): Learn how to gather data about functions that use a particular runtime.
- [Runtime modifications](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-modify.html): Learn how to use internal extensions to modify the runtime process and wrapper scripts to customize the runtime startup behavior.
- [Runtime API](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html): Learn how to use the Lambda Runtime API when working with custom runtimes.

### [OS-only runtimes](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-provided.html)

Lambda provides managed runtimes for Java, Python, Node.js, .NET, and Ruby.

- [Building a custom runtime](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html): You can implement an AWS Lambda runtime in any programming language.
- [Custom runtime tutorial](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-walkthrough.html): In this tutorial, you create a Lambda function with a custom runtime.
- [Open source repositories](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-open-source.html): Learn about AWS Lambda's open source tools, libraries, and components for building serverless applications.


## [Configuring functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-functions.html)

### [.zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-zip.html)

Learn how to use the Lambda console and the Lambda API to create and configure a function defined with a .zip file archive.

- [Encryption](https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html): Learn how to encrypt .zip deployment packages.
- [Container images](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html): Create a container image for a Lambda function by using an AWS provided base image or an alternative base image.
- [Memory](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html): Configure memory for a Lambda function.
- [Ephemeral storage](https://docs.aws.amazon.com/lambda/latest/dg/configuration-ephemeral-storage.html): Configure the ephemeral storage for your Lambda function.
- [Instruction sets (ARM/x86)](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html): Learn how to select and configure an ARM64 or x86 instruction set architecture for your Lambda function.
- [Timeout](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html): Configure the timeout setting for your Lambda function.
- [Configure durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-configuration.html): Configure execution timeout, retention period, and other settings for durable functions.

### [Environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html)

Learn how to use environment variables in Lambda.

- [Securing environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars-encryption.html): Learn how to use environment variables in Lambda.
- [Attaching functions to a VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html): Learn how to configure a Lambda function to access resources in an Amazon VPC.
- [Attaching functions to resources in another account](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-cross-account.html): Learn how to configure a Lambda function to access a resource in an Amazon VPC in another account.
- [Internet access for VPC functions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-internet.html): Learn how to configure a Lambda function to access the public internet from a private subnet.
- [Inbound networking](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Lambda without requiring access over the internet or through a NAT device, VPN connection, or Direct Connect connection.
- [File system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html): Configure your Lambda function to access a file system such as an Amazon EFS file system.

### [Aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html)

Create a Lambda function alias to use as a pointer to a specific function version.

- [Using aliases](https://docs.aws.amazon.com/lambda/latest/dg/using-aliases.html): You can configure an event source mapping to use a Lambda function alias.
- [Weighted aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuring-alias-routing.html): You can configure an alias to send a specified percentage of traffic to multiple function versions.
- [Versions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html): Manage the deployment of your Lambda functions using versions.
- [Tags](https://docs.aws.amazon.com/lambda/latest/dg/configuration-tags.html): Use tags to grant attribute-based access to your Lambda functions or to organize them by owner, project, or department.

### [Response streaming](https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html)

Create a Lambda function that streams responses.

- [Writing functions](https://docs.aws.amazon.com/lambda/latest/dg/config-rs-write-functions.html): Create a Lambda function that streams responses.
- [Invoking functions](https://docs.aws.amazon.com/lambda/latest/dg/config-rs-invoke-furls.html): Use Lambda function URLs to invoke response streaming enabled functions.
- [Tutorial: Creating a response streaming function with a function URL](https://docs.aws.amazon.com/lambda/latest/dg/response-streaming-tutorial.html): Create a Lambda function with an HTTP(S) endpoint using a .zip file archive that streams responses.


## [Invoking functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html)

- [Invoke a function synchronously](https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html): Learn how to invoke a Lambda functions synchronously using the AWS CLI

### [Asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html)

When you invoke a Lambda function asynchronously, Lambda places the request in a queue and returns a success response without additional information.

- [Error handling](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-error-handling.html): When you invoke a Lambda function asynchronously, if the function returns an error, Lambda attempts to retry the function.
- [Configuration](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-configuring.html): You can use the AWS CLI or the Lambda console to configure how Lambda handles errors and retries for your function when you invoke it asynchronously.
- [Retaining records](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html): You can configure Lambda to send records of asynchronous invocations to another AWS service on success or failure.
- [Invocation](https://docs.aws.amazon.com/lambda/latest/dg/durable-invocation.html): Learn how to invoke durable functions synchronously and asynchronously, and manage long-running executions.

### [Event source mappings](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html)

Configure a Lambda event source mapping to invoke your function from queue and stream event sources, such as Amazon SQS, Kinesis, and DynamoDB.

- [Event source mapping tags](https://docs.aws.amazon.com/lambda/latest/dg/tags-esm.html): Use tags to grant attribute-based access to your event source mappings or to organize them by owner, project, or department.
- [Event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html): Use event filtering with a Lambda event source mapping to filter out stream and queue events to your Lambda function based on certain filter criteria.
- [Testing in console](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html): Create shareable or private test events in the Lambda console to test your Lambda function's invocation results.
- [Function states](https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html): Lambda includes a State field in the function configuration for all functions to indicate when your function is ready to invoke.
- [Retries](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html): Learn about retry behavior for Lambda function errors.
- [Recursive loop detection](https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html): Learn how Lambda can detect and stop infinite recursive loops between your functions, Amazon SNS, Amazon S3, and Amazon SQS.

### [Function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html)

Configure a Lambda function URL to assign an HTTP(S) endpoint to your Lambda function without having to integrate with other AWS services.

- [Access control](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html): Secure and limit access to your Lambda function URL using the AuthType parameter along with resource-based policies.
- [Invoking function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html): Invoke your Lambda function through a dedicated HTTP(S) endpoint using a web browser, curl, Postman, or any HTTP client.
- [Monitoring function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-monitoring.html): Monitor your Lambda function using CloudTrail and CloudWatch.
- [Function URLs vs Amazon API Gateway](https://docs.aws.amazon.com/lambda/latest/dg/furls-http-invoke-decision.html): Choose between function URLs and API Gateway to invoke a Lambda function.
- [Tutorial: Creating a webhook endpoint](https://docs.aws.amazon.com/lambda/latest/dg/urls-webhook-tutorial.html): Create a webhook using a Lambda function URL


## [Function scaling](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html)

- [Configuring reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html): In Lambda, concurrency is the number of in-flight requests that your function is currently handling.
- [Configuring provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html): In Lambda, concurrency is the number of in-flight requests that your function is currently handling.
- [Scaling behavior](https://docs.aws.amazon.com/lambda/latest/dg/scaling-behavior.html): Learn how Lambda scales up your function to the concurrency quota for your AWS account.
- [Monitoring concurrency](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-concurrency.html): Lambda emits Amazon CloudWatch metrics to help you monitor concurrency for your functions.


## [Building with Node.js](https://docs.aws.amazon.com/lambda/latest/dg/lambda-nodejs.html)

- [Handler](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-handler.html): The Lambda function handler is the method in your function code that processes events.
- [Deploy .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-package.html): Your AWS Lambda functionâs code comprises a .js or .mjs file containing your functionâs handler code, together with any additional packages and modules your code depends on.
- [Deploy container images](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-image.html): Deploy your Node.js Lambda function code as a container image using an AWS provided base image or the runtime interface client.
- [Layers](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-layers.html): Learn how to package and create a Node.js Lambda layer.
- [Context](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-context.html): When Lambda runs your function, it passes a context object to the handler.
- [Logging](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-logging.html): This page describes how to output logs in a Node.js Lambda function and monitor function metrics using Amazon CloudWatch.
- [Tracing](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-tracing.html): Learn how to instrument Node.js Lambda functions using X-Ray tracing.


## [Building with TypeScript](https://docs.aws.amazon.com/lambda/latest/dg/lambda-typescript.html)

- [Handler](https://docs.aws.amazon.com/lambda/latest/dg/typescript-handler.html): The Lambda function handler is the method in your TypeScript code that processes events.
- [Deploy .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/typescript-package.html): Before you can deploy TypeScript code to AWS Lambda, you need to transpile it into JavaScript.
- [Deploy container images](https://docs.aws.amazon.com/lambda/latest/dg/typescript-image.html): Deploy your TypeScript code in Lambda as a container image using an AWS provided base image.
- [Context](https://docs.aws.amazon.com/lambda/latest/dg/typescript-context.html): When Lambda runs your function, it passes a context object to the handler.
- [Logging](https://docs.aws.amazon.com/lambda/latest/dg/typescript-logging.html): This page describes how to output logs in a TypeScript Lambda function and monitor function metrics using Amazon CloudWatch.
- [Tracing](https://docs.aws.amazon.com/lambda/latest/dg/typescript-tracing.html): Learn how to instrument TypeScript Lambda functions using X-Ray tracing.


## [Building with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)

- [Handler](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html): The Lambda function handler is the method in your Python code that processes events.
- [Deploy .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html): Learn how to deploy Python Lambda function code using a .zip file deployment package.
- [Deploy container images](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html): Deploy your Python Lambda function code as a container image using an AWS provided base image or the runtime interface client.
- [Layers](https://docs.aws.amazon.com/lambda/latest/dg/python-layers.html): Learn how to package and create a Python Lambda layer.
- [Context](https://docs.aws.amazon.com/lambda/latest/dg/python-context.html): When Lambda runs your function, it passes a context object to the handler.
- [Logging](https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html): This page describes how to output logs in a Python Lambda function and monitor function metrics using Amazon CloudWatch.
- [Testing](https://docs.aws.amazon.com/lambda/latest/dg/python-testing.html): Learn how to test serverless functions written in Python.
- [Tracing](https://docs.aws.amazon.com/lambda/latest/dg/python-tracing.html): Learn how to instrument Python Lambda functions using X-Ray tracing.


## [Building with Ruby](https://docs.aws.amazon.com/lambda/latest/dg/lambda-ruby.html)

- [Handler](https://docs.aws.amazon.com/lambda/latest/dg/ruby-handler.html): The Lambda function handler is the method in your Ruby code that processes events.
- [Deploy .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/ruby-package.html): Learn how to deploy Ruby Lambda function code using a .zip file deployment package.
- [Deploy container images](https://docs.aws.amazon.com/lambda/latest/dg/ruby-image.html): Deploy your Ruby Lambda function code as a container image using an AWS provided base image or the runtime interface client.
- [Layers](https://docs.aws.amazon.com/lambda/latest/dg/ruby-layers.html): Learn how to package and create a Ruby Lambda layer.
- [Context](https://docs.aws.amazon.com/lambda/latest/dg/ruby-context.html): When Lambda runs your function, it passes a context object to the handler.
- [Logging](https://docs.aws.amazon.com/lambda/latest/dg/ruby-logging.html): This page describes how to output logs in a Ruby Lambda function and monitor function metrics using Amazon CloudWatch.
- [Tracing](https://docs.aws.amazon.com/lambda/latest/dg/ruby-tracing.html): Lambda integrates with AWS X-Ray to enable you to trace, debug, and optimize Lambda applications.


## [Building with Java](https://docs.aws.amazon.com/lambda/latest/dg/lambda-java.html)

- [Handler](https://docs.aws.amazon.com/lambda/latest/dg/java-handler.html): The Lambda function handler is the method in your function code that processes events.
- [Deploy .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/java-package.html): Your AWS Lambda function's code consists of scripts or compiled programs and their dependencies.
- [Deploy container images](https://docs.aws.amazon.com/lambda/latest/dg/java-image.html): Deploy your Java Lambda function code as a container image using an AWS provided base image or the runtime interface client.
- [Layers](https://docs.aws.amazon.com/lambda/latest/dg/java-layers.html): Learn how to package and create a Java Lambda layer.
- [Custom serialization](https://docs.aws.amazon.com/lambda/latest/dg/java-custom-serialization.html): Use custom serialization to handle event payloads from third-party APIs or custom internal systems.
- [Custom startup behavior](https://docs.aws.amazon.com/lambda/latest/dg/java-customization.html): This page describes settings specific to Java functions in AWS Lambda.
- [Context](https://docs.aws.amazon.com/lambda/latest/dg/java-context.html): When Lambda runs your function, it passes a context object to the handler.
- [Logging](https://docs.aws.amazon.com/lambda/latest/dg/java-logging.html): This page describes how to output logs in a Java Lambda function and monitor function metrics using Amazon CloudWatch.
- [Tracing](https://docs.aws.amazon.com/lambda/latest/dg/java-tracing.html): Learn how to instrument Java Lambda functions using X-Ray tracing.
- [Sample apps](https://docs.aws.amazon.com/lambda/latest/dg/java-samples.html): The GitHub repository for this guide provides sample applications that demonstrate the use of Java in AWS Lambda.


## [Building with Go](https://docs.aws.amazon.com/lambda/latest/dg/lambda-golang.html)

- [Handler](https://docs.aws.amazon.com/lambda/latest/dg/golang-handler.html): The Lambda function handler is the method in your function code that processes events.
- [Context](https://docs.aws.amazon.com/lambda/latest/dg/golang-context.html): In Lambda, the context object provides methods and properties with information about the invocation, function, and execution environment.
- [Deploy .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/golang-package.html): This page describes how to create a .zip file as your deployment package for Go using an (the provided runtime family).
- [Deploy container images](https://docs.aws.amazon.com/lambda/latest/dg/go-image.html): Deploy your Go Lambda function code as a container image using an AWS provided base image or the runtime interface client.
- [Layers](https://docs.aws.amazon.com/lambda/latest/dg/golang-layers.html): Learn why it's unnecessary to use Lambda layers with Go functions.
- [Logging](https://docs.aws.amazon.com/lambda/latest/dg/golang-logging.html): This page describes how to output logs in a Go Lambda function and monitor function metrics using Amazon CloudWatch.
- [Tracing](https://docs.aws.amazon.com/lambda/latest/dg/golang-tracing.html): Learn how to instrument Go Lambda functions using X-Ray tracing.


## [Building with C#](https://docs.aws.amazon.com/lambda/latest/dg/lambda-csharp.html)

- [Handler](https://docs.aws.amazon.com/lambda/latest/dg/csharp-handler.html): Learn how to define a Lambda function handler for C# functions.

### [Deployment package](https://docs.aws.amazon.com/lambda/latest/dg/csharp-package.html)

Learn how to build and deploy .NET code to Lambda using .zip file archives.

- [NET Lambda Global CLI](https://docs.aws.amazon.com/lambda/latest/dg/csharp-package-cli.html): Learn how to use the .NET CLI and .NET Lambda Global CLI extension to develop .NET Lambda projects.
- [AWS SAM](https://docs.aws.amazon.com/lambda/latest/dg/csharp-package-sam.html): Learn how to download, build, and deploy a sample Hello World .NET application using AWS SAM.
- [AWS CDK](https://docs.aws.amazon.com/lambda/latest/dg/csharp-package-cdk.html): Learn how to download, build, and deploy a sample Hello World .NET application using AWS CDK.
- [ASP.NET](https://docs.aws.amazon.com/lambda/latest/dg/csharp-package-asp.html): Learn how to use AWS tooling to deploy existing ASP.NET applications to Lambda
- [Layers](https://docs.aws.amazon.com/lambda/latest/dg/dotnet-layers.html): Learn why it's unnecessary to use Lambda layers with .NET functions.
- [Deploy container images](https://docs.aws.amazon.com/lambda/latest/dg/csharp-image.html): Deploy your .NET Lambda function code as a container image using an AWS provided base image or the runtime interface client.
- [Native AOT compilation](https://docs.aws.amazon.com/lambda/latest/dg/dotnet-native-aot.html): Learn how to create and deploy Lambda functions that use .NET 7 and .NET 8 with native AOT compilation, which can reduce cold start times.
- [Context](https://docs.aws.amazon.com/lambda/latest/dg/csharp-context.html): When Lambda runs your function, it passes a context object to the handler.
- [Logging](https://docs.aws.amazon.com/lambda/latest/dg/csharp-logging.html): This page describes how to output logs in a C# Lambda function and monitor function metrics using Amazon CloudWatch.
- [Tracing](https://docs.aws.amazon.com/lambda/latest/dg/csharp-tracing.html): Lambda integrates with AWS X-Ray to help you trace, debug, and optimize Lambda applications.
- [Testing](https://docs.aws.amazon.com/lambda/latest/dg/dotnet-csharp-testing.html): Learn how to test serverless functions written in C#.


## [Building with PowerShell](https://docs.aws.amazon.com/lambda/latest/dg/lambda-powershell.html)

- [Development Environment](https://docs.aws.amazon.com/lambda/latest/dg/powershell-devenv.html): Lambda provides a set of tools and libraries for the PowerShell runtime.
- [Deployment package](https://docs.aws.amazon.com/lambda/latest/dg/powershell-package.html): A deployment package for the PowerShell runtime contains your PowerShell script, PowerShell modules that are required for your PowerShell script, and the assemblies needed to host PowerShell Core.
- [Handler](https://docs.aws.amazon.com/lambda/latest/dg/powershell-handler.html): Learn how to define a Lambda function handler for PowerShell functions.
- [Context](https://docs.aws.amazon.com/lambda/latest/dg/powershell-context.html): When Lambda runs your function, it passes context information by making a $LambdaContext variable available to the handler.
- [Logging](https://docs.aws.amazon.com/lambda/latest/dg/powershell-logging.html): This page describes how to output logs in a Powershell Lambda function and monitor function metrics using Amazon CloudWatch.


## [Building with Rust](https://docs.aws.amazon.com/lambda/latest/dg/lambda-rust.html)

- [Handler](https://docs.aws.amazon.com/lambda/latest/dg/rust-handler.html): The Lambda function handler is the function in your code that processes events.
- [Context](https://docs.aws.amazon.com/lambda/latest/dg/rust-context.html): The context object provides information about the invocation, function, and execution environment.
- [HTTP events](https://docs.aws.amazon.com/lambda/latest/dg/rust-http-events.html): This page describes how to handle HTTP events with Rust functions.
- [Deploy .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/rust-package.html): This page describes how to build and deploy a Rust function to AWS Lambda.
- [Layers](https://docs.aws.amazon.com/lambda/latest/dg/rust-layers.html): Learn why it's unnecessary to use Lambda layers with Rust functions.
- [Logging](https://docs.aws.amazon.com/lambda/latest/dg/rust-logging.html): This page describes how to output logs in a Rust Lambda function and monitor function metrics using Amazon CloudWatch.


## [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html)

- [Activating SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-activate.html): Use the Lambda console, the AWS CLI, or the Lambda API to activate SnapStart on a Lambda function.
- [Handling uniqueness](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-uniqueness.html): To maintain randomness when working with Lambda SnapStart, use a CSPRNG and avoid caching random values during initialization.

### [Runtime hooks](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html)

Use runtime hooks to implement code before creating a Lambda function snapshot or after restoring a snapshot.

- [Java](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks-java.html): Use Java runtime hooks to implement code before creating a Lambda function snapshot or after restoring a snapshot.
- [Python](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks-python.html): Use Python runtime hooks to implement code before creating a Lambda function snapshot or after restoring a snapshot.
- [.NET](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks-dotnet.html): Use .NET runtime hooks to implement code before creating a Lambda function snapshot or after restoring a snapshot.
- [Monitoring](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-monitoring.html): CloudWatch records the Init Duration and Restore Duration for Lambda SnapStart functions.
- [Security model](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html): Learn how Lambda encrypts snapshots when SnapStart is active.
- [Best practices](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-best-practices.html): Learn how to optimize function performance with Lambda SnapStart.
- [Troubleshooting](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-troubleshooting.html): Resolve common issues that occur when creating and invoking Lambda function snapshots.


## [Tenant isolation](https://docs.aws.amazon.com/lambda/latest/dg/tenant-isolation.html)

- [Enabling tenant isolation](https://docs.aws.amazon.com/lambda/latest/dg/tenant-isolation-configure.html): Learn how to implement tenant isolation in AWS Lambda functions using console, AWS CLI, CloudFormation, and SDK methods.
- [Invoking functions with tenant isolation](https://docs.aws.amazon.com/lambda/latest/dg/tenant-isolation-invoke.html): Learn how to invoke AWS Lambda functions that have tenant isolation enabled using console, AWS CLI, API, and Amazon API Gateway methods.
- [Accessing in code](https://docs.aws.amazon.com/lambda/latest/dg/tenant-isolation-context.html): Learn how to access and use the tenant identifier within your AWS Lambda function code for tenant-specific logic, monitoring, and debugging.
- [Monitoring](https://docs.aws.amazon.com/lambda/latest/dg/tenant-isolation-monitor.html): Learn how to implement tenant isolation in AWS Lambda functions using console, AWS CLI, CloudFormation, and SDK methods.
- [Troubleshooting](https://docs.aws.amazon.com/lambda/latest/dg/tenant-isolation-troubleshooting.html): Resolve common issues that occur when creating and invoking Lambda function with tenant isolation mode enabled.


## [Integrating other services](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)

### [Apache Kafka](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka-esm.html)

Learn how to use an Apache Kafka cluster as an event source for Lambda.

### [MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html)

Use a Lambda function with Amazon MSK to process records in an Apache Kafka topic.

- [Cluster and network setup](https://docs.aws.amazon.com/lambda/latest/dg/with-msk-cluster-network.html): Learn how to correctly configure your Amazon MSK cluster and Amazon VPC for use with Lambda.
- [Configure permissions](https://docs.aws.amazon.com/lambda/latest/dg/with-msk-permissions.html): Learn how to correctly configure the required execution role permissions to allow an Amazon MSK cluster to invoke your Lambda function.

### [Configure event source](https://docs.aws.amazon.com/lambda/latest/dg/with-msk-configure.html)

Learn how to use an Amazon MSK cluster as an event source for Lambda.

- [Cluster authentication](https://docs.aws.amazon.com/lambda/latest/dg/msk-cluster-auth.html): Lambda needs permission to access your Amazon MSK cluster, retrieve records, and perform other tasks.
- [Event source mapping](https://docs.aws.amazon.com/lambda/latest/dg/msk-esm-create.html): To create an event source mapping, you can use the Lambda console, the AWS Command Line Interface (CLI), or an AWS SDK.
- [Cross-account event source mappings](https://docs.aws.amazon.com/lambda/latest/dg/msk-cross-account.html): You can use multi-VPC private connectivity to connect a Lambda function to a provisioned MSK cluster in a different AWS account.
- [Configuration parameters](https://docs.aws.amazon.com/lambda/latest/dg/msk-esm-parameters.html): All Lambda event source types share the same CreateEventSourceMapping and UpdateEventSourceMapping API operations.
- [Tutorial](https://docs.aws.amazon.com/lambda/latest/dg/services-msk-tutorial.html): Configure IAM auth, AWS PrivateLink networking and Lambda resources necessary to process Amazon MSK events with a Lambda function.

### [Self-managed Apache Kafka](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html)

Learn how to use a self-managed Apache Kafka cluster as an event source for Lambda.

- [Cluster and network setup](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka-cluster-network.html): Set up your self-managed Apache Kafka cluster and configure network access for Lambda.
- [Configure permissions](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka-permissions.html): Configure the necessary permissions for your Lambda function to work with self-managed Apache Kafka.

### [Configure event source](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka-configure.html)

Learn how to use a self-managed Apache Kafka cluster as an event source for Lambda.

- [Cluster authentication](https://docs.aws.amazon.com/lambda/latest/dg/kafka-cluster-auth.html): Lambda supports several methods to authenticate with your self-managed Apache Kafka cluster.
- [Event source mapping](https://docs.aws.amazon.com/lambda/latest/dg/kafka-esm-create.html): To create an event source mapping, you can use the Lambda console, the AWS Command Line Interface (CLI), or an AWS SDK.
- [Configuration parameters](https://docs.aws.amazon.com/lambda/latest/dg/kafka-esm-parameters.html): All Lambda event source types share the same CreateEventSourceMapping and UpdateEventSourceMapping API operations.
- [Event poller scaling](https://docs.aws.amazon.com/lambda/latest/dg/kafka-scaling-modes.html): Configure event poller scaling modes for Amazon MSK and self-managed Apache Kafka event source mappings.
- [Polling and stream positions](https://docs.aws.amazon.com/lambda/latest/dg/kafka-starting-positions.html): Configure starting positions for your Amazon MSK and self-managed Apache Kafka event source mappings.
- [Consumer group ID](https://docs.aws.amazon.com/lambda/latest/dg/kafka-consumer-group-id.html): Configure consumer group IDs for Amazon MSK and self-managed Apache Kafka event source mappings.
- [Event filtering](https://docs.aws.amazon.com/lambda/latest/dg/kafka-filtering.html): Control which Kafka records are passed to your Lambda function by using event filtering.
- [Schema registries with event sources](https://docs.aws.amazon.com/lambda/latest/dg/services-consume-kafka-events.html): Learn how to consume Kafka events for Lambda.
- [Low latency Apache Kafka](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka-low-latency.html): Learn how to optimize AWS Lambda's Kafka event source mapping for low-latency processing.
- [Retry configurations](https://docs.aws.amazon.com/lambda/latest/dg/kafka-retry-configurations.html): You can configure how Lambda handles errors and retries for your Kafka event source mappings.
- [Retain failed invocations](https://docs.aws.amazon.com/lambda/latest/dg/kafka-on-failure.html): Learn how to configure an on-failure destination for Amazon MSK and self-managed Apache Kafka event sources to capture discarded batches.
- [Kafka on-failure destination](https://docs.aws.amazon.com/lambda/latest/dg/kafka-on-failure-destination.html): You can configure a Kafka topic as an on-failure destination for your Kafka event source mappings.
- [Kafka ESM logging](https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html): You can configure the system-level logging for your Kafka event source mappings to enable and filter the system logs that Lambda event pollers send to CloudWatch.
- [Troubleshooting](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka-troubleshoot.html): Get troubleshooting advice for Amazon MSK and self-managed Apache Kafka with Lambda

### [API Gateway](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html)

Learn how to use AWS Lambda with Amazon API Gateway.

- [Tutorial](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-tutorial.html): Learn how to create an API Gateway REST API with a backend Lambda function.
- [Errors](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-errors.html): Learn how to use AWS Lambda with Amazon API Gateway.
- [API Gateway vs function URLs](https://docs.aws.amazon.com/lambda/latest/dg/apig-http-invoke-decision.html): Choose between function URLs and API Gateway to invoke a Lambda function.
- [Infrastructure Composer](https://docs.aws.amazon.com/lambda/latest/dg/services-appcomposer.html): How to use AWS Lambda with AWS Infrastructure Composer.
- [CloudFormation](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudformation.html): Trigger a Lambda function with CloudFormation.

### [Amazon DocumentDB](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html)

Learn how to set up and start using Amazon DocumentDB with Lambda.

- [Tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb-tutorial.html): Learn how to create a Lambda function that consumes messages from a Amazon DocumentDB change stream.

### [DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html)

Describes how to process records from DynamoDB with AWS Lambda.

- [Create mapping](https://docs.aws.amazon.com/lambda/latest/dg/services-dynamodb-eventsourcemapping.html): Create an event source mapping to tell Lambda to send records from your stream to a Lambda function.
- [Batch item failures](https://docs.aws.amazon.com/lambda/latest/dg/services-ddb-batchfailurereporting.html): To allow for partial successes while processing batches from an Kinesis Data Streams event source, turn on ReportBatchItemFailures.
- [Error handling](https://docs.aws.amazon.com/lambda/latest/dg/services-dynamodb-errors.html): Configure an on-failure destination for DynamoDB event source mappings to retain records that fail processing.
- [Stateful processing](https://docs.aws.amazon.com/lambda/latest/dg/services-ddb-windows.html): Lambda functions can run continuous stream processing applications.
- [Parameters](https://docs.aws.amazon.com/lambda/latest/dg/services-ddb-params.html): All Lambda event source types share the same CreateEventSourceMapping and UpdateEventSourceMapping API operations.
- [Event filtering](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb-filtering.html): How to use event filtering with DynamoDB event sources.
- [Tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb-example.html): In this tutorial, you create a Lambda function to consume events from an Amazon DynamoDB stream.
- [EC2](https://docs.aws.amazon.com/lambda/latest/dg/services-ec2.html): Use an AWS Lambda function to manage resources in Amazon EC2.
- [Elastic Load Balancing (Application Load Balancer)](https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html): Use an AWS Lambda function to process messages from an Application Load Balancer.
- [Invoke using an EventBridge Scheduler](https://docs.aws.amazon.com/lambda/latest/dg/with-eventbridge-scheduler.html): Describes invoking a Lambda function on a schedule using EventBridge Scheduler.
- [IoT](https://docs.aws.amazon.com/lambda/latest/dg/services-iot.html): Learn how to trigger a Lambda function with AWS IoT.

### [Kinesis Data Streams](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html)

Learn how Lambda processes records from Kinesis Data Streams.

- [Create mapping](https://docs.aws.amazon.com/lambda/latest/dg/services-kinesis-create.html): Create an event Lambda source mapping for Amazon Kinesis Data Streams.
- [Batch item failures](https://docs.aws.amazon.com/lambda/latest/dg/services-kinesis-batchfailurereporting.html): To allow for partial successes while processing batches from an Kinesis Data Streams event source, turn on ReportBatchItemFailures.
- [Error handling](https://docs.aws.amazon.com/lambda/latest/dg/kinesis-on-failure-destination.html): Configure an on-failure destination for Kinesis Data Streams event source mappings to retain batches that fail processing.
- [Stateful processing](https://docs.aws.amazon.com/lambda/latest/dg/services-kinesis-windows.html): Use tumbling windows to maintain state across Lambda invocations for an Kinesis Data Streams event source.
- [Parameters](https://docs.aws.amazon.com/lambda/latest/dg/services-kinesis-parameters.html): Learn about Kinesis Data Streams event source mapping options for Lambda.
- [Event filtering](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis-filtering.html): How to use event filtering with Kinesis event sources.
- [Tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis-example.html): Create a Lambda function that consumes events from an Kinesis data stream.
- [Kubernetes](https://docs.aws.amazon.com/lambda/latest/dg/with-kubernetes.html): You can deploy and manage Lambda functions with the Kubernetes API using AWS Controllers for Kubernetes (ACK) or Crossplane.

### [MQ](https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html)

Use a Lambda function with Amazon MQ to process records from a message broker.

- [Configure event source](https://docs.aws.amazon.com/lambda/latest/dg/process-mq-messages-with-lambda.html): Learn how to process messages from Amazon MQ with a Lambda function.
- [Parameters](https://docs.aws.amazon.com/lambda/latest/dg/services-mq-params.html): Learn about Amazon MQ and RabbitMQ event source mapping options for Lambda.
- [Event filtering](https://docs.aws.amazon.com/lambda/latest/dg/with-mq-filtering.html): How to use event filtering with Amazon MQ event sources.
- [Troubleshoot](https://docs.aws.amazon.com/lambda/latest/dg/services-mq-errors.html): When a Lambda function encounters an unrecoverable error, your Amazon MQ consumer stops processing records.

### [RDS](https://docs.aws.amazon.com/lambda/latest/dg/services-rds.html)

Use an AWS Lambda function to process messages from an Amazon RDS database.

- [Amazon RDS vs DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/ddb-rds-database-decision.html): Choose between DynamoDB and Amazon RDS for your database solution for serverless apps.

### [S3](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html)

Use Lambda to process event notifications from Amazon S3.

- [Tutorial: Use an S3 trigger](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html): In this tutorial, you use the console to create a Lambda function and configure a trigger for an Amazon Simple Storage Service (Amazon S3) bucket.
- [Tutorial: Use an Amazon S3 trigger to create thumbnails](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-tutorial.html): In this tutorial, you create and configure a Lambda function that resizes images added to an Amazon Simple Storage Service (Amazon S3) bucket.
- [Secrets Manager](https://docs.aws.amazon.com/lambda/latest/dg/with-secrets-manager.html): Learn how to retrieve secrets in your Lambda functions using the AWS Parameters and Secrets Lambda extension.

### [SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)

How Lambda processes records from Amazon SQS

- [Create mapping](https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-configure.html): Learn how to create and configure an Amazon SQS event source mapping in Lambda.
- [Scaling behavior](https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-scaling.html): You can control the scaling behavior of your Amazon SQS event source mappings either through maximum concurrency settings or by enabling provisioned mode.
- [Error handling](https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-errorhandling.html): Learn how to handle errors and return partial batch item failures for an Quick event source.
- [Parameters](https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-parameters.html): Learn about Amazon SQS event source mapping options for Lambda.
- [Event filtering](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs-filtering.html): How to use event filtering with Amazon SQS event sources.
- [Tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs-example.html): Learn how to create a Lambda function that consumes messages from an Amazon SQS queue.
- [SQS cross-account tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs-cross-account-example.html): Learn how to use Lambda with an Amazon SQS queue in a different AWS account.
- [Step Functions](https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html): How Lambda processes records from Amazon SQS
- [S3 Batch](https://docs.aws.amazon.com/lambda/latest/dg/services-s3-batch.html): Use Lambda to process batch operations from Amazon S3.

### [SNS](https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html)

Use Lambda to process Amazon SNS notifications.

- [Tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html): In this tutorial, you use a Lambda function in one AWS account to subscribe to an Amazon Simple Notification Service (Amazon SNS) topic in a separate AWS account.


## [Lambda permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html)

### [Execution role (permissions for functions to access other resources)](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)

Learn how to manage permissions for your Lambda function's execution role.

- [Update execution role](https://docs.aws.amazon.com/lambda/latest/dg/permissions-executionrole-update.html): Learn how to update permissions for your Lambda function's execution role.
- [AWS managed policies](https://docs.aws.amazon.com/lambda/latest/dg/permissions-managed-policies.html): Learn how to use the AWS managed policies that Lambda supports for execution roles.
- [Source function ARN](https://docs.aws.amazon.com/lambda/latest/dg/permissions-source-function-arn.html): Learn how to use the source function ARN to control function access to other resources.

### [Access permissions (permissions for other entities to access your functions)](https://docs.aws.amazon.com/lambda/latest/dg/permissions-granting-access.html)

Learn how to manage permissions that other AWS users and entities need to access your Lambda functions.

### [Identity-based policies](https://docs.aws.amazon.com/lambda/latest/dg/access-control-identity-based.html)

Learn how to use identity-based policies to grant users access to your Lambda resources.

- [Function access](https://docs.aws.amazon.com/lambda/latest/dg/permissions-user-function.html): Create identity-based permissions policies for Lambda functions.
- [Layer access](https://docs.aws.amazon.com/lambda/latest/dg/permissions-user-layer.html): Create identity-based permissions policies for Lambda layers.

### [Resource-based policies](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html)

Learn how to view resource-based permissions policies for Lambda functions and layers.

- [Function access for AWS services](https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-services.html): Use resource-based permissions policies to grant AWS services access to Lambda functions.
- [Function access for AWS Organizations](https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-organization.html): Learn how resource-based permissions policies for Lambda functions and layers let you grant permissions to other AWS accounts or organizations to use your functions on a per-resource basis.
- [Function access for other accounts](https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-cross-account.html): Learn how to grant other AWS accounts access to Lambda functions.
- [Layer access for other accounts](https://docs.aws.amazon.com/lambda/latest/dg/permissions-layer-cross-account.html): Learn how to grant other AWS accounts access to Lambda layers.

### [Attribute-based access control](https://docs.aws.amazon.com/lambda/latest/dg/attribute-based-access-control.html)

Learn how to use tags to control access to your Lambda functions.

- [Secure your functions by tag](https://docs.aws.amazon.com/lambda/latest/dg/attribute-based-access-control-example.html): The following steps demonstrate one way to set up permissions for functions using ABAC.
- [Resources and Conditions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html): Learn how to restrict access to your Lambda resources by specifying resources and conditions in an IAM policy.


## [Security, governance, and compliance](https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html)

### [Data protection](https://docs.aws.amazon.com/lambda/latest/dg/security-dataprotection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS Lambda.

- [Encryption at rest](https://docs.aws.amazon.com/lambda/latest/dg/security-encryption-at-rest.html): Learn how Lambda handles data encryption at rest.
- [Using service-linked roles](https://docs.aws.amazon.com/lambda/latest/dg/using-service-linked-roles.html): How to use service-linked roles to give Lambda access to resources in your AWS account.

### [Identity and Access Management](https://docs.aws.amazon.com/lambda/latest/dg/security-iam.html)

How to authenticate requests and manage access to your Lambda resources.

- [How AWS Lambda works with IAM](https://docs.aws.amazon.com/lambda/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Lambda, learn what IAM features are available to use with Lambda.
- [Identity-based policy examples](https://docs.aws.amazon.com/lambda/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Lambda resources.
- [AWS managed policies](https://docs.aws.amazon.com/lambda/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for Lambda and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/lambda/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Lambda and IAM.

### [Governance](https://docs.aws.amazon.com/lambda/latest/dg/governance-concepts.html)

Achieve the right balance between agility and governance for your serverless applications by implementing a comprehensive governance strategy for Lambda, leveraging tools like AWS CloudFormation Guard, AWS Config, and Amazon Inspector to enforce policies and controls throughout your software development lifecycle.

- [Proactive controls with Guard](https://docs.aws.amazon.com/lambda/latest/dg/governance-cloudformation-guard.html): AWS CloudFormation Guard is an open-source, general-purpose, policy-as-code evaluation tool.
- [Proactive controls with AWS Config](https://docs.aws.amazon.com/lambda/latest/dg/governance-config.html): Ensure compliance in your serverless applications early in the development process using AWS Config's proactive controls.
- [Detective controls with AWS Config](https://docs.aws.amazon.com/lambda/latest/dg/governance-config-detection.html): Use AWS Config detective and corrective controls to govern your Lambda environment.
- [Code signing](https://docs.aws.amazon.com/lambda/latest/dg/governance-code-signing.html): AWS Signer is a fully managed code-signing service that allows you to validate your code against a digital signature to confirm that code is unaltered and from a trusted publisher.
- [Code scanning](https://docs.aws.amazon.com/lambda/latest/dg/governance-code-scanning.html): Amazon Inspector provides continuous security vulnerability assessments for AWS Lambda functions and layers.
- [Observability](https://docs.aws.amazon.com/lambda/latest/dg/governance-observability.html): AWS Config is a useful tool to find and fix non-compliant AWS Serverless resources.
- [Compliance validation](https://docs.aws.amazon.com/lambda/latest/dg/security-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/lambda/latest/dg/security-resilience.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Lambda features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/lambda/latest/dg/security-infrastructure.html): Learn how AWS Lambda isolates service traffic.
- [Securing workloads with public endpoints](https://docs.aws.amazon.com/lambda/latest/dg/security-public-endpoints.html): For workloads that are accessible publicly, AWS provides a number of features and services that can help mitigate certain risks.

### [Code signing](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html)

Code signing checks every code deployment and verifies that the function code package is signed by a trusted source.

- [Create configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning-create.html): Create a code signing configuration for Lambda.
- [Permissions](https://docs.aws.amazon.com/lambda/latest/dg/config-codesigning-policies.html): Use IAM to control who can create code signing configurations.
- [Code signing configuration tags](https://docs.aws.amazon.com/lambda/latest/dg/tags-csc.html): Use tags to grant attribute-based access to your code signing configurations or to organize them by owner, project, or department.


## [Monitoring and debugging functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html)

### [Function metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html)

Make use of CloudWatch metrics provided for Lambda functions to help monitor application performance.

- [View function metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-view.html): Learn how to view CloudWatch metrics for your Lambda function using the Lambda console.
- [Metric types](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html): Learn about the different types of metrics for Lambda: invocation metrics, performance metrics, concurrency metrics, asynchronous invocation metrics, and event source mapping metrics.

### [Function logs](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-logs.html)

Learn about Lambda function logs, their destinations, and how to configure them for efficient troubleshooting and analysis.

- [Log formats](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-logformat.html): Capturing your log outputs as JSON key value pairs makes it easier to search and filter when debugging your functions.
- [Log-level filtering](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-log-level.html): Lambda can filter your function's logs so that only logs of a certain detail level or lower are sent to CloudWatch Logs.

### [Log with CloudWatch Logs](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html)

Make use of Lambda's automatic function monitoring to help validate your code is working as expected and troubleshoot failures.

- [Configure CloudWatch function logs](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-loggroups.html): By default, CloudWatch automatically creates a log group named /aws/lambda/<function name> for your function when it's first invoked.
- [View function logs](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-view.html): You can view Amazon CloudWatch logs for your Lambda function using the Lambda console, the CloudWatch console, or the AWS Command Line Interface (AWS CLI).
- [Log with Firehose](https://docs.aws.amazon.com/lambda/latest/dg/logging-with-firehose.html): Configure your Lambda function to send logs directly to Firehose for real-time streaming and analysis.
- [Log with Amazon S3](https://docs.aws.amazon.com/lambda/latest/dg/logging-with-s3.html): Configure your Lambda function to send logs directly to Amazon S3 for long-term storage and analysis.
- [CloudTrail logs](https://docs.aws.amazon.com/lambda/latest/dg/logging-using-cloudtrail.html): Learn about logging AWS Lambda with AWS CloudTrail.
- [AWS X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html): Use AWS X-Ray with Lambda to visualize components of your applications and understand performance
- [Function insights](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-insights.html): This page describes how to enable and use Amazon CloudWatch Lambda Insights to diagnose issues with your AWS Lambda functions.
- [View application metrics](https://docs.aws.amazon.com/lambda/latest/dg/applications-console-monitoring.html): Learn how to monitor Lambda applications.
- [Application Signals](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-application-signals.html): This page describes how to enable and use Amazon CloudWatch Application Signals to view metrics related to your application performance.
- [Debug with VS Code](https://docs.aws.amazon.com/lambda/latest/dg/debugging.html): Remotely debug Lambda functions with Visual Studio Code


## [Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html)

- [Packaging layers](https://docs.aws.amazon.com/lambda/latest/dg/packaging-layers.html): Learn how to properly package a Lambda layer.
- [Creating and deleting layers](https://docs.aws.amazon.com/lambda/latest/dg/creating-deleting-layers.html): Learn how to properly create and delete a Lambda layer.
- [Adding layers](https://docs.aws.amazon.com/lambda/latest/dg/adding-layers.html): Learn how to add a Lambda layer to a function.
- [Layers with CloudFormation](https://docs.aws.amazon.com/lambda/latest/dg/layers-cfn.html): Learn how to use Lambda layers with CloudFormation.
- [Layers with AWS SAM](https://docs.aws.amazon.com/lambda/latest/dg/layers-sam.html): Learn how to use Lambda layers with AWS SAM.


## [Lambda extensions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html)

- [Configuring extensions](https://docs.aws.amazon.com/lambda/latest/dg/extensions-configuration.html): Learn how to configure extensions for both Lambda .zip file archives and container images.
- [Extensions partners](https://docs.aws.amazon.com/lambda/latest/dg/extensions-api-partners.html): List of AWS Lambda partners with ready to use extensions.
- [Extensions API](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-extensions-api.html): Use the extensions API to create extensions that integrate code with the Lambda execution environment.

### [Telemetry API](https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api.html)

Learn how to use the Lambda Telemetry API to subscribe extensions to telemetry streams.

- [API reference](https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api-reference.html): Learn how to use the Subscribe API in the Lambda Telemetry API to subscribe a Lambda extension to a telemetry stream.
- [Event schema reference](https://docs.aws.amazon.com/lambda/latest/dg/telemetry-schema-reference.html): Learn about all the Event and shared object types that the Lambda Telemetry API supports, and how you can use them.
- [Converting events to OTel Spans](https://docs.aws.amazon.com/lambda/latest/dg/telemetry-otel-spans.html): Learn how to convert Lambda Telemetry API Event objects to OTel Spans using Span Events or Child Spans.
- [Logs API](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-logs-api.html): Lambda extensions can use the Logs API to subscribe to function logs and platform logs.


## [Troubleshooting](https://docs.aws.amazon.com/lambda/latest/dg/lambda-troubleshooting.html)

- [Configuration](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-configuration.html): Learn how to troubleshoot common configuration issues in Lambda
- [Deployment](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-deployment.html): Learn how to troubleshoot common deployment issues in Lambda
- [Invocation](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-invocation.html): Learn how to troubleshoot common invocation issues in Lambda
- [Execution](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-execution.html): Learn how to troubleshoot common execution issues in Lambda
- [Event source mapping](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-event-source-mapping.html): Learn how to troubleshoot common event source mapping issues in Lambda
- [Networking](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-networking.html): Learn how to troubleshoot common Lambda networking issues.


## [Code examples](https://docs.aws.amazon.com/lambda/latest/dg/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/lambda/latest/dg/service_code_examples_basics.html)

The following code examples show how to use the basics of Lambda with AWS SDKs.

- [Hello Lambda](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_Hello_section.html): Hello Lambda
- [Learn the basics](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_Scenario_GettingStartedFunctions_section.html): Learn the basics of Lambda with an AWS SDK

### [Actions](https://docs.aws.amazon.com/lambda/latest/dg/service_code_examples_actions.html)

The following code examples show how to use Lambda with AWS SDKs.

- [CreateAlias](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_CreateAlias_section.html): Use CreateAlias with a CLI
- [CreateFunction](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_CreateFunction_section.html): Use CreateFunction with an AWS SDK or CLI
- [DeleteAlias](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_DeleteAlias_section.html): Use DeleteAlias with a CLI
- [DeleteFunction](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_DeleteFunction_section.html): Use DeleteFunction with an AWS SDK or CLI
- [DeleteFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_DeleteFunctionConcurrency_section.html): Use DeleteFunctionConcurrency with a CLI
- [DeleteProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_DeleteProvisionedConcurrencyConfig_section.html): Use DeleteProvisionedConcurrencyConfig with a CLI
- [GetAccountSettings](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_GetAccountSettings_section.html): Use GetAccountSettings with a CLI
- [GetAlias](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_GetAlias_section.html): Use GetAlias with a CLI
- [GetFunction](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_GetFunction_section.html): Use GetFunction with an AWS SDK or CLI
- [GetFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_GetFunctionConcurrency_section.html): Use GetFunctionConcurrency with a CLI
- [GetFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_GetFunctionConfiguration_section.html): Use GetFunctionConfiguration with a CLI
- [GetPolicy](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_GetPolicy_section.html): Use GetPolicy with a CLI
- [GetProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_GetProvisionedConcurrencyConfig_section.html): Use GetProvisionedConcurrencyConfig with a CLI
- [Invoke](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_Invoke_section.html): Use Invoke with an AWS SDK or CLI
- [ListFunctions](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_ListFunctions_section.html): Use ListFunctions with an AWS SDK or CLI
- [ListProvisionedConcurrencyConfigs](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_ListProvisionedConcurrencyConfigs_section.html): Use ListProvisionedConcurrencyConfigs with a CLI
- [ListTags](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_ListTags_section.html): Use ListTags with a CLI
- [ListVersionsByFunction](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_ListVersionsByFunction_section.html): Use ListVersionsByFunction with a CLI
- [PublishVersion](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_PublishVersion_section.html): Use PublishVersion with a CLI
- [PutFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_PutFunctionConcurrency_section.html): Use PutFunctionConcurrency with a CLI
- [PutProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_PutProvisionedConcurrencyConfig_section.html): Use PutProvisionedConcurrencyConfig with a CLI
- [RemovePermission](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_RemovePermission_section.html): Use RemovePermission with a CLI
- [TagResource](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_TagResource_section.html): Use TagResource with a CLI
- [UntagResource](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_UntagResource_section.html): Use UntagResource with a CLI
- [UpdateAlias](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_UpdateAlias_section.html): Use UpdateAlias with a CLI
- [UpdateFunctionCode](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_UpdateFunctionCode_section.html): Use UpdateFunctionCode with an AWS SDK or CLI
- [UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_UpdateFunctionConfiguration_section.html): Use UpdateFunctionConfiguration with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/lambda/latest/dg/service_code_examples_scenarios.html)

The following code examples show how to use Lambda with AWS SDKs.

- [Automatically confirm known users with a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_CognitoAutoConfirmUser_section.html): Automatically confirm known Amazon Cognito users with a Lambda function using an AWS SDK
- [Automatically migrate known users with a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_CognitoAutoMigrateUser_section.html): Automatically migrate known Amazon Cognito users with a Lambda function using an AWS SDK
- [Create a REST API to track COVID-19 data](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_ApiGatewayDataTracker_section.html): Create an API Gateway REST API to track COVID-19 data
- [Create a lending library REST API](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_AuroraRestLendingLibrary_section.html): Create a lending library REST API
- [Create a messenger application](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_StepFunctionsMessenger_section.html): Create a messenger application with Step Functions
- [Create a serverless application to manage photos](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_PAM_section.html): Create a photo asset management application that lets users manage photos using labels
- [Create a websocket chat application](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_ApiGatewayWebsocketChat_section.html): Create a websocket chat application with API Gateway
- [Create an application to analyze customer feedback](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_FSA_section.html): Create an application that analyzes customer feedback and synthesizes audio
- [Invoke a Lambda function from a browser](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_LambdaForBrowser_section.html): Invoke a Lambda function from a browser
- [Transform data with S3 Object Lambda](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_ServerlessS3DataTransformation_section.html): Transform data for your application with S3 Object Lambda
- [Use API Gateway to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_LambdaAPIGateway_section.html): Use API Gateway to invoke a Lambda function
- [Use Step Functions to invoke Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_ServerlessWorkflows_section.html): Use Step Functions to invoke Lambda functions
- [Use scheduled events to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_LambdaScheduledEvents_section.html): Use scheduled events to invoke a Lambda function
- [Use the Neptune API to query graph data](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_Neptune_Query_section.html): Use the Amazon Neptune API to develop a Lambda function that queries graph data
- [Write custom activity data with a Lambda function after Amazon Cognito user authentication](https://docs.aws.amazon.com/lambda/latest/dg/example_cross_CognitoCustomActivityLog_section.html): Write custom activity data with a Lambda function after Amazon Cognito user authentication using an AWS SDK

### [Serverless examples](https://docs.aws.amazon.com/lambda/latest/dg/service_code_examples_serverless_examples.html)

The following code examples show how to use Lambda with AWS SDKs.

- [Connecting to an Amazon RDS database in a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_connect_RDS_Lambda_section.html): Connecting to an Amazon RDS database in a Lambda function
- [Invoke a Lambda function from a Kinesis trigger](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_Kinesis_Lambda_section.html): Invoke a Lambda function from a Kinesis trigger
- [Invoke a Lambda function from a DynamoDB trigger](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_DynamoDB_Lambda_section.html): Invoke a Lambda function from a DynamoDB trigger
- [Invoke a Lambda function from a Amazon DocumentDB trigger](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_DocumentDB_Lambda_section.html): Invoke a Lambda function from a Amazon DocumentDB trigger
- [Invoke a Lambda function from an Amazon MSK trigger](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_MSK_Lambda_section.html): Invoke a Lambda function from an Amazon MSK trigger
- [Invoke a Lambda function from an Amazon S3 trigger](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_S3_Lambda_section.html): Invoke a Lambda function from an Amazon S3 trigger
- [Invoke a Lambda function from an Amazon SNS trigger](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_SNS_Lambda_section.html): Invoke a Lambda function from an Amazon SNS trigger
- [Invoke a Lambda function from an Amazon SQS trigger](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_SQS_Lambda_section.html): Invoke a Lambda function from an Amazon SQS trigger
- [Reporting batch item failures for Lambda functions with a Kinesis trigger](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_Kinesis_Lambda_batch_item_failures_section.html): Reporting batch item failures for Lambda functions with a Kinesis trigger
- [Reporting batch item failures for Lambda functions with a DynamoDB trigger](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_DynamoDB_Lambda_batch_item_failures_section.html): Reporting batch item failures for Lambda functions with a DynamoDB trigger
- [Reporting batch item failures for Lambda functions with an Amazon SQS trigger](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_SQS_Lambda_batch_item_failures_section.html): Reporting batch item failures for Lambda functions with an Amazon SQS trigger

### [AWS community contributions](https://docs.aws.amazon.com/lambda/latest/dg/service_code_examples_aws_community_contributions.html)

AWS community contributions are examples that were created and are maintained by multiple teams across AWS.

- [Build and test a serverless application](https://docs.aws.amazon.com/lambda/latest/dg/example_tributary-lite_serverless-application_section.html): Build and test a serverless application
