# Source: https://docs.datadoghq.com/security/default_rules/def-000-sma.md

---
title: Verify permissions on System Login Banner for Remote Connections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify permissions on System Login
  Banner for Remote Connections
---

# Verify permissions on System Login Banner for Remote Connections
 
## Description{% #description %}

To properly set the permissions of `/etc/issue.net`, run the command:

```
$ sudo chmod 0644 /etc/issue.net
```

## Rationale{% #rationale %}

Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.

Proper permissions will ensure that only root user can modify the banner.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

chmod u-xs,g-xws,o-xwt /etc/issue.net
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```zed
- name: Test for existence /etc/issue.net
  stat:
    path: /etc/issue.net
  register: file_exists
  tags:
  - PCI-DSSv4-1.2
  - PCI-DSSv4-1.2.8
  - configure_strategy
  - file_permissions_etc_issue_net
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xws,o-xwt on /etc/issue.net
  file:
    path: /etc/issue.net
    mode: u-xs,g-xws,o-xwt
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - PCI-DSSv4-1.2
  - PCI-DSSv4-1.2.8
  - configure_strategy
  - file_permissions_etc_issue_net
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
