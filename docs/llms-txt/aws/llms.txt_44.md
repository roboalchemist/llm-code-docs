# Source: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/llms.txt

# Amazon CloudWatch Synthetics Welcome

> You can use Amazon CloudWatch Synthetics to continually monitor your services. You can create and manage canaries, which are modular, lightweight scripts that monitor your endpoints and APIs from the outside-in. You can set up your canaries to run 24 hours a day, once per minute. The canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. The canaries seamlessly integrate with CloudWatch ServiceLens to help you trace the causes of impacted nodes in your applications. For more information, see Using ServiceLens to Monitor the Health of Your Applications in the Amazon CloudWatch User Guide.

- [Welcome](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_Operations.html)

- [AssociateResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_AssociateResource.html): Associates a canary with a group.
- [CreateCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateCanary.html): Creates a canary.
- [CreateGroup](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateGroup.html): Creates a group which you can use to associate canaries with each other, including cross-Region canaries.
- [DeleteCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html): Permanently deletes the specified canary.
- [DeleteGroup](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteGroup.html): Deletes a group.
- [DescribeCanaries](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html): This operation returns a list of the canaries in your account, along with full details about each canary.
- [DescribeCanariesLastRun](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanariesLastRun.html): Use this operation to see information from the most recent run of each canary that you have created.
- [DescribeRuntimeVersions](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeRuntimeVersions.html): Returns a list of Synthetics canary runtime versions.
- [DisassociateResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DisassociateResource.html): Removes a canary from a group.
- [GetCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanary.html): Retrieves complete information about one canary.
- [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html): Retrieves a list of runs for a specified canary.
- [GetGroup](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetGroup.html): Returns information about one group.
- [ListAssociatedGroups](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListAssociatedGroups.html): Returns a list of the groups that the specified canary is associated with.
- [ListGroupResources](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListGroupResources.html): This operation returns a list of the ARNs of the canaries that are associated with the specified group.
- [ListGroups](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListGroups.html): Returns a list of all groups in the account, displaying their names, unique IDs, and ARNs.
- [ListTagsForResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListTagsForResource.html): Displays the tags associated with a canary or group.
- [StartCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StartCanary.html): Use this operation to run a canary that has already been created.
- [StartCanaryDryRun](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StartCanaryDryRun.html): Use this operation to start a dry run for a canary that has already been created
- [StopCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StopCanary.html): Stops the canary to prevent all future runs.
- [TagResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified canary or group.
- [UntagResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UntagResource.html): Removes one or more tags from the specified resource.
- [UpdateCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UpdateCanary.html): Updates the configuration of a canary that has already been created.


## [Data Types](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_Types.html)

- [ArtifactConfigInput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ArtifactConfigInput.html): A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.
- [ArtifactConfigOutput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ArtifactConfigOutput.html): A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.
- [BaseScreenshot](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_BaseScreenshot.html): A structure representing a screenshot that is used as a baseline during visual monitoring comparisons made by the canary.
- [BrowserConfig](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_BrowserConfig.html): A structure that specifies the browser type to use for a canary run.
- [Canary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_Canary.html): This structure contains all information about one canary in your account.
- [CanaryCodeInput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryCodeInput.html): Use this structure to input your script code for the canary.
- [CanaryCodeOutput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryCodeOutput.html): This structure contains information about the canary's Lambda handler and where its code is stored by CloudWatch Synthetics.
- [CanaryDryRunConfigOutput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryDryRunConfigOutput.html): Returns the dry run configurations set for a canary.
- [CanaryLastRun](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryLastRun.html): This structure contains information about the most recent run of a single canary.
- [CanaryRun](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRun.html): This structure contains the details about one run of one canary.
- [CanaryRunConfigInput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunConfigInput.html): A structure that contains input information for a canary run.
- [CanaryRunConfigOutput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunConfigOutput.html): A structure that contains information about a canary run.
- [CanaryRunStatus](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunStatus.html): This structure contains the status information about a canary run.
- [CanaryRunTimeline](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunTimeline.html): This structure contains the start and end times of a single canary run.
- [CanaryScheduleInput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryScheduleInput.html): This structure specifies how often a canary is to make runs and the date and time when it should stop making runs.
- [CanaryScheduleOutput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryScheduleOutput.html): How long, in seconds, for the canary to continue making regular runs according to the schedule in the Expression value.
- [CanaryStatus](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryStatus.html): A structure that contains the current state of the canary.
- [CanaryTimeline](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryTimeline.html): This structure contains information about when the canary was created and modified.
- [Dependency](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_Dependency.html): A structure that contains information about a dependency for a canary.
- [DryRunConfigOutput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DryRunConfigOutput.html): Returns the dry run configurations set for a canary.
- [EngineConfig](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_EngineConfig.html): A structure of engine configurations for the canary, one for each browser type that the canary is configured to run on.
- [Group](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_Group.html): This structure contains information about one group.
- [GroupSummary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GroupSummary.html): A structure containing some information about a group.
- [RetryConfigInput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_RetryConfigInput.html): This structure contains information about the canary's retry configuration.
- [RetryConfigOutput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_RetryConfigOutput.html): This structure contains information about the canary's retry configuration.
- [RuntimeVersion](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_RuntimeVersion.html): This structure contains information about one canary runtime version.
- [S3EncryptionConfig](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_S3EncryptionConfig.html): A structure that contains the configuration of encryption-at-rest settings for canary artifacts that the canary uploads to Amazon S3.
- [VisualReferenceInput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_VisualReferenceInput.html): An object that specifies what screenshots to use as a baseline for visual monitoring by this canary.
- [VisualReferenceOutput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_VisualReferenceOutput.html): If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run that is used as the baseline for screenshots, and the coordinates of any parts of those screenshots that are ignored during visual monitoring comparison.
- [VpcConfigInput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_VpcConfigInput.html): If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint.
- [VpcConfigOutput](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_VpcConfigOutput.html): If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint.
