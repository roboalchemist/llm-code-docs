# Source: https://docs.aws.amazon.com/appconfig/latest/userguide/llms.txt

# AWS AppConfig User Guide

> Use AWS AppConfig, a tool in AWS Systems Manager, to create, manage, and quickly deploy feature flags and other forms of application configuration data. AWS AppConfig supports controlled deployments to applications of any size and includes built-in validation checks and monitoring. You can use AWS AppConfig with applications hosted on Amazon EC2 instances, AWS Lambda, containers, mobile applications, or IoT devices.

- [Security](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-security.html)
- [Document history](https://docs.aws.amazon.com/appconfig/latest/userguide/doc-history.html)

## [What is AWS AppConfig?](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)

- [AWS AppConfig quotas](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-service-quotas.html): You can view information about AWS AppConfig endpoints and service quotas in the Amazon Web Services General Reference.
- [Additional resources](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-additional-resources.html): The following resources can help you learn more about AWS AppConfig.


## [Setting up AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/setting-up-appconfig.html)

- [Understanding IPv6 support](https://docs.aws.amazon.com/appconfig/latest/userguide/setting-up-IPv6.html): Learn how to use IPv6 with AWS AppConfig APIs and understand the endpoints for both control plane and data plane operations.


## [Creating](https://docs.aws.amazon.com/appconfig/latest/userguide/creating-feature-flags-and-configuration-data.html)

- [Understanding the configuration profile IAM role](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile-iam-role.html): Learn about the IAM roles required for AWS AppConfig to access your configuration data from different sources.
- [Creating a namespace](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-namespace.html): Create an application namespace to organize and manage your feature flags and configuration data in AWS AppConfig.
- [Creating environments](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html): Set up deployment environments to manage configuration deployments across different stages of your application lifecycle.

### [Creating a configuration profile in AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile.html)

Create configuration profiles to define the structure and validation requirements for your configuration data.

### [Creating a feature flag configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile-feature-flags.html)

Learn how to create and manage feature flags to control feature availability in your applications.

- [Creating a feature flag configuration profile (console)](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-feature-flag-configuration-create-console.html): Use the AWS AppConfig to create and configure feature flags for your applications with a visual interface.
- [Creating a feature flag configuration profile (command line)](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-feature-flag-configuration-commandline.html): Create and manage feature flags programmatically using the AWS CLI for automation and scripting.

### [Creating multi-variant feature flags](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-multi-variant-feature-flags.html)

Implement multi-variant feature flags to deliver different feature experiences to different user segments.

- [Understanding multi-variant feature flag concepts and common use cases](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-multi-variant-feature-flags-concepts.html): Learn the key concepts of multi-variant feature flags including variants, rules, and targeting.

### [Understanding multi-variant feature flag rules](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-multi-variant-feature-flags-rules.html)

Discover how to create rules for multi-variant feature flags to target specific user segments.

- [Defining rules for multi-variant feature flags](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-multi-variant-feature-flags-rules-operators.html): Explore the operators available for creating powerful targeting rules in multi-variant feature flags.
- [Creating a multi-variant feature flag](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-multi-variant-feature-flags-procedures.html): Follow step-by-step procedures to create and configure multi-variant feature flags for your applications.
- [Understanding the type reference for AWS.AppConfig.FeatureFlags](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-type-reference-feature-flags.html): Review the technical reference for feature flag types, attributes, and constraints in AWS AppConfig.
- [Saving a previous feature flag version to a new version](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile-feature-flags-editing-version.html): Learn how to restore and modify previous feature flag versions by copying them to new versions in AWS AppConfig.

### [Creating a free form configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-free-form-configurations-creating.html)

Create flexible free-form configurations to store and manage custom application settings in AWS AppConfig.

- [Understanding validators](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile-validators.html): Implement validators to ensure your configuration data meets required format and content standards.
- [Understanding configuration store quotas and limitations](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile-quotas.html): Learn about the size limits and quotas for configuration data in AWS AppConfig.
- [Understanding the AWS AppConfig hosted configuration store](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile-about-hosted-store.html): Discover how the AWS AppConfig hosted configuration store provides a simple way to store and manage your configuration data.
- [Understanding configurations stored in Amazon S3](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile-S3-source.html): Configure AWS AppConfig to use configuration data stored in Amazon S3 buckets for your applications.
- [Creating an AWS AppConfig freeform configuration profile (console)](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-free-form-configuration-and-profile-create-console.html): Use the AWS AppConfig console to create and configure free-form configuration profiles for your applications with a visual interface.
- [Creating an AWS AppConfig freeform configuration profile (command line)](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-free-form-configuration-and-profile-create-commandline.html): Create and manage free-form configurations programmatically using the AWS CLI for automation and scripting.
- [Creating a configuration profile for non-native data sources](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile-other-data-sources.html): Integrate AWS AppConfig with other AWS services like Systems Manager Parameter Store and Secrets Manager to manage your configuration data.


## [Deploying](https://docs.aws.amazon.com/appconfig/latest/userguide/deploying-feature-flags.html)

### [Working with deployment strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html)

Learn how to create and manage deployment strategies to safely roll out configuration changes to your applications.

- [Using predefined deployment strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy-predefined.html): Learn about AWS AppConfig's built-in deployment strategies for safely rolling out configuration changes to your applications.
- [Create a deployment strategy](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy-create.html): Learn how to create custom deployment strategies in AWS AppConfig to control how configuration changes are rolled out to your applications.
- [Deploying a configuration](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying.html): Learn how to deploy feature flags and configuration data to your applications using AWS AppConfig deployment strategies.
- [Deploying with CodePipeline](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-codepipeline.html): Discover how to automate AWS AppConfig configuration deployments using AWS CodePipeline for continuous delivery.
- [Reverting a configuration](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying-reverting.html): Learn how to roll back or revert AWS AppConfig configuration deployments using automatic rollbacks and manual reversion options.


## [Retrieving](https://docs.aws.amazon.com/appconfig/latest/userguide/retrieving-feature-flags.html)

- [What is AWS AppConfig Agent?](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent.html): Learn how AWS AppConfig Agent simplifies feature flag and configuration retrieval by providing local caching and automatic updates for your applications.

### [How to use AWS AppConfig Agent to retrieve configuration data](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html)

Configure AWS AppConfig Agent to retrieve and cache configuration data for your applications using environment variables and configuration files.

### [Using AWS AppConfig Agent with AWS Lambda](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions.html)

Implement AWS AppConfig Agent as a Lambda extension to efficiently manage feature flags and configuration data in your Lambda functions.

- [Understanding how the AWS AppConfig Agent Lambda extension works](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions-how-it-works.html): Discover how AWS AppConfig Agent Lambda extension manages configuration data caching and updates during function initialization and execution.
- [Adding the AWS AppConfig Agent Lambda extension](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions-add.html): Add the AWS AppConfig Agent Lambda extension to your function using the Lambda console or AWS CLI.
- [Configuring the AWS AppConfig Agent Lambda extension](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions-config.html): Configure the AWS AppConfig Agent Lambda extension using environment variables to specify application, environment, and configuration settings.
- [Understanding available versions of the AWS AppConfig Agent Lambda extension](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions-versions.html): Select the appropriate AWS AppConfig Agent Lambda extension version based on your runtime requirements and feature needs.
- [Using AWS AppConfig Agent with Amazon EC2 and on-premises machines](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-ec2.html): Deploy AWS AppConfig Agent on Amazon EC2 instances and on-premises servers to manage feature flags and configuration data locally.

### [Using AWS AppConfig Agent with Amazon ECS and Amazon EKS](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent.html)

Implement AWS AppConfig Agent in containerized environments to manage feature flags and configuration data for Amazon ECS and Amazon EKS workloads.

- [Starting the AWS AppConfig agent for Amazon ECS integration](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent-starting-ecs.html): Start AWS AppConfig Agent in your Amazon ECS tasks using container definitions and environment variables.
- [Starting the AWS AppConfig agent for Amazon EKS integration](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent-starting-eks.html): Deploy AWS AppConfig Agent in your Amazon EKS cluster using Kubernetes manifests and configuration settings.
- [(Optional) Running AWS AppConfig as a DaemonSet in Amazon EKS](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent-daemon.html): Configure AWS AppConfig Agent as a daemon service to share configuration data across multiple containers in your cluster.
- [(Optional) Using environment variables to configure AWS AppConfig Agent for Amazon ECS and Amazon EKS](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent-configuring.html): Customize AWS AppConfig Agent behavior in containerized environments using environment variables and configuration files.
- [Retrieving configuration data for applications running in Amazon ECS and Amazon EKS](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent-retrieving-data.html): Access configuration data from AWS AppConfig Agent in your containerized applications using HTTP endpoints.
- [Retrieving feature flags](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-retrieving-feature-flags.html): Retrieve feature flag configurations using AWS AppConfig Agent's specialized endpoints for flag evaluation and management.

### [Using a manifest to enable additional retrieval features](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use-additional-features.html)

Enable advanced AWS AppConfig Agent features using manifest files to customize configuration retrieval and caching behavior.

- [Configuring AWS AppConfig Agent to retrieve configurations from multiple accounts](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use-additional-features-multi-account.html): Configure AWS AppConfig Agent to retrieve configuration data from multiple AWS accounts using cross-account roles.
- [Configuring AWS AppConfig Agent to write configuration copies to disk](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use-additional-features-write-to-disk.html): Set up AWS AppConfig Agent to persist configuration data to disk for backup and offline access scenarios.
- [Generating a client using the OpenAPI specification](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-OpenAPI.html): Generate client libraries for AWS AppConfig configuration retrieval using the OpenAPI specification and tools.

### [Working with AWS AppConfig Agent local development mode](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use-local-development.html)

Set up AWS AppConfig Agent in local development environments to test feature flags and configuration changes.

- [Samples for local development mode](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use-local-development-samples.html): Explore sample configurations and code examples for testing feature flags with AWS AppConfig Agent in local environments.
- [Browser and mobile use considerations](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-mobile.html): Implement AWS AppConfig configuration retrieval in browser-based and mobile applications using AWS SDKs.
- [Retrieving configuration data without AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/about-data-plane.html): Access AWS AppConfig configuration data directly using API calls when AWS AppConfig Agent integration is not suitable for your use case.


## [Extending AWS AppConfig workflows](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)

- [Understanding AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-about.html): Learn about AWS AppConfig extension concepts and how they help you add custom logic to your configuration deployment workflows.

### [Working with AWS authored extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-about-predefined.html)

Learn how to use built-in AWS AppConfig extensions to integrate with AWS services like Amazon EventBridge, Amazon SNS, and Amazon SQS.

- [Using the AWS AppConfig deployment events to Amazon EventBridge extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-about-predefined-notification-eventbridge.html): Monitor and respond to AWS AppConfig configuration deployments by sending notifications to Amazon EventBridge.
- [Using the AWS AppConfig deployment events to Amazon SNS extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-about-predefined-notification-sns.html): Send notifications to Amazon SNS topics when AWS AppConfig configurations are deployed, enabling automated monitoring and response workflows.
- [Using the AWS AppConfig deployment events to Amazon SQS extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-about-predefined-notification-sqs.html): Configure the AWS AppConfig deployment events to Amazon SQS extension to receive notifications about configuration deployments in your Amazon SQS queues.
- [Using the Jira extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-about-jira.html): Automatically create issues in the Atlassian Jira console when you make changes to an AWS AppConfig feature flag.

### [Walkthrough: Creating custom AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-creating-custom.html)

Learn how to create custom AWS AppConfig extensions to automate configuration management tasks and integrate with external services.

- [Step 1: Create a Lambda function for a custom AWS AppConfig extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-creating-custom-lambda.html): Create a Lambda function to define the custom processing logic for your AWS AppConfig extension.
- [Step 2: Configure permissions for a custom AWS AppConfig extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-creating-custom-permissions.html): Set up IAM permissions to allow AWS AppConfig to invoke your extension's Lambda function.

### [Step 3: Create a custom AWS AppConfig extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-creating-custom-extensions.html)

Define your custom AWS AppConfig extension by specifying its actions, parameters, and integration with your Lambda function.

- [Customizing AWS authored notification extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-creating-custom-notification.html): Learn how to customize AWS authored notification extensions to modify their action points and notification behavior.
- [Step 4: Create an extension association for a custom AWS AppConfig extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-creating-custom-association.html): Connect your custom extension to AWS AppConfig resources by creating an extension association.


## [Code samples](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-code-samples.html)

- [Creating or updating a freeform configuration stored in the hosted configuration store](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-code-samples-creating-freeform.html): Create freeform configurations in the AWS AppConfig hosted configuration store using code samples.
- [Creating a configuration profile for a secret stored in Secrets Manager](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-code-samples-secrets-manager.html): Create configuration profiles that reference secrets stored in AWS Secrets Manager using code samples.
- [Deploying a configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-code-samples-deploying.html): Deploy configuration profiles to environments using AWS AppConfig deployment strategies with code samples.
- [Using AWS AppConfig Agent to read a freeform configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-code-samples-agent-read-configuration.html): Retrieve freeform configuration data using AWS AppConfig Agent with code samples.
- [Using AWS AppConfig Agent to read a specific feature flag](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-code-samples-agent-read-feature-flag.html): Retrieve individual feature flag values using AWS AppConfig Agent with code samples.
- [Using AWS AppConfig Agent to retrieve a feature flag with variants](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-code-samples-agent-read-feature-flag-with-variants.html): Retrieve feature flags with variants using context headers and AWS AppConfig Agent with code samples.
- [Using the GetLatestConfiguration API action to read a freeform configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-code-samples-using-API-read-configuration.html): Retrieve configuration data directly using AWS AppConfig Data APIs with code samples.
- [Cleaning up your environment](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-code-samples-clean-up.html): Delete AWS AppConfig resources created during testing using cleanup code samples.


## [Deletion protection](https://docs.aws.amazon.com/appconfig/latest/userguide/deletion-protection.html)

- [Bypassing or forcing a deletion protection check](https://docs.aws.amazon.com/appconfig/latest/userguide/deletion-protection-check.html): Learn how to bypass or force deletion protection checks when managing AWS AppConfig environments and configuration profiles.


## [Monitoring](https://docs.aws.amazon.com/appconfig/latest/userguide/monitoring-overview.html)

- [CloudTrail logs](https://docs.aws.amazon.com/appconfig/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS AppConfig with AWS CloudTrail.
- [Logging metrics for AWS AppConfig data plane calls](https://docs.aws.amazon.com/appconfig/latest/userguide/monitoring-data-plane-call-logging.html): Learn how to enable and configure Amazon CloudWatch Logs to log metrics for AWS AppConfig data plane calls and create metric filters for monitoring API usage.
- [Monitoring deployments for automatic rollback](https://docs.aws.amazon.com/appconfig/latest/userguide/monitoring-deployments.html): Learn how to configure AWS AppConfig to automatically roll back deployments when Amazon CloudWatch alarms detect application issues during configuration changes.
