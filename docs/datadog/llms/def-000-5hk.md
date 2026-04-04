# Source: https://docs.datadoghq.com/security/default_rules/def-000-5hk.md

---
title: Private endpoint should be enabled for MySQL servers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Private endpoint should be enabled for
  MySQL servers
---

# Private endpoint should be enabled for MySQL servers

## Description{% #description %}

This rule checks if private endpoint connections are enabled for MySQL servers. Enabling private endpoint connections adds an additional layer of security by restricting access to the server to only specified networks or resources, reducing the exposure to potential threats from the public internet.

## Remediation{% #remediation %}

To enable private endpoint connections for MySQL servers, follow the instructions provided by the cloud provider. For Azure MySQL servers, you can enable private endpoint connections by following the steps outlined in [Enable Private Endpoint for Azure Database for MySQL](https://docs.microsoft.com/en-us/azure/mysql/howto-private-link-service-entry-enable).
