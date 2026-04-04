# Source: https://docs.datadoghq.com/security/default_rules/def-000-wkz.md

---
title: Configure SELinux Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Configure SELinux Policy
---

# Configure SELinux Policy

## Description{% #description %}

The SELinux `targeted` policy is appropriate for general-purpose desktops and servers, as well as systems in many other roles. To configure the system to use this policy, add or correct the following line in `/etc/selinux/config`:

```
SELINUXTYPE=targeted

```

Other policies, such as `mls`, provide additional security labeling and greater confinement but are not compatible with many general-purpose use cases.

## Rationale{% #rationale %}

Setting the SELinux policy to `targeted` or a more specialized policy ensures the system will confine processes that are likely to be targeted for exploitation, such as network or system services.

Note: During the development or debugging of SELinux modules, it is common to temporarily place non-production systems in `permissive` mode. In such temporary cases, SELinux policies should be developed, and once work is completed, the system should be reconfigured to `targeted`.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; then

var_selinux_policy_name='targeted'


if [ -e "/etc/selinux/config" ] ; then

    LC_ALL=C sed -i "/^SELINUXTYPE=/Id" "/etc/selinux/config"
else
    touch "/etc/selinux/config"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/selinux/config"

cp "/etc/selinux/config" "/etc/selinux/config.bak"
# Insert at the end of the file
printf '%s\n' "SELINUXTYPE=$var_selinux_policy_name" >> "/etc/selinux/config"
# Clean up after ourselves.
rm "/etc/selinux/config.bak"

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: XCCDF Value var_selinux_policy_name # promote to variable
  set_fact:
    var_selinux_policy_name: !!str targeted
  tags:
    - always

- name: Configure SELinux Policy
  block:

  - name: Check for duplicate values
    lineinfile:
      path: /etc/selinux/config
      create: true
      regexp: ^SELINUXTYPE=
      state: absent
    check_mode: true
    changed_when: false
    register: dupes

  - name: Deduplicate values from /etc/selinux/config
    lineinfile:
      path: /etc/selinux/config
      create: true
      regexp: ^SELINUXTYPE=
      state: absent
    when: dupes.found is defined and dupes.found > 1

  - name: Insert correct line to /etc/selinux/config
    lineinfile:
      path: /etc/selinux/config
      create: true
      regexp: ^SELINUXTYPE=
      line: SELINUXTYPE={{ var_selinux_policy_name }}
      state: present
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-27279-9
  - DISA-STIG-RHEL-07-020220
  - NIST-800-171-3.1.2
  - NIST-800-171-3.7.2
  - NIST-800-53-AC-3
  - NIST-800-53-AC-3(3)(a)
  - NIST-800-53-AU-9
  - NIST-800-53-SC-7(21)
  - PCI-DSSv4-1.2.6
  - low_complexity
  - low_disruption
  - medium_severity
  - reboot_required
  - restrict_strategy
  - selinux_policytype
```
