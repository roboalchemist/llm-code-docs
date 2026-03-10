# Source: https://docs.aws.amazon.com/STS/latest/APIReference/llms.txt

# AWS Security Token Service API Reference

> AWS Security Token Service (AWS STS) enables you to request temporary, limited-privilege credentials for users. This guide provides descriptions of the AWS STS API. For more information about using this service, see Temporary Security Credentials.

- [Welcome](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/STS/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/STS/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/STS/latest/APIReference/API_Operations.html)

- [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html): Returns a set of temporary security credentials that you can use to access AWS resources.
- [AssumeRoleWithSAML](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html): Returns a set of temporary security credentials for users who have been authenticated via a SAML authentication response.
- [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html): Returns a set of temporary security credentials for users who have been authenticated in a mobile or web application with a web identity provider.
- [AssumeRoot](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html): Returns a set of short term credentials you can use to perform privileged tasks on a member account in your organization.
- [DecodeAuthorizationMessage](https://docs.aws.amazon.com/STS/latest/APIReference/API_DecodeAuthorizationMessage.html): Decodes additional information about the authorization status of a request from an encoded message returned in response to an AWS request.
- [GetAccessKeyInfo](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetAccessKeyInfo.html): Returns the account identifier for the specified access key ID.
- [GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html): Returns details about the IAM user or role whose credentials are used to call the operation.
- [GetDelegatedAccessToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetDelegatedAccessToken.html): Exchanges a trade-in token for temporary AWS credentials with the permissions associated with the assumed principal.
- [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html): Returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for a user.
- [GetSessionToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html): Returns a set of temporary credentials for an AWS account or IAM user.
- [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html): Returns a signed JSON Web Token (JWT) that represents the calling AWS identity.


## [Data Types](https://docs.aws.amazon.com/STS/latest/APIReference/API_Types.html)

- [AssumedRoleUser](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumedRoleUser.html): The identifiers for the temporary security credentials that the operation returns.
- [Credentials](https://docs.aws.amazon.com/STS/latest/APIReference/API_Credentials.html): AWS credentials for API authentication.
- [FederatedUser](https://docs.aws.amazon.com/STS/latest/APIReference/API_FederatedUser.html): Identifiers for the federated user that is associated with the credentials.
- [PolicyDescriptorType](https://docs.aws.amazon.com/STS/latest/APIReference/API_PolicyDescriptorType.html): A reference to the IAM managed policy that is passed as a session policy for a role session or a federated user session.
- [ProvidedContext](https://docs.aws.amazon.com/STS/latest/APIReference/API_ProvidedContext.html): Contains information about the provided context.
- [Tag](https://docs.aws.amazon.com/STS/latest/APIReference/API_Tag.html): You can pass custom key-value pair attributes when you assume a role or federate a user.
