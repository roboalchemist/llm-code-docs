# Source: https://docs.datadoghq.com/security/default_rules/def-000-vz7.md

---
title: Uninstall talk Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall talk Package
---

# Uninstall talk Package

## Description{% #description %}

The `talk` package contains the client program for the Internet talk protocol, which allows the user to chat with other users on different systems. Talk is a communication program which copies lines from one terminal to the terminal of another user. The `talk` package can be removed with the following command:

```

$ apt-get remove talk
```

## Rationale{% #rationale %}

The talk software presents a security risk as it uses unencrypted protocols for communications. Removing the `talk` package decreases the risk of the accidental (or intentional) activation of talk client program.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove talk
# from the system, and may remove any packages
# that depend on talk. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "talk"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall talk Package: Ensure talk is removed'
  ansible.builtin.package:
    name: talk
    state: absent
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_talk_removed
```
