# Source: https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/llms.txt

# AWS IAM Identity Center Portal API Reference

> AWS IAM Identity Center Portal is a web service that you can use to assign your users access to IAM Identity Center resources such as the AWS access portal. The AWS access portal provides your users with single sign-on access to their assigned AWS accounts and applications. For information about how to assign your users access to AWS accounts and applications, see the IAM Identity Center User Guide.

- [Welcome](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_Operations.html)

- [GetRoleCredentials](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.html): Returns the STS short-term credentials for a given role name that is assigned to the user.
- [ListAccountRoles](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_ListAccountRoles.html): Lists all roles that are assigned to the user for a given AWS account.
- [ListAccounts](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_ListAccounts.html): Lists all AWS accounts assigned to the user.
- [Logout](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_Logout.html): Removes the locally stored SSO tokens from the client-side cache and sends an API call to the IAM Identity Center service to invalidate the corresponding server-side IAM Identity Center sign in session.


## [Data Types](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_Types.html)

- [AccountInfo](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_AccountInfo.html): Provides information about your AWS account.
- [RoleCredentials](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_RoleCredentials.html): Provides information about the role credentials that are assigned to the user.
- [RoleInfo](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_RoleInfo.html): Provides information about the role that is assigned to the user.
