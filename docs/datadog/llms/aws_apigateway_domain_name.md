# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_apigateway_domain_name.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_apigateway_domain_name{% #aws_apigateway_domain_name %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `certificate_arn`{% #certificate_arn %}

**Type**: `STRING`**Provider name**: `certificateArn`**Description**: The reference to an Amazon Web Services-managed certificate that will be used by edge-optimized endpoint for this domain name. Certificate Manager is the only supported source.

## `certificate_name`{% #certificate_name %}

**Type**: `STRING`**Provider name**: `certificateName`**Description**: The name of the certificate that will be used by edge-optimized endpoint for this domain name.

## `certificate_upload_date`{% #certificate_upload_date %}

**Type**: `TIMESTAMP`**Provider name**: `certificateUploadDate`**Description**: The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

## `distribution_domain_name`{% #distribution_domain_name %}

**Type**: `STRING`**Provider name**: `distributionDomainName`**Description**: The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custom domain name to this distribution name. For more information about CloudFront distributions, see the Amazon CloudFront documentation.

## `distribution_hosted_zone_id`{% #distribution_hosted_zone_id %}

**Type**: `STRING`**Provider name**: `distributionHostedZoneId`**Description**: The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is `Z2FDTNDATAQYW2` for all the regions. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway.

## `domain_name`{% #domain_name %}

**Type**: `STRING`**Provider name**: `domainName`**Description**: The custom domain name as an API host name, for example, `my-api.example.com`.

## `domain_name_arn`{% #domain_name_arn %}

**Type**: `STRING`

## `domain_name_status`{% #domain_name_status %}

**Type**: `STRING`**Provider name**: `domainNameStatus`**Description**: The status of the DomainName migration. The valid values are `AVAILABLE` and `UPDATING`. If the status is `UPDATING`, the domain cannot be modified further until the existing operation is complete. If it is `AVAILABLE`, the domain can be updated.

## `domain_name_status_message`{% #domain_name_status_message %}

**Type**: `STRING`**Provider name**: `domainNameStatusMessage`**Description**: An optional text message containing detailed information about status of the DomainName migration.

## `endpoint_configuration`{% #endpoint_configuration %}

**Type**: `STRUCT`**Provider name**: `endpointConfiguration`**Description**: The endpoint configuration of this DomainName showing the endpoint types of the domain name.

- `types`**Type**: `UNORDERED_LIST_STRING`**Provider name**: `types`**Description**: A list of endpoint types of an API (RestApi) or its custom domain name (DomainName). For an edge-optimized API and its custom domain name, the endpoint type is `"EDGE"`. For a regional API and its custom domain name, the endpoint type is `REGIONAL`. For a private API, the endpoint type is `PRIVATE`.
- `vpc_endpoint_ids`**Type**: `UNORDERED_LIST_STRING`**Provider name**: `vpcEndpointIds`**Description**: A list of VpcEndpointIds of an API (RestApi) against which to create Route53 ALIASes. It is only supported for `PRIVATE` endpoint type.

## `mutual_tls_authentication`{% #mutual_tls_authentication %}

**Type**: `STRUCT`**Provider name**: `mutualTlsAuthentication`**Description**: The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.

- `truststore_uri`**Type**: `STRING`**Provider name**: `truststoreUri`**Description**: An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example `s3://bucket-name/key-name`. The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.
- `truststore_version`**Type**: `STRING`**Provider name**: `truststoreVersion`**Description**: The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket.
- `truststore_warnings`**Type**: `UNORDERED_LIST_STRING`**Provider name**: `truststoreWarnings`**Description**: A list of warnings that API Gateway returns while processing your truststore. Invalid certificates produce warnings. Mutual TLS is still enabled, but some clients might not be able to access your API. To resolve warnings, upload a new truststore to S3, and then update you domain name to use the new version.

## `ownership_verification_certificate_arn`{% #ownership_verification_certificate_arn %}

**Type**: `STRING`**Provider name**: `ownershipVerificationCertificateArn`**Description**: The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the regionalCertificateArn.

## `regional_certificate_arn`{% #regional_certificate_arn %}

**Type**: `STRING`**Provider name**: `regionalCertificateArn`**Description**: The reference to an Amazon Web Services-managed certificate that will be used for validating the regional domain name. Certificate Manager is the only supported source.

## `regional_certificate_name`{% #regional_certificate_name %}

**Type**: `STRING`**Provider name**: `regionalCertificateName`**Description**: The name of the certificate that will be used for validating the regional domain name.

## `regional_domain_name`{% #regional_domain_name %}

**Type**: `STRING`**Provider name**: `regionalDomainName`**Description**: The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name. The regional domain name is returned by API Gateway when you create a regional endpoint.

## `regional_hosted_zone_id`{% #regional_hosted_zone_id %}

**Type**: `STRING`**Provider name**: `regionalHostedZoneId`**Description**: The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway.

## `security_policy`{% #security_policy %}

**Type**: `STRING`**Provider name**: `securityPolicy`**Description**: The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`
