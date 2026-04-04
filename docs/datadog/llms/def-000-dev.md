# Source: https://docs.datadoghq.com/security/default_rules/def-000-dev.md

---
title: User Initialization Files Must Be Owned By the Primary User
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > User Initialization Files Must Be Owned
  By the Primary User
---

# User Initialization Files Must Be Owned By the Primary User

## Description{% #description %}

Set the owner of the user initialization files for interactive users to the primary owner with the following command:

```
$ sudo chown USER /home/USER/.*
```

This rule ensures every initialization file related to an interactive user is owned by an interactive user.

## Rationale{% #rationale %}

Local initialization files are used to configure the user's shell environment upon logon. Malicious modification of these files could compromise accounts upon logon.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

awk -F: '{if ($3 >= 1000 && $3 != 65534) print $3":"$6}' /etc/passwd | while IFS=: read -r uid home; do find -P "$home" -maxdepth 1 -type f -name "\.[^.]*" -exec chown -f --no-dereference -- $uid "{}" \;; done
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Ensure interactive local users are the owners of their respective initialization
    files
  ansible.builtin.shell:
    cmd: 'awk -F: ''{if ($3 >= 1000 && $3 != 65534) print $3":"$6}'' /etc/passwd |
      while IFS=: read -r uid home; do find -P "$home" -maxdepth 1 -type f -name "\.[^.]*"
      -exec chown -f --no-dereference -- $uid "{}" \;; done'
  tags:
  - accounts_user_dot_user_ownership
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```

## Warning{% #warning %}

Due to OVAL limitation, this rule can report a false negative in a specific situation where two interactive users swap the ownership of their respective initialization files.
