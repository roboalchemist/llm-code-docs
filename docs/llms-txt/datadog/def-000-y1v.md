# Source: https://docs.datadoghq.com/security/default_rules/def-000-y1v.md

---
title: Verify Only Group Root Has GID 0
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Only Group Root Has GID 0
---

# Verify Only Group Root Has GID 0
 
## Description{% #description %}

If any group other than root has a GID of 0, this misconfiguration should be investigated and the groups other than root should be removed or have their GID changed.

## Rationale{% #rationale %}

Ensuring that only the `root` group has a GID of 0 helps prevent root group owned files from becoming accidentally accessible to non-privileged users.

## Warning{% #warning %}

This rule doesn't come with a remediation. The removal of groups from a system or reassigning the GID is considered too disruptive.
