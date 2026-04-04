# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_acmpca_certificateauthority.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_acmpca_certificateauthority{% #aws_acmpca_certificateauthority %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `arn`{% #arn %}

**Type**: `STRING`**Provider name**: `Arn`**Description**: Amazon Resource Name (ARN) for your private certificate authority (CA). The format is `12345678-1234-1234-1234-123456789012`.

## `certificate_authority_configuration`{% #certificate_authority_configuration %}

**Type**: `STRUCT`**Provider name**: `CertificateAuthorityConfiguration`**Description**: Your private CA configuration.

- `csr_extensions`**Type**: `STRUCT`**Provider name**: `CsrExtensions`**Description**: Specifies information to be added to the extension section of the certificate signing request (CSR).
  - `key_usage`**Type**: `STRUCT`**Provider name**: `KeyUsage`**Description**: Indicates the purpose of the certificate and of the key contained in the certificate.
    - `crl_sign`**Type**: `BOOLEAN`**Provider name**: `CRLSign`**Description**: Key can be used to sign CRLs.
    - `data_encipherment`**Type**: `BOOLEAN`**Provider name**: `DataEncipherment`**Description**: Key can be used to decipher data.
    - `decipher_only`**Type**: `BOOLEAN`**Provider name**: `DecipherOnly`**Description**: Key can be used only to decipher data.
    - `digital_signature`**Type**: `BOOLEAN`**Provider name**: `DigitalSignature`**Description**: Key can be used for digital signing.
    - `encipher_only`**Type**: `BOOLEAN`**Provider name**: `EncipherOnly`**Description**: Key can be used only to encipher data.
    - `key_agreement`**Type**: `BOOLEAN`**Provider name**: `KeyAgreement`**Description**: Key can be used in a key-agreement protocol.
    - `key_cert_sign`**Type**: `BOOLEAN`**Provider name**: `KeyCertSign`**Description**: Key can be used to sign certificates.
    - `key_encipherment`**Type**: `BOOLEAN`**Provider name**: `KeyEncipherment`**Description**: Key can be used to encipher data.
    - `non_repudiation`**Type**: `BOOLEAN`**Provider name**: `NonRepudiation`**Description**: Key can be used for non-repudiation.
  - `subject_information_access`**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `SubjectInformationAccess`**Description**: For CA certificates, provides a path to additional information pertaining to the CA, such as revocation and policy. For more information, see [Subject Information Access](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.2.2) in RFC 5280.
    - `access_location`**Type**: `STRUCT`**Provider name**: `AccessLocation`**Description**: The location of `AccessDescription` information.
      - `directory_name`**Type**: `STRUCT`**Provider name**: `DirectoryName`
        - `common_name`**Type**: `STRING`**Provider name**: `CommonName`**Description**: For CA and end-entity certificates in a private PKI, the common name (CN) can be any string within the length limit. Note: In publicly trusted certificates, the common name must be a fully qualified domain name (FQDN) associated with the certificate subject.
        - `country`**Type**: `STRING`**Provider name**: `Country`**Description**: Two-digit code that specifies the country in which the certificate subject located.
        - `custom_attributes`**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `CustomAttributes`**Description**: Contains a sequence of one or more X.500 relative distinguished names (RDNs), each of which consists of an object identifier (OID) and a value. For more information, see NIST's definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier).Custom attributes cannot be used in combination with standard attributes.
          - `object_identifier`**Type**: `STRING`**Provider name**: `ObjectIdentifier`**Description**: Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).
          - `value`**Type**: `STRING`**Provider name**: `Value`**Description**: Specifies the attribute value of relative distinguished name (RDN).
        - `distinguished_name_qualifier`**Type**: `STRING`**Provider name**: `DistinguishedNameQualifier`**Description**: Disambiguating information for the certificate subject.
        - `generation_qualifier`**Type**: `STRING`**Provider name**: `GenerationQualifier`**Description**: Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.
        - `given_name`**Type**: `STRING`**Provider name**: `GivenName`**Description**: First name.
        - `initials`**Type**: `STRING`**Provider name**: `Initials`**Description**: Concatenation that typically contains the first letter of the GivenName, the first letter of the middle name if one exists, and the first letter of the Surname.
        - `locality`**Type**: `STRING`**Provider name**: `Locality`**Description**: The locality (such as a city or town) in which the certificate subject is located.
        - `organization`**Type**: `STRING`**Provider name**: `Organization`**Description**: Legal name of the organization with which the certificate subject is affiliated.
        - `organizational_unit`**Type**: `STRING`**Provider name**: `OrganizationalUnit`**Description**: A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.
        - `pseudonym`**Type**: `STRING`**Provider name**: `Pseudonym`**Description**: Typically a shortened version of a longer GivenName. For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.
        - `serial_number`**Type**: `STRING`**Provider name**: `SerialNumber`**Description**: The certificate serial number.
        - `state`**Type**: `STRING`**Provider name**: `State`**Description**: State in which the subject of the certificate is located.
        - `surname`**Type**: `STRING`**Provider name**: `Surname`**Description**: Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.
        - `title`**Type**: `STRING`**Provider name**: `Title`**Description**: A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.
      - `dns_name`**Type**: `STRING`**Provider name**: `DnsName`**Description**: Represents `GeneralName` as a DNS name.
      - `edi_party_name`**Type**: `STRUCT`**Provider name**: `EdiPartyName`**Description**: Represents `GeneralName` as an `EdiPartyName` object.
        - `name_assigner`**Type**: `STRING`**Provider name**: `NameAssigner`**Description**: Specifies the name assigner.
        - `party_name`**Type**: `STRING`**Provider name**: `PartyName`**Description**: Specifies the party name.
      - `ip_address`**Type**: `STRING`**Provider name**: `IpAddress`**Description**: Represents `GeneralName` as an IPv4 or IPv6 address.
      - `other_name`**Type**: `STRUCT`**Provider name**: `OtherName`**Description**: Represents `GeneralName` using an `OtherName` object.
        - `type_id`**Type**: `STRING`**Provider name**: `TypeId`**Description**: Specifies an OID.
        - `value`**Type**: `STRING`**Provider name**: `Value`**Description**: Specifies an OID value.
      - `registered_id`**Type**: `STRING`**Provider name**: `RegisteredId`**Description**: Represents `GeneralName` as an object identifier (OID).
      - `rfc822_name`**Type**: `STRING`**Provider name**: `Rfc822Name`**Description**: Represents `GeneralName` as an [RFC 822](https://datatracker.ietf.org/doc/html/rfc822) email address.
      - `uniform_resource_identifier`**Type**: `STRING`**Provider name**: `UniformResourceIdentifier`**Description**: Represents `GeneralName` as a URI.
    - `access_method`**Type**: `STRUCT`**Provider name**: `AccessMethod`**Description**: The type and format of `AccessDescription` information.
      - `access_method_type`**Type**: `STRING`**Provider name**: `AccessMethodType`**Description**: Specifies the `AccessMethod`.
      - `custom_object_identifier`**Type**: `STRING`**Provider name**: `CustomObjectIdentifier`**Description**: An object identifier (OID) specifying the `AccessMethod`. The OID must satisfy the regular expression shown below. For more information, see NIST's definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier).
- `key_algorithm`**Type**: `STRING`**Provider name**: `KeyAlgorithm`**Description**: Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate. When you create a subordinate CA, you must use a key algorithm supported by the parent CA.
- `signing_algorithm`**Type**: `STRING`**Provider name**: `SigningAlgorithm`**Description**: Name of the algorithm your private CA uses to sign certificate requests. This parameter should not be confused with the `SigningAlgorithm` parameter used to sign certificates when they are issued.
- `subject`**Type**: `STRUCT`**Provider name**: `Subject`**Description**: Structure that contains X.500 distinguished name information for your private CA.
  - `common_name`**Type**: `STRING`**Provider name**: `CommonName`**Description**: For CA and end-entity certificates in a private PKI, the common name (CN) can be any string within the length limit. Note: In publicly trusted certificates, the common name must be a fully qualified domain name (FQDN) associated with the certificate subject.
  - `country`**Type**: `STRING`**Provider name**: `Country`**Description**: Two-digit code that specifies the country in which the certificate subject located.
  - `custom_attributes`**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `CustomAttributes`**Description**: Contains a sequence of one or more X.500 relative distinguished names (RDNs), each of which consists of an object identifier (OID) and a value. For more information, see NIST's definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier).Custom attributes cannot be used in combination with standard attributes.
    - `object_identifier`**Type**: `STRING`**Provider name**: `ObjectIdentifier`**Description**: Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).
    - `value`**Type**: `STRING`**Provider name**: `Value`**Description**: Specifies the attribute value of relative distinguished name (RDN).
  - `distinguished_name_qualifier`**Type**: `STRING`**Provider name**: `DistinguishedNameQualifier`**Description**: Disambiguating information for the certificate subject.
  - `generation_qualifier`**Type**: `STRING`**Provider name**: `GenerationQualifier`**Description**: Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.
  - `given_name`**Type**: `STRING`**Provider name**: `GivenName`**Description**: First name.
  - `initials`**Type**: `STRING`**Provider name**: `Initials`**Description**: Concatenation that typically contains the first letter of the GivenName, the first letter of the middle name if one exists, and the first letter of the Surname.
  - `locality`**Type**: `STRING`**Provider name**: `Locality`**Description**: The locality (such as a city or town) in which the certificate subject is located.
  - `organization`**Type**: `STRING`**Provider name**: `Organization`**Description**: Legal name of the organization with which the certificate subject is affiliated.
  - `organizational_unit`**Type**: `STRING`**Provider name**: `OrganizationalUnit`**Description**: A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.
  - `pseudonym`**Type**: `STRING`**Provider name**: `Pseudonym`**Description**: Typically a shortened version of a longer GivenName. For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.
  - `serial_number`**Type**: `STRING`**Provider name**: `SerialNumber`**Description**: The certificate serial number.
  - `state`**Type**: `STRING`**Provider name**: `State`**Description**: State in which the subject of the certificate is located.
  - `surname`**Type**: `STRING`**Provider name**: `Surname`**Description**: Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.
  - `title`**Type**: `STRING`**Provider name**: `Title`**Description**: A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.

## `created_at`{% #created_at %}

**Type**: `TIMESTAMP`**Provider name**: `CreatedAt`**Description**: Date and time at which your private CA was created.

## `failure_reason`{% #failure_reason %}

**Type**: `STRING`**Provider name**: `FailureReason`**Description**: Reason the request to create your private CA failed.

## `key_storage_security_standard`{% #key_storage_security_standard %}

**Type**: `STRING`**Provider name**: `KeyStorageSecurityStandard`**Description**: Defines a cryptographic key management compliance standard used for handling CA keys.**Default**: FIPS_140_2_LEVEL_3_OR_HIGHER

Note: Amazon Web Services Region ap-northeast-3 supports only FIPS_140_2_LEVEL_2_OR_HIGHER. You must explicitly specify this parameter and value when creating a CA in that Region. Specifying a different value (or no value) results in an `InvalidArgsException` with the message "A certificate authority cannot be created in this region with the specified security standard."

## `last_state_change_at`{% #last_state_change_at %}

**Type**: `TIMESTAMP`**Provider name**: `LastStateChangeAt`**Description**: Date and time at which your private CA was last updated.

## `not_after`{% #not_after %}

**Type**: `TIMESTAMP`**Provider name**: `NotAfter`**Description**: Date and time after which your private CA certificate is not valid.

## `not_before`{% #not_before %}

**Type**: `TIMESTAMP`**Provider name**: `NotBefore`**Description**: Date and time before which your private CA certificate is not valid.

## `owner_account`{% #owner_account %}

**Type**: `STRING`**Provider name**: `OwnerAccount`**Description**: The Amazon Web Services account ID that owns the certificate authority.

## `restorable_until`{% #restorable_until %}

**Type**: `TIMESTAMP`**Provider name**: `RestorableUntil`**Description**: The period during which a deleted CA can be restored. For more information, see the `PermanentDeletionTimeInDays` parameter of the [DeleteCertificateAuthorityRequest](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthorityRequest.html) action.

## `revocation_configuration`{% #revocation_configuration %}

**Type**: `STRUCT`**Provider name**: `RevocationConfiguration`**Description**: Information about the Online Certificate Status Protocol (OCSP) configuration or certificate revocation list (CRL) created and maintained by your private CA.

- `crl_configuration`**Type**: `STRUCT`**Provider name**: `CrlConfiguration`**Description**: Configuration of the certificate revocation list (CRL), if any, maintained by your private CA. A CRL is typically updated approximately 30 minutes after a certificate is revoked. If for any reason a CRL update fails, Amazon Web Services Private CA makes further attempts every 15 minutes.
  - `crl_distribution_point_extension_configuration`**Type**: `STRUCT`**Provider name**: `CrlDistributionPointExtensionConfiguration`**Description**: Configures the behavior of the CRL Distribution Point extension for certificates issued by your certificate authority. If this field is not provided, then the CRl Distribution Point Extension will be present and contain the default CRL URL.
    - `omit_extension`**Type**: `BOOLEAN`**Provider name**: `OmitExtension`**Description**: Configures whether the CRL Distribution Point extension should be populated with the default URL to the CRL. If set to `true`, then the CDP extension will not be present in any certificates issued by that CA unless otherwise specified through CSR or API passthrough.Only set this if you have another way to distribute the CRL Distribution Points ffor certificates issued by your CA, such as the Matter Distributed Compliance Ledger This configuration cannot be enabled with a custom CNAME set.
  - `crl_type`**Type**: `STRING`**Provider name**: `CrlType`**Description**: Specifies whether to create a complete or partitioned CRL. This setting determines the maximum number of certificates that the certificate authority can issue and revoke. For more information, see Amazon Web Services Private CA quotas.
    - `COMPLETE` - The default setting. Amazon Web Services Private CA maintains a single CRL ï¬le for all unexpired certiï¬cates issued by a CA that have been revoked for any reason. Each certiï¬cate that Amazon Web Services Private CA issues is bound to a speciï¬c CRL through its CRL distribution point (CDP) extension, deï¬ned in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.9).
    - `PARTITIONED` - Compared to complete CRLs, partitioned CRLs dramatically increase the number of certiï¬cates your private CA can issue.When using partitioned CRLs, you must validate that the CRL's associated issuing distribution point (IDP) URI matches the certiï¬cate's CDP URI to ensure the right CRL has been fetched. Amazon Web Services Private CA marks the IDP extension as critical, which your client must be able to process.
  - `custom_cname`**Type**: `STRING`**Provider name**: `CustomCname`**Description**: Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point. Use this value if you don't want the name of your S3 bucket to be public.The content of a Canonical Name (CNAME) record must conform to [RFC2396](https://www.ietf.org/rfc/rfc2396.txt) restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as "http://" or "https://".
  - `custom_path`**Type**: `STRING`**Provider name**: `CustomPath`**Description**: Designates a custom ï¬le path in S3 for CRL(s). For example, `http://<CustomName>/ <CustomPath>/<CrlPartition_GUID>.crl`.
  - `enabled`**Type**: `BOOLEAN`**Provider name**: `Enabled`**Description**: Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action or for an existing CA when you call the [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html) action.
  - `expiration_in_days`**Type**: `INT32`**Provider name**: `ExpirationInDays`**Description**: Validity period of the CRL in days.
  - `s3_bucket_name`**Type**: `STRING`**Provider name**: `S3BucketName`**Description**: Name of the S3 bucket that contains the CRL. If you do not provide a value for the CustomCname argument, the name of your S3 bucket is placed into the CRL Distribution Points extension of the issued certificate. You can change the name of your bucket by calling the [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html) operation. You must specify a [bucket policy](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCreateCa.html#s3-policies) that allows Amazon Web Services Private CA to write the CRL to your bucket.The `S3BucketName` parameter must conform to the [S3 bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).
  - `s3_object_acl`**Type**: `STRING`**Provider name**: `S3ObjectAcl`**Description**: Determines whether the CRL will be publicly readable or privately held in the CRL Amazon S3 bucket. If you choose PUBLIC_READ, the CRL will be accessible over the public internet. If you choose BUCKET_OWNER_FULL_CONTROL, only the owner of the CRL S3 bucket can access the CRL, and your PKI clients may need an alternative method of access. If no value is specified, the default is `PUBLIC_READ`. Note: This default can cause CA creation to fail in some circumstances. If you have have enabled the Block Public Access (BPA) feature in your S3 account, then you must specify the value of this parameter as `BUCKET_OWNER_FULL_CONTROL`, and not doing so results in an error. If you have disabled BPA in S3, then you can specify either `BUCKET_OWNER_FULL_CONTROL` or `PUBLIC_READ` as the value. For more information, see [Blocking public access to the S3 bucket](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCreateCa.html#s3-bpa).
- `ocsp_configuration`**Type**: `STRUCT`**Provider name**: `OcspConfiguration`**Description**: Configuration of Online Certificate Status Protocol (OCSP) support, if any, maintained by your private CA. When you revoke a certificate, OCSP responses may take up to 60 minutes to reflect the new status.
  - `enabled`**Type**: `BOOLEAN`**Provider name**: `Enabled`**Description**: Flag enabling use of the Online Certificate Status Protocol (OCSP) for validating certificate revocation status.
  - `ocsp_custom_cname`**Type**: `STRING`**Provider name**: `OcspCustomCname`**Description**: By default, Amazon Web Services Private CA injects an Amazon Web Services domain into certificates being validated by the Online Certificate Status Protocol (OCSP). A customer can alternatively use this object to define a CNAME specifying a customized OCSP domain.The content of a Canonical Name (CNAME) record must conform to [RFC2396](https://www.ietf.org/rfc/rfc2396.txt) restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as "http://" or "https://".For more information, see [Customizing Online Certificate Status Protocol (OCSP) ](https://docs.aws.amazon.com/privateca/latest/userguide/ocsp-customize.html)in the Amazon Web Services Private Certificate Authority User Guide.

## `serial`{% #serial %}

**Type**: `STRING`**Provider name**: `Serial`**Description**: Serial number of your private CA.

## `status`{% #status %}

**Type**: `STRING`**Provider name**: `Status`**Description**: Status of your private CA.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`

## `type`{% #type %}

**Type**: `STRING`**Provider name**: `Type`**Description**: Type of your private CA.

## `usage_mode`{% #usage_mode %}

**Type**: `STRING`**Provider name**: `UsageMode`**Description**: Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly. Short-lived certificate validity is limited to seven days. The default value is GENERAL_PURPOSE.
