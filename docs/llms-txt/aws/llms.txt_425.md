# Source: https://docs.aws.amazon.com/greengrass/v2/APIReference/llms.txt

# AWS IoT Greengrass API Reference, Version 2

> Describes all the API operations for AWS IoT Greengrass V2 in detail. Also provides sample requests, responses, and errors for the supported web services protocols.

- [Welcome](https://docs.aws.amazon.com/greengrass/v2/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/greengrass/v2/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/greengrass/v2/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Operations.html)

- [AssociateServiceRoleToAccount](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_AssociateServiceRoleToAccount.html): Associates a Greengrass service role with AWS IoT Greengrass for your AWS account in this AWS Region.
- [BatchAssociateClientDeviceWithCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_BatchAssociateClientDeviceWithCoreDevice.html): Associates a list of client devices with a core device.
- [BatchDisassociateClientDeviceFromCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_BatchDisassociateClientDeviceFromCoreDevice.html): Disassociates a list of client devices from a core device.
- [CancelDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CancelDeployment.html): Cancels a deployment.
- [CreateComponentVersion](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CreateComponentVersion.html): Creates a component.
- [CreateDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CreateDeployment.html): Creates a continuous deployment for a target, which is a Greengrass core device or group of core devices.
- [DeleteComponent](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeleteComponent.html): Deletes a version of a component from AWS IoT Greengrass.
- [DeleteCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeleteCoreDevice.html): Deletes a Greengrass core device, which is an AWS IoT thing.
- [DeleteDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeleteDeployment.html): Deletes a deployment.
- [DescribeComponent](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DescribeComponent.html): Retrieves metadata for a version of a component.
- [DisassociateServiceRoleFromAccount](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DisassociateServiceRoleFromAccount.html): Disassociates the Greengrass service role from AWS IoT Greengrass for your AWS account in this AWS Region.
- [GetComponent](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponent.html): Gets the recipe for a version of a component.
- [GetComponentVersionArtifact](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponentVersionArtifact.html): Gets the pre-signed URL to download a public or a Lambda component artifact.
- [GetConnectivityInfo](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetConnectivityInfo.html): Retrieves connectivity information for a Greengrass core device.
- [GetCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetCoreDevice.html): Retrieves metadata for a Greengrass core device.
- [GetDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetDeployment.html): Gets a deployment.
- [GetServiceRoleForAccount](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetServiceRoleForAccount.html): Gets the service role associated with AWS IoT Greengrass for your AWS account in this AWS Region.
- [ListClientDevicesAssociatedWithCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListClientDevicesAssociatedWithCoreDevice.html): Retrieves a paginated list of client devices that are associated with a core device.
- [ListComponents](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListComponents.html): Retrieves a paginated list of component summaries.
- [ListComponentVersions](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListComponentVersions.html): Retrieves a paginated list of all versions for a component.
- [ListCoreDevices](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListCoreDevices.html): Retrieves a paginated list of Greengrass core devices.
- [ListDeployments](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListDeployments.html): Retrieves a paginated list of deployments.
- [ListEffectiveDeployments](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListEffectiveDeployments.html): Retrieves a paginated list of deployment jobs that AWS IoT Greengrass sends to Greengrass core devices.
- [ListInstalledComponents](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListInstalledComponents.html): Retrieves a paginated list of the components that a Greengrass core device runs.
- [ListTagsForResource](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListTagsForResource.html): Retrieves the list of tags for an AWS IoT Greengrass resource.
- [ResolveComponentCandidates](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ResolveComponentCandidates.html): Retrieves a list of components that meet the component, version, and platform requirements of a deployment.
- [TagResource](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_TagResource.html): Adds tags to an AWS IoT Greengrass resource.
- [UntagResource](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_UntagResource.html): Removes a tag from an AWS IoT Greengrass resource.
- [UpdateConnectivityInfo](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_UpdateConnectivityInfo.html): Updates connectivity information for a Greengrass core device.


## [Data Types](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Types.html)

- [AssociateClientDeviceWithCoreDeviceEntry](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_AssociateClientDeviceWithCoreDeviceEntry.html): Contains a request to associate a client device with a core device.
- [AssociateClientDeviceWithCoreDeviceErrorEntry](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_AssociateClientDeviceWithCoreDeviceErrorEntry.html): Contains an error that occurs from a request to associate a client device with a core device.
- [AssociatedClientDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_AssociatedClientDevice.html): Contains information about a client device that is associated to a core device for cloud discovery.
- [CloudComponentStatus](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CloudComponentStatus.html): Contains the status of a component version in the AWS IoT Greengrass service.
- [Component](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Component.html): Contains information about a component.
- [ComponentCandidate](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentCandidate.html): Contains information about a component that is a candidate to deploy to a Greengrass core device.
- [ComponentConfigurationUpdate](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentConfigurationUpdate.html): Contains information about a deployment's update to a component's configuration on Greengrass core devices.
- [ComponentDependencyRequirement](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentDependencyRequirement.html): Contains information about a component dependency for a Lambda function component.
- [ComponentDeploymentSpecification](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentDeploymentSpecification.html): Contains information about a component to deploy.
- [ComponentLatestVersion](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentLatestVersion.html): Contains information about the latest version of a component.
- [ComponentPlatform](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentPlatform.html): Contains information about a platform that a component supports.
- [ComponentRunWith](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentRunWith.html): Contains information system user and group that the AWS IoT Greengrass Core software uses to run component processes on the core device.
- [ComponentVersionListItem](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentVersionListItem.html): Contains information about a component version in a list.
- [ConnectivityInfo](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ConnectivityInfo.html): Contains information about an endpoint and port where client devices can connect to an MQTT broker on a Greengrass core device.
- [CoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CoreDevice.html): Contains information about a Greengrass core device, which is an AWS IoT thing that runs the AWS IoT Greengrass Core software.
- [Deployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Deployment.html): Contains information about a deployment.
- [DeploymentComponentUpdatePolicy](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeploymentComponentUpdatePolicy.html): Contains information about a deployment's policy that defines when components are safe to update.
- [DeploymentConfigurationValidationPolicy](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeploymentConfigurationValidationPolicy.html): Contains information about how long a component on a core device can validate its configuration updates before it times out.
- [DeploymentIoTJobConfiguration](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeploymentIoTJobConfiguration.html): Contains information about an AWS IoT job configuration.
- [DeploymentPolicies](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeploymentPolicies.html): Contains information about policies that define how a deployment updates components and handles failure.
- [DisassociateClientDeviceFromCoreDeviceEntry](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DisassociateClientDeviceFromCoreDeviceEntry.html): Contains a request to disassociate a client device from a core device.
- [DisassociateClientDeviceFromCoreDeviceErrorEntry](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DisassociateClientDeviceFromCoreDeviceErrorEntry.html): Contains an error that occurs from a request to disassociate a client device from a core device.
- [EffectiveDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_EffectiveDeployment.html): Contains information about a deployment job that AWS IoT Greengrass sends to a Greengrass core device.
- [EffectiveDeploymentStatusDetails](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_EffectiveDeploymentStatusDetails.html): Contains all error-related information for the deployment record.
- [InstalledComponent](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_InstalledComponent.html): Contains information about a component on a Greengrass core device.
- [IoTJobAbortConfig](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_IoTJobAbortConfig.html): Contains a list of criteria that define when and how to cancel a configuration deployment.
- [IoTJobAbortCriteria](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_IoTJobAbortCriteria.html): Contains criteria that define when and how to cancel a job.
- [IoTJobExecutionsRolloutConfig](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_IoTJobExecutionsRolloutConfig.html): Contains information about the rollout configuration for a job.
- [IoTJobExponentialRolloutRate](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_IoTJobExponentialRolloutRate.html): Contains information about an exponential rollout rate for a configuration deployment job.
- [IoTJobRateIncreaseCriteria](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_IoTJobRateIncreaseCriteria.html): Contains information about criteria to meet before a job increases its rollout rate.
- [IoTJobTimeoutConfig](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_IoTJobTimeoutConfig.html): Contains information about the timeout configuration for a job.
- [LambdaContainerParams](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaContainerParams.html): Contains information about a container in which AWS Lambda functions run on Greengrass core devices.
- [LambdaDeviceMount](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaDeviceMount.html): Contains information about a device that Linux processes in a container can access.
- [LambdaEventSource](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaEventSource.html): Contains information about an event source for an AWS Lambda function.
- [LambdaExecutionParameters](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaExecutionParameters.html): Contains parameters for a Lambda function that runs on AWS IoT Greengrass.
- [LambdaFunctionRecipeSource](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaFunctionRecipeSource.html): Contains information about an AWS Lambda function to import to create a component.
- [LambdaLinuxProcessParams](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaLinuxProcessParams.html): Contains parameters for a Linux process that contains an AWS Lambda function.
- [LambdaVolumeMount](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaVolumeMount.html): Contains information about a volume that Linux processes in a container can access.
- [ResolvedComponentVersion](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ResolvedComponentVersion.html): Contains information about a component version that is compatible to run on a Greengrass core device.
- [SystemResourceLimits](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_SystemResourceLimits.html): Contains information about system resource limits that the AWS IoT Greengrass Core software applies to a component's processes.
- [ValidationExceptionField](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ValidationExceptionField.html): Contains information about a validation exception field.
