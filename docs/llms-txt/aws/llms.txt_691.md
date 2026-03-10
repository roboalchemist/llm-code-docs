# Source: https://docs.aws.amazon.com/recyclebin/latest/APIReference/llms.txt

# Recycle Bin Welcome

> This is the Recycle Bin API Reference. This documentation provides descriptions and syntax for each of the actions and data types in Recycle Bin.

- [Welcome](https://docs.aws.amazon.com/recyclebin/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/recyclebin/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/recyclebin/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_Operations.html)

- [CreateRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_CreateRule.html): Creates a Recycle Bin retention rule.
- [DeleteRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_DeleteRule.html): Deletes a Recycle Bin retention rule.
- [GetRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_GetRule.html): Gets information about a Recycle Bin retention rule.
- [ListRules](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_ListRules.html): Lists the Recycle Bin retention rules in the Region.
- [ListTagsForResource](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_ListTagsForResource.html): Lists the tags assigned to a retention rule.
- [LockRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_LockRule.html): Locks a Region-level retention rule.
- [TagResource](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_TagResource.html): Assigns tags to the specified retention rule.
- [UnlockRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UnlockRule.html): Unlocks a retention rule.
- [UntagResource](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UntagResource.html): Unassigns a tag from a retention rule.
- [UpdateRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UpdateRule.html): Updates an existing Recycle Bin retention rule.


## [Data Types](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_Types.html)

- [LockConfiguration](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_LockConfiguration.html): Information about a retention rule lock configuration.
- [ResourceTag](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_ResourceTag.html): [Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.
- [RetentionPeriod](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_RetentionPeriod.html): Information about the retention period for which the retention rule is to retain resources.
- [RuleSummary](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_RuleSummary.html): Information about a Recycle Bin retention rule.
- [Tag](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_Tag.html): Information about the tags to assign to the retention rule.
- [UnlockDelay](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UnlockDelay.html): Information about the retention rule unlock delay.
