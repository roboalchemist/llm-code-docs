# Source: https://docs.datadoghq.com/security/default_rules/def-000-ndd.md

---
title: Verify Group Ownership on SSH Server Public *.pub Key Files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Group Ownership on SSH Server
  Public *.pub Key Files
---

# Verify Group Ownership on SSH Server Public *.pub Key Files

## Description{% #description %}

SSH server public keys, files that match the `/etc/ssh/*.pub` glob, must be group-owned by `root` group.

## Rationale{% #rationale %}

If a public host key file is modified by an unauthorized user, the SSH service may be compromised.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; then

find /etc/ssh/ -maxdepth 1 -type f ! -group 0 -regex '^.*\.pub$' -exec chgrp 0 {} \;

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Find /etc/ssh/ file(s) matching ^.*\.pub$
  command: find -H /etc/ssh/ -maxdepth 1 -type f ! -group 0 -regex "^.*\.pub$"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-86132-8
  - configure_strategy
  - file_groupownership_sshd_pub_key
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/ssh/ file(s) matching ^.*\.pub$
  file:
    path: '{{ item }}'
    group: '0'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-86132-8
  - configure_strategy
  - file_groupownership_sshd_pub_key
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
