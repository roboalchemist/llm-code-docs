# Source: https://docs.datadoghq.com/security/default_rules/def-000-ivn.md

---
title: Ensure All Accounts on the System Have Unique Names
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure All Accounts on the System Have
  Unique Names
---

# Ensure All Accounts on the System Have Unique Names
 
## Description{% #description %}

Ensure accounts on the system have unique names. To ensure all accounts have unique names, run the following command:

```
$ sudo getent passwd | awk -F: '{ print $1}' | uniq -d
```

If a username is returned, change or delete the username.

## Rationale{% #rationale %}

Unique usernames allow for accountability on the system.
