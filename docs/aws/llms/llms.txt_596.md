# Source: https://docs.aws.amazon.com/mpa/latest/APIReference/llms.txt

# Multi-party approval Welcome

> Multi-party approval is a capability of AWS Organizations that allows you to protect a predefined list of operations through a distributed approval process. Use Multi-party approval to establish approval workflows and transform security processes into team-based decisions.

- [Welcome](https://docs.aws.amazon.com/mpa/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/mpa/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/mpa/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/mpa/latest/APIReference/API_Operations.html)

- [CancelSession](https://docs.aws.amazon.com/mpa/latest/APIReference/API_CancelSession.html): Cancels an approval session.
- [CreateApprovalTeam](https://docs.aws.amazon.com/mpa/latest/APIReference/API_CreateApprovalTeam.html): Creates a new approval team.
- [CreateIdentitySource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_CreateIdentitySource.html): Creates a new identity source.
- [DeleteIdentitySource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_DeleteIdentitySource.html): Deletes an identity source.
- [DeleteInactiveApprovalTeamVersion](https://docs.aws.amazon.com/mpa/latest/APIReference/API_DeleteInactiveApprovalTeamVersion.html): Deletes an inactive approval team.
- [GetApprovalTeam](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetApprovalTeam.html): Returns details for an approval team.
- [GetIdentitySource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetIdentitySource.html): Returns details for an identity source.
- [GetPolicyVersion](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetPolicyVersion.html): Returns details for the version of a policy.
- [GetResourcePolicy](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetResourcePolicy.html): Returns details about a policy for a resource.
- [GetSession](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetSession.html): Returns details for an approval session.
- [ListApprovalTeams](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListApprovalTeams.html): Returns a list of approval teams.
- [ListIdentitySources](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListIdentitySources.html): Returns a list of identity sources.
- [ListPolicies](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListPolicies.html): Returns a list of policies.
- [ListPolicyVersions](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListPolicyVersions.html): Returns a list of the versions for policies.
- [ListResourcePolicies](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListResourcePolicies.html): Returns a list of policies for a resource.
- [ListSessions](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListSessions.html): Returns a list of approval sessions.
- [ListTagsForResource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListTagsForResource.html): Returns a list of the tags for a resource.
- [StartActiveApprovalTeamDeletion](https://docs.aws.amazon.com/mpa/latest/APIReference/API_StartActiveApprovalTeamDeletion.html): Starts the deletion process for an active approval team.
- [StartApprovalTeamBaseline](https://docs.aws.amazon.com/mpa/latest/APIReference/API_StartApprovalTeamBaseline.html): Starts a baseline session for specified approvers on an ACTIVE approval team.
- [TagResource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_TagResource.html): Creates or updates a resource tag.
- [UntagResource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_UntagResource.html): Removes a resource tag.
- [UpdateApprovalTeam](https://docs.aws.amazon.com/mpa/latest/APIReference/API_UpdateApprovalTeam.html): Updates an approval team.


## [Data Types](https://docs.aws.amazon.com/mpa/latest/APIReference/API_Types.html)

- [ApprovalStrategy](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ApprovalStrategy.html): Strategy for how an approval team grants approval.
- [ApprovalStrategyResponse](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ApprovalStrategyResponse.html): Contains details for how an approval team grants approval.
- [ApprovalTeamRequestApprover](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ApprovalTeamRequestApprover.html): Contains details for an approver.
- [Filter](https://docs.aws.amazon.com/mpa/latest/APIReference/API_Filter.html): Contains the filter to apply to requests.
- [GetApprovalTeamResponseApprover](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetApprovalTeamResponseApprover.html): Contains details for an approver.
- [GetSessionResponseApproverResponse](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetSessionResponseApproverResponse.html): Contains details for an approver response in an approval session.
- [IamIdentityCenter](https://docs.aws.amazon.com/mpa/latest/APIReference/API_IamIdentityCenter.html): AWS IAM Identity Center credentials.
- [IamIdentityCenterForGet](https://docs.aws.amazon.com/mpa/latest/APIReference/API_IamIdentityCenterForGet.html): AWS IAM Identity Center credentials.
- [IamIdentityCenterForList](https://docs.aws.amazon.com/mpa/latest/APIReference/API_IamIdentityCenterForList.html): AWS IAM Identity Center credentials.
- [IdentitySourceForList](https://docs.aws.amazon.com/mpa/latest/APIReference/API_IdentitySourceForList.html): Contains details for an identity source.
- [IdentitySourceParameters](https://docs.aws.amazon.com/mpa/latest/APIReference/API_IdentitySourceParameters.html): Contains details for the resource that provides identities to the identity source.
- [IdentitySourceParametersForGet](https://docs.aws.amazon.com/mpa/latest/APIReference/API_IdentitySourceParametersForGet.html): Contains details for the resource that provides identities to the identity source.
- [IdentitySourceParametersForList](https://docs.aws.amazon.com/mpa/latest/APIReference/API_IdentitySourceParametersForList.html): Contains details for the resource that provides identities to the identity source.
- [ListApprovalTeamsResponseApprovalTeam](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListApprovalTeamsResponseApprovalTeam.html): Contains details for an approval team
- [ListResourcePoliciesResponseResourcePolicy](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListResourcePoliciesResponseResourcePolicy.html): Contains details about a policy for a resource.
- [ListSessionsResponseSession](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListSessionsResponseSession.html): Contains details for an approval session.
- [MfaMethod](https://docs.aws.amazon.com/mpa/latest/APIReference/API_MfaMethod.html): MFA configuration and sycnronization status for an approver
- [MofNApprovalStrategy](https://docs.aws.amazon.com/mpa/latest/APIReference/API_MofNApprovalStrategy.html): Strategy for how an approval team grants approval.
- [PendingUpdate](https://docs.aws.amazon.com/mpa/latest/APIReference/API_PendingUpdate.html): Contains details for the pending updates for an approval team, if applicable.
- [Policy](https://docs.aws.amazon.com/mpa/latest/APIReference/API_Policy.html): Contains details for a policy.
- [PolicyReference](https://docs.aws.amazon.com/mpa/latest/APIReference/API_PolicyReference.html): Contains the Amazon Resource Name (ARN) for a policy.
- [PolicyVersion](https://docs.aws.amazon.com/mpa/latest/APIReference/API_PolicyVersion.html): Contains details for the version of a policy.
- [PolicyVersionSummary](https://docs.aws.amazon.com/mpa/latest/APIReference/API_PolicyVersionSummary.html): Contains details for the version of a policy.


## [Service-specific Errors](https://docs.aws.amazon.com/mpa/latest/APIReference/API_Errors.html)

- [AccessDeniedException](https://docs.aws.amazon.com/mpa/latest/APIReference/API_AccessDeniedException.html): You do not have sufficient access to perform this action.
- [ConflictException](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ConflictException.html): The request cannot be completed because it conflicts with the current state of a resource.
- [InternalServerException](https://docs.aws.amazon.com/mpa/latest/APIReference/API_InternalServerException.html): The service encountered an internal error.
- [InvalidParameterException](https://docs.aws.amazon.com/mpa/latest/APIReference/API_InvalidParameterException.html): The request contains an invalid parameter value.
- [ResourceNotFoundException](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ResourceNotFoundException.html): The specified resource doesn't exist.
- [ServiceQuotaExceededException](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ServiceQuotaExceededException.html): The request exceeds the service quota for your account.
- [ThrottlingException](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ThrottlingException.html): The request was denied due to request throttling.
- [TooManyTagsException](https://docs.aws.amazon.com/mpa/latest/APIReference/API_TooManyTagsException.html): The request exceeds the maximum number of tags allowed for this resource.
- [ValidationException](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ValidationException.html): The input fails to satisfy the constraints specified by an AWS service.
