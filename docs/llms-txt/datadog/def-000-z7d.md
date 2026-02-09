# Source: https://docs.datadoghq.com/security/default_rules/def-000-z7d.md

---
title: Ensure that All Root's Path Directories Are Owned by Root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure that All Root's Path Directories
  Are Owned by Root
---

# Ensure that All Root's Path Directories Are Owned by Root
 
## Description{% #description %}

For each element in root's path, run:

```
# ls -ld DIR
         
```

and ensure that the directory is owned by the root user.

## Rationale{% #rationale %}

Directories in root's path that are not owned by root could allow unprivileged users to manipulate the execution environment of root, potentially leading to privilege escalation or execution of malicious code.
