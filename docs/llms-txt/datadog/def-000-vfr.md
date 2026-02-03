# Source: https://docs.datadoghq.com/security/default_rules/def-000-vfr.md

---
title: Ensure that Root's Path Does Not Include Relative Paths or Null Directories
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure that Root's Path Does Not
  Include Relative Paths or Null Directories
---

# Ensure that Root's Path Does Not Include Relative Paths or Null Directories
 
## Description{% #description %}

Ensure that none of the directories in root's path is equal to a single `.` character, or that it contains any instances that lead to relative path traversal, such as `..` or beginning a path without the slash (`/`) character. Also ensure that there are no "empty" elements in the path, such as in these examples:

```
PATH=:/bin
PATH=/bin:
PATH=/bin::/sbin
```

These empty elements have the same effect as a single `.` character.

## Rationale{% #rationale %}

Including these entries increases the risk that root could execute code from an untrusted location.
