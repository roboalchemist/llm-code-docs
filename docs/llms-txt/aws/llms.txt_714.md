# Source: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/llms.txt

# Resource Groups Tagging API API Reference

> AWS Resource Groups lets you organize your AWS resources into groups, tag resources using virtually any criteria, and manage, monitor, and automate tasks on grouped resources. This guide is the API reference for the tagging operations on AWS resources.

- [AWS Resource Groups Tagging API Reference](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html)
- [Supported services](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html)
- [Common Parameters](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/CommonErrors.html)
- [Making API requests](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/making-api-requests.html)

## [Actions](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_Operations.html)

- [DescribeReportCreation](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.html): Describes the status of the StartReportCreation operation.
- [GetComplianceSummary](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.html): Returns a table that shows counts of resources that are noncompliant with their tag policies.
- [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html): Returns all the tagged or previously tagged resources that are located in the specified AWS Region for the account.
- [GetTagKeys](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagKeys.html): Returns all tag keys currently in use in the specified AWS Region for the calling account.
- [GetTagValues](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagValues.html): Returns all tag values for the specified key that are used in the specified AWS Region for the calling account.
- [StartReportCreation](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_StartReportCreation.html): Generates a report that lists all tagged resources in the accounts across your organization and tells whether each resource is compliant with the effective tag policy.
- [TagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html): Applies one or more tags to the specified resources.
- [UntagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntagResources.html): Removes the specified tags from the specified resources.


## [Data Types](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_Types.html)

- [ComplianceDetails](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_ComplianceDetails.html): Information that shows whether a resource is compliant with the effective tag policy, including details on any noncompliant tag keys.
- [FailureInfo](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_FailureInfo.html): Information about the errors that are returned for each failed resource.
- [ResourceTagMapping](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_ResourceTagMapping.html): A list of resource ARNs and the tags (keys and values) that are associated with each.
- [Summary](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_Summary.html): A count of noncompliant resources.
- [Tag](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_Tag.html): The metadata that you apply to AWS resources to help you categorize and organize them.
- [TagFilter](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagFilter.html): A list of tags (keys and values) that are used to specify the associated resources.
