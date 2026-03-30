# Source: https://docs.aws.amazon.com/imagebuilder/latest/userguide/llms.txt

# EC2 Image Builder User Guide

> EC2 Image Builder is a fully managed AWS service that makes it more efficient to automate creating, managing, and deploying customized, secure, and up-to-date server images that are pre-installed and pre-configured with software and settings to meet specific IT standards.

- [Get set up](https://docs.aws.amazon.com/imagebuilder/latest/userguide/set-up-ib-env.html)
- [Tag resources](https://docs.aws.amazon.com/imagebuilder/latest/userguide/tag-resources.html)
- [Delete resources](https://docs.aws.amazon.com/imagebuilder/latest/userguide/delete-resources.html)
- [Troubleshoot Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/imagebuilder/latest/userguide/doc-history.html)

## [What is Image Builder?](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html)

- [How Image Builder works](https://docs.aws.amazon.com/imagebuilder/latest/userguide/how-image-builder-works.html): Overview of how Image Builder works to create a custom machine image.
- [Semantic versioning](https://docs.aws.amazon.com/imagebuilder/latest/userguide/ibhow-semantic-versioning.html): Image Builder uses semantic versioning to organize resources and ensure that they have unique IDs.


## [Image Builder tutorials](https://docs.aws.amazon.com/imagebuilder/latest/userguide/ib-tutorials.html)

- [Pipeline wizard: Create AMI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-image-pipeline.html): Create an image pipeline with AMI output from the Image Builder console wizard, and build your first image.
- [Pipeline wizard: Create container image](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-container-pipeline.html): Create an image pipeline with an output Docker container image from the Image Builder console wizard, and build your first image.
- [Custom component with parameters](https://docs.aws.amazon.com/imagebuilder/latest/userguide/tutorial-component-parameters.html): Create and use Image Builder components that have parameters that can be set to custom values by Image Builder recipes.
- [Use a base image parameter in your recipe](https://docs.aws.amazon.com/imagebuilder/latest/userguide/tutorial-ssm-parameters-recipe.html): Use AWS Systems Manager Parameter Store parameters in your EC2 Image Builder recipes and image distribution to maintain dynamic, secure, and centrally managed image building processes.


## [Components](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-components.html)

- [List and view components](https://docs.aws.amazon.com/imagebuilder/latest/userguide/component-details.html): List and view Image Builder component details.
- [Use AWS Marketplace components](https://docs.aws.amazon.com/imagebuilder/latest/userguide/use-marketplace-components.html): Learn about and subscribe to AWS Marketplace components that you can use to to customize your EC2 Image Builder image.

### [Use managed components](https://docs.aws.amazon.com/imagebuilder/latest/userguide/use-managed-components.html)

Use Amazon managed components to customize your EC2 Image Builder image.

- [Distributor package Windows application install](https://docs.aws.amazon.com/imagebuilder/latest/userguide/mgdcomponent-distributor-win.html): Use Distributor package managed components to install application packages for your Image Builder Windows images with the Systems Manager Distributor capability.
- [CIS hardening](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-cis.html): Use CIS hardening components to ensure that Image Builder images meet compliance standards.
- [STIG hardening components](https://docs.aws.amazon.com/imagebuilder/latest/userguide/ib-stig.html): Describes the Amazon managed Image Builder STIG components, and system-specific lists of the settings that the component applies to the Amazon EC2 build instance during image creation.

### [Develop custom components](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-custom-components.html)

Develop custom components for your Image Builder image

- [Create a YAML component document](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-component-yaml.html): Create a YAML component document to use when you create a custom component for your Image Builder image.
- [Create custom components with Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-component.html): Create a custom component from EC2 Image Builder to build or test your images.

### [AWSTOE component manager application](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-component-manager.html)

How Image Builder uses the AWSTOE component manager application to orchestrate workflows, modify system configurations, and test your images.

### [Manual set up](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-get-started.html)

Manually install and set up the AWSTOE application to develop custom components for image configuration and testing.

- [Verify signature](https://docs.aws.amazon.com/imagebuilder/latest/userguide/awstoe-verify-sig.html): Verify the signature of the AWSTOE installation download

### [Use the component document framework](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-use-documents.html)

Use YAML component documents with AWS Task Orchestrator and Executor component document framework to create custom components that you can use to build AMIs and container images.

- [Variables](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-user-defined-variables.html): Define variables, including input parameters and constants for the YAML or JSON component document that defines your custom component.
- [Conditional constructs](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-conditional-constructs.html): Use conditional constructs, such as the "if" construct in AWS Task Orchestrator and Executor component documents to conditionally control the document flow.
- [Comparison operators](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-comparison-operators.html): Learn how to use comparison operators in AWS Task Orchestrator and Executor component documents.
- [Logical operators](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-logical-operators.html): Learn how to use logical operators in AWS Task Orchestrator and Executor component documents.
- [Looping constructs](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-looping-constructs.html): Learn how to use looping constructs and reference iteration variables in AWSTOE component documents.
- [Action modules](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-action-modules.html): Describes the features of commonly used AWSTOE action modules, and how to configure them, including examples.
- [Configure input](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-run-config-input.html): Configure command parameters and options for the AWSTOE run command in a file, to streamline command line input.


## [Image resources](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-images.html)

- [List images and build versions](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-details-list.html): List EC2 Image Builder images and build versions.
- [View image resource details](https://docs.aws.amazon.com/imagebuilder/latest/userguide/view-image-details.html): View EC2 Image Builder image resource details.
- [Create custom images with Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-images.html): Create Image Builder custom images.
- [Import and export VM images](https://docs.aws.amazon.com/imagebuilder/latest/userguide/vm-import-export.html): Import and export virtual machines (VMs), and use them to create custom images with Image Builder.
- [Import ISO disk images](https://docs.aws.amazon.com/imagebuilder/latest/userguide/import-iso-disk.html): Import an image from a verified Windows ISO disk file, and use it to create an Amazon Machine Image (AMI) with Image Builder.
- [Manage security findings](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-security-findings.html): Activate Amazon Inspector scans and manage vulnerability findings in EC2 Image Builder.


## [Manage image lifecycle](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-image-lifecycles.html)

- [Prerequisites](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-lifecycle-prerequisites.html): Prerequisites for EC2 Image Builder image lifecycle management.
- [List lifecycle policies](https://docs.aws.amazon.com/imagebuilder/latest/userguide/list-lifecycle-policies.html): List EC2 Image Builder image lifecycle management policies.
- [View lifecycle policies](https://docs.aws.amazon.com/imagebuilder/latest/userguide/view-lifecycle-policy.html): View EC2 Image Builder lifecycle management policies.
- [Create lifecycle policies](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-lifecycle-policies.html): Create EC2 Image Builder lifecycle management policies.
- [How lifecycle rules work](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-lifecycle-rules.html): How lifecycle rules work for EC2 Image Builder image resources.


## [Configure custom images](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-resources.html)

### [Recipes](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-recipes.html)

Manage Image Builder image and container recipes.

- [List and view image recipes](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-recipe-details.html): List and view EC2 Image Builder image recipe details.
- [List and view container recipes](https://docs.aws.amazon.com/imagebuilder/latest/userguide/container-recipe-details.html): List and view EC2 Image Builder container recipe details.
- [Create a new version of an image recipe](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-image-recipes.html): Create a new version of an Image Builder image recipe.
- [Create a new version of a container recipe](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-container-recipes.html): Create a new version of an EC2 Image Builder container recipe.

### [Infrastructure configurations](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-infra-config.html)

Manage Image Builder infrastructure configuration using the AWS Management Console, or Image Builder commands in the AWS CLI.

- [List and view infrastructure configurations](https://docs.aws.amazon.com/imagebuilder/latest/userguide/infra-config-details.html): List and view EC2 Image Builder infrastructure configuration resource details.
- [Create an infrastructure configuration](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-infra-config.html): Create an EC2 Image Builder infrastructure configuration resource.
- [Update an infrastructure configuration](https://docs.aws.amazon.com/imagebuilder/latest/userguide/update-infra-config.html): Update an EC2 Image Builder infrastructure configuration resource.
- [AWS PrivateLink VPC endpoints](https://docs.aws.amazon.com/imagebuilder/latest/userguide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Image Builder without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.

### [Distribution settings](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-distribution-settings.html)

Manage Image Builder distribution settings from the console, or AWS CLI.

- [List and view distribution configurations](https://docs.aws.amazon.com/imagebuilder/latest/userguide/distribution-settings-detail.html): List and view EC2 Image Builder distribution configuration detail.
- [Create and update AMI distribution](https://docs.aws.amazon.com/imagebuilder/latest/userguide/cr-upd-ami-distribution-settings.html): Create and update distribution configurations for EC2 Image Builder AMIs.
- [Create and update container image distribution](https://docs.aws.amazon.com/imagebuilder/latest/userguide/cr-upd-container-distribution-settings.html): Create and update EC2 Image Builder distribution settings for container images.
- [Set up cross-account AMI distribution](https://docs.aws.amazon.com/imagebuilder/latest/userguide/cross-account-dist.html): Distribute an AMI created with Image Builder to other accounts using the AWS CLI.
- [Specify an AMI launch template](https://docs.aws.amazon.com/imagebuilder/latest/userguide/dist-using-launch-template.html): Configure your Image Builder AMI distribution settings to use an Amazon EC2 launch template.
- [Use enhanced AMI distribution](https://docs.aws.amazon.com/imagebuilder/latest/userguide/distribution-enhanced_functionality.html): Leverage enhanced Image Builder AMI distribution capabilities.


## [Share resources](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-shared-resources.html)

- [Create a resource share](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-shared-resources-share.html): Create an AWS RAM resource share to hold the Image Builder resources that you want to share.
- [Unshare a resource](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-shared-resources-unshare.html): Unshare a previously shared Image Builder resource from an AWS RAM resource share.


## [Image workflows](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-image-workflows.html)

- [List image workflows](https://docs.aws.amazon.com/imagebuilder/latest/userguide/list-image-workflows.html): List EC2 Image Builder image workflows.
- [Create an image workflow](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-workflow-create-resource.html): Create an image workflow resource to control build and test stages for the images that EC2 Image Builder creates in your account.

### [Create a YAML workflow document](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-workflow-create-document.html)

Create a YAML workflow document for your EC2 Image Builder image pipelines.

- [Step actions](https://docs.aws.amazon.com/imagebuilder/latest/userguide/wfdoc-step-actions.html): Use supported step actions in for your Image Builder YAML workflow document.
- [Dynamic variables](https://docs.aws.amazon.com/imagebuilder/latest/userguide/wfdoc-dynamic-vars.html): Use dynamic variables in your Image Builder YAML workflow document to perform string interpolation with JSONPath expressions.
- [Conditional statements](https://docs.aws.amazon.com/imagebuilder/latest/userguide/wfdoc-conditional-statements.html): Use conditional statements in your image workflow steps.


## [Manage pipelines](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-pipelines.html)

### [Configure pipeline execution](https://docs.aws.amazon.com/imagebuilder/latest/userguide/schedule-pipeline.html)

Configure the Image Builder image pipeline execution settings, including the build schedule, dependency settings, and logging.

- [Run pipeline manually](https://docs.aws.amazon.com/imagebuilder/latest/userguide/pipelines-run.html): Manually run your EC2 Image Builder pipeline.
- [Use cron expressions](https://docs.aws.amazon.com/imagebuilder/latest/userguide/cron-expressions.html): learn how Image Builder uses cron expressions to set the schedule for refreshing images with updates to the base image AMI and components.
- [List and view pipelines](https://docs.aws.amazon.com/imagebuilder/latest/userguide/pipeline-details.html): List and view EC2 Image Builder image pipeline details.

### [Create and update pipelines (AMI)](https://docs.aws.amazon.com/imagebuilder/latest/userguide/ami-image-pipelines.html)

Create and update Image Builder AMI image pipelines.

- [Create AMI pipeline from the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/cli-create-image-pipeline.html): Use the AWS CLI to define an Image Builder image pipeline that creates an output AMI.
- [Update pipeline from the console](https://docs.aws.amazon.com/imagebuilder/latest/userguide/update-image-pipeline-console.html): Use the AWS Management Console to define an Image Builder image pipeline that creates an output AMI.
- [Update pipeline from the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/cli-update-image-pipeline.html): Use the AWS CLI to update an Image Builder image pipeline that creates an output AMI.

### [Create and update pipelines (container)](https://docs.aws.amazon.com/imagebuilder/latest/userguide/container-image-pipelines.html)

Create and update EC2 Image Builder container image pipelines.

- [Create pipeline from the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/cli-create-container-pipeline.html): Use the AWS CLI to define an Image Builder image pipeline that creates an output container image.
- [Update pipeline from the console](https://docs.aws.amazon.com/imagebuilder/latest/userguide/update-container-pipeline-console.html): Use the AWS Management Console to define an EC2 Image Builder image pipeline that creates an output container image.
- [Update pipeline from the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/cli-update-container-pipeline.html): Use the AWS CLI to update an EC2 Image Builder image pipeline that creates an output container image.
- [Configure pipeline workflows](https://docs.aws.amazon.com/imagebuilder/latest/userguide/pipeline-workflows.html): Configure image workflows for your Image Builder pipelines.
- [Use EventBridge rules](https://docs.aws.amazon.com/imagebuilder/latest/userguide/ev-rules-for-pipeline.html): Use Amazon EventBridge with EC2 Image Builder to automate Image Builder workflows.


## [Integrate products and services](https://docs.aws.amazon.com/imagebuilder/latest/userguide/integrate-products-services.html)

- [Amazon EventBridge](https://docs.aws.amazon.com/imagebuilder/latest/userguide/integ-eventbridge.html): You can configure the Amazon EventBridge serverless event bus service to track and respond to event notifications from Image Builder and related services.
- [Amazon Inspector](https://docs.aws.amazon.com/imagebuilder/latest/userguide/integ-inspector.html): Image Builder integrates with Amazon Inspector to identify vulnerabilities in your Image Builder images.
- [AWS Marketplace](https://docs.aws.amazon.com/imagebuilder/latest/userguide/integ-marketplace.html): Find and subscribe to AWS Marketplace image products directly from EC2 Image Builder.
- [Amazon Simple Notification Service](https://docs.aws.amazon.com/imagebuilder/latest/userguide/integ-sns.html): Configure Image Builder to send detailed image build action messages to an Amazon SNS topic.
- [Compliance products](https://docs.aws.amazon.com/imagebuilder/latest/userguide/integ-compliance-products.html): Build compliance into your Image Builder images with components available from Image Builder and AWS Marketplace.


## [Monitor events and logs](https://docs.aws.amazon.com/imagebuilder/latest/userguide/monitor.html)

- [CloudTrail logs](https://docs.aws.amazon.com/imagebuilder/latest/userguide/log-cloudtrail.html): Log Image Builder API calls in CloudTrail.
- [CloudWatch Logs](https://docs.aws.amazon.com/imagebuilder/latest/userguide/monitor-cwlogs.html): Monitor, store, and access your Image Builder log files with Amazon CloudWatch Logs.


## [Security in Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-security.html)

- [Data protection](https://docs.aws.amazon.com/imagebuilder/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Image Builder.

### [Identity and Access Management](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security-iam.html)

Learn how Image Builder integrates with AWS Identity and Access Management (IAM) to manage access and authentication.

- [How Image Builder works with IAM policies and roles](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security_iam_service-with-iam.html): Learn how Image Builder works with IAM policies and roles.
- [Manage data perimeters](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security-iam-data-perimeter.html): Manage data perimeters for S3 buckets that contain downloadable resources for Image Builder.
- [Identity-Based Policies](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security-iam-identity-based-policies.html): Use identity-based policies with Image Builder.
- [Managed policies](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security-iam-awsmanpol.html): Use AWS managed policies for EC2 Image Builder and review recent changes to those policies.
- [Service-linked roles](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-service-linked-role.html): Learn how Image Builder uses IAM service-linked roles.
- [Troubleshooting](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security_iam_troubleshoot.html): Troubleshoot AWS Identity and Access Management issues in Image Builder.
- [Compliance validation](https://docs.aws.amazon.com/imagebuilder/latest/userguide/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/imagebuilder/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Image Builder features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/imagebuilder/latest/userguide/infrastructure-security.html): Learn how Image Builder implements infrastructure security.
- [Patch management](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security-patch-management.html): Learn how to keep Image Builder and related assets up to date.
- [Best practices](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security-best-practices.html): Best practices for using Image Builder
