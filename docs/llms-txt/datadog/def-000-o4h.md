# Source: https://docs.datadoghq.com/security/default_rules/def-000-o4h.md

---
title: Remove tnftp Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Remove tnftp Package
---

# Remove tnftp Package

## Description{% #description %}

tnftp an enhanced FTP client, is the user interface to the Internet standard File Transfer Protocol. The program allows a user to transfer files to and from a remote network site. The `ftp` package can be removed with the following command:

```

$ apt-get remove ftp
```

## Rationale{% #rationale %}

Unless there is a need to run the system using Internet standard File Transfer Protocol (for example, to allow anonymous downloads), it is recommended that the package be removed to reduce the potential attack surface.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove tnftp
# from the system, and may remove any packages
# that depend on tnftp. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "tnftp"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Remove tnftp Package: Ensure tnftp is removed'
  ansible.builtin.package:
    name: tnftp
    state: absent
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - package_tnftp_removed
```
