# Source: https://docs.datadoghq.com/security/default_rules/def-000-cfq.md

---
title: Redis server wrote suspicious module file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Redis server wrote suspicious module
  file
---

# Redis server wrote suspicious module file
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1129-shared-modules](https://attack.mitre.org/techniques/T1129)
## What happened{% #what-happened %}

The file `{{ @file.path }}` was written by `{{ @process.comm }}` and could be a malicious module used to achieve command execution.

## Goal{% #goal %}

Detect Redis writing a malicious module.

## Strategy{% #strategy %}

One of the primary methods for compromising vulnerable Redis deployments is to use the `SLAVEOF` command (now renamed to `REPLICAOF`) to modify the replication settings of a Redis instance to join it to an attacker controlled Redis cluster. From there, the attacker will push a malicious Redis module to the compromised Redis node using the Redis cluster replication capabilities. This is used to achieve command execution on the compromised Redis instance.

## Triage and response{% #triage-and-response %}

1. Determine if the Redis module is authorized on the host.
1. If the activity is not authorized, verify if the instance has been joined to an attacker controlled cluster by running the `CLUSTER INFO` command.
1. If the instance has been compromised, initiate incident response procedures.

*Requires Agent version 7.27 or greater*
