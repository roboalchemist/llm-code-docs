# Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/llms.txt

# AWS CloudFormation User Guide

> Create and manage AWS infrastructure deployments predictably and repeatedly using AWS CloudFormation with this User Guide.

- [What is CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
- [Best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)
- [Template Reference Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/link-to-reference-guide.html)
- [Quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html)
- [Troubleshooting](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html)
- [Troubleshooting with Amazon Q](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-troubleshooting-with-amazon-q.html)
- [Document history](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html)

- [How CloudFormation works](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html): Describes how CloudFormation works and introduces you to the key concepts you'll need to know about as you use it.
- [Signing up for an AWS account](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sign-up-for-aws.html): Learn how to sign up for an AWS account.
- [Creating your first stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.walkthrough.html): Walk through the process of creating your first CloudFormation stack using the AWS Management Console.


## [Working with templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html)

### [Template format](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-formats.html)

Provides an overview of the available CloudFormation template formats and the full template structure.

- [Using regular expressions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-regexes.html): Discover how to use regular expressions within your CloudFormation templates, and learn the technique for escaping backslashes for templates written in JSON syntax.

### [Template sections](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html)

Describes the sections that you can use in the JSON or YAML text file that describes your AWS infrastructure.

- [Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html): Define the AWS resources to provision as part of your stack in the Resources section of a CloudFormation template.
- [Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html): Customize the resources being provisioned by defining input parameters in the Parameters section of a CloudFormation template.
- [Outputs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html): Return one or more values by defining outputs in the Outputs section of a CloudFormation template.
- [Mappings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html): Specify conditional values based on a mapping key by defining mappings in the Mappings section of a template.

### [Metadata](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html)

Use the Metadata section to store additional information in your template.

- [AWS::CloudFormation::Interface](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-cloudformation-interface.html): When you create or update stacks, use the AWS::CloudFormation::Interface metadata key to group and sort parameters in the CloudFormation console.
- [Rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/rules-section-structure.html): Describes advanced parameter constraints for resources in the Rules section of an AWS CloudFormation template.
- [Conditions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/conditions-section-structure.html): Control the provisioning of resources based on logical expressions by using intrinsic functions in the Conditions section of a template.
- [Transform](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-section-structure.html): Declare the macros that CloudFormation processes when you submit your template.
- [Format version](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/format-version-structure.html): Specify the CloudFormation template format version that the template conforms to.
- [Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-description-structure.html): Provide a description of your template in the Description section of a template.
- [Infrastructure Composer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/infrastructure-composer-for-cloudformation.html): Use Infrastructure Composer in CloudFormation console mode for a drag-and-drop interface for building templates in the console.
- [AWS CloudFormation language server](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ide-extension.html): Use the AWS CloudFormation language server to author, validate, and deploy CloudFormation templates directly within your IDE.

### [IaC generator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html)

Generate infrastructure as code (IaC) templates from AWS resource types deployed in your account that are not managed by CloudFormation.

- [Start a resource scan](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/iac-generator-start-resource-scan.html): Learn how to start a resource scan with IaC generator.
- [View the scan summary](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC-view-scan-summary.html): Learn how to view a visual breakdown of your scanned resources.
- [Create a template from scanned resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/iac-generator-create-template-from-scanned-resources.html): Learn how to use IaC generator to create a template from scanned resources.
- [Create a stack from scanned resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/iac-generator-create-stack-from-scanned-resources.html): Learn how to create the stack and import the scanned resources.

### [Resolve write-only properties](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC-write-only-properties.html)

Learn how to resolve issues with write-only properties when using the IaC generator.

- [AWS::ApiGateway::RestApi write-only properties](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC-apigateway-restapi.html): Learn how to resolve issues with write-only properties in AWS::ApiGateway::RestApi resources when using the IaC generator.
- [AWS::Lambda::Function write-only properties](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC-lambda-function.html): Learn how to resolve issues with write-only properties in AWS::Lambda::Function resources when using the IaC generator.

### [Get values stored in other services](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html)

Dynamic references give you a convenient way to specify external values stored in other services and decouple sensitive information from your infrastructure-as-code templates.

- [Get Systems Manager plaintext value](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references-ssm.html): When you're creating a CloudFormation template, you might want to use plaintext values stored in Parameter Store.
- [Get Systems Manager secure string](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references-ssm-secure-strings.html): In CloudFormation, you can use sensitive data like passwords or license keys without exposing them directly in your templates by storing the sensitive data as a "secure string" in AWS Systems Manager Parameter Store.
- [Get Secrets Manager value](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references-secretsmanager.html): Secrets Manager is a service that allows you to securely store and manage secrets like database credentials, passwords, and third-party API keys.
- [Get AWS values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html): Pseudo parameters are built-in variables that provide contextual information about your AWS account, Region, and other contextual data.
- [Get stack outputs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html): Export stack output values so that other CloudFormation stacks in the same AWS account and Region can import them.
- [Specify existing resources at runtime](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-supplied-parameter-types.html): Learn how to create template parameters that require users to input identifiers of existing AWS resources or Systems Manager parameters by using CloudFormation-supplied parameter types.

### [Walkthroughs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/walkthroughs.html)

A collection of walkthroughs designed to give you hands-on practice with stack deployments.

- [Refer to resource outputs in another CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/walkthrough-crossstackref.html): Use the Export output field and the Fn::ImportValue intrinsic function to create cross-stack references across CloudFormation stacks.
- [Deploy applications on Amazon EC2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/deploying.applications.html): Learn how to install packages, create files, and start services on a Linux Amazon EC2 instance with CloudFormation using helper scripts.
- [Update a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/updating.stacks.walkthrough.html): Walk through a simple progression of updates to a running stack with CloudFormation.
- [Create a scaled and load-balanced application](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/walkthrough-autoscaling.html): Use this sample template to create a basic Apache website that uses Elastic Load Balancing and Amazon EC2 Auto Scaling.
- [Peer with a VPC in another account](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/peer-with-vpc-in-another-account.html): Learn how to use the AWS::EC2::VPCPeeringConnection resource to peer your VPC with a VPC in another AWS account.

### [Perform ECS blue/green deployments](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html)

Learn how to perform AWS CodeDeploy blue/green deployments on Amazon ECS using CloudFormation.

- [About blue/green deployments](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/about-blue-green-deployments.html): This topic provides an overview of how performing blue/green deployments with CloudFormation works.
- [Considerations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green-considerations.html): This section provides the limitations and considerations when managing your blue/green deployment using CloudFormation.
- [Hook syntax](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green-hook-syntax.html): The following syntax describes the structure of an AWS::CodeDeploy::BlueGreen hook for ECS blue/green deployments.
- [Template example](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green-template-example.html): The following example template sets up a CodeDeploy blue/green deployment on ECS.

### [Template snippets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-snippets.html)

Provides practical examples to accelerate the development of your CloudFormation templates.

- [General](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-general.html): Use these sample snippets to learn about different CloudFormation template features.

### [Auto scaling](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-autoscaling.html)

Use these example template snippets to declare CloudFormation resources and components for Amazon EC2 Auto Scaling and and Application Auto Scaling.

- [Configure Amazon EC2 Auto Scaling resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2-auto-scaling.html): Use these example template snippets to configure Amazon EC2 Auto Scaling resources with CloudFormation.
- [Configure Application Auto Scaling resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-application-auto-scaling.html): Use these example template snippets to configure Application Auto Scaling resources with CloudFormation.
- [AWS Billing Console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-billingconductor.html): Use these AWS Billing Console sample templates to help you create AWS Billing Console topics with CloudFormation.
- [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-cloudformation.html): Use these CloudFormation sample templates to help you describe CloudFormation resources.
- [CloudFront](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-cloudfront.html): Use these sample template snippets with your Amazon CloudFront distribution resources in CloudFormation.
- [CloudWatch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-cloudwatch.html): Use these CloudWatch sample templates to help you describe your CloudWatch dashboards and alarms with CloudFormation.
- [CloudWatch Logs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-cloudwatchlogs.html): Use Amazon CloudWatch Logs template snippets to help you describe CloudWatch Logs resources in your CloudFormation templates.
- [DynamoDB](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-dynamodb.html): Use Amazon DynamoDB template snippets to help you describe DynamoDB resources in your CloudFormation templates.

### [Amazon EC2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2.html)

Use these example template snippets to declare CloudFormation resources and components for Amazon EC2.

- [Configure EC2 instances](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2-instance-config.html): Use these example template snippets to configure Amazon EC2 instances with CloudFormation.
- [Create launch templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2-launch-templates.html): Use these example template snippets to configure Amazon EC2 launch templates with CloudFormation.
- [Manage security groups](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2-sg.html): Use these example template snippets to manage security groups and Amazon EC2 instances with CloudFormation.
- [Allocate Elastic IPs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2-elastic-ip.html): Use these example template snippets to manage EIPs for your Amazon EC2 instances with CloudFormation.
- [Configure VPC resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2-vpc.html): Use these example template snippets to configure Amazon VPC resources with CloudFormation.
- [Amazon ECS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ecs.html): Use Amazon Elastic Container Service sample template snippets to help you describe Amazon ECS resources in your CloudFormation templates.
- [Amazon EFS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-efs.html): Use an Amazon Elastic File System sample template to describe Amazon Elastic File System resources in your CloudFormation templates.
- [Elastic Beanstalk](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-elasticbeanstalk.html): Use Elastic Beanstalk sample template snippets to help you describe Elastic Beanstalk resources in your CloudFormation templates.
- [Elastic Load Balancing](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-elb.html): Use these Elastic Load Balancing sample templates to help you define your load balancers using CloudFormation.
- [IAM](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html): Use these sample template snippets with your AWS Identity and Access Management resources in CloudFormation.
- [AWS Lambda](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-lambda.html): Use the example template to help you describe AWS Lambda resources in your CloudFormation templates.
- [Amazon Redshift](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-redshift.html): Use Amazon Redshift sample template snippets to help you describe Amazon Redshift resources in your CloudFormation templates.
- [Amazon RDS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-rds.html): Use these sample template snippets with your Amazon RDS Instance resources with CloudFormation.
- [RouteÂ 53](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-route53.html): Use these RouteÂ 53 sample templates to help you describe RouteÂ 53 resource record sets with CloudFormation.
- [Amazon S3](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-s3.html): Use these Amazon S3 sample templates to help describe your Amazon S3 buckets with CloudFormation.
- [Amazon SNS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-sns.html): Use these Amazon SNS sample templates to help you create Amazon SNS topics with CloudFormation.
- [Amazon SQS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/scenario-sqs-queue.html): Use these Amazon SQS sample templates to help you describe Amazon SQS queues with CloudFormation.
- [Amazon Timestream](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/scenario-timestream-queue.html): Use these Amazon Timestream sample templates to help you create describe Amazon Timestream queues with CloudFormation.

### [Windows-based stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-windows-stacks.html)

Discover technical reference documentation for CloudFormation resources commonly used in Windows-based deployments.

- [Bootstrapping Windows stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-windows-stacks-bootstrapping.html): Use CloudFormation to bootstrap a Windows stack.

### [Use CloudFormation-supplied resource types](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-supplied-resource-types.html)

Learn about CloudFormation-supplied resource types that you can use in your stack templates to extend CloudFormation's capabilities beyond those of a simple stack template.

### [Custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html)

Specifies custom resources so that non-AWS resources can be included in a CloudFormation stack.

- [Request and response reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref.html): Request and response details for Create, Update, and Delete operations on CloudFormation custom resources.
- [Amazon SNS-backed custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-sns.html): Learn how to use custom resources and Amazon SNS notifications to invoke custom provisioning logic in CloudFormation.

### [Lambda-backed custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-lambda.html)

Learn how to use custom resources to invoke Lambda functions when you create, update, or delete a stack.

- [Walkthrough: Create a delay mechanism with a Lambda-backed custom resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/walkthrough-lambda-backed-custom-resources.html): Learn how to configure and launch a Lambda-backed custom resource using our sample template.
- [cfn-response module](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-lambda-function-code-cfnresponsemodule.html): Describes a helper module for sending responses to Lambda-backed custom resources in CloudFormation.

### [Template macros](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html)

Learn how to use macros to perform custom processing on templates, from simple actions like find-and-replace operations to extensive transformations of entire templates.

- [Macros overview](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros-overview.html): Learn about macros for CloudFormation stack templates.
- [Create a macro definition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros-author.html): Learn how to create a CloudFormation macro definition.
- [Example simple string replacement macro](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/macros-example.html): Learn how to create a simple macro that inserts a specified string in place of the specified target content in the processed template.
- [Troubleshoot the processed template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros-troubleshoot-processed-template.html): Learn how to resolve issues with macros after the template is processed for CloudFormation stack templates.
- [Nested stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html): Learn how to split large CloudFormation templates into smaller, reusable pieces.
- [Wait conditions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-waitcondition.html): Create a wait condition in a template to coordinate the creation of stack resources or track the progress of a configuration process.

### [Create reusable resource configurations with modules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/modules.html)

Discover how to create reusable resource configurations that can be included across multiple CloudFormation stack templates.

- [Understand module versioning](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/module-versioning.html): Understand how stack operations work when you use different versions of modules.
- [Use modules in a template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/modules-using.html): Discover how to use module in your CloudFormation templates.
- [Use parameters to specify module values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/module-using-params.html): Discover how to use parameters to specify module values in your CloudFormation templates.
- [Reference module resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/module-ref-resources.html): Discover how to reference module resources in your CloudFormation templates.


## [Creating and managing stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html)

- [Create a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html): Learn how to create a stack using a wizard-driven interface from the CloudFormation console.
- [View stack information](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.html): Learn how to view information about your stack from the CloudFormation console.
- [Update your stack template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-get-template.html): Learn how to update the CloudFormation template for your stack.
- [Understand update behaviors of stack resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html): Update an existing CloudFormation stack by submitting a template or input parameters that specify updates to the resources in the stack.

### [Update stacks using change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html)

Learn how to update a CloudFormation stack by executing a change set, so that you can preview the changes CloudFormation will make before you update your stack.

- [Create a change set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets-create.html): Learn how to create a change set for a running CloudFormation stack.
- [View a change set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets-view.html): Learn how to view a change set for a CloudFormation stack.
- [Drift-aware change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/drift-aware-change-sets.html): Use drift-aware change sets to preview and manage the impact of CloudFormation deployments on drifted resources in a safe and predictable manner.
- [Execute a change set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets-execute.html): Learn how to execute a change set for a CloudFormation stack.
- [Delete a change set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets-delete.html): Learn how to delete a change set for a CloudFormation stack.
- [Example change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets-samples.html): Discover example change sets for common CloudFormation stack changes.
- [Change sets for nested stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/change-sets-for-nested-stacks.html): Learn how to use change sets for nested stacks to execute changes to applications modeled with nested stacks.
- [Validate stack deployments](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/validate-stack-deployments.html): Learn how you can identify and resolve potential deployment issues before executing your CloudFormation change sets, with pre-deployment validation.
- [Update stacks directly](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.html): Update a CloudFormation stack directly by submitting a template or input parameters that specify updates to the stack's resources.
- [Cancel a stack update](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-update-cancel.html): Cancel an CloudFormation stack update that is in progress to rollback any changes.

### [Delete a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html)

Delete a running stack by using the CloudFormation console.

- [View deleted stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-view-deleted-stacks.html): Learn how to use the filter status option so that deleted stacks are visible when viewing stacks from the CloudFormation console.

### [Monitor stack progress](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/monitor-stack-progress.html)

Learn how to monitor the progress and status of CloudFormation stack deployments.

- [View stack events](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/view-stack-events.html): Learn how to monitor when resources are being created, updated, or deleted, and whether the stack deployment is proceeding as expected.
- [View stack events by operation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/view-stack-events-by-operation.html): Learn how to view stack events grouped by operation to better understand the sequence and scope of changes made to your stack.
- [View stack deployment timeline graph](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-deployment-timeline-graph.html): Describes the stack deployment timeline graph, which gives a detailed graphical view into the stack deployment process.
- [Understand stack creation events](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-resource-configuration-complete.html): CloudFormation stacks have multiple events that can be used to coordinate resource provisioning.
- [Monitor stack updates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-monitor-stack.html): Monitor the progress of an CloudFormation stack update by viewing its events.
- [Continue rolling back an update](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html): For a stack in the UPDATE_ROLLBACK_FAILED state, fix the error that caused the failure and continue rolling back the update to return the stack to a working state (UPDATE_ROLLBACK_COMPLETE).
- [Determine the cause of a stack failure](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/determine-root-cause-for-stack-failures.html): Learn how to determine the event that's likely the root cause for a stack failure.
- [Stack failure options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-failure-options.html): Discover how to resume provisioning from failure points without rolling back successful resources during iterative application development.
- [Roll back your stack on alarm breach](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-rollback-triggers.html): Discover how to use CloudWatch alarms to monitor stack creation and updating.

### [Detect unmanaged configuration changes to stacks and resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html)

Drift detection enables you to detect whether a stack's actual configuration differs, or has drifted, from its expected configuration.

- [Detect drift on an entire CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/detect-drift-stack.html): Performing a drift detection operation on a stack determines whether the stack has drifted from its expected template configuration, and returns detailed information about the drift status of each resource in the stack that supports drift detection.
- [Detect drift on individual stack resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/detect-drift-resource.html): You can detect drift on specific resources within a stack, rather than the entire stack.
- [Resolve drift with an import operation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-resolve-drift.html): There may be cases where a resource's configuration has drifted from its intended configuration and you want to accept the new configuration as the intended configuration.

### [Import AWS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/import-resources.html)

Discover how to import existing AWS resources into a stack, move resources between stacks, and nest existing stacks using the resource import feature.

### [Manually import AWS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/import-resources-manually.html)

Discover how to manually import existing AWS resources into a stack, move resources between stacks, and nest existing stacks using the resource import feature.

- [Creating a stack from existing resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-new-stack.html): Create a stack from existing AWS resources to bring them into CloudFormation management.
- [Importing existing resources into a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-existing-stack.html): Import an existing AWS resource into a stack to bring it into CloudFormation.
- [Moving resources between stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/refactor-stacks.html): Use the resource import feature to move resources between stacks.
- [Nesting an existing stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-nested-stacks.html): Use the resource import feature to nest existing stacks within a parent stack.
- [Automatically import AWS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/import-resources-automatically.html): Discover how to automatically import existing AWS resources into a stack, move resources between stacks, and nest existing stacks using the resource import feature.
- [Reverting an import operation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-revert.html): Revert an import operation.
- [Stack refactoring](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-refactoring.html): Stack refactoring simplifies stack reorganization, like moving resources between stacks or splitting larger stacks, while maintaining the same properties and data.
- [Resource type support](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html): View a table that lists the AWS resource types that support import, drift detection, and IaC generator operations.
- [Use quick-create links to create CloudFormation stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stacks-quick-create-links.html): Use quick-create links with URL query parameters to simplify stack creation in the CloudFormation console.

### [Example commands for the AWS CLI and PowerShell](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/service_code_examples.html)

Examples of the command syntax to use when creating, updating, and deleting stacks with the AWS CLI and PowerShell.

- [Upload local artifacts to an S3 bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-package.html): Learn how to upload local artifacts that are referenced by a CloudFormation template to an Amazon S3 bucket with the AWS CLI.


## [Managing stacks with StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)

- [StackSets concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html): Describes fundamental StackSets concepts and how they're related.

### [Prerequisites](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html)

Discover how to complete the prerequisites for performing StackSets operations.

- [Enable AWS Regions that are disabled by default](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-opt-in-regions.html): Describes how to enable AWS Regions that are disabled by default.
- [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html): Describes how to create the IAM service roles required by StackSets to deploy across accounts and AWS Regions with self-managed permissions.

### [Activate trusted access](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html)

Describes how to activate trusted access with AWS Organizations to deploy across accounts and AWS Regions using service-managed permissions.

- [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html): Describes how to register a delegated administrator account that can create and manage StackSets with service-managed permissions for an organization.
- [Get started using a sample template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started.html): Walk through the process of creating your first StackSet using a sample template from the AWS Management Console.
- [Create StackSets (self-managed permissions)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create-self-managed.html): Learn how to create StackSets with self-managed permissions using either the CloudFormation console or the AWS CLI.
- [Create StackSets (service-managed permissions)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-associate-stackset-with-org.html): Learn how to create StackSets with service-managed permissions using either the CloudFormation console or the AWS CLI.
- [Enable-disable automatic deployments](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-auto-deployment.html): Learn how to enable and disable automatic deployments for StackSets in AWS Organizations using either the CloudFormation console or AWS CLI.
- [Update StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-update.html): Learn how to update your StackSets using either the CloudFormation console or the AWS CLI.
- [Add stacks to StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stackinstances-create.html): Learn how to add stacks to StackSets using either the CloudFormation console or the AWS CLI.
- [Override parameters on stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stackinstances-override.html): Learn how to override parameters that allow you to change property values in stacks to those specified by the user and not the StackSet itself.
- [Delete stacks from StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stackinstances-delete.html): Learn how to delete stacks from StackSets using either the CloudFormation console or the AWS CLI.
- [Delete StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-delete.html): Learn how to delete StackSets and service roles using either the CloudFormation console or AWS CLI.
- [Target account gates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-account-gating.html): Account gates let you specify a Lambda function to verify target account requirements before CloudFormation begins StackSets operations in that account.
- [Choose the Concurrency Mode](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concurrency-mode.html): Describes the concurrency mode parameter, which allows you to choose how the concurrency level behaves during StackSet operations.
- [Detecting drift on StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html): Describes how to perform drift detection on StackSets.

### [Import stacks into StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-import.html)

Use the stack import operation to import existing stacks into new or existing StackSets to replicate your stacks across multiple Regions and accounts.

- [Self-managed stack import](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/self-managed-import.html): Describes self-managed stack imports into StackSets, which can import stacks in the administrator account or in different target accounts and AWS Regions.
- [Service-managed stack import](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/service-managed-import.html): Describes service-managed stack imports into StackSets, which can import any stack in the same AWS Organizations as the management account.
- [Revert stack imports](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/revert-stackset-import.html): Learn how to revert stack imports into StackSets.
- [Best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-bestpractices.html): Describes the best practices for defining a StackSet template, creating or adding stacks to a StackSet, or updating a StackSet.
- [Sample templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.html): Provides sample CloudFormation templates that can help you use CloudFormation StackSets in your enterprise.
- [Troubleshooting](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-troubleshooting.html): This topic contains some common StackSets issues, and suggested solutions for those issues.


## [Syncing stacks with Git source code](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/git-sync.html)

- [How Git sync works](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/git-sync-concepts-terms.html): Learn how Git sync works and the key concepts required to work with it.
- [Prerequisites](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/git-sync-prereq.html): Learn how to complete the prerequisites for using Git sync to automatically sync stacks with source code stored in a Git repository.
- [Create a stack from repository source code](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/git-sync-create-stack-from-repository-source-code.html): Learn how to use Git sync to create AWS stack deployments from a Git repository.
- [Enable comments on pull requests](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gitsync-enable-comments-on-pull-requests.html): Learn how to enable comments on pull requests so that CloudFormation can post a summary of stack changes in pull requests in your Git repository.
- [Status dashboard](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/git-sync-status.html): Learn how to monitor and edit Git sync deployments with the Git sync status dashboard.


## [Managing extensions with the CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)

- [Concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-concepts.html): Get started with the CloudFormation registry by learning basic terms and concepts.
- [View the available and activated extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-view.html): Discover how to view the available and activated extensions in the CloudFormation registry.

### [Public extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html)

Third-party public extensions are those extensions from third parties that you have activated for use in your AWS account.

- [Activate a public extension](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public-activate-extension.html): Learn how to activate a third-party public extension in the CloudFormation registry so it's available for use in your account.
- [Update a public extension](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public-update-extension-console.html): After you activate a third-party public extension, you can update most extension details from your account.
- [Deactivate public extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public-deactivate-extension.html): Discover how to deactivate a third-party public extension you previously activated in your account.

### [Private extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-private.html)

Third-party private extensions are those extensions from third parties that you have registered for use in your AWS account.

- [Register a private extension](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register-private-extension.html): Learn how to register a third-party private extension that's shared with you so it's available for use in your account.
- [Deregister private extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-private-deregister-extension.html): Discover how to deregister a third-party private extension you previously registered in your account.
- [Edit configuration data for extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-set-configuration.html): Learn how to edit configuration data for extensions in your account within a specific Region.
- [Record resource types in AWS Config](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-config-record.html): Discover how to enable AWS Config to automatically track your private resource types and record configuration changes.


## [Continuous delivery](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline.html)

- [Walkthrough: Building a pipeline for test and production stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-basic-walkthrough.html): Learn how to build a CodePipeline pipeline that automates many CloudFormation actions for a continuous delivery workflow.
- [Configuration properties reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html): Specify CloudFormation-specific configuration properties when you choose CloudFormation as a provider for the CodePipeline Deploy action.
- [CloudFormation artifacts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html): Build an CloudFormation artifact so that CodePipeline can process stacks and change sets in a pipeline.
- [Using parameter override functions with CodePipeline pipelines](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html): Use parameter override functions to specify dynamic values for CloudFormation template parameters in CodePipeline pipelines.


## [Security](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/security.html)

- [Protect stacks from being deleted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html): Prevent a stack from being accidentally deleted by enabling termination protection on the stack.
- [Prevent updates to stack resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html): Prevent stack resources from being unintentionally updated or deleted during a stack update by using CloudFormation stack policies.
- [Data protection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/security-data-protection.html): Learn how the AWS shared responsibility model applies to data protection in CloudFormation.

### [Control access with IAM](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html)

Use AWS Identity and Access Management to control who has access to CloudFormation.

- [Identity-based policy examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify CloudFormation resources.
- [AWS managed policies](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/security-iam-awsmanpol.html): Learn about AWS managed policies for CloudFormation and recent changes to those policies.
- [CloudFormation service role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html): Use an IAM service role to give CloudFormation permission to make calls to resources in a stack on your behalf.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cross-service-confused-deputy-prevention.html): Learn how to prevent cross-service confused deputy issues by using IAM role trust policies to limit the permissions that CloudFormation gives another service.
- [FAS requests and permission evaluation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/fas-requests-and-permission-evaluation.html): Learn how CloudFormation uses Forwarded Access Sessions (FAS) tokens for resource operations, regardless of whether a custom IAM role is provided, and how this impacts permission checks during stack operations.
- [Logging API calls](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-api-logging-cloudtrail.html): Learn about logging CloudFormation API calls with AWS CloudTrail.
- [Infrastructure security](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/infrastructure-security.html): Learn how CloudFormation isolates service traffic.
- [Resilience](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific CloudFormation features for data resiliency.
- [Compliance validation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/vulnerability-analysis-and-management.html): Describes the customer responsibility regarding updates and patches in CloudFormation.
- [Security best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/security-best-practices.html): Describes guidelines and best practices for addressing security issues in CloudFormation.
- [AWS PrivateLink](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/vpc-interface-endpoints.html): You can use AWS PrivateLink to create a private connection between your VPC and CloudFormation.


## [Monitoring with EventBridge](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/eventbridge-integration.html)

- [Creating a custom event pattern](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/eventbridge-using-events-rules-patterns.html): Learn how to create a custom event pattern for an EventBridge rule for CloudFormation and Git sync events.

### [Events detail reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/events-detail-reference.html)

All events from AWS services have a common set of fields containing metadata about the event, such as the AWS service that's the source of the event, the time the event was generated, the account and region in which the event took place, and others.

- [Resource Status Change](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/event-detail-resource-status-change.html): Below are the detail fields for Resource Status Change events.
- [Stack Status Change](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/event-detail-stack-status-change.html): Below are the detail fields for Stack Status Change events.
- [Drift Detection Status Change](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/event-detail-stack-drift-detection-change.html): Below are the detail fields for stack drift detection events.
- [StackSet Status Change](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/event-detail-stackset-status-change.html): Below are the detail fields for StackSet Status Change events.
- [StackSet Stack Instance Status Change](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/event-detail-stackset-stack-instance-status-change.html): Below are the detail fields for StackSet stack instance status events.
- [StackSet Operation Status Change](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/event-detail-stackset-operation-status-change.html): Below are the detail fields for StackSet Operation Status Change events.
- [Repository Sync Status Change](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/event-detail-respository-sync-status-change.html): Below are the detail fields for Repository Sync Status Change events.
- [Resource Sync Status Change](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/event-detail-resource-sync-status-change.html): Below are the detail fields for Resource Sync Status Change events.
