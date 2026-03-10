# Source: https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/llms.txt

# CloudWatch investigations CloudWatch investigations API Reference

> The CloudWatch investigations feature is a generative AI-powered assistant that can help you respond to incidents in your system. It uses generative AI to scan your system's telemetry and quickly surface suggestions that might be related to your issue. These suggestions include metrics, logs, deployment events, and root-cause hypotheses.

- [Welcome](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_Operations.html)

- [CreateInvestigationGroup](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_CreateInvestigationGroup.html): Creates an investigation group in your account.
- [DeleteInvestigationGroup](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_DeleteInvestigationGroup.html): Deletes the specified investigation group from your account.
- [DeleteInvestigationGroupPolicy](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_DeleteInvestigationGroupPolicy.html): Removes the IAM resource policy from being associated with the investigation group that you specify.
- [GetInvestigationGroup](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroup.html): Returns the configuration information for the specified investigation group.
- [GetInvestigationGroupPolicy](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroupPolicy.html): Returns the JSON of the IAM resource policy associated with the specified investigation group in a string.
- [ListInvestigationGroups](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_ListInvestigationGroups.html): Returns the ARN and name of each investigation group in the account.
- [ListTagsForResource](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_ListTagsForResource.html): Displays the tags associated with a CloudWatch investigations resource.
- [PutInvestigationGroupPolicy](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_PutInvestigationGroupPolicy.html): Creates an IAM resource policy and assigns it to the specified investigation group.
- [TagResource](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_UntagResource.html): Removes one or more tags from the specified resource.
- [UpdateInvestigationGroup](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_UpdateInvestigationGroup.html): Updates the configuration of the specified investigation group.


## [Data Types](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_Types.html)

- [CrossAccountConfiguration](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_CrossAccountConfiguration.html): This structure contains information about the cross-account configuration in the account.
- [EncryptionConfiguration](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_EncryptionConfiguration.html): Use this structure to specify a customer managed AWS KMS key to use to encrypt investigation data.
- [ListInvestigationGroupsModel](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_ListInvestigationGroupsModel.html): This structure contains information about one investigation group in the account.
