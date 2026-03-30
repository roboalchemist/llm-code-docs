# Source: https://docs.datadoghq.com/security/default_rules/def-000-6kx.md

---
title: Enable systemd_timesyncd Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Enable systemd_timesyncd Service
---

# Enable systemd_timesyncd Service

## Description{% #description %}

The `systemd_timesyncd` service can be enabled with the following command:

```
$ sudo systemctl enable systemd_timesyncd.service
```

## Rationale{% #rationale %}

Enabling the `systemd_timesyncd` service ensures that this host uses the ntp protocol to fetch time data from a ntp server. Synchronizing time is essential for authentication services such as Kerberos, but it is also important for maintaining accurate logs and auditing possible security breaches.

Additional information on Ubuntu network time protocol is available at [https://help.ubuntu.com/lts/serverguide/NTP.html.en](https://help.ubuntu.com/lts/serverguide/NTP.html.en).

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' && { ( ! ( dpkg-query --show --showformat='${db:Status-Status}' 'chrony' 2>/dev/null | grep -q '^installed$' ) && ! ( dpkg-query --show --showformat='${db:Status-Status}' 'ntp' 2>/dev/null | grep -q '^installed$' ) ); }; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
"$SYSTEMCTL_EXEC" unmask 'systemd-timesyncd.service'
if [[ $("$SYSTEMCTL_EXEC" is-system-running) != "offline" ]]; then
  "$SYSTEMCTL_EXEC" start 'systemd-timesyncd.service'
fi
"$SYSTEMCTL_EXEC" enable 'systemd-timesyncd.service'

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
  - NIST-800-53-AU-8(1)(a)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.4
  - PCI-DSSv4-10.6
  - PCI-DSSv4-10.6.1
  - enable_strategy
  - high_severity
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_timesyncd_enabled

- name: Enable systemd_timesyncd Service - Enable service systemd-timesyncd
  block:

  - name: Gather the package facts
    package_facts:
      manager: auto

  - name: Enable systemd_timesyncd Service - Enable Service systemd-timesyncd
    ansible.builtin.systemd:
      name: systemd-timesyncd
      enabled: true
      state: started
      masked: false
    when:
    - '"systemd" in ansible_facts.packages'
  when:
  - '"linux-base" in ansible_facts.packages'
  - ( not ( "chrony" in ansible_facts.packages ) and not ( "ntp" in ansible_facts.packages
    ) )
  tags:
  - NIST-800-53-AU-8(1)(a)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.4
  - PCI-DSSv4-10.6
  - PCI-DSSv4-10.6.1
  - enable_strategy
  - high_severity
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - service_timesyncd_enabled
```
