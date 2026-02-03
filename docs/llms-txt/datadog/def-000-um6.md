# Source: https://docs.datadoghq.com/security/default_rules/def-000-um6.md

---
title: Verify firewalld Enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify firewalld Enabled
---

# Verify firewalld Enabled
 
## Description{% #description %}

The `firewalld` service can be enabled with the following command:

```
$ sudo systemctl enable firewalld.service
```

## Rationale{% #rationale %}

Access control methods provide the ability to enhance system security posture by restricting services and known good IP addresses and address ranges. This prevents connections from unknown hosts and protocols.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ] && { rpm --quiet -q firewalld; }; then

SYSTEMCTL_EXEC='/usr/bin/systemctl'
"$SYSTEMCTL_EXEC" unmask 'firewalld.service'
"$SYSTEMCTL_EXEC" start 'firewalld.service'
"$SYSTEMCTL_EXEC" enable 'firewalld.service'

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
  - CCE-80998-8
  - DISA-STIG-RHEL-07-040520
  - NIST-800-171-3.1.3
  - NIST-800-171-3.4.7
  - NIST-800-53-AC-4
  - NIST-800-53-CA-3(5)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-7(21)
  - PCI-DSSv4-1.2.1
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_firewalld_enabled

- name: Enable service firewalld
  block:

  - name: Gather the package facts
    package_facts:
      manager: auto

  - name: Enable service firewalld
    systemd:
      name: firewalld
      enabled: 'yes'
      state: started
      masked: 'no'
    when:
    - '"firewalld" in ansible_facts.packages'
  when:
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  - '"firewalld" in ansible_facts.packages'
  tags:
  - CCE-80998-8
  - DISA-STIG-RHEL-07-040520
  - NIST-800-171-3.1.3
  - NIST-800-171-3.4.7
  - NIST-800-53-AC-4
  - NIST-800-53-CA-3(5)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-SC-7(21)
  - PCI-DSSv4-1.2.1
  - enable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - service_firewalld_enabled
```
