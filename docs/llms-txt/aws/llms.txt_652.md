# Source: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/llms.txt

# AWS Payment Cryptography Control Plane API Reference

> AWS Payment Cryptography Control Plane APIs manage encryption keys for use during payment-related cryptographic operations. You can create, import, export, share, manage, and delete keys. You can also manage AWS Identity and Access Management (IAM) policies for keys. For more information, see Identity and access management in the AWS Payment Cryptography User Guide.

- [Welcome](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/Welcome.html)

## [Actions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_Operations.html)

- [AddKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_AddKeyReplicationRegions.html): Adds replication AWS Regions to an existing AWS Payment Cryptography key, enabling the key to be used for cryptographic operations in additional AWS Regions.
- [CreateAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html): Creates an alias, or a friendly name, for an AWS Payment Cryptography key.
- [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html): Creates an AWS Payment Cryptography key, a logical representation of a cryptographic key, that is unique in your account and AWS Region.
- [DeleteAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html): Deletes the alias, but doesn't affect the underlying key.
- [DeleteKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html): Deletes the key material and metadata associated with AWS Payment Cryptography key.
- [DisableDefaultKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DisableDefaultKeyReplicationRegions.html): Disables Multi-Region key replication settings for the specified AWS Regions in your AWS account, preventing new keys from being automatically replicated to those regions.
- [EnableDefaultKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_EnableDefaultKeyReplicationRegions.html): Enables Multi-Region key replication settings for your AWS account, causing new keys to be automatically replicated to the specified AWS Regions when created.
- [ExportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKey.html): Exports a key from AWS Payment Cryptography.
- [GetAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html): Gets the AWS Payment Cryptography key associated with the alias.
- [GetCertificateSigningRequest](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetCertificateSigningRequest.html): Creates a certificate signing request (CSR) from a key pair.
- [GetDefaultKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetDefaultKeyReplicationRegions.html): Retrieves the list of AWS Regions where Multi-Region key replication is currently enabled for your AWS account.
- [GetKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html): Gets the key metadata for an AWS Payment Cryptography key, including the immutable and mutable attributes specified when the key was created.
- [GetParametersForExport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html): Gets the export token and the signing key certificate to initiate a TR-34 key export from AWS Payment Cryptography.
- [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html): Gets the import token and the wrapping key certificate in PEM format (base64 encoded) to initiate a TR-34 WrappedKeyBlock or a RSA WrappedKeyCryptogram import into AWS Payment Cryptography.
- [GetPublicKeyCertificate](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html): Gets the public key certificate of the asymmetric key pair that exists within AWS Payment Cryptography.
- [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html): Imports symmetric keys and public key certificates in PEM format (base64 encoded) into AWS Payment Cryptography.
- [ListAliases](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html): Lists the aliases for all keys in the caller's AWS account and AWS Region.
- [ListKeys](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html): Lists the keys in the caller's AWS account and AWS Region.
- [ListTagsForResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListTagsForResource.html): Lists the tags for an AWS resource.
- [RemoveKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RemoveKeyReplicationRegions.html): Removes Replication Regions from an existing AWS Payment Cryptography key, disabling the key's availability for cryptographic operations in the specified AWS Regions.
- [RestoreKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RestoreKey.html): Cancels a scheduled key deletion during the waiting period.
- [StartKeyUsage](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StartKeyUsage.html): Enables an AWS Payment Cryptography key, which makes it active for cryptographic operations within AWS Payment Cryptography
- [StopKeyUsage](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html): Disables an AWS Payment Cryptography key, which makes it inactive within AWS Payment Cryptography.
- [TagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html): Adds or edits tags on an AWS Payment Cryptography key.
- [UntagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UntagResource.html): Deletes a tag from an AWS Payment Cryptography key.
- [UpdateAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html): Associates an existing AWS Payment Cryptography alias with a different key.


## [Data Types](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_Types.html)

- [Alias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_Alias.html): Contains information about an alias.
- [CertificateSubjectType](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CertificateSubjectType.html): The metadata used to create the certificate signing request.
- [DiffieHellmanDerivationData](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DiffieHellmanDerivationData.html): The shared information used when deriving a key using ECDH.
- [ExportAs2805KeyCryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportAs2805KeyCryptogram.html): Parameter information for key material export using AS2805 key cryptogram format.
- [ExportAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportAttributes.html): The attributes for IPEK generation during export.
- [ExportDiffieHellmanTr31KeyBlock](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportDiffieHellmanTr31KeyBlock.html): Key derivation parameter information for key material export using asymmetric ECDH key exchange method.
- [ExportDukptInitialKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportDukptInitialKey.html): Parameter information for IPEK generation during export.
- [ExportKeyCryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKeyCryptogram.html): Parameter information for key material export using asymmetric RSA wrap and unwrap key exchange method.
- [ExportKeyMaterial](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKeyMaterial.html): Parameter information for key material export from AWS Payment Cryptography using TR-31 or TR-34 or RSA wrap and unwrap key exchange method.
- [ExportTr31KeyBlock](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportTr31KeyBlock.html): Parameter information for key material export using symmetric TR-31 key exchange method.
- [ExportTr34KeyBlock](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportTr34KeyBlock.html): Parameter information for key material export using the asymmetric TR-34 key exchange method.
- [ImportAs2805KeyCryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportAs2805KeyCryptogram.html): Parameter information for key material import using AS2805 key cryptogram format.
- [ImportDiffieHellmanTr31KeyBlock](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportDiffieHellmanTr31KeyBlock.html): Key derivation parameter information for key material import using asymmetric ECDH key exchange method.
- [ImportKeyCryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKeyCryptogram.html): Parameter information for key material import using asymmetric RSA wrap and unwrap key exchange method.
- [ImportKeyMaterial](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKeyMaterial.html): Parameter information for key material import into AWS Payment Cryptography using TR-31 or TR-34 or RSA wrap and unwrap key exchange method.
- [ImportTr31KeyBlock](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportTr31KeyBlock.html): Parameter information for key material import using symmetric TR-31 key exchange method.
- [ImportTr34KeyBlock](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportTr34KeyBlock.html): Parameter information for key material import using the asymmetric TR-34 key exchange method.
- [Key](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_Key.html): Metadata about an AWS Payment Cryptography key.
- [KeyAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_KeyAttributes.html): The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key.
- [KeyBlockHeaders](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_KeyBlockHeaders.html): Optional metadata for export associated with the key material.
- [KeyModesOfUse](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_KeyModesOfUse.html): The list of cryptographic operations that you can perform using the key.
- [KeySummary](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_KeySummary.html): Metadata about an AWS Payment Cryptography key.
- [ReplicationStatusType](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ReplicationStatusType.html): Represents the replication status information for a key in a replication region for Multi-Region key replication.
- [RootCertificatePublicKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RootCertificatePublicKey.html): Parameter information for root public key certificate import.
- [Tag](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_Tag.html): A structure that contains information about a tag.
- [TrustedCertificatePublicKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TrustedCertificatePublicKey.html): Parameter information for trusted public key certificate import.
- [WrappedKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_WrappedKey.html): Parameter information for generating a WrappedKeyBlock for key exchange.
