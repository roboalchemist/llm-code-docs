# Source: https://docs.aws.amazon.com/payment-cryptography/latest/userguide/llms.txt

# AWS Payment Cryptography User Guide

- [Getting started](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/getting-started.html)
- [Quotas](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/doc-history.html)

## [What is AWS Payment Cryptography?](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/what-is.html)

- [Concepts](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/concepts.html): Learn the basic terms and concepts used in AWS Payment Cryptography and how you can use them to help you protect your data.
- [Industry terminology](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/terminology.html)
- [Endpoints](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/endpoints.html): Learn about the endpoints for AWS Payment Cryptography.


## [Managing keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-manage.html)

- [Creating keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/create-keys.html): You can create AWS Payment Cryptography keys using the CreateKey API operation.
- [Listing keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-list.html): Use the ListKeys operation to get a list of keys accessible to you in your account and Region.
- [Enabling and disabling keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-enable-disable.html): You can disable and re-enable AWS Payment Cryptography keys.
- [Replicating keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html): Learn how to use Multi-Region key replication for AWS Payment Cryptography to replicate and manage AWS Payment Cryptography keys across multiple AWS Regions.
- [Deleting keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-deleting.html): Learn how to schedule and cancel deletion of AWS Payment Cryptography keys.

### [Importing and exporting keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-importexport.html)

You can import AWS Payment Cryptography keys from other solutions and export them to other solutions, such as HSMs.

- [Import keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-import.html)
- [Export keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-export.html)

### [Advanced Topics](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keyexchange-advanced.html)

This section covers advanced key exchange scenarios and configurations.

- [Bring Your Own Certificate Authority (BYOCA)](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keyexchange-byoca.html): By default, when a public key certificate is needed for asymmetric(RSA,ECC) keys created within the service, these certificates are issued by a AWS Payment Cryptography and account-unique certificate authority(CA).

### [Using aliases](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-managealias.html)

An alias is a friendly name for an AWS Payment Cryptography key.

- [About aliases](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/alias-about.html): Learn how aliases work in AWS Payment Cryptography.
- [Using aliases in your applications](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/alias-using.html): You can use an alias to represent an AWS Payment Cryptography key in your application code.

### [Get keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/getkeys.html)

An AWS Payment Cryptography key represents a single unit of cryptographic material and can only be used for cryptographic operations for this service.

- [Get the public key/certificate associated with a key pair](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys.getpubliccertificate-example.html): Get Public Key/Certificate returns the public key indicated by the KeyArn.

### [Tagging keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/tagging-keys.html)

Learn how to use tags on AWS Payment Cryptography.

- [About tags in AWS Payment Cryptography](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/tags-about.html): A tag is an optional metadata label that you can assign (or AWS can assign) to an AWS resource.
- [Viewing key tags in the console](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/manage-tags-console.html): To view tags in the console, you need tagging permission on the key from an IAM policy that includes the key.
- [Managing key tags with API operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/manage-tags-api.html): You can use the AWS Payment Cryptography API to add, delete, and list tags for the keys that you manage.
- [Controlling access to tags](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/tag-permissions.html): To add, view, and delete tags by using the API, principals need tagging permissions in IAM policies.
- [Using tags to control access to keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/tag-authorization.html): You can control access to AWS Payment Cryptography based on the tags on the key.
- [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html): A tenet of proper key management is that keys are appropriately scoped and can only be used for permitted operations.


## [Data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.html)

### [Encrypt, Decrypt and Re-encrypt data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops.encryptdecrypt.html)

Encryption and Decryption methods can be used to encrypt or decrypt data using a variety of symmetric and asymmetric techniques including TDES, AES and RSA.

- [Encrypt data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/encrypt-data.html): The Encrypt Data API is used to encrypt data using symmetric and asymmetric data encryption keys as well as DUKPT and EMV derived keys.
- [Decrypt data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/decrypt-data.html): The Decrypt Data API is used to decrypt data using symmetric and asymmetric data encryption keys as well as DUKPT and EMV derived keys.

### [Generate and verify card data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-carddata.html)

Generate and verify card data incorporates data derived from card data, for instance CVV, CVV2, CVC and DCVV.

### [Generate card data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-card-data.html)

The Generate Card Data API is used to generate card data using algorithms such as CVV,CVV2 or Dynamic CVV2.

- [Generate CVV2](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-cvv2.html)
- [Generate iCVV](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-iCVV.html)

### [Verify card data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-card-data.html)

Verify Card Data is used to verify data that has been created using payment algorithms that rely on encryption principals such as DISCOVER_DYNAMIC_CARD_VERIFICATION_CODE.

- [Verify CVV2](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-cvv2.html)
- [Verify iCVV](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-iCVV.html)

### [Generate, translate and verify PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.pindata.html)

PIN data functions allow you to generate random pins, pin verification values (PVV) and validate inbound encrypted pins against PVV or PIN Offsets.

- [Translate PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/translate-pin-data.html): Translate PIN data functions are used for translating encrypted PIN data from one set of keys to another without the encrypted data leaving the HSM.

### [Generate PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-pin-data.html)

Generate PIN data functions are used for generating PIN-related values, such as PVV and pin block offsets used for validating pin entry by users during transaction or authorization time.

- [Generate a random pin and matching Visa PVV](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-pvv-random.html)
- [Generate a Visa PVV for a known pin](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-pvv-givenpin.html)
- [Generate IBM3624 pin offset for a pin](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-ibm3624.html): IBM 3624 PIN Offset also sometimes called the IBM method.

### [Verify PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-pin-data.html)

Verify PIN data functions are used for verifying whether a pin is correct.

- [Validate a PIN against previously stored IBM3624 pin offset](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-pin-data.ibm3624-example.html): In this example, we will validate a cardholder provided PIN against the pin offset stored on file with the card issuer/processor.
- [Verify auth request (ARQC) cryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.verifyauthrequestcryptogram.html): The verify auth request cryptogram API is used for verifying ARQC.

### [Generate and verify MAC](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-mac.html)

Message Authentication Codes (MAC) are typically used to authenticate the integrity of a message (whether it's been modified).

- [Generate MAC](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-mac.html): Learn how to generate MAC within AWS Payment Cryptography.
- [Verify MAC](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-mac.html): Learn how to verify MAC within AWS Payment Cryptography.
- [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html): Certain keys can only be used for certain operations.


## [Common use cases](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases.html)

### [Issuers and issuer processors](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.html)

Issuer use cases typically consist of a few parts.

### [General Functions](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.html)

- [Pins and PVV](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.pvv.html)
- [CVV](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.cvv.html): CVV or CVV1 is a value that is traditionally embedded in a cards magnetic stripe.
- [CVV2](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.cvv2.html): CVV2 is a value that is traditionally provided on the back of a card and is used for online purchases.
- [iCVV](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.icvv.html): iCVV uses the same algorithm as CVV/CVV2 but iCVV is embedded inside a chip card.
- [EMV ARQC](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html): ARQC (Authorization Request Cryptogram) is a cryptogram generated by an EMV (chip) card and used to validate the transaction details as well as the use of an authorized card.
- [EMV MAC](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.emvmac.html): EMV MAC is MAC using an input of an EMV derived key and then performing a ISO9797-3 (Retail) MAC over the resulting data.
- [EMV PIN Change](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.emvpinchange.html): EMV PIN change combines two operations: generating a MAC for an issuer script and encrypting a new PIN for offline PIN change on an EMV chip card.

### [Network specific functions](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.networkfunctions.html)

- [Visa](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.networkfunctions.visa.html)
- [Mastercard](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.networkfunctions.mastercard.html)
- [AMEX](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.networkfunctions.amex.html)
- [JCB](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.networkfunctions.jcb.html)

### [Acquiring and payment facilitators](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-acquirers.html)

Acquirers, PSPs and Payment Facilators typically have a different set of cryptographic requirements than issuers.

- [Using Dynamic Keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-acquirers-dynamickeys.html): Dynamic Keys allows one-time or limited use keys to be used for cryptographic operations like EncryptData.


## [Region specific features](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/advanced.regional.html)

### [AS2805](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/advanced.regional.as2805.html)

Australia Standard 2805 (AS2805) is a standard for electronic funds transfers used primarily for card-based payment transactions.

- [Initial Key(KEK) exchange](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/as2805.kekexchange.html): In AS2805, each side has their own KEK.
- [Validation of KEK](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/as2805.kekvalidation.html)
- [Creation and transmission of working keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/as2805.workingkeys.create.html): Typical working keys used in AS2805 includes two sets of keys:
- [Exporting working keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/as2805.workingkeys.export.html): To maintain compatibility with other parties, AWS Payment Cryptography supports AS2805 symmetric key wrapping techniques which use key variants instead of keyblocks like TR-31.
- [Pin Translation](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/as2805.pintranslation.html): AS2805 describes a session specific key derivation mode in section 6.4.
- [Mac Generation and Validation](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/as2805.mac.html): The generate and verify MAC commands support a variety of MACs including HMAC, CMAC, EMV MAC, etc.


## [Security](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Payment Cryptography.
- [Resilience](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/resilience.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Payment Cryptography features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/infrastructure-security.html): Learn how AWS Payment Cryptography isolates service traffic.
- [Use Amazon VPC and AWS PrivateLink](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/vpc-endpoint.html): Learn how to connect to AWS Payment Cryptography from a private endpoint in your VPC.

### [Hybrid post-quantum TLS](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pqtls.html)

Learn how to use hybrid post-quantum key agreement algorithms for TLS

- [How to use it](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pqtls-details.html): AWS SDKs and tools have cryptographic capabilities and configuration that differ across language and runtime.
- [Security best practices](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-best-practices.html): Learn about security best practices for using the AWS Payment Cryptography service.


## [Compliance validation](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/compliance-validation.html)

- [Compliance of the service](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/service-compliance.html): Third-party auditors assess the security and compliance of AWS Payment Cryptography as part of multiple AWS compliance programs.

### [PIN Compliance](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance.html)

The documentation and evidence that you will need to prepare for a PCI PIN assessment.

- [Common Topics](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/compliance.pin.commontopics.html): Migrating applications from connecting to HSM to a managed service such as AWS Payment Cryptography brings up common issues and concepts for customers and their assessors.

### [Assessment Scope](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-scope.html)

The first step in planning any assessment is documenting the scope.

- [Shared Responsibility](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-scope-sr.html): AWS Payment Cryptography is an Encryption and Support Organization (ESO) and a PIN-Acquiring Third-Party Servicer (TPS), as defined by the Visa PIN Security Program and listed on the Visa Global Service Provider Registry, under âAmazon Web Services, LLCâ.
- [High-Level Network Diagrams](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-scope-diagram.html): The PCI PIN Reporting Template requires, âFor entities engaged in the processing of PIN based transaction provide a network schematic describing PIN based transaction flows with the associated key type usage.
- [Key Table](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-scope-kt.html): The report requires that all keys protecting PINs, directly or indirectly, are listed.
- [Document References](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-scope-dr.html): Vendor documentation and recommendations for secure use of AWS Payment Cryptography is in the Userâs Guide and API Reference.

### [Transaction Processing Operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-control.html)

PCI PIN requirements are organized in Control Objectives.

- [Control Objective 1: PINs used in transactions governed by these requirements are processed using equipment and methodologies that ensure they are kept secure.](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-control-1.html): Requirement 1: HSMs used by AWS Payment Cryptography were assessed as part of our PCI PIN assessment.
- [Control Objective 2: Cryptographic keys used for PIN encryption/decryption and related key management are created using processes that ensure that it is not possible to predict any key or determine that certain keys are more probable than other keys.](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-control-2.html): Requirement 5: Key generation by AWS Payment Cryptography was assessed as part of our PCI PIN assessment.
- [Control Objective 3: Keys are conveyed or transmitted in a secure manner.](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-control-3.html): Requirement 8: Key conveyance with AWS Payment Cryptography was assessed as part of our PCI PIN assessment.
- [Control Objective 4: Key-loading to HSMs and POI PIN-acceptance devices is handled in a secure manner.](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-control-4.html): Requirement 12: You are responsible for loading keys from components or shares.
- [Control Objective 5: Keys are used in a manner that prevents or detects their unauthorized usage.](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-control-5.html): Requirement 17: The service provides mechanisms, such as tags and aliases, for keys that enable tracking of key sharing relationships.
- [Control Objective 6: Keys are administered in a secure manner.](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-control-6.html): Requirement 21: Key storage and use with AWS Payment Cryptography was assessed as part of the serviceâs PCI PIN assessment.
- [Control Objective 7: Equipment used to process PINs and keys is managed in a secure manner.](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-control-7.html): Requirement 29: Your requirements for physical and logical protections for HSMs are met by use of AWS Payment Cryptography.
- [P2PE Compliance](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/p2pe-compliance.html): Instructions for using AWS Payment Cryptography as part of a P2PE solution.


## [Identity and access management](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)

- [How AWS Payment Cryptography works with IAM](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Payment Cryptography, you should understand what IAM features are available to use with AWS Payment Cryptography.
- [Identity-based policy examples](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify AWS Payment Cryptography resources.
- [Troubleshooting](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_troubleshoot.html): Topics will be added to this section as IAM-related issues that are specific to AWS Payment Cryptography are identified.


## [Monitoring](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/monitoring.html)

- [CloudTrail logs](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/monitoring-cloudtrail.html): Learn about logging AWS Payment Cryptography with AWS CloudTrail .


## [Cryptographic details](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/cryptographic-details.html)

- [Design goals](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/cryptographic-details.designgoals.html): AWS Payment Cryptography is designed to meet the following requirements:
- [Foundations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/cryptographic-details.foundations.html): The topics in this chapter describe the cryptographic primitives of AWS Payment Cryptography and where they are used.
- [Internal operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/cryptographic-details-internalops.html): This topic describes internal requirements implemented by the service to secure customer keys and cryptographic operations for a globally distributed and scalable payment cryptography and key management service.
- [Customer operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/cryptographic-details-customerops.html): AWS Payment Cryptography has full responsibility for the HSM physical compliance under PCI standards.
