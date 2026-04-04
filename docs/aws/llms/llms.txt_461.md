# Source: https://docs.aws.amazon.com/inspector/v1/APIReference/llms.txt

# Amazon Inspector Classic API Reference

> Amazon Inspector Classic enables you to analyze the behavior of your AWS resources and to identify potential security issues. For more information, see Amazon Inspector Classic User Guide.

- [Welcome](https://docs.aws.amazon.com/inspector/v1/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/inspector/v1/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/inspector/v1/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/inspector/v1/APIReference/API_Operations.html)

- [AddAttributesToFindings](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AddAttributesToFindings.html)
- [CreateAssessmentTarget](https://docs.aws.amazon.com/inspector/v1/APIReference/API_CreateAssessmentTarget.html)
- [CreateAssessmentTemplate](https://docs.aws.amazon.com/inspector/v1/APIReference/API_CreateAssessmentTemplate.html)
- [CreateExclusionsPreview](https://docs.aws.amazon.com/inspector/v1/APIReference/API_CreateExclusionsPreview.html)
- [CreateResourceGroup](https://docs.aws.amazon.com/inspector/v1/APIReference/API_CreateResourceGroup.html)
- [DeleteAssessmentRun](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DeleteAssessmentRun.html)
- [DeleteAssessmentTarget](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DeleteAssessmentTarget.html)
- [DeleteAssessmentTemplate](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DeleteAssessmentTemplate.html)
- [DescribeAssessmentRuns](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeAssessmentRuns.html)
- [DescribeAssessmentTargets](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeAssessmentTargets.html)
- [DescribeAssessmentTemplates](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeAssessmentTemplates.html)
- [DescribeCrossAccountAccessRole](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeCrossAccountAccessRole.html)
- [DescribeExclusions](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeExclusions.html)
- [DescribeFindings](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeFindings.html)
- [DescribeResourceGroups](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeResourceGroups.html)
- [DescribeRulesPackages](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeRulesPackages.html)
- [GetAssessmentReport](https://docs.aws.amazon.com/inspector/v1/APIReference/API_GetAssessmentReport.html)
- [GetExclusionsPreview](https://docs.aws.amazon.com/inspector/v1/APIReference/API_GetExclusionsPreview.html)
- [GetTelemetryMetadata](https://docs.aws.amazon.com/inspector/v1/APIReference/API_GetTelemetryMetadata.html)
- [ListAssessmentRunAgents](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListAssessmentRunAgents.html)
- [ListAssessmentRuns](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListAssessmentRuns.html)
- [ListAssessmentTargets](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListAssessmentTargets.html)
- [ListAssessmentTemplates](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListAssessmentTemplates.html)
- [ListEventSubscriptions](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListEventSubscriptions.html)
- [ListExclusions](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListExclusions.html)
- [ListFindings](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListFindings.html)
- [ListRulesPackages](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListRulesPackages.html)
- [ListTagsForResource](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListTagsForResource.html)
- [PreviewAgents](https://docs.aws.amazon.com/inspector/v1/APIReference/API_PreviewAgents.html)
- [RegisterCrossAccountAccessRole](https://docs.aws.amazon.com/inspector/v1/APIReference/API_RegisterCrossAccountAccessRole.html)
- [RemoveAttributesFromFindings](https://docs.aws.amazon.com/inspector/v1/APIReference/API_RemoveAttributesFromFindings.html)
- [SetTagsForResource](https://docs.aws.amazon.com/inspector/v1/APIReference/API_SetTagsForResource.html)
- [StartAssessmentRun](https://docs.aws.amazon.com/inspector/v1/APIReference/API_StartAssessmentRun.html)
- [StopAssessmentRun](https://docs.aws.amazon.com/inspector/v1/APIReference/API_StopAssessmentRun.html)
- [SubscribeToEvent](https://docs.aws.amazon.com/inspector/v1/APIReference/API_SubscribeToEvent.html)
- [UnsubscribeFromEvent](https://docs.aws.amazon.com/inspector/v1/APIReference/API_UnsubscribeFromEvent.html)
- [UpdateAssessmentTarget](https://docs.aws.amazon.com/inspector/v1/APIReference/API_UpdateAssessmentTarget.html)


## [Data Types](https://docs.aws.amazon.com/inspector/v1/APIReference/API_Types.html)

- [AgentAlreadyRunningAssessment](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AgentAlreadyRunningAssessment.html): Used in the exception error that is thrown if you start an assessment run for an assessment target that includes an EC2 instance that is already participating in another started assessment run.
- [AgentFilter](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AgentFilter.html): Contains information about an Amazon Inspector Classic agent.
- [AgentPreview](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AgentPreview.html): Used as a response element in the action.
- [AssessmentRun](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentRun.html): A snapshot of an Amazon Inspector Classic assessment run that contains the findings of the assessment run .
- [AssessmentRunAgent](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentRunAgent.html): Contains information about an Amazon Inspector Classic agent.
- [AssessmentRunFilter](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentRunFilter.html): Used as the request parameter in the action.
- [AssessmentRunNotification](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentRunNotification.html): Used as one of the elements of the data type.
- [AssessmentRunStateChange](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentRunStateChange.html): Used as one of the elements of the data type.
- [AssessmentTarget](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentTarget.html): Contains information about an Amazon Inspector Classic application.
- [AssessmentTargetFilter](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentTargetFilter.html): Used as the request parameter in the action.
- [AssessmentTemplate](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentTemplate.html): Contains information about an Amazon Inspector Classic assessment template.
- [AssessmentTemplateFilter](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentTemplateFilter.html): Used as the request parameter in the action.
- [AssetAttributes](https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssetAttributes.html): A collection of attributes of the host from which the finding is generated.
- [Attribute](https://docs.aws.amazon.com/inspector/v1/APIReference/API_Attribute.html): This data type is used as a request parameter in the and actions.
- [DurationRange](https://docs.aws.amazon.com/inspector/v1/APIReference/API_DurationRange.html): This data type is used in the data type.
- [EventSubscription](https://docs.aws.amazon.com/inspector/v1/APIReference/API_EventSubscription.html): This data type is used in the data type.
- [Exclusion](https://docs.aws.amazon.com/inspector/v1/APIReference/API_Exclusion.html): Contains information about what was excluded from an assessment run.
- [ExclusionPreview](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ExclusionPreview.html): Contains information about what is excluded from an assessment run given the current state of the assessment template.
- [FailedItemDetails](https://docs.aws.amazon.com/inspector/v1/APIReference/API_FailedItemDetails.html): Includes details about the failed items.
- [Finding](https://docs.aws.amazon.com/inspector/v1/APIReference/API_Finding.html): Contains information about an Amazon Inspector Classic finding.
- [FindingFilter](https://docs.aws.amazon.com/inspector/v1/APIReference/API_FindingFilter.html): This data type is used as a request parameter in the action.
- [InspectorServiceAttributes](https://docs.aws.amazon.com/inspector/v1/APIReference/API_InspectorServiceAttributes.html): This data type is used in the data type.
- [NetworkInterface](https://docs.aws.amazon.com/inspector/v1/APIReference/API_NetworkInterface.html): Contains information about the network interfaces interacting with an EC2 instance.
- [PrivateIp](https://docs.aws.amazon.com/inspector/v1/APIReference/API_PrivateIp.html): Contains information about a private IP address associated with a network interface.
- [ResourceGroup](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ResourceGroup.html): Contains information about a resource group.
- [ResourceGroupTag](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ResourceGroupTag.html): This data type is used as one of the elements of the data type.
- [RulesPackage](https://docs.aws.amazon.com/inspector/v1/APIReference/API_RulesPackage.html): Contains information about an Amazon Inspector Classic rules package.
- [Scope](https://docs.aws.amazon.com/inspector/v1/APIReference/API_Scope.html): This data type contains key-value pairs that identify various Amazon resources.
- [SecurityGroup](https://docs.aws.amazon.com/inspector/v1/APIReference/API_SecurityGroup.html): Contains information about a security group associated with a network interface.
- [Subscription](https://docs.aws.amazon.com/inspector/v1/APIReference/API_Subscription.html): This data type is used as a response element in the action.
- [Tag](https://docs.aws.amazon.com/inspector/v1/APIReference/API_Tag.html): A key and value pair.
- [TelemetryMetadata](https://docs.aws.amazon.com/inspector/v1/APIReference/API_TelemetryMetadata.html): The metadata about the Amazon Inspector Classic application data metrics collected by the agent.
- [TimestampRange](https://docs.aws.amazon.com/inspector/v1/APIReference/API_TimestampRange.html): This data type is used in the data type.
