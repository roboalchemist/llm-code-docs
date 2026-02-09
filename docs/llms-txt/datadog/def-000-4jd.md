# Source: https://docs.datadoghq.com/security/default_rules/def-000-4jd.md

---
title: Cloudflare CASB Finding
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Cloudflare CASB Finding
---

# Cloudflare CASB Finding
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when a Cloudflare CASB finding is observed.

## Strategy{% #strategy %}

Cloudflare's Cloud Access Security Broker (CASB) scans SaaS integrations for various misconfigurations, and security issues that can occur after a user has successfully logged in. These scans result in findings that detail the security issues detected within the SaaS application.

## Triage & response{% #triage--response %}

Investigate the asset `{{@AssetDisplayName}}` involved in the finding: `{{@FindingTypeDisplayName}}`from the `{{@IntegrationDisplayName}}` integration.
