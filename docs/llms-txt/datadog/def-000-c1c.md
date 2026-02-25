# Source: https://docs.datadoghq.com/security/default_rules/def-000-c1c.md

---
title: Verify Permissions on gshadow File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Permissions on gshadow File
---

# Verify Permissions on gshadow File

## Description{% #description %}

To properly set the permissions of `/etc/gshadow`, run the command:

```
$ sudo chmod 0640 /etc/gshadow
```

## Rationale{% #rationale %}

The `/etc/gshadow` file contains group password hashes. Protection of this file is critical for system security.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

chmod u-xs,g-xws,o-xwrt /etc/gshadow
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```zed
- name: Test for existence /etc/gshadow
  stat:
    path: /etc/gshadow
  register: file_exists
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - configure_strategy
  - file_permissions_etc_gshadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xws,o-xwrt on /etc/gshadow
  file:
    path: /etc/gshadow
    mode: u-xs,g-xws,o-xwrt
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - configure_strategy
  - file_permissions_etc_gshadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
