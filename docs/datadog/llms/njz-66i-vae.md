# Source: https://docs.datadoghq.com/security/default_rules/njz-66i-vae.md

---
title: The certificate authorities file should have permissions of 644 or stricter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The certificate authorities file should
  have permissions of 644 or stricter
---

# The certificate authorities file should have permissions of 644 or stricter
Classification:complianceFramework:cis-kubernetesControl:4.1.7
## Description{% #description %}

Ensure that the certificate authorities file has permissions of 644 or more restrictive.

## Rationale{% #rationale %}

The certificate authorities file controls the authorities used to validate API requests. You should restrict its file permissions to maintain the integrity of the file. The file should be writable by only the administrators on the system.

## Audit{% #audit %}

Run the following command: `ps -ef | grep kubelet`. Find the file specified by the `--client-ca-file` argument. Run the following command: `stat -c %a <filename>`. Verify that the permissions are 644 or more restrictive.

## Remediation{% #remediation %}

Run the following command to modify the file permissions of the `--client-ca-file`:

```
chmod 644 <filename>
```

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default no `--client-ca-file` is specified.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/authentication/#x509-client-certs](https://kubernetes.io/docs/admin/authentication/#x509-client-certs)

## CIS controls{% #cis-controls %}

Version 6 5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.

Version 7.14.4 Protect Information With Access Control Lists - All information stored on systems shall be protected with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.

Version 7 14.6 Protect Information through Access Control Lists - Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.
