# Source: https://docs.datadoghq.com/security/default_rules/def-000-7bn.md

---
title: Ensure that Root's Path Does Not Include World or Group-Writable Directories
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure that Root's Path Does Not
  Include World or Group-Writable Directories
---

# Ensure that Root's Path Does Not Include World or Group-Writable Directories

## Description{% #description %}

For each element in root's path, run:

```
# ls -ld DIR

```

and ensure that write permissions are disabled for group and other.

## Rationale{% #rationale %}

Such entries increase the risk that root could execute code provided by unprivileged users, and potentially malicious code.
