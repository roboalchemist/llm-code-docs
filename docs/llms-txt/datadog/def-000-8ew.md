# Source: https://docs.datadoghq.com/security/default_rules/def-000-8ew.md

---
title: App Service should use the latest version of TLS encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > App Service should use the latest
  version of TLS encryption
---

# App Service should use the latest version of TLS encryption
 
## Description{% #description %}

The Transport Layer Security (TLS) protocol ensures secure data transmission over the internet through standard encryption technology. To maximize security, it's crucial to use the latest version of TLS. By default, App Service uses TLS 1.3, which is now the benchmark in industry standards like PCI DSS. App Service supports various TLS versions, including 1.0, 1.1, 1.2, and 1.3. It is highly recommended to utilize TLS 1.3 to ensure the most secure connections.

## Remediation{% #remediation %}

For detailed guidance on configuring TLS for your web apps, refer to the [Azure App Service TLS Overview](https://learn.microsoft.com/en-us/azure/app-service/overview-tls).
