# Source: https://docs.datadoghq.com/security/default_rules/def-000-7ib.md

---
title: Verify Group Who Owns cron.weekly
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Group Who Owns cron.weekly
---

# Verify Group Who Owns cron.weekly
 
## Description{% #description %}

To properly set the group owner of `/etc/cron.weekly`, run the command:

```
$ sudo chgrp root /etc/cron.weekly
```

## Rationale{% #rationale %}

Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations. Therefore, service configuration files should be owned by the correct group to prevent unauthorized changes.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if getent group "0" >/dev/null 2>&1; then
  newgroup="0"
fi
if [[ -z ${newgroup} ]]; then
  echo "0 is not a defined group on the system"
  exit 1
fi
find -H /etc/cron.weekly/ -maxdepth 1 -type d  ! -group 0 -exec chgrp -L $newgroup {} \;

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
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_cron_weekly
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupowner_cron_weekly_newgroup variable if represented by gid
  set_fact:
    file_groupowner_cron_weekly_newgroup: '0'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_cron_weekly
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/cron.weekly/
  file:
    path: /etc/cron.weekly/
    state: directory
    group: '{{ file_groupowner_cron_weekly_newgroup }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_cron_weekly
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
