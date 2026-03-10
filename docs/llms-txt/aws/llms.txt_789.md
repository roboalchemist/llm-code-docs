# Source: https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/llms.txt

# AWS IAM Identity Center OIDC API Reference

> AWS IAM Identity Center OpenID Connect (OIDC) is a web service that enables a client (such as AWS CLI or a native application) to register with IAM Identity Center. The service also enables the client to fetch the userâs access token upon successful authentication and authorization with IAM Identity Center.

- [Welcome](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_Operations.html)

- [CreateToken](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html): Creates and returns access and refresh tokens for clients that are authenticated using client secrets.
- [CreateTokenWithIAM](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.html): Creates and returns access and refresh tokens for authorized client applications that are authenticated using any IAM entity, such as a service role or user.
- [RegisterClient](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_RegisterClient.html): Registers a publicÂ client with IAM Identity Center.
- [StartDeviceAuthorization](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_StartDeviceAuthorization.html): Initiates device authorization by requesting a pair of verification codes from the authorization service.


## [Data Types](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_Types.html)

- [AwsAdditionalDetails](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_AwsAdditionalDetails.html): This structure contains AWS-specific parameter extensions and the identity context.
