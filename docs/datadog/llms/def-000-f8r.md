# Source: https://docs.datadoghq.com/security/default_rules/def-000-f8r.md

---
title: Uninstall nfs-kernel-server Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall nfs-kernel-server Package
---

# Uninstall nfs-kernel-server Package

## Description{% #description %}

The `nfs-kernel-server` package can be removed with the following command:

```

$ apt-get remove nfs-kernel-server
```

## Rationale{% #rationale %}

If the system does not export NFS shares or act as an NFS client, it is recommended that these services be removed to reduce the remote attack surface.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove nfs-kernel-server
# from the system, and may remove any packages
# that depend on nfs-kernel-server. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "nfs-kernel-server"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall nfs-kernel-server Package: Ensure nfs-kernel-server is removed'
  ansible.builtin.package:
    name: nfs-kernel-server
    state: absent
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - package_nfs-kernel-server_removed
```
