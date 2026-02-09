# Source: https://docs.datadoghq.com/security/default_rules/def-000-0kg.md

---
title: PAM authentication library hooked using eBPF
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > PAM authentication library hooked using
  eBPF
---

# PAM authentication library hooked using eBPF
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1056-input-capture](https://attack.mitre.org/techniques/T1056) 
## Goal{% #goal %}

Detect processes hooking PAM authentication with the purpose of stealing credentials.

## Strategy{% #strategy %}

The detection monitors system processes for the presence of eBPF programs that intercept and manipulate Linux PAM (Pluggable Authentication Modules) authentication calls. It specifically focuses on identifying any unauthorized eBPF programs that may be used to steal user credentials during the authentication process.

## Triage and response{% #triage-and-response %}

1. Review the BPF programs that are loaded on the system.
1. Terminate any BPF programs that are unexpected to prevent further credential theft.
1. Use related signals and other logs to find and repair the root cause.
1. Determine if any user credentials were potentially compromised during the time frame when the unauthorized eBPF program(s) were active. Rotate any affected credentials.

*Requires Agent version 7.34 or later.*
