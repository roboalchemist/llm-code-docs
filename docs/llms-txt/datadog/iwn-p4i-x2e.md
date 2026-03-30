# Source: https://docs.datadoghq.com/security/default_rules/iwn-p4i-x2e.md

---
title: The etcd data directory should be owned by etcd:etcd
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The etcd data directory should be owned
  by etcd:etcd
---

# The etcd data directory should be owned by etcd:etcd
Classification:complianceFramework:cis-kubernetesControl:1.1.12
## Description{% #description %}

Ensure that the etcd data directory ownership is set to `etcd:etcd`.

## Rationale{% #rationale %}

`etcd` is a highly-available key-value store used by Kubernetes deployments for persistent storage of all of its REST API objects. This data directory should be protected from any unauthorized reads or writes. It should be owned by `etcd:etcd`.

## Audit{% #audit %}

On the etcd server node, get the etcd data directory passed as an argument `--data-dir` from the command:

```bash
ps -ef | grep etcd
```

Based on the etcd data directory found above, run the command:

```bash
stat -c %U:%G /var/lib/etcd
```

Verify the ownership is set to `etcd:etcd`.

## Remediation{% #remediation %}

On the etcd server node, get the etcd data directory, passed as an argument `--data-dir`, from the below command: `ps -ef | grep etcd`

Run the command (based on the etcd data directory found above): `chown etcd:etcd /var/lib/etcd`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, etcd data directory ownership is set to `etcd:etcd`.

## References{% #references %}

1. [https://coreos.com/etcd/docs/latest/op-guide/configuration.html#data-dir](https://coreos.com/etcd/docs/latest/op-guide/configuration.html#data-dir)
1. [https://kubernetes.io/docs/admin/etcd/](https://kubernetes.io/docs/admin/etcd/)

## CIS controls{% #cis-controls %}

Version 6

14 Controlled Access Based on the Need to Know

Version 7

5.2 Maintain Secure Images - Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
