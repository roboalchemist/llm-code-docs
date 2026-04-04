# Source: https://docs.datadoghq.com/security/default_rules/def-000-ybk.md

---
title: Ensure SELinux Not Disabled in /etc/default/grub
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure SELinux Not Disabled in
  /etc/default/grub
---

# Ensure SELinux Not Disabled in /etc/default/grub

## Description{% #description %}

SELinux can be disabled at boot time by an argument in `/etc/default/grub`. Remove any instances of `selinux=0` from the kernel arguments in that file to prevent SELinux from being disabled at boot.

## Rationale{% #rationale %}

Disabling a major host protection feature, such as SELinux, at boot time prevents it from confining system services at boot time. Further, it increases the chances that it will remain off during system operation.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ] && { rpm --quiet -q grub2-common; }; then

sed -i --follow-symlinks "s/selinux=0//gI" /etc/default/grub /etc/grub2.cfg /etc/grub.d/*
sed -i --follow-symlinks "s/enforcing=0//gI" /etc/default/grub /etc/grub2.cfg /etc/grub.d/*

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```go
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - CCE-26961-3
  - NIST-800-171-3.1.2
  - NIST-800-171-3.7.2
  - NIST-800-53-AC-3
  - NIST-800-53-AC-3(3)(a)
  - PCI-DSSv4-1.2.6
  - grub2_enable_selinux
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure SELinux Not Disabled in /etc/default/grub - Find /etc/grub.d/ files
  ansible.builtin.find:
    paths:
    - /etc/grub.d/
    follow: true
  register: result_grub_d
  when:
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  - '"grub2-common" in ansible_facts.packages'
  tags:
  - CCE-26961-3
  - NIST-800-171-3.1.2
  - NIST-800-171-3.7.2
  - NIST-800-53-AC-3
  - NIST-800-53-AC-3(3)(a)
  - PCI-DSSv4-1.2.6
  - grub2_enable_selinux
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure SELinux Not Disabled in /etc/default/grub - Ensure SELinux Not Disabled
    in /etc/grub.d/ files
  ansible.builtin.replace:
    dest: '{{ item.path }}'
    regexp: (selinux|enforcing)=0
  with_items:
  - '{{ result_grub_d.files }}'
  when:
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  - '"grub2-common" in ansible_facts.packages'
  tags:
  - CCE-26961-3
  - NIST-800-171-3.1.2
  - NIST-800-171-3.7.2
  - NIST-800-53-AC-3
  - NIST-800-53-AC-3(3)(a)
  - PCI-DSSv4-1.2.6
  - grub2_enable_selinux
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure SELinux Not Disabled in /etc/default/grub - Check if /etc/grub2.cfg
    exists
  ansible.builtin.stat:
    path: /etc/grub2.cfg
  register: result_grub2_cfg_present
  when:
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  - '"grub2-common" in ansible_facts.packages'
  tags:
  - CCE-26961-3
  - NIST-800-171-3.1.2
  - NIST-800-171-3.7.2
  - NIST-800-53-AC-3
  - NIST-800-53-AC-3(3)(a)
  - PCI-DSSv4-1.2.6
  - grub2_enable_selinux
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure SELinux Not Disabled in /etc/default/grub - Check if /etc/default/grub
    exists
  ansible.builtin.stat:
    path: /etc/default/grub
  register: result_default_grub_present
  when:
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  - '"grub2-common" in ansible_facts.packages'
  tags:
  - CCE-26961-3
  - NIST-800-171-3.1.2
  - NIST-800-171-3.7.2
  - NIST-800-53-AC-3
  - NIST-800-53-AC-3(3)(a)
  - PCI-DSSv4-1.2.6
  - grub2_enable_selinux
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure SELinux Not Disabled in /etc/default/grub - Ensure SELinux Not Disabled
    in /etc/grub2.cfg
  ansible.builtin.replace:
    dest: /etc/grub2.cfg
    regexp: (selinux|enforcing)=0
  when:
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  - '"grub2-common" in ansible_facts.packages'
  - result_grub2_cfg_present.stat.exists
  tags:
  - CCE-26961-3
  - NIST-800-171-3.1.2
  - NIST-800-171-3.7.2
  - NIST-800-53-AC-3
  - NIST-800-53-AC-3(3)(a)
  - PCI-DSSv4-1.2.6
  - grub2_enable_selinux
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure SELinux Not Disabled in /etc/default/grub - Ensure SELinux Not Disabled
    in /etc/default/grub
  ansible.builtin.replace:
    dest: /etc/default/grub
    regexp: (selinux|enforcing)=0
  when:
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  - '"grub2-common" in ansible_facts.packages'
  - result_default_grub_present.stat.exists
  tags:
  - CCE-26961-3
  - NIST-800-171-3.1.2
  - NIST-800-171-3.7.2
  - NIST-800-53-AC-3
  - NIST-800-53-AC-3(3)(a)
  - PCI-DSSv4-1.2.6
  - grub2_enable_selinux
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
