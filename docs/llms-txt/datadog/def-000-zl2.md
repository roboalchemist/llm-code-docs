# Source: https://docs.datadoghq.com/security/default_rules/def-000-zl2.md

---
title: Disable storing core dump
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable storing core dump
---

# Disable storing core dump
 
## Description{% #description %}

The `Storage` option in `[Coredump]` sectionof `/etc/systemd/coredump.conf` can be set to `none` to disable storing core dumps permanently.

## Rationale{% #rationale %}

A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers or system operators trying to debug problems. Enabling core dumps on production systems is not recommended, however there may be overriding operational requirements to enable advanced debuging. Permitting temporary enablement of core dumps during such situations should be reviewed through local needs and policy.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if rpm --quiet -q systemd; then

if [ -e "/etc/systemd/coredump.conf" ] ; then
    
    LC_ALL=C sed -i "/^\s*Storage\s*=\s*/Id" "/etc/systemd/coredump.conf"
else
    touch "/etc/systemd/coredump.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/systemd/coredump.conf"

cp "/etc/systemd/coredump.conf" "/etc/systemd/coredump.conf.bak"
# Insert at the end of the file
printf '%s\n' "Storage=none" >> "/etc/systemd/coredump.conf"
# Clean up after ourselves.
rm "/etc/systemd/coredump.conf.bak"

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
  - CCE-83428-3
  - NIST-800-53-CM-6
  - PCI-DSS-Req-3.2
  - PCI-DSSv4-3.3.1.1
  - coredump_disable_storage
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Disable storing core dump
  block:

  - name: Check for duplicate values
    lineinfile:
      path: /etc/systemd/coredump.conf
      create: false
      regexp: ^\s*Storage\s*=\s*
      state: absent
    check_mode: true
    changed_when: false
    register: dupes

  - name: Deduplicate values from /etc/systemd/coredump.conf
    lineinfile:
      path: /etc/systemd/coredump.conf
      create: false
      regexp: ^\s*Storage\s*=\s*
      state: absent
    when: dupes.found is defined and dupes.found > 1

  - name: Insert correct line to /etc/systemd/coredump.conf
    lineinfile:
      path: /etc/systemd/coredump.conf
      create: false
      regexp: ^\s*Storage\s*=\s*
      line: Storage=none
      state: present
  when: '"systemd" in ansible_facts.packages'
  tags:
  - CCE-83428-3
  - NIST-800-53-CM-6
  - PCI-DSS-Req-3.2
  - PCI-DSSv4-3.3.1.1
  - coredump_disable_storage
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```

## Warning{% #warning %}

If the `/etc/systemd/coredump.conf` file does not already contain the `[Coredump]` section, the value will not be configured correctly.
