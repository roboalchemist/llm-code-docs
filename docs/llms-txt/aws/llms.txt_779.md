# Source: https://docs.aws.amazon.com/signin/latest/APIReference/llms.txt

# AWS Sign-In Welcome

## [AWS SignIn Control Plane](https://docs.aws.amazon.com/signin/latest/APIReference/Welcome_AWS_SignIn_Control_Plane.html)

With AWS Sign-In, you can access AWS resources using an AWS Builder ID, or as a root user, IAM user, user in IAM Identity Center, or federated user. For more information about how to sign in to AWS depending on your user type, see [What is AWS Sign-In?](/signin/latest/userguide/what-is-sign-in.html).

This guide provides information about API actions for identity-aware sessions. For more information, see [Enabling identity-aware console sessions](/singlesignon/latest/userguide/awsapps.html#identity-aware-sessions).

### Actions

- [CreateTrustedIdentityPropagationApplicationForConsole](https://docs.aws.amazon.com/signin/latest/APIReference/API_CreateTrustedIdentityPropagationApplicationForConsole.html): Creates an IAM Identity Center application that represents the AWS Management Console on an IAM Identity Center organization instance.
- [ListTrustedIdentityPropagationApplicationsForConsole](https://docs.aws.amazon.com/signin/latest/APIReference/API_ListTrustedIdentityPropagationApplicationsForConsole.html): Lists an IAM Identity Center application that represents the AWS Management Console.

### Data Types

- [ValidationExceptionField](https://docs.aws.amazon.com/signin/latest/APIReference/API_ValidationExceptionField.html): Returns information about a field passed inside a request that resulted in an exception.

## [AWS Sign-In Data Plane](https://docs.aws.amazon.com/signin/latest/APIReference/Welcome_AWS_Sign-In_Data_Plane.html)

The AWS Sign-In Data Plane implements OAuth 2.0 flows for AWS CLI authentication, providing secure token exchange and refresh capabilities.

### Actions

- [AuthorizeOAuth2Access](https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_AuthorizeOAuth2Access.html): Grants permission to authenticate through a browser and obtain an OAuth 2.0 authorization code for credential exchange.
- [CreateOAuth2Token](https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateOAuth2Token.html): Grants permission to exchange an authorization code for OAuth 2.0 access token and refresh token that can be used to access AWS services from developer tools and applications.

### Data Types

- [AccessToken](https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_AccessToken.html): The AWS access credentials.
- [CreateOAuth2TokenRequestBody](https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateOAuth2TokenRequestBody.html): Input structure for the CreateOAuth2Token operation.
- [CreateOAuth2TokenResponseBody](https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateOAuth2TokenResponseBody.html): Output structure for CreateOAuth2Token operation.

## Common

- [Common Parameters](https://docs.aws.amazon.com/signin/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/signin/latest/APIReference/CommonErrors.html)