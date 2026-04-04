# Source: https://docs.aws.amazon.com/grafana/latest/APIReference/llms.txt

# Amazon Managed Grafana API Reference

> Amazon Managed Grafana is a fully managed and secure data visualization service that you can use to instantly query, correlate, and visualize operational metrics, logs, and traces from multiple sources. Amazon Managed Grafana makes it easy to deploy, operate, and scale Grafana, a widely deployed data visualization tool that is popular for its extensible data support.

- [Welcome](https://docs.aws.amazon.com/grafana/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/grafana/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/grafana/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/grafana/latest/APIReference/API_Operations.html)

- [AssociateLicense](https://docs.aws.amazon.com/grafana/latest/APIReference/API_AssociateLicense.html): Assigns a Grafana Enterprise license to a workspace.
- [CreateWorkspace](https://docs.aws.amazon.com/grafana/latest/APIReference/API_CreateWorkspace.html): Creates a workspace.
- [CreateWorkspaceApiKey](https://docs.aws.amazon.com/grafana/latest/APIReference/API_CreateWorkspaceApiKey.html): Creates a Grafana API key for the workspace.
- [CreateWorkspaceServiceAccount](https://docs.aws.amazon.com/grafana/latest/APIReference/API_CreateWorkspaceServiceAccount.html): Creates a service account for the workspace.
- [CreateWorkspaceServiceAccountToken](https://docs.aws.amazon.com/grafana/latest/APIReference/API_CreateWorkspaceServiceAccountToken.html): Creates a token that can be used to authenticate and authorize Grafana HTTP API operations for the given workspace service account.
- [DeleteWorkspace](https://docs.aws.amazon.com/grafana/latest/APIReference/API_DeleteWorkspace.html): Deletes an Amazon Managed Grafana workspace.
- [DeleteWorkspaceApiKey](https://docs.aws.amazon.com/grafana/latest/APIReference/API_DeleteWorkspaceApiKey.html): Deletes a Grafana API key for the workspace.
- [DeleteWorkspaceServiceAccount](https://docs.aws.amazon.com/grafana/latest/APIReference/API_DeleteWorkspaceServiceAccount.html): Deletes a workspace service account from the workspace.
- [DeleteWorkspaceServiceAccountToken](https://docs.aws.amazon.com/grafana/latest/APIReference/API_DeleteWorkspaceServiceAccountToken.html): Deletes a token for the workspace service account.
- [DescribeWorkspace](https://docs.aws.amazon.com/grafana/latest/APIReference/API_DescribeWorkspace.html): Displays information about one Amazon Managed Grafana workspace.
- [DescribeWorkspaceAuthentication](https://docs.aws.amazon.com/grafana/latest/APIReference/API_DescribeWorkspaceAuthentication.html): Displays information about the authentication methods used in one Amazon Managed Grafana workspace.
- [DescribeWorkspaceConfiguration](https://docs.aws.amazon.com/grafana/latest/APIReference/API_DescribeWorkspaceConfiguration.html): Gets the current configuration string for the given workspace.
- [DisassociateLicense](https://docs.aws.amazon.com/grafana/latest/APIReference/API_DisassociateLicense.html): Removes the Grafana Enterprise license from a workspace.
- [ListPermissions](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListPermissions.html): Lists the users and groups who have the Grafana Admin and Editor roles in this workspace.
- [ListTagsForResource](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListTagsForResource.html): The ListTagsForResource operation returns the tags that are associated with the Amazon Managed Service for Grafana resource specified by the resourceArn.
- [ListVersions](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListVersions.html): Lists available versions of Grafana.
- [ListWorkspaces](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListWorkspaces.html): Returns a list of Amazon Managed Grafana workspaces in the account, with some information about each workspace.
- [ListWorkspaceServiceAccounts](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListWorkspaceServiceAccounts.html): Returns a list of service accounts for a workspace.
- [ListWorkspaceServiceAccountTokens](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListWorkspaceServiceAccountTokens.html): Returns a list of tokens for a workspace service account.
- [TagResource](https://docs.aws.amazon.com/grafana/latest/APIReference/API_TagResource.html): The TagResource operation associates tags with an Amazon Managed Grafana resource.
- [UntagResource](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UntagResource.html): The UntagResource operation removes the association of the tag with the Amazon Managed Grafana resource.
- [UpdatePermissions](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdatePermissions.html): Updates which users in a workspace have the Grafana Admin or Editor roles.
- [UpdateWorkspace](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspace.html): Modifies an existing Amazon Managed Grafana workspace.
- [UpdateWorkspaceAuthentication](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspaceAuthentication.html): Use this operation to define the identity provider (IdP) that this workspace authenticates users from, using SAML.
- [UpdateWorkspaceConfiguration](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspaceConfiguration.html): Updates the configuration string for the given workspace


## [Data Types](https://docs.aws.amazon.com/grafana/latest/APIReference/API_Types.html)

- [AssertionAttributes](https://docs.aws.amazon.com/grafana/latest/APIReference/API_AssertionAttributes.html): A structure that defines which attributes in the IdP assertion are to be used to define information about the users authenticated by the IdP to use the workspace.
- [AuthenticationDescription](https://docs.aws.amazon.com/grafana/latest/APIReference/API_AuthenticationDescription.html): A structure containing information about the user authentication methods used by the workspace.
- [AuthenticationSummary](https://docs.aws.amazon.com/grafana/latest/APIReference/API_AuthenticationSummary.html): A structure that describes whether the workspace uses SAML, IAM Identity Center, or both methods for user authentication, and whether that authentication is fully configured.
- [AwsSsoAuthentication](https://docs.aws.amazon.com/grafana/latest/APIReference/API_AwsSsoAuthentication.html): A structure containing information about how this workspace works with IAM Identity Center.
- [IdpMetadata](https://docs.aws.amazon.com/grafana/latest/APIReference/API_IdpMetadata.html): A structure containing the identity provider (IdP) metadata used to integrate the identity provider with this workspace.
- [NetworkAccessConfiguration](https://docs.aws.amazon.com/grafana/latest/APIReference/API_NetworkAccessConfiguration.html): The configuration settings for in-bound network access to your workspace.
- [PermissionEntry](https://docs.aws.amazon.com/grafana/latest/APIReference/API_PermissionEntry.html): A structure containing the identity of one user or group and the Admin, Editor, or Viewer role that they have.
- [RoleValues](https://docs.aws.amazon.com/grafana/latest/APIReference/API_RoleValues.html): This structure defines which groups defined in the SAML assertion attribute are to be mapped to the Grafana Admin and Editor roles in the workspace.
- [SamlAuthentication](https://docs.aws.amazon.com/grafana/latest/APIReference/API_SamlAuthentication.html): A structure containing information about how this workspace works with SAML.
- [SamlConfiguration](https://docs.aws.amazon.com/grafana/latest/APIReference/API_SamlConfiguration.html): A structure containing information about how this workspace works with SAML.
- [ServiceAccountSummary](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ServiceAccountSummary.html): A structure that contains the information about one service account.
- [ServiceAccountTokenSummary](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ServiceAccountTokenSummary.html): A structure that contains the information about a service account token.
- [ServiceAccountTokenSummaryWithKey](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ServiceAccountTokenSummaryWithKey.html): A structure that contains the information about a service account token.
- [UpdateError](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateError.html): A structure containing information about one error encountered while performing an UpdatePermissions operation.
- [UpdateInstruction](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateInstruction.html): Contains the instructions for one Grafana role permission update in a UpdatePermissions operation.
- [User](https://docs.aws.amazon.com/grafana/latest/APIReference/API_User.html): A structure that specifies one user or group in the workspace.
- [ValidationExceptionField](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ValidationExceptionField.html): A structure that contains information about a request parameter that caused an error.
- [VpcConfiguration](https://docs.aws.amazon.com/grafana/latest/APIReference/API_VpcConfiguration.html): The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.
- [WorkspaceDescription](https://docs.aws.amazon.com/grafana/latest/APIReference/API_WorkspaceDescription.html): A structure containing information about an Amazon Managed Grafana workspace in your account.
- [WorkspaceSummary](https://docs.aws.amazon.com/grafana/latest/APIReference/API_WorkspaceSummary.html): A structure that contains some information about one workspace in the account.
