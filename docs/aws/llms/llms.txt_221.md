# Source: https://docs.aws.amazon.com/codedeploy/latest/APIReference/llms.txt

# AWS CodeDeploy API Reference

> AWS CodeDeploy is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances running in your own facility, serverless AWS Lambda functions, or applications in an Amazon ECS service.

- [Welcome](https://docs.aws.amazon.com/codedeploy/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/codedeploy/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/codedeploy/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_Operations.html)

- [AddTagsToOnPremisesInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AddTagsToOnPremisesInstances.html): Adds tags to on-premises instances.
- [BatchGetApplicationRevisions](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetApplicationRevisions.html): Gets information about one or more application revisions.
- [BatchGetApplications](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetApplications.html): Gets information about one or more applications.
- [BatchGetDeploymentGroups](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentGroups.html): Gets information about one or more deployment groups.
- [BatchGetDeploymentInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentInstances.html)
- [BatchGetDeployments](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeployments.html): Gets information about one or more deployments.
- [BatchGetDeploymentTargets](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentTargets.html): Returns an array of one or more targets associated with a deployment.
- [BatchGetOnPremisesInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetOnPremisesInstances.html): Gets information about one or more on-premises instances.
- [ContinueDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ContinueDeployment.html): For a blue/green deployment, starts the process of rerouting traffic from instances in the original environment to instances in the replacement environment without waiting for a specified wait time to elapse. (Traffic rerouting, which is achieved by registering instances in the replacement environment with the load balancer, can start as soon as all instances have a status of Ready.)
- [CreateApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateApplication.html): Creates an application.
- [CreateDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html): Deploys an application revision through the specified deployment group.
- [CreateDeploymentConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeploymentConfig.html): Creates a deployment configuration.
- [CreateDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeploymentGroup.html): Creates a deployment group to which application revisions are deployed.
- [DeleteApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteApplication.html): Deletes an application.
- [DeleteDeploymentConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteDeploymentConfig.html): Deletes a deployment configuration.
- [DeleteDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteDeploymentGroup.html): Deletes a deployment group.
- [DeleteGitHubAccountToken](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteGitHubAccountToken.html): Deletes a GitHub account connection.
- [DeleteResourcesByExternalId](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteResourcesByExternalId.html): Deletes resources linked to an external ID.
- [DeregisterOnPremisesInstance](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeregisterOnPremisesInstance.html): Deregisters an on-premises instance.
- [GetApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetApplication.html): Gets information about an application.
- [GetApplicationRevision](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetApplicationRevision.html): Gets information about an application revision.
- [GetDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeployment.html): Gets information about a deployment.
- [GetDeploymentConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentConfig.html): Gets information about a deployment configuration.
- [GetDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentGroup.html): Gets information about a deployment group.
- [GetDeploymentInstance](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentInstance.html): Gets information about an instance as part of a deployment.
- [GetDeploymentTarget](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentTarget.html): Returns information about a deployment target.
- [GetOnPremisesInstance](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetOnPremisesInstance.html): Gets information about an on-premises instance.
- [ListApplicationRevisions](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListApplicationRevisions.html): Lists information about revisions for an application.
- [ListApplications](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListApplications.html): Lists the applications registered with the user or AWS account.
- [ListDeploymentConfigs](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentConfigs.html): Lists the deployment configurations with the user or AWS account.
- [ListDeploymentGroups](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentGroups.html): Lists the deployment groups for an application registered with the AWS user or AWS account.
- [ListDeploymentInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentInstances.html)
- [ListDeployments](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeployments.html): Lists the deployments in a deployment group for an application registered with the user or AWS account.
- [ListDeploymentTargets](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentTargets.html): Returns an array of target IDs that are associated a deployment.
- [ListGitHubAccountTokenNames](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListGitHubAccountTokenNames.html): Lists the names of stored connections to GitHub accounts.
- [ListOnPremisesInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListOnPremisesInstances.html): Gets a list of names for one or more on-premises instances.
- [ListTagsForResource](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListTagsForResource.html): Returns a list of tags for the resource identified by a specified Amazon Resource Name (ARN).
- [PutLifecycleEventHookExecutionStatus](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_PutLifecycleEventHookExecutionStatus.html): Sets the result of a Lambda validation function.
- [RegisterApplicationRevision](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RegisterApplicationRevision.html): Registers with AWS CodeDeploy a revision for the specified application.
- [RegisterOnPremisesInstance](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RegisterOnPremisesInstance.html): Registers an on-premises instance.
- [RemoveTagsFromOnPremisesInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RemoveTagsFromOnPremisesInstances.html): Removes one or more tags from one or more on-premises instances.
- [SkipWaitTimeForInstanceTermination](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_SkipWaitTimeForInstanceTermination.html): In a blue/green deployment, overrides any specified wait time and starts terminating instances immediately after the traffic routing is complete.
- [StopDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_StopDeployment.html): Attempts to stop an ongoing deployment.
- [TagResource](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TagResource.html): Associates the list of tags in the input Tags parameter with the resource identified by the ResourceArn input parameter.
- [UntagResource](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_UntagResource.html): Disassociates a resource from a list of tags.
- [UpdateApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_UpdateApplication.html): Changes the name of an application.
- [UpdateDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_UpdateDeploymentGroup.html): Changes information about a deployment group.


## [Data Types](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_Types.html)

- [Alarm](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_Alarm.html): Information about an alarm.
- [AlarmConfiguration](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AlarmConfiguration.html): Information about alarms associated with a deployment or deployment group.
- [ApplicationInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ApplicationInfo.html): Information about an application.
- [AppSpecContent](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AppSpecContent.html): A revision for an AWS Lambda or Amazon ECS deployment that is a YAML-formatted or JSON-formatted string.
- [AutoRollbackConfiguration](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AutoRollbackConfiguration.html): Information about a configuration for automatically rolling back to a previous version of an application revision when a deployment is not completed successfully.
- [AutoScalingGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AutoScalingGroup.html): Information about an Auto Scaling group.
- [BlueGreenDeploymentConfiguration](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BlueGreenDeploymentConfiguration.html): Information about blue/green deployment options for a deployment group.
- [BlueInstanceTerminationOption](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BlueInstanceTerminationOption.html): Information about whether instances in the original environment are terminated when a blue/green deployment is successful.
- [CloudFormationTarget](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CloudFormationTarget.html): Information about the target to be updated by an CloudFormation blue/green deployment.
- [DeploymentConfigInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentConfigInfo.html): Information about a deployment configuration.
- [DeploymentGroupInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentGroupInfo.html): Information about a deployment group.
- [DeploymentInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentInfo.html): Information about a deployment.
- [DeploymentOverview](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentOverview.html): Information about the deployment status of the instances in the deployment.
- [DeploymentReadyOption](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentReadyOption.html): Information about how traffic is rerouted to instances in a replacement environment in a blue/green deployment.
- [DeploymentStyle](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentStyle.html): Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.
- [DeploymentTarget](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentTarget.html): Information about the deployment target.
- [Diagnostics](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_Diagnostics.html): Diagnostic information about executable scripts that are part of a deployment.
- [EC2TagFilter](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_EC2TagFilter.html): Information about an EC2 tag filter.
- [EC2TagSet](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_EC2TagSet.html): Information about groups of Amazon EC2 instance tags.
- [ECSService](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ECSService.html): Contains the service and cluster names used to identify an Amazon ECS deployment's target.
- [ECSTarget](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ECSTarget.html): Information about the target of an Amazon ECS deployment.
- [ECSTaskSet](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ECSTaskSet.html): Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment.
- [ELBInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ELBInfo.html): Information about a Classic Load Balancer in Elastic Load Balancing to use in a deployment.
- [ErrorInformation](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ErrorInformation.html): Information about a deployment error.
- [GenericRevisionInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GenericRevisionInfo.html): Information about an application revision.
- [GitHubLocation](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GitHubLocation.html): Information about the location of application artifacts stored in GitHub.
- [GreenFleetProvisioningOption](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GreenFleetProvisioningOption.html): Information about the instances that belong to the replacement environment in a blue/green deployment.
- [InstanceInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_InstanceInfo.html): Information about an on-premises instance.
- [InstanceSummary](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_InstanceSummary.html): This data type has been deprecated.
- [InstanceTarget](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_InstanceTarget.html): A target Amazon EC2 or on-premises instance during a deployment that uses the EC2/On-premises compute platform.
- [LambdaFunctionInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_LambdaFunctionInfo.html): Information about a Lambda function specified in a deployment.
- [LambdaTarget](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_LambdaTarget.html): Information about the target AWS Lambda function during an AWS Lambda deployment.
- [LastDeploymentInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_LastDeploymentInfo.html): Information about the most recent attempted or successful deployment to a deployment group.
- [LifecycleEvent](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_LifecycleEvent.html): Information about a deployment lifecycle event.
- [LoadBalancerInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_LoadBalancerInfo.html): Information about the Elastic Load Balancing load balancer or target group used in a deployment.
- [MinimumHealthyHosts](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_MinimumHealthyHosts.html): Information about the minimum number of healthy instances.
- [MinimumHealthyHostsPerZone](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_MinimumHealthyHostsPerZone.html): Information about the minimum number of healthy instances per Availability Zone.
- [OnPremisesTagSet](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_OnPremisesTagSet.html): Information about groups of on-premises instance tags.
- [RawString](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RawString.html): This data type has been deprecated.
- [RelatedDeployments](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RelatedDeployments.html): Information about deployments related to the specified deployment.
- [RevisionInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RevisionInfo.html): Information about an application revision.
- [RevisionLocation](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RevisionLocation.html): Information about the location of an application revision.
- [RollbackInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RollbackInfo.html): Information about a deployment rollback.
- [S3Location](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_S3Location.html): Information about the location of application artifacts stored in Amazon S3.
- [Tag](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_Tag.html): Information about a tag.
- [TagFilter](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TagFilter.html): Information about an on-premises instance tag filter.
- [TargetGroupInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TargetGroupInfo.html): Information about a target group in Elastic Load Balancing to use in a deployment.
- [TargetGroupPairInfo](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TargetGroupPairInfo.html): Information about two target groups and how traffic is routed during an Amazon ECS deployment.
- [TargetInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TargetInstances.html): Information about the instances to be used in the replacement environment in a blue/green deployment.
- [TimeBasedCanary](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TimeBasedCanary.html): A configuration that shifts traffic from one version of a Lambda function or Amazon ECS task set to another in two increments.
- [TimeBasedLinear](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TimeBasedLinear.html): A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in equal increments, with an equal number of minutes between each increment.
- [TimeRange](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TimeRange.html): Information about a time range.
- [TrafficRoute](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TrafficRoute.html): Information about a listener.
- [TrafficRoutingConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TrafficRoutingConfig.html): The configuration that specifies how traffic is shifted from one version of a Lambda function to another version during an AWS Lambda deployment, or from one Amazon ECS task set to another during an Amazon ECS deployment.
- [TriggerConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TriggerConfig.html): Information about notification triggers for the deployment group.
- [ZonalConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ZonalConfig.html): Configure the ZonalConfig object if you want AWS CodeDeploy to deploy your application to one Availability Zone at a time, within an AWS Region.
