# Source: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/llms.txt

# AWS AppConfig API Reference

## [AWS AppConfig](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/Welcome_Amazon_AppConfig.html)

AWS AppConfig feature flags and dynamic configurations help software builders quickly and securely adjust application behavior in production environments without full code deployments. AWS AppConfig speeds up software release frequency, improves application resiliency, and helps you address emergent issues more quickly. With feature flags, you can gradually release new capabilities to users and measure the impact of those changes before fully deploying the new capabilities to all users. With operational flags and dynamic configurations, you can update block lists, allow lists, throttling limits, logging verbosity, and perform other operational tuning to quickly respond to issues in production environments.

Despite the fact that application configuration content can vary greatly from application to application, AWS AppConfig supports the following use cases, which cover a broad spectrum of customer needs:

- Feature flags and toggles- Safely release new capabilities to your customers in a controlled environment. Instantly roll back changes if you experience a problem.
- Application tuning- Carefully introduce application changes while testing the impact of those changes with users in production environments.
- Allow list or block list- Control access to premium features or instantly block specific users without deploying new code.
- Centralized configuration storage- Keep your configuration data organized and consistent across all of your workloads. You can use AWS AppConfig to deploy configuration data stored in the AWS AppConfig hosted configuration store, AWS Secrets Manager, Systems Manager, Parameter Store, or Amazon S3.

How AWS AppConfig works

This section provides a high-level description of how AWS AppConfig works and how you get started.

This reference is intended to be used with the [AWS AppConfig User Guide](http://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html).

### Actions

- [CreateApplication](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateApplication.html): Creates an application.
- [CreateConfigurationProfile](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateConfigurationProfile.html): Creates a configuration profile, which is information that enables AWS AppConfig to access the configuration source.
- [CreateDeploymentStrategy](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateDeploymentStrategy.html): Creates a deployment strategy that defines important criteria for rolling out your configuration to the designated targets.
- [CreateEnvironment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateEnvironment.html): Creates an environment.
- [CreateExtension](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateExtension.html): Creates an AWS AppConfig extension.
- [CreateExtensionAssociation](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateExtensionAssociation.html): When you create an extension or configure an AWS authored extension, you associate the extension with an AWS AppConfig application, environment, or configuration profile.
- [CreateHostedConfigurationVersion](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.html): Creates a new configuration in the AWS AppConfig hosted configuration store.
- [DeleteApplication](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteApplication.html): Deletes an application.
- [DeleteConfigurationProfile](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteConfigurationProfile.html): Deletes a configuration profile.
- [DeleteDeploymentStrategy](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteDeploymentStrategy.html): Deletes a deployment strategy.
- [DeleteEnvironment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteEnvironment.html): Deletes an environment.
- [DeleteExtension](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteExtension.html): Deletes an AWS AppConfig extension.
- [DeleteExtensionAssociation](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteExtensionAssociation.html): Deletes an extension association.
- [DeleteHostedConfigurationVersion](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteHostedConfigurationVersion.html): Deletes a version of a configuration from the AWS AppConfig hosted configuration store.
- [GetAccountSettings](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetAccountSettings.html): Returns information about the status of the DeletionProtection parameter.
- [GetApplication](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetApplication.html): Retrieves information about an application.
- [GetConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetConfiguration.html): (Deprecated) Retrieves the latest deployed configuration.
- [GetConfigurationProfile](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetConfigurationProfile.html): Retrieves information about a configuration profile.
- [GetDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetDeployment.html): Retrieves information about a configuration deployment.
- [GetDeploymentStrategy](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetDeploymentStrategy.html): Retrieves information about a deployment strategy.
- [GetEnvironment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetEnvironment.html): Retrieves information about an environment.
- [GetExtension](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetExtension.html): Returns information about an AWS AppConfig extension.
- [GetExtensionAssociation](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetExtensionAssociation.html): Returns information about an AWS AppConfig extension association.
- [GetHostedConfigurationVersion](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetHostedConfigurationVersion.html): Retrieves information about a specific configuration version.
- [ListApplications](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListApplications.html): Lists all applications in your AWS account.
- [ListConfigurationProfiles](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListConfigurationProfiles.html): Lists the configuration profiles for an application.
- [ListDeployments](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListDeployments.html): Lists the deployments for an environment in descending deployment number order.
- [ListDeploymentStrategies](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListDeploymentStrategies.html): Lists deployment strategies.
- [ListEnvironments](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListEnvironments.html): Lists the environments for an application.
- [ListExtensionAssociations](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListExtensionAssociations.html): Lists all AWS AppConfig extension associations in the account.
- [ListExtensions](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListExtensions.html): Lists all custom and AWS authored AWS AppConfig extensions in the account.
- [ListHostedConfigurationVersions](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListHostedConfigurationVersions.html): Lists configurations stored in the AWS AppConfig hosted configuration store by version.
- [ListTagsForResource](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListTagsForResource.html): Retrieves the list of key-value tags assigned to the resource.
- [StartDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StartDeployment.html): Starts a deployment.
- [StopDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StopDeployment.html): Stops a deployment.
- [TagResource](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_TagResource.html): Assigns metadata to an AWS AppConfig resource.
- [UntagResource](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UntagResource.html): Deletes a tag key and value from an AWS AppConfig resource.
- [UpdateAccountSettings](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateAccountSettings.html): Updates the value of the DeletionProtection parameter.
- [UpdateApplication](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateApplication.html): Updates an application.
- [UpdateConfigurationProfile](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateConfigurationProfile.html): Updates a configuration profile.
- [UpdateDeploymentStrategy](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateDeploymentStrategy.html): Updates a deployment strategy.
- [UpdateEnvironment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateEnvironment.html): Updates an environment.
- [UpdateExtension](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateExtension.html): Updates an AWS AppConfig extension.
- [UpdateExtensionAssociation](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateExtensionAssociation.html): Updates an association.
- [ValidateConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ValidateConfiguration.html): Uses the validators in a configuration profile to validate a configuration.

### Data Types

- [Action](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Action.html): An action defines the tasks that the extension performs during the AWS AppConfig workflow.
- [ActionInvocation](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ActionInvocation.html): An extension that was invoked as part of a deployment event.
- [Application](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Application.html)
- [AppliedExtension](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_AppliedExtension.html): An extension that was invoked during a deployment.
- [BadRequestDetails](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_BadRequestDetails.html): Detailed information about the input that failed to satisfy the constraints specified by a call.
- [ConfigurationProfileSummary](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ConfigurationProfileSummary.html): A summary of a configuration profile.
- [DeletionProtectionSettings](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeletionProtectionSettings.html): A parameter to configure deletion protection.
- [DeploymentEvent](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeploymentEvent.html): An object that describes a deployment event.
- [DeploymentStrategy](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeploymentStrategy.html)
- [DeploymentSummary](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeploymentSummary.html): Information about the deployment.
- [Environment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Environment.html)
- [ExtensionAssociationSummary](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ExtensionAssociationSummary.html): Information about an association between an extension and an AWS AppConfig resource such as an application, environment, or configuration profile.
- [ExtensionSummary](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ExtensionSummary.html): Information about an extension.
- [HostedConfigurationVersionSummary](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_HostedConfigurationVersionSummary.html): Information about the configuration.
- [InvalidConfigurationDetail](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_InvalidConfigurationDetail.html): Detailed information about the bad request exception error when creating a hosted configuration version.
- [Monitor](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Monitor.html): Amazon CloudWatch alarms to monitor during the deployment process.
- [Parameter](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Parameter.html): A value such as an Amazon Resource Name (ARN) or an Amazon Simple Notification Service topic entered in an extension when invoked.
- [Validator](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Validator.html): A validator provides a syntactic or semantic check to ensure the configuration that you want to deploy functions as intended.

## [AWS AppConfig Data](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/Welcome_AWS_AppConfig_Data.html)

AWS AppConfig Data provides the data plane APIs your application uses to retrieve configuration data. Here's how it works:

Your application retrieves configuration data by first establishing a configuration session using the AWS AppConfig Data API action. Your session's client then makes periodic calls to to check for and retrieve the latest data available.

When calling `StartConfigurationSession`, your code sends the following information:

- Identifiers (ID or name) of an AWS AppConfig application, environment, and configuration profile that the session tracks.
- (Optional) The minimum amount of time the session's client must wait between calls to `GetLatestConfiguration`.

In response, AWS AppConfig provides an `InitialConfigurationToken`to be given to the session's client and used the first time it calls `GetLatestConfiguration`for that session.

When calling `GetLatestConfiguration`, your client code sends the most recent `ConfigurationToken`value it has and receives in response:

- `NextPollConfigurationToken`: the `ConfigurationToken`value to use on the next call to `GetLatestConfiguration`.
- `NextPollIntervalInSeconds`: the duration the client should wait before making its next call to `GetLatestConfiguration`. This duration may vary over the course of the session, so it should be used instead of the value sent on the `StartConfigurationSession`call.
- The configuration: the latest data intended for the session. This may be empty if the client already has the latest version of the configuration.

For more information and to view example AWS CLI commands that show how to retrieve a configuration using the AWS AppConfig Data `StartConfigurationSession`and `GetLatestConfiguration`API actions, see [Retrieving feature flags and configuration data in AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/retrieving-feature-flags.html)in the AWS AppConfig User Guide.

### Actions

- [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html): Retrieves the latest deployed configuration.
- [StartConfigurationSession](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.html): Starts a configuration session used to retrieve a deployed configuration.

### Data Types

- [BadRequestDetails](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_BadRequestDetails.html): Detailed information about the input that failed to satisfy the constraints specified by a call.
- [InvalidParameterDetail](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_InvalidParameterDetail.html): Information about an invalid parameter.

## Common

- [Common Parameters](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/CommonErrors.html)