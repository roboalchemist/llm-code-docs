# Source: https://docs.aws.amazon.com/sdkref/latest/guide/llms.txt

# AWS SDKs and Tools Reference Guide

> A guide to common features and functionality of the AWS SDKs and developer tools. Includes maintenance and support policies, as well as a complete reference for configuring your AWS credentials and other settings.

- [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html)
- [Common Runtime](https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html)
- [Maintenance policy](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html)
- [Version lifecycle](https://docs.aws.amazon.com/sdkref/latest/guide/version-support-matrix.html)
- [Document history](https://docs.aws.amazon.com/sdkref/latest/guide/doc-history.html)

## [Configuration](https://docs.aws.amazon.com/sdkref/latest/guide/creds-config-files.html)

- [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html): Format and syntax specifications for the ~\.aws\config and ~\.aws\credentials file for the AWS Command Line Interface (AWS CLI), the AWS SDKs, and other tools.
- [Location of the shared files](https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html): Location of the shared config and credentials files on different operating systems.
- [Environment variables](https://docs.aws.amazon.com/sdkref/latest/guide/environment-variables.html): Environment variables provide another way to specify configuration options and credentials, and can be useful for scripting or temporarily setting a named profile as the default.
- [JVM system properties](https://docs.aws.amazon.com/sdkref/latest/guide/jvm-system-properties.html): JVM system properties provide another way to specify configuration options and credentials for SDKs that run on the JVM such as the AWS SDK for Java and the AWS SDK for Kotlin.


## [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html)

- [Login using console credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-login.html): Learn how to login using console credentials.

### [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html)

Learn how to configure AWS IAM Identity Center for your AWS SDKs and tools.

- [Understand IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/understanding-sso.html): Deep dive explanation of the authentication process for SDKs and tools using AWS IAM Identity Center.
- [IAM Roles Anywhere](https://docs.aws.amazon.com/sdkref/latest/guide/access-rolesanywhere.html): Learn how to authenticate calls for AWS SDKs and tools by using IAM Roles Anywhere.
- [Assume a role](https://docs.aws.amazon.com/sdkref/latest/guide/access-assume-role.html): Learn how to configure and assume a role.
- [Assume a role (web)](https://docs.aws.amazon.com/sdkref/latest/guide/access-assume-role-web.html): Learn how to configure and assume a role.

### [AWS access keys](https://docs.aws.amazon.com/sdkref/latest/guide/access-users.html)

To use the AWS SDKs to access AWS services, you need an AWS account and AWS credentials.

- [Short-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-temp-idc.html): Learn how to get temporary credentials from the AWS IAM Identity Center for your SDK or tool.
- [Long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html): Learn how to use long-term credentials from an IAM user to quickly get started using AWS SDKs and tools.
- [IAM roles for EC2 instances](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-roles-for-ec2.html): Sets up an IAM role to provide permissions for applications to use on Amazon EC2 instances
- [Trusted identity propagation](https://docs.aws.amazon.com/sdkref/latest/guide/access-tip.html): Learn how to use the trusted identity propagation (TIP) SDK plugin that streamlines the token exchange process for applications that authenticate outside of AWS via an external identity provider (IdP) such as Microsoft EntraID, Okta, and others.


## [Settings reference](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html)

### [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html)

Many credential providers have been standardized to consistent defaults and to work the same way across many SDKs.

- [AWS access keys](https://docs.aws.amazon.com/sdkref/latest/guide/feature-static-credentials.html): The AWS SDKs and tools can automatically use static credentials to sign API requests to AWS, so that your workloads can access your AWS resources and data securely and conveniently.
- [Login provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-login-credentials.html): You can use your existing AWS Management Console sign-in credentials to acquire short-term credentials that can be used for programmatic access.
- [Assume role provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-assume-role-credentials.html): SDK and tool settings to configure and assume a role.
- [Container provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-container-credentials.html): The container credential provider fetches credentials for customer's containerized application, such as Amazon Elastic Container Service and Amazon Elastic Kubernetes Service .
- [IAM Identity Center provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html): Learn how to configure profiles for IAM Identity Center so that they can use single sign-on authentication (SSO) to run AWS SDK code.
- [IMDS provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-credentials.html): Instance metadata is data about your instance that you can use to configure or manage a running Amazon Elastic Compute Cloud instance.
- [Process provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-process-credentials.html): SDKs provide a way to extend the credential provider chain for custom use cases.

### [Standardized features](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-features.html)

Many features have been standardized to consistent defaults and to work the same way across many SDKs.

- [Account-based endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-account-endpoints.html): Account-based endpoints help ensure high performance and scalability by using your AWS account ID to streamline the routing of AWS service requests for services that support this feature.
- [Application ID](https://docs.aws.amazon.com/sdkref/latest/guide/feature-appid.html): The application ID setting is a unique string you assign to your application to identify which of your applications makes calls to AWS.
- [Amazon EC2 instance metadata](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ec2-instance-metadata.html): Amazon EC2 provides a service on instances called the Instance Metadata Service (IMDS).
- [Amazon S3 access points](https://docs.aws.amazon.com/sdkref/latest/guide/feature-s3-access-point.html): The Amazon S3 service provides access points as an alternative way to interact with Amazon S3 buckets.
- [Amazon S3 Multi-Region Access Points](https://docs.aws.amazon.com/sdkref/latest/guide/feature-s3-mrap.html): Amazon S3 Multi-Region Access Points provide a global endpoint that applications can use to fulfill requests from Amazon S3 buckets located in multiple AWS Regions.
- [S3 Express One Zone session authentication](https://docs.aws.amazon.com/sdkref/latest/guide/feature-s3-express.html): AWS SDKs and tools can automatically use S3 Express One Zone session authentication to improve performance when making requests to S3 Express One Zone buckets.
- [Authentication scheme](https://docs.aws.amazon.com/sdkref/latest/guide/feature-auth-scheme.html): AWS SDKs and tools can be configured to prefer specific authentication schemes when multiple schemes are supported by a service.
- [AWS Region](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html): With AWS Regions, you can access AWS services that physically reside in a specific geographic area.
- [AWS STS Regional endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html): The AWS STS Regional endpoints feature specifies how the SDK determines the AWS service endpoint that it uses to talk to the AWS Security Token Service (AWS STS).
- [Data Integrity Protections](https://docs.aws.amazon.com/sdkref/latest/guide/feature-dataintegrity.html): AWS SDKs and tools can automatically perform integrity checks when uploading or downloading to Amazon S3.
- [Dual-stack and FIPS endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html): Dual-stack endpoints, which support both IPv4 and IPv6 traffic, and Federal Information Processing Standards (FIPS) endpoints.
- [Endpoint discovery](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoint-discovery.html): SDKs use endpoint discovery to access service endpoints (URLs to access various resources), while still maintaining flexibility for AWS to alter URLs as needed.
- [General configuration](https://docs.aws.amazon.com/sdkref/latest/guide/feature-gen-config.html): SDKs support some general settings that configure overall SDK behaviors.
- [Host prefix injection](https://docs.aws.amazon.com/sdkref/latest/guide/feature-host-prefix.html): Some AWS services use host prefixes in their API endpoints to route requests to the correct service components.
- [IMDS client](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-client.html): SDKs implement an Instance Metadata Service Version 2 (IMDSv2) client using session-oriented requests.
- [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html): Retry behavior includes settings regarding how the SDKs attempt to recover from failures resulting from requests made to AWS services.
- [Request compression](https://docs.aws.amazon.com/sdkref/latest/guide/feature-compression.html): AWS SDKs and tools can automatically compress payloads when sending requests to AWS services that support receiving compressed payloads.

### [Service-specific endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html)

Service-specific endpoint configuration provides the option to use an endpoint of your choosing for API requests and to have that choice persist.

- [Identifiers for service-specific endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/ss-endpoints-table.html): Complete list of all environment variables and service identifier keys for the configuration of service-specific endpoints.
- [Smart configuration defaults](https://docs.aws.amazon.com/sdkref/latest/guide/feature-smart-config-defaults.html): With the smart configuration defaults feature, AWS SDKs can provide predefined, optimized default values for other configuration settings.
