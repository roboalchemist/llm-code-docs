# Source: https://docs.datadoghq.com/security/default_rules/def-000-ssc.md

---
title: Uninstall rsync Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall rsync Package
---

# Uninstall rsync Package

## Description{% #description %}

The rsyncd service can be used to synchronize files between systems over network links. The `rsync` package can be removed with the following command:

```

$ apt-get remove rsync
```

## Rationale{% #rationale %}

The rsyncd service presents a security risk as it uses unencrypted protocols for communication.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove rsync
# from the system, and may remove any packages
# that depend on rsync. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "rsync"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall rsync Package: Ensure rsync is removed'
  ansible.builtin.package:
    name: rsync
    state: absent
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_rsync_removed
```
