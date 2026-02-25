# Source: https://docs.datadoghq.com/security/default_rules/4cm-yt8-dji.md

---
title: The registry certificate files should have read-only or stricter permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The registry certificate files should
  have read-only or stricter permissions
---

# The registry certificate files should have read-only or stricter permissions
Classification:complianceFramework:cis-dockerControl:3.8
## Description{% #description %}

You should verify that all the registry certificate files, usually found under `/etc/docker/certs.d/<registry-name> directory`, have permissions of 444 or are set more restrictively.

## Rationale{% #rationale %}

The `/etc/docker/certs.d/<registry-name>` directory contains Docker registry certificates. These certificate files must have permissions of 444or more restrictive permissions in order to ensure that unprivileged users do not have full access to them..

## Audit{% #audit %}

You should execute the command below to verify that registry certificate files have permissions of 444+.

```
stat -c %a /etc/docker/certs.d/<registry-name>/*
```

## Remediation{% #remediation %}

Run the following command: `chmod 444 /etc/docker/certs.d/<registry-name>/*`

This sets the permissions for the registry certificate files to 444.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the permissions for registry certificate files might not be 444. The default file permissions are governed by the system or user specific umask values which are defined within the operating system itself.

## References{% #references %}

1. [https://docs.docker.com/registry/insecure/](https://docs.docker.com/registry/insecure/)

## CIS controls{% #cis-controls %}

Version 6

14.4 Protect Information With Access Control Lists - All information stored on systems shall be protected with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.

Version 7

14.6 Protect Information through Access Control Lists - Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.
