# Source: https://docs.datadoghq.com/security/default_rules/ztr-rnu-ycv.md

---
title: >-
  The Docker server certificate file should have read-only or more restrictive
  permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Docker server certificate file
  should have read-only or more restrictive permissions
---

# The Docker server certificate file should have read-only or more restrictive permissions
Classification:complianceFramework:cis-dockerControl:3.12
## Description{% #description %}

You should verify that the Docker server certificate file, the file that is passed along with the `--tlscert` parameter, has permissions of 444 or more restrictive permissions.

## Rationale{% #rationale %}

The Docker server certificate file should be protected from any tampering. It is used to authenticate the Docker server based on the given server certificate. It should therefore have permissions of 444 to prevent its modification.

## Audit{% #audit %}

Verify that the Docker server certificate file has permissions of `444` or more restrictive, by running:

```
stat -c %a <path to Docker server certificate file>
```

## Remediation{% #remediation %}

Run the command below: `chmod 444 <path to Docker server certificate file>`

This sets the file permissions of the Docker server certificate file to 444.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the permissions for the Docker server certificate file might not be 444. The default file permissions are governed by the operating system or user specific umask values.

## References{% #references %}

1. [https://docs.docker.com/registry/insecure/](https://docs.docker.com/registry/insecure/)
1. [https://docs.docker.com/engine/security/https/](https://docs.docker.com/engine/security/https/)

## CIS controls{% #cis-controls %}

Version 6

14.4 Protect Information With Access Control Lists - All information stored on systems shall be protected with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.

Version 7

14.6 Protect Information through Access Control Lists - Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.
