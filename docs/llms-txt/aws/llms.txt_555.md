# Source: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/llms.txt

# AWS Managed Services Change Management API Reference

> The change management API provides operations to create and manage requests for change (RFCs). RFCs can be created, updated, submitted, approved (or rejected), and canceled.

- [Welcome](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_Operations.html)

- [ApproveRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ApproveRfc.html): Marks the specified RFC as approved.
- [CancelRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CancelRfc.html): Cancels the specified RFC.
- [CreateRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html): Creates a new RFC.
- [CreateRfcAttachment](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfcAttachment.html): Create an attachment for an existing RFC.
- [CreateRfcCorrespondence](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfcCorrespondence.html): Create the correspondence for an RFC.
- [GetChangeTypeVersion](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_GetChangeTypeVersion.html): Returns information about the specified change type; optionally, you can specify a change type version identifier.
- [GetRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_GetRfc.html): Returns information about the specified RFC ID.
- [GetRfcAttachment](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_GetRfcAttachment.html): Retrieve the attachment from an RFC.
- [ListChangeTypeCategories](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListChangeTypeCategories.html): Returns the available change type category values.
- [ListChangeTypeClassificationSummaries](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListChangeTypeClassificationSummaries.html): Returns the classifications (category, subcategory, item, and operation) for all change types that meet the specified (optional) filter criteria.
- [ListChangeTypeItems](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListChangeTypeItems.html): Returns the available change type item values for the specified category and subcategory values.
- [ListChangeTypeOperations](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListChangeTypeOperations.html): Returns the available change type operation values for the specified category and subcategory values.
- [ListChangeTypeSubcategories](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListChangeTypeSubcategories.html): Returns the available change type subcategory values for the specified category value.
- [ListChangeTypeVersionSummaries](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListChangeTypeVersionSummaries.html): Returns version information (versions and deprecation times) for the specified change type.
- [ListRestrictedExecutionTimes](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListRestrictedExecutionTimes.html): Returns the time ranges during which change execution is restricted.
- [ListRfcAttachmentSummaries](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListRfcAttachmentSummaries.html): The Request for Change (RFCs) attachments.
- [ListRfcCorrespondences](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListRfcCorrespondences.html): List the existing correspondences of an RFC.
- [ListRfcSummaries](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListRfcSummaries.html): Returns summaries of Request for Change (RFCs) that meet the specified criteria.
- [RejectRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RejectRfc.html): Marks the specified RFC as rejected.
- [SubmitRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_SubmitRfc.html): Submits the specified RFC, and optionally specifies whether to observe default execution settings.
- [UpdateRestrictedExecutionTimes](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_UpdateRestrictedExecutionTimes.html): Replaces the existing times when change execution is restricted.
- [UpdateRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_UpdateRfc.html): Updates settings for the specified RFC ID.


## [Data Types](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_Types.html)

- [AutomationStatus](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_AutomationStatus.html): Whether the change type is automated or manual.
- [ChangeTypeAccessLevel](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ChangeTypeAccessLevel.html): The access level of the change type.
- [ChangeTypeApprovalCondition](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ChangeTypeApprovalCondition.html): The approvals that are required for the execution of a change type.
- [ChangeTypeApprovalRequirement](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ChangeTypeApprovalRequirement.html): The kind of approval that is required for the execution of a change type.
- [ChangeTypeAutomationStatus](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ChangeTypeAutomationStatus.html): The automation status of a change type (Automated or Manual).
- [ChangeTypeClassificationSummary](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ChangeTypeClassificationSummary.html): The category, subcategory, item, and operation values of a change type.
- [ChangeTypeOperationSummary](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ChangeTypeOperationSummary.html): The operation values and change type IDs for a particular category, subcategory, and item value.
- [ChangeTypeVersion](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ChangeTypeVersion.html): Information about a specific version of a change type.
- [ChangeTypeVersionSummary](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ChangeTypeVersionSummary.html): Summary information about a change type version.
- [Email](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_Email.html): The notification email structure.
- [Filter](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_Filter.html): An attribute and value pair to use for narrowing search results.
- [LinkedAttachment](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_LinkedAttachment.html): The list of attachments that are linked to the correspondence.
- [RestrictedExecutionTime](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RestrictedExecutionTime.html): The time ranges during which change execution is restricted.
- [Rfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_Rfc.html): A request for change.
- [RfcActionState](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcActionState.html): The action state of the RFC.
- [RfcApprovalState](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcApprovalState.html): The status of the approvals for the RFC.
- [RfcApprovalStatus](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcApprovalStatus.html): An ID and name for an approval status of an RFC.
- [RfcAttachment](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcAttachment.html): The RFC attachment.
- [RfcAttachmentSummary](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcAttachmentSummary.html): The RFC attachment summary structure.
- [RfcCorrespondence](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcCorrespondence.html): The RFC correspondence structure.
- [RfcNotification](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcNotification.html): The RFC notification structure.
- [RfcRestrictedExecutionTimesOverride](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcRestrictedExecutionTimesOverride.html): An ID and name for an option for overriding preset restrictions on execution of a change.
- [RfcStatus](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcStatus.html): An ID and name for the status of the RFC.
- [RfcSummary](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcSummary.html): Summary information about a request for change.
- [TimeRange](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_TimeRange.html): A starting and ending date and time.
- [UserType](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_UserType.html): The type of owner of the correspondence, either customer or AWS operator.
