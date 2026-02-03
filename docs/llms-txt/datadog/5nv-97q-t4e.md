# Source: https://docs.datadoghq.com/security/default_rules/5nv-97q-t4e.md

---
title: The Kubernetes API Server should enable audit logs on its server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes API Server should enable
  audit logs on its server
---

# The Kubernetes API Server should enable audit logs on its server
Classification:complianceFramework:cis-kubernetesControl:1.2.22 
## Description{% #description %}

Enable auditing on the Kubernetes API Server and set the desired audit log path.

## Rationale{% #rationale %}

Auditing the Kubernetes API Server provides a security-relevant chronological set of records documenting the sequence of activities that have affected system by individual users, administrators or other components of the system. Even though currently, Kubernetes provides only basic audit capabilities, it should be enabled. You can enable it by setting an appropriate audit log path.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--audit-log-path` argument is set as appropriate.

## Remediation{% #remediation %}

Edit the API server pod specification file /etc/kubernetes/manifests/kube-apiserver.yaml on the master node and set the âaudit-log-path parameter to a suitable path and file where you would like audit logs to be written, for example: âaudit-log-path=/var/log/apiserver/audit.log

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, auditing is not enabled.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/) 2. [https://kubernetes.io/docs/concepts/cluster-administration/audit/](https://kubernetes.io/docs/concepts/cluster-administration/audit/) 3. [https://github.com/kubernetes/features/issues/22](https://github.com/kubernetes/features/issues/22)

## CIS controls{% #cis-controls %}

Version 6 6.2 Ensure Audit Log Settings Support Appropriate Log Entry Formatting Validate audit log settings for each hardware device and the software installed on it, ensuring that logs include a date, timestamp, source addresses, destination addresses, and various other useful elements of each packet and/or transaction. Systems should record logs in a standardized format such as syslog entries or those outlined by the Common Event Expression initiative. If systems cannot generate logs in a standardized format, log normalization tools can be deployed to convert logs into such a format. Version 7 6.2 Activate audit logging Ensure that local logging has been enabled on all systems and networking devices. 6.3 Enable Detailed Logging Enable system logging to include detailed information such as an event source, date, user, timestamp, source addresses, destination addresses, and other useful elements.
