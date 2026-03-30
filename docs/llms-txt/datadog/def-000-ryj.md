# Source: https://docs.datadoghq.com/security/default_rules/def-000-ryj.md

---
title: Ensure SELinux is Not Disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure SELinux is Not Disabled
---

# Ensure SELinux is Not Disabled

## Description{% #description %}

The SELinux state should be set to `enforcing` or `permissive` at system boot time. In the file `/etc/selinux/config`, add or correct the following line to configure the system to boot into enforcing or permissive mode:

```
SELINUX=enforcing
```

OR

```
SELINUX=permissive
```

## Rationale{% #rationale %}

Running SELinux in disabled mode is strongly discouraged. It prevents enforcing the SELinux controls without a system reboot. It also avoids labeling any persistent objects such as files, making it difficult to enable SELinux in the future.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; then

if [ -e "/etc/selinux/config" ] ; then

    LC_ALL=C sed -i "/^SELINUX=/Id" "/etc/selinux/config"
else
    touch "/etc/selinux/config"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/selinux/config"

cp "/etc/selinux/config" "/etc/selinux/config.bak"
# Insert at the end of the file
printf '%s\n' "SELINUX=permissive" >> "/etc/selinux/config"
# Clean up after ourselves.
rm "/etc/selinux/config.bak"

fixfiles onboot
fixfiles -f relabel

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Ensure SELinux is Not Disabled
  block:

  - name: Check for duplicate values
    lineinfile:
      path: /etc/selinux/config
      create: true
      regexp: ^SELINUX=
      state: absent
    check_mode: true
    changed_when: false
    register: dupes

  - name: Deduplicate values from /etc/selinux/config
    lineinfile:
      path: /etc/selinux/config
      create: true
      regexp: ^SELINUX=
      state: absent
    when: dupes.found is defined and dupes.found > 1

  - name: Insert correct line to /etc/selinux/config
    lineinfile:
      path: /etc/selinux/config
      create: true
      regexp: ^SELINUX=
      line: SELINUX=permissive
      state: present
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-87213-5
  - high_severity
  - low_complexity
  - low_disruption
  - reboot_required
  - restrict_strategy
  - selinux_not_disabled
```

## Warning{% #warning %}

In case the SELinux is "disabled", the automated remediation will adopt a more conservative approach and set it to "permissive" in order to avoid any system disruption and give the administrator the opportunity to assess the impact and necessary efforts before setting it to "enforcing", which is strongly recommended.
