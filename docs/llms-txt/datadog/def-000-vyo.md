# Source: https://docs.datadoghq.com/security/default_rules/def-000-vyo.md

---
title: Ensure Remote Login Warning Banner Is Configured Properly
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure Remote Login Warning Banner Is
  Configured Properly
---

# Ensure Remote Login Warning Banner Is Configured Properly

## Description{% #description %}

To configure the system remote login warning banner edit the `/etc/issue.net` file. The contents of this file is displayed to users prior to login from remote connections. Replace the default text with a message compliant with the local site policy. The message should not contain information about operating system version, release, kernel version or patch level. The recommended banner text can be tailored in the XCCDF Value `xccdf_org.ssgproject.content_value_cis_banner_text`:

```
Authorized users only. All activity may be monitored and reported.
```

## Rationale{% #rationale %}

Warning messages inform users who are attempting to login to the system of their legal status regarding the system and must include the name of the organization that owns the system and any monitoring policies that are in place. Displaying OS and patch level information in login banners also has the side effect of providing detailed system information to attackers attempting to target specific exploits of a system. Authorized users can easily get this information by running the `uname -a` command once they have logged in.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

cis_banner_text='Authorized users only. All activity may be monitored and reported.'

echo "$cis_banner_text" > "/etc/issue.net"

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - banner_etc_issue_net_cis
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
- name: XCCDF Value cis_banner_text # promote to variable
  set_fact:
    cis_banner_text: !!str Authorized users only. All activity may be monitored and reported.
  tags:
    - always

- name: Ensure Remote Login Warning Banner Is Configured Properly - Copy using inline
    content
  ansible.builtin.copy:
    content: '{{ cis_banner_text }}'
    dest: /etc/issue.net
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - banner_etc_issue_net_cis
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
