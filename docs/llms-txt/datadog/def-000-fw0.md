# Source: https://docs.datadoghq.com/security/default_rules/def-000-fw0.md

---
title: Supply-Chain Firewall unverified package manager command
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Supply-Chain Firewall unverified
  package manager command
---

# Supply-Chain Firewall unverified package manager command
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1195-supply-chain-compromise](https://attack.mitre.org/techniques/T1195) 
## Goal{% #goal %}

This rule detects instances of [Supply-Chain Firewall](https://github.com/DataDog/supply-chain-firewall) running a package manager command without verification, which occurs when the underlying package manager is on an unsupported version. Supply-Chain Firewall was therefore unable to resolve the command's installation targets, if any.

## Strategy{% #strategy %}

This rule monitors Supply-Chain Firewall's logs for `@verified:false`. This attribute is set only in cases when Supply-Chain Firewall was unable to verify a package manager command it executed.

## Triage and response{% #triage-and-response %}

- Examine the logs to determine the package manager command that was executed and whether the command may have installed packages.
- Determine whether any packages that were installed have associated security advisories using:
  - Datadog Security Research's public malicious packages [dataset](https://github.com/Datadog/malicious-software-packages-dataset)
  - OSV.dev's public [API](https://google.github.io/osv.dev/quickstart/) or [website](https://osv.dev)
- Based on the results of the previous step, take any necessary action to remediate the system where the command was executed.
- If possible, update the affected package manager to a [supported version](https://github.com/DataDog/supply-chain-firewall#compatibility-and-limitations) to take advantage of Supply-Chain Firewall verification.
