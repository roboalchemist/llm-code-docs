# Source: https://docs.datadoghq.com/security/default_rules/def-000-cc3.md

---
title: Verify No netrc Files Exist
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify No netrc Files Exist
---

# Verify No netrc Files Exist

## Description{% #description %}

The `.netrc` files contain login information used to auto-login into FTP servers and reside in the user's home directory. These files may contain unencrypted passwords to remote FTP servers making them susceptible to access by unauthorized users and should not be used. Any `.netrc` files should be removed.

## Rationale{% #rationale %}

Unencrypted passwords for remote FTP servers may be stored in `.netrc` files.
