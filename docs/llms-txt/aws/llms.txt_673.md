# Source: https://docs.aws.amazon.com/privateca/latest/APIReference/llms.txt

# AWS Private Certificate Authority API Reference

> This is the AWS Private Certificate Authority API Reference. It provides descriptions, syntax, and usage examples for each of the actions and data types involved in creating and managing a private certificate authority (CA) for your organization.

- [Welcome](https://docs.aws.amazon.com/privateca/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/privateca/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/privateca/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/privateca/latest/APIReference/API_Operations.html)

- [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html): Creates a root or subordinate private certificate authority (CA).
- [CreateCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html): Creates an audit report that lists every time that your CA private key is used to issue a certificate.
- [CreatePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html): Grants one or more permissions on a private CA to the AWS Certificate Manager (ACM) service principal (acm.amazonaws.com).
- [DeleteCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthority.html): Deletes a private certificate authority (CA).
- [DeletePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html): Revokes permissions on a private CA granted to the AWS Certificate Manager (ACM) service principal (acm.amazonaws.com).
- [DeletePolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePolicy.html): Deletes the resource-based policy attached to a private CA.
- [DescribeCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html): Lists information about your private certificate authority (CA) or one that has been shared with you.
- [DescribeCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthorityAuditReport.html): Lists information about a specific audit report created by calling the CreateCertificateAuthorityAuditReport action.
- [GetCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html): Retrieves a certificate from your private CA or one that has been shared with you.
- [GetCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCertificate.html): Retrieves the certificate and certificate chain for your private certificate authority (CA) or one that has been shared with you.
- [GetCertificateAuthorityCsr](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCsr.html): Retrieves the certificate signing request (CSR) for your private certificate authority (CA).
- [GetPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetPolicy.html): Retrieves the resource-based policy attached to a private CA.
- [ImportCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html): Imports a signed private CA certificate into AWS Private CA.
- [IssueCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html): Uses your private certificate authority (CA), or one that has been shared with you, to issue a client certificate.
- [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html): Lists the private certificate authorities that you created by using the CreateCertificateAuthority action.
- [ListPermissions](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html): List all permissions on a private CA, if any, granted to the AWS Certificate Manager (ACM) service principal (acm.amazonaws.com).
- [ListTags](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListTags.html): Lists the tags, if any, that are associated with your private CA or one that has been shared with you.
- [PutPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html): Attaches a resource-based policy to a private CA.
- [RestoreCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RestoreCertificateAuthority.html): Restores a certificate authority (CA) that is in the DELETED state.
- [RevokeCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html): Revokes a certificate that was issued inside AWS Private CA.
- [TagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html): Adds one or more tags to your private CA.
- [UntagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html): Remove one or more tags from your private CA.
- [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html): Updates the status or configuration of a private certificate authority (CA).


## [Data Types](https://docs.aws.amazon.com/privateca/latest/APIReference/API_Types.html)

- [AccessDescription](https://docs.aws.amazon.com/privateca/latest/APIReference/API_AccessDescription.html): Provides access information used by the authorityInfoAccess and subjectInfoAccess extensions described in RFC 5280.
- [AccessMethod](https://docs.aws.amazon.com/privateca/latest/APIReference/API_AccessMethod.html): Describes the type and format of extension access.
- [ApiPassthrough](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ApiPassthrough.html): Contains X.509 certificate information to be placed in an issued certificate.
- [ASN1Subject](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ASN1Subject.html): Contains information about the certificate subject.
- [CertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CertificateAuthority.html): Contains information about your private certificate authority (CA).
- [CertificateAuthorityConfiguration](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CertificateAuthorityConfiguration.html): Contains configuration information for your private certificate authority (CA).
- [CrlConfiguration](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html): Contains configuration information for a certificate revocation list (CRL).
- [CrlDistributionPointExtensionConfiguration](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlDistributionPointExtensionConfiguration.html): Contains configuration information for the default behavior of the CRL Distribution Point (CDP) extension in certificates issued by your CA.
- [CsrExtensions](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CsrExtensions.html): Describes the certificate extensions to be added to the certificate signing request (CSR).
- [CustomAttribute](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CustomAttribute.html): Defines the X.500 relative distinguished name (RDN).
- [CustomExtension](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CustomExtension.html)
- [EdiPartyName](https://docs.aws.amazon.com/privateca/latest/APIReference/API_EdiPartyName.html): Describes an Electronic Data Interchange (EDI) entity as described in as defined in Subject Alternative Name in RFC 5280.
- [ExtendedKeyUsage](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ExtendedKeyUsage.html): Specifies additional purposes for which the certified public key may be used other than basic purposes indicated in the KeyUsage extension.
- [Extensions](https://docs.aws.amazon.com/privateca/latest/APIReference/API_Extensions.html): Contains X.509 extension information for a certificate.
- [GeneralName](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GeneralName.html): Describes an ASN.1 X.400 GeneralName as defined in RFC 5280.
- [KeyUsage](https://docs.aws.amazon.com/privateca/latest/APIReference/API_KeyUsage.html): Defines one or more purposes for which the key contained in the certificate can be used.
- [OcspConfiguration](https://docs.aws.amazon.com/privateca/latest/APIReference/API_OcspConfiguration.html): Contains information to enable and configure Online Certificate Status Protocol (OCSP) for validating certificate revocation status.
- [OtherName](https://docs.aws.amazon.com/privateca/latest/APIReference/API_OtherName.html): Defines a custom ASN.1 X.400 GeneralName using an object identifier (OID) and value.
- [Permission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_Permission.html): Permissions designate which private CA actions can be performed by an AWS service or entity.
- [PolicyInformation](https://docs.aws.amazon.com/privateca/latest/APIReference/API_PolicyInformation.html): Defines the X.509 CertificatePolicies extension.
- [PolicyQualifierInfo](https://docs.aws.amazon.com/privateca/latest/APIReference/API_PolicyQualifierInfo.html): Modifies the CertPolicyId of a PolicyInformation object with a qualifier.
- [Qualifier](https://docs.aws.amazon.com/privateca/latest/APIReference/API_Qualifier.html): Defines a PolicyInformation qualifier.
- [RevocationConfiguration](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevocationConfiguration.html): Certificate revocation information used by the CreateCertificateAuthority and UpdateCertificateAuthority actions.
- [Tag](https://docs.aws.amazon.com/privateca/latest/APIReference/API_Tag.html): Tags are labels that you can use to identify and organize your private CAs.
- [Validity](https://docs.aws.amazon.com/privateca/latest/APIReference/API_Validity.html): Validity specifies the period of time during which a certificate is valid.
