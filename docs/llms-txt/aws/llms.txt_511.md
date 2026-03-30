# Source: https://docs.aws.amazon.com/kms/latest/cryptographic-details/llms.txt

# AWS Key Management Service AWS KMS Cryptographic Details

> Learn about the cryptographic operations that are run within AWS when you use AWS KMS.

- [Document history](https://docs.aws.amazon.com/kms/latest/cryptographic-details/doc-history.html)

## [Introduction](https://docs.aws.amazon.com/kms/latest/cryptographic-details/intro.html)

- [Concepts](https://docs.aws.amazon.com/kms/latest/cryptographic-details/basic-concepts.html): Learn the concepts that are basic to AWS Key Management Service.
- [Design goals](https://docs.aws.amazon.com/kms/latest/cryptographic-details/design-goals.html): AWS KMS is designed to meet several key requirements.


## [AWS Key Management Service foundations](https://docs.aws.amazon.com/kms/latest/cryptographic-details/foundation.html)

- [Cryptographic primitives](https://docs.aws.amazon.com/kms/latest/cryptographic-details/crypto-primitives.html): AWS KMS uses configurable cryptographic algorithms so that the system can quickly migrate from one approved algorithm, or mode, to another.
- [AWS KMS key hierarchy](https://docs.aws.amazon.com/kms/latest/cryptographic-details/key-hierarchy.html): Learn the hierarchy of AWS KMS key, from the top-level KMS key to the HSM backing key and exported key tokens (EKTs).


## [Use cases](https://docs.aws.amazon.com/kms/latest/cryptographic-details/use-cases.html)

- [EBS volume encryption](https://docs.aws.amazon.com/kms/latest/cryptographic-details/ebs-volume-encryption.html): Amazon EBS offers volume encryption capability.
- [Client-side encryption](https://docs.aws.amazon.com/kms/latest/cryptographic-details/client-side-encryption.html): The AWS Encryption SDK includes an API operation for performing envelope encryption using a KMS key.


## [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/cryptographic-details/kms-keys.html)

- [Calling CreateKey](https://docs.aws.amazon.com/kms/latest/cryptographic-details/create-key.html): An AWS KMS key is generated as a result of a call to the CreateKey API call.
- [Importing key material](https://docs.aws.amazon.com/kms/latest/cryptographic-details/importing-key-material.html): AWS KMS provides a mechanism for importing the cryptographic material used for an HBK.
- [Enabling and disabling keys](https://docs.aws.amazon.com/kms/latest/cryptographic-details/enable-and-disable-key.html): Disabling a KMS key prevents the key from being used in cryptographic operations.
- [Deleting keys](https://docs.aws.amazon.com/kms/latest/cryptographic-details/key-deletion.html): Authorized users can use the ScheduleKeyDeletion API to schedule the deletion of a KMS key and all associated HBKs.
- [Rotating key material](https://docs.aws.amazon.com/kms/latest/cryptographic-details/rotate-customer-master-key.html): Authorized users can enable automatic annual rotation of their customer managed KMS keys.


## [Customer data operations](https://docs.aws.amazon.com/kms/latest/cryptographic-details/customer-data-operations.html)

- [Generating data keys](https://docs.aws.amazon.com/kms/latest/cryptographic-details/generating-data-keys.html): Use AWS KMS GenerateDataKey API (and related APIs) to request a specific type of data key or a random key of arbitrary length.
- [Encrypt](https://docs.aws.amazon.com/kms/latest/cryptographic-details/encrypt-operation.html): Use AWS KMS to encrypt smaller than 4 KB under a KMS key.
- [Decrypt](https://docs.aws.amazon.com/kms/latest/cryptographic-details/decrypt-operation.html): Use the AWS KMS Decrypt operation to decrypt ciphertext.
- [Reencrypting an encrypted object](https://docs.aws.amazon.com/kms/latest/cryptographic-details/reencrypting-an-encrypted-object.html): Use the AWS KMS reencrypt command to reencrypt an existing customer ciphertext.


## [AWS KMS internal operations](https://docs.aws.amazon.com/kms/latest/cryptographic-details/kms-internals.html)

- [Domains and domain state](https://docs.aws.amazon.com/kms/latest/cryptographic-details/domains-and-domain-state.html): A cooperative collection of trusted internal AWS KMS entities within an AWS Region is referred to as a domain.
- [Internal communication security](https://docs.aws.amazon.com/kms/latest/cryptographic-details/internal-communication-security.html): Commands between the service hosts or AWS KMS operators and the HSMs are secured through a quorum-signed request method and an authenticated session using an HSM-service host protocol.
- [Replication process for multi-Region keys](https://docs.aws.amazon.com/kms/latest/cryptographic-details/replicate-key-details.html): AWS KMS uses a cross-Region replication mechanism to copy the key material in a KMS key from an HSM in one AWS Region to an HSM in a different AWS Region.
- [Durability protection](https://docs.aws.amazon.com/kms/latest/cryptographic-details/durability-protection.html): Additional service durability for AWS KMS is provided by offline HSMs, multiple nonvolatile storage of exported domain tokens, and redundant storage of encrypted AWS KMS keys.


## [Reference](https://docs.aws.amazon.com/kms/latest/cryptographic-details/kms-article-reference.html)

- [Abbreviations](https://docs.aws.amazon.com/kms/latest/cryptographic-details/kms-abbreviations.html): Learn the abbreviations used in this document.
- [Keys](https://docs.aws.amazon.com/kms/latest/cryptographic-details/keys.html): Learn the AWS KMS keys referenced in this document.
- [Contributors](https://docs.aws.amazon.com/kms/latest/cryptographic-details/kms-contributors.html): Learn which individuals and organizations contributed to this document.
- [Bibliography](https://docs.aws.amazon.com/kms/latest/cryptographic-details/kms-bibliography.html): Find source material that was cited in this document.
