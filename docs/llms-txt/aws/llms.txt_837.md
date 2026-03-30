# Source: https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/llms.txt

# Amazon Verified Permissions User Guide

- [What is Amazon Verified Permissions?](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html)
- [Getting started with policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/getting-started-first-policy-store.html)
- [Designing an authorization model](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/design-authz-strategy.html)
- [Policy validation mode](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-validation-mode.html)
- [Working with AWS CloudFormation](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/cloudformation-verified-permissions.html)
- [Using AWS PrivateLink](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/vpc-interface-endpoints.html)
- [Quotas](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/quotas.html)
- [Cedar v4 FAQ](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/cedar4-faq.html)
- [Document history](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/doc-history.html)

## [Policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores.html)

### [Creating policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores-create.html)

Learn how to create a sample or OIDC policy store using the AWS Management Console and an empty policy store using the AWS Management Console, AWS CLI, or AWS SDKs.

- [Creating a policy store using Rust](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/code-samples-rust.html): Walk through an example AVP policy store set up using the AWS SDK for Rust.

### [API-linked policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores-api-userpool.html)

Describes how Amazon Verified Permissions builds policy stores with an Amazon API Gateway API and an identity source.

- [Moving to production](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores-api-userpool-considerations-production.html): Learn about moving Amazon Verified Permissions API-linked policy stores to production using CloudFormation.
- [Troubleshooting](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores-api-userpool-considerations-troubleshooting.html): Troubleshooting information for Amazon Verified Permissions API-linked policy stores.
- [Deleting policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores-delete.html): Learn how to delete Amazon Verified Permissions policy stores.


## [Policy store schema](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/schema.html)

- [Editing schema](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/schema-edit.html): Learn how to edit an Amazon Verified Permissions schema in JSON or visual mode in the AWS Management Console.


## [Policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies.html)

- [Creating static policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies-create.html): Learn how to create a Amazon Verified Permissions static policy for permitting or forbidding principals from taking certain actions on a specified resource.
- [Editing static policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies-edit.html): Learn how to edit an Amazon Verified Permissions static policy.
- [](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/context.html): Understand context in Verified Permissions and learn how to populate them to authorization requests and policies
- [Testing policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/test-bench.html): Understand the Amazon Verified Permissions test bench.
- [Example policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies-examples.html): See examples of Amazon Verified Permissions policies for allowing anyone, individual entities, groups of entities, or entities with certain attributes to access resources.


## [Policy templates and template-linked policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-templates.html)

- [Creating policy templates](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-templates-create.html): Learn how to create an Amazon Verified Permissions policy template for use creating template-linked policies.
- [Creating template-linked policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-templates-create-policy.html): Learn what Amazon Verified Permissions template-linked policies are and how to create them using the AWS Management Console, AWS CLI, or AWS SDKs.
- [Editing policy templates](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-templates-edit.html): Learn how to edit an Amazon Verified Permissions policy template.
- [Example template-linked policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-templates-example-policies.html): Examples of Amazon Verified Permissions template-linked policies for the sample policy stores.


## [Identity sources](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-sources.html)

### [Working with Amazon Cognito identity sources](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-sources-cognito.html)

Verified Permissions works closely with Amazon Cognito user pools.

- [Creating identity sources](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/cognito-create.html): Learn how to create an Amazon Verified Permissions identity source that works with Amazon Cognito using the AWS Management Console or the AWS CLI.
- [Editing identity sources](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/cognito-edit.html): Learn how to edit an Amazon Verified Permissions identity source that works with Amazon Cognito or an OIDC provider using the AWS Management Console or the AWS CLI.
- [Mapping tokens to schema](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/cognito-map-token-to-schema.html): Learn how to map Amazon Cognito tokens to Amazon Verified Permissions policy store schema.
- [Client and audience validation](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/cognito-validation.html): When you add an identity source to a policy store, Verified Permissions has configuration options that verify that ID and access tokens are being used as intended.

### [Working with OIDC identity sources](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-sources-oidc.html)

You can also configure any compliant OpenID Connect (OIDC) IdP as the identity source of a policy store.

- [Creating identity sources](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/oidc-create.html): Learn how to create an Amazon Verified Permissions identity source that works with an OIDC provider using the AWS Management Console or the AWS CLI.
- [Editing identity sources](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/oidc-edit.html): Learn how to edit an Amazon Verified Permissions identity source that works with Amazon Cognito or an OIDC provider using the AWS Management Console or the AWS CLI.
- [Mapping tokens to schema](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/oidc-map-token-to-schema.html): Learn how to map OIDC tokens to Amazon Verified Permissions policy store schema.
- [Client and audience validation](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/oidc-validation.html): When you add an identity source to a policy store, Verified Permissions has configuration options that verify that ID and access tokens are being used as intended.


## [Integrations](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/framework-integrations.html)

- [Using Express](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/integration-express.html): Implement authorization in your Express.js applications using the Amazon Verified Permissions Express integration.


## [Authorize requests](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/authorization.html)

- [Test model](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/authorization-testing.html): Use a tool that interacts with the Amazon Verified Permissions REST API to craft example authorization requests and test your policies and schema.
- [Integrating with applications](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/authorization-sdk.html): With Amazon Verified Permissions, you can add an AWS SDK to an application and generate authorization decisions using the authorization models from Verified Permissions.


## [Security](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security-data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Verified Permissions.

- [Customer managed keys](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security-data-protection-cmk.html): Learn how to use AWS Key Management Service customer managed keys to encrypt your Amazon Verified Permissions resources.

### [Identity and access management](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Amazon Verified Permissions resources.

- [How Amazon Verified Permissions works with IAM](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security_iam_service-with-iam.html): Learn more about the IAM features that are available.
- [IAM policies for Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security-iam-getting-started-policies.html): Verified Permissions manages the permissions of users within your application.
- [Identity-based policy examples](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security_iam_id-based-policy-examples.html): Learn about the best practices for identity-based policies.
- [AWS managed policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Verified Permissions and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security_iam_troubleshoot.html): Learn how to troubleshoot and fix common issues with Verified Permissions and IAM.
- [Compliance validation](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security-compliance-validation.html): Learn whether Amazon Verified Permissions is in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security-disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Verified Permissions features for data resiliency.


## [Monitoring](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/monitoring.html)

- [CloudTrail logs](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/monitoring-cloudtrail.html): Learn about logging Amazon Verified Permissions with AWS CloudTrail.


## [Terms & concepts](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/terminology.html)

- [Differences with Cedar](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/terminology-differences-avp-cedar.html): Learn about the differences between the Cedar policy language and the way Amazon Verified Permissions implements it.
