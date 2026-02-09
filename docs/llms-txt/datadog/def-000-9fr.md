# Source: https://docs.datadoghq.com/security/default_rules/def-000-9fr.md

---
title: >-
  AWS Cloudtrail possible secret enumeration in multiple regions and secret
  retrieval
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Cloudtrail possible secret
  enumeration in multiple regions and secret retrieval
---

# AWS Cloudtrail possible secret enumeration in multiple regions and secret retrieval
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555) 
## Goal{% #goal %}

Detects when a user enumerates AWS Secrets Manager secrets across multiple regions and then retrieves secret values.

## Strategy{% #strategy %}

This rule monitors AWS CloudTrail events for `ListSecrets` API calls spanning multiple regions and subsequent `GetSecretValue` API calls by the same user identity. This behavior pattern is concerning because legitimate users typically work within specific regions and don't require broad secret enumeration across multiple geographic locations before accessing secrets. Attackers often perform discovery to map available secrets across an organization's AWS infrastructure before extracting valuable credentials.

## Triage & Response{% #triage--response %}

- Determine if `{{@userIdentity.arn}}` should be performing secret enumeration activities across multiple AWS regions.
- Review the specific regions where `ListSecrets` operations occurred to determine if cross-region access aligns with the user's normal responsibilities.
- Identify which secrets were retrieved through `GetSecretValue` and assess their sensitivity and business criticality.
- Check for any other suspicious activities from the same user identity, such as unusual resource access or privilege escalation attempts.
- Verify if the user identity has been recently compromised by reviewing authentication logs and access patterns leading up to the secret enumeration.
- Determine if the retrieved secrets have been used for unauthorized access to other AWS services or external systems.
