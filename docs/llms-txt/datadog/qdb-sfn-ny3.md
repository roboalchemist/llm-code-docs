# Source: https://docs.datadoghq.com/security/default_rules/qdb-sfn-ny3.md

---
title: The certificate authorities file should be owned by root:root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The certificate authorities file should
  be owned by root:root
---

# The certificate authorities file should be owned by root:root
Classification:complianceFramework:cis-kubernetesControl:4.1.8 
## Description{% #description %}

Ensure that the certificate authorities file ownership is set to `root:root`.

## Rationale{% #rationale %}

The certificate authorities file controls the authorities used to validate API requests. You should set its file ownership to maintain the integrity of the file. The file should be owned by `root:root`.

## Audit{% #audit %}

Run the following command: `ps -ef | grep kubelet`. Find the file specified by the `--client-ca-file` argument. Run the following command: `stat -c %U:%G <filename>`. Verify that the ownership is set to `root:root`.

## Remediation{% #remediation %}

Run the following command to modify the ownership of the `--client-ca-file`:

```
chown root:root <filename>
```

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default no `--client-ca-file` is specified.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/authentication/#x509-client-certs](https://kubernetes.io/docs/admin/authentication/#x509-client-certs)

## CIS controls{% #cis-controls %}

Version 6.5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.

Version 7.5.2 Maintain Secure Images - Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
