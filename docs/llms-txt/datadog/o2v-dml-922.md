# Source: https://docs.datadoghq.com/security/default_rules/o2v-dml-922.md

---
title: Potential cryptomining detected through IP callback
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Potential cryptomining detected through
  IP callback
---

# Potential cryptomining detected through IP callback
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496)
## Goal{% #goal %}

Detect when a host is potentially infected with a cryptominer.

## Strategy{% #strategy %}

This rule compares the `@network.client.ip` standard attribute to a curated list of cryptomining pools.

## Triage and response{% #triage-and-response %}

1. Determine if the `{{host}}` host should be contacting a cryptomining pool.
1. If not, begin your company's IR process.

**Note** You can use the signal sidepanel to assist with the initial investigation by looking at CPU utilization and processes to identify unauthorized activity.

## Changelog{% #changelog %}

- 8 April 2022 - Initial beta release to select organizations.
- 13 April 2022 - Added additional filters for specific ports to reduce false positives.
- 26 April 2022 - Removed `restrictedToOrgs` settings, launching rule to all of production.
