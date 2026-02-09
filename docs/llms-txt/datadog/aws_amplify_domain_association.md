# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_amplify_domain_association.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_amplify_domain_association{% #aws_amplify_domain_association %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `auto_sub_domain_creation_patterns`{% #auto_sub_domain_creation_patterns %}

**Type**: `UNORDERED_LIST_STRING`**Provider name**: `autoSubDomainCreationPatterns`**Description**: Sets branch patterns for automatic subdomain creation.

## `auto_sub_domain_iam_role`{% #auto_sub_domain_iam_role %}

**Type**: `STRING`**Provider name**: `autoSubDomainIAMRole`**Description**: The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains.

## `certificate`{% #certificate %}

**Type**: `STRUCT`**Provider name**: `certificate`**Description**: Describes the SSL/TLS certificate for the domain association. This can be your own custom certificate or the default certificate that Amplify provisions for you. If you are updating your domain to use a different certificate, `certificate` points to the new certificate that is being created instead of the current active certificate. Otherwise, `certificate` points to the current active certificate.

- `certificate_verification_dns_record`**Type**: `STRING`**Provider name**: `certificateVerificationDNSRecord`**Description**: The DNS record for certificate verification.
- `custom_certificate_arn`**Type**: `STRING`**Provider name**: `customCertificateArn`**Description**: The Amazon resource name (ARN) for a custom certificate that you have already added to Certificate Manager in your Amazon Web Services account. This field is required only when the certificate type is `CUSTOM`.
- `type`**Type**: `STRING`**Provider name**: `type`**Description**: The type of SSL/TLS certificate that you want to use. Specify `AMPLIFY_MANAGED` to use the default certificate that Amplify provisions for you. Specify `CUSTOM` to use your own certificate that you have already added to Certificate Manager in your Amazon Web Services account. Make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1). For more information about using ACM, see [Importing certificates into Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the ACM User guide.

## `certificate_verification_dns_record`{% #certificate_verification_dns_record %}

**Type**: `STRING`**Provider name**: `certificateVerificationDNSRecord`**Description**: The DNS record for certificate verification.

## `domain_association_arn`{% #domain_association_arn %}

**Type**: `STRING`**Provider name**: `domainAssociationArn`**Description**: The Amazon Resource Name (ARN) for the domain association.

## `domain_name`{% #domain_name %}

**Type**: `STRING`**Provider name**: `domainName`**Description**: The name of the domain.

## `domain_status`{% #domain_status %}

**Type**: `STRING`**Provider name**: `domainStatus`**Description**: The current status of the domain association.

## `enable_auto_sub_domain`{% #enable_auto_sub_domain %}

**Type**: `BOOLEAN`**Provider name**: `enableAutoSubDomain`**Description**: Enables the automated creation of subdomains for branches.

## `status_reason`{% #status_reason %}

**Type**: `STRING`**Provider name**: `statusReason`**Description**: Additional information that describes why the domain association is in the current state.

## `sub_domains`{% #sub_domains %}

**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `subDomains`**Description**: The subdomains for the domain association.

- `dns_record`**Type**: `STRING`**Provider name**: `dnsRecord`**Description**: The DNS record for the subdomain.
- `sub_domain_setting`**Type**: `STRUCT`**Provider name**: `subDomainSetting`**Description**: Describes the settings for the subdomain.
  - `branch_name`**Type**: `STRING`**Provider name**: `branchName`**Description**: The branch name setting for the subdomain.
  - `prefix`**Type**: `STRING`**Provider name**: `prefix`**Description**: The prefix setting for the subdomain.
- `verified`**Type**: `BOOLEAN`**Provider name**: `verified`**Description**: The verified status of the subdomain

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`

## `update_status`{% #update_status %}

**Type**: `STRING`**Provider name**: `updateStatus`**Description**: The status of the domain update operation that is currently in progress. The following list describes the valid update states.

{% dl %}

{% dt %}
REQUESTING_CERTIFICATE
{% /dt %}

{% dd %}
The certificate is in the process of being updated.
{% /dd %}

{% dt %}
PENDING_VERIFICATION
{% /dt %}

{% dd %}
Indicates that an Amplify managed certificate is in the process of being verified. This occurs during the creation of a custom domain or when a custom domain is updated to use a managed certificate.
{% /dd %}

{% dt %}
IMPORTING_CUSTOM_CERTIFICATE
{% /dt %}

{% dd %}
Indicates that an Amplify custom certificate is in the process of being imported. This occurs during the creation of a custom domain or when a custom domain is updated to use a custom certificate.
{% /dd %}

{% dt %}
PENDING_DEPLOYMENT
{% /dt %}

{% dd %}
Indicates that the subdomain or certificate changes are being propagated.
{% /dd %}

{% dt %}
AWAITING_APP_CNAME
{% /dt %}

{% dd %}
Amplify is waiting for CNAME records corresponding to subdomains to be propagated. If your custom domain is on Route 53, Amplify handles this for you automatically. For more information about custom domains, see [Setting up custom domains](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html) in the Amplify Hosting User Guide.
{% /dd %}

{% dt %}
UPDATE_COMPLETE
{% /dt %}

{% dd %}
The certificate has been associated with a domain.
{% /dd %}

{% dt %}
UPDATE_FAILED
{% /dt %}

{% dd %}
The certificate has failed to be provisioned or associated, and there is no existing active certificate to roll back to.
{% /dd %}

{% /dl %}


