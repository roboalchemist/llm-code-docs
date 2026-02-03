# Source: https://docs.datadoghq.com/security/default_rules/def-000-skj.md

---
title: Azure managed identity has dangerous key vault role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure managed identity has dangerous
  key vault role
---

# Azure managed identity has dangerous key vault role
 
## Description{% #description %}

This rule detects Azure AD managed identities with dangerous key vault roles. It specifically detects the assignment of Key Vault Administrator and Key Vault Contributor.

## Rationale{% #rationale %}

Assigning these key vault roles to Azure AD managed identities can unintentionally grant broad access to sensitive secrets, certificates, and encryption keys. Removing these assignments helps prevent privilege escalation, unauthorized access, and potential data breaches through misconfigured role assignments.

## Remediation{% #remediation %}

Review the managed identities and assess whether the assigned roles are necessary. If access is not justified, remove the roles or assign more restrictive, least-privilege alternatives that align with the principle of minimum access.
