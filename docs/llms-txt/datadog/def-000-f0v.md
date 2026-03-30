# Source: https://docs.datadoghq.com/security/default_rules/def-000-f0v.md

---
title: Ensure that /etc/at.allow exists
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure that /etc/at.allow exists
---

# Ensure that /etc/at.allow exists

## Description{% #description %}

The file `/etc/at.allow` should exist and should be used instead of `/etc/at.deny`.

## Rationale{% #rationale %}

Using the at.allow file to control who can run at jobs enforces this who can schedule jobs. It is easier to manage an allow list than a deny list.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

touch /etc/at.allow
    chown 0 /etc/at.allow
    chmod 0640 /etc/at.allow

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
  - disable_strategy
  - file_at_allow_exists
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Add empty /etc/at.allow
  file:
    path: /etc/at.allow
    state: touch
    owner: '0'
    mode: '0640'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - disable_strategy
  - file_at_allow_exists
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
