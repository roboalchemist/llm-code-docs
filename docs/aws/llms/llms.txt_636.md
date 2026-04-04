# Source: https://docs.aws.amazon.com/organizations/latest/APIReference/llms.txt

# AWS Organizations API reference

> AWS Organizations API Reference.

- [Welcome](https://docs.aws.amazon.com/organizations/latest/APIReference/Welcome.html)
- [API operations by account](https://docs.aws.amazon.com/organizations/latest/APIReference/action-reference.html)
- [Common Parameters](https://docs.aws.amazon.com/organizations/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/organizations/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Operations.html)

- [AcceptHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_AcceptHandshake.html): Accepts a handshake by sending an ACCEPTED response to the sender.
- [AttachPolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_AttachPolicy.html): Attaches a policy to a root, an organizational unit (OU), or an individual account.
- [CancelHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CancelHandshake.html): Cancels a .
- [CloseAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CloseAccount.html): Closes an AWS member account within an organization.
- [CreateAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccount.html): Creates an AWS account that is automatically a member of the organization whose credentials made the request.
- [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html): This action is available if all of the following are true:
- [CreateOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateOrganization.html): Creates an AWS organization.
- [CreateOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateOrganizationalUnit.html): Creates an organizational unit (OU) within a root or parent OU.
- [CreatePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreatePolicy.html): Creates a policy of a specified type that you can attach to a root, an organizational unit (OU), or an individual AWS account.
- [DeclineHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeclineHandshake.html): Declines a .
- [DeleteOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeleteOrganization.html): Deletes the organization.
- [DeleteOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeleteOrganizationalUnit.html): Deletes an organizational unit (OU) from a root or another OU.
- [DeletePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeletePolicy.html): Deletes the specified policy from your organization.
- [DeleteResourcePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeleteResourcePolicy.html): Deletes the resource policy from your organization.
- [DeregisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.html): Removes the specified member AWS account as a delegated administrator for the specified AWS service.
- [DescribeAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html): Retrieves AWS Organizations-related information about the specified account.
- [DescribeCreateAccountStatus](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeCreateAccountStatus.html): Retrieves the current status of an asynchronous request to create an account.
- [DescribeEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html): Returns the contents of the effective policy for specified policy type and account.
- [DescribeHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeHandshake.html): Returns details for a handshake.
- [DescribeOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeOrganization.html): Retrieves information about the organization that the user's account belongs to.
- [DescribeOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeOrganizationalUnit.html): Retrieves information about an organizational unit (OU).
- [DescribePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribePolicy.html): Retrieves information about a policy.
- [DescribeResourcePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeResourcePolicy.html): Retrieves information about a resource policy.
- [DescribeResponsibilityTransfer](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeResponsibilityTransfer.html): Returns details for a transfer.
- [DetachPolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DetachPolicy.html): Detaches a policy from a target root, organizational unit (OU), or account.
- [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html): Disables the integration of an AWS service (the service that is specified by ServicePrincipal) with AWS Organizations.
- [DisablePolicyType](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisablePolicyType.html): Disables an organizational policy type in a root.
- [EnableAllFeatures](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAllFeatures.html): Enables all features in an organization.
- [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html): Provides an AWS service (the service that is specified by ServicePrincipal) with permissions to view the structure of an organization, create a service-linked role in all the accounts in the organization, and allow the service to perform operations on behalf of the organization and its accounts.
- [EnablePolicyType](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html): Enables a policy type in a root.
- [InviteAccountToOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_InviteAccountToOrganization.html): Sends an invitation to another account to join your organization as a member account.
- [InviteOrganizationToTransferResponsibility](https://docs.aws.amazon.com/organizations/latest/APIReference/API_InviteOrganizationToTransferResponsibility.html): Sends an invitation to another organization's management account to designate your account with the specified responsibilities for their organization.
- [LeaveOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_LeaveOrganization.html): Removes a member account from its parent organization.
- [ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html): Lists all the accounts in the organization.
- [ListAccountsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccountsForParent.html): Lists the accounts in an organization that are contained by the specified target root or organizational unit (OU).
- [ListAccountsWithInvalidEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccountsWithInvalidEffectivePolicy.html): Lists all the accounts in an organization that have invalid effective policies.
- [ListAWSServiceAccessForOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAWSServiceAccessForOrganization.html): Returns a list of the AWS services that you enabled to integrate with your organization.
- [ListChildren](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListChildren.html): Lists all of the organizational units (OUs) or accounts that are contained in the specified parent OU or root.
- [ListCreateAccountStatus](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListCreateAccountStatus.html): Lists the account creation requests that match the specified status that is currently being tracked for the organization.
- [ListDelegatedAdministrators](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListDelegatedAdministrators.html): Lists the AWS accounts that are designated as delegated administrators in this organization.
- [ListDelegatedServicesForAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListDelegatedServicesForAccount.html): List the AWS services for which the specified account is a delegated administrator.
- [ListEffectivePolicyValidationErrors](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListEffectivePolicyValidationErrors.html): Lists all the validation errors on an effective policy for a specified account and policy type.
- [ListHandshakesForAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListHandshakesForAccount.html): Lists the recent handshakes that you have received.
- [ListHandshakesForOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListHandshakesForOrganization.html): Lists the recent handshakes that you have sent.
- [ListInboundResponsibilityTransfers](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListInboundResponsibilityTransfers.html): Lists transfers that allow you to manage the specified responsibilities for another organization.
- [ListOrganizationalUnitsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOrganizationalUnitsForParent.html): Lists the organizational units (OUs) in a parent organizational unit or root.
- [ListOutboundResponsibilityTransfers](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOutboundResponsibilityTransfers.html): Lists transfers that allow an account outside your organization to manage the specified responsibilities for your organization.
- [ListParents](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListParents.html): Lists the root or organizational units (OUs) that serve as the immediate parent of the specified child OU or account.
- [ListPolicies](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListPolicies.html): Retrieves the list of all policies in an organization of a specified type.
- [ListPoliciesForTarget](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListPoliciesForTarget.html): Lists the policies that are directly attached to the specified target root, organizational unit (OU), or account.
- [ListRoots](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html): Lists the roots that are defined in the current organization.
- [ListTagsForResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListTagsForResource.html): Lists tags that are attached to the specified resource.
- [ListTargetsForPolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListTargetsForPolicy.html): Lists all the roots, organizational units (OUs), and accounts that the specified policy is attached to.
- [MoveAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_MoveAccount.html): Moves an account from its current source parent root or organizational unit (OU) to the specified destination parent root or OU.
- [PutResourcePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_PutResourcePolicy.html): Creates or updates a resource policy.
- [RegisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RegisterDelegatedAdministrator.html): Enables the specified member account to administer the Organizations features of the specified AWS service.
- [RemoveAccountFromOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RemoveAccountFromOrganization.html): Removes the specified account from the organization.
- [TagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TagResource.html): Adds one or more tags to the specified resource.
- [TerminateResponsibilityTransfer](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TerminateResponsibilityTransfer.html): Ends a transfer.
- [UntagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UntagResource.html): Removes any tags with the specified keys from the specified resource.
- [UpdateOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UpdateOrganizationalUnit.html): Renames the specified organizational unit (OU).
- [UpdatePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UpdatePolicy.html): Updates an existing policy with a new name, description, or content.
- [UpdateResponsibilityTransfer](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UpdateResponsibilityTransfer.html): Updates a transfer.


## [Data Types](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Types.html)

- [Account](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Account.html): Contains information about an AWS account that is a member of an organization.
- [Child](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Child.html): Contains a list of child entities, either OUs or accounts.
- [CreateAccountStatus](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccountStatus.html): Contains the status about a or request to create an AWS account or an AWS GovCloud (US) account in an organization.
- [DelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DelegatedAdministrator.html): Contains information about the delegated administrator.
- [DelegatedService](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DelegatedService.html): Contains information about the AWS service for which the account is a delegated administrator.
- [EffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EffectivePolicy.html): Contains rules to be applied to the affected accounts.
- [EffectivePolicyValidationError](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EffectivePolicyValidationError.html): Contains details about the validation errors that occurred when generating or enforcing an effective policy, such as which policies contributed to the error and location of the error.
- [EnabledServicePrincipal](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnabledServicePrincipal.html): A structure that contains details of a service principal that represents an AWS service that is enabled to integrate with AWS Organizations.
- [Handshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Handshake.html): Contains details for a handshake.
- [HandshakeFilter](https://docs.aws.amazon.com/organizations/latest/APIReference/API_HandshakeFilter.html): Contains the filter used to select the handshakes for an operation.
- [HandshakeParty](https://docs.aws.amazon.com/organizations/latest/APIReference/API_HandshakeParty.html): Contains details for a participant in a handshake.
- [HandshakeResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_HandshakeResource.html): Contains additional details for a handshake.
- [Organization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Organization.html): Contains details about an organization.
- [OrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_OrganizationalUnit.html): Contains details about an organizational unit (OU).
- [Parent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Parent.html): Contains information about either a root or an organizational unit (OU) that can contain OUs or accounts in an organization.
- [Policy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Policy.html): Contains rules to be applied to the affected accounts.
- [PolicySummary](https://docs.aws.amazon.com/organizations/latest/APIReference/API_PolicySummary.html): Contains information about a policy, but does not include the content.
- [PolicyTargetSummary](https://docs.aws.amazon.com/organizations/latest/APIReference/API_PolicyTargetSummary.html): Contains information about a root, OU, or account that a policy is attached to.
- [PolicyTypeSummary](https://docs.aws.amazon.com/organizations/latest/APIReference/API_PolicyTypeSummary.html): Contains information about a policy type and its status in the associated root.
- [ResourcePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ResourcePolicy.html): A structure that contains details about a resource policy.
- [ResourcePolicySummary](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ResourcePolicySummary.html): A structure that contains resource policy ID and Amazon Resource Name (ARN).
- [ResponsibilityTransfer](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ResponsibilityTransfer.html): Contains details for a transfer.
- [Root](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Root.html): Contains details about a root.
- [Tag](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Tag.html): A custom key-value pair associated with a resource within your organization.
- [TransferParticipant](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TransferParticipant.html): Contains details for a participant in a transfer.
