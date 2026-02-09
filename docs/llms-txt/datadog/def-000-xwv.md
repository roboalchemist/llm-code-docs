# Source: https://docs.datadoghq.com/security/default_rules/def-000-xwv.md

---
title: Ensure shadow Group is Empty
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure shadow Group is Empty
---

# Ensure shadow Group is Empty
 
## Description{% #description %}

The shadow group allows system programs which require access the ability to read the /etc/shadow file. No users should be assigned to the shadow group.

## Rationale{% #rationale %}

Any users assigned to the shadow group would be granted read access to the /etc/shadow file. If attackers can gain read access to the /etc/shadow file, they can easily run a password cracking program against the hashed passwords to break them. Other security information that is stored in the /etc/shadow file (such as expiration) could also be useful to subvert additional user accounts.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

sed -ri 's/(^shadow:[^:]*:[^:]*:)([^:]+$)/\1/' /etc/group
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Ensure interactive local users are the owners of their respective initialization
    files
  ansible.builtin.lineinfile:
    dest: /etc/group
    backrefs: true
    regexp: (^shadow:[^:]*:[^:]*:)([^:]+$)
    line: \1
  tags:
  - PCI-DSS-Req-8.2.1
  - PCI-DSSv4-8.3
  - PCI-DSSv4-8.3.2
  - ensure_shadow_group_empty
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```

## Warning{% #warning %}

This rule remediation will ensure the group membership is empty in /etc/group. To avoid any disruption the remediation won't change the primary group of users in /etc/passwd if any user has the shadow GID as primary group.
