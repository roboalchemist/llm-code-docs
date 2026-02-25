# Source: https://docs.datadoghq.com/security/default_rules/def-000-dgw.md

---
title: Remove telnet Clients
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Remove telnet Clients
---

# Remove telnet Clients

## Description{% #description %}

The telnet client allows users to start connections to other systems via the telnet protocol.

## Rationale{% #rationale %}

The `telnet` protocol is insecure and unencrypted. The use of an unencrypted transmission medium could allow an unauthorized user to steal credentials. The `ssh` package provides an encrypted session and stronger security and is included in Ubuntu 20.04.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove telnet
# from the system, and may remove any packages
# that depend on telnet. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "telnet"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Remove telnet Clients: Ensure telnet is removed'
  ansible.builtin.package:
    name: telnet
    state: absent
  tags:
  - NIST-800-171-3.1.13
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - package_telnet_removed
```
