# Source: https://docs.datadoghq.com/security/default_rules/def-000-sc0.md

---
title: Supply-Chain Firewall blocked package manager command
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Supply-Chain Firewall blocked package
  manager command
---

# Supply-Chain Firewall blocked package manager command
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1195-supply-chain-compromise](https://attack.mitre.org/techniques/T1195)
## Goal{% #goal %}

This rule detects instances of [Supply-Chain Firewall](https://github.com/DataDog/supply-chain-firewall) automatically blocking package manager commands from running.

## Strategy{% #strategy %}

This rule monitors Supply-Chain Firewall's logs for automatically blocked package manager commands (`@evt.outcome:BLOCK -@warned:true`). These events occur when Supply-Chain Firewall determines that running a command would result in known malware being installed.

Note that blocked commands with `@warned:true` correspond to user-initiated cancellations of package manager commands after being presented with warnings by Supply-Chain Firewall. These warnings are generally related to vulnerabilities, not malware, and hence have been excluded.

## Triage and response{% #triage-and-response %}

Any logs detected by this rule are for package manager commands that were blocked from running, so no incident response measures are required.

- Examine the logs to determine which package(s) caused Supply-Chain Firewall to block.
- Investigate the context in which the blocked command was executed.
- Determine whether the blocked command resulted from a false positive in Supply-Chain Firewall's verifiers.
  - This can occur, for example, when a benign package hosted internally in your enterprise has the same name as a malicious package hosted on the public registry.
- In the event of a true positive, audit other endpoints in your environment for completed installations of the packages of concern.
