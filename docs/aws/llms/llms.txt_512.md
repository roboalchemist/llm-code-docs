# Source: https://docs.aws.amazon.com/kms/latest/developerguide/llms.txt

# AWS Key Management Service Developer Guide

> Learn how to use AWS Key Management Service (AWS KMS) to securely store and manage encryption keys and perform encryption and decryption of user data.

- [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
- [Enable and disable keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html)
- [Generate data key pairs](https://docs.aws.amazon.com/kms/latest/developerguide/data-key-pairs.html)
- [Document history](https://docs.aws.amazon.com/kms/latest/developerguide/dochistory.html)

## [Accessing AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/kms/latest/developerguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.

### [Hybrid post-quantum TLS](https://docs.aws.amazon.com/kms/latest/developerguide/pqtls.html)

Learn how to use hybrid post-quantum key agreement algorithms for your AWS KMS transactions.

- [Configure hybrid post-quantum TLS](https://docs.aws.amazon.com/kms/latest/developerguide/pqtls-how-to.html): In this procedure, add a Maven dependency for the AWS Common Runtime HTTP Client.

### [Connect to AWS KMS through a VPC endpoint](https://docs.aws.amazon.com/kms/latest/developerguide/kms-vpc-endpoint.html)

Learn how to connect to AWS KMS) from a private endpoint in your VPC.

- [Create a VPC endpoint for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/vpce-create-endpoint.html): You can create a VPC endpoint for AWS KMS by using the Amazon VPC console or the Amazon VPC API.
- [Connect to a VPC endpoint](https://docs.aws.amazon.com/kms/latest/developerguide/vpce-connect.html): You can connect to AWS KMS through the VPC endpoint by using an AWS SDK, the AWS CLI, or AWS Tools for PowerShell.
- [Use VPC endpoints to control access to AWS KMS resources](https://docs.aws.amazon.com/kms/latest/developerguide/vpce-policy-condition.html): You can control access to AWS KMS resources and operations when the request comes from VPC or uses a VPC endpoint.
- [Logging AWS KMS requests that use a VPC endpoint](https://docs.aws.amazon.com/kms/latest/developerguide/vpce-logging.html): AWS CloudTrail logs all operations that use the VPC endpoint.
- [Dual-stack endpoints](https://docs.aws.amazon.com/kms/latest/developerguide/ipv6-kms.html): Use both IPv4 and IPv6 to communicate with AWS KMS


## [Concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts-intro.html)

### [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)

- [Asymmetric keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html): Learn how to use asymmetric KMS keys and data keys.
- [HMAC keys](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html): Learn how to create, use, and manage HMAC KMS keys.
- [ML-DSA keys](https://docs.aws.amazon.com/kms/latest/developerguide/mldsa.html): Learn about ML-DSA KMS keys.

### [Multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html)

Learn how to create and use multi-Region keys

- [Security considerations for multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/mrk-when-to-use.html): Use an AWS KMS multi-Region key only when you need one.
- [How multi-Region keys work](https://docs.aws.amazon.com/kms/latest/developerguide/mrk-how-it-works.html): You begin by creating a symmetric or asymmetric multi-Region primary key in an AWS Region that AWS KMS supports, such as US East (N.

### [Imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html)

Learn the pros and cons of importing key material into AWS KMS and get an overview of the steps.

- [Special considerations for imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-considerations.html): Before you decide to import key material into AWS KMS, you should understand the following characteristics of imported key material.
- [Protecting imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/import-keys-protect.html): The key material that you import is protected in transit and at rest.
- [KMS keys in a CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/manage-cmk-keystore.html): You can create, view, manage, use, and schedule deletion of the AWS KMS keys in an AWS CloudHSM key store.
- [KMS keys in external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external-key-manage.html): To create, view, manage, use, and schedule deletion of the KMS keys in an external key store, you use procedures that are very similar to those you use for other KMS keys.
- [AWS KMS cryptography essentials](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html): AWS KMS uses configurable cryptographic algorithms so that the system can quickly migrate from one approved algorithm, or mode, to another.
- [Supported algorithms](https://docs.aws.amazon.com/kms/latest/developerguide/supported-algorithms.html): Provides an overview of cryptographic algorithms used by AWS services, including their status as preferred or acceptable.


## [KMS key access and permissions](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html)

### [Key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html)

Use key policies (resource-based policies) to specify permissions and control access to your AWS KMS keys.

- [Creating a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-overview.html): You can create and manage key policies in the AWS KMS console or by using AWS KMS API operations, such as CreateKey, ReplicateKey, and PutKeyPolicy.
- [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html): When you create a KMS key, you can specify the key policy for the new KMS key.
- [View a key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-viewing.html): Learn how to view the key policy for an AWS KMS key in AWS Key Management Service (AWS KMS).
- [Change a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html): Use the AWS Management Console and the AWS Key Management Service (AWS KMS) API to change the key policies that control access to your customer managed keys
- [Permissions for AWS services](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-services.html): Many AWS services use AWS KMS keys to protect the resources they manage.

### [IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html)

Use IAM policies (identity-based policies) to specify permissions and control access to your AWS KMS keys in AWS Key Management Service (AWS KMS).

- [Best practices for IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies-best-practices.html): Securing access to AWS KMS keys is critical to the security of all of your AWS resources.
- [Specifying KMS keys in IAM policy statements](https://docs.aws.amazon.com/kms/latest/developerguide/cmks-in-iam-policies.html): You can use an IAM policy to allow a principal to use or manage KMS keys.
- [Examples](https://docs.aws.amazon.com/kms/latest/developerguide/customer-managed-policies.html): In this section, you can find example IAM policies that allow permissions for various AWS KMS actions.
- [Resource control policies](https://docs.aws.amazon.com/kms/latest/developerguide/resource-control-policies.html): Learn how to use resource control policies in AWS Organizations to centrally establish a data perimeter across your AWS environment and restrict external access to your KMS keys

### [Grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html)

Use grants to allow access to AWS KMS keys in AWS Key Management Service (AWS KMS).

- [Best practices](https://docs.aws.amazon.com/kms/latest/developerguide/grant-best-practices.html): AWS KMS recommends the following best practices when creating, using, and managing grants.
- [Controlling access to grants](https://docs.aws.amazon.com/kms/latest/developerguide/grant-authorization.html): You can control access to the operations that create and manage grants in key policies, IAM policies, and in grants.
- [Creating grants](https://docs.aws.amazon.com/kms/latest/developerguide/create-grant-overview.html): Before creating a grant, learn about the options for customizing your grant.
- [Viewing grants](https://docs.aws.amazon.com/kms/latest/developerguide/grant-view.html): To view the grant, use the ListGrants operation.
- [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html): The AWS KMS API follows an eventual consistency model.
- [Retiring and revoking grants](https://docs.aws.amazon.com/kms/latest/developerguide/grant-delete.html): To delete a grant, retire or revoke it.

### [Condition keys](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html)

Use AWS Key Management Service (AWS KMS) condition keys (context keys) in a permissions policy.

- [AWS global condition keys](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-aws.html): AWS defines global condition keys, a set of policy conditions keys for all AWS services that use IAM for access control.
- [AWS KMS condition keys](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html): AWS KMS provides a set of condition keys that you can use in key policies and IAM policies.

### [AWS KMS condition keys for attested platforms](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-attestation.html)

AWS KMS provides condition keys to support cryptographic attestation for AWS Nitro Enclaves and NitroTPM.

- [Condition keys for Nitro Enclaves](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclave.html): The following condition keys are specific to Nitro Enclaves attestation:
- [Condition keys for NitroTPM](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html): The following condition keys are specific to NitroTPM attestation:
- [Least-privilege permissions](https://docs.aws.amazon.com/kms/latest/developerguide/least-privilege.html): Learn more about how to apply the security best practice of least-privilege permissions.

### [Attribute-based access control (ABAC)](https://docs.aws.amazon.com/kms/latest/developerguide/abac.html)

Learn how to use attribute-based access control (ABAC) for AWS KMS keys

- [Troubleshooting ABAC for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/troubleshooting-tags-aliases.html): Controlling access to KMS keys based on their tags and aliases is convenient and powerful.
- [Role-based access control (RBAC)](https://docs.aws.amazon.com/kms/latest/developerguide/rbac.html): Learn more about role-based access control strategies that you can use to apply the best practices of least-privilege permissions.
- [Cross-account access](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html): You can allow users or roles in a different AWS account to use a KMS key in your account.
- [Control access to multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-auth.html): Learn about permissions required for using and managing multi-Region keys

### [Determining access](https://docs.aws.amazon.com/kms/latest/developerguide/determining-access.html)

Learn how to determine who can access an AWS KMS key in AWS Key Management Service (AWS KMS).

- [Examining the key policy](https://docs.aws.amazon.com/kms/latest/developerguide/determining-access-key-policy.html): Key policies are the primary way to control access to KMS keys.
- [Examining IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/determining-access-iam-policies.html): In addition to the key policy and grants, you can also use IAM policies to allow access to a KMS key.
- [Examining grants](https://docs.aws.amazon.com/kms/latest/developerguide/determining-access-grants.html): Grants are advanced mechanisms for specifying permissions that you or an AWS service integrated with AWS KMS can use to specify how and when a KMS key can be used.
- [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html)
- [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html): Learn how to check that your AWS Key Management Service (AWS KMS) API calls succeed.
- [Troubleshooting AWS KMS permissions](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html): Access to a KMS key is determined by the key policy, IAM policies, and grants.
- [Glossary](https://docs.aws.amazon.com/kms/latest/developerguide/access-glossary.html): Learn about important terms in AWS KMS access control


## [Create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html)

- [Create a symmetric encryption KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-symmetric-cmk.html): This topic explains how to create the basic KMS key, a symmetric encryption KMS key for a single Region with key material from AWS KMS.
- [Create an asymmetric KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/asymm-create-key.html): You can create asymmetric KMS keys in the AWS KMS console, by using the CreateKey API, or by using the AWS::KMS::Key CloudFormation template.
- [Create an HMAC KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html): You can create HMAC KMS keys in the AWS KMS console, by using the CreateKey API, or by using the AWS::KMS::Key CloudFormation template.
- [Create multi-Region primary keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-primary-keys.html): You can create a multi-Region primary key in the AWS KMS console or by using the AWS KMS API.
- [Create multi-Region replica keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-replicate.html): Learn how to create multi-Region replica keys

### [Create a KMS key with imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-conceptual.html)

Imported key material lets you protect your AWS resources under cryptographic keys that you generate.

- [Step 1: Create an AWS KMS key without key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-create-cmk.html): To import your own key material, follow these steps to create an AWS KMS key with no key material.
- [Step 2: Download the wrapping public key and import token](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-get-public-key-and-token.html): After you create an encryption KMS key with no key material, download a wrapping public key and import token for that KMS key.
- [Step 3: Encrypt the key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-encrypt-key-material.html): Use the public key to encrypt your key material before sending the encrypted key material to AWS KMS.
- [Step 4: Import the key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-import-key-material.html): After you encrypt your key material, upload it to AWS KMS with your downloaded import token to import your key material.
- [Create a KMS key in an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-cmk-keystore.html): After you have created an AWS CloudHSM key store, you can create AWS KMS keys in your key store.
- [Create a KMS key in external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/create-xks-keys.html): After you have created and connected your external key store, you can create AWS KMS keys in your key store.


## [Identify and view keys](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html)

- [Find the key ID and key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/find-cmk-id-arn.html): To identify an AWS KMS key, you can use the key ID or the Amazon Resource Name (key ARN).
- [Access and list KMS key details](https://docs.aws.amazon.com/kms/latest/developerguide/finding-keys.html): You can use the AWS KMS console or the DescribeKey operation to access and list detailed information about the KMS keys in the account and Region.
- [Identify different key types](https://docs.aws.amazon.com/kms/latest/developerguide/identify-key-types.html): The following topics explain how to identify different key types in the AWS KMS console and DescribeKey responses.
- [Customize your console view](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-console-customize.html): You can customize the view of the AWS KMS console to make it easier to find your KMS keys.

### [Find KMS keys and key material in an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/find-key-material.html)

If you manage an AWS CloudHSM key store, you might need to identify the KMS keys in each AWS CloudHSM key store.

- [Find the KMS keys in an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/find-cmk-in-keystore.html): If you manage an AWS CloudHSM key store, you might need to identify the KMS keys in each AWS CloudHSM key store.
- [Find all keys for an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/find-all-kmsuser-keys.html): You can identify the keys in your AWS CloudHSM cluster that serve as key material for your AWS CloudHSM key store.
- [Find the KMS key for an AWS CloudHSM key](https://docs.aws.amazon.com/kms/latest/developerguide/find-label-for-key-handle.html): If you know the key reference or ID of a key that the kmsuser owns in the cluster, you can use that value to identify the associated KMS key in your AWS CloudHSM key store.
- [Find the AWS CloudHSM key for a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/find-handle-for-cmk-id.html): You can use the KMS key ID of a KMS key in an AWS CloudHSM key store to identify the key in your AWS CloudHSM cluster that serves as its key material.


## [Rotate keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)

- [Enable automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-enable.html): By default, when you enable automatic key rotation for a KMS key, AWS KMS generates new cryptographic material for the KMS key every year.
- [Disable automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-disable.html): Disable automatic key rotation for symmetric encryption customer managed keys using the AWS KMS console or DisableKeyRotation API operation.
- [Perform on-demand key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-on-demand.html): You can perform on-demand rotation of the key material in customer managed KMS keys, regardless of whether or not automatic key rotation is enabled.
- [List rotations and key materials](https://docs.aws.amazon.com/kms/latest/developerguide/list-rotations.html): KMS keys that support automatic or on-demand key rotation can have multiple key materials associated with them.
- [Rotate keys manually](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys-manually.html): You might want to create a new KMS key and use it in place of a current KMS key instead of using automatic or on-demand key rotation.
- [Change the primary key in a set of multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-update.html): Every set of related multi-Region keys must have a primary key.


## [Delete keys](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html)

- [Control access to key deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-adding-permission.html): If you use IAM policies to allow AWS KMS permissions, IAM identities that have AWS administrator access ("Action": "*") or AWS KMS full access ("Action": "kms:*") are already allowed to schedule and cancel key the deletion of KMS keys.
- [Schedule key deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html): The following procedures describe how to schedule key deletion and cancel key deletion of AWS KMS keys (KMS keys) in AWS KMS using the AWS Management Console and the AWS KMS API.
- [Cancel key deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-cancelling-key-deletion.html): After you schedule a KMS key for deletion, you can cancel the key deletion while it is still in the pending deletion state.
- [Create an alarm](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html): Learn how to create an Amazon CloudWatch alarm that notifies you when a person or application attempts to use a KMS key pending deletion.
- [Determine past usage of a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-determining-usage.html): Learn how to determine past usage of a KMS key in AWS Key Management Service (AWS KMS).
- [Delete imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-delete-key-material.html): Delete imported key material to make the AWS KMS keys unusable.


## [Generate data keys](https://docs.aws.amazon.com/kms/latest/developerguide/data-keys.html)

- [How unusable KMS keys affect data keys](https://docs.aws.amazon.com/kms/latest/developerguide/unusable-kms-keys.html): When a KMS key becomes unusable, the effect is almost immediate (subject to eventual consistency).


## [Perform offline operations with public keys](https://docs.aws.amazon.com/kms/latest/developerguide/offline-public-key.html)

- [Download public key](https://docs.aws.amazon.com/kms/latest/developerguide/download-public-key.html): You can download the public key from an asymmetric KMS key pair in the AWS KMS console or by using the GetPublicKey operation.
- [Example offline operations](https://docs.aws.amazon.com/kms/latest/developerguide/offline-operations.html): After downloading the public key of your asymmetric KMS key pair, you can share it with others and use it to perform offline operations.


## [Monitor keys](https://docs.aws.amazon.com/kms/latest/developerguide/monitoring-overview.html)

### [Logging with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html)

Learn how to audit AWS KMS keys with AWS CloudTrail.

### [Examples of AWS KMS log entries](https://docs.aws.amazon.com/kms/latest/developerguide/understanding-kms-entries.html)

AWS KMS writes entries to your CloudTrail log when you call an AWS KMS operation and when an AWS service calls an operation on your behalf.

- [CancelKeyDeletion](https://docs.aws.amazon.com/kms/latest/developerguide/ct-cancel-key-deletion.html): Contains an example of a log entry for a CancelKeyDeletion operation
- [ConnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/ct-connect-keystore.html): Contains an example of a log entry for a ConnectCustomKeyStore operation
- [CreateAlias](https://docs.aws.amazon.com/kms/latest/developerguide/ct-createalias.html): Contains a CreateAlias log example
- [CreateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/ct-create-keystore.html): Contains an example of a log entry for a CreateCustomKeyStore operation
- [CreateGrant](https://docs.aws.amazon.com/kms/latest/developerguide/ct-creategrant.html): Contains a CreateGrant log example
- [CreateKey](https://docs.aws.amazon.com/kms/latest/developerguide/ct-createkey.html): Contains CreateKey log examples
- [Decrypt](https://docs.aws.amazon.com/kms/latest/developerguide/ct-decrypt.html): Contains Decrypt log examples
- [DeleteAlias](https://docs.aws.amazon.com/kms/latest/developerguide/ct-deletealias.html): Contains a DeleteAlias log example
- [DeleteCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/ct-delete-keystore.html): Contains an example of a log entry for a DeleteCustomKeyStore operation
- [DeleteExpiredKeyMaterial](https://docs.aws.amazon.com/kms/latest/developerguide/ct-deleteexpiredkeymaterial.html): Contains an example of a log entry for the operation that deletes expired key material from a KMS key with imported key material that expires.
- [DeleteImportedKeyMaterial](https://docs.aws.amazon.com/kms/latest/developerguide/ct-deleteimportedkeymaterial.html): Contains an example of a log entry for the DeleteImportedKeyMaterial operation.
- [DeleteKey](https://docs.aws.amazon.com/kms/latest/developerguide/ct-delete-key.html): Contains examples of log entries for the operation that deletes a KMS key.
- [DescribeCustomKeyStores](https://docs.aws.amazon.com/kms/latest/developerguide/ct-describe-keystores.html): Contains an example of a log entry for a DescribeCustomKeyStores operation
- [DescribeKey](https://docs.aws.amazon.com/kms/latest/developerguide/ct-describekey.html): Contains a DescribeKey log example
- [DisableKey](https://docs.aws.amazon.com/kms/latest/developerguide/ct-disablekey.html): Contains a DisableKey log example
- [DisableKeyRotation](https://docs.aws.amazon.com/kms/latest/developerguide/ct-disable-key-rotation.html): Contains DisableKeyRotation CloudTrail log entry examples
- [DisconnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/ct-disconnect-keystore.html): Contains an example of a log entry for a DisconnectCustomKeyStore operation
- [EnableKey](https://docs.aws.amazon.com/kms/latest/developerguide/ct-enablekey.html): Contains an EnableKey log example
- [EnableKeyRotation](https://docs.aws.amazon.com/kms/latest/developerguide/ct-enablekeyrotation.html): Contains an example of a log entry for an EnableKeyRotation operation
- [Encrypt](https://docs.aws.amazon.com/kms/latest/developerguide/ct-encrypt.html): Contains an Encrypt log example
- [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/developerguide/ct-generatedatakey.html): Contains a GenerateDataKey log example
- [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/developerguide/ct-generatedatakeypair.html): Contains a GenerateDataKeyPair log example
- [GenerateDataKeyPairWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/developerguide/ct-generatedatakeypairwithoutplaintext.html): Contains a GenerateDataKeyPairWithoutPlaintext log example
- [GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/developerguide/ct-generatedatakeyplaintext.html): Contains a GenerateDataKeyWithoutPlaintext log example
- [GenerateMac](https://docs.aws.amazon.com/kms/latest/developerguide/ct-generatemac.html): Contains a GenerateMac log example
- [GenerateRandom](https://docs.aws.amazon.com/kms/latest/developerguide/ct-generaterandom.html): Contains a GenerateRandom log example
- [GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/developerguide/ct-getkeypolicy.html): Contains a GetKeyPolicy log example
- [GetKeyRotationStatus](https://docs.aws.amazon.com/kms/latest/developerguide/ct-getkeyrotationstatus.html): Contains a GetKeyRotationStatus log example
- [GetParametersForImport](https://docs.aws.amazon.com/kms/latest/developerguide/ct-getparametersforimport.html): Contains an example of a log entry for the operation that downloads the public import token that you use to import key material into a KMS key.
- [ImportKeyMaterial](https://docs.aws.amazon.com/kms/latest/developerguide/ct-importkeymaterial.html): Contains an example of a log entry for the operation that imports key material into a KMS key.
- [ListAliases](https://docs.aws.amazon.com/kms/latest/developerguide/ct-listaliases.html): Contains a ListAliases log example
- [ListGrants](https://docs.aws.amazon.com/kms/latest/developerguide/ct-listgrants.html): Contains a ListGrants log example
- [ListKeyRotations](https://docs.aws.amazon.com/kms/latest/developerguide/ct-listkeyrotations.html): Contains a ListKeyRotations log example
- [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/developerguide/ct-put-key-policy.html): Contains PutKeyPolicy CloudTrail log entry examples
- [ReEncrypt](https://docs.aws.amazon.com/kms/latest/developerguide/ct-reencrypt.html): Contains an ReEncrypt log example
- [ReplicateKey](https://docs.aws.amazon.com/kms/latest/developerguide/ct-replicate-key.html): Contains an example of a log entry for a ReplicateKey operation
- [RetireGrant](https://docs.aws.amazon.com/kms/latest/developerguide/ct-retire-grant.html): Contains an example of a log entry for a RetireGrant operation.
- [RevokeGrant](https://docs.aws.amazon.com/kms/latest/developerguide/ct-revoke-grant.html): Contains an example of a log entry for a RevokeGrant operation.
- [RotateKey](https://docs.aws.amazon.com/kms/latest/developerguide/ct-rotatekey.html): Contains an example of a log entry for the operation that rotates a KMS key.
- [RotateKeyOnDemand](https://docs.aws.amazon.com/kms/latest/developerguide/ct-rotatekeyondemand.html): Contains a RotateKeyOnDemand log example
- [ScheduleKeyDeletion](https://docs.aws.amazon.com/kms/latest/developerguide/ct-schedule-key-deletion.html): Contains examples of log entries for ScheduleKeyDeletion operations.
- [Sign](https://docs.aws.amazon.com/kms/latest/developerguide/ct-sign.html): Contains Sign log examples
- [SynchronizeMultiRegionKey](https://docs.aws.amazon.com/kms/latest/developerguide/ct-synchronize-multi-region-key.html): Contains an example of a log entry for an operation that synchronizes a multi-Region key.
- [TagResource](https://docs.aws.amazon.com/kms/latest/developerguide/ct-tagresource.html): Contains an example of a log entry for a TagResource operation
- [UntagResource](https://docs.aws.amazon.com/kms/latest/developerguide/ct-untagresource.html): Contains an example of a log entry for a UntagResource operation.
- [UpdateAlias](https://docs.aws.amazon.com/kms/latest/developerguide/ct-updatealias.html): Contains an UpdateAlias log example
- [UpdateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/ct-update-keystore.html): Contains an example of a log entry for a UpdateCustomKeyStore operation
- [UpdateKeyDescription](https://docs.aws.amazon.com/kms/latest/developerguide/ct-update-key-description.html): Contains UpdateKeyDescription CloudTrail log entry examples
- [UpdatePrimaryRegion](https://docs.aws.amazon.com/kms/latest/developerguide/ct-update-primary-region.html): Contains examples of the log entries for a UpdatePrimaryRegion operation
- [VerifyMac](https://docs.aws.amazon.com/kms/latest/developerguide/ct-verifymac.html): Contains a VerifyMac log example
- [Verify](https://docs.aws.amazon.com/kms/latest/developerguide/ct-verify.html): Contains Verify log examples
- [Amazon EC2 example one](https://docs.aws.amazon.com/kms/latest/developerguide/ct-ec2one.html): Contains an EC2 log example
- [Amazon EC2 example two](https://docs.aws.amazon.com/kms/latest/developerguide/ct-ec2two.html): Contains an EC2 log example

### [Monitor keys with CloudWatch](https://docs.aws.amazon.com/kms/latest/developerguide/monitoring-cloudwatch.html)

Understand the data that AWS Key Management Service (AWS KMS) sends to Amazon CloudWatch and how to use it.

- [Create a CloudWatch alarm for expiration of imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/imported-key-material-expiration-alarm.html): You can create a CloudWatch alarm that notifies you when the imported key material in a KMS key is approaching its expiration time.
- [Create CloudWatch alarms for external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/xks-alarms.html): You can create Amazon CloudWatch alarms based on external key store metrics to notify you when a metric value exceeds a threshold you specified.
- [Monitor keys with Amazon EventBridge](https://docs.aws.amazon.com/kms/latest/developerguide/kms-events.html): Understand the events that AWS Key Management Service (AWS KMS) sends to Amazon EventBridge and how to use them to monitor your KMS keys.


## [Aliases](https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html)

- [Controlling access to aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-access.html): When you create or change an alias, you affect the alias and its associated KMS key.
- [Create aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-create.html): Learn how to create aliases for your KMS keys using the AWS KMS console or the AWS KMS API.
- [Find the alias name and alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/alias-view.html): Learn how to view the aliases associated with your KMS keys using the AWS KMS console or the AWS KMS API, with operations like ListAliases and DescribeKey.
- [Update aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-update.html): Because an alias is an independent resource, you can change the KMS key associated with an alias.
- [Delete an alias](https://docs.aws.amazon.com/kms/latest/developerguide/alias-delete.html): You can delete an alias in the AWS KMS console or by using the DeleteAlias operation.
- [Use aliases to control access to KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/alias-authorization.html): You can control access to KMS keys based on the aliases that are associated with the KMS key.
- [Learn how to use aliases in your applications](https://docs.aws.amazon.com/kms/latest/developerguide/alias-using.html): You can use an alias to represent a KMS key in your application code.
- [Find aliases in AWS CloudTrail logs](https://docs.aws.amazon.com/kms/latest/developerguide/alias-ct.html): You can use an alias to represent an AWS KMS key in an AWS KMS API operation.


## [Tags](https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html)

- [Controlling access to tags](https://docs.aws.amazon.com/kms/latest/developerguide/tag-permissions.html): To add, view, and delete tags, either in the AWS KMS console or by using the API, principals need tagging permissions.
- [Add tags](https://docs.aws.amazon.com/kms/latest/developerguide/add-tags.html): Learn how to add tags to customer managed keys using the AWS KMS console and AWS KMS API.
- [Edit tags](https://docs.aws.amazon.com/kms/latest/developerguide/edit-tags.html): Tags help identify and organize your AWS resources.
- [Remove tags](https://docs.aws.amazon.com/kms/latest/developerguide/remove-tags.html): Tags help identify and organize your AWS resources.
- [View tags](https://docs.aws.amazon.com/kms/latest/developerguide/view-tags.html): Learn how to view and identify the tags associated with your customer managed KMS keys using the AWS KMS console or AWS KMS API.
- [Use tags to control access to KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/tag-authorization.html): You can control access to AWS KMS keys based on the tags on the KMS key.


## [Key stores](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html)

### [AWS CloudHSM key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html)

An AWS CloudHSM key store is a custom key store backed by a AWS CloudHSM cluster.

- [Control access to your AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/authorize-key-store.html): You use IAM policies to control access to your AWS CloudHSM key store and your AWS CloudHSM cluster.
- [Create an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html): You can create one or several AWS CloudHSM key stores in your account.
- [View an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/view-keystore.html): You can view the AWS CloudHSM key stores in each account and Region by using the AWS KMS console or the DescribeCustomKeyStores operation.
- [Edit AWS CloudHSM key store settings](https://docs.aws.amazon.com/kms/latest/developerguide/update-keystore.html): You can change the settings of an existing AWS CloudHSM key store.
- [Connect an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/connect-keystore.html): New AWS CloudHSM key stores are not connected.
- [Disconnect an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/disconnect-keystore.html): When you disconnect an AWS CloudHSM key store, AWS KMS logs out of the AWS CloudHSM client, disconnects from the associated AWS CloudHSM cluster, and removes the network infrastructure that it created to support the connection.
- [Delete an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/delete-keystore.html): When you delete an AWS CloudHSM key store, AWS KMS deletes all metadata about the AWS CloudHSM key store from KMS, including information about its association with an AWS CloudHSM cluster.
- [Troubleshooting a custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html): AWS CloudHSM key stores are designed to be available and resilient.

### [External key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html)

External key stores allow you to protect your AWS resources using cryptographic keys outside of AWS.

- [Control access to your external key store](https://docs.aws.amazon.com/kms/latest/developerguide/authorize-xks-key-store.html): All AWS KMS access control features â key policies, IAM policies, and grants â that you use with standard KMS keys, work the same way for KMS keys in an external key store.

### [Choose a proxy connectivity option](https://docs.aws.amazon.com/kms/latest/developerguide/choose-xks-connectivity.html)

Before creating your external key store, choose the connectivity option that determines how AWS KMS communicates with your external key store components.

- [Configure VPC endpoint service connectivity](https://docs.aws.amazon.com/kms/latest/developerguide/vpc-connectivity.html): Use the guidance in this section to create and configure the AWS resources and related components that are required for an external key store that uses VPC endpoint service connectivity.
- [Create an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-xks-keystore.html): You can create one or many external key stores in each AWS account and Region.
- [Edit external key store properties](https://docs.aws.amazon.com/kms/latest/developerguide/update-xks-keystore.html): You can edit selected properties of an existing external key store.
- [View external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/view-xks-keystore.html): You can view external key stores in each account and Region by using the AWS KMS console or by using the DescribeCustomKeyStores operation.
- [Monitor external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/xks-monitoring.html): AWS KMS collects metrics for each interaction with an external key store and publishes them in your CloudWatch account.

### [Connect and disconnect external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/xks-connect-disconnect.html)

New external key stores are not connected.

- [Connect an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/about-xks-connecting.html): When your external key store is connected to its external key store proxy, you can create KMS keys in your external key store and use its existing KMS keys in cryptographic operations.
- [Disconnect an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/about-xks-disconnecting.html): When you disconnect an external key store with VPC endpoint service connectivity from its external key store proxy, AWS KMS deletes its interface endpoint to the VPC endpoint service and removes the network infrastructure that it created to support the connection.
- [Delete an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/delete-xks.html): When you delete an external key store, AWS KMS deletes all metadata about the external key store from AWS KMS, including information about its external key store proxy.
- [Troubleshooting external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/xks-troubleshooting.html): The resolution for most problems with external key stores are indicated by the error message that AWS KMS displays with each exception, or by the connection error code that AWS KMS returns when an attempt to connect the external key store to its external key store proxy fails.


## [Security](https://docs.aws.amazon.com/kms/latest/developerguide/kms-security.html)

- [Data protection](https://docs.aws.amazon.com/kms/latest/developerguide/data-protection.html): Learn how your encryption keys are protected in the AWS Key Management Service (AWS KMS) service.

### [Identity and access management](https://docs.aws.amazon.com/kms/latest/developerguide/security-iam.html)

AWS Identity and Access Management (IAM) helps you securely control access to AWS resources.

- [AWS managed policies](https://docs.aws.amazon.com/kms/latest/developerguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS KMS and recent changes to those policies.

### [Service-linked roles](https://docs.aws.amazon.com/kms/latest/developerguide/using-service-linked-roles.html)

How to use service-linked roles to give AWS KMS access to resources in your AWS account.

- [Authorizing AWS KMS to manage AWS CloudHSM and Amazon EC2 resources](https://docs.aws.amazon.com/kms/latest/developerguide/authorize-kms.html): To support your AWS CloudHSM key stores, AWS KMS needs permission to get information about your AWS CloudHSM clusters.
- [Authorizing AWS KMS to synchronize multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-auth-slr.html): To support multi-Region keys, AWS KMS needs permission to synchronize the shared properties of a multi-Region primary key with its replica keys.
- [Logging and monitoring](https://docs.aws.amazon.com/kms/latest/developerguide/security-logging-monitoring.html): Learn how your encryption keys are protected in the AWS Key Management Service (AWS KMS) service.
- [Compliance validation](https://docs.aws.amazon.com/kms/latest/developerguide/kms-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/kms/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy and about specific AWS Key Management Service features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/kms/latest/developerguide/infrastructure-security.html): Learn how AWS Key Management Service isolates service traffic.


## [Quotas](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html)

- [Resource quotas](https://docs.aws.amazon.com/kms/latest/developerguide/resource-limits.html): AWS KMS establishes resource quotas to ensure that it can provide fast and resilient service to all of our customers.
- [Request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html): AWS KMS establishes quotas for the number of API operations requested in each second.
- [Throttling requests](https://docs.aws.amazon.com/kms/latest/developerguide/throttling.html): To ensure that AWS KMS can provide fast and reliable responses to API requests from all customers, it throttles API requests that exceed certain boundaries.


## [Code examples](https://docs.aws.amazon.com/kms/latest/developerguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/kms/latest/developerguide/service_code_examples_basics.html)

The following code examples show how to use the basics of AWS KMS with AWS SDKs.

- [Hello AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_Hello_section.html): Hello AWS Key Management Service
- [Learn the basics](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_Scenario_Basics_section.html): Learn the basics of AWS KMS with an AWS SDK

### [Actions](https://docs.aws.amazon.com/kms/latest/developerguide/service_code_examples_actions.html)

The following code examples show how to use AWS KMS with AWS SDKs.

- [CreateAlias](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_CreateAlias_section.html): Use CreateAlias with an AWS SDK or CLI
- [CreateGrant](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_CreateGrant_section.html): Use CreateGrant with an AWS SDK or CLI
- [CreateKey](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_CreateKey_section.html): Use CreateKey with an AWS SDK or CLI
- [Decrypt](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_Decrypt_section.html): Use Decrypt with an AWS SDK or CLI
- [DeleteAlias](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_DeleteAlias_section.html): Use DeleteAlias with an AWS SDK or CLI
- [DescribeKey](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_DescribeKey_section.html): Use DescribeKey with an AWS SDK or CLI
- [DisableKey](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_DisableKey_section.html): Use DisableKey with an AWS SDK or CLI
- [EnableKey](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_EnableKey_section.html): Use EnableKey with an AWS SDK or CLI
- [EnableKeyRotation](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_EnableKeyRotation_section.html): Use EnableKeyRotation with an AWS SDK or CLI
- [Encrypt](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_Encrypt_section.html): Use Encrypt with an AWS SDK or CLI
- [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_GenerateDataKey_section.html): Use GenerateDataKey with an AWS SDK or CLI
- [GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_GenerateDataKeyWithoutPlaintext_section.html): Use GenerateDataKeyWithoutPlaintext with an AWS SDK or CLI
- [GenerateRandom](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_GenerateRandom_section.html): Use GenerateRandom with an AWS SDK or CLI
- [GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_GetKeyPolicy_section.html): Use GetKeyPolicy with an AWS SDK or CLI
- [ListAliases](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_ListAliases_section.html): Use ListAliases with an AWS SDK or CLI
- [ListGrants](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_ListGrants_section.html): Use ListGrants with an AWS SDK or CLI
- [ListKeyPolicies](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_ListKeyPolicies_section.html): Use ListKeyPolicies with an AWS SDK or CLI
- [ListKeys](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_ListKeys_section.html): Use ListKeys with an AWS SDK or CLI
- [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_PutKeyPolicy_section.html): Use PutKeyPolicy with an AWS SDK or CLI
- [ReEncrypt](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_ReEncrypt_section.html): Use ReEncrypt with an AWS SDK or CLI
- [RetireGrant](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_RetireGrant_section.html): Use RetireGrant with an AWS SDK or CLI
- [RevokeGrant](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_RevokeGrant_section.html): Use RevokeGrant with an AWS SDK or CLI
- [ScheduleKeyDeletion](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_ScheduleKeyDeletion_section.html): Use ScheduleKeyDeletion with an AWS SDK or CLI
- [Sign](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_Sign_section.html): Use Sign with an AWS SDK or CLI
- [TagResource](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_TagResource_section.html): Use TagResource with an AWS SDK or CLI
- [UpdateAlias](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_UpdateAlias_section.html): Use UpdateAlias with an AWS SDK or CLI
- [Verify](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_Verify_section.html): Use Verify with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/kms/latest/developerguide/service_code_examples_scenarios.html)

The following code examples show how to use AWS KMS with AWS SDKs.

- [Work with table encryption](https://docs.aws.amazon.com/kms/latest/developerguide/example_dynamodb_Scenario_EncryptionExamples_section.html): Work with DynamoDB table encryption using AWS Command Line Interface v2


## [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html)

- [How to make attested calls to AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/attested-calls.html): To make an attested call to AWS KMS, use the Recipient parameter in the request to provide the signed attestation document and the encryption algorithm to use with the public key in the attestation document.

### [Monitoring attested requests](https://docs.aws.amazon.com/kms/latest/developerguide/ct-attestation.html)

You can use your AWS CloudTrail logs to monitor Decrypt, DeriveSharedSecret, GenerateDataKey, GenerateDataKeyPair, and GenerateRandom operations that use attestation.

- [Monitoring requests for Nitro enclaves](https://docs.aws.amazon.com/kms/latest/developerguide/ct-nitro-enclave.html): For Nitro enclave attestation, the CloudTrail log includes the module ID (attestationDocumentModuleId), image digest (attestationDocumentEnclaveImageDigest), and platform configuration registers (PCRs) from the attestation document.
- [Monitoring requests for NitroTPM](https://docs.aws.amazon.com/kms/latest/developerguide/ct-nitro-tpm.html): For NitroTPM attestation, the CloudTrail log includes the module ID (attestationDocumentModuleId) and platform configuration registers (PCRs) from the attestation document.


## [Encrypting AWS services](https://docs.aws.amazon.com/kms/latest/developerguide/service-integration.html)

- [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/kms/latest/developerguide/services-ebs.html): Learn how Amazon EBS uses AWS KMS to encrypt volumes.
- [Amazon EMR](https://docs.aws.amazon.com/kms/latest/developerguide/services-emr.html): Learn how Amazon EMR uses AWS Key Management Service (AWS KMS) to encrypt data.
- [Amazon Redshift](https://docs.aws.amazon.com/kms/latest/developerguide/services-redshift.html): Discusses how Amazon Redshift uses AWS KMS to encrypt data. uses KMS.


## [Reference](https://docs.aws.amazon.com/kms/latest/developerguide/references.html)

- [Key state reference](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html): Learn how the key state of an AWS Key Management Service AWS KMS keys affects the API operations that you can use for that KMS key.
- [Key type reference](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-compare.html): AWS KMS supports different features for different types of KMS keys.
- [Key spec reference](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose-key-spec.html): When you create an asymmetric KMS key or an HMAC KMS key, you select its key spec.
- [Permissions reference](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html): Use AWS Key Management Service (AWS KMS) permissions (actions) and resources in a permissions policy.

### [AWS KMS internal operations](https://docs.aws.amazon.com/kms/latest/developerguide/kms-internals.html)

AWS KMS internals are required to scale and secure HSMs for a globally distributed key management service.

- [Domains and domain state](https://docs.aws.amazon.com/kms/latest/developerguide/domains-and-domain-state.html): A cooperative collection of trusted internal AWS KMS entities within an AWS Region is referred to as a domain.
- [Internal communication security](https://docs.aws.amazon.com/kms/latest/developerguide/internal-communication-security.html): Commands between the service hosts or AWS KMS operators and the HSMs are secured through a quorum-signed request method and an authenticated session using an HSM-service host protocol.
- [Replication process for multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/replicate-key-details.html): AWS KMS uses a cross-Region replication mechanism to copy the key material in a KMS key from an HSM in one AWS Region to an HSM in a different AWS Region.
- [Durability protection](https://docs.aws.amazon.com/kms/latest/developerguide/durability-protection.html): Additional service durability for AWS KMS is provided by offline HSMs, multiple nonvolatile storage of exported domain tokens, and redundant storage of encrypted AWS KMS keys.
