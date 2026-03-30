# Source: https://docs.datadoghq.com/security/default_rules/def-000-q1w.md

---
title: Enable systemd-journal-upload Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Enable systemd-journal-upload Service
---

# Enable systemd-journal-upload Service

## Description{% #description %}

Ubuntu 24.04 must offload rsyslog messages for networked systems in real time and offload standalone systems at least weekly. The `systemd-journal-upload` service can be enabled with the following command:

```gdscript3
$ sudo systemctl enable systemd-journal-upload.service
```

## Rationale{% #rationale %}

Ubuntu 24.04 must offload rsyslog messages for networked systems in real time and offload standalone systems at least weekly.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' && { ( [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ] && dpkg-query --show --showformat='${db:Status-Status}' 'systemd-journal-remote' 2>/dev/null | grep -q '^installed$' ); }; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
"$SYSTEMCTL_EXEC" unmask 'systemd-journal-upload.service'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" start 'systemd-journal-upload.service'
fi
"$SYSTEMCTL_EXEC" enable 'systemd-journal-upload.service'

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
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_systemd-journal-upload_enabled

- name: Enable systemd-journal-upload Service - Enable service systemd-journal-upload
  block:

  - name: Gather the package facts
    package_facts:
      manager: auto

  - name: Enable systemd-journal-upload Service - Enable Service systemd-journal-upload
    ansible.builtin.systemd:
      name: systemd-journal-upload
      enabled: true
      state: started
      masked: false
    when:
    - '"systemd-journal-remote" in ansible_facts.packages'
  when:
  - '"linux-base" in ansible_facts.packages'
  - ( ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
    and "systemd-journal-remote" in ansible_facts.packages )
  tags:
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_systemd-journal-upload_enabled
```
