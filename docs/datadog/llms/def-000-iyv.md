# Source: https://docs.datadoghq.com/security/default_rules/def-000-iyv.md

---
title: Package "prelink" Must not be Installed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Package "prelink" Must not be Installed
---

# Package "prelink" Must not be Installed

## Description{% #description %}

The `prelink` package can be removed with the following command:

```

 $ apt-get remove prelink
```

## Rationale{% #rationale %}

The use of the `prelink` package can interfere with the operation of AIDE since it binaries. Prelinking can also increase damage caused by vulnerability in a common library like libc.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if [[ -f /usr/sbin/prelink ]];
then
prelink -ua
fi

DEBIAN_FRONTEND=noninteractive apt-get remove -y "prelink"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Check If Prelinked Is Installed
  ansible.builtin.stat:
    path: /usr/sbin/prelink
    get_checksum: false
  register: prelink
  tags:
  - disable_strategy
  - low_disruption
  - medium_complexity
  - medium_severity
  - no_reboot_needed
  - package_prelink_removed

- name: Restore Prelinked Binaries
  ansible.builtin.command:
    cmd: prelink -ua
  when: prelink.stat.exists
  tags:
  - disable_strategy
  - low_disruption
  - medium_complexity
  - medium_severity
  - no_reboot_needed
  - package_prelink_removed

- name: Ensure prelink is Removed
  ansible.builtin.package:
    name: prelink
    state: absent
  tags:
  - disable_strategy
  - low_disruption
  - medium_complexity
  - medium_severity
  - no_reboot_needed
  - package_prelink_removed
```
