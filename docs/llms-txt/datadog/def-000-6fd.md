# Source: https://docs.datadoghq.com/security/default_rules/def-000-6fd.md

---
title: Google Compute Engine network created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Google Compute Engine network created
---

# Google Compute Engine network created
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1578-modify-cloud-compute-infrastructure](https://attack.mitre.org/techniques/T1578) 
## Goal{% #goal %}

Detect when a Google Compute Engine network is created.

## Strategy{% #strategy %}

This rule lets you monitor Google Compute Engine activity audit logs to determine when the following method is invoked to create a new Compute Engine network:

- `beta.compute.networks.insert`
- `v*.compute.networks.insert`

An attacker could create a compute network with the intention of enabling cryptomining and bypassing networking limitations.

## Triage and response{% #triage-and-response %}

Review the Compute Engine network.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
- 30 September 2024 - Updated query to replace attribute `@threat_intel.results.subcategory:anonymizer`.
