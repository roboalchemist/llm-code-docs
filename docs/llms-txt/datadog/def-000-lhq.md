# Source: https://docs.datadoghq.com/security/default_rules/def-000-lhq.md

---
title: Cloudflare L7 DDOS detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Cloudflare L7 DDOS detected
---

# Cloudflare L7 DDOS detected
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1498-network-denial-of-service](https://attack.mitre.org/techniques/T1498)
## Goal{% #goal %}

Detect when a Layer 7 Distributed Denial of Service (DDoS) occurs.

## Strategy{% #strategy %}

The Cloudflare HTTP DDoS Attack Protection managed ruleset is a set of pre-configured rules used to match known DDoS attack vectors at layer 7 (application layer) on the Cloudflare global network. The rules match known attack patterns and tools, suspicious patterns, protocol violations, requests causing large amounts of origin errors, excessive traffic hitting the origin/cache, and additional attack vectors at the application layer.

This rule inspects the `@Source` attribute for the value `l7ddos` to determine that the L7 DDoS product has been triggered.

## Triage and response{% #triage-and-response %}

1. Monitor application for indications of reduced performance or outages.
1. Analyze identified traffic to ensure it is not a [false positive](https://developers.cloudflare.com/ddos-protection/managed-rulesets/adjust-rules/false-positive/) that should be tuned.
1. In addition, CloudFlare provides a [response guide](https://developers.cloudflare.com/ddos-protection/best-practices/respond-to-ddos-attacks/) for all customers to reduce the impact of a DDoS attack on your application.
