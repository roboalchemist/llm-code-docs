# Source: https://docs.aws.amazon.com/acm/latest/APIReference/llms.txt

# AWS Certificate Manager API Reference

> You can use AWS Certificate Manager (ACM) to manage SSL/TLS certificates for your AWS-based websites and applications. For more information about using ACM, see the AWS Certificate Manager User Guide.

- [Welcome](https://docs.aws.amazon.com/acm/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/acm/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/acm/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/acm/latest/APIReference/API_Operations.html)

- [AddTagsToCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_AddTagsToCertificate.html): Adds one or more tags to an ACM certificate.
- [DeleteCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteCertificate.html): Deletes a certificate and its associated private key.
- [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html): Returns detailed metadata about the specified ACM certificate.
- [ExportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ExportCertificate.html): Exports a private certificate issued by a private certificate authority (CA) or a public certificate for use anywhere.
- [GetAccountConfiguration](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetAccountConfiguration.html): Returns the account configuration options associated with an AWS account.
- [GetCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetCertificate.html): Retrieves a certificate and its certificate chain.
- [ImportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ImportCertificate.html): Imports a certificate into AWS Certificate Manager (ACM) to use with services that are integrated with ACM.
- [ListCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html): Retrieves a list of certificate ARNs and domain names.
- [ListTagsForCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForCertificate.html): Lists the tags that have been applied to the ACM certificate.
- [PutAccountConfiguration](https://docs.aws.amazon.com/acm/latest/APIReference/API_PutAccountConfiguration.html): Adds or modifies account-level configurations in ACM.
- [RemoveTagsFromCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RemoveTagsFromCertificate.html): Remove one or more tags from an ACM certificate.
- [RenewCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RenewCertificate.html): Renews an eligible ACM certificate.
- [RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html): Requests an ACM certificate for use with other AWS services.
- [ResendValidationEmail](https://docs.aws.amazon.com/acm/latest/APIReference/API_ResendValidationEmail.html): Resends the email that requests domain ownership validation.
- [RevokeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeCertificate.html): Revokes a public ACM certificate.
- [UpdateCertificateOptions](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateCertificateOptions.html): Updates a certificate.


## [Data Types](https://docs.aws.amazon.com/acm/latest/APIReference/API_Types.html)

- [CertificateDetail](https://docs.aws.amazon.com/acm/latest/APIReference/API_CertificateDetail.html): Contains metadata about an ACM certificate.
- [CertificateOptions](https://docs.aws.amazon.com/acm/latest/APIReference/API_CertificateOptions.html): Structure that contains options for your certificate.
- [CertificateSummary](https://docs.aws.amazon.com/acm/latest/APIReference/API_CertificateSummary.html): This structure is returned in the response object of action.
- [DomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_DomainValidation.html): Contains information about the validation of each domain name in the certificate.
- [DomainValidationOption](https://docs.aws.amazon.com/acm/latest/APIReference/API_DomainValidationOption.html): Contains information about the domain names that you want ACM to use to send you emails that enable you to validate domain ownership.
- [ExpiryEventsConfiguration](https://docs.aws.amazon.com/acm/latest/APIReference/API_ExpiryEventsConfiguration.html): Object containing expiration events options associated with an AWS account.
- [ExtendedKeyUsage](https://docs.aws.amazon.com/acm/latest/APIReference/API_ExtendedKeyUsage.html): The Extended Key Usage X.509 v3 extension defines one or more purposes for which the public key can be used.
- [Filters](https://docs.aws.amazon.com/acm/latest/APIReference/API_Filters.html): This structure can be used in the action to filter the output of the certificate list.
- [HttpRedirect](https://docs.aws.amazon.com/acm/latest/APIReference/API_HttpRedirect.html): Contains information for HTTP-based domain validation of certificates requested through Amazon CloudFront and issued by ACM.
- [KeyUsage](https://docs.aws.amazon.com/acm/latest/APIReference/API_KeyUsage.html): The Key Usage X.509 v3 extension defines the purpose of the public key contained in the certificate.
- [RenewalSummary](https://docs.aws.amazon.com/acm/latest/APIReference/API_RenewalSummary.html): Contains information about the status of ACM's managed renewal for the certificate.
- [ResourceRecord](https://docs.aws.amazon.com/acm/latest/APIReference/API_ResourceRecord.html): Contains a DNS record value that you can use to validate ownership or control of a domain.
- [Tag](https://docs.aws.amazon.com/acm/latest/APIReference/API_Tag.html): A key-value pair that identifies or specifies metadata about an ACM resource.
- [ThrottlingReason](https://docs.aws.amazon.com/acm/latest/APIReference/API_ThrottlingReason.html): A description of why a request was throttled.
