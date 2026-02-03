# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_apigateway_client_certificate.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_apigateway_client_certificate{% #aws_apigateway_client_certificate %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `client_certificate_arn`{% #client_certificate_arn %}

**Type**: `STRING`

## `client_certificate_id`{% #client_certificate_id %}

**Type**: `STRING`**Provider name**: `clientCertificateId`**Description**: The identifier of the client certificate.

## `created_date`{% #created_date %}

**Type**: `TIMESTAMP`**Provider name**: `createdDate`**Description**: The timestamp when the client certificate was created.

## `description`{% #description %}

**Type**: `STRING`**Provider name**: `description`**Description**: The description of the client certificate.

## `expiration_date`{% #expiration_date %}

**Type**: `TIMESTAMP`**Provider name**: `expirationDate`**Description**: The timestamp when the client certificate will expire.

## `pem_encoded_certificate`{% #pem_encoded_certificate %}

**Type**: `STRING`**Provider name**: `pemEncodedCertificate`**Description**: The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint .

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`
