# Source: https://docs.datadoghq.com/security/default_rules/def-000-aoq.md

---
title: Uninstall avahi Server Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall avahi Server Package
---

# Uninstall avahi Server Package

## Description{% #description %}

If the system does not need to have an Avahi server which implements the DNS Service Discovery and Multicast DNS protocols, the avahi-autoipd and avahi packages can be uninstalled.

## Rationale{% #rationale %}

Automatic discovery of network services is not normally required for system functionality. It is recommended to remove this package to reduce the potential attack surface.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove avahi-daemon
# from the system, and may remove any packages
# that depend on avahi-daemon. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "avahi-daemon"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall avahi Server Package: Ensure avahi-daemon is removed'
  ansible.builtin.package:
    name: avahi-daemon
    state: absent
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_avahi_removed
```
