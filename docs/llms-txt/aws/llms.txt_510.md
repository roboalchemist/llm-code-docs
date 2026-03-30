# Source: https://docs.aws.amazon.com/kms/latest/APIReference/llms.txt

# AWS Key Management Service API Reference

> AWS Key Management Service (AWS KMS) is an encryption and key management web service. This guide describes the AWS KMS operations that you can call programmatically. For general information about AWS KMS, see the AWS Key Management Service Developer Guide.

- [Welcome](https://docs.aws.amazon.com/kms/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/kms/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/kms/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/kms/latest/APIReference/API_Operations.html)

- [CancelKeyDeletion](https://docs.aws.amazon.com/kms/latest/APIReference/API_CancelKeyDeletion.html): Cancels the deletion of a KMS key.
- [ConnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_ConnectCustomKeyStore.html): Connects or reconnects a custom key store to its backing key store.
- [CreateAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateAlias.html): Creates a friendly name for a KMS key.
- [CreateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateCustomKeyStore.html): Creates a custom key store backed by a key store that you own and manage.
- [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html): Adds a grant to a KMS key.
- [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html): Creates a unique customer managed KMS key in your AWS account and Region.
- [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html): Decrypts ciphertext that was encrypted by a KMS key using any of the following operations:
- [DeleteAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteAlias.html): Deletes the specified alias.
- [DeleteCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteCustomKeyStore.html): Deletes a custom key store.
- [DeleteImportedKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteImportedKeyMaterial.html): Deletes key material that was previously imported.
- [DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html): Derives a shared secret using a key agreement algorithm.
- [DescribeCustomKeyStores](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeCustomKeyStores.html): Gets information about custom key stores in the account and Region.
- [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html): Provides detailed information about a KMS key.
- [DisableKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html): Sets the state of a KMS key to disabled.
- [DisableKeyRotation](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKeyRotation.html): Disables automatic rotation of the key material of the specified symmetric encryption KMS key.
- [DisconnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisconnectCustomKeyStore.html): Disconnects the custom key store from its backing key store.
- [EnableKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html): Sets the key state of a KMS key to enabled.
- [EnableKeyRotation](https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKeyRotation.html): Enables automatic rotation of the key material of the specified symmetric encryption KMS key.
- [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html): Encrypts plaintext of up to 4,096 bytes using a KMS key.
- [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html): Returns a unique symmetric data key for use outside of AWS KMS.
- [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair.html): Returns a unique asymmetric data key pair for use outside of AWS KMS.
- [GenerateDataKeyPairWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPairWithoutPlaintext.html): Returns a unique asymmetric data key pair for use outside of AWS KMS.
- [GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html): Returns a unique symmetric data key for use outside of AWS KMS.
- [GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html): Generates a hash-based message authentication code (HMAC) for a message using an HMAC KMS key and a MAC algorithm that the key supports.
- [GenerateRandom](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateRandom.html): Returns a random byte string that is cryptographically secure.
- [GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyPolicy.html): Gets a key policy attached to the specified KMS key.
- [GetKeyRotationStatus](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyRotationStatus.html): Provides detailed information about the rotation status for a KMS key, including whether automatic rotation of the key material is enabled for the specified KMS key, the rotation period, and the next scheduled rotation date.
- [GetParametersForImport](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetParametersForImport.html): Returns the public key and an import token you need to import or reimport key material for a KMS key.
- [GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html): Returns the public key of an asymmetric KMS key.
- [ImportKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_ImportKeyMaterial.html): Imports or reimports key material into an existing KMS key that was created without key material.
- [ListAliases](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListAliases.html): Gets a list of aliases in the caller's AWS account and region.
- [ListGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListGrants.html): Gets a list of all grants for the specified KMS key.
- [ListKeyPolicies](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeyPolicies.html): Gets the names of the key policies that are attached to a KMS key.
- [ListKeyRotations](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeyRotations.html): Returns information about the key materials associated with the specified KMS key.
- [ListKeys](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html): Gets a list of all KMS keys in the caller's AWS account and Region.
- [ListResourceTags](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListResourceTags.html): Returns all tags on the specified KMS key.
- [ListRetirableGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListRetirableGrants.html): Returns information about all grants in the AWS account and Region that have the specified retiring principal.
- [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html): Attaches a key policy to the specified KMS key.
- [ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html): Decrypts ciphertext and then reencrypts it entirely within AWS KMS.
- [ReplicateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReplicateKey.html): Replicates a multi-Region key into the specified Region.
- [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html): Deletes a grant.
- [RevokeGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html): Deletes the specified grant.
- [RotateKeyOnDemand](https://docs.aws.amazon.com/kms/latest/APIReference/API_RotateKeyOnDemand.html): Immediately initiates rotation of the key material of the specified symmetric encryption KMS key.
- [ScheduleKeyDeletion](https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html): Schedules the deletion of a KMS key.
- [Sign](https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html): Creates a digital signature for a message or message digest by using the private key in an asymmetric signing KMS key.
- [TagResource](https://docs.aws.amazon.com/kms/latest/APIReference/API_TagResource.html): Adds or edits tags on a customer managed key.
- [UntagResource](https://docs.aws.amazon.com/kms/latest/APIReference/API_UntagResource.html): Deletes tags from a customer managed key.
- [UpdateAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateAlias.html): Associates an existing AWS KMS alias with a different KMS key.
- [UpdateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateCustomKeyStore.html): Changes the properties of a custom key store.
- [UpdateKeyDescription](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateKeyDescription.html): Updates the description of a KMS key.
- [UpdatePrimaryRegion](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdatePrimaryRegion.html): Changes the primary key of a multi-Region key.
- [Verify](https://docs.aws.amazon.com/kms/latest/APIReference/API_Verify.html): Verifies a digital signature that was generated by the operation.
- [VerifyMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_VerifyMac.html): Verifies the hash-based message authentication code (HMAC) for a specified message, HMAC KMS key, and MAC algorithm.


## [Data Types](https://docs.aws.amazon.com/kms/latest/APIReference/API_Types.html)

- [AliasListEntry](https://docs.aws.amazon.com/kms/latest/APIReference/API_AliasListEntry.html): Contains information about an alias.
- [CustomKeyStoresListEntry](https://docs.aws.amazon.com/kms/latest/APIReference/API_CustomKeyStoresListEntry.html): Contains information about each custom key store in the custom key store list.
- [GrantConstraints](https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html): Use this structure to allow cryptographic operations in the grant only when the operation request includes the specified encryption context.
- [GrantListEntry](https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantListEntry.html): Contains information about a grant.
- [KeyListEntry](https://docs.aws.amazon.com/kms/latest/APIReference/API_KeyListEntry.html): Contains information about each entry in the key list.
- [KeyMetadata](https://docs.aws.amazon.com/kms/latest/APIReference/API_KeyMetadata.html): Contains metadata about a KMS key.
- [MultiRegionConfiguration](https://docs.aws.amazon.com/kms/latest/APIReference/API_MultiRegionConfiguration.html): Describes the configuration of this multi-Region key.
- [MultiRegionKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_MultiRegionKey.html): Describes the primary or replica key in a multi-Region key.
- [RecipientInfo](https://docs.aws.amazon.com/kms/latest/APIReference/API_RecipientInfo.html): Contains information about the party that receives the response from the API operation.
- [RotationsListEntry](https://docs.aws.amazon.com/kms/latest/APIReference/API_RotationsListEntry.html): Each entry contains information about one of the key materials associated with a KMS key.
- [Tag](https://docs.aws.amazon.com/kms/latest/APIReference/API_Tag.html): A key-value pair.
- [XksKeyConfigurationType](https://docs.aws.amazon.com/kms/latest/APIReference/API_XksKeyConfigurationType.html): Information about the external key that is associated with a KMS key in an external key store.
- [XksProxyAuthenticationCredentialType](https://docs.aws.amazon.com/kms/latest/APIReference/API_XksProxyAuthenticationCredentialType.html): AWS KMS uses the authentication credential to sign requests that it sends to the external key store proxy (XKS proxy) on your behalf.
- [XksProxyConfigurationType](https://docs.aws.amazon.com/kms/latest/APIReference/API_XksProxyConfigurationType.html): Detailed information about the external key store proxy (XKS proxy).
