# Source: https://docs.datadoghq.com/security/default_rules/def-000-l4y.md

---
title: User Initialization Files Must Be Group-Owned By The Primary Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > User Initialization Files Must Be
  Group-Owned By The Primary Group
---

# User Initialization Files Must Be Group-Owned By The Primary Group

## Description{% #description %}

Change the group owner of interactive users files to the group found in

```
/etc/passwd
```

for the user. To change the group owner of a local interactive user home directory, use the following command:

```
$ sudo chgrp USER_GROUP /home/USER/.INIT_FILE

```

This rule ensures every initialization file related to an interactive user is group-owned by an interactive user.

## Rationale{% #rationale %}

Local initialization files for interactive users are used to configure the user's shell environment upon logon. Malicious modification of these files could compromise accounts upon logon.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

awk -F: '{if ($4 >= 1000 && $4 != 65534) print $4":"$6}' /etc/passwd | while IFS=: read -r gid home; do find -P "$home" -maxdepth 1 -type f -name "\.[^.]*" -exec chgrp -f --no-dereference -- $gid "{}" \;; done
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Ensure interactive local users are the group-owners of their respective initialization
    files
  ansible.builtin.shell:
    cmd: 'awk -F: ''{if ($4 >= 1000 && $4 != 65534) print $4":"$6}'' /etc/passwd |
      while IFS=: read -r gid home; do find -P "$home" -maxdepth 1 -type f -name "\.[^.]*"
      -exec chgrp -f --no-dereference -- $gid "{}" \;; done'
  tags:
  - accounts_user_dot_group_ownership
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```

## Warning{% #warning %}

Due to OVAL limitation, this rule can report a false negative in a specific situation where two interactive users swap the group-ownership of their respective initialization files.
