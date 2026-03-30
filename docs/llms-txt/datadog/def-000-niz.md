# Source: https://docs.datadoghq.com/security/default_rules/def-000-niz.md

---
title: Verify Group Ownership on SSH Server Private *_key Key Files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Group Ownership on SSH Server
  Private *_key Key Files
---

# Verify Group Ownership on SSH Server Private *_key Key Files

## Description{% #description %}

SSH server private keys, files that match the `/etc/ssh/*_key` glob, must be group-owned by `ssh_keys` group.

## Rationale{% #rationale %}

If an unauthorized user obtains the private SSH host key file, the host could be impersonated.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; then

find /etc/ssh/ -maxdepth 1 -type f ! -group ssh_keys -regex '^.*_key$' -exec chgrp ssh_keys {} \;

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Find /etc/ssh/ file(s) matching ^.*_key$
  command: find -H /etc/ssh/ -maxdepth 1 -type f ! -group ssh_keys -regex "^.*_key$"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-86125-2
  - configure_strategy
  - file_groupownership_sshd_private_key
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/ssh/ file(s) matching ^.*_key$
  file:
    path: '{{ item }}'
    group: ssh_keys
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-86125-2
  - configure_strategy
  - file_groupownership_sshd_private_key
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
