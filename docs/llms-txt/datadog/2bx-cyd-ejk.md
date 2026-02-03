# Source: https://docs.datadoghq.com/security/default_rules/2bx-cyd-ejk.md

---
title: The Docker server certificate key file needs to have permissions of 400
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Docker server certificate key file
  needs to have permissions of 400
---

# The Docker server certificate key file needs to have permissions of 400
Classification:complianceFramework:cis-dockerControl:3.14 
## Description{% #description %}

You should verify that the Docker server certificate key file, the file that is passed along with the `--tlskey` parameter, has permissions of 400.

## Rationale{% #rationale %}

The Docker server certificate key file should be protected from any tampering or unneeded reads. It holds the private key for the Docker server certificate. It must therefore have permissions of 400 to ensure that the certificate key file is not modified.

## Audit{% #audit %}

Verify that the Docker server certificate key file has permissions of `400` by running:

```
stat -c %a <path to Docker server certificate key file>
```

## Remediation{% #remediation %}

You should execute the following command: `chmod 400 <path to Docker server certificate key file>`

This sets the Docker server certificate key file permissions to 400.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the permissions for the Docker server certificate key file might not be 400. The default file permissions are governed by the operating system or user specific umask values.

## References{% #references %}

1. [https://docs.docker.com/registry/insecure/](https://docs.docker.com/registry/insecure/)
1. [https://docs.docker.com/engine/security/https/](https://docs.docker.com/engine/security/https/)

## CIS controls{% #cis-controls %}

Version 6

14.4 Protect Information With Access Control Lists All information stored on systems shall be protected with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.

Version 7

14.6 Protect Information through Access Control Lists Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.
