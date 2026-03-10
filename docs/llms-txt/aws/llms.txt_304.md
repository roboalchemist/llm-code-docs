# Source: https://docs.aws.amazon.com/dlm/latest/APIReference/llms.txt

# Amazon Data Lifecycle Manager API Reference

> With Amazon Data Lifecycle Manager, you can manage the lifecycle of your AWS resources. You create lifecycle policies, which are used to automate operations on the specified resources.

- [Welcome](https://docs.aws.amazon.com/dlm/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/dlm/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/dlm/latest/APIReference/CommonErrors.html)
- [Logging API Calls Using AWS CloudTrail](https://docs.aws.amazon.com/dlm/latest/APIReference/logging-using-cloudtrail.html)

## [Actions](https://docs.aws.amazon.com/dlm/latest/APIReference/API_Operations.html)

- [CreateLifecyclePolicy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CreateLifecyclePolicy.html): Creates an Amazon Data Lifecycle Manager lifecycle policy.
- [DeleteLifecyclePolicy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_DeleteLifecyclePolicy.html): Deletes the specified lifecycle policy and halts the automated operations that the policy specified.
- [GetLifecyclePolicies](https://docs.aws.amazon.com/dlm/latest/APIReference/API_GetLifecyclePolicies.html): Gets summary information about all or the specified data lifecycle policies.
- [GetLifecyclePolicy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_GetLifecyclePolicy.html): Gets detailed information about the specified lifecycle policy.
- [ListTagsForResource](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ListTagsForResource.html): Lists the tags for the specified resource.
- [TagResource](https://docs.aws.amazon.com/dlm/latest/APIReference/API_TagResource.html): Adds the specified tags to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/dlm/latest/APIReference/API_UntagResource.html): Removes the specified tags from the specified resource.
- [UpdateLifecyclePolicy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_UpdateLifecyclePolicy.html): Updates the specified lifecycle policy.


## [Data Types](https://docs.aws.amazon.com/dlm/latest/APIReference/API_Types.html)

- [Action](https://docs.aws.amazon.com/dlm/latest/APIReference/API_Action.html): [Event-based policies only] Specifies an action for an event-based policy.
- [ArchiveRetainRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRetainRule.html): [Custom snapshot policies only] Specifies information about the archive storage tier retention period.
- [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html): [Custom snapshot policies only] Specifies a snapshot archiving rule for a schedule.
- [CreateRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CreateRule.html): [Custom snapshot and AMI policies only] Specifies when the policy should create snapshots or AMIs.
- [CrossRegionCopyAction](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyAction.html): [Event-based policies only] Specifies a cross-Region copy action for event-based policies.
- [CrossRegionCopyDeprecateRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyDeprecateRule.html): [Custom AMI policies only] Specifies an AMI deprecation rule for cross-Region AMI copies created by an AMI policy.
- [CrossRegionCopyRetainRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRetainRule.html): Specifies a retention rule for cross-Region snapshot copies created by snapshot or event-based policies, or cross-Region AMI copies created by AMI policies.
- [CrossRegionCopyRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html): [Custom snapshot and AMI policies only] Specifies a cross-Region copy rule for a snapshot and AMI policies.
- [CrossRegionCopyTarget](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyTarget.html): [Default policies only] Specifies a destination Region for cross-Region copy actions.
- [DeprecateRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_DeprecateRule.html): [Custom AMI policies only] Specifies an AMI deprecation rule for AMIs created by an AMI lifecycle policy.
- [EncryptionConfiguration](https://docs.aws.amazon.com/dlm/latest/APIReference/API_EncryptionConfiguration.html): [Event-based policies only] Specifies the encryption settings for cross-Region snapshot copies created by event-based policies.
- [EventParameters](https://docs.aws.amazon.com/dlm/latest/APIReference/API_EventParameters.html): [Event-based policies only] Specifies an event that activates an event-based policy.
- [EventSource](https://docs.aws.amazon.com/dlm/latest/APIReference/API_EventSource.html): [Event-based policies only] Specifies an event that activates an event-based policy.
- [Exclusions](https://docs.aws.amazon.com/dlm/latest/APIReference/API_Exclusions.html): [Default policies only] Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs.
- [FastRestoreRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_FastRestoreRule.html): [Custom snapshot policies only] Specifies a rule for enabling fast snapshot restore for snapshots created by snapshot policies.
- [LifecyclePolicy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_LifecyclePolicy.html): Information about a lifecycle policy.
- [LifecyclePolicySummary](https://docs.aws.amazon.com/dlm/latest/APIReference/API_LifecyclePolicySummary.html): Summary information about a lifecycle policy.
- [Parameters](https://docs.aws.amazon.com/dlm/latest/APIReference/API_Parameters.html): [Custom snapshot and AMI policies only] Specifies optional parameters for snapshot and AMI policies.
- [PolicyDetails](https://docs.aws.amazon.com/dlm/latest/APIReference/API_PolicyDetails.html): Specifies the configuration of a lifecycle policy.
- [RetainRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_RetainRule.html): [Custom snapshot and AMI policies only] Specifies a retention rule for snapshots created by snapshot policies, or for AMIs created by AMI policies.
- [RetentionArchiveTier](https://docs.aws.amazon.com/dlm/latest/APIReference/API_RetentionArchiveTier.html): [Custom snapshot policies only] Describes the retention rule for archived snapshots.
- [Schedule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_Schedule.html): [Custom snapshot and AMI policies only] Specifies a schedule for a snapshot or AMI lifecycle policy.
- [Script](https://docs.aws.amazon.com/dlm/latest/APIReference/API_Script.html): [Custom snapshot policies that target instances only] Information about pre and/or post scripts for a snapshot lifecycle policy that targets instances.
- [ShareRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ShareRule.html): [Custom snapshot policies only] Specifies a rule for sharing snapshots across AWS accounts.
- [Tag](https://docs.aws.amazon.com/dlm/latest/APIReference/API_Tag.html): Specifies a tag for a resource.
