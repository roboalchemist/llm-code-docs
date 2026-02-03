# Source: https://docs.datadoghq.com/security/default_rules/def-000-skw.md

---
title: TLS Version should be set to 'TLSV1.2' for MySQL flexible Database Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > TLS Version should be set to 'TLSV1.2'
  for MySQL flexible Database Server
---

# TLS Version should be set to 'TLSV1.2' for MySQL flexible Database Server
 
## Description{% #description %}

Transport Layer Security (TLS) connectivity enhances security by encrypting the communication between database servers and client applications. Enforcing TLS connections helps protect data from "man-in-the-middle" attacks by securing the data stream between the server and the application.

## Remediation{% #remediation %}

To configure TLS settings for your Azure Database for MySQL flexible servers, consult the [Azure Database for MySQL documentation](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/overview#enterprise-grade-security-compliance-and-privacy)
