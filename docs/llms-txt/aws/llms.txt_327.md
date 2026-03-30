# Source: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/llms.txt

# AWS Elastic Beanstalk API Reference

> Get formal descriptions of all the API operations for AWS Elastic Beanstalk. In addition, find sample requests, responses, and errors for the supported web services protocols.

- [Welcome](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_Operations.html)

- [AbortEnvironmentUpdate](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_AbortEnvironmentUpdate.html): Cancels in-progress environment configuration update or application version deployment.
- [ApplyEnvironmentManagedAction](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplyEnvironmentManagedAction.html): Applies a scheduled managed action immediately.
- [AssociateEnvironmentOperationsRole](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_AssociateEnvironmentOperationsRole.html)
- [CheckDNSAvailability](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CheckDNSAvailability.html): Checks if the specified CNAME is available.
- [ComposeEnvironments](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ComposeEnvironments.html): Create or update a group of environments that each run a separate component of a single application.
- [CreateApplication](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplication.html): Creates an application that has one configuration template named default and no application versions.
- [CreateApplicationVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplicationVersion.html): Creates an application version for the specified application.
- [CreateConfigurationTemplate](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateConfigurationTemplate.html): Creates an AWS Elastic Beanstalk configuration template, associated with a specific Elastic Beanstalk application.
- [CreateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateEnvironment.html): Launches an AWS Elastic Beanstalk environment for the specified application using the specified configuration.
- [CreatePlatformVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreatePlatformVersion.html): Create a new version of your custom platform.
- [CreateStorageLocation](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateStorageLocation.html): Creates a bucket in Amazon S3 to store application versions, logs, and other files used by Elastic Beanstalk environments.
- [DeleteApplication](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteApplication.html): Deletes the specified application along with all associated versions and configurations.
- [DeleteApplicationVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteApplicationVersion.html): Deletes the specified version from the specified application.
- [DeleteConfigurationTemplate](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteConfigurationTemplate.html): Deletes the specified configuration template.
- [DeleteEnvironmentConfiguration](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteEnvironmentConfiguration.html): Deletes the draft configuration associated with the running environment.
- [DeletePlatformVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeletePlatformVersion.html): Deletes the specified version of a custom platform.
- [DescribeAccountAttributes](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeAccountAttributes.html): Returns attributes related to AWS Elastic Beanstalk that are associated with the calling AWS account.
- [DescribeApplications](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplications.html): Returns the descriptions of existing applications.
- [DescribeApplicationVersions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplicationVersions.html): Retrieve a list of application versions.
- [DescribeConfigurationOptions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationOptions.html): Describes the configuration options that are used in a particular configuration template or environment, or that a specified solution stack defines.
- [DescribeConfigurationSettings](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationSettings.html): Returns a description of the settings for the specified configuration set, that is, either a configuration template or the configuration set associated with a running environment.
- [DescribeEnvironmentHealth](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentHealth.html): Returns information about the overall health of the specified environment.
- [DescribeEnvironmentManagedActionHistory](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentManagedActionHistory.html): Lists an environment's completed and failed managed actions.
- [DescribeEnvironmentManagedActions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentManagedActions.html): Lists an environment's upcoming and in-progress managed actions.
- [DescribeEnvironmentResources](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentResources.html): Returns AWS resources for this environment.
- [DescribeEnvironments](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html): Returns descriptions for existing environments.
- [DescribeEvents](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEvents.html): Returns list of event descriptions matching criteria up to the last 6 weeks.
- [DescribeInstancesHealth](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeInstancesHealth.html): Retrieves detailed information about the health of instances in your AWS Elastic Beanstalk environments.
- [DescribePlatformVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribePlatformVersion.html): Describes a platform version.
- [DisassociateEnvironmentOperationsRole](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DisassociateEnvironmentOperationsRole.html)
- [ListAvailableSolutionStacks](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html): Returns a list of the available solution stack names, with the public version first and then in reverse chronological order.
- [ListPlatformBranches](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformBranches.html): Lists the platform branches available for your account in an AWS Region.
- [ListPlatformVersions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformVersions.html): Lists the platform versions available for your account in an AWS Region.
- [ListTagsForResource](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListTagsForResource.html): Return the tags applied to an AWS Elastic Beanstalk resource.
- [RebuildEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RebuildEnvironment.html): Deletes and recreates all of the AWS resources (for example: the Auto Scaling group, load balancer, etc.) for a specified environment and forces a restart.
- [RequestEnvironmentInfo](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RequestEnvironmentInfo.html): Initiates a request to compile the specified type of information of the deployed environment.
- [RestartAppServer](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RestartAppServer.html): Causes the environment to restart the application container server running on each Amazon EC2 instance.
- [RetrieveEnvironmentInfo](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RetrieveEnvironmentInfo.html): Retrieves the compiled information from a request.
- [SwapEnvironmentCNAMEs](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SwapEnvironmentCNAMEs.html): Swaps the CNAMEs of two environments.
- [TerminateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_TerminateEnvironment.html): Terminates the specified environment.
- [UpdateApplication](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplication.html): Updates the specified application to have the specified properties.
- [UpdateApplicationResourceLifecycle](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplicationResourceLifecycle.html): Modifies lifecycle settings for an application.
- [UpdateApplicationVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplicationVersion.html): Updates the specified application version to have the specified properties.
- [UpdateConfigurationTemplate](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateConfigurationTemplate.html): Updates the specified configuration template to have the specified properties or configuration option values.
- [UpdateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateEnvironment.html): Updates the environment description, deploys a new application version, updates the configuration settings to an entirely new configuration template, or updates select configuration option values in the running environment.
- [UpdateTagsForResource](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html): Update the list of tags applied to an AWS Elastic Beanstalk resource.
- [ValidateConfigurationSettings](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ValidateConfigurationSettings.html): Takes a set of configuration settings and either a configuration template or environment, and determines whether those values are valid.


## [Data Types](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_Types.html)

- [ApplicationDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplicationDescription.html): Describes the properties of an application.
- [ApplicationMetrics](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplicationMetrics.html): Application request metrics for an AWS Elastic Beanstalk environment.
- [ApplicationResourceLifecycleConfig](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplicationResourceLifecycleConfig.html): The resource lifecycle configuration for an application.
- [ApplicationVersionDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplicationVersionDescription.html): Describes the properties of an application version.
- [ApplicationVersionLifecycleConfig](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplicationVersionLifecycleConfig.html): The application version lifecycle settings for an application.
- [AutoScalingGroup](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_AutoScalingGroup.html): Describes an Auto Scaling launch configuration.
- [BuildConfiguration](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_BuildConfiguration.html): Settings for an AWS CodeBuild build.
- [Builder](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_Builder.html): The builder used to build the custom platform.
- [ConfigurationOptionDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ConfigurationOptionDescription.html): Describes the possible values for a configuration option.
- [ConfigurationOptionSetting](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ConfigurationOptionSetting.html): A specification identifying an individual configuration option along with its current value.
- [ConfigurationSettingsDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ConfigurationSettingsDescription.html): Describes the settings for a configuration set.
- [CPUUtilization](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CPUUtilization.html): CPU utilization metrics for an instance.
- [CustomAmi](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CustomAmi.html): A custom AMI available to platforms.
- [Deployment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_Deployment.html): Information about an application version deployment.
- [EnvironmentDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EnvironmentDescription.html): Describes the properties of an environment.
- [EnvironmentInfoDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EnvironmentInfoDescription.html): The information retrieved from the Amazon EC2 instances.
- [EnvironmentLink](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EnvironmentLink.html): A link to another environment, defined in the environment's manifest.
- [EnvironmentResourceDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EnvironmentResourceDescription.html): Describes the AWS resources in use by this environment.
- [EnvironmentResourcesDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EnvironmentResourcesDescription.html): Describes the AWS resources in use by this environment.
- [EnvironmentTier](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EnvironmentTier.html): Describes the properties of an environment tier
- [EventDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EventDescription.html): Describes an event.
- [Instance](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_Instance.html): The description of an Amazon EC2 instance.
- [InstanceHealthSummary](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_InstanceHealthSummary.html): Represents summary information about the health of an instance.
- [Latency](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_Latency.html): Represents the average latency for the slowest X percent of requests over the last 10 seconds.
- [LaunchConfiguration](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_LaunchConfiguration.html): Describes an Auto Scaling launch configuration.
- [LaunchTemplate](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_LaunchTemplate.html): Describes an Amazon EC2 launch template.
- [Listener](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_Listener.html): Describes the properties of a Listener for the LoadBalancer.
- [LoadBalancer](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_LoadBalancer.html): Describes a LoadBalancer.
- [LoadBalancerDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_LoadBalancerDescription.html): Describes the details of a LoadBalancer.
- [ManagedAction](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ManagedAction.html): The record of an upcoming or in-progress managed action.
- [ManagedActionHistoryItem](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ManagedActionHistoryItem.html): The record of a completed or failed managed action.
- [MaxAgeRule](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_MaxAgeRule.html): A lifecycle rule that deletes application versions after the specified number of days.
- [MaxCountRule](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_MaxCountRule.html): A lifecycle rule that deletes the oldest application version when the maximum count is exceeded.
- [OptionRestrictionRegex](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_OptionRestrictionRegex.html): A regular expression representing a restriction on a string configuration option value.
- [OptionSpecification](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_OptionSpecification.html): A specification identifying an individual configuration option.
- [PlatformBranchSummary](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_PlatformBranchSummary.html): Summary information about a platform branch.
- [PlatformDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_PlatformDescription.html): Detailed information about a platform version.
- [PlatformFilter](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_PlatformFilter.html): Describes criteria to restrict the results when listing platform versions.
- [PlatformFramework](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_PlatformFramework.html): A framework supported by the platform.
- [PlatformProgrammingLanguage](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_PlatformProgrammingLanguage.html): A programming language supported by the platform.
- [PlatformSummary](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_PlatformSummary.html): Summary information about a platform version.
- [Queue](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_Queue.html): Describes a queue.
- [ResourceQuota](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ResourceQuota.html): The AWS Elastic Beanstalk quota information for a single resource type in an AWS account.
- [ResourceQuotas](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ResourceQuotas.html): A set of per-resource AWS Elastic Beanstalk quotas associated with an AWS account.
- [S3Location](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_S3Location.html): The bucket and key of an item stored in Amazon S3.
- [SearchFilter](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SearchFilter.html): Describes criteria to restrict a list of results.
- [SingleInstanceHealth](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SingleInstanceHealth.html): Detailed health information about an Amazon EC2 instance in your Elastic Beanstalk environment.
- [SolutionStackDescription](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SolutionStackDescription.html): Describes the solution stack.
- [SourceBuildInformation](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SourceBuildInformation.html): Location of the source code for an application version.
- [SourceConfiguration](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SourceConfiguration.html): A specification for an environment configuration.
- [StatusCodes](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_StatusCodes.html): Represents the percentage of requests over the last 10 seconds that resulted in each type of status code response.
- [SystemStatus](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SystemStatus.html): CPU utilization and load average metrics for an Amazon EC2 instance.
- [Tag](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_Tag.html): Describes a tag applied to a resource in an environment.
- [Trigger](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_Trigger.html): Describes a trigger.
- [ValidationMessage](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ValidationMessage.html): An error or warning for a desired configuration option value.
