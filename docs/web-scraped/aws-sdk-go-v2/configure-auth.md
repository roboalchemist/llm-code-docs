# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-auth.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#configure-auth "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

DefinitionsAuth scheme resolution workflowNatively-supported AuthSchemes

# Configure Authentication

The AWS SDK for Go provides the ability to configure the authentication behavior service. In most cases, the default configuration will suffice, but configuring custom authentication allows for additional behavior such as working with pre-release service features. 

## Definitions

This section provides a high-level description of authentication components in the AWS SDK for Go. 

### AuthScheme

An [AuthScheme](https://pkg.go.dev/github.com/aws/smithy-go/transport/http#AuthScheme) is the interface that defines the workflow through which the SDK retrieves a caller identity and attaches it to an operation request. 

An auth scheme uses the following components, described in detail further below: 

  * A unique ID which identifies the scheme 

  * An identity resolver, which returns a caller identity used in the signing process (e.g. your AWS credentials) 

  * A signer, which performs the actual injection of caller identity into the operation's transport request (e.g. the `Authorization` HTTP header) 




Each service client options includes an `AuthSchemes` field, which by default is populated with the list of auth schemes supported by that service. 

### AuthSchemeResolver

Each service client options includes an `AuthSchemeResolver` field. This interface, defined per-service, is the API called by the SDK to determine the possible authentication options for each operation. 

###### Important

The auth scheme resolver does NOT dictate what auth scheme is used. It returns a list of schemes that _can_ be used ("options"), the final scheme is selected through a fixed algorithm described here. 

### Option

Returned from a call to `ResolverAuthSchemes`, an [Option](https://pkg.go.dev/github.com/aws/smithy-go/auth#Option) represents a possible authentication option. 

An option consists of three sets of information: 

  * An ID representing the possible scheme 

  * An opaque set of properties to be provided to the scheme's identity resolver 

  * An opaque set of properties to be provided to the scheme's signer 




#### A note on properties

For 99% of use cases, callers need not be concerned with the opaque properties for identity resolution and signing. The SDK will pull out the necessary properties for each scheme and pass them to the strongly-typed interfaces exposed in the SDK. For example, the default auth resolver for services encode the SigV4 option to have signer properties for the signing name and region, the values of which are passed to the client's configured [v4.HTTPSigner](https://pkg.go.dev/github.com/aws/smithy-go/auth#Option) implementation when SigV4 is selected. 

### Identity

An [Identity](https://pkg.go.dev/github.com/aws/smithy-go/auth#Identity) is an abstract representation of who the SDK caller is. 

The most common type of identity used in the SDK is a set of `aws.Credentials`. For most use cases, the caller need not concern themselves with `Identity` as an abstraction and can work with the concrete types directly. 

###### Note

To preserve backwards compatibility and prevent API confusion, the AWS SDK-specific identity type `aws.Credentials` does not directly satisfy the `Identity` interface. This mapping is handled internally. 

### IdentityResolver

[IdentityResolver](https://pkg.go.dev/github.com/aws/smithy-go/auth#IdentityResolver) is the interface through which an `Identity` is retrieved. 

Concrete versions of `IdentityResolver` exist in the SDK in strongly-typed form (e.g. [aws.CredentialsProvider](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#CredentialsProvider)), the SDK handles this mapping internally. 

A caller will only need to directly implement the `IdentityResolver` interface when defining an external auth scheme. 

### Signer

[Signer](https://pkg.go.dev/github.com/aws/smithy-go/transport/http#Signer) is the interface through which a request is supplemented with the retrieved caller `Identity`. 

Concrete versions of `Signer` exist in the SDK in strongly-typed form (e.g. [v4.HTTPSigner](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws/signer/v4#HTTPSigner)), the SDK handles this mapping internally. 

A caller will only need to directly implement the `Signer` interface when defining an external auth scheme. 

### AuthResolverParameters

Each service takes a specific set of inputs which are passed to its resolution function, defined in each service package as `AuthResolverParameters`. 

The base resolver parameters are as follows: 

name  |  type  |  description   
---|---|---  
`Operation` |  `string` |  The name of the operation being invoked.   
`Region` |  `string` |  The client's AWS region. Only present for services that use SigV4[A].   
  
If you are implementing your own resolver, you should never need to construct your own instance of its parameters. The SDK will source these values per-request and pass them to your implementation. 

## Auth scheme resolution workflow

When you call an AWS service operation through the SDK, the following sequence of actions occurs after the request has been serialized: 

  1. The SDK calls the client's `AuthSchemeResolver.ResolveAuthSchemes()` API, sourcing the input parameters as necessary, to obtain a list of possible [Options](https://pkg.go.dev/github.com/aws/smithy-go/auth#Option) for the operation. 

  2. The SDK iterates over that list and selects the first scheme that satisfies the following conditions. 

     * A scheme with matching ID is present in the client's own `AuthSchemes` list 

     * The scheme's identity resolver exists (is non-`nil`) on the client's Options (checked via the scheme's `GetIdentityResolver` method, the mapping to the concrete identity resolver types described above is handled internally) (1) 

  3. Assuming a viable scheme was selected, the SDK invokes its `GetIdentityResolver()` API to retrieve the caller's identity. For example, the builtin SigV4 auth scheme will map to the client's `Credentials` provider internally. 

  4. The SDK calls the identity resolver's `GetIdentity()` (e.g. `aws.CredentialProvider.Retrieve()` for SigV4). 

  5. The SDK calls the endpoint resolver's `ResolveEndpoint()` to find the endpoint for the request. The endpoint may include additional metadata that influences the signing process (e.g. unique signing name for S3 Object Lambda). 

  6. The SDK calls the auth scheme's `Signer()` API to retrieve its signer, and uses its `SignRequest()` API to sign the request with the previously-retrieved caller identity. 




(1) If the SDK encounters the anonymous option (ID `smithy.api#noAuth`) in the list, it is selected automatically, as there is no corresponding identity resolver. 

## Natively-supported `AuthScheme`s

The following auth schemes are natively supported by AWS SDK for Go. 

Name  |  Scheme ID  |  Identity resolver  |  Signer  |  Notes   
---|---|---|---|---  
[SigV4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) |  `aws.auth#sigv4` |  [aws.CredentialsProvider](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#Credentials) |  [v4.HTTPSigner](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws/signer/v4#Signer) |  The current default for most AWS service operations.   
SigV4A  |  `aws.auth#sigv4a` |  aws.CredentialsProvider  |  n/a  |  SigV4A usage is limited at this time, the signer implementation is internal. See this [announcement](https://github.com/aws/aws-sdk-go-v2/discussions/2812) for a new opt-in module _aws-http-auth_ that exposes general purpose APIs for signing HTTP requests.   
SigV4Express  |  `com.amazonaws.s3#sigv4express` |  [s3.ExpressCredentialsProvider](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#ExpressCredentialsProvider) |  v4.HTTPSigner  |  Used for [Express One Zone](https://aws.amazon.com/s3/storage-classes/express-one-zone/).   
HTTP Bearer  |  `smithy.api#httpBearerAuth` |  [smithybearer.TokenProvider](https://pkg.go.dev/github.com/aws/smithy-go/auth/bearer#TokenProvider) |  [smithybearer.Signer](https://pkg.go.dev/github.com/aws/smithy-go/auth/bearer#Signer) |  Used by [codecatalyst](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/codecatalyst).   
Anonymous  |  `smithy.api#noAuth` |  n/a  |  n/a  |  No authentication - no identity is required, and the request is not signed or authenticated.   
  
### Identity configuration

In AWS SDK for Go, the identity components of an auth scheme are configured in SDK client `Options`. The SDK will automatically pick up and use the values for these components for the scheme it selects when an operation is called. 

###### Note

For backwards compatibility reasons, the SDK implicitly allows the use of the anonymous auth scheme if no identity resolvers are configured. This can be manually achieved by setting all identity resolvers on a client's `Options` to `nil` (the sigv4 identity resolver can also be set to `aws.AnonymousCredentials{}`). 

### Signer configuration

In AWS SDK for Go, the signer components of an auth scheme are configured in SDK client `Options`. The SDK will automatically pick up and use the values for these components for the scheme it selects when an operation is called. No additional configuration is necessary. 

#### Custom auth scheme

In order to define a custom auth scheme and configure it for use, the caller must do the following: 

  1. Define an [AuthScheme](https://pkg.go.dev/github.com/aws/smithy-go/transport/http#AuthScheme) implementation 

  2. Register the scheme on the SDK client's `AuthSchemes` list 

  3. Instrument the SDK client's `AuthSchemeResolver` to return an auth `Option` with the scheme's ID where applicable 




###### Warning

The following services have unique or customized authentication behavior. We recommend you delegate to the default implementation and wrap accordingly if you require custom authentication behavior: 

Service  |  Notes   
---|---  
S3  |  Conditional use of SigV4A and SigV4Express depending on operation input.   
EventBridge  |  Conditional use of SigV4A depending on operation input.   
Cognito  |  Certain operations are anonymous-only.   
SSO  |  Certain operations are anonymous-only.   
STS  |  Certain operations are anonymous-only.   
  
![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Configure the SDK

Client Endpoints

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
