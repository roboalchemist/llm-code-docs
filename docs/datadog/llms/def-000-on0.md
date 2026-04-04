# Source: https://docs.datadoghq.com/security/default_rules/def-000-on0.md

---
title: Ensure that /etc/cron.allow exists
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure that /etc/cron.allow exists
---

# Ensure that /etc/cron.allow exists

## Description{% #description %}

The file `/etc/cron.allow` should exist and should be used instead of `/etc/cron.deny`.

## Rationale{% #rationale %}

Access to `crontab` should be restricted. It is easier to manage an allow list than a deny list. Therefore, `/etc/cron.allow` needs to be created and used instead of `/etc/cron.deny`. Regardless of the existence of any of these files, the root administrative user is always allowed to setup a crontab.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

touch /etc/cron.allow
    chown 0 /etc/cron.allow
    chmod 0600 /etc/cron.allow

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
  - file_cron_allow_exists
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Add empty /etc/cron.allow
  file:
    path: /etc/cron.allow
    state: touch
    owner: '0'
    mode: '0600'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - disable_strategy
  - file_cron_allow_exists
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
