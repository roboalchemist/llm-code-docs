# Source: https://docs.datadoghq.com/security/default_rules/gqh-gvy-7jy.md

---
title: Etcd data directory should have permissions of 700 or more restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Etcd data directory should have
  permissions of 700 or more restrictive
---

# Etcd data directory should have permissions of 700 or more restrictive
Classification:complianceFramework:cis-kubernetesControl:1.1.11 
## Description{% #description %}

Ensure that the etcd data directory has permissions of 700 or more restrictive.

## Rationale{% #rationale %}

etcd is a highly-available key-value store used by Kubernetes deployments for persistent storage of all of its REST API objects. This data directory should be protected from any unauthorized reads or writes. It should not be readable or writable by any group members or the world.

## Audit{% #audit %}

On the etcd server node, get the etcd data directory passed as an argument `--data-dir`, from the command:

```bash
ps -ef | grep etcd
```

Based on the etcd data directory found above, run the command:

```bash
stat -c %a /var/lib/etcd
```

Verify the permissions are `700` or more restrictive.

## Remediation{% #remediation %}

On the etcd server node, get the etcd data directory, passed as an argument `--data-dir`, from the below command: `ps -ef | grep etcd`

Run the command (based on the etcd data directory found above): `chmod 700 /var/lib/etcd`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, etcd data directory has permissions of 755.

## References{% #references %}

1. [https://coreos.com/etcd/docs/latest/op-guide/configuration.html#data-dir](https://coreos.com/etcd/docs/latest/op-guide/configuration.html#data-dir)
1. [https://kubernetes.io/docs/admin/etcd/](https://kubernetes.io/docs/admin/etcd/)

## CIS controls{% #cis-controls %}

Version 6

14 Controlled Access Based on the Need to Know

Version 7

5.2 Maintain Secure Images - Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
