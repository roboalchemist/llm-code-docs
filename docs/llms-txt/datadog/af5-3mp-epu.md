# Source: https://docs.datadoghq.com/security/default_rules/af5-3mp-epu.md

---
title: The /etc/docker directory permissions should be set to 755 or stricter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The /etc/docker directory permissions
  should be set to 755 or stricter
---

# The /etc/docker directory permissions should be set to 755 or stricter
Classification:complianceFramework:cis-dockerControl:3.6
## Description{% #description %}

You should verify that the `/etc/docker` directory permissions are correctly set to 755 or more restrictively.

## Rationale{% #rationale %}

The `/etc/docker` directory contains certificates and keys in addition to various sensitive files. It should therefore only be writeable by root to ensure that it can not be modified by a less privileged user.

## Audit{% #audit %}

You should execute the command below to verify that the directory has permissions of 755+:

```
stat -c %a /etc/docker
```

## Remediation{% #remediation %}

Run the following command: `chmod 755 /etc/docker`

This sets the permissions for the directory to 755.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the permissions for this directory are set to 755.

## References{% #references %}

1. [https://docs.docker.com/engine/security/https/](https://docs.docker.com/engine/security/https/)

## CIS controls{% #cis-controls %}

Version 6

14.4 Protect Information With Access Control Lists - All information stored on systems shall be protected with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.

Version 7

14.6 Protect Information through Access Control Lists - Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.
