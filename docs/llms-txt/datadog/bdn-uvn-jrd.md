# Source: https://docs.datadoghq.com/security/default_rules/bdn-uvn-jrd.md

---
title: Secure transfer required should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Secure transfer required should be
  enabled
---

# Secure transfer required should be enabled
 
## Description{% #description %}

The secure transfer option enhances the security of a storage account by only allowing requests to the storage account by a secure connection. For example, when calling REST APIs to access storage accounts, the connection must be HTTPS. Any requests using HTTP is rejected when secure transfer required is enabled. When using the Azure files service, connection without encryption fails, including scenarios using SMB 2.1, SMB 3.0 without encryption, and some flavors of the Linux SMB client. Because Azure storage doesn't support HTTPS for custom domain names, this option is not applied when using a custom domain name.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to **Storage Accounts**.
1. For each storage account, go to **Configuration**.
1. Set **Secure transfer required** to `Enabled`.
