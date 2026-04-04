# Source: https://docs.aws.amazon.com/security-ir/latest/APIReference/llms.txt

# AWS Security Incident Response API Reference

> This guide documents the action and response elements for use of the service.

- [Welcome](https://docs.aws.amazon.com/security-ir/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/security-ir/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/security-ir/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_Operations.html)

- [BatchGetMemberAccountDetails](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_BatchGetMemberAccountDetails.html): Provides information on whether the supplied account IDs are associated with a membership.
- [CancelMembership](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CancelMembership.html): Cancels an existing membership.
- [CloseCase](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CloseCase.html): Closes an existing case.
- [CreateCase](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CreateCase.html): Creates a new case.
- [CreateCaseComment](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CreateCaseComment.html): Adds a comment to an existing case.
- [CreateMembership](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CreateMembership.html): Creates a new membership.
- [GetCase](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetCase.html): Returns the attributes of a case.
- [GetCaseAttachmentDownloadUrl](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetCaseAttachmentDownloadUrl.html): Returns a Pre-Signed URL for uploading attachments into a case.
- [GetCaseAttachmentUploadUrl](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetCaseAttachmentUploadUrl.html): Uploads an attachment to a case.
- [GetMembership](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetMembership.html): Returns the attributes of a membership.
- [ListCaseEdits](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListCaseEdits.html): Views the case history for edits made to a designated case.
- [ListCases](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListCases.html): Lists all cases the requester has access to.
- [ListComments](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListComments.html): Returns comments for a designated case.
- [ListInvestigations](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListInvestigations.html): Lists all investigations associated with cases that the requester has access to.
- [ListMemberships](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListMemberships.html): Returns the memberships that the calling principal can access.
- [ListTagsForResource](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListTagsForResource.html): Returns currently configured tags on a resource.
- [SendFeedback](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_SendFeedback.html): Submits feedback about an investigation action or result.
- [TagResource](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_TagResource.html): Adds a tag(s) to a designated resource.
- [UntagResource](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UntagResource.html): Removes a tag(s) from a designate resource.
- [UpdateCase](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateCase.html): Updates an existing case.
- [UpdateCaseComment](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateCaseComment.html): Updates an existing case comment.
- [UpdateCaseStatus](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateCaseStatus.html): Updates the state transitions for a designated cases.
- [UpdateMembership](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateMembership.html): Updates membership configuration.
- [UpdateResolverType](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateResolverType.html): Updates the resolver type for a case.


## [Data Types](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_Types.html)

- [CaseAttachmentAttributes](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CaseAttachmentAttributes.html)
- [CaseEditItem](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CaseEditItem.html)
- [CaseMetadataEntry](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CaseMetadataEntry.html): Represents a single metadata entry associated with a case.
- [GetMembershipAccountDetailError](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetMembershipAccountDetailError.html)
- [GetMembershipAccountDetailItem](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetMembershipAccountDetailItem.html)
- [ImpactedAwsRegion](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ImpactedAwsRegion.html)
- [IncidentResponder](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_IncidentResponder.html)
- [InvestigationAction](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_InvestigationAction.html): Represents a specific action or recommendation generated during a security investigation.
- [InvestigationFeedback](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_InvestigationFeedback.html): Contains user feedback about an investigation action, including ratings and comments to help improve investigation quality.
- [ListCasesItem](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListCasesItem.html)
- [ListCommentsItem](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListCommentsItem.html)
- [ListMembershipItem](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListMembershipItem.html)
- [MembershipAccountsConfigurations](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_MembershipAccountsConfigurations.html): The MembershipAccountsConfigurations structure defines the configuration settings for managing membership accounts withinAWS.
- [MembershipAccountsConfigurationsUpdate](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_MembershipAccountsConfigurationsUpdate.html): The MembershipAccountsConfigurationsUpdatestructure represents the configuration updates for member accounts within an AWS organization.
- [OptInFeature](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_OptInFeature.html)
- [ThreatActorIp](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ThreatActorIp.html)
- [ValidationExceptionField](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ValidationExceptionField.html)
- [Watcher](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_Watcher.html)
