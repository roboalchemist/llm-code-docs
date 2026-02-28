# Source: https://docs.datadoghq.com/security/default_rules/def-000-8gm.md

---
title: Verify nftables Service is Enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify nftables Service is Enabled
---

# Verify nftables Service is Enabled

## Description{% #description %}

The nftables service allows for the loading of nftables rulesets during boot, or starting on the nftables service The `nftables` service can be enabled with the following command:

```
$ sudo systemctl enable nftables.service
```

## Rationale{% #rationale %}

The nftables service restores the nftables rules from the rules files referenced in the `/etc/sysconfig/nftables.conf` file during boot or the starting of the nftables service

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ( dpkg-query --show --showformat='${db:Status-Status}' 'nftables' 2>/dev/null | grep -q '^installed$' && ! (systemctl is-active firewalld &>/dev/null) && dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' ); then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
"$SYSTEMCTL_EXEC" unmask 'nftables.service'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" start 'nftables.service'
fi
"$SYSTEMCTL_EXEC" enable 'nftables.service'

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
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_nftables_enabled

- name: Verify nftables Service is Enabled - Enable service nftables
  block:

  - name: Gather the package facts
    package_facts:
      manager: auto

  - name: Verify nftables Service is Enabled - Enable Service nftables
    ansible.builtin.systemd:
      name: nftables
      enabled: true
      state: started
      masked: false
    when:
    - '"nftables" in ansible_facts.packages'
  when: ( "nftables" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  tags:
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_nftables_enabled
```
