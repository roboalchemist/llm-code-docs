# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_acm.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_acm{% #aws_acm %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `certificate_arn`{% #certificate_arn %}

**Type**: `STRING`**Provider name**: `CertificateArn`**Description**: The Amazon Resource Name (ARN) of the certificate. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the Amazon Web Services General Reference.

## `certificate_authority_arn`{% #certificate_authority_arn %}

**Type**: `STRING`**Provider name**: `CertificateAuthorityArn`**Description**: The Amazon Resource Name (ARN) of the private certificate authority (CA) that issued the certificate. This has the following format: `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012`

## `created_at`{% #created_at %}

**Type**: `TIMESTAMP`**Provider name**: `CreatedAt`**Description**: The time at which the certificate was requested.

## `domain_name`{% #domain_name %}

**Type**: `STRING`**Provider name**: `DomainName`**Description**: The fully qualified domain name for the certificate, such as [www.example.com](https://www.example.com) or example.com.

## `domain_validation_options`{% #domain_validation_options %}

**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `DomainValidationOptions`**Description**: Contains information about the initial validation of each domain name that occurs as a result of the RequestCertificate request. This field exists only when the certificate type is `AMAZON_ISSUED`.

- `domain_name`**Type**: `STRING`**Provider name**: `DomainName`**Description**: A fully qualified domain name (FQDN) in the certificate. For example, `www.example.com` or `example.com`.
- `resource_record`**Type**: `STRUCT`**Provider name**: `ResourceRecord`**Description**: Contains the CNAME record that you add to your DNS database for domain validation. For more information, see [Use DNS to Validate Domain Ownership](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html). Note: The CNAME information that you need does not include the name of your domain. If you include your domain name in the DNS database CNAME record, validation fails. For example, if the name is "_a79865eb4cd1a6ab990a45779b4e0b96.yourdomain.com", only "_a79865eb4cd1a6ab990a45779b4e0b96" must be used.
  - `name`**Type**: `STRING`**Provider name**: `Name`**Description**: The name of the DNS record to create in your domain. This is supplied by ACM.
  - `type`**Type**: `STRING`**Provider name**: `Type`**Description**: The type of DNS record. Currently this can be `CNAME`.
  - `value`**Type**: `STRING`**Provider name**: `Value`**Description**: The value of the CNAME record to add to your DNS database. This is supplied by ACM.
- `validation_domain`**Type**: `STRING`**Provider name**: `ValidationDomain`**Description**: The domain name that ACM used to send domain validation emails.
- `validation_emails`**Type**: `UNORDERED_LIST_STRING`**Provider name**: `ValidationEmails`**Description**: A list of email addresses that ACM used to send domain validation emails.
- `validation_method`**Type**: `STRING`**Provider name**: `ValidationMethod`**Description**: Specifies the domain validation method.
- `validation_status`**Type**: `STRING`**Provider name**: `ValidationStatus`**Description**: The validation status of the domain name. This can be one of the following values:
  - `PENDING_VALIDATION`
  - `SUCCESS`
  - `FAILED`

## `exported`{% #exported %}

**Type**: `BOOLEAN`**Provider name**: `Exported`**Description**: Indicates whether the certificate has been exported. This value exists only when the certificate type is `PRIVATE`.

## `extended_key_usages`{% #extended_key_usages %}

**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `ExtendedKeyUsages`**Description**: Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID).

- `name`**Type**: `STRING`**Provider name**: `Name`**Description**: The name of an Extended Key Usage value.
- `oid`**Type**: `STRING`**Provider name**: `OID`**Description**: An object identifier (OID) for the extension value. OIDs are strings of numbers separated by periods. The following OIDs are defined in RFC 3280 and RFC 5280.
  - `1.3.6.1.5.5.7.3.1 (TLS_WEB_SERVER_AUTHENTICATION)`
  - `1.3.6.1.5.5.7.3.2 (TLS_WEB_CLIENT_AUTHENTICATION)`
  - `1.3.6.1.5.5.7.3.3 (CODE_SIGNING)`
  - `1.3.6.1.5.5.7.3.4 (EMAIL_PROTECTION)`
  - `1.3.6.1.5.5.7.3.8 (TIME_STAMPING)`
  - `1.3.6.1.5.5.7.3.9 (OCSP_SIGNING)`
  - `1.3.6.1.5.5.7.3.5 (IPSEC_END_SYSTEM)`
  - `1.3.6.1.5.5.7.3.6 (IPSEC_TUNNEL)`
  - `1.3.6.1.5.5.7.3.7 (IPSEC_USER)`

## `failure_reason`{% #failure_reason %}

**Type**: `STRING`**Provider name**: `FailureReason`**Description**: The reason the certificate request failed. This value exists only when the certificate status is `FAILED`. For more information, see [Certificate Request Failed](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting.html#troubleshooting-failed) in the Certificate Manager User Guide.

## `has_additional_subject_alternative_names`{% #has_additional_subject_alternative_names %}

**Type**: `BOOLEAN`**Provider name**: `HasAdditionalSubjectAlternativeNames`**Description**: When called by ListCertificates, indicates whether the full list of subject alternative names has been included in the response. If false, the response includes all of the subject alternative names included in the certificate. If true, the response only includes the first 100 subject alternative names included in the certificate. To display the full list of subject alternative names, use DescribeCertificate.

## `imported_at`{% #imported_at %}

**Type**: `TIMESTAMP`**Provider name**: `ImportedAt`**Description**: The date and time when the certificate was imported. This value exists only when the certificate type is `IMPORTED`.

## `in_use`{% #in_use %}

**Type**: `BOOLEAN`**Provider name**: `InUse`**Description**: Indicates whether the certificate is currently in use by any Amazon Web Services resources.

## `in_use_by`{% #in_use_by %}

**Type**: `UNORDERED_LIST_STRING`**Provider name**: `InUseBy`**Description**: A list of ARNs for the Amazon Web Services resources that are using the certificate. A certificate can be used by multiple Amazon Web Services resources.

## `issued_at`{% #issued_at %}

**Type**: `TIMESTAMP`**Provider name**: `IssuedAt`**Description**: The time at which the certificate was issued. This value exists only when the certificate type is `AMAZON_ISSUED`.

## `issuer`{% #issuer %}

**Type**: `STRING`**Provider name**: `Issuer`**Description**: The name of the certificate authority that issued and signed the certificate.

## `key_algorithm`{% #key_algorithm %}

**Type**: `STRING`**Provider name**: `KeyAlgorithm`**Description**: The algorithm that was used to generate the public-private key pair.

## `key_usages`{% #key_usages %}

**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `KeyUsages`**Description**: A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include `DIGITAL_SIGNATURE`, `KEY_ENCIPHERMENT`, `NON_REPUDIATION`, and more.

- `name`**Type**: `STRING`**Provider name**: `Name`**Description**: A string value that contains a Key Usage extension name.

## `not_after`{% #not_after %}

**Type**: `TIMESTAMP`**Provider name**: `NotAfter`**Description**: The time after which the certificate is not valid.

## `not_before`{% #not_before %}

**Type**: `TIMESTAMP`**Provider name**: `NotBefore`**Description**: The time before which the certificate is not valid.

## `options`{% #options %}

**Type**: `STRUCT`**Provider name**: `Options`**Description**: Value that specifies whether to add the certificate to a transparency log. Certificate transparency makes it possible to detect SSL certificates that have been mistakenly or maliciously issued. A browser might respond to certificate that has not been logged by showing an error message. The logs are cryptographically secure.

- `certificate_transparency_logging_preference`**Type**: `STRING`**Provider name**: `CertificateTransparencyLoggingPreference`**Description**: You can opt out of certificate transparency logging by specifying the `DISABLED` option. Opt in by specifying `ENABLED`.

## `renewal_eligibility`{% #renewal_eligibility %}

**Type**: `STRING`**Provider name**: `RenewalEligibility`**Description**: Specifies whether the certificate is eligible for renewal. At this time, only exported private certificates can be renewed with the RenewCertificate command.

## `renewal_summary`{% #renewal_summary %}

**Type**: `STRUCT`**Provider name**: `RenewalSummary`**Description**: Contains information about the status of ACM's [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for the certificate. This field exists only when the certificate type is `AMAZON_ISSUED`.

- `domain_validation_options`**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `DomainValidationOptions`**Description**: Contains information about the validation of each domain name in the certificate, as it pertains to ACM's [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html). This is different from the initial validation that occurs as a result of the RequestCertificate request. This field exists only when the certificate type is `AMAZON_ISSUED`.
  - `domain_name`**Type**: `STRING`**Provider name**: `DomainName`**Description**: A fully qualified domain name (FQDN) in the certificate. For example, `www.example.com` or `example.com`.
  - `resource_record`**Type**: `STRUCT`**Provider name**: `ResourceRecord`**Description**: Contains the CNAME record that you add to your DNS database for domain validation. For more information, see [Use DNS to Validate Domain Ownership](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html). Note: The CNAME information that you need does not include the name of your domain. If you include your domain name in the DNS database CNAME record, validation fails. For example, if the name is "_a79865eb4cd1a6ab990a45779b4e0b96.yourdomain.com", only "_a79865eb4cd1a6ab990a45779b4e0b96" must be used.
    - `name`**Type**: `STRING`**Provider name**: `Name`**Description**: The name of the DNS record to create in your domain. This is supplied by ACM.
    - `type`**Type**: `STRING`**Provider name**: `Type`**Description**: The type of DNS record. Currently this can be `CNAME`.
    - `value`**Type**: `STRING`**Provider name**: `Value`**Description**: The value of the CNAME record to add to your DNS database. This is supplied by ACM.
  - `validation_domain`**Type**: `STRING`**Provider name**: `ValidationDomain`**Description**: The domain name that ACM used to send domain validation emails.
  - `validation_emails`**Type**: `UNORDERED_LIST_STRING`**Provider name**: `ValidationEmails`**Description**: A list of email addresses that ACM used to send domain validation emails.
  - `validation_method`**Type**: `STRING`**Provider name**: `ValidationMethod`**Description**: Specifies the domain validation method.
  - `validation_status`**Type**: `STRING`**Provider name**: `ValidationStatus`**Description**: The validation status of the domain name. This can be one of the following values:
    - `PENDING_VALIDATION`
    - `SUCCESS`
    - `FAILED`
- `renewal_status`**Type**: `STRING`**Provider name**: `RenewalStatus`**Description**: The status of ACM's [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) of the certificate.
- `renewal_status_reason`**Type**: `STRING`**Provider name**: `RenewalStatusReason`**Description**: The reason that a renewal request was unsuccessful.
- `updated_at`**Type**: `TIMESTAMP`**Provider name**: `UpdatedAt`**Description**: The time at which the renewal summary was last updated.

## `revocation_reason`{% #revocation_reason %}

**Type**: `STRING`**Provider name**: `RevocationReason`**Description**: The reason the certificate was revoked. This value exists only when the certificate status is `REVOKED`.

## `revoked_at`{% #revoked_at %}

**Type**: `TIMESTAMP`**Provider name**: `RevokedAt`**Description**: The time at which the certificate was revoked. This value exists only when the certificate status is `REVOKED`.

## `serial`{% #serial %}

**Type**: `STRING`**Provider name**: `Serial`**Description**: The serial number of the certificate.

## `signature_algorithm`{% #signature_algorithm %}

**Type**: `STRING`**Provider name**: `SignatureAlgorithm`**Description**: The algorithm that was used to sign the certificate.

## `status`{% #status %}

**Type**: `STRING`**Provider name**: `Status`**Description**: The status of the certificate. A certificate enters status PENDING_VALIDATION upon being requested, unless it fails for any of the reasons given in the troubleshooting topic [Certificate request fails](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-failed.html). ACM makes repeated attempts to validate a certificate for 72 hours and then times out. If a certificate shows status FAILED or VALIDATION_TIMED_OUT, delete the request, correct the issue with [DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html) or [Email validation](https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html), and try again. If validation succeeds, the certificate enters status ISSUED.

## `subject`{% #subject %}

**Type**: `STRING`**Provider name**: `Subject`**Description**: The name of the entity that is associated with the public key contained in the certificate.

## `subject_alternative_name_summaries`{% #subject_alternative_name_summaries %}

**Type**: `UNORDERED_LIST_STRING`**Provider name**: `SubjectAlternativeNameSummaries`**Description**: One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website. When called by ListCertificates, this parameter will only return the first 100 subject alternative names included in the certificate. To display the full list of subject alternative names, use DescribeCertificate.

## `subject_alternative_names`{% #subject_alternative_names %}

**Type**: `UNORDERED_LIST_STRING`**Provider name**: `SubjectAlternativeNames`**Description**: One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`

## `type`{% #type %}

**Type**: `STRING`**Provider name**: `Type`**Description**: The source of the certificate. For certificates provided by ACM, this value is `AMAZON_ISSUED`. For certificates that you imported with ImportCertificate, this value is `IMPORTED`. ACM does not provide [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see [Importing Certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the Certificate Manager User Guide.
