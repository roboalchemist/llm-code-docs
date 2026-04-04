# Source: https://docs.aws.amazon.com/cdk/v1/guide/llms.txt

# AWS Cloud Development Kit (AWS CDK) v1 Developer Guide

> Provides a conceptual overview and practical examples to help you understand the features provided by the AWS CDK and how to use them.

- [What is the AWS CDK?](https://docs.aws.amazon.com/cdk/v1/guide/home.html)
- [Managing dependencies](https://docs.aws.amazon.com/cdk/v1/guide/manage-dependencies.html)
- [Migrating to AWS CDK v2](https://docs.aws.amazon.com/cdk/v1/guide/work-with-cdk-v2.html)
- [Translating from TypeScript](https://docs.aws.amazon.com/cdk/v1/guide/multiple-languages.html)
- [Abstractions and escape hatches](https://docs.aws.amazon.com/cdk/v1/guide/cfn-layer.html)
- [Best practices](https://docs.aws.amazon.com/cdk/v1/guide/best-practices.html)
- [API reference](https://docs.aws.amazon.com/cdk/v1/guide/reference.html)
- [Testing constructs](https://docs.aws.amazon.com/cdk/v1/guide/testing.html)
- [Troubleshooting](https://docs.aws.amazon.com/cdk/v1/guide/troubleshooting.html)
- [Videos](https://docs.aws.amazon.com/cdk/v1/guide/videos.html)
- [OpenPGP keys](https://docs.aws.amazon.com/cdk/v1/guide/pgp-keys.html)
- [Document history](https://docs.aws.amazon.com/cdk/v1/guide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/cdk/v1/guide/getting-started.html)

- [Your first AWS CDK app](https://docs.aws.amazon.com/cdk/v1/guide/hello-world.html): Build a simple AWS CDK application.


## [Working with the AWS CDK](https://docs.aws.amazon.com/cdk/v1/guide/work-with.html)

- [In TypeScript](https://docs.aws.amazon.com/cdk/v1/guide/work-with-cdk-typescript.html): TypeScript is a fully-supported client language for the AWS CDK and is considered stable.
- [In JavaScript](https://docs.aws.amazon.com/cdk/v1/guide/work-with-cdk-javascript.html): JavaScript is a fully-supported client language for the AWS CDK and is considered stable.
- [In Python](https://docs.aws.amazon.com/cdk/v1/guide/work-with-cdk-python.html): Python is a fully-supported client language for the AWS CDK and is considered stable.
- [In Java](https://docs.aws.amazon.com/cdk/v1/guide/work-with-cdk-java.html): Java is a fully-supported client language for the AWS CDK and is considered stable.
- [In C#](https://docs.aws.amazon.com/cdk/v1/guide/work-with-cdk-csharp.html): .NET is a fully-supported client language for the AWS CDK and is considered stable.
- [In Go](https://docs.aws.amazon.com/cdk/v1/guide/work-with-cdk-go.html): Go is a fully-supported client language for the AWS CDK and is considered stable.


## [Concepts](https://docs.aws.amazon.com/cdk/v1/guide/core-concepts.html)

- [Constructs](https://docs.aws.amazon.com/cdk/v1/guide/constructs.html): Constructs, which represent cloud components, are the basic building blocks of AWS CDK apps.
- [Apps](https://docs.aws.amazon.com/cdk/v1/guide/apps.html): As described in , to provision infrastructure resources, all constructs that represent AWS resources must be defined, directly or indirectly, within the scope of a Stack construct.
- [Stacks](https://docs.aws.amazon.com/cdk/v1/guide/stacks.html): The unit of deployment in the AWS CDK is called a stack.
- [Environments](https://docs.aws.amazon.com/cdk/v1/guide/environments.html): Each Stack instance in your AWS CDK app is explicitly or implicitly associated with an environment (env).
- [Resources](https://docs.aws.amazon.com/cdk/v1/guide/resources.html): As described in , the AWS CDK provides a rich class library of constructs, called AWS constructs, that represent all AWS resources.
- [Identifiers](https://docs.aws.amazon.com/cdk/v1/guide/identifiers.html): The AWS CDK deals with many types of identifiers and names.
- [Tokens](https://docs.aws.amazon.com/cdk/v1/guide/tokens.html): Tokens represent values that can only be resolved at a later time in the lifecycle of an app (see ).
- [Parameters](https://docs.aws.amazon.com/cdk/v1/guide/parameters.html): CloudFormation templates can contain parametersâcustom values that are supplied at deployment time and incorporated into the template.
- [Tagging](https://docs.aws.amazon.com/cdk/v1/guide/tagging.html): Tags are informational key-value elements that you can add to constructs in your AWS CDK app.
- [Assets](https://docs.aws.amazon.com/cdk/v1/guide/assets.html): Assets are local files, directories, or Docker images.
- [Permissions](https://docs.aws.amazon.com/cdk/v1/guide/permissions.html): The AWS Construct Library uses a few common, widely-implemented idioms to manage access and permissions.
- [Context](https://docs.aws.amazon.com/cdk/v1/guide/context.html): Get information about the runtime context through context providers.
- [Feature flags](https://docs.aws.amazon.com/cdk/v1/guide/featureflags.html): Specify optional behavior of the AWS CDK.
- [Aspects](https://docs.aws.amazon.com/cdk/v1/guide/aspects.html): Aspects are a way to apply an operation to all constructs in a given scope.
- [Bootstrapping](https://docs.aws.amazon.com/cdk/v1/guide/bootstrapping.html): Deploying AWS CDK apps into an AWS environment (a combination of an AWS account and region) may require that you provision resources the AWS CDK needs to perform the deployment.


## [Examples](https://docs.aws.amazon.com/cdk/v1/guide/examples.html)

- [Serverless](https://docs.aws.amazon.com/cdk/v1/guide/serverless-example.html): This example creates a widget dispensing service.
- [ECS](https://docs.aws.amazon.com/cdk/v1/guide/ecs-example.html): Learn how to create an AWS Fargate service.
- [AWS CDK examples](https://docs.aws.amazon.com/cdk/v1/guide/about-examples.html): Examples for the AWS CDK.


## [How tos](https://docs.aws.amazon.com/cdk/v1/guide/how-tos.html)

- [Get environment value](https://docs.aws.amazon.com/cdk/v1/guide/get-env-var.html): To get the value of an environment variable, use code like the following.
- [Get CloudFormation value](https://docs.aws.amazon.com/cdk/v1/guide/get-cfn-param.html): See for information about using CloudFormation parameters with the AWS CDK.
- [Import or migrate CloudFormation template](https://docs.aws.amazon.com/cdk/v1/guide/use-cfn-template.html): The cloudformation-include.CfnInclude construct converts the resources in an imported CloudFormation template to AWS CDK L1 constructs.
- [Use resources from the CloudFormation Public Registry](https://docs.aws.amazon.com/cdk/v1/guide/use-cfn-public-registry.html): The CloudFormation Public Registry is a collection of CloudFormation extensions from both AWS and third parties that are available for use by all AWS customers.
- [Get SSM value](https://docs.aws.amazon.com/cdk/v1/guide/get-ssm-value.html): The AWS CDK can retrieve the value of AWS Systems Manager Parameter Store attributes.
- [Get Secrets Manager value](https://docs.aws.amazon.com/cdk/v1/guide/get-secrets-manager-value.html): To use values from AWS Secrets Manager in your AWS CDK app, use the fromSecretAttributes() method.
- [Create an app with multiple stacks](https://docs.aws.amazon.com/cdk/v1/guide/stack-how-to-create-multiple-stacks.html): Most of the other code examples in the AWS CDK Developer Guide involve only a single stack.
- [Set CloudWatch alarm](https://docs.aws.amazon.com/cdk/v1/guide/how-to-set-cw-alarm.html): The aws-cloudwatch package supports setting CloudWatch alarms on CloudWatch metrics.
- [Get context value](https://docs.aws.amazon.com/cdk/v1/guide/get-context-var.html): You can specify a context variable either as part of an AWS CDK CLI command, or in cdk.json.
- [Create CDK Pipeline](https://docs.aws.amazon.com/cdk/v1/guide/cdk-pipeline.html): CDK Pipelines is a construct library module for painless continuous delivery of AWS CDK applications.


## [Tools](https://docs.aws.amazon.com/cdk/v1/guide/tools.html)

- [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/v1/guide/cli.html): The AWS CDK Toolkit, the CLI command cdk, is the primary tool for interacting with your AWS CDK app.
- [AWS Toolkit for VS Code](https://docs.aws.amazon.com/cdk/v1/guide/vscode.html): The AWS Toolkit for Visual Studio Code is an open source plug-in for Visual Studio Code that makes it easier to create, debug, and deploy applications on AWS.
- [AWS SAM integration](https://docs.aws.amazon.com/cdk/v1/guide/sam.html): The AWS CDK and the AWS Serverless Application Model (AWS SAM) can work together to let you to locally build and test serverless applications defined in the CDK.


## [Security](https://docs.aws.amazon.com/cdk/v1/guide/security.html)

- [Identity and access management](https://docs.aws.amazon.com/cdk/v1/guide/security-iam.html): Provides information about identity and access management for AWS CDK.
- [Compliance validation](https://docs.aws.amazon.com/cdk/v1/guide/compliance-validation.html): Provides information about compliance validation for AWS CDK.
- [Resilience](https://docs.aws.amazon.com/cdk/v1/guide/disaster-recovery-resiliency.html): Provides information about resilience for AWS CDK.
- [Infrastructure security](https://docs.aws.amazon.com/cdk/v1/guide/infrastructure-security.html): Provides information about infrastructure security for AWS CDK.
